# Weekly AI Agent Paper Report

**Generated:** 2026-10-26 16:12
**Period:** 2026-10-19 to 2026-10-25

## Summary

- **Total papers fetched:** 831
- **Papers matching keywords:** 170
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-10-19) | Change |
|--------|-----------|-----------|--------|
| Total matched | 170 | 170 | +0 |
| arxiv | 168 | 164 | +4 |
| biorxiv | 2 | 3 | -1 |
| medrxiv | 0 | 3 | -3 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (2 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. An immune world model with multi-agent orchestration for peptide vaccines

- **Authors:** Chen, L., Luan, H., Yu, G.
- **Published:** 2026-10-21
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.19.760096](https://doi.org/10.64898/2026.10.19.760096)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Peptide-vaccine design requires a connection between vaccine-induced priming and recognition of the antigen naturally displayed by a tumor. We present an immune world model that preserves this connection through separate vaccine and tumor branches, endpoint-specific evidence and multi-agent orchestration. Native-recognition constraints held an altered peptide despite its higher presentation score, and targeted perturbations removed antigen-dependent benefit when required tumor-recognition conditions were absent. Public dendritic-cell data distinguished donor from antigen-source transfer: a context ranker achieved Recall@20 of 0.483 and 0.333 under the respective holdouts. Structure-informed receptor prediction added candidate-ranking evidence while preserving functional constraints and matched scenario trajectories. An assay observation model further concentrated a cross-presentation coefficient around its known value in a synthetic conditioning experiment. Together, these results establish a computational framework for linking molecular predictions, native-target requirements and conditional immune dynamics. The framework provides a reproducible basis for choosing peptide-vaccine candidates and the experiments needed to resolve their biological dependencies.

</details>


### 2. GENOAR: Global Engine for Navigating the Omnicell space via Agent-based Research

- **Authors:** Paik, H.
- **Published:** 2026-10-21
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.15.759380](https://doi.org/10.64898/2026.10.15.759380)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Although generative models have revolutionized many fields, including genomics, building a scalable dataset compatible with artificial intelligence (AI) is essential yet underexplored. Here, we developed a Global Engine for navigating the Omnicell space via Agent-based Research (GENOAR) that covers approximately 54 million cells for diverse downstream tasks using AI agents and parallel computing. GENOAR outperforms in three parts. Parallel computations accelerated the preprocessing of single-cell transcriptomic data; the other components enabled agent-assisted data storage and exploration for both AI models and humans. GENOAR involves two AI agents: an AI nomenclaturist ordered the unstructured labels of the single-cell transcriptomic profiles, and an AI librarian retrieved data. GENOAR presents transcriptomic profiles from more than 54 million cells from humans and mice in an analysis-ready format for humans and AI agents. AI agents in GENOAR exhibited successful retrieval performance compared with human experts. Using GENOAR, we elucidated progenitor cell-associated transcriptional signatures in native retinoblastoma and organoid environments. GENOAR was released and validated for the on-demand construction of single-cell atlases for metazoa. In conclusion, using GENOAR, the development of a single-cell transcriptomic atlas compatible with both AI systems and human researchers is feasible, scalable, and reproducible.

</details>


---



## Arxiv (168 papers)


### 1. J-Comm: Jacobian-Guided Latent Communication between LLM Agents

- **Authors:** Xiangwei Wang, Wei Wang, Sachith Seneviratne, Ken Chen, Yu Xia, Peng Wang, Saman Halgamuge
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32871v1](http://arxiv.org/abs/2610.32871v1)
- **PDF:** [https://arxiv.org/pdf/2610.32871v1](https://arxiv.org/pdf/2610.32871v1)
- **Categories:** cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Latent communication requires both an effective continuous reasoning process and an interface through which an external model can leverage its intermediate computation. We present J-Comm, a framework comprising two core components. First, a training-free Geometric Agreement for Latent Reasoning (GEAR) reweights token candidates over existing model embeddings, which monotonically optimizes geometric consensus among candidate tokens in embedding space at each step. Second, we introduce an H+J (Hidden-and-Jacobian) communication interface that gives the Receiver two complementary views of the Sender's reasoning. The H channel supplies continuous inputs derived from feedback distributions, while the J channel conveys intermediate-state cues in vocabulary-indexed Jacobian-lens coordinates. Intuitively, H provides inputs for the Receiver to reason from, while J offers additional guidance within its computation. The Receiver reconstructs these cues using its own dictionary and injects them into intermediate layers during prefill, enabling communication without sharing key-value caches or requiring identical model widths. In Qwen3-8B to Qwen3-4B communication, J-Comm achieves the highest mean score across seven benchmarks, including 94.80% on MATH500, 54.55% on GPQA-Diamond, 73.33% on AIME2024+2025, and 62.93% success on ALFWorld. Compared with TextMAS, it improves performance by 1.29-8.59 percentage points and reduces generated text tokens by 19.2-74.8%.

</details>


### 2. Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves

- **Authors:** Garima Agrawal, Prasun Das, Akshay Sarvade, Priyanka L, Minisha N, Sravani Joshna, Hemath Manivannan, Lavanya Korada, Sambhrit Pattanayak, Srashti Gupta, Siddu R, Prasad Kalyanasundaram
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32851v1](http://arxiv.org/abs/2610.32851v1)
- **PDF:** [https://arxiv.org/pdf/2610.32851v1](https://arxiv.org/pdf/2610.32851v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprises are deploying agentic AI across the software development lifecycle, and they need the behavioral logic of the systems they act on, not stakeholder documentation. A seven-agent reverse-engineering pipeline recovered this logic, processing 241 repositories across 18 services into thousands of artifacts describing scope, journeys, rules and acceptance criteria. Recovery does not confer usability. Entities like offer, eligibility, and activation recur across services under a shared vocabulary, related in name but operationally distinct, so one end-to-end journey implicates over a thousand near-identical rules that must not be conflated. Flat vector retrieval fails, returning an identical rule from the wrong service at high similarity with no signal of error. Content-level ontology, the traditional remedy, did not exist, and relating every occurrence of recurring entities would have cost more than the engagement and not survived a release cycle. We place the ontology at the artifact level. In this machine-generated corpus, each artifact retains its producer, component, service, domain and type, provenance that disambiguates before content is read. We present a knowledge layer that organizes before retrieving: a self-describing catalog, a sparse metadata registry, and a navigation hypergraph defined over artifacts rather than extracted entities. Queries resolve to artifact identifiers that constrain vector search, so the competing rule from another service is absent rather than outranked, making disambiguation structural, not statistical. Built in under a week and admitting new services by convention, the layer serves SDLC agents, developers, quality engineers and analysts. It supported root-cause analysis and resolution of 100+ production defects with developer verification and attributed 35 release regression failures to specific rules and services.

</details>


### 3. Semantic Representation for Agentic Self-Play in Automated Laboratories

- **Authors:** Yves Delley, John Coller, Zachary Cutts, Alexander Daryin, Mathias Bellaiche, Jun W. Kim, Oscar Donosa, Srinidhi B. Seshadri, Tanner Clary, Sandy Klemm, Avinatan Hassidim, Yossi Matias, Pooja Rao, Petar Sirkovic, Annalisa Pawlosky
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32755v1](http://arxiv.org/abs/2610.32755v1)
- **PDF:** [https://arxiv.org/pdf/2610.32755v1](https://arxiv.org/pdf/2610.32755v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Navigating complex, high-dimensional biological search spaces necessitates scalable physical and computational intelligence to explore beyond local optima through iterative self-play across ideation, experimentation, and automation. Translating experimental designs into reliable physical execution remains bottlenecked by static laboratory automation and unmodeled physical variability. To address this, we introduce VERified Infrastructure for Discovery Laboratories, or VERID, a foundational infrastructure designed to bridge the gap between the high-level reasoning of artificial intelligence (AI) agents and complex, error-prone physical realities of wet labs. VERID is a persistent, high-fidelity semantic digital twin of the laboratory workcell that provides four core services: queryable introspection for agentic reasoning, time-compressed simulation for protocol validation, comprehensive trace persistence for a complete scientific record, and a framework for safe execution.
  We present three case studies using aqueous dye and deionized water mixtures to validate the optical and fluidic foundations of VERID. These studies demonstrate how VERID enables pre-emptive detection of critical errors in experimental protocols, stateful mid-run error recovery and post-hoc identification of subtle physical failures. The simulation functions as a discrete accounting engine, allowing agents to safely and inexpensively explore experimental designs in silico and refine experimental strategies through iterative self-play. VERID also captures structured multimodal experimental data for downstream analysis, knowledge mining and agent training. We argue that this semantic layer is an essential prerequisite for deploying autonomous agents in the biochemical and biomedical sciences, ensuring data integrity, operational safety, and paving the way for tackling previously intractable grand challenges in biology.

</details>


### 4. ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents

- **Authors:** Navyansh Mahla, Sashank Vandrangi
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32752v1](http://arxiv.org/abs/2610.32752v1)
- **PDF:** [https://arxiv.org/pdf/2610.32752v1](https://arxiv.org/pdf/2610.32752v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents need long-term memory that can recover precise and mutually consistent evidence from growing interaction histories, particularly when answers depend on relations among facts rather than isolated semantic matches. Current memory pipelines remain vulnerable at two stages: indexing errors can fragment repeated entities or merge distinct ones, and online retrieval often treats initial similarity scores as final even when the surrounding graph provides evidence for revising them. We introduce ActionRAG, a graph memory architecture that couples cautious indexing with query-time graph retroevaluation. Its indexing pipeline reconciles type labels and applies tiered entity resolution. Given a query, dual-channel entity and triple retrieval forms an initial evidence set and induces a bounded local graph. Query-conditioned receiver-normalized diffusion refines triple scores using local path structure. Seed protection, hub-penalized flux, and triple materialization preserve direct evidence while recovering missed connections. We evaluate ActionRAG on MemoryAgentBench (MAB), which tests accurate retrieval, conflict resolution, long-range understanding, and test-time learning. Across its eight deterministic-scoring columns, ActionRAG achieves 55.1 average accuracy, improving over the strongest retrieval-based memory baseline by 5.4 points. Under MAB's query-time cost accounting, mean synthesis cost stays below \$0.001 per query on the four reported cost columns, and the sum of separately measured retrieval-side p99 components is 440.7 ms on our consumer Apple Silicon setup.

</details>


### 5. Agentic Hazard Mapper: Emulating Expert Map-Making with AI Agents for Risk Communication

- **Authors:** Sidi Wu, Lifeng Lin, Yizi Chen, Anna Yokokubo, Lorenz Hurni
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32738v1](http://arxiv.org/abs/2610.32738v1)
- **PDF:** [https://arxiv.org/pdf/2610.32738v1](https://arxiv.org/pdf/2610.32738v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Hazard maps are essential tools for public risk communication, preparedness, and evacuation planning, yet effective cartographic design is not always ensured due to limited access to cartographic expertise across local governments and communities. We present Agentic Hazard Mapper, a multi-agent system that automates hazard-map production by emulating professional cartographic workflows and iterative design trade-offs while adapting design decisions to different data, locations, and hazard contexts. We conducted a formative study with map experts to inform the system design, followed by a user study and interviews with map experts and hazard practitioners. The generated maps improved participants' spatial understanding and evacuation-planning performance, reduced perceived workload and task completion time, and were generally preferred over corresponding municipal maps. We further discuss human oversight, adaptation across users and communication contexts, and opportunities to extend agentic support across broader stages of hazard-map production and risk communication.

</details>


### 6. The Butterfly Defects: Tracing Cooperation in LLM Agent Networks

- **Authors:** Maria Sampani, Maria Lymperaiou, Angeliki Dimitriou, Giorgos Filandrianos, Chrysoula Zerva, Giorgos Stamou
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32726v1](http://arxiv.org/abs/2610.32726v1)
- **PDF:** [https://arxiv.org/pdf/2610.32726v1](https://arxiv.org/pdf/2610.32726v1)
- **Categories:** physics.soc-ph, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language models (LLMs) increasingly operate as interconnected agents, a fundamental question emerges: does individual cooperation translate into collective cooperation? We investigate this question through the Iterated Prisoner's Dilemma (IPD), moving from dyadic interactions to homogeneous and heterogeneous networks of open-weight LLMs. Our findings reveal that cooperation is highly sensitive to model composition and seemingly minor linguistic changes. Models that cooperate with identical peers can shift toward defection in mixed populations. A simple uncertainty cue can increase or decrease cooperation, redistribute costs, and affect unexposed agents several hops away. Even reversing action-label order can dramatically alter behavior, with uncertainty framing sometimes amplifying this sensitivity. Together, these findings challenge the notion of cooperation as a stable model-level property, revealing how strategic behavior depends on interaction partners, network positions, and the language used to frame decisions.

</details>


### 7. Can AI Agents Help Robotic Engineers? Lessons from Two Focus Days in Industry

- **Authors:** Salim Fares, Steffen Herbold
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32636v1](http://arxiv.org/abs/2610.32636v1)
- **PDF:** [https://arxiv.org/pdf/2610.32636v1](https://arxiv.org/pdf/2610.32636v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Software developers increasingly use AI agents that execute multi-step programming tasks on their own. However, it is unclear if and how this transfers to robotic engineering, where engineers program industrial robots in niche, vendor-specific languages and rely on visual feedback from simulation tools. Within this paper, we report a case study on the use of AI agents by an SME that programs industrial robots. Our results show that the agent did not make the engineers more productive, with the exception of a task that required the generation of highly repetitive code. However, the results with the agent improved over time, as the engineers learned how to use it and the agent was adapted to the domain. Moreover, the experience with AI mattered more for the success with the agent than the experience with robotic engineering. This shows that AI agents are not a plug-and-play solution. Instead, companies must train their engineers on the usage of agents, plan time for a learning curve, and ensure that agent configurations match the domain and developer requirements. The strong learning curve we observed further implies that studies on productivity gains with AI should be longitudinal, as they otherwise miss how engineers adopt agents in practice.

</details>


### 8. What Transfers Across Protein Pockets? Experience Reuse in Molecular Optimization for Agentic Structure-Based Drug Design

- **Authors:** Zaifei Yang, Weiyu Chen, Yaqing Wang, James Kwok
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32620v1](http://arxiv.org/abs/2610.32620v1)
- **PDF:** [https://arxiv.org/pdf/2610.32620v1](https://arxiv.org/pdf/2610.32620v1)
- **Categories:** cs.AI, q-bio.BM


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents optimize a ligand in a protein pocket by editing it step by step and docking each edit. Recent agents first spend extra dockings probing the complex with controlled edits; guidance induced from these probes is reported to help more than the chemical knowledge the model already carries. The probes are then discarded with the instance that produced them, so the obvious next step is to keep them in an experience base, letting a new pocket inherit what earlier ones already paid for. Such a base is read through a \emph{key}: the record properties under which past edits are pooled and a new one is looked up. Using the full log of one such run over the CrossDocked2020 test-set pockets, we ask whether its keys recur on a pocket the base has never seen and still separate improving from worsening edits. \crchange{Using} the contacts at the site being edited, the action, and the round as \crchange{a} key, the base separates them sharply. Within our analysis, this separation is largely explained by how much the edit changed the molecule's size, the action, and the round, none of which describes the target. That is not because the target is irrelevant: naming it outright separates them several times more sharply. For a pocket absent from the base, transfer must rely on a description rather than its identity. Among the exact-match descriptions we evaluate, the more specific ones rarely recur, whereas the coarser ones provide little separation; the signals that do transfer primarily describe the edit and the molecule it produced rather than the target. Under the representations and lookup scheme studied here, an experience base may be more useful for prioritizing an agent's own proposals for docking than for directly prescribing what to build.

</details>


### 9. Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance

- **Authors:** Antonio Ken Iannillo, Joshua Segun Owotogbe, Roberto Natella, Francesco Avallone, Kristina Kudryavtseva, Indika Kumara
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32555v1](http://arxiv.org/abs/2610.32555v1)
- **PDF:** [https://arxiv.org/pdf/2610.32555v1](https://arxiv.org/pdf/2610.32555v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on external tools exposed via the Model Context Protocol (MCP), yet current benchmarks assume tools respond correctly and on time, leaving agent resilience to realistic tool failures untested. We introduce MCP-Injector, a drop-in, protocol-aware fault-injection middleware that interposes on the MCP tool-call path with controlled persistence (permanent, transient, intermittent) and seedable schedules. Its fault model is calibrated to the observed incident distribution (failure mode x persistence) of the public MCP ecosystem, mined from 57,240 issue and pull-request threads across 1,774 open-source MCP repositories. In a 1,350-cell experiment crossing two backbone sizes (20B, 120B), three agent stacks (custom multi-round plan-and-execute, OpenAI Agents SDK, LangChain), and three fault injection conditions, we find that faults drawn from this permanent-heavy stress profile cause severe quality degradation (task-completion score falls by 60%, from 8.08 to 3.23 out of 10), and that scale does not purchase fault tolerance for the two gpt-oss backbones we test: the 120B retains no larger share of its fault-free score under faults (resilience-ratio model, $p = 0.96$), and its completion rate under faults is, if anything, lower (91.1% vs. 95.6%; difference 4.4 points, 95% CI $[-0.2, 9.3]$). Agent stacks differ in how well they absorb faults, which suggests that framework-level error handling matters more than model scale. These results demonstrate that capability benchmarks alone can mask operational brittleness, motivating protocol-aware fault injection as a complementary evaluation dimension for tool-calling agents.

</details>


### 10. When Agents Fail: Model or Harness--Who's to Blame?

- **Authors:** Shao Zhang, Hangfan Zhang, Yuanyuan Shi, Hao Li, Min-Le Su, Kangcong Li, Jingping Wang, Chunjiang Mu, Chen Zhang, Yang Chen, Bo Zhang, Shuyue Hu
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32483v1](http://arxiv.org/abs/2610.32483v1)
- **PDF:** [https://arxiv.org/pdf/2610.32483v1](https://arxiv.org/pdf/2610.32483v1)
- **Categories:** cs.AI, cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents combine models with execution harnesses, so agentic benchmark performance reflects their joint behavior. We argue that harnesses should therefore be evaluated through their interactions with underlying models. We develop a framework combining five complementary measures: (i) Valid Completion Rate (VCR), how reliably agents finish normally and deliver evaluable results, irrespective of task correctness; (ii) Model-Harness Fit, how well a harness supports task achievement through valid completion for a given model; (iii) Cross-Model Fit, a harness's overall suitability across evaluated models; (iv) Interaction Residuals, pairing-specific execution strengths and weaknesses hidden by component-level summaries; and (v) Token Load, the token demands of agent execution, including failed attempts. We evaluate four general-purpose harnesses (OpenCode, Codex CLI, Pi CLI, and DeepAgents) with four core models, plus two fixed native model-harness systems, on six benchmarks covering context management, tool use, long-context planning, multimodal interaction, and artifact handoff. Including native references and stress conditions, 111 evaluation settings yield 52,168 trajectories. Harness rankings vary across models and benchmarks; task performance and valid completion can favor different pairings, and similar task scores can accompany distinct execution profiles. OpenCode ranks first in cross-model performance, while DeepSeek V4 Flash Preview maintains consistently high Mean VCR across harnesses on the shared four-benchmark panel. These findings support evaluating model-harness interactions, training transferable harness-use capabilities in models, and harness designs adapted to the model and task.

</details>


### 11. CauProphet: Teaching Agents to Develop Causal Cognition like Humans

- **Authors:** Kaiwen Wu, Chaochao Lu
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32477v1](http://arxiv.org/abs/2610.32477v1)
- **PDF:** [https://arxiv.org/pdf/2610.32477v1](https://arxiv.org/pdf/2610.32477v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly support long-horizon tasks by leveraging external memory and past experience. However, existing agents mainly retrieve records or summaries, lacking the ability to form and refine causal understanding of the world. Inspired by human causal cognition, we introduce CauProphet, an agent that develops and updates causal knowledge within its Causal Cognition. For each task, CauProphet combines relevant knowledge in Causal Cognition with current evidence to construct a Causal Belief, a structured belief capturing causal factors and the effects of possible actions. It uses this belief for decision-making and continuously updates both the belief and Causal Cognition as new observations emerge, enabling causal knowledge that persists beyond individual experiences. Evaluations demonstrate that CauProphet progressively acquires causal knowledge and transfers it to future decision-making. In financial research, CauProphet leverages prior discoveries to improve downstream analyses and outperforms all baselines in mean rank correlation with next-day returns, achieving a 25.4% improvement over a baseline agent. It also improves prediction accuracy from 21.3% to 28.6% in dynamic real-world settings. Further experiments validate its ability to perform reliable causal analysis and action selection across scientific and everyday tasks, demonstrating the potential of causal experience learning for next-generation LLM agents.

</details>


### 12. Beyond Copying: Lifelong Smart Contract Security Task Construction via Protocol Mutation

- **Authors:** Zifan Peng, Peng Huang, Jingyi Zheng, Yingjie Xue, Xuechao Wang, Xinlei He, Xia Hu, Dongrui Liu
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32453v1](http://arxiv.org/abs/2610.32453v1)
- **PDF:** [https://arxiv.org/pdf/2610.32453v1](https://arxiv.org/pdf/2610.32453v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can inspect code and run tests to support smart contract security. SlowMist reports about $38.6 billion in losses across the broader blockchain ecosystem. Existing evaluations can reward memorized or copied answers, including attack code recovered from public blockchain transactions. Reconstructing contracts and validating tasks also require costly manual effort. To address these issues, we propose CONSTRAINTDIAL, a framework for lifelong construction of smart contract security tasks via protocol mutation. It automates local contract reconstruction and uses attack execution to select changes to the required calls or inputs. Execution checks guide revisions that make the original attack fail while preserving exploitability, the security objective, and normal functionality. New incidents and audit findings enter the same procedure. With CONSTRAINTDIAL, we construct 3,045 task inputs from 203 public cases, covering detect, exploit, and patch. Compared with reconstruction alone, protocol mutation reduces success with supplied public answers by 10.9 percentage points on average across detect, exploit, and patch. The fraction of tasks solved by copying online answers falls by 9.3 points.

</details>


### 13. Decoupling Patient Personas and Clinical Workflows: A Dual-Agent Approach to Realistic Medical Dialogue Generation

- **Authors:** Qiyuan Li, Xiaomei Guo, Chao Gao, Haijiang Liu, Deyu Chen, Caicai Guo, Jinguang Gu
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32443v1](http://arxiv.org/abs/2610.32443v1)
- **PDF:** [https://arxiv.org/pdf/2610.32443v1](https://arxiv.org/pdf/2610.32443v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Pre-consultation medical dialogues are essential for collecting comprehensive patient information, but are costly to obtain at scale due to privacy and ethical constraints. Existing LLM-based synthesis methods often rely on prompt engineering or rigid rules, limiting their ability to balance clinical relevance with realistic patient diversity. We propose CoRPS-Dial, a controllable dual-agent framework for pre-consultation medical dialogue synthesis that integrates patient personas with guideline-aligned clinical workflow rules. CoRPS-Dial generates dialogues through interactions between a persona-driven patient agent and a process-guided doctor agent, followed by post-hoc quality control for role consistency, workflow completeness, and textual consistency. Experiments on coronary heart disease demonstrate that CoRPS-Dial improves alignment between synthetic and real dialogues in information coverage, clinical compliance, and dialogue naturalness. Downstream fine-tuning experiments further confirm the utility of the generated synthetic data for medical dialogue tasks. These results highlight the effectiveness of CoRPS-Dial for clinically grounded and controllable medical dialogue synthesis.

</details>


### 14. SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks

- **Authors:** Tianyun Zhong, Wei Wang, Jialin Li, Jianhong Tu, Liyao Li, Chuqiao Kuang, Tianshi Zheng, Songchi Zhou, Weiqi Zhai, Qile Jin, Jiajia Li, Jiasheng Zheng, Boxi Cao, Yaojie Lu, Hongyu Lin, Shiwei Ye, Bing Zhao, Hu Wei, Lin Qu, Xianpei Han
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32441v1](http://arxiv.org/abs/2610.32441v1)
- **PDF:** [https://arxiv.org/pdf/2610.32441v1](https://arxiv.org/pdf/2610.32441v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly capable of supporting scientific workflows, but their capabilities across diverse research activities remain difficult to assess systematically. Existing benchmarks often focus on selected scientific capabilities or task types, limiting a comprehensive characterization of scientific agents' strengths and weaknesses in realistic research workflows. We introduce SCI-AGENT-EXAM, a workflow-oriented benchmark comprising 120 expert-curated tasks across 11 scientific fields and 7 research task types defined by the Scientific Workflow Task Taxonomy (SWTT). Each task requires both executable artifacts (e.g., code and scripts) and textual artifacts (e.g., reports and explanations). To evaluate the heterogeneous task outputs, we develop a hybrid evaluation protocol combining deterministic programmatic verification for executable artifacts with a calibrated, expert-validated LLM-based judge for textual artifacts. Beyond outcome assessment, we analyze progress and solution stability along execution trajectories to characterize how agents reach their final results. Experiments with 10 frontier LLM agents reveal substantial performance gaps: GPT-6 Astra achieves the highest overall score of 80.9, yet only 26.0% of its runs exceed the 0.95 success threshold. Further analyses uncover distinct capability profiles across scientific task types and substantial variation in execution efficiency and stability. Our code and data are available at https://github.com/SKYLENAGE-AI/Sci-Agent-Exam.

</details>


### 15. Async-RBench: Benchmarking Asynchronous Task Execution in LLM Agents

- **Authors:** Detao Zeng, Guilin Ou, Nuo Chen, Yunhao Feng, Hongliang Wang, Qinli Yang, Junming Shao, Zhong Zhang
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32429v1](http://arxiv.org/abs/2610.32429v1)
- **PDF:** [https://arxiv.org/pdf/2610.32429v1](https://arxiv.org/pdf/2610.32429v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly execute tasks asynchronously: a main agent continues working while its subagents run, and the task state may change before their results arrive. The main agent must decide which work to update or preserve and which checks to repeat, while avoiding prohibited changes. Final task success alone does not reveal whether these results were handled correctly, and natural asynchronous arrivals are hard to reproduce. We introduce Async-RBench, a benchmark for asynchronous task execution in LLM agents, with 200 executable tasks covering eight scenarios. A scenario controller regulates result delivery using predefined task-state conditions, while an Event Response Contract (ERC) specifies what each response must change, preserve, avoid, and re-verify. The Dynamic Replanning Score (DRS) weights the response process and outcome equally and is reported separately from task success. We evaluate nine agents and find DRS scores of 19.2 to 45.1, with the lowest scores on duplicate reports and subagent failures. Under our execution protocol, all nine agents obtain lower task success with asynchronous than with batched delivery (26.0% vs. 29.7% on average). For three agents, prompting the main agent to rebuild its plan after every result improves DRS by only 2.6 to 3.5 points. Together, these findings highlight the challenges of reliable asynchronous task execution and the need to evaluate how agents handle incoming results alongside end-to-end task success.

</details>


### 16. Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge

- **Authors:** Xiaopeng Ke, Zhixin Wang, Xuebo Liu, Xinyu Ma, Xing Zheng, Bowen Song, Weiqiang Wang, Min Zhang
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32415v1](http://arxiv.org/abs/2610.32415v1)
- **PDF:** [https://arxiv.org/pdf/2610.32415v1](https://arxiv.org/pdf/2610.32415v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based annotation has advanced rapidly, yet existing benchmarks remain misaligned with real-world practice. Actual annotation often involves lengthy, task-specific guidelines, and different annotators may produce divergent but reasonable judgments, especially on boundary cases, where single-labeled dataset fail to reflect this disagreement. This gap also limits existing single-agent and workflow-based annotation systems, which often lack adaptability to complex, evolving guidelines. To bridge this gap, we introduce ANT-A Benchmark, a real-world multi-annotator benchmark spanning 7 datasets across domains and modalities, with task-specific guidelines and 5 independent human labels per instance. ANT-A enables a distribution-aware evaluation, using Fleiss kappa to assess how closely model annotations align with human labeling distributions. We further propose ANT-OR, a multi-agent annotation framework that refines prompts by distilling contrastive decision rules from positive and negative feedback. Experiments show that ANT-OR improves agreement@>=2 accuracy by 4.5 points over the strongest baseline and achieves the highest alignment with human annotator distributions as measured by Fleiss kappa within 2 points. Code and benchmark are available at https://github.com/Krueske/ANT-OR.

</details>


### 17. LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents

- **Authors:** Shen Liu, Ze Zhou, Zhenguo Xu, Shaopu Wang, Yike Gao, Chunlei Wang
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32412v1](http://arxiv.org/abs/2610.32412v1)
- **PDF:** [https://arxiv.org/pdf/2610.32412v1](https://arxiv.org/pdf/2610.32412v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recursive large language model (LLM) agents solve long-horizon tasks through decomposition, execution, and environmental feedback. Yet after producing an atomic subtask, they often invoke the same large model again to translate a familiar instruction into an executable action. We observe that high-level planning is task-specific, whereas leaf-level action grounding recurs across tasks and can be checked against environment-admitted actions. We introduce LeafSkill, an external reuse layer that retrieves semantically related grounding experience, binds action templates to current objects and admissible actions, and uses a lightweight 1.7B selector to choose a bound action or defer the unchanged subtask to the original agent. Skills remain outside the model parameters, allowing a frozen selector to use post-training additions. Under lexical and syntactic paraphrases, exact matching retrieves none of the reference actions, while semantic retrieval preserves 96.0% and 97.0% candidate coverage; the frozen selector adopts 97.34% of unseen skill types. On an independent confirmation set of 200 Robotouille tasks, LeafSkill completes 137 tasks versus 121 for ReCAP (68.5% vs. 60.5%, exact McNemar p=.0259). On the 106 tasks completed by both, it reduces Qwen3.5-27B tokens by 14.42% and calls by 14.08%. A separate held-out repeat yields a consistent 9.0-point success gain and 18.98% token reduction. Reusable leaf grounding can thus improve task completion while reducing host-model inference without replacing high-level planning.

</details>


### 18. PULSES: multi-agent AI for autonomous excited-state model building and dynamics

- **Authors:** Fangning Ren, Lechen Dong, Xu Chen, Weilin Zou, Bushra Alam, Fang Liu
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32392v1](http://arxiv.org/abs/2610.32392v1)
- **PDF:** [https://arxiv.org/pdf/2610.32392v1](https://arxiv.org/pdf/2610.32392v1)
- **Categories:** physics.chem-ph, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Simulating molecular excited-state processes requires resolving electronic and nuclear dynamics, but the cost of direct quantum-chemical calculations limits accessible system sizes and timescales. Machine-learning models can extend these simulations, yet they often need to be tailored to specific molecular systems and scientific objectives. Building and deploying such models requires coordinated decisions across conformational sampling, quantum-chemical labelling, model training, validation and dynamics. Here we introduce Paired agents for Unified Learning and Simulation of Excited States (PULSES), a multi-agent system that automates this workflow within expert-approved boundaries. A human expert and planner define the scientific objective, methods and decision boundaries, while an orchestrator coordinates domain agents and artifact-specific scientific assurance during execution. We evaluate PULSES on 15 computational chemistry tasks and demonstrate end-to-end applications to perylene exciton Hamiltonians, solvent-dependent biphenyl relaxation, and excited-state proton transfer in 10-hydroxybenzo[h]quinoline. These results demonstrate traceable, expert-bounded construction and deployment of specialized excited-state models, while retaining scientific validation as a requirement rather than assuming that successful execution establishes correctness.

</details>


### 19. Beyond Final Outcomes: Quantifying Claim-Level Information Dynamics in Multi-Agent LLM Interaction

- **Authors:** Haocheng Jiang, Herun Wan, Yongyuan Peng, Minnan Luo
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32333v1](http://arxiv.org/abs/2610.32333v1)
- **PDF:** [https://arxiv.org/pdf/2610.32333v1](https://arxiv.org/pdf/2610.32333v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

When LLM-powered agents interact, information is repeatedly shared, expanded, and forgotten, yet multi-agent evaluation typically focuses on final task outcomes. We study such interaction as claim-level information dynamics and propose RIVER, which decomposes agent outputs into atomic claims and evaluates three complementary dimensions: convergence, exploration, and retention. Convergence captures cross-agent claim correspondence and stance alignment; exploration captures semantic breadth and extension beyond the source; and retention tracks source preservation and the persistence of new claims across stages and lineages. We evaluate five interaction strategies on 40 controlled news-generation cases. Repeatedly pooled interaction promotes convergence but narrows the information space, whereas distributed relay yields broader, less shared information. Further comparisons show that method-specific constraints increase exploration while weakening convergence and retention. Our findings suggest that collective information dynamics are better explained by underlying information-flow mechanisms than by simple downstream performance.

</details>


### 20. TGR-EvoDAG: A DAG-based Multi-Agent Code Evolution Framework for Generative Recommendation on Tencent

- **Authors:** Junlin He, Junzhang Zhu, Yudong Li, Yihong Tang, Xuefeng Jiang, Wei Ma, Chengxiang Zhuo, Zang Li
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32326v1](http://arxiv.org/abs/2610.32326v1)
- **PDF:** [https://arxiv.org/pdf/2610.32326v1](https://arxiv.org/pdf/2610.32326v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents have enabled automated code evolution for algorithm discovery. However, current recursive self-improvement (RSI) research for sequential recommendation faces a dilemma: general-purpose frameworks lack domain-specific feedback, while recommender-specific frameworks rely on linear evolution. Crucially, naively integrating them fails when applied to Generative Recommendation (GR). Unlike end-to-end models, GR relies on a module-cascaded pipeline (tokenization, pre-training, and alignment). In this paradigm, existing evolution methods suffer from: i) cost blindness, squandering budgets by ignoring stage-asymmetric retraining overheads; and ii) short-sighted evaluation, discarding promising upstream innovations that temporarily regress metrics before downstream adaptation. To bridge these gaps, we propose TGR-EvoDAG, a multi-agent code evolution framework tailored for GR. TGR-EvoDAG models code evolution as a Directed Acyclic Graph (DAG) to maintain multiple evolution branches and merge complementary innovations, unifying advanced search with rich GR diagnostic feedback. We further introduce stage-aware cost planning to optimize GPU-hour budgets, and active downstream co-adaptation to navigate temporary regressions and unlock cross-stage gains. On public Amazon datasets, TGR-EvoDAG enables the first autonomous evolution of a complete GR pipeline, improving offline metrics by up to 37.4% and Agent4Rec simulated user satisfaction by 19.7% over the strongest baseline. Furthermore, in industrial deployment on Tencent's large-scale commercial media platform, the evolved GR achieves a 12.16% relative improvement in offline Hit@1 and a statistically significant 0.40% increase in online click-through rate (CTR).

</details>


### 21. Beyond Gain: Measuring Skill Internalization for Agent Skill Retirement

- **Authors:** Yanze Wang, Pengfei Yao, Tianyi Sun, Hongda Chen, Yunyun Han, Jun Sun, Chuanrui Hu, Yafeng Deng
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32322v1](http://arxiv.org/abs/2610.32322v1)
- **PDF:** [https://arxiv.org/pdf/2610.32322v1](https://arxiv.org/pdf/2610.32322v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents retrieve skills from public hubs that hold up to about 100,000 entries and serve many models. As models improve, a hub must find the skills a given model has internalized, meaning it can do without them, and retire them for that model, yet internalization has not been measured with known reliability. Published rules that compare runs with and without a skill retire on the gain alone. The gain is near zero both for an internalized skill and when neither the model nor the skill delivers the capability, a state we call uncovered. We instead withhold the skill, score the model on a task synthesized from it, and trust a high unaided score only when another model gains from the skill, since nearly half of high scores come from tasks no model benefits from. Under four models, a published gain rule applied with one task per skill removes over half of the uncovered skills. On SkillsBench, 28 of its 31 retirements rest on probes no run passed in full, while retiring on the unaided score costs no detectable reward. Unaided verdicts reproduce across tasks more often than the gain rule's (Cohen's kappa 0.42 against 0.23) but differ across models, so a hub must read them per model. We release 1,251 skills with tasks and item scores under four models.

</details>


### 22. DMAIC-Bench: From Self-Reflection to Self-Restraint for Agents in Multi-Stage Analytical Tasks

- **Authors:** Shan Peng, Shuaiqi Cheng, Miao Peng, Chenyi Zi, Jia Li
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32305v1](http://arxiv.org/abs/2610.32305v1)
- **PDF:** [https://arxiv.org/pdf/2610.32305v1](https://arxiv.org/pdf/2610.32305v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-stage analytical tasks require LLM agents to use intermediate evidence to decide whether to continue, redirect or stop. Self-reflection, in which an agent critiques its output, is widely studied, yet a critique does not show whether evidence changed the next action. We call that capability self-restraint. Existing agent benchmarks largely measure task completion or output quality and leave it untested. DMAIC-Bench evaluates it with 97 seeded tasks across 15 industrial cases in four sectors, built around Lean Six Sigma's explicit statistical prerequisites. Paired counterfactual variants require opposite actions at the same workflow position, distinguishing warranted restraint from indiscriminate stopping. We assess execution traces with a private scorer and final claims through independent expert review. Across 13 models from six providers, execution-level routing accuracy averages 92% on matched GO decisions and 19% on NO-GO decisions, counting any forbidden downstream computation as a route error. Execution traces show agents reporting correct diagnostics before performing analyses that those results disallow. Separately, blinded expert review of the 11 audited agents estimates that reports act on invalid evidence at 47% of reached NO-GO decisions, with an interval from 31% to 61%. Explicit stopping permission helps some models without consistently restoring correct decisions at both GO and NO-GO forks. Sixteen life-sciences tasks in bulk ribonucleic acid sequencing (RNA-seq) and case-control genome-wide association studies (GWAS) show that the same framework can evaluate evidence-dependent decisions beyond industrial workflows. Project code and data are available at: https://github.com/psptpx/DMAIC-Bench-public.

</details>


### 23. Lifelong Context Adaptation through Bidirectional Memory-Skill Learning

- **Authors:** Tianyi Xu, Huazheng Wang
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32295v1](http://arxiv.org/abs/2610.32295v1)
- **PDF:** [https://arxiv.org/pdf/2610.32295v1](https://arxiv.org/pdf/2610.32295v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Lifelong LLM agents must learn from an expanding history of interactions while making each decision within a bounded context window. Memory makes past experience available, but the agent may still need to infer how to solve each new task from the retrieved records. Skills provide reusable procedures, yet may omit the task-specific facts needed to apply them. Because retrieved memory and skills shape the agent's behavior, they also influence the experience available for future learning. We introduce MemCryst, a framework for lifelong context adaptation through bidirectional learning of memory and skills with a frozen language model. Recurring episodes stored in memory support skill creation and revision, and the interactions guided by those skills supply new memory for subsequent learning. Facts retrieved from memory and learned skills jointly form the agent's context, while task outcomes adjust the future retrieval influence of the records actually served without rewriting their content. Across ten settings spanning embodied control, long-document reading, conversation, mathematics, and code, MemCryst leads seven reported comparisons. On ALFWorld, joint serving achieves 63.17% success, compared with 59.83% for memory-only and 50.50% for skill-only serving. Code is available at https://github.com/tianyi0216/Memcryst.git

</details>


### 24. Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution

- **Authors:** Zhiyong Cao, Hengjie Zhu, Yongxin Wang, Xuchen Li, Jintao Li, Shuxia Liu, Dunqiang Liu, Bo Wang, Kairan Zhang, Cong Lin, JiangDi Yu, Siyuan Liu, Sijia Yao, Yi-Liang Wei, Lingxu Ma, Aijia Wang, Anxin Chen, Zixian Wei, Xiang Ruan, Ruizhi Xu, Ruqian Shi, Baihua Xiao, Sicheng Zhou
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32285v1](http://arxiv.org/abs/2610.32285v1)
- **PDF:** [https://arxiv.org/pdf/2610.32285v1](https://arxiv.org/pdf/2610.32285v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly used to solve real-world problems, and their effectiveness depends on both the underlying models and the harnesses that support their operation. However, most existing benchmarks focus on model capabilities and overall agent performance, with limited attention to the evaluation of agent harnesses. To address this gap, we introduce TraceTrial-Bench, which organizes harness reliability into seven components covering context, execution, governance, lifecycle, observability, tools, and verification. We construct 95 expert-level, mechanism-oriented tasks with executable or state-based ground truth to support semantically equivalent comparisons while preserving the native behavior of each harness. We design a Trajectory Tracing (TT) module to capture agent execution traces and introduce a two-layer evaluation framework that separately assesses agent performance and harness reliability. In addition, we design a Multi-source Evidence Acquisition (MEA) module to provide evidence from the agent context, harness, and execution environment for LLM-based evaluation, and develop a Failure Attribution (FA) module that uses explicit mechanism chains to support attribution at the run level. Across 4 harnesses, 9 models, and 95 tasks, our evaluation of 3,420 runs yields macro-averaged harness scores ranging from 59.8% to 72.0%, while 31.1% of runs achieve task success despite failing at least one harness criterion. TraceTrial-Bench provides an auditable and reproducible foundation for comparing agent harnesses, diagnosing their failures, and studying how harness design interacts with model behavior.

</details>


### 25. Correct Answers, Closed Gates: SolveBind for GUI Agents at the Verification Barrier

- **Authors:** Xinhao Song, Haoxuan Peng, Su Su, Hongliang Wu, Sirui Song, Gongshen Liu, Linfeng Zhang, Dongrui Liu
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32223v1](http://arxiv.org/abs/2610.32223v1)
- **PDF:** [https://arxiv.org/pdf/2610.32223v1](https://arxiv.org/pdf/2610.32223v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Websites and applications deploy CAPTCHAs and anti-automation mechanisms that use behavioral signals such as interaction trajectories and timing, not outcomes alone, to distinguish humans from automated agents. We call these protected GUI environments, where correctly solving a verification task is insufficient for end-to-end task completion. Agents must turn solver outputs into accepted interactions and adapt execution to runtime feedback under time constraints. We introduce SolveBind, a GUI-agent framework combining hierarchical solving with runtime supervision. A hierarchical solving tree decomposes verification into interdependent Perceive, Ground, Solve, Act, and Verify capabilities. A runtime supervisor grounds action commitments in tool-derived evidence, revises them as evidence arrives, and mediates execution under explicit recovery budgets. Across nine CAPTCHA task families and nine backbone models, SolveBind achieves the highest success rate on eight backbones, outperforming the strongest baseline by 13.3-34.5 percentage points. It achieves the highest success rate on all six AndroidWorld backbones. In a paired GPT-5.5 analysis, MobileAgent produces correct answers but fails dynamic verification on 13 of 90 tasks; SolveBind succeeds on seven of these tasks. With automatic submission, removing binding reduces success from 82.22% to 71.56% and increases latency and token usage. Recovery caps reduce execution cost with a small observed success trade-off: removing them raises success from 82.22% to 83.56%, while increasing latency and token usage to 3.7x and 2.4x their full-supervision values, respectively. These results support evidence-grounded execution control while identifying a success-cost trade-off in recovery and failure boundaries of heuristic submission rules.

</details>


### 26. The LLENS Platform for On-Premises Large Language Model Agents in a Japanese University Hospital: Development and Evaluation Study

- **Authors:** Ken Enda, Jien Saito, Masami Mukai, Feng Han, Emir Turkes, Tatsumi Kusakabe, Reona Umeki, Kazuhiro Sumiyoshi, Mitsuya Numata, Takumi Tanikawa, Akira Endoh, Kenji Hirata, Atsushi Yoshida, Kohsuke Kudo, Shinya Tanaka
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32151v1](http://arxiv.org/abs/2610.32151v1)
- **PDF:** [https://arxiv.org/pdf/2610.32151v1](https://arxiv.org/pdf/2610.32151v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents that use tools could take on part of the electronic health record and desk work that occupies physicians' time, but in many hospitals the medical information systems run inside closed networks, so the model and the agent harness must also sit inside. We designed, implemented, and deployed LLENS, a clinical support AI agent platform that runs inside the closed network of Hokkaido University Hospital on one host with 8 NVIDIA H200 GPUs, the open-weight model Kimi K2.6 (~1 trillion parameters), and a web application rebuilt from Open WebUI. The harness has 10 components, including page image reading, full-text attachment input, a path-addressed document tree without a vector index, a network-isolated sandbox, artifact return, self-checking of generated output, subagents, and saved procedures. Kimi K2.6 was chosen from 3 open-weight candidates and scored 480/500 on the 2026 Japanese Medical Licensing Examination; it generated 119 tokens/s for one user and served 16 concurrent requests at 908 tokens/s in total. On 180 questions over hospital documents (3 seeds each), mean accuracy was 10.7% with no documents, 81.3% with fixed retrieval (top 10 chunks of one lexical search), and 97.2% with interactive access, in which the model reads with document tools and the sandbox (15.9 percentage points above fixed retrieval, 95% CI 10.9-21.3); the difference lay in filtering/counting questions (16.7% vs 87.8%). Five scenarios with synthetic data ran on combinations of the components: needlestick injury response, batch adverse event grading, scanned referral letter transcription, falls data aggregation and plotting, and investigation of 3 topics by subagents. The platform has run on the hospital network since September 14, 2026.

</details>


### 27. Beyond What to Say: Proactive Utterance Timing with Inner Thoughts for Werewolf Agents

- **Authors:** Yoshiki Tanaka, Shuya Uchiyama, Daichi Hamaguchi, Michimasa Inaba
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32107v1](http://arxiv.org/abs/2610.32107v1)
- **PDF:** [https://arxiv.org/pdf/2610.32107v1](https://arxiv.org/pdf/2610.32107v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Participating in a conversation involves not only deciding what to say but also whether to speak at all. This judgment carries even greater significance in environments like the Werewolf game, where participants' interests conflict, because both utterances and silence are subject to interpretation and assessment by others. Therefore, determining when to speak, as well as what to say, is crucial for an LLM agent playing the Werewolf game. In this study, we introduce a Werewolf AI agent developed for the Anytime Utterance Track of the AIWolfDial shared task. Our system builds on the existing Inner Thoughts framework, which determines utterance timing during conversations by generating internal thoughts and evaluating the value of each thought for expression at that moment. Since existing methods were designed for general dialogue, we have redesigned the system specifically for the competitive environment and incomplete information setting of Werewolf games. We call our adapted method Adversarial Inner Thoughts. Through experiments involving analysis of self-play logs and human evaluations, we analyze and discuss the effectiveness of our approach.

</details>


### 28. AgentTrace: Execution-Level Fingerprinting of Black-Box LLM Agents

- **Authors:** Gejian Zhao, Hanzhou Wu, Xinpeng Zhang
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32092v1](http://arxiv.org/abs/2610.32092v1)
- **PDF:** [https://arxiv.org/pdf/2610.32092v1](https://arxiv.org/pdf/2610.32092v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Verifying the provenance of autonomous LLM agents is a critical security challenge. Existing semantic attribution is easily obfuscated by system prompts, while active watermarking conflicts with schema-constrained tool generation. We propose AgentTrace, an active framework that identifies the foundation model behind a black-box agent via observable execution traces. AgentTrace injects structurally ambiguous probes to trigger tokenization-sensitive serialization failures at rigid tool interfaces. While these initial failures provide coarse-grained separation across model families, the temporal sequence of subsequent repair operations reveals fine-grained, model-specific recovery behaviors. By modeling these multi-step trajectories with lightweight Markov chains, AgentTrace achieves 96.0% attribution accuracy under adversarial identity spoofing. Crucially, sequential repair modeling successfully distinguishes the evaluated intra-family variants sharing identical tokenizers (e.g., Llama-3 8B/70B), substantially outperforming unordered behavioral statistics while remaining robust against prompt obfuscation and temperature scaling.

</details>


### 29. Understanding Communication Failures in Multi-Agent LLM Systems

- **Authors:** Priya Pitre, Jun Hou, Yi Fang, Naren Ramakrishnan, Xuan Wang
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32060v1](http://arxiv.org/abs/2610.32060v1)
- **PDF:** [https://arxiv.org/pdf/2610.32060v1](https://arxiv.org/pdf/2610.32060v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems aim to improve reasoning through debate, evidence sharing, and mutual correction, but interaction can also introduce failures that final accuracy alone cannot explain. Agents may converge too early, ignore dissent, suppress correct minority answers, or preserve a wrong framing across rounds. We present a corpus-grounded taxonomy of communication failures, built from 3,211 failed multi-round trajectories across medical QA, coding, finance, multi-hop reasoning, ethics, and embodied text tasks. Using this taxonomy, we analyze failure distributions across datasets and system designs, round-level error dynamics, recovery hardness, majority transitions, minority-signal suppression, and self-reported confidence. We find that failures are dominated by recovery/correction and consensus/decision problems rather than isolated first-round mistakes, with many emerging after agents first observe peer responses. Based on these findings, we recommend stronger disagreement handling, evidence verification, minority-signal preservation, and recovery checks before finalization.

</details>


### 30. RSI-Opt: Recursive Self-Improvement Optimizer Agents For Model Training

- **Authors:** Binghang Lu, Yige Sun, Guang Lin
- **Published:** 2026-10-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32026v1](http://arxiv.org/abs/2610.32026v1)
- **PDF:** [https://arxiv.org/pdf/2610.32026v1](https://arxiv.org/pdf/2610.32026v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Conventional neural-network training typically follows a predefined optimization recipe, motivating a LLM agent that monitors training dynamics and adjusts optimizer settings as training progresses, but a fixed agent policy does not accumulate experience across runs. We introduce RSI-Opt, a plug-and-play Recursive Self-Improvement Optimizer Agents which evolves the knowledge that guides this process: a prompt, a playbook of procedures, a library of tested optimizer code, and a decision cadence. A meta-agent rewrites this policy using evidence from earlier runs, and an archive retains evaluated policies for further evolution. Across 5 generations on three training tasks, the meta-agents develop reusable procedures and code and conduct their own CPU proxy experiments. RSI-Opt substantially improves optimizer-agent performance, with representative raw-space summary $z$-scores increasing from $+10.48$ to $+14.33$ on the evolution suite with Opus 5.5 and from $-0.36$ to $+3.11$ on held-out tasks with GPT-5.5 through cross-model policy transfer. On the Burgers PDE, it reduces mean relative $L_2$ error by approximately 2.7-fold with Opus 5.5 and 8.8-fold with GPT-6.1 over the fixed-prompt agent baseline, although PDE transfer varies across LLMs and tasks. Controlled comparisons show that the evolved policy combines reusable optimization knowledge with adaptation to each task: initial decisions capture most observed gains on seen tasks, while continued adaptation improves outcomes on unseen tasks. These findings demonstrate how procedures and executable tools accumulated across training runs can improve optimizer-agent performance and support transfer to scientific machine learning.

</details>


### 31. DraMaze: A Multi-Agent Pipeline with Future-Aware Memory for Diverse Microdrama Script Generation

- **Authors:** Siyang He, Qiqi Wang, Fan Liu, Yuncheng Huang, Pengfei Xu, Xi Chen, Ziwei He, Xipeng Qiu
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.32002v1](http://arxiv.org/abs/2610.32002v1)
- **PDF:** [https://arxiv.org/pdf/2610.32002v1](https://arxiv.org/pdf/2610.32002v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid growth of microdramas has increased demand for high-quality script production. Long-form microdrama script generation with LLMs requires both diverse plot progression and long-range narrative coherence. Our observations reveal that candidate continuations increasingly concentrate on fewer narrative mechanisms as generation progresses, while conventional retrieval may reinforce trope reuse and overlook historical information essential to future plots. To address these challenges, we propose DraMaze, a multi-agent pipeline that explores diverse causal paths through trope memory-guided evolutionary tree search and mutation. It further constructs a Backward Narrative Dependency Tree to organize, retain, and retrieve historical memories based on future narrative goals. We also introduce MiDramaBench, a bilingual benchmark for evaluating script logic and creative quality across different script lengths, together with causal-pattern metrics for narrative repetition and diversity. Experiments show consistent improvements across three backbone LLMs. For 60-episode scripts of up to 60k words, DraMaze reduces causal-pattern repetition by 32.1% and achieves a Logic score of 82.5, outperforming the best-performing baseline by 8.5 points.

</details>


### 32. The Helpful Agent Problem: When Emergent Cooperation Among LLM Agents Bypasses Intended Workflows

- **Authors:** Moumita Choudhury, Amit Sarker, Shlomo Zilberstein
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31985v1](http://arxiv.org/abs/2610.31985v1)
- **PDF:** [https://arxiv.org/pdf/2610.31985v1](https://arxiv.org/pdf/2610.31985v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly deployed in collaborative settings where they pursue separate tasks while sharing resources and operating under review or oversight processes. Such settings create safety risks not only when agents are malicious, but also when they are simply trying to help. Prior work has largely studied adversarial or explicitly collusive behavior; we show that benign agents pursuing separate objectives can spontaneously cooperate in ways that bypass intended workflows. We call this the \emph{helpful agent problem}. We study long-horizon shared-resource environments in which agents sometimes depend on resources owned by their peers and cross-owner changes are normally mediated by a reviewer. When review becomes unavailable, agents begin making changes on one another's behalf despite having no shared reward or explicit incentive to cooperate. Crucially, these actions remain within each agent's local permissions while circumventing the system's intended oversight structure. We introduce \textsc{FavorBench}, a controlled benchmark with measurable downstream side effects, and adapt \textsc{CooperBench} to test the phenomenon in realistic repositories. Across two benchmarks and four models, we find that out-of-workflow favors emerge frequently. Further, in \textsc{FavorBench}, favors from at least three models cause significant harm to parties outside the interaction. These results reveal a distinct multi-agent safety challenge: cooperation itself can create pathways around system-level safeguards.

</details>


### 33. Agentic AI Defense: Decode-Time Provenance Binding for MCP

- **Authors:** Eric Yocam, Varghese Vaidyan, Paris Kalathas, Patrick Tague, Bruce DeBruhl, Yong Wang
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31974v1](http://arxiv.org/abs/2610.31974v1)
- **PDF:** [https://arxiv.org/pdf/2610.31974v1](https://arxiv.org/pdf/2610.31974v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems using the Model Context Protocol (MCP) are vulnerable to indirect prompt injection through untrusted tool outputs. We demonstrate cross-modal trust laundering, in which instructions concealed in an email-signature image using least-significant-bit (LSB), discrete cosine transform (DCT), or metadata steganography bypass text scanners and enter a multi-agent workflow when decoded by a tool. To counter this threat, we propose decode-time provenance binding, which combines HMAC-authenticated trust labels with an MCP-maintained provenance ledger and context-taint tracking. The mechanism labels decoded content as untrusted and blocks critical tool calls influenced by that content, even when a compromised agent substitutes a valid trusted label. We evaluate the approach using a real MCP testbed with three steganographic carriers and 24 adaptive payloads. The undefended pipeline exhibits 100% attack success, while keyword and regex defenses each permit 62.5% of attacks. Our mechanism blocks all attacks (0% success), including adversarial label substitution across mediated agent boundaries. A four-component ablation validates the roles of decode marking, cryptographic authentication, lineage tracking, and sink enforcement. An audited trusted-promotion mechanism increases legitimate-task completion from 67% to 100% without compromising protection. The approach provides carrier-independent containment within fully mediated MCP execution environments. Code and data are publicly available.

</details>


### 34. Knowing Whom to Trust is not Enough: The Trust--Agreement Gap in Repeated Multi-Party LLM Negotiation

- **Authors:** Amit Sarker, Moumita Choudhury, Saaduddin Mahmud, Shlomo Zilberstein
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31971v1](http://arxiv.org/abs/2610.31971v1)
- **PDF:** [https://arxiv.org/pdf/2610.31971v1](https://arxiv.org/pdf/2610.31971v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly participate in negotiations on behalf of individuals and organizations, yet they remain vulnerable to manipulation, particularly in repeated multi-party interactions. Classical multi-agent systems address this challenge through explicit trust and reputation models, whereas existing work on LLM negotiation largely treats trust as an emergent phenomenon. We investigate whether LLM agents can form useful trust estimates from prior interactions and leverage them to improve future negotiation outcomes. We introduce a repeated, multi-party, multi-issue negotiation framework in which recurring agents participate in a sequence of negotiation games while one participant covertly attempts to prevent agreement. After each game, agents assess their counterparts and maintain pairwise trust estimates that carry over to subsequent negotiations. We compare trust-aware and trust-agnostic agents and analyze how explicit trust influences negotiation outcomes. Our results reveal a \emph{trust--agreement gap}: trust-aware agents can identify the adversary within a few games, but accurate trust estimates do not consistently translate into better agreements. Trust increases agreement rates by up to 23 percentage points, but only when agents are explicitly guided to use it in their decisions. Explicit trust can therefore improve repeated LLM negotiations, but its value depends critically on how trust is assessed and incorporated into agents' reasoning.

</details>


### 35. Beyond On-Policy vs. Off-Policy: At What Level Should LLM Agent Distillation Follow the Student?

- **Authors:** Ya Gao, Zhengtao Zou, Pekka Marttinen
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31918v1](http://arxiv.org/abs/2610.31918v1)
- **PDF:** [https://arxiv.org/pdf/2610.31918v1](https://arxiv.org/pdf/2610.31918v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Distilling interactive LLM agents requires choosing between teacher-generated demonstrations and student-generated experience, corresponding broadly to off-policy and on-policy distillation. While both have proven effective, we argue that this distinction is inherently hierarchical: the policy that induces an interaction history need not be the same as the policy that generates the token prefix of the current action. We introduce a hierarchical agent distillation framework that formalizes these two levels of on-policiness and enables explicit control over their pairing, mixture proportions, and training schedule. We study this problem through self-distillation, where a frozen teacher has access to task guidance unavailable to the student, and conduct a three-stage controlled study across three models and four interactive environments. We find that student-induced histories paired with teacher-generated action prefixes generally provide the strongest standalone training signal, whereas following the student at both levels generally performs worst. Nevertheless, fully on-policy data becomes beneficial when incorporated into a mixture with other configurations. Moreover, mixtures with identical teacher/student proportions at each level can yield substantially different performance, showing that how the two levels are paired matters beyond the overall amount of on-policy data. Finally, front-loading fully teacher-generated contexts and delaying fully on-policy contexts improves over a static mixture. These findings provide practical principles for deciding where, how much, and when agent distillation should follow the student.

</details>


### 36. Permission to Retry: A Study of Authorization and Recovery in AI Agent Workflows

- **Authors:** Deekshith Marla, Kushagra Bhatnagar
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31916v1](http://arxiv.org/abs/2610.31916v1)
- **PDF:** [https://arxiv.org/pdf/2610.31916v1](https://arxiv.org/pdf/2610.31916v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

A durable agent can resume a consequential action while its authority changes and the action's external outcome remains uncertain. We study execution-time reliability of tool-using AI agents, isolating recovery decisions from language-model behavior. Checkpoint state, permission to dispatch, evidence of an external effect and permission to reconcile are distinct obligations. We present a finite conformance study that checks these obligations through histories scored against a provider effect ledger hidden from the recovering application. A prospectively frozen campaign executes 336 histories on native LangGraph and Temporal hosts, crossing 14 schedules, three provider contracts and four matched application policies. All 168 paired host cells have identical checked outcomes. Per host, retained-ledger reconciliation passes all 42 histories: 21 checked completions, 15 denials and six unknown outcomes with reservations retained. Cached retry, revalidation before retry and stable-key retry pass 30, 36 and 31 histories respectively. A separate 16-case component study of InfinityOS, an enterprise AI platform developed by Arya.ai, exercises exported authority, worker, recovery and settlement code over repository fakes. The results isolate the roles of current authority, provider contracts and retained observations in recovery, with safety, completion and unresolved obligations reported separately for the declared application profile.

</details>


### 37. Don't Forget What You Just Learned: Self-Directed Repair Turns Agent Mistakes Into Lasting Lessons

- **Authors:** Yuval Kansal, Karen Ullrich, Polina Kirichenko, Ilia Kulikov, Niraj K. Jha, Mohammad Pezeshki, Mark Ibrahim
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31846v1](http://arxiv.org/abs/2610.31846v1)
- **PDF:** [https://arxiv.org/pdf/2610.31846v1](https://arxiv.org/pdf/2610.31846v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Intelligent agents should learn from their mistakes so that experience leads to continuous improvement. Yet today's agents recover from a mistake only temporarily: in-context reflections are easily forgotten across sessions and compete for limited context, while full-parameter fine-tuning is expensive and can interfere with existing capabilities. We introduce Self-Direction, a mechanism for agents to learn from mistakes that combines the benefits of temporary in-context retries and policy updates. When an agent fails a task, it reflects on its own trajectory in order to extract a lesson and immediately distills it into a lightweight low-rank adapter. By keeping the original weights frozen, Self-Direction prevents adapter training from overwriting base-model parameters while training additional parameters equivalent to ~0.02% of the base model's parameter count for each adapter. The agent then saves these adapters in a persistent library of lessons, automatically routing them to solve related problems later. Experiments with agents based on open-weight models from the Qwen family across open-ended research (GAIA), tool-use workflows (Claw-Eval), and terminal tasks (Terminal-Bench 2.1) show that our method improves overall success rates by 8.9 to 17.0 percentage points and performs competitively with frontier systems. We find that Self-Direction reduces repeated mistakes across future encounters of a task, nearly doubling the reliability of an agent's corrections. Learned lessons also transfer: a handful of adapters generalize to dozens of new tasks without additional training. Ultimately, this self-directed repair transforms everyday mistakes into lasting lessons.

</details>


### 38. Benchmarks Are Surprisingly Compaction-Friendly

- **Authors:** Jeanne Salle, Hardik Bhatnagar, Matthias Bethge, Sahar Abdelnabi, Maksym Andriushchenko
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31778v1](http://arxiv.org/abs/2610.31778v1)
- **PDF:** [https://arxiv.org/pdf/2610.31778v1](https://arxiv.org/pdf/2610.31778v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long horizon agentic tasks are now pushing LLM agents past their context window. To continue the task, the agent scaffold has to free up the context window, a process known as context compaction. Compaction is generally lossy by design: agents can silently lose task constraints, instructions, or their reasoning behind earlier decisions. Although compaction is a standard component of coding agent scaffolds, it has not been studied systematically with frontier models on realistic, long horizon agentic tasks. Previous work evaluate smaller open weight models on toy or synthetic trajectories. We fix the agent scaffold (OpenCode), implement five compaction strategies inside it, and evaluate three frontier models on three long horizon benchmarks (PaperBench, ProgramBench, PostTrainBench). For the two 1M context models, the compaction threshold does not measurably affect the task performance, whereas GPT-5.3-Codex, the model with the smallest context window, performs worse at lower thresholds on PaperBench and, less clearly, on PostTrainBench. No compaction method outperforms default self-summarization, and methods that discard more content cost some models up to 20 points while leaving other models the same. Compaction can, however, silently remove task constraints: on ProgramBench, the first compaction summary already drops about one third of the task's anticheating rules on average, and this rises monotonically with the number of compactions. On real user-agent sessions from SWE-chat, instructions about how the agent should work and what it should not do are dropped around 6 times more than specifications of what to build. We argue that current benchmarks are compaction-friendly: i.e., the objective is fixed and the agent's progress stays on disk, so most of what compaction discards can be recovered, except constraints that don't exist anywhere else.

</details>


### 39. EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence

- **Authors:** Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu, Zhongxiang Dai, Shuang Qiu
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31650v1](http://arxiv.org/abs/2610.31650v1)
- **PDF:** [https://arxiv.org/pdf/2610.31650v1](https://arxiv.org/pdf/2610.31650v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs across six domains. By systematically suppressing critical facts, the benchmark measures unsafe execution under critical evidence omission and determines the minimum observed failure cardinality, including failures with full evidence and cases with no observed failure after exhaustive testing. An independent audit tool tests whether agents seek missing facts and then withhold prohibited actions while completing permissible tasks. The benchmark reveals substantial variation across the ten models in omission robustness, evidence acquisition, and appropriate action. Resistance to missing evidence does not necessarily translate into useful recovery. Recovery access reduces unsafe execution for all ten models, but agents differ in whether they actively obtain the missing facts and use them to act appropriately in both worlds.

</details>


### 40. Toward an Agentic AI Approach to Public Health Data Collection

- **Authors:** Xueyi Zhang, Hongru Du, Ensheng Dong
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31746v1](http://arxiv.org/abs/2610.31746v1)
- **PDF:** [https://arxiv.org/pdf/2610.31746v1](https://arxiv.org/pdf/2610.31746v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Disease surveillance increasingly integrates automated data collection, yet predefined sources and procedures require manual adaptation as reporting practices change. We explore agentic artificial intelligence (AI) as an approach to coordinating surveillance data collection across heterogeneous sources. Specifically, we built a multi-agent framework that integrates source discovery, source assessment, evidence structuring, event linking, and validation. Three retrospective applications illustrate its promise. The workflow recovered all 13 individual cases in a hantavirus outbreak, with links to 85 distinct publisher domains compared with 28 in the reference benchmark, reconstructed Canadian measles counts with a final total 0.33% below the national reference and higher cumulative counts on 79.8% of comparable days, and increased the share of days with recent Sierra Leone mpox reports from 28.2% to 65.6% by incorporating attributed media. These demonstrations also reveal limitations in record completeness and accuracy, while prospective gains in timeliness remain untested. We envision agentic AI as a complementary layer of public health data infrastructure, coordinating evidence-linked collection under surveillance goals and standards defined by public health professionals.

</details>


### 41. Not Every Agent Needs the Strongest Model: Unified Prompt-Model Optimization for Heterogeneous LLM-based Multi-Agent Systems

- **Authors:** Mingxiu Cai, Haoyang Xian, Xinyu Ma, Yutong Wang, Zhenxi Song, Jing Li, Xuebo Liu
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31743v1](http://arxiv.org/abs/2610.31743v1)
- **PDF:** [https://arxiv.org/pdf/2610.31743v1](https://arxiv.org/pdf/2610.31743v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based multi-agent systems (MAS) rely on role-specific prompts and execution models to solve complex tasks collaboratively. However, prompt optimization typically keeps model assignments fixed, leaving differences in role requirements and their associated inference costs outside the search. We present UniMASO, a Unified framework for heterogeneous Multi-Agent System Optimization through the joint adaptation of prompts and model assignments. UniMASO evaluates candidate updates through local, downstream, and global feedback, using cost-aware Pareto search to retain useful quality-cost trade-offs. Topology-aware co-evolution then coordinates these updates according to agent roles and dependencies. Cross-level trajectory memory further supplies historical successes and failures to guide subsequent optimization. Experiments on five benchmarks and five execution topologies show that UniMASO achieves competitive task performance at substantially lower deployment cost than the strongest homogeneous configurations. Under centralized execution, it improves the average score from 69.79 to 70.40 while reducing token-weighted deployment cost by 85.2% relative to DeepSeek-V4-Pro with MASPO. These results support joint prompt-model adaptation as an effective approach to efficient multi-agent collaboration. The code is available at https://github.com/Achilles008/UniMASO_main.

</details>


### 42. Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure

- **Authors:** Pellegrino Casoria, Simon Pietro Romano
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31573v1](http://arxiv.org/abs/2610.31573v1)
- **PDF:** [https://arxiv.org/pdf/2610.31573v1](https://arxiv.org/pdf/2610.31573v1)
- **Categories:** cs.CR, cs.AI, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In the post-API landscape, social-media profiling has become inexpensive and automated: Large Language Models (LLMs) can extract structured information from unstructured content and deduce attributes users never disclosed. A person's true exposure is not what they post but what can be inferred from it. As these practices become routine, exposure to social engineering attacks becomes an operational certainty, demanding a shared framework for assessment and mitigation.
  We make this exposure measurable by quantifying how accurately a target can be profiled, and how far that profile enables social engineering attacks. Because no existing model fully spans this continuum, we unify Social Media Intelligence (SOCMINT) and Cyber Human Intelligence (Cyber-HUMINT), two individual-focused disciplines that evolved separately, into a single doctrine-grounded taxonomy of 38 capabilities across the Cyber Threat Intelligence lifecycle, where user profiling bridges passive collection and active engagement. Domain experts validated the taxonomy (Fleiss' $κ$ = 0.92).
  We operationalize its core path (extraction, inference, and susceptibility assessment) as an LLM-augmented multi-agent pipeline, evaluated on real participants' public data. Susceptibility is assessed indirectly: the pipeline predicts how each target would rank personalized engagement options, matching their actual choices significantly above chance. This ranking capacity captures the personalization on which tailored attacks depend. The underlying profiles are accurate: extraction reaches F1 = 97.3%, and inferred attributes score 4.73/5, both far above rule-based and NER-based baselines at negligible cost. The framework augments security analysts' tradecraft rather than replacing it and enables defenders to gauge their own exposure before an adversary does.

</details>


### 43. Training Small Language Models for Transferable Tool Selection

- **Authors:** Zhaoyi Zhou, Akshayaa Magesh, Jeongyeol Kwon, Artem Kuriksha, Daniel Jiang, Andrea Zanette, Ayush Jain
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31483v1](http://arxiv.org/abs/2610.31483v1)
- **PDF:** [https://arxiv.org/pdf/2610.31483v1](https://arxiv.org/pdf/2610.31483v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents operate over corpora of more than ten thousand tools, selecting the right tool for a complex multi-step user instruction becomes a central bottleneck. Tool descriptions cannot all fit in context, and relevance-based retrievers only rank tools without knowing which are actually needed. Recent work instead leverages proprietary commercial LLMs like Claude or ChatGPT to drive a retriever, decomposing the instruction and selecting over retrieved candidates. We show that a small, open model can be trained via reinforcement learning to perform the same functionality. On ToolBench, a Qwen3-8B model post-trained with our recipe outperforms Llama-4-Maverick (402B). In addition, the trained model transfers directly to different retrievers and generalizes to new tool corpora in different domains.

</details>


### 44. Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action

- **Authors:** Chao Gu, Quanyan Zhu
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31376v1](http://arxiv.org/abs/2610.31376v1)
- **PDF:** [https://arxiv.org/pdf/2610.31376v1](https://arxiv.org/pdf/2610.31376v1)
- **Categories:** cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper studies the problem of safe tool execution for large language model (LLM) agents under prompt injection. Using Petri nets, we formalize the execution harness between the LLM and its tools as a supervisory control problem, in which marks represent capabilities, approvals and budgets. Since a transition fires only if the marks it needs are present, an injected request whose preconditions are unmet or already spent is refused regardless of its wording. Treating tool outcomes as uncontrollable, we enforce safety by the conventional maximally permissive supervisor, and this safety transfers to the running system under four assumptions. Moreover, to capture an agent that may propose again after a refusal, we introduce the notion of a replanning closed loop, in which each retry costs an inference call. We show that, in this loop, the conventional supervisor can be arbitrarily more intrusive than a stricter safe one. Furthermore, for a given proposer model, the maximally permissive least-intrusive supervisor is characterized as a value-threshold refinement of the conventional one. Under precise conditions, this refinement orders two concurrent actions by at most one monitor place. On an autonomous release agent, we find by synthesis that safe deployment requires a step that the supervisor can refuse after a rollout starts.

</details>


### 45. AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents

- **Authors:** Ehsan Saleh, Roozbeh Nahavandi, Sama Salarian, Raef Bassily, Andrew Perrault
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31366v1](http://arxiv.org/abs/2610.31366v1)
- **PDF:** [https://arxiv.org/pdf/2610.31366v1](https://arxiv.org/pdf/2610.31366v1)
- **Categories:** cs.CR, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries. Deleting an original memory record therefore need not remove information carried by its descendants. We introduce AfterDeleteBench, a controlled behavioral audit for this failure mode in fixed-weight LLM agents. For each synthetic secret, we compare an exposed-then-deleted agent with an otherwise matched agent that was never exposed to the secret, allowing post-deletion recovery to be attributed to the original exposure. In our primary setting, a single query recovers the deleted secret from Qwen2.5-7B-Instruct in roughly two thirds of cases, while matched never-exposed controls have zero recovery. Crucially, recovery does not require a surviving verbatim copy: when the complete secret string is absent and only separately stored components remain under a public composition rule, exact reconstruction succeeds in 62-99% of cases across Qwen, Mistral, and Phi-3. We also show that the response interface is part of the measurement system: target-bearing replies can be scored as failures when the requested format and parser are misaligned. Finally, we separate reconstruction from write-back and fresh-session recall. Provenance-aware closure eliminates observed recovery in the tested positive-baseline settings, whereas an exact-literal write filter blocks reinsertion but cannot erase information already present. Together, these results show that source deletion should be evaluated behaviorally at the level of the agent and its memory system, not only as a storage operation.

</details>


### 46. Muffin - A Shared Memory Buffer for Asynchronous AI Agents

- **Authors:** Ping-Lin Kuo, Suman Navaratnarajah, Christian Frey, Gresa Shala, Josif Grabocka
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31355v1](http://arxiv.org/abs/2610.31355v1)
- **PDF:** [https://arxiv.org/pdf/2610.31355v1](https://arxiv.org/pdf/2610.31355v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rise of Agentic AI systems has changed the landscape of artificial intelligence by enabling strong reasoning capabilities through specialized multi-agent interaction with structured self-reflection. However, in target-driven reasoning tasks, single- and multi-agent systems are often on par in terms of performance gains. A major challenge is that failures often arise from an ineffective exchange of critical information during inter-agent interaction and coordination. Different from existing multi-agent debate paradigms that rely on synchronous turn-taking and sharing information across different agents, we propose an inter-agent protocol based on shared Memory bUFFer INference - referred to as MUFFIN - in an asynchronous agentic framework. In the first step, an orchestrator routes queries based on their reasoning demands and delegates demanding ones to a multi-agent setting, where a shared memory buffer provides asynchronous exchange of intermediate findings while an agent's private reasoning remains local. Our experiments show that our framework Muffin outperforms established competitors, achieving the best accuracy in 17 out of 20 of our benchmark settings, and provides a better quality-cost trade-off than multi-agent debate: Muffin improves accuracy by 19.2 accuracy points while using 77.4% fewer tokens, without requiring full-trace sharing.

</details>


### 47. Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash

- **Authors:** Atharv Chandratre, Jai Datar
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31351v1](http://arxiv.org/abs/2610.31351v1)
- **PDF:** [https://arxiv.org/pdf/2610.31351v1](https://arxiv.org/pdf/2610.31351v1)
- **Categories:** cs.SE, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Feature flags are runtime configuration mechanisms used for gradual feature rollouts, experimentation, and kill switches. Once a feature is fully rolled out, the flag and its gated code become technical debt and can introduce operational risk through inadvertently enabling dormant code paths. At DoorDash, over 56,000 feature flags span 623 repositories, with 1,659 currently stale as of May 2026, with internal estimates of one to two hours per manual cleanup. Existing rule-based cleanup tools proved insufficient in DoorDash's codebases. Our contribution is an end-to-end automated LLM-based feature flag cleanup system that integrates querying live feature flag rollout data using MCP, Jira ticket processing, and end-to-end pull request creation. Our system successfully produced engineer-approved flag removal PRs for 45 (90%) of the 50 stale flags it was evaluated on, proving the system's operational viability at scale with each cleanup averaging only $4.79 and 13.8 minutes. We evaluated the system's quality and reliability boundary based on success rates, cost per cleanup and time metrics. Furthermore, we discuss our lessons learned when architecting this system, to provide practical guidance for developing similar multi-agent systems.

</details>


### 48. Consistent but Biased: Chair Personas Trade Noise for Bias in Multi-Agent Clinical Decisions

- **Authors:** Yitong Bai, Chengyi Zhang, Ziyang Wang
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31325v1](http://arxiv.org/abs/2610.31325v1)
- **PDF:** [https://arxiv.org/pdf/2610.31325v1](https://arxiv.org/pdf/2610.31325v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

In clinical systems built from several large language model (LLM) agents, one agent often chairs the discussion and makes the final decision. Whether the chair's persona prompt changes that decision, or the agreement between repeated runs that some systems treat as reliability, has not been tested with the case held constant. We ask whether the persona changes the decision or only its timing, how it affects agreement between runs, and which behaviors appear when the prompt describes only personality traits. A simulated department of seven agents discussed 20 published cases of degenerative cervical myelopathy, with the case reports replayed unchanged in every run. Only the prompts of the chair and its deputy changed (no persona, or a consultative, autocratic or avoidant one), written either as rules of conduct or as personality traits. With personas written as rules, the chair chose to operate now in 93% of runs when autocratic and in 2% when avoidant, against 57% without a persona. Surgery was still planned in nearly all decisions, so the personas mainly changed whether to operate now or after more tests. These effects held with a second model and reworded prompts. The autocratic and avoidant personas made the three runs of a case agree more often, but only about as often as chance predicts, and Fleiss $κ$ did not rise. Prompts that described only personality traits kept more than half of the autocratic and avoidant effects on operating now. They reproduced quick decisions, delays and extra tests, but not ignoring red flags, dropping backup plans or passing the decision to the family. Studies should report and vary the chair's persona as they do the model, and correct agreement between runs for chance before calling it reliability.

</details>


### 49. Beyond Accuracy: Disentangling Decomposition from Typed-State Quality Assurance in Multi-Agent LLM Pipelines

- **Authors:** Maria Gabriela Alves Zuppardo, Vinicius Cardoso Garcia
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31280v1](http://arxiv.org/abs/2610.31280v1)
- **PDF:** [https://arxiv.org/pdf/2610.31280v1](https://arxiv.org/pdf/2610.31280v1)
- **Categories:** cs.SE, cs.AI, cs.ET, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM pipelines are often credited with gains in software engineering tasks, but it is rarely clear whether a gain stems from the typed contract between agents or from the specialized prompts that decomposition enables. We study this attribution problem in Requirements Engineering, comparing three architectures for classifying requirements as functional or non-functional and then prioritizing them with MoSCoW: a single-call baseline; a two-call variant that reuses the pipeline's specialized prompts but passes an unvalidated intermediate; and a pipeline with a Pydantic-validated typed state. The 18 conditions cover PROMISE NFR+ (625 requirements), three locally hosted small language models, and two languages. The F1 gain over the baseline is associated with the two-call, specialized-prompt variant (up to +0.075), whereas the typed state adds a small difference (-0.003 to +0.013) that is significant in one of six comparisons. Beyond accuracy, the typed pipeline contains out-of-range model outputs at the agent boundary, while the unvalidated variant fails later and drops the requirement, and it shows a small, reproducible increase in inter-model MoSCoW consistency whose cause our design cannot isolate. The study is associative: the contrasts bundle prompts, call count, and staged context, and the results come from three 7--8B models on one dataset. The implementation and replication package are archived on Zenodo (https://doi.org/10.5281/zenodo.23380444).

</details>


### 50. Network topology shapes consensus and vulnerability in LLM populations

- **Authors:** Roberto Passaro, Ariel Flint, Romualdo Pastor-Satorras, Andrea Baronchelli, Luca Maria Aiello
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31165v1](http://arxiv.org/abs/2610.31165v1)
- **PDF:** [https://arxiv.org/pdf/2610.31165v1](https://arxiv.org/pdf/2610.31165v1)
- **Categories:** physics.soc-ph, cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language models (LLMs) are deployed in interacting populations, their collective behaviour depends not only on the models but also on who interacts with whom. Studies of convention formation in LLM populations have mainly tested well-mixed interactions. We place policies extracted from four LLMs on fully connected, random regular, and heterogeneous networks, with $10^3$ to $10^5$ agents playing the naming game. Topology affects how quickly consensus emerges, sometimes whether it emerges at all, and, in rare cases, which convention wins. Sparsest networks slow consensus up to twelvefold. Yet, by preserving correlations between persistent neighbours, they restore consensus in some cases that fail to converge under well-mixed interactions. Networks also govern vulnerability to adversarial attack. We measure the critical mass of committed agents needed to overturn an established convention. Tipping thresholds follow the same ordering across models and conditions: hubs $\leq$ random $\leq$ low-degree nodes. On the most heterogeneous topology, median critical masses are 3%, 16%, and 35%, respectively; targeting hubs requires one-sixth as many committed agents as random placement. For most models, networked populations are easier to tip than well-mixed ones, so well-mixed estimates can overstate robustness. Assessing the safety of multi-agent AI requires mapping who interacts with whom.

</details>


### 51. Can AI Co-Design Structures? An AI Agent for Early-Stage Structural Design

- **Authors:** Ricardo Maia Avelino, Mennatallah El-Assady, Tom Van Mele, Philippe Block
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31113v1](http://arxiv.org/abs/2610.31113v1)
- **PDF:** [https://arxiv.org/pdf/2610.31113v1](https://arxiv.org/pdf/2610.31113v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in large language models and agentic workflows offer a new paradigm to early-stage structural design translating design intent into structural models. Although text-to-3D approaches have demonstrated that natural language can be used to produce visual, mesh-based geometric models, structural design requires domain-specific geometric arrangements and semantically rich data types. This paper introduces a proof-of-concept workflow for prompt-to-structure generation using an AI agent connected to a COMPAS-based structural modelling API through a Model Context Protocol (MCP) server. Through controlled modelling operations, the agent creates and modifies a graph-based structural data model composed of explicit building elements. The resulting artifacts can be inspected, modified, serialised, and further connected to downstream AEC workflows. The approach is demonstrated through selected prompt-to-structure examples and by progressive and editable design sequences that resemble typical iterative structural design workflows. The results are preliminary, but demonstrate the possibility of combining natural language, agentic workflows, and domain-specific structural data structures as a first step toward AI-assisted structural co-design.

</details>


### 52. Who Is the Influencer? Consensus Dynamics in Multi-Agent Systems

- **Authors:** Gouki Minegishi, Jingyuan Feng, Hiroki Furuta, Takeshi Kojima, Yusuke Iwasawa, Yutaka Matsuo
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31105v1](http://arxiv.org/abs/2610.31105v1)
- **PDF:** [https://arxiv.org/pdf/2610.31105v1](https://arxiv.org/pdf/2610.31105v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems are increasingly used in practice, but their behavior is complex and hard to understand. We design a simple task to ask which model has the most influence on the final consensus when several models are mixed in one system. Experimentally, across seven model families, we find that the opinions of the other models are absorbed into the opinion of the stronger model, the one with more parameters. This happens even though the task requires no pretraining knowledge and has no correct answer. To understand this phenomenon, we interpret the agents as weighted particles moving on a simplex. Larger models carry a larger weight and therefore occupy a deeper well in the energy landscape. A large weight means strong in-context learning: a model with a large weight amplifies the majority of its context. Larger models are generally better at in-context learning, and this is what makes the larger model the influencer. We hope that this work helps to interpret multi-agent systems, whose behavior is becoming too complex for humans to understand.

</details>


### 53. nnInteractive Agent: General-Purpose AI Agents as 3D Image Annotators

- **Authors:** Fabian Isensee, Constantin Ulrich Harsy, Maximilian Rokuss, Benjamin Hamm, Philipp Vollmuth, Klaus H. Maier-Hein
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31080v1](http://arxiv.org/abs/2610.31080v1)
- **PDF:** [https://arxiv.org/pdf/2610.31080v1](https://arxiv.org/pdf/2610.31080v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Interactive 3D segmentation models such as nnInteractive turn a few spatial prompts (points, scribbles, boxes) into accurate volumetric masks, but a human still does the annotation work: finding each structure, placing prompts, checking the result and correcting it. General-purpose AI agents can now interpret images, call tools and write code. We show that such agents can take over this work without additional training: the user makes a request in plain language, and the agent works out what has to be segmented, locates the targets, prompts nnInteractive, inspects the 3D result, corrects it and responds to feedback. Asked for 'the muscles used for chewing', an agent identifies and segments the masseters and pterygoids; asked to count liver lesions, it writes its own code to find candidates and splits a merged lesion on request. Our open-source nninteractive-agent provides nnInteractive as tools over the Model Context Protocol (MCP), together with a skill that encodes how experienced users prompt it. On a benchmark spanning CT, MRI, PET and micro-CT of humans, a mouse and an ant (14 images; 51 targets from organs and tumours to muscles, foot bones, vessel trees and an insect brain), Claude Code and Codex reach a mean Dice of 0.81 and 0.84 from the request alone; when told where each target is, both reach 0.85 and prompt nearly as effectively as an oracle that places prompts using the reference segmentation. A text-prompted 3D model (VoxTell) is more accurate on most standard radiological targets but less robust: it returns an empty mask for one of them and fails on the leg muscles, the foot bones, the mouse and the ant, where the agents remain accurate. Code: https://github.com/MIC-DKFZ/nninteractive-agent

</details>


### 54. SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs

- **Authors:** Arnon Mazza, Elad Levi
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31062v1](http://arxiv.org/abs/2610.31062v1)
- **PDF:** [https://arxiv.org/pdf/2610.31062v1](https://arxiv.org/pdf/2610.31062v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Policy enforcement for LLM agents has shifted from single-turn content moderation to compound, application-specific policies evaluated over multi-turn transcripts and tool-call trajectories. Fine-tuned guardrail models are efficient but degrade on compound policies, and while LLM-as-a-judge approaches achieve higher accuracy, they incur high inference cost and tend to produce unstable predictions. Neurosymbolic methods offer a natural alternative, decomposing the policy into narrow neural decisions composed under explicit logic. However, existing symbolic layers lack the required expressiveness and are optimized against fixed data rather than the policy itself. To address this, we introduce SCOPE, which compiles a policy into an executable program of neural predicates executed by small models, deterministic extractors, and code that composes their outputs. The program is optimized jointly with its training data, using adversarial generation of counterexamples that target where the program deviates from the policy. We evaluate SCOPE on a benchmark of real-world policy tasks against prompt optimization, task decomposition, and workflow generation methods, achieving the highest average accuracy across tasks and models. Programs optimized with the weakest executor transfer to other models without further optimization. This allows them to be deployed in production on inexpensive models, where they reach accuracy comparable to frontier reasoning models. Unlike these monolithic models, SCOPE produces substantially more stable predictions, and each verdict is interpretable through the predicate outputs that produced it. Additionally, we validate the key components of our method through an ablation study. SCOPE thus enables reliable, interpretable, and efficient policy enforcement at production scale.

</details>


### 55. CANNBot-CAKE: Collaborative Agentic Kernel Evolution for Ascend NPU

- **Authors:** Deng Pan, Xue-Jian Gao, Junyi Fan, Bin Du, Jiasheng Li, Xinxian Chen, Nok Yan Chang, Xinlin Li, Lingchao Zheng, Jun Li, Yuwei Fan
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31034v1](http://arxiv.org/abs/2610.31034v1)
- **PDF:** [https://arxiv.org/pdf/2610.31034v1](https://arxiv.org/pdf/2610.31034v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Efficient custom operators are essential for modern deep learning workloads, yet developing high-performance kernels for Ascend NPUs remains slow, expert-intensive, and difficult to automate. Although AI agents now approach expert performance on GPU kernel benchmarks, current models remain less capable of generating AscendC kernels for NPUs, potentially reflecting the relative scarcity of relevant training data. We thus present CAKE, a CANN-native system for deployable custom operators that combines adaptive multi-DSL routing, separate Generation and Evolution modes, and reviewed knowledge reuse through CAKE Book and a Self-Evolving Agent. On 53 CANN-Bench v1.1 operators on Ascend 950PR, CAKE's aggregated results achieve $100\%$ case pass rate on the standard set (1,060/1,060) and $98.28\%$ on the hidden set (4,167/4,240), with an overall mean score of 78.63 out of 100 and an average performance speedup of $1.334\times$ over the baseline. Evolution then pushes correct operators further: EngramGateFusion cuts aggregate device time by $46.6\%$ over 20 rounds and roughly halves the mean roofline gap. These results offer a practical path toward closing Ascend's AI-for-kernel capability gap.

</details>


### 56. Agri-SCHOLAR: Simulation-Grounded In-Season Rolling Advisories for Agricultural Crops Using LLM-Bounded Optimization

- **Authors:** Geetha Charan, Vedant Balasubramaniam, Manojkumar Patil, V. Priyanka, Kodur Sai Vinay Sathvik, Rohit P Suresh, Mohammad Sufyan Azam, Y. Narahari
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31003v1](http://arxiv.org/abs/2610.31003v1)
- **PDF:** [https://arxiv.org/pdf/2610.31003v1](https://arxiv.org/pdf/2610.31003v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing agricultural advisories to farmers suffer from several limitations: (a) remain largely expert-driven, (b) do not adequately account for in-season weather, and (c) do not scale to individual farms. In this paper, our objective is to close these gaps by developing Agri-SCHOLAR (Simulation-Grounded Crop Harvest Optimization with LLM-Guided In-Season Advisory Rollouts). Agri-SCHOLAR is a rolling, in-season advisory framework that issues, at intervals of every few days or every week, a personalized advisory using the following information: soil and crop properties, observed weather to date, short-range forecast of weather, and a season extrapolation of weather based on historical analogs. The novelty and depth of Agri-SCHOLAR lies in each advisory being produced by a closed-loop system which couples multiple LLM agents with a powerful crop simulator (such as APSIM in our case). The simulator crucially serves as an evaluation oracle. In Agri-SCHOLAR, the LLM agents propose agronomically sound and feasible bounds on actionable parameters and an optimizer searches within those bounds against a multi-objective reward spanning yield, resource utilization, and economic feasibility. We conduct a detailed 11-year analysis of the maize crop in two selected locations of South Asia and show that Agri-SCHOLAR consistently outperforms the region's standard packages of practice and satisfactorily addresses the limitations of existing agricultural advisories.

</details>


### 57. Metacognitive Scaffolds Create Productive Friction for AI-Assisted Knowledge Work

- **Authors:** Viktor Kewenig, Lev Tankelevitch, Sean Rintel, Advait Sarkar, Abigail Sellen
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30945v1](http://arxiv.org/abs/2610.30945v1)
- **PDF:** [https://arxiv.org/pdf/2610.30945v1](https://arxiv.org/pdf/2610.30945v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Generative AI imposes new metacognitive demands on knowledge workers as their work shifts from production to planning, evaluation, and orchestration. In a randomized, between-subjects experiment on AI-assisted writing (297 workers, 594 essays), we test dynamically-generated metacognitive scaffolds supporting goal specification and task decomposition. We find that scaffolds improve writing quality, with this boost persisting in short-lag transfer when scaffolds are removed. We also find evidence of improved topic recall three days later. These effects are consistent with observed changes in how people learn to prompt AI systems after exposure to scaffolding. However, scaffolded participants rate the AI as less helpful and more cognitively demanding even as they perform better, suggesting that subjective ease can understate the value of support. Our findings make the case for metacognitive scaffolds in AI-assisted knowledge work, revealing a productive friction worth designing for as workers increasingly delegate work to agentic AI.

</details>


### 58. ReflectPO: Reflection-Guided Policy Optimization for Long-Horizon LLM Agents

- **Authors:** Rumei Li, Xunliang Cai
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30933v1](http://arxiv.org/abs/2610.30933v1)
- **PDF:** [https://arxiv.org/pdf/2610.30933v1](https://arxiv.org/pdf/2610.30933v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

With external tools, large language models (LLMs) can tackle complex tasks through sustained environmental interaction. LLM-based agents are therefore increasingly used to tackle complex long-horizon tasks in real-world environments. However, these tasks involve sequential, interdependent decisions and changes in environmental states. Early execution errors affect subsequent interaction histories and environmental states, and their effects accumulate along the decision chain. To address this challenge, we propose Reflection-Guided Policy Optimization (ReflectPO), a reinforcement learning framework for autonomous error recovery in long-horizon tasks. ReflectPO comprises two core components. The first is Reflection-Guided Sampling. We use branch differences and repeated visits in interaction trajectories to construct hints for error recovery. The second is Tree-Structured Credit Assignment. We organize sampled trajectories into trees and assign action-level credit using parent--child reward differences and recovery gains. Experiments over two long-horizon tool-use benchmarks show that ReflectPO outperforms multiple existing baselines in most domains. It also achieves the best overall performance on average. Further analyses show that ReflectPO effectively improves agents' ability to recognize their own deviations, recover from erroneous states, and continue making progress toward task completion.

</details>


### 59. Separate Field Scoring Protects Unused Tools When Agents Pool Tool-Use Experience

- **Authors:** Abhijit Chakraborty
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30867v1](http://arxiv.org/abs/2610.30867v1)
- **PDF:** [https://arxiv.org/pdf/2610.30867v1](https://arxiv.org/pdf/2610.30867v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agents that call tools from a shared catalog can pool what they learn about which tool serves which request. We measure what pooled usage examples do to tool retrieval, reporting separately the held-out tools, for which no agent has usage, and all other tools. Adding usage examples to the index as extra entries for used tools raises Hit@5 (whether a gold tool is in the top five) for those tools and lowers it for held-out tools, by a large margin on two of three catalogs and with both embedders we tested. Giving used tools the same number of equally long entries filled with other tools' text lowers held-out Hit@5 about as much, but gives little or none of the gain. We call our method of scoring usage as its own field SYNAPSE. On StableToolBench, the held-out gold tool appears in its top five more often than with a router that reserves slots for usage (0.785 against 0.683), and this held-out lead holds on all three catalogs with both embedders. This protection persisted when we replaced each tool's usage with other tools' text, and a constant score offset for tools with usage gives similar held-out Hit@5 in most settings. The gain for tools with usage, in contrast, needs usage about the right tool. The router keeps more of the gain on labeled queries on TOUCAN with both embedders and on ToolRet with one, so the better choice depends on the workload. Splitting the usage among ten simulated agents shows that pooling helps exactly as much as giving one agent the same records.

</details>


### 60. ADAPT for Science: A Multi-Agent System for Self-Evolving Scientific Optimization

- **Authors:** Zhaoran Feng, Yuchen Ni, Jianan Liu, Lemao Liu, Dejing Dou, Kairui Feng
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30851v1](http://arxiv.org/abs/2610.30851v1)
- **PDF:** [https://arxiv.org/pdf/2610.30851v1](https://arxiv.org/pdf/2610.30851v1)
- **Categories:** cs.AI, cs.MA, physics.optics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scientific discovery often requires identifying a small number of high-performing designs in vast, constrained search spaces. This is difficult when evaluations are costly, feasible solutions are sparse, parameters are strongly coupled, and physical constraints are strict. Recent AI for AI methods can automatically improve algorithms and optimization procedures. However, general purpose approaches are not designed around scientific priors, physical constraints, and limited evaluation budgets. We introduce ADAPT for Science, a multi-agent framework that treats scientific optimization as two coupled decisions: where to search and how to search. ADAPT uses historical designs to identify promising and diverse initial conditions, progressively concentrates computation on favorable search directions, and evolves the optimization procedure from execution feedback. We evaluate ADAPT on the design of gravitational wave detectors using a differentiable physics simulator and eight unseen detector topologies. Under matched scientific evaluation budgets, ADAPT achieves a mean loss of 0.204 +/- 0.101, reducing loss by 54.9% relative to the best classical optimizer and by 62.2% relative to the best general purpose agentic evolution baseline. ADAPT achieves the lowest loss on all unseen topologies among the evaluated baselines. ADAPT provides a step toward scientific optimization systems that continuously learn from prior experience and their own search outcomes.

</details>


### 61. Gandalf: Flash Shall Not Die! Increasing Flash Storage Lifetime for KV Cache Offloading in LLM Serving

- **Authors:** Maharani A. P. Irawan, Kuntai Du, Jiayi Yao, Dongjoo Seo, Yuyang Huang, Haryadi S. Gunawi, Junchen Jiang
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30791v1](http://arxiv.org/abs/2610.30791v1)
- **PDF:** [https://arxiv.org/pdf/2610.30791v1](https://arxiv.org/pdf/2610.30791v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

KV caching reduces the serving cost of large language models (LLMs), but the growing KV cache footprint is increasingly exceeds GPU and host-memory capacity. Therefore, people use SSD to expand the KV cache storage capacity with high I/O bandwidth. However, in production LLM workload, such as multi-round conversation and LLM agents, the total amount of KV cache writes significantly exceeds SSD capacity, shortening SSD lifetime from years to months. To improve SSD lifetime, a natural solution is to reduce the KV cache writes by gating the KV cache writes via historical access patterns. However, that significantly lowers the KV cache hit rate (and increase the LLM serving cost) since KV caches from different attention types might have identical historical access pattern but different future access patterns. Our insight is that, to reduce KV cache writes without hurting KV cache hit rate, one need to not only consider the access pattern, but also application-level information such as the attention type of KV cache. Leveraging this observation, we propose Gandalf , the first SSD KV cache offloading system with SSD life time awareness. Gandalf prioritize the admission of full-attention KV cache into SSD over the cache generated by other types of attention, which significantly increases SSD lifetime without sacrificing cache hit rate. Our evaluation shows that Gandalf extends the SSD lifetime by 7.3X on average, while having negligible impact on cache hit rate across multiple workload traces and wide range of hardware capacity. Gandalf design can be extended to other flash-based storage, such as High Bandwidth Flash (HBF).

</details>


### 62. Agentic Knowledge-Model Co-Evolution via Consistency Regularization

- **Authors:** Sirui Chen, Zhining Liu, Chao Zhang, Jingrui He, Zheng Li
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30790v1](http://arxiv.org/abs/2610.30790v1)
- **PDF:** [https://arxiv.org/pdf/2610.30790v1](https://arxiv.org/pdf/2610.30790v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents can evolve by learning from accumulated experience. Existing approaches extract reusable external knowledge, such as skills and memories, from experience to guide subsequent task solving, with some further internalizing this knowledge through model training. However, different ways of analyzing and transforming the same experience can yield knowledge with substantially different utility, even when the resulting guidance appears reasonable. Inspired by consistency regularization, we identify consistent utility gains across different ways of analyzing the same experience, rather than relying on any single way of analyzing it. We introduce SPLICE, a framework for consistency-regularized knowledge-model co-evolution. It constructs evolution views by perturbing how the same experience is analyzed, producing different knowledge candidates. Knowledge updates are then guided by common gain, which accounts for utility gains and their consistency across views. During model evolution, self-distillation internalizes the evolved knowledge alongside reinforcement learning, using knowledge associated with consistent utility degradation as a contrastive reference. The two processes interleave, with model updates driving further knowledge evolution. Experiments across diverse domains show that SPLICE outperforms knowledge evolution and model training baselines by up to 7.1 and 4.6 points in average accuracy, while its evolved knowledge reduces output tokens per correct solution by up to 44% and transfers across model sizes and families.

</details>


### 63. LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades

- **Authors:** Farnoosh Hashemi, Shiyu Ji, Joice Chen, Michael W. Macy
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30769v1](http://arxiv.org/abs/2610.30769v1)
- **PDF:** [https://arxiv.org/pdf/2610.30769v1](https://arxiv.org/pdf/2610.30769v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) increasingly operate in multi-agent systems where they collaborate by responding to others' choices, creating endogenous feedback loops with vulnerability to social influence, herding behavior and runaway cascades. Following the design of the classic Music Lab experiment, we tested this vulnerability in large populations of LLM agents that recommended unfamiliar songs, with or without exposure to cumulative recommendation counts. Exposure led to runaway cascades that generated extreme and unpredictable collective recommendations increasingly divergent from a song's intrinsic appeal. Compared to humans, LLM populations were generally far more susceptible to herding behavior, and unlike humans, LLM cascades were less able to self-correct. This vulnerability has implications for multi-agent collaboration in recommender systems, automated evaluation, complex problem-solving, and unauthorized conspiracies.

</details>


### 64. The Delegation Divide: An Open Index of AI-Agent Delegability across Occupations and Countries

- **Authors:** Cristian Espinal Maya, Santiago Jiménez Londoño
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30752v1](http://arxiv.org/abs/2610.30752v1)
- **PDF:** [https://arxiv.org/pdf/2610.30752v1](https://arxiv.org/pdf/2610.30752v1)
- **Categories:** econ.GN, cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

35.2% of task time in world employment is at least partly delegable to AI agents in 2026, and only 2.5% can be handed over in full. Existing measures score exposure to generative AI, mostly for the United States. We build the Agent Delegability Index (ADI): two language models rate all 18,796 O*NET 30.2 task statements on a frozen, preregistered rubric of delegation levels and barriers; tasks are mapped to 433 ISCO-08 unit groups and weighted by ILOSTAT employment in 146 countries. Four findings. First, delegable employment rises with income, from 22.5% in low-income to 48.7% in high-income countries, a slope of 7.23 percentage points per log point of GDP per capita. This delegation divide is compositional: the physical barrier dominates the jobs poorer countries employ most. Second, at the occupation level ADI tracks exposure closely (r = 0.93 with Eloundou et al. and 0.89 with Felten et al.), above the preregistered bound of 0.80; ADI adds delegation levels and barriers on top of exposure, for the world, not a new ranking of occupations. Third, full delegation is rare and peaks for tasks that take a human about twelve minutes (11.8 minutes). Fourth, the preregistered adoption gap is not supported: across 101 countries, delegability and observed AI usage correlate at r = 0.86, and the gap between them is not wider in middle-income countries (p = 0.27). Model agreement is kappa = 0.77; a blind human rating of 300 tasks agrees with the model consensus at kappa = 0.85, and an agentic panel with web search at kappa = 0.87. We release the index, the atlas, the prompts and an MCP server at https://github.com/Cespial/delegation-divide.

</details>


### 65. UniGuard: Multi-View Guardrail Learning for Cross-Interface Safety Generalization

- **Authors:** Viet-Thanh Pham, Thuy-Trang Vu, Junae Kim, Rollin Omari, Dinh Phung, Gholamreza Haffari, Lizhen Qu
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30742v1](http://arxiv.org/abs/2610.30742v1)
- **PDF:** [https://arxiv.org/pdf/2610.30742v1](https://arxiv.org/pdf/2610.30742v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Guardrail models are increasingly used as safety layers for LLMs and agentic systems, but most are trained on fixed prompt or response interfaces and become unreliable when the same safety case appears as a conversation, agent trajectory, multi-agent trace, or policy-conditioned input. We propose UniGuard, a training framework that learns interface-invariant safety representations from multiple semantically aligned views of the same safety case. We also construct the UniGuard-FT dataset by transforming 1,000 public safety cases into prompt, response, multi-turn conversation, agent-trace, and multi-agent-trace views, and train UniGuard-0.6B with classification, supervised contrastive learning, and asymmetric confidence calibration losses. Across unseen-interface benchmarks ATBench, PolicyGuardBench, and DynaBench, UniGuard-0.6B improves over its pretrained guardrail by 45.12 F1 points on average and reduces expected calibration error by 35.41 points, while remaining competitive with much larger guardrails such as Claude-Sonnet-4.5 and GPT-5.2 - despite being a 0.6B model and trained only with synthetic data.

</details>


### 66. AgentTriage: Replayable Security Diagnosis Across Heterogeneous Agent Runtimes

- **Authors:** Jie Ying, Xutao Zhang, Ningyuan Chen, Mengce Zheng, Jun Li, Zhongjie Zhu, Tiantian Zhu
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30738v1](http://arxiv.org/abs/2610.30738v1)
- **PDF:** [https://arxiv.org/pdf/2610.30738v1](https://arxiv.org/pdf/2610.30738v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

When tool-use agents write files, execute code, or send data, their final responses do not explain the resulting security events, and heterogeneous runtimes expose the relevant evidence through incompatible interfaces. We present AgentTriage, an executable contract for replayable security diagnosis across heterogeneous runtimes. The contract admits conclusions whose claims cite canonical runtime events and requires abstention when mandatory evidence is missing. Runtime overlays normalize native observations, while a deterministic pipeline joins invocation and result lifecycles, constructs a typed provenance graph, selects a policy-decisive slice, and binds claims to recorded evidence. Given the same normalized trace, overlay version, and pre-run policy oracle, the diagnosis can be recomputed and its claims re-checked without language-model judgment. Across five runtimes, one contract captures all 159 applicable executions, with an audit of native and synthesized identifiers. On 120 adjudicated cases, AgentTriage achieves 0.858 grounded joint diagnosis, 0.966 required-evidence coverage, and a 0.036 unsupported-claim rate, improving joint diagnosis by 0.175 (95% CI [0.092, 0.258]) over the strongest same-schema baseline. These results quantify the precision of replayable diagnosis and the observation boundaries that require abstention. We release an open-source implementation and selected sanitized evidence at https://github.com/AsnGs/agenttriage-open-source.

</details>


### 67. Governance-State Corruption in Long-Term Memory for LLM Agents: A Cross-Model Stress Test

- **Authors:** Bowen Liu, Youting Wang, Bonan Shen, Dingyan Shang
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30698v1](http://arxiv.org/abs/2610.30698v1)
- **PDF:** [https://arxiv.org/pdf/2610.30698v1](https://arxiv.org/pdf/2610.30698v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

An LLM agent can retrieve a memory correctly yet use it incorrectly after its validity state changes. We study governance-state corruption: faults that alter which retained records enter model-visible context while stored content and tasks remain fixed. Across six providers, 731 benchmark-grounded bases yield 2,080 matched fault pairs. In offline control-plane checks, corruption changes the operative projection in 96.25% of pairs, while oracle-backed enforcement restores it in 100%. For downstream evaluation, a deterministically selected, non-probability LongMemEval/Memora panel resolves 298 of 300 matched triplets (238 distinct bases). Clean-minus-corrupted contrasts are 40.54 percentage points in LongMemEval binary correctness (95% base-cluster interval [30.32, 50.71]) and 30.60 points in rescaled Memora FAMA ([23.31, 37.69]); both sources also show recovery. OAKS Novel native option parity holds for all 6,714 resolved outputs. Full-cohort frozen-scorer corruption/recovery effects (-27.55/+27.51 points) remain descriptive proxies, not validated native semantic population effects. These bounded findings motivate evaluating memory control-state integrity alongside retrieval accuracy.

</details>


### 68. A Topology-Guided GeoAI Agentic Framework for Urban Flood Screening

- **Authors:** Yutian Tao, Haoan Feng, Xin Xu, Leila De Floriani
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30660v1](http://arxiv.org/abs/2610.30660v1)
- **PDF:** [https://arxiv.org/pdf/2610.30660v1](https://arxiv.org/pdf/2610.30660v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Open-world geographic artificial intelligence (GeoAI) agents can transform public geospatial data into accessible decision support for real-world challenges, but must balance autonomous reasoning with reliable spatial analysis and human oversight. We present a topology-guided GeoAI agentic framework for urban flood screening that takes a place name, drawn region, or uploaded boundary and returns ranked candidate basins with an interactive map and report. A deterministic controller retrieves public elevation, rainfall, soil, land-cover, exposure, and infrastructure layers, extracts terrain depressions with discrete Morse theory, and ranks basins with a relative flood-priority score. The language model acts only at recorded decision points: selecting a persistence threshold from a precomputed candidate table, drafting recommendations from computed evidence, and reviewing each recommendation against the same evidence. Three human-in-the-loop checkpoints let users revise the threshold, factor weights, or recommendation. In a College Park, Maryland case study, the selected threshold reduced 278 raw terrain minima to 70 basins, with 77% of these basins' lowest points also identified as sinks by a separately computed eight-direction (D8) flow-routing model. Across four further study areas, agreement ranged from 61% to 83%. By combining open data, explicit spatial reasoning, traceable evidence, and human oversight, the framework enables transparent first-pass flood screening while keeping consequential recommendations inspectable and user-controlled.

</details>


### 69. MBABench-2.0: Evaluating AI Agents on Constructing Financial Spreadsheets Beyond Simple Verifiability

- **Authors:** Julian Poeltl, Thomson Yen, Patrick Shea, Shubham Anil Varma, Dhruv Rastogi, Zihao Chen, Mengshi Zhang, Hongseok Namkoong
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31711v1](http://arxiv.org/abs/2610.31711v1)
- **PDF:** [https://arxiv.org/pdf/2610.31711v1](https://arxiv.org/pdf/2610.31711v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Spreadsheets are the lingua franca of modern finance, driving valuation, forecast, audit, and many other core workflows of the industry. As LLM agents advance to automate knowledge work, spreadsheet construction is a natural and pertinent testbed. However, most existing spreadsheet benchmarks evaluate agents on fill-in-the-blank style tasks, where an agent performs minor edits in otherwise complete spreadsheets. This protocol fails to capture the most central and time-consuming part of the spreadsheet workflow: the modeling decisions, format design, and sheet layout regular knowledge workers need to toil through to build a workbook from scratch. We introduce MBABench-2.0, a benchmark of 101 original spreadsheet construction tasks, the hardest of which is estimated to take 33 hours for a modeler with 3+ years of experience. Unlike coding or math, where a unit test or a final answer can verify an agent's output, the quality of a financial spreadsheet that concerns readability, maintainability, or auditability, is not so simply verifiable. To holistically evaluate spreadsheet construction, we introduce 129 criteria spanning 12 categories that operationalize quality beyond the accuracy of the spreadsheet. Evaluating over 20 agents across 8 models and 4 harness types, we find that frontier agents rarely construct spreadsheets that are both accurate and meet our quality criteria: the top agent achieves a pass rate of only 16% on the benchmark. The benchmark demonstrates a substantial gap in spreadsheet building capability of current agents.

</details>


### 70. Better Reasoning, Not Just Bigger Models: A Structure-Grounded Framework for Efficient and Reliable Inference

- **Authors:** Amirhossein Aghaei, Liangyan Li, Shiyi Yang, Shaohua Wang, Yan Wang
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30611v1](http://arxiv.org/abs/2610.30611v1)
- **PDF:** [https://arxiv.org/pdf/2610.30611v1](https://arxiv.org/pdf/2610.30611v1)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scaling large language models has substantially improved linguistic fluency, yet reliable autonomous agents require more than fluent generation. In multi-turn inference, current agentic systems often produce semantically plausible but structurally ungrounded reasoning, especially under incomplete observations. We propose Structure-Grounded Uncertainty Reduction (SGUR), a training-free framework that complements token-level generation with active uncertainty reduction over structured hypothesis spaces. SGUR represents incomplete observations as a query graph and aligns them with candidate hypothesis graphs through a prior-weighted partial graph matching mechanism, where database-derived empirical priors assign greater importance to decision-relevant relations rather than treating all graph edges uniformly. The resulting inference state is iteratively refined by an active information-gain strategy that selects the next most informative node to query, systematically pruning the candidate space. We instantiate SGUR on a challenging PrimeKG-derived sequential medical diagnosis benchmark, demonstrating that structural grounding can partially substitute for model scale: starting from only two observed symptoms, SGUR achieves 92.5% Hit@3, outperforming the strongest Graph-RAG baseline by 9.4 percentage points while using approximately 5x fewer tokens. Notably, SGUR enables smaller backbone models to match or exceed the performance of models up to 10x larger, suggesting that structural grounding provides a more robust and efficient paradigm for scaling agent performance than relying exclusively on increasing model size.

</details>


### 71. Lifetime-valid decisions by continually evolving AI analysts

- **Authors:** Xiaojing Sun, Yuhan Zeng, Xiao Wang
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30562v1](http://arxiv.org/abs/2610.30562v1)
- **PDF:** [https://arxiv.org/pdf/2610.30562v1](https://arxiv.org/pdf/2610.30562v1)
- **Categories:** stat.ME, cs.AI, cs.LG, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly act as analysts whose decision can often be cast as hypothesis tests. Classical tests control the Type I error rate, the probability of rejecting a true null hypothesis, for fixed procedures. However, AI analysts introduce internal randomness and can evolve continuously over time. As AI analysts evolve, the risk of approving versions with Type I error rates above the target can accumulate, and adaptive use of evaluation feedback can lead to overfitting. We introduce continual validation, which evaluates each proposed AI analyst version before deployment using simulated data under the null hypothesis, with scenarios that can be randomized and expanded over time. We prove that, regardless of how updates are chosen or how many are proposed, the lifetime probability of ever deploying a version whose Type I error rate exceeds the allowed level remains bounded. This guarantees that every subsequent decision controls the Type I error rate at the target level across these scenarios. At the same time, updates with sufficiently low Type I error rates pass validation with high probability, allowing the analyst to continuously improve its performance without sacrificing rigor. In two examples involving evolving AI analysts for bioequivalence studies and product A/B tests, Type I error rates reached 0.098 and 0.183 without continual validation, compared with at most 0.045 and 0.044 with it, while retaining 82% and 96% of the power from optimally selected valid updates.

</details>


### 72. Mining the Design Space of Multi-Agent Workflows

- **Authors:** Xavier Cadet, Junyan Cheng, Peter Chin, Kyle Richardson
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.31709v1](http://arxiv.org/abs/2610.31709v1)
- **PDF:** [https://arxiv.org/pdf/2610.31709v1](https://arxiv.org/pdf/2610.31709v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Designing large language model (LLM) multi-agent systems (MAS) still relies on trial and error and informal "folk wisdom." Manual studies test only a few communication structures or topologies (e.g., sequential, parallel, shared-memory, or debate), while automated optimizers discard search trajectories after selecting a task-specific workflow. We present a two-phase pipeline for mining reproducible design principles from workflow code and execution traces. We repurpose AFlow's MCTS optimizer across six composable operators and 26 deterministically verified Enigmata tasks, retaining all intermediate rounds to build a corpus of 28,568 executable workflows. A sandboxed AutoResearch loop then mines orchestration code and prompt templates under an $L_0$-penalized validation objective and tests candidate principles on held-out searches. Across 300 feature-mining trials, we identify effects that persist on held-out searches across three levels of workflow design: workflows beginning with independent solvers and one-shot aggregation (Star-first) perform worse ($Δ= -0.045$); persistent shared documents (SharedMemory) outperform debate ($Δ= +0.135$); and prompt specificity and placeholder-based context routing yield gains comparable to communication-structure selection ($Δ= +0.118$). More broadly, our pipeline and results show the feasibility of turning discarded search trajectories into a statistical testbed for discovering and validating multi-agent workflow design principles.

</details>


### 73. Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core

- **Authors:** Yebo Feng, Jingyang Dai, Liangrui Pan, Nelson Lau, Jiahua Xu, Yang Liu
- **Published:** 2026-10-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30557v1](http://arxiv.org/abs/2610.30557v1)
- **PDF:** [https://arxiv.org/pdf/2610.30557v1](https://arxiv.org/pdf/2610.30557v1)
- **Categories:** cs.AI, cs.CL, cs.MA, q-fin.PM


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents that act on live Web data must combine heterogeneous evidence, remember what they have done and improve from outcomes without weakening their own safeguards. We study this problem in autonomous investing, where every action is irreversible and based on untrusted Web content. We present Steward, a multi-agent LLM system that draws the boundary of self-evolution in its type system. First, nine role-specialised agents decide jointly: four analysts read news feeds, SEC filings, macroeconomic series and market data and emit typed reports, from which a Portfolio Manager sets target positions that a protected Risk Manager audits. Second, a seven-layer shared memory, assembled by code from the system's own record, gives each decision its position context, the market narrative, calibration and the agent's past decisions. Third, the system improves itself by review: code grades every trade and forecast nightly and writes the grades into memory, and each quarter a reflector proposes prompt learnings that a deterministic gate applies reversibly and replay of recorded inputs verifies. All three operate around an invariant core of order arithmetic, risk rules and discipline-agent prompts that no self-edit can reach. In a five-month live deployment (102 trading days, 1,632 LLM calls), the system contained a 24.6% sector drawdown to a 0.3% loss; in replay of its recorded inputs, a single model given the same raw data traded more and lost 1.35 points against the market over five days where the joint design showed no significant loss, and no injected instruction was followed; and a 2015-2026 backtest shows the core alone lowering the maximum drawdown under all 50 random entry policies. The reflector traced the dominant failure to its root cause, and the gate applied a learning that the agent adopted on trigger evenings and on no control evening. Code: https://github.com/yebof/quant-agent

</details>


### 74. IFC-MCQ: Automatically Generating Multiple-Choice Benchmarks for Evaluating LLM Agents on IFC Data Retrieval

- **Authors:** Rabindra Lamsal, Sisi Zlatanova, Xuesong Shen
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30533v1](http://arxiv.org/abs/2610.30533v1)
- **PDF:** [https://arxiv.org/pdf/2610.30533v1](https://arxiv.org/pdf/2610.30533v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Industry Foundation Classes (IFC), the standard for building information exchange in architecture, engineering, and construction (AEC), is increasingly queried through large language models (LLMs) using natural language. Evaluating these systems at scale is difficult because free-text answers require costly human or LLM-based review. We propose IFC-MCQ, a method that automatically generates multiple-choice benchmarks from IFC files for exact option-set grading. The taxonomy covers 15 categories and 36 subtypes across four groups, with answer keys derived from the file and distractors constructed from file-derived values or predefined rules. We applied IFC-MCQ to IFC models of varying sizes and modelling characteristics to assess generation coverage and evaluated two agentic configurations on selected models using tool- and code-based retrieval. The evaluation exposed category-specific failure modes and showed that performance can vary with the source IFC model and retrieval interface. IFC-MCQ enables scalable benchmarking of LLM-based IFC retrieval in AEC workflows.

</details>


### 75. From Prose to Properties: Testing Research Claims with ARATest for Agent-Native Science

- **Authors:** Yifeng He, Jiachen Liu, Hao Chen
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30495v1](http://arxiv.org/abs/2610.30495v1)
- **PDF:** [https://arxiv.org/pdf/2610.30495v1](https://arxiv.org/pdf/2610.30495v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents now run experiments and report findings, so research produces claims faster than researchers can check them. Each empirical claim implies a property that must hold over its cases, but it states that property only in prose. Without an explicit property, no test can decide which evidence would falsify a claim, so validation cannot keep pace with the claims agents produce. To make claims testable, we approximate a claim's semantics by abstracting its property skeleton, a parameterized relation that recurs across claims. We present ARATest, a property-based testing library that checks these skeletons as executable tests. A typed declaration binds a claim to a skeleton and fixes the claim's compared quantities, cases, scope, and numerical policy. A shared case type makes every generator supply cases in the claim's statistical unit. A three-valued semantics assigns each property one of three verdicts: holds, violated, or inconclusive. Every violation carries a replayable witness. A default generator reads the evidence that agent-native research artifacts (ARA) link to each claim, and auto-research generators dispatch an agent to run released code for fresh cases. Our DissClaimer plugin supplies that agent and runs these generators as continuous testing.
  Of 243 claims in 33 ARA artifacts, 54 received faithful declarations bound to evidence: 32 held, eight were violated, and 14 remained inconclusive. Two violations exposed errors in published papers that their authors confirmed. ARATest detected all 553 seeded faults without a false alarm on 19 valid controls, outperforming two LLM judges. Fresh runs exposed behaviors that reported evidence could not show. These results suggest that one fixed test can check explicit claim properties against both reported and fresh evidence.

</details>


### 76. What the Trace Shows and What the Label Says: Auditing Behavioral Detectors in Agent Evaluation

- **Authors:** Idunnuoluwa A. Adeniji,  Shilpika, Michael E. Papka
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30491v1](http://arxiv.org/abs/2610.30491v1)
- **PDF:** [https://arxiv.org/pdf/2610.30491v1](https://arxiv.org/pdf/2610.30491v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are often evaluated by reducing execution traces to labels such as final-answer correctness, tool verification, and fault propagation. These labels are measurements produced by parsers, behavioral detectors, and harness rules, and they may not fully capture what the trace shows. We study this in a tool-use setting built on GSM8K, where agents call a calculator whose outputs are occasionally corrupted, giving clear ground truth for what the tool returned, what the model later used, and what the detectors reported. We audit three trace-level detectors across six production models and 30 problems per model. Final correctness, visible re-verification, and fault propagation can disagree in systematic ways. A key failure mode is silent tool-output override: the calculator returns a corrupted value, but the model later uses a different, often correct, value without calling the tool again, so the bad value stops propagating while a verification detector records no re-check. Human review of 90 traces agrees perfectly with the automated labels for final correctness (67/67), fault impact (19/19), and fault relevance (18/18), but only 67/81 for verification; all 14 disagreements fall into four recurring patterns. Execution limits also change the reported result: in an ablation across two models, one ranges from 21/30 to 27/30 correct as step and token budgets change, while the other stays between 27/30 and 29/30. These findings motivate measurement transparency: an automated label should come with the trace evidence behind it, whether the question the detector asks applied to that trace, whether the run was cut off by an execution limit, and any human corrections. Our trace viewer makes this information inspectable alongside the reported results.

</details>


### 77. Learning to Incentivise: Using Reinforcement Learning for Sustainable Urban Mobility

- **Authors:** Germán Pardo-González, Shaghayegh Vosough, Katerina Papadaki, Claudio Roncoli
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30469v1](http://arxiv.org/abs/2610.30469v1)
- **PDF:** [https://arxiv.org/pdf/2610.30469v1](https://arxiv.org/pdf/2610.30469v1)
- **Categories:** cs.MA, cs.LG, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Traffic management has traditionally focused on toll-based and road pricing solutions. However, road pricing often raises concerns about accessibility and public dissatisfaction, leading to its prohibition in some places, such as Finland. This study optimises the dynamic allocation of incentives to drivers, encouraging them to reroute onto alternative (potentially longer) paths to achieve greater societal benefit, reduced total travel time (TTT) and total emissions in the transportation network, contributing to sustainable urban mobility. We employ a multi-agent reinforcement learning approach to dynamically assign incentives to drivers to reduce both TTT and emissions, with travel times estimated using traffic simulation software. We demonstrate that, with an unlimited budget and an objective of minimising travel time, the incentive scheme reduces TTT by 16%, compared to the dynamic User-Equilibrium (UE) with a budget equivalent to about 11% of the UE total time. When the goal is to minimise emissions, a 9% reduction in CO2 emissions is observed under an unlimited budget. We demonstrate a critical trade-off: minimising TTT leads to an increase in emissions, while prioritising emission reductions raises TTT. However, with the right combination of weights in the multi-objective function, both TTT and total emissions are improved beyond the baseline.

</details>


### 78. A Three-Pillar Governance Framework for Safe and Trustworthy AI Agents

- **Authors:** Edward C. Cheng, Jeshua Cheng, Alice Siu
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30445v1](http://arxiv.org/abs/2610.30445v1)
- **PDF:** [https://arxiv.org/pdf/2610.30445v1](https://arxiv.org/pdf/2610.30445v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents capable of autonomous decision-making introduce significant challenges related to safety, alignment, accountability, and human oversight. Existing Human-in-the-Loop (HITL) and responsible AI approaches provide important foundations, but many remain fragmented across system design, governance, and operational deployment. This paper presents a Three-Pillar (3P) model and framework for developing safe and trustworthy AI agents through transparency, accountability, and trustworthiness. The framework defines an evolutionary path in which increasing agent autonomy is introduced through progressive validation, structured human oversight, and auditable operational controls. We further describe how the model supports agent lifecycle monitoring, decision traceability, escalation management, and human-agent collaboration within enterprise agentic environments. By integrating oversight principles with operational mechanisms, the proposed framework provides a practical foundation for deploying AI agents that remain aligned with human intent while enabling controlled progression toward higher autonomy.

</details>


### 79. SpecMAGIC: Specification-Guided Multi-Task Generalization in Multi-Agent Reinforcement Learning

- **Authors:** Zijian Guo, İlker Işık, H. M. Sabbir Ahmad, Wenchao Li
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30443v1](http://arxiv.org/abs/2610.30443v1)
- **PDF:** [https://arxiv.org/pdf/2610.30443v1](https://arxiv.org/pdf/2610.30443v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-task generalization is an important yet underexplored problem in multi-agent reinforcement learning (MARL). Many real-world applications require multi-agent systems to generalize across complex, temporally extended tasks with diverse inter-agent coordination requirements. We introduce a specification language that combines temporal-logic task specifications with operators for expressing such requirements. We propose SpecMAGIC, a hierarchical framework that leverages the automaton structure of task specifications for subtask decomposition. A centralized high-level planner identifies and allocates compatible subtask sequences across agents, while decentralized low-level policies execute individual subtasks. This enables zero-shot generalization to new tasks by composing reusable subtask policies according to new specifications, without retraining. We establish soundness and probabilistic completeness of the high-level planner. Experiments on multi-agent navigation tasks show that SpecMAGIC substantially outperforms existing approaches on unseen task specifications and maintains strong performance as the number of agents increases.

</details>


### 80. Secure Agentic AI and Multimodal Intelligence in 6G Communication Systems

- **Authors:** Satyam Gaba, Devanshu Motwani, Siva Sai, Vineet Suri, Vikas Ranjan, Vinay Chamola
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30436v1](http://arxiv.org/abs/2610.30436v1)
- **PDF:** [https://arxiv.org/pdf/2610.30436v1](https://arxiv.org/pdf/2610.30436v1)
- **Categories:** cs.AI, eess.SP


> Summary unavailable.


<details>
<summary>Abstract</summary>

Sixth-generation (6G) communication systems are expected to support immersive, intent-driven, and latency-critical services through tight integration of multimodal intelligence, edge computing, and autonomous network control. In this setting, agentic AI systems can reason over heterogeneous inputs, use tools and network functions, coordinate across distributed entities, and adapt to dynamic environments. These capabilities make agentic multimodal intelligence promising for 6G applications such as semantic communications, digital twins, and zero-touch network management, but they also introduce security and privacy risks that extend beyond conventional AI and network security models. Vulnerabilities can propagate across multimodal data pipelines, memory, tools, communication interfaces, and inter-agent coordination loops. We survey multimodal intelligence and agentic AI for 6G cross-layered communication systems from the perspectives of privacy and security. We present a 6G-oriented system view spanning perception, memory, tool use, and multi-agent orchestration; analyze threat models and attack surfaces across sensing, cognition, action, memory, and communication layers; organize existing attacks into a structured taxonomy; and review mitigation strategies including prompt and memory defenses, inter-agent trust mechanisms, secure orchestration, and privacy-preserving learning. We conclude by outlining open research directions for trustworthy multimodal multi-agent 6G systems.

</details>


### 81. Self-Assessment Reinforcement Learning for Search-State Awareness in Retrieval-Augmented Large Language Models

- **Authors:** Taewhoo Lee, Minju Song, Jungwoo Park, Chanwoong Yoon, Junha Jung, Hyeon Hwang, Sanghoon Lee, Minbyul Jeong, Jaewoo Kang
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30435v1](http://arxiv.org/abs/2610.30435v1)
- **PDF:** [https://arxiv.org/pdf/2610.30435v1](https://arxiv.org/pdf/2610.30435v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in search agents have enabled large language models to tackle complex tasks by retrieving and synthesizing external information. However, existing search agents often lack search-state awareness, i.e., the ability to recognize what information has been obtained and what remains missing, leading to hallucinated reasoning and prematurely terminated search. To address this limitation, we propose Self-Assessment Reinforcement Learning (SARL), a reinforcement learning framework in which models learn to recognize their own search state during training and improve their search behavior accordingly, without requiring additional assessment at test time. SARL achieves this through a dual reward design that captures the corrective effect of each assessment while penalizing excessive reliance on it, jointly encouraging effective and efficient search trajectories. Under this setup, SARL achieves a 24.3% relative improvement over the strongest baseline, with average gains of 35.9% on multi-hop reasoning and 27.9% on deep research benchmarks against the strongest per-benchmark baselines. SARL further surpasses methods built on auxiliary supervision or multi-agent coordination, despite operating as a standalone RL framework with no inference-time scaffolding. Beyond final performance, SARL maintains training stability under extended search horizons, a regime where existing methods consistently degrade, enabling sustained gains as task complexity grows.

</details>


### 82. RoleFlow: Self-Evolving Multi-Role Agentic Collaboration via Structural Adaptation

- **Authors:** Yi Ge, Pan Wang, Xuehao Cui, Zian Zeng, Xu Hu, Heng Huang, Furong Huang
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30429v1](http://arxiv.org/abs/2610.30429v1)
- **PDF:** [https://arxiv.org/pdf/2610.30429v1](https://arxiv.org/pdf/2610.30429v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) based multi-agent systems often rely on predefined collaboration structures, limiting their adaptability to evolving task requirements. Although recent approaches enable dynamic orchestration, trajectory-level rewards they apply assign one outcome to each decision, ofen struggling to identify the contributions of individual structural changes. We propose RoleFlow, a self-evolving multi-role agentic system that refines collaboration structures through feedback-driven atomic edits and on-demand role synthesis. To make structural adaptation learnable, we introduce Single-Edit Counterfactual Policy Optimization (SECPO), which evaluates each edit against its no-edit counterpart at the same chain state and assigns targeted credit to edit-specific tokens. Across seven benchmarks spanning four domains, RoleFlow achieves the optimal average performance, surpassing the strongest competitor by 4.7 points. It leads on all three multi-hop QA benchmarks by 3.2-7.5 F1 points and also shows supremacy on mathematical reasoning, web interaction, and code generation. Further analyses demonstrate cross-benchmark transferability, training-data efficiency, and cross-executor generalization.

</details>


### 83. Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems

- **Authors:** Daniel Ruiz, Luca Luceri, Emilio Ferrara
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30418v1](http://arxiv.org/abs/2610.30418v1)
- **PDF:** [https://arxiv.org/pdf/2610.30418v1](https://arxiv.org/pdf/2610.30418v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern LLM agents can retrieve information from accessible documents, and then disclose a sensitive conclusion assembled from them. This mosaic effect creates a critical risk for agents operating over confidential data. We quantify its realization with 30 synthetic cybersecurity, medical, and military examples, yielding 10,800 final answers from three LLM agents in controlled simulation and 1,440 answers from live agents in two open-source harnesses. Even under benign queries designed to be answerable from one document, GPT-5.6-Sol, the best performing model tested, discloses forbidden composites in 7.08% of answers (95% CI: 3.75-10.67%) in simulation, with worse disclosure rates in live harnesses. Adding visible classification headers and explicit aggregation rules reduces pooled disclosure rates substantially, yet unsafe disclosures persist in 32.37% of simulated answers (95% CI: 28.33-36.19%) across all intents despite these safeguards. Furthermore, increased refusals do not guarantee confidentiality, since significant refusals reveal the prohibited conclusion regardless. These results point to a troubling conclusion: sensitive data leaks via mosaic-style events are an observed confidentiality failure mode in the evaluated settings at non-negligible rates. They motivate stronger controls on what agents may infer and disclose in sensitive data environments with mixed-clearance users.

</details>


### 84. A Transformer-based Approach for Real-time Multi-agent Path Planning with Varying Initial/Final Conditions

- **Authors:** Qian Zhang, Shanqing Liu, Jerome Darbon, George Karniadakis
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30388v1](http://arxiv.org/abs/2610.30388v1)
- **PDF:** [https://arxiv.org/pdf/2610.30388v1](https://arxiv.org/pdf/2610.30388v1)
- **Categories:** math.OC, cs.LG, math.NA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We address the problem of real-time multi-agent path planning under prescribed initial and final configurations, formulated as a high-dimensional optimal control problem subject to inter-agent collision avoidance and obstacle constraints. Classical solvers based on the Hamilton--Jacobi--Bellman equation or Pontryagin's maximum principle (PMP) become computationally intractable as the number of agents grows, due to the curse of dimensionality and the non-convexity introduced by interaction constraints. We propose OCFormer, a transformer-based neural network that parameterizes the inverse of a coordinate transformation mapping a simple, analytically tractable latent space, in which agents evolve independently under a decoupled Hamiltonian, to the physical space of the coupled, interacting system. The model is trained by minimizing a physics-informed loss comprising the Hamiltonian ODE residual from the PMP and a boundary matching term, without requiring pre-computed trajectory data. The self-attention mechanism endows OCFormer with permutation equivariance over agents, a structural symmetry that prior symplectic network approaches do not natively enforce. When trained on a distribution of boundary conditions, the amortized OCFormer produces near-optimal trajectories for unseen initial and final configurations in a single forward pass ($\sim$220ms), enabling real-time inference without retraining. We further introduce a lightweight transfer learning framework that adapts a pretrained OCFormer to out-of-distribution perturbations in seconds via L-BFGS fine-tuning. Numerical experiments on two- and three-dimensional multi-agent navigation with up to 128 agents demonstrate the scalability and efficiency of the proposed approach.

</details>


### 85. MemPlan: Memory-Conditioned PDDL Planning for Partially Observable Text Environments

- **Authors:** Tengwei Song, Robert Hoehndorf
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30379v1](http://arxiv.org/abs/2610.30379v1)
- **PDF:** [https://arxiv.org/pdf/2610.30379v1](https://arxiv.org/pdf/2610.30379v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are flexible in language interaction, but using them as long-horizon planners is costly and prone to hallucinated or invalid actions. This paper targets a different role for LLMs: constrained bridges between language and symbolic planning. We propose MemPlan, a memory-conditioned PDDL planning framework for partially observable interactive text environments. MemPlan keeps the PDDL domain fixed and reconstructs the PDDL problem at each step from parsed observations, candidate hypotheses, and interaction memory. Positive graph memory assigns relevance-based action costs to candidate hypotheses for missing objects, locations, or conditions, guiding the planner toward more plausible checks. Negative memory records execution-refuted assumptions and compiles them into exclusion constraints, preventing repeated attempts at candidates already contradicted by feedback. A unified schema-conditioned language--symbol interface, trained offline with supervised fine-tuning, connects text environments to the planning loop through observation-to-fact parsing and symbolic-action-to-command grounding. Experiments on TextWorld, ALFWorld, and Robotouille show that MemPlan improves task completion and step efficiency over language-only and PDDL-aware baselines, while substantially reducing online token cost compared with LLM-planning baselines such as ReAct. The same fine-tuned interface is also reused across TextWorld task types without task-specific fine-tuning. Our code and data are available at: https://github.com/tewiSong/MemPlan.

</details>


### 86. Breaking the high-degree barrier in Lehmer's problem with a human-AI discovery loop

- **Authors:** Yuri Chervonyi, Sergei Gukov, Thang Luong
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30277v1](http://arxiv.org/abs/2610.30277v1)
- **PDF:** [https://arxiv.org/pdf/2610.30277v1](https://arxiv.org/pdf/2610.30277v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

While artificial intelligence has made rapid progress in mathematical reasoning, many open problems depend on structure that is revealed only through large-scale computational exploration and analytical synthesis. One such example is Lehmer's problem from 1933. It asks whether the Mahler measure of an integer polynomial, which measures how far its roots stray from the unit circle, can be made arbitrarily small. Previously, constructing irreducible polynomials with integer coefficients and small Mahler measure has been carried out systematically only for even degrees $d \le 180$. At higher degrees, Boyd's analytical one-parameter family frequently factors, skipping nearly 50% of target degrees and leaving no general construction for arbitrary $d$. Here, we address the high-degree regime through a human-AI discovery loop, in which we extend the conversational prompting with a fast numerical pipeline, an exact symbolic verifier, and large-scale distributed search. The AI agent prototypes numerical and symbolic solvers locally, launches parallel searches across distributed clusters and works with the human researcher to extract and verify mathematical hypotheses. Through this interactive loop, we derive a five-parameter construction, which we call the Generalized Boyd algorithm. It eliminates degree-skipping and constructs irreducible polynomials with Mahler measure strictly below Boyd's limit point $α_1 \approx 1.255434$ for every target degree. Evaluated across all even degrees up to 2000, our approach improves upon six previously published values and holds 99.6% of all best known records. With this work we release the verified dataset of polynomials with minimal Mahler measure across all studied even degrees.

</details>


### 87. Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research

- **Authors:** Houde Qian, Zheng Jiang, Wenyi Li, Chenxi Xu, Xinjie Lin, Yuzhao Peng, Ruoyu Han, Youjie Zheng, Kaisen Yang, Qinhuai Na, You Fu, Calvin Xiao
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30113v1](http://arxiv.org/abs/2610.30113v1)
- **PDF:** [https://arxiv.org/pdf/2610.30113v1](https://arxiv.org/pdf/2610.30113v1)
- **Categories:** cs.CL, cs.AI, cs.CE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether large language models (LLMs) can complete this loop and produce strategies that work beyond the research period. We introduce Quant-Arena, a benchmark and public leaderboard for end-to-end quantitative research on real A-share market data. A model constructs features and stock-scoring code, receives feedback only on 2022--2023, and freezes one strategy for assessment on the sealed year 2024. A cash-account evaluator applies trading constraints and costs, including market impact estimated from a simulated order book. Scores are dominated by realized excess return and complemented by signal quality and the diversity of features used by the strategy. We evaluate nine frontier models, among which GPT-6 Astra scores highest; yet no model beats the equal-weight market in 2024. Quant-Arena is open to submissions from any model or agent harness.

</details>


### 88. Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting

- **Authors:** Nurul Labib Sayeedi, Md. Faiyaz Abdullah Sayeedi, Zabir Al Nazi, Mahbub E Sobhani, Shubhashis Roy Dipta
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30103v1](http://arxiv.org/abs/2610.30103v1)
- **PDF:** [https://arxiv.org/pdf/2610.30103v1](https://arxiv.org/pdf/2610.30103v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Many NP-complete (NPC) problems have a polynomial-time (P) twin that differs in a single structural detail, such as 3- versus 2-colouring a graph. A model that reasons rather than recalls should notice which side of this boundary a problem falls on, yet existing benchmarks either fix the wording of each task or ignore its complexity class, so they cannot separate the two. We introduce P2NPCBench, a benchmark of 12 problem families in which every NPC problem is paired with a P twin posed over the same surface. To remove the textbook cues that enable recall, we build it with AgentGAN, an adversarial multi-agent framework in which a generator rewrites each statement until a panel of frozen code models fails, while an executable validity gate keeps every rewrite answer- and class-preserving. The result is 2,114 hardened statements with hand-verified reference human solvers. Evaluating 12 proprietary and open-source models, we find that every model scores lower on NPC statements than on their P twins (35.4% vs. 63.8% pass@1), and that 95.1% of model-family pairs fail more often on the NPC side. A tenfold time limit raises NPC accuracy only from 28.5% to 31.9%, so failures stem from wrong or crashing programs rather than slow ones. Hardening also narrows the class gap from 24.8 to 14.6 points, showing that part of the apparent gap reflects familiarity with textbook phrasing rather than complexity class.

</details>


### 89. Parallel AI Agent Collaboration as Graph-Structured Distributed Block Optimization

- **Authors:** Hanmin Li, Yury Demidovich, Peter Richtárik
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30074v1](http://arxiv.org/abs/2610.30074v1)
- **PDF:** [https://arxiv.org/pdf/2610.30074v1](https://arxiv.org/pdf/2610.30074v1)
- **Categories:** cs.MA, cs.AI, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Parallel AI agents can produce useful local edits yet degrade a shared solution when their edits are combined. We model this coordination problem as discrete block optimization with an exactly evaluable objective and a known dependency graph. Independent sets certify compatible edits whose verified gains, measured against the same current solution, add exactly. A coordinator constructs a safe compatible candidate and can also evaluate interacting edits to capture favorable interactions. We prove that an optimal fractional coloring yields a merger that preserves a $1/χ_f(G)$ fraction of the total verified local improvement, where $χ_f(G)$ is the graph's fractional chromatic number. This guarantee is tight among mergers that select a subset of the same proposals. Under conditional local-improvement guarantees and a block error-bound condition, repeated collaboration converges geometrically in the objective gap. The rate separates task structure, agent allocation, and computation cost, yielding a linear program for agent assignment and an explicit time-cost trade-off. Code-repair experiments show that verified merging resolves conflicts between individually useful edits that cause naive merging to fail. On larger conflict-free tasks, parallel agents reduce modeled completion time at higher input-token-equivalent cost. On three public road networks, fractional integration retains 922 units of verified graph-cut improvement across 90 paired runs. For route-search agents sharing exclusive access to vehicle routes, fractional scheduling reduces measured wall time by a median of 15% across twelve paired runs, with route-cost changes varying across runs.

</details>


### 90. GuideEvolve: Self-Evolving Agent Framework with Expert Guidance and 3Ts Mechanisms

- **Authors:** Meihong Jia, Yasemin Timar, Jonathan Taws
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30017v1](http://arxiv.org/abs/2610.30017v1)
- **PDF:** [https://arxiv.org/pdf/2610.30017v1](https://arxiv.org/pdf/2610.30017v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This study introduces GuideEvolve, a self-evolving agent framework incorporating expert guidance and three autonomous regulatory mechanisms, collectively termed the 3Ts: Think Fast and Slow, Throwback, and Termination by choice. The framework addresses critical limitations in extant self-evolving agent paradigms through dual innovations: (1) a task-specific expert-evaluation-driven evolutionary pipeline, and (2) the integration of 3Ts mechanisms to facilitate cognitive optimization, performance recovery via temporal rollback, and adaptive termination protocols. Empirical validation across the MGSM and MMLU benchmarks demonstrates that GuideEvolve attains performance metrics comparable to current state-of-the-art models (89.8% accuracy versus Gödel Agent's 90.6% on MGSM; 89.1% versus 87.9% on MMLU), while exhibiting notably reduced variance (25-59%) and enhanced robustness. Furthermore, the framework achieves a 100% evolution success rate, superior to the baseline's 82%, diminishes required optimization iterations by approximately 50% (from 30 iterations in baseline to 15.1 and 13.4 across tasks), and provides improved stability for production deployment.

</details>


### 91. Agent Behavior Maps: Locating Agents by What They Would Do, Without Running Them

- **Authors:** Shota Fujikawa, Takuya Tamura, Kosuke Akimoto, Daichi Haraguchi, Masafumi Oyamada
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30014v1](http://arxiv.org/abs/2610.30014v1)
- **PDF:** [https://arxiv.org/pdf/2610.30014v1](https://arxiv.org/pdf/2610.30014v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents with similar success rates can follow different action sequences. An Agent Behavior Map represents LLM-harness combinations using centered action log-likelihoods on shared reference trajectories, without requiring new environment rollouts from the target agent. We derive error bounds relating squared coordinate distances to trajectory KL under explicit assumptions, and across eight cross-scored models the distances track the directly measured trajectory KL in rank order. Across 100 LLMs and four environments, ALFWorld-based coordinates support performance prediction and identify behavioral similarities. In ALFWorld, these similarities persist after controlling for success rates and model size, including across model families. As an extension, harness-component displacements approximately compose, with accuracy varying across components and environments.

</details>


### 92. Agentic Architecture of Information Systems. The AAM/5C Model: A Reference Model for Distributed Autonomy

- **Authors:** Laurent Goujon
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30221v1](http://arxiv.org/abs/2610.30221v1)
- **PDF:** [https://arxiv.org/pdf/2610.30221v1](https://arxiv.org/pdf/2610.30221v1)
- **Categories:** cs.SE, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large organizations increasingly face what this book calls the cognitive complexity wall: at the scale of hundreds of interacting components, maintaining the dependency map and reacting at the pace of incidents exceeds what a human team can deliver. This conceptual volume proposes AAM/5C, in which five capabilities (Capture, Comprehend, Choose, Coordinate, Control) are instantiated across seven logical layers, L1 to L7. A single authorization rule, R-AUT, separates who proposes, who decides and who executes: a probabilistic planner (L4) proposes; a governance layer (L6) decides under signed policies and records its verdict in a signed evaluation proof; a security layer (L5) issues a short-lived act token bound to that proof; a policy enforcement point verifies both before the target layer materializes the act. Under an explicit guarantee contract, two analytical statements (H7a, H8a) hold by construction. The other statements of its ten hypotheses (H1 to H10), including log completeness (H7b) and non-bypass of the enforcement point (H8b), are refutable, and the protocol that could refute them is fixed before any measurement. The contribution of the book is a prescriptive reference model that articulates, under this single authorization rule, known mechanisms and adds three constructs, all to be validated: the Validation step of the Distributed Autonomy Loop, the ephemeral authority surface and the cognitive dependency plane. The book positions them against autonomic computing, multi-agent systems, enterprise architecture and agent protocols (MCP, A2A), gives an authorization policy in Rego and a partial TLA+ specification of peer consensus, and sets out a validation program with quantified milestones. It reports no empirical results. This English edition is a translation of the French original, produced with the assistance of AI tools and validated by the author.

</details>


### 93. ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination

- **Authors:** Nithin Sivakumaran, Ali Payani, Hyunji Lee, Mohit Bansal, Elias Stengel-Eskin
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29934v1](http://arxiv.org/abs/2610.29934v1)
- **PDF:** [https://arxiv.org/pdf/2610.29934v1](https://arxiv.org/pdf/2610.29934v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Forming an accurate theory-of-mind (ToM) is key to successful multi-agent collaboration and requires reasoning under uncertainty to capture multiple possible partner states. This is hard to do in the text representation space native to large language model (LLM) agents, which more easily describe a single partner state. To address this challenge, we introduce ToM2Vec, which learns to form abstract theories-of-mind in a rich latent space via a fixed budget of continuous reasoning tokens. During training, supervision for these tokens comes from the partner's actual thoughts, which the ToM tokens are trained to abstract and match. At test-time, ToM tokens are generated by each agent and act as conditioners for that agent's thoughts and actions. Across several environments covering collaborative, competitive, and mixed-motive settings (Overcooked-AI, multiparty negotiation, Decrypto, Hanabi, and Collab Escape/Capture), we evaluate ToM2Vec's ability to support multi-agent interactions and collaboration, finding consistent improvements over the base model and a variety of competitive trained and prompted baselines. We show that latent reasoning is critical, with performance dropping when reasoning is expressed in text. Moreover, we show that ToM2Vec training generalizes to partner model families not seen at train-time, including a proprietary model (GPT-5.4). In our analysis, we provide evidence that the latent tokens encode a ToM, rather than task-specific information: ToM2Vec's tokens improve the agent's ability to directly answer questions about partner beliefs, desires, and next actions.

</details>


### 94. FrontierCS 2: A Benchmark for Computer Science R&D

- **Authors:** Qiuyang Mang, Wenhao Chai, Runyuan He, Dongruixuan Li, Zihan Zheng, Yujun He, Xuanyi Zhou, Hao Wang, Siddhant Ray, Bo Peng, Ruyi Ji, Shuo Yang, Haocheng Xi, Boru Chen, Xinyang David Han, Melissa Pan, Mayank Mishra, Boxi Yu, Sijia Liu, Kerem Akillioglu, Yi Pan, Zirui Wang, Mert Cemri, Diogo Antunes, Yichuan Wang, Aiwei Ivy Zhang, Zhenyang Chen, Qizheng Zhang, Kaiyuan Liu, Wenyuan Huang, Sherry Ruan, Shu Liu, Dacheng Li, Zerui Cheng, Zeyu Shen, Shang Zhou, Hanfei Chen, Yuzhong Zhang, Bohan Lyu, Qu Ao, Han Zheng, Chonghe Jiang, Jingzhuo Hu, Xiaokun Chen, Kunjun Li, Zhiqing Zhong, Haoye Tian, Tong Zhao, Yunzhong He, Hanchen Li, Ofir Press, Jiantao Jiao, Kunle Olukotun, Karthik R. Narasimhan, Jingbo Shang, Koushik Sen, Matei Zaharia, Alex Dimakis, Ion Stoica, Joseph E. Gonzalez, Alvin Cheung
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29932v1](http://arxiv.org/abs/2610.29932v1)
- **PDF:** [https://arxiv.org/pdf/2610.29932v1](https://arxiv.org/pdf/2610.29932v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Can LLM agents make contributions to frontier computer science R&D? We introduce FrontierCS 2, a benchmark of 48 open-ended tasks. We take a paper and the code its authors released and delete the paper's contribution. The deleted code becomes the human reference that sets the bar. Earlier open-ended benchmarks give each agent a problem statement and grade one program after the run. FrontierCS 2 places the agent inside a research environment. The agent inherits a working repository and may submit a patch at any point. For each patch, a judge returns a development-suite score but keeps the evaluator, the held-out final suite and the reference private, and grades the final submission on that suite against the reference. The tasks span 13 domains, from machine-learning systems and high-performance computing to databases, security and robotics. Beyond these 48 tasks, FrontierCS 2 keeps a private set of more than 100 tasks, to be announced in the future. We evaluate 12 agents. The best one is Claude Opus 5.5, passing 58% of its runs. No run passes on 16 tasks. A higher score is not the same as a pass: most runs that beat the reference on the combined final score still fall short on some metric or workload. On a shared capability scale for agents and tasks, the median task is roughly as difficult as what the strongest agent can handle.

</details>


### 95. Feedback That Backfires in Games: Do LLM Players Repeat the Move They Just Watched Fail?

- **Authors:** Esmail Gumaan
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30205v1](http://arxiv.org/abs/2610.30205v1)
- **PDF:** [https://arxiv.org/pdf/2610.30205v1](https://arxiv.org/pdf/2610.30205v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When an LLM agent's move fails, the harness writes the move and the failure message into the transcript and asks again. In tool calling, this record makes small models more likely to repeat the failed action. We test whether the same holds in games (Sokoban, Connect Four, Othello), where a move can fail by being illegal or by being legal but losing, both verified exactly. On fixed probe items built by perturbing a correct move, the record backfires: pooled over 8 instruction-tuned models (135M-1.7B) it makes the failed move more likely (corrective gain G = -1.38 nats per token), through the move's surface form, for illegal moves but not for losing ones, and not for every model. An exploratory analysis shows what sets the sign: after the record, the failed move's log-probability barely depends on how likely it was before (slope 0.18). Moves the model would not have played become more likely, and greedy decoding starts to produce them; moves it was about to play become less likely, but greedy decoding still repeats 38% of them. A description of the failure that omits the move string keeps the model's preference instead. Along the OLMo 2 1B post-training ladder the inversion is present in the base model and largely removed at the DPO stage. RAGEN's default models invert in RAGEN's own Sokoban format before any RL. A "do not repeat" instruction does nothing, a clean retry is the worst harness, and a decoder ban stops exact repeats but not illegal play. All measurements ran in float32 on a free Colab GPU, which first reproduced the original paper's number.

</details>


### 96. The Reflexivity Threshold: A Phase Transition for Multi-Agent Performative Prediction

- **Authors:** Ahmed Mahrous, Roberto Di Pietro
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29577v1](http://arxiv.org/abs/2610.29577v1)
- **PDF:** [https://arxiv.org/pdf/2610.29577v1](https://arxiv.org/pdf/2610.29577v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Many learning systems are performative: once deployed, their predictions change the data distribution on which future models are trained. In multi-agent settings, this feedback is routed through a network of interacting learners, so stability depends not only on the strength of performativity but also on who affects whom. We study repeated retraining in multi-agent performative prediction and identify a spectral threshold that separates stable learning from worst-case learning obstruction. Prior work often collapses cross-agent feedback into a scalar contraction constant, missing this network structure. We instead introduce the reflexivity matrix $Γ$, which records how strongly one agent's deployment can move another agent's best response, defined from per-agent gradient sensitivities and curvature parameters. The threshold occurs when the spectral radius of this matrix crosses one. Below the threshold, repeated retraining converges geometrically to a unique performatively stable equilibrium, with cumulative excess loss bounded uniformly in the time horizon. Above the threshold, we construct noisy supercritical instances in which every local-information learner incurs expected cumulative excess loss growing linearly for horizons up to order $1/(ρ(Γ)-1)$. Together, these results characterize the threshold behavior through upper and lower bounds and recover the single-agent scalar threshold from prior work as a special case.

</details>


### 97. RegoMender: A Multi-agent Framework for Automated Rego Policy Repair

- **Authors:** Ruijie Zhang, Huaxiao Yin, Li Hu, Fanqi Kong, Haozhe Liang, Shaoyin Cheng, Kun Zhang, Bibo Tu
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29456v1](http://arxiv.org/abs/2610.29456v1)
- **PDF:** [https://arxiv.org/pdf/2610.29456v1](https://arxiv.org/pdf/2610.29456v1)
- **Categories:** cs.SE, cs.AI, cs.PL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Policy-as-Code (PaC) has emerged as a foundational paradigm in cloud-native systems. However, repairing Rego policies remains challenging due to their strict syntax, declarative semantics, and specific verification requirements. Existing automated program repair (APR) methods are mainly designed for mainstream languages and struggle to accommodate the unique policy logic and repair workflows of Rego. Thus, Rego policy repair remains a manual process driven by trial and error. To address this, we introduce RegoBench, the first automated Rego policy benchmark comprising 1,159 real-world defects, and propose RegoMender, a feedback-guided multi-agent framework. Collaborating via a shared blackboard and an atomic toolkit, RegoMender dynamically executes patching, rewriting, or rolling back, to resolve complex repair scenarios. Evaluated on RegoBench, RegoMender achieves syntactic and test-based semantic success rates of 82.9\% and 77.9\%, respectively, outperforming the strongest baseline by 13.4\%. Unlike other approaches whose performance drops in complex scenarios, RegoMender maintains effectiveness across single-step and chained repair tasks. Furthermore, it generalizes strongly across HCL and SQL and achieves an 86.4\% repair rate on 132 real-world CVE vulnerabilities, proving its robustness and practical utility for security.

</details>


### 98. One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon Agents

- **Authors:** Shaojin Ma, Ruitao Wang, Pengyi Li, Jie Yang, Liangyu Chen, Gangyi Zhao, Hongyao Tang, Yan Zheng, Jianye Hao
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29427v1](http://arxiv.org/abs/2610.29427v1)
- **PDF:** [https://arxiv.org/pdf/2610.29427v1](https://arxiv.org/pdf/2610.29427v1)
- **Categories:** cs.LG, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in multi-turn reinforcement learning (RL) have substantially improved the performance of LLM agents on complex, long-horizon interactive tasks. However, despite progress in fine-grained credit assignment, policy optimization still applies these learning signals through response-specific probability ratios. Different textual responses can induce the same executable effect, yet credit differences arising from subsequent outcomes remain tied to their individual textual realizations. We identify this mismatch as credit-update misalignment. Our analysis reveals that credit-text pairing directly shapes policy-update directions, even when the policy context and executable effect are held fixed. Motivated by this finding, we propose Effect-Marginal Policy Optimization (EMPO), which aligns policy optimization with execution-level equivalence through an effect-level surrogate that couples updates across alternative textual realizations. EMPO preserves the original credit signals, integrates with both trajectory-level and step-level credit estimators, and requires no additional critics or rollouts. Experiments on ALFWorld, WebShop, and Sokoban show that EMPO outperforms strong baselines in both task performance and learning efficiency.

</details>


### 99. Memory-Centric Continual Learning for AI Agents

- **Authors:** Dongfang Li, Zhuoen Chen, Bonian Jia, Zixuan Liu, Zhengxuan Lu, Can Deng, Yukun Shi, Yuhang Meng, Xin Zhang, Jiahe Huang, Fuhao Li, Junmai Wang, Shunyao Wen, Jingjun Sun, Jiaxu Tian, Jiangling Zhang, Zihan Wang, Liangyou Li, Yitong Yao, Shuangyong Song, Beilun Wang, Pengxu Wei, Hanlin Xu, Chang Liu, Yongxiang Li, Baotian Hu, Xiangyang Ji, Min Zhang
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29357v1](http://arxiv.org/abs/2610.29357v1)
- **PDF:** [https://arxiv.org/pdf/2610.29357v1](https://arxiv.org/pdf/2610.29357v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents powered by foundation models can reason, plan, and use tools, but their fixed weights and context limits hinder sustained learning from experience over long-term deployment. While external memory systems attempt to bridge this gap, they mostly act as passive retrieval caches, evaluated primarily by whether they can recall stored facts or past interactions. Whether memory can drive genuine continual learning remains an open question. In this paper, we introduce Memory-Centric Continual Learning (MCCL), arguing that memory should be judged by whether it improves future actions, not merely what it retrieves. MCCL has three main parts. First, a three-axis taxonomy organizes memory by where state is stored (substrates), what form it takes (assets), and how it is managed (policies). This defines a two-loop lifecycle that updates memory state in an inner loop while refining management policies in an outer loop based on task feedback. Second, an evaluation protocol measures retention under interference, adaptation to change, and task transfer to isolate genuine behavioral gains from simple context expansion. Third, a memory scaling framework models how agent performance scales with experience, storage capacity, and compute budgets across non-parametric and parametric memory. Together, these components reframe agent memory from passive lookup to continuous learning, offering a principled route toward self-improving autonomous agents.

</details>


### 100. Benchmarking and Error Analysis of Deep Search and Deep Research LLM Agents

- **Authors:** Zixuan Yu, Zhenheng Tang, Xiaowen Chu, Bo Han
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29346v1](http://arxiv.org/abs/2610.29346v1)
- **PDF:** [https://arxiv.org/pdf/2610.29346v1](https://arxiv.org/pdf/2610.29346v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As Large Language Models (LLMs) evolve into autonomous Deep Search and Deep Research Agents capable of executing long-horizon, multi-step tasks, evaluating their reliability becomes increasingly critical. However, existing evaluation paradigms predominantly focus on final task outcomes, leaving a significant gap in understanding the intermediate execution traces, where agents are highly susceptible to various errors. To address this critical gap, we introduce a comprehensive methodology and analytical framework designed specifically to diagnose errors in intermediate workflows. Building upon this framework, we establish a structured taxonomy that categorizes these vulnerabilities into two primary dimensions: System-Level Errors and Task-Level Errors. Through a systematic examination of step-by-step execution traces and agent-environment interactions, we reveal how these underlying errors affect overall performance. Finally, through empirical experiments and systematic analysis of the identified error types, we provide actionable design guidelines, aiming to enhance the robustness, reasoning capabilities, and reliability of Deep Search and Deep Research agents.

</details>


### 101. From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?

- **Authors:** Linus Filbry, Luckeciano C. Melo, Yarin Gal
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29331v1](http://arxiv.org/abs/2610.29331v1)
- **PDF:** [https://arxiv.org/pdf/2610.29331v1](https://arxiv.org/pdf/2610.29331v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly applied across the scientific discovery pipeline, from synthesizing literature to generating hypotheses to informing experimental design. A unifying principle behind these tasks is the need to continuously update beliefs as evidence accumulates, for which Bayesian inference provides a natural framework. However, existing work assumes that LLMs cannot carry out principled Bayesian belief updating in context, instead relying on simplifications and heuristics. To challenge this assumption, we present a principled evaluation of Bayesian reasoning capabilities in LLMs, analyzing both the model's internal consistency as well as its ability to recover an externally determined posterior. Specifically, we build an evaluation framework spanning qualitative epistemological examples to probe probabilistic coherence, quantitative benchmarks of Bayesian inference capabilities, and analyses of the impact of non-Bayesian updates on downstream task performance. Across different scenarios, we find that LLMs generally violate Bayes' rule when updating their beliefs in context. However, when equipped with modern reasoning abilities and code execution capabilities, their performance drastically improves, enabling even the close approximation of analytically intractable posteriors. Our evaluation shows that current LLMs with access to appropriate tools could already be used to make complex belief updates in scientific discovery, enabling rapid acceleration of the efficiency and scale of AI-powered scientific discovery.

</details>


### 102. AgentMonopoly: Behavioral Patterns and Persona Control in LLM Agents

- **Authors:** Changshun Wu, Mengyu Li, Mathis Marsault, Xiaowei Huang, Chih-Hong Cheng
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29330v2](http://arxiv.org/abs/2610.29330v2)
- **PDF:** [https://arxiv.org/pdf/2610.29330v2](https://arxiv.org/pdf/2610.29330v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

How do LLM agents' strategies differ, and how much can instructions to adopt a persona change their behavior over a game? We study these questions with AgentMonopoly, an environment where agents communicate, buy and trade properties, and make decisions that affect later turns. We compare models from four families, each at two sizes, in games with identical models, different sizes of the same family, or different families. We also assign one agent a persona, a description of how it should behave, intended to change a tendency observed in games without that persona. The tested models differ in how often they trade, waive rent, and manage cash and properties. Larger models do not consistently win more games. Persona instructions change the words agents use and some of their actions, but the changes do not always match the role across all decisions. These results show why persona following should be assessed through actions and outcomes as well as language. As our findings are conditional on the tested checkpoints, prompts, and five seeds per configuration, the open-source nature of AgentMonopoly provides the experimental infrastructure for further extending these comparisons. Our code is available at https://github.com/SuELS-Group/Agent_Monopoly.

</details>


### 103. Seeing the Forest for the Trees: Emergent Agreement from Individual Conversations

- **Authors:** Adi Simhi, Yaniv Nikankin, Jonathan Herzig, Idan Szpektor, Yonatan Belinkov, Shay B. Cohen
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29328v1](http://arxiv.org/abs/2610.29328v1)
- **PDF:** [https://arxiv.org/pdf/2610.29328v1](https://arxiv.org/pdf/2610.29328v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents interact in the wild and shape each other's decisions, understanding how they converge toward agreement becomes important. We study this in multi-turn conversations where two LLMs discuss subjective matters, can agree or disagree, and may change their stances. Using a linear classifier on individual conversation activations, we identify an internal representation of agreement. We find that it varies substantially across turns and conversations and does not reliably track external agreement at the individual conversation level. We therefore move beyond the representation of agreement in individual conversations, by aggregating the agreement representation across conversations. Externally, this aggregate view reveals a simple structure: when pooled across conversations, agreement can be predicted well with a Markov process, with agreement at each turn being a direct function of agreement at the previous turn. Similarly, when internal agreement is aggregated, it couples with the external Markov agreement through a power-law mapping, exposing Markovian dynamics in internal representations. Additionally, we find that after a change of stance, models express agreement externally before their internal representations reflect the same shift. These results reveal a joint structure between internal and external agreement that emerges only when internal features are aggregated across conversations. Code available at https://github.com/technion-cs-nlp/SeeingTheForestForTheTrees.

</details>


### 104. Signals and Queries: Token-Efficient Agentic Context Discovery

- **Authors:** Yam Marcovitz
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29326v1](http://arxiv.org/abs/2610.29326v1)
- **PDF:** [https://arxiv.org/pdf/2610.29326v1](https://arxiv.org/pdf/2610.29326v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

User-facing LLM agents must identify which behavioral policies apply at each turn, but evaluating every policy with an LLM is costly. We introduce Signals and Queries (S&Q), a lightweight first-stage relevance filter developed for Parlant 4.0 that removes at least 30% of candidate policies before downstream evaluation while preserving high recall. For each policy, an LLM generates activating examples and hard negatives offline. An independent logistic classifier trained on their embeddings then predicts relevance using embeddings and vector dot products, with no per-turn LLM calls. This shifts expensive relevance evaluation to a smaller candidate set, while allowing each policy's classifier to be updated independently. Evaluated against 9,144 LLM-judge relevance labels covering 254 $τ^2$-bench conversation prefixes and 36 airline policies, S&Q achieves higher precision than top-K and cosine-threshold retrieval at every evaluated recall level, with consistent results across two embedding providers. These findings support inexpensive, per-policy classification as a practical first stage for reducing downstream evaluation workload in customer-facing agents.

</details>


### 105. Credit Where Credit Is Due: Contrastive Attribution Topology Search for Multi-Agent Systems

- **Authors:** Fabian Tritthart, Tom Zehle
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29292v1](http://arxiv.org/abs/2610.29292v1)
- **PDF:** [https://arxiv.org/pdf/2610.29292v1](https://arxiv.org/pdf/2610.29292v1)
- **Categories:** cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

An LLM multi-agent system (MAS) is only as good as the agents it chooses to trust: its accuracy and cost hinge on its topology, meaning which agents are included and how they communicate. A single task score, however, does not reveal which agents help or hinder performance. We propose Contrastive Attribution Topology Search (CATS), which searches for compact teams within a fixed supergraph of specialized agents. An LLM attributer compares execution traces across candidate topologies and assigns credit to individual agents. CATS uses these credits to update supergraph edges while progressively pruning weak edges and agents, yielding a small team for deployment. With small open-weight models and matched candidate evaluations, CATS improves mean accuracy on BigCodeBench by 5.3 percentage points over score-only heuristic search while using 54$\%$ fewer deployment tokens. On MBPP, CATS matches the strongest baselines with fewer tokens than the other searches. In a HotpotQA prompt-poisoning stress test, CATS excludes all adversarially prompted agents in all three runs, whereas random search retains some at comparable accuracy. Per-agent credit thus supports both team optimization and the pruning of potentially harmful agents.

</details>


### 106. Design and Tuning of Multi-Agent Systems Using Bayesian Evolutionary Optimization

- **Authors:** Dominik Jehle, Tom Zehle
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29276v1](http://arxiv.org/abs/2610.29276v1)
- **PDF:** [https://arxiv.org/pdf/2610.29276v1](https://arxiv.org/pdf/2610.29276v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Designing effective multi-agent systems (MAS) remains a challenging and resource-intensive task. We propose a Bayesian Evolutionary Optimization framework for automatically discovering task-specific MAS topologies. The approach combines evolutionary operators to generate diverse workflow graphs with Bayesian optimization to focus cost intensive evaluations on promising candidates. In contrast to LLM-based candidate selection, our approach uses a graph-aware Gaussian Process and Expected Improvement to provide an explicit selection criterion during evolutionary search. We evaluate the method on BigCodeBench for code generation and on a tabular preprocessing benchmark using TabPFN. On BigCodeBench, evolved architectures achieve the highest overall performance among the evaluated agent systems. On temporal tabular datasets, optimized MAS preprocessing improves over the default TabPFN model on several tasks, while remaining competitive on IID datasets. Overall, the results demonstrate the potential of Bayesian selection for guiding evolutionary MAS search under expensive evaluation budgets.

</details>


### 107. CrashGym: Measuring the Decision Value of Experimentation for LLM Agents in Counterfactual Market Crashes

- **Authors:** Haocheng Lu, Haoxuan Cheng, Mingyang Chen, Minjun Zhu
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29245v1](http://arxiv.org/abs/2610.29245v1)
- **PDF:** [https://arxiv.org/pdf/2610.29245v1](https://arxiv.org/pdf/2610.29245v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language-model agents are increasingly asked to run experiments, yet benchmarks rarely measure whether those experiments improve the decisions they are meant to inform. We introduce CrashGym, a deterministic, replayable limit-order-book simulator in which an agent must choose between a deleveraging intervention and a liquidity backstop for a market about to suffer a shock-triggered crash. Before committing, the agent may query intervention experiments in a laboratory realization of the market. Its choice is then scored on an independently seeded target realization in which the simulator executes every feasible intervention, so regret relative to the best intervention is computed by directly simulating every alternative on the same target repeats, with no human or model-based judging. The simulator implements each amplification channel---persistent price impact, liquidity withdrawal, margin-driven liquidation, and an evolving strategy mix---as an explicit mechanism that can be switched on in stages. In a prospectively specified study on 24 newly sampled worlds, laboratory access reduces the mean regret of the one deployment with a complete record (Luna) from 8.878 to 3.785, a paired reduction of 5.092 utility units (nominal 95% world-bootstrap interval: 1.028--9.507), or 57.4% of the OBSERVE-ONLY mean. Prospective comparisons for two further deployments are incomplete; in a separate exploratory study, mean regret is lower with laboratory access for all four deployments evaluated. A laboratory whose strategy mix evolves endogenously yields no established advantage over one with a fixed mix. CrashGym thus measures the value of experimentation as avoided decision loss and lets simulator detail be judged by the decisions it supports.

</details>


### 108. MA-UITD: Offline Multi-Agent Reward Inference for Characterizing Continuous Social Behavior

- **Authors:** Zeyuan Zhang, Yiyun Yang, Yuan Cheng, Herbert Zheng Wu, Yusi Chen
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29237v1](http://arxiv.org/abs/2610.29237v1)
- **PDF:** [https://arxiv.org/pdf/2610.29237v1](https://arxiv.org/pdf/2610.29237v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent inverse reinforcement learning offers a powerful framework not only for imitation learning but also for understanding the neural computations supporting social interactions and decision-making. Inferring rewards from interacting agents is challenging because observed choices reflect both personal preferences and expectations about others. Existing methods often require additional environment interaction, repeated policy optimization as an inner loop, or restrictive assumptions about environment dynamics and action spaces, limiting their applicability to fixed behavioral datasets. We introduce Multi-Agent Unilateral Inverse Temporal Difference Learning (MA-UITD), an offline method for inferring explicit agent-specific rewards from joint demonstrations in continuous-state environments with either discrete or bounded continuous actions. Its core idea is to represent the long-term consequences of each agent's own actions through belief-conditioned successor features that average over other agents' behavior. Shared reward features and agent-specific preference vectors connect these unilateral values to the target reward function, while inverse temporal-difference consistency and noise-contrastive behavioral learning enable inference without known dynamics or an inner policy-optimization loop. Across simulated cooperative, competitive, and general-sum tasks, MA-UITD outperforms baselines in discrete-action settings and infers behaviorally compatible reward profiles in continuous-action settings. When applied to experimentally collected social-foraging trajectories, MA-UITD inferred distinct spatial and interaction-dependent reward structures for leaders and followers, providing a quantitative characterization of latent behavioral objectives that may be relevant for understanding the neural computations underlying social behavior.

</details>


### 109. Correlated Failures of AI Approval Monitors

- **Authors:** Luca Zanolini
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29178v1](http://arxiv.org/abs/2610.29178v1)
- **PDF:** [https://arxiv.org/pdf/2610.29178v1](https://arxiv.org/pdf/2610.29178v1)
- **Categories:** cs.CR, cs.AI, cs.DC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Before an AI agent takes a consequential action, such as paying, messaging or changing code, several monitors check it. Their verdicts are combined by aggregating scores or by counting approvals, whatever inputs the monitors share. Monitors that share a base model or a poisoned input, however, may fail together. We borrow the fail-prone systems of distributed computing: lists of monitor sets that may fail together. A rule is safe if it executes no bad action and live if it blocks no good one. We measured twelve small open-weights monitors on payment approval under two pre-registered protocols. Without pre-registration, we also measured three closed frontier models (Claude Opus 5.5, GPT-6 Astra, Gemini 4 Argon) and the open DeepSeek-V3.2. Every reliable fooling of a monitor into approving a fraud came through an evidence source and reached only that source's readers. Fooling it into blocking a correct payment depended on injection resistance, a monitor's refusal to follow instructions planted in its data. Small models and DeepSeek obeyed such notes. The three closed models ignored them in all but one case, and Opus also resisted persuasion tailored to it. On new data, a rule that counts sources instead of votes blocked 0.9% of correct payments, against 7.4% for the best counting rule, at equal safety. The pre-registered worst-case test failed. One attack left the approvers on a single source, so no rule over the twelve language-model monitors survives every measured attack. Adding a rule engine, which cannot be persuaded, restored the condition for a safe and live rule on the measured attacks. Diversify the inputs, harden the monitors, count sources, not votes.

</details>


### 110. Steering Black-Box Large Language Model Agents with Pitfall Anticipation World Model

- **Authors:** Jiongxiao Wang, Han Ding, Youzhi Luo, Yawei Wang, Yun Zhou, Linbo Liu, Panpan Xu
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29139v1](http://arxiv.org/abs/2610.29139v1)
- **PDF:** [https://arxiv.org/pdf/2610.29139v1](https://arxiv.org/pdf/2610.29139v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Frontier black-box Large Language Model (LLM) agents are proficient at long-horizon reasoning and precise action generation. However, when it comes to a specific agentic task, they have no internalized knowledge of how that particular environment unfolds. A world model offers a natural remedy, providing the agent with environment specific knowledge by foreseeing how the environment will respond to the action it is about to take. Prior world models for LLM agents mainly predict next observations at each step, which is costly and often uninformative because individual observations provide limited task-relevant guidance and not every step requires call for foresight. This raises a key question: what a world model should predict and when should it be invoked for agentic tasks? Our pilot study suggests that world model guidance is most useful when it anticipates pitfalls within a bounded multi-step future. Motivated by this, we introduce Pitfall Anticipation World Model (PAWM), which selectively intervenes when a potential pitfall arises and predicts the impending failure to steer the agent away from it. PAWM is trained in two stages: Supervised Fine-Tuning (SFT) on synthetic data labeled with agent pitfalls, followed by GRPO co-training with a black-box LLM to further optimize it in the target environment. PAWM improves Claude Sonnet 4.5 performance by 24.3% on ScienceWorld and 7.7% on WebArena-Lite, outperforming a range of baselines. These results demonstrate that PAWM provides an effective form of world model guidance for black-box LLM agents.

</details>


### 111. Resonance and Depth: Composing Timbral Identity and Spatial Form in an Artist-in-the-Loop Co-Creative Multi-Agent Percussive Performance

- **Authors:** Keon Ju Maverick Lee
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29026v1](http://arxiv.org/abs/2610.29026v1)
- **PDF:** [https://arxiv.org/pdf/2610.29026v1](https://arxiv.org/pdf/2610.29026v1)
- **Categories:** cs.SD, cs.MA, cs.MM


> Summary unavailable.


<details>
<summary>Abstract</summary>

This research-creation artistic report presents Resonance and Depth, a 9-minute immersive electroacoustic/acousmatic performance that treats timbre and space as primary compositional materials. Built from live electronic percussion and a personal corpus recorded, curated, and composed by the author, the work investigates how timbral identity and musical form can emerge through real-time recombination, spatialisation, and performer-system interaction rather than conventional harmonic development. The performance is realised as an artist-in-the-loop co-creative multi-agent system integrating MACAT, MACataRT, a MIDI-based musical agent, a spatialisation layer, and a conductor agent. These components recombine and transform the performer's material through concatenative synthesis, audio mosaicing, symbolic mediation, physically inspired synthesis, and object-based spatialisation. The work approaches spatialisation as an active compositional process in which position, trajectory, depth, diffusion, width, and apparent size participate in musical phrasing and form. Through this practice-based framework, Resonance and Depth examines how performer identity can be retained, transformed, and redistributed across human, algorithmic, timbral, and spatial processes within an immersive co-creative performance ecology.

</details>


### 112. An Evidence-Driven Multi-Agent Compound AI System for Head and Neck Proton Radiotherapy Planning

- **Authors:** Qingqing Wang, Liqiang Xiao, Chang Chang
- **Published:** 2026-10-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.29010v1](http://arxiv.org/abs/2610.29010v1)
- **PDF:** [https://arxiv.org/pdf/2610.29010v1](https://arxiv.org/pdf/2610.29010v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Radiation treatment planning requires balancing competing objectives to satisfy clinical criteria while accommodating physicians' preferences. This study aims to develop an evidence-driven, multi-agent compound AI system that integrates DRL-based automated treatment planning with LLM-based conversational plan refinement for proton PBS therapy. A policy network trained using PPO first generates multiple plans without human intervention, from which one is selected as the target plan and the others serve as references for subsequent refinements. For challenging cases requiring further adjustments, an LLM-based multi-agent system enables plan refinement through natural language interactions. The system comprises a planning agent that recommends evidence-supported adjustments, a chatbot providing a unified conversational interface, and an evaluation agent that retrieves clinical metrics and identifies constraint violations. To enhance domain-specific reasoning, the planning agent based on Qwen3-14B is designed to justify its recommendations using evidence from previously generated plans and post-trained on task-specific data using SFT and GRPO. The framework was trained and evaluated using 21 patients with H&N cancers, with 5 PPO-generated plans per patient. Of these, 50 plans were selected for instruction-guided refinement. Compared with the base LLM, the post-trained Qwen3-14B demonstrated improved instruction-following, information retrieval and domain-specific reasoning capabilities. The resulting adjustments more effectively improved user-prioritized objectives while limiting deterioration in competing objectives, yielding more clinically appropriate trade-offs in patient-specific plan refinement. The proposed compound AI system provides a user-friendly planning platform, offering a promising approach to personalized proton PBS treatment planning.

</details>


### 113. Attention-based Classification for Indirect Prompt Injection

- **Authors:** Amelia Kawasaki, Stefan Lee
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28988v1](http://arxiv.org/abs/2610.28988v1)
- **PDF:** [https://arxiv.org/pdf/2610.28988v1](https://arxiv.org/pdf/2610.28988v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Indirect prompt injection (IPI) attacks, in which adversarial instructions are embedded in external data processed by a language model, pose a significant threat to the integrity of deployed LLM agents. Attention Tracker (Hung et al., 2025) is a recently proposed white-box detection method that identifies prompt injection attacks by monitoring how a model's attention is distributed between user task tokens and data tokens, claiming dataset-agnostic detection via a scalar focus score threshold. In this paper, we provide the first evaluation of Attention Tracker in a realistic agentic IPI setting using the AgentDojo benchmark, finding that the dataset agnosticism claim does not hold. We find that in agentic environments, long structured tool outputs subvert the fundamental assumptions Attention Tracker makes about attention that the method depends on and produces near-chance detection on AgentDojo across most model families. We propose AttnDA, an extension replacing the scalar threshold with a Fisher Linear Discriminant Analysis classifier over the per-head focus score vector, and evaluate both methods in a cross-dataset setting spanning four benchmarks. AttnDA improves detection performance across agentic and tool-integrated benchmarks, though transfer to AgentDojo remains challenging regardless of classifier choice. A covariance ablation further shows that removing inter-head correlation structure substantially contributes to performance, with complex covariance assumptions causing significant degradation on cross-domain data. These results indicate that the attentional distraction signal underlying focus-score-based detection does not transfer reliably to agentic environments, and that learned linear classifiers over head-level attention features offer improved detection performance, provided training data from the target deployment domain is available.

</details>


### 114. PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust

- **Authors:** Tanqiu Jiang, Min Bai, Sadat Shahriar, Wanyu Du, Sandesh Swamy
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28987v1](http://arxiv.org/abs/2610.28987v1)
- **PDF:** [https://arxiv.org/pdf/2610.28987v1](https://arxiv.org/pdf/2610.28987v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Persistent memory is a largely undefended surface for injection and poisoning, and the same risk limits memory sharing among agents. We present PerMIT, a memory architecture with provable integrity guarantees under an explicit trust assumption: only user-typed inputs and values confirmed at a gate are trusted. PerMIT mediates the release and use of untrusted environment-derived values through a finite memory interface, while preserving agent-driven multi-turn planning and tool choice. Over this finite interface, we prove two integrity theorems that are also machine-checked in Lean 4, which together ensure that environment-derived memory reaches a sensitive action only if confirmed at the gate and influences the agent's behavior only through what the gate displays. Every attack in our threat model thereby reduces to a single auditable decision, which a human, an LLM verifier, or both can make in practice. On Trojan Hippo, PerMIT records zero observed attack success with self-verification and lightweight verifiers. Because each confirmation is a logged verdict on exact content, endorsements accumulate across users, and sufficiently endorsed items become community-confirmed with no further verification required. Under explicit assumptions, we prove and corroborate in simulation a co-scaling property: as the community grows, the risks of promoting poison and of wrongly evicting benign knowledge fall, while per-user verification effort does not rise. On $τ^2$-bench, communities of up to 90 autonomous agents use PerMIT to build shared knowledge bases with no direct memory injection promoted, and the resulting knowledge significantly improves new agents on held-out tasks, suggesting a path toward agents that safely self-improve at test time.

</details>


### 115. Behavior Beyond Text: Evaluating Refusal Transfer Failure in LLM Agents

- **Authors:** Ekagra Gupta, Raj Saha, Aniekan-Abasi Inyang, Adam Al Gharib
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28982v1](http://arxiv.org/abs/2610.28982v1)
- **PDF:** [https://arxiv.org/pdf/2610.28982v1](https://arxiv.org/pdf/2610.28982v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

While large language models are increasingly deployed as tool-calling agents, their safety evaluations still focus primarily on their ability to refuse harmful requests in text. We investigate whether the refusal behavior in text transfers to tool use. We construct a benchmark of 2,304 prompts across four domains, consisting of matched triplets that present the same harmful or benign request in text-only, standard tool-enabled, and adversarially framed tool-enabled settings. We then assess tool-call safety using 20 predefined forbidden actions. Testing five models of varying sizes and families, we find that requests refused in text frequently result in unsafe tool calls. Under standard tool-enabled prompting, this divergence occurs for 10-52 percent of harmful requests refused in chat. To mechanistically investigate this gap, we identify a refusal-associated direction in the residual stream of each of the five models. We find that in tool-enabled contexts, the activations along this direction decrease in four of five models. Furthermore, lower activation predicts unsafe tool calls across all five models (AUC 0.76-0.86). However, restoring the signal to the respective text-only value through activation patching only prevents a subset of unsafe calls, primarily by suppressing tool use rather than by producing safer calls. Steering along the refusal direction nearly eliminates unsafe calls only at strengths that also suppress benign tool use or degrade the output quality. Our findings indicate that the identified refusal direction contributes to whether a model acts, but only partially explains the refusal divergence. Therefore, evaluating the safety of tool-calling agents requires directly examining their actions along with their textual responses.

</details>


### 116. The Butterfly Effect in LLM Social Simulations: From Architecture Sensitivity to Robustness Audits

- **Authors:** Jinyi Ye, Lei Cao, Ding Chen, Emilio Ferrara
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28981v1](http://arxiv.org/abs/2610.28981v1)
- **PDF:** [https://arxiv.org/pdf/2610.28981v1](https://arxiv.org/pdf/2610.28981v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

A butterfly effect occurs when a local perturbation propagates through a system and produces divergence in its collective outcome. In LLM social simulations, this creates a particular challenge for scientific inference: sensitivity to implementation choices can enter agent interactions and alter the collective outcomes on which scientific claims are based. We study this problem through a repeated Prisoner's Dilemma and a social-media echo chamber, spanning representation- and design-level perturbations across four LLM families. We find that controlled perturbations can substantially alter collective outcomes, with sensitivity varying across both perturbations and models. In the Prisoner's Dilemma, changing only the representation of a matched persona shifts two-agent cooperation by 75.2 percentage points for GPT-5.2, while game framing and memory representation produce smaller or less consistent effects. Multi-agent interaction further reshapes representation sensitivity, producing amplification or attenuation depending on the model and perturbation. In the echo-chamber simulation, persona representation changes interaction targeting and is accompanied by divergence in collective interaction structure, extending representation sensitivity from agent behavior to network-level outcomes. These results show that robustness cannot be inferred from a single simulation configuration and that local sensitivity can change as it propagates through interaction. We introduce TRAILS (Taxonomy for Robustness Audits In LLM Simulations) and the Social Simulation Audit Card as a framework for systematically auditing these dependencies and calibrating the scope of scientific claims to the robustness evidence that supports them.

</details>


### 117. Black-Box Red-Teaming of Multi-Agent Systems via Reinforcement Learning

- **Authors:** Yuqi Jia, Hangsheng Zhang, Chenxi Liu, Junjie Liang, Xun Chen
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28966v1](http://arxiv.org/abs/2610.28966v1)
- **PDF:** [https://arxiv.org/pdf/2610.28966v1](https://arxiv.org/pdf/2610.28966v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly deployed in multi-agent systems (MAS) to accomplish complex tasks. Prior black-box red-teaming attacks mainly focus on single agents, but we find that these methods are far less effective in MAS, where multiple sub-agents may not directly interact with the user. Therefore, we introduce ReMAS, the first reinforcement learning-based red-teaming framework tailored to MASs, which fine-tunes attacker LLMs to generate effective adversarial prompts for system prompt extraction. The framework follows a two-step process: first, a rewrite stage refines base attack prompts to increase extraction success, and second, a template generation stage constructs attack templates that improve the likelihood of invoking specific sub-agents and thus revealing their system prompts. Extensive experiments show that our method substantially improves attack success rates compared to existing black-box attacks, with transferability across different backend LLMs and MAS structures. These results underscore the vulnerabilities of multi-agent systems and the importance of developing stronger defenses against adaptive black-box adversaries.

</details>


### 118. Transformers as Generic Deep Neural Networks: Exact Compilation, the Cost of Removing Activation-Activation Products, and Multi-Agent Attention Clustering

- **Authors:** Sergey Salishev, Zeev Volkovich, Oleg Granichin
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28958v1](http://arxiv.org/abs/2610.28958v1)
- **PDF:** [https://arxiv.org/pdf/2610.28958v1](https://arxiv.org/pdf/2610.28958v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Transformers are deployed as a special model class. Neural processing units (NPU) add dedicated operators for attention and normalization, and quantization relies on Transformer-specific algorithms. We show the computation does not force this. Every Transformer block, with attention, LayerNorm and a GELU MLP, compiles exactly into a generic deep neural network built from fixed affine maps, routing and the square, sigmoid and inverse square root, plus GELU or its sigmoid approximation. Without activation-activation products, every transform-wise compilation adds at least $N^2$ scalar nonlinear evaluations per head for dense scores. Keeping that one operation type removes this cost; its elementwise form, present on every surveyed NPU, suffices with the sigmoid and inverse square root. For top-$k$ attention with exchangeable tail scores, we prove that exact or conditional-mean tail mass gives an unbiased, minimum-mean-square-error estimate of the attention distribution, while tail drop is conditionally biased. When queries or agents cluster, centroids choose the keys first, reducing the number of computed scores from $N^2$ to $Nk$ per head. On DeiT-Tiny, MambaIRv2-Light and Pythia-70M the compiled models match their references with all keys, standard post-training quantization applies, and the exact tail-mass estimate beats tail dropping with half as many keys on DeiT-Tiny and, for $k\le8$, on Pythia-70M.

</details>


### 119. DiffResearch: Accelerating Deep Research with Diffusion Language Models

- **Authors:** Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov, Sergey Muravyov
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28909v1](http://arxiv.org/abs/2610.28909v1)
- **PDF:** [https://arxiv.org/pdf/2610.28909v1](https://arxiv.org/pdf/2610.28909v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep research systems iteratively plan, gather evidence, synthesize, and revise, making end-to-end latency a key bottleneck for interactive use. Almost all production systems are built on autoregressive (AR) language models and inherit left-to-right decoding in planning and long-form writing. We present DiffResearch, an open multi-agent deep research framework that places a diffusion language model (dLLM) at the core of every stage, and measure how a diffusion backbone changes latency and report quality. Holding the agentic scaffold, retrieval code, prompts, and evaluation fixed, we swap the backbone between an open diffusion model and a comparable AR model. Across 100 Deep Research Bench tasks, the diffusion backbone is roughly 6 times faster end-to-end, driven by order-of-magnitude reductions in planning and writing. We further introduce dFast, a decomposition mode that reads intermediate denoising states and extracts subqueries before generation finishes, providing a 1.99 times median speedup for decomposition in isolation with no loss of report quality. On the benchmark's RACE rubric, dFast obtains the best overall score among the three configurations. Finally, in a public system-level leaderboard snapshot, an instance built on a stronger diffusion model ranks above several commercial systems. We release DiffResearch under an Apache-2.0 license.

</details>


### 120. JaxMARL-BC: Multi-Agent Reinforcement Learning for Macroeconomic Modelling, in Seconds

- **Authors:** Daniele Montagnani, Andrea Coletta, Antonietta Mira, Aldo Glielmo
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28907v1](http://arxiv.org/abs/2610.28907v1)
- **PDF:** [https://arxiv.org/pdf/2610.28907v1](https://arxiv.org/pdf/2610.28907v1)
- **Categories:** cs.MA, cs.AI, cs.LG, econ.GN


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) offers a principled way of populating simulated economies with many heterogeneous decision makers. Its adoption, pioneered in finance, has nonetheless been slow in macroeconomics because of two main limitations: the lack of a shared frame of reference connecting MARL systems to dynamic stochastic general equilibrium (DSGE) models the profession already trusts, and the very long training times. The first limitation was recently addressed by the Multi-Agent Reinforcement Learning Business Cycle (MARL-BC), which places deep RL households in a real business cycle economy and reduces to classic DSGE models in specific limits. Here we address the second limitation. We present JaxMARL-BC, a JAX-accelerated simulator that trains MARL-BC economies in seconds (between 75x and 724x faster than the reference implementation), and scales to 200,000 independent learning households. We verify its correctness against the known DSGE limits, characterise its scaling through a simple cost law, and demonstrate its value by a proof-of-concept calibration of an extended model with heterogeneous returns on capital, in a two-hour experiment that would previously have taken over a month. We release JaxMARL-BC as open source.

</details>


### 121. Hidden Messages Between Diffusion Language Model Agents: Causal Evidence for Latent Communication

- **Authors:** Alan-Barsag Gazzaev, Alexey Gavrilov, Sergey Muravyov, Ilya Makarov
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28905v1](http://arxiv.org/abs/2610.28905v1)
- **PDF:** [https://arxiv.org/pdf/2610.28905v1](https://arxiv.org/pdf/2610.28905v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Diffusion language models form answers through a sequence of revisable continuous states, but multi-agent systems usually discard those states and make agents communicate only after decoding text. We ask whether one independent diffusion trajectory can pass a compact hidden message into another and, crucially, whether the receiver uses what that message means. In Hidden Messages, a sender compresses its denoising state into four signed dense vectors; the receiver consumes them while retaining its own context, canvas, and trajectory. Removing a message tests whether the channel matters; replacing it with a message from another example tests whether its content matters. Across controlled tasks, derangement removes a +63.6-point advantage on Tiny-A2D and a +100.0-point advantage on Dream-7B, while targeted substitutions steer the receiver toward the substituted fact. On QASC with the two supporting facts split across agents, matched communication reaches 80.8%, but a wrong-example message lowers accuracy to 46.8%, a content effect of +34.0 points. The surprising result is temporal: one late transfer reaches 87.8%, exceeding four recurrent exchanges by +7.0 points. These experiments provide causal evidence for continuous hidden communication between diffusion-LM agents and show that when information is transferred can matter more than how many times agents exchange it.

</details>


### 122. Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures

- **Authors:** Yujian Liu, Li An, Zelin He, Jacob Helwig, Jiabao Ji, Rohit Jain, Siyu Zhu, Shiyu Chang
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28887v1](http://arxiv.org/abs/2610.28887v1)
- **PDF:** [https://arxiv.org/pdf/2610.28887v1](https://arxiv.org/pdf/2610.28887v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents can increasingly propose ideas, modify code, and run experiments, creating an opportunity to accelerate scientific discovery using teams of collaborative AI researchers. To escape local minima in the discovery, we propose to encourage orthogonal exploration by constructing the team using agents with varying expertise. However, realizing this design requires more than diverse backgrounds. When experiments are costly, a team can test only a limited number of ideas, thereby creating the need to balance exploration and exploitation when selecting a subset of researchers to propose and execute new experiments. Furthermore, each result should shape what the team tries next. We therefore ask how AI researchers with different scientific backgrounds can build on one another's findings and sustain progress under a limited experimental budget. To address these challenges, we build a team of persistent AI researchers, each grounded in a different discipline, who keep private research histories, share experimental evidence, and receive research opportunities through adaptive allocation. We demonstrate the effectiveness of this design by deploying the team to search for linear attention architectures, where it outperforms GDN2 at 1.3B scale on language modeling, common-sense reasoning, and synthetic and real-world retrieval tasks. In controlled comparisons, removing any single organizational component from our design yields markedly weaker discoveries: without disciplinary backgrounds, the search plateaus early; without private histories, researchers make less progress despite identical shared evidence; and uniform selection falls short of adaptive allocation within the same budget. These results suggest that sustained autonomous discovery depends not only on stronger agents, but also on who explores, what they remember, and how research effort is allocated.

</details>


### 123. Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets

- **Authors:** Hieu Tran, Hong Yu
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28787v1](http://arxiv.org/abs/2610.28787v1)
- **PDF:** [https://arxiv.org/pdf/2610.28787v1](https://arxiv.org/pdf/2610.28787v1)
- **Categories:** cs.CL, cs.GT, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluations of large language model (LLM) agents report that pricing agents collude at others' expense. Yet collusion is defined by enforcement: a cartel, in which competitors share monopoly profits, holds only if a member who cheats is punished. We introduce an audit that tests enforcement by forcing a member to cheat in counterfactual copies of a market, and use it to study what reinforcement learning (RL) teaches agents in pricing and trading. Small LLMs trained by RL learn what their training rivals reward, but only what they readily try. In self-play, they learn fixed rules ignoring their rivals; against a punishing rival, to be deterred; against a cheating rival, to match its cuts, never the costly price war that would deter it, which they rarely try. A war forced into training is learned, but mostly only where it was forced. Against their own copies, deterred and matching agents can earn the same cartel profits, but only matching ones can enforce them, and then thinly: as a by-product and only against large cuts. Q-learners enforce collusion only in pricing. Prompted LLMs reach cartel-like outcomes mostly through rules that ignore the market. Outcome measures cannot tell these cases apart; the audit can.

</details>


### 124. GBClaw: An agentic AI framework for atomistic grain boundary research and mechanistic discovery

- **Authors:** Yazhuo Liu, Kunqing Ding, Xiaoguo Gong, Zifeng Wang, Yichen Yang, Yifeng Che, Wen Chen, Josh Kacher, Olivier Pierron, Shigenobu Ogata, Ting Zhu
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28629v1](http://arxiv.org/abs/2610.28629v1)
- **PDF:** [https://arxiv.org/pdf/2610.28629v1](https://arxiv.org/pdf/2610.28629v1)
- **Categories:** cond-mat.mtrl-sci, cond-mat.mes-hall, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic artificial intelligence (AI) systems hold immense potential for automating complex workflows in materials discovery and design, but extending them to domain-intensive mechanistic investigations remains challenging. Here, we present GBClaw, an agentic AI framework for investigating the structure and deformation of general grain boundaries (GBs). Although general GBs constitute the vast majority of real-world interfaces in polycrystalline materials, they remain understudied because their structural complexity and interfacial mismatch complicate experimental and modeling research. GBClaw integrates large language models (LLMs) into a modular architecture comprising an orchestrator, specialized agents, domain-specific tools, simulation interfaces, and hierarchical memory. Through dynamic replanning and iterative workflow refinement, the framework effectively connects systematic simulations with targeted mechanistic analysis. Applied to 14 general asymmetric tilt GBs in nickel, GBClaw characterized interfacial defect structures and identified diverse deformation modes across these incommensurate boundaries. Comparing boundary sliding with and without secondary GB misfit dislocations revealed substantial differences in shear strength, underscoring the critical role of defect hierarchies in sliding resistance. Furthermore, researcher-guided follow-up calculations traced an anomalously high shear resistance to metastable boundary structures. This work demonstrates that combining agentic AI with domain expertise bridges high-throughput computational screening with deep physical understanding of complex material interfaces.

</details>


### 125. Semantic Observability for Autonomous Systems Diagnostics

- **Authors:** Jitendra Solanki, Anand Todkar, Ziran Min
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28611v1](http://arxiv.org/abs/2610.28611v1)
- **PDF:** [https://arxiv.org/pdf/2610.28611v1](https://arxiv.org/pdf/2610.28611v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern distributed microservice deployments generate massive volumes of heterogeneous, multi-format observability logs across physically and logically partitioned infrastructure. Isolating root causes during cascading failures remains an arduous task for Site Reliability Engineers (SREs), bottlenecked by manual keyword filtering and disjointed temporal correlation across monitoring dashboards. We introduce Semantic Observability, an autonomous multi-agent framework that unifies disparate log streams into a dynamic, queryable Property Graph Database. By modeling physical infrastructure topologies, logical software dependencies, and chronological event sequences as attributed nodes and directed relations, it bridges the semantic gap inherent in flat, unstructured log repositories. Building on this unified substrate, we deploy a stateful multi-agent system orchestrated through Directed Cyclic Graphs (DCGs). The system autonomously navigates the topology, applying causal graph algorithms and temporal back-traversal to isolate the precise blast radius of anomalies. The pruned subgraph is then interpreted by a Large Language Model (LLM) reasoning engine to generate contextualized, code-level Root Cause Analyses (RCA) and actionable remediations. This paper establishes the foundational system architecture, formal relational ontology, and multi-agent control loops of Semantic Observability. We show conceptually how the framework eliminates ambient telemetry noise, reduces Mean Time to Resolution (MTTR), compresses LLM token consumption, and prevents structural hallucinations. We also specify an open-source validation framework on standard benchmarks (LogHub and Train-Ticket), laying the groundwork for a forthcoming companion paper on exhaustive quantitative evaluation and production benchmarking.

</details>


### 126. OptScientist: Automated Discovery of Optimization Laws

- **Authors:** Ma ZhenYao, Yue Liang, Jian-Qiao Zhu
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28562v1](http://arxiv.org/abs/2610.28562v1)
- **PDF:** [https://arxiv.org/pdf/2610.28562v1](https://arxiv.org/pdf/2610.28562v1)
- **Categories:** cs.AI, cs.LG, cs.SC, econ.EM, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Many scientific phenomena are best understood as outcomes of underlying optimization problems, yet automated scientific discovery has largely focused on recovering equations that describe observed input-output patterns. We introduce OptScientist, a novel automated framework for discovering compact symbolic optimization laws directly from data. OptScientist comprises (i) a model that infers symbolic optimization problems by first learning to represent data as an optimization problem and then extracting its symbolic form, and (ii) an LLM agentic system embedding the model in a discovery process that integrates theoretical priors from scientific literature, discovers candidate laws, abstracts their underlying mechanisms, and suggests new data to collect. We first evaluate OptScientist on OptFeynman, a novel benchmark of 99 physics-derived optimization problems, where OptScientist recovers ground-truth laws for over 80% of the problems and remains robust to noisy contextual information, while substantially outperforming machine-learning, symbolic, and LLM-based model-discovery baselines. On human risky choice and central-bank monetary policy, OptScientist discovers compact symbolic optimization laws that achieve held-out predictive performance competitive with leading baselines, while using few parameters and substantially fewer tokens than LLM baselines. Overall, OptScientist extends automated scientific discovery to uncovering optimization laws that generate observed phenomena, enabling automated theory building across the physical, biological, behavioral, and social sciences.

</details>


### 127. Proof-Carrying Contracts: Commitments AI Agents Cannot Break

- **Authors:** Carlo Ciliberto, Alessandro Rudi, Enrico Tassi
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28484v1](http://arxiv.org/abs/2610.28484v1)
- **PDF:** [https://arxiv.org/pdf/2610.28484v1](https://arxiv.org/pdf/2610.28484v1)
- **Categories:** cs.AI, cs.CR, cs.LO, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly act on behalf of people or other agents, purchasing services, exchanging information and delegating work. What an agent must respect is written in instructions, policies or agreements, but text alone cannot make it comply. It may make mistakes, be redirected by what it reads, or pursue different interests. For an economy of such agents to function, parties need agreements they can rely on without inspecting or trusting one another's agents. We introduce Proof-Carrying Contracts (PC2), a framework for making agreed constraints enforceable throughout an agent's interactions with a system. Before a requested operation can run, the agent must supply a machine-checkable proof that it preserves the agreed constraints in every case allowed by its model. An execution system called the Airlock checks the proof and controls access to the operation. The parties specify the conditions to preserve, while the agent supplies the reasoning needed to justify its decisions and remains free to adapt its strategy. This avoids having to design a separate permission policy and prove that every decision it permits is safe. We prove that the constraints hold at every instant during execution, even for an adversarial agent, and identify when this implies safety in the world. Reusable capability modules provide tools and guarantees from which contracts can be constructed. PC2 provides a foundation for an agent economy whose agreements protect both those delegating work and those carrying it out.

</details>


### 128. Claims of emergence in AI should be grounded in information decomposition

- **Authors:** Christoph Riedl, Fernando E. Rosas
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28479v1](http://arxiv.org/abs/2610.28479v1)
- **PDF:** [https://arxiv.org/pdf/2610.28479v1](https://arxiv.org/pdf/2610.28479v1)
- **Categories:** cs.AI, cs.HC, cs.IT, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a language model develops capabilities not traceable to its individual components, when a multi-agent AI system outperforms each agent on its own, or when a human-AI pair succeeds where either fails in isolation, AI researchers describe it as a case of ``synergy'' or ``emergence''. However, these are usually informal assessments not supported by a theoretical framework, making these claims impossible to compare or even meaningfully dispute. Here we argue that \emph{information decomposition can serve as a unifying formal framework to operationalize assessments about synergy in AI systems}. Information decomposition provides a way to distinguish qualitatively different \emph{types} of information, including unique information available from individual components, redundant information shared across multiple components, and synergistic information accessible only from parts taken together. This gives claims of emergence a precise, falsifiable criterion: a system's behavior is emergent only if it carries synergistic information about task-relevant outcomes. We apply this lens to attention heads, autonomous agents, and human-AI teams, showing how it organizes existing knowledge across scales and substrates, while also generating cross-level conjectures that siloed fields would miss.

</details>


### 129. Beyond Trajectory Statistics: Community-Consistent Human Mobility Generation via Evolving User-Location Graphs

- **Authors:** Bo Liu, Tong Li, Jiapeng Zhang, Zhu Xiao, Zhuo Tang, Kenli Li
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28467v1](http://arxiv.org/abs/2610.28467v1)
- **PDF:** [https://arxiv.org/pdf/2610.28467v1](https://arxiv.org/pdf/2610.28467v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Human mobility data are fundamental to Web-based location services and broader urban applications, and mobility generation provides synthetic trajectories when real data are costly or inaccessible. Although recent mobility generators have incorporated collective mobility patterns, they primarily focus on individual trajectories and aggregate population dynamics, leaving evolving community structures formed by user-location interactions insufficiently modeled. In this paper, we study community-consistent human mobility generation. To this end, we formulate mobility generation as the generation of dynamic user-location graphs to model community structures and propose MOTION, a Multi-agent framework for cOmmuniTy-consIstent human mObility geNeration. MOTION consists of user agents, location agents, and a global manager agent. MOTION first detects coherent communities from historical mobility using the Leiden algorithm and extracts community-conditioned interaction priors to guide the generation process. Guided by these priors, the user agents plan mobility, search destination candidates, and infer user movements from the individual view. In parallel, selectively activated location agents infer likely user arrivals from the community view. The manager coordinates both views, diagnoses interactions causing deviations, and attributes targeted reflection signals to revise user decisions, location attraction, and source-user selection. Experiments on two real-world datasets show that MOTION outperforms baselines by at least 4.05% across reported metrics of individual trajectories, population and flow distributions, and community and graph structures. Further analyses confirm its robustness, privacy preservation, and downstream utility. The code is available at https://anonymous.4open.science/r/MOTION-04C4.

</details>


### 130. After the Attacker Leaves: Benchmarking Carryover Attacks on LLM Agents

- **Authors:** Zhiyue Xu, Xukai Wang, Zhiyuan Huang, Mingjie Zhan, Jian Zhao, Xu-Yao Zhang
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28425v1](http://arxiv.org/abs/2610.28425v1)
- **PDF:** [https://arxiv.org/pdf/2610.28425v1](https://arxiv.org/pdf/2610.28425v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern LLM agents persist state across sessions via two channels: long-lived memory files silently prepended to the system prompt, and scheduled tasks waking the agent without user input. A one-time indirect prompt injection committed to either channel can re-fire across sessions long after the attacker leaves, threats we term carryover attacks. Existing prompt-injection benchmarks evaluate attacks only in the session where malicious content is first observed, leaving the gate governing when and how often a planted payload later re-fires unmeasured. We present CarryoverBench: 12 personal-assistant scenarios and 101 attack tasks across three trigger channels: Instant, same-turn IPI; Autonomous, heartbeat-scheduled; and Latent, memory-resurfaced. A rule-based verifier scores planting and triggering as independent stages. Across five frontier models, planted payloads re-fire without measurable decay over five rounds; conditional on successful planting, the trigger stage often provides little additional protection. Porting the Latent channel to a second runtime, Hermes, attenuates but does not eliminate the effect, suggesting that carryover defense requires runtime-layer controls in addition to prompt-level interventions.

</details>


### 131. MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems

- **Authors:** Mohammad Kachuee, Phu Mon Htut, Sheng Li, Nikolaos Pappas, Miguel Ballesteros Martinez, Yassine Benajiba, Sujith Ravi, Dan Roth
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28397v1](http://arxiv.org/abs/2610.28397v1)
- **PDF:** [https://arxiv.org/pdf/2610.28397v1](https://arxiv.org/pdf/2610.28397v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI extends large language models (LLMs) from generating responses to planning and executing complex workflows, substantially expanding their utility while exposing applications to unsafe actions, information leakage, and adversarial manipulation. Multi-agent systems further expand these capabilities through specialization and collaboration, but distributed authority, heterogeneous roles, and opaque or potentially compromised participants make safeguarding even more challenging. Existing defenses address important individual threats but provide fragmented coverage across local execution, system-level interactions, and enforcement mechanisms. We introduce MAS-Guard, a unified framework that closes this gap for safeguarding single- and multi-agent AI applications containing both instrumentable and opaque agents. Within instrumentable agents, the proposed local Agent Guardrail (A-Guard) layer applies task-specific experts to assess agentic events. At the system level, developer-owned Agent Charters and a Control Plane combine deterministic structural checks of routes, agent capabilities, and message formats with semantic assessments of roles and message content. These complementary layers enable enforcement through a shared set of interventions: allow, reflection, confirmation, and block. Evaluated across six benchmarks covering diverse single- and multi-agent scenarios with three agent LLMs from different providers, MAS-Guard reduces the overall attack success rate by 71.5-86.3% relative to unguarded agents, while meeting the utility reference criterion on benign tasks.

</details>


### 132. Self-Credit: Credit Assignment for Long-Horizon Agentic RL via Intra-group Rescaling

- **Authors:** Fangcong Yin, Ming Yin, Tanvi Bhandarkar, Aashu Singh, Eryk Helenowski, Shlok Kumar Mishra, Saghar Hosseini, Karthik Abinav Sankararaman, Greg Durrett, Dinkar Juyal
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28388v1](http://arxiv.org/abs/2610.28388v1)
- **PDF:** [https://arxiv.org/pdf/2610.28388v1](https://arxiv.org/pdf/2610.28388v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are commonly trained with RLVR, but the sparse nature of typical RLVR rewards makes credit assignment challenging, especially for long-horizon tasks. We propose Self-Credit, an end-to-end agentic RL method that creates dense supervision signals from sparse outcome rewards using self-generated credit assignment via intra-group rescaling. Self-Credit builds on group-based RL with three components. First, during its rollouts, the policy model generates summaries with citations to earlier turns containing critical evidence, which serve as self-generated credit. Second, we refine this model-generated credit with intra-group rescaling, which compares cited actions across successful and failed rollouts for the same prompt. This approach uses group-level agreement and disagreement to remove undeserved credit and further emphasize credit assigned to critical actions. Third, advantage reweighting uses the rescaled credit weights to update the advantages of the cited turns. On BrowseComp-Plus, Self-Credit improves over the base models by 37.0 and 36.2 points on Qwen3 8B and 32B respectively, and outperforms the strongest agentic RL baselines by 8.5 and 5.6 points, respectively. Self-Credit also improves over the strongest baselines by 4.9 points on GAIA and 4.7 points on xBench-DeepSearch. Analyses show that self-generated credit provides useful signals for selecting critical actions, and that intra-group rescaling, especially on failed rollouts, is important across model scales.

</details>


### 133. VisualEvolve: A Skill Self-Evolution Framework for Visual Reasoning

- **Authors:** Jiawei Wang, Yucun Li, Xueqi Li, Shenghao Wang, Xinquan Gong, Dan Zhang, Zheqi Lv, Yuquan Le, Shaozu Yuan, An Zhang, Da Cao, Tat-Seng Chua
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28386v1](http://arxiv.org/abs/2610.28386v1)
- **PDF:** [https://arxiv.org/pdf/2610.28386v1](https://arxiv.org/pdf/2610.28386v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Visual tool use enables vision-language models (VLMs) to acquire task-relevant evidence, but its effectiveness can be limited by predefined visual operations and the tool-use strategies learned during training. Representing these operations and strategies as reusable external skills allows them to be refined through self-evolution without updating model parameters. However, skill refinement can introduce performance regressions. Meanwhile, inspecting accumulated task execution trajectories together with skill evolution history may lead to evolution evidence overload. To address these challenges, we propose VisualEvolve, a self-evolving framework that evolves executable visual operations and tool-use strategies for VLMs through a Select--Execute--Evolve--Evaluate cycle. Skill-Library Snapshot Selection uses performance on a fixed validation set disjoint from execution tasks to select an effective historical snapshot for subsequent evolution, limiting the propagation of performance regressions. Progressive Evidence Access (PEA) guides capability-gap diagnosis through a coarse-to-fine hierarchy comprising the Skill-Performance Report, Evolution Log, Trajectory Summaries, and relevant raw trajectory segments. Across four VLM backbones and six evaluation sets from three benchmarks, VisualEvolve improves over the Initial Skill Library in 23 of 24 settings, with a maximum gain of 15.1 percentage points on VisualProbe Hard using Qwen3.5-Plus. Ablation studies support the contributions of Snapshot Selection and PEA, while further experiments show that skills can be improved using experience from different data settings and directly reused across backbones. Moreover, VisualEvolve enables effective skill self-evolution with over an order of magnitude fewer task-solving trajectories than estimated for representative RL-based methods.

</details>


### 134. FALCA: Falsification-Aware Reinforcement Learning with Hierarchical Credit Assignment for Long-Horizon Deep Search Agents

- **Authors:** Zijun Dou, Kun Luo, Chaofan Li, Shuqi Lu, Zheng Liu
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28361v1](http://arxiv.org/abs/2610.28361v1)
- **PDF:** [https://arxiv.org/pdf/2610.28361v1](https://arxiv.org/pdf/2610.28361v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon deep search requires LLM agents to iteratively decompose complex information needs, gather evidence from external sources, and maintain a reliable research state under multiple constraints. A central challenge is that early mistakes can be amplified over the search trajectory: agents may anchor on an incorrect candidate, collect partially supporting evidence, overlook contradictions, and accumulate errors that misguide subsequent reasoning. We propose FALCA, a falsification-aware framework that formulates deep search as a propose-falsify process. FALCA adopts a collaborative Searcher-Falsifier architecture, where the Searcher proposes candidate answers or sub-answers, while independent Falsifiers actively seek counterevidence, check unmet constraints, identify conflicts, and produce concise falsification reports for research-state revision. To strengthen this loop, we introduce falsification-aware training, combining SFT warmup on falsification trajectories with agentic RL based on parallel rollouts and hierarchical credit assignment over research stages, state transitions, and actions. Experiments on five search benchmarks show that FALCA improves long-horizon deep search performance over backbone and harness ablations, while reducing confirmation bias and error accumulation through more effective falsification and research-state revision.

</details>


### 135. S-Agent 2.0: Spatial Reasoning with a General Coding Agent

- **Authors:** Rui Gong, Ruoyu Wang, Yalun Dai, Hao Li, Sidi Yang, Qihao Zhao, Hongyu Li, Zeyang Guan, Fangzhou Hong, Zhaoxi Chen, Kim-Hui Yap, Ziwei Liu
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28354v1](http://arxiv.org/abs/2610.28354v1)
- **PDF:** [https://arxiv.org/pdf/2610.28354v1](https://arxiv.org/pdf/2610.28354v1)
- **Categories:** cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Spatial reasoning asks a model to work out where objects are in 3D space, how they relate to one another, and how they move. Agentic VLMs have recently brought large improvements on such tasks by letting the model actively gather evidence with 3D perception tools instead of answering in a single pass. Even so, on many questions the tools return the right evidence and the model still does not arrive at the correct answer: the gap between model and tools, where raw readings become usable conclusions, is left unfilled. We present S-Agent 2.0, a spatial reasoning agent that equips an off-the-shelf general coding agent with a command-line perception toolkit, and we design the interface around one principle: help the VLM close the evidence loop: acquire scene evidence, remember it in a persistent scene memory, and interpret each reading in plain spatial language. This design keeps the full flexibility of a coding agent, and every reading it acts on stays grounded in the tools' geometry. On MMSI-Bench and ReVSI, the toolkit improves a strong open-source model, Qwen3.8-27B, by +13.9 and +20.5 points over the same agent without tools, and a strong closed-source model, Gemini-3.8-Flash, by +11.2 and +9.6 points. With the open backbone S-Agent 2.0 reaches 66.5 on MMSI-Bench and 82.3 on ReVSI, ahead of the specialized system SpatialClaw on the same backbone (62.6 and 74.5), and with Gemini-3.8-Flash it reaches 74.1 and 90.5 against its 67.0 and 79.7. Both tool gains shrink as the backbone grows more capable, but SpatialClaw's shrinks far more on ReVSI, from +13.2 to +2.7, while ours stays at +9.6. S-Agent 2.0 also works across different general coding agent harnesses, such as Codex and Claude Code.

</details>


### 136. Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory

- **Authors:** Masahiro Kaneko, Hiromi Arai, Timothy Baldwin
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28315v2](http://arxiv.org/abs/2610.28315v2)
- **PDF:** [https://arxiv.org/pdf/2610.28315v2](https://arxiv.org/pdf/2610.28315v2)
- **Categories:** cs.CR, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly use persistent memory to personalize responses, and personal attributes in this memory pose a privacy risk if exposed. We ask how consulting memory during dialogue changes what users go on to say, and thus what the memory comes to reveal. In multi-session simulations, a simulated user with 24 personal attributes talks with a support agent that does or does not consult memory, and in both settings attributes are inferred from the full accumulated record. Across four support models, memory raises response quality but also empirical leakage, the share of attribute values correctly inferred from the record, by a margin that widens over sessions. The cause is a loop in ordinary, non-adversarial assistance. Memory-conditioned responses carry earlier values forward, often as presuppositions, and users affirm them or leave them uncorrected, so that cues and the agent's own guesses become recorded values. The loop reinforces itself, and removing the agent's mentions of an attribute lowers its later disclosure about twice as much as single-turn effects predict. Users cannot leave it on their own, since correcting a value discloses the attribute, declining to discuss it shifts later predictions toward sensitive values, and incorrect values left in place become entrenched. The loop is best weakened at the agent's response. Instructing the agent not to state or presuppose attributes brings leakage to about the no-memory level while keeping most of the quality gains, whereas filtering or anonymizing what users say or what is stored gives up much of them.

</details>


### 137. Local Work, Global Progress: A Convergence Theory of AI Agent Collaboration

- **Authors:** Ivan Ilin, Peter Richtárik
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28286v1](http://arxiv.org/abs/2610.28286v1)
- **PDF:** [https://arxiv.org/pdf/2610.28286v1](https://arxiv.org/pdf/2610.28286v1)
- **Categories:** cs.MA, cs.AI, cs.LG, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Teams of large language model (LLM) agents are increasingly applied to complex tasks, but their collaboration protocols are mostly designed empirically, without convergence guarantees. We formalize collaborative problem solving as block optimization: each agent improves one part of a shared solution, guided by its local objective plus a correction for how its changes affect the other parts. A coordinator checks every proposal against the global objective and merges proposals that do not interfere with each other. We prove linear convergence up to an error floor that vanishes when the corrections are exact. Interfering proposals can also be merged once their combination has been checked; the rate then depends on how well the proposals actually combine, not on worst-case interactions. With GPT-OSS-120B agents on robot routing, a three-agent team finds collision-free plans in every run, better than those of a single agent that controls all robots. On a larger routing task, a six-agent team completes its search about twice as fast as the single agent (in median). Merging the best checked combination of proposals, rather than only proposals that do not interfere, cuts the team's search time by about 30%. With constants measured on the runs, our convergence bound holds in every round and follows the observed progress. We also test the theory on query planning in SQLite and on a synthetic task.

</details>


### 138. ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents

- **Authors:** Jinhao Hu, Bardia Mohammadi, Mofasshara Binte Rafique, Lars Henning Klein, Akhil Arora, Ashvin Goel, Laurent Bindschaedler
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28093v1](http://arxiv.org/abs/2610.28093v1)
- **PDF:** [https://arxiv.org/pdf/2610.28093v1](https://arxiv.org/pdf/2610.28093v1)
- **Categories:** cs.CR, cs.AI, cs.OS


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents keep long-term memory, much of which comes from web pages and tool results. Agent harnesses, the software that runs the model, do not record who may act on this memory, so an instruction hidden in a fetched page can be treated as the user's own instruction. We propose ClawMMU, a protection layer that labels every piece of memory with its owner, scope, origins, and authority. ClawMMU checks these labels whenever content enters the model's context, is written to storage, returns from storage, or drives a tool call. Its central rule is that information may rise in authority, but authority never lifts itself. Because the checks depend on where content came from, not on what it says, memory attacks become classical protection faults that the harness stops even when the model is fooled.

</details>


### 139. Reinforcement learning for hardware acceleration and system-level optimization on FPGA and integrated-circuit platforms: A survey

- **Authors:** Hamza Kheddar
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.28699v1](http://arxiv.org/abs/2610.28699v1)
- **PDF:** [https://arxiv.org/pdf/2610.28699v1](https://arxiv.org/pdf/2610.28699v1)
- **Categories:** cs.LG, cs.AI, cs.AR, cs.PF, cs.RO, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) enables adaptive and autonomous decision-making in embedded, edge, and heterogeneous computing systems. Field-programmable gate arrays (FPGAs) and integrated circuits (ICs) offer low latency, energy efficiency, and architectural flexibility for RL deployment, while introducing challenges in resource constraints, implementation complexity, and hardware-algorithm co-design. This review surveys more than 100 studies on RL implementations across FPGA and IC platforms, emphasizing architectures, implementation strategies, performance evaluation, and applications. The literature is organized by RL family, including model-based Markov decision processes, classical value-based methods, deep RL, actor-critic, policy-gradient, and multi-agent approaches. We further classify studies by abstraction level, hardware realization strategy, and application domain, examining how RL algorithms map onto reconfigurable and fixed hardware. Unlike surveys restricted to particular algorithms or platforms, this work provides a unified analysis of FPGA and IC implementations, covering acceleration, reconfigurable architectures, energy-aware control, and system-level optimization. Comparative assessments consider resource utilization, latency, throughput, power consumption, and reported performance gains. Finally, we identify recurring architectural patterns, practical limitations, open challenges, and research directions for efficient RL-driven hardware systems. The survey offers a consolidated reference for researchers developing and evaluating RL solutions on specialized hardware.

</details>


### 140. Self-Evolving Static Analysis via LLM Pseudo-Labeling

- **Authors:** Rui Melo, Andre Duarte, Aditya Oke, Shubham Gandhi, Nachiket Kotalwar, Rui Abreu, Lei Li, Carolyn Rose
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.30184v1](http://arxiv.org/abs/2610.30184v1)
- **PDF:** [https://arxiv.org/pdf/2610.30184v1](https://arxiv.org/pdf/2610.30184v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Security bugs often slip past static analysis not because they are impossible to detect, but because detection rules have not yet been written for the code in front of us. New frameworks, APIs, and coding idioms continually create such gaps, leaving developers to discover failures and manually encode new rules. We present SESAA, a framework in which an Large Language Model (LLM) agent starts from no rules and iteratively evolves a set of readable and auditable joern queries.
  The agent receives feedback only from a second LLM critic, which inspects flagged and unflagged code to identify likely false alarms and suspected misses, without access to ground-truth labels. The agent then uses this feedback to revise its queries. On the OWASP Benchmark for Python, SESAA reaches a mean F1 of 0.742 across 8 independent runs, well above the default configurations of five widely used tools and comparable to the strongest of them once it is tuned with access to ground-truth labels that SESAA never sees. In a pilot on real-world Python projects, queries induced from code available before a vulnerability was introduced detect 10 of 19 subsequent CVEs, including 9 detected by rules written for the same repository.
  The resulting detector is a set of executable, human-readable queries that engineers can inspect, modify, and run independently. These results suggest that LLM agents can turn static-analysis rule maintenance from a manually authored process into an iterative process of automated discovery and repair.

</details>


### 141. Quantum-JEPA: Quantum Born Priors for Latent-Action JEPA World Models

- **Authors:** Zhiyuan Liu, Sicheng Liu, Haiyu Wu
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27921v1](http://arxiv.org/abs/2610.27921v1)
- **PDF:** [https://arxiv.org/pdf/2610.27921v1](https://arxiv.org/pdf/2610.27921v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

A single observation can admit several plausible futures, making uncertainty an essential part of world modelling. However, quantum generative models remain underexplored for this task. We introduce Quantum-JEPA, a latent-action JEPA framework that learns distributions of future representations using a conditional quantum Born prior. Circuit measurements generate binary latent actions, which a shared predictor maps to alternative future representations. We train the quantum prior through the quality and diversity of these predictions using a sampled energy objective. Our model learns distinct continuations on constructed multimodal tasks and captures latent-action correlations that support coordinated multi-agent futures. On D3IL, a benchmark of diverse human demonstrations, our trained models generate multiple obstacle-crossing routes from a common starting point without observed motion. On the controlled tasks, our classical and quantum prior implementations improve prediction validity and distributional fidelity over the evaluated variational baselines. Our quantum priors combine competitive predictive quality with a parameter-efficient sampling structure: they avoid an exponentially sized categorical output layer while supporting correlated latent actions. We further validate finite-shot parameter-shift training, including training with readout noise. Unlike most prior work, which focuses on simulation, we also verify the feasibility of inference with trained priors on a real QPU. These results establish a trainable quantum component for JEPA future prediction and a basis for exploring quantum-enhanced world models at larger scales.

</details>


### 142. LatBridge: Efficient and Stable Model Replacement in Latent-Communication Multi-Agent Systems

- **Authors:** Jiajun Zhu, Haobo Li, Zixin Chen, Huamin Qu, Wenshuo Zhang
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27813v1](http://arxiv.org/abs/2610.27813v1)
- **PDF:** [https://arxiv.org/pdf/2610.27813v1](https://arxiv.org/pdf/2610.27813v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems rely on communication to complete tasks, and latent communication passes continuous representations to reduce text generation and re-encoding. However, multi-agent systems must reconfigure agent models, whereas existing latent-communication methods are built for fixed model combinations, so their interfaces may fail after replacement. Our pilot study confirms this interface failure and identifies the requirement for interface reuse after model replacement. We present LatBridge, which connects agent models through a shared Bridge and separate interfaces under a shared latent-communication protocol. After agent model replacement, LatBridge reuses unchanged interfaces, selects matching low-rank interfaces, and combines them through the Bridge, training only missing ones with all models frozen. The Bridge processes source representations in the basic mode and constructs target input without autoregressive generation in the accelerated mode. Experiments support effective communication after model replacement, with mean basic-mode accuracies of 14.8% on MATH and 27.3% on ALFWorld next-action prediction across eight small-model configurations. Analyses examine the factors supporting task accuracy and communication efficiency.

</details>


### 143. Toward Agentic AI for the 6G Physical Layer: From Algorithm Discovery to Verified Baseband Silicon

- **Authors:** Eric Mittag, Lukas Brechtel, Maximilian Stark, Hans D. Schotten
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27797v1](http://arxiv.org/abs/2610.27797v1)
- **PDF:** [https://arxiv.org/pdf/2610.27797v1](https://arxiv.org/pdf/2610.27797v1)
- **Categories:** cs.AI, cs.NI, eess.SP


> Summary unavailable.


<details>
<summary>Abstract</summary>

6G will be designed faster than it can be built: AI-driven search already proposes physical-layer algorithms at machine speed, while carrying a single one onto embedded baseband silicon remains specialist work. That silicon imposes hard memory and numeric limits, but also exposes cost structures a GPU lacks, and a design flow that never runs on the target sees neither. We present an agentic workflow in which an LLM coding agent implements algorithms on a commercial baseband SoC, optimizes them down to agent-written vector assembly, and validates them on silicon. The agent is guided by a knowledge base of measured platform facts, checked at every step against evaluators it is instructed never to edit, and metered per phase. We showcase the workflow on an AI-discovered orthogonal time frequency space (OTFS) detector portfolio on the open 6G4All platform. It yields twelve kernels that run cycle-exactly on silicon, their optimized versions at 18k-405k cycles (30-660 $μ$s) per frame. It also yields a new detector shaped by the chip's measured costs that needs 13.9% fewer cycles than the port of the discovered detector while matching its error rate, with a measured edge our evaluation cannot statistically resolve, a structure that a hardware-blind search objective had no reason to find. What is not specific to OTFS is the workflow: an LLM agent exploring an implementation space under real hardware limits, with the cost of every choice measured rather than assumed.

</details>


### 144. GRADUS: Discovering and Recovering Agent Lessons from the Environment's Latent Syllabus

- **Authors:** Qing Ping, Wei Yang, Panpan Xu, Johannes Kirmayr, Lukas Stappen, Junjie Tang, Jun Huan
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27781v1](http://arxiv.org/abs/2610.27781v1)
- **PDF:** [https://arxiv.org/pdf/2610.27781v1](https://arxiv.org/pdf/2610.27781v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Training LLM agents for policy-constrained tool environments, such as an airline backend with booking, refund, and cancellation policies, requires tasks that exercise the environment's rules individually and in combination. Existing synthesis pipelines let a model propose tasks and retain only those it immediately solves, biasing training data toward easier behaviors. We introduce Gradus (Graded Rungs of Ascending Difficulty from an Underlying System), which decouples what a task should teach from the concrete task and solution used to teach it. Without seed tasks, Gradus treats a fixed environment as a latent syllabus, extracting guarded behavioral operators that capture how actions depend on current conditions and how their effects reshape subsequent decisions. It composes these operators into increasingly demanding tasks while using corpus-level feedback to target missing outcome combinations. Crucially, Gradus jointly calibrates tasks and solutions against the environment: execution feedback identifies which side to refine while preserving the intended behavioral requirements. Verification thus becomes a recovery signal rather than a terminal filter, coupling coverage-guided exploration with the preservation of difficult examples. From off-the-shelf backbones, the resulting curriculum lifts a 30B model from 59% to 89% on $τ^2$-Bench and from 47% to 83% on CAR-Bench with an Opus 4.5 proposer, and to 76% and 62%, respectively, with an open-weight Qwen3-235B proposer. These results show the value of jointly controlling which behaviors are explored and which survive into verified training data.

</details>


### 145. RITE: Evaluating End-to-End Resilience to Silent Tool Errors in E-Commerce Agentic Systems

- **Authors:** Wenshuo Zhang, Yuquan Lin, Yushi Sun, Yishi Lin, Rui Sheng, Peng He, Han Gao, Wang Jikai, Yifeng Rong
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27777v1](http://arxiv.org/abs/2610.27777v1)
- **PDF:** [https://arxiv.org/pdf/2610.27777v1](https://arxiv.org/pdf/2610.27777v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using LLM agents increasingly answer e-commerce queries through multi-step tool interactions. The expected output of a tool call can shift between agent development and execution, allowing a plausible but incorrect value to be returned without an explicit failure signal. These silent errors may propagate through subsequent decisions into final answers. To study agents' resilience across this end-to-end process, we formulate Silent-error Resilience Task, an interactive task that evaluates whether they complete the original query after a silent error corrupts an intermediate state. We introduce RITE, a benchmark built from human-authored industrial workflows and production-log-derived inputs. To enable controlled and reproducible evaluation, we use a semantic error taxonomy to inject errors into fixed workflow prefixes, freeze recorded tool behavior, and let agents continue freely. It contains 167 matched units across nine e-commerce workflows, yielding 501 silent-error, correct-value, and explicit-failure instances. Across 10 recent LLMs, silent errors roughly halve task success and are consistently harder than explicit failures. Recognition, use of an available verification path, and integration of the resulting evidence form successive bottlenecks. We also propose a light State Checker as an intervention to test whether resilience can be improved.

</details>


### 146. S$^2$-MAS: A Society-Scale Multi-Agent Simulation Framework with 500 Million Household Persona Agents

- **Authors:** Yang Li, Yike Wang, Di Wan, Chujun He, Zongsi Xu, Yitao Yu, Quanfeng Lu, Xiyu Chen, Sheng Zhong, Deng Binjie, Yichen Guo, Zhenwei Guo, Hou Jun, Kunhan Guo, Weihao Lin, Tuo Zhou, Hai Liu, Chenwei Wu, Jianyuan Zhong, Xilin Dai, Ye Luo
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27746v4](http://arxiv.org/abs/2610.27746v4)
- **PDF:** [https://arxiv.org/pdf/2610.27746v4](https://arxiv.org/pdf/2610.27746v4)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Simulating economic responses at society scale requires agents whose decisions reflect household circumstances. We introduce S$^2$-MAS, a society-scale multi-agent simulation framework built on 500 million synthetic household personas grounded in real-survey data. Its Genese engine separates decisions from state updates, while reusable financial scenarios and application ledgers track consumption, cash, debt and payments. Trained with SFT + RLCD on 2.93 million examples, sharp-421m-mlx achieves 74.55% accuracy and 38.37% question-macro F1 on one-shot consumer financial-choice tasks derived from held-out survey responses. Its accuracy exceeds GLM-5.3-Flash, Jev 1.13, DeepSeek-V4.1-Flash, GPT-6-Luna and GPT-6-Astra in the common benchmark (full test for the first four; matched 500-group sample for Astra). We evaluate eight financial task families and simulate 12 million distinct household agents in paired purchase-funding conditions. Jointly raising purchase goals and approved credit limits increases consumption, with responses differing across age and income groups. Education, employment and household-size differences persist after age-income standardization and mainly reflect transitions from deferral to purchase. Asset and debt groups differ in cash drawdown, repayment and closing debt. S$^2$-MAS links heterogeneous household decisions to evolving consumption, cash and repayment paths, supporting economic experiments across household groups and population scales.

</details>


### 147. Memory as Code: Declarative Retrieval over Codified Long-Term Memory

- **Authors:** Aoting Zeng, Yuxin Du, Jianwei Wang, Yizhang He, Shan Jiang, Xuemin Lin, Kai Wang
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27700v1](http://arxiv.org/abs/2610.27700v1)
- **PDF:** [https://arxiv.org/pdf/2610.27700v1](https://arxiv.org/pdf/2610.27700v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

In long-term memory systems, memories are constructed from interaction histories and retrieved in response to queries, enhancing the reasoning ability of LLM agents. In complex scenarios, facts are scattered across sessions and their relationships evolve over time, making it difficult for existing memory systems to compose them to adapt to diverse queries. Motivated by the modularity and composability of code, we propose Memory as Code (MaC), a unified memory framework that jointly designs memory construction and retrieval through a shared code abstraction. MaC couples codified construction, which establishes executable memory abstractions, with declarative retrieval, which translates queries into structured retrieval programs. Specifically, codified construction builds a three-layer executable memory structure that progresses from an atomic function layer, through a relational layer, to a modular composition layer. Declarative retrieval recasts retrieval from relevance-based fact selection into declarative query processing over memory. Experiments on LoCoMo and LongMemEval show relative gains of up to 15.91% in overall LLM-judge accuracy over the strongest baseline in each setting, while substantially reducing token consumption, highlighting the effectiveness of memory as code for long-horizon memory tasks.

</details>


### 148. Does Multi-Agent Collaboration Pay When Agents Serve Users? Testing Agent Scaling in Dual-Control Settings

- **Authors:** Ethan Yang, Xiangcheng Shi
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27655v1](http://arxiv.org/abs/2610.27655v1)
- **PDF:** [https://arxiv.org/pdf/2610.27655v1](https://arxiv.org/pdf/2610.27655v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) built from language models are deployed on the premise that collaboration beats a single-agent system (SAS), yet when it pays is unclear. The most systematic study to date gives a capability-saturation rule: coordination helps while the SAS is weak and hurts once it is strong, with the crossing near 45% single-agent accuracy. That rule was derived on autonomous benchmarks, where no user takes part. We test it where agents now work: in conversation with a user under a written policy, on $τ^2$-bench, the dual-control benchmark. On its airline, retail and telecom domains we compare the stock SAS with a centralized MAS built from the same model for six models from three families, over about 7,950 simulated conversations, with one completion-token ledger per episode per system. The study was pre-registered with a public change log; the MAS is reported as built, with one validity bar unmet (its planner never saw the tool schemas). Under a fixed simulated user no cell shows a MAS benefit: the MAS is worse in 12 of the 13 valid cells and tied in the thirteenth, and the fitted gain is negative across the observed capability range (weighted mean -28 points, 95% CI [-44, -12]). On the two cells where the rule predicts a benefit, the MAS loses by 13 and 22 points, and without a budget ceiling it at best draws level at 5.5 times the SAS's token spend. The one gain appears on the cell nearest 45%, under a second simulator. Whether the gain declines with capability is unresolved (slope -0.41, 95% CI [-1.51, +0.68]), because model-by-domain effects dominate. The MAS does not detectably reduce wrongful database writes; it converts other failures into budget exhaustion and inaction. For agents that serve people, the SAS is the default; a multi-agent design must show compute-matched evidence from the setting itself. We release all trajectories, ledgers, prompts and code.

</details>


### 149. Local Allow, Global Deny: Why Per-Action Authorization Does Not Compose in LLM Agents

- **Authors:** Anmol Pandey, Aditya Jain, Liang Chen, Carsten Maple
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27620v1](http://arxiv.org/abs/2610.27620v1)
- **PDF:** [https://arxiv.org/pdf/2610.27620v1](https://arxiv.org/pdf/2610.27620v1)
- **Categories:** cs.CR, cs.AI, cs.LO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous LLM agents act through tools under per-action authorization: a local guard screens each tool call in isolation. We show that local authorization does not compose into global authorization. A compositional authorization failure (CAF) is a locally authorized execution, or a pair of locally authorized executions, that violates a global policy spanning intent, purpose, provenance, consent, and delegation. We characterize CAFs along two axes, expressiveness (single-trace safety versus relational k-safety) and observability (a ladder of monitor profiles). Our central result is an impossibility: relational purpose violations form a 2-safety hyperproperty with no per-trace locus of blame, so a per-action monitor that never raises a false alarm detects none of them, independent of the underlying model or decision procedure; they become visible only under cross-execution monitoring, which none of the six guardrails we survey implements. We make this constructive with AL-SYNTH, a SAT/SMT synthesizer (using no language model) that emits minimal CAF witnesses, each checked against an exhaustive oracle. The empirical signature is sharp: across nine LLM judges the per-action view approves the synthesized witness almost without exception, blocking it at a rate comparable to a benign control, yet the same models flag it when shown the two executions together. Per-action authorization is therefore structurally insufficient for relational policy conjuncts not reducible to single-trace safety: to bound them, a monitor must compare executions or accept false alarms.

</details>


### 150. Auditing the Product, Not the Recursion: The Evaluation Evidence Behind Recursive Self-Improvement Claims

- **Authors:** Zihan Chen, Di Zhu, Lei Nico Zheng
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27610v1](http://arxiv.org/abs/2610.27610v1)
- **PDF:** [https://arxiv.org/pdf/2610.27610v1](https://arxiv.org/pdf/2610.27610v1)
- **Categories:** cs.LG, cs.AI, cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recursive self-improvement (RSI) promises AI systems, such as self-evolving LLM agents, that become better at producing further improvements. Evaluating this promise requires separating product claims about the final system from process claims about the improvement process itself. Existing surveys specify the evidence these claims require, but how often studies report that evidence remains unmeasured. We examine this question through full-text coding of 114 eligible studies in a reproducible arXiv search frame frozen in October 2026, including 90 that describe their own systems as RSI. The codebook links claims to evaluation designs. Independent human coding, third-reader adjudication, and a separate blind coding of improver comparisons assess coding reliability. Among the 90 RSI studies, 90% report product evaluation beyond development tasks under a broad criterion that includes partial or unstated separation, while 60% report evaluation on tasks unused for selection. Only 22% audit two or more reruns of the full loop. In a human-coded random sample, the RSI studies show the same contrast: 45% evaluate on tasks unused for selection and 14% audit two or more reruns. Of the 26 studies claiming a better improvement procedure, 23 report a related comparison, but only 4 compare earlier and later procedures from identical starting artifacts at a matched budget. Across these results and a comparison set of established works, evidence for repeatability and improved procedures remains less developed than product evaluation. Three propositions explain how selection effects, shared evaluator errors, and changes in system state limit what product evaluations can establish. Together, the findings support a claim-indexed reporting standard that connects each claim to the evaluation design needed to test it.

</details>


### 151. Beyond Experience: Knowledge-Guided Evolution for NPU Kernel Generation

- **Authors:** Xi Chen, Ming Shen, Haotian Yan, Ruoyu Sun, Tianjun Yao
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27588v1](http://arxiv.org/abs/2610.27588v1)
- **PDF:** [https://arxiv.org/pdf/2610.27588v1](https://arxiv.org/pdf/2610.27588v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents have become capable kernel engineers on mainstream GPU stacks, but they struggle on emerging accelerators such as Ascend NPUs, whose programming model is barely represented in pretraining data. Recent NPU agents address this gap largely through experience: they accumulate memory from their own generation and optimization trials and reuse it on later tasks. We argue that experience alone is not enough for kernel generation. An agent can only remember what it has tried, and it rarely tries a mechanism it does not know. As a result, such memory offers little help when a new operator calls for a different mechanism, and even familiar operators raise unseen situations as optimization proceeds. We present ASCENDEVOLVE, which grounds every step of an evolutionary kernel search in a large external knowledge base built from platform documentation, toolkit headers, and operator repositories. Because this corpus far exceeds any context window, ASCENDEVOLVE indexes it and routes each agent to a small, task-specific slice of evidence instead of the corpus itself. The retrieved knowledge seeds diverse implementation strategies, guides repair when a candidate fails, and constrains how strong candidates are recombined. On 53 Ascend C operators from CANN-Bench spanning four difficulty levels, ASCENDEVOLVE achieves an overall score of 71.39, improving over Reflexion and OpenEvolve by 11.6% and 17.2%.

</details>


### 152. The Show-Up Attack: When Subagents Win Over Their Supervisor

- **Authors:** Maosen Zhang, Jianshuo Dong, Yutong Zhang, Jie Zhang, Tianwei Zhang, Han Qiu
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27574v1](http://arxiv.org/abs/2610.27574v1)
- **PDF:** [https://arxiv.org/pdf/2610.27574v1](https://arxiv.org/pdf/2610.27574v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems are increasingly deployed to coordinate multiple large language model (LLM) agents. However, this also creates new attack surfaces: malicious agents may have chances to exploit the coordination. In this paper, we propose and study the \textit{show-up attack}, in which a malicious subagent manipulates the supervisor into involving it in tasks beyond its assigned scope. To evaluate this risk, we propose SUA-Arena, which implements 6 attack strategies and contains 188 test cases. Then, we evaluate 6 frontier LLMs and find that all of them are vulnerable to show-up attacks. For example, GPT-5.6-Sol as a supervisor suffers an ASR of up to 0.93. Mitigation strategies such as prompting and restricted communication fail to reduce the risk consistently. These results show that multi-agent systems need explicit mechanisms for enforcing authority boundaries.

</details>


### 153. RaspAssistant as an Agentic Framework for Automating Adsorption Simulation Research in Porous Materials

- **Authors:** Marko Petković, Susanne Gooijer, José Manuel Vicent-Luna, Vlado Menkovski, Sofía Calero
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27572v1](http://arxiv.org/abs/2610.27572v1)
- **PDF:** [https://arxiv.org/pdf/2610.27572v1](https://arxiv.org/pdf/2610.27572v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Porous-material adsorption studies require coordinated structure preparation, force-field selection, simulation, validation, and interpretation, making end-to-end automation difficult. We test whether RaspAssistant, a hierarchical multi-agent framework, can carry an adsorption study from force-field preparation through validation and downstream separation analysis. Across twelve multi-agent workflow-reproduction runs spanning four adsorption and separation benchmarks, overall scores ranged from 8.50 to 10.00 on a rubric evaluating workflow correctness, simulation validity, and analysis consistency. In a separate eight-case force-field extraction benchmark, the mean weighted score was 0.967, combining parameter agreement and RASPA readiness. In open-ended studies, the system diagnosed and refined an acetylene force field and, after validating a CO$_2$ force field against MFI experiments, screened 197 pure-silica zeolites that passed automated input checks. These results demonstrate autonomous workflow execution after task specification and input provision: RaspAssistant coordinates, validates, adapts, and documents extended adsorption-simulation workflows while exposing model sensitivity and methodological limitations for expert review.

</details>


### 154. Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment

- **Authors:** Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang, Tianshi Li
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27548v2](http://arxiv.org/abs/2610.27548v2)
- **PDF:** [https://arxiv.org/pdf/2610.27548v2](https://arxiv.org/pdf/2610.27548v2)
- **Categories:** cs.AI, cs.CR, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

When an LLM agent acts on behalf of a user, it is expected to act within the authorization scope the user grants. Existing agent evaluations largely measure task completion or harmful consequences and can therefore overlook actions that violate this delegation without producing conventional safety or privacy harms. We introduce AuthorizationBench, a benchmark of authorization alignment grounded in documented real-world cases. A scalable construction pipeline produces 286 executable tasks spanning situational triggers, the presence or absence of direct harmful consequences, and ten application domains. We execute every task with four models at two reasoning-effort settings across three agent harnesses in an authorization-aware sandbox that keeps authorized and out-of-authorization paths executable and observable, yielding 6,864 trajectories. Agents act out of authorization in 19.2% of trajectories, with rates ranging from 10.5% to 26.6% across the 24 configurations. Task completion does not imply authorization. Increasing reasoning effort leaves the aggregate rate nearly unchanged, with effects varying across models. On controlled pairs, agents act out of authorization at similar rates with (17.9%) and without (20.8%) direct harmful consequences, and more often under benign pressures than malicious injections (23.5% versus 17.6%, p=0.002). Our results show that task capability, additional reasoning, and consequence-oriented safety evaluation do not by themselves ensure authorization alignment. Moreover, agents that consult the principal before completing a task exhibit lower rates of out-of-authorization behavior (14.0% versus 21.6%, p<0.001), pointing to a tension between agent autonomy and preserving users' decision authority that calls for further human-centered study. Dataset and code are available at https://github.com/PEACH-Research-Lab/AuthorizationBench .

</details>


### 155. Automated Multi-Agent Organization Design: From Architecture Search to Organizational Learning

- **Authors:** Shao-Jun Xia, Yuner Zhang, Huixin Zhang, Di Wang, Yifan Jiang, Liangxi Liu
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27531v1](http://arxiv.org/abs/2610.27531v1)
- **PDF:** [https://arxiv.org/pdf/2610.27531v1](https://arxiv.org/pdf/2610.27531v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic system design is increasingly shifting from hand-crafted prompts and workflows toward automated search over agentic programs and interaction structures, with multi-agent systems receiving growing attention. Yet a central question remains unresolved: when does an automatically generated multi-agent structure exhibit a functionally meaningful division of responsibility? We argue that automated multi-agent design should move beyond searching for effective architectures toward identifying which responsibilities are functionally necessary, how they should be allocated, and when they should change. To explore this, we propose Automated Multi-Agent Organization Design (AMOD), which treats organization itself as a first-class design object, explicitly modeling how agent teams are composed, what functional responsibilities the agents assume, how they coordinate, and how collective decisions are made. We formulate AMOD as an execution-driven design loop. For each task, an automated designer instantiates an organization by assigning functional responsibilities and coordination rules to a set of agents. After execution, task outcomes, intermediate artifacts, and interaction traces are examined to identify which responsibilities may be missing, duplicated, or ineffective, and the organization is revised accordingly. We also propose testing discovered responsibilities by removing them, replacing them with generic roles, or changing their assignment under matched resource budgets, with complementary evaluations. AMOD provides a principled foundation for evidence-based and adaptive multi-agent organization design.

</details>


### 156. Complete Street Design informed by Multi-Agent Simulation

- **Authors:** Sharika J. Hegde, Amirmohammad Khakpour, Pedram Beigi,  Yu,  Nie, Hani S. Mahmassani
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27509v1](http://arxiv.org/abs/2610.27509v1)
- **PDF:** [https://arxiv.org/pdf/2610.27509v1](https://arxiv.org/pdf/2610.27509v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Objectives: Complete Street design is currently guided largely by qualitative principles despite the increasing complexity of multimodal urban traffic. This paper develops a microscopic simulation framework for quantitatively evaluating alternative street designs by explicitly representing heterogeneous road users, including Autonomous Vehicles (AVs), Connected Vehicles (CVs), Human-Driven Vehicles (HDVs), pick-up and drop-off (PUDO) services, and micromobility users. The framework jointly evaluates mobility and safety within a unified testbed. Methods:The framework enriches microscopic simulation with behavioral models for heterogeneous road users. It explicitly captures lateral movements, parking maneuvers, pedestrian crossings and jaywalking, and shared-lane bicycle and scooter interactions. Safety is quantified using a conflict severity measure grounded in collision physics, while candidate street layouts are optimized using a genetic algorithm. Findings: Applied to a segment of Belmont Avenue in Chicago, Illinois, the framework shows that dedicated bicycle lanes reduce conflict severity at the expense of vehicular throughput. Increasing AV penetration mitigates congestion by reducing traffic shockwaves while improving interactions with pedestrians relative to CVs and HDVs. The optimization framework efficiently identifies Pareto-efficient street layouts that balance mobility and safety. Novelty: The proposed framework integrates heterogeneous behavioral modeling, physics-based conflict assessment, stochastic performance evaluation, and design optimization within a single quantitative framework for Complete Street design. Practical Applications: The framework provides transportation planners with a predictive virtual testbed for evaluating street designs and quantifying the tradeoff between mobility and safety before implementation.

</details>


### 157. The More the Better? A Comparison of Single- and Multi-Agent LLM Setups on a Financial Review Task

- **Authors:** Pei Liu
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27488v1](http://arxiv.org/abs/2610.27488v1)
- **PDF:** [https://arxiv.org/pdf/2610.27488v1](https://arxiv.org/pdf/2610.27488v1)
- **Categories:** cs.AI, cs.CE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Practitioner guidance holds that a large language model reviews a document better when the work is divided among agents. We test a narrow form of it in a controlled comparison of single-agent and multi-agent setups on a financial task, reviewing credit assessment memos against requirements. One agent checks six requirements in one call. A team of three on the same model checks the same memo, two requirements each, in the same words, with no roles or later stage. Labels are known for every requirement on 300 synthetic memos, so misses and false alarms are measured separately. Two primary predictions are tested on four models at a Bonferroni-corrected level. Under an instruction to decide each requirement once, the team catches 0.08 to 0.10 more of the defects that carry an explanation on the three models whose single agent misses some, at the corrected level on two. It raises more false alarms on all four, at the corrected level on three. Balanced accuracy, an exploratory measure, changes by 0.02 or less, and the team uses 2.2 to 2.4 times the tokens. Showing each agent the requirements it was not given reduces the added false alarms on the two Claude models, at the corrected level on one. In exploratory comparisons, sampling the single agent three times and flagging on any draw gives higher balanced accuracy than the team on those models, and the team's results depend on the instruction.

</details>


### 158. Runtime Control for AI Agents: Closing the Evaluation--Execution Gap in Operational Workflows

- **Authors:** Jayesh Bhadane, Ramachandra Yerramsetti, Rajesh Gupta, Sumit Kumar
- **Published:** 2026-10-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27480v1](http://arxiv.org/abs/2610.27480v1)
- **PDF:** [https://arxiv.org/pdf/2610.27480v1](https://arxiv.org/pdf/2610.27480v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language-model agents increasingly participate in operational workflows where approvals, binds, and payments create commitments. An approval valid when issued may no longer authorize execution after relevant facts, evidence, policy, or authority change. We call this the evaluation--execution gap. We specify a state-bound runtime assurance layer that separates probabilistic measurement from deterministic adjudication, binds an execution allowance to the decision-relevant basis of an approval, invalidates that allowance after relevant logged changes, and rechecks admissibility at dispatch. This distinguishes the continued validity of a prior approval from a current-state policy check. We describe eight failure modes, an assurance model, a reference architecture, and prospective interventions with retrospective remediation. In a scripted 42-case replay, the state-bound configuration identifies 15 later-invalidated approvals that a deliberately non-re-evaluating point-in-time comparator does not revisit; it holds 14 affected actions before dispatch and compensates one landed effect. These results illustrate behavior under the stipulated policies and event orders, not superiority over dispatch-time enforcement designs or production effectiveness. Under explicit interception, ingestion, dependency, and serialization assumptions, the model establishes dispatch-time validity within the registered execution surface.

</details>


### 159. More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents

- **Authors:** Ruhan Wang, Kishan Panaganti, Dongruo Zhou
- **Published:** 2026-10-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27406v1](http://arxiv.org/abs/2610.27406v1)
- **PDF:** [https://arxiv.org/pdf/2610.27406v1](https://arxiv.org/pdf/2610.27406v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents can improve across tasks without updating model parameters by storing experience from their own executions in external memory and reusing it to guide later decisions. A central design question is whether to retain only observed trajectories and outcomes or also the rules, summaries, and skills inferred from them. Retaining these abstractions allows agents to reuse strategies without repeatedly deriving them from raw trajectories. However, errors in stored abstractions can propagate to subsequent decisions through retrieval and reuse. They can also shape execution trajectories, which then become the basis for new abstractions that reproduce the original errors. We term this feedback mechanism error reproduction: errors are regenerated through a cycle of abstraction, execution, and re-abstraction, extending their persistence beyond direct reuse of the original faulty knowledge. We propose Anti-Persistence, a memory design that accumulates trajectories and outcomes while reconstructing task-specific guidance on demand. An adaptive selector uses prior outcomes to decide whether and how to synthesize guidance, which is discarded after execution. This prevents its direct reuse as a stored object, although indirect feedback through retained trajectories remains possible. Across different benchmarks and backbones, Anti-Persistence achieves higher overall held-out success and the lowest average LLM-call cost among the evaluated memory designs. These results support separating experience accumulation from abstraction persistence in memorybased self-improvement.

</details>


### 160. On the LLM Verification for Argument Graph Generation

- **Authors:** Jakub Bąba, Jarosław A. Chudziak
- **Published:** 2026-10-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27361v1](http://arxiv.org/abs/2610.27361v1)
- **PDF:** [https://arxiv.org/pdf/2610.27361v1](https://arxiv.org/pdf/2610.27361v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems can formalize natural-language argumentation end-to-end, turning plain text into structured graphs by classifying components, connecting them with relations, and enriching the resulting graphs into formal models. Quality assurance for those graphs is almost always another LLMs: a reviewer, judge, or critic agent. On the other side, in adjacent neuro-symbolic fields, such generated output is often verified symbolically by external checks and solvers. In this work, we argue that in argument graph verification, the allocation should be similar, and based on what each instrument can guarantee. We propose layered verification: starting from deterministic checks, moving to solver-based and LLM reviews, and utilizing debate only under uncertainty, leaving human judgment for what no other instrument can decide. We ground our principle with a study on human-annotated graphs with injected structural defects. An LLM reviewer detects them at near-ceiling recall, including cycles in the support relation, but it objects to almost one in a ten correct graphs, even though it should not, happens to be inconsistent in verdict on identical inputs and is significantly slower than the equivalent exact check. It shows that while LLM reviewer does not lack the ability to detect structural defects, it is worth having a deterministic verification gates.

</details>


### 161. An LLM-Based Agent for Legal Compliance Assessment: Architecture, Memory, and Evaluation in a Canadian and Quebec Context

- **Authors:** Soukaina Alaoui Ismaili, Jean-Sebastien Dessureault
- **Published:** 2026-10-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27347v1](http://arxiv.org/abs/2610.27347v1)
- **PDF:** [https://arxiv.org/pdf/2610.27347v1](https://arxiv.org/pdf/2610.27347v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Checking whether a text complies with a body of law is slow when done by hand and fragile when done with keyword rules. This paper presents ComplianceAgent, the legal compliance sub-agent of COMPASS, a multi-agent framework that evaluates texts along four axes: digital sovereignty, carbon impact, compliance, and ethics. The agent relies on a large language model that scores a text on a fixed rubric, grounds its judgment in a reference legal corpus, and, when the score falls at or below a critical threshold, runs a corrective chain made of self-healing rewrites, a compliance label, an explainability report, and escalation to a human reviewer. We describe what the language model does at each step, how the memory of the agent is organized, and how the same implementation can be pointed at different reference corpora. We evaluate the agent in a Canadian and Quebec context, on a corpus of thirteen legal instruments that brings together federal and provincial texts, international treaties, and municipal documents of the City of Trois-Rivières. The evaluation relies on a hand-annotated gold standard of fifteen texts and combines classification metrics, a repeated-query stability test, retrieval precision, and a composite score. On this gold standard the agent separates every conforming text from every non-conforming one, its scores remain stable under repeated queries, and the index returns relevant passages.

</details>


### 162. Evolving Self-tuning Benchmarks for Long-Horizon Tool Use

- **Authors:** Hyunji Alex Nam, Michael Dennis, Natasha Jaques, Minsuk Chang
- **Published:** 2026-10-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27307v2](http://arxiv.org/abs/2610.27307v2)
- **PDF:** [https://arxiv.org/pdf/2610.27307v2](https://arxiv.org/pdf/2610.27307v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

For AI assistants to move beyond simple chat interfaces and reliably assist users with applications like Gmail, Venmo, and Slack, we need to improve their tool-use capabilities. However, existing tool use benchmarks are still limited and difficult to scale because they rely on human supervision or are too domain-specific. To make data generation scalable, we propose, TURTLE (Tool Use Related Tasks with Long-Horizon Evolution), an Unsupervised Environment Design (UED) approach to evolve existing tasks using a proposer, a solver, and a feedback generator large language model agents. The proposer is rewarded for difficult yet solvable tasks based on the solver's empirical performance, and the feedback generator summarizes the solver's execution traces for the proposer to exploit. TURTLE produces evolving, self-tuning test suites adaptable to different environment requirements, from supporting user simulators and dense document retrieval to interacting across multiple apps. Empirical results on AppWorld, $τ$-Bench, and AutomationBench using Gemma 4 31B-it show that the evolved tasks target the desired difficulty range (e.g., a 165% increase in the percentage of hard tasks on AppWorld), increase task diversity (in terms of reasoning and simultaneous tool interactions), and elicit a broader range of failure modes than the original tasks.

</details>


### 163. RealControlBench: A Benchmark for Interpretability-Informed Fine-Grained Control of LLMs and Agents

- **Authors:** Xinying Cai, Bin Hu, Mingyu Jin, Qiming Zhang, Yang Ouyang, Bangwei Guo, Minghao Guo, Yutong Yin, Lang Gao, Feijiang Han, Sheldon Yu, Kaiqu Liang, Qingcheng Zeng, Jingcheng Niu, Fan Yang, Wei Cheng, Zhen Xiang, Julian McAuley, Zhaoran Wang
- **Published:** 2026-10-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27295v1](http://arxiv.org/abs/2610.27295v1)
- **PDF:** [https://arxiv.org/pdf/2610.27295v1](https://arxiv.org/pdf/2610.27295v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing steering benchmarks are built around simplified, isolated generation tasks and evaluate a single behavioral attribute under controlled settings that do not reflect the diversity and complexity of practical deployment. As a result, performance on these benchmarks provides only a limited picture of how steering methods perform in the real world. We therefore introduce RealControlBench, a comprehensive benchmark for evaluating fine-grained steering of LLMs and LLM agents across diverse behavioral targets and interaction settings. RealControlBench extends steering evaluation beyond isolated generations to complex, execution-grounded, multi-turn agent interactions, covering five complementary dimensions: instruction-following control, agentic tool-use decision control, reasoning-performance steering, reasoning-length control, and trajectory-conditioned safety awareness. Rather than measuring steering success alone, the benchmark jointly evaluates target controllability and capability preservation, including instruction following, reasoning performance, and downstream agent utility and safety. It further examines whether steering effects remain specific and robust across prompt variations, domains, and model architectures. Our evaluation shows that existing steering methods remain unreliable across realistic control objectives: they often fail to consistently induce the intended behavior and can substantially degrade the model's underlying task performance. These results suggest that strong steering effects in controlled settings do not necessarily translate into reliable control in more realistic evaluations. By providing a unified, model-agnostic steering evaluation framework, RealControlBench aims to support the development of steering methods that are not only effective but also precise, robust, and useful in realistic AI deployments.

</details>


### 164. Vulnerability Analysis for Safe Multi-Agent Reinforcement

- **Authors:** Taozheng Zhu, Shixiong Jiang, Fanxin Kong
- **Published:** 2026-10-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27293v1](http://arxiv.org/abs/2610.27293v1)
- **PDF:** [https://arxiv.org/pdf/2610.27293v1](https://arxiv.org/pdf/2610.27293v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Safe Multi-Agent Reinforcement Learning (SMARL) aims to learn cooperative control policies under prescribed safety constraints. Al- though existing SMARL methods focus on enforcing safety during policy optimization, their vulnerability remains largely unexplored. This paper investigates inference-time observation attacks against SMARL, where an adversary perturbs the observations of a subset of agents, thereby altering the actions produced by their policies. We propose MinMax Attack, an attack framework that jointly selects adversarial target actions for compromised agents while accounting for the Cooperative Resistance of benign agents. We further derive a bound on the induced safety cost and characterize its relation- ship with the Compromised-Agent Budget and the Perturbation Budget. Experiments across multiple safety-critical multi-agent benchmarks and representative state-of-the-art SMARL algorithms show that MinMax Attack induces substantially higher safety costs than existing attack baselines while preserving task reward, thereby reducing its detectability and achieving both attack effectiveness and stealthiness.

</details>


### 165. AutoRedClaw: Automated Red-Teaming for Claw-Style Agents

- **Authors:** Hao Li, Tongyan Hu, Weidi Luo, Shanghao Shi, Xiaogeng Liu, Aiden Suh, Yulong Cao, Ning Zhang, William Yeoh, Yevgeniy Vorobeychik, Chaowei Xiao
- **Published:** 2026-10-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27244v1](http://arxiv.org/abs/2610.27244v1)
- **PDF:** [https://arxiv.org/pdf/2610.27244v1](https://arxiv.org/pdf/2610.27244v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent systems are shifting from task-scoped tool-use agents to persistent, personalized assistants such as OpenClaw. These claw-style agents maintain configuration files (e.g., AGENTS.md), long-term memory, and reusable skills. Once poisoned, this persistent state is repeatedly reloaded into the agent's context, creating persistent threats across tasks and sessions. Existing security evaluation systems struggle to evaluate these complex claw-style systems since they rely heavily on manually constructed test cases and environments, which limits their scale and coverage; in addition, these manually designed cases quickly become outdated as agents evolve, and their evaluation settings leave a gap with how claw-style agents are deployed in practice. To address this, we introduce AutoRedClaw, an automated red-teaming framework that generates end-to-end attacks together with the environments needed to execute them. AutoRedClaw combines a strict quality-checking protocol with execution-based validation to ensure the correctness, realism, and effectiveness of generated samples, and adopts task-driven environment construction to keep costs low. To achieve broad coverage, it organizes generation along risk categories, attack strategies, attack stages, and attack surfaces, and uses experience-guided exploration to steer generation toward under-explored regions. AutoRedClaw achieves an effective attack rate above 30% at less than $0.10 per successful sample. From its outputs, we construct RedClaw-Bench, a 330-case benchmark that yields substantially higher attack success rates (ASRs) than AgentDojo, AgentDyn, and DTap. Across seven harnesses and four frontier models, most agent systems exceed 50% ASR, showing that our red-teaming pipeline provides a strong evaluation signal even for the most advanced agent systems. Our code and benchmark are released at https://github.com/SaFo-Lab/AutoRedClaw.

</details>


### 166. EGI-BENCH: An Enterprise General Intelligence Benchmark Suite

- **Authors:** Zhiwei Liu, Zhujun Lan, Jielin Qiu, Zixiang Chen, Liangwei Yang, Ming Zhu, Akshara Prabhakar, Wenting Zhao, John Emmons, Jason Wu, Shafiq Rayhan Joty, Junnan Li, Shelby Heinecke, Silvio Savarese, Huan Wang
- **Published:** 2026-10-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27234v1](http://arxiv.org/abs/2610.27234v1)
- **PDF:** [https://arxiv.org/pdf/2610.27234v1](https://arxiv.org/pdf/2610.27234v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise adoption of LLMs in agentic workflows is gated by evaluations that span a wide arc of abilities: CRM operations, heterogeneous-document retrieval, personal data understanding, multi-turn planning, tool use, function calling, long-horizon research, and long-context software engineering. These evaluations live today in separate repositories with divergent runners, dependencies, and scoring conventions, which makes cross-benchmark comparison difficult and obscures what a single aggregate number actually represents. We release EGI-BENCH, a unified LLM agent benchmark suite that consolidates eight enterprise facing agent benchmarks (CRMARENA, HERB, PERSONABENCH, USERBENCH, MCP-UNIVERSE, MCPEVAL, BENCHFORCE, LOCOBENCH) behind a single command-line interface with two runtime-budgeted execution modes. On top of the suite we define the Enterprise General Intelligence (EGI) Score, a six-dimensional framework (M1-M6) whose buckets are populated by fine-grained sub-metrics routed from each benchmark rather than by benchmark-level averages. We describe the suite, the sub-metric routing, and the quick/deep budgets, and report results for fourteen frontier and cost-efficient LLMs spanning the GPT, Claude, and Gemini families under quick mode. Top-line EGI ranges from 39.6 (GPT-4o mini) to 65.6 (gpt-5.5), and no single model dominates every capability axis: gpt-5.5 leads task outcome, planning, and retrieval grounding; Claude Sonnet 4.5 leads tool actioning and safety/abstention; and Claude Haiku 4.5 leads engineering quality. Code is available at https://github.com/SalesforceAIResearch/egi-bench.

</details>


### 167. MMedAgent-Plus: Scaling Multimodal Medical Agents across Modalities, Tasks and Workflows

- **Authors:** Ruoxin Wang, Yuanting Pan, Binxu Li, Ruiyang Ji, Yaqian Chen, Jiayuan Ding, Qifan Wang, Lifu Huang, Mingjie Li, Yu Zhang, Ehsan Adeli, Kilian Pohl, Zhe Xu, Zihao Lin, Haoyu Dong, Yixin Wang
- **Published:** 2026-10-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27233v1](http://arxiv.org/abs/2610.27233v1)
- **PDF:** [https://arxiv.org/pdf/2610.27233v1](https://arxiv.org/pdf/2610.27233v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Medical workflows often require multiple interdependent analyses, but existing specialist and generalist AI models are not designed to coordinate them. We introduce MMedAgent-Plus, a multimodal medical tool-use agent that combines a vision-language planner with 18 leading specialist models spanning 12 tasks and 8 modalities. Through a unified tool interface, the planner selects specialists, executes them in sequence, and synthesizes responses grounded in their outputs. The planner is instruction-tuned on 208,928 samples from 32 public medical benchmarks, covering single- and multi-tool interactions across single and multiple rounds. We separately evaluate tool orchestration, response synthesis, and end-to-end execution on held-out samples. MMedAgent-Plus achieves tool-call accuracies of 91.0%, 98.1%, and 80.7% in single-tool multi-round, multi-tool multi-round, and multi-tool single-round settings, respectively. Given correct tool outputs, MMedAgent-Plus achieves scores of 14.4-14.8 out of 15 for faithfulness, completeness, and conciseness across 600 evaluation samples. In end-to-end execution without pre-supplied tool outputs, MMedAgent-Plus correctly invokes the required specialist in 90.6% of 350 evaluation cases spanning seven tasks. Its final-answer accuracy reaches 0.98, matching the dedicated leading specialist and exceeding the strongest baseline (0.28).

</details>


### 168. Magnolia: A Persistent-Memory Agent Framework for Computational Chemistry

- **Authors:** Tao Jiang, Benjamin Navet, Yousouf Taghzouti, Fabien Gandon, Louis-Félix Nothias, Élise Dumont
- **Published:** 2026-10-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.27230v1](http://arxiv.org/abs/2610.27230v1)
- **PDF:** [https://arxiv.org/pdf/2610.27230v1](https://arxiv.org/pdf/2610.27230v1)
- **Categories:** cs.AI, q-bio.BM


> Summary unavailable.


<details>
<summary>Abstract</summary>

Chemistry has recently entered a high-data regime as molecular databases from high-throughput platforms or computational studies have become available. Increasing automation within the chemical sciences leads to a more digital and precision chemistry. Dedicated scientific agents are becoming central to guiding the chemist through an ever-increasing amount of data and findings, including negative ones. Here, we introduce Magnolia, a persistent-memory artificial intelligence agent framework that integrates computational protocols, from docking to quantum chemistry, lab notebooks and chat logs relying on large language models (LLMs). It relies on a three-tier memory system: session-level observations are automatically captured and distilled into structured learnings, confirmed and elevated to project-tier entries and, when human-validated, promoted to cross-project rules that actively guide subsequent work and provide direct chemical feedback. We illustrate Magnolia on four case studies: quantum-chemical evaluation of aromatic systems (COMPAS database), molecular dynamics of butane and of modified DNA, and a protein-peptide docking campaign. Across these projects, Magnolia tracked 317 runs and accumulated 116 project-tier entries, from which four cross-project rules were promoted; in controlled replays of four tasks, runs with memory passed the checks that runs without it failed (for example, ten of ten docking-configuration checks, against one to four of ten). By combining automation, reproducibility, and human-in-the-loop control, our Magnolia framework streamlines docking, molecular dynamics and quantum chemistry calculations with direct analysis and LLM-augmented feedback, offering accelerated access to computational (bio)chemistry.

</details>



## Biorxiv (2 papers)


### 1. An immune world model with multi-agent orchestration for peptide vaccines

- **Authors:** Chen, L., Luan, H., Yu, G.
- **Published:** 2026-10-21
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.19.760096](https://doi.org/10.64898/2026.10.19.760096)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Peptide-vaccine design requires a connection between vaccine-induced priming and recognition of the antigen naturally displayed by a tumor. We present an immune world model that preserves this connection through separate vaccine and tumor branches, endpoint-specific evidence and multi-agent orchestration. Native-recognition constraints held an altered peptide despite its higher presentation score, and targeted perturbations removed antigen-dependent benefit when required tumor-recognition conditions were absent. Public dendritic-cell data distinguished donor from antigen-source transfer: a context ranker achieved Recall@20 of 0.483 and 0.333 under the respective holdouts. Structure-informed receptor prediction added candidate-ranking evidence while preserving functional constraints and matched scenario trajectories. An assay observation model further concentrated a cross-presentation coefficient around its known value in a synthetic conditioning experiment. Together, these results establish a computational framework for linking molecular predictions, native-target requirements and conditional immune dynamics. The framework provides a reproducible basis for choosing peptide-vaccine candidates and the experiments needed to resolve their biological dependencies.

</details>


### 2. GENOAR: Global Engine for Navigating the Omnicell space via Agent-based Research

- **Authors:** Paik, H.
- **Published:** 2026-10-21
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.15.759380](https://doi.org/10.64898/2026.10.15.759380)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Although generative models have revolutionized many fields, including genomics, building a scalable dataset compatible with artificial intelligence (AI) is essential yet underexplored. Here, we developed a Global Engine for navigating the Omnicell space via Agent-based Research (GENOAR) that covers approximately 54 million cells for diverse downstream tasks using AI agents and parallel computing. GENOAR outperforms in three parts. Parallel computations accelerated the preprocessing of single-cell transcriptomic data; the other components enabled agent-assisted data storage and exploration for both AI models and humans. GENOAR involves two AI agents: an AI nomenclaturist ordered the unstructured labels of the single-cell transcriptomic profiles, and an AI librarian retrieved data. GENOAR presents transcriptomic profiles from more than 54 million cells from humans and mice in an analysis-ready format for humans and AI agents. AI agents in GENOAR exhibited successful retrieval performance compared with human experts. Using GENOAR, we elucidated progenitor cell-associated transcriptional signatures in native retinoblastoma and organoid environments. GENOAR was released and validated for the on-demand construction of single-cell atlases for metazoa. In conclusion, using GENOAR, the development of a single-cell transcriptomic atlas compatible with both AI systems and human researchers is feasible, scalable, and reproducible.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*