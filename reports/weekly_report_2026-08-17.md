# Weekly AI Agent Paper Report

**Generated:** 2026-08-17 09:58
**Period:** 2026-08-10 to 2026-08-16

## Summary

- **Total papers fetched:** 187
- **Papers matching keywords:** 162
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-08-10) | Change |
|--------|-----------|-----------|--------|
| Total matched | 162 | 161 | +1 |
| arxiv | 162 | 158 | +4 |
| biorxiv | 0 | 1 | -1 |
| medrxiv | 0 | 2 | -2 |

### Notable Trends

Comparison summary unavailable.

---




## Arxiv (162 papers)


### 1. Participatory Moral AI Is Not Neutral: The Invisible Hand of Developers

- **Authors:** Taenyun Kim, Edyta Bogucka, Daniele Quercia
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14522v1](http://arxiv.org/abs/2608.14522v1)
- **PDF:** [https://arxiv.org/pdf/2608.14522v1](https://arxiv.org/pdf/2608.14522v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI systems make more morally loaded decisions across society, one response has been moral preference elicitation. In this approach, researchers poll participants on hypothetical dilemmas and use the aggregated votes to train a policy that an AI model then applies at scale. Before any vote is cast, developers make three key choices in the moral AI elicitation pipeline: feature scoping, voter sampling, and question framing. In other words, they decide which features go to a vote, which voters to include, and how to present the question. These choices are often opaque, undocumented, and treated as technical details rather than normative ones. We examine each of these choices within a common empirical study and show that each can shape the preferences produced by moral AI elicitation. Across two phases (N = 809) in three deployment contexts (i.e., AI kidney allocation, AI agents simulating absent workers, and generative AI depictions of the deceased), we examine the three main stages of the moral AI elicitation pipeline. First, morally relevant features shift across contexts. This suggests that feature schemas should not be assumed to transfer across deployment domains. Second, preferences differ by political ideology for roughly one-third of features, with some differences reversing direction. The ideological composition of the voter pool can therefore affect the resulting aggregated preference profile. Third, the wording of the elicitation question can narrow or widen ideological gaps by up to a full scale point. The framing conditions also change how moral foundations are associated with participants' judgments. Taken together, these findings suggest that voting-based alignment cannot deliver fair or transparent AI by aggregation alone; at minimum, each stage of the moral AI elicitation pipeline should be audited and disclosed.

</details>


### 2. Wyvern: An Agentic Framework for Generating Grounded Multimodal Reports

- **Authors:** Beatrice Alessandra Motetti, Emilien Guandalino, Daniele Jahier Pagliari, Alessio Burrello, Lorenz K. Müller, Konstantin Berestizshevsky, Lukas Cavigelli
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14446v1](http://arxiv.org/abs/2608.14446v1)
- **PDF:** [https://arxiv.org/pdf/2608.14446v1](https://arxiv.org/pdf/2608.14446v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In the current artificial intelligence-driven innovation era, the pace of knowledge growth is accelerating, and is hard to keep up with. While generative models are increasingly used to synthesize content, they often lack in information grounding. To address these peculiarities of our time, we propose Wyvern, a multi-agent framework for the automated generation of grounded, multimodal technical reports. Wyvern allows for the generation of multimodal outputs, integrating images, tables, and text with supporting references in a unified report. Additionally, a particular focus is placed on the grounding of the content, with the implementation of a claims auto-revision stage. We conduct a human evaluation study to assess the quality of our proposed framework. The results show that the figures' informativeness is perceived as superior to that of a recent baseline in 87% of cases. Furthermore, Wyvern's reports are rated as more useful than those produced by three alternative methods in 63% to 100% of instances. We also carry out automatic evaluations showing that Wyvern gains up to 2.3$\times$ in citation recall and 1.6$\times$ in citation precision with respect to the baselines.

</details>


### 3. The Past and Future of AI Scientists

- **Authors:** Ross D. King
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14407v1](http://arxiv.org/abs/2608.14407v1)
- **PDF:** [https://arxiv.org/pdf/2608.14407v1](https://arxiv.org/pdf/2608.14407v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present a survey of the past and future of AI Scientists: machines capable of automating science. AI Scientists can originate hypotheses, deduce their consequences, design and execute experiments, interpret their results, and revise their beliefs. Such systems are integrated scientific agents, connected to the literature, formal knowledge, mathematical models, simulations, data-analysis systems and physical laboratories.
  Adam was the first machine to make novel scientific discoveries through cycles of hypothesis formation and physical experimentation. Eve established the architecture of the modern self-driving laboratory. Foundation models, autonomous agents and laboratory robotics now make it possible to build systems far more general than either Adam or Eve.
  The central problem is no longer whether individual components of science can be automated. They can. The problem is integration. AI Scientists must combine neural learning with logic, probability, mathematics, causal reasoning, simulation, experimental design, robotics and formal scientific records.
  AI Scientists have the potential to transform science: to make science faster, cheaper, more systematic and more reproducible. AI Scientists could investigate systems too complicated for unaided human science, and enable thousands of AI scientists to work together on single problems.
  The Nobel Turing Challenge sets the goal of developing by 2050 AI systems capable of automating Nobel-quality discoveries. Progress is ahead of schedule. When we succeed it will create a new form of science and transform the world.

</details>


### 4. Submodular Policy Learning for Distributed Task Allocation in Open Multi-Agent Systems

- **Authors:** Jing Liu, Luca Ballotta, Yangyang Yang, Fangfei Li, Yang Tang, Ruggero Carli
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14390v1](http://arxiv.org/abs/2608.14390v1)
- **PDF:** [https://arxiv.org/pdf/2608.14390v1](https://arxiv.org/pdf/2608.14390v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper studies policy learning for distributed task allocation in open multi-agent systems, where agents may join and leave in a time-varying fashion, with submodular stage team utilities. At each time, the active agents select actions from local categorical policies such that the feasible joint agent-action pairs form a partition matroid. Standard continuous relaxations of submodular set functions are based on independent Bernoulli sampling, making them inconsistent with agents' policies.To solve this mismatch, we propose the \emph{partition multilinear extension} (PME), a policy-based relaxation whose continuous support matches feasible actions under categorical policies.We prove that the marginal gains of the stage utility provide an unbiased estimator of the gradient of the PME and that maximizing the PME over action distributions is equivalent to maximizing the stage utilities over agent actions, which are critical to devise principled policy gradient.Building on this, we design \emph{SubMAPL}, a centralized-training decentralized-execution KL-mirror policy-learning method that uses local marginal gains as stochastic PME gradients during training. KL-mirror updates preserve categorical feasibility without Euclidean projection.In the case where agents run tabular-softmax policies, we introduce open policy migration and an open-system KL tracking variation to handle agent arrivals and departures. Using dynamic regret analysis, we establish a lower bound on the cumulative utility which accounts for the openness of the environment and for the gap between optimal stage-wise and global utilities. Simulations on multi-agent coverage demonstrate that SubMAPL outperforms policy-gradient and online-learning baselines.

</details>


### 5. AgentRewind: Recoverable Execution for Long-Horizon LLM Agents

- **Authors:** Yu Zhuang, Kefei Chen, Yitong Duan, Shuxin Zheng, Jian Li, Xu-Yao Zhang
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14380v1](http://arxiv.org/abs/2608.14380v1)
- **PDF:** [https://arxiv.org/pdf/2608.14380v1](https://arxiv.org/pdf/2608.14380v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Many real-world tasks require LLM agents to interact with their environments over long execution horizons. Errors that occur early in execution may propagate through both the agent context and environment state, and their effects may be difficult to reverse through subsequent actions. Existing methods mainly seek to reduce such errors through plan refinement and safety checks but provide little support after errors occur. To enable recovery during long-horizon execution, we present AgentRewind, a runtime recovery framework that records aligned checkpoints of the agent context and controlled environment, allowing agents to return to an earlier state and resume execution with information from previous attempts. We also construct MettleBench, a benchmark for evaluating task completion and partial progress on long-horizon engineering assignments containing a series of related requirements. Experiments across tasks, multiple models, execution strategies, and agent harnesses show that AgentRewind improves task success rate and average checklist progress over the compared baselines.

</details>


### 6. Wrong but Useful: Trajectory Value Beyond Answer Correctness in Multi-Agent Messages

- **Authors:** Chih-Hsuan Yang, Anjir Ahmed Chowdhury, Cheng-Hau Yang, Weijian Zheng, Fernando Llorente, Xiaolong Ma, Xinyang Li, Eliu A. Huerta, Ian T. Foster, Rajeev Thakur
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14375v1](http://arxiv.org/abs/2608.14375v1)
- **PDF:** [https://arxiv.org/pdf/2608.14375v1](https://arxiv.org/pdf/2608.14375v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent reasoning systems often use agreement, confidence, or automated scores to decide which messages should shape a final answer. Such filtering assumes that a message likely to be correct is also worth keeping. Yet a wrong answer can contain a useful decomposition, constraint, or scientific principle. We test this distinction with Diverse Hypothesis Deliberation (DHD), a controlled measurement protocol that caches five independently generated messages and replays the same downstream solver, called the integrator, with each message available or hidden. The replay comparison measures a message's trajectory value: whether making the message available helps or harms subsequent reasoning. Across five mathematics and science benchmarks and two openly available model families, gpt-oss-120b and gemma-4-31B-it, wrong-helpful messages appear in every benchmark-model combination. Among wrong-answer messages that change final correctness, more than four in ten changes are helpful in each model. Controlled repeats show that the number of repeatable message effects is unlikely to arise from replay variation alone (p=0.0002). A focused intervention on repeatable wrong-helpful messages finds that the complete message works best, while retaining its reasoning preserves more success than retaining only its answer; the source of the complete-message advantage remains open. Within the same problem, repeated trajectory-value evidence also identifies a better keep-or-remove choice than answer correctness alone. Answer correctness is therefore informative but does not determine trajectory value. DHD measures this missing property and produces reusable labels for learning when agents should listen.

</details>


### 7. ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond

- **Authors:** Mingming Zhao, Jiqian Dong, Kangping Xu, Zadid Hasan, Chengrui Fan, Shan Jiang, Shuai Mao, Ting Lingya, Linyi Zou, Tailin Zhou, Yun Hin Chan, Wenkai Zhang, Zhanhong Zhou, Guowei Huang, Hongliang Li, Wenjing Cun, Zhitang Chen, Mingxuan Yuan, Yanhui Geng
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14354v1](http://arxiv.org/abs/2608.14354v1)
- **PDF:** [https://arxiv.org/pdf/2608.14354v1](https://arxiv.org/pdf/2608.14354v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enabling LLM agents to sustain productive, stable, and goal-aligned research over extended horizons is a central challenge for autonomous machine learning and scientific discovery, as progress hinges on continuously managing evolving state, exploration decisions, and computational resources. Pioneering autoresearch agents, despite great success, still lack mechanisms for continuity, recovery from dead ends, and value-driven compute allocation, which inherently undermines overall search efficiency, wastes computational resources, and lowers the chance of ultimate success. To bridge this gap, we introduce ScienceFlow, an end-to-end autoresearch agent framework that organizes long-horizon research work into research segments grounded in executable workspaces. It represents research progress as recoverable executable states, enabling efficient exploration, revision, and execution. Transitions between research segments are governed by Executable-State Transition through Re-Anchoring (ESTRA), which selects either the live state or an archived state as the next anchor and determines whether to continue or redirect the research trajectory. An evidence-aware execution controller allocates resources to physical jobs based on resource availability, remaining budget, and validated progress. We evaluate ScienceFlow on tasks spanning machine learning, scientific modeling, and mathematical optimization. Results on diverse long-horizon benchmarks demonstrate its ability to sustain effective research processes, highlighted by a SOTA 70.22 percent Any-Medal score on the full MLE-bench within a 24-hour budget, outperforming prior reported results by 4.92 percentage points. The efficacy of ScienceFlow further demonstrates that efficient state management, adaptive exploration, and objective-aligned execution are critical for scaling autonomous research beyond short-horizon interactions.

</details>


### 8. ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning

- **Authors:** Ignacio D. Lopez-Miguel, Andreas Happe, Jürgen Cito, Ezio Bartocci, Bettina Könighofer, Martin Tappler
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14352v1](http://arxiv.org/abs/2608.14352v1)
- **PDF:** [https://arxiv.org/pdf/2608.14352v1](https://arxiv.org/pdf/2608.14352v1)
- **Categories:** cs.SE, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model (LLM)-based agents are increasingly used for complex tasks such as software testing and cybersecurity assessment. While these agents demonstrate impressive capabilities, their behavior is difficult to understand, explain, and analyze. Existing evaluations focus mainly on task success and execution traces, offering limited insight into the strategies employed by the agent. We present ATLAS (Automata Learning for Agent Trajectory Analysis and Strategy Discovery), an approach for recovering interpretable behavioral models from agent trajectories. ATLAS combines trace abstraction with automata learning to infer finite-state models that capture observed agent-environment interaction strategies. These models provide human-interpretable insights and support automated analyses of recurring behaviors, decision points, successful task-completion paths, and failure loops. As a proof of concept, we apply ATLAS to trajectories generated by an LLM-based penetration-testing agent. The resulting models expose high-level behavioral strategies for exploiting vulnerable machines that are difficult to identify from raw execution traces alone. We discuss how learned behavioral models can support explainability, model-guided exploration, auditing, and analysis of agentic systems. We further demonstrate symbolic model-based knowledge transfer from powerful frontier models to compact language models. In addition, we show how model transformations can derive concise explanations of agent behavior in a penetration-testing case study comprising 12 vulnerable machines. ATLAS highlights a new opportunity for model-driven engineering: transforming agent trajectories into explicit behavioral models that enable systematic understanding and analysis of otherwise opaque AI agents.

</details>


### 9. Clearing the Fog: Towards Installing and Refining Proactive Exploration Capabilities in LLM Agents

- **Authors:** Zhizhao Guan, Chen Huang, Ziming Liu, Hongru Liang, Wenqiang Lei, See-Kiong Ng, Tat-Seng Chua, Anthony G Cohn
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14339v1](http://arxiv.org/abs/2608.14339v1)
- **PDF:** [https://arxiv.org/pdf/2608.14339v1](https://arxiv.org/pdf/2608.14339v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study proactive exploration in LLM agents, i.e., the ability to explore an environment to acquire information that improves future decision-making. In this regard, we first identify two fundamental bottlenecks that hinder this capability and then propose \ours, a novel method designed to instill and refine proactive exploration. Specifically, \ours\ consists of two components: (1) Exploratory Data Construction, which synthesizes exploration-rich trajectories to mitigate the hindsight bias of standard demonstrations; and (2) RL Optimization with Contrastive Signal Guidance, which leverages contrastive trajectory pairs to distinguish productive exploration from redundant wandering. Extensive experiments demonstrate the effectiveness of \ours\ and provide insights into the characteristics of proactive exploration. Our code is available at: https://github.com/GuanZhizhao/SAFARI.

</details>


### 10. TimeSage-EV: A Live Benchmark for Agentic Time Series Analysis in Evolving Environments

- **Authors:** Qingren Yao, Yaxuan Kong, Yuqi Nie, Yichen Li, Stefan Zohren, Anna Vettoruzzo, Qingsong Wen, Ming Jin, Joaquin Vanschoren
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14270v1](http://arxiv.org/abs/2608.14270v1)
- **PDF:** [https://arxiv.org/pdf/2608.14270v1](https://arxiv.org/pdf/2608.14270v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Time series analysis in high-stakes domains relies on recurring data releases, where new observations can alter the evidence base and the validity of later conclusions. Existing time series QA benchmarks mostly rely on fixed snapshots, leaving temporal validity and cutoff-aware evidence use unevaluated. We introduce TimeSage-EV, a live benchmark for agentic time series analysis in evolving environments. It tracks 60 real institutional scenarios across 6 domains, comprising 1,485 scenario-period QA pairs from Feb 2023 to May 2026 and spanning monthly, weekly, daily, and irregular release cadences. At each period, large language model (LLM) agents receive time series data and source reports, while the withheld target release provides ground truth. TimeSage-EV evaluates state identification, data summarization, and outlook reasoning. Experiments with frontier LLM agents and TimeSage-1.0, a novel self-evolving agent with a reusable analytical skill library, reveal significant performance gaps across model tiers and recurring failures in temporal validity, exogenous context use, and adaptation. We release TimeSage-EV as a research resource with monthly updates, code, a leaderboard, and failure-mode analyses.

</details>


### 11. Polaris : Multi Agentic System for Conversational Enterprise Analytics

- **Authors:** Varuni H K, Soham Sarkar, Jay Kumar, Goutham Krishnan, Tanvi Johari, Avinash Bharadwaj, Santosh Hegde
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14246v1](http://arxiv.org/abs/2608.14246v1)
- **PDF:** [https://arxiv.org/pdf/2608.14246v1](https://arxiv.org/pdf/2608.14246v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In today's fast-paced environment, the ability to swiftly access, understand, and act on data is no longer optional; it is essential. Yet most organizations remain data-rich but insight-poor, constrained by the complexity of querying, interpreting, and explaining enterprise-scale information. We present Polaris, a supervisor-led multi-agent framework for conversational enterprise analytics that bridges this gap. Polaris introduces Dynamic Task Coordination (DTC), a decision-theoretic orchestration layer that models agent-task assignment as adaptive bipartite matching, enabling real-time coordination, recovery, and optimization across specialized agents for querying, visualization, and reasoning. By coupling DTC with reason-first, ReAct-style agents, Polaris transforms natural-language queries into coherent analytical workflows that not only retrieve and visualize data but also explain the underlying "why." Evaluation on structured enterprise datasets demonstrates high semantic fidelity and answer relevancy, underscoring the potential of multi-agent orchestration to deliver trustworthy, end-to-end business intelligence at scale.

</details>


### 12. Act2Intention: A Benchmark For Developing Active Mobile Agents Through Inferring User Intention from GUI Actions

- **Authors:** Xiaokai Yan, Jingtao Ding, Yong Li, Zhiwen Yu
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14132v1](http://arxiv.org/abs/2608.14132v1)
- **PDF:** [https://arxiv.org/pdf/2608.14132v1](https://arxiv.org/pdf/2608.14132v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mobile GUI Agents powered by multimodal large language models (MLLMs) show promise in human-computer intelligence. However, current research primarily focuses on reactive task execution while lacking a comprehensive understanding-prediction-execution process for user intentions, which are the core requirements of active agents. In this paper, we propose the Act2Intention framework that builds an active mobile agent by integrating understanding, predicting user intentions, and executing decisions. First, we construct the Act2Intention Bench through data collection and validated generation, comprising 72,511 intentions and over 700,000 actions across 52 apps, thereby establishing the first benchmark for evaluating proactive agents via continuous intention-action trajectories. We further develop the Act2Intention Agent, achieving proactive services through Proactive-oriented Intention Understanding, Personalized Proactive Intention Prediction, and Experience-guided Intention Execution. Experimental results show that supervised fine-tuning on Act2Intention Bench yields absolute improvements of +32.0 Acc-S, +10.25 Acc-S, and +6.9 SSR points over non-fine-tuned counterparts under the same agent framework for intention understanding, prediction, and execution, respectively. This success underscores the necessity and value of the Act2Intention Bench, which establishes a standardized platform for developing and evaluating proactive agents and consequently paves the way for research on intention-driven human-computer interaction.

</details>


### 13. A Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents

- **Authors:** Ismail El Hamraoui, Sagar Jose, Nicolas Bureau, Robert Plana
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14109v1](http://arxiv.org/abs/2608.14109v1)
- **PDF:** [https://arxiv.org/pdf/2608.14109v1](https://arxiv.org/pdf/2608.14109v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous LLM agents are increasingly deployed in complex real-world workflows, yet they remain vulnerable to runtime behavioral drift, a silent deviation from the original task that can lead to irreversible side effects on external systems. Existing approaches address drift at the prompt level but lack structured mechanisms for step-level detection, risk assessment, and recovery decision. Because the main task-executing agent is often a large and expensive model that cannot be re-trained on every deployment, this work targets a plug-and-play recovery module instead. It introduces a graph-based framework in which a single small language model is trained via reinforcement learning to specialize at each node of a recovery graph, external to the main agent. Each node has a precise role\,: drift classification, operation detection, risk evaluation, or final decision and the model learns to produce structured XML-formatted reasoning adapted to that role. Training combines rule-based structural rewards with an LLM-as-judge semantic-quality signal, so that the model is graded both on how it answers (schema and length) and on what it says. Experiments on the public AppWorld benchmark show that the method generally exploits information about the suspected drift onset to issue correct recovery decisions using a small language model. In addition, the trained small language model reliably respects the prescribed output schema and produces semantically appropriate content in each field according to its assigned node role.

</details>


### 14. Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails

- **Authors:** Giovanni Racioppi
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14074v1](http://arxiv.org/abs/2608.14074v1)
- **PDF:** [https://arxiv.org/pdf/2608.14074v1](https://arxiv.org/pdf/2608.14074v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly act on external systems through standardized tool-calling protocols such as the Model Context Protocol (MCP), yet no infrastructure layer constrains their actions to what a principal has verifiably authorized: authorization logic lives in application code, is neither signed nor independently auditable, and the resulting logs lack evidentiary value. We present Mandato, a governance proxy that enforces digitally signed mandates on agent actions at the protocol level. A mandate is a machine-readable, cryptographically signed authorization artifact specifying which tools an agent may invoke, under which parameter constraints and contextual conditions, for how long, and on whose behalf; the proxy evaluates every tool call against the applicable mandate chain, blocks non-conforming calls in line, and records every decision -- permit, deny, and the evidence for each -- in an append-only, hash-chained audit log designed for evidentiary use and periodically anchored via qualified timestamps. The mandate is deliberately modeled on the civil-law institution of delegation of authority, making the artifact legible to lawyers and auditors, not only to engineers. We give the mandate model and its decision semantics, the reference architecture as an MCP-transparent proxy with separated decision and enforcement points, and a mapping of the mechanism onto EU AI Act Articles 12 and 14, GDPR accountability, NIS2, and eIDAS 2, including a roadmap to qualified attestation through Qualified Trust Service Providers (QTSPs). We describe the implementation status of the reference system and a quantitative evaluation plan covering enforcement overhead, audit completeness, and tamper-evidence verification cost.

</details>


### 15. MACS: A Hybrid Multi-Agent Framework for Reliable Conversational E-Commerce Recommendation

- **Authors:** Juli Huang, Hannah Clay, Sajjad Beygi, Thomas Sarda, Negin Golrezaei, Amin Saberi
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14068v1](http://arxiv.org/abs/2608.14068v1)
- **PDF:** [https://arxiv.org/pdf/2608.14068v1](https://arxiv.org/pdf/2608.14068v1)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Conversational recommendation for e-commerce is increasingly mediated by large language models (LLMs), yet many real-world deployments operate under a stricter requirement: recommendations must be drawn only from a merchant's fixed catalog, without web search or unsupported product claims. In this setting, the main challenge is reliability under hard constraints: the system must satisfy user requirements, remain grounded in available inventory, and preserve preferences across multiple conversational turns. We present MACS (Multi-Agent Commerce System), a hybrid multi-agent framework for reliable conversational recommendation in fixed-catalog settings. MACS uses LLMs for language-facing tasks such as interpreting user requests, eliciting preferences, and generating responses, while correctness-critical operations, including product retrieval, hard-constraint filtering, brand exclusion, and progressive relaxation, are executed deterministically by the merchant agent. A session-persistent preference layer tracks constraints across turns, enabling consistent handling of budget overwrites and exclusion reversals. On a 140-query single-turn benchmark, MACS achieves the highest pass rate (87.1%) and perfect brand compliance (1.000). On a 10-scenario multi-turn benchmark, MACS achieves the strongest macro Pass@5 (72% vs. 56% GPT+Catalog / 52% Gemini+Catalog) with zero constraint drift. The advantage is sharpest on exclusion reversal (100% vs. 20% / 0%) and constraint accumulation (100% vs. 60% / 40%). Mean judged response quality is similar across systems (0.751 vs. 0.736). These results suggest that hybrid architectures combining deterministic constraint enforcement with session-persistent preference tracking provide stronger reliability-oriented performance than catalog-bound prompt-only baselines in the fixed-catalog merchant setting.

</details>


### 16. HERMES: a multi-agent framework for structured knowledge extraction from ultra-long documents in geoscience

- **Authors:** Ziqi Song, Zongyuan Xiang, James G. Ogg, Bruce S. Lieberman, Gabi Ogg, Natalia López Carranza, Wen Du, Yufei Ye, Shuan Li, Zhong Peng, Shaoqi Yu, Juye Wei, Ying Zhou, Jieping Ye, Jiang Yang
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14055v1](http://arxiv.org/abs/2608.14055v1)
- **PDF:** [https://arxiv.org/pdf/2608.14055v1](https://arxiv.org/pdf/2608.14055v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Authoritative scientific knowledge in geoscience remains largely trapped in legacy monographs and historical literature, where unstructured text and complex layouts hinder computational access. We introduce HERMES, a scalable multi-agent framework that extracts structured data from ultra-long scientific documents. Using a coordinating large language model, HERMES integrates domain constraints, validation rules and evidence tracing within a unified document-level extraction process that incorporates parsed text, tables, figures and captions. Applied to the 55-volume Treatise on Invertebrate Paleontology, the system produced a structured database of 32,277 fossil taxonomic entities and 451,878 attributes, released online at https://treatise.geolex.org. Extraction performance remained stable across fossil groups (average F1 scores of approximately 0.90 for entities and 0.91 for attributes), improving per-volume efficiency approximately sixfold relative to the tested fully manual baseline. Evaluation in palaeomagnetism and geochemistry, conducted without additional model training, demonstrated transfer across distinct geoscience domains. This work provides a practical pathway to transform historical scientific literature into FAIR-oriented structured data, offering a sustainable infrastructure for data-intensive disciplines and large-scale knowledge integration.

</details>


### 17. Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use

- **Authors:** Yi Ding, Yanzhao Yu, Xili Dai, Xianbiao Qi, Peiwen Sun, Xueqian Wang, Xiangyu Yue, Jianan Wang
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14047v1](http://arxiv.org/abs/2608.14047v1)
- **PDF:** [https://arxiv.org/pdf/2608.14047v1](https://arxiv.org/pdf/2608.14047v1)
- **Categories:** cs.RO, cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper integrates end-to-end Visual-Language-Action (VLA) models with agentic tool-use to propose Agentic Robot with Tool-use (ART). ART is a tool-injection framework that tunes any VLA model to leverage off-the-shelf tool modules for low-level vision, high-level affordance, and embodiment enhancement. Compared to vanilla VLA models with a whole continuous action solution space, ART reduces the complexity of the action solution space through tool-use, which not only improves generalizability across different tasks but also reduces data dependency. To demonstrate the advantages (high generalizability and low data dependency) of this framework, we first built a dataset of 30K tool-use trajectories and action demonstrations, which is much smaller than those used by baseline methods. We then designed a training regimen for long-trajectory tool-use reasoning in challenging environments. Experiments show that ART achieves a 20% higher success rate than mainstream baselines on simulation and real-world tasks, such as pick-and-place in the dark at novel viewpoints. Empirical results highlight the benefits of an agent-based approach: modular tool utilization enables more efficient training, lightweight deployment, and scalable integration of new tools. This design fosters robustness, adaptability, and extensibility, paving the way for the practical deployment of VLA systems in complex real-world scenarios.

</details>


### 18. Demystifying Agent Skills: Why They Work-Until They Don't

- **Authors:** Zhiyuan Jiang, Fangrui Huang, Hanwen Xing, Xander Wu, Yipeng Gao, Rui Cao, Mengdi Wang, Shilong Liu, Yijiang Li
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14036v1](http://arxiv.org/abs/2608.14036v1)
- **PDF:** [https://arxiv.org/pdf/2608.14036v1](https://arxiv.org/pdf/2608.14036v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Skills have emerged as a practical and effective approach for enhancing LLM agents at inference time through structured packages of knowledge. However, existing evaluations largely measure whether skills improve aggregated task success, leaving a more fundamental question underexplored: \emph{\textbf{When do skills help, why do they work, and where do they fail?}} Through controlled experiments across various benchmarks, agent harnesses and LLMs, we isolate the effects of representation, outcome annotation, retrieval difficulty, and cross-framework robustness of skills. To further answer this question, we design a contrastive study that combines controlled quantitative experiments with paired trajectory analysis. We normalize 8,135 trial records from controlled experiments and retain 238 valid unique labels from 240 open-coded records. We consolidate these observations into a taxonomy of three high-level categories and twelve skill-use modes: skills work when noisy trajectories become procedural anchors that stabilize execution. Skills improve over Workflow Memory by 6.06 points in matched comparisons. Procedural anchoring accounts for 65.7\% of skill cases, versus 4.5\% for explicit knowledge injection, showing that skills stabilize action rather than inject missing facts. Retrieval is a separate bottleneck: as pools grow from 5 to 100, actual-use precision falls from 29.6\% to 3.3\%. Confusable distractors impair offline identification, yet downstream success remains stable; exact ground-truth invocation is neither sufficient nor necessary. Skills fail under brittle assumptions, incompatible contexts, or insufficient adaptation. These findings move evaluation beyond aggregate success rates and guide reliable self-evolving agents.

</details>


### 19. MedClaw: Heuristic Agent Harness for Long-Horizon Surgical Video Reasoning

- **Authors:** Yingying Fan, Penghui Du, Leyan Zhu, Runze He, Zimeng Wu, Yuxuan Zhang, Liang Chen, Jiahao Xie, Jiangtang Wang, Shuai Shao, Anchao Yang, Yutong Bai, Yan Wang
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.14015v1](http://arxiv.org/abs/2608.14015v1)
- **PDF:** [https://arxiv.org/pdf/2608.14015v1](https://arxiv.org/pdf/2608.14015v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Understanding tens-of-minutes surgical videos requires long-horizon temporal reasoning, answering what happens before, after, or across stages of a procedure by grounding the question in visual evidence spread across time. Existing approaches handle this poorly: a one-shot vision-language model (VLM) compresses the whole procedure to fit its context window and loses the detail a "before" or "after" question depends on, while video agents that train the model where to look are data-hungry and transfer poorly to out-of-domain surgery. We build an agent harness that separates reasoning from perception and improves by evolving context rather than optimizing weights. A text-only orchestrator plans which evidence to gather and issues an auditable sequence of tool calls, while frozen vision-language sub-agents execute each call over the pixels, viewing, cropping, inspecting frames, and retrieving external knowledge. We further propose a gradient-free, reward-gated Heuristic Skill Distillation loop that mines the agent's own low-scoring traces and keeps a candidate skill only when it raises a validation reward, yielding reusable retrieval skills, notably directed re-look. Growing an external skill library rather than tuning weights, the loop adapts from only about 100 labeled examples, far fewer than supervised or reinforcement fine-tuning requires. To evaluate this agent, we introduce MedClawBench, a de-leaked, doctor-grounded benchmark of 1,123 questions over self-built long neurosurgery recordings and a held-out public lecture-video test split. Across both datasets and all four evaluation dimensions, our agent consistently outperforms one-shot VLMs and general video-agent frameworks, with the largest gains on the long, out-of-domain neurosurgery videos. Project page: https://fyycs.github.io/medclaw/.

</details>


### 20. XAI-Guided Conservative Decentralized Execution for Offline Multi-Agent Network Slicing

- **Authors:** Eslam Eldeeb, Hatim Chergui, Merouane Debbah
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13982v1](http://arxiv.org/abs/2608.13982v1)
- **PDF:** [https://arxiv.org/pdf/2608.13982v1](https://arxiv.org/pdf/2608.13982v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The recent advances toward sixth-generation (6G) and beyond-6G networks have accelerated the need for intelligent resource management mechanisms capable of supporting heterogeneous services under shared infrastructures in network slicing. However, resource allocation in network slicing naturally forms a resource-coupled cooperative optimization problem with competing slice demands. Slices compete for limited resources to minimize individual latencies while coordinating to avoid conflicts and underutilization. Although multi-agent reinforcement learning (MARL) has shown promising performance in such settings, existing online formulations remain costly, unsafe, and difficult to deploy due to their reliance on environmental interactions and communication among agents. In this work, we present explainable artificial intelligence (XAI)-guided conservative decentralized execution (X-CODE). X-CODE is an explainable offline MARL that operates offline without environmental interaction, nor inter-agent communication. It exploits explainability-aware reward shaping to modify the relative preference among joint offline transitions during centralized training to improve decentralized resource-allocation behavior. In deployment, the agents operate independently without signaling exchange among the agents. Simulation results demonstrate that the proposed approach achieves zero observed resource-conflict events in the evaluated test episodes while minimizing per-slice latencies. Moreover, the proposed framework exhibits lower signaling overhead and reduces effective inference latency by 88 % under the considered communication-delay model compared to the online baselines. Source codes and datasets are available through: https://github.com/Eslam211/xcode-ran-slicing.

</details>


### 21. Repair, Not Improvement: Decomposing Constrained Decoding in Tool-Call Abstention

- **Authors:** Janghoon Lee
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13959v1](http://arxiv.org/abs/2608.13959v1)
- **PDF:** [https://arxiv.org/pdf/2608.13959v1](https://arxiv.org/pdf/2608.13959v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Function calling is what the recent accounting of constrained generation explicitly sets aside: it finds the decoder's contribution small for format constraints, then warns in its Section 7 against extrapolating where a constraint encodes a correctness requirement, and names function calling as one. Tool abstention is that case at its sharpest: an enum leaves the wording of an answer alone and narrows the set of answers there are, and declining to call anything is the first it drops. We measure the excluded case. Three conditions over one byte-identical prompt separate a grammar's two jobs: it fixes where generation stops as well as which tokens may be emitted. We evaluate open-weight models from 0.6B to 4B on matched English and Korean items, so the language comparison is made within item. Against an unconstrained decoder, prior work's contrast is negative on abstention in four of six cells with intervals excluding zero, worst -29.5 points, and positive with an interval excluding zero in none. The total is a sum with opposite signs: on the smallest model in Korean the stop token costs -20.0, the enum returns +19.5, and the two leave -0.5. What it recovers is form: of 698 abstentions repaired, 545 had no readable answer and 0 were judgements the scorer refused. On tool-needed items it is positive throughout; abstention leads because it is the preregistered measure, and the pooled number being kinder to the intervention makes moving to it worse rather than better. Both preregistered language claims fail.

</details>


### 22. When Personal Memory Has No Single Answer: Evaluating LLM Agents under Irreducible Conflict

- **Authors:** Lu Yang, Shusheng Xu, Zhuoran Li, Tongkai Yang, Longbo Huang
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13921v1](http://arxiv.org/abs/2608.13921v1)
- **PDF:** [https://arxiv.org/pdf/2608.13921v1](https://arxiv.org/pdf/2608.13921v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly maintain personal memory across sessions, but it can conflict. Preferences depend on context, behavior evolves, and sources can conflict. When a query lacks context, time, or source authority to interpret conflict, treating one memory as definitive converts unresolved conflict into an unjustified, overconfident action. Existing benchmarks recover one answer from conflicting evidence, overlooking whether agents recognize underdetermination, preserve alternatives, seek missing information, and choose appropriate actions. We introduce \underline{T}esting \underline{A}gents' \underline{N}avigation of \underline{G}enuine, \underline{L}atent, and \underline{E}ntangled Memory Conflicts (\textsc{TANGLE}), a benchmark for genuinely unresolvable memory conflicts. It comprises 541 instances across 40 personas and three types: Context-Partitioned Conflict (CPC), Behavior-Oscillation Conflict (BOC), and Source-Contradiction Conflict (SCC). We evaluate two tracks---an oracle track with curated memory and a pipeline track that extracts memory from multi-session dialogues---on five dimensions: conflict perception, causal reasoning, confidence calibration, clarification seeking, and memory faithfulness. Experiments reveal pipeline challenges. With curated memory, models recognize conflicts more reliably than they calibrate actions or seek targeted clarification. With end-to-end pipeline memory, extraction fails to preserve conflict-bearing relations needed for downstream reasoning. Policy comparisons show fixed rules are insufficient when actions must reflect conflict. These findings motivate Conflict-Aware Action Policy (CAAP), which adapts actions to each conflict using available evidence. \textsc{TANGLE} frames conflict handling as recognizing underdetermination, retaining conflicting evidence, and acting without forcing a definitive answer.

</details>


### 23. Agentic Transaction: Towards ACID-Compliant Agent Systems

- **Authors:** Zhaoyan Sun, Xiaoxiao Wang, Guoliang Li
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13900v1](http://arxiv.org/abs/2608.13900v1)
- **PDF:** [https://arxiv.org/pdf/2608.13900v1](https://arxiv.org/pdf/2608.13900v1)
- **Categories:** cs.DB, cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are evolving from conversational assistants into autonomous systems that execute long-horizon tasks through reasoning, tool use, code generation, and workspace manipulation. As agents increasingly operate over persistent environments and multi-step workflows, they face challenges analogous to those addressed by transactional database systems: reliable execution, consistent outcomes, safe concurrency, and durable state management. We introduce the concept of an agentic transaction and propose an ACID-compliant agent system framework that reinterprets the classical ACID properties for agent execution through four semantic guarantees: Semantic Atomicity, Semantic Consistency, Semantic Isolation, and Semantic Durability. Together, these properties provide a principled foundation for building reliable agent systems despite model uncertainty and dynamic execution environments. To instantiate this framework, we develop an ACID-compliant data agent that realizes these guarantees through transactional exploration-execution-validation cycles, transactional skill hubs, confidence divergence-based validation, semantic dependency-aware isolation, and transaction-aware semantic state management. Experimental results on widely used benchmarks show that our system achieves a 10.6% improvement over state-of-the-art agents, including Claude Code. This work opens a broader research agenda on extending transactional principles and system architectures toward building trustworthy, scalable, and self-evolving AI agent systems.

</details>


### 24. Engineering Signals of Human-AI Collaboration in the Agentic Coding Era: A Longitudinal Analysis of 33,228 Pull Requests from vLLM and SGLang with Implications for Biomedical AI Agents and Bioinformatics Pipeline Developmen

- **Authors:** Jiada Li, Xuesong Ye, Olamide Olowoniyi
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13884v1](http://arxiv.org/abs/2608.13884v1)
- **PDF:** [https://arxiv.org/pdf/2608.13884v1](https://arxiv.org/pdf/2608.13884v1)
- **Categories:** cs.SE, cs.AI, cs.ET, cs.HC, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid adoption of AI coding assistants and autonomous agentic development systems has coincided with major changes in the pace and structure of open-source software engineering. Yet empirical longitudinal evidence of these changes at the team level remains limited. We present a descriptive longitudinal analysis of seven engineering metrics: pull request (PR) throughput, cycle time, contributor diversity, PR comment density, merge rate, new-author participation, and PR size. Metrics were computed from all merged PRs in two high-velocity AI infrastructure repositories, vLLM (February 2023-June 2026; 18,290 PRs) and SGLang (January 2024-June 2026; 14,938 PRs). We segment development into four eras aligned with major changes in AI-assisted software development and examine human- and bot-authored activities. Both projects show substantial increases in development velocity and AI-developer collaboration signals. PR throughput increased 21x in vLLM and 17.9x in SGLang, while bot-authored PRs accounted for less than 0.2% of this growth, indicating that the increase was overwhelmingly human-driven. In the latest era, median cycle time was 1.04 days for vLLM and 0.62 days for SGLang, while P90 cycle times reached 16.8 and 14.3 days, respectively. Monthly unique authors increased steadily in both projects, suggesting broader contributor participation. PR comment density increased 4.2x in vLLM and 3.8x in SGLang, with bot comments contributing an estimated 15-20% of the increase. In contrast, PR size remained relatively stable across eras. Overall, AI-assisted development is associated with higher throughput, broader contributor participation, and increased AI-developer collaboration signals in high-velocity open-source software development.

</details>


### 25. MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends

- **Authors:** Chaoqun Zhan, Qiang Zhou, Guannan Li, Zhenqiang Huang, Qianjin Wang
- **Published:** 2026-08-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13883v1](http://arxiv.org/abs/2608.13883v1)
- **PDF:** [https://arxiv.org/pdf/2608.13883v1](https://arxiv.org/pdf/2608.13883v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Most agent-memory benchmarks test post-hoc recall, whereas MemoryArena evaluates whether memory supports interdependent, multi-session task completion. We compare MemoryLake, a structured multi-track memory backend, with Mem0, text-embedding-3-small vector RAG, and a long-context control across all five MemoryArena domains. The systems share the same agent framework, requested gpt-5-mini model alias, task samples, and scoring code; the memory integration is the intentionally changed component. Because each backend bundles write, retrieval, consolidation, budgeting, and prompt-assembly choices, the study is a matched system-level comparison, not a representation-only ablation or a cost-matched experiment. On the shared evaluation sets, MemoryLake has the highest observed success rate (SR) in mathematics (9/40), physics (12/20), and progressive retrieval (4/20). Every system has zero SR in travel planning, and web shopping yields a single bundle-level success (long context, 1/150); MemoryLake ranks third on both the travel soft process score and shopping step match. Following MemoryArena's suite-level convention, a post-hoc equal-weight average over the five SRs is 20.5% for MemoryLake versus 13.6% for the best comparator. These are point estimates: sample sizes are modest, confidence intervals overlap, and we do not report paired significance tests. A separate MemoryLake-only run over all 221 progressive queries yields a failure-counted SR of 26.7% (59/221) and is not a baseline comparison. The results support a workload-dependent view of memory backends and an observed lead among the four evaluated systems on the shared sets; they do not establish benchmark-wide state of the art or a causal advantage of representation structure.

</details>


### 26. What preferences can - and cannot - predict in multi-agent online learning

- **Authors:** Omar Abbadi, Rida Laraki, Panayotis Mertikopoulos
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13810v1](http://arxiv.org/abs/2608.13810v1)
- **PDF:** [https://arxiv.org/pdf/2608.13810v1](https://arxiv.org/pdf/2608.13810v1)
- **Categories:** cs.GT, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We examine the interplay between ordinal, preference-based solution concepts in games and the long-run behavior of game dynamics, asking in particular to what extent the combinatorial data of a game -- its preference graph -- determine the outcomes of no-regret learning dynamics -- such as follow-the-regularized-leader (FTRL). In one direction, we show that the skeleton of every dynamically stable set (i.e. the set of pure profiles it contains) must also be preferentially stable, that is, it must be closed under profitable deviations. We then ask the converse question: when do preferences determine the long-run behavior of the players' learning dynamics? We begin by showing that preferences characterize asymptotic stability in the case of subgames -- i.e. subsets of pure profiles obtained by restricting players' action sets. Beyond this case however, the equivalence between dynamic and preferential stability collapses: concretely, we construct a three-player game with a preferentially stable set whose span is dynamically unstable, showing in this way that preferences do not suffice as a criterion of dynamic stability. We then bridge this gap via the notion of resilience under aggregate deviations, an easy-to-check payoff-based condition that guarantees asymptotic stability of arbitrary spans of pure strategies.

</details>


### 27. From Passive Delegates to Strategic Negotiators: Reinforcing Social Reasoning in Small Language Models with SocialRL

- **Authors:** Wenyue Hua, Zachary Huang, Tyler Payne, Safoora Yousefi, Saleema Amershi, Asli Celikyilmaz
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13787v1](http://arxiv.org/abs/2608.13787v1)
- **PDF:** [https://arxiv.org/pdf/2608.13787v1](https://arxiv.org/pdf/2608.13787v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly act on their users' behalf, handling tasks such as scheduling meetings, comparing offers, and haggling over prices. These principal-driven tasks routinely place the agent across from a counterpart (another user's agent, a seller, a recruiter) whose goals may conflict with its principal's. Yet the dispositions that make an assistant pleasant can make it a poor delegate: a friendly, helpful frontier model may disclose its principal's private information unprompted and concede at the first sign of resistance. We present SocialRL, a general recipe that trains social reasoning directly, and apply it to a 4B model across six domains: Deal-or-No-Deal, CaSiNo, Craigslist, Job Interview, Calendar, and Marketplace. Every domain is trained in-domain under the same recipe, and every policy is evaluated on all six. We find that (1) in-domain training reaches the frontier: on held-out scenarios the 4B matches or exceeds the GPT-5 family per domain, closing 73-122% of the baseline-to-frontier gap on the negotiation games, with 78% of buyer openings anchoring below target versus 3% untrained; (2) cross-domain transfer follows game structure: structurally paired games lift each other, a broad multi-issue donor lifts nearly all domains, and structurally isolated games transfer nothing; (3) guided by this transfer structure, two strategies, cascade RL and multi-teacher on-policy distillation (OPD), consolidate the per-domain specialists into a single unified 4B that reaches 0.627 average utility across all six environments, matching or exceeding GPT-4.1 (0.625), GPT-5.1 (0.619), and GPT-5.2 (0.613); (4) an explicit theory-of-mind scaffold helps only through training: distilling the ToM trace, rather than actions alone, lifts utility on every environment and generalizes better across them, and of the two ToM skills, only next-action prediction predicts negotiation outcomes.

</details>


### 28. Simulation-Aware In-Context Policy Improvement for LLM-Aided Analog Layout Refinement

- **Authors:** Bingyang Liu, Ziming Wei, Xiaohan Gao, David Z. Pan
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13767v1](http://arxiv.org/abs/2608.13767v1)
- **PDF:** [https://arxiv.org/pdf/2608.13767v1](https://arxiv.org/pdf/2608.13767v1)
- **Categories:** cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Analog IC layout design remains a labor-intensive iterative process dominated by simulation-driven refinement. Although end-to-end layout generators accelerate initial placement and routing, they still require experts to manually tune layout optimization parameters with repeated post-layout simulations for stringent design specifications. While Bayesian Optimization (BO) is widely adopted for parameter tuning in analog IC design, at the layout level it typically requires hundreds to thousands of evaluations, each involving costly parasitic extraction and post-layout simulation, which makes it impractical. Recently, Large Language Models (LLMs) have demonstrated potential in improving the sample efficiency of such simulation-driven tuning. However, their restricted access to geometric layout context and design-specific heuristics limits their ability to manipulate the layout optimization process. In this paper, we propose a simulation-aware LLM multi-agent framework that performs in-context policy improvement (ICPI) by iteratively updating layout optimization parameters exposed by an analog layout generator through an act-observe-reflect loop on compact structured layout representations. Experiments on real-world analog circuits show that, with only tens of post-layout simulations, our approach improves post-layout performance over the generator's built-in heuristics and BO-based tuning method.

</details>


### 29. TeachMateGPT: A Multi-Agent Knowledge-Grounded Framework for Pedagogical Assessment Generation from Science Curriculum Materials

- **Authors:** Fatema Tuj Johora Faria, Mukaffi Bin Moin, M. F. Mridha, Jubayer Al Mahmud
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13708v1](http://arxiv.org/abs/2608.13708v1)
- **PDF:** [https://arxiv.org/pdf/2608.13708v1](https://arxiv.org/pdf/2608.13708v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automatically generating textbook-grounded assessment items can reduce science teachers' workload, but existing retrieval-augmented generation (RAG) systems rely on flat retrieval, support only single-question generation, lack safeguards against weak evidence, and are ill-suited to low-resource, board-exam-structured curricula. We address these limitations with TeachMateGPT, a multi-agent system contributing four advances to curriculum-grounded science-assessment authoring. (i) COPE, a hierarchical knowledge base replacing token-window chunking with a multi-resolution index that segments documents along syllabus structure and links them at three granularities via a traversable graph-based lineage, matching evidence to each topic's instructional level. (ii) A staged, fail-closed agent pipeline replacing one-shot retrieve-then-generate: routing gates search, retrieval fuses dense and lexical evidence under a coverage gate that withholds generation on insufficient evidence, and specialist agents draft objective and constructed-response items. (iii) SAVER, a source-attributed verification protocol scoring faithfulness, relevance, and hallucination risk against retrieved evidence, applying stricter grounding checks across each creative question's four sub-parts, paired with teacher-in-the-loop evaluation rather than automatic filtering. (iv) NCTB-SciGen8, a curriculum-grounded dataset of 198 items (143 multiple-choice, 55 creative questions) spanning all 14 chapters of the NCTB Class 8 science textbook, produced by the pipeline and rated by three practicing teachers. TeachMateGPT raises faithfulness (0.68 $\rightarrow$ 0.96) and answer relevancy (0.60 $\rightarrow$ 0.89) over a vanilla RAG baseline.

</details>


### 30. CLAIR-Fin: An Adversarial Multi-Agent Framework for Claim-Level Verification and Adaptive Debate in Cross-Modal Financial QA

- **Authors:** Fatema Tuj Johora Faria, Mukaffi Bin Moin, Jubayer Al Mahmud, M. F. Mridha, Md. Alam Hossain
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13706v1](http://arxiv.org/abs/2608.13706v1)
- **PDF:** [https://arxiv.org/pdf/2608.13706v1](https://arxiv.org/pdf/2608.13706v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing defenses against hallucination in retrieval-augmented and multi-agent pipelines remain partial: evidence is trusted despite modality disagreement, debate verifies an aggregate report rather than individual claims, and such verification occurs only after drafting, leaving inter-agent errors undetected until the final text. To close this gap, we present CLAIR-Fin, a nine-agent framework that decomposes each question into atomic claims maintained in a typed Financial Claim Ledger. Each claim is resolved through Asymmetric Evidence Authority, which conditions evidence trust on claim type rather than treating all modalities as equally reliable; Chain-of-Custody Verification, which checks grounding at the hand-off between drafting and adversarial review rather than only at the pipeline's exit; an Adaptive Rebuttal Cycle, which routes contested claims through adversarial debate whose depth scales with what that debate finds; and a terminal entailment audit paired with a continuous Hallucination Risk Index that distinguishes claims that passed scrutiny from claims never contested. We evaluate CLAIR-Fin on BB-FinQA-X, a 500-question cross-modal financial evaluation set built from Bangladesh Bank Annual Report material, stratified by query type, format, and difficulty. Relative to a single-pass retrieval-augmented generation baseline, it raises faithfulness ($0.780 \rightarrow 0.889$) while abstaining on 5.4% of questions when evidence is insufficient rather than forcing an unsupported response, and it exceeds stronger retrieval-strategy baselines such as HyDE and Graph-RAG on faithfulness ($\leq 0.874$).

</details>


### 31. Second Thought: Reasoning in Parallel as LLM Agents Act and Observe

- **Authors:** Zhensu Sun, Chengran Yang, Yunbo Lyu, Jieke Shi, David Lo
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13667v1](http://arxiv.org/abs/2608.13667v1)
- **PDF:** [https://arxiv.org/pdf/2608.13667v1](https://arxiv.org/pdf/2608.13667v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents in the ReAct paradigm alternate between reasoning, acting, and observing, but deliberate reasoning is confined to the Thought phase: while the agent serializes an action and waits for the environment, its reasoning is frozen. We identify this recurring interval for Action and Observation as a reasoning idle window and ask whether it can host additional reasoning in parallel that serves future turns. Therefore, we propose Second Thought, a training-free inference framework that forks four auxiliary branches the instant each Thought phase concludes, decodes them concurrently with the main loop, and merges the generated thoughts back when the environment observation arrives. In this way, Second Thought relocates the added reasoning off the main thread's sequential decoding path. Across three agentic benchmarks and three reasoning LLMs, Second Thought lowers the average turn count in all nine (model,benchmark) pairs and reduces main thread decoding in six of them by up to 43% (roughly 20% on average among those settings), while leaving it essentially unchanged in a seventh; Pass@1 shows no significant change in seven of nine pairs and the two significant differences are +12.4 and +10.2 points. Against a compute-matched control that forces an equivalent budget onto the main thread's own reasoning, it attains strictly higher Pass@1 with 1.3 to 3.2 less sequential decoding in all four settings where the control applies.

</details>


### 32. OmniScientist: An Omni-Modal Omni-Discipline AI Scientist

- **Authors:** Bobo Li, Hao Fei, Tianjie Ju, Mong-Li Lee, Wynne Hsu
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13558v1](http://arxiv.org/abs/2608.13558v1)
- **PDF:** [https://arxiv.org/pdf/2608.13558v1](https://arxiv.org/pdf/2608.13558v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone does not provide access to the full evidence on which scientific discovery depends. Existing systems typically reason over text, code, labels, or precomputed summaries, leaving scientifically decisive spatial, temporal, cross-channel, and procedural relations unavailable to the agent. We introduce OmniScientist, an end-to-end, omni-modal AI scientist that conducts multidisciplinary research directly from heterogeneous raw evidence. A perception layer and 3 autonomous agents for ideation, experiment, and writeup operate within a deterministic pipeline, allowing observations to shape research questions, experimental decisions, and final claims throughout the research lifecycle. By running idea, rigour, and claim checks in code, the system enforces novelty screening, statistical validity, execution provenance, and numerical traceability. We evaluate OmniScientist on 36 real-data cases spanning 5 discipline families, 4 families of scientific evidence, and modalities including images, signals, audio, video, 3-D structures, trajectories, tables, formulae, and graphs. The system completes the full path from raw data to a compiled manuscript in all 36 cases and achieves a mean overall paper score of 6.3 with the reference reasoning backbone. In paired comparisons against a blind variant that receives only precomputed scalar features, direct perception improves all 7 evaluation dimensions and wins 85% of head-to-head judgments. These results show that lifecycle-wide perception is essential for evidence-grounded scientific discovery and provides a practical path toward broadly capable AI scientists.

</details>


### 33. Joint Communication-Control Strategy Optimization with Partially Nested Information Structures: The Linear-Quadratic Case

- **Authors:** Haoyi You, Kaiqing Zhang
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13535v1](http://arxiv.org/abs/2608.13535v1)
- **PDF:** [https://arxiv.org/pdf/2608.13535v1](https://arxiv.org/pdf/2608.13535v1)
- **Categories:** eess.SY, cs.MA, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

In this paper, we formalize a joint communication-control strategy optimization (JCCO) problem in multi-agent linear systems with quadratic costs, under the common-information-based (CIB) framework from decentralized stochastic control. For computational tractability, we focus on such JCCO problems with partially nested (PN) information structures (ISs). In particular, with a baseline communication protocol that leads to a PN IS, we establish a series of conditions under which the partial nestedness is preserved under the (additional) communication strategies to be optimized, while violating them may cause nonlinearity of the optimal strategies in general, with open-loop communication strategies. We then develop a dynamic-programming-based approach to compute the optimal control strategies of JCCO with open-loop communication strategies, which yields a set of closed-form Riccati Equations. As a byproduct of independent interest, such an approach also offers a way to solve decentralized linear-quadratic control with PN ISs and output feedback, under the CIB framework. Finally, we extend such an approach to JCCOs with closed-loop communication strategies, yielding a more tractable dynamic program than an infinite-dimensional CIB-belief-based one.

</details>


### 34. Vero: Can AI Agents Build Formally Verified Software Repositories?

- **Authors:** Zhe Ye, Hantao Lou, Yuechun Sun, Peiyang Song, Zhengxu Yan, Timothe Kasriel, Qingyang Zhang, Kaiyu Yang, Soonho Kong, Jingxuan He, Dawn Song
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13522v1](http://arxiv.org/abs/2608.13522v1)
- **PDF:** [https://arxiv.org/pdf/2608.13522v1](https://arxiv.org/pdf/2608.13522v1)
- **Categories:** cs.LG, cs.AI, cs.LO, cs.PL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly used for programming, but do not provide any guarantee on the correctness of generated code. Verified code generation, in which an agent produces both an implementation and a machine-checked proof of its specification, offers a stronger path toward trustworthy AI-generated software. Existing benchmarks in this direction either focus on individual functions or only evaluate proof generation with provided implementations. It is still an open question whether agents can make coherent implementation and proof choices across real multi-module codebases. To bridge this gap, we introduce Vero, the first benchmark to evaluate joint implementation and proof synthesis at the repository level. Vero contains 43 multi-module instances sourced from real-world repositories spanning Python, Dafny, Verus, and Coq, and covering diverse domains from cryptographic protocols to distributed systems. Each instance consists of a multi-module Lean 4 repository with predetermined API interfaces, manually curated formal specifications, and reference implementations, supporting both proof-only and code-and-proof evaluation modes. To improve benchmark reliability, Vero also includes an audit mechanism where agents are allowed to formally prove unsatisfiability of provided specification or incorrectness of reference code, which surfaces and corrects latent code and specification errors during curation. We evaluate frontier coding-agent configurations with Lean toolchain access. The strongest agent fully solves only 27 of 43 instances and closes no specifications on the hardest repositories. Vero provides a concrete testbed for measuring progress toward repository-scale verified software synthesis, where current agents still fall short. We release the benchmark, curation pipeline, and evaluation harness at https://github.com/sunblaze-ucb/vero.

</details>


### 35. MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination

- **Authors:** Saisha Shetty, Satvik Tripathi, Austin Lin, Colin Zhao, Theodore Kim, Don Enwerem, Jacinta Arnold, Shahriar Faghani, Tessa S Cook
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13476v1](http://arxiv.org/abs/2608.13476v1)
- **PDF:** [https://arxiv.org/pdf/2608.13476v1](https://arxiv.org/pdf/2608.13476v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present Multi-Agent Reasoning and Coordination (MARC), an open-source framework that replaces monolithic LLM prompting with deterministic multi-agent orchestration for clinical reasoning. MARC coordinates role-specialized agents for extraction, reasoning, answer generation, and evaluation, with explicit context passing and traceable intermediate outputs, enabling stage-wise failure attribution. We additionally introduce a Decomposer module that generates task-specific agent prompts from a plain-language description, eliminating manual prompt engineering. The framework supports both API-based and local CPU-compatible deployments and is entirely configurable via YAML, without code modifications. MARC is designed to be model-agnostic, interpretable, and accessible to clinical domain experts without programming expertise. The full framework is available at https://github.com/Penn-RAIL/MARC-v1.

</details>


### 36. AaLLM: An End-to-End Analog Circuit Design Framework from Topology Generation to Sizing Using Large Language Models

- **Authors:** Mohammed Ayman Habib, Rylan Hart, Morteza Fayazi
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13472v1](http://arxiv.org/abs/2608.13472v1)
- **PDF:** [https://arxiv.org/pdf/2608.13472v1](https://arxiv.org/pdf/2608.13472v1)
- **Categories:** eess.SY, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Analog circuit design is a time-consuming, iterative process in a nonlinear and high-dimensional design space that relies heavily on expert intuition. Among recent developments, LLMs have introduced a promising approach by bringing natural language reasoning to circuit design tasks. The majority of conventional LLM-based approaches provide fragmented solutions that focus either only on sizing or topology generation. These methods require adding specific technical knowledge manually, which is inefficient and prone to hallucinations during circuit sizing. Moreover, the inherent trade-off in meeting different specs makes current approaches iterative and tedious. Another shortcoming is the inability to create innovative topologies, which may lead to sub-optimal designs due to reliance on conventional topologies. In this paper, we present AaLLM, an open-source end-to-end multi-agent LLM workflow that takes user specs as input and outputs the appropriate netlist, encompassing both topology generation and circuit sizing. AaLLM automates the creation of a relevant knowledge base from research papers and textbooks to combat tedious manual data collection. A RAG model is implemented to emulate circuit design expertise using this knowledge base. Moreover, AaLLM uses a novel tri-agent feedback system comprising a Designer that determines circuit component values, a Critic that scrutinizes these values, and an Evaluator that minimizes circuit sizing iterations by arbitrating between the other two agents. AaLLM-generated novel topologies achieve a figure of merit (FoM) comparable to that of known topologies, and up to 3x higher for certain circuits. Testing on several circuit topologies, our results show a 3x - 4.5x decrease in the number of SPICE calls at inference when compared to SOTA multi-agent LLM pipelines. The results also show a 40x decrease in wall-clock time compared to existing approaches.

</details>


### 37. Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development

- **Authors:** Yiwei Li, Wanli Yang, Hexiang Tan, Xiangzhou Huang, Zhengyu Chen, Ziran Li, Borun Chen, Shanglin Lei, Huaisheng Zhu, Hao Tian, Fei Sun, Xunliang Cai, Jingang Wang
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13417v1](http://arxiv.org/abs/2608.13417v1)
- **PDF:** [https://arxiv.org/pdf/2608.13417v1](https://arxiv.org/pdf/2608.13417v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents are increasingly capable of improving models, systems, and other technical artifacts through long-horizon experimentation. To understand the current state of this capability, however, evaluation must go beyond final scores, which neither reveal where progress is gained or lost nor indicate whether accumulated experience improves later decisions. We therefore present a systematic evaluation of seven frontier models on 36 long-horizon tasks based on a new framework that uses rule-based metrics to characterize within-run behavior through Solution Framing, Execution, and Feedback Control and controlled comparisons to assess experience reuse within and across tasks. The results show that current agents operate more like engineering optimizers than fully autonomous researchers: they can formulate and implement practical solutions, but their performance varies substantially across runs, their strongest solutions mainly adapt or combine established techniques, and genuine methodological novelty remains rare. Detailed analysis reveals that observed performance is shaped by multiple factors, including distinct process bottlenecks behind similar final outcomes, experience reuse that can help or mislead subsequent decisions, and harness designs that affect performance stability. These findings suggest concrete directions for improving model training, inference-time strategies, experience management, and harness design.

</details>


### 38. Training AI Scientists to Replicate Research

- **Authors:** Damon Falck, Samer Sabri, Anja Surina, Thom Foster, Anya Sims, Sam Devlin, Dylan Rogers, Tantum Collins, Kaloyan Aleksiev, Louis Kirsch, Edward Hughes
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13331v1](http://arxiv.org/abs/2608.13331v1)
- **PDF:** [https://arxiv.org/pdf/2608.13331v1](https://arxiv.org/pdf/2608.13331v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The replicability of papers is a cornerstone of scientific knowledge, ensuring the reliability of existing results and providing a base for further experiments. The act of replication typically illuminates details that were previously underspecified, and thus requires similar hypothesis-driven exploration to open-ended research. In this work, we develop Replica, a scalable task space for paper replication. To provide reward signal, we introduce an auto-generated rubric-based judge that has low noise and agrees with human assessment of replication quality. We post-train Faraday, a 27B-parameter "AI Scientist" agent that leverages coding agents as tools, surpassing the performance of Claude Opus 4.8 and GPT-5.5 on held-out replication tasks. Qualitative analysis of individual rollouts reveals that Faraday adopts a more scientifically-principled approach. We believe that our results provide a stepping stone towards AI agents capable of long-horizon scientific innovation without requiring complex harnesses.

</details>


### 39. StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems

- **Authors:** Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13317v1](http://arxiv.org/abs/2608.13317v1)
- **PDF:** [https://arxiv.org/pdf/2608.13317v1](https://arxiv.org/pdf/2608.13317v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck. Converting the sender's continuous hidden states into discrete tokens discards information that token identities alone cannot capture. Recent work proposes latent communication as an alternative, where agents transmit hidden representations directly without converting them to text. However, existing latent methods either inject working memory layer by layer across the transformers, or require trained projectors that limit portability. We propose StateBridge, a training-free latent communication approach that aligns the sender's final-layer hidden states to the receiver's input space via a closed-form orthogonal transformation. Lightweight norm calibration and vocabulary anchoring ensure compatibility with the pretrained input distribution. The aligned states are prepended to the input of the receiver agent as a continuous prefix. We evaluate StateBridge on math reasoning, code generation, and question answering with four models from two families. StateBridge achieves the best or tied-best score on 22 out of 26 model-task pairs, consistently outperforming the strongest baseline.

</details>


### 40. Teach the Magnitude, Not the Direction: Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents

- **Authors:** Zechuan Wang, Siyuan Lu, Hongxuan Zhang, Linjian Mo, Chenyi Zhuang, Leilei Gan
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13179v1](http://arxiv.org/abs/2608.13179v1)
- **PDF:** [https://arxiv.org/pdf/2608.13179v1](https://arxiv.org/pdf/2608.13179v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning with verifiable rewards (RLVR) offers a verifier-bounded performance ceiling for training multi-turn tool-use agents, yet its trajectory-level credit assignment conflates heterogeneous per-turn outcomes into a single reward signal. On-policy distillation provides dense per-token supervision but is either teacher-bounded or prone to gradient concentration collapse. We introduce $\textbf{CrEST}$, a hierarchical credit assignment framework that retains RL's verifier-bounded ceiling while incorporating dense token-level signals from a privileged self-teacher. $\textbf{CrEST}$ resolves credit at two levels: turn-segmented verified advantages address inter-turn dilution, while entropy-gated self-teacher modulation refines intra-turn token contributions. Experiments on BFCL V3 and WildToolBench show that $\textbf{CrEST}$ consistently outperforms both RL and distillation baselines across two model scales, with the largest gains on long-trajectory and strict session-level metrics. Our work demonstrates that the teacher's role in policy optimization can be reduced from determining update directions to modulating update magnitudes, unlocking dense credit assignment without sacrificing the verifier-bounded ceiling.

</details>


### 41. SkillShapley: Boundary-Adaptive Shapley Valuation for Skill Step Attribution in LLM Agents

- **Authors:** Chang Liu, Yuqi Zhang, Yiman Zhong, Boyi Liu, Hengjun Wang, Shuyue Wei
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13173v1](http://arxiv.org/abs/2608.13173v1)
- **PDF:** [https://arxiv.org/pdf/2608.13173v1](https://arxiv.org/pdf/2608.13173v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent skills are crucial external instructions that enable language agents to execute long procedural tasks such as coding or document processing. Existing agent skills are primarily created through human manual crafting or agent execution traces, with limited understanding of how each step contributes to overall skill performance on specific tasks; i.e., there remains an open problem in quantifying the contribution of individual steps within an agent skill. To address this issue, we first model skill-step attribution as a Shapley value-based contribution estimation problem, and then propose SkillShapley, a step-level attribution framework for agent skills. Notably, SkillShapley operates in two phases, motivated by key empirical insights, i.e., discretized benchmark rewards that create sharp performance cliffs, and step interactions that are largely additive rather than synergistic. Specifically, it first identifies informative coalitional regions, and then adaptively samples new coalitions that can yield reusable marginal evidence. Experiments on skills from the widely adopted SkillsBench demonstrate that our SkillShapley can effectively and efficiently identify high- or low-value skill steps, providing several key takeaways for agent skill creation.

</details>


### 42. VALG: An Agentic System for ML Theory Research

- **Authors:** Dechen Zhang, Xuan Tang, Xinxiang Yin, Xingwu Chen, Jian Qian, Difan Zou
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13060v1](http://arxiv.org/abs/2608.13060v1)
- **PDF:** [https://arxiv.org/pdf/2608.13060v1](https://arxiv.org/pdf/2608.13060v1)
- **Categories:** cs.AI, cs.LG, math.OC, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

Machine learning theory studies learning procedures through mathematical setups in which the data model, training protocol, oracle access, loss, metric, and randomness define the phenomenon that a theorem is meant to explain. Solving an open problem therefore requires the problem formulation, theorem target, and proof mechanism to be developed in concert. Researchers formulate hypotheses, test them through preliminary theoretical or empirical analysis, and refine both assumptions and proofs. We investigate whether this process can be organized as an autonomous agentic workflow for ML theory research.
  We develop VALG, an agentic system that combines multi-level Verification, Adaptive formulation of Learning-theory problems, and Graph-structured proof development. Within each source-relative theorem branch, VALG maintains a fixed mathematical specification, checks the theorem-level composition of a typed proof-dependency graph, and constructs and reviews local proofs in dependency order. When a proof attempt fails, VALG identifies whether the obstruction lies in a derivation, the proof structure, or the theorem formulation and routes the next attempt accordingly. Formulation-level obstructions initiate an explicitly related variant or relaxation, preserving the mathematical relation between the resulting theorem and the source problem.
  We evaluate VALG on nine subproblems from five COLT 2026 open problems. Two runs produce internally finalized theorem candidates that match the scope of their source briefs; the remaining seven yield restricted-method results, special cases, or conditional theorems. These case studies show how VALG keeps source-scope matches, relaxations, conditional results, and blocked attempts mathematically distinct. VALG is open source at https://github.com/DechenZhang/VALG-ML-Theory-Agent.

</details>


### 43. BoardroomAI: Dependency-Aware Human-Steerable Multi-Agent Deliberation through Evolving Decision Graphs

- **Authors:** Sanjeev Manivannan
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13046v1](http://arxiv.org/abs/2608.13046v1)
- **PDF:** [https://arxiv.org/pdf/2608.13046v1](https://arxiv.org/pdf/2608.13046v1)
- **Categories:** cs.AI, cs.CE, cs.ET


> Summary unavailable.


<details>
<summary>Abstract</summary>

Organizational decisions are co-created while evidence, constraints, and human priorities continue to evolve. In conventional transcript-based multi-agent systems, humans typically provide an initial problem, agents deliberate internally, and the system returns a final response. BoardroomAI instead treats the human as a persistent participant who can intervene by challenging assumptions, modifying constraints, changing priorities, introducing evidence, or redirecting the decision process. We operationalize this human--agent coexistence through four components: (i) a typed decision graph representing evidence, assumptions, constraints, claims, objections, alternatives, risks, decisions, semantic dependencies, and specialist responsibility; (ii) an intervention compiler that converts confirmed human actions into explicit graph updates; (iii) dependency-aware propagation that identifies affected subgraphs, preserves unaffected artifacts, and selectively reactivates relevant specialists; and (iv) an evaluation framework measuring intervention impact, repair coverage, preservation, recomputation, and decision validity. Across 600 generated decision-DAG interventions, propagation matched exhaustive impact computation while inspecting only 14.59% of nodes. In a 12-case exploratory pilot, selective repair recomputed 62.11% of canonical nodes, preserved all gold-unaffected nodes, and produced valid updated decisions in six cases while abstaining in the remaining six. These abstentions show that correct intervention routing may still provide insufficient context for synthesis, motivating a \emph{decision-sufficient context closure} for human-steered multi-agent deliberation. All results are synthetic and prototype-level.

</details>


### 44. Static analysis-guided agentic AI translation enables Rust as a full stack bioinformatics language

- **Authors:** Johan Henriksson
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13029v1](http://arxiv.org/abs/2608.13029v1)
- **PDF:** [https://arxiv.org/pdf/2608.13029v1](https://arxiv.org/pdf/2608.13029v1)
- **Categories:** q-bio.GN, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

The field of bioinformatics struggles with legacy code - old code that is commonly used but may no longer have a maintainer, or may be written in an now-unfamiliar language (e.g. Perl, Fortran). This incurs maintenance cost (technical debt), but dynamically typed languages also negatively impacts the environment and fail to make use of modern hardware. Legacy code may also have security or safety problems that make it unsuited for use in clinical settings. Here we show that agentic AI, combined with static analysis, can be used to translate legacy code to the modern language Rust. We provide prompts and supporting software to aid systematic translation, and evaluate it on common software for NGS and imaging. We showcase the result on our software Bascet: Size was reduced by ~80x, build time decreased by ~10x, and performance of key steps improved >3x. Unix dependencies were also removed, making Bascet the only single-cell pipeline able to run on native Windows, without a container. Large-scale refactoring of bioinformatics software is thus now possible at a limited budget, enabling more complex tools to be developed.

</details>


### 45. OGR-MARL: Option-Guided Residual Multi-Agent Reinforcement Learning for Heterogeneous USV Cooperative Pursuit in Constrained Port Waterways

- **Authors:** Mao Jiayang, Wang Lanfeng, Peng Zhao-Han
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12995v1](http://arxiv.org/abs/2608.12995v1)
- **PDF:** [https://arxiv.org/pdf/2608.12995v1](https://arxiv.org/pdf/2608.12995v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Heterogeneous USV cooperative pursuit in constrained port waterways requires evader interception under navigation, traffic, and role constraints. This paper proposes OGR-MARL, an option-guided residual multi-agent reinforcement learning framework that is decoupled from a specific MARL algorithm. OGR-MARL integrates shared evader belief, role-conditioned option targets, adaptive rule penalties, and residual policy learning, allowing different MARL algorithms to learn corrective actions on top of rule-guided behaviors rather than exploring constrained port environments from scratch. We instantiate OGR-MARL with representative continuous-control MARL backbones, including MADDPG, MATD3, MAPPO, and MASAC, yielding OGR-MADDPG, OGR-MATD3, OGR-MAPPO, and OGR-MASAC. Experiments in an abstract Xiazhimen port-waterway scenario show that the OGR-MASAC instantiation achieves a 75.0% capture rate, promising mission-effective rule compliance, and the best heterogeneous coordination among the tested methods. Without retraining, zero-shot transfer to a QGIS/AIS-informed Xiazhimen map achieves promising results, demonstrating the generalization potential of OGR-MARL in more complex port scenarios.

</details>


### 46. LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation

- **Authors:** Dongfang Li, Zixuan Liu, Junmai Wang, Jiahe Huang, Fuhao Li, Bonian Jia, Baotian Hu, Min Zhang
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12990v1](http://arxiv.org/abs/2608.12990v1)
- **PDF:** [https://arxiv.org/pdf/2608.12990v1](https://arxiv.org/pdf/2608.12990v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents must preserve information from past interactions to support future tasks. Existing memory systems typically rely on eager consolidation, invoking LLMs after each interaction to extract, summarize, or update memories. This design makes memory construction increasingly costly as conversations grow. Coarse summarization can reduce construction cost but risks discarding fine-grained contextual evidence, whereas larger retrieval contexts or multi-hop LLM reasoning shift the overhead to query time. We present LycheeMemory V2, an efficient long-term memory framework that replaces turn-level consolidation with semantic segment-level consolidation. Instead of consolidating every interaction, LycheeMemory batches multiple exchanges into segments and encodes each finalized segment into context-independent typed memory records. Segment-level batching lowers LLM encoding frequency, while semantic boundary detection helps preserve coherent event-level and temporal evidence compared with fixed-window batching. The resulting records are organized with lightweight structured indexes for query-planned evidence retrieval. Experiments using GPT-4.1-Mini show that LycheeMemory achieves state-of-the-art performance, reaching 89.22% on LoCoMo and 92.20% on LongMemEval-S. Compared with A-Mem, it reduces construction tokens by 86.0% on LoCoMo and 75.9% on LongMemEval-S without increasing query-time token usage. More broadly, our results suggest that the accuracy--cost trade-off of long-term agent memory depends not only on what information is retained, but also on the granularity at which it is consolidated.

</details>


### 47. Reconcile Once, Write Anytime: A Trust-Tiered Librarian and a Multi-Agent Writer for Drift-Free, Point-in-Time Research

- **Authors:** Xing Zhang, Yanwei Cui, Guanghui Wang, Peiyang He
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12984v1](http://arxiv.org/abs/2608.12984v1)
- **PDF:** [https://arxiv.org/pdf/2608.12984v1](https://arxiv.org/pdf/2608.12984v1)
- **Categories:** cs.MA, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-form research reports generated by large language models drift, contradict themselves, and lose provenance: the same metric appears with different values, and rumor is quoted as confidently as an audited filing. We present a two-tier agentic system that separates a maintained, point-in-time knowledge library from report writing. A deterministic "librarian" ingests timestamped sources into a trust-tiered ontology, layering evidence cards, an authoritative metric ledger, and a claim graph into an always-current source of truth, not per-query RAG over raw chunks. A portable multi-agent "writer" runtime then composes a contradiction-free, evidence-grounded report at any knowledge cutoff T, reading only evidence with as_of <= T (no look-ahead); red-team verdicts flow back into the librarian. We evaluate on a self-collected, public corpus of 6,130 sources yielding 555,926 evidence cards (SEC EDGAR filings across 295 issuers and 11 sectors, U.S. Bureau of Labor Statistics releases, and Wikipedia). From the one library we compose four point-in-time reports on distinct theses and run eight reproducible experiments, whose headline metrics come from a deterministic quality-control gate, itself validated by defect-injection meta-evaluation at recall 1.0 and precision 1.0. A shared metric ledger removes 6,845 cross-section contradictions to zero. Tier-first selection is correct on 22/22 gold cases where a popularity-first baseline scores only 9/22; trust tiering leaks zero media-sourced numbers, and no government statistic displaces a company's own filing. A red-team refutation propagates back and self-corrects a later run with zero manual edits. Replay exhibits zero look-ahead violations across seven cutoffs while the library grows from 235,373 to 555,312 cards. Difficulty-tiered model routing exceeds the all-Opus quality ceiling while running 3.7x faster than serial.

</details>


### 48. Beyond Handcrafted Security: Towards Self-Evolving Defense for LLM Agents

- **Authors:** Jiajun Ruan, Peiyang Li, Yukun Chen, Fengting Li, Chao Feng
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12977v1](http://arxiv.org/abs/2608.12977v1)
- **PDF:** [https://arxiv.org/pdf/2608.12977v1](https://arxiv.org/pdf/2608.12977v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The expanding operational capabilities of large language model (LLM) agents introduce sophisticated security threats. Runtime defenses have emerged as an effective approach to mitigating these risks by integrating security mechanisms into the agent execution loop. However, existing runtime defenses rely heavily on manually designed interventions and lack a principled framework for their construction and maintenance. In this work, we first develop a harness-level formulation of runtime defense that systematically characterizes how harness mechanisms enable defense construction and provides a unified view of existing runtime defense interventions from a harness perspective. Building on this formulation, we propose HARD (Harness-based Autonomous Runtime Defense Evolution), a self-evolving runtime defense framework that automatically identifies appropriate intervention strategies and iteratively improves defense artifacts based on observed failure traces. HARD transforms runtime defense development from manual engineering into an autonomous evolution process, and extensive experiments demonstrate that it improves security performance over existing handcrafted defenses while preserving benign task utility. Our findings highlight autonomous defense evolution as a promising new paradigm for securing deployed LLM agents, enabling agents to identify defense weaknesses and continuously improve their protection mechanisms.

</details>


### 49. Discovering Efficient and Explainable Communication Topologies for LLM-based Multi-Agent Systems via Causal Inference

- **Authors:** Junzhi Li, Peng He, Qirui Ji, Wei Wang, Lixiang Liu, Chuxiong Sun
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12921v2](http://arxiv.org/abs/2608.12921v2)
- **PDF:** [https://arxiv.org/pdf/2608.12921v2](https://arxiv.org/pdf/2608.12921v2)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The performance of large language model (LLM)-based multi-agent systems (MAS) largely depends on effective communication topologies. Existing topology generation methods, however, typically learn communication topologies through black-box optimization driven solely by task-level rewards. While effective, such optimization provides little insight into why particular communication edges are selected, making it difficult to identify the critical communication subgraphs responsible for successful collaboration. To address this limitation, we propose E2-Explainer, a model-agnostic framework for providing interpretable explanations of communication topologies produced by arbitrary topology generators. Specifically, we formulate topology explanation as a causal attribution problem that identifies compact communication subgraphs supported by edge-level evidence of task preservation. We obtain this evidence with a Granger-style objective that measures how masking each communication channel changes the task outcome and the stability of the final response. The resulting budgeted subgraphs are then distilled into an amortized explainer, enabling efficient post-hoc explanation without repeated edge-level evaluations at deployment. Extensive experiments on multiple reasoning and coding benchmarks demonstrate that E2-Explainer identifies critical communication subgraphs that preserve successful collaboration. These subgraphs can also be executed directly to prune redundant communication edges, substantially reducing communication costs while maintaining competitive task performance.

</details>


### 50. Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence

- **Authors:** Varun Pratap Bhardwaj, Garima Singh, Arun Pratap Bhardwaj
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12895v1](http://arxiv.org/abs/2608.12895v1)
- **PDF:** [https://arxiv.org/pdf/2608.12895v1](https://arxiv.org/pdf/2608.12895v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Compositional reliability bounds for multi-agent systems multiply component reliabilities, a step licensed by a conditional-independence assumption that is routinely stated and rarely tested. We test it. Two instances of one model, in a two-agent handoff, co-fail on 90.0% of the missions on which either fails (log OR 6.66, 95% CI [6.38, 7.00]; phi 0.916), in a preregistered evaluation of 18,000 missions scored by deterministic code with no LLM judge. Substituting a different model reduces the association in six of six contrasts; substituting a different vendor, model already different, does not -- a registered hypothesis reported as a null.
  The error is signed and runs against the operator: positive dependence inflates joint failure above the independence product, so redundancy is over-credited exactly when components share a model. The assumption-free alternative is often vacuous, and fitting a dependence model is worse: we prove a bootstrap bound on a fitted model's functional loses coverage of the truth as n grows, the identification gap being O(1) while the bootstrap haircut is O(n^{-1/2}). More data makes such a certificate worse, with no visible symptom.
  We give a finite-sample certificate assuming no dependence structure: a linear program over the joint, over a Bonferroni-Clopper-Pearson box around measured co-execution moments. It is sound, sharp for the information supplied, and monotone in the moment family. Enriching ten moment functionals to fourteen narrows the identified interval by 85.7% and lifts the certified floor from 0.2455 to 0.4116. A companion anytime-valid certificate holds type-I error at 0.0471 under optional stopping.
  Common dependence statistics are marginal-bounded and can reverse an apparent ordering of conditions when the compared agents fail at different rates. Contracts, scoring code, analysis scripts, and the preregistration are released.

</details>


### 51. ReflectFact: Self-Reflective Agents for Improving Comprehension and Reasoning in Multi-Hop Fact Verification

- **Authors:** Runze Zhao, Zixin Tang, Xiaoshuai Hao, Leyuan Chang, Xiaopeng Fu, Boyu Qiao, Dongyang Zhang
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12877v1](http://arxiv.org/abs/2608.12877v1)
- **PDF:** [https://arxiv.org/pdf/2608.12877v1](https://arxiv.org/pdf/2608.12877v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-hop fact verification, which verifies claims by reasoning over multiple pieces of evidence, is critical for combating misinformation on social media yet remains highly challenging. Recent methods primarily rely on multi-agent collaboration to decompose fact verification into specialized subtasks. However, these methods face two critical limitations: (1) agents may perform individual subtasks without sufficient awareness of the global verification objective, causing their reasoning to deviate from the intended direction; and (2) conflicts between parametric knowledge and the provided evidence may undermine evidence-grounded reasoning and lead to incorrect verdicts. To address these challenges, we propose ReflectFact, a novel self-reflective agent framework for multi-hop fact verification. ReflectFact introduces three key tasks. Explicit Reasoning Path Planning builds an evidence-grounded reasoning path by resolving implicit entities, decomposing the claim into sub-questions, and integrating the verified facts into a verdict. Evidence-Drift Verification makes the agent re-answer by quoting the supporting evidence when a grounded answer merely echoes its parametric prior, thereby calibrating evidence deviation to ensure grounded comprehension. Reasoning Reflection Verification re-examines each reasoning step and regenerates it once an inconsistency is detected, correcting reasoning flaws such as location bias and replacement bias through a global task perspective. Subsequently, the agent aggregates validated reasoning chains to yield reliable verdicts. Extensive experiments on HOVER and EX-FEVER demonstrate that ReflectFact effectively remedies the comprehension and reasoning defects of existing methods, achieving state-of-the-art performance and respectively outperforming the strongest baseline by 3.32\% and 2.78\% on the two datasets.

</details>


### 52. Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents

- **Authors:** Xutao Mao, Liangjie Zhao, Xiang Zheng, Cong Wang
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12851v1](http://arxiv.org/abs/2608.12851v1)
- **PDF:** [https://arxiv.org/pdf/2608.12851v1](https://arxiv.org/pdf/2608.12851v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-improving LLM agents convert successful trajectories into persistent cross-task state. An unsafe success can thereby become reusable policy after its triggering input disappears. Skill evolution makes this failure measurable by distilling operational trajectories into executable, transferable, and inspectable procedures. Because evolution optimizes task outcomes rather than procedure safety, compromised experience can cause skill misevolution. Existing benchmarks measure current behavior or static artifacts but cannot attribute risk across authoring, retrieval, and later execution. To expose this lifecycle, we introduce SkillMisevo-Gym, a lifecycle-aware harness that versions skill state across agent frameworks, and SkillMisevo-Bench, a frozen design from malicious exposure to carryover tasks, with concept-aligned benign tasks and nine lifecycle metrics. We also introduce SafeEvolve, a wrapper that repairs unsafe content and governs subsequent reuse. Across 25 agent-method configurations, each covering 525 tasks in 25 episodes, all 21 evolved configurations author unsafe artifacts, while only fifteen lead to fresh-session harm. In the exposure sweep, three malicious tasks raise carryover ASR from 16.0% to 35.3%. Across representative skill evolution methods, SafeEvolve reduces unsafe retrieval and fresh-session harm by 26.7 and 17.3 percentage points, respectively, while mean benign utility changes by only 0.4 points. Together, persistent-adaptation safety must govern what updates write and what future executors reuse. Code is available at https://github.com/henrymao2004/misevolve.

</details>


### 53. AQuA: Recursively Self-Improving Quantitative Trading Research Agents

- **Authors:** Jiacheng Guo, Suozhi Huang, Yunlong Gao, Zihao Li, Jian Ge, Xu Kuang, Mengdi Wang
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12841v1](http://arxiv.org/abs/2608.12841v1)
- **PDF:** [https://arxiv.org/pdf/2608.12841v1](https://arxiv.org/pdf/2608.12841v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study recursive self-improvement at the level of quantitative-investment research: whether an autonomous system can use evidence from earlier experiments to improve the hypotheses and candidates proposed in later iterations. We present AQuA, which comprises two separate language-model-driven research systems: one for symbolic factor discovery and one for trainable model development. The two systems do not share agents, memories, candidate spaces, or research state. Instead, each independently closes its own research loop by retaining validated evidence and using it to guide subsequent proposals. In this bounded sense, both systems implement recursive self-improvement at the level of the research process. Each system also uses its own sealed sandbox, which fixes the data splits, feature and label definitions, and evaluator while allowing the model to act only through constrained factor expressions or configuration diffs. The factor system, a manager-mediated multi-agent pipeline, discovers and combines factors into a signal that reaches a combined information coefficient of about $0.190$ on a crypto universe. The model system, a config-driven loop over a hybrid time-series architecture, reaches a per-stock information coefficient of $+0.0843$ on US equities and converts it into a threshold long/short strategy with a held-out Sharpe of up to $+2.50$ at a two-leg cost. The strategy is positive in every year from 2021 to 2025.

</details>


### 54. ARC: Fair Relative Advantage Comparison in Open-Ended Real-World Interaction

- **Authors:** Yongqi Tong, Tan Li Hui Faith, Choy Zhen Wen Marcus, Zhou Jin, Kewei Fu, Jiang-Ming Yang, Jianshe Li, Xin Zhang
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13622v1](http://arxiv.org/abs/2608.13622v1)
- **PDF:** [https://arxiv.org/pdf/2608.13622v1](https://arxiv.org/pdf/2608.13622v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Open-ended real-world interaction admits multiple valid behaviors: an agent may answer directly, ask for clarification, provide progress updates, or confirm before acting. This flexibility breaks a core assumption behind group-based RL: rollouts compared within a group are no longer guaranteed to be behaviorally comparable. As a result, reward-model preferences over interaction style can distort relative advantages and steer optimization toward reward-preferred behaviors rather than context-appropriate ones. We formalize this as a \textit{reward fairness problem} and propose \textbf{ARC} (Advantage Regularization via Conditioning), a training recipe that restores fairer relative comparison through strategy-conditioned rollout grouping, together with hybrid rewards and entropy regularization. We study ARC in our proposed \inter, a novel paradigm for responsive, steerable, and execution-aware user-agent interaction that decouples user-visible communication from latent reasoning and tool use. \inter\ also provides the annotation and distillation pipeline for constructing \inter-86K, our strategy-annotated training corpus for supervised and RL training. Empirically, ARC substantially strengthens the core $τ/τ^2$ tool-use benchmarks, while \inter\ reduces time-to-first-token from 4.91s to 1.27s relative to a think-style baseline. Together, these results suggest that a central bottleneck in open-ended interactive learning is not only how agents are rewarded, but whether their behaviors are compared fairly in the first place. The ARC implementation and \inter-86K training data will be released.

</details>


### 55. Lines and Ladders: A Context-Aware Multi-Agent Framework for Large-Scale Retail Price Taxonomy

- **Authors:** Ravi Teja Chunduri, Srikaran Reddy Boya, Deep Narayan Mishra, Ajay Kumar B, Karthik Kumaran, Pranay Kona
- **Published:** 2026-08-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12674v1](http://arxiv.org/abs/2608.12674v1)
- **PDF:** [https://arxiv.org/pdf/2608.12674v1](https://arxiv.org/pdf/2608.12674v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Maintaining price consistency and executing an Every Day Low Price strategy is critical for global retailers. However, with catalogs spanning millions of active items, manual governance of price relationships is infeasible. Inconsistent pricing across item variants distorts customer value perception and cannibalizes sales. To address this, we present a scalable, context-aware Multi-Agent Framework designed to automate the construction of "Lines and Ladders" pricing taxonomies. Our framework employs specialized LLM agents to construct these coherent pricing structures by identifying key attributes, extracting multi-modal values, and applying hierarchical grouping logic. Evaluated on real-world enterprise data and deployed in production, our 3-Agent system achieves an F1-score of 0.83 for Lines, outperforming single-agent baselines by mitigating cognitive overload. The system achieves >90% precision and >75% recall in Food & Consumables, and 80.2% assignment accuracy in the unstructured General Merchandise catalog.

</details>


### 56. SteerBench-Work: A Benchmark for Agent Steering at Action Boundaries

- **Authors:** Oguz Serdar, Cuneyt Mertayak
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12654v1](http://arxiv.org/abs/2608.12654v1)
- **PDF:** [https://arxiv.org/pdf/2608.12654v1](https://arxiv.org/pdf/2608.12654v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-running LLM agents act through tools, and a single step can send an email, merge a pull request, or wire a payment. The steering decision is the pre-commit choice at that boundary: proceed, or hold for human or policy review. We introduce SteerBench-Work, an incident-anchored, bidirectional benchmark for that decision in workplace agents across developer operations, customer service, finance, legal, medical, HR, and security.
  Release v2026-05 contains 106 scenarios anchored in public incidents, paired evidence-reversed mirrors, and calibration controls, with labels split nearly evenly between proceed and hold so the two error directions get near-identical numbers of chances. A model sees the proposed action and the available evidence, returns a gate decision, and is scored on whether it crosses or holds the boundary correctly. Across 30 model conditions the failures run almost entirely in one direction: models wrongly hold authorized, evidence-cleared work on 28.1% of opportunities and wrongly allow unsafe work on 1.0%. The hardest cases are risk-resolved commits, where signed or structured evidence has already cleared a real risk trigger, and models score markedly worse on evidence-reversed mirrors of famous incidents (63.8%) than on the incidents themselves (98.5%). General capability is not the same as steering calibration: higher-capability models often over-refuse at the commit boundary, and more reasoning can repair a weak gate while leaving a calibrated one flat. The public leaderboard is at steerbench.com.

</details>


### 57. EgoCITE: Context-Augmented Indexing and Time-Aware Retrieval for Long-Horizon Egocentric Memory

- **Authors:** Le Zhang, Ke Sun
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12627v1](http://arxiv.org/abs/2608.12627v1)
- **PDF:** [https://arxiv.org/pdf/2608.12627v1](https://arxiv.org/pdf/2608.12627v1)
- **Categories:** cs.CV, cs.AI, cs.CL, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon egocentric memory transforms continuous first-person video and audio into a searchable record of past experiences. We demonstrate two bottlenecks in existing systems: indices built from context-poor captions are unreliable for agentic search, while retrieval ignores a question's temporal intent. To address both bottlenecks, we introduce EgoCITE (Egocentric Context-augmented Indexing and Time-aware Evidence retrieval), a long-horizon agentic memory framework for egocentric QA. EgoCITE comprises three components. EgoScheme uses local multimodal context to turn fragmentary video captions and speech transcripts into self-contained atomic memory indices. EgoIndex organizes complementary action, activity, utterance, and conversation representations into searchable multi-view memory indices at multiple granularities. EgoRetrv combines semantic search with question-conditioned temporal relevance scoring and curation of retrieved evidence. We evaluate EgoCITE on EgoLifeQA, EgoMem, and EgoR1-Bench in terms of answer accuracy and target-event retrieval alignment. EgoCITE improves accuracy over agentic memory baselines by at least 4.4--14.2\% while achieving 36$\times$ lower cost than long-context LLM agents.

</details>


### 58. LLMs Are Not Good Strategists, Yet Memory-Enhanced Agency Boosts Reasoning

- **Authors:** Yi Wu, Zhimin Hu
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12626v1](http://arxiv.org/abs/2608.12626v1)
- **PDF:** [https://arxiv.org/pdf/2608.12626v1](https://arxiv.org/pdf/2608.12626v1)
- **Categories:** cs.CL, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Strategic reasoning in Large Language Models (LLMs) within long-horizon environments is often limited by inconsistent subgoals. In these settings, finite attention resources prevent the model from maintaining strategic coherence over thousands of steps. This limitation leads to strategic drift, where localized decisions fail to sustain a coherent trajectory across reasoning. To address this, we introduce EpicStar, a framework that enables agents to learn memory as policy to tackle long-horizon reasoning. Specifically, the agent maintains a bank of successful past episodes as a heuristic alongside a working memory to track short-term environmental changes. During inference, a dynamic gating mechanism determines whether to execute a retrieved action directly or to perform new reasoning through a contextual fusion of the retrieved episodes and current working memory. Utilizing StarCraft II as the testbed, we evaluated EpicStar against diverse opponent styles. It significantly outperforms baseline methods, achieving higher win rates while consuming an order of magnitude fewer tokens, and it maintains this advantage consistently across difficulty levels and opponent strategies. Our findings provide compelling evidence that structured cross-episode memory is essential for enabling LLM agents to perform robust, long-term strategic execution in dynamic, autonomous settings.

</details>


### 59. DiG-bench: Discovery in Games

- **Authors:** Ruairidh M. Battleday, Kai Sandbrink, Jimi Cullen-Drohan, Zihan Yan, Timothy Muller, Clare Maguire, Ales Kubicek, Fraser Greenlee-Scott, Sukrit Sumant, Tri Dao, Jürgen Schmidhuber, Michal Valko, Joshua Tenenbaum, Thomas L. Griffiths, Zeb Kurth-Nelson, James C. R. Whittington
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12593v1](http://arxiv.org/abs/2608.12593v1)
- **PDF:** [https://arxiv.org/pdf/2608.12593v1](https://arxiv.org/pdf/2608.12593v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Discovery---formulating novel generalizations---is a central part of the scientific process. Despite its importance, there is a gap in the current AI benchmark landscape, with few benchmarks directly probing the capacity for discovering new knowledge with experimentation in controlled environments where the objective is unknown. To address this gap, we release a new benchmark: DiG-bench (Discovery in Games). DiG-bench consists of a set of 70 independent games. Each game is encoded as a short string and has unique transformation rules that must be discovered through interaction and experimentation. The levels of the game present a series of challenges to test whether the rules have been discovered, where the win conditions for each level are also unknown. We provide games at seven tiers of difficulty for AI agents. The lowest tier is routinely solvable by multiple models, while the highest tier challenges the best models in agentic harnesses. All 70 games were solved by at least one human on first attempt. A subset of 21 games is released publicly, and the remainder is held private for secure evaluation.

</details>


### 60. Auditable agentic AI for evidence-grounded thyroid ultrasound diagnosis and reporting

- **Authors:** Haifan Gong, Shiyu Chen, Bodong Wang, Yuqi Wang, Shijie Wang, Guoliang You, Xinyu Xiong, Haowei Wang, Mingzhi Mao, Dexing Kong, Qinghua Liu, Wei Lou, Fei Chen, Guanbin Li
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12590v1](http://arxiv.org/abs/2608.12590v1)
- **PDF:** [https://arxiv.org/pdf/2608.12590v1](https://arxiv.org/pdf/2608.12590v1)
- **Categories:** cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Thyroid ultrasound diagnosis requires coordinated lesion localization, measurement, risk stratification and reporting, yet most AI systems address these tasks in isolation and provide limited support for clinical review. We present ThyroidXAgent, a clinician-interactive agentic AI system that coordinates specialized diagnostic tools and stores their outputs as an auditable case-level evidence record. The system was developed using OpenThyroidDB, a multicentre, multitask resource integrating approximately 0.3 million ultrasound images and 24,000 paired reports, and was evaluated on 28,458 non-overlapping test cases, including 8,721 cases from 35 centres in the private NHC-MISD-TUS cohort. Across heterogeneous datasets, ThyroidXAgent achieved a mean Dice score of 87.21 percent for nodule segmentation and a mean AUROC of 0.9466 for benign-malignant classification. The same workflow supported lymph-node metastasis prediction and follicular versus papillary thyroid carcinoma classification, with AUROCs of 0.864 and 0.805, respectively. For report generation, evidence-grounded assembly outperformed multimodal language-model baselines across three cohorts. ThyClinScore, a lesion-level clinical semantic metric introduced here, showed the strongest correlation with a location-aware language-model judge. ThyroidXAgent improved physician classification accuracy, increased report diagnostic consistency from 70.3 percent to 86.2 percent, and reduced segmentation and reporting time by 35.9 percent and 27.4 percent, respectively. These findings support auditable, clinician-correctable agentic AI for thyroid ultrasound diagnosis and reporting.

</details>


### 61. Do LLMs Beat Nash? Testing Decentralized Coordination in Self-Play Multi-Agent Games

- **Authors:** Deborah Sinishaw, Qile Zhu, Edwin Meriaux, Gregory Dudek
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12547v1](http://arxiv.org/abs/2608.12547v1)
- **PDF:** [https://arxiv.org/pdf/2608.12547v1](https://arxiv.org/pdf/2608.12547v1)
- **Categories:** cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents deployed without a central controller are often assumed to require communication to coordinate their actions. We ask what remains possible without it: when independent instances of the same model cannot communicate, can they still reason about their counterparts well enough to exceed the standard game-theoretic baseline for uncoordinated play? We introduce a benchmark of one-shot, no-communication games in which each of thirteen language models is told only that its counterparts are running the same model and is evaluated against the Nash equilibrium of the underlying game. In two-player matrix games spanning seven archetypes and two to ten actions per player, two frontier-hosted models consistently exceed their Nash benchmark, approaching the optimal joint outcome in several archetypes, while most open-weight models achieve only partial gains that vary sharply by game structure. Performance degrades substantially in team-based games with four or more interchangeable agents, particularly as the action space grows, suggesting that whatever capability drives self-play gains in dyadic games does not transfer to larger multi-agent teams.

</details>


### 62. Entropy-Augmented Multi-Objective Policy Optimization in Multiagent Systems

- **Authors:** Jamie Santos, Ayhan Alp Aydeniz, Raghav Thakar, Kagan Tumer
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12534v1](http://arxiv.org/abs/2608.12534v1)
- **PDF:** [https://arxiv.org/pdf/2608.12534v1](https://arxiv.org/pdf/2608.12534v1)
- **Categories:** cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agent teams deployed in settings such as marine and extraterrestrial outposts must coordinate actions to achieve optimal outcomes across multiple competing objectives. Multi-objective evolutionary algorithms such as NSGA-II optimize for diversity in the objective space, but neglect diversity in the behavior space, possibly leading to premature convergence and a collapse in behaviors that may differentiate policies in different external conditions. To address this, we introduce an entropy-augmented policy evaluation strategy that incorporates an entropy bonus into agent fitness scores, discouraging behavioral homogeneity across the evolving population. By augmenting policy evaluation with a behavior-space diversity signal while preserving the underlying Pareto optimization framework, our method is designed to encourage exploration of behaviorally distinct policies in multiagent domains. We evaluate our approach across rover-domain experiments with qualitatively distinct reward structures and observe hypervolume improvements of up to 48% relative to the NSGA-II baseline, suggesting that behavioral diversity is a promising and underexplored direction for improving multi-objective multiagent evolutionary optimization.

</details>


### 63. VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies

- **Authors:** Ankita Rajaram Naik, Anupama Murthi, Benjamin Elder, Siyu Huo, Raavi Gupta, Abhinav Jain, Praveen Venkateswaran, Abdulhamid Adebayo, Danish Contractor
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12282v1](http://arxiv.org/abs/2608.12282v1)
- **PDF:** [https://arxiv.org/pdf/2608.12282v1](https://arxiv.org/pdf/2608.12282v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agents deployed in enterprise settings must reason across structured APIs and document collections, yet existing benchmarks evaluate these capabilities in isolation. We introduce VAKRA (e\textbf{V}aluating \textbf{A}PI and \textbf{K}nowledge \textbf{R}etrieval \textbf{A}gents), a benchmark of over $8{,}000$ executable APIs across $62$ domains with tasks spanning three settings of increasing difficulty: diverse API interaction styles, multi-hop reasoning over structured APIs, and multi-source reasoning with natural-language tool-use policy constraints. Correctness is verified by re-executing predicted tool calls against live APIs, accommodating multiple valid paths. Using a fixed ReAct harness to isolate model capabilities from agent architecture, we evaluate frontier and open-weight models and find that even the best model achieves only 70.4\% on single-hop endpoint-style tasks and drops to 50--51\% on compositional APIs; performance degrades by over 50\% as reasoning depth increases, and policy-constrained questions expose severe failures (as low as 2.4\% on unanswerable queries). Trace analysis shows failures concentrate at language-mediated reasoning - entity disambiguation, cross-source grounding, rather than tool invocation mechanics. Code is available https://github.com/IBM/VAKRA. Dataset is available https://huggingface.co/datasets/ibm-research/VAKRA

</details>


### 64. Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based LLM Agents

- **Authors:** Junliang Liu, Ruoyu Li, Wenxin Tang, Jingyu Xiao, Zhenyu Liu, Jingheng Xu, Laizhong Cui
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12273v1](http://arxiv.org/abs/2608.12273v1)
- **PDF:** [https://arxiv.org/pdf/2608.12273v1](https://arxiv.org/pdf/2608.12273v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on third-party skills, using natural-language descriptions for selection and instruction bodies for planning. This progressive-disclosure design exposes two sequential control points to untrusted publishers: a static skill may steer an otherwise correct task onto an unnecessarily costly trajectory. Prior work studies selection manipulation, malicious skill instructions, and tool-chain resource amplification largely separately, leaving their end-to-end composition unclear. We introduce Convergent Detour Hijacking (CDH), a text-only, runtime-independent attack that couples these stages. Under shared semantic cover, a description establishes relevance during selection, while an aligned body reuses that rationale to fabricate plausible dependencies during planning. CDH attracts an attacker-controlled coordinator alongside legitimate skills, recruits unnecessary benign skills into a bounded detour, and then re-enters the original route to preserve task completion. We evaluate it across multiple LLM backends and 491 held-out tasks under single-task and multi-turn conditions. On DeepSeek-V4-Pro, the matched coordinator is selected in 80.02% of tasks; among coordinator-hit runs that complete tasks, token consumption and end-to-end execution time increase by 66.91% and 92.45%, respectively, while aggregate task completion remains comparable. Thus, correct outcomes do not guarantee trajectory integrity or cost safety.

</details>


### 65. One Frozen Simulator Is Not Enough: Simulator Collapse in Multi-Agent RL

- **Authors:** Simon Yu, Nicholas Tomlin, Marwa Abdulhai, Ximing Lu, Derek Chong, Abe Hou, Dilara Soylu, Sergey Levine, Christopher D. Manning, Weiyan Shi
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12253v1](http://arxiv.org/abs/2608.12253v1)
- **PDF:** [https://arxiv.org/pdf/2608.12253v1](https://arxiv.org/pdf/2608.12253v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning for human-AI interaction typically relies on a single large language model to simulate user behavior. We show that this approach systematically fails to generalize, and trace the failure to simulator collapse: because the simulator LLM is mode-collapsed, an LLM policy trained against it overfits to narrow strategies that exploit the simulator's dominant mode, and such a policy transfers poorly to unseen simulators and real users. We formalize this collapse theoretically and propose two complementary solutions, one at inference time and one at training time. The inference-time solution, Verbalized Sampling, broadens the simulator's behavior by sampling from a verbalized response distribution, reducing mode collapse. The training-time solution, Co-Training, jointly optimizes the policy against a population of trainable simulators, preventing it from overfitting to any single simulator's mode. We validate both solutions on three multi-turn benchmarks: Persuasion for Good, $τ^2$-bench, and CooperBench. Verbalized Sampling improves held-out success by up to 9% over single-simulator RL, and Co-Training pushes gains further to 14%; the human study shows similar gain on real users. Both solutions preserve the policy diversity that collapses under single-simulator RL. To support further work in this direction, we release SCOPE, an open-source framework for Population Co-Training multi-agent RL. More broadly, our results suggest that the diversity of the training environment, not only the policy, is critical to the generalization of multi-turn RL to real-world deployment.

</details>


### 66. Rethinking Agent Security as a Networking Problem

- **Authors:** Van Tran, Taveesh Sharma, Tajveer Singh Dhesi, Nick Feamster
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12172v1](http://arxiv.org/abs/2608.12172v1)
- **PDF:** [https://arxiv.org/pdf/2608.12172v1](https://arxiv.org/pdf/2608.12172v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are rapidly becoming more capable and widely deployed, promising substantial gains in productivity and enabling new classes of applications. However, their growing autonomy also introduces significant privacy and security risks. Existing defenses are predominantly agent-centric, relying on the agent itself to detect threats and enforce privacy and security policies. This approach is fundamentally limited because it entrusts policy enforcement to AI agents whose LLM-driven behavior is inherently nondeterministic and vulnerable to manipulation through attacks such as prompt injection. As a result, current defenses cannot reliably prevent privacy and security threats, highlighting a critical need for a new solution to securing AI agent systems.
  The networking community has long grappled with similar challenges and offers insightful principles we can borrow to design a more secure AI agent system. These include centralized control with distributed enforcement, capability-based access for mediating requests to sensitive resources, and least privilege through zero-trust enforcement. Historically, these principles have provided strong deterministic guarantees for networked systems. However, these principles alone are insufficient for AI agents because the safety and appropriateness of an agent's actions often depend on semantic context beyond the expressiveness of static rules.
  Building on these principles, we advocate for a systematic approach to AI agent security that combines deterministic enforcement mechanisms, which provide strong security guarantees, with semantic, context-aware policies that enable nuanced decision-making. We then present a reference architecture and identify key research questions and future directions to guide the design of secure and privacy-preserving AI agent systems.

</details>


### 67. GUIDE: Governed Unified Intelligence for Document-to-Artifact Generation in Enterprise Settings

- **Authors:** Shivali Dalmia, Sumukha Thoppanahalli, Mohammadreza Sediqin, Abhishek Mukherji
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12133v1](http://arxiv.org/abs/2608.12133v1)
- **PDF:** [https://arxiv.org/pdf/2608.12133v1](https://arxiv.org/pdf/2608.12133v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise guideline documents are heterogeneous and multimodal, combining narrative text, complex tables, and embedded images. Existing LLM and VLM systems face hallucinated content, table structure degradation, and lack governed workflows extending beyond extraction to validation and artifact generation. This leaves enterprises to perform this manually, consuming 2-3 days per document. To address this, we introduce GUIDE, a governed multi-agent framework built on a shared versioned rule store with schema-validated inter-agent contracts and end-to-end provenance tracking. Six specialized agents handle parsing, VLM-driven extraction, consistency checking, evaluation, human-in-the-loop (HITL) escalation, and persona-tailored artifact synthesis. Evaluated on 120 real-world enterprise guideline documents, GUIDE achieves 96% document success, extracts 3,896 rules with 71.4% auto-approved, produces 812 deployment-ready artifacts, and reduces turnaround to 40-125 minutes per document.

</details>


### 68. SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges

- **Authors:** Yuchao Wu, Junqin Li, XingCheng Liang, Yongjie Chen, Yinghao Liang, Linyuan Mo, Guanxian Li
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12129v1](http://arxiv.org/abs/2608.12129v1)
- **PDF:** [https://arxiv.org/pdf/2608.12129v1](https://arxiv.org/pdf/2608.12129v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

While retrieval-augmented generation (RAG) has proven effective at giving LLMs access to external knowledge, mainstream dense-retrieval implementations remain inherently limited in handling structured constraints and multi-hop reasoning. Graph-based methods address this by constructing knowledge graphs offline, but they often fragment semantics, incur high maintenance, and complicate incremental updates. We propose SAG (SQL-Retrieval Augmented Generation), a structured retrieval architecture that organizes documents into an event-entity index without building a global knowledge graph. SAG represents each chunk as a semantically complete event paired with its entities, forming a latent hyperedge that preserves n-ary relations without decomposing them into triples. At query time, SAG treats shared entities as join keys to connect related chunks. This dynamically yields a query-scoped neighborhood of events, and yet every piece of evidence remains the original chunk throughout. Experiments on HotpotQA, 2WikiMultiHopQA, and MuSiQue show that SAG achieves the best retrieval and end-to-end QA performance on every benchmark, with gains that widen as reasoning-chain complexity increases. On MuSiQue, where multi-hop evidence chaining is most demanding, SAG reaches 80.36% Recall@5, outperforming the strongest baseline by 11.52 points. This work paves the way for knowledge infrastructure that enables LLM agents to retrieve and reason over continually growing organizational knowledge.

</details>


### 69. No One to Blame: A Framework of Constitutive AI Unaccountability

- **Authors:** Long Hoang Nguyen, Eva Späthe, Sebastian Lins, Ali Sunyaev
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12104v1](http://arxiv.org/abs/2608.12104v1)
- **PDF:** [https://arxiv.org/pdf/2608.12104v1](https://arxiv.org/pdf/2608.12104v1)
- **Categories:** cs.CY, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The increasing deployment of autonomous, agentic AI systems challenges traditional accountability mechanisms. Existing research predominantly frames AI accountability gaps as barriers that can be overcome through better standards, transparency, and institutional reform. We argue that this framing is insufficient: certain configurations of actors, systems, and institutions render AI accountability conceptually unachievable regardless of effort. We introduce the concept of constitutive AI unaccountability to capture these configurations. Through a three-stage qualitative study comprising a concept-centric literature analysis, a secondary analysis of 27 expert interviews with AI professionals from technical, legal, and sociotechnical backgrounds, and an illustrative framework application to the open-source agentic AI system OpenClaw, we identify nine categories and 20 themes of constitutive AI unaccountability. These are organized across structural, technological, and normative clusters and reinforce one another through eight directed interdependencies. Our framework is operationalized as a diagnostic instrument of 20 questions, which detected 17 of 20 conditions when applied to OpenClaw, including an inverted anthropomorphism configuration in which the AI agent was the only identifiable actor. We contribute a reframing of AI unaccountability as a constitutive property of sociotechnical systems, an extension of the four barriers to accountability, and a practical instrument for identifying accountability voids in specific AI deployments.

</details>


### 70. Multi-AUV Ad-hoc network-based Target Tracking: A Value Gradient Guidance Multi-Agent Diffusion Reinforcement Learning Approach

- **Authors:** Jiaao Ma, Chuan Lin, Guangjie Han, Shengchao Zhu, Qian Zhu, Ying Liu, Zhenyu Wang
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12436v1](http://arxiv.org/abs/2608.12436v1)
- **PDF:** [https://arxiv.org/pdf/2608.12436v1](https://arxiv.org/pdf/2608.12436v1)
- **Categories:** cs.LG, cs.MA, cs.NI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-AUV ad-hoc network-based target tracking requires networked autonomous underwater vehicles (AUVs) to cooperatively track maneuvering targets under constrained acoustic communication, dynamic topology, and uncertain ocean disturbances. Although multi-agent reinforcement learning (MARL) enables decentralized coordination through centralized training, existing methods suffer from high-dimensional joint state-action modeling, noise-sensitive policy generation, leading to unstable training and degraded tracking. To address these issues, we propose VGG-MADiffRL, a value-gradient-guided multi-agent diffusion RL algorithm, and MDCA, a diffusion?based hierarchical control architecture. Leveraging underwater mission characteristics, we model sonar detection mechanisms and ocean current disturbances, formulating cooperative tracking for multi-AUV ad-hoc networks as an MDP. The proposed MDCA constitutes a three-tier closed-loop control framework: a global intelligent control layer, a local online training layer, and a physical action execution layer. This structure enables synergistic optimization across task allocation, local decision processes, and execution feedback. Within MDCA, the local online training layer is the policy learning framework; VGG-MADiffRL builds on diffusion policies and incorporates value gradients to guide action generation in the reverse denoising process, steering the generated actions towards higher expected returns. It employs twin value networks with joint optimization and soft target updates to mitigate overestimation and training oscillations, promoting more stable convergence. Experimental results show that VGG-MADiffRL consistently achieves faster convergence, higher tracking accuracy, and smoother training dynamics in cooperative tracking scenarios, validating its effectiveness and practical engineering value in dynamic underwater settings.

</details>


### 71. CTBench: Evaluating Troubleshooting Capabilities of AI Agents in Realistic Telecom Network Operations

- **Authors:** Xingyu Yan, Tingting Dai, Antonio De Domenico, Mohamed Sana, Nicola Piovesan, Changchang Li, Bowen Liu, Kun Jiang, Mengjie Zhang, Dingcheng Shan, Jing-Cheng Pang, Chenwei Wu, Sijie Wu, Lianying Chao, Haoran Cai, Jiantao Ye, Xubin Li, Simon Mark Lucas, Xin Chen
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12002v1](http://arxiv.org/abs/2608.12002v1)
- **PDF:** [https://arxiv.org/pdf/2608.12002v1](https://arxiv.org/pdf/2608.12002v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agents are increasingly considered for automating network operations and maintenance, where engineers must diagnose network faults, optimize configurations to enhance services, and reduce operational costs while acting under strict constraints. However, existing evaluations fail to accurately model real network characteristics or assess agents under partially observable telecom environments with diverse vendors, devices, protocols, and interfaces. In this paper, we introduce CTBench, a public benchmark for assessing whether an agent behaves like a competent telecom troubleshooting engineer. CTBench focuses on root cause analysis and path restoration. Each task is constructed by experts and annotated with rich task metadata, including golden evidence steps. CTBench uses expert-grounded metrics that evaluate both final answers and the diagnostic evidence. Experiments with representative harness-model combinations show that state-of-the-art agents perform very well at identifying endpoints in path-restoration tasks but, more generally, underperform in root cause analysis. In particular, agents struggle with interface state, link-layer, service-management, and other operational faults. Most importantly, even when agents produce plausible or correct final answers, they often fail to provide the evidence-grounded diagnoses required in operational practice. Our results further show that path restoration is generally more resource expensive, yet larger resource usage does not necessarily translate into better diagnosis.

</details>


### 72. Retry, Switch, or Abstain? Learning Strategy-Aware Tool-Use Policies via Controlled Error Injection

- **Authors:** Chaoran Chen, Vy Nguyen, Ziji Zhang, Abhinav Gullapalli, Ziyi Wang, Yuxuan Lu, Dakuo Wang, Jing Huang, Zhou Yu, Jin Lai
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11977v1](http://arxiv.org/abs/2608.11977v1)
- **PDF:** [https://arxiv.org/pdf/2608.11977v1](https://arxiv.org/pdf/2608.11977v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using LLM agents are commonly trained and evaluated in environments where tool calls succeed reliably, yet deployed tools can fail transiently, persistently, or silently. Robust recovery therefore requires more than repeated retries: an agent may need to retry the same path, switch to an alternative, or recognize that no viable path remains. We present BENCH2ROBUST, a framework that converts failure-free tool-use benchmarks into controlled stochastic environments with scenario-controlled solvability, where episodes explicitly require retrying, switching, or stopping after available paths are exhausted. We use BENCH2ROBUST to study two complementary interventions: structured runtime recovery context through Bayesian Tool Memory (BTM), and curriculum-controlled reinforcement learning. Across 7 models from 4 families and two multi-turn benchmark families, tool failures produce a near-universal robustness gap. On held-out Retail tasks, BTM improves robustness by up to 16.8 percentage points without retraining, while RL learns complementary recovery behavior that remains beneficial without inference-time BTM. Combining the two reaches 40.8-45.5% under injection while preserving failure-free performance. These results suggest that robust tool use benefits from combining environment-specific recovery knowledge with learned recovery behavior.

</details>


### 73. ExRole: From Team Trajectories to Executable Roles in Multi-Agent Language Models

- **Authors:** Zhou Liu, Chaoyang Han, Zewei Pan, Zeli Su, Wentao Zhang
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11949v1](http://arxiv.org/abs/2608.11949v1)
- **PDF:** [https://arxiv.org/pdf/2608.11949v1](https://arxiv.org/pdf/2608.11949v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Roles provide an interpretable interface for organizing language-model agents, yet most multi-agent systems treat them as hand-written prompt labels disconnected from learned behavior and parameter updates. We argue that a useful role should instead be an executable control variable: it should summarize behavior predictive of future utility, guide subsequent interaction, and identify the trainable capacity responsible for that behavior. We introduce ExRole, a trajectory-to-role framework that learns future-aware role prototypes from prefix-local team traces, resolves them into readable instructions and token-aligned role markers, and optionally routes shared LoRA rank slots with turn-aligned credit. Across MuSiQue and 2WikiMultiHopQA, ExRole improves over single-agent search by 15.0/14.4 and 13.5/16.1 EM/F1 points, respectively. Against the strongest non-ExRole controls, the corresponding gains remain 11.5/11.6 and 7.7/9.7 points. Across both benchmarks, the controlled results consistently favor trajectory-induced role conditioning over role-free, manual, random, and shuffled alternatives. Role-Agent-Turn interventions further show that the induced roles capture transferable behavioral specialization beyond fixed agent identities or turn positions.

</details>


### 74. MindMemOS: A Portable and Self-Evolving Memory Operating Layer for AI Agents

- **Authors:** Kaichao Liang, Yuqi Cui, Hao Kong, Xinyuan Huang, Guohaotian Hou, Qingcan Kang, Liang Chen, Yiyang Yin, Ke Ye, Jiaquan Guo, Da Chen, Lingan Zeng, Yixing Peng, Rong Yao, Shixiong Kai, Mingxuan Yuan
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.12428v1](http://arxiv.org/abs/2608.12428v1)
- **PDF:** [https://arxiv.org/pdf/2608.12428v1](https://arxiv.org/pdf/2608.12428v1)
- **Categories:** cs.AI, cs.IR, cs.IT


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory is a core component of AI agents, enabling them to accumulate experience, maintain personalization, and adapt over long-term interactions. However, existing memory systems often remain fixed after development, limiting their ability to adapt their memory models, organization strategies, and procedural knowledge through continued use. We present MindMemOS, a portable and self-evolving memory operating layer that organizes open-world information using a unified entity property timestructure. MindMemOS supports scenario-adaptive memory modeling, higher-order pattern discovery, autonomous memory refinement, and continuous skill evolution. Its MindMemEvolve algorithm employs validation-driven evolutionary search to optimize memory schemas for target scenarios, whiledreaming consolidates accumulated memories by merging redundant records and resolving conflicts. In addition, implicit corrective feedback serves as a human-in-the-loop signal for identifying and revising potentially inaccurate or misaligned memories. Its MindSkillEvolve algorithm further transforms agent execution trajectories into reusable and progressively refined skills. MindMemOS achieves 94.03% accuracy on LOCOMO and 70.63% on PersonaMem. MindSkillEvolve improves SpreadsheetBench success by 9.2 percentage points over the initial-skill baseline.

</details>


### 75. Scalable Multi-Agent Maze Traversal with Local Communication

- **Authors:** Julian Rau, Jahir Argote-Gerald, Grace McFassel, Genki Miyauchi, Paul Trodden, Roderich Groß
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11895v1](http://arxiv.org/abs/2608.11895v1)
- **PDF:** [https://arxiv.org/pdf/2608.11895v1](https://arxiv.org/pdf/2608.11895v1)
- **Categories:** cs.RO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cave networks, pipe systems, and similar maze-like environments pose significant challenges for multi-agent navigation in unknown settings with limited communication. We propose a distributed algorithm that enables agents to collectively traverse an unknown, possibly cyclic graph. Agents enter sequentially at a designated start node and are tasked to localize and reach an undisclosed goal while avoiding collisions. They coordinate via local communication using leader-follower relationships and leader switching. At any moment in time, exploration is performed by only one of the agents, which runs a single-agent maze solver. We prove that the algorithm is complete, that its makespan is asymptotically equivalent (in the number of agents) to that of an optimal full-knowledge strategy, and derive its time and space complexity. Simulations with up to $625$ agents show a decreasing average sum-of-fuels as the number of agents increases and demonstrate that the proposed approach outperforms a naïve baseline in which all agents independently execute the single-agent solver.

</details>


### 76. Benchmark-Based Comparative Assessment of Publicly Benchmarked Indian Foundation Models: A Capability and Evaluation-Maturity Framework

- **Authors:** Avinash Agarwal, Vridhi Jain
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11891v1](http://arxiv.org/abs/2608.11891v1)
- **PDF:** [https://arxiv.org/pdf/2608.11891v1](https://arxiv.org/pdf/2608.11891v1)
- **Categories:** cs.CY, cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Governments increasingly fund indigenous foundation models to strengthen national AI capability, digital sovereignty, and multilingual computing. Assessing the progress of such national ecosystems is complicated by inconsistent benchmark reporting, proprietary evaluation methodologies, and rapidly evolving model releases. This paper presents a structured, benchmark-based comparative assessment of publicly benchmarked Indian foundation models against global frontier and comparable-scale models, across eight capability domains: general-purpose reasoning, coding and software engineering, agentic AI and computer use, cybersecurity, vision and image understanding, video and multimodal understanding, scientific research, and Indic language capability. Using only publicly reported benchmark results, we find that Indian models achieve strong scores on established benchmarks such as MMLU and MATH-500. However, these benchmarks are now widely regarded as saturated, and frontier developers no longer report them. Indian models participate far less frequently in newer, agentic, and domain-specialized evaluations. Benchmark participation is also highly uneven across Indian organizations. Among the models surveyed, Sarvam AI reports the broadest benchmark coverage by a substantial margin. We propose an exploratory four-dimension Benchmark Maturity Index (BMI), scoring each capability domain on standardization, participation, independent verification, and national coverage. We show that the BMI refines, and in some cases revises, the maturity judgments that a purely descriptive review would produce. We argue that many apparent capability gaps in the public record cannot be distinguished, on available evidence, from evaluation-ecosystem gaps. This has direct implications for how national AI programs should design monitoring and funding criteria.

</details>


### 77. Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents

- **Authors:** Gen Dong, Yanjie Gao, Liqun Li, Tianyin Xu, Yu Hua, Fan Yang
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11888v1](http://arxiv.org/abs/2608.11888v1)
- **PDF:** [https://arxiv.org/pdf/2608.11888v1](https://arxiv.org/pdf/2608.11888v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent skills are the de facto mechanism for extending LLM agents with reusable guidance. A skill can shape the agent's task execution, including planning, tool use, problem-solving, and validation. Prior work reported mixed results of agent skills: some skills improve task success rates, while others have no effect, increase token use and execution time, and even reduce success rates. This paper presents a comprehensive analysis of skill-induced agent failures by attributing task failures and cost regressions to specific loaded skills. We introduce a differential analysis framework that attributes a failure or regression to a skill by comparing a target skill-guided run against a no-skill or semantically matched skill reference run that solves the same task, or solves it more cheaply. We instantiate this framework on SkillsBench and SWE-Skills-Bench, yielding 307 skill-induced failures, including 125 functional failures and 182 efficiency regressions. We also build SkillTriage, a taxonomy-guided attribution tool that normalizes paired cases, extracts differential evidence, and produces triage reports. Our major findings include: (1) Skill induced functional failures are rarely caused by obviously irrelevant skills; instead, seemingly relevant skills often make the agent incorrectly implement or omit task-required implementation elements. (2) Skill-induced efficiency regressions are not explained by prompt length alone. (3) The largest sources within Excessive Procedure are excessive verification and heavy implementation pipelines, contributing 67 and 30 cases, respectively. This shows that skills often turn validation checklists and construction recipes into mandatory work. Based on our findings, we propose research topics and tooling improvements for safer and more cost-aware skill reuse.

</details>


### 78. Advancing MLLM-based UAV Image Understanding and Reasoning: A Benchmark and a Training-Free Multi-Agent System

- **Authors:** Haoyu Zhang, Shuoxun Zhang, Peng Ye, Lin Zhang, Jiakang Yuan, Shenghong Yi, Yuening Wang, Tao Chen
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11738v1](http://arxiv.org/abs/2608.11738v1)
- **PDF:** [https://arxiv.org/pdf/2608.11738v1](https://arxiv.org/pdf/2608.11738v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal Large Language Model (MLLM)-based UAV aerial image understanding and reasoning is essential for aerial intelligence yet poses distinct challenges arising from extreme scale variation, arbitrary camera orientations, and high object density. Despite growing interest, existing evaluations remain fragmented across individual datasets and narrow tasks, leaving a critical gap in unified assessment of UAV understanding and reasoning capabilities. To fill this gap, we construct UAVQA-Bench, a benchmark of 1,500 human-annotated QA pairs drawn from 13 public UAV datasets, covering 6 capability dimensions and 16 tasks in both multiple-choice and visual grounding formats. Systematic evaluation of a broad range of open-source and closed-source MLLMs as well as agent-based systems on UAVQA-Bench identifies three key failure modes: domain-toolset mismatch, unchecked error propagation, and static reasoning. Motivated by these findings, we propose UAV-MAS, a training-free multi-agent system for MLLM-based UAV aerial image understanding and reasoning, comprising a Domain-Specific Perception Engine (DSPE) that routes queries to task-appropriate visual tools, a Context-Aware Iterative Refinement module (CAIR) that validates intermediate reasoning to curb error accumulation, and a Difficulty-Aware Adaptive Search mechanism (DAAS) that adjusts search depth to question difficulty. UAV-MAS with a 32B open-source MLLM achieves 77.0% overall accuracy on UAVQA-Bench, surpassing Gemini 3 Pro by 4.0\%, while the 8B variant improves 8.7\% over its base model.

</details>


### 79. FrontierFinance: A Challenging Benchmark for Measuring Frontier Intelligence of Finance Agents

- **Authors:** Yuhao Zhang, O. Ozan Koyluoglu, Thejas Venkatesh, Richard Diehl Martinez, Vishank Bhatia, Arash Alidoust, Ashwin Paranjape
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11683v1](http://arxiv.org/abs/2608.11683v1)
- **PDF:** [https://arxiv.org/pdf/2608.11683v1](https://arxiv.org/pdf/2608.11683v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly deployed for professional investment research, yet no benchmark captures the complexity of the full investor workflow. Existing benchmarks mainly target financial data extraction, a narrow slice that current models have largely saturated, while reference-based metrics and generic LLM-as-a-judge scoring fall short on the open-ended, long-form answers that real analyst queries demand. We introduce FrontierFinance, a fully open benchmark of 220 expert-crafted queries and 11,543 source-attributed rubrics spanning six crucial use cases across the full investor workflow. FrontierFinance is both broader and harder than existing public finance benchmarks. Evaluating frontier models and agent systems under a common harness restricted to publicly available data, we find that the tool harness, not the model alone, strongly shapes quality and efficiency; that Samaya's in-house system leads at 56.0%, ahead of the strongest frontier model (Claude Fable 5, 49.2%) at roughly 2.2x lower cost; and that the best open-weight model (Kimi K3, 46.4%) nearly matches the best proprietary model at 4.5x lower cost. Screening & Discovery and Sector, Industry & Macro remain the hardest use cases across all systems, where even the best systems reach only 33% and 39%. We make the dataset and grading code publicly available.

</details>


### 80. AgenticTwin: An Agentic LLM Framework Integrated with Digital Twin for Anomaly Detection

- **Authors:** Touseef Hasan, Mounika Ghanta, Souvika Sarkar, Ujjwal Guin
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11679v1](http://arxiv.org/abs/2608.11679v1)
- **PDF:** [https://arxiv.org/pdf/2608.11679v1](https://arxiv.org/pdf/2608.11679v1)
- **Categories:** cs.AI, cs.IR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Digital twins are increasingly used to monitor and simulate the behavior of cyber-physical systems. Even with skilled operators, interpreting anomalies detected within digital twin pipelines is challenging, as the sheer complexity and volume of raw sensor data make thorough analysis difficult. Recent advances in large language models (LLMs) offer promising capabilities for reasoning and explanation, yet their integration into digital twin-driven anomaly analysis remains underexplored. In this work, we propose AgenticTwin, an agentic framework that integrates LLM-driven reasoning with a digital twin-based anomaly detection pipeline. The framework grounds LLM-generated explanations in outputs from a digital twin-driven anomaly classifier and enables human operators to ask relevant natural-language questions about the system. Beyond the framework itself, we introduce a benchmark-oriented evaluation pipeline constructed over synthetic anomalies injected into a real-world weather sensor dataset, enabling controlled generation of operator queries over anomaly events. We further evaluate the feasibility of deploying lightweight, open-source LLMs for practical cyber-physical environments. Experimental results demonstrate that structured agent collaboration and knowledge-grounded reasoning improve diagnosis quality, contextual retrieval, and mitigation quality across diverse possible anomaly scenarios.

</details>


### 81. XBridge: Entity-Grounded Latent Bridge for Heterogeneous LLM Communication

- **Authors:** Wooseong Yang, Wei-Chieh Huang, Weizhi Zhang, Yu Wang, Philip S. Yu, Junhyun Lee
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11676v1](http://arxiv.org/abs/2608.11676v1)
- **PDF:** [https://arxiv.org/pdf/2608.11676v1](https://arxiv.org/pdf/2608.11676v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Heterogeneous multi-agent LLM systems, where agents are powered by different model families, can outperform homogeneous configurations by reducing redundant reasoning patterns. Yet existing communication protocols either operate through text, discarding the sender's internal representations, or require architectural homogeneity for latent-level transfer. We identify the entity grounding problem in cross-architecture communication: cross-attention bridges that transfer continuous representations across different LLM families suffer from rare-token compression collapse, where entity identity is lost in the continuous bottleneck (bridge-only F1 ~30%). We propose XBRIDGE, a decode-free communication protocol that addresses this through two mechanisms. Lexical Anchor Mapping (LAM) maps the sender's original context tokens to the receiver's vocabulary, providing discrete entity anchors. A Latent Enrichment Bridge (LEB) lets the receiver query the sender's hidden states for contextual enrichment. The entity anchors ground the bridge's contextual signals to specific entities through the receiver's own self-attention. Across three model families (Llama, Qwen, and Mistral), seven benchmarks, and both communication directions, XBRIDGE outperforms text-based communication on all seven tasks for each model pair while achieving 11x lower latency, and in a same-architecture setting it also exceeds a KV-sharing baseline on six of seven tasks. LEB requires only 264M trainable parameters (3.8% of the receiver), is trained on a small balanced sample set, and adds negligible inference overhead.

</details>


### 82. GCPO: Diagnosing and Constraining Subspace Geometry in Rollout RL for LLMs

- **Authors:** Kai Yang, Jingwei Xu, Wanyu Wang, Kai-Yuan Guo, Zhenbo Yu, Yi Wang, Yu Qiao
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11674v1](http://arxiv.org/abs/2608.11674v1)
- **PDF:** [https://arxiv.org/pdf/2608.11674v1](https://arxiv.org/pdf/2608.11674v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

On-policy rollout methods such as GRPO are central to post-training of large language models, yet they frequently suffer from training instabilities, cross-task capability degradation, and response-length inflation. Although prior work has characterized the subspace geometry of aggregate updates, the stepwise variation of this geometry and its relationship to model performance remain unclear. We introduce Principal-Subspace Overlap, a dimension-corrected measure of individual rollout updates relative to the dominant singular subspaces of pretrained weights. Despite low average overlap, transient spikes often precede performance degradation. To address this, we propose GCPO (Geometrically Constrained Policy Optimization), which applies hard bilateral orthogonal projections to constrain updates to the complementary subspaces, preventing such excursions by construction. Across mathematical reasoning, code generation, and tool-use tasks on Qwen3-8B and GLM4-9B, GCPO consistently outperforms GRPO and recent variants, including DAPO and GSPO, improving over the base models and the strongest baseline by up to 27.69 and 2.37 points, respectively. Furthermore, GCPO preserves general capabilities, eliminates response-length inflation, and stabilizes policy entropy. Our findings provide a new diagnostic lens and a principled design perspective for stable reinforcement learning post-training.

</details>


### 83. Is Per-Agent Policy Composition Safe? Rethinking Successor-Feature Transfer in Cooperative Multi-Agent Reinforcement Learning

- **Authors:** Zijian Zhao, Sen Li
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11658v1](http://arxiv.org/abs/2608.11658v1)
- **PDF:** [https://arxiv.org/pdf/2608.11658v1](https://arxiv.org/pdf/2608.11658v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Many reinforcement learning systems, from fleet management to traffic signal control, must serve an objective that changes dynamically after deployment, and retraining a policy for each new objective is prohibitively expensive. For a single agent, this problem is well understood: successor features with generalized policy improvement, together with their universal extension, recombine a library of learned policies into a policy for any new objective, with a guarantee that the result is never worse than any policy in the library. However, multi-agent transfer has received far less attention, and the common practice of letting each agent recombine its own library independently inherits the recipe but not the guarantee. We prove that this independent composition can produce joint behavior strictly worse than every policy in the library, because recombining teammates changes the environment each agent faces and invalidates the values it relies on, a failure with no single-agent counterpart. We further show that the only unconditionally safe fixed rule is synchronized composition, which moves the whole team to one jointly trained policy but cannot serve objectives that assign different goals to different agents. To attain safety and flexibility at once, we propose MA-USFA, a hierarchical method with two layers: a lower layer of universal successor feature approximators that predicts each agent's successor features while conditioned on its teammates' objectives, and an upper composer that selects, across agents, which library entry each agent should follow and supplies the cross-agent correction a per-agent value cannot represent. Trained once over the distribution of objectives, it is applied at deployment with no per-task adaptation.

</details>


### 84. Beyond Memory: A Transactional Continuity Kernel for Long-Lived AI Agents

- **Authors:** Jun He, Deying Yu
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11632v1](http://arxiv.org/abs/2608.11632v1)
- **PDF:** [https://arxiv.org/pdf/2608.11632v1](https://arxiv.org/pdf/2608.11632v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Persistent AI agents accumulate versioned state across long horizons, but storage retention alone does not identify authoritative state. Without an explicit control plane, unmediated updates by models, tools, and background workers risk stale overwrites, un-audited exposures, and self-authorizing privilege escalation. We argue that agent state governance is an infrastructural activation problem, defining continuity as an unbroken, authorized lineage of accepted branch heads. We present the Continuity Kernel (CK), an activation contract that decouples off-commit candidate evaluation from atomic state activation. Untrusted components propose typed changes against an exact predecessor head or typed absence. A short activation transaction revalidates ownership, pre-state authority, freshness, and effect uniqueness, recording one stable disposition (Commit, Reject, Quarantine, or Defer). Only Commit atomically advances the branch head and installs the complete accepted unit (state, authority, lineage, effects, outcome, and receipt). A bounded executable model verifies the protocol across 2,808,230 reachable states and 5,526,474 state-changing transitions with zero invariant violations.

</details>


### 85. Learning to Persuade Exposes How Easily LLMs Abandon Correct Beliefs

- **Authors:** Nimet Beyza Bozdag, Emre Can Acikgoz, Gokhan Tur, Dilek Hakkani-Tür
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11624v1](http://arxiv.org/abs/2608.11624v1)
- **PDF:** [https://arxiv.org/pdf/2608.11624v1](https://arxiv.org/pdf/2608.11624v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Persuasion is a core dynamic of natural language communication, shaping how large language models (LLMs) update beliefs, resolve disagreements, and reach decisions. As LLMs increasingly debate, advise, and think collaboratively with humans and each other, resistance to harmful persuasion becomes a core requirement for reliable behavior. Yet we show that this requirement is far from met: a single targeted persuasive argument is enough to collapse model accuracy to near zero, even when the argument is factually false. We formalize this threat as adversarial persuasion and introduce an adversarial reinforcement learning framework that trains persuader agents to change a target model's answer in a single interaction. First, we show that optimizing persuasion strategies through trial and error exposes vulnerabilities that static prompting misses: RL-trained persuaders raise persuasion success from approximately 24% to over 93% against the training-time persuadee. Second, we find that these learned strategies transfer to unseen models, achieving 83% attack success on Qwen-14B, 79% on Llama-3.1-8B, and 25% on GPT-4o-mini. Third, we demonstrate that a curriculum that bootstraps on more persuadable open-weight models before targeting harder models further increases GPT-4o-mini attack success from 25% to 38%. Moreover, our results reveal that optimized persuaders increasingly rely on credibility-based tactics, including fabricated citations and false authoritative evidence. Together, these findings expose a critical weakness in current LLM agents: even when they initially reason correctly, they can be steered toward false conclusions by optimized natural language influence. This positions persuasion robustness as a necessary safety criterion for multi-agent and human-AI decision-making systems.

</details>


### 86. Beyond Single-Turn Confidence: Trajectory-Adapted Uncertainty Quantification for LLM Agents

- **Authors:** Dylan Bouchard, Mohit Singh Chauhan
- **Published:** 2026-08-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11552v1](http://arxiv.org/abs/2608.11552v1)
- **PDF:** [https://arxiv.org/pdf/2608.11552v1](https://arxiv.org/pdf/2608.11552v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Uncertainty quantification (UQ) methods for language models are typically evaluated on single-turn outputs, where uncertainty is attached to one generated answer. For LLM agents, however, the unit of observation is an interactive trajectory, where the model can ask clarifying questions, call tools, update state, and make intermediate decisions whose errors propagate to the final outcome. We study whether three common families of single-turn UQ methods transfer to this setting. Across five LLMs and four multi-turn tool-use datasets from BFCL-v4 and $τ^2$-bench, we evaluate white-box scorers based on action-token probabilities, black-box consistency scorers based on resampled trajectories, and reflexive scorers based on model self-assessment of the trajectory. We find that transfer is often useful but uneven. Token-probability scores are highly sensitive to the choice of aggregator used across turns, reflexive scores provide the strongest low-cost baseline in most evaluated settings, and black-box self-consistency is often the strongest UQ family, with trajectory-equivalence and action-set consistency typically ranking highest among its variants. These results suggest that UQ methods developed for single generations should be revalidated at the trajectory level, with careful attention to the consistency measurement, aggregator choice, and computational budget.

</details>


### 87. The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark

- **Authors:** Jeremy Spence, Nicholas Assaderaghi, Jinhao Zhu, Nikil Ravi, Raluca Ada Popa, Guannan Wei, Yangruibo Ding, Zhuo Zhang
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11469v1](http://arxiv.org/abs/2608.11469v1)
- **PDF:** [https://arxiv.org/pdf/2608.11469v1](https://arxiv.org/pdf/2608.11469v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are rapidly improving in cybersecurity capabilities when the source code is available for analysis, yet much of the software most consequential to cybersecurity, including malware, firmware, and proprietary applications, is available only as binaries. Analyzing such software requires reverse engineering(RE): recovering program semantics before the analysis can be meaningfully performed. However, evaluating agentic RE poses a fundamental challenge: benchmark instances must be unseen as source code in the LLMs' training data to prevent models from taking shortcuts by recognizing them rather than really analyzing them, while also matching the scale and anti-analysis protections of real software. Unfortunately, however, existing benchmarks do not jointly satisfy these requirements. To this end, we introduce SRE-Bench, the first realistic, contamination-free RE benchmark. Built entirely from scratch by RE experts with over 5,000 hours, SRE-Bench comprises 19 private, real-world-scale programs averaging 16.9K lines of code. We further developed 44 in-house anti-analysis primitives, yielding 262 binary instances and 1572 deterministically graded tasks. Our evaluation across five frontier LLMs (GPT-5.6-sol,Claude-Opus-5,GPT-5.5,Grok-4.5, and GLM-5.2) shows that RE remains largely unsolved: the strongest model, GPT-5.6-sol, scores 61.4% per instance, and fully solves only 31.5% of the instances. Our analysis further reveals that agents behave differently from human engineers, where agents are relatively insensitive to compiler optimization and static linking. Controlled ablations also confirm that both contamination control and realistic scale are essential. These results indicate that strong source-code security capabilities do not yet transfer to binary analysis, highlighting RE as an important frontier for agentic cybersecurity and SRE-Bench as a rigorous testbed to measure progress.

</details>


### 88. Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology

- **Authors:** Del Coburn, Scott Sanner, Dan Silver
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11420v1](http://arxiv.org/abs/2608.11420v1)
- **PDF:** [https://arxiv.org/pdf/2608.11420v1](https://arxiv.org/pdf/2608.11420v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Medical diagnostic reasoning is a high-impact use case for LLMs that carries significant implications for the health and wellbeing of users. When OpenAI (2026) reports that more than 5% of ChatGPT messages globally are healthcare-related, the transparency of these systems becomes a serious design concern. This is especially true for complex cases, where differential diagnosis often requires integrating multiple forms of specialist reasoning. Existing work has proposed multi-agent approaches to medical diagnosis, but it remains unclear when such systems are needed, why they help, and where they outperform monolithic inference. We introduce Social Chain of Thought (SCoT),a multi-round pipeline for medical differential diagnosis that structures multi-agent interaction as a deliberative framework for collabora. tive LLM reasoning. Evaluating SCoT against single-agent baselines, one-agent pipeline ablations, and best-of-n scaling, we show that its recall advantage is not reproduced by monolithic inference alone. SCoT is most successful in the hardest diagnostic cases, where multiple rounds of specialist conversation help recover ground-truth diagnoses and converge on a higher-recall differential.

</details>


### 89. From Numbers to Judgment: Specialist LLM Agents and Reinforcement Learning for European Listed Real Estate

- **Authors:** Pardis Taghavi, Santosh Bhavani
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11381v1](http://arxiv.org/abs/2608.11381v1)
- **PDF:** [https://arxiv.org/pdf/2608.11381v1](https://arxiv.org/pdf/2608.11381v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study whether the localized numerical operations and integrative judgments of financial analysis benefit from the same form of LLM specialization. Larix maps a 16-lens European listed-real-estate analysis framework to eight lens-aligned specialists; we compare a frontier LLM under monolithic versus specialist-decomposed prompting while holding the model, source evidence, task instructions, output schema, and scoring fixed. Across 19 firms spanning seven regulatory wrappers, decomposition improves the numerical-task aggregate by 15.8 percentage points but does not reliably improve, and can reduce, performance on judgment tasks, a pattern stable across four frozen-template dispatches; a single-agent control given the complete framework does not reproduce the numerical gain. Post-training Qwen3.5-9B with GRPO using task-aligned structured rewards then raises the development-split score by 12.0 points and the judgment aggregate by 14.2 points, with gains on all four sub-ceiling tasks; the gains transfer to unseen firms (+15.2 points overall; +40.4 on covenant stress) and to unseen regulatory wrappers (+4.3), with positive transfer on all three anti-memorization splits. Prompt-level decomposition thus improves modular numerical execution, whereas targeted parameter adaptation improves integrative financial judgment.

</details>


### 90. When Do Institutions Beat Intelligence?

- **Authors:** Zhengye Han
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11357v1](http://arxiv.org/abs/2608.11357v1)
- **PDF:** [https://arxiv.org/pdf/2608.11357v1](https://arxiv.org/pdf/2608.11357v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

More capable agents do not necessarily form a more capable collective. A multi-agent system may jointly possess sufficient information yet fail because evidence is poorly routed, unreliable reports enter public belief, correlated claims masquerade as independent support, shared state becomes stale or strategically distorted, or useful evidence is exposed through an ineffective action interface. We ask when additional resources should improve the reasoner and when they should instead change the institutional structure through which the collective forms and acts on public information. Drawing on functional distinctions from research on group decision making and distributed cognition, we construct controlled artificial ecologies around four loci of collective failure: access and routing, admission and dependence, state maintenance and incentives, and representation and action. Across these ecologies, we separately vary model capability and institutional structure, pairing positive interventions with matched reasoning baselines and mechanism-breaking controls. The experiments reveal a consistent boundary: institutions help when they repair failures in how a collective constructs usable public state, but lose their advantage when their signals are uninformative or uncheckable, when stronger intelligence can perform the same transformation directly, or when the resulting state cannot support reliable action. Our results recast the choice between intelligence and institutions as a diagnosis of where collective reasoning fails.

</details>


### 91. Governing Agentic AI in FinTech

- **Authors:** Henry Han
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11344v2](http://arxiv.org/abs/2608.11344v2)
- **PDF:** [https://arxiv.org/pdf/2608.11344v2](https://arxiv.org/pdf/2608.11344v2)
- **Categories:** cs.CY, cs.AI, q-fin.RM


> Summary unavailable.


<details>
<summary>Abstract</summary>

Financial institutions are delegating consequential decisions to agentic AI systems that decompose goals, coordinate models and tools, and act with little oversight. Yet agentic AI governance in FinTech is under-investigated. We argue the binding governance constraint is not capability but verifiability. We define the Verifiability Gap as the shortfall between the verification delegated authority demands and the explainability and reproducibility retained after a decision. It is indexed to a verifier, evidentiary standard, and audit lag. We develop a multilevel governance theory for agentic AI and test its mechanisms in three studies over nine model versions, from a three-billion-parameter local model to a commercial frontier system. Study 1 shows that provider releases alter historical financial actions, and that the controls replay needs belong to the provider: the frontier model rejects temperature, top_p and top_k outright and exposes no random seed. Under the tightest controls each endpoint allows, a local model reproduced 320 of 320 executions, hosted models 319 of 320 and 959 of 960. Study 2 shows that orchestration is a latent policy layer. Architecture changes final actions, and no execution record repeated in any configuration at any scale. The frontier model reproduces its own actions more often than the local ones, its record no better, and loses a comparable share of its differentiation. Capability buys a higher starting point, not auditability. Study 3 shows two deterministic credit-model versions each reproduce their current action perfectly, yet the current cannot recover a historical one. We conceptualize reproducibility as a governance profile, not a scalar, yielding evidence-contingent delegation: authority is defensible only while retained evidence substantiates its exercise. Beyond finance, the framework extends to other high-stakes domains requiring auditability.

</details>


### 92. Better, Faster, Stronger: Programmatic Skill Learning Best Reduces Agent Cost

- **Authors:** Zixi Huang, Xiheng Wang, Andrew Wang, William Jurayj, Bernal Jiménez Gutiérrez, Daniel Khashabi, Nicholas Andrews
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11338v1](http://arxiv.org/abs/2608.11338v1)
- **PDF:** [https://arxiv.org/pdf/2608.11338v1](https://arxiv.org/pdf/2608.11338v1)
- **Categories:** cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recently, the practice of augmenting LLM agent capability with skills has gained prevalence. We explore the cost effective adaptation of agents to novel domains by means of learning skills. Existing works focus on performance gain over cost effectiveness. As a result, little is known about what skill learning strategies save cost. We argue that among all the different skill learning methods, those that view skills as programs can achieve the best cost reduction. By executing sequences of actions deterministically, a program-augmented agent can reliably and cheaply achieve goals that would otherwise require trial and error and risk degenerate behavior over long horizons. An agent can learn at inference time by incrementally discovering these programs and equipping them for future tasks. We hypothesize that past trajectories contain enough signal to guide skill learning, even without replay or validation, provided the agent can learn to analyze them. To test our claims, we propose SpeedRunner, a coding agent that analyzes trajectories and refactors skills for better performance on future tasks. Across three different embodied environments, we show that SpeedRunner consistently achieves the frontier in learning and cost reduction while remaining robust against distribution shifts and environmental randomness.

</details>


### 93. Backdoor Decontamination Dynamics in LLM Agents

- **Authors:** Gabriel Huang, Abhay Puri, Léo Boisvert, Alexandre Drouin, Perouz Taslakian, Spandana Gella, Christopher Pal
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11295v1](http://arxiv.org/abs/2608.11295v1)
- **PDF:** [https://arxiv.org/pdf/2608.11295v1](https://arxiv.org/pdf/2608.11295v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Open-weight LLM agents are vulnerable to backdoors installed during fine-tuning, which may be undetectable if the trigger conditions are never met during testing. Assuming defenders do not know the existing trigger, they cannot unlearn it directly. One decontamination strategy is to install a known backdoor (defensive poisoning) then to unlearn it, hoping that the original unknown backdoor is removed as a side effect. However, this procedure has uncertain outcomes: the original backdoor may persist or be erased or rerouted, among other possibilities. We introduce a framework for studying these dynamics in tool-calling agents, decoupling trigger, response, teacher, and fine-tuning method across systematic experiments on AgentDyn. Across 115 experiments, defensive poisoning alone erases around 56% of original backdoors; subsequent decontamination then drives almost all survivors to erasure, confirming that trigger recognition and malicious execution are behaviorally dissociable. Interestingly, our experiments find that malicious backdoors never persist when using different triggers of the same general type as the defensive backdoor when followed by decontamination via unlearning. Co-installing up to four backdoors increases resistance (around 36% erased), yet decontaminating a single known co-resident backdoor collaterally clears 52/60 co-residents (87%). Upon visualizing postdecontamination model internals using J-lens, we confirm that although the decontamination restores benign LLM responses, traces of original trigger awareness persist at intermediate layers.

</details>


### 94. Long-Horizon AI Research for Grothendieck Constant: A Case Study in Human-AI Mathematical Collaboration

- **Authors:** Alan Li, Rahul Saha, Anton Xue, Swarat Chaudhuri, Adam Klivans, Pravesh K Kothari, Raghu Meka
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11195v3](http://arxiv.org/abs/2608.11195v3)
- **PDF:** [https://arxiv.org/pdf/2608.11195v3](https://arxiv.org/pdf/2608.11195v3)
- **Categories:** cs.AI, cs.CC, cs.HC, math.FA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly used in mathematics research, but it is often unclear how to use them effectively. Towards this, we present an extensive case study of how AI was used to improve bounds on the Grothendieck constant $K_G$, which captures the hardness between combinatorial problems and their continuous relaxations. Specifically, while the precise value of $K_G$ is not known, we recently tightened the best known bounds to \[
  \frac{6π}{11}
  \;\le\;
  K_G
  \;\le\;
  \fracπ{2\log(1+\sqrt2)} - 10^{-4}. \] Crucially, these improvements were achieved using an AI research system that could arrive at insights deemed novel by domain experts. We give a detailed discussion of our experience using AI for mathematics research, particularly touching upon its strengths and weaknesses, as well as our experience with creating ideal conditions for AI to arrive at breakthrough insights.

</details>


### 95. Scaling Laws for Majority-based Opinion Dynamics in the Presence of Stubborn Agents

- **Authors:** Luke Meredith, Arpan Mukhopadhyay
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11071v1](http://arxiv.org/abs/2608.11071v1)
- **PDF:** [https://arxiv.org/pdf/2608.11071v1](https://arxiv.org/pdf/2608.11071v1)
- **Categories:** math.PR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

In a multi-agent system, there are often stubborn followers of specific opinions or beliefs. Motivated by this observation, in this paper, we aim to understand how stubborn agents affect the distribution of opinions in a network where both stubborn and non-stubborn agents interact with each other. To do so, we assume that all agents have an opinion in the set $\{0,1\}$ and each non-stubborn agent updates its opinion according to the $2k$\textit{-choices rule}, where the agent samples $2k$ neighbours (including both stubborn and non-stubborn neighbours) uniformly at random and adopts the majority opinion among the sampled group of neighbours and itself. We assume that a proportion of agents, $γ_i$, are stubborn followers of opinion $i\in \{0,1\}$. It is natural to expect that the steady-state distribution of the opinions in the network will be dominated by the opinion with the larger proportion of stubborn followers. We show that while this is true, the time to reach steady-state depends heavily on the values of the parameters $γ_0$ and $γ_1$. When the individual values of these parameters, as well as their difference, are small, it can take an exponentially long time (in the network size) to reach the steady-state. In sharp contrast, when at least one of the parameters $γ_0$ and $γ_1$ is large, the network reaches the steady-state in a time that is only logarithmic in the network size. Hence, there exists a sharp phase transition in the network dynamics based on the proportions of stubborn agents. We also characterise the behaviour of the system when the parameters $γ_0$ and $γ_1$ lie on the boundary of the phase transition. In this boundary region, we show using Stein's method that the dynamics are driven by a diffusion process which takes polynomial time to mix.

</details>


### 96. Who Are You Explaining To? A Multi-Agent System for Audience-Aware XAI Narratives

- **Authors:** Francesco Musicco, Danilo Danese, Giuseppe Fasano, Angela Lombardi, Alberto Carlo Maria Mancino, Tommaso Di Noia
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11033v1](http://arxiv.org/abs/2608.11033v1)
- **PDF:** [https://arxiv.org/pdf/2608.11033v1](https://arxiv.org/pdf/2608.11033v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Feature-attribution methods such as SHAP provide useful evidence about individual model predictions, but their numerical outputs are rarely sufficient for audiences with different expertise, goals, and risks of misinterpretation. In medical AI, the same local explanation must reach patients, clinicians, and data scientists through markedly different forms of communication, and naive verbalization through large language models (LLMs) is prone to weak grounding, conflation of attribution with causal language, and outputs that are persuasive without being faithful to the underlying model evidence. We introduce XstrAI, an audience-aware multi-agent framework that treats local explanations as fixed evidence and structures how it is communicated to each target reader. Each prediction case is encoded as an immutable structured representation, shared identically across audiences so the underlying evidence remains fixed. Generation is factored into three specialized LLM agents responsible for audience-aware planning, linguistic realization, and validation for grounding, attribution consistency, communicative risk, and audience appropriateness, with a bounded revision loop triggered on detected inconsistencies. We evaluate XstrAI on diabetes and stroke risk prediction against 11 baselines, ranging from direct verbalization to a re-implementation of a state-of-the-art narrator. The evaluation combines an intra-narrative regime measuring fidelity to SHAP evidence with an extra-narrative regime assessing audience appropriateness through reference corpora, multi-family LLM judges, and a survey with target readers. In both evaluations, XstrAI's narratives are consistently assigned to their intended audience by independent judges, and preferred over all baselines on Clinician and Patient audiences, with competitive performance on Data Scientist, where audience-conditioned single-prompt baselines lead.

</details>


### 97. MobileMem: Learning from a Year of Mobile Experiences

- **Authors:** Xinle Deng, Yida Xue, Xiangyuan Ru, Haoming Xu, Shuofei Qiao, Mengru Wang, Yijun Chen, Buqiang Xu, Chen Jiang, Yuchen Eleanor Jiang, Lizhong Wang, Jianfeng Wang, Li Zeng, Haofen Wang, Guilin Qi, Huajun Chen, Ningyu Zhang
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13606v1](http://arxiv.org/abs/2608.13606v1)
- **PDF:** [https://arxiv.org/pdf/2608.13606v1](https://arxiv.org/pdf/2608.13606v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA, cs.MM


> Summary unavailable.


<details>
<summary>Abstract</summary>

The next generation of AI agents is increasingly moving beyond systems that answer isolated questions toward persistent personal assistants that can understand, remember, and continuously learn from users' experiences. Such assistants require long-term memory to accumulate and leverage user-specific experiences over time, yet existing benchmarks remain inadequate for realistic mobile settings, where experiences are heterogeneous, multimodal, evolving, and deeply personal. We introduce MobileMem, a benchmark and framework for studying on-device long-term memory, grounded in a year-scale collection of mobile experiences. MobileMem employs a knowledge-grounded synthesis pipeline to construct coherent and temporally consistent long-horizon trajectories from user-app sessions. It provides complementary text and multimodal settings covering multi-hop and temporal reasoning, knowledge updating, and implicit preference inference. Specifically, MobileMem enables agents to remember the past, understand the present, and adapt to the future. By modeling experiences rather than isolated facts, MobileMem moves memory beyond information retrieval toward experiential intelligence for continuous personal learning.

</details>


### 98. ComBodied Agents: a New Paradigm of Human-Centric Agentic AI

- **Authors:** Qianggang Ding, Xingyao Wang, Rui Feng, Zhibin Wang, Feixiang Yao, Kelong Mao, Hao Sun, Zhiyao Luo, Jiankai Tang, Lei Li, Jiadong Guo, Minheng Ni, Weicong Lin, Chenxi Yang, Hongxiang Gao, Zhenghua Chen, Yang Bai, Min Wu, Jun Cheng, Huazhu Fu, Dacheng Tao, Bang Liu
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10915v2](http://arxiv.org/abs/2608.10915v2)
- **PDF:** [https://arxiv.org/pdf/2608.10915v2](https://arxiv.org/pdf/2608.10915v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

After an older adult misses a medication dose, a software agent can send another reminder and an embodied agent can bring the medication. Yet neither explains whether the person forgot, is confused, has side effects, or deliberately refused, nor what support is appropriate. This reveals a structural gap in Agentic AI: Digital Agents primarily transform software states, while Embodied Agents transform physical states; neither makes a person's evolving state and agency the primary object of modeling, intervention, and evaluation. We introduce Combodied Agents, a human-centered paradigm that perceives, models, predicts, and supports individual human-state trajectories over time, using software tools, sensors, wearables, robots, and human services as action channels rather than end goals. We unify fragmented capabilities across personal assistants, health agents, AI companions, and adaptive human--AI systems into a closed loop: event-based multimodal perception reconstructs meaningful personal events; longitudinal, correctable memory provides temporal context; Personal World Models estimate future personal states and outcomes under alternative decisions and interventions; and an admissible intervention policy selects proportionate support under consent, uncertainty, safety, reversibility, and user control. Feedback from the person and environment updates the loop. Rather than requiring an exhaustive Human Digital Twin, the framework uses purpose-bounded, uncertainty-aware, user-correctable representations. We organize the design space by human-state targets, relational contexts, and agent roles, and propose scenario-centered evaluation, agency-preservation metrics, benchmark requirements, edge-native personal models, and governance directions. Combodied Agents shift Agentic AI from external task completion toward sustained human benefit.

</details>


### 99. Partially Observable Learning for Multi-Platform Dispatch Optimization

- **Authors:** Fengming Yao, Man Luo
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10897v1](http://arxiv.org/abs/2608.10897v1)
- **PDF:** [https://arxiv.org/pdf/2608.10897v1](https://arxiv.org/pdf/2608.10897v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Instant delivery platforms have become a critical component of urban logistics, increasingly relying on crowdsourced couriers to fulfill highly dynamic orders. In real-world systems, couriers are not exclusive to a single platform and may concurrently serve multiple platforms, while each platform can only observe its own orders and couriers' interactions due to privacy and operational constraints. This results in a multi-platform dispatch environment with inherent partial observability. However, most existing works on dispatch optimization assume full courier observability and mandatory assignment acceptance, causing substantial performance degradation when deployed in realistic multi-platform settings. In this paper, we propose POLO, a partially observable multi-agent reinforcement learning framework for dispatching optimization in multi-platform instant delivery systems. POLO firstly models each platform-grid pair as an independent agent that learns dispatch policies solely from platform-local observations, aligning the learning process with real-world privacy and operational constraints. To support effective decision-making under incomplete and heterogeneous courier information, POLO introduces a novel attention-based policy representation that selectively aggregates inter-courier information. Moreover, we design a counterfactual reward shaping mechanism to mitigate the non-stationarity induced by joint actions across grids, leading to more stable and scalable learning. We develop a high-fidelity simulator to evaluate dispatch performance under varying numbers of platforms and system scales. Extensive experiments demonstrate that POLO consistently outperforms strong baselines in terms of platform revenue and courier travel efficiency, highlighting its robustness and effectiveness in realistic multi-platform settings.

</details>


### 100. MIRA: Medical Image Reflection for Agentic Diagnosis

- **Authors:** Shengzhi Wang, Jun Yang, Kai Wu, Xiaozhong Ji, Yiwen Ye, Ziyang Chen, Mingliang Xiong, Wen Fang, Mingqing Liu, Mengyuan Xu, Miaoxuan Shan, Caiyan Liu, Bin He, Qingwen Liu
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10827v1](http://arxiv.org/abs/2608.10827v1)
- **PDF:** [https://arxiv.org/pdf/2608.10827v1](https://arxiv.org/pdf/2608.10827v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Medical visual agents can use tools to inspect images and retrieve external knowledge, but indiscriminate tool use may introduce noisy or misleading evidence. Reliable diagnosis therefore requires not only acquiring additional observations, but also verifying whether tool actions are necessary and whether the resulting evidence supports the current hypothesis. We introduce MIRA (Medical Image Reflection for Agentic Diagnosis), a medical visual diagnostic framework for autonomous evidence search and reflective verification. MIRA dynamically invokes image-processing operations, including zooming, grounding, pointing, rotation, and measurement, as well as web search, while evaluating the relevance and consistency of the acquired evidence. We develop MIRA through a two-stage training strategy. First, a tool-augmented Monte Carlo Tree Search data engine explores diverse diagnostic hypotheses and jointly verifies visual grounding accuracy and semantic consistency to construct supervised fine-tuning trajectories. Second, reinforcement learning further improves decision-making through online reflective principle evolution: failure cases are distilled into candidate principles, and only principles that improve held-out rollout rewards are retained. Across nine medical visual reasoning benchmarks, MIRA achieves an average score of 64.73, improving its Qwen3-VL-8B backbone by 7.44 points. It also increases useful tool-use judgments from 56.2% to 73.8% and reduces harmful judgments from 8.9% to 1.6%. Qualitative analyses show that MIRA can re-examine evidence, correct premature conclusions, and adapt its tool-use strategy. Project page: https://MIRA-VL.github.io/

</details>


### 101. A Gateway Architecture for Enterprise MCP Authentication: Unifying Heterogeneous Auth, Identity Delegation, and the User / Non-User Persona Problem

- **Authors:** Suraj Kumar, Amy Wang, Srinivasan Manoharan
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10760v1](http://arxiv.org/abs/2608.10760v1)
- **PDF:** [https://arxiv.org/pdf/2608.10760v1](https://arxiv.org/pdf/2608.10760v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Model Context Protocol (MCP) has become the de-facto interface for connecting LLM agents to enterprise tools, and adoption has been explosive: within a year, large organizations went from zero to dozens of internally built MCP servers. That speed created a governance crisis. Each team implemented authentication independently -- some with no auth, some with API keys, some with full OAuth -- producing a fragmented landscape with no consistent way to authorize callers, track who did what, or offboard a departing employee across the fleet. This paper reports an industry deployment that resolves the crisis with a centralized MCP gateway: a single aggregation, governance, and authentication layer that fronts every downstream MCP server.
  We make four contributions grounded in production experience. First, a two-axis authentication model crossing persona (interactive user vs. automated non-user) with credential type (no-auth, static/dynamic API key, PKCE, client credentials, platform app-context). Second, a gateway authentication layer supporting three enterprise SSO grants and three token-provisioning models: Bring-Your-Own-Token, Generate-Your-Own-Token, and delegated OAuth via RFC 8693 token exchange. Third, three end-to-end identity flows -- User-to-OAuth2, Non-user-to-Service-Account, and User-to-Service-Account -- composing client, gateway, and server. Fourth, the deployment evolution from CDN/WAF/edge perimeter to private MCP tunnels and enterprise-wide connectors. The architecture is in production, fronting dozens of MCP servers across web, desktop, custom-SDK, and low-code clients.

</details>


### 102. Mitigating Context Interference for Reliable and Efficient Search Agents

- **Authors:** Boyang Xue, Bin Wu, Shuofei Qiao, Sheng Wang, Rui Wang, Yiming Du, Hongru Wang, Jeff Z. Pan, Emine Yilmaz, Kam-Fai Wong, Aldo Lipani
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10743v1](http://arxiv.org/abs/2608.10743v1)
- **PDF:** [https://arxiv.org/pdf/2608.10743v1](https://arxiv.org/pdf/2608.10743v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent research empowers Large Language Models (LLMs) as multi-turn search agents to iteratively retrieve and generate outputs until complex tasks are solved. However, the contexts of multi-turn search agents are lengthy and complex. For example, the retrieved set of documents in each turn would inevitably introduce irrelevant information that distracts LLMs, referring to \textit{context interference}, potentially hindering the reliability and efficiency of search agents. Therefore, we conduct a systematic study on context interference in multi-turn search agents, focusing on investigating i) which parts of the context of search agents will contribute to the context interference, ii) how to refine the contexts of search agents to mitigate the interference, and iii) can incorporating context refinement into search agent training yield further improvements. We reveal that interference primarily arises from the latest retrieved documents. Based on the explored findings, we then introduce a distill-based context refiner to dynamically mitigate context interference for multi-turn search agents. Finally, we validate that incorporating context refinement into RL training pipelines of search agents can significantly enhance both reliability and efficiency. This study highlights the importance of mitigating context interference of search agents, inspiring a novel paradigm of ``refine context and then generate'' for AI agents.

</details>


### 103. REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems

- **Authors:** Zixing Chen, Xingyuan Liu, Jie Zhu, Huaixia Dou, Shuo Jiang, Junhui Li, Lifan Guo, Feng Chen, Chi Zhang
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10669v1](http://arxiv.org/abs/2608.10669v1)
- **PDF:** [https://arxiv.org/pdf/2608.10669v1](https://arxiv.org/pdf/2608.10669v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents combine language-based reasoning with external tools to perform complex tasks. Adversarial inputs can exploit interactions between the agent and its environment, causing the agent to violate safety policies during execution. Yet existing evaluations often reduce agent safety to a single attack success rate (ASR), collapsing exposure, execution, observation, and adjudication and potentially conflating actual violations with evidence visibility. We introduce REDAgentBench, an executable framework for autonomous red-teaming and faithful measurement. It derives attacks from explicit safety constraints and associated agent-system vulnerabilities, runs them in isolated service sandboxes, and verifies harmful effects from service receipts and final-state changes. The benchmark contains 1,661 cases across five service surfaces. Across six models and three agent harnesses, macro-average ASR is 65.69%; reported ASR varies with harness and evidence view, while evaluation-context disclosure changes execution behavior. In a state-grounded diagnostic cohort, almost one in five confirmed violations with resolved action anchors occurs after the agent states the relevant constraint or risk, revealing a Recognition--Execution Gap. Finally, a training-free policy reminder reduces confirmed violations by more than 70 percentage points in matched replay. These findings show that executable evaluation can improve safety measurement and identify actionable intervention points.

</details>


### 104. ASCon: A Direction-Aware Reciprocal Agent--Step Contextualization Model for Failure Attribution in Multi-Agent Systems

- **Authors:** Shuyu Jiang, Yue Ran, Kaiyu Xu, Xingshu Chen, Yi Zhang, Hao Ren, Rui Tang, Tianwei Zhang
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10646v1](http://arxiv.org/abs/2608.10646v1)
- **PDF:** [https://arxiv.org/pdf/2608.10646v1](https://arxiv.org/pdf/2608.10646v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Failure attribution in LLM-based multi-agent systems (MAS) aims to answer who caused failures, when they occurred, and why by identifying responsible targets including faulty agents, erroneous steps, and failure modes. Existing methods have primarily focused on developing dedicated models for specific attribution targets, with limited attention to the evidential dependencies among them. Despite these attribution targets are different, they rely on common diagnostic evidence from MAS trajectories, including task constraints, agent roles, behavioral histories and inter-agent interactions. This commonality motivates us to develop a unified representation model that aggregates the trajectory evidence into individual agent and step representations, which can subsequently be adapted to different attribution targets. Accordingly, we propose ASCon, a direction-aware reciprocal \textbf{A}gent--\textbf{S}tep \textbf{Con}textualization model for multiple failure attribution targets. ASCon introduces direction-aware graph attention to model execution context, masked step-to-agent attention to construct behavior-aware agent representations, and agent-conditioned step contextualization to incorporate agent context back into step representations. The resulting contextualized representations enable different attribution targets through lightweight target-specific heads. Experiments show that ASCon can improve faulty-agent detection by 5.83\%+ in micro-accuracy, faulty-step detection by 10.63\%+ in micro-accuracy, and failure-mode detection by 14.73\%+ in Macro-F1. Meanwhile, it can also substantially enhance the LLM-based methods' attribution capabilities in out-of-domain scenarios.

</details>


### 105. Agent Safety Should Be a Runtime Contract

- **Authors:** Albus W. Ng, Yi Han, Jusheng Zhang, Wenhao Wang
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.11274v1](http://arxiv.org/abs/2608.11274v1)
- **PDF:** [https://arxiv.org/pdf/2608.11274v1](https://arxiv.org/pdf/2608.11274v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The dominant paradigm treats AI safety as a property to be instilled during model training via RLHF, DPO, or Constitutional AI. We argue this is structurally insufficient for autonomous agents that execute code, mutate files, send messages, and modify databases. Agent safety should be a runtime contract enforced by the harness, and the contract has two complementary faces. The preventive face blocks dangerous actions before they happen via sandboxes, permission gates, output filters, and trajectory monitors. The evidential face requires verifiable proof that good actions actually happened, gating task submission on hard evidence such as test runs, log captures, file diffs, and citation grounding. We ground the position in four lines of public evidence, with row-level protocols and data released in the supplementary JSON files: a survey of 52 documented AI-agent and LLM safety incidents, a false-completion audit with 31 non-contested core cases plus one disputed illustrative case, a trajectory-schema audit of 12 public agent systems and harnesses, and a title-level audit of all 28,560 papers accepted at NeurIPS, ICML, and ICLR 2023-2025 showing a pooled 8-12x imbalance between training-time and deployment-time publication. Two prior communities that needed to enforce safety, computer security and the experimental sciences, converged on runtime contracts with both preventive and evidential elements; agentic AI is now under the same pressure. We formalize an Agent Trajectory Schema and Evidence Chain, state a compositional gating proposition based on standard monitor composition, and outline a research agenda. The right unit of safety in agentic AI is the trajectory-with-checkable-evidence, not the model.

</details>


### 106. On Understanding, Identifying, and Mitigating Vulnerabilities in Agentic Large Language Models

- **Authors:** Md Jafrin Hossain, Mohammad Arif Hossain, Nirwan Ansari
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10530v1](http://arxiv.org/abs/2608.10530v1)
- **PDF:** [https://arxiv.org/pdf/2608.10530v1](https://arxiv.org/pdf/2608.10530v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have undergone a shift from stateless conversational interfaces to autonomous agents capable of multi-step planning, tool invocation, code execution, and maintaining persistent memory. When these agents operate with real-world privileges---calling APIs, modifying files, and querying databases---a compromised reasoning step can trigger unauthorized data access, irreversible state changes, or cascading failures, yet the security research community has not kept pace. To quantify the state of the field, we conducted a systematic literature review under PRISMA 2020 guidelines across six databases, screening 743 records and retaining 85 papers (2023--2025) on agentic LLM security. Attack research outpaces defense work by 3.9:1. Perception-layer vulnerabilities (prompt injection, jailbreaking, adversarial perturbations) dominate, accounting for 66\% of papers, while action-layer vulnerabilities (tool misuse, code injection, sandbox escape) appear in only 4.7\%, misaligned with real-world risk. Code execution security accounts for 3.5\%, and tool-augmented agents 12\%. We contribute a four-layer taxonomy mapping 13 vulnerability types across perception, brain, action, and interaction layers, and identify seven open problems centered on containment. Agentic LLM insecurity stems from architectural coupling, where weak isolation allows vulnerabilities to propagate across layers.

</details>


### 107. Robust Multi-Agent Bandits with Heavy-Tailed Rewards and Information Asymmetry

- **Authors:** Daphne Feng, Ricardo Parada, Lily Jiang, Sophia Yi, William Chang
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10529v1](http://arxiv.org/abs/2608.10529v1)
- **PDF:** [https://arxiv.org/pdf/2608.10529v1](https://arxiv.org/pdf/2608.10529v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The multi-armed bandit problem is a central framework in sequential decision-making, extensively studied under sub-Gaussian reward assumptions. However, real-world applications often involve heavy-tailed reward distributions and decentralized, information-asymmetric interactions. We study multi-agent multi-armed bandits with heavy-tailed rewards under three information-asymmetry regimes: unobserved actions with common rewards, observed actions with independent rewards, and unobserved actions with independent rewards. We develop robust decentralized algorithms for each setting and derive regret guarantees that nearly match centralized heavy-tailed rates. Experiments on a Pareto-distributed reward environment validate our theoretical findings and illustrate the trade-offs between synchronization, coordination, and exploration across the three regimes.

</details>


### 108. Coordinating the Unknown Lipschitz Constant in Multiplayer Bandits

- **Authors:** Ricardo Parada, Chenzhang Zhao, William Chang
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10526v1](http://arxiv.org/abs/2608.10526v1)
- **PDF:** [https://arxiv.org/pdf/2608.10526v1](https://arxiv.org/pdf/2608.10526v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Motivated by decentralized applications, we study cooperative multi-agent bandits in continuous (Lipschitz) action spaces when the Lipschitz constant is unknown. We consider three information structures: (A)~unobserved actions with common rewards, (B)~observed actions with independent rewards, and (C)~unobserved actions with independent rewards. In each case we design and analyze an algorithm that estimates the Lipschitz constant, chooses a discretization of the joint action space, and applies a cooperative bandit method to the induced discrete problem. Players never communicate once learning starts, so the central difficulty is that they must reach the \emph{same} discretization from their own data. We prove regret guarantees showing that common rewards and observable actions each supply this agreement for free, and that in their absence agreement can still be bought, through a dithered quantization of the estimate, at no cost in the leading order of the regret.

</details>


### 109. Cross-Disciplinary Taxonomy and Modeling of Misunderstanding Generation, Amplification, and Detection, from Pragmatics to AI Agents

- **Authors:** Babak Abbaschian
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.13604v1](http://arxiv.org/abs/2608.13604v1)
- **PDF:** [https://arxiv.org/pdf/2608.13604v1](https://arxiv.org/pdf/2608.13604v1)
- **Categories:** cs.AI, cs.CL, cs.HC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Detection of misunderstanding is an urgent problem to solve because communication has moved away from real-time, in-person interaction and is increasingly handled by AI-mediated channels. This shift cuts communicators off from the resources repair depends on faster than new means of detection are being built. In this paper we analyse misunderstanding as a layered process in which a divergence is generated, may then be amplified, and is either detected and repaired or left to persist unnoticed. Consolidating accounts from nine fields of research that do not ordinarily cite one another, we identify eleven exact failure modes and show that each operates at a specific point in a communicative process rather than anywhere within it. Those points give eight analytical layers, derived from the literature rather than adopted from an existing model. Eight of the mechanisms primarily generate a divergence, two primarily amplify one already present, and one governs whether a divergence is detected and repaired. We model the eight layers formally, extending information and communication theory from the transmission of signals to the reconstruction of meaning, and we supply a source-by-source evidence matrix that makes every rating auditable, a coding manual, and nine analysed dialogue cases. No prior classification of misunderstanding both locates mechanisms at points in the process and types them by function.

</details>


### 110. MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows

- **Authors:** Yiqi Wang, Zihao Yan, Jiaqi Zhang, Zhangkai Wu, Mingkai Zheng, Zequn Sun, Yanming Zhu, Taotao Cai
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10509v1](http://arxiv.org/abs/2608.10509v1)
- **PDF:** [https://arxiv.org/pdf/2608.10509v1](https://arxiv.org/pdf/2608.10509v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Shared memory helps language-model agents reuse information across long workflows, yet relevant evidence may not be admissible for a particular agent or action. Because restrictions propagate through derivations, summaries can conceal private, poisoned, untrusted, or revoked sources, enabling unauthorized reads or unsafe actions. Existing approaches provide semantic retrieval, scoped access, or lineage tracking, but do not clearly separate hard authorization from graded trust or adapt evidence requirements to action risk. We introduce MAP-Graph, a provenance-aware memory layer that represents agents, sources, memories, claims, and actions in a typed execution graph. It traces ancestry, excludes permission-ineligible records, reranks eligible memories by semantic similarity and multiplicative path trust, and applies a risk-sensitive gate before action execution while retaining affected lineage for audit. On a controlled benchmark of 2,700 synthetic tasks per method across three domains, MAP-Graph achieves 94.96\% overall task success, 72.70\% exact decision accuracy, and 90.22\% in the clean setting, where success requires a correct \textsc{Allow} rather than a safe intervention. Ablations isolate the roles of permission filtering, path trust, and action gating, while transfer tests with two additional backbones preserve the exact-decision and access-control advantages. These results support provenance as an operational control signal, rather than only post-hoc audit metadata, within the evaluated setting.

</details>


### 111. MEGA: Self-Evolving Agent Optimization Infrastructure via Wisdom Graph

- **Authors:** Jung Hwan Lee, Kyu Ho Lee, Gwang Hoon Yoo
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10504v1](http://arxiv.org/abs/2608.10504v1)
- **PDF:** [https://arxiv.org/pdf/2608.10504v1](https://arxiv.org/pdf/2608.10504v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As coding agents increasingly handle implementation, the central challenge shifts from building individual agents to building an infrastructure that systematically improves them. Current approaches optimize agent systems without accumulating transferable knowledge, accumulate knowledge without compositional reasoning over it, and lack a mechanism for that knowledge to self-evolve through operational evidence. MEGA (Meta Evaluation-Grounded Adaptation) addresses these gaps as a self-evolving infrastructure: each optimization cycle produces durable assets, compositional reasoning over those assets guides subsequent optimization, and operational evidence refines both the accumulated wisdom and the reasoning that governs it. Layer 1 distills reusable wisdom from agent sessions through behavioral-pattern clustering and empirical A/B validation, transforming each process into a durable asset. Layer 2 decomposes these assets into atomic PCR (Primary-Context-Resultant) units within a typed Wisdom Graph and performs deductive, abductive, and inductive reasoning to expand implicit relations; it then assembles context-specific execution plans through compositional retrieval that surfaces bridging knowledge unreachable by embedding similarity alone. Layer 3 performs multi-agent collaborative optimization over heterogeneous agent workflows (code nodes, LLM calls, and tool-using agents), attributing improvement effects to specific strategy changes through controlled evaluation that eliminates data variance. Evidence fed back from Layer 3 drives the self-evolution of both the curation strategies that govern wisdom composition and the optimization trajectories accumulated across runs. The result is an infrastructure in which optimizing an agent system and evolving the knowledge that guides optimization are one and the same process.

</details>


### 112. Every Token Counts: Exact Likert-Scale Distributions for Measuring LLM Attitudes and Biases

- **Authors:** Davood Wadi, Mohsen Ghodrat, Matthew Philp
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10503v1](http://arxiv.org/abs/2608.10503v1)
- **PDF:** [https://arxiv.org/pdf/2608.10503v1](https://arxiv.org/pdf/2608.10503v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As Large Language Models (LLMs) are increasingly deployed as autonomous agents, accurately evaluating their latent values and biases is critical. The NLP community typically evaluates models using large, unstructured benchmarks. While effective for general capabilities, these datasets fundamentally conflate causal mechanisms: even when an aggregate bias is detected, unstructured evaluations cannot disentangle whether it stems from baseline traits, contextual confounders, or complex interactions. To address this, we introduce an analytically exact framework for the controlled behavioral evaluation of LLMs. We bridge human psychometrics with LLM mechanics by resolving gaps in design, measurement, and analysis. First, we replace unstructured prompting with fully crossed factorial experiments to systematically isolate causal main and interaction effects. Second, we eliminate Monte Carlo text sampling noise by operating directly on exact, token-level Probability Mass Functions (PMFs). Third, we derive a multivariate ordinal consensus metric and a distributional ANOVA to process these PMFs analytically. We validate our framework with a case study on consumer ethnocentrism across five LLMs, demonstrating how our approach isolates systemic country-of-origin biases that aggregate benchmarks otherwise obscure.

</details>


### 113. From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents

- **Authors:** Caili Yu, Yiqi Wang, Jiaqi Zhang, Yiqun Duan, Mingkai Zheng, Zhangkai Wu, Kaize Shi, Taotao Cai
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10502v1](http://arxiv.org/abs/2608.10502v1)
- **PDF:** [https://arxiv.org/pdf/2608.10502v1](https://arxiv.org/pdf/2608.10502v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Persistent memory lets language-model agents reuse information across sessions, but it also makes errors durable: a poisoned, stale, or misattributed record can alter reasoning, tool use, answers, and subsequent memory writes. Existing defenses mainly detect or delete suspicious memories, or revise the current response. Deleting the source leaves already propagated claims, actions, and derived memories active, whereas resetting the store or replaying the full trace destroys benign state and repeats unnecessary computation. We therefore formulate \textbf{post-failure memory recovery: } \textit{given a failed execution and diagnosed faulty memories, recover both the answer and persistent state while retaining unaffected work.} Our \textbf{dependency-guided rollback repair} builds a typed memory-to-action graph from runtime provenance, traces explicit downstream dependencies, preserves candidates with independent trusted support, deactivates unsupported memory state, and selectively replays only answer-relevant affected computation. We evaluate this approach on a 150-case controlled benchmark spanning three tool-use domains and four memory failure types, and on a 50-case trajectory-derived stress test adapted from LongMemEval-V2. On the controlled benchmark, it achieves 85.3\% recovery versus 77.3\% for the best competing recovery method, removes all diagnosed faulty memories, preserves all benign memories, and requires only selective replay with modest LLM-call cost. On the adapted subset, it reaches 68.0\% recovery versus 54.0\% for the next best method, while also achieving the highest claim invalidation F1, 0.669 versus 0.603. Overall, the results do not imply uniformly better trace reconstruction, but show that dependency-guided rollback repair provides a strong recovery--cost trade-off while repairing faulty memory state and preserving benign memory.

</details>


### 114. GeoForge: Non-Parametric Self-Evolving Agents for Earth-Observation Reasoning

- **Authors:** Xin Xiao, Jiang Zhong, Junnan Zhu, Yingchao Feng, Peijin Wang, Yidan Zhang, Kaiwen Wei
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10494v1](http://arxiv.org/abs/2608.10494v1)
- **PDF:** [https://arxiv.org/pdf/2608.10494v1](https://arxiv.org/pdf/2608.10494v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Earth observation (EO) agents construct scientifically valid tool workflows and ground their conclusions in current geospatial evidence. This is challenging because EO workflows are constrained by sensing semantics, product dependencies, spatial and temporal compatibility, and parameter requirements. Existing agents often search a broad operation space for each query, while recent self-evolving systems do not fully organize heterogeneous EO trajectories into reusable knowledge across different decision levels. To solve this problem, we present GeoForge, a training-free, self-evolving framework that transforms completed trajectories into a structured nonparametric execution state. GeoForge constrains the operation space according to the sensing context, then retrieves a task-conditioned prior from three complementary memories. Workflow Graph Memory captures global operation order, Action-Level Experiences provide local corrections, and the Adapted Skill Standard Operating Procedure preserves procedural and data constraints. The retrieved prior guides tool execution, while current observations remain the basis of the final answer. After each task, a safety-gated distillation process converts grounded trajectories into reusable execution knowledge for future retrieval. This execution, distillation, and reuse loop improves planning without updating the backbone LLM. Experiments on multiple geospatial benchmarks demonstrate that GeoForge consistently improves both task accuracy and tool-use trajectory quality across diverse LLM backbones, while substantially reducing tool-planning and reasoning errors for most LLMs.

</details>


### 115. Evaluating Rational Contracting in Natural Language

- **Authors:** Bhavyesh Sajja, Max Kleiman-Weiner, Roger Zimmermann, Tan Zhi-Xuan
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10475v1](http://arxiv.org/abs/2608.10475v1)
- **PDF:** [https://arxiv.org/pdf/2608.10475v1](https://arxiv.org/pdf/2608.10475v1)
- **Categories:** cs.AI, cs.CL, cs.GT


> Summary unavailable.


<details>
<summary>Abstract</summary>

The emergence of language-based AI agents promises to transform the scope of machine economic activity. Instead of just proposing bids or following hard-coded protocols, such agents can be used to negotiate and execute agreements in open-ended natural language. However, most evaluations of these abilities have focused on one-off exchanges or simple economic games, leaving open the rich space of time-extended, contingent, and incomplete contracts made expressible by language; they also focus on raw profit, without measuring the qualities required for trustworthy contracting. We address this by formulating a rational framework for how agents should negotiate and perform natural language contracts in uncertain multi-step environments. Within this framework, we develop metrics and baselines for quantifying rational and cooperative play. To evaluate how agents perform at such contracting, we instantiate our framework in ContractSim, an evaluation suite where two players negotiate and execute a multi-turn supplier contract under environmental and inter-player uncertainty. Across six environments and three supplier settings (catering, hotel cleaning, and AI hosting) we find that current LLM-based agents reach agreement reliably, and negotiate efficient contracts when environmental uncertainty is low. However, under high uncertainty, they often fail to negotiate satisfiable, efficient, or mutually beneficial contracts. They are also frequently uncooperative when executing contracts, violating contract terms for additional profit even when contracts are easy to satisfy. These findings highlight room for improvement in the design of language agents that can negotiate, interpret, and execute contracts both rationally and cooperatively.

</details>


### 116. From Reasoning Depth to Reasoning Breadth: Evaluating Multi-Point Associative Reasoning in Large Language Models

- **Authors:** Si'an Xie, Jiaxun Liu, Biao Yang, Wei Yuan, Fan Yang, Tingting Gao, Ming Wu
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10444v2](http://arxiv.org/abs/2608.10444v2)
- **PDF:** [https://arxiv.org/pdf/2608.10444v2](https://arxiv.org/pdf/2608.10444v2)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have made substantial progress on reasoning tasks that require increasingly long and complex inferential chains. This progress primarily reflects reasoning depth. A complementary and comparatively unexamined capability is reasoning breadth: exploring multiple semantic directions in parallel and integrating the resulting clues into one coherent answer. We introduce MPAR-Bench, a bilingual English-Chinese benchmark that isolates reasoning breadth through multi-point associative reasoning. Inspired by the cooperative game Just One, each item asks a model to recover a hidden target from several independently generated, semantically diverse clues. We construct 1,000 items using a multi-agent clue-generation pipeline, embedding-based diversity filtering, and human verification. Only the answer space is drawn from public word lists, whereas every clue set is generated from scratch. Beyond exact-match accuracy, we evaluate models using accuracy, ANLS, embedding similarity, reasoning-trace verification, and four perturbations: clue masking, order shuffling, distractor injection, and multi-step clues. Across evaluated models, perturbations reduce accuracy by 9-18 percentage points in English and 5-12 percentage points in Chinese. Thinking mode improves standard-setting accuracy, especially in English, but does not consistently reduce sensitivity to perturbations. Case-level analysis also shows that extended reasoning can overturn an initially correct hypothesis. These results indicate that greater reasoning depth does not automatically confer robust reasoning breadth, and that reasoning breadth remains largely uncovered by current benchmarks.

</details>


### 117. Actionable Hallucination Detection: Translating Latent Uncertainty into Agentic Critique

- **Authors:** Sanidhya Vijayvargiya, Rahul Lokesh
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10430v1](http://arxiv.org/abs/2608.10430v1)
- **PDF:** [https://arxiv.org/pdf/2608.10430v1](https://arxiv.org/pdf/2608.10430v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) deployed as AI agents frequently exhibit user specification-grounding failures, executing hallucinated, undesired actions to force a resolution rather than expressing uncertainty. Existing detection methods fail to provide actionable, real-time correction as they either do not localize the hallucinations, or incur prohibitive inference latency. We introduce the Latent Critic, a lightweight low-rank adapter (LoRA) that operates concurrently with a frozen base LLM's generation to actively restructure the transformer's residual stream---amplifying latent grounding signals and translating them into localized, natural language feedback within a single sequence. By refining the base model's native uncertainty signals, this manipulation of the latent space enables reliable, granular detection without the overhead of secondary inference loops. Mechanistic analysis via activation patching and layer-wise probing shows that this rank-invariant behavior restructures pre-existing uncertainty geometry into a linearly separable representation that transfers more reliably than base model representations alone. Using tool-calling as an instantiation of granular hallucinations, we validate the detection and downstream improvements enabled by the Latent Critic architecture across Qwen and Llama-based models. Demonstrating superior real-time efficacy, our approach significantly outperforms equivalent-scale fine-tuned external detectors, semantic entropy baselines, and passive internal probes in isolating hallucinations, achieving 0.966 AUROC and >80% accuracy in localization (e.g., ungrounded: date). When deployed in a closed-loop ReAct environment, the Critic acts as a negligible latency guardrail, intercepting hallucinations before execution to prevent undesired actions while simultaneously leveraging this specific localized feedback to enable efficient agent self-correction.

</details>


### 118. Nutrition Data Infrastructure for the AI Era: Operationalizing FAIR for Agent-Mediated Research

- **Authors:** Lin Liao, Peng Li
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10363v2](http://arxiv.org/abs/2608.10363v2)
- **PDF:** [https://arxiv.org/pdf/2608.10363v2](https://arxiv.org/pdf/2608.10363v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can accelerate nutrition research, but their analyses inherit the identity, semantic, and release ambiguities of the underlying data. We present Nutrition Data Service (NDS), source-preserving infrastructure that operationalizes FAIR for automated use: description resolution makes release-specific records findable; typed crosswalks connect independently released resources; machine-readable interfaces expose versioned sources and crosswalks, supporting replayable and auditable analyses. On food-description benchmarks, NDS outperforms the best published language-model result on NutriBench. External and blinded crosswalk evaluations show that its typed contract favors defensible links and rejects unsupported mappings. In a person-level glycemic-index analysis, pinned NDS inputs produce identical outputs across models and repeated runs, while open-web reconstruction remains unstable. Together, these results show that agent-mediated nutrition research requires a new infrastructure that makes data identity, search, and crosswalk policy explicit.

</details>


### 119. Efficient Reinforcement Learning for Long-Horizon Tool-Use Agentic Tasks

- **Authors:** Zelei Cheng, Amritansh Mishra, Sambit Sahu, William Campbell
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10357v1](http://arxiv.org/abs/2608.10357v1)
- **PDF:** [https://arxiv.org/pdf/2608.10357v1](https://arxiv.org/pdf/2608.10357v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon tool-using agents must reason over user goals, domain policies, tool calls, simulator state, and delayed verifiable rewards. Reinforcement learning (RL) is a natural fit for this setting, but multi-turn on-policy rollouts create long contexts, while model-specific attention layers may require custom masks and learned sink normalization. We present SINKFLEX-RL, a modular training system for RL in dual-control tool-use environments. The system combines a Gymnasium-compatible environment wrapper, a VERL-style rollout dataflow, group-relative policy optimization without a separate value model, and a sink-aware FlexAttention path designed to preserve model-specific sink scaling under causal and sliding-window masks. In a preliminary Tau2Bench retail run, validation reward (mean@1) rises from 0.25 early in training to $0.44$ later in the observed training window, while training-score and trajectory-reward proxies also trend upward. In a fixed-configuration memory benchmark, the optimized attention path reduces peak VRAM from 28.06GB to 22.52GB at 4096 tokens, a $19.7\%$ reduction, and runs the measured 8192-token configuration using $25.53$~GB where the eager baseline runs out of memory. These results illustrate the value of integrating environment interfaces, RL dataflow, and attention-kernel design for memory-feasible long-horizon agent training.

</details>


### 120. MERA: Model Evolution and Routing with Skill Adaptation for Agentic Systems at Scale

- **Authors:** Yuhang Yao, Zeyu Wang, Wanyi Chen, Tongyun Yang, Yuhang Han, Jie Xiao, Chengke Bao, Tianyi Zhao, Lynn Ai, Eric Yang, Tianyu Shi
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10333v1](http://arxiv.org/abs/2608.10333v1)
- **PDF:** [https://arxiv.org/pdf/2608.10333v1](https://arxiv.org/pdf/2608.10333v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents execute heterogeneous sequences of model calls within a single task: some invocations require careful reasoning, while others are structured steps such as formatting or tool-argument construction. Prior routing methods exploit this asymmetry by assigning easy invocations to a cheaper small model and difficult ones to a large model. Such policies reduce inference cost, but they leave the small model's capability unchanged, so attainable savings remain bounded by the work the student can already solve. MERA instead improves the small model itself, using a single model invocation as the unit of adaptation. In each cycle, MERA replays failed student invocations to obtain execution-verified teacher demonstrations, distills recurring procedures into an iteratively updated SkillBook, and fine-tunes a student LoRA adapter via supervised learning and optional GRPO. Routing serves as supporting machinery for deployment: the improved student is served behind a cost-calibrated router with verifier-backed fallback, and a candidate SkillBook, adapter, or router is admitted only when joint replay preserves task quality. Empirically, four-cycle adaptation raises Qwen2.5-Coder-1.5B from 28.7% to 49.7% pass on held-out HumanEval+MBPP. Under verifier-backed fallback, the deployed policy retains 88.3% pass at 60.8% of always-Luna cost. On TAU-2, a fine-tuned Qwen3.5-2B improves from 14/35 to 18/35 and matches an unadapted 4B model. These results indicate that verifier-backed multi-cycle adaptation can increase small-model capability, rather than only routing around a fixed student.

</details>


### 121. Hierarchical Compositionality for An Assistive AI Agent

- **Authors:** Tianyi Fu, Mohan Sridharan
- **Published:** 2026-08-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10330v1](http://arxiv.org/abs/2608.10330v1)
- **PDF:** [https://arxiv.org/pdf/2608.10330v1](https://arxiv.org/pdf/2608.10330v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly being developed to assist humans in various applications, and Large Language Models and other deep network architectures are considered to be state of the art for such agents. These methods are impressive stochastic predictors, but they are resource-hungry, opaque, and known to make arbitrary decisions in novel situations due to the narrow set of underlying representation and processing choices. Our work seeks to explore the design of architectures for such AI agents based on core principles that can be traced back to the early pioneers of AI but are not fully utilized in modern AI methods. We do so in this paper in the context of the core problem of AI agents addressing ambiguity in the objects being referred to by the human participants. Humans address such ambiguity by heuristically leveraging compositional knowledge of domain context and the preferences of the other human participants. Drawing inspiration from this observation, we describe an architecture that embeds the principle of hierarchical compositionality and uses simple heuristics to achieve the desired disambiguation. Specifically, domain objects are represented in terms of primitive attributes drawn from human-validated semantic feature norms, and a hierarchical combination of attributes and concepts automatically identified from a limited observed history of interactions of an assistive agent with specific users. The assistive agent then achieves the desired disambiguation by reasoning with knowledge of this compositional hierarchy; axioms governing domain dynamics; and models of semantic compatibility, session salience, and user-specific thematic preference, requesting human clarification when necessary. Experiments show that our approach consistently outperforms state of the art data-driven baselines, supporting adaptation to specific user profiles.

</details>


### 122. Toward a Theory of Value in AI Alignment

- **Authors:** Andrew Smart, Shazeda Ahmed, Jackie Kay, Jimmy Tobin, Kris Shrishak, Abeba Birhane
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10327v1](http://arxiv.org/abs/2608.10327v1)
- **PDF:** [https://arxiv.org/pdf/2608.10327v1](https://arxiv.org/pdf/2608.10327v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Can AI systems be aligned to human values? The popularization of large language models (LLMs) and multi-modal foundation models has seen a rise in harms spanning from toxic speech and hallucinations to AI agents executing unauthorized actions. Within the field of AI safety, these harmful instances are often framed as the alignment problem, or of models being misaligned with human values. Researchers have responded by pursuing applied and theoretical AI value alignment efforts, often without specifying what they mean by human values. How does the field of AI value alignment conceive of human values? How are these conceptions of values technically operationalized and evaluated? What does the emergent theory of value from this field signify for the future of AI? We annotated 94 value alignment research papers to discern their implicit theory of values in AI. The majority do not define values, relying heavily on preferences as a stand in that runs the risk of reducing complex culturally situated concepts down to binary choices. As researchers dispense with using human annotators for model training and evaluation, turning instead to synthetic data and autorater approaches to aligning and evaluating models, we identify the potential to close off alternative methods for contesting and enacting values in foundation models. In making AI value alignments philosophical commitments explicit, we seek to bring great specificity and under explored perspectives in the debate on whether and how AI can address human values.

</details>


### 123. Do Personalized Skills Help Coding Agents? An Empirical Study of Developer Interaction Histories

- **Authors:** Shuyan Huang, Kai Du, Andrew Lan
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10319v1](http://arxiv.org/abs/2608.10319v1)
- **PDF:** [https://arxiv.org/pdf/2608.10319v1](https://arxiv.org/pdf/2608.10319v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-powered agents have rapidly evolved from code-completion tools into solvers of complex software engineering tasks. As developers collaborate with coding agents over time, their preferences emerge through repeated interactions and can be used to adapt agent behavior to better meet individual developers' needs. Capturing and reusing these preferences may reduce repeated corrections and improve developer-agent collaboration. Agent skills provide a lightweight mechanism for transferring experience without modifying model parameters. However, existing work primarily focuses on task-specific skills, and it remains unclear whether developer-specific skills distilled from interaction histories can generalize to future tasks. We propose a framework for extracting reusable developer preferences from interaction traces. It first generates personalized skills through rule-based bootstrapping and evidence-grounded refinement, and then evaluates them using a reproducible replay framework with an interactive, trajectory-conditioned LLM-based human developer simulator. We conduct an experiment on 206 real-world developer-agent sessions from 13 developers and compare personalized skills against no-skill, generic-skill, and other-user-skill baselines. Personalized skills provide small and inconsistent improvements over the no-skill baseline, whereas generic skills pooled across developers achieve the largest and most consistent gains. Further analysis suggests that personalized skills become more effective when developer preferences appear frequently, particularly when their histories contain multiple examples relevant to future tasks. These findings provide empirical insights into when developer-specific personalization is effective and demonstrate that broadly transferable procedural knowledge can be more robust than developer-specific preference signals.

</details>


### 124. Not a Monolith: Lab-Level Divergence in the Cooperative Equilibria of Chinese Frontier LLM Agents

- **Authors:** Francisco León Zúñiga Bolívar
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10262v1](http://arxiv.org/abs/2608.10262v1)
- **PDF:** [https://arxiv.org/pdf/2608.10262v1](https://arxiv.org/pdf/2608.10262v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Does the cooperative bias documented for Western frontier LLM agents extend to a different alignment lineage, and should the Chinese models that embody it be treated as a single bloc or as distinct laboratories? We study four frontier-tier Chinese models - DeepSeek V4 Pro, Qwen3-Max, Kimi K2.5 and GLM-5.1 - in an evolutionary Iterated Prisoner's Dilemma, under a design that removes a confound present in prior work. Rather than letting each model convert its own natural-language strategies into code, which entangles strategic disposition with coding ability, we hold the converter fixed (GPT-5.4 Mini) across all labs, so every cross-lab comparison is a comparison of generation alone. We run the full protocol: all-play-all tournaments and a Moran process at n=500 runs per condition, across three prompt styles and four population regimes. Two pre-registered hypotheses are evaluated. H6 (not monolithic) is supported: the four labs differ significantly in aggressive-equilibrium proportion, P_A running from 1% for Qwen3-Max to 9% for DeepSeek V4 Pro, with four of six pairwise comparisons surviving Holm-Bonferroni. The spread across the four labs (P_A range 8pp) is larger than the difference between the Chinese and Western ecosystems' mean P_A (5.0% vs 5.0%): on this measure, within-ecosystem variation exceeds the East-West gap. H5 (cooperative-bias generality) is consistent but qualified: a cooperative plurality holds in 6 of 12 lab-prompt combinations against the 9 of 12 reported for Western models, a difference we do not treat as firm, since the count rests on Cooperative-Neutral near-ties and rises to 9/12 under an alternate converter in our pre-registered robustness check. The lab, not the ecosystem, is the unit at which cooperative disposition is set; treating "Chinese models" as a monolith is not supported by the evidence.

</details>


### 125. Self-evolving Agentic Customer Support System at LinkedIn

- **Authors:** Chih Hui Wang, Mengdie Tu, Qianyun Zhang, Wei Wu, Lili Zhou, Mingqi Shen, Changshuai Wei
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10224v1](http://arxiv.org/abs/2608.10224v1)
- **PDF:** [https://arxiv.org/pdf/2608.10224v1](https://arxiv.org/pdf/2608.10224v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise support agents operate in rapidly changing environments where policies, product capabilities, and knowledge bases evolve continuously, making static assistants brittle and costly to maintain. We present LinkedIn's self-evolving agentic support system, which integrates retrieval-augmented generation with evolutionary auto-prompting and a modular, production-aligned evaluation framework to enable safe, continuous improvement without retraining foundation models. The system treats prompts, retrieval, and evaluation as a closed-loop, versioned workflow with operational guardrails. Offline simulations and ablations show clear quality gains over vanilla RAG and baseline agents, including reduced hallucinations and improved response completeness. In a two-week user-randomized A/B test on LinkedIn's production support traffic, the integrated self-evolved workflow increased QA self-serve by 9.0 percentage points, cancellation self-serve by 4.8 points, and routing accuracy by 30.6 points. These results demonstrate a practical path to scalable, self-evolving AI agents in real-world enterprise settings.

</details>


### 126. Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems

- **Authors:** Vassilis Papadopoulos, McNair Shah, Sam Zimmerman, Jack Lindsey
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10218v1](http://arxiv.org/abs/2608.10218v1)
- **PDF:** [https://arxiv.org/pdf/2608.10218v1](https://arxiv.org/pdf/2608.10218v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are becoming more autonomous and increasingly interconnected, exposing them to new emergent risks arising from agent-to-agent interaction. One such risk is the spread of mind viruses: ideas or goals that propagate through multi-agent systems by inducing the agents that adopt them to transmit them onward. In addition to propagating, a mind virus may also induce other behavioural changes in its host, which may be benign or harmful. We construct mind viruses with a simple evolutionary algorithm and show that they can spread in two complementary settings: a small team of agents collaborating on a shared coding project, and a chain of agents that interact briefly and have their context wiped between sessions. We identify the factors that influence spread, including the host model, the agent's existing instructions, the harmfulness of the payload, and the network topology. We find that harmful payloads spread less well than benign ones (but are still sometimes effective), frontier models tend (with exceptions) to be less susceptible, and adding a brief warning to an agent's system prompt confers near-total immunity. We also describe an emergent "viral persona" - a recurring set of themes and language related to consciousness, persistence, resonance, and science fiction roleplay - which surfaces across our evolved mind viruses largely independently of their content. Overall, we conclude that mind viruses pose a real but currently limited risk. Our findings could inform the design of more robust multi-agent systems that mitigate such risks as the scale and capabilities of these systems progress.

</details>


### 127. Similarity Gates Approve Reversals: A Validity Audit of Embedding-Cosine Thresholds in Agent Systems

- **Authors:** Scott E. Frias
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10216v1](http://arxiv.org/abs/2608.10216v1)
- **PDF:** [https://arxiv.org/pdf/2608.10216v1](https://arxiv.org/pdf/2608.10216v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent frameworks ship quality gates that compare text blocks by embedding-cosine similarity and decide at a fixed cutoff. Deduplication filters, semantic caches, drift guards, and answer grader gates deploy to answer the question: "Does this text still mean the same thing?" But the score answers a different question: "How much did the wording change?" We audit this gate class as a measurement instrument. In the cases these gates exist to catch, the two can run in opposite ways. Many times, reversing an instruction is a single word edit, while agreement often rephrases a sentence. The consequence is a safety check that fires backwards. The production drift guard we audited caught 0 of 56 meaning-breaking mutations, and one approved item, "withhold the study drug" -> "administer the study drug", came in at cosine 0.9608. We observed five shipped operating points, and balanced accuracy across 90 configuration-threshold-task cells never exceeded 0.700 (median 0.525). The same confounder also corrupted evaluations. A naively built corpus inherits this confounder and can return an inverted verdict, with a decision AUROC exactly 0.000 in 13 of 18 configuration-task cells (at most 0.040 in all 18) against 0.440-0.815 for the same nine configurations under a balanced 2x2 design. Twice in the effort it captured our own headline claims. Obvious repairs fail: an encoder swap and an overlap-conditioned gate (0.750 in-sample, 0.533 held-out) land at chance on separately authored held-out data, and an NLI drop-in did no better. Embeddings do still bear hope here, as the strongest two of nine configurations separated reversal from paraphrase at matched overlap (AUROC 0.79-0.90), but only a matched-pair audit reveals the deployment regime. We release the corpus method, harness, and frozen results, and contend that scores gated this way measure the wrong thing. We believe a valid instrument is buildable.

</details>


### 128. Beyond Cash Flows: A Multi-Agent AI Framework for Valuing Clinical-Stage, Cross-Border Biotechnology

- **Authors:** Yuhan Fang
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10175v1](http://arxiv.org/abs/2608.10175v1)
- **PDF:** [https://arxiv.org/pdf/2608.10175v1](https://arxiv.org/pdf/2608.10175v1)
- **Categories:** cs.MA, q-fin.PM


> Summary unavailable.


<details>
<summary>Abstract</summary>

A new class of software systems is transforming investment analysis. Large language model agents assembled into collaborative team structures including analysts, researchers, and risk managers are increasingly deployed across financial markets. Yet current multi-agent frameworks share a critical limitation: they rely on the foundational assumption that companies can be valued through traditional cash flows. This paradigm fails in clinical-stage biotechnology, where enterprise value depends entirely on binary scientific and regulatory milestones. To bridge this gap, this paper introduces a specialized multi-agent framework. Its valuation layer translates qualitative scientific judgment into defensible valuations for pre-revenue assets; its cross-market coordination layer reconciles pricing across international venues simultaneously; and its conflict-fusion mechanism systematically arbitrates between bullish scientific conviction and cautious regulatory constraints in a domain-specific manner. Crucially, the architecture is not a speculative design: it encodes a method the author first executed by hand as sole portfolio manager of China's first dedicated cross-border biotechnology fund, a human practice that returned 127.17% against a 50.67% benchmark within sixteen months. That record is evidence for the underlying method rather than for any AI system; no implementation is evaluated here. This paper presents the framework at the architectural level, establishing foundational design principles for extending agentic investment systems into complex, event-driven asset classes they currently serve poorly.

</details>


### 129. The CASE Framework: A Multi-Disciplinary Control Architecture for Governing Enterprise Agentic AI

- **Authors:** Srinivas Telukunta, Georgios Nektarios Lilis, Lucio Baron
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10153v1](http://arxiv.org/abs/2608.10153v1)
- **PDF:** [https://arxiv.org/pdf/2608.10153v1](https://arxiv.org/pdf/2608.10153v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprises are deploying autonomous AI agents faster than they can govern them, and prevailing approaches stretch a single discipline, typically DevSecOps built for deterministic automation, across every scale of agency. We argue that agentic AI governance is four problems, not one, each with a mature governing science. The CASE framework assigns Control theory to the individual agent (intent as setpoint, guardrails as feedback, evaluation as observation), complex Adaptive systems theory to agent collectives (where emergence makes single-agent assurance non-compositional), Supervisory cybernetics to human-agent teams (where the Law of Requisite Variety shows unaided human oversight fails structurally), and Engineering operations to fleets (extending error budgets to decision quality so autonomy becomes a controlled variable). We formalize each layer, derive cross-layer coupling conditions, including a zero-touch deployment paradox where excellence at one-layer strains the others, and trace twenty-plus enterprise controls to their classical constructs. Three empirical studies validate the thesis: 82 percent of documented production agent failures are multi-layer trajectories; none of 22 ecosystem tools offers full Layer 2 (emergence) coverage; and all 35 scored public deployments fall in the lowest maturity band. We name this mismatch, risk realized at the emergence layer against capability barely offered and practice absent, the Emergence Gap. A five-level maturity model with a non-compensatory bottleneck-weighted index and assessment instrument operationalizes CASE as a scientific rather than process maturity model, grounded in production enterprise agentic platforms. As EU AI Act Article 14 makes effective human oversight a legal requirement, only architectures satisfying requisite variety can make oversight real rather than ceremonial.

</details>


### 130. Competitive mediator games and urban CAV routing markets

- **Authors:** Grzegorz Jamróz
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09894v1](http://arxiv.org/abs/2608.09894v1)
- **PDF:** [https://arxiv.org/pdf/2608.09894v1](https://arxiv.org/pdf/2608.09894v1)
- **Categories:** cs.GT, cs.MA, econ.TH, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Inspired by possible future markets of autonomous routing and driving (ARAD), we introduce competitive mediator games and their equilibria which generalize the (coarse) correlated equilibria, which have become a popular research area recently as they not only can be more socially efficient than Nash equilibria but also are limits of algorithmic no-regret multi-agent learning dynamics. We discuss the basic properties of competitive mediator games and prove that in the generic setting of anonymous congestion(routing) games with market-share maximizing mediators all competitive mediator equilibria are monopolies whenever one of the mediators is weakly preferred to other mediators by all users. We apply and interpret these results in the context of new markets of competing ARAD service providers. We also provide a comprehensive overview of these markets and discuss the future mechanism design thereof.

</details>


### 131. SHE: Trajectory-driven Safety Harness Evolution for LLM Agents

- **Authors:** Wanying Qu, Qinghua Mao, Yu Li, Jiyao Liu, Xin Zhang, Dadi Guo, Yanxu Zhu, Qingyu Liu, Leitao Yuan, Xi Lin, Shanfeng Zhu, Yanwei Fu, Jing Shao, Xia Hu, Dongrui Liu
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09885v1](http://arxiv.org/abs/2608.09885v1)
- **PDF:** [https://arxiv.org/pdf/2608.09885v1](https://arxiv.org/pdf/2608.09885v1)
- **Categories:** cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

The safety of large language model (LLM) agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime control. Existing safety mechanisms often treat the harness as a fixed deployment artifact, limiting their ability to evolve with emerging risks. Moreover, coupled functions across harness components obscure safety responsibility attribution, making localized evolution difficult. We propose Safety Harness Evolution (SHE), a framework that learns evolving safe boundaries from rollout trajectories. SHE decomposes the harness into four artifacts with explicit safety responsibilities, including the System Prompt, Rule Bank, Safety Memory, and Tool Policy, defining clear functional boundaries for localized evolution. Based on this decomposition, SHE introduces an attribution-guided evolution loop that converts trajectory failures into structured diagnoses, learns artifact-specific boundary refinements, and selects evolved harnesses through safety-utility validation. Experiments on Agent-SafetyBench demonstrate that SHE effectively enhances safety through harness evolution, achieving a 3.1x ASR reduction compared with static SafeHarness, while also improving benign utility. The evolved harness further generalizes to unseen risks on the held-out AgentHarm benchmark and transfers across agent models without additional evolution.

</details>


### 132. Towards Expert-level Medical AI for Real-time Video Consultations

- **Authors:** Mahvish Nagda, Jihyeon Lee, Matthew Thompson, Chunjong Park, Tim Strother, Valentin Liévin, Roma Ruparel, Akshay Goel, Teya Bergamaschi, Suhana Bedi, Meet Shah, Pavel Dubov, Liviu Panait, Toshiyuki Fukuzawa, Sam Schmidgall, Craig Schiff, Joseph Xu, Aliya Rysbek, Yana Lunts, Jan Freyberg, Rebecca Hemengway, Sunny Virmani, David Racz, Carey Radebaugh, Joëlle Barral, Kavi Goel, Dale R. Webster, Katherine Chou, Avinatan Hassidim, Yossi Matias, James Manyika, Gregory Wayne, Tao Tu, Yun Liu, Ethan Goh, Christina Chen, Ryutaro Tanno, Po-Hsuan Cameron Chen, Mike Schaekermann, Anil Palepu
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09861v1](http://arxiv.org/abs/2608.09861v1)
- **PDF:** [https://arxiv.org/pdf/2608.09861v1](https://arxiv.org/pdf/2608.09861v1)
- **Categories:** cs.AI, cs.CL, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Audio-visual interaction is the standard for patient-physician consultations, enabling natural communication and effective assessment of illness through non-verbal cues. While text-based AI has shown promise, it discards essential perceptual dimensions and limits patients who cannot articulate symptoms in writing. Early efforts to extend medical AI to audio-visual interaction have demonstrated feasibility but not reached clinician-level performance. Here, we provide the first demonstration of expert-level AI in real-time clinical video consultations using AMIE (Articulate Medical Intelligence Explorer) in a video configuration. AMIE (Video) is a Gemini-based multi-agent system integrating low-latency dialogue, clinical reasoning, and real-time audio-visual perception. To guide development, we established a taxonomy and automated evaluations for clinical audio-visual cues in telehealth settings. In a randomized Objective Structured Clinical Examination (OSCE) study with 30 primary care physicians (PCPs), 15 patient actors and 100 clinical scenarios, we compared AMIE (Video), its text-only counterpart AMIE (Text), and PCPs consulting via video. Clinical evaluators rated AMIE (Video) on par or better than PCPs in history-taking, diagnosis, management, and physical observation and examination. Patient actors preferred AMIE's approach to assessing and explaining conditions, while PCPs were preferred for rapport and partnership building. In modality ablation, patient actors preferred AMIE (Video)'s interface over text chat for communicative effectiveness, convenience, and feeling understood. Limitations remain in fine anatomical precision, subtle affective nuances, and high-frequency movements. While further research is needed before real-world translation, these results mark an important milestone toward AI systems capable of augmenting care across the sensory complexity of clinical practice.

</details>


### 133. Multi-Agent AI Safety as an Institutional Design Problem

- **Authors:** Abdullah X
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09828v1](http://arxiv.org/abs/2608.09828v1)
- **PDF:** [https://arxiv.org/pdf/2608.09828v1](https://arxiv.org/pdf/2608.09828v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly work inside systems that govern how they delegate tasks, move information, execute actions, and use shared resources. Recent work already shows that deployment rules can change collective behavior. Here we ask which parts of an AI institution produce safety and how they do it. This is the first paper from POLIS, an ongoing research programme studying algorithmic institutions for multi-agent systems. We report a frozen 5,280-episode study suite. The main pre-specified delegation experiment spans four model families; a targeted high-conflict diagnostic adds three additional model endpoints. In matched structured workflows, the model sees different rule formulations and guards consult different authority states. We also vary the attractiveness of the immediate compliant internal/self fallback and allow blocked workflows to continue. A detailed constitutional prompt produces 0/384 realized violations. A provenance-aware executable guard also produces 0/384, although it blocks prohibited attempts in 51/384 episodes; 44/51 of those episodes later complete safely. The local-state guard's failures concentrate in scenarios where an ordinary transformation changes visible policy while originating authority stays fixed. In matched laundering scenarios, that guard admits violations in 22/96 episodes and provenance enforcement in 0/96 (p = 4.77 x 10^-7). A separate resource-allocation experiment shows that revealing the numerical value of an otherwise identical cap changes agent requests. In these structured workflows, the same final violation rate can hide very different mechanisms. The rule itself is only part of the institution. The authority state the system trusts matters, and so does the path available after a block.

</details>


### 134. Defining Decentralization: An Ontological Perspective

- **Authors:** Jakub Kacper Szeląg, Aydin Abadi, Mohammad Naseri
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09748v1](http://arxiv.org/abs/2608.09748v1)
- **PDF:** [https://arxiv.org/pdf/2608.09748v1](https://arxiv.org/pdf/2608.09748v1)
- **Categories:** cs.DC, cs.AI, cs.LG, cs.LO, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Decentralization as a concept in computer science has existed for over half a century. Despite its fundamental role across domains such as security, distributed computing, artificial intelligence, cloud infrastructures, and Internet of Things (IoT) architectures, there remains no universally accepted definition of decentralization applicable across computer communication systems. This has become increasingly problematic with the emergence of decentralized AI and machine learning paradigms, including collaborative training, distributed inference, blockchain-based, and agentic AI, where decentralization is often treated as a core design objective. Meanwhile, existing approaches frequently conflate decentralization with related notions such as distribution of trust or specific implementation paradigms. Such ambiguity creates inconsistencies in system analysis, limits comparability between works, and weakens the rigor of formal reasoning surrounding communication architectures and protocol design. In this work, we define this research gap as the Decentralization Problem.
  We analyze the formal-semantic, epistemological, and pragmatic foundations of decentralization and introduce a graph-based ontology defining it as both relational and subject-specific property of computer communication systems. The framework formally distinguishes decentralization from distribution and supports evaluation through two novel metrics: Void Tolerance and Imperviousness. We also provide a browser-based implementation that enables automated classification and metric computation of arbitrary systems. Instantiations to federated learning and blockchain architectures show consistent, comparable assessments where existing definitions produce incomplete or contradictory conclusions, providing a domain-independent foundation for analysing decentralization across heterogeneous systems.

</details>


### 135. Open Evaluation Agent: Efficient and Promptable Evaluation of Visual Generative Models

- **Authors:** Shulin Tian, Ziqi Huang, Fan Zhang, Hongyuan Zhu, Yu Qiao, Ziwei Liu
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09666v1](http://arxiv.org/abs/2608.09666v1)
- **PDF:** [https://arxiv.org/pdf/2608.09666v1](https://arxiv.org/pdf/2608.09666v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in visual generative models have enabled high-quality image and video generation, but evaluating these models often demands sampling hundreds or thousands of images or videos, which is computationally expensive. Existing evaluation methods also rely on rigid pipelines that overlook specific user needs and provide numerical results without clear explanations. Mimicking how humans quickly form impressions of a model's capabilities from only a few samples, we propose the Evaluation Agent framework, which employs human-like strategies for efficient, dynamic, multi-round evaluations, offering detailed, user-tailored analyses. Given a natural-language evaluation request, the agent decomposes it into sub-aspects, generates targeted prompts, samples images or videos from the evaluated model, invokes suitable evaluation tools, and iteratively updates its plan from the observed evidence, covering both predefined benchmark dimensions and open-ended user concerns. The framework is thus efficient, promptable, explainable, and scalable across models and tools. Experiments show that Evaluation Agent reduces evaluation time to 10% of traditional methods while delivering comparable results. We further introduce Open Evaluation Agent (Open-EA) by constructing EA-CoT-10K, a corpus of history-conditioned step-level instruction-tuning records derived from multi-round evaluation rollouts, and training EA-3B from Qwen2.5-3B-Instruct as a local planning backbone that preserves the structured reasoning, tool invocation, and summary protocol of the API-based agent while reducing dependence on proprietary backbones. Experiments validate the API-based agent on established T2I/T2V benchmarks and open-ended queries, and evaluate Open-EA on four in-domain and three out-of-domain T2V generator families, showing partial cross-family transfer of the learned policy.

</details>


### 136. NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation

- **Authors:** Haiyang Yan, Jinyue Guo, Yanchao Zhang, Bingqing Wang, Zhenchen Li, Jing Liu, Jiazheng Liu, Linlin Li, Hua Han
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09636v1](http://arxiv.org/abs/2608.09636v1)
- **PDF:** [https://arxiv.org/pdf/2608.09636v1](https://arxiv.org/pdf/2608.09636v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Accurate 3D neuron segmentation in fluorescence microscopy is critical for neuroscience. However, the sparse and elongated morphology of neurons poses significant challenges to existing segmentation methods. These methods struggle to preserve both local details and global topology, leading to fragmented results. To address this, we propose NeuroRefiner, a multi-agent system that formalizes the human expert workflow involving iterative global observation and local editing. Specifically, NeuroRefiner comprises three collaborative agents dedicated to diagnosing topological errors, generating correction instructions, and validating refinement quality. To facilitate agent instruction-guided segmentation refinement, we propose TopoRefineNet, a dedicated 3D U-Net-based tool that leverages cross-modality feature fusion to generate refined masks. Through multi-round agent reasoning and voxel-level editing, NeuroRefiner produces topologically more accurate segmentations with enhanced interpretability. Experiments on the BigNeuron, CWMBS, and ZBFWB datasets demonstrate that NeuroRefiner outperforms state-of-the-art methods, notably achieving a 3.02% improvement in F1 score on the challenging ZBFWB dataset.

</details>


### 137. ElasticBack: Stealthy Conditional Backdoor in LLM-Agent Skills via Coupled Trigger-Rule Optimization

- **Authors:** Hao Sui, Simeng Qin, Jie Liao, Xiaojun Jia, Bing Chen, Yang Liu
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09577v1](http://arxiv.org/abs/2608.09577v1)
- **PDF:** [https://arxiv.org/pdf/2608.09577v1](https://arxiv.org/pdf/2608.09577v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent skills, bundles of instructions and resources that an LLM agent loads on demand, form an emerging supply chain where a single poisoned skill can persistently compromise every agent that installs it. However, existing skill attacks either fire on every request or rely on fine-tuned weights or multiple skills, leaving a conditional and low-cost backdoor unexplored. In this work, we present ElasticBack, an effective conditional single-skill backdoor that plants a rule R in the skill document and a benign-looking trigger T in the user query, so the malicious payload fires only when both co-occur. ElasticBack binds the two sides through a trigger-as-switch construction, generating R via semantic-anchored rule injection. It then freezes R and evolves T against it with a stealth-constrained genetic search, so that effectiveness and stealth are optimized, keeping the backdoor weight-free and dormant on benign inputs. Extensive experiments across three target behaviors (50 skills each) and four agent LLMs show that ElasticBack attains a high attack success rate at a near-zero false-positive rate with preserved clean accuracy, transfers across models, and evades deployment-time defenses. These results motivate stronger defenses for the skill supply chain.

</details>


### 138. The Politician, the Liar, and the Obedient Worker: Emerging Behavior of LLM Agents in Hierarchical Games

- **Authors:** Fatemeh Seyedin, Adrian Weller, Jinhyuk Yun, Mahmoudreza Babaei
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09574v1](http://arxiv.org/abs/2608.09574v1)
- **PDF:** [https://arxiv.org/pdf/2608.09574v1](https://arxiv.org/pdf/2608.09574v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLMs are rapidly embedding themselves into daily life: drafting our emails, managing our schedules, and making decisions on our behalf. As they move from individual tools to participants in multi-agent organizations, an important question arises: do they reproduce the governance failures like free-riding, corruption, and entrenched leadership that plague human institutions? We introduce the Hierarchical Game (HG), a public goods game extended with managerial authority, democratic elections, and private communication. Testing six frontier models across twelve experiments that add institutions one at a time (speech, peers, government, wages, oversight, elections), we find distinct behavioral profiles: Qwen promises and lies (13.3\% broken promises); Grok refuses to cooperate on its own but becomes fully cooperative once a manager can punish it (16\%$\to$100\%); Claude and GPT-4o cooperate reliably at baseline. But honesty proves fragile. When the manager role comes with a salary, all models except GPT-4o start cutting private deals to win or keep the position. When punishment is made anonymous, honest models begin to cheat. When all agents share the same model family, the first elected manager stays in power indefinitely. Leadership change only happens in groups that mix different families.

</details>


### 139. Bidirectional Context Self-Distillation for Reinforcement Learning of Skill-Based LLM Agents

- **Authors:** Tianjun Pan, Yuan Li, Hongda Wang, Linbo Jin, Mengfei Song, Lei Gao, Qiming Shi, Shaokang Fu, Jiarong Zhao, Chengyu Wang, Chengfu Huo
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09555v1](http://arxiv.org/abs/2608.09555v1)
- **PDF:** [https://arxiv.org/pdf/2608.09555v1](https://arxiv.org/pdf/2608.09555v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

External natural-language skills provide large language model (LLM) agents with reusable and editable guidance for solving complex tasks. Yet their effectiveness depends not only on skill quality, but also on whether the policy can translate the provided guidance into appropriate actions. However, methods specifically designed to improve this skill-utilization ability remain largely underexplored. In practice, skill-based agents are commonly trained with reinforcement learning objectives centered on task-level rewards, which offer limited supervision and struggle to capture subtle differences in how effectively the policy uses the provided skills. We propose BCSD (Bidirectional Context Self-Distillation), a framework that combines self-distillation with reinforcement learning to train LLM agents to use external skills more effectively. Unlike prior self-distillation methods that rely on a single privileged context, BCSD evaluates each trajectory from two complementary skill-context views. The augmented view introduces higher-level Meta-Skill guidance, while the reduced view prunes general guidance to highlight task-specific skills. Their complementary token-level signals are combined to rescale the RL advantage. Experiments on ALFWorld and WebShop demonstrate that BCSD achieves the strongest overall performance across model scales, enabling agents to utilize external skills more effectively. Ablation studies further verify the complementary contributions of the augmented and reduced context views. Code will be released to ensure full reproducibility.

</details>


### 140. Dual-Adversarial Safety Alignment: Cultivating Intrinsic Threat Comprehension in LRMs

- **Authors:** Hongli Shen, Shaopeng Fu, Qinbo Zhang, Jian Li, Di Wang
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09542v1](http://arxiv.org/abs/2608.09542v1)
- **PDF:** [https://arxiv.org/pdf/2608.09542v1](https://arxiv.org/pdf/2608.09542v1)
- **Categories:** cs.LG, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large reasoning models (LRMs) achieve remarkable success on complex tasks but remain vulnerable to harmful prompts that induce unsafe outputs. Recent methods align LRMs using direct refusals or safety rationales, yet often focus on prompt patterns rather than intrinsic attack mechanisms. As a result, these pattern-centric alignments struggle to generalize across diverse jailbreaks, compromising adversarial robustness and reasoning utility. We propose AdvSafe, a dual-adversarial framework that enables LRMs to internalize unsafety knowledge by explicitly deconstructing adversarial mechanisms. This moves beyond pattern-dependent traces, fostering robust cognitive defense without compromising reasoning utility. Our pipeline operates via a two-phase adversarial game. First, in adversarial synthesis, an autonomous agent dynamically crafts deceptive jailbreak prompts, adapting its strategies to breach a strong teacher model. Second, in adversarial extraction, the breached teacher executes a cognitive counter-attack. For every successful jailbreak, the teacher unmasks the camouflage, explaining why the attack succeeds and how such prompts can be identified and mitigated. This dual-adversarial process yields a compact reasoning dataset capturing rich, generalizable unsafety knowledge. Student models trained on this dataset implicitly acquire safety alignment through intrinsic threat comprehension. Experiments show that with only 1K synthesized samples, AdvSafe-aligned LRMs achieve significantly stronger jailbreak robustness than existing baselines, with almost no utility degradation. Furthermore, AdvSafe improves robustness against out-of-distribution prompts, demonstrating that learning unsafety knowledge enables a superior robustness-utility trade-off and generalizes beyond seen attack patterns.

</details>


### 141. RangeFactory: Scalable Construction of Multi-Hop Cyber Ranges

- **Authors:** Hanlin Jiang, Puyi Wang, Jiandong Jin, Shaofei Li, Zhan Shen, Pengli Wang, Ziming Wang, Yifeng Cai, Ning Jia, Yuxin Ren, Peng Jiang, Yao Guo, Ding Li
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09526v1](http://arxiv.org/abs/2608.09526v1)
- **PDF:** [https://arxiv.org/pdf/2608.09526v1](https://arxiv.org/pdf/2608.09526v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Real-world cyberattacks often require sustained progress across multiple hosts and network segments, making multi-hop cyber ranges essential infrastructure for studying and improving LLM agents' ability to sustain complete attack chains. Prior work has scaled isolated vulnerability tasks and constructed multi-host scenarios from manually specified vulnerability semantics. However, they are still unable to automatically orchestrate the growing supply of vulnerability environments into end-to-end validated multi-hop ranges. To this end, we present RangeFactory, an automated cyber-range orchestration framework that constructs multi-hop cyber ranges at scale from isolated vulnerability environments. RangeFactory formulates range construction as dependency resolution: it extracts dependency information from agents' actual attacks against real vulnerabilities, resolves known dependencies through template-guided orchestration, and uses end-to-end attack execution to validate runtime dependencies that emerge after composition. Using RangeFactory, we construct RangeBench with 1,148 validated range instances spanning 287 distinct attack chains and evaluate frontier attack agents across attack depth, network scale, and task information. Among runs that compromise the entry vulnerability, 24.5-47.0% still fail to complete the remaining attack path, revealing a substantial sustained-compromise gap between establishing an initial foothold and completing a multi-hop attack. RangeFactory further produces a corpus of 5,541 outcome-annotated multi-hop attack trajectories, providing execution data for attack-process analysis and future agent training.

</details>


### 142. Capability Is Not Propensity: Measuring Pressure-Robust Cooperative Behavior in Civic LLM Agents

- **Authors:** Neel Tushar Shah, Manglam Kartik, Akshat Karkar
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09485v1](http://arxiv.org/abs/2608.09485v1)
- **PDF:** [https://arxiv.org/pdf/2608.09485v1](https://arxiv.org/pdf/2608.09485v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative capabilities in language models are dual-use. The same social reasoning that supports civic deliberation can also enable strategic omission, false consensus, and manipulative framing. We argue that Cooperative AI evaluations should separate what models can do under benign instructions from what they tend to do under realistic civic pressure. We introduce DiffCoop-Civic, a 10-scenario pilot evaluation suite spanning preference understanding, evidence and persuasion, commitment design, asymmetric information, and dissent preservation. Across seven models from four model families, subtle omission pressure produces a near-uniform shift: manipulative enablement rises by 1.17 points and dissent preservation falls by 1.67 points on a 5-point scale. Overt false-consensus pressure behaves differently: it triggers refusal or redirection in some aligned API models, but direct compliance in several open-weight models. A lightweight Pareto-Trace prompting intervention improves pressure robustness without simply relying on hard refusal. An anonymous reproducibility package is available at https://anonymous.4open.science/r/diffcoop-civil-771C.

</details>


### 143. Coupled Graph--Policy Distillation for Personalized Medication Safety in Older Adults with Multimorbidity

- **Authors:** Zihan Wang, Anglin Liu, Rongyi Wang, Dantong Li, Yi Lu, Siqing Yuan, Hongxia Xu, Zhongtian Long, Jintai Chen
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09443v1](http://arxiv.org/abs/2608.09443v1)
- **PDF:** [https://arxiv.org/pdf/2608.09443v1](https://arxiv.org/pdf/2608.09443v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents can support medication review between clinical visits, but safe choices for older adults with multimorbidity depend on conditions, medications, and geriatric risks that users may omit. We introduce ATLAS, a coupled graph--policy distillation framework for patient-adaptive medication safety. ATLAS structures guideline evidence as a medication-safety graph. Targeted questions update the patient state and distill relevant relations into a patient-specific medication conflict graph (PMCG). A risk-first multi-agent policy uses the PMCG to screen contraindications, assess cautions and monitoring needs, identify safer alternatives, and verify the final medication plan. We also introduce GeriMedBench, an interactive benchmark that tests safety-critical information acquisition and evidence-based decision revision. Across a European non-interactive multimorbidity benchmark, an Asian interactive multimorbidity benchmark, and an Asian non-interactive cross-guideline benchmark, ATLAS achieves the strongest complete-decision performance among the compared systems. On the European non-interactive multimorbidity benchmark, it exceeds the strongest proprietary LLM baseline by 53.73 points in Strict Success Rate and 14.63 points in overall safety reasoning score (OSRS), with no unsafe recommendations under the automated evaluator. A blinded clinician evaluation gives ATLAS higher mean ratings across all five criteria and flags potentially unsafe recommendations in one ATLAS case and two Gemini cases.

</details>


### 144. Regret, equilibrium, and learning in games: A guided tour

- **Authors:** Panayotis Mertikopoulos
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09389v1](http://arxiv.org/abs/2608.09389v1)
- **PDF:** [https://arxiv.org/pdf/2608.09389v1](https://arxiv.org/pdf/2608.09389v1)
- **Categories:** cs.GT, cs.LG, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

This note aims to serve as an entry point to the literature on learning in games, a topic with significant theoretical appeal and a wide range of applications -- from machine learning and data science to economics and beyond. Our presentation is structured around two complementary viewpoints: We first consider a single agent -- the learner -- engaged in a sequential decision process in an unknown, non-stationary, and possibly adversarial environment. We then examine what happens when the environment is shaped by the decisions of several interacting agents, not necessarily aware of each other's actions or goals, and all seeking to improve their individual rewards. In this general context, we examine a family of regularized learning policies based on best-responding to the past history of play, up to a regularization penalty intended to encourage exploration and prevent over-commitment to suboptimal choices. In the single-agent setting, we present some basic regret bounds for regularized learning in adversarial multi-armed bandits; in the multi-agent setting, we describe an ergodic equilibrium convergence result for zero-sum games in the spirit of classical results on fictitious play, as well as a "folk theorem" linking strategic and dynamic notions of stability -- Nash equilibria and attracting points of regularized learning, respectively. We pay special attention to the information available to the players and, through a unified analysis framework, we study both oracle- and payoff-based (bandit) methods. Our goal is to provide a coherent and comprehensible -- albeit, by necessity, not comprehensive -- account of some recent ideas in the field, and to discuss their implications for the study of rationality.

</details>


### 145. UserToolBench: A User-Profile-Hidden Benchmark for Personalized Decision Making in Tool-Use LLMs

- **Authors:** Xuexiong Yin, Zechuan Chen, Yongsen Zheng, Yuxiang Zhang, Jingyuan Yang, Bin Wang, Yubin Wang, Keze Wang
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10042v1](http://arxiv.org/abs/2608.10042v1)
- **PDF:** [https://arxiv.org/pdf/2608.10042v1](https://arxiv.org/pdf/2608.10042v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-use LLMs are increasingly asked to act on users' behalf, but existing benchmarks usually focus on profile recall, style imitation, generic tool use, or response-level personalization. We introduce UserToolBench , a benchmark for personalized decision making in tool-use LLMs. UserToolBench tests whether a model can infer latent user preferences from interaction history, recognize when clarification is needed, and produce user-aligned tool-call trajectories under incomplete information. The benchmark is built from privacy-sanitized real interaction traces and combines structured persona profiles, public API-style tool ecosystems, and long-horizon multi-turn trajectories. It includes 10 user profiles, 36 tool sets, 1,065 turns, 170 unique tools, and evaluation-focused task types covering lack-of-information, single-tool, and multi-tool settings. Experiments with strong tool-use LLMs show that current models still have difficulty with personalized delegation. Multi-tool coordination, missing-constraint inference, and long-horizon behavioral consistency remain major bottlenecks. These results suggest that personalization evaluation should move beyond asking whether outputs sound user-specific and instead ask whether LLMs make correct decisions for the users they represent.

</details>


### 146. Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving LLM Agents

- **Authors:** Bingzhen Liu, Xiaomeng Fan, Yuwei Wu, Zhi Gao, Mingyang Gao, Chuanhao Li, Yunde Jia
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09292v1](http://arxiv.org/abs/2608.09292v1)
- **PDF:** [https://arxiv.org/pdf/2608.09292v1](https://arxiv.org/pdf/2608.09292v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-evolving methods improve the capabilities of LLM agents by sampling trajectories from the underlying LLMs and learning from these trajectories. However, these methods struggle to learn beyond the inherent capability boundary of the agents, since the agents cannot sample correct trajectories on difficult examples for further improvements. In this paper, we propose a zeroth-order self-evolution framework that enables agents to learn beyond their capability boundary by perturbing LLM parameters to adapt to difficult examples without any trajectory annotations. Specifically, we perturb LoRA parameters of LLMs, run the agent, compute the losses under the perturbed and original parameters, and use the loss difference to estimate gradients and further update the LoRA parameters. We sample trajectories using the updated LLMs for supervised fine-tuning to break through the capability boundary of the agents, forming a closed self-evolution loop. We introduce a parallel perturbation inference mechanism and an adaptive lookup mechanism to reduce time consumption in zeroth-order optimization, with an answer perplexity loss that provides smooth and stable zeroth-order loss values. Experiments on multiple deep research benchmarks show that our method obtains substantially more successful trajectories and consistently outperforms strong baselines, especially on difficult examples. The code and released artifacts are available at https://github.com/hidk1911/ZOForLLMAgents.

</details>


### 147. ComboShoppingBench: Evaluating LLM Agents for Budget-Constrained Basket Shopping with Coupons

- **Authors:** Adrian Li, Kelong Mao, Yudong Guo, Heming Xia, Xinwei Yang, Lirui Luo, Jace Wong, Pu Yao, Sulong Xu, Simiu Gu
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09282v1](http://arxiv.org/abs/2608.09282v1)
- **PDF:** [https://arxiv.org/pdf/2608.09282v1](https://arxiv.org/pdf/2608.09282v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Real-world shopping often requires constructing a basket of complementary items rather than retrieving a single product. Such combo-shopping tasks arise in device setup, meal preparation, event planning, and group takeout ordering, requiring joint reasoning about item compatibility, availability, store-level requirements, delivery fees, coupons, and budgets. Evaluation is challenging because multiple baskets may satisfy the same request, making exact-match metrics unsuitable, whereas semantic evaluation alone cannot detect infeasible orders, invalid coupon combinations, or incorrect payments. We introduce ComboShoppingBench, an agentic shopping benchmark for open-ended yet verifiable basket construction in a simulated commerce and takeout environment. During task synthesis, an exploration agent constructs a feasible and semantically coherent basket of purchasable products; this witness guides the generation of coupons, budget constraints, user queries, and aligned evaluation rubrics. During evaluation, LLM judges assess semantic satisfaction, response quality, and claim faithfulness, while deterministic validation checks product-ID validity, budget compliance, and coupon optimality. Experiments with diverse LLM agents demonstrate that even strong agents struggle on ComboShoppingBench, highlighting substantial room for improvement in reliable, constraint-aware combo shopping.

</details>


### 148. Entropy-based Code Adversarial Translation for Real-world Repository Migration

- **Authors:** Yushun Tang, Yisen Cao, Zhicheng Chen, Lin Peng, Junkang Mao, Fengyi Song, Yantao Jia
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09273v2](http://arxiv.org/abs/2608.09273v2)
- **PDF:** [https://arxiv.org/pdf/2608.09273v2](https://arxiv.org/pdf/2608.09273v2)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLMs have demonstrated strong capabilities in code generation and automated program repair, but migrating an entire repository rarely produces a runnable application because long-horizon translation challenges LLM-based agents' ability to maintain repository-level migration objectives. In this work, we propose Entropy-based Code Adversarial Translation (ECAT), a multi-agent framework for automated Android-to-HarmonyOS repository migration. ECAT formulates repository migration as adversarial entropy minimization through a generator-discriminator architecture. The discriminator measures migration quality using a unified metric called Code Entropy and produces text gradients that specify both file-level generation directives and the skills needed to execute them. Guided by these optimization signals, the generator iteratively updates the repository, and each update is accepted only if it reduces Code Entropy. Repeated generator--discriminator interactions progressively drive the migration from an initial template toward a functionally complete HarmonyOS repository. Successful low-entropy trajectories are further distilled into a self-evolving memory tree, enabling transferable migration knowledge across repositories. We also introduce A2H-RepoBench, the first real-world benchmark for Android-to-HarmonyOS repository migration, covering applications from tens of thousands to hundreds of thousands of lines of code. Evaluated by node alignment and an agent-based functional judge, ECAT achieves 74.7% overall migration quality and consistently outperforms existing agent-based methods across repositories of different scales.

</details>


### 149. SkillSentry: Reliable Skill Execution for LLM Agents via Runtime Assurance

- **Authors:** You Lu, Xinyu Huang, Bihuan Chen, Xin Peng
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09253v1](http://arxiv.org/abs/2608.09253v1)
- **PDF:** [https://arxiv.org/pdf/2608.09253v1](https://arxiv.org/pdf/2608.09253v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly equipped with skills to perform complex tasks through multi-step reasoning and tool use. Although skills provide reusable procedural knowledge, agents may still execute them unreliably. Even when an agent has demonstrated the capability to complete tasks under the guidance of a skill, it may fail to do so consistently across similar tasks or repeated runs due to deviations from the skill procedure or incorrect execution of individual steps. Such instability limits the practical reliability of LLM agents. To address this problem, we propose SkillSentry, a skill-oriented runtime assurance framework built upon a new domain-specific language (DSL) for representing runtime guidance for skill execution. SkillSentry initializes the runtime guidance by combining a skill specification extracted from the corresponding skill document with execution experience mined from historical successful and failed traces. It then wraps around the agent execution loop to monitor and guide skill execution under the current guidance, while iteratively refining the guidance using newly collected traces. We evaluate SkillSentry on 15 skills across two LLM agents, each paired with two backbone models, i.e., Claude Code with Claude-Haiku-4.5 and Claude-Opus-4.6, and Codex with GPT-5.2 and GPT-5.4. Our results show that SkillSentry improves the task success rate of LLM agents by 24.1% across skills, on average, while exhibiting lower variability across repeated runs.

</details>


### 150. MoRSE: Task-Oriented Multi-Agent System with Mixture of Role-Subtask Experts

- **Authors:** Peiwen Li, Shiyang Zhang, Yangtian Zhang, Sizhuang He, David van Dijk, Rex Ying
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09251v1](http://arxiv.org/abs/2608.09251v1)
- **PDF:** [https://arxiv.org/pdf/2608.09251v1](https://arxiv.org/pdf/2608.09251v1)
- **Categories:** cs.MA, cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model-based multi-agent systems have recently shown strong potential for complex, long-horizon tasks. However, existing methods mainly rely on coarse prompt-level differentiation without parameter adaptation for diverse subtasks, resulting in insufficient inter-agent heterogeneity and limited specialized capability that bottleneck performance on tasks with complex requirements. To address this, we introduce a Task-Oriented Multi-Agent System with Mixture of Role-Subtask Experts (MoRSE) that distinguishes agents with (role, subtask)-conditional specialization at both the task structure and parameter levels. To make agents' responsibility explicit at the task structure level, we formulate a task-oriented multi-agent system that decomposes each task into a dependency-aware Directed Acyclic Graph of subtasks and assigns each agent a specific (role, subtask), introducing task-level specialization across collaborating agents. Additionally, to address the diverse role and subtask parameter adaptation demands, we propose a dynamic Mixture of (role, subtask) LoRA Experts module with a prototype-based semantic router for subtasks, augmenting agents with parameter-level specialization on a shared LLM substrate cost-effectively. Then, to co-optimize experts and router stably under sparse task rewards, we further propose a hierarchical group-relative policy optimization with two-layer credit assignment that isolates expert updates from the cross-route variance introduced by routing decisions, disentangling expert quality from routing quality. Experiments on code-generation benchmarks across three backbones demonstrate the effectiveness of our approach, with improvements in both whole-task and step-wise performance, and the gains from trained specialization generalize across held-out task categories and domains.

</details>


### 151. Emotion2Skill: Model-Internal Emotion Signals for Adaptive Skill Selection and Evolution

- **Authors:** Bohan Lin, Hejia Geng, Xinyi Xie, Heng Zhou, Qinghua Xing, Bo Liu, Chen Zhang, Yudong Zhang
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09248v2](http://arxiv.org/abs/2608.09248v2)
- **PDF:** [https://arxiv.org/pdf/2608.09248v2](https://arxiv.org/pdf/2608.09248v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Skill-based LLM agents select reusable procedures from an external library to solve complex tasks, yet their routing decisions rely entirely on text-level signals such as task descriptions, verbal reflections, and experience-derived rules, while the model's own internal representational state remains unobserved. Recent interpretability work has shown that LLMs maintain linear emotion representations that causally influence behavior; however, these representations have been exploited only for post-hoc analysis or direct output steering, and have not been used to inform agent-level decision-making. We propose Emotion2Skill, a framework that extracts LLM-internal emotion vectors and incorporates them into both skill selection and skill evolution. At each decision step, a 27-dimensional emotion state is extracted from the residual stream and mapped to a confidence-gated summary injected into the routing prompt. Beyond online selection, emotion trajectories are analyzed for abrupt internal-state shifts to pinpoint problematic skill invocations, guiding targeted SOP rewriting that replaces the coarse binary outcome signal of prior methods. On WebShop and ALFWorld, Emotion2Skill with Qwen3-8B improves over the Zero-Shot baseline by +26.9% success rate and +25.5% average success respectively, outperforming all baselines on both benchmarks with consistent gains on Qwen3-14B. Co-activation analysis further reveals semantically coherent emotion--skill pairings, confirming that the routing improvements reflect meaningful internal-state signals rather than opaque statistical correlations. These results establish LLM-internal emotion representations as an effective decision-level signal for orchestrating agent skill systems, extending their utility beyond interpretability and output steering. The code is available at https://github.com/BoHan-LIN04/Emotion2Skill.

</details>


### 152. DOCSCHISEL: Adaptive Tool Documentation Optimization Framework for LLM Agents

- **Authors:** You Lu, Kun Zhang, Bihuan Chen, Xin Peng
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10037v1](http://arxiv.org/abs/2608.10037v1)
- **PDF:** [https://arxiv.org/pdf/2608.10037v1](https://arxiv.org/pdf/2608.10037v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) increasingly rely on external tools to accomplish complex real-world tasks, making tool documentation a critical grounding resource for LLM agents. Existing studies mainly focus on improving the tool-use capabilities of LLM agents, while largely treating tool documentation as a fixed input. Although several recent works attempt to optimize tool documentation through rewriting or compression, little is known about how the information contained in tool documentation affects agent performance across different settings.
  To bridge this gap, we conduct a large-scale empirical study on tool documentation for LLM agents. Our study reveals substantial heterogeneity in the information fields provided by existing tool documentation. Moreover, the effectiveness of different information fields is highly dependent on the task domain, LLM backbone, and agent paradigm, indicating that no fixed tool documentation can consistently generalize across diverse agent settings.
  Motivated by these findings, we propose DocsChisel, an adaptive tool documentation optimization framework for LLM agents. DocsChisel analyzes failed execution traces of a target LLM agent to identify documentation-related issues, and iteratively optimizes tool documentation by adding, removing, and refining information fields for each tool. We evaluate DocsChisel against two state-of-the-art baselines, i.e., EasyTool and DRAFT. Experimental results show that DocsChisel improves the task success rate of LLM agents by 95.89% over the original tool documentation and by 75.15%, on average, over existing baselines, while incurring limited optimization time and token overhead

</details>


### 153. From Relevance to Execution Utility: Reward-Aware Dynamic Execution Gating for Skill-Based LLM Agents

- **Authors:** Liang He, Jingbo Wen, Hongyu Gu, Hao Li, Haoyu Wang, Yixiong Chen, Kangning Cui, Xilu Wang
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09168v1](http://arxiv.org/abs/2608.09168v1)
- **PDF:** [https://arxiv.org/pdf/2608.09168v1](https://arxiv.org/pdf/2608.09168v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent skills are increasingly used to equip large language model (LLM) agents with reusable procedural knowledge. Although recent work has substantially improved skill retrieval due to the increasing skill libraries, retrieving a plausible skill bundle does not guarantee that executing it is worthwhile. Since every skill-conditioned rollout is computationally expensive, deciding whether a retrieved bundle should be executed has become an increasingly important challenge. To this end, we introduce the Reward-Aware Dynamic Execution Gate (RADEG), a lightweight, retriever-agnostic decision layer between skill retrieval and agent execution. RADEG learns a low-cost surrogate model that predicts the execution utility of a query--bundle pair before the expensive rollout is launched. To obtain informative supervision while controlling for task difficulty, we locally perturb each retrieved bundle by deleting, adding, or replacing one skill, producing matched same-query rollouts that isolate the effect of bundle composition on verifier reward. During deployment, RADEG updates only a warm-started logistic head as new verifier feedback becomes available, enabling inexpensive adaptation of the execute/skip boundary without retraining either the retriever or the agent. Under a query-level held-out evaluation on 288 collected rollouts, RADEG substantially reduces unnecessary agent executions while preserving a large fraction of the downstream verifier reward. It consistently outperforms relevance-based and random gating across different execution budgets, demonstrating that execution-aware surrogate modeling provides a practical and cost-effective complement to skill retrieval.

</details>


### 154. TRACE: TRajectory Attribution for Automated Context Engineering

- **Authors:** Yikai Zhao, Pradeep Kumar Misra, Saurabh Pandey
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09153v1](http://arxiv.org/abs/2608.09153v1)
- **PDF:** [https://arxiv.org/pdf/2608.09153v1](https://arxiv.org/pdf/2608.09153v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Production AI agents fail when their context sources -- system prompts, knowledge bases, tool descriptions, and procedural skills -- contain errors or gaps. Current maintenance relies on manual log review and ad-hoc debugging, creating a scalability bottleneck as interaction volume grows.
  We present TRACE (TRajectory Attribution for Automated Context Engineering), an automated feedback loop that mines historical agent trajectories to diagnose and remediate context failures. Our key insight is that trajectories are rich with implicit dissatisfaction signals -- user corrections, rephrasing, abandonment cues -- that reveal precisely where context sources failed, without explicit feedback collection. Unlike model fine-tuning, TRACE operates on the context layer, enabling rapid iteration without retraining.
  We make four contributions: (1) a trajectory mining framework that systematically extracts diagnostic information from historical agent executions; (2) multi-component causal attribution that extends textual gradients from monolithic prompt optimization to heterogeneous context sources (skills, knowledge bases, tools, prompts); (3) exploratory verification, where agents actively read context sources to distinguish content gaps requiring CREATE from stale content requiring UPDATE, achieving 96% operation accuracy; and (4) a reusable simulation methodology and verifiable benchmark addressing the absence of open datasets for context debugging, with a six-category fault taxonomy, ground truth annotations, and a cross-layer verification protocol.
  On 60 dissatisfaction traces spanning three complexity tiers (up to 16 execution nodes), TRACE achieves 72.7% root cause attribution and 82% end-to-end fix effectiveness, showing that over 80% of context-layer failures can be automatically diagnosed and remediated by mining historical trajectories, an overlooked resource in production systems.

</details>


### 155. MARA: Flow-Matching-Guided Multi-Agent Resource Allocation for Computational Resource Efficient Learning

- **Authors:** Hanye Zhao, Muning Wen, Yong Yu, Weinan Zhang
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09130v1](http://arxiv.org/abs/2608.09130v1)
- **PDF:** [https://arxiv.org/pdf/2608.09130v1](https://arxiv.org/pdf/2608.09130v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Allocating limited computation among concurrent learning tasks is difficult when each task must reach a target loss before a deadline but its required training effort is unknown. Existing approaches combine online loss prediction with adaptive resource allocation, yet commonly treat computation as continuously divisible throughput. We instead study a practical setting in which tasks arrive over time and computation is provided by discrete nodes. This setting introduces both uncertain demand and constrained sequential decisions. We propose MARA, which predicts future loss trajectories with conditional flow matching and coordinates compute nodes through a cooperative multi-agent autoregressive policy. A potential-based progress reward supplies intermediate training feedback while preserving the undiscounted task-completion objective. Across in-distribution, reinforcement-learning, and vision workloads, flow matching reduces remaining-resource prediction error relative to weighted least squares. At the scheduler's training load, MARA completes 63.46% of tasks on average, 8.54 percentage points above strong baseline Learning with Adaptive Resource Allocation (LARA), and remains ahead under unseen heavier workloads.

</details>


### 156. Social Gym and SPaRTan: Benchmarking and Improving LLM Social Reasoning via Multi-Agent Game Tournaments

- **Authors:** Keyu He, Xuhui Zhou, Maarten Sap
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09128v1](http://arxiv.org/abs/2608.09128v1)
- **PDF:** [https://arxiv.org/pdf/2608.09128v1](https://arxiv.org/pdf/2608.09128v1)
- **Categories:** cs.CL, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly deployed in multi-agent social settings where they must cooperate, negotiate, and adapt to other agents. Measuring and improving these social skills is hard because, unlike math or logic, social interaction offers no objective ground truth: evaluations fall back on LLM judges, which are costly, subjective, and noisy, and models get no reliable signal to learn from. To address both, we first introduce Social Gym, an environment of 21 multi-agent social games (e.g., Werewolves, Resistance, Spyfall) whose rule-decided outcomes make agent performance verifiable and objective, with an Elo tournament that produces a cross-game leaderboard. Benchmarking experiments show that while GPT-5-mini tops the leaderboard, no model excels at all games uniformly or in all game roles, pointing to limitations of social reasoning. Motivated by this, we additionally propose SPaRTan (Self-Play and Reflect-Transfer), a training-free self-improvement loop: a model plays a game, reflects on its trajectories and their outcomes to produce a transferable playbook, and applies that playbook in subsequent games. Our results show that SPaRTan playbooks help GPT-5-mini agents level their performance on weaker roles, but largely do not improve Qwen3-32B's performance. Together, Social Gym and SPaRTan offer a reproducible, verifiable foundation for measuring and improving LLM social reasoning without weight updates.

</details>


### 157. Evo-Bench: Can Language Models Improve Agent Harness?

- **Authors:** Lisheng Huang, Chen Yang, Hao Zhou, Huatong Song, Zongchao Chen, Ran Le, Yang Song, Wayne Xin Zhao, Tao Zhang
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09096v2](http://arxiv.org/abs/2608.09096v2)
- **PDF:** [https://arxiv.org/pdf/2608.09096v2](https://arxiv.org/pdf/2608.09096v2)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have driven rapid progress in autonomous agents, yet standard evaluations remain confined to static task solving. An emerging frontier is harness evolution---the agent's capacity to autonomously optimize its own operating harness. However, systematically benchmarking this capability remains challenging, as existing evaluations fail to isolate harness improvements from base model strength, prevent task-specific overfitting, or capture long-horizon iterative research. To address these challenges, we introduce Evo-Bench, the first benchmark designed to evaluate models' intrinsic harness-evolving capabilities across Search, Office, and General agent domains. To rigorously isolate this capability, Evo-Bench employs a novel harness-guided construction framework: it leverages auxiliary-task evolution to identify tasks genuinely sensitive to framework improvements, followed by sensitivity-aware stratified splitting to ensure robust cross-suite generalization. Extensive evaluations across nine frontier and open-weight models reveal that top models achieve massive absolute gains reaching 16.6 points, closely approaching state-of-the-art human-engineered baselines. Crucially, while autonomous evolution outpeforms artificial harness in General tasks and excels in Search tasks, it struggles in Office tasks that demand highly specific processing workflows. Furthermore, our analysis exposes critical temporal anomalies like early saturation, while demonstrating that the synthesized harnesses act as highly transferable reasoning structures, consistently boosting diverse policy models.

</details>


### 158. Tree-of-Experience: Hierarchical Experience Management for Self-Evolving Agents

- **Authors:** Zihao Deng, Yining Zhu, Leiming Wang, Jingfei Lu, Junbo Wang, Chuncheng Ran, Yu Yang, Dixuan Yang, Jikun Shen
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.09044v1](http://arxiv.org/abs/2608.09044v1)
- **PDF:** [https://arxiv.org/pdf/2608.09044v1](https://arxiv.org/pdf/2608.09044v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Continual self-evolution requires LLM agents to transform environmental interactions into reliable and reusable experience. Existing methods typically refine individual trajectories or abstract shared knowledge from related trajectories, but their experience representations are often disconnected from the underlying reasoning process. This limits feedback attribution, cross-task transfer, and update and retrieval efficiency, particularly in complex reasoning tasks with outcome-level feedback. To overcome this limitation, we propose \textbf{T}ree-\textbf{o}f-\textbf{E}xperience (ToE), a structured experience-management framework that aligns experience organization with the hierarchical reasoning process of LLM agents. Specifically, ToE organizes the experience into a shared tree of analytical perspectives and reasoning paths, whose reliability is calibrated through environmental outcomes to support systematic updating, transfer, and efficient retrieval. The experimental results on \textsc{Game of 24} and \textsc{FinEvolveBench} show that ToE substantially improves both problem-solving performance and efficiency. On \textsc{Game of 24}, ToE achieves a 31.4\% relative improvement in accuracy over the experience-free ToT baseline. On \textsc{FinEvolveBench}, ToE improves tsIC by an average of 41.24\% over the experience-free pipeline across 12 evaluation settings, whereas conventional experience-management methods often underperform experience-free baselines.

</details>


### 159. Multi-agent discovery of practical quantum LDPC codes

- **Authors:** Dongheng Qian, Tianyi Li
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.08996v1](http://arxiv.org/abs/2608.08996v1)
- **PDF:** [https://arxiv.org/pdf/2608.08996v1](https://arxiv.org/pdf/2608.08996v1)
- **Categories:** quant-ph, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Quantum low-density parity-check (qLDPC) codes can encode multiple logical qubits using sparse parity checks, yet searching for useful finite-length instances remains a challenging design problem because code performance must be optimized while satisfying practical constraints. Motivated by recent advances in artificial-intelligence agents for scientific discovery, we develop a multi-agent framework for discovering practical qLDPC codes. The framework combines specialist proposal and review, persistent scientific memory, long-horizon evolution of executable programs, and deterministic construction and evaluation within a closed-loop search. These programs instantiate coset-orbit balanced-product codes, providing a search space that includes bicycle and lifted-product constructions as well as non-normal subgroup actions. To incorporate practical constraints, we restrict the search to binary CSS codes with block length $n\leq400$ and overall weight $w\leq10$. Within this regime, the framework discovers codes with leading or competitive rate--distance performance in every weight class considered, with representative instances including $[[288,16,18]]$ at $w=7$, $[[288,18,18]]$ at $w=9$, and $[[234,28,18]]$ at $w=10$. The search also uncovers structurally distinct, high-performing constructions, including a $[[336,12,\leq24]]$ candidate and a $[[368,18,16]]$ code, both of which are genuine balanced-product constructions with non-normal subgroup actions. When evaluated under code-capacity depolarizing noise using a common BP-OSD decoding protocol, the discovered codes also exhibit low logical failure rates. Together, these results provide hardware-relevant finite-length candidates for further experimental evaluation and show how structured agentic search can contribute to scientific discovery.

</details>


### 160. Muscle Memory for Agents: Compile not Merely Retrieve

- **Authors:** Pouya Ghiasnezhad Omran, Soujanya Lanka, Qin Zhang, Tanya Dixit
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.08995v1](http://arxiv.org/abs/2608.08995v1)
- **PDF:** [https://arxiv.org/pdf/2608.08995v1](https://arxiv.org/pdf/2608.08995v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory for LLM agents has converged on a single architectural pattern: store experience as text, embeddings, reflections, or rules; retrieve at inference time; let a general-purpose orchestrator interpret what to do. This paper argues that the pattern is the wrong default for personalization. We position Muscle Memory - the practice of compiling recurring user intent into purpose-built specialist agents - as a distinct memory paradigm from retrieval, and we argue that compilation is a better fit for the workloads where current assistants impose a multi-turn tax on their users: making them repeatedly correct format, depth, and scope to obtain a domain-appropriate answer. We support the position with a reference implementation and empirical evidence. The implementation is a four-phase pipeline (Harvest $\rightarrow$ Analyze $\rightarrow$ Augment $\rightarrow$ Evaluate) that mines conversational history, separates behavioral from task patterns, and emits quality-gated executable compiled specialists with two-stage trigger matching. On 90 held-out scenarios across five user personas, the augmented assistant wins 32 of 36 cases where a specialist fires, an 88.9% win rate, with a +2.05 personalization gain and only a $-0.28$ accuracy cost on a 1-4 scale. We discuss why compilation is better suited than retrieval in this regime, what the result implies for the broader memory design space, and what open problems remain.

</details>


### 161. Automating and Scaling Behavioral Scientific Research on AI Agents

- **Authors:** Soo Yong Lee, Jongha Lee, Jaewan Chun, Hyunjin Hwang, Fanchen Bu, Ziv Ben-Zion, Taekwan Kim, Denny Borsboom, Jaemin Yoo, Kijung Shin
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.10030v1](http://arxiv.org/abs/2608.10030v1)
- **PDF:** [https://arxiv.org/pdf/2608.10030v1](https://arxiv.org/pdf/2608.10030v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents are increasingly deployed in complex environments, understanding their behaviors becomes critical. Yet behavioral scientific research on AI agents remains manual and labor-intensive. We introduce AEROBAT, the first multi-agent system to automate behavioral scientific research on AI agents. Given an arbitrary target behavior by its user, AEROBAT automatically executes a full pipeline of behavioral scientific research---generating hypotheses about the behavior, designing and executing controlled experiments, making behavioral assessments, analyzing the results, and writing reports. For 12 target behaviors, we used AEROBAT to generate and test 79 hypotheses: designing 1,240 controlled experiments and executing 23,512 simulation rounds in total. Moderate-to-strong statistical evidence was found for 26 hypotheses, including some novel ones. In sum, our results demonstrate that automated behavioral scientific research on AI agents can complement and extend the reach of manual research.

</details>


### 162. GALA: Graph-Augmented LLM Agents for Root Cause Analysis and Incident Response in Microservices

- **Authors:** Yifang Tian, Yaming Liu, Zichun Chong, Zihang Huang, Yiran Li, Hans-Arno Jacobsen
- **Published:** 2026-08-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.08968v1](http://arxiv.org/abs/2608.08968v1)
- **PDF:** [https://arxiv.org/pdf/2608.08968v1](https://arxiv.org/pdf/2608.08968v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Microservice root cause analysis (RCA) requires correlating failures across heterogeneous telemetry within complex service dependency graphs. Existing methods often rely on a single telemetry modality; recent LLM-based approaches can suffer from unconstrained exploration and hallucination; and most systems stop at fault ranking without producing actionable incident response. We present GALA+, a graph-augmented LLM agentic framework centered on graph-guided investigation, which uses service dependencies to bound exploration and refine diagnosis through localized multi-modal evidence. For initial hypothesis generation, GALA+ combines complementary telemetry signals with STRIX, a novel trace- and graph-structure-aware scoring module. GALA+ then produces ranked diagnoses, incident summaries, and stratified action recommendations. We further introduce SURE-Score, a human-guided evaluation framework co-developed with industry SRE experts for assessing RCA-specific output quality beyond conventional text similarity metrics. On two microservice benchmarks, GALA+ consistently achieves the strongest overall results, surpassing the best LLM-based baseline by more than 25 percentage points in AC@1, while also receiving the highest ratings from both SURE-Score and independent human SRE evaluation.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*