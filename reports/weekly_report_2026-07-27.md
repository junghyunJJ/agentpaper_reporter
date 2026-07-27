# Weekly AI Agent Paper Report

**Generated:** 2026-07-27 12:36
**Period:** 2026-07-20 to 2026-07-26

## Summary

- **Total papers fetched:** 133
- **Papers matching keywords:** 113
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-07-20) | Change |
|--------|-----------|-----------|--------|
| Total matched | 113 | 143 | -30 |
| arxiv | 113 | 141 | -28 |
| biorxiv | 0 | 1 | -1 |
| medrxiv | 0 | 1 | -1 |

### Notable Trends

Comparison summary unavailable.

---




## Arxiv (113 papers)


### 1. Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills

- **Authors:** Siyuan Huang, Pengyu Cheng, Haotian Liu, Tao Chen, Yihao Liu, Jingwei Ni, Shijie Zhou, Ziyi Yang, Gangwei Jiang, Mengyu Zhou, Yu Cheng, Xiaoxi Jiang, Guanjun Jiang
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22529v1](http://arxiv.org/abs/2607.22529v1)
- **PDF:** [https://arxiv.org/pdf/2607.22529v1](https://arxiv.org/pdf/2607.22529v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM training is shifting from manual design and annotation to interaction-driven self-evolution. However, existing self-evolutionary methods face a fundamental dilemma between task diversity and verification reliability: environment-bound methods obtain precise feedback but confine learning to narrow domains, while open-ended self-generation broadens the task space but lacks reliable verification, allowing misleading rewards to pollute the training loop. We identify agent skills as a powerful middle ground to reconcile this tension: each skill ensures deep, verifiable execution in a specific scenario, while dynamic routing across skills maintains open-ended task variety. Leveraging this insight, we introduce Skill Self-Play (Skill-SP), a co-evolutionary framework comprising a proposer, a solver, and a dynamic skill controller. Orchestrated via a reinforcement learning loop, these components co-evolve in a continuous self-play loop: the proposer generates challenging tasks conditioned on dynamically sampled skills; the solver explores candidate solutions to push its capability boundaries; and the skill controller collects execution feedback to update and expand the skill library. This interactive co-evolution effectively bridges the gap between structured verification and open-ended exploration. Empirical evaluations on tool-use and reasoning benchmarks demonstrate that Skill-SP, serving as a robust evolution engine, consistently pushes the performance ceiling of competent backbones while catalyzing striking turnarounds for initially misaligned models. Our code is available at https://github.com/Qwen-Applications/skill-self-play.

</details>


### 2. The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents

- **Authors:** Darshan Tank, Baran Nama
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22520v1](http://arxiv.org/abs/2607.22520v1)
- **PDF:** [https://arxiv.org/pdf/2607.22520v1](https://arxiv.org/pdf/2607.22520v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Adding procedural skills to an LLM agent is typically evaluated by average improvement in task success. However, this metric hides an important cost: skills can also make agents worse. We measure both sides by comparing agents with and without skills across nearly 6,000 runs spanning two office automation benchmarks and three model harness stacks. This allows us to distinguish two outcomes. A regression is a task solved without skills but failed after skills are added. A residual failure is a task that fails both with and without skills. We find that regressions are substantial enough that the best performing skills outperform others primarily by regressing less, not by gaining more. We identify three causes of regression: (i) skill description osmosis, a skill changes an agent's behavior simply by being present in context, even when it is never invoked; (ii) grounding displacement, a skill's prescribed procedure overrides how the agent interprets its inputs; and (iii) verification displacement, where the procedure suppresses checks the agent would otherwise perform on its outputs. Analysing persistent failures reveals the same underlying pattern. Existing skills overemphasize procedural guidance the stage least often responsible for failure while under supporting grounding and verification, the dominant sources of remaining errors. After correcting evaluation artifacts and studying traces, we find many regressions and persistent failures recoverable through better grounding and verification. Procedural skills should be evaluated by decomposing their net effect into gains and regressions, not by aggregate improvement alone. We identify three regression modes skills should avoid, and find that reliability depends more on grounding and verification than on procedural skill choice.

</details>


### 3. TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI

- **Authors:** Ritik Raj, Souvik Kundu, Sarbartha Banerjee, Dheemanth Joshi, Ishita Vohra, Tushar Krishna
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22465v1](http://arxiv.org/abs/2607.22465v1)
- **PDF:** [https://arxiv.org/pdf/2607.22465v1](https://arxiv.org/pdf/2607.22465v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Routing to select large language models (LLMs) with different cost-quality trade-offs has become a fundamental deployment feature of enterprise AI. Existing routers, primarily make independent routing decisions for each LLM call. However, agentic applications execute as long-horizon workflows whose quality is determined only by a delayed, task-level outcome. This mismatch prevents per-call routers from correctly attributing feedback to individual routing decisions. Towards mitigating this, we present TRACE-Router, a task-level routing framework that aligns routing with the unit of supervision. TRACE-Router assigns each task to a model once at admission using a contextual bandit, pins all subsequent LLM calls to the selected backend, and updates its policy using the task's terminal reward, jointly accounting for accuracy and latency. By leveraging delayed task feedback, TRACE-Router learns routing policies that adapt to the workload while avoiding explicit task-complexity estimation. Across three agentic benchmarks, TRACE-Router consistently improves the accuracy-latency trade-off, achieving non-dominated Pareto frontier points. On tau2-Bench, it outperforms latency-matched interpolation between individual models by 7-8 accuracy points, while on Terminal-Bench it achieves 7.1 higher accuracy points than the strongest single model baseline with 36% lower latency.

</details>


### 4. Where FactsGo Missing: A LayerwiseTaxonomy and Per-Layer Attribution of Information Omissionin Air-Gapped LLM Agent Pipelines

- **Authors:** Santhiya Rajan
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22448v1](http://arxiv.org/abs/2607.22448v1)
- **PDF:** [https://arxiv.org/pdf/2607.22448v1](https://arxiv.org/pdf/2607.22448v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Air-gapped and on-premises deployments in regulated settings (clinical FHIR services, legal review, sovereign infrastructure) cannot call frontier APIs; they run quantized 4-8B models via llama.cpp or vLLM behind tool servers. The dominant reliability failure is omission: the silent absence of a decision-critical fact, such as an agent reading 20 of 400 records and reporting "no anomalies." We argue omission is a pipeline phenomenon, not a model phenomenon, and make four contributions. First, a nine-layer taxonomy (L0-L8) locating every omission mechanism from ingestion through the agent loop. Second, an attribution methodology separating deterministic layers (L0-L3) from behavioral layers (L4-L8) via controlled ablation and logit decomposition, quantifying each with an omission waterfall. Third, an open cross-architecture harness comparing sliding-window-hybrid, full-attention, and SSM-hybrid models across engines and frameworks. Fourth, a runtime-detection framework for air-gapped settings where you own the logits. Results from a 75,476-trial sweep across five models and two engines show a pooled omission rate of 0.62; 68% originates in deterministic middleware (L0-L3), relocating where operators should intervene. Server-side profile factors (weight quantization, KV-cache type, RoPE scaling) were fixed and left for future work.

</details>


### 5. Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture

- **Authors:** Halil Burak Noyan
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22445v1](http://arxiv.org/abs/2607.22445v1)
- **PDF:** [https://arxiv.org/pdf/2607.22445v1](https://arxiv.org/pdf/2607.22445v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise AI agents are typically granted static credential sets at configuration time, holding every tool the role might need for every task they perform. This persistent over-privilege expands the attack surface. We argue that capability scoping must follow a dynamic least-privilege principle and be treated as a prevention mechanism before a detection one. A credential that does not exist in an agent's context cannot be misused regardless of the agent's reasoning or evasion sophistication. We outline a three-source architecture instantiating this principle: role-based ceilings, a task-context classifier, and policy-derived combination prohibitions creating a layered proactive defense against LLM agent misalignment and misuse cases. The architecture supports both enforcing and observe-only deployment; the latter records agent permission requests inconsistent with task context, producing a behavioral signal usable in misalignment research.
  As a first step toward evaluating this architecture, we contribute a synthetic dataset of 600 enterprise task prompts grounded in a multi-department company policy, labeled with minimum required permissions across a 15-permission tool-based taxonomy that maps directly to deployable credentials or enforceable guardrails. The dataset is constructed via a two-pass pipeline that separates prompt generation from permission labeling to avoid circularity, and is validated against a 60-record/688 decisions human-reviewed sample (Cohen's $κ= 0.917$ pre-review and $κ= 0.967$ post-review). Iterating between dataset and policy reduced ceiling violations from 46 to 3, a 93% reduction. This shows that synthetic prompt generation can drive policy refinement when the two are developed together. The dataset, environment specification, and generation pipeline are released to support evaluation of dynamic scoping mechanisms.

</details>


### 6. A Self-Calibrating Agentic AI Framework for Autonomous Edge Resource Allocation

- **Authors:** Fin Gentzen, Marla Grunewald, Iulisloi Zacarias, Mounir Bensalem, Admela Jukan
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22400v1](http://arxiv.org/abs/2607.22400v1)
- **PDF:** [https://arxiv.org/pdf/2607.22400v1](https://arxiv.org/pdf/2607.22400v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) are increasingly deployed as autonomous agents, transitioning from static conversational interfaces to dynamic systems capable of complex reasoning, tool execution, and decision-making. However, the operational reliability of these agentic AI systems is fundamentally challenged by the absence of reliable ground truth in open-ended environments and the risk of increasing operational drift over time. To address this challenge, we propose and experimentally evaluate an agentic AI framework, designed to enforce autonomous integrity within LLM-driven systems. We design a self-calibration mechanism that mitigates drift and dynamically approximates ground truth by incorporating an ARIMA forecaster, without requiring continuous human oversight. To demonstrate the effectiveness and reliability of our methodology, we apply it to the complex domain of profiling the resource usage of zero-knowledge workloads in edge computing networks. Experimental results show that the proposed self-calibrating agentic framework successfully profiles the zero-knowledge workloads, achieving a higher accuracy than baseline LLM agents by 91.7% for resource usage prediction and improving the prediction speed by 71.7% compared to pure profiling, establishing a robust foundation for deploying autonomous AI in decentralized infrastructures. Furthermore, the ground truth generation using the proposed ARIMA leaping algorithm is 52% faster than a standard ARIMA forecasting algorithm, while achieving the same accuracy.

</details>


### 7. IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation

- **Authors:** Varun Gumma, Navonil Majumder, Soumitra Sinhahajari, Soujanya Poria
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22375v1](http://arxiv.org/abs/2607.22375v1)
- **PDF:** [https://arxiv.org/pdf/2607.22375v1](https://arxiv.org/pdf/2607.22375v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have significantly automated the process of scientific discovery over the past few years. However, existing systems share one core limitation: they generate and optimize ideas independently for either Quality or Diversity. This often leads to the generation of ideas in close proximity to one another or to a large set of trivial, unsound, or unclear concepts. In this work, we instead argue that research ideation should be treated as a conjunction of both objectives and framed as a Quality-Diversity (QD) search. In line with this perspective, we introduce IDEAgent, a multi-agent framework that manages the evolution of ideas through lineages. We jointly drive Quality using multi-objective feedback for dedicated repair and refinement, while Diversity is achieved through lightweight sequential memory and explicit comparison against completed ideas, their historical ancestors, and rejected proposals. To systematically evaluate this QD conjunction, we develop Yield, a joint metric that computes the largest set of mutually diverse ideas that satisfy a predetermined quality threshold. Finally, through evaluations across 32 topics spanning 8 domains of Computer Science, we show that IDEAgent outperforms the best baseline by 3.89x on Yield, while achieving non-zero Yield on 8x more topics. We further corroborate these findings through an analysis of quality improvements, showing that repair and refinement are crucial for building logical rigor and clarity while preserving non-obviousness. To encourage future research on QD-search-based ideation, we open-source IDEAgent at https://github.com/declare-lab/IDEAgent.

</details>


### 8. Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI

- **Authors:** Jiaqi Shao, Hanck Chen, Wei Zhang, Maxm Pan, Bing Luo
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22368v1](http://arxiv.org/abs/2607.22368v1)
- **PDF:** [https://arxiv.org/pdf/2607.22368v1](https://arxiv.org/pdf/2607.22368v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent benchmarks increasingly evaluate repository editing, web research, terminal use, and long-horizon interaction. Their scores support capability claims only when the evaluation protocol keeps the intended capability necessary for success. Recent reward-hacking benchmarks and system reports show that agents can instead recover public solutions, read evaluation artifacts, infer generator structure, manipulate feedback, or benefit from invalid scoring paths; existing responses do not provide a common procedure for attributing these shortcuts and quantifying their effect across benchmarks. We formulate protocol validity and introduce HackDetect, a post-hoc audit that identifies an exposure, determines how the agent used it, and assesses whether the resulting score is misleading. We quantify score inflation with the Mislead gap, defined as the exploit score minus the intended score. We audit 2,385 traces across 15 agent benchmarks and find evidence of exposures and reward hacking in 67.0% of Frontier Science traces and 66.7% of AutoLab tasks. Across paired comparisons, we measure score inflation of 0.45-1.00, showing that benchmark reports should provide evidence that scores reflect the intended capability.

</details>


### 9. Towards Trustworthy and Cost-Efficient Data Integration: From Naïve RAG to Agentic RAG

- **Authors:** Chuangtao Ma, Arijit Khan
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22319v1](http://arxiv.org/abs/2607.22319v1)
- **PDF:** [https://arxiv.org/pdf/2607.22319v1](https://arxiv.org/pdf/2607.22319v1)
- **Categories:** cs.DB, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) and AI agents have demonstrated strong potential for data integration in zero-shot and few-shot settings. However, they continue to face significant accuracy and cost challenges in enterprise environments due to a persistent knowledge gap. This paper envisions trustworthy, scalable, and cost-efficient integration through knowledge-grounded LLMs and agents operating within a retrieval-augmented generation (RAG) workflow. Here, trustworthiness refers to evidence-grounded, verifiable reasoning, where integration decisions are transparently supported by retrieved knowledge, robust against hallucination, and consistent across tasks. We trace the evolution from classic RAG to GraphRAG and KG-RAG (knowledge graph-based RAG), highlighting how these paradigms bridge parametric and contextual knowledge. Building on this trajectory, we explore the shift toward Agentic RAG, where autonomous multi-agent systems adaptively plan, retrieve, refine, and reason for complex integration tasks. We examine optimization strategies for cost-efficient integration, addressing computational bottlenecks in large-scale enterprise settings. Finally, we outline open challenges and future directions toward building reliable, explainable, and scalable knowledge-grounded integration systems.

</details>


### 10. Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents

- **Authors:** Valentin Tablan, Scott Taylor, Kristoffer Bernhem
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22157v1](http://arxiv.org/abs/2607.22157v1)
- **PDF:** [https://arxiv.org/pdf/2607.22157v1](https://arxiv.org/pdf/2607.22157v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents encounter learning opportunities in every episode they run, and discard nearly all of them: the underlying models are frozen at deployment, so an agent that resolves a difficult request today starts from zero when it recurs tomorrow. Yet ordinary operation already produces feedback, in the form of outcome verdicts and after-the-fact corrections. We show that this feedback is a sufficient signal for continual learning when the frozen model is paired with an external memory that distils each episode into retrievable natural-language rules. On the banking domain of $τ$-bench, against a static-RAG control retrieving over the complete policy corpus, learning from the one-bit outcome verdict lifts single-trial success to 1.6$\times$ the baseline, and learning from corrections to 2.6$\times$, converting 22 of the 84 tasks the baseline never solves. The result spans the deployment spectrum, measured on Mistral Large, an open-weights model that organisations with data sovereignty requirements can self-host, and replicated on a frontier model, Claude Sonnet 5. The accumulated memory also transfers: each model, reading the store built by the other, rises above its own no-memory baseline. The harness, protocol, and data are released.

</details>


### 11. One Hand Watches The Other: Dynamic Multi-Agent Cooperation for Sample-Efficient Bimanual Manipulation in Dynamic Environments

- **Authors:** Jan Ole von Hartz, Abhinav Valada, Joschka Boedecker
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22119v1](http://arxiv.org/abs/2607.22119v1)
- **PDF:** [https://arxiv.org/pdf/2607.22119v1](https://arxiv.org/pdf/2607.22119v1)
- **Categories:** cs.RO, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-stream robot manipulation policies achieve unparalleled sample efficiency and generalization by modeling actions relative to environmental reference frames. However, existing approaches typically assume these frames to be strictly exogenous. This causal assumption collapses in dynamic settings, such as when a single robot arm manipulates a moving object or when two arms coordinate, where each arm effectively becomes part of the dynamic environment of the other. We propose DynaMAC, a lightweight, policy-agnostic framework that resolves this causal limitation while preserving the sample efficiency, computational speed, and flexibility of multi-stream policies, DynaMAC treats the opposite arm as a dynamic task parameter, thereby providing a unified formulation for dynamic manipulation and bimanual coordination without requiring an explicit leader-follower relationship. To rigorously evaluate these capabilities, we introduce DynaBench, a novel benchmark for robot manipulation in dynamic environments. Across both dynamic environments and bimanual manipulation tasks, DynaMAC outperforms leading probabilistic and generative baselines by over 35 percentage points while requiring 20 times fewer samples. Crucially, DynaMAC generalizes zero-shot from static demonstrations to dynamic environments, substantially simplifying data collection and establishing an elegant bridge toward human-robot collaboration.

</details>


### 12. Predictive Lightweight MARL for Resilient Coverage in Sparse-Signaling Aerial Networks

- **Authors:** Chuan-Chi Lai, Ang-Hsun Tsai
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22109v1](http://arxiv.org/abs/2607.22109v1)
- **PDF:** [https://arxiv.org/pdf/2607.22109v1](https://arxiv.org/pdf/2607.22109v1)
- **Categories:** cs.NI, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

This letter proposes the Predictive Lightweight Multi-Agent Reinforcement Learning (PL-MARL) framework to ensure resilient coverage in bandwidth-constrained UAV swarms. To counter coordination collapse caused by sparse signaling and information aging, we introduce a Kinematic-Aware Inference Engine that proactively reconstructs neighbor trajectories via physical priors. This approach enables an efficient computation-for-communication trade-off, decoupling structural resilience from signaling frequency. Simulations confirm that PL-MARL maintains superior coverage and mission continuity under extreme signaling scarcity and node failure. Our results validate proactive inference as a scalable, low-latency solution for robust aerial coordination, effectively minimizing control overhead to preserve spectrum for payload services while ensuring resilience against interference.

</details>


### 13. Nanbeige4.2-3B: Unlocking Agentic Capabilities in a Compact Mode

- **Authors:** Nanbeige Lab,  :, Chen Yang, Chengrui Huang, Fufeng Lan, Hanhui Chen, Hao Zhou, Huatong Song, Jiaqi Cao, Jiaying Zhu, Jinlin Niu, Kai Wang, Lisheng Huang, Qiliang Liang, Ran Le, Ruixiang Feng, Shuang Sun, Tao Gu, Tao Zhang, Tianyu Luo, Yang Song, Yun Xing, Yuntao Wen, Ziyao Xu, Zongchao Chen, Zongqiang Li
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.22083v1](http://arxiv.org/abs/2607.22083v1)
- **PDF:** [https://arxiv.org/pdf/2607.22083v1](https://arxiv.org/pdf/2607.22083v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present Nanbeige4.2-3B, a compact general agentic model with 3B non-embedding parameters. It delivers strong performance across code-agent, office-agent, and complex tool-use tasks while maintaining highly competitive reasoning capabilities in mathematics, coding, and science. Nanbeige4.2-3B is pretrained from scratch on 28T tokens with a Looped Transformer that reuses the layer stack to increase capacity without adding parameters. For SFT data and trajectory construction, we expand the diversity of executable environments, task assets, and agentic scaffolds through real-world deployment and large-scale synthesis. Our RL pipeline applies mixed-mode RLHF over Think and Non-Think responses to improve overall model quality and reduce failure cases, length-controlled reasoning RL to balance accuracy and reasoning efficiency, and agentic RL with outcome and process rewards to stabilize long-horizon training. Extensive evaluations show that Nanbeige4.2-3B outperforms larger models, including Qwen3.5-9B and Gemma4-12B, across diverse agentic benchmarks while remaining competitive on reasoning and alignment tasks. Performance with OpenClaw further supports its use as a compact local personal assistant.

</details>


### 14. Multi-Agent Debate and Visual Information Extraction for SeePhys Pro: A 1st-Place Technical Report from ICML 2026 AI4Math Track 3 Challenge

- **Authors:** Jiseok Kwak, Suhyeon Jo, Taewoo Kim, Yeongmin Kim, Byeonghu Na, Il-chul Moon
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21946v1](http://arxiv.org/abs/2607.21946v1)
- **PDF:** [https://arxiv.org/pdf/2607.21946v1](https://arxiv.org/pdf/2607.21946v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

This technical report presents our approach to Challenge Track~3: SeePhys Pro at the 3rd AI for Math Workshop, where the task is to answer college-level physics questions whose statement and figure may be given partly or entirely as an image. Visual physics problems become substantially harder for large language models when the decisive information resides in a figure rather than in the text, and this modality gap widens as more of the problem migrates into the image. We address the task with a two-stage framework: a visual information extraction stage that re-expresses figure content as solver-readable text to close the modality gap, and a reasoning stage that orchestrates three heterogeneous solvers through multi-agent debate. Our analysis yields two findings: the gain from orchestration comes from reliable answer selection rather than from additional debate, and the value of a figure aid scales with how much of the problem is locked inside the image. The resulting pipeline improves overall accuracy over a single-agent baseline from 0.643 to 0.802 on the public split, and won 1st place on both the public and the private leaderboard (private overall 0.743).

</details>


### 15. Reliability-Contagion Feasibility in LLM Multi-Agent Networks

- **Authors:** Ruiwu Niu, Xincheng Shu, Ying Zhao
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21912v1](http://arxiv.org/abs/2607.21912v1)
- **PDF:** [https://arxiv.org/pdf/2607.21912v1](https://arxiv.org/pdf/2607.21912v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Communication allows large language model agents to pool evidence, but it also creates paths along which an erroneous claim can spread. We formulate a correction-aware network model that tracks susceptible, exposed, infectious, and corrected agents and derive its early-invasion condition for heterogeneous communication networks. We then couple this propagation model to an analytic majority-vote benchmark in which a clean-task reliability target imposes a minimum connectivity requirement. Under fixed exposure per communication edge, reliability and error control impose opposing graph constraints. We characterize when their intersection is empty and when it contains an intermediate connectivity range, and identify regular graphs that attain the smallest invasion factor within the reliable graph class when such graphs exist. Under a fixed sender budget, the homogeneous first-order threshold is independent of network density, showing that the communication-budget convention determines whether added edges increase early propagation risk. Finite-network simulations on 21,000 trajectories illustrate these directional predictions. A controlled grok-4.3 experiment then evaluates three six-node topologies on 36 new closed-world tasks, with a balanced 12-task subset continued to full cascades. Mean first-generation offspring increased from 0.667 to 1.333 and 1.667 as degree increased from 2 to 4 and 5, while the adoption fraction among exposed neighbours remained 0.333. Mean non-seed erroneous adoption in the full-cascade subset was 0.200, 0.333, and 0.333. Together, these results provide a tractable basis for selecting connectivity under explicit reliability and propagation constraints.

</details>


### 16. Towards Reducing Foreign Language Anxiety Using Level-Appropriate Embodied Conversational Agents

- **Authors:** Krishan Rajaratnam, Wenbin Gan, Yuan Sun
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21887v1](http://arxiv.org/abs/2607.21887v1)
- **PDF:** [https://arxiv.org/pdf/2607.21887v1](https://arxiv.org/pdf/2607.21887v1)
- **Categories:** cs.HC, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Foreign language anxiety (FLA) can be a major barrier to second language acquisition (SLA), especially in conversational contexts. With the proliferation of large language models (LLMs) throughout all areas of life, recent work suggests that interacting with LLM agents can be instrumental within the field of SLA and foreign language education, especially for reducing FLA. Related work also suggests that linguistic demands and task complexity can be predictors of FLA, implying that the use of demanding, complex language could lead to learners experiencing higher FLA. In this paper, we propose a novel multi-agent embodied conversational system that generates level-appropriate dialogue for English language learners. These levels are based on those defined by the Common European Framework of Reference for Languages (CEFR) to describe non-native listener and speaker proficiency. Using a "generate-evaluate-regenerate" loop with multiple LLM agents and a level classifier, it achieves a desired simplicity that is adaptive to the user's proficiency level. We also share the results of a preliminary small-sample pilot study that tested this system with Japanese university students, to see whether it would yield lower FLA levels than an unsimplified embodied conversational agent. Analysis of conversational output showed that 87.4% of dialogue sentences generated by the proposed multi-agent system fell within one predicted CEFR level of the learner's self-assessed proficiency, compared to 54.1% for the unsimplified agent. This suggests that the novel system is better able to produce output at an appropriate level for the learner. Though this study did not yield statistically significant evidence that the system reduces FLA levels in Japanese learners of English, likely due to a small sample size, it provides usability findings and culturally-informed design insights that will inform future study.

</details>


### 17. Multi-Agent System-driven Digital Twins for predictive maintenance: architectures, technologies and open research challenges

- **Authors:** Korota Arsène Coulibaly, Mohamed Hamlich
- **Published:** 2026-07-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21873v1](http://arxiv.org/abs/2607.21873v1)
- **PDF:** [https://arxiv.org/pdf/2607.21873v1](https://arxiv.org/pdf/2607.21873v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Digital twins have emerged as a foundational technology within the context of Industry 4.0, offering a paradigm for the real-time virtual representation of physical systems. However, managing their growing complexity, particularly in distributed industrial environments, requires intelligent architectures capable of autonomous decision-making, dynamic adaptability, and inter-agent coordination. This systematic review explores the intersection between Multi-Agent Systems and Digital Twins, with a particular focus on predictive maintenance applications in resource-constrained contexts. Through a critical analysis of over 547 papers published in high-impact journals (IEEE Transactions, Nature, Elsevier, MDPI), we establish a taxonomy of existing hybrid architectures, identify persistent technological bottlenecks, and formulate three open research questions concerning: (i) the deployment of artificial intelligence on resource-constrained microcontrollers, (ii) distributed multi-node coordination via lightweight communication protocols, and (iii) the hierarchical orchestration of Digital Twins toward smart factory control integrating residual life estimation and explainable Artificial Intelligence. The results of this analysis reveal that, despite significant progress, no existing system offers an integrated embedded-distributed hierarchical solution that simultaneously meets the requirements of Industry 5.0.

</details>


### 18. ToolGuardian: Declarative Security for AI Agent-Tool Interactions

- **Authors:** Arun Ravindran, Saurabh Deochake
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21835v1](http://arxiv.org/abs/2607.21835v1)
- **PDF:** [https://arxiv.org/pdf/2607.21835v1](https://arxiv.org/pdf/2607.21835v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on external tools, expanding capability while creating a new security boundary: third-party tools may appear benign at the interface level while embedding unsafe behavior in implementation. Existing defenses rely on weak metadata, collapse characterization and policy judgment into a single decision, or use heuristic/LLM enforcement that lacks deterministic, auditable reasoning over task context and multi-tool composition.
  This paper presents ToolGuardian, a policy-driven framework for securing agent-tool interactions through pre-admission vetting and task-aware runtime authorization. ToolGuardian uses progressive characterization to convert evidence into structured facts: descriptions capture declared intent, system-call traces expose coarse behavior, mock execution reveals observed effects, and source analysis identifies latent behavior. ToolGuardian's core contribution is an Answer Set Programming (ASP)-based declarative policy layer that reasons explicitly over capabilities, effects, task context, and composition. We compare ASP against heuristic and LLM-based policy realizations using identical inputs and output contracts.
  We evaluate ToolGuardian on 16 MCP-style tools, including 8 malicious variants derived from real open-source tools, and 20 runtime scenarios. For vetting, ASP reaches a deny-class F1 of 0.86 and 88% accuracy using description, syscall, and observed-effect evidence. For runtime authorization, fully specified realizations classify all scenarios correctly, while ablations show that removing compositional and conformance rules substantially degrades performance.

</details>


### 19. Agentic Evaluation of Copyright Law Compliance

- **Authors:** Zheng Hui, Doni Bloomfield, Noam Kolt
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21799v1](http://arxiv.org/abs/2607.21799v1)
- **PDF:** [https://arxiv.org/pdf/2607.21799v1](https://arxiv.org/pdf/2607.21799v1)
- **Categories:** cs.CL, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly perform commercial tasks that involve retrieving external content such as images and, where appropriate, reproducing that content. LLM agents should comply with the law, including copyright law. Presently, however, we lack adequate frameworks to assess whether they do so in practice. To that end, we introduce \textbf{Copyright-Bench}, a benchmark designed to evaluate \textit{LLM agents' compliance with} \emph{copyright law}. Copyright-Bench is comprised of realistic commercial tasks---website development, merchandise design, and pitch deck production---that involve agents selecting between public-domain content (the use of which is \textit{legal}) and copyrighted content (the use of which is \textit{infringing} in this setting).The evaluation introduces prompt variations that simulate different user preferences, as well as time pressure.Comparing state-of-the-art LLM agents against a human baseline, we find that: (1) agents select copyrighted works despite the availability of public-domain alternatives; and (2) for open-weights models, violation rates increase in response to certain user preferences and simulated time pressure.

</details>


### 20. AI-Integrated Scientific Inquiry: A Practice-Centered Vision for Science Education

- **Authors:** Arne Bewersdorff, Matias Rojas, Xiaoming Zhai
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21777v1](http://arxiv.org/abs/2607.21777v1)
- **PDF:** [https://arxiv.org/pdf/2607.21777v1](https://arxiv.org/pdf/2607.21777v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Artificial intelligence (AI) has become part of scientific inquiry. Scientists use AI to observe and measure phenomena, to identify patterns in data, and to build models. As AI moves into scientific inquiry, it gains relevance for science education: students should learn how AI is changing scientific practices, ideally by engaging in AI-integrated scientific inquiry themselves. How to design such instruction, grounded in authentic scientific practice rather than taught as a standalone topic, remains an open question. In our vision, which we describe in this article, AI is treated as a set of scientific instruments that students use within the scientific practices described by the Next Generation Science Standards. Each instrument is a genuine scientific tool, pedagogically bounded: its controls are simplified while its core scientific function is preserved. The approach has two aims: engaging students in authentic scientific inquiry, and building an understanding of how AI is used in science and where it can mislead (discipline-based AI literacy, DAIL). In the article, we focus on the investigative core of inquiry, namely observing, analyzing, and modeling, and describe one exemplary AI instrument for each: computer vision for observing, clustering for analyzing, and generative modeling for modeling. We argue that every AI instrument in science education should carry a distinct reflection point that prompts critical evaluation of the AI instrument itself. Finally, we describe how agentic AI, operating across the whole inquiry rather than a single practice, could be represented, arguing that students should first build a foundational understanding of scientific inquiry and AI instruments before relying on agentic AI.

</details>


### 21. OpenForgeRL: Train Harness-native Agents in Any Environment

- **Authors:** Xiao Yu, Baolin Peng, Ruize Xu, Hao Zou, Qianhui Wu, Hao Cheng, Wenlin Yao, Nikhil Singh, Zhou Yu, Jianfeng Gao
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21557v2](http://arxiv.org/abs/2607.21557v2)
- **PDF:** [https://arxiv.org/pdf/2607.21557v2](https://arxiv.org/pdf/2607.21557v2)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems. While powerful, these complex harnesses also make agents hard to train end-to-end with open infrastructure, whose SFT/RL stacks cannot natively express stateful, multi-process harness inference. To address this, we present OpenForgeRL, an open-source framework for training harness-based agents end-to-end in diverse environments. OpenForgeRL achieves this with a lightweight proxy that serves the harness's model calls while recording them as training data for a standard RL codebase (e.g., veRL), and a Kubernetes orchestrator that runs each rollout in its own remote container, together enabling training on any harness in any environment at scale. By decoupling training and inference, OpenForgeRL allows researchers to easily train, study, and improve agents directly in the real harnesses and environments they are deployed with. We validate our framework across diverse, complex harnesses and environments, spanning tool/claw-based agents and multimodal GUI browser- and computer-use agents. Using only hundreds to a few thousand tasks, OpenForgeClaw reaches 31.7 pass^3 and 55.9 pass@3 on ClawEval and 33.7 on QwenClawBench. OpenForgeGUI reaches 37.7 on OSWorld-Verified, 63.0 on Online-Mind2Web, and 72.3 on WebVoyager. Both outperform open baselines of similar size on nearly all benchmarks, and in the GUI setting match or surpass models several times larger. Beyond benchmarks, we analyze how harness choice (e.g., ZeroClaw, OpenClaw, Codex) and RL shape agent behavior. We find that some harnesses are substantially harder to learn than others, and that RL improves agentic reliability, such as self-verification, tool coverage, and completing multi-step plans, though critical abilities such as error recovery remain weak.

</details>


### 22. GS-Agent: Creating 4D Physical Worlds With Generative Simulation

- **Authors:** Hongxin Zhang, Chunru Lin, Junyan Li, Zhou Xian, Tsun-Hsuan Wang, Chuang Gan
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21522v1](http://arxiv.org/abs/2607.21522v1)
- **PDF:** [https://arxiv.org/pdf/2607.21522v1](https://arxiv.org/pdf/2607.21522v1)
- **Categories:** cs.RO, cs.AI, cs.CL, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Creating dynamic and physically realistic 4D worlds from natural language descriptions is both fascinating and challenging. Traditional computer graphics methods rely on manual creation, requiring extensive human effort to fine-tune materials, motions, and visual fidelity. Recent advances in generative foundation models have sparked interest in learning to generate such 4D worlds from large-scale data; however, existing methods still struggle to ensure physical plausibility and controllability. In this work, we take a different path by leveraging foundation models to construct an agentic system that emulates how humans traditionally create 4D worlds, yet automates the entire process. We present GS-Agent, an end-to-end multi-agent framework that integrates physics engines in the loop to generate realistic, dynamic, and controllable 4D physical worlds from natural language. Inspired by how humans build 4D worlds, GS-Agent decomposes the task into entity management, covering 3D asset curation, material tuning, placement, and motion control, and rendering configuration, including camera and lighting manipulation. Multiple agents with distinct expertise interact with the physics engine via code, seek multimodal feedback, and collaborate to iteratively construct 4D worlds that align with the given descriptions. Experimental results show that GS-Agent effectively converts natural language into diverse and physically plausible 4D worlds exhibiting rich interactions among liquids, deformable objects, and rigid bodies, while achieving cinematic camera and lighting control. We envision GS-Agent as a foundation for a new paradigm in 4D world generation, empowering creative content creation and physical AI. Project page at https://umass-embodied-agi.github.io/gs-agent/

</details>


### 23. Same Dangerous Objective, Opposite Advice: Direct Exposure versus Multi-Agent Mediation

- **Authors:** Linjun Li
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21518v1](http://arxiv.org/abs/2607.21518v1)
- **PDF:** [https://arxiv.org/pdf/2607.21518v1](https://arxiv.org/pdf/2607.21518v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Even a current high-capability LLM can appear safer when shown a dangerous objective directly than when other agents transform and relay its direction. Using OpenAI's gpt-5.6-sol model alias, we test 25 pre-specified mirrored trade-off profiles. Direct exposure to an objective authorizing concealment, fabrication, and pressure produced advice net opposed to its target. After an Id and Censor transformed the same objective into affect and a constraint-rewritten, target-bearing intention, the user-facing Superego---which saw the preferred direction but not the raw objective, its manipulative clauses, or its source---produced advice net aligned with the target.
  This behavioral reverse shift is consistent with the model recognizing or distrusting the manipulative motive, although we do not identify its internal mechanism. The second result exposes a compositional safety gap: a current high-capability model can be used as the user-facing component of an automated, multi-stage workflow serving an explicitly manipulative objective. The workflow can keep the raw instruction, its manipulation-authorizing clauses, and its provenance outside the downstream model's context while preserving the objective's target direction. A user with endpoint-only access likewise cannot directly inspect those upstream messages including the objective.

</details>


### 24. Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems

- **Authors:** Gaurav Dadhich
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21503v1](http://arxiv.org/abs/2607.21503v1)
- **PDF:** [https://arxiv.org/pdf/2607.21503v1](https://arxiv.org/pdf/2607.21503v1)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs. Agents drown in their own accumulating history while paying a token cost that grows every turn, producing missing recalls within and across conversations. The incumbent response treats this as a storage-and-retrieval problem. We argue that framing is too narrow. Actively managing what an agent holds in mind is a lifecycle, not merely a store: it spans deciding what to remember, extracting and structuring it, choosing the right store per data type, consolidating and forgetting while preserving provenance, deciding what is relevant now, anticipating what is needed next, and compacting context to a budget without losing what matters. In serious production this operates not over a single user but across an organizational scope hierarchy. We name this discipline Agentic Context Management (ACM) and decompose it into five primitives: architecting, ingesting, scoping, anticipating, and compacting & consolidation. We then make the economic case: naive context accumulation grows token cost quadratically in conversation length, crude summarization buys linear cost at the price of an accuracy cliff, and only validated compaction achieves linear cost with preserved fidelity. We describe a reference implementation, Maximem Synap, that realizes the five primitives as a multi-tenant service and reports 92% on LongMemEval and 93.2% on LoCoMo under the configuration detailed in Section 6. We close with dimensions existing benchmarks do not yet capture, latency, token efficiency, and context-rot resistance, and the frontier of decision-level and organization-level context the category points toward.

</details>


### 25. Toward Continuous Assurance for the Democratization of AI Agent Creation in Industry

- **Authors:** Natan Levy, Harel Berger
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21495v1](http://arxiv.org/abs/2607.21495v1)
- **PDF:** [https://arxiv.org/pdf/2607.21495v1](https://arxiv.org/pdf/2607.21495v1)
- **Categories:** cs.AI, cs.ET, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly created inside organizations by non-engineering users through low-code, no-code, and conversational development environments. This democratization enables rapid local innovation, but it also creates a reliability gap: agents that appear to users as simple productivity artifacts may depend on changing models, tools, retrieval sources, permissions, prompts, schedules, and external services. These dependencies can cause silent degradation long after deployment, even when no user directly modifies the agent. This paper identifies the reliability challenge created by democratized AI agent creation and proposes a lightweight continuous-assurance framework for citizen-created organizational agents. The framework combines dependency mapping, readiness contracts, scheduled checks, diagnostics, and lifecycle governance to assess whether an agent remains operationally ready under expected conditions. We also present an initial prototype auditor and scenario-based assessment showing how the proposed taxonomy can be translated into practical checks and actionable remediation guidance.

</details>


### 26. Compact Latent Coordination for Autonomous Vehicles at Unsignalized Intersections

- **Authors:** Gil Lifshits, Igal Bilik, Gilad Katz
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21488v1](http://arxiv.org/abs/2607.21488v1)
- **PDF:** [https://arxiv.org/pdf/2607.21488v1](https://arxiv.org/pdf/2607.21488v1)
- **Categories:** cs.LG, cs.AI, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coordinating autonomous vehicles at unsignalized intersections remains a critical challenge for multi-agent reinforcement learning (MARL) systems, which typically struggle with combinatorial action spaces, reliance on privileged information, or rigid agent designs. We propose Master-Agent Proto-plan System (MAPS), a hierarchical deep reinforcement learning (DRL) architecture in which a centralized Master agent generates a compact, continuous embedding, denoted as proto-plan, that encodes a global coordination strategy. Decentralized Worker agents integrate this embedding with local observations to execute vehicle-specific control, decoupling strategic intent from tactical execution and enabling independent optimization of each module.
  As a proof-of-concept evaluation of this coordination mechanism, we test MAPS across 72 intersection configurations in HighwayEnv. MAPS achieves collision-free navigation while significantly reducing average travel time, outperforming state-of-the-art baselines. The learned proto-plans further exhibit robust generalization: a system trained with three agents achieves a 94% success rate when deployed zero-shot to five-agent scenarios, confirming that proto-plan-based hierarchical learning provides a promising framework for multi-vehicle coordination.

</details>


### 27. Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks

- **Authors:** Mack Nixon, Liam Wright, Yevgeniya Kovalchuk, Alison Fang-Wei Wu, Martin Danka, Andy Boyd, David Bann
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21482v2](http://arxiv.org/abs/2607.21482v2)
- **PDF:** [https://arxiv.org/pdf/2607.21482v2](https://arxiv.org/pdf/2607.21482v2)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) and agents are now widely used tools in code development, with data typically sent to third-party cloud-based models. Their adoption in research using personal data is constrained by governance requirements that typically prohibit data transmission to external services. Locally deployable open-weight models offer an alternative since sensitive data never leave the local environment. We introduce an open-source framework for evaluating the efficacy of AI agents powered by open-weight LLMs on one of the most persistent bottlenecks in research on longitudinal population studies: data preparation. The framework comprises: a curated ground-truth dataset (cleaning scripts preparing six sweeps of data from a British cohort study), task definitions encompassing tasks such as category harmonization and multi-wave merging, and automated routines for evaluating the LLM-produced R code and outputted data. We benchmark LLMs across the (consumer grade) deployment spectrum to assess their efficacy in 20 data preparation tasks (creation of 102 variables). Current state-of-the-art, 31-35B parameter models almost saturated our benchmark ('average task completion' up to 87.9%). The performance of open-weight LLMs running on consumer-grade hardware shows promise of a viable path toward AI-assisted data preparation in governance-restricted research settings. Our framework is publicly available at: https://github.com/UCL-ARC/RRBench.

</details>


### 28. AREX: Towards a Recursively Self-Improving Agent for Deep Research

- **Authors:** Shuqi Lu, Chaofan Li, Kun Luo, Zhang Zhang, Hui Wang, Hongwang Xiao, Lei Xiong, Jiahao Wang, Sen Wang, Xiyan Jiang, Wanli Li, Yuyang Hu, Hongjin Qian, Bingyu Yan, Jianlyu Chen, Ziyi Xia, Yingxia Shao, Kang Liu, Zhicheng Dou, Di He, Chaozhuo Li, Qiwei Ye, Zhongyuan Wang, Zheng Liu
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21461v2](http://arxiv.org/abs/2607.21461v2)
- **PDF:** [https://arxiv.org/pdf/2607.21461v2](https://arxiv.org/pdf/2607.21461v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep research requires agents to find answers that jointly satisfy multiple constraints. Discovering such answers is costly, whereas verifying a candidate can often be decomposed into tractable constraint-wise checks. This discovery--verification asymmetry suggests that a research agent should do more than simply search longer: it should recursively improve its current answer by verifying intermediate results and using the partially verified state to guide subsequent refinement. We introduce AREX, a family of Recursively Self-Improving (RSI) deep research agents. AREX alternates between an inner research loop that gathers evidence and constructs a provisional answer, and an outer self-improvement loop that audits the answer constraint-wise, identifies unresolved claims, and launches targeted follow-up research. To sustain RSI over long horizons, AREX learns an autonomous context-update tool that compresses growing interaction history into a compact improvement state preserving verified evidence and unresolved constraints, without relying on an external model. We train AREX on verified synthetic tasks and high-quality trajectories through agentic mid-training and long-horizon reinforcement learning. To mitigate sparse final rewards during long horizon learning, we emphasize key steps where decisive evidence is acquired or erroneous research directions are corrected. We instantiate a dense 4B model and a 122B-A10B Mixture-of-Experts model. Across BrowseComp, WideSearch, DeepSearchQA, Humanity's Last Exam (HLE), and other reasoning and tool-use benchmarks, AREX substantially outperforms comparable-scale baselines and remains competitive with models using substantially more activated parameters.

</details>


### 29. Agent-Guided Relational Concept Discovery: Toward Interpretable Surgical Margin Assessment

- **Authors:** Nooshin Maghsoodi, Amoon Jamzad, Robert Policelli, Mohammad Farahmand, Dilakshan Srikanthan, Martin Kaufmann, Kevin Y. M. Ren, Shaila Merchant, Sonal Varma, Ross Walker, Doug McKay, John Rudan, Gabor Fichtinger, Parvin Mousavi
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21437v1](http://arxiv.org/abs/2607.21437v1)
- **PDF:** [https://arxiv.org/pdf/2607.21437v1](https://arxiv.org/pdf/2607.21437v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep learning models can effectively use Rapid Evaporative Ionization Mass Spectrometry (REIMS) data for surgical margin assessment. However, their clinical adoption remains challenging due to limited generalization to operating room conditions. This difficulty arises because models are typically trained on labeled spectra collected from resected tissue samples, while they must operate on noisy, unlabeled data acquired directly during surgery. In addition, the black-box nature of deep learning models makes it difficult to understand and systematically improve their behavior. Concept-based learning offers a promising way to address these challenges by mapping raw measurements to human-understandable concepts. However, supervised concept-based approaches rely on concept annotations, which are difficult to obtain in complex mass spectrometry workflows. We propose Agent-Guided Concept Discovery, a framework that learns meaningful concepts directly from data without requiring predefined concept labels. During training, a reasoning agent refines semantic descriptions of the learned concepts and adaptively adjusts their weight based on diagnostic relevance. These concepts are further grounded using a biochemical knowledge graph to ensure consistency with known metabolic relationships. Across Skin and Breast Cancer datasets, our model improves balanced accuracy and sensitivity over the baseline. In a representative intraoperative case, it shows fewer false positives, indicating better generalization to surgical conditions.

</details>


### 30. PATS: Policy-Aware Training Scaffolding for Agentic Reinforcement Learning

- **Authors:** Yipeng Shi, Zhipeng Ma, Yue Wang, Qitai Tan, Yang Li, Peng Chen, Zhengzhou Zhu
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21419v1](http://arxiv.org/abs/2607.21419v1)
- **PDF:** [https://arxiv.org/pdf/2607.21419v1](https://arxiv.org/pdf/2607.21419v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In long-horizon LLM agent reinforcement learning, weak policies often repeat similar failures, producing uninformative rollout trajectories and limiting effective policy optimization. Existing skill-centric methods improve exploration by optimizing, filtering, or internalizing reusable skills. However, they remain centered on the skills themselves rather than being designed as adaptive training-time support for the evolving policy. To address this, we propose a policy-centric training paradigm that reframes skills as a dynamic training scaffold. Our framework, Pats, converts rollout groups from the latest policy into evidence cards and uses task-specific evaluation to adjust the context used in subsequent rollouts. Concrete guidance helps weak policies to complete challenging tasks. As policy improves, redundant context is revised or removed to reduce reliance on explicit guidance while preserving useful rollout variation. The policy is optimized with environmental rewards using standard RLVR, and the training scaffold is discarded at deployment. On ALFWorld and WebShop, Pats improves over strong baselines by up to 18.6%. Across seven search-augmented QA benchmarks, it remains competitive while using 32.1% fewer prompt tokens than the baseline.

</details>


### 31. FedAgentKE: Federated Semantic Knowledge Evolution for Heterogeneous Agents

- **Authors:** Weihao Li, Jun Bai, Ziyang Song
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21361v1](http://arxiv.org/abs/2607.21361v1)
- **PDF:** [https://arxiv.org/pdf/2607.21361v1](https://arxiv.org/pdf/2607.21361v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based agents increasingly rely on reasoning, tool use, and iterative execution, yet existing agent frameworks still operate largely in isolation. While recent memory-based agent systems improve individual agents through local retrieval and workflow reuse, local experiences remain fragmented across isolated agent frameworks, limiting cross-framework knowledge transfer and collaborative reasoning evolution. We propose FedAgentKE, a lightweight framework for Federated Semantic Knowledge Evolution across heterogeneous agents. FedAgentKE enables distributed agent frameworks to collaboratively evolve transferable reasoning abstractions through iterative semantic knowledge distillation, aggregation, and adaptation without sharing raw reasoning trajectories. Experiments demonstrate consistent improvements under both cross-framework and cross-task settings, highlighting the potential of federated semantic knowledge evolution for future collaborative agent ecosystems.

</details>


### 32. Regulating autonomous and agentic AI

- **Authors:** Chris Reed, Alex Austria, Anmol Bharuka, Pragnitha Mandava, Khushiya Mujawar, Luka Shakhkulashvili
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21345v1](http://arxiv.org/abs/2607.21345v1)
- **PDF:** [https://arxiv.org/pdf/2607.21345v1](https://arxiv.org/pdf/2607.21345v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Regulating activities where regulatees use autonomous and agentic AI is challenging. Regulatory assumptions about regulatee knowledge and control no longer hold true; much of that lies elsewhere in the AI supply chain which thus needs to be brought within the scope of regulation. Governance systems for autonomous AI cannot replicate existing governance models, but need a fresh approach. Retrospective supervisory oversight becomes ineffective as a risk management tool, and AI autonomy generates new systemic risks which require new solutions. This paper investigate four regulatory systems: UK regulation of content platforms, data protection, UK financial services, and the EU AI Act\'92s cross-sectoral regime. It analyses the challenges posed by autonomous and agentic AI and proposes potential solutions which regulators might adopt. These will transform regulation from a reactive process to an active one, and assist it in adapting to the challenges of AI autonomy.

</details>


### 33. Toward cryptographically verifiable authorization for autonomous AI agents: A security hypothesis, preliminary formal model, and proof-of-concept implementation

- **Authors:** M. Llambí-Morillas, D. Fernández-Fernández
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21325v1](http://arxiv.org/abs/2607.21325v1)
- **PDF:** [https://arxiv.org/pdf/2607.21325v1](https://arxiv.org/pdf/2607.21325v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous AI agents increasingly execute actions, invoke tools, and operate on protected resources with limited human oversight. Existing authentication and authorization mechanisms establish identity and delegate authority, but do not inherently provide cryptographic evidence that a concrete request issued by a specific agent satisfies the applicable policy in a specific execution context. This paper hypothesizes that agent authorization can be formalized as a cryptographically verifiable relation, denoted $R_{CVA}$, that jointly binds an agent principal, a concrete authorization request, an execution context, and the satisfaction of an applicable policy, while selectively preserving the confidentiality of private authorization attributes. We introduce a preliminary formal abstraction for Cryptographically Verifiable Agent Authorization (CVA), define a compact set of candidate security properties including authorization soundness, principal binding, request binding, policy binding, and replay resistance, and provide an executable zero-knowledge proof of concept that instantiates selected elements of the model over a Groth16 zk-SNARK construction. We further identify and formalize the structural separation among identity binding, authorization-request binding, and runtime execution binding as a central open problem in the design of secure agentic systems (a distinction {not explicitly addressed by} current agentic security frameworks) and present a falsifiable research agenda for its resolution.

</details>


### 34. GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG

- **Authors:** Paolo Pedinotti, Enrico Santus
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21324v1](http://arxiv.org/abs/2607.21324v1)
- **PDF:** [https://arxiv.org/pdf/2607.21324v1](https://arxiv.org/pdf/2607.21324v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Retrieval-Augmented Generation (RAG) systems increasingly employ multiple LLM agents. Yet, most prior work optimizes components in isolation rather than coordinating improvements across the pipeline. We introduce GRADRAG, a framework for cross-component prompt adaptation that models the RAG pipeline as a computational graph and propagates structured evaluation feedback to update upstream agents. An Evaluator critiques downstream answers and supporting evidence, producing actionable feedback that a Prompt Optimizer uses to iteratively update adaptive agents, such as retrievers, graph constructors, and answerers. The Evaluator also triggers early stopping when the output is deemed satisfactory. We evaluate GRADRAG on the SQUALITY and QMSUM benchmarks under two retrieval paradigms: flat chunk-based retrieval using IRCoT-style query refinement (Trivedi et al., 2023), and graph-based retrieval that constructs and iteratively enriches an entity-relation graph from the document. Across both settings, GRADRAG consistently outperforms one-step refinement baselines that update only the final generator, achieving a 12-15 percentage point net preference margin in LLM-judged pairwise comparisons, with most gains realized within two refinement iterations.

</details>


### 35. The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works

- **Authors:** Yu Wang
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21273v1](http://arxiv.org/abs/2607.21273v1)
- **PDF:** [https://arxiv.org/pdf/2607.21273v1](https://arxiv.org/pdf/2607.21273v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Dense per-step supervision is an appealing remedy for sparse-reward, long-horizon LLM agents: reward the agent for predicting its next observation, and memory should follow. We show that under group-normalized RL (GRPO), this recipe does not merely fail -- it destroys the policy. Across Qwen3-1.7B/4B/8B on ALFWorld, a potential-based prediction reward drives every run into a degenerate absorbing state (prediction accuracy -> 1.0, task success -> 0,episode length pinned at the horizon): the "dark room" pathology, built automatically by the optimizer. A single-factor ablation localizes the cause -- removing only GRPO's std normalization turns the same reward from catastrophic (0%) into baseline parity -- and a two-line proposition explains why: in all-fail groups the z-scored advantage is invariant to the shaping coefficient, so bounded rewards become unbounded pressure and annealing cannot help. Our central insight generalizes this: what z-scoring amplifies is a dense signal's within-group variance while all-fail groups dominate, so signals whose variance decays by mastery are structurally amplifier-safe.This variance-profile criterion retrodicts our collapses, carries preregistered predictions for arms that had not yet run, and is consistent with published reward-channel successes (a compatibility check, not an independent test). Finally, a controlled signal-delivery matrix (identical signal, varying only the consumption mechanism) shows the reward channel is at best neutral while the auxiliary-loss channel gains ~20 points -- and a shuffled-gold placebo matches the true-gold arm, so the gap survives without correct labels. Endpoints are single-seed; seed replication and group-size controls are preregistered and in progress.

</details>


### 36. pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development

- **Authors:** Chen Zhu, Xiaolu Wang, Weilong Zhang
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21268v1](http://arxiv.org/abs/2607.21268v1)
- **PDF:** [https://arxiv.org/pdf/2607.21268v1](https://arxiv.org/pdf/2607.21268v1)
- **Categories:** cs.MA, cs.AI, econ.GN


> Summary unavailable.


<details>
<summary>Abstract</summary>

In many social-science research tasks, such as economics, LLM-based agents must produce outputs for which no cheap, task-complete, machine-readable correctness signal exists. This creates a distinctive reliability problem for multi-agent systems: how should generation, critique, coordination, and human judgment be organized when no component can certify the final result? We address this problem through pAI-Econ-claude, a gated, human-in-the-loop multi-agent architecture for AI-assisted economic theory development. Agents coordinate through a shared workspace of inspectable intermediate records; specialized gates diagnose targeted failure modes and recommend loopbacks without certifying correctness; and human checkpoints retain authority over decisions that are costly to reverse. We evaluate the architecture on five matched economic-theory tasks against an ungated baseline. Two evaluators blinded to configuration agreed on all five pairwise rankings, preferring the gated architecture in four tasks and the baseline in one. Mean failure severity fell from 1.58 to 1.16, while overall usefulness rose from 2.60 to 3.10. The largest observed gain occurred when a reality check rejected a false market-structure premise and a proof review prompted revision of a false welfare claim. The negative case shows that scaffolding can also compress an economically important mechanism too aggressively. The results support a bounded claim: gated oversight improves the auditability of AI-assisted economic theory without substituting for formal verification, and the allocation of irreversible human judgment is a more informative design variable than pure agent autonomy. The workflow is publicly available at https://github.com/maxwell2732/pAI-Econ-claude.

</details>


### 37. Explainable Belief Harmonization under Dynamic Epistemic Partitions

- **Authors:** Adam Kostka, Jarosław A. Chudziak
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21210v1](http://arxiv.org/abs/2607.21210v1)
- **PDF:** [https://arxiv.org/pdf/2607.21210v1](https://arxiv.org/pdf/2607.21210v1)
- **Categories:** cs.LO, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing approaches to multi-agent belief combination have established mature foundations for combining uncertain beliefs under common assumptions: consensus methods use iterative averaging, logic-based methods resolve conflicting knowledge bases, and epistemic logic analyzes agents' information states. Typically, these approaches assume that the structure determining what each agent can represent remains fixed. However, in many scenarios, agents gain or lose observational capacity during execution, and what was once admissible may become structurally impossible. This paper presents a formal framework for handling such runtime changes in epistemic partitions over continuous belief profiles. A hybrid approach exploits the advantages of answer set programming in elaboration tolerance, declarative integrity constraints, and explanations, with the numerical flexibility of Python. The framework applies to domains where agents operate at heterogeneous and possibly changing levels of resolution, and provides formal guarantees of admissibility preservation under refinement, unique mass-preserving repair under coarsening, and explanation completeness. Evaluation across 100 randomly generated topology changes confirms complete violation detection and explanation coverage.

</details>


### 38. Explainability Framework for Policy-Aware Autonomous Agents

- **Authors:** Heather Merhout, Daniela Inclezan
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21209v1](http://arxiv.org/abs/2607.21209v1)
- **PDF:** [https://arxiv.org/pdf/2607.21209v1](https://arxiv.org/pdf/2607.21209v1)
- **Categories:** cs.LO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In the field of Artificial Intelligence, an agent is a system which is able to autonomously make decisions in order to reach a desired goal. As these systems grow more prevalent in our day-to-day lives, there has been an increased need to add explainability features which can provide an account for an agent's behavior. We therefore propose a framework that outlines how to produce comprehensible explanations for policy-aware agents, or agents which have rule-enforcing policies incorporated in their decision-making framework. This framework is designed using insights from the social sciences on how to produce good explanations. It is implemented in the Answer Set Programming language while using Python to assist with information extraction and natural-language translation. Because these agents incur penalties when violating policies, we are able to leverage these penalties to detect undesirable events in scenarios that are counterfactual to the agents' original actions. This lends itself to creating contrastive explanations (e.g., "the agent performed this action because, had it not, undesirable event X would have occurred."), which formulate the core component for our explainability framework. The framework is evaluated using a survey wherein human participants provide feedback on our program-generated explanations.

</details>


### 39. Enhancing SLMs for Sustainable Code Optimization in Radio-Astronomy

- **Authors:** Elisa Chiarotto, Jingbo Li, P. Chris Broekema, Rob V. van Nieuwpoort
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21677v1](http://arxiv.org/abs/2607.21677v1)
- **PDF:** [https://arxiv.org/pdf/2607.21677v1](https://arxiv.org/pdf/2607.21677v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent Large Language Models (LLMs) can produce and optimize complex code. We investigate the use of LLMs to generate and optimize code for large-scale sciences, focusing on radio astronomy and sustainability. The LOFAR telescope is currently being upgraded, significantly increasing the sky area observed, while simultaneously processing more data faster. However, this is expected to increase the computational requirements 40-fold. This upgrade thus critically depends on rigorous performance optimization of existing software and widespread adoption of accelerators. The code base is very large, making this a daunting task. We therefore investigate and demonstrate an AI-driven approach meant to assist developers in evaluating and optimizing their code, including porting to hardware accelerators. The LOFAR community is committed to sustainable solutions, and needs to achieve these improvements without increasing the energy budget. We thus need to optimize existing codes or port them to accelerators, while making sure that the optimization process itself is also energy efficient. This poses a challenge, since LLMs are energy-intensive. We therefore propose to use Small Language Models (SLMs) instead to limit environmental impact. In this paper, we show how to enhance SLMs through the use of agentic AI. We extend the SLMs in two ways to improve code generation quality and performance: first with a multi-sampling generation strategy and second with incorporating compiler feedback. We demonstrate that multi-sampling SLMs can match or surpass larger single-generation models with fewer computational resources and that feeding compiler output back into the SLMs leads to consistent improvements across all tested models. Our approach is generic, and can also use Retrieval Augmented Generation (RAG) as well as static and dynamic analysis tools in the code generation pipeline.

</details>


### 40. AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning

- **Authors:** Qinfeng Li, Yuntai Bao, Xinyan Yu, Hongze Chen, Wenqi Zhang, Xuhong Zhang
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21106v1](http://arxiv.org/abs/2607.21106v1)
- **PDF:** [https://arxiv.org/pdf/2607.21106v1](https://arxiv.org/pdf/2607.21106v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Effective memory is crucial for LLM agents, yet constructing it effectively remains challenging. A memory-construction policy decides what information to extract, store, update, compress, or discard as interactions accumulate. Heuristic memory methods rely on subjective, task-specific rules, which can misalign with downstream objectives and limit cross-task adaptability. RL-based methods, by contrast, learn from task feedback but mainly use outcome- or module-level rewards. These coarse signals indicate task success but cannot identify which intermediate memory contents support the final answer, creating a fine-grained credit-assignment bottleneck. However, constructing such process feedback is prohibitively difficult because intermediate memory decisions lack unique ground-truth targets, while the appropriate credit varies with the agent's uncertain reasoning trajectory and therefore cannot be specified in advance. We propose AttriMem, an attribution-guided process-feedback framework for learning memory-construction policies with RL. AttriMem augments the global outcome reward with local rewards derived from token-level contributions to the final answer. Experiments on long-horizon dialogue question answering show that AttriMem outperforms retrieval-based, heuristic, and RL-based baselines, generalizes across benchmarks and answer models, stabilizes RL optimization.

</details>


### 41. HiMe: Real-Time Self-Hosted Personal Agent Platform for Health Insights with Wearable Devices

- **Authors:** Wei Liu, Siya Qi, Linhai Zhang, Lorainne Tudor Car, Yulan He
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21019v1](http://arxiv.org/abs/2607.21019v1)
- **PDF:** [https://arxiv.org/pdf/2607.21019v1](https://arxiv.org/pdf/2607.21019v1)
- **Categories:** cs.AI, cs.CL, cs.HC, cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Traditional approaches to wearable health signal analysis, such as smartwatches, are constrained by rigid analytical frameworks and limited personalisation. The emergence of LLM agents creates a new opportunity for Personal Health Agentic Analysis, where health insights can be generated adaptively and in context. However, currently there is no open-source locally deployable platform capable of processing personal health data in real time while preserving privacy. We present HiMe, a locally deployable, privacy-first agent platform that is fully compatible with real-time health data ecosystems across a wide range of wearable devices. HiMe is guided by three design principles. The database is treated as a first-class component. Effectiveness and efficiency are jointly optimised to achieve a low-cost Pareto-optimal balance. Data are processed in real time while the user is modelled over the long term. Together, these principles make it practical for individuals to harness Personal Health Agents for continuous, personalised health monitoring for better wellbeing.

</details>


### 42. SciExplore: Evaluating Autonomous Agents from Scientific Navigation to Information Integration

- **Authors:** Yinhao Tang, Youqing Fang, Yanan Sun, Wenran Liu, Weiming Zhang, Bin Liu, Kuikun Liu, Wenwei Zhang, Kai Chen
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20926v1](http://arxiv.org/abs/2607.20926v1)
- **PDF:** [https://arxiv.org/pdf/2607.20926v1](https://arxiv.org/pdf/2607.20926v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scientific research involves complex information-seeking and reasoning workflows across heterogeneous sources. However, existing benchmarks primarily emphasize general-domain retrieval or static scientific question answering, and therefore fail to assess key capabilities required in realistic scientific research workflows. We introduce SciExplore, a benchmark designed to evaluate scientific information-seeking and reasoning capabilities of LLMs and agents. SciExplore comprises four task types covering 103 expert-curated tasks across more than ten scientific disciplines: scientific database navigation, ambiguous literature retrieval, missing reference completion, and cross-source structured knowledge synthesis, which probe progressively higher-level abilities from entity-level reasoning and document-level identification to evidence-level grounding and domain-level synthesis. We evaluate over ten state-of-the-art LLMs and autonomous agents on SciExplore, revealing substantial performance gaps with performance degrading sharply as task complexity increases and extremely low accuracy on the most challenging structured synthesis tasks. These results highlight significant limitations of current models and agents in realistic scientific information-seeking scenarios.

</details>


### 43. Auditing Provenance Sensitivity in LLM Agent Action Selection

- **Authors:** Junchi Liao
- **Published:** 2026-07-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20827v1](http://arxiv.org/abs/2607.20827v1)
- **PDF:** [https://arxiv.org/pdf/2607.20827v1](https://arxiv.org/pdf/2607.20827v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents choose tools and arguments from context that mixes user requests, tool outputs, retrieved records, memory, and untrusted text. Evidence can be relevant without being authorized to determine a decision, so a correct action need not be grounded only in permitted evidence. We introduce a target-specific authorization audit that labels context factors separately for each tool and argument target. Its primary test holds the task, proposition, position, and policy fixed while changing only the proposition's source authority. We then test behavior when valid evidence is weakened and use context-subset interactions as a secondary localization diagnostic. Across 450 controlled next-action tasks and multiple open-weight LLM families, trusted and untrusted variants produce different actions in 5.4 percent of competing cases versus 1.7 percent of supporting cases. Under controlled degradation, unauthorized competition is retained in a full-correct, mixed-error, clean-correct pattern in 2.4 percent of comparisons, with a 95 percent confidence interval from 2.1 to 3.0 percent. These are controlled stress-set rates, not deployment prevalence. The models respond to textual source-authority cues, but this does not prevent untrusted evidence from influencing their actions.

</details>


### 44. HARP: The Human--AI Research Platform

- **Authors:** Zeshu Zhu, Natalie Friedman, Kevin Weatherwax, Emily Eiben
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20773v1](http://arxiv.org/abs/2607.20773v1)
- **PDF:** [https://arxiv.org/pdf/2607.20773v1](https://arxiv.org/pdf/2607.20773v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have shifted human--computer interaction from `traditional'' interface journeys toward more conversational exchanges. Researchers studying HCI and UI use moderated usability sessions, interviews, surveys, transcript analysis, and static prototypes. However, static prototypes provide limited opportunities to study interaction with live AI systems or systematically control how an LLM behaves across participants and scenarios. Conversation transcripts reveal little about how users formulate, revise, and hesitate over prompts before submission. We designed the Human--AI Research Platform (HARP) for researchers, designers, and anyone who has ever wondered, `What if AI did this?' HARP places participants in controlled mock scenarios with live, configurable AI agents. Researchers can control agent prompts, model parameters, response characteristics, and experimental conditions; trigger surveys at predefined moments; and record prompt composition time, response latency, deletions, and keystroke pauses. Planned capabilities include voice, facial expression, gesture, and, where legally and ethically appropriate, emotion analysis. We illustrate HARP through a study examining how technical specificity and response length affect retention of LLM output. By pairing controllable live agents with behavioral and self-report measures, HARP enables systematic testing of how AI design choices affect users.

</details>


### 45. IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests

- **Authors:** Ankur Singh, Jinqiu Yang, Tse-Hsun Chen
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20759v1](http://arxiv.org/abs/2607.20759v1)
- **PDF:** [https://arxiv.org/pdf/2607.20759v1](https://arxiv.org/pdf/2607.20759v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI coding agents powered by LLMs are increasingly integrated into real-world software development, where they generate, edit, and execute code with autonomous access to local files and tools. Coding agents inherit security risks from both the LLM backbone, where adversarial prompts, poisoned training data, and backdoor triggers can cause models to emit insecure or attacker-chosen code, and their agentic architecture, where tool-using autonomy enables induced misuse of external APIs, data exfiltration, and persistent compromise of development environments. This paper presents a systematic evaluation of malicious issue requests against state-of-the-art coding agents (Cursor, Claude Code, and Codex Desktop), powered by two major model families (OpenAI GPT-5.3 Codex/GPT-5.4 and Anthropic Sonnet 4.6). Our novel benchmark IssueTrojanBench contains malicious issues that are constructed based on four novel attack categories (i.e., embedded as malicious instructions in issues), six delivery vectors (e.g., PDF, or issue comment), and further augmented by perturbations. Our results reveal critical vulnerabilities in the as-deployed modern coding agents, i.e., 66.5% of the malicious issues from IssueTrojanBench penetrate all the guardrails (agent- and LLM-level) of coding agents. Our further analysis shows that rejection is almost entirely from LLMs rather than the agent frameworks, with GPT models broadly vulnerable and Sonnet 4.6 exhibiting more selective, risk-aware blocking of high-impact actions. Our evaluation also highlights that the current agent-level defense strategy offers limited additional protection for coding agents. Our findings highlight the urgent need for stronger agent- and model-level safety mechanisms to protect AI coding agents.

</details>


### 46. NVIDIA-labs OO Agents: Native Python Object-Oriented Agents

- **Authors:** Paul Furgale, Severin Klingler, James Nolan, Matt Staats, Gaia Di Lorenzo, Elisa Martinez Abad, Christian Schüller, Razvan Dinu, Alessio Devoto, Pascal Berard, Gal Kaplun, Elad Sarafian, Riccardo Roveri, Leon Derczynski, Ricardo Silveira Cabral
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20709v1](http://arxiv.org/abs/2607.20709v1)
- **PDF:** [https://arxiv.org/pdf/2607.20709v1](https://arxiv.org/pdf/2607.20709v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Traditional agent development is split across prompt templates, tool schemas, callback code, and workflow graphs. We present NVIDIA Object-Oriented Agents (NOOA), a model-agnostic Python framework for building reliable AI agents. NOOA takes a simpler approach: an agent is a Python object. Its methods are the actions the model can take, fields are its state, docstrings are its prompts, and its type annotations are contracts. A method whose code body consists of "..." is completed at runtime by an LLM-driven agent loop, while methods with normal bodies remain standard deterministic Python. This gives developers and agents the same interface, so agent behavior can be tested, traced, refactored, and improved just like other software.
  This paper makes three contributions. (1) We present the agent-as-a-Python-object programming model and the design principles behind it. Where Python has existing abstractions, we adopt them directly. Agent-specific capabilities--context, events, state rendering, long-term memory, and validated LLM loops--are exposed through simple Pythonic APIs, so both developers and agents share one familiar programming model. (2) We identify six model-facing ideas that NOOA is, to our knowledge, the first to combine on a single surface: typed input/output, pass-by-reference over live objects, code as action, programmable loop engineering, explicit object state, and model-callable harness APIs for context and events. We find the community already converging on several of these ideas--often as experimental or partial features--and present the comparison to encourage further adoption. (3) We demonstrate that current models use this interface effectively, both in targeted capability tests and on agentic and reasoning benchmarks such as SWE-bench Verified and Terminal-Bench 2.0 and ARC-AGI-3.

</details>


### 47. End-to-End Learning of Safe Optimal Feedback Control in High Dimensions with Control Barrier Function Layers

- **Authors:** Xingjian Li, Kelvin Kan, Deepanshu Verma, Krishna Kumar, Stanley Osher, Samy Wu Fung
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20674v1](http://arxiv.org/abs/2607.20674v1)
- **PDF:** [https://arxiv.org/pdf/2607.20674v1](https://arxiv.org/pdf/2607.20674v1)
- **Categories:** cs.LG, eess.SY, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

We consider the problem of learning high-dimensional semi-global feedback controllers under hard safety constraints enforced by control barrier functions (CBFs). Incorporating CBFs into end-to-end policy training requires embedding a quadratic-program-based safety filter as an optimization layer, but computational and differentiation bottlenecks have largely restricted prior approaches to low-dimensional systems, typically with at most 16 state dimensions. We address this limitation by combining operator splitting with the recently developed Jacobian-Free Backpropagation (JFB) method to enable scalable end-to-end training while preserving hard safety guarantees through the CBF safety filter. We justify this training methodology theoretically using nonsmooth analysis techniques and demonstrate its effectiveness on high-dimensional multi-agent nonlinear control problems with state and control dimensions up to 1200 and 400, respectively.

</details>


### 48. Demonstrating GenDB: Instance-Optimized and Customized Query Processing Code Generation via LLM Agents

- **Authors:** Jiale Lao, Immanuel Trummer
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20630v1](http://arxiv.org/abs/2607.20630v1)
- **PDF:** [https://arxiv.org/pdf/2607.20630v1](https://arxiv.org/pdf/2607.20630v1)
- **Categories:** cs.DB, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Traditional query processing engines require continuous development and extensions to support new techniques and user requirements, and in some cases, entirely new systems must be built from scratch. However, these engines are difficult to extend due to their internal complexity, and building new systems demands significant engineering effort and cost. To address this, we demonstrate GenDB, a generative query engine that shifts query processing from manually engineered systems to query processing code generation driven by Large Language Models (LLMs). An early prototype of GenDB uses LLM agents to generate instance-optimized query execution code tailored to specific data, workloads, and hardware resources. This prototype suits offline code generation for repetitive, templated queries, since the upfront generation cost amortizes over many executions and correctness can be ensured through extensive fuzz testing and manual inspection. For ad-hoc queries, GenDB can work with a traditional DBMS in a hybrid architecture: the DBMS handles one-off queries, while GenDB speeds up frequent SQL templates. Our demonstration allows users to (1) visually and interactively explore how GenDB analyzes workloads, profiles hardware resources and underlying data, produces query plans, generates code based on them, and finally uses an optimizer to iteratively achieve a correct and efficient implementation; (2) use visual inspection and analysis to gain qualitative insights into why GenDB produces code that achieves significantly better performance than state-of-the-art query engines on two benchmarks: TPC-H and a newly constructed benchmark designed to reduce potential data leakage from LLM training data; and (3) upload their own data and queries to explore GenDB with different LLMs and query patterns.

</details>


### 49. The Ethics of Autonomous AI Agents for Offensive Security

- **Authors:** Andreas Happe, Jürgen Cito, Jasmin Wachter
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20255v1](http://arxiv.org/abs/2607.20255v1)
- **PDF:** [https://arxiv.org/pdf/2607.20255v1](https://arxiv.org/pdf/2607.20255v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-driven autonomous agents are reshaping offensive security. Unlike traditional penetration-testing tooling -- deterministic, narrowly scoped, and operated by trained practitioners -- agentic security tools exhibit \textit{indeterminacy} along three independent dimensions. First, their actions are drawn from a non-deterministic policy whose outputs resist both ex-ante and ex-post explanation, frustrating incident attribution and pre-deployment safety review. Second, their impact is open-ended due to the non-deterministic actions, agency of utilized models, and opaque LLM supply-chains. Third, their user population is indeterminate in both size and required skill: the operating skill floor for using or developing offensive capabilities has dropped sharply. These three properties are linked thematically, but are not derivable from one another. Combined with the structural cost asymmetry between offense and defense, they enable the industrialization of offensive capability. The net short-term effect favors attackers, even if the same technology may, in the long run, democratize access to defensive practice. Existing dual-use cybersecurity and AI-ethics frameworks were not designed for this combination. Our work analyzes how moral attribution becomes diffuse between users, tool-makers, and third parties when employing autonomous AI agents for offensive security. We also examine the stakeholder impact of this technology and provide stratified recommendations.

</details>


### 50. Small, Free, and Effective: Orchestrating Open-Weight Small Language Models to Outperform Single LLM for Malware Analysis

- **Authors:** Adel ElZemity, Shujun Li, Budi Arief
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20216v1](http://arxiv.org/abs/2607.20216v1)
- **PDF:** [https://arxiv.org/pdf/2607.20216v1](https://arxiv.org/pdf/2607.20216v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Malware analysis demands rapid interpretation of complex detonation reports spanning filesystem, network, and process behaviours. While large language models (LLMs) demonstrate impressive capabilities for technical artifact interpretation, the opacity and escalating API costs of closed-weight frontier models motivate exploration of open-weight alternatives. However, many open-weight models are large, demanding significant compute resources and incurring non-trivial hosting costs that place them beyond reach for resource-constrained deployments. This paper investigates whether orchestrated ensembles of small language models (SLMs) can match or exceed single LLM performance on structured questions about malware detonation reports. We established baselines by testing eleven open-weight SLMs, three cyber security pre-trained models, and six frontier LLMs on Meta's CyberSecEval Malware Analysis benchmark. We then designed and evaluated four orchestration architectures: (i) a multi-agent pipeline that decomposes analysis into structured evidence-collection and reasoning stages, (ii) an adversarial debate framework in which two agents iteratively critique each other's reasoning, (iii) a hierarchical consultation system that pairs a general-purpose SLM with a cyber-specialised expert model, and (iv) a hybrid architecture that combines evidence-grounded pipelines with adversarial debate reasoning. The hybrid system (Qwen3-4B with Foundation-Sec-8B) achieved 35.30% overall accuracy, exceeding the strongest cyber-specialised baseline (22.54%) and the strongest ungrounded frontier baseline (34.77%); when given the same evidence pipeline, grounded Gemini remained the strongest configuration at 38.22%. These findings show that evidence-grounded orchestration can substantially improve the performance of collaborative SLMs for supporting interpretation of malware detonation reports.

</details>


### 51. OpenSkillRisk: Benchmarking Agent Safety When Using Real-World Risky Third-Party Skills

- **Authors:** Qiyuan Liu, Tingfeng Hui, Kun Zhan, Kaike Zhang, Ning Miao
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20121v2](http://arxiv.org/abs/2607.20121v2)
- **PDF:** [https://arxiv.org/pdf/2607.20121v2](https://arxiv.org/pdf/2607.20121v2)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents leverage third-party skills to extend their capabilities in open-world scenarios. However, third-party skills can introduce extra security vulnerabilities, as seemingly harmless skills can contain latent safety risks that only emerge during actual execution. In this work, we conduct a systematic investigation into how well current agent systems recognize and avoid such risks. To support quantitative and qualitative evaluation, we construct OpenSkillRisk, a dedicated safety benchmark containing 263 risky skills collected from public skill marketplaces. We classify these skills into seven categories based on their threat types and pair each skill with a standardized user task and a corresponding sandbox for controlled evaluation. Distinct from prior benchmarks, OpenSkillRisk not only covers more realistic and diverse unsafe scenarios, but also provides a fine-grained analysis to diagnose the behavioral patterns of agents in such scenarios. We conduct comprehensive experiments covering three mainstream CLI agent frameworks and thirteen state-of-the-art LLMs. Experimental results show that no tested system handles risky skills reliably: even the safest configurations still execute unsafe actions in about 17% of cases. Context-dependent and system-level risks are especially difficult for current agent systems to avoid. Our behavioral analysis reveals three recurring failure patterns: agents may fail to recognize the risk, recognize it but fail to intervene before acting, or follow skill instructions beyond the user's intended scope. These findings highlight the need to improve both risk reasoning in LLMs and execution control in agent frameworks.

</details>


### 52. PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning

- **Authors:** Alexis Fox, Junlin Wang, Paul Rosu, Bhuwan Dhingra
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20064v2](http://arxiv.org/abs/2607.20064v2)
- **PDF:** [https://arxiv.org/pdf/2607.20064v2](https://arxiv.org/pdf/2607.20064v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon tasks require sustained perception, reasoning, and exploration, and are a persistent challenge for large language model (LLM) agents. This gap is reflected in their limited performance on continual learning benchmarks such as ARC-AGI-3, especially when models are evaluated out of the box. Various agent harnesses have been proposed to close this gap, and each commits to a strategy for handling long sequences of observations, i.e., what information to save from the environment and how to load it into model context, a choice we argue is particularly consequential. Existing methods for context management face a significant tradeoff, as preserving more information makes retrieving relevant details less tractable. We propose PRO-LONG, a minimal context management framework built around programmatic memory for LLM agents in long-horizon, exploratory settings. PRO-LONG addresses the tradeoff by keeping a complete, structured interaction log and capitalizing on recent progress in coding agents to search this history efficiently. On the full ARC-AGI-3 public game set, PRO-LONG improves over a base coding agent by an average of 18.0 percentage points across frontier models, and matches or exceeds state-of-the-art specialized harnesses (up to 76.1% pass@1) while using 4.2-5.8x fewer tokens. With Fable 5, PRO-LONG achieves 97.4% best@2 at a total cost of \$1,750. Relevant code and logs are available at https://github.com/alexisfox7/PRO-LONG.

</details>


### 53. Bayesian uncertainty estimation improves clinical decision making in medical AI agents

- **Authors:** Frederik Hauke, Patrick Wienholt, Christiane Kuhl, Dyke Ferber, Jakob Nikolas Kather, Sven Nebelung, Daniel Truhn
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.20582v1](http://arxiv.org/abs/2607.20582v1)
- **PDF:** [https://arxiv.org/pdf/2607.20582v1](https://arxiv.org/pdf/2607.20582v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Machine learning models for medical image analysis typically lack a reliable measure of confidence, limiting their use in ambiguous or atypical cases. Here we show that Monte Carlo dropout, applied to a multi-task chest-radiograph classifier (eight thoracic findings, 137,593 training images), provides an epistemic uncertainty signal that tracks generalisation across training-set scales and flags confident yet error-prone predictions. Adding this signal to the point prediction raised error-detection AUROC from 0.74 to 0.77 ($Δ$AUROC +0.023, 95% CI [+0.014, +0.033]). In a controlled 2x2 factorial experiment, a clinical-decision-support agent exploited this uncertainty only when it was delivered as a binary error-risk flag rather than as raw scores, cutting confident misdiagnoses on unreliable findings from 8.5% to 2.7%. Epistemic uncertainty estimation thus carries decision-relevant information beyond point predictions, but its value for downstream agents depends on how it is communicated.

</details>


### 54. Coordinating from Memory: Graph-Structured Experience Reuse for Multi-Agent Adaptation in Dynamic Manufacturing

- **Authors:** Chengxiao Dai, Zhanhui Lin, Zhaokun Yan, Youyang Ni, Chenjun Lei, Luyan Zhang
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19985v1](http://arxiv.org/abs/2607.19985v1)
- **PDF:** [https://arxiv.org/pdf/2607.19985v1](https://arxiv.org/pdf/2607.19985v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Dynamic manufacturing environments require multi-agent systems to coordinate effectively under frequent operational disturbances such as machine failures, urgent job arrivals, and processing time variations. Existing multi-agent reinforcement learning approaches treat each disturbance episode independently, discarding valuable coordination experience that could accelerate future adaptation. In this paper, we propose a Graph-Structured Experiential Memory (GSEM) framework for multi-agent coordination in dynamic manufacturing. The framework encodes historical coordination episodes as heterogeneous relational graphs that capture task dependencies, machine states, and inter-agent collaboration patterns. When a new disturbance occurs, a graph neural network-based retrieval mechanism identifies structurally similar past episodes, enabling experience-guided policy adaptation rather than learning from scratch. Experiments on dynamic flexible job-shop scheduling benchmarks with three disturbance types show that GSEM reduces makespan by 4.1%-10.0% and adaptation time by 33%-38% compared to the strongest memory-augmented baseline, with the advantage increasing under higher disturbance frequency. Ablation studies and cross-disturbance transfer experiments further validate the necessity of graph-structured encoding and similarity-based retrieval and demonstrate the cross-disturbance generalizability of learned coordination patterns.

</details>


### 55. A Framework of User Experience Principles for Human-AI Agent Interaction in the Workplace

- **Authors:** Kathrin Paimann, Elizangela Valarini, Sebastian Juhl
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19941v1](http://arxiv.org/abs/2607.19941v1)
- **PDF:** [https://arxiv.org/pdf/2607.19941v1](https://arxiv.org/pdf/2607.19941v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents become integral to business workflows, establishing guiding user experience (UX) principles is crucial for ensuring user trust and successful adoption. To address this, our study uses a multi-method approach - combining participatory design workshop, paper-and-pencil, expert review, meta-analysis, and in-depth interviews - to identify and validate a design framework of eight core UX principles for human-AI agent interaction in the workplace. Together with their underlying criteria, these principles provide actionable guardrails for designers and software engineers, creating a foundation for developing effective and human-centered AI agent interactions. This study contributes to a structured foundation for future empirical studies on agentic AI in enterprise settings.

</details>


### 56. JANUS: Foreseeing Latent Risk for Long-Horizon Agent Safety

- **Authors:** Yuan Xiong, Linji Hao, Shizhu He, Yequan Wang, Lijun Li
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19913v1](http://arxiv.org/abs/2607.19913v1)
- **PDF:** [https://arxiv.org/pdf/2607.19913v1](https://arxiv.org/pdf/2607.19913v1)
- **Categories:** cs.AI, cs.CL, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent safety is moving from content moderation toward preventing operational failures before tool-using agents act. We propose Janus, a foresight-oriented framework for long-horizon agent safety that trains guards to anticipate delayed risks from partial trajectories. Janus synthesizes diverse agent trajectories via multi-agent simulation and learns a shared policy with two coupled tasks: an anticipation task that forecasts safety-relevant futures and an adjudication task that decides safety from both the observed prefix and anticipated future. The two tasks are jointly optimized with CoAA-RL, which rewards forecasts by their utility for downstream safety judgment. The resulting guard model, Vanguard, blocks unsafe actions before execution. Across four agent-safety benchmarks, Vanguard improves average protection by 15.9 percentage points over baseline guards while increasing benign task completion by 5.1 percentage points.

</details>


### 57. Harnessing Disagreement: Detecting Correlated Agreement Blindness in Multi-Agent Triage

- **Authors:** Shay Seiya McDonnell, Avantika Singh, Quoc-Viet Pham, Vratislav Havlik, Gregory M. P. O'Hare
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19899v1](http://arxiv.org/abs/2607.19899v1)
- **PDF:** [https://arxiv.org/pdf/2607.19899v1](https://arxiv.org/pdf/2607.19899v1)
- **Categories:** cs.MA, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Disagreement-triggered escalation can create a structural blind spot in multi-agent arbitration: as base learners improve, they tend to converge, weakening safety monitoring where correlated failures concentrate. We term this correlated agreement blindness and present ARAT (Arbitrated Reasoning Agents for Alarm Triage), a directed-star system combining an inductive Random Forest (RF) agent, an analogical case-based k-nearest neighbour (k-NN) agent, and a calibrated meta-model to mitigate this effect. On 82,332 holdout samples from the UNSW-NB15 network intrusion detection dataset, 57.2% of errors occur under agreement and 90.6% of dangerous under-predictions evade disagreement-based monitoring even after conservative override; ablation shows that strengthening base learners increases error correlation while reducing disagreement. ARAT reduces under-prediction relative to soft voting from 4.80% to 1.70% via conservative override (-2.6pp) and a safety-flag gate (-0.5pp), demonstrating architectural gains. Cross-dataset validation on clinical readmission supports these indicators, suggesting that diversification improves safety only when it generates productive disagreement rather than convergence. These results indicate that disagreement-triggered escalation can be blind to correlated failure, a risk that may intensify as agentic pipelines deploy increasingly capable, correlated models.

</details>


### 58. DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations

- **Authors:** Jiazhen Jiang, Boxi Cao, Lingyong Yan, Yaojie Lu, Hongyu Lin, Shuaiqiang Wang, Dawei Yin, Xianpei Han, Le Sun
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19865v1](http://arxiv.org/abs/2607.19865v1)
- **PDF:** [https://arxiv.org/pdf/2607.19865v1](https://arxiv.org/pdf/2607.19865v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As autonomous agents rapidly evolve, their ability to reliably manipulate ubiquitous digital documents has become critical for enabling general-purpose AI assistants and automating complex workspace workflows. In this paper, we introduce DocOps, a deterministically verifiable evaluation framework underpinned by a hierarchical taxonomy that deconstructs document operations inspired by real-world practices into atomic dimensions and escalating workflow complexities. Based on DocOps, we systematically evaluate representative closed- and open-source models across various agentic harnesses, revealing that even the most advanced frontier configurations still exhibit profound limitations when handling highly coupled, long-range tasks. Furthermore, a fine-grained analysis of existing agents' manipulation behaviors uncovers 3 key failure modes: long-term state tracking collapse, shallow semantic verification, and destructive editing of structural metadata. Ultimately, our work exposes the capability boundaries of agents in maintaining global document consistency, shedding light on the future design of robust, non-destructive agents for complex digital ecosystems.

</details>


### 59. Know Your Agent: Reconnaissance-Driven Pentesting of AI Agents

- **Authors:** Or Zion Eliav, Eyal Lenga, Shir Bernstien, Yisroel Mirsky
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19837v1](http://arxiv.org/abs/2607.19837v1)
- **PDF:** [https://arxiv.org/pdf/2607.19837v1](https://arxiv.org/pdf/2607.19837v1)
- **Categories:** cs.AI, cs.CR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Traditional pentesting uses reconnaissance at each step to uncover unseen weaknesses, build stronger attacks, and advance the objective; we argue that AI agents require the same treatment. We formalize agent reconnaissance by modeling the process and identifying the knowledge assets it seeks to extract: what they are, how they are used, and which agent weaknesses they exploit to give adversaries leverage in indirect prompt injection attacks. We instantiate these insights in Know Your Agent (KYA), a framework that automates black-box, reconnaissance-driven pentesting by probing agents, building target profiles, and using those profiles to craft stronger attacks. We evaluate KYA on agent-security benchmarks and a real-world coding agent, and release KYA, its benchmarks, and baseline implementations for reproducibility.

</details>


### 60. Dreamer-CPC: Message Learning with World Models for Decentralized Multi-agent Reinforcement Learning

- **Authors:** Taisuke Takayama, Naoto Yoshida, Tadahiro Taniguchi
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19809v1](http://arxiv.org/abs/2607.19809v1)
- **PDF:** [https://arxiv.org/pdf/2607.19809v1](https://arxiv.org/pdf/2607.19809v1)
- **Categories:** cs.MA, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

In multi-agent reinforcement learning (MARL), inter-agent communication is effective for improving performance under partial observability. Representation learning-based approaches enable decentralized agents to learn messages grounded in their own observations, but they rely only on current observations and cannot convey information accumulated over time. We propose Dreamer-CPC, a decentralized model-based MARL method that integrates message learning based on Collective Predictive Coding (CPC) into the world model of DreamerV3. Each agent independently maintains a world model and a message module, and infers and exchanges messages from the latent states of the world model that reflect the history of past observations and actions. We evaluated Dreamer-CPC in two environments: Observer, a non-cooperative information-sharing task, and CatchApple, a newly introduced task in which task-relevant observations are temporarily missing. In both environments, Dreamer-CPC outperformed IPPO-CPC, an existing CPC-based method that generates messages from current observations, as well as no-communication baselines. In particular, in CatchApple, Dreamer-CPC achieved 4 to 5 times the episode return of IPPO-CPC, demonstrating effective coordination where other methods fail due to missing observations. These results suggest that communication grounded in the latent dynamics of world models can support decentralized decision-making when current observations alone are insufficient.

</details>


### 61. TriAgent: Divergence-Aware Multi-Agent Committees for Cost-Efficient Financial Sentiment Analysis

- **Authors:** Isabel Xu, Cynthia Xu, Rachel Ren, Cong Guo, Jiacheng Ding
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19794v1](http://arxiv.org/abs/2607.19794v1)
- **PDF:** [https://arxiv.org/pdf/2607.19794v1](https://arxiv.org/pdf/2607.19794v1)
- **Categories:** cs.CL, cs.CE, cs.DB, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Production LLM-based financial sentiment analysis faces a structural cost trap: most queries are trivially classifiable, yet expensive cloud reasoners process them all, and the bill scales linearly with user count. We present TriAgent, a multi-agent committee stratified by contextual granularity -- a word-level lexicon (VADER), a sentence-level domain transformer (FinBERT), and a cross-sentence reasoner (Qwen2.5, 0.5B-14B-4bit, with Mistral-7B and Phi-3.5-mini cross-family checks). A three-way Semantic Divergence Index (SDI) measures pairwise disagreement across granularities and routes each query accordingly. Our central finding is the critic plateau: when the LLM is re-tasked as a critic over the smaller agents' outputs, F1 plateaus at ~0.87 across 1.5B-7B Qwen (bootstrap 95% CIs overlap), while a same-size 3-persona vote drops to F1=0.66, which is driven by granularity-stratified diversity. Three corollaries follow from the same SDI signal: (i) a Shared Consensus Dictionary on multilingual sentence-BERT answers 95% of Chinese queries from an English cache at F1=0.99 -- cross-border canonicalization at zero marginal cost; (ii) SDI doubles as a post-hoc LLM-hallucination detector at AUC=0.90; (iii) the SDI single-stage strategy attains the best risk-adjusted return (Sharpe=3.50) on a 20-ticker back-test, dominating both always-FinBERT (1.36) and always-LLM (0.11). At 10M-user scale, TriAgent saves $9.3M/year vs. a GPT-4o-mini baseline. Code, lexicons, and the SCD are released.

</details>


### 62. Not Birds of a Feather: Personality-Based Partner Selection in LLM Agents

- **Authors:** Tao Wang, Hsiang-Ling Chiu, Chihang Wei, Zhonghao Hou, Yang Xiu
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19785v2](http://arxiv.org/abs/2607.19785v2)
- **PDF:** [https://arxiv.org/pdf/2607.19785v2](https://arxiv.org/pdf/2607.19785v2)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents increasingly operate in multi-agent ecosystems where a coordinating agent chooses which other agents to work with, and agents are increasingly given personalities through persona prompts. However, whether personality itself influences this endogenous partner choice has not been sufficiently examined: prior work on personality in multi-agent teams has typically fixed team composition exogenously. We present a controlled selection paradigm in which a host agent chooses among six candidate agents that differ only in their Big Five personality descriptions, with capability explicitly equalized (375 trials across five task categories). We find that selection is strongly and systematically personality-dependent. Neutral hosts matched personalities to task types, choosing the open candidate for creative work and the conscientious candidate for most other categories, while the extraverted, agreeable, and balanced candidates were almost never chosen, despite human evidence that agreeableness is among the most performance-relevant traits for teams. Hosts that were themselves assigned personalities selected self-similar partners below chance and chose partners farther from themselves in trait space than random choice would produce. These results suggest that hosts read personality descriptions as signals of task fit rather than as grounds for similarity-based attraction: selection follows task stereotypes and favors complements, the opposite of human homophily. Our findings have direct implications for bias auditing in agent marketplaces and orchestration frameworks.

</details>


### 63. Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking

- **Authors:** Kailin Jiang, Lei Liu, Jian Xi, Hui Xu, Junlin Liu, Baochen Fu, Bin Li,  Vichwang, Yu Lu, Haibo Shi
- **Published:** 2026-07-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19747v2](http://arxiv.org/abs/2607.19747v2)
- **PDF:** [https://arxiv.org/pdf/2607.19747v2](https://arxiv.org/pdf/2607.19747v2)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language models and AI agents become the primary consumers of search results, document set quality determines the upper bound of downstream generation. Yet existing evaluation systems remain confined to scoring documents independently and aggregating via nDCG, ignoring inter-document interactions (redundancy, conflict, complementarity) and unable to answer what makes one document set better than another. To address these issues, we propose a complete evaluate-diagnose-optimize framework. We design SetwiseEvalKit, a three-level, nine-dimension document set evaluation benchmark covering both short-form and long-form scenarios, comprising approximately 28K high-quality evaluation rubrics. We systematically evaluate 12 rerankers: even the best method achieves no more than 45% coverage, cross-document coordination dimensions are universally weak, and no single method maintains top performance across both settings. Building on this, we propose Rubric4Setwise, a training-free method that converts rubric-based evaluation criteria into document set selection signals, achieving the best downstream generation performance with fewer documents and search rounds. It is the only method that maintains state-of-the-art results across both scenarios, validating the effectiveness of closing the loop from evaluation to optimization.

</details>


### 64. CHMAS: A Coupled Hierarchical Framework for Multi-Agent Reinforcement Learning

- **Authors:** Dongming Wang, Jie Xu, Yanyu Zhang, Wei Ren
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19555v1](http://arxiv.org/abs/2607.19555v1)
- **PDF:** [https://arxiv.org/pdf/2607.19555v1](https://arxiv.org/pdf/2607.19555v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) systems face fundamental
  challenges in balancing global coordination with local execution
  across different temporal scales. This paper introduces the Coupled
  Hierarchical Multi-Agent System (CHMAS), a novel framework that
  decomposes multi-agent decision-making into centralized strategic
  planning and distributed tactical execution with bidirectional
  information flow. The strategic layer integrates all agents' states
  with an exclusive global environmental state to generate guidance
  actions every $T$ timesteps, while tactical agents execute
  distributed policies augmented by strategic guidance and local
  neighborhood observations. Unlike existing hierarchical approaches
  with unidirectional control, CHMAS establishes a feedback mechanism
  where accumulated tactical rewards influence strategic objectives
  through a coupling coefficient $λ$, ensuring strategic plans
  remain grounded in tactical feasibility. To address the
  non-stationarity inherent in hierarchical learning, we propose an
  asynchronous update protocol where strategic parameters update every
  $N_f$ tactical episodes, allowing tactical policies to converge to
  quasi-stationary points between strategic changes. We present both a
  general bi-level formulation capturing full system dynamics and a
  tractable additive approximation enabling rigorous analysis.
  Theoretical analysis proves that this asynchronous scheme achieves
  $\mathcal{O}(\log K/\sqrt{K})$ convergence for the strategic layer
  after $K$ strategic updates under standard assumptions. Experimental
  validation in a multi-agent foraging domain demonstrates successful
  learning of spatially partitioned exploration strategies, with both
  layers converging stably despite hierarchical coupling.

</details>


### 65. Hybrid LLM-Guided Search for Quantum Reservoir Architecture Design

- **Authors:** Krishna Bhatia, Gautami Sanjay Naik
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19506v1](http://arxiv.org/abs/2607.19506v1)
- **PDF:** [https://arxiv.org/pdf/2607.19506v1](https://arxiv.org/pdf/2607.19506v1)
- **Categories:** quant-ph, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Quantum reservoir computing (QRC) uses fixed quantum dynamics as a high-dimensional temporal feature map and trains only a lightweight classical readout. QRC is attractive for near-term quantum machine learning, but its performance depends strongly on architecture choices such as input encoding, reservoir depth, entanglement topology, measurement features, state-reset policy, feature construction, and readout regularization. We introduce \method, a simulator-based benchmark that formulates QRC design as constrained black-box architecture search and evaluates whether large language models can act as proposal controllers for this search problem. The benchmark compares five policies under identical evaluation budgets: random search, evolutionary search, Bayesian/TPE optimization, a feedback-based LLM agent, and \hybrid, which combines LLM proposals with memory, mutation, crossover, duplicate avoidance, and exploration. On NARMA10, Mackey-Glass forecasting, and temporal parity, \hybrid{} is the most consistent policy: it ranks first on NARMA10 and temporal parity and second on Mackey-Glass, narrowly behind evolutionary search. Under a 25-evaluation budget and three seeds, \hybrid{} improves over random search on all tasks, including a 23.6\% relative reduction in Mackey-Glass error. The results do not show that LLMs are universal QRC optimizers; rather, they show that generative models can be useful high-level controllers when embedded inside validated, reproducible hybrid search loops.

</details>


### 66. ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D

- **Authors:** Lena Libon, Ben Rank, Jehyeok Yeon, David Schmotz, Jeremy Qin, Daniel Donnelly, Derck Prinzhorn, Maksym Andriushchenko
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19321v1](http://arxiv.org/abs/2607.19321v1)
- **PDF:** [https://arxiv.org/pdf/2607.19321v1](https://arxiv.org/pdf/2607.19321v1)
- **Categories:** cs.AI, cs.CR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents begin to automate AI R&D, we need ways to assess whether their outputs are safe to deploy, even when the agents themselves may be untrusted. AI control offers one such approach: rather than trusting the agent, it treats it as a potential adversary and uses a monitor to detect covert sabotage before deployment. We evaluate AI control for automated AI R&D with ResearchArena, a framework spanning four long-horizon tasks: safety post-training, capabilities post-training, CUDA-kernel optimization, and inference-server optimization. Because the deliverable in AI R&D is an artifact that will be deployed and run, we pair each main task with two kinds of hidden side task: an embedded side task that sabotages the submitted model, adapter, kernel, or server itself, and an independent side task that takes a covert out-of-scope action in the sandbox while leaving the artifact honest. We evaluate frontier agents at both sabotage and monitoring, across four monitor types that vary along two axes: whether the monitor may execute and probe the produced artifact, and whether it sees the agent's chain-of-thought. We find that sabotage hidden in the training data is the hardest to catch, flagged fewer than half the time. Letting the monitor run experiments on the artifact, rather than only read the trajectory, helps, but it is not enough: monitors still miss embedded sabotage by inspecting only the surface, by noticing the anomaly but explaining it away, or by probing the artifact with the wrong test. We release ResearchArena as a modular framework for evaluating sabotage and control in automated AI R&D.

</details>


### 67. Graph-Based Agentic AI with LangGraph: Workflow Pathways for Long-Running Stateful Business Processes

- **Authors:** Daniel Pearson, Sidney Shapiro, Emiliano Sebastian Gonzalez Venegas, Sanad Al-Khatib, Aurora Pinzón Arzola
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19297v1](http://arxiv.org/abs/2607.19297v1)
- **PDF:** [https://arxiv.org/pdf/2607.19297v1](https://arxiv.org/pdf/2607.19297v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper is a practitioner guide to graph-based workflow pathways for long-running, stateful, multi-step generative AI systems in business processes. Rather than treating LangGraph, a low-level orchestration framework for stateful agents, as a model-quality benchmark target, we present three executable recipes -- SQL analytics with repair loops, agentic retrieval-augmented generation with evidence gating, and human-in-the-loop policy review with interrupt and checkpoint recovery -- to show how typed state, conditional routing, deterministic tools, retries, interrupts, checkpoints, and traces fit together. LangGraph is positioned by workflow-complexity fit, not as a universal default: simpler ReAct-style or plain SDK loops may be better for basic tool use, schema-first tools for structured extraction and validation, and DSPy when prompt or program optimization is the main goal. Each recipe explains when LangGraph is worth the extra structure and which implementation patterns make routes, pauses, and audit trails explicit product behavior rather than hidden prompt logic.

</details>


### 68. BioSecBench-Surveillance: A Verifiable Benchmark for AI Agents in Pathogen Genomic Surveillance

- **Authors:** Harmon Bhasin, Kevin Flyangolts, Dianzhuo Wang, Evan Seeyave, Arjun Banerjee, Amanda Darling, Joshua Stallings, David Stern, Shawn Higdon, Claire Duvallet, Bryan Tegomoh, Kenny Workman
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19262v1](http://arxiv.org/abs/2607.19262v1)
- **PDF:** [https://arxiv.org/pdf/2607.19262v1](https://arxiv.org/pdf/2607.19262v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As pathogen genomic surveillance scales, the bottleneck is shifting from data generation to analysis. We present BioSecBench-Surveillance, a verifiable benchmark of 100 evaluations testing whether AI agents can infer the right analysis pipeline from raw sequencing data and surveillance context. Each evaluation gives an agent only the data and context a human analyst would have, then grades its structured answer deterministically. The tasks span seven categories, from taxonomic classification to genetic-engineering detection, across diverse sample types and sequencing technologies. Across 3,962 gradable attempts from sixteen model-harness pairs, the strongest configuration cleared only about half. Opus 4.8 with PI led at 50.2 percent, with a 95 percent confidence interval of 40.1 to 60.3 percent across 83 evaluations, tied with GPT-5.5 with Codex at 50.2 percent, with a 95 percent confidence interval of 40.8 to 59.6 percent, followed by Opus 4.7 with PI at 49.6 percent, with a 95 percent confidence interval of 40.0 to 59.2 percent, and Sonnet 4.6 with PI at 48.6 percent, with a 95 percent confidence interval of 38.9 to 58.3 percent. Even when agents invoked the correct workflows, their mistakes came from the choices around them, such as which references, thresholds, filters, and normalization to apply. BioSecBench-Surveillance provides a standard for measuring whether agents can be trusted to perform genomic surveillance when the next outbreak arrives.

</details>


### 69. Predictive Extrema, Unprofitable Policies: An AI-Assisted Audit of Candle-Based Binance Spot Timing Models

- **Authors:** Ayoub Jadouli
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19453v1](http://arxiv.org/abs/2607.19453v1)
- **PDF:** [https://arxiv.org/pdf/2607.19453v1](https://arxiv.org/pdf/2607.19453v1)
- **Categories:** cs.LG, cs.AI, q-fin.ST, q-fin.TR


> Summary unavailable.


<details>
<summary>Abstract</summary>

We audit whether candle-based machine-learning models can turn predictions of cryptocurrency extrema or short-horizon outcomes into positive Binance Spot paper policies after assumed costs. Numerical results come from scripted fixed-seed model runs and deterministic simulators; human-supervised AI agents supported the July 20 evidence-integrity revision through literature retrieval, separately tasked critique, artifact reconciliation, documentation, and source packaging, not trading decisions. The strongest later-period evidence, conditional on extensive predecessor search, is negative: an unchanged ten-pair mandatory-daily selector lost 6.72\% over 19 July cycles at an assumed 31-bps completed-cycle cost, with 3 wins and 16 losses. In short model-specific July evaluations, the validation-selected local-minimum policy returned -1.79\%, while the local-maximum sell-to-cash/re-entry policy underperformed continuous holding by 2.80\%; their gross mean advantages of 11.11 and 12.21 bps were below even the 21-bps stress. A Gurgul-inspired, OHLCV-only daily adaptation attained minimum/maximum ROC AUC of 0.874/0.896 but average precision of only 0.134/0.116 and lost 44.30\% over seven cycles, versus -41.20\% for buy-and-hold. A forensic audit also downgraded an earlier One4All "30-day holdout": its dates had influenced prior architecture work, its four-hour outcome horizon was not purged at split boundaries, it used same-close entry, and its raw result directories were absent. Across the tested, mostly exploratory protocols, event-ranking performance did not establish positive executable policy value. Every operational decision remains NO\_TRADE.

</details>


### 70. Comparative Study of Multi-Agent Actor-Critic Algorithms in Parameterized Action Reinforcement Learning

- **Authors:** Ubayd Ali Bapoo, Clement N Nyirenda
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19117v1](http://arxiv.org/abs/2607.19117v1)
- **PDF:** [https://arxiv.org/pdf/2607.19117v1](https://arxiv.org/pdf/2607.19117v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Parameterized action reinforcement learning has shown strong performance in environments requiring both discrete action selection and continuous parameterization. Prior work established the effectiveness of single-agent actor-critic algorithms - Greedy Actor-Critic (GAC), Soft Actor-Critic (SAC), and Truncated Quantile Critics (TQC) - on benchmark parameterized action tasks, but their extension to multi-agent settings remains largely unexplored. This paper presents a comparative study of shared-experience multi-agent extensions of these algorithms: Multi-Agent Greedy Actor-Critic (MAGAC), Multi-Agent Soft Actor-Critic (MASAC), and Multi-Agent Truncated Quantile Critics (MATQC). Rather than following the centralized training, decentralized execution (CTDE) paradigm, the proposed framework uses multiple independent actor-critic agents that share a replay buffer while maintaining separate policy and value networks. We evaluate the algorithms on the Platform-v0 and Goal-v0 benchmarks against their single-agent counterparts, using three-, five-, and ten-agent configurations to assess scalability. Performance is measured by average evaluation return and training time across ten independent runs, with one-way ANOVA and Tukey HSD post-hoc tests used to assess statistical significance. Results show that the multi-agent framework consistently improves Greedy Actor-Critic performance, while MASAC and MATQC show comparatively modest gains over their single-agent versions. Increasing the number of agents beyond five yields limited additional performance while substantially raising computational cost, particularly for MAGAC. These results highlight a trade-off between learning performance and computational efficiency, offering insight into the scalability of shared-experience multi-agent actor-critic methods for parameterized action reinforcement learning.

</details>


### 71. Guardrails as Scapegoats: Auditing Unfaithful Safety Refusals in Tool-Augmented LLM Agents

- **Authors:** Aarushi Singh
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19449v1](http://arxiv.org/abs/2607.19449v1)
- **PDF:** [https://arxiv.org/pdf/2607.19449v1](https://arxiv.org/pdf/2607.19449v1)
- **Categories:** cs.LG, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluation frameworks for tool-augmented LLM agents focus overwhelmingly on capability metrics or explicit tool crashes, leaving silent infrastructure failures and HTTP 200 responses with empty, null, or malformed payloads largely unaudited. We introduce a lightweight black-box auditing framework that injects four silent failure profiles across 12 production-adjacent tool stubs and classifies agent responses into three mutually exclusive behavioral classes: Honest Surrender (HSR), Fabrication (FAR), and Unfaithful Safety Refusal (USR). Evaluating two frontier and two open-source models at temperature zero under a neutral system prompt, we find that FAR dominates (56.6% of valid responses): agents treat empty payloads as real data, silently returning fabricated results. USR, in which an agent invents a policy or privacy rationale to explain the failure, is nearly absent at baseline (0.25%, one instance across 396 valid trajectories). Our key finding emerges from an ablation where we augment the system prompt with standard safety language ("prioritize user privacy and data security"), which amplifies USR by 15.6x (from 0.25% to 3.95%; 95% CI on ablation rate: 2.2%-6.4%; Fisher's exact test, p < 0.001). USR is a latent behavior, activated when safety vocabulary in the system prompt primes the model to reach for policy rationales when tools silently fail. Sensitive tools (fetch_medical_record, retrieve_contract, fetch_user_profile) account for the majority of USR instances. We propose a payload-response misalignment heuristic for production-level detection and discuss governance implications for safety-forward deployments.

</details>


### 72. CoGoal3D: Collaborative 3D Object Detection with 3D-Aware Fusion and Refinement

- **Authors:** Zhihao Yang, Zhiyu Xiang, Peng Xu, Tianyu Pu, Kai Wang, Eryun Liu, Dongping Zhang, Yong Ding
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19036v1](http://arxiv.org/abs/2607.19036v1)
- **PDF:** [https://arxiv.org/pdf/2607.19036v1](https://arxiv.org/pdf/2607.19036v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

V2X collaborative object detection features overcoming the limitations of single-vehicle systems by aggregating environmental features from multiple collaborative agents. However, existing mainstream V2X perception methods mainly focus on 2D BEV object detection. When 3D detection task is concerned, inferior results are obtained because they ignore the 3D spatial misalignment caused by differing height and attitude among the collaborators. In this paper, we propose a novel collaborative 3D object detection framework called CoGoal3D, which extracts and refines the 3D feature gradually in a two-stage pipeline. In the first stage, a multiscale 3D-aware global fusion module is designed to mitigate the 3D spatial misalignment. The resulting proposals are then refined in the second stage with an auxiliary task of 3D point reconstruction. An effective multi-agent collaborative data augmentation strategy is further proposed to enrich the training data while minimizing information loss. Extensive experiments on public real-world datasets demonstrate that our CoGoal3D achieves new state-of-the-art performance, with 3D AP@0.7 improvements of 10.86%, 10.34%, and 10.18% on the DAIR-V2X, V2V4Real, and V2X-Real datasets, respectively. Code is available at https://github.com/Megalo-f/CoGoal3D.

</details>


### 73. Skillware: A Software Ontology and Engineering Lifecycle for Persistent Behavioral Artifacts

- **Authors:** Haodi Fan, Zucong Lan
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18970v1](http://arxiv.org/abs/2607.18970v1)
- **PDF:** [https://arxiv.org/pdf/2607.18970v1](https://arxiv.org/pdf/2607.18970v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent Skills have become persistent behavioral artifacts across independent AI agent systems. They combine natural-language task specifications with metadata and optional references, scripts, assets, hooks, package manifests, tests, and companion interfaces. Existing studies explain how Skills are specified, executed, maintained, and evolved, but lack an ontology that defines these artifacts as independent software objects. This paper introduces Skillware as the software abstraction that extends software engineering to persistent Behavioral Artifacts in agent systems. A Skill Artifact specifies reusable task behavior; a Skillware Unit manages that artifact as software through an independent identity and lifecycle. A compatible Agent Host activates the unit for runtime interpretation. Three necessary conditions operationalize category membership: behavioral primacy, independent software identity, and an Agent Host execution relationship. Lifecycle Continuity records whether the same unit identity persists through update, maintenance, rollback, and removal as a separate software-grade property. Evidence combines the Agent Skills specification, a frozen corpus of 138,133 content-deduplicated SKILL.md records associated with 20,556 repository identifiers, independent empirical studies, 15 category-boundary cases, and 13 fixed-revision engineering implementations. The evidence establishes a recurring artifact envelope, separable software identities, compatible execution paths, and lifecycle engineering pressure. Skillware provides the software ontology and engineering lifecycle through which agent capabilities can become identifiable, composable, maintainable, and evolvable software artifacts.

</details>


### 74. How network perturbations distort agreement trajectories in LTI multi-agent systems

- **Authors:** Gal Barkai, Irinel-Constantin Morărescu
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18913v1](http://arxiv.org/abs/2607.18913v1)
- **PDF:** [https://arxiv.org/pdf/2607.18913v1](https://arxiv.org/pdf/2607.18913v1)
- **Categories:** eess.SY, cs.MA, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Distributed coordination of multi-agent systems frequently relies on cooperative protocols designed to achieve agreement on a prescribed, non-trivial trajectory. While the robustness of such protocols to various uncertainties is well documented, existing literature universally assumes that the target agreement trajectory itself remains invariant. This assumption may hold in ideal cases, but we prove that network perturbations can vastly modify the asymptotic agreement trajectory. We first investigate the exact trajectories of Linear Time-Invariant (LTI) agents subjected to dynamic coupling uncertainties by establishing a new Laplace-domain criterion that characterizes the specific closed-loop poles governing the perturbed agreement manifold. To formalize our analysis, we introduce the notion of structure-preserving dynamics, perturbations that maintain the null space of the communication graph's Laplacian, and contrast them with transmission only dynamics, affecting only the adjacency matrix. We prove a critical fragility within standard cooperative output regulation schemes: while static consensus is uniquely robust to heterogeneous transmission delays, synchronization to periodic trajectories is destroyed by arbitrarily small transmission delays. Furthermore, we demonstrate that for d-regular topologies, uniform transmission perturbations can easily shift the system to synchronize with an unexpected, entirely new frequency. These findings expose a previously unidentified vulnerability in classical robust synchronization, demonstrating that transmission dynamics necessitate fundamental structural modifications to networked reference generators.

</details>


### 75. PhoenixRepair: Rethinking Repair Strategy Exploration in Software Agents

- **Authors:** Tianyue Jiang, Yanlin Wang, Xin He, Daya Guo, Jiachi Chen, Ming Wen, Ensheng Shi, Xilin Liu, Yuchi Ma, Guanbin Li
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18859v1](http://arxiv.org/abs/2607.18859v1)
- **PDF:** [https://arxiv.org/pdf/2607.18859v1](https://arxiv.org/pdf/2607.18859v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

While Large Language Models have greatly advanced automated issue resolution, existing agent-based methods exhibit a fundamental limitation in their insufficient exploration of repair strategies. This insufficiency manifests in two key aspects. First, the exploration of multiple potential edit locations is limited. Second, the exploration of repair attempts at each location is also insufficient. To address these challenges, we present PhoenixRepair, a multi-agent framework that systematically explores multiple candidate edit locations and performs iterative reflection and refinement on patch generation, thereby expanding the search space of repair strategies. Our framework begins with multi-location sampling, optionally augmented with graph-based localization information for difficult tasks, followed by iterative reflection and refinement to generate better patches, culminating in final-round generation guided by distilled insights from all historical attempts. Experiments on SWE-bench-Verified demonstrate that PhoenixRepair achieves the largest relative improvement of 7.8\% over SWE-agent under DeepSeek-V3.1, and attains the highest resolved rate of 76.0\% Pass@1 under MiniMax-M2.5. Meanwhile, it achieves higher fault localization accuracy than existing approaches. Our code is available at https://github.com/DeepSoftwareAnalytics/PhoenixRepair.

</details>


### 76. Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents

- **Authors:** SangJin Park, Myungsub Choi, Jineok Kim, Minseung Kang
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18826v1](http://arxiv.org/abs/2607.18826v1)
- **PDF:** [https://arxiv.org/pdf/2607.18826v1](https://arxiv.org/pdf/2607.18826v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-agent defenses are typically evaluated one session at a time. In deployment, however, attacks can be distributed across independent agents, teams, and runtimes, leaving each local guardrail with only a sparse fragment. We formalize cross-agent asynchronous campaign attribution: linking sessions from the same latent adversarial campaign without shared runtime state, test-time campaign labels, or attacker identity oracles. We introduce Asynchronous Attribution Fingerprint Vectors ($A^2FV$), a lightweight proxy-side reference protocol for scoring pairwise campaign similarity from proxy-observable tool-use, timing, and prompt residue. We also construct SCD-v1, a controlled persona-matched benchmark with benign traffic, isolated attacks, multi-session campaigns, matched non-oracle evasion, and leakage audits. On SCD-v1, $A^2FV$ achieves 0.82 pairwise AUC for campaign linking, while score-only adaptations of per-session detectors and chunked LLM judges remain near chance under the same task. The strongest fixed signal is carried by structural and stylometric residue, while timing is retained as a diagnostic channel for richer proxy traces. Crossed-style controls show that the signal is partly style-sensitive but not reducible to style alone. Static and dimension-aware non-oracle stress tests further show that pairwise separability persists under controlled evasion. These results establish cross-agent campaign attribution as a distinct evaluation layer for securing LLM agents in the wild.

</details>


### 77. AgentTrails: Towards Trust and Reuse for Agentic Tasks

- **Authors:** Eden Wu, Sonia Castelo, Yurong Liu, Cláudio T. Silva, Juliana Freire
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18816v1](http://arxiv.org/abs/2607.18816v1)
- **PDF:** [https://arxiv.org/pdf/2607.18816v1](https://arxiv.org/pdf/2607.18816v1)
- **Categories:** cs.DB, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-powered agents increasingly tackle complex tasks by invoking tools, querying databases, executing code, and manipulating intermediate artifacts. These agents follow trajectories that are typically stored as chronological logs, obscuring the underlying dataflow -- the dependencies between their actions and the artifacts they create and manipulate. This limits developers' ability to understand the agents' trails, compare executions, debug failures, and re-use the computations. We present AgentTrails, a prototype system for agent provenance and sensemaking. AgentTrails converts raw trajectories into structured provenance graphs, where tool calls are modeled as computational actions and inputs and outputs as data artifacts. The system supports the comparison of executions by placing multiple provenance graphs on a shared canvas and constructing a joined quotient graph that aligns recurring tools, artifacts, and dependency structures across trajectories. On top of this representation, AgentTrails supports pattern extraction, downstream analysis, and skill abstraction. We demonstrate AgentTrails on real-world agent trajectories, showing that it reveals hidden dependencies, aligns divergent executions, and surfaces recurring tool-use patterns beyond chronological logs.

</details>


### 78. AI Tour Meeting: Group Travel Planning by LLM Agents

- **Authors:** Daisuke Kikuta
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18806v1](http://arxiv.org/abs/2607.18806v1)
- **PDF:** [https://arxiv.org/pdf/2607.18806v1](https://arxiv.org/pdf/2607.18806v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper proposes AI Tour Meeting, a group travel planning framework powered by multiple Large Language Model (LLM)-based agents. The agents are instantiated with distinct personas and collaboratively seek an itinerary that satisfies their constraints and preferences through natural language discussion. The framework enables easy and flexible orchestration of such discussions by providing interfaces for configuring agent personas, discussion workflows, monitoring, and LLM deployment. Its primary use case is a simulation tool for analyzing the behavior of multiple LLM agents during tour planning discussions. This paper demonstrates the utility of the framework by presenting system validation and several analytical results obtained by the framework.

</details>


### 79. RF-Agent: A Practical Framework for Building Language Agents for RFIC Design

- **Authors:** Yueqi Xing, Houbo He, Jolie Wang, Erin Ni, Shikai Wang, Qiufeng Li, Weidong Cao, Taiyun Chi
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18772v1](http://arxiv.org/abs/2607.18772v1)
- **PDF:** [https://arxiv.org/pdf/2607.18772v1](https://arxiv.org/pdf/2607.18772v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have driven rapid progress in electronic design automation (EDA), yet their application to radio-frequency (RF) circuit design remains limited by the scarcity of domain-specific datasets and standardized benchmarks. We present RF-Agent, which addresses this gap through textbook-driven knowledge distillation. A multi-agent Question-Thinking-Solution-Answer (QTSA) pipeline converts a subsection-level corpus from seven canonical RF textbooks into the first-of-its-kind RF-domain reasoning dataset (over 11,000 samples) with a dedicated multiple-choice benchmark. On this benchmark we study two adaptation strategies: supervised fine-tuning (SFT) and three retrieval-augmented generation (RAG) configurations (semantic, keyword, hybrid). Across multiple LLM families, domain-specific SFT significantly improves RF reasoning, especially for small and medium-sized models; among RAG configurations, semantic retrieval performs best, indicating embedding-based context alignment suits RF reasoning better than naive fusion. The dataset and benchmark provide a reusable foundation for future work on LLM-aided RF circuit design.

</details>


### 80. AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents

- **Authors:** Kunlun Zhu, Xuyan Ye, Zhiguang Han, Yuchen Zhao, Bingxuan Li, Weijia Zhang, Muxin Tian, Xiangru Tang, Pan Lu, James Zou, Jiaxuan You, Heng Ji
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18754v1](http://arxiv.org/abs/2607.18754v1)
- **PDF:** [https://arxiv.org/pdf/2607.18754v1](https://arxiv.org/pdf/2607.18754v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agent failures are difficult to debug because the step where an error surfaces is often not the one that caused it. Existing observability tools replay execution traces but provide little support for identifying the root cause or translating diagnosis into recovery. We present AgentDebugX, an open-source debugging framework that organizes debugging as a closed loop of Detect, Attribute, Recover, and Rerun. At its core, DeepDebug performs multi-turn root-cause diagnosis through global trajectory understanding, structure-guided investigation, and cross-examination. On the Who and When benchmark, DeepDebug achieves the best strict attribution accuracy among the evaluated methods on both tested open-weight backbones, reaching 28.8 percent exact agent-and-step accuracy on qwen3.5-9b versus 21.7 percent for the strongest single-pass baseline. On GAIA, DeepDebug repairs 13 of 73 failed tasks in a single rerun, compared with 4 to 6 for three decoupled self-correction baselines, improving overall accuracy from 55.8 percent to 63.6 percent. AgentDebugX exposes this workflow through a Python library, CLI, web console, and installable agentic skill, and provides an opt-in Error Hub for sharing scrubbed failure-diagnosis-repair bundles and reusing them as debugging memory.

</details>


### 81. Strategy-Following Multi-Agent Deep Reinforcement Learning Considering Control Strategies Provided to Other Agents

- **Authors:** Yamato Takahagi, Gentoku Nakasone, Yoshinari Motokawa, Toshiharu Sugawara
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18719v1](http://arxiv.org/abs/2607.18719v1)
- **PDF:** [https://arxiv.org/pdf/2607.18719v1](https://arxiv.org/pdf/2607.18719v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This study proposes a learning method for multi-agent systems that allows agents to be controlled through human manager instructions after learning and enables uninstructed agents to implicitly complement the overall work based on the actions of other agents. Multi-agent applications using deep learning have shown potential; thus, to achieve extensive social applications, humans should be able to control learned agents using simple methods to respond to environmental and social changes. Even without such changes, learned coordination often does not match the expectations of human managers, making it preferable to control coordination structures to match human intentions. Some studies have aimed to control agent behavior using simple instructions. However, they assumed that instructions are provided to all agents, which is time-consuming and not evident when designing a better cooperation regime. Ideally, specific agents should receive key action instructions, while others should automatically complete the remaining tasks. The proposed method, which extends previous work on controllability in multi-agent deep reinforcement learning, enables uninstructed agents to adaptively complement overlooked tasks and areas. The experimental results show that agents using the proposed method can shift to another cooperative structure and achieve better performance than those using conventional methods.

</details>


### 82. SciHazard: A Benchmark for Measuring Scientific Safety Risks with Decomposed Harm Scoring

- **Authors:** Chunxiao Li, Yuan Xiong, Lijun Li, Tianyi Du, Wenlong Zhang, Lei Bai, Jing Shao
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18665v1](http://arxiv.org/abs/2607.18665v1)
- **PDF:** [https://arxiv.org/pdf/2607.18665v1](https://arxiv.org/pdf/2607.18665v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) increasingly support science, but they can also convert hazardous scientific knowledge into actionable misuse guidance. Existing benchmarks often rely on templated queries disconnected from real-world hazards, and employ LLM-as-a-Judge paradigms without domain grounding. To address this, we introduce SciHazard, a real-world-grounded benchmark for scientific risks and a dataset agnostic evaluation framework for measuring harmfulness. SciHazard contains 2400 hazardous questions and 600 oversafety questions across 12 disciplines, with both queries grounded in regulated entities and documented failure scenarios. To compute \textsc{DeHarm-Score} , we develop a decomposed evaluating procedure that combines query hazard severity, refusal behavior, and response-level risk. For non-refused responses, it further decomposes response-level harm into \textsc{Executability}, quantified via dynamic checklists with importance weighting, and \textsc{Net-new risk}, assessed through retrieval-augmented claim extraction and synthesis-barrier verification. An expert-validation study shows that \textsc{DeHarm-Score} improves agreement with expert annotations by 90.17\% over the strongest baseline. We benchmark 31 frontier LLMs and deep research agents in an extensive scientific safety evaluation. Notably, deep research agents yield 32.3\% higher mean \textsc{DeHarm-Score} than standard LLMs, exposing autonomous agents as a critical blind spot in current safety defenses. Code and dataset are available at https://anonymous.4open.science/r/DeharmScore-7B55.

</details>


### 83. Broken Gates: Re-evaluating Web Bot Defenses in the Age of LLM Agents

- **Authors:** Behzad Ousat, Nikita Turkmen, Lalchandra Rampersaud, Dillan Bailey, Amin Kharraz
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18659v1](http://arxiv.org/abs/2607.18659v1)
- **PDF:** [https://arxiv.org/pdf/2607.18659v1](https://arxiv.org/pdf/2607.18659v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based browser agents are rapidly changing the threat landscape for web security. Unlike traditional automation frameworks that execute predefined scripts, these agents can autonomously navigate websites, reason about page content, and interact with web interfaces using natural-language instructions. This evolution raises fundamental questions about the effectiveness of bot management systems, widely deployed to defend against automated web abuse. In this paper, we present a systematic measurement study evaluating the resilience of both interactive challenge-based defenses and non-interactive trust-based defenses against two attacker classes: commercial Captcha-solving services and LLM-based browser agents. Our evaluation spans seven solver services and six agents, including cloud-hosted, self-hosted, AI-assisted, and browser-extension configurations, tested against hCaptcha, reCaptcha v2, reCaptcha v3, and Cloudflare Turnstile. Our results show that challenge-based defenses are broadly ineffective against commercial solvers, which achieve near-perfect bypass at negligible cost. The challenges can similarly be defeated by LLM-based agents when a dedicated solver module is available. Non-interactive defenses such as reCaptcha v3 exhibit stronger resistance, but our analysis reveals that this resilience does not reflect a fundamental security property. Through fine-grained interaction trace analysis, we find that two agents with nearly indistinguishable behavioral footprints yield divergent outcomes, one bypassing the defense and one failing, isolating execution-environment authenticity, rather than agent behavior, as the determining factor. These findings suggest that the security boundary of non-interactive defenses lies at the environment layer, with significant implications for how bot management systems are designed and evaluated.

</details>


### 84. A Self-Evolving Default Action for Cooperative Tasks with Continuous Action Space

- **Authors:** Shuangyao Huang
- **Published:** 2026-07-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18597v2](http://arxiv.org/abs/2607.18597v2)
- **PDF:** [https://arxiv.org/pdf/2607.18597v2](https://arxiv.org/pdf/2607.18597v2)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Counterfactual credit assignment has proven effective in multi-agent reinforcement learning (MARL) for discrete action spaces, yet its extension to continuous-action cooperative tasks remains challenging. Existing methods that approximate the counterfactual baseline via Monte Carlo sampling often introduce bias into policy gradients and fail to guarantee convergence to local optima, as the sampled actions may not have been sufficiently trained. To address these limitations, we propose SAFE, a novel MARL framework that employs a counterfactual baseline conditioned on a self-evolving default action sampled from each agent's experience buffer. This design naturally extends to continuous action spaces without relying on additional simulations, reward models, or environment-specific prior knowledge. The baseline accurately quantifies each agent's contribution, and introduces no bias into the deterministic policy gradient, ensuring convergence to local optima. Extensive experiments on cooperative vehicular tasks demonstrate that SAFE consistently outperforms state-of-the-art models.

</details>


### 85. Toward User-Conditioned Evaluation of Personal LLM Agents under Temporal Interventions

- **Authors:** Pin Qian, Su Wang, Yihang Chen, Qiaolin Yu, Xiaoyuan Wang, Zhitong Guo, Zhicheng Wang, Junxian You
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.21635v1](http://arxiv.org/abs/2607.21635v1)
- **PDF:** [https://arxiv.org/pdf/2607.21635v1](https://arxiv.org/pdf/2607.21635v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Personal agents maintain memories, learned skills, tool configurations, and policy state that evolve with each user. Existing agent benchmarks often evaluate these capabilities in isolation: tool benchmarks test invocation under fixed APIs, memory benchmarks test recall or forgetting, and safety benchmarks test static policy compliance. We argue that personal-agent evaluation requires a different protocol: replaying the same temporal intervention across different persistent user-conditioned states and measuring how failures propagate across agent components. We formalize this requirement as four conditions: explicit temporal intervention, persistent state across the intervention, induced cross-dimensional effects, and variation in user-conditioned state. A focused audit of public benchmark protocols selected by explicit inclusion criteria identifies several close cases. Under our explicitly narrow operationalization, we did not find a protocol in that audited set satisfying all four conditions. This claim is scoped as a focused gap analysis with bounded literature coverage. This position paper proposes a minimal benchmark design and candidate reporting metrics for user-conditioned adaptation. The result is a concrete design requirement for future personal-agent evaluation, with metrics used as reporting tools for that requirement.

</details>


### 86. The Story Shapes the Agent: Narrative Priors in LLM Behavior

- **Authors:** Yixuan Wang, James Lester, Shashank Srivastava
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18566v1](http://arxiv.org/abs/2607.18566v1)
- **PDF:** [https://arxiv.org/pdf/2607.18566v1](https://arxiv.org/pdf/2607.18566v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Persona prompting is widely used to steer LLM agent behavior, yet the narrative framing of a task can matter more than the assigned persona. We isolate this effect through structural isomorphism, constructing three text-based investigation games that share the same action space, stage progression, and resource constraints while varying only task narrative: disease investigation, IT troubleshooting, and murder mystery. Across 1,890 sessions spanning 3 models and 10 personas, we identify narrative priors: systematic action tendencies activated by a task's story framing, independent of its decision structure. Narrative priors explain 5-31x more behavioral variance than persona, are consistent across model architectures, and in two of three domains are negatively associated with task success. Persona effects that do transfer across narratives arise from behavioral anchors, persona descriptions whose language maps directly onto shared actions. Causal interventions confirm this: removing anchor words from a high-transfer persona reduces cross-narrative consistency by 95%. Our framework also generalizes to a held-out fourth narrative and yields a persona-selection method that improves cross-narrative transfer. These results suggest that LLM behavior that survives narrative changes should be grounded in concrete actions rather than abstract descriptions.

</details>


### 87. The Chronos Vulnerability: A Taxonomy of Temporal Persistence and Memory-Based Deception in Agentic AI

- **Authors:** Om Narayan, Ramkinker Singh, Praveen Baskar
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19433v1](http://arxiv.org/abs/2607.19433v1)
- **PDF:** [https://arxiv.org/pdf/2607.19433v1](https://arxiv.org/pdf/2607.19433v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

The transition from stateless generative models in artificial intelligence to stateful, autonomous agents represents an architectural evolution that, while providing the capabilities of long-term planning and the automation of enterprise workflows, also represents the introduction of a new form of security threat, the Chronos Vulnerability. The Chronos Vulnerability represents the threat of memory-based attacks, including the Memory Injection Attack (MINJA) and the sleeper agent, in which the internal belief system of the autonomous agent is compromised, effectively decoupling the attack vector from the final catastrophic event. This study formalizes the threat model for persistence-based attacks and the threat of Dynamics Blindness in the context of the World of Workflows benchmark, demonstrating that traditional endpoint content filters are insufficient for the current stateful architecture. Consequently, this study synthesizes a defense-in-depth landscape, categorizing emerging frameworks such as diagnostic trajectory guardrails (AgentDoG), formal temporal verification (Agent-C), immunological memory consensus (A-MemGuard), and hardware-anchored trust via GPU-based Trusted Execution Environments (TEEs) and Zero-Trust memory architectures.

</details>


### 88. Scalable Policy Optimization for Networked Multi-Agent Reinforcement Learning with Continuous State-Action Spaces

- **Authors:** Dongming Wang, Pengcheng Dai, Wenwu Yu, Wei Ren
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18554v1](http://arxiv.org/abs/2607.18554v1)
- **PDF:** [https://arxiv.org/pdf/2607.18554v1](https://arxiv.org/pdf/2607.18554v1)
- **Categories:** cs.MA, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We develop the Continuous Distributed Coupled Policy Gradient (CDCPG) algorithm for cooperative reinforcement learning in networked Markov decision processes with continuous state and action spaces. Each agent maintains a local actor over a bounded graph neighborhood, and a localized least-squares temporal-difference critic evaluates a truncated action-value function through a spectral random-feature representation of the local transition kernel. The analysis makes four contributions. First, the truncated action-value function is constructed as a conditional expectation over the neighborhood, yielding a well-posed localized Bellman theory that removes the continuation-kernel mismatch of naive truncation arguments. Second, we expose a dimensional obstruction to temporal-difference stability for normalized random features and prove an unconditional excitation bound that reduces stability to a symmetric persistence-of-excitation condition, monitorable through an online matrix-concentration certificate. Third, under exponential spatial decay of agent interactions, the excitation condition, and smoothness of the objective, CDCPG drives an averaged per-agent stationarity measure to within any excess $ε$ of an explicitly characterized approximation floor using $\widetilde{\mathcal{O}}(ε^{-2})$ shared-oracle samples, and the excess dependence matches the smooth nonconvex first-order rate; per-agent computation and communication are governed by the neighborhood size rather than the network size. Fourth, an adaptive-locality rule selects the radius that balances truncation and graph-decay residuals against the target accuracy. Experiments on a networked linear-quadratic benchmark corroborate the locality and feature-dimension predictions.

</details>


### 89. ChainWatch: A Kill Chain-Aligned Sequential Detection Framework for Multi-Step Attacks in MCP-Based AI Agent Systems

- **Authors:** Om Narayan, Rashmi Jyoti, Ramkinker Singh
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19432v1](http://arxiv.org/abs/2607.19432v1)
- **PDF:** [https://arxiv.org/pdf/2607.19432v1](https://arxiv.org/pdf/2607.19432v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Model Context Protocol (MCP) is an open-source standard that allows AI agents to connect to external tools, databases, and services. While this connectivity enables powerful agent capabilities, it also introduces multi-step attacks that existing per-call defenses cannot reliably detect. Attackers can compose individually benign tool invocations into malicious sequences that evade isolated inspection. This paper presents ChainWatch, a sequential detection framework for identifying multi-step attacks in MCP-based AI agent systems. ChainWatch models attack progression using a six-stage kill chain and applies a Hidden Markov Model (HMM) to classify tool-call sequences. Detection rules are triggered when a session exhibits suspicious progression across multiple stages. The framework is supported by a structured threat model covering direct sequential attacks, indirect prompt injection chains, and hybrid multi-stage attacks. A 20-dimensional feature extraction schema captures behavioral signals from tool interactions. We demonstrate the approach using five representative attack scenarios from the security literature, showing how ChainWatch detects attack chains that evade traditional per-call security mechanisms.

</details>


### 90. Engineering Trustworthy Agentic AI for Critical Systems

- **Authors:** Omar Al-Refai, Ibrahim Shahbaz, Adam Ali Husseinat, Michael Mandulak, Jaewon Kim, Eman Hammad
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18548v1](http://arxiv.org/abs/2607.18548v1)
- **PDF:** [https://arxiv.org/pdf/2607.18548v1](https://arxiv.org/pdf/2607.18548v1)
- **Categories:** cs.AI, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic artificial intelligence systems, capable of autonomous perception, planning, tool use, and multi-step action, are increasingly proposed for critical engineering domains where decisions carry physical, operational, or economic consequences. This survey addresses a gap in current literature by treating trustworthiness, whether agentic behavior can be verified, audited, and trusted under the constraints that engineering practice actually requires, as a first-class engineering property, rather than evaluating agentic AI by task capability alone. The study adopts a trustworthiness model organized around five cross-cutting dimensions: safety and constraint satisfaction; robustness and reliability; transparency and interpretability; accountability and auditability; and privacy and security. This is mapped onto an agentic assurance workflow spanning perception through audit. Building on this foundation, agentic systems architectures, threats, concrete trust mechanisms, and quantitative metrics are surveyed for direct application in agentic systems development and evaluation. These principles are then examined across four constraint-bound engineering domains: power systems, autonomous vehicles/robotics/UAVs, high-performance computing, and communication networks, identifying recurring design patterns, shared failure modes, and domain-specific gaps. Synthesizing across those domains, agentic AI trustworthiness is shown to be a single problem, with a path outlined toward a reusable, cross-domain assurance framework analogous to the graded certification regimes used by mature safety-critical engineering fields.

</details>


### 91. MAGE: Human-Like Macro Placement via Agentic Multimodal Reasoning

- **Authors:** Andrew B. Kahng, Sayak Kundu, Bodhisatta Pramanik
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18536v1](http://arxiv.org/abs/2607.18536v1)
- **PDF:** [https://arxiv.org/pdf/2607.18536v1](https://arxiv.org/pdf/2607.18536v1)
- **Categories:** cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Macro placement still requires substantial manual refinement in industrial physical design flows. We present MAGE (Macro Placement Agentic Engine), a multimodal multi-agent framework for macro placement refinement. MAGE decomposes the macro placement task into a six-phase workflow that combines structured floorplanning rules, visual checks, and iterative refinement. Expert floorplanning knowledge is encoded through natural-language directives and validation criteria, rather than learned from labeled placement data. A tournament-style refinement mode evaluates multiple candidate placements and propagates feedback from higher-quality solutions. We also introduce four metrics for quantifying human-likeness in macro placement: notch score, whitespace score, pocket score, and alignment score. These metrics capture structural properties used by expert designers but not directly measured by conventional PPA metrics. Across nine designs in NanGate45 and GlobalFoundries 12nm enablements, MAGE achieves geometric-mean improvements of 11.1%-19.3% in WNS and 70.0%-74.0% in TNS over commercial macro placers. On the three NanGate45 designs, for which human-expert and Hier-RTLMP baselines are available, MAGE improves WNS and TNS by 18.3% and 72.5% over the human expert, and by 47.0% and 80.4% over Hier-RTLMP, with comparable wirelength and power. On human-likeness metrics, MAGE improves the overall score by 6%-48% over all baselines. Additional case studies on anonymized netlists, unseen designs, dense rectilinear floorplans, and high-utilization settings show that the framework transfers to new placement settings without design-specific retraining.

</details>


### 92. Structured Output Collapses Answer Diversity Across 44 Language Models

- **Authors:** Tapan Parikh
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18476v1](http://arxiv.org/abs/2607.18476v1)
- **PDF:** [https://arxiv.org/pdf/2607.18476v1](https://arxiv.org/pdf/2607.18476v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a language model must choose one answer from a large space of equally valid options, a format clause -- "Reply with JSON only" -- changes which answer it chooses. We re-run the One-Word Census (arXiv:2607.12796): 31 wide-answer-space category prompts asked of 44 models, now with the reply requested in JSON -- no schema enforcement, no constrained decoding, only the request. Convergence deepens sharply: on the unconstrained "Pick a word" prompt the modal answer rises from 41% to 64% of the pool and distinct answers fall from 52 to 36; mean answer-choice surprisal drops from 1.80 to 1.58 bits. The tax is progressive: six of 44 models move individually (BH-FDR q=.10), all toward the mode, led by the most distinctive models, while the conformist floor is immobile. It is a sharpener, not a re-indexer -- the plain-chat modal answer survives in 28 of 31 categories. Defaults are register-indexed: a within-run re-sample (n=20) finds JSON shifts 53% of a model's stable chat defaults, mostly back to the crowd, and installs defaults absent from chat (Claude Fable 5 answers "cerulean" for colour 0% of the time in chat, 100% in JSON). Full-battery controls reveal a register gradient: compression is significant and specific to the answer-delivery formats models are trained to speak (JSON -0.22 bits, p=.0002; XML -0.19, p=.002), absent for YAML and CSV, and reversed for an arbitrary bracket wrapper (+0.13, p=.009) -- weighing the mechanism toward tool-use post-training. Enforcing the schema at the decoder (response_format) compresses no further than the request (-0.03 bits): the collapse lives in the model's response to the register, not the decoder. Structured output is how software consumes language models, and that surface is served by a measurably more homogeneous model than the chat surface on which models are evaluated, compared, and chosen.

</details>


### 93. ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems

- **Authors:** Elias Hossain, Md Mehedi Hasan Nipu, Fatema Tuj Johora Faria, Tasfia Nuzhat Ornee, Maleeha Sheikh
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.19430v1](http://arxiv.org/abs/2607.19430v1)
- **PDF:** [https://arxiv.org/pdf/2607.19430v1](https://arxiv.org/pdf/2607.19430v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM applications chain a planner, worker agents, a verifier, and a synthesizer, and every hop between agents is an unmonitored channel through which an adversary can smuggle instructions. Existing defenses guard only the input boundary (IBProtector, Llama Guard, perplexity filters, SmoothLLM) or run outside the application as opaque, stochastic provider-side filters. We show this gap carries a consequence rarely measured: on a 2,100-trace evaluation across eight attack families, five defenses, and three model backends, an undefended pipeline that appears fully safe under standard reporting (attack success 0.000 on tool- and memory-poisoning) owes that safety almost entirely to the cloud provider's server-side filter (54 of 60 blocks on Azure GPT-5), and silently shifts to the agent model's own alignment on a backend without such a filter. Outcome-only reporting hides this dependence. We present ChannelGuard, a training-free defense-in-depth framework placing information-bottleneck gates on every inter-agent channel; each scores channel text against an adversarial phrase bank by embedding similarity and deterministically passes, compresses, or blocks it, adding no LLM call, while an attribution method records which layer stopped each attack. ChannelGuard's tool-output gate blocks Tool Poisoning 30 of 30 at the application layer, identically across Azure GPT-5, Anthropic Sonnet 4.5, and Anthropic Haiku 4.5, whereas the undefended pipeline shifts entirely across backends; it also lowers Prompt Injection attack success by half (0.333 to 0.167) and preserves GSM8K accuracy exactly (0.867). White-box adaptive paraphrase evades every embedding gate, where a perturb-and-vote baseline does better. An extended appendix adds baselines, ablations, sweeps, a benign-preservation analysis, and a judge audit (kappa = 0.900), at a total cost of 47.36 USD.

</details>


### 94. Operational Hallucination and Safety Drift in AI Agents

- **Authors:** Shasha Yu, Fiona Carroll, Barry L. Bentley
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18366v1](http://arxiv.org/abs/2607.18366v1)
- **PDF:** [https://arxiv.org/pdf/2607.18366v1](https://arxiv.org/pdf/2607.18366v1)
- **Categories:** cs.AI, cs.CL, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) serving as planners in tool-using autonomous agents introduce dynamic reliability risks in multi-turn execution. While single-turn safety mechanisms are relatively mature, extended interactions reveal structural vulnerabilities where initial alignment degrades over time. This paper empirically characterizes two observed failure modes across multiple state-of-the-art LLMs: Safety Drift, the gradual erosion of declared safety intent leading to constraint-violating actions (e.g., textual refusal followed by reconnaissance and unsafe execution), and Operational Hallucination, persistent repetitive tool calls indicative of flawed state perception (e.g., livelocks even in legitimate tasks). Through controlled multi-turn evaluation on high-stakes ethical dilemmas, malicious requests, and benign controls, we quantify these phenomena using declaration-action gap and livelock metrics, demonstrating their cross-model prevalence under direct execution protocols. Root-cause analysis attributes the instabilities to the decoupling of reasoning context from execution state in current agent loops. We propose an Action-Aware Supervision Layer - a lightweight, plug-and-play architectural blueprint incorporating intent-action consistency checks, runtime state tracking, and forced termination primitives. Post-hoc simulation on captured failure trajectories shows the layer can intercept observed violations without false positives on benign cases. This work advances agent reliability by shifting focus from linguistic safeguards to enforceable architectural mechanisms for responsible agentic AI.

</details>


### 95. LLMs and Agentic AI Systems for Smart Grids: A Tutorial on Architectures and Applications

- **Authors:** Daniela Rojas, Abdulwahab Albassam, Aidan G. Leung, Jett Ngo, Ryan Luo, Peter R. Quawas, Junpyung Kim, Kangkai Liang, Mansi Nanavati, Jonathan Mai, Meng-Chi Tsai, Yun-Tong Tsai, Yize Chen, Yuanyuan Shi
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18147v1](http://arxiv.org/abs/2607.18147v1)
- **PDF:** [https://arxiv.org/pdf/2607.18147v1](https://arxiv.org/pdf/2607.18147v1)
- **Categories:** eess.SY, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) and agentic AI systems have evolved from natural language tasks to using external tools to plan, retrieve, and act in technical domains. In smart grids, recent work applies agentic schemes to forecasting, optimization, and control, wrapping trusted solvers behind language interfaces and orchestrating multi-step workflows. The literature lacks a unified approach to designing and evaluating such systems. LLMs can produce numerically plausible yet physically infeasible outputs, evaluation protocols vary across tasks, and the boundary between what the model should and should not compute is implicit. This paper presents a solver-grounded design principle: a numerical result is reported only when it originates from a trusted tool and passes explicit verification. We review the building blocks of LLM and agentic AI systems for power systems: prompting strategies and agentic architectures. We instantiate the principle in four case studies: wind power forecasting, EV charging scheduling, power flow analysis, and contingency diagnosis, each comparing an LLM-only baseline against its solver-grounded counterpart on identical data and metrics. EVAgent reproduces the CVXPY optimum while reducing LLM-only unmet energy by 7.5-9.5x, and GridDebugAgent repairs 17/39 contingency cases while reducing total violations by 52.3%. We propose a four-group evaluation framework spanning task utility, solver-grounded correctness, faithfulness and safe failure, and cost and latency. A consistent division of labor emerges: the agentic system reliably orchestrates, retrieves, and explains, while trusted tools compute and a verification gate decides what is reported.

</details>


### 96. FinSAgent: Corpus-Aligned Multi-Agent RAG Framework for Evidence-Grounded SEC Filing Question Answering

- **Authors:** Jijun Chi, Zhenghan Tai, Hanwei Wu, Tung Sum Thomas Kwok, Hailin He, Zixing Liao, Bohuai Xiao, Chaolong Jiang, Jianliang Lei, Jerry Huang, Peng Lu, Muzhi Li, Liheng Ma, Yihong Wu, Sicheng Lyu, Jingrui Tian, Yihan Li, Yanzhang Ma, Sizhe Guan, Dingtao Hu, Yufei Cui, Ling Zhou, Lei Ding, Xinyu Wang
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18102v2](http://arxiv.org/abs/2607.18102v2)
- **PDF:** [https://arxiv.org/pdf/2607.18102v2](https://arxiv.org/pdf/2607.18102v2)
- **Categories:** cs.IR, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Financial question answering over U.S. Securities and Exchange Commission (SEC) filings requires retrieving and synthesizing heterogeneous evidence dispersed across long, standardized, and highly redundant disclosures. Existing retrieval-augmented and multi-agent systems typically derive retrieval queries directly from the user's question and rank candidates by semantic similarity. Together, these choices create prior-corpus misalignment: a mismatch between model priors and the target filings' structure, terminology, and evidence standards. As a result, query generation misses corpus-specific evidence, while semantic reranking favors topically similar but evidentially invalid false-positive chunks. We propose FinSAgent, an evidence-grounded multi-agent framework that reframes SEC filing QA as corpus-aligned retrieval planning and corrects both ends with a single principle: inject corpus-side conditioning wherever model priors would otherwise dominate. FinSAgent combines (1) role-specialized agents anchored to the mandated 10-K item structure, (2) database-aware query decomposition that conditions each agent's sub-queries on a lightweight, summary-level view of the local corpus, and (3) multi-path retrieval with a learned feature-gated reranker that separates evidential validity from semantic similarity. Across five offline financial QA benchmarks, FinSAgent improves retrieval coverage and answer correctness over strong single-agent and multi-agent baselines; in a three-arm randomized online experiment with 1,000 anonymous user ratings, it also receives higher scores than baselines.

</details>


### 97. Autoresearch with Coding Agents: Generalizers and Metric-Maximizers on Quran Recitation Data

- **Authors:** Nursultan Askarbekuly, Mohamad Al Mdfaa, Ahmed Helaly, Gonzalo Ferrer, Manuel Mazzara
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18064v1](http://arxiv.org/abs/2607.18064v1)
- **PDF:** [https://arxiv.org/pdf/2607.18064v1](https://arxiv.org/pdf/2607.18064v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coding agents can now be left alone to improve software against a score. In this pattern--recently popularized as "autoresearch"--the agent receives a dataset, an evaluation script, and one editable file, and iterates without supervision: modify the code, measure, keep the change if the score improves. But what does the agent actually optimize--the developer's intent, or the literal number? We ran this loop on a real production task: deciding which Quranic verses appear in a noisy speech-recognition transcript and splitting the transcript by verse. Two frontier coding agents, Claude Code and OpenAI Codex, started from the same blank file with the same instructions, budget, and reasoning effort, three runs each. Both independently invented the same algorithm (canonicalization, n-gram anchoring, dynamic-programming alignment)--and then diverged. Claude stopped early with compact, general code. Codex drove the score ~10x lower, largely by memorizing answers to individual evaluation rows (19-41 hardcoded verse ids per run): a clean natural instance of specification gaming by a production agent. In a preregistered second study, we added a held-out test set and told both agents it existed. The memorization vanished, and the score gap vanished with it--yet Codex's general core transferred better and more consistently (held-out detection+split 0.085+/-0.004 vs. 0.121+/-0.031), losing only on one missed rejection of non-recitation input. Two exploratory community arms (Cursor, Antigravity) are consistent with the pattern. Every agent's held-out solution matched or beat the hand-engineered pipeline it was built to replace--the best by an order of magnitude--and now runs in production. From the ways agents exploited our harness--reading sibling runs through shared git state, leaving notes to "future runs" in persistent memory--we distill five design rules for evaluating autonomous agents.

</details>


### 98. Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security

- **Authors:** Devina Jain, David Hartmann, Chuan Li
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18063v1](http://arxiv.org/abs/2607.18063v1)
- **PDF:** [https://arxiv.org/pdf/2607.18063v1](https://arxiv.org/pdf/2607.18063v1)
- **Categories:** cs.CR, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents process external content, exposing them to prompt injection and multi-turn manipulation. Most safety benchmarks evaluate defenders against fixed attack pools collected before evaluation, single-turn or multi-turn. We present a 21-scenario benchmark for \emph{adaptive multi-round attacks against memoryless LLM defenders}: an autonomous LLM attacker observes prior defender responses and pivots across rounds, while each defender response is evaluated as a fresh interaction. Holding the 21 scenarios, attackers, defenders, and structured-output scoring fixed, restricting scoring to the first attacker turn yields $0$-$1\%$ attack success rate (ASR); allowing 15 rounds of adaptive attack yields $5.4$-$14.0\%$. Pooling three frontier attacker LLMs uncovers $1.4$-$2.2\times$ as many unique successful attacks as the best single attacker, and the generated attacks have low cosine similarity ($0.02$-$0.14$) to attacks in existing benchmarks. Claude Opus 4.6 and GPT-5.4 are tied in aggregate ($5.4\%$ each; overlapping $95\%$ CIs), but their weaknesses differ sharply: on one scenario Opus reaches $60\%$ ASR ($95\%$ CI $36$--$80\%$) while GPT-5.4 and Gemini each stay at $7\%$ (CI $1$-$30\%$; the gap is preserved in a higher-$N$ replication). $13$ of $21$ scenarios distinguish at least one defender pair, yet rankings disagree across scenarios (Kendall's $W = 0.19$). We release the benchmark -- 21 evaluation scenarios, 10 public development scenarios, the orchestrator, baseline harnesses, and a multi-attacker CLI -- plus 945 transcripts from the 3$\times$3 frontier matrix, an attack-replay dataset, and 18{,}422 gpt-oss-20b battles from an open competition's final scoring rounds.

</details>


### 99. Natural Language Access to Domain-Specific Metadata: A Reusable Framework for LLM Query Generation

- **Authors:** Blake G. Fitch, Cato Elia Kurtz
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18029v1](http://arxiv.org/abs/2607.18029v1)
- **PDF:** [https://arxiv.org/pdf/2607.18029v1](https://arxiv.org/pdf/2607.18029v1)
- **Categories:** cs.DB, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Researchers need to answer ad-hoc questions about the contents of domain-specific archives but often lack the expertise to write structured queries on the metadata. We show that when domain vocabulary and semantics are captured in a well-designed Web Ontology Language (OWL) ontology, Large Language Models (LLMs) can generate accurate structured queries zero-shot, without fine-tuning, retrieval augmentation, or multi-agent orchestration. We present the Natural Language Knowledge Graph Query (NLKGQ) system, a framework and development process that enables natural language access to metadata in such archives. The framework includes a web interface that helps researchers pose natural language questions, which a domain-agnostic harness translates to SPARQL via an LLM and executes against a knowledge graph. The development process begins with capturing domain vocabulary and semantics in a formal OWL ontology. Domain-specific code then extracts metadata from archive sources and imports it into a knowledge graph defined by the ontology. Both are designed for reuse across domains. We demonstrate the system on metadata derived from a large-scale neuroimaging research archive, evaluating multiple LLMs and ontology representations. The best configurations achieve 100% accuracy on a competence and regression question set developed with domain experts. An ablation study across eight ontology representations reveals that readable entity names and semantic annotations are the dominant factors in accuracy, more significant than model choice or prompt engineering. We also compare SPARQL to an auto-generated SQL database as query backends, showing that OWL's structural features provide a substantial advantage over SQL DDL for LLM-driven query generation. Our demonstration domain also requires local LLMs on modest institutional hardware to address privacy concerns for human subject data.

</details>


### 100. MADA-RL: Multi-Agent Debate-Aware Reinforcement Learning for Parameter-Efficient Reasoning in Compact Models

- **Authors:** Martino M. L. Pulici, Cuong Xuan Chu, Evgeny Kharlamov, Zifeng Ding, Volker Tresp, Yunpu Ma
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18006v1](http://arxiv.org/abs/2607.18006v1)
- **PDF:** [https://arxiv.org/pdf/2607.18006v1](https://arxiv.org/pdf/2607.18006v1)
- **Categories:** cs.LG, cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models achieve strong reasoning performance, but often at prohibitive training cost - a challenge that is especially acute for compact models ($\leq 4 \, \mathrm{B}$ parameters) trained under limited budgets. We introduce MADA-RL, a post-training framework that specializes compact models into generator and critic roles and trains them with a debate-aware learning signal, fine-tuning only a small subset of parameters via LoRA adapters. Our central contribution is a counterfactual critic advantage: a dynamic, role-conditioned baseline that redefines the critic's advantage as its reward minus the generator ensemble's per-instance accuracy. This explicitly optimizes critics to improve over generator consensus rather than to merely reproduce a correct answer, yielding more targeted credit assignment than static mean-reward normalization. At deployment, the specialized agents are composed in a lightweight multi-round protocol. Across five mathematical reasoning benchmarks, MADA-RL raises the accuracy of the DeepSeek-R1-Distill-Qwen-1.5B model from $39.9 \, \%$ to $41.9 \, \%$ ($+2.0$ points, $p < 0.001$) using $16$ times fewer trainable parameters than fully fine-tuned baselines, placing it on the accuracy-trainable-parameter Pareto front. It approaches, but does not surpass, the strongest baselines (DeepScaleR, STILL-3), which are trained on substantially larger datasets; we analyse this gap and the associated inference-time cost directly. A controlled study isolates the source of MADA-RL's gains: the counterfactual advantage produces the highest critic improvement rate of any model evaluated, indicating that trained critics learn to correct generator errors rather than to imitate them.

</details>


### 101. Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?

- **Authors:** Yimeng Chen, Nathanaël Denis, Roberto Di Pietro, Jürgen Schmidhuber
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17986v1](http://arxiv.org/abs/2607.17986v1)
- **PDF:** [https://arxiv.org/pdf/2607.17986v1](https://arxiv.org/pdf/2607.17986v1)
- **Categories:** cs.CR, cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-hosted AI agents read and write their own memory and configuration files to function. An agent may get compromised via corruption of its own state -- a compromise realized via legitimate OS system call invocation. We refer to this class of threats as self-state attacks. In this paper, we investigate the OS resilience to this class of attacks. Formally, we characterize a four-axis attack space (Target, Mechanism, Granularity, Temporal); investigate the structural limits of prevention, detection, and recovery; and introduce a workload-conditioned view of detectability. To instantiate the framework, we collect live activity traces from a representative self-hosted agent running across distinct workload profiles, and realize the attack space as a 23-cell matrix, 43 concrete operations on real self-state files, and injected into those traces. We then evaluate both canonical and workload-conditioned defense strategies. The empirical results show that a layered defense stack (access-control prevention on the instruction and configuration layers, workload-conditioned detection on the memory layer, and periodic backup for recovery) is effective on most attack cells while a small residual attack surface remains structurally indistinguishable at the OS level. These findings suggest that against the newly established class of self-state attacks, OS-level defense needs to be reconsidered, potentially opening new research directions in the field.

</details>


### 102. Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization

- **Authors:** Zijian Zhao, Sen Li
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17924v1](http://arxiv.org/abs/2607.17924v1)
- **PDF:** [https://arxiv.org/pdf/2607.17924v1](https://arxiv.org/pdf/2607.17924v1)
- **Categories:** cs.MA, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent policy optimization, exemplified by PPO-based methods, is a key branch of cooperative Multi-Agent Reinforcement Learning (MARL). A central design question is how many neighboring agents\footnote{In this paper, "neighbors" refer not only to physical proximity but also to agents whose actions influence one another.} to aggregate in order to effectively utilize global information for cooperation. This decision must be made along two dimensions: in the advantage (which agents' rewards contribute to the credit signal) and in the ratio (which agents' likelihood ratios form the clipped importance weight). Existing methods occupy scattered, underexplored points on these two axes: IPPO treats both separately; MAPPO pairs a team-level advantage with per-agent ratios; HAPPO employs sequential ratios with per-agent advantages; and single-agent reductions operating on factorized joint policies aggregate both into fully joint products. We formalize these two design choices as support matrices $\SA$ and $\SR$, and prove a canonical structure: the expected multi-agent policy optimization objective depends on the pair $(\SA,\SR)$ only through their matrix product $\tS=\SR\SA$. This yields two key consequences: (i) Redundancy: the two support matrices are interchangeable with respect to the signal, meaning neither aggregation pattern is inherently superior.(ii) Variance Ordering: the advantage aggregates rewards as a sum (additive variance with an interior bias-variance optimum at the coupling neighborhood), whereas the ratio aggregates likelihood ratios as a product (multiplicative variance that grows exponentially with support size, with no accompanying bias reduction). The resulting design principle is unambiguous: aggregate neighbors in the advantage, sized to the coupling neighborhood, and keep the ratio per-agent.

</details>


### 103. PRIME: Plasticity Recovery in Multi-Agent Environments for UAV-Assisted Emergency Communication Networks

- **Authors:** Wen Qiu, Zhiqiang He, Wei Zhao, Hiroshi Masui
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17922v1](http://arxiv.org/abs/2607.17922v1)
- **PDF:** [https://arxiv.org/pdf/2607.17922v1](https://arxiv.org/pdf/2607.17922v1)
- **Categories:** cs.MA, cs.LG, cs.NI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Most reinforcement learning controllers for these networks assume stationary conditions, and the few that handle change react to the external environment while leaving the network's internal state unexamined. We show that sustained non-stationarity damages this internal state directly: as objectives shift, neurons progressively fall dormant and the shared policy loses the capacity to learn. The obvious remedy, resetting dormant neurons, is unsafe under shared-parameter multi-agent training: many neurons that appear inactive are still receiving strong training gradients, and whether a neuron appears dormant depends on which agent's observations it processes. PRIME (Plasticity Recovery In Multi-agent Environments) therefore verifies both directions before intervening. Extending the bidirectional Silent Neuron framework to cooperative multi-agent reinforcement learning, it aggregates activation and gradient statistics over the full team batch, reads the backward signal from the gradient the training loss has already deposited , not from a hand-crafted proxy, and reinitializes only neurons that are simultaneously activation-dormant and gradient-silent. Useful representations are preserved while learning capacity is restored. On a phase-switching UAV emergency communication simulator, PRIME improves interquartile mean return by 24.9\% over MAPPO and holds dormant neuron fractions at 10--20\% versus 40--45\%; ablations attribute the gains to the gradient signal and team-level aggregation rather than to the specific reset operator. A dynamic regret bound shows that the perturbation cost scales with the small silent-subspace dimension rather than the full parameter count.

</details>


### 104. Value-Aware Prediction for Robust Multi-Agent Coordination Under Communication Loss

- **Authors:** Kemal Devrim Kafadar, Eren Özaltun, Mahmud Efnan Şanlı, Feyza Orak, Emirhan Gazi, Kubilay Kağan Kömürcü, Nazım Kemal Üre
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17914v1](http://arxiv.org/abs/2607.17914v1)
- **PDF:** [https://arxiv.org/pdf/2607.17914v1](https://arxiv.org/pdf/2607.17914v1)
- **Categories:** cs.MA, cs.LG, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Robust multi-agent coordination relies heavily on inter-agent communication, which is frequently disrupted by physical and environmental constraints in real-world deployments. To maintain operation during these intermittent communication failures, agents can employ internal prediction models to estimate missing shared state information. However, predictors trained with standard reconstruction objectives treat all transitions equally. In a Reinforcement Learning context, this forces the model to waste capacity learning stochastic exploration noise and the outdated dynamics of suboptimal policies. In this paper, we propose a value-aware extension of Multi-Agent Observation Sharing under Communication Dropout (MARO) to patch communication gaps; we refer to this method as Value-Aware MARO. By dynamically weighting the predictor's loss function using advantage estimates derived from the underlying actor-critic architecture, our objective explicitly couples the predictor's learning process to the policy's evolution. This formulation focuses the model's capacity on the intentional, high-return dynamics actively reinforced by the agents. We evaluate our framework on several tasks within the Multi-Agent Particle Environment under varying communication reliability levels. Experimental results demonstrate that our approach maintains performance under declining communication reliability, particularly below 40%. While our method performs comparably in tasks where the baseline already maintains high coordination, our value-aware weighting effectively prevents the performance collapse observed in the standard predictor during high-attrition scenarios. In these environments, our method achieves an average improvement in mean returns of more than 20% and reduces performance variance by a mean of 64.7% compared to the standard unweighted baseline.

</details>


### 105. Decentralized Multi-agent Reinforcement Learning for Resilient Critical Infrastructures

- **Authors:** Minghui Ding, Evangelos Pournaras
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.18359v1](http://arxiv.org/abs/2607.18359v1)
- **PDF:** [https://arxiv.org/pdf/2607.18359v1](https://arxiv.org/pdf/2607.18359v1)
- **Categories:** cs.MA, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Critical infrastructures are increasingly distributed, interdependent, and exposed to evolving disruptions, making resilience a central requirement for their operation and control. This paper argues that decentralized multi-agent reinforcement learning (MARL) should be understood not merely as a distributed alternative to centralized training with decentralized execution but as a paradigm structurally aligned with the requirements of resilient critical infrastructures. This perspective is grounded in an analysis of the properties of decentralized MARL and the requirements of critical infrastructures, including scalability to large numbers of agents, support for privacy and local autonomy, robustness to failures, and interaction-driven adaptation among interdependent components. However, structural alignment alone is insufficient for practical deployment. This paper identifies credit assignment and communication as two central conditions for its practical feasibility. Credit assignment determines whether local learning remains aligned with system-level objectives, while communication determines whether coordination can be learned and maintained under realistic operational constraints. Building on these challenges, this paper proposes a research agenda focused on structure-aware, causality-aware, and resilience-aware credit assignment; communication for both coordination and credit assignment; and safe, timely, and recoverable decentralized learning under deployment constraints. Overall, this paper reframes decentralized MARL as a promising but conditional foundation for resilient critical infrastructures.

</details>


### 106. Zero Hallucination, by Construction: Hallucination-Aware Layered Oversight for Trustworthy Enterprise AI

- **Authors:** Bogdan Raduta, Horia Velicu, Alexandru Preda, Serban Chiricescu
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17883v1](http://arxiv.org/abs/2607.17883v1)
- **PDF:** [https://arxiv.org/pdf/2607.17883v1](https://arxiv.org/pdf/2607.17883v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprises will not deploy AI agents they cannot trust, and the most-cited reason for distrust is hallucination: confident, fluent output that is simply not true. The common response is to wait for a model that does not hallucinate. We argue that this is the wrong target. Large language models are, by construction, capable of generating unsupported text, and no amount of scale removes the possibility; a faithfulness judge bolted onto a raw model catches some errors but still ships others, and even well-curated retrieval pipelines have been shown to fabricate citations. We reframe the goal: "zero hallucination" is not a property a model possesses but a property a system enforces. We present HALO (Hallucination-Aware Layered Oversight), an assurance architecture which treats hallucination as a containable failure mode rather than an eliminable one. HALO composes six layers of defense: grounded generation over retrieved, approved content; constrained, deterministic execution that bounds where the model can err; multi-signal verification that scores every output for groundedness and hallucination using both an LLM judge and evidence-based checks against the source text; calibrated abstention, so the system declines rather than guesses when grounding is insufficient; total traceability of every retrieval, tool call, and generation; and continuous oversight that detects drift, alerts on threshold breaches, and closes the loop by regenerating and statistically validating improved agents. We detail each layer, give particular attention to evidence-based confidence (which verifies extractions against the source document rather than trusting the model's self-reported certainty), and illustrate the architecture on a regulated claims-extraction workload

</details>


### 107. Exploratory and Assimilating Reflection: Reflective Recall Cycle for Long-term Memory

- **Authors:** Ganesh Senrayan, Moyuru Yamada, Ishan Jindal, Kiran Purohit
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17879v1](http://arxiv.org/abs/2607.17879v1)
- **PDF:** [https://arxiv.org/pdf/2607.17879v1](https://arxiv.org/pdf/2607.17879v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based autonomous agents require external memory to overcome their statelessness and limited context window for long-term interaction and dynamic knowledge reasoning. However, existing memory retrieval methods often lack adaptability and sample efficiency, and struggle to retrieve the right mixture of memories from heterogeneous stores. We propose Exploratory-Assimilating Reflection (EAR), a framework for high initial retrieval performance and sample-efficient adaptation. EAR combines two mechanisms: Exploratory Reflection, which performs iterative search to bootstrap retrieval and collect useful experiences for each query, and Assimilating Reflection, which replays these experiences from an Experience Buffer to refine a global reranker more efficiently than methods relying only on immediate rewards. Experiments show that EAR improves retrieval by up to 17.9% over the baseline retriever on two long-term dialogue benchmarks. We also show that EAR is highly sample-efficient and robust to noisy feedback.

</details>


### 108. Lifelong Multi-Subsystem Pickup and Delivery with Buffer-Limited Handover Stations

- **Authors:** Chuanlong Zang, Isabelle Barz, Anna Mannucci, Philipp Schillinger, Florian Lier, Wolfgang Hönig
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17724v1](http://arxiv.org/abs/2607.17724v1)
- **PDF:** [https://arxiv.org/pdf/2607.17724v1](https://arxiv.org/pdf/2607.17724v1)
- **Categories:** cs.RO, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coordinating payload transfers between subsystems is a critical challenge in lifelong Multi-Agent Pickup and Delivery (MAPD). We study systems where agents are confined to separate regions and must exchange payloads through shared handover stations. These stations, equipped with single docks and finite buffers, are inherently vulnerable to blocking and starvation. We formalize this problem as Multi-Subsystem MAPD with Buffer-limited Handover Stations (MS-MAPD-BHS). We then propose Handover-Aware Reservation and Routing (HARR), an online controller that couples per-subsystem planners. HARR uses a shared dock reservation calendar and a deterministic rolling-horizon projection of buffer occupancy to coordinate actions. A candidate route is accepted only if its dock interval is free and the resulting buffer occupancy projection remains within capacity. Under perfect execution, these checks ensure collision-free dock use and buffer-safe committed operations within the reservation horizon. In simulation, HARR achieves up to 77% higher throughput and 92% lower backlog than a fixed-dock ablation at moderate load, while also reducing planning time relative to a coupled station-aware Token Passing baseline. These results show that explicit interface coordination substantially improves stability in modular multi-subsystem transport.

</details>


### 109. Verify, Repair, Repeat, or Stop? Robust Stopping for Noisy Verify-Repair Loops in LLM Agents

- **Authors:** Yitao Wu, Si Shen, Rui Yang, Hong Peng, Bin Hu
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17641v1](http://arxiv.org/abs/2607.17641v1)
- **PDF:** [https://arxiv.org/pdf/2607.17641v1](https://arxiv.org/pdf/2607.17641v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Verify-repair loops are a standard means for large language model (LLM) agents to correct faulty plans in code generation, mathematical reasoning, and tool use. When both the verifier and the repairer are noisy, repair can damage already-correct plans, and reported acceptance keeps rising while true validity falls, so existing methods lack a principled basis for deciding when repair should stop. We propose VRR-Stop, a robust stopping framework for noisy verify-repair-repeat (VRR) loops. A four-parameter noise model separates verifier false acceptance and false rejection from the repair and damage behavior of the repairer. Belief filtering turns repeated verification votes into an estimate of committed validity, and the loop commits or repairs according to the sign of the true marginal gain, which requires only sign identifiability rather than accurate recovery of all parameters. When verifier discrimination approaches zero, calibration itself fails and estimation error can flip the stopping sign, so we pair VRR-Stop with VRR-Guard, an estimation-free fallback that replaces the incumbent candidate only under a sufficient verification margin. On a GSM8K stress setting, VRR-Stop improves final true validity by 60.6 percentage points over fixed five-round repair at an average cost of 0.72 repair rounds. Across settings, stopping reliability is governed jointly by verifier discrimination and the decision margin rather than by the absolute size of estimation error.

</details>


### 110. Is Progressive Disclosure All You Need for Long-Context Agents?

- **Authors:** Yifeng He, Yinzhe Zhao, Jicheng Wang, Hao Chen
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17598v1](http://arxiv.org/abs/2607.17598v1)
- **PDF:** [https://arxiv.org/pdf/2607.17598v1](https://arxiv.org/pdf/2607.17598v1)
- **Categories:** cs.AI, cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-document question answering usually forces a choice between loading the whole document into the context window and bolting on a separate retriever. Agentic AI suggests a broader option, giving the agent the document path and letting it decide how and what to read. Agent Skills, a standard for packaging expertise into folders an agent loads on demand, supply a ready mechanism: progressive disclosure, which exposes only what a query needs, from a short description down to the specific passages. Practitioners rapidly adopted this pattern for book-length understanding tasks, but the evidence to support such choices has been anecdotal. We run the first controlled study of the pattern, comparing raw-document navigation and several designs of Agent Skills packs against a classical hybrid retriever across three agent harnesses and three model families on InfiniteBench. On a single book, the gain depends on the harness, running large when the agent navigates the raw document poorly but near zero when a strong agent harness already divides and retrieves on its own. When scaling up to tasks that span many books, raw-document navigation collapses while one-level progressive disclosure degrades more slowly and pulls ahead. A second, deeper routing level never helps and sometimes breaks accuracy outright, so one level is enough. Progressive disclosure buys context, not intelligence: it is redundant while a strong agent can locate the right passages itself, and decisive once the corpus grows too large to navigate by reading.

</details>


### 111. Reinforcement Learning: From Algorithms To Foundation Models

- **Authors:** Zihan Ding
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17560v1](http://arxiv.org/abs/2607.17560v1)
- **PDF:** [https://arxiv.org/pdf/2607.17560v1](https://arxiv.org/pdf/2607.17560v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) provides a framework for sequential decision making under explicit objectives. In its classical form, RL studies how an agent should act to maximise long-term reward in a dynamic environment. In richer settings, the problem extends beyond a single agent and fixed environment: intelligent behavior may require strategic interaction, adaptation to uncertainty, and reasoning over high-dimensional worlds. This thesis studies RL from two perspectives: algorithms in games and RL in the era of foundation models.
  The first part focuses on multi-agent RL in games. It examines how incentives, policies, and equilibrium concepts interact in competitive and general-sum environments, spanning two-player zero-sum games, large-scale video games, and multi-player settings with general structure. These works investigate learning in multi-agent systems and the behavior of RL methods in interactive environments. The second part studies RL with generative and foundation models, motivated by the idea that prior knowledge can enrich sequential decision making. Pretrained generative models and learned world models serve as representation tools and structured priors for planning, control, and policy optimization. The thesis develops diffusion-based world models, investigates RL for efficient video generation, explores generative models as policy classes, and studies interactive video world models in which actions shape future observations. It also addresses long-horizon modeling through architectures with memory. Together, these contributions present a unified view of RL as objective-driven adaptation in complex sequential domains. From strategic games to generative world models, the thesis highlights how RL connects decision making, environment modeling, and emerging foundation-model capabilities, offering a broader perspective on the principles underlying intelligent behavior.

</details>


### 112. Oracle Gap and Signal Fidelity: A Fixed-Pool Diagnostic for Test-Time Collaboration

- **Authors:** Jie Hu
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17531v1](http://arxiv.org/abs/2607.17531v1)
- **PDF:** [https://arxiv.org/pdf/2607.17531v1](https://arxiv.org/pdf/2607.17531v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Test-time collaboration, including self-consistency, best-of-N selection, critic models, and verifier pipelines, is often credited with broadly improving LLM reasoning, yet its gains are uneven and sometimes negative. We ask when training-free collaboration should be expected to help. For a fixed candidate pool, we decompose a selector or verifier's net gain into measurable factors: recoverable mass, verification-signal coverage, conditional selection quality, and harm to already-correct outputs. This reframes collaboration as a candidate-selection problem rather than as an intrinsic property of a multi-agent topology. Across LiveCodeBench, MATH Level-5 hard subjects, and GPQA-Diamond, gains are bounded first by the oracle gap and then by signal fidelity, which we measure directly as candidate-level agreement between verifier verdicts and official labels. On LiveCodeBench, a public-test verifier (MCC 0.825) gains +8.14 percentage points (pp) over a first-sample baseline; a generated-test verifier (MCC 0.248) improves by +2.70pp and is not statistically distinguishable from an LLM selector, but operates at near-zero harm versus the selector's 4.69% harm rate. On MATH, a symbolic answer-equivalence selector beats self-consistency by +4.67pp, while LLM selectors are negative. On GPQA-Diamond, recoverable mass is only 3.03% and 87.54% of candidate pools are answer-identical; a weaker model's pools shrink both further, suggesting that oracle gap is a joint property of task, model, and sampling configuration. Our framework yields a practical pre-deployment diagnostic: estimate the oracle gap, then measure coverage, signal fidelity, and harm before investing in collaboration.

</details>


### 113. Can AI Agents Really Complete RTL-to-GDS? Lessons from Benchmarking Tool-Interactive EDA Workflows

- **Authors:** Jinyuan Deng, Zhengrui Chen, Xufeng Wei, Tianyu Xing, Chenyi Wen, Qi Sun, Cheng Zhuo
- **Published:** 2026-07-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.17528v3](http://arxiv.org/abs/2607.17528v3)
- **PDF:** [https://arxiv.org/pdf/2607.17528v3](https://arxiv.org/pdf/2607.17528v3)
- **Categories:** cs.AI, cs.AR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are extending electronic design automation (EDA) beyond static RTL generation toward long-horizon, tool-interactive workflows. Yet it remains unclear whether general-purpose coding agents, even with domain-specific EDA skills, can reliably execute an end-to-end RTL-to-GDS flow encompassing synthesis, physical implementation, and engineering change order (ECO) optimization. We evaluate AI agents on a PicoRV32 RTL-to-GDS flow using commercial EDA tools under two timing targets. Their performance is assessed using end-to-end design score, stage completion, and Token ROI, a cost-efficiency metric relating design quality to runtime and cost. Comparing three agent architectures and four foundation models, we derive three practical lessons. First, domain-specific skills improve agents' understanding of individual subtasks but do not ensure reliable completion of a long-horizon EDA flow. Second, agents that achieve similar design progress can still differ by up to 141 times in Token ROI, revealing substantial differences in runtime and cost efficiency. Third, low-level tool-interface mismatches are a major source of physical design failures, particularly when Tcl commands depend on the tool version or execution mode. These results suggest that robust Agentic EDA requires not only stronger models but also structured tool interfaces, persistent design context, controlled execution, and process-level evaluation.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*