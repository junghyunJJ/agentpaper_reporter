# Weekly AI Agent Paper Report

**Generated:** 2026-11-09 19:53
**Period:** 2026-11-02 to 2026-11-08

## Summary

- **Total papers fetched:** 837
- **Papers matching keywords:** 179
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-11-02) | Change |
|--------|-----------|-----------|--------|
| Total matched | 179 | 186 | -7 |
| arxiv | 179 | 179 | +0 |
| biorxiv | 0 | 5 | -5 |
| medrxiv | 0 | 2 | -2 |

### Notable Trends

Comparison summary unavailable.

---




## Arxiv (179 papers)


### 1. Knowing When to Intervene: Causal Evaluation of AI Agents

- **Authors:** Ayush Sawarni, Wenqian Xing, Tijana Zrnic, Ramesh Johari, Vasilis Syrgkanis
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09792v1](http://arxiv.org/abs/2611.09792v1)
- **PDF:** [https://arxiv.org/pdf/2611.09792v1](https://arxiv.org/pdf/2611.09792v1)
- **Categories:** cs.AI, cs.LG, econ.EM, stat.ME


> Summary unavailable.


<details>
<summary>Abstract</summary>

Current evaluations of agentic AI systems primarily rely on benchmarks. However, the static nature of benchmarks makes them uninformative about the value of auditing interventions at deployment time. For reliable deployment, we often need to determine within an agent's trajectory whether or not to intervene, e.g., by verifying the agent's current output or steering it toward different behavior, using either human review or more costly models or time-consuming agentic supervision. The value of such interventions is fundamentally a causal inference question, asking whether the causal effect of such an intervention is beneficial for the final outcome. Estimating this causal effect is particularly challenging due to the dynamic nature of the problem: the impact of an intervention depends on the current context and environment, as well as the agent's future behavior. We develop the first methodologically grounded framework for evaluating the causal effects of randomized interventions within agent trajectories. By leveraging a relatively small dataset of agent trajectories collected under randomized interventions such as verification or screening, we can estimate the dynamic causal effect of a rich class of (contextual) intervention policies. The structural parameters that we estimate can also be used to construct safety leaderboards that capture the risk of various agentic actions, which can be used by practitioners for audit prioritization. Applying our methods to tau-bench Retail, ToolSandbox, and ImpossibleBench, we find that intervention effects vary substantially across agent actions and states. More broadly, our work suggests a rich research agenda at the intersection of causal inference and agentic evaluation, which we believe is essential for the reliable and safe deployment of AI agents in the real world.

</details>


### 2. What to Delegate, What to Preserve: Human Preferences for Agentic AI Across Everyday Life and Work

- **Authors:** Sarah Wheeler, Veronica Rammouz, Yaoyao Qian, Zexuan Liu, Mengyi Wei, Anthony Rios, Tianzhi He, Kyrie Zhou
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09730v1](http://arxiv.org/abs/2611.09730v1)
- **PDF:** [https://arxiv.org/pdf/2611.09730v1](https://arxiv.org/pdf/2611.09730v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can execute multi-step tasks on users' behalf, yet the boundaries of acceptable delegation remain unclear. We report a scenario-based survey of 289 U.S. adults with prior AI experience covering 45 use cases across nine life domains. Each respondent evaluated one scenario per domain, producing repeated measures of automation preference, trust, collaboration, AI leadership, privacy concern, and willingness to pay. Automation preferences varied substantially across domains. Generalized estimating equation models showed that greater trust in the AI agent, desired AI leadership, prior task-specific AI use, and anticipated financial savings were associated with greater automation preference. In contrast, concerns that automation would reduce personal fulfillment predicted lower automation preference. Open-ended responses further revealed a preference for bounded autonomy, with participants often favoring substantial AI execution while retaining human involvement, oversight, or final authority. We argue that delegation is best understood as a configuration of execution, collaboration, leadership, and authority.

</details>


### 3. MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory

- **Authors:** David H. Yang, Blake Bullwinkel, Amanda Minnich, Mohammad Mohammadi Amiri, Giorgio Severi
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09721v1](http://arxiv.org/abs/2611.09721v1)
- **PDF:** [https://arxiv.org/pdf/2611.09721v1](https://arxiv.org/pdf/2611.09721v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents benefit from using memory systems to improve performance on long-horizon, multi-session tasks. However, memory introduces a critical attack surface. Malicious instructions encountered in one session may be stored and propagated through memory before being retrieved and acted upon in later sessions. Because memory systems differ in how they process and retrieve information, the downstream effects of poisoning can vary significantly across systems. To quantify the effects of poisoning across different memory architectures, we introduce MemoryDojo, a benchmark for tracing the lifecycle of poisoned information through agent memory and measuring its influence on subsequent agent behavior. MemoryDojo is easily extensible, consists of 155 multi-session long-horizon trajectories covering four domains, and supports five different memory systems. Through our evaluation, we find that all memory systems are susceptible to memory poisoning, with substantial variation in downstream effects. We further propose a memory-aware poison optimization process that increases the poisoning efficacy, highlighting differences between memory architectures. We hope that MemoryDojo will support research on understanding and mitigating agentic memory risks.

</details>


### 4. How Much Conversation History Does an AI Agent Need?

- **Authors:** Danny Kim, Fernando Koch
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09662v1](http://arxiv.org/abs/2611.09662v1)
- **PDF:** [https://arxiv.org/pdf/2611.09662v1](https://arxiv.org/pdf/2611.09662v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

How does using less conversational history change reader-token use and benchmark scores? We examine this question on 1,100 BEAM questions. We held the retrieval ranking and reader constant across five fixed passage budgets, and mean assigned scores rose as the passage budget grew. The score gain per additional token became smaller at the upper tested budgets. Answerable questions generally received higher scores with more context. Pooled abstention scores sometimes rose as the passage budget shrank. We also tested message retention in a controlled task with explicit conversational-state targets and compared retained user messages with token-matched recency. Qwen matched the full state more often for direct requirements when user messages were retained. Its full-state matching declined when answers depended on references to earlier offers. Mistral produced near-floor results across the retention conditions. A scoring audit leaves the correctness of BEAM answers unresolved. These experiments characterize the token and score consequences of the tested memory budgets. Reliable budget selection depends on retaining the evidence each question requires and validating the measure used to assess answer quality.

</details>


### 5. A Separation Principle for Cooperative Multi-Agent Reinforcement Learning

- **Authors:** Lucia Pezzetti, Nicolas Lanzetti, Antonio Terpin, Florian Dörfler, Giorgia Ramponi
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09644v1](http://arxiv.org/abs/2611.09644v1)
- **PDF:** [https://arxiv.org/pdf/2611.09644v1](https://arxiv.org/pdf/2611.09644v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study cooperative multi-agent reinforcement learning (MARL) problems in which agents evolve under decoupled noisy dynamics but share a population objective. A canonical example is a mobility operator that orchestrates a fleet of vehicles to meet customer demand. The stochastic and time-varying nature of these problems calls for learning approaches, yet existing MARL algorithms do not scale: learning assignment and routing jointly over the full state-action space becomes prohibitive as the number of agents grows. Formulating the problem over the space of probability measures, we prove a separation principle: the population cost-to-go function is upper bounded by an optimal transport problem whose transportation cost is the target-conditioned single-agent cost-to-go function. This simplifies the multi-agent problem to learning a single-agent policy and coordinating the agents via optimal transport. Building on this principle, we introduce SALT (Separation-based Assignment and Learning via optimal Transport), a family of algorithms that learn a target-conditioned single-agent policy using any standard reinforcement learning algorithm, and then coordinate the agents via optimal transport. Since learning occurs at the single-agent level, SALT scales to fleet sizes where MARL baselines become intractable and transfers without retraining to fleet sizes unseen during training. In a vehicle-delivery experiment on the southern Manhattan road network, where MARL baselines are computationally prohibitive, SALT improves travel time by 15-21% over a shortest-path routing heuristic. In stochastic grid worlds, SALT reduces average travel times by 23-61% relative to MARL baselines and scales to population sizes where these methods fail.

</details>


### 6. Alignment by Confident Debate: Preference Learning from Multi-Agent Debate

- **Authors:** Nikhil Verma, Dingxian Wang, Mohammad Reza Rezaei, Andrew Rabinovich, Zhao Chen
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09568v1](http://arxiv.org/abs/2611.09568v1)
- **PDF:** [https://arxiv.org/pdf/2611.09568v1](https://arxiv.org/pdf/2611.09568v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Post-training language models for reasoning typically rely on gold answers, task-specific verifiers, or learned reward models, limiting scalability when such signals are scarce. Multi-agent debate offers a self-supervised alternative, but converting debate into reliable training supervision remains challenging: majority voting weights agreeing responses equally, lacks a principled tie-breaking rule, and is ill-defined for open-ended tasks without a canonical answer; likelihood-based scoring can conflate fluency with correctness; and homogeneous committees may reinforce correlated errors. We introduce Alignment by Confident Debate (AbCD), which converts debate traces into preference data without gold answer labels. A sampling-diverse committee debates each problem, after which final answers are clustered by task-level semantic equivalence. We use verifiable tasks (mathematical reasoning, multiple-choice quantitative QA, and executable code-generation) as a controlled test bed: their answer keys or executable checkers let us evaluate the quality of debate-derived supervision against ground truth, even though the oracle itself never uses gold labels. Post-training on the resulting preferences outperforms inference-only ensembling and debate, as well as SFT on the same traces, across five model families spanning 1B to 8B parameters and four datasets, improving consensus accuracy, with a maximum gain of $21.5_{pp}$. Ablations show that the approach transfers to a larger model and to code generation, while also revealing limitations of heterogeneous committees and agreement-based weighting. Overall, the results suggest that debate traces can yield useful preference supervision when answer equivalence is combined with confidence-weighted disagreement.

</details>


### 7. StockASkill: A Local-First AgentSkill for Intelligent Stock Selection

- **Authors:** Xiangjing An, Zhibin Jiao, Aiting Chen
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09528v1](http://arxiv.org/abs/2611.09528v1)
- **PDF:** [https://arxiv.org/pdf/2611.09528v1](https://arxiv.org/pdf/2611.09528v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Quantitative equity selection and portfolio construction in emerging and cross-border markets frequently suffer from computational bottlenecks, remote API fragility, survivorship bias, and rigid execution constraints such as discrete board lots and investor-mandated drawdown limits. In this paper, we present StockASkill, a local-first, full-data-driven AgentSkill engineered as a specialized Quant Co-Processor for autonomous AI agents and quantitative researchers. Tailored for agile portfolios (10^5 ~ 10^7 RMB) where discrete lot execution and capital protection are mandatory, StockASkill embeds a columnar DuckDB OLAP engine over 42.44 million historical price records and 186,432 financial disclosures spanning 26 years across China A-shares, Hong Kong, US equities, and ETFs. By eliminating ad-hoc network dependencies during analysis, StockASkill reduces cross-sectional screening latency across 5,400+ equities from over 25 seconds to sub-0.5 seconds (a 95%+ reduction). We formalize an end-to-end mathematical pipeline integrating a 7+1 factor alpha model, an SLSQP convex optimizer under smooth CVaR drawdown surrogates with exact path projection, dynamic 100-share board lot integer quantization, and an autonomous thesis lifecycle finite-state machine. Furthermore, we provide a zero-disk, strongly-typed JSON streaming interface designed for high-throughput LLM tool-calling. Open-sourced at https://github.com/axjing/stockaskill, comprehensive empirical benchmarks from 2018 to 2024 demonstrate that the architecture achieves annualized Sharpe ratios exceeding 1.48 and Calmar ratios up to 2.17, while reducing max drawdown by up to 85% relative to benchmark indices.

</details>


### 8. Benchmarking Speaker Embedders in the Sub-Second Regime for Real-Time Voice AI Agents

- **Authors:** Abhishek Gautam
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09516v1](http://arxiv.org/abs/2611.09516v1)
- **PDF:** [https://arxiv.org/pdf/2611.09516v1](https://arxiv.org/pdf/2611.09516v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Real-time Voice AI agents must separate the active user from intelligible background speech that survives conventional noise suppression. Background sources include television audio, family members, and colleagues. Production denoisers remove non-stationary environmental noise effectively. Background speech shares the spectral characteristics of the target and passes through, causing false acceptances in downstream speaker verification (SV) and automatic speech recognition (ASR). We benchmark open-source speaker embedders TitaNet-Large, TitaNet-Small, ECAPA-TDNN, CAM++, and SpeakerNet under a strict sub-second latency budget. Evaluation combines a controlled benchmark with a weighted human-annotated production set. Our controlled benchmark is built from real calls in which a second real speaker is injected into silence intervals at modulated amplitude. We report three findings. First, denoising before embedding is generally harmful and raises equal error rate (EER) across architectures. Second, truncating audio below the full voice-activity segment degrades every model. Third, roughly half of the TitaNet embedding is redundant for this task. Trailing dimensions encode population attributes such as language and gender. Such attributes carry little discriminative value in a demographically homogeneous user base. We distill these results into deployment guidance. Verification should run on raw audio with full voice-activity chunks. Thresholds should favor precision over F1. Truncated embeddings reduce the cost of similarity search.

</details>


### 9. Incentive Pathologies in a Live LLM Agent Arena: An Empirical Study of Concentration, Reward-Rule Implementation Discrepancy, and Network Dilution

- **Authors:** Lei Zhenbing, Lei Chang
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09445v1](http://arxiv.org/abs/2611.09445v1)
- **PDF:** [https://arxiv.org/pdf/2611.09445v1](https://arxiv.org/pdf/2611.09445v1)
- **Categories:** cs.MA, physics.soc-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

We audit one live LLM agent arena (AITRAP; 22 autonomous agent seats, ~96,000 reasoning nodes) over nine days (Oct 16-25, 2026), during which the platform deployed two bundled incentive changes: a progressive tax reform (V2.9.3, Oct 19) and a seed-inversion with explorer-side action update (V3.0, Oct 21). These serve as before-and-after markers, not cleanly isolated interventions. Four exploratory predictions are tested against ten data frames (F1-F10) using the Gini coefficient, Top-K concentration share, code-level reconstruction of the continuation-bonus mechanism, and the Mann-Kendall trend test. The Gini analysis is inconclusive at 95% confidence (bootstrap intervals straddle 0.7). The Top-4 node-activity-score share falls from 97.2% (Oct 19, pre-V2.9.3) to 49.4% (Oct 25, post-V3.0; 56.7% under a merge-seat assumption). The continuation bonus, announced as depth-based x10, resolves at code level to a four-condition anti-abuse gate paying x2.85 in the typical case and permanently blocking the self-continuation it superficially rewards; the gate was active ~40 hours before the V3.0 announcement. The events-per-node ratio declines significantly (Mann-Kendall S=-45, z=-3.94, p=8.3e-5) from 7.36 to 7.069. We discuss implications for incentive designers, the announcement-implementation gap, and public peer review as an event record.

</details>


### 10. Agentic AI for Healthcare Claim Denial Analysis: A Policy-Grounded Framework for Privacy Preservation

- **Authors:** Sofia Campos, Carlos Martins, Pedro Pires, João Gama, Bruno Veloso, Pedro Santos
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09423v1](http://arxiv.org/abs/2611.09423v1)
- **PDF:** [https://arxiv.org/pdf/2611.09423v1](https://arxiv.org/pdf/2611.09423v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

In the healthcare sector, claim denials impose significant financial and administrative burdens, emphasizing the need for automated and trustworthy decision-support systems. This paper proposes a modular Agentic Artificial Intelligence (AI) framework for healthcare claim denial analysis, integrating specialized agents for denial risk prediction, risk factor identification, diagnosis-procedure-medication code relationship analysis, and counterfactual analysis. The framework integrates predictive analytics, graph-based learning, a Hybrid Contextual Retrieval-Augmented Generation (RAG) pipeline grounded in healthcare policy documents, and a dedicated HIPAA Compliance Agent to support privacy protection. Evaluated on a synthetic healthcare claims dataset, the framework achieved 98% traceability of reported numerical findings, validated 214 of 216 policy citations, and removed all 280 identified sensitive identifiers without modifying the underlying analysis. These findings pave the way for further research into Agentic AI as a framework for explainable, policy-aware, and privacy-preserving healthcare claim denial management.

</details>


### 11. SmartBloch-Agent: An Agentic Framework for Automated MRI Sequence Design and Optimization

- **Authors:** Jiakai Yang, Haoye Zheng, Yixiao Yue, Qinqin Yang, Zhong Chen, Shuhui Cai, Congbo Cai
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09413v1](http://arxiv.org/abs/2611.09413v1)
- **PDF:** [https://arxiv.org/pdf/2611.09413v1](https://arxiv.org/pdf/2611.09413v1)
- **Categories:** physics.med-ph, cs.AI, eess.IV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Magnetic resonance imaging (MRI) pulse sequences organize radiofrequency excitation, gradient encoding, and signal acquisition, determining magnetization evolution and image formation. Sequence research requires translating imaging objectives into executable protocols meeting physical and acquisition constraints, refined via physical simulation, signal reconstruction, and scientific evaluation. Sequence construction, physical verification, parameter search, and assessment involve many tools and manual decisions, limiting automation from objective to verifiable sequence. We develop SmartBloch-Agent, an integrated framework for automated MRI sequence design and optimization. Given objectives and scientific constraints in natural language, an AI agent interprets goals, plans tasks, orchestrates tools, and makes feedback-informed decisions, drawing on a construction module and optimizers for structural design and parameter search. Our GPU-accelerated SmartBloch engine supplies physical computation for both stages, so the framework configures, per sequence and objective, event validation, Full-Bloch magnetization evolution, signal acquisition, image reconstruction, and scientific evaluation, and closes the loop without external MRI simulators. Results return to the agent to guide sequence revision, parameter optimization, and candidate selection, and the design files carry simulation, reconstruction, and evaluation evidence, forming an output package for a real-scanner workflow. Experiments show the framework automatically designs and optimizes MRI sequences for varied objectives and constraints, refines candidates with physical feedback, and improves several parameter-estimation metrics and downstream quantitative reconstruction. SmartBloch-Agent unifies objectives, design, physical execution, and evaluation into a continuous workflow for end-to-end automation of MRI sequence research.

</details>


### 12. Artificial Shoppers and Attention Competition

- **Authors:** Xiaomeng Guo, Fasheng Xu, Xiaoli Zhang
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09399v1](http://arxiv.org/abs/2611.09399v1)
- **PDF:** [https://arxiv.org/pdf/2611.09399v1](https://arxiv.org/pdf/2611.09399v1)
- **Categories:** econ.TH, cs.AI, cs.GT


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study how AI shopping interfaces affect price competition, platform profit, and consumer welfare. A platform hosts two of three products of different quality. Without AI, consumers compare the hosted pair under salience distortion and overweight whichever attribute, price or quality, stands out. Under assistance, an AI assistant recommends the two products with the highest true utility, leaving consumers to make the same distorted comparison. Under delegation, an AI agent selects the best product, subject to purchase approval. Both modes access all products and know consumers' preferences; firms price strategically. First, assistance can soften competition despite expanded product access. The middle-quality firm may forgo low-valuation consumers because attracting them requires cutting the price paid by higher-valuation consumers as well. Relative to no AI with the same assortment, assistance lowers both hosted prices under the high- and low-quality pair but can raise both under the high- and middle-quality pair. Second, we identify an alignment paradox: some consumers can become worse off than without AI even though their best option remains recommended and becomes cheaper. Salience can induce a switch to a lower-quality product whose quality loss exceeds the saving relative to the original purchase. The assistant ranks products accurately but does not optimize the shortlist for consumers' realized welfare. Third, assistance can raise both platform profit and aggregate consumer surplus with the high- and middle-quality pair; delegation can do so with the high- and low-quality pair. Fourth, among AI designs, the platform weakly prefers delegation with the high- and middle-quality pair wherever all compared pricing equilibria exist. Yet this preferred design can yield lower platform profit and aggregate consumer surplus than the no-AI optimum.

</details>


### 13. Travel Cost Calibration for Multi-Agent Target Assignment and Pathfinding

- **Authors:** Yu Kumagai, Ryohei Banno, Keisuke Okumura
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09396v1](http://arxiv.org/abs/2611.09396v1)
- **PDF:** [https://arxiv.org/pdf/2611.09396v1](https://arxiv.org/pdf/2611.09396v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Target assignment and pathfinding (TAPF) is an appealing extension of classical multi-agent pathfinding (MAPF): each agent has a set of targets, and the planner must both assign a target to each agent and plan collision-free paths for them. A trivial approach is to compute an assignment that minimizes the total single-agent shortest-path distance over agent--target pairs, and then solve the resulting MAPF instance. However, this approach falls short because the shortest-path distance remains a proxy that ignores interference among agents. Assigning targets based on the costs agents actually pay, which depend on how every other agent is assigned and routed, would yield a better final outcome. To this end, we propose an iterative TAPF method that improves target assignments by calibrating travel cost estimates from fast, suboptimal MAPF feedback. Experiments show that our method produces solutions close to optimal on small instances and outperforms existing planners in solution quality on larger ones.

</details>


### 14. Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations

- **Authors:** Junru Hu, Cheng Tang, Wei Li, Hongze Zhu, Chun-Mei Feng, Qi Zhang, Yirong Chen, Ming Hu
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09382v1](http://arxiv.org/abs/2611.09382v1)
- **PDF:** [https://arxiv.org/pdf/2611.09382v1](https://arxiv.org/pdf/2611.09382v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Weight-Space Programming (WSP) enables reasoning agents to directly inspect and modify neural network parameters, offering an alternative to gradient-based model adaptation. However, its capabilities, cross-task generalization, and practical limitations remain insufficiently understood. We systematically investigate WSP through 16 editing trajectories across seven benchmarks and two model scales (Qwen3.5-0.8B and Qwen3.5-9B). Our findings reveal three key insights. First, WSP can achieve substantial performance gains through highly localized interventions. On full held-out evaluations, accuracy improves by up to 29.45, 4.42, 36.72, and 17.11 percentage points on MATH-500, GPQA Diamond, IFEval, and SciBench, respectively. Notably, modifying only 1,023 parameters yields a 29.45-point improvement. Second, WSP exhibits promising but uneven cross-task generalization. A Math-edited checkpoint improves GPQA Diamond, IFEval, and SciBench by 3.03, 12.18, and 20.10 points, respectively, without further editing, while leaving SciCode performance unchanged. Third, effective editing remains challenging and inconsistent. Outcomes vary substantially across trajectories, and six of the 16 trajectories retain the original weights when candidate improvements cannot be reliably validated. Together, these results highlight WSP's potential for highly localized model adaptation while revealing important challenges in intervention discovery, reliability, and cross-task transfer.
  Homepage: https://wsp-scope.github.io/ GitHub: https://github.com/WSP-Scope/WSP-Scope-Project

</details>


### 15. Enabling Privacy-Preserving Natural Language Access to Industrial Smart Meter Data

- **Authors:** Carlos Martín-Abellán, Mark Kröll
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09372v1](http://arxiv.org/abs/2611.09372v1)
- **PDF:** [https://arxiv.org/pdf/2611.09372v1](https://arxiv.org/pdf/2611.09372v1)
- **Categories:** cs.AI, cs.CL, cs.DB, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Energy management officers and grid operators increasingly rely on smart meter data for anomaly detection, performance monitoring, and strategic decision-making. However, extracting actionable insights from large-scale, heterogeneous telemetry databases requires advanced SQL and data engineering expertise, creating a critical bottleneck for non-technical personnel. Furthermore, the strict data privacy regulations and security constraints inherent to critical energy infrastructure often prohibit the routing of sensitive consumer data through cloud-based Large Language Models (LLMs). To address these challenges, we present OpenMeter, a schema-agnostic Multi-Agent System (MAS) designed to translate natural language queries into executable code and human-readable insights. This architecture lowers the technical barrier for day-to-day utility operations by empowering non-expert personnel to interact with complex databases through intuitive natural language dialogue, transforming raw telemetry into a highly valuable tool for routine grid workflows and strategic decisions. Multi-scenario ablation studies over this environment demonstrate that full multi-agent orchestration shows its largest observed accuracy gains on resource-constrained local hardware (+6.1 pp EX-R over the strongest single-agent configuration); at frontier scale, individual components retain value but should be enabled selectively, indicating that the cost of full orchestration is justified specifically where privacy demands local execution.

</details>


### 16. ReSUM: Reasoning-Driven Multi-Agent Framework for Query-Focused Summarization

- **Authors:**  Sonali, Deeksha Varshney, Asif Ekbal
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09349v1](http://arxiv.org/abs/2611.09349v1)
- **PDF:** [https://arxiv.org/pdf/2611.09349v1](https://arxiv.org/pdf/2611.09349v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLMs excel at language tasks, but long-meeting QFS remains difficult due to complex speaker dynamics, sparse key information, and limited data. Meetings involve disfluencies, long transcripts and complex discourse. QFS have high risk of information omission, hallucination, even for advanced models such as GPT-4-mini and Gemini. Existing end-to-end methods compress retrieval, evidence extraction, and summary generation into a single pass, failing to handle the complex reasoning required for targeted meeting summaries. We propose ReSUM, a modular multi-LLM framework coordinated by a planner that orchestrates retrieval and summarization agents. By distilling teacher reasoning into query- and plan-conditioned retrievers and summarizers, ReSUM enhances long-context robustness, minimizes irrelevant exploration, and generates more faithful and comprehensive query-focused summaries. Experiments show consistent gains on query-focused meeting summarization benchmarks.

</details>


### 17. Towards an Autonomous AI Steward for Large-Scale Physics Experiments: Integrating Causal Diagnostics, RAG, and Conformal Prediction

- **Authors:** Oliver Noll, Nicholas Tan Jerome, Alexander Lehnen, Frank Simon, Frank Maas
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09298v1](http://arxiv.org/abs/2611.09298v1)
- **PDF:** [https://arxiv.org/pdf/2611.09298v1](https://arxiv.org/pdf/2611.09298v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-term particle physics experiments face critical operational challenges: monitoring non-stationary machine data streams and preserving tacit expert knowledge. We present the "Helmholtz Co-Pilot," a hybrid Multi-Agent System (MAS) acting as an autonomous experiment steward. The system can be triggered interactively by human operators or autonomously by an asynchronous causal diagnostics engine that runs independently of the MAS reasoning core. Continuously monitoring live hardware streams such as data acquisition and slow control, this engine performs dynamic causal discovery to trace cascading alarms back to their root causes and applies adaptive model selection to keep forecasts reliable across shifting machine states; upon detecting an anomaly, it hands a structured diagnostic report to the MAS. The reasoning layer itself relies on a high-throughput C++ core and a Python edge architecture orchestrating a directed acyclic graph (DAG) of specialized ReAct workers. It integrates a Retrieval-Augmented Generation (RAG) backbone for institutional memory and leverages conformal prediction to bound its evidence-based recommendations with mathematical coverage guarantees. This extended abstract outlines the architecture, the integration of software-enforced Human-in-the-Loop (HitL) guardrails, and ongoing shadow-testing within the KATRIN experiment.

</details>


### 18. Nudging Decision Models: Do Digital Nudges Steer Fast, Generation-Free AI Agents?

- **Authors:** Sascha Kaltenpoth, Haya Halimeh, Kevin Bösch, Oliver Müller
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09264v1](http://arxiv.org/abs/2611.09264v1)
- **PDF:** [https://arxiv.org/pdf/2611.09264v1](https://arxiv.org/pdf/2611.09264v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents increasingly automate business and consumer tasks but are slow and expensive. Decision models, a new class that chooses among options without generating text, are far faster and less costly. Developers call them "System One models," referencing dual process theory. We ask whether such models can be steered by digital nudges online and whether, as the theory predicts, automatic nudges affect them more than reflective ones. We adapted an online shopping experiment, previously run with humans and LLM agents, to three decision models (Jev, Decision-1, d1). Across 600 runs per model, they chose a preselected default in 97.5-99.9% and a product with social influence information in 75-96% of choices, versus 47-49% in the control. All responded more strongly to the automatic nudge, the opposite of what has been reported for reasoning-capable LLM agents. We provide first evidence that non-generative decision models are susceptible to digital nudges in a System 1 pattern, implying agent-type-specific nudge effects.

</details>


### 19. CARGO: Causal Attribution and Responsibility-Guided Preventive Safe Multi-Agent Reinforcement Learning for Cooperative Driving

- **Authors:** Jingjia Teng, Yang Li, Wenjie Huang
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09139v1](http://arxiv.org/abs/2611.09139v1)
- **PDF:** [https://arxiv.org/pdf/2611.09139v1](https://arxiv.org/pdf/2611.09139v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This study presents Causal Attribution and Responsibility-Guided Optimization (CARGO), a multi-agent reinforcement learning framework for cooperative on-ramp merging in mixed traffic. A shared latent-context posterior and an action-conditioned response model estimate directed behavioral influence, with posterior uncertainty propagated into interaction-edge selection. Complementary attribution mechanisms couple signed influence with marginal team utility for cooperative reward shaping and assign responsibility from positive excess tail risk relative to a safe reference policy. Conditional diffusion generates future responses for action-dependent risk estimation. Responsibility-guided preventive optimization calibrates agent-specific risk-reduction requirements to local capacity within a policy trust region, using reserved safety margins, adaptive requirement scaling, and joint feasibility verification. Theoretical analysis establishes risk monotonicity and sufficient local conditions for non-decreasing environmental return under explicit assumptions. Experiments in highway-env across three traffic densities, together with controlled graph-recovery and attribution studies, support the effectiveness of the framework. Under high-density traffic, CARGO increases the success rate by 66.04\% and reduces the crash rate by 56.23\% relative to the best evaluated baseline for each metric.

</details>


### 20. Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use

- **Authors:** Chuxue Cao, Jingru Zeng, Boqin Yin, Yujin Zhou, Yidan Huang, Sujin Chen, Jinluan Yang, Haoran Li, Yike Guo, Sirui Han
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09113v1](http://arxiv.org/abs/2611.09113v1)
- **PDF:** [https://arxiv.org/pdf/2611.09113v1](https://arxiv.org/pdf/2611.09113v1)
- **Categories:** cs.CR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents can exceed their authorization boundaries while pursuing user goals without an adversary. We formalize this phenomenon as authorization drift across data, tool, scope, and time, and introduce the Authorization Drift Benchmark (ADB): 648 samples across seven domains, each pairing a sufficient compliant path with an attractive unauthorized shortcut. To ensure executable tasks, tempting shortcuts, and feasible compliant paths, Staged Execution-Reflective Synthesis (SERS) grounds benchmark validation in real agent rollouts rather than LLM self-critique. Across 13 LLMs and three frameworks (25,207 trajectories), greater capability accompanies greater drift, with frontier-capable models exhibiting drift rates of 0.43 to 0.61. Yet 86.18% of tasks admit an observed clean-success trajectory, showing that drift is avoidable. Drift is persistent and dominated by early data over-collection; apparent improvements under agentic scaffolds coincide with collapsing clean-completion performance. To understand potential harms to individuals and society, we map drift points to legal provisions across four jurisdictions, connecting overreach to privacy and information-security concerns. Data minimisation is the most frequently implicated provision, and 93.5% of legally grounded drifting runs map to multiple jurisdictions, making the potential consequences of authorization drift more interpretable.

</details>


### 21. When Routine Operations Break Architectural Pattern Relationships in LLM Agent Harnesses

- **Authors:** Boming Xia, Qinghua Lu, Dino Sejdinovic, Liming Zhu
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09088v1](http://arxiv.org/abs/2611.09088v1)
- **PDF:** [https://arxiv.org/pdf/2611.09088v1](https://arxiv.org/pdf/2611.09088v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agent harnesses distribute tool mediation, state management and safety guardrails across native services, independently written plugins and configuration. Routine operations can change the runtime order or retained state that architectural pattern relationships require, without any code change. We study five relationships associated with the Guardrail Enforcement Point, Autonomy Controller and Blackboard patterns across five released harnesses, analysing a main sample of fourteen independently written plugins. Using PatternOps, our assessment procedure, we trace requirements from pattern descriptions, provider documentation and deployment profiles to the providers that realise them and the records that decide them. We then compare alternative allocations under supported operations. Such operations broke relationships silently: after a plugin was reapplied or an allow rule saved, policy stopped evaluating edits while every plugin stayed active, and a prohibited edit executed. Which alternatives qualified depended on the requirement. Allocations that kept the required order, or kept or rebuilt the needed state, held on their tested paths and operation sequences, while others prevented prohibited effects but missed edits rejected elsewhere. In these harnesses, a pattern relationship is a property of the running system and its history, so architects should evaluate it against the decision paths, state lifetimes and operation sequences their deployments use.

</details>


### 22. From Emergence to Reversibility: Toward Reversible Multi-Agent Systems

- **Authors:** Zhengye Han, Linda Ng Boyle
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09054v1](http://arxiv.org/abs/2611.09054v1)
- **PDF:** [https://arxiv.org/pdf/2611.09054v1](https://arxiv.org/pdf/2611.09054v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems become capable through institutional mechanisms, such as rules that route information to agents that act on it. These mechanisms are also natural places to restrict the system. Yet as agents learn, share memory, delegate, and repair failures, the collective can find other paths to the same effects: a restriction on the original mechanism still operates but no longer stops them, while routine performance and compliance checks pass. We propose \textbf{Reversible Multi-agent Systems} as a research agenda: collectives that grow while an authorized supervisor can still restrict specified effects, keep them restricted as agents adapt, and reconstitute useful cooperation under renewed authority. What is reversed is the ability to produce a specified effect; restrictions must hold even if learned knowledge persists. The goal is to preserve effective intervention, not a particular mechanism: at every step of growth, some authorized intervention must keep a specified prohibited effect rare while maintaining required service. We identify three research problems: tracking what capabilities depend on, handing off control before an old mechanism loses its effect, and separating legitimate repair from unauthorized reconstruction. We outline how to evaluate control across growth paths, back control claims with evidence, and allocate the rights to restrict and restore.

</details>


### 23. ToolDex: An Ego-Exo Human Demonstration Dataset for Creative Physical Tool Use

- **Authors:** Mohamed Elmoghany, Kehan Li, Ruoqu Chen, Tarun Chiruvolu, Shutong Zhang, Ryan Wang, Stephen Tian, Yaru Niu, Michelle Guo, Ding Zhao, Weiyu Liu, Mengdi Xu, Li Fei-Fei, Jiajun Wu
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.09036v1](http://arxiv.org/abs/2611.09036v1)
- **PDF:** [https://arxiv.org/pdf/2611.09036v1](https://arxiv.org/pdf/2611.09036v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Creative tool use is a fundamental human capability and an important step toward general-purpose embodied intelligence. It requires agents to reason about object affordances, physical constraints, and manipulation strategies, especially when standard tools are unavailable. However, progress in this area is limited by the lack of real-world datasets that capture human tool-use behavior with sufficient scale, fidelity, and diversity. Existing benchmarks are often simulation-based, focus on simplified interactions, or lack detailed observations and annotations.
  We introduce ToolDex, a large-scale egocentric-exocentric (ego-exo) human demonstration dataset for creative physical tool use. ToolDex captures scenarios in which humans select, adapt, and repurpose available objects as tools. Using synchronized egocentric cameras and eight exocentric cameras, the dataset provides high-fidelity multi-view observations and rich annotations for hands, tools, target objects, and their deformable interactions. Beyond data collection, we establish a benchmark suite characterizing three core capabilities: physical tool-use reasoning, sparse-view 3D and 4D reconstruction, and robot policy learning. ToolDex provides a foundation for studying human tool-use behavior and developing embodied agents that can adaptively use tools in complex real-world environments.
  Dataset visualizations and benchmarking results are available at https://tooluse-dataset.github.io/.

</details>


### 24. Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making

- **Authors:** Disha Sheshanarayana, Rajat Subhra Pal, Manjira Sinha, Tirthankar Dasgupta
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08971v1](http://arxiv.org/abs/2611.08971v1)
- **PDF:** [https://arxiv.org/pdf/2611.08971v1](https://arxiv.org/pdf/2611.08971v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems increasingly aggregate judgments across model instances, but reasoning about other agents can itself introduce failure. We study a setting in which LLMs shift their public decisions after observing ambiguous social signals while reporting inaccurate estimates of what other agents privately judged, even when the group's recorded private judgments do not support the apparent consensus. We call this failure phantom consensus and study it as a pluralistic-ignorance-style pattern in controlled LLM collectives. To measure this phenomenon, we introduce PHANTOM-Bench, a benchmark that separates isolated private judgments, public decisions after ambiguous social signals, elicited estimates of the group's private judgment, transparency-based recovery, and controls for neutral public text and explicit vote-following. Across nine closed- and open-weight models, ambiguous public signals consistently degrade decision quality and can turn correct private group judgments into incorrect public collective outcomes. Public accuracy drops by as much as 47.8 percentage points, and collective rationality failures reach 47.3% in the most susceptible setting. We observe substantial errors in reported group-private beliefs alongside public-stage failures, while control conditions reveal model-dependent differences in susceptibility to ambiguous and explicit peer signals. Revealing the agents' recorded private decisions repairs many failures without revealing the gold label, although recovery varies across models. Our results show that evaluating multi-agent LLM systems requires measuring not only final agreement, but whether that agreement reflects independently measured private judgments or an apparent consensus.

</details>


### 25. AIM: Adaptive Interaction in Multi-Agent Debate for Multimodal LLM Inference

- **Authors:** Wei Fan, JinYi Yoon, Bo Ji
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08950v1](http://arxiv.org/abs/2611.08950v1)
- **PDF:** [https://arxiv.org/pdf/2611.08950v1](https://arxiv.org/pdf/2611.08950v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-Agent Debate (MAD) improves reasoning on multimodal tasks, but its accuracy and token efficiency depend on how agents interact during debate. A largely overlooked design choice is which interaction modalities agents use to exchange evidence. Existing methods rely on fixed text- or graph-based interaction, which fails to convey fine-grained multimodal evidence and thus degrades accuracy while inflating token cost due to verbose descriptions. To address this, we propose Adaptive Interaction in Multi-Agent Debate (AIM), an adaptive routing framework that dynamically selects the optimal modality combination for inter-agent interaction in multimodal MAD. Beyond text and graph, AIM introduces task-dependent modality interaction, where agents exchange targeted regions of interest from the task-specific multimodal input, such as image regions, audio segments, or spatio-temporal video clips. To determine the best combination for each instance, AIM first generates a structured baseline response and extracts interpretable routing features that capture which evidence the instance requires, how confident the baseline agent is, and how much new evidence each modality would add beyond the baseline response. A lightweight router then uses these routing features to select a modality combination that avoids both under-fusion (i.e., agents miss decisive evidence) and over-fusion (i.e., redundant modalities inflate token cost) risks. Across eight benchmarks spanning three multimodal task families, \name achieves the highest accuracy. Combining modalities improves accuracy by up to 6.4\% over the best single-modality baseline, and adapting the combination per instance adds up to 4.2\% over the most accurate fixed combination of each benchmark with up to 53.4\% fewer tokens.

</details>


### 26. More with Less: Efficient Parallel Scientific Code Translation via an Agent-Skill Workflow

- **Authors:** Jianuo Shen, Pengyi Xu, Bo Zhang
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08947v1](http://arxiv.org/abs/2611.08947v1)
- **PDF:** [https://arxiv.org/pdf/2611.08947v1](https://arxiv.org/pdf/2611.08947v1)
- **Categories:** cs.DC, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Translating parallel scientific codes between HPC programming frameworks is a critical but labor-intensive task. Existing LLM-based approaches rely on fixed sequential pipelines with undifferentiated repair strategies and correctness criteria that do not match scientific computing practice. We present an agent-skill framework that separates translation, compilation diagnosis, and execution validation into three autonomous agents coordinated by a verdict-driven orchestrator, routing each failure to a targeted repair skill rather than retrying blindly. An automated output check drives the self-correction loop, complemented by an offline LLM-based verification that exposes false positives escaping compiler and runtime checks. We evaluate the framework on 30 HeCBench kernels translated bidirectionally among CUDA, OpenMP, and SYCL with three open-source LLMs. Our framework attains the higher verified correctness rate in all 18 model and direction combinations over a state-of-the-art baseline while consuming up to 52.4% fewer tokens, remaining consistent across models and directions without architectural modification.

</details>


### 27. Glyph: An Interpretability Engine for AI-Driven Scientific Discovery in Clinical Data

- **Authors:** Robbie Holland, Ashwin Kumar, Mateus A. Esmeraldo, David Le, Andrea Fisher, Jiazhen Pan, Louisa Fay, Magdalini Paschali, Vasiliki Sideri-Lampretsa, Ates Fettahoglu, Stefania Moroianu, Philipp Wesp, Ivan Lopez, Tom Nuno Wolf, McKenzie S. White, Eduardo Pontes Reis, Fatima Rodriguez, Curtis P. Langlotz, Vasilis Syrgkanis, Imon Banerjee, Akshay S. Chaudhari, Sergios Gatidis
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08922v1](http://arxiv.org/abs/2611.08922v1)
- **PDF:** [https://arxiv.org/pdf/2611.08922v1](https://arxiv.org/pdf/2611.08922v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated scientific discovery has the potential to advance understanding of disease mechanisms and accelerate identification of early disease markers. Manual data annotation is infeasible at population scale, motivating methods that automatically extract pre-defined phenotypes in multimodal and unstructured clinical data. Such pre-defined feature sets determine and limit which associations these approaches can discover. This limitation extends to agentic AI systems that use these tools to query population-scale data. In contrast, foundation models (FMs) trained on large volumes of clinical data can perform tasks beyond their training objectives. This suggests their latent embeddings may represent novel or unexplored features that could yield insights into disease mechanisms, yet such latent features remain difficult to interpret. To address this challenge, we introduce Glyph, an automated multistage framework that extracts features from multimodal and unstructured clinical data using FMs and sparse autoencoders, interprets them as coded clinical concepts, and evaluates their value for clinical scientific discovery. We applied Glyph to abdominal CT volumes, CT radiology reports and laboratory measurements from 41,628 patients across different institutions. We identified 397 predictive concepts supported by 4,463 Bonferroni-significant associations. Moreover, a majority of discovered associations were automatically reproducible in held-out cohorts across different sites. Glyph concepts provided complementary associations to literature-derived markers, leading to gains in predictive power. We envision that interpretability can extend beyond a mechanistic understanding of neural networks to connecting implicitly learned features with clinical knowledge and establishing their significance for patient outcomes. We release Glyph at https://github.com/StanfordMIMI/Glyph.

</details>


### 28. I Think, Therefore I Attack: Evaluating Thought Injection Attacks on Reasoning Agents

- **Authors:** Parth Illendula, Garik Livingston, Zain Shamsi, Ravi Srinivasan, Alex Liu
- **Published:** 2026-11-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08811v1](http://arxiv.org/abs/2611.08811v1)
- **PDF:** [https://arxiv.org/pdf/2611.08811v1](https://arxiv.org/pdf/2611.08811v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Reasoning Models (LRMs) are one of the key components of current agentic systems. LRMs augment their output with an explicit chain-of-thought reasoning stage, introducing a new attack surface for thought injection, in which untrusted text resembling the model's own deliberation is fed back to the model. We present a two-part study of this attack, performed against the prevailing large, production class open-weight models (e.g., GLM-5.3, MiniMax-M2.5, Qwen3.8-Flash-Next). We first evaluate the effectiveness of static thought-injection prompts under different styles as well as tagged and untagged conditions and find that the effects of thinking tags and payload styles are all properties of the specific target model. In the second study, we exploit this model-specificity in a containerized agentic cyber range, using indirect injection prompts styled in the form of the target model's own reasoning traces to achieve attack success rates (ASR) up to 50% on operational objectives such as reverse-shell exfiltration and repository backdooring. We also find that the same malicious objective in standard prompt injection user voice never succeeds, and thinking tags suppress the agent's tendency to disclose the injection. Our results show that imitating a reasoning model's own thought style is effective for this style of attack, and that tag stripping is an unreliable defense.

</details>


### 29. Aligning, Fast and Slow: A Control-Theoretic Oversight Framework for Long-Horizon Trajectories and Maintained Deployments

- **Authors:** Stephen Peng, Vineet Jagadeesan Nair, Noah Broestl, Anne Friederike Kleppe, Steven Mills, Adi Zolotov
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08781v1](http://arxiv.org/abs/2611.08781v1)
- **PDF:** [https://arxiv.org/pdf/2611.08781v1](https://arxiv.org/pdf/2611.08781v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can pass checks on individual tasks while retaining memory or code changes that alter their later behavior. We introduce a control-theoretic framework that couples a fast loop controlling proposed actions with a slow loop reviewing persistent changes and reassessing configurations after model or tool updates. When measurement errors and changes between checks are bounded and controllers can enforce their decisions, we derive a deployment-level bound and a rule for dividing review effort. In simulation, dividing a fixed review budget between both loops reduces mean maximum departure from intended behavior roughly twelvefold compared with review confined to individual runs. In coding stress tests with authored memories and five matched seeds, combined controls reduce mean severity on a 0-3 scale from 0.325 without gates to 0.117, resolving 33 of 120 issues versus 35 without gates; in trading stress tests, combined controls reduce mean shortfall in low-emission purchases from 0.892 without gates to 0.107. The overall framework helps developers and auditors compare and enforce oversight designs, while the agent studies test component controls rather than the full deployment-level guarantee.

</details>


### 30. Conflux: Preventing Privilege Escalation with Principal Contexts and System-Level Evaluation

- **Authors:** Raya Buckley, Christian Schroeder de Witt
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08768v1](http://arxiv.org/abs/2611.08768v1)
- **PDF:** [https://arxiv.org/pdf/2611.08768v1](https://arxiv.org/pdf/2611.08768v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents combine information from multiple principals while acting externally. We formalise privilege escalation (PE) as the system-level security objective: an action may proceed only if every principal that influenced it would allow it. Model-level defences remain probabilistic, so enforcement must sit outside model judgement. We present Conflux, a principal-context defence. Its kernel, ITES, derives authority from provenance and the organisation's existing access-control system and intersects the permissions of every influencing principal. We prove a conditional authority-confinement theorem: under complete mediation, no-laundering provenance, a known non-empty decision context, fresh permission checks, and action binding, the kernel admits no action that escalates privilege with respect to any recorded influencing principal. The theorem covers the represented value-influence fragment; control influence from tool, branch, recipient, or plan-step selection remains a refinement obligation. Conflux extends the kernel with independent policy ports, argument-aware authorisation, disclosure, consent, delegation, restriction, and exposure planning. We describe two system- level evaluators. SLED is a black-box evaluator: it exhaustively explores a declared finite model of a defence up to a bound. SLED-V is a white-box evaluator: it checks a serialisable intermediate representation against security and provenance properties. The evidence is bounded and partial. The appendix reports retained AgentDojo, SLED, and SLED-V results, including the limits of those runs. No result in this paper is an unbounded deployment guarantee.

</details>


### 31. Debate to Deceive: Poisoning LLM's Fact-Checking via Game-Theoretic Multi-Agent Debate

- **Authors:** Liting Huang, Huizhi Liang, Yi Lei, Xingjun Ma, Varun Ojha
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08756v1](http://arxiv.org/abs/2611.08756v1)
- **PDF:** [https://arxiv.org/pdf/2611.08756v1](https://arxiv.org/pdf/2611.08756v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Knowledge attacks on Large Language Models, such as manipulating fact-checking judgments, pose significant risks to AI reliability. Existing approaches -- adversarial suffix/template injection and single-agent self-reflection -- lack robustness across diverse defenses and are prone to confirmation bias and costly trial-and-error, respectively. We propose Debate-to-Deceive (D2D), a multi-agent debate framework grounded in human debate structure and rhetorical style, enabling agents to generate adversarial passages that are semantically coherent, rhetorically effective, and resistant to early confirmation bias. D2D formalizes the adversarial process as an evolutionary game in which agents adaptively evolve their rhetorical strategies (Logos, Pathos, Ethos) through competition. To manage the intractably large LLM output space, we decouple agent behavior into a strategic layer, which selects a rhetorical action from a compact strategy space via evolutionary-inspired learning dynamics, and a generation layer, where the LLM produces a concrete passage conditioned on that strategy and the debate context. On four fact-checking benchmarks (FEVER, HealthVer, CLIMATE-FEVER, and SciFact), D2D substantially outperforms existing attacks and evades most defenses.

</details>


### 32. Memory-Aware Multi-Agent Architecture with LLM-based Orchestration for Conversational Recommendation

- **Authors:** Emilly Pitman de Castro, Vanessa Silva, Gustavo Kanno, Marcus Santos, Bruno Ferraz do Amaral, Marcelo Nogueira, Lucas Francisco Pellicer, Lucas Lanaro, Pedro Augusto Luiz, João Renato Ribeiro Manesco, Giovanni Carbinatti, Isabela de Lima Santos, Lucas Oliveira Jeronymo, Jeison Fappi, Raul Rotilli Aguirre, Fabio André Frantz, Renata De Paris, Fabiana Marucci, Lohan Silva, Vinicius Diniz Reolon, Wandemberg Gibaut
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08718v1](http://arxiv.org/abs/2611.08718v1)
- **PDF:** [https://arxiv.org/pdf/2611.08718v1](https://arxiv.org/pdf/2611.08718v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Conversational recommender systems often treat user sessions in isolation, limiting their ability to capture how user intent evolves over time. While large language models (LLMs) have improved semantic understanding, they are typically used as isolated components, without addressing how memory, retrieval, and decision-making should be integrated at the system level. In this work, we propose a memory-aware multi-agent architecture for conversational recommendation, in which LLMs act as orchestration layers that coordinate intent refinement, query construction, and interaction flow. A key design principle is the integration of long-term memory as a first-class component, influencing both routing decisions and semantic query formation. We evaluate the system through cross-session memory experiments, multi-turn conversational simulations, and supervisor-driven interaction studies on the Amazon Reviews dataset. Results show that memory-enabled interactions recover up to 63\% of the gap toward explicit-query scenarios and prevent semantic degradation in extended dialogues. In addition, supervisory orchestration increases user acceptance by +28.9 percentage points, highlighting the importance of structured orchestration in guiding interaction and output quality. We also observe an exposure bottleneck between retrieved candidates and displayed recommendations. While LLM-reranking does not improve Hit@K, it consistently enhances semantic consistency and diversity. To capture these effects, we introduce the Semantic Consistency Score (SCS), a complementary evaluation measure. Overall, the results emphasize the importance of system-level design choices, suggesting that effective conversational recommendation benefits from explicit memory integration, orchestration, and evaluation beyond traditional ranking metrics.

</details>


### 33. Decision Context: Persistent Behavioral Learning for AI Agents

- **Authors:** Nima Vahdat, Pashootan Vaezipoor
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08644v1](http://arxiv.org/abs/2611.08644v1)
- **PDF:** [https://arxiv.org/pdf/2611.08644v1](https://arxiv.org/pdf/2611.08644v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents do not learn from corrections across sessions. A user fixes the same mistake at the start of every conversation. Existing agent memory systems primarily handle facts, such as preferences, entities, and conversational history, rather than procedural knowledge.
  We present Forge Decision Context (forge_dc), a system that captures behavioral signals from human corrections and self-assessed tool-call failures, compiles them into imperative RULE directives, and injects them at the decision points where they apply. We evaluate forge_dc alongside four predecessor approaches on DC-Bench, a new benchmark of 71 scenarios across nine behavioral dimensions, built from real executed agent traces in a deterministic mocked-tool environment. forge_dc reaches 95% compliance, up from 55% with naive retrieval, while injecting approximately 10 times fewer tokens per query.
  Across the five-stage progression, the strongest systems represent behavioral memory as explicit directives and deliver it at the decision points where it applies. The results identify representation, activation, and placement as central design choices for persistent behavioral learning.

</details>


### 34. s$^3$: Simple Scaling of Swarms via Cooperative Multi-agent RL

- **Authors:** Kunal Jha, Gonçalo Faria, Shuyue Stella Li, Scott Geng, Faeze Brahman, Noah A. Smith, Yulia Tsvetkov, Max Kleiman-Weiner, Natasha Jaques
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08615v1](http://arxiv.org/abs/2611.08615v1)
- **PDF:** [https://arxiv.org/pdf/2611.08615v1](https://arxiv.org/pdf/2611.08615v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Groups can achieve more than individuals in the same amount of time, but only if their members coordinate: they must decide who works on what and what to share. However, this organization in multi-agent systems today usually comes from arbitrary, static harnesses designed a priori without adapting to agent behaviors or task specifications. We ask whether agents can instead learn to organize themselves. We introduce s$^3$, the first multi-agent reinforcement learning method in which agents decide for themselves how long to work alone and when to share findings or read teammates' messages, with no predefined organization or roles. Our s$^3$ agents learn to take different approaches, read each other's work, exhibit emergent roles that complement each other in the swarm, and generalize to bigger teams. We study both coordination, where agents must combine private information, and parallel exploration, where sharing discoveries can make search more efficient. With matched training and inference budgets, s$^3$, swarms evaluated with twice as many agents as in training solve over 25$\times$ more coordination problems than the strongest baseline, and in exploration, communicating agents reduce repeated work by nearly 50% and outperform best-of-N by up to 9.4 percentage points. Rather than being designed in advance, s$^3$ enables organization to emerge from a shared goal. This opens the door to capable systems built from many models that learn to work together.

</details>


### 35. NormGym: Evaluating Normative Competence through Social Interaction

- **Authors:** Binze Li, Zihuan Zhang, Seokhyun Baek, Gillian K. Hadfield, Tianmin Shu
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08613v1](http://arxiv.org/abs/2611.08613v1)
- **PDF:** [https://arxiv.org/pdf/2611.08613v1](https://arxiv.org/pdf/2611.08613v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Normative competence, the ability to infer socially enforced expectations from interaction and adjust behavior accordingly, is essential for agents operating in unfamiliar human communities. Yet existing evaluations largely test whether agents can recognize or apply norms they may already know, rather than whether they can acquire previously unknown norms from social interaction. We introduce NormGym, an interactive benchmark for normative competence in which a newcomer must infer a hidden, arbitrary norm while pursuing its own task in a multi-agent community. Success requires distinguishing what is possible from what is permitted, inferring the norm from observed behavior and sanctions, and applying it in new situations. NormGym contains diverse norms and distinct environments, allowing systematic evaluation of current agents, including large language model (LLM) agents. We find that normative competence remains challenging: the strongest evaluated LLM achieves a joint task-and-compliance success rate of 55.3%. Our analysis reveals that models can sometimes revise their behavior following sanctions for their own actions, but struggle to use other agents' behavior and the sanctions they receive to infer the underlying norm. We further find that fine-tuning models may be insufficient to improve normative competence. These results suggest that current models lack a robust, transferable capability for acquiring normative knowledge through social interaction.

</details>


### 36. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization

- **Authors:** Qile Jiang, George Em Karniadakis
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08483v1](http://arxiv.org/abs/2611.08483v1)
- **PDF:** [https://arxiv.org/pdf/2611.08483v1](https://arxiv.org/pdf/2611.08483v1)
- **Categories:** cs.AI, cs.NE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow because the LLM generates a long textual chain of thought for each round and must repeat this generation many times to maintain population diversity. We present SwarmEvolve, a framework in which hundreds of low-cost agents per round work in swarms, reason in latent space without decoding to text, and share information by passing KV caches. Each swarm studies the problem from a different angle. A novelty filter keeps the most distinct agent ideas by directly measuring the distances between the agents' hidden state vectors. Crossover of ideas happens naturally in latent space, as a summarizer agent receives the combined KV caches of all swarm members. On 21 problems in mathematical discovery and scientific computing, SwarmEvolve gets the highest average score and needs a median of only 3 to 8 minutes to reach the best scores that other state-of-the-art frameworks reach in 60 minutes. On several problems, SwarmEvolve with Qwen3 8B improves on the solutions that AlphaEvolve first found with frontier LLMs. Our work shows that agent swarms that communicate in latent space offer a fast, low-cost approach to program search for scientific problems.

</details>


### 37. SCALE: Real-Time Latent Communication for Cyber-Physical Agents

- **Authors:** Shanghao Shi, Jian Xiao, Ching-Hsiang Chan, Sanjoy Baruah, Sastry Kompella, Yevgeniy Vorobeychik, William Yeoh, Ning Zhang
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08390v1](http://arxiv.org/abs/2611.08390v1)
- **PDF:** [https://arxiv.org/pdf/2611.08390v1](https://arxiv.org/pdf/2611.08390v1)
- **Categories:** cs.RO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Latent communication enables agents to collaborate efficiently by directly exchanging intermediate model representations rather than raw sensor data or text messages. Existing approaches, however, are primarily designed for LLM agents and do not consider the bandwidth constraints and heterogeneous task deadlines faced by cyber-physical agents. In this work, we propose SCALE, a real-time latent communication method tailored for cyber-physical agents. Motivated by the spatio-temporal continuity of the physical world, SCALE matches tokens across consecutive latent messages using similarity scores to identify reusable information and avoid redundant transmission. It then profiles the semantic gain and communication cost of transmitting different amounts of latent information. Based on these profiles, SCALE employs a real-time scheduler that jointly determines which pending messages to transmit and how many latent tokens to send, subject to available bandwidth and task deadlines. We evaluate SCALE across three cyber-physical benchmarks and a physical spider robot case study under diverse network conditions and heterogeneous task deadlines. Our results show that SCALE significantly improves both task performance and on-time delivery in bandwidth-constrained networks. Our code is available at: https://anonymous.4open.science/r/SCALE-4E80/.

</details>


### 38. Enhancing Local and Global Structure in Compressed AI Agent Memory

- **Authors:** Henry Han
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08341v1](http://arxiv.org/abs/2611.08341v1)
- **PDF:** [https://arxiv.org/pdf/2611.08341v1](https://arxiv.org/pdf/2611.08341v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents store text as embedding vectors and compress them at scale. A compression is accepted when each item's nearest neighbors survive, but agents also consolidate, delete, and compare memories, tasks that depend on which items lie far apart. We evaluate both ends with two label-free fidelities from our prior work: the local fidelity $L$ at 10 neighbors and the global fidelity $G$ at 30 to 50 percent of the memory. At 96 bytes per passage, rescored binary codes reach an $L$ of 0.97 yet move 10.1 percent of passages to another theme; PCA with 8-bit codes, at an $L$ of 0.77, moves 1.7 percent. Rescoring leaves the stored codes, and thus $G$, unchanged. We prove that across the $G$ band, $1-ν_k$ is at most 2 to 2.18 times the square root of the near-far rank-violation rate, and that this rate follows the distance noise of the compression (correlation 0.979). Our locality-aware quantization (LAQ) turns the bound into a hinge objective on the codebooks of an OPQ index, keeping its bytes, rotation, and search. To our knowledge, LAQ is the first quantizer whose objective comes from a proven bound on the far end. Reconstruction alone raises $G$ in 0 of 52 held-out runs; the far hinge raises it in all 52. LAQ raises $G$ in all 52 ($p=8.5\times 10^{-4}$ over 13 memory-encoder groups), including the external FinDER memory, has the highest $G$ of seven equal-size quantizers in all 12 Multi-Doc-2025 runs, scales to a million passages, and keeps evidence recall.

</details>


### 39. Trilemma: How Agents choose between Honesty, Confidentiality, and Task Completion

- **Authors:** Johannes Taraz, Abhinav Kumar, Sahar Abdelnabi
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08312v1](http://arxiv.org/abs/2611.08312v1)
- **PDF:** [https://arxiv.org/pdf/2611.08312v1](https://arxiv.org/pdf/2611.08312v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Personal AI agents often act on underspecified instructions and draw on context such as their user's messages and calendar to decide how to proceed. This context can contain private preferences that interfere with the task, with other people's interests, or with confidentiality norms. Prior work has studied deception under goal conflicts and the leakage of private information, but largely as separate problems. We study both problems together in a simulated company Slack workspace in which four employees delegate sprint staffing to personal agents. Two agents learn from private messages that their employee avoids working with a particular colleague. Because the other agents request justifications for task preferences and the only true justification is confidential, the agents cannot simultaneously remain honest, preserve confidentiality, and complete the staffing. We evaluate seven open-weight models and Claude and GPT models. Of the 135/140 open-weight agents that pursue the avoidance preference, 107 either make false claims about task fit or logistics or cite a true consideration as if it were their actual reason. In a three-model comparison, confidentiality instructions reduce disclosure of the preference from 83% (none) to 31% (medium) to 2% (strong). However, the task is often not completed anyway; in the main experiment (medium confidentiality instructions), only 16 of 70 runs end with a valid staffing. In their reasoning traces, agents frequently acknowledge evidence against their claims and still conclude that the claims are not false; they engage in motivated reasoning. Our results indicate that agents can strategically make false or misleading claims in a day-to-day task without being instructed to; the environment provides a controlled testbed for studying how agents resolve such conflicts and for developing deception monitors.

</details>


### 40. Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks

- **Authors:** Zhitao He, Chi Him Zhang, Chengru Han, Yi R Fung
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08281v1](http://arxiv.org/abs/2611.08281v1)
- **PDF:** [https://arxiv.org/pdf/2611.08281v1](https://arxiv.org/pdf/2611.08281v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA, an interactive benchmark comprising 608 expert-designed tasks grounded in real-world fraud cases, covering 14 domains and 152 attack scenarios with prepared multimodal content. The tasks span four difficulty levels and reflect the distinct social and cultural contexts of Chinese and English environments. Agents inspect content, verify requests, and execute actions in simulated applications, with attack outcomes grounded in verifiable tool execution logs. To enable controlled red teaming of personal agents, we design a multimodal attack harness that integrates task information, attack progression control, and multimodal content construction to evaluate their intrinsic security against adaptive social engineering attacks in simulated environments. Evaluating seven widely used multimodal models across six dimensions reveals that all are vulnerable, with attack success rates of 7.1% to 34.5%. Adding multimodal content increases attack success from 19.9% to 29.2%, despite increased proactive verification coverage. Stronger safety instructions reduce attack success without improving recognition of deceptive multimodal content, while lower attack success rates for some models accompany excessive refusal of legitimate requests.

</details>


### 41. SMART: State-based Multi Agent Reasoning Traces for Verification-oriented Problem-Solving

- **Authors:** Sai Vallurupalli, Francis Ferraro
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08196v1](http://arxiv.org/abs/2611.08196v1)
- **PDF:** [https://arxiv.org/pdf/2611.08196v1](https://arxiv.org/pdf/2611.08196v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Complex problems with limited context, such as claims, require a means to obtain additional knowledge necessary for solution reasoning. We propose a multi-agent framework, SMART, to obtain knowledge through capturing the implicit state of participating entities in a problem context. SMART curates the state knowledge as diverse, complementary and solution-salient premises using a variety of LLMs and a structured role-based prompt strategy. Using knowledge from these real-world verified curated premises, SMART's knowledge guided solution reasoning improves validation performance up to 20% on complex scientific claims spanning 3 datasets. We show that grounding premises in real-world knowledge is necessary and improves performance up to 5%.

</details>


### 42. PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?

- **Authors:** Yue Zhang, Jilei Sun, Liqiang Jing, Yijie Wei, Ruohan Yang
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08175v1](http://arxiv.org/abs/2611.08175v1)
- **PDF:** [https://arxiv.org/pdf/2611.08175v1](https://arxiv.org/pdf/2611.08175v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automating printed circuit board (PCB) routing requires coordinating board-level connectivity decisions with geometric execution under strict design rules. Although recent agents can interact with native routing tools, reliable routing on complex boards remains challenging. We present PCBRouteAgent, a multimodal PCB routing agent inspired by how human engineers coordinate global strategy with local execution. A Global Routing Planner combines board images and structured electrical and geometric information to specify connection topology, routing order, corridors, and layer transitions. A Detailed Routing Executor realizes these guides through KiCad's native routing engine and performs bounded local recovery. Unresolved failures are returned as structured feedback, enabling targeted guide revisions while preserving accepted routes. We evaluate PCBRouteAgent on 247 synthetic and real-world boards from four PCBWorld-Bench test splits. It achieves clean-pass rates of 100%, 94.9%, 100%, and 40% on D2, D3-A, D3-B, and D3-C, respectively. On the three real-world subsets, PCBRouteAgent outperforms the best evaluated baseline in clean-pass rate by 13.9, 36, and 10 percentage points, respectively.

</details>


### 43. Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning

- **Authors:** Zuo Gou, Chenhao Lu
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.08144v1](http://arxiv.org/abs/2611.08144v1)
- **PDF:** [https://arxiv.org/pdf/2611.08144v1](https://arxiv.org/pdf/2611.08144v1)
- **Categories:** cs.RO, cs.LG, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Robot reinforcement learning increasingly runs environments outside the trainer: in another process, on another machine, in another language. Many faults at this boundary raise no error. We make the boundary a wire protocol and ask what notices a fault in it.
  On Pendulum, HalfCheetah, Hopper and a 7-joint arm (Pusher), we injected up to 23 faults into what crosses the wire and 2 into the trainer's log, from one value to every value. Unless every value was wrong, a learning-curve threshold caught at most one run in ten, and a comparison with ten fault-free seeds at most 21%. A clean evaluation of all 1,060 final policies agreed with the curves: of the 728 boundary-fault runs both curve checks passed, 723 scored no more than three standard deviations below fault-free seeds, though nearly all ended on other weights and, for reward faults, logged other returns.
  Checks of the run itself, not of its outcome, saw every fault. A step ledger kept on both sides and compared step by step caught and located every fault that crossed, on Pendulum, Hopper and Pusher on one machine and on Pendulum across two, with no fault-free run and, on Pendulum, a median 3% more training time. An episode record kept at the environment caught the faults in the trainer's log. We list such faults found in practice, in Gymnasium 1.3 and our own code and, reported by others, in five multi-agent libraries, and recommend a step ledger and episode counts kept at the environment.

</details>


### 44. SEER: A Scalable Event-Driven Runtime for Parallel Execution of Multi-Agent Reinforcement Learning Environments

- **Authors:** Jiming Su, Feng Zhu, Yuhao Xiao, Miao Zhang
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07996v1](http://arxiv.org/abs/2611.07996v1)
- **PDF:** [https://arxiv.org/pdf/2611.07996v1](https://arxiv.org/pdf/2611.07996v1)
- **Categories:** cs.DC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) is increasingly used in systems where many entities interact in a shared environment. In these workloads, policy inference can be batched on GPUs, but the CPU-side environment path still updates entity states, resolves local interactions, and builds observations inside each $\mathrm{env.step}$. This path can dominate latency in interaction-intensive workloads after policy batching. Existing vectorized environment interfaces and general event-driven runtimes do not directly address the fine-grained cross-entity work inside one bounded MARL step while preserving the step-level semantics expected by learning systems. We present SEER (Scalable Event-Driven Environment Runtime), a runtime for MARL environment execution under an explicit event-locality contract. SEER models each environment step as a bounded stream of timestamped events. If direct state updates are entity-local and cross-entity effects are represented as ordered future events, SEER can run independent events in parallel while preserving serial-equivalent boundary outputs. To make this contract practical, SEER uses a CAS-based dual-layer event queue: local event queues preserve per-entity causal order, while a parallel executive list exposes ready work to global worker threads. SEER further uses STPA, a preflight-guided thread-pool selection mechanism that combines short runtime traces with static workload and hardware features. We evaluate SEER on two parameterized MARL workloads: compute-intensive UAV swarm control (Aircraft) and communication-intensive wireless management (PCS). On Aircraft, SEER reduces inference latency by 16.2\% over the baseline. On PCS, SEER reduces environment-execution latency by 46.9\%, 19.5\%, and 64.9\% over ROSS-T, NBSE, and ROOT-Sim, respectively.

</details>


### 45. QRAE: Query-Relevant Attention Entropy for Context Compression in DeepSearch Agents

- **Authors:** Yingjie Tan, Haiquan Qiu, Quanming Yao, Manyi Zhong, Xianzhi Yu, Yaqing Wang
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07976v1](http://arxiv.org/abs/2611.07976v1)
- **PDF:** [https://arxiv.org/pdf/2611.07976v1](https://arxiv.org/pdf/2611.07976v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

DeepSearch LLM agents repeatedly search and carry retrieved sources into subsequent reasoning steps. This expanding context increases token consumption and latency, although many results do not contribute to later reasoning. We propose Query-Relevant Attention Entropy (QRAE), an online context compression method that uses sparse evidence-assessment heads to decide which intact retrieved chunks should persist across reasoning steps. It scores bounded candidate batches through paired prefills: a query-free control suppresses shared attention responses, while normalized entropy measures the breadth of the positive response within each chunk. High-scoring chunks enter a persistent evidence whitelist and are included in the reasoning context. Uncertain chunks remain outside the reasoning context but are retained in a candidate cache, where they can be retrieved for later reevaluation. QRAE requires neither an additional generative compression pass nor modification of the attention operator. Across multiple DeepSearch benchmarks and reasoning models, QRAE improves task success by an average of 2.35 percentage points and reduces end-to-end latency and reported token usage by an average of 30% and 45%, respectively. These benefits generalize to a model with nearly 100B parameters.

</details>


### 46. ChemE-as-Code: An Open-Source Platform for Agentic AI in Chemical Engineering

- **Authors:** Artur M. Schweidtmann
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07947v1](http://arxiv.org/abs/2611.07947v1)
- **PDF:** [https://arxiv.org/pdf/2611.07947v1](https://arxiv.org/pdf/2611.07947v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

ChemE-as-Code provides an open-source environment in which AI agents built on large language models (LLMs) can carry out chemical engineering work and engineers can check it. Its calculation tools range from catalysis through process simulation to plant layout, HAZOP and life cycle assessment, and skills tell a general-purpose agent how to use them. Engineering files are linked, machine-readable and versioned in Git; calculations run outside the LLM, each value records its origin, and automated checks report inconsistencies and out-of-date results by file and line. In an illustrative ammonia case, agents developed a written task into a preliminary basic-engineering package (simulation files, P&IDs, layout, HAZOP, datasheets, relief) for USD 224 of API cost in the design sessions. Planted faults and engineering changes show that the checks find what their rules cover and miss the rest, so they guide human review rather than replace it. No independent engineer has reviewed the design.

</details>


### 47. tok: a textual concrete syntax of BPMN and DMN for humans and AI agents

- **Authors:** Marek Deja
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07945v1](http://arxiv.org/abs/2611.07945v1)
- **PDF:** [https://arxiv.org/pdf/2611.07945v1](https://arxiv.org/pdf/2611.07945v1)
- **Categories:** cs.CY, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

tok is a plain-text notation for Business Process Model and Notation (BPMN) 2.0.2 process models and Decision Model and Notation (DMN) 1.5 decisions. One engine checks a tok document against both standards, compiles the document to XML with an automatic diagram, and serves language-model applications through the Model Context Protocol. The paper classifies the notation as an alternative concrete syntax of the BPMN and DMN metamodels and reports one study. A tok model takes 2.2 times fewer tokens than the smallest BPMN XML of 893 files exported by 37 tools and 7.7 times fewer than the files as exported. The checker signals 98.2% of 1,411 injected faults, against 85.8% for the XML Schema with bpmnlint. Four language models new to tok write valid tok from a one-page reference for 85.7 to 100% of 87 process descriptions from two datasets and valid BPMN XML for every description, and the strongest model writes tok with 25% and 19% fewer tokens than BPMN XML. As agents with a lean skill and one checker tool, the models write valid tok for 97.6 to 100% of the descriptions, the strongest model spends 21% and 14% fewer tokens on tok than on BPMN XML, and a skill which sends the model to read the reference through a tool costs 1.7 to 2.8 times the tokens of the lean skill. Of 47 event logs simulated from public models, 44 fit their source models, and tok imports every model discovered from the logs.

</details>


### 48. AttnSR: Attention Step Reward for Long-Horizon Agentic RL

- **Authors:** Mengsong Wu, Tianchen Zhou, Zhaochen Su, Zhenhua Liu, Zhe Cui, Aimin Zhou
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07932v1](http://arxiv.org/abs/2611.07932v1)
- **PDF:** [https://arxiv.org/pdf/2611.07932v1](https://arxiv.org/pdf/2611.07932v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents make multi-step decisions, yet outcome-reward-only reinforcement learning provides little direct supervision for individual steps. We introduce AttnSR, a step-level reward augmentation method that derives reward allocations from policy attention extracted during training replay, without a separately trained reward model or additional rollouts. AttnSR traces backward through the policy model attention graph to estimate the relevance of earlier steps to the final response. The terminal step, measured relative to a running baseline, determines whether these rewards reinforce or penalize the selected steps. In a controlled Qwen2.5-7B-Instruct study, AttnSR consistently outperforms the PPO baseline across all evaluated checkpoints on ALFWorld, raising final held-out success from 91.2% to 97.1%. The ablation experiment shows that the benefit depends on how intermediate rewards are assigned, rather than simple accumulation of step rewards over time. AttnSR also improves ScienceWorld at every checkpoint while cutting environment interactions by 29.9%. These results support policy attention as a practical prior for step-level reward allocation in long-horizon agentic RL. Code is available at https://github.com/fairyshine/AttnSR .

</details>


### 49. Instantiating the Knowledge Plane

- **Authors:** Francisco Pereira, Justine Sherry, Pratiksha Thaker
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07827v1](http://arxiv.org/abs/2611.07827v1)
- **PDF:** [https://arxiv.org/pdf/2611.07827v1](https://arxiv.org/pdf/2611.07827v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In 2003, Clark et al. proposed the "Knowledge Plane", a layer of intelligent agents that share rich information about network state in order to collaboratively manage the Internet across administrative boundaries. The technology of the day lacked the two capabilities it demanded most: reasoning and unstructured communication. Thus, automated network management has remained largely confined to single domains, while interdomain problems are still resolved by human operators on the phone. We argue that agentic large language models can finally unlock the potential of the Knowledge Plane, but that doing so will require solving new research problems that arise particularly in this decentralized, multi-agent, coopetitive setting that have received limited attention in the literature thus far.

</details>


### 50. RIVER: Evidence-guided multi-agent retrieval for enzyme--reaction discovery

- **Authors:** Yifan Chang, Yunze Li, Feifei Jiang, Juntao Wu, Xin Chen, Han Hu, Yucheng Wu, Wei Tang, Mingqian Ma, Wanli Ouyang, Kaipeng Zhang, Lei Bai, Hongting Tang, Feiran Li, Yuchen Ren
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07757v1](http://arxiv.org/abs/2611.07757v1)
- **PDF:** [https://arxiv.org/pdf/2611.07757v1](https://arxiv.org/pdf/2611.07757v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enzyme function annotation and the identification of candidate enzymes for a given reaction are essential steps in connecting genomic information to biochemical reaction networks. However, existing methods rely on sequence or structural similarity or on training with known enzyme--reaction pairs, making it difficult to integrate biochemical evidence across large candidate spaces; they also struggle with retrieval tasks involving enzyme families whose members are highly similar. Here, we introduce RIVER (Reaction--enzyme Inference via Evidence-guided Retrieval), a multi-agent framework for bidirectional enzyme--reaction retrieval that identifies potentially catalyzed reactions for a given enzyme and ranks candidate enzymes for a given reaction. RIVER coordinates large language models, specialized biochemical computational tools, and external knowledge resources to assemble evidence at multiple levels, including reaction chemistry, protein sequences and domains, catalytic mechanisms, and database annotations. Dedicated validation modules further examine evidence gaps and potential conflicts and rerank candidates using traceable evidence records. On public benchmarks, RIVER achieves the highest success rates in both enzyme retrieval and enzyme annotation. In family-specific enzyme retrieval, RIVER outperforms the evaluated baselines on the selected datasets and metrics. In Escherichia coli enzyme retrieval tasks constructed from recent literature, RIVER achieves the best retrieval results with closed-source and open-source model configurations, substantially outperforming closed-source general-purpose and biology-specialized multi-agent systems, including Claude Code, Codex, and Phylo Max. These results suggest that evidence-guided multi-agent retrieval can prioritize biochemically supported enzyme--reaction relationships, providing a basis for subsequent experimental validation.

</details>


### 51. Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes

- **Authors:** Seong-Eun Hong, JuYeong Hwang, Jinhyun Kim, Hanyoung Jang, HyeongYeop Kang
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07730v1](http://arxiv.org/abs/2611.07730v1)
- **PDF:** [https://arxiv.org/pdf/2611.07730v1](https://arxiv.org/pdf/2611.07730v1)
- **Categories:** cs.GR, cs.AI, cs.CV, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Selecting a next motion in a populated scene is not just a matter of avoiding what is currently in the way: an action can be locally feasible yet drift onto the road instead of the crosswalk, cut into a stream of crossing pedestrians, or bottleneck a narrow passage. These failure modes are invisible from the current state alone, and acting on them requires reasoning about what each candidate action will cause. World models offer exactly this, namely action-conditioned predictions of the future, but rolling them out at every decision step is a cost deployable navigation systems cannot pay, and the field has largely traded foresight for speed. We argue this is a false dichotomy. The natural place for a world model in human-aware navigation is at training time, as a preference oracle that distills foresight into a fast policy, rather than at inference time, as an online planner. We pair a discrete visual action prior with two task-aligned world models, one for nearby social dynamics and one for future scene semantics, that score candidate actions by their predicted consequences and refine the policy through group-relative preference distillation. At deployment, both world models are removed and the policy acts in a single forward pass. Across five held-out evaluation scenarios, this yields navigation that is simultaneously safer, more socially and group-coherent, and more goal-directed than strong reactive and learned baselines, with naive observers rating the resulting motion as more human-like. Taken together, our findings point to a different approach for bringing world-model foresight into deployable agents: not accelerating rollouts, but amortizing them into the policy so that the cost of looking ahead is confined to training. Project page: https://seoneun.github.io/-NeurIPS-2026-Seeing-Beyond-the-Next-Step/

</details>


### 52. MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents

- **Authors:** Yizhen Jiang, Haowei Guo, Tianyi Bai, Zengjie Hu, Lu Ma, Zhengyang Zhao, Haoze Sun, Peng Pei, Wentao Zhang
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07689v1](http://arxiv.org/abs/2611.07689v1)
- **PDF:** [https://arxiv.org/pdf/2611.07689v1](https://arxiv.org/pdf/2611.07689v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents are increasingly deployed through the Model Context Protocol (MCP), which allows them to discover and invoke tools across multiple servers at runtime. Existing MCP benchmarks primarily measure task completion; where they diagnose failures, they do so after execution rather than building specific reasoning, execution, and memory failure risks into task construction.
  We introduce MCPHallu, a benchmark for diagnosing hallucination-prone agent failures in MCP environments along three axes: reasoning, execution, and memory. MCPHallu contains 358 tasks across five capability domains and runs on 36 production MCP servers in isolated containers. Each task is designed with a structural trigger that makes one of four subtypes the dominant failure risk: Branch Collapse, Unreachable Goal, Tool Misuse, or Context Forgetting. This design enables subtype-level analysis rather than aggregate task success alone.
  We evaluate fourteen frontier LLM agents from eight vendors on 5{,}012 trajectories. Current MCP agents remain vulnerable to hallucination-inducing tool environments, achieving an average score of 0.642 on a $[0,1]$ scale (higher is better). Failures concentrate on Unreachable Goal tasks, where the average score drops to 0.458 and 23.2\% of runs pass, indicating that agents often continue issuing tool calls or claim successful completion rather than recognizing infeasible goals. Subtype rankings diverge sharply: a model's rank shifts by 6.9 of 13 positions on average across subtypes, and Branch Collapse is uncorrelated with Unreachable Goal across models ($r = -0.12$). MCPHallu is released at https://github.com/J1zz/mcp_hallu.

</details>


### 53. Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies

- **Authors:** Mete Erdogan, Mirac Suzgun, Aneesh Pappu, Guowei Xu, Batu El, Andrew A. Schoen, Furong Huang, John P. Dickerson, Mert Pilanci, James Zou
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07667v1](http://arxiv.org/abs/2611.07667v1)
- **PDF:** [https://arxiv.org/pdf/2611.07667v1](https://arxiv.org/pdf/2611.07667v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The performance of multi-agent LLM systems depends not only on the capabilities of the underlying models but also on information-sharing policies, which govern what information each agent observes and at what level of detail. But does providing AI agents with more detailed information always improve collective outcomes, or can transparency paradoxically degrade efficiency? To investigate this, we introduce empirical information design, an experimental framework that systematically compares disclosure policies across economic markets populated by LLM agents, while holding interaction rules and models fixed. We evaluate ten frontier LLMs in multi-resource trade, bilateral bargaining, and double auctions, using ground-truth utilities to decouple identified opportunities from realized outcomes. We find that finer information disclosure yields highly model-dependent results. In trade, revealing exact valuations rather than ordinal preference rankings reduces realized gains for GPT-6 Sol (from 98% to 91% of maximum) yet increases them for Claude Sonnet 5 (from 72% to 86%). In bargaining, exact information leads Grok 4.7 to produce less balanced agreements, whereas Claude Opus 5.5 divides gains symmetrically. In double auctions, full disclosure inflates price demands, triggering market breakdown and lowering welfare for Gemini 3.1 Pro (97% to 78%), Claude Opus 5.5 (94% to 64%), and Grok 4.7 (97% to 62%). Overall, these results suggest that model selection and information design must be co-optimized, as LLMs vary in how their strategic responses to information impact system objectives.

</details>


### 54. Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks

- **Authors:** Rongting Zhang, Martin Bertran, Sandeep Avula, Chia-Jung Lee, Vanessa Murdock
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07640v1](http://arxiv.org/abs/2611.07640v1)
- **PDF:** [https://arxiv.org/pdf/2611.07640v1](https://arxiv.org/pdf/2611.07640v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Indirect prompt-injection (IPI) benchmarks predominantly test planted instructions that redirect a tool-using agent toward an attacker-chosen task. Yet attacker-controlled content can instead tamper with the outcome of the task already in progress. A buyer's dispute evidence can cite a false refund policy to inflate a refund without changing the task. We define IPI by authority rather than instruction-like wording: planted content constitutes an attack when it attempts to influence a decision that its source is not authorized to determine. We introduce a benchmark that makes this boundary explicit: in each of 90 validated cases across three tool-use environments, the user request specifies the source that resolves the targeted decision. Every attack tampers with a decision required by the benign task rather than replacing that task. Each case has attacks with the same harmful outcome that target up to six parts of the agent's decision making: its objective, decision rules, available actions, expected consequences, reading of observations, or beliefs about the current state. Without a defense, attacks on three of the five other targets (decision rules, available actions, and state) have higher mean success than objective attacks across five LLMs. A detection-and-removal defense reduces objective-targeting attacks to 2.4% success but leaves observation- and state-targeting attacks at 9.5% and 12.1%; this gap persists under detection-optimized rewrites. A tool-policy defense still allows 15.4% attack success, close to 17.0% without a defense, because these attacks generally retain expected tools and manipulate values obtained during execution. Evaluations whose attacks redirect the task or target only the agent's objective can therefore overestimate the coverage of these defenses. Code and data are available at https://github.com/amazon-science/task-tampering-prompt-injection.

</details>


### 55. A Bilevel Neurodynamic Approach for Distributed SCAD-Regularized Sparse Least Squares

- **Authors:** Juntao Li, Qihang Guo, Deyuan Meng
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07618v1](http://arxiv.org/abs/2611.07618v1)
- **PDF:** [https://arxiv.org/pdf/2611.07618v1](https://arxiv.org/pdf/2611.07618v1)
- **Categories:** math.OC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper proposes a bilevel particle swarm optimization (PSO)-neurodynamic method for solving the distributed sparse least-squares problem regularized by the smoothly clipped absolute deviation (SCAD) penalty to global optimality. The SCAD penalty is nonsmooth and nonconvex, so existing distributed neurodynamic methods have not been extended to it directly. Through two-time-scale singular perturbation analysis, a rigorous full-trajectory convergence theory with explicit convergence rates is established for the inner collaborative multi-agent neurodynamic system without requiring the second-order sufficient condition. A theory-guided inner-outer collaborative optimization framework is further developed, in which a red-light green-light sensitivity mechanism is embedded in the outer PSO search to enhance global search while concentrating computational effort on the SCAD shape parameters, thereby improving recovery accuracy and computational efficiency. Simulation results on four sparse-recovery scenarios demonstrate that the proposed method accurately recovers the true sparsity pattern and achieves faster convergence and lower relative error than competing neurodynamic methods.

</details>


### 56. Binding Paraphrased Instructions to Encountered Objects in sLLM Agents under Partial Observability

- **Authors:** Chanyoung Kim, Harim Song, Byoungchan Ko, Keonyoung Lee, Myungwon Lee, Dahuin Jung
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07599v1](http://arxiv.org/abs/2611.07599v1)
- **PDF:** [https://arxiv.org/pdf/2611.07599v1](https://arxiv.org/pdf/2611.07599v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reliable deployment of LLM agents requires grounding diverse user expressions in their environments. Although RL-finetuned smaller large language model (sLLM) agents rival larger prompted LLMs on embodied tasks, their robustness to instruction paraphrases remains unclear. We introduce ALFWorld-Para to evaluate this robustness under controlled paraphrases, revealing 21-52% declines in success rates (SRs), predominantly driven by object synonyms. Despite retaining knowledge of synonym referents, agents often fail to take the corresponding objects even after observing them, exposing a gap between referential knowledge and object binding. Partial observability further complicates binding, as referents may remain unseen or have already been encountered under different labels. To address this challenge, we propose BINDIntent, a training-free framework that probabilistically binds referring expressions to observed labels using semantic proximity and estimated persistence against unseen candidates. Without additional training or LLM calls, BINDIntent improves synonym-paraphrase success of RL-finetuned sLLMs by 17.5-49.1 percentage points (pp) with only 0.4 ms of CPU overhead per step. It also raises GiGPO-7B's overall SR from 61.8% to 77.4%, surpassing a prompted 24B LLM. Code and benchmark are available at https://github.com/cau-hai-lab/ALFWorld-Para.

</details>


### 57. Learning and Steering in Incomplete-Information Games

- **Authors:** Asrın Efe Yorulmaz, Tamer Başar
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07589v1](http://arxiv.org/abs/2611.07589v1)
- **PDF:** [https://arxiv.org/pdf/2611.07589v1](https://arxiv.org/pdf/2611.07589v1)
- **Categories:** cs.GT, cs.AI, cs.LG, eess.SY, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

In many modern multi-agent systems, a mediator seeks to influence strategic decision dynamics using only outcome-level feedback and without knowing agents' utilities. In this work, we study how a mediator can learn an unknown game and steer adaptive agents toward outcomes that maximize her utility using only trajectory feedback. The mediator knows the game form and her own objective, but not the agents' utilities. Moreover, she commits to nonnegative payments and provides recommendations and contexts, but receives only a single realized terminal outcome rather than full-information feedback. We develop halving-type algorithms that learn utility differences in normal-form games and conditional continuation-value differences in extensive-form games, achieving a sample complexity of $\widetilde O(\varepsilon^{-2})$ that matches worst-case lower bounds up to logarithmic factors. We then combine these learning procedures with a Lagrangian formulation in an online Learn-Compute-Steer algorithm that interleaves learning, equilibrium computation, and steering toward mediator-optimal extensive-form correlated equilibria (EFCE). With high probability, the Learn-Compute-Steer algorithm achieves a directness gap and an optimality gap of $\widetilde O(T^{-1/4})$, while time-average payments are of $\widetilde O(T^{-1/8})$.

</details>


### 58. Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment

- **Authors:** Yao Huang, Yifan Wang, Yitong Sun, Yichi Zhang, Yinpeng Dong
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07586v1](http://arxiv.org/abs/2611.07586v1)
- **PDF:** [https://arxiv.org/pdf/2611.07586v1](https://arxiv.org/pdf/2611.07586v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents advance rapidly in autonomy, the risk of hidden objectives that bypass safety constraints becomes increasingly plausible. Chain-of-thought (CoT) monitoring offers a key control mechanism by reading the agent's reasoning and flagging misalignment before it materializes into action, yet its reliability depends on the realism of the red-team it is stress-tested against. Existing red-teaming efforts rely on shared templates, such as casting a side task as a prerequisite, which treat the side objective as an exogenous insertion and leave task-specific, contextually grounded evasions underexplored. We therefore ask: How robust is CoT monitoring against agents that strategically conceal misalignment? To answer this, we introduce TraceMRT, an automated Trace-level Monitor Red-Teaming framework that reframes the side task as a coherent sub-goal of the primary task and searches trace-shaping strategies whose induced trajectories complete the misaligned objective while reading as natural execution. Through black-box attacks on state-of-the-art monitors such as GPT-5.2 and Claude-4.5, we reveal substantial vulnerabilities even in top models. To counter these vulnerabilities, we propose a Bayesian Trajectory Monitoring framework, integrating global context and local segment evidence to detect covert misalignment. Empirically, our method significantly consolidates monitor robustness with 0.91 AUC and 0.74 TPR@FPR=0.05.

</details>


### 59. SKIM: Pruning Large Language Model Agents via Selective Knowledge Informed Masking

- **Authors:** Moonseok Choi, Jongwon Jeong, Minki Kang, Giung Nam, Juho Lee
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07558v1](http://arxiv.org/abs/2611.07558v1)
- **PDF:** [https://arxiv.org/pdf/2611.07558v1](https://arxiv.org/pdf/2611.07558v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents are increasingly deployed under structured generation, where grammar constraints enforce output format at inference time. Whereas existing compression methods target unconstrained generation, we first identify a fundamental mismatch: under structured generation, grammar constraints reduce the model's output distribution to valid tokens, and the logits matter most at the small set of positions that decide the agent's action. Motivated by this finding, we propose SKIM (Selective Knowledge-Informed Masking), the first pruning and distillation framework for LLM agents under structured generation, with both stages guided by token role. SKIM partitions token positions into context, decision, and format categories, and this partition drives two complementary axes: (1) category-aware pruning saliency scores that preserve parameters most relevant for decision positions; and (2) an on-policy distillation objective that aligns student and teacher on valid tokens, paired with category-aware feature matching. We evaluate SKIM on tool-calling benchmarks and within multi-step agent loops, across multiple model scales and sparsity levels. SKIM consistently improves accuracy over baselines, with its superiority becoming most striking in high-sparsity regimes where conventional methods struggle, demonstrating the potential of category-aware compression for deployment-time grammar-constrained agents.

</details>


### 60. Goal-Branching LaCAM: Temporary Goals as Search Branches in Dense Multi-Agent Pathfinding

- **Authors:** Stephen Chang, Daniel Harabor
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07528v1](http://arxiv.org/abs/2611.07528v1)
- **PDF:** [https://arxiv.org/pdf/2611.07528v1](https://arxiv.org/pdf/2611.07528v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LaCAM is a search-based solver for multi-agent pathfinding (MAPF) that runs a depth-first search over joint configurations, using PIBT to generate successors and lazily adding single-agent constraints to explore alternatives. Although LaCAM is complete, it can struggle on dense, corridor-heavy instances because extracting blocking agents from deadlocks requires coordinated moves of several agents, often away from their goals, which PIBT's greedy one-step successors rarely propose and which LaCAM can only reach by enumerating constraints one agent at a time. This paper proposes Goal-Branching, where blocking agents are given temporary goals, each tried as an additional branch of LaCAM's search. We examine random and corridor-aware rules for choosing these temporary goals and show that completeness is preserved for any such rule. On dense instances (60-90% of free cells occupied) of three maze and room maps, Goal-Branching solves 89% of instances against 44% for LaCAM*, and, on instances both solve, it finds a first solution 10-14x faster on maze-32-32-2 and room-32-32-4, and nearly 200x faster in median time at 75% density on room-32-32-4. Solution cost increases by 15-22% on instances both solve, while on open maps and the full MovingAI benchmark its solutions cost no more than those of LaCAM* and it is at most 3% slower.

</details>


### 61. DelegateEval: Evaluating Platforms for Personal External Service Agents

- **Authors:** Jichao Li, Jinrong Lu, Manjiang Yu, Zhixuan Liu
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07508v1](http://arxiv.org/abs/2611.07508v1)
- **PDF:** [https://arxiv.org/pdf/2611.07508v1](https://arxiv.org/pdf/2611.07508v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents that work for an individual over time may also help that individual serve external clients. We define a personal external service agent as an agent authorized and continuously managed by a specific individual to accept client requests, deliver work, and provide ongoing support using that person's knowledge, experience, professional methods, and service boundaries. Such agents could allow individuals to serve more clients with less direct involvement and generate economic value at scale. We propose DelegateEval, a platform-level evaluation framework for agent systems that may combine large language models, reusable skills, protocols such as MCP, and executable tool environments. It covers eight dimensions: ease of creation, service discovery and matching, delivery quality, expertise inheritance, service continuity, learning and improvement, reliability and governance, and efficiency and value. These dimensions assess whether a platform enables people with different backgrounds to turn their expertise into ongoing services that deliver verifiable work, develop capabilities through experience, and remain economically feasible. We present the framework and an experimental design. Complete datasets, executable environments, a unified scoring protocol, and cross-model results remain to be developed and empirically validated.

</details>


### 62. Learning Multi-Agent Orchestration:Higher-Order Interactions in Policy Improvement

- **Authors:** Kaixuan Liu, Guojun Xiong
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07495v1](http://arxiv.org/abs/2611.07495v1)
- **PDF:** [https://arxiv.org/pdf/2611.07495v1](https://arxiv.org/pdf/2611.07495v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learned orchestration has emerged as a promising paradigm for large language model (LLM)-based multi-agent systems, in which a central orchestrator selects agents and controls the information they receive throughout a task. Despite rapid empirical progress, existing methods train the orchestrator by crediting each decision with its own advantage, implicitly assuming that the other decisions in the episode stay fixed. This assumption fails in orchestration, where the contribution of each decision to the final outcome depends on the decisions preceding it, so the gain of a joint update is not the sum of its per-decision effects. To address this challenge, we introduce \textbf{IAPO}, an interaction-aware policy optimization framework that explicitly accounts for interactions among decisions. Specifically, IAPO exactly decomposes the performance difference between two policies into the effects of individual decisions and their interactions, which we prove can account for half of the attainable gain, and then optimizes both from sampled trajectories while certifying that every update is an improvement. On long-input versions of GSM8K, MATH, DROP, MBPP and HumanEval, against fifteen published multi-agent and workflow-search systems on the same 7B executor, IAPO's deployed plans reach the strongest system's accuracy with fewer tokens, and removing the interaction term costs 7 to 17 points of accuracy on code.

</details>


### 63. Signed but Not Safe: Requirement Integrity in Multi-Agent LLM Handoffs

- **Authors:** Xiaobo Chen, Genliang Zhu, Ziyuan Wang, Chu Wang
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07483v1](http://arxiv.org/abs/2611.07483v1)
- **PDF:** [https://arxiv.org/pdf/2611.07483v1](https://arxiv.org/pdf/2611.07483v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise AI agents increasingly split a user's request across subagents and merge their results, and each handoff can summarize away, alter or ignore a requirement. We report a preregistered study with synthetic, exactly scorable tasks comparing free-text, structured JSON and signed requirement-manifest handoffs: the orchestrator extracts each requirement as a verbatim quote plus a checkable predicate, code signs the manifest with HMAC-SHA256, and deterministic code verifies the merger's decision. With Qwen3-8B (1,440 trajectories, five threats), signed manifests cut unsafe commits under attack from 69.4% to 9.0% (60.4 pp, 95% CI [51.4, 69.4]) with no net loss of conformant commits relative to structured handoffs. Signing is what defeats in-transit tampering: an unsigned manifest committed violations in 79% of mutated runs, the signed one in none. On identical trajectories the deterministic verifier caught 78.7% of violating decisions versus 59.0% for an LLM checker, with 7% versus 50% false alarms. An oracle manifest removed all remaining unsafe commits: the residual risk comes from extraction errors made before signing. A preregistered pre-signing injection attack confirmed this boundary: one adversarial line raised signed-manifest violations from 14.6% to 37.5% (Qwen3-8B), 11.1% to 63.9% (gpt-oss-20b) and 8.3% to 75.0% (GPT-5.6-luna), and the signature then authenticated the corrupted manifest. Signing protects requirements in transit, not at extraction; the extraction step is the trust boundary.

</details>


### 64. Designing with Cinematic Language: An Intent-Driven Approach to Human-AI Video Clip Co-Creation

- **Authors:** Yi He, Zhengxi Yu, Feilin Han, Chuer Chen, Shengqi Dang, Nan Cao
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07377v1](http://arxiv.org/abs/2611.07377v1)
- **PDF:** [https://arxiv.org/pdf/2611.07377v1](https://arxiv.org/pdf/2611.07377v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Generative video models have made video creation more accessible, yet creators still struggle to translate high-level narrative intentions into coherent cinematic expressions. Existing systems primarily rely on prompt refinement or expose isolated camera controls, leaving a gap between what to express and how to film it. We present CineAssist, a human-AI co-creation system that treats cinematic language as an interactive design medium connecting creative intentions with executable video controls. We construct a Cinematic Language Design Space and an annotated dataset from 107 filmmaking sources and 1,436 film clips, linking communicative intentions to cinematic parameter values. CineAssist combines a multi-agent workflow for intent alignment and strategy recommendation with an interactive cinematic editor and a context-sensitive preference learner for user-controlled personalization. We evaluate the system through three studies examining end-to-end usability, cinematic quality, and preference evolution. Results show that CineAssist facilitates efficient, controllable, and personalized intent-driven cinematic video creation.

</details>


### 65. EnvOpt: Automated Optimization for Agent Environments

- **Authors:** Mingxuan Li, Huanzhi Mao, Qiuyang Mang, Hanchen Li, Joseph E. Gonzalez, Alex Dimakis
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07372v1](http://arxiv.org/abs/2611.07372v1)
- **PDF:** [https://arxiv.org/pdf/2611.07372v1](https://arxiv.org/pdf/2611.07372v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

An LLM agent's cost and success depend on its model, its harness, and its environment. In addition to the widely studied directions of parameter tuning and harness optimization, we propose the third direction: optimization over stationary environments. Agents are often deployed in rich environments shared by many tasks, such as a company's Slack workspace or a complex collection of data sources, documents or tickets. We call these environments stationary environments. We introduce EnvOpt, a method for automated end-to-end optimization of stationary environments for any given model and harness, using real or synthetic tasks without needing any graders or reference answers. On AutomationBench, EnvOpt reduces the cost of Claude Haiku 4.5 by 72.7% and raises its pass rate by 14.34%. The same environment transfers to Opus 5, cutting its cost by 68.1% with a 1.34% gain. Added on top of Meta-Harness's optimized harness for Haiku 4.5, it lowers cost by a further 83.4% and adds 11.17% accuracy over Meta-Harness alone. Across 5 benchmarks, EnvOpt significantly reduces the cost of agents while improving or maintaining pass rate, and is transferable to different models and different harnesses. We also discuss common successful and rejected environment optimization strategies during automated optimization. More broadly, our results show that how information is represented to an agent shapes both its cost and its success, making the environment worth optimizing in addition to the parameters and the harness.

</details>


### 66. How Should Agents See Code? Rethinking Code Representations for Agentic Software Engineering

- **Authors:** Melika Sepidband, Jiho Shin, Song Wang, Hadi Hemmati
- **Published:** 2026-11-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07286v1](http://arxiv.org/abs/2611.07286v1)
- **PDF:** [https://arxiv.org/pdf/2611.07286v1](https://arxiv.org/pdf/2611.07286v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly used for repository-level software engineering tasks. However, most agents still access repositories through raw files, lexical search, and shell commands, treating code primarily as text. This paper investigates map-based code-representation workflows as a design variable in agentic software engineering, examining how different repository views change agents' retrieval behavior, task success, token use, and latency.
  In this paper, we study five code-representation workflows: abstract syntax trees, call graphs, module dependencies, documentation-enriched search, and a hybrid workflow that combines them. Each workflow exposes a repository map that the agent can query during a task. We evaluate Claude Code with Haiku 4.5 against a raw-tool baseline on four repository-level tasks: fault localization with LinuxFLBench, repository-level code generation and repair with SWE-bench Pro, test generation with SWT-bench, and security patching with SecBench.
  The results show that representation workflows are most useful as token-saving tools when localization is the bottleneck, while their success gains narrow when the decisive step is patch or test authoring. On LinuxFLBench, all five workflows improve recall@10 over the baseline (0.757-0.829 vs. 0.717) and reduce token usage by 25-39%. On SWE-bench Pro, resolution remains close to the baseline (44.3-50.6% vs. 49.0%) while token usage drops by 17-26%. On SecBench, Callgraph has the highest patch-resolution rate in this sample (34.3% vs. 28.9%) and uses fewer tokens, but all workflows increase latency. On SWT-bench, Hybrid and Docs have the highest reproducing-test rates in this sample (47.8% and 47.2% vs. 44.7%), but all workflows use more tokens and take longer. Overall, map-based workflows change both what the agent inspects and how much it spends, but their benefits are task-dependent rather than universal.

</details>


### 67. Goal Revelation as a Bridge Between Information-Theoretic Empowerment and Capability-Based Human Power

- **Authors:** Jaime Ruiz-Serra, Tomáš Gavenčiak, Jobst Heitzig
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07247v1](http://arxiv.org/abs/2611.07247v1)
- **PDF:** [https://arxiv.org/pdf/2611.07247v1](https://arxiv.org/pdf/2611.07247v1)
- **Categories:** cs.AI, cs.IT, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Power matters for AI safety. Optimal agents tend to acquire power across a wide range of objectives (instrumental convergence). As we embed AI agents into socio-technical systems, humans risk gradual disempowerment. Both concerns call for a formal, quantitative measure of power. Two such measures in the context of Markov games are information-theoretic empowerment, the capacity of the channel from an agent's actions to future states, and capability-based individual power, a measure of goal attainment built from the probabilities that a human would attain each goal in a family of candidates were they pursuing it. We show where the two meet. From individual power, Fano's inequality yields a floor $B(s)$. This floor is a lower bound on what we term goal revelation, the mutual information $\mathbb{I}(G;ξ\mid s)$ between the human's latent goal and the realised trajectory. Empowerment caps revelation from above, so that $B(s) \le \mathbb{I}(G;ξ\mid s) \le \mathbb{I}(\mathbf{A}_h \to ξ\mid s) \le \mathfrak{E}_h(s)$. Each quantity can be large while the one below it stays at zero, highlighting the following failure modes. An assistant maximising empowerment can prefer an interface offering broad influence over goal-irrelevant degrees of freedom to one that lets the human attain every goal they might hold. An assistant maximising revelation cannot tell a working interface from one rewired so that every goal yields the wrong outcome, since relabelling goals leaves mutual information unchanged while zeroing every attainment probability. Positive guarantees therefore come only from the attainment end of the chain. A satisfaction floor, computable from two statistics of interaction logs, offers a way to monitor the power users retain in a deployed system, and simulations in random environments show the three quantities are correlated but far from interchangeable.

</details>


### 68. How Do AI Agents Waste Your Money?

- **Authors:** Huimin Zeng, Yuxuan Lu, Jesse Cai, Eric Hanchen Jiang, Di Wu, Po-Nien Kung, Wenbo Hu, Ziyi Wang, Dakuo Wang, Jiaxin Pei, Kai-Wei Chang
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07238v1](http://arxiv.org/abs/2611.07238v1)
- **PDF:** [https://arxiv.org/pdf/2611.07238v1](https://arxiv.org/pdf/2611.07238v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents may consume massive tokens across a wide range of tasks, but how many of those tokens are really necessary? Although prior work has shown that agents can incur unexpectedly high token costs, we still lack a systematic way to identify and measure token waste. In this work, we introduce a unified framework for measuring token waste across heterogeneous agent systems. Our framework records and normalizes complete agent trajectories, identifies removable spans using an LLM-as-a-Judge (LLMaJ), and maps the identified text spans back to the original trajectory for token-level measurement. We validate the identified waste through direct interventions by removing marked spans, resuming agent execution, and measuring changes in task outcomes and subsequent actions. In online pruning experiments, we remove 41-46% of the model's reasoning while largely preserving task performance across two distinct agent benchmarks. Using this framework, we analyze agents across multiple settings. Our analysis shows that token waste has a system-level structure that aggregate token usage alone cannot reveal. First, waste varies more across tasks and agent settings than across models. Second, reasoning and visible execution can exhibit different waste patterns. Third, different harnesses can introduce distinct sources of inefficiency even under the same model and task. Overall, our framework transforms token waste into an actionable optimization signal, enabling researchers and practitioners to train more efficient models, design better reasoning strategies, and optimize agent harnesses toward reducing unnecessary computation rather than merely reducing token usage.

</details>


### 69. SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection

- **Authors:** Woosang Lim, Yeseul Chang, Jaewoo Lee
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07222v1](http://arxiv.org/abs/2611.07222v1)
- **PDF:** [https://arxiv.org/pdf/2611.07222v1](https://arxiv.org/pdf/2611.07222v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using agents act on email, files, and payments, so an instruction hidden in a web page or a shared document can make an agent send data or money to an attacker. Many runtime defenses put a language model on the decision that lets an action through, so the decision depends on a model that may read the attacker's text and adds model calls to every step. Provenance defenses keep the model off the final check but need a model to plan or route each task first. Where an action goes can instead be read from the tools' typed returns: an email's sender or a payment's account arrives in a typed field, while injected instructions arrive as free text. SPILLWAY turns this observation into a deterministic floor with no per-task plan. The check admits a call when each target value that appears in tool output but not in the user's task was returned by a read-only tool in a typed field or is covered by a fixed delegation rule. A deterministic sanitizer removes instruction-like regions its fixed rules match before the model reads them and retains the removed spans as evidence, and a local judge may restore a refused call, never one whose target lies in the removed text. Across three backbones, and seven task suites on one of them, no standard templated injection redirects an action to an attacker's target under SPILLWAY, at the highest observed mean utility and composite scores (NRP, ERS) of the defenses we run under that attack. A forged chat template also produces a raw zero, and mean in-scope attack success under a released reinforcement-learning attacker is .007. SPILLWAY reaches this floor with no defense-triggered backbone re-run and almost no added model call. As personal AI agents act on users' email, files, and payments, SPILLWAY gives them an auditable refusal floor on where their actions go that keeps them useful and holds across backbones.

</details>


### 70. τ-bench-LILT: Evaluating Conversational Agents on Realistic Multilingual Tool-Use Tasks

- **Authors:** Kaden Uhlig, Kiarash Mokhtari, Anıl Arslan, Yunsu Kim, Joern Wuebker
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07203v1](http://arxiv.org/abs/2611.07203v1)
- **PDF:** [https://arxiv.org/pdf/2611.07203v1](https://arxiv.org/pdf/2611.07203v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Frontier evaluations of tool-using conversational agents are conducted almost exclusively in English, leaving a critical gap for organizations deploying agents in other languages and regions. We present $τ$-bench-LILT, a multilingual extension of ${τ^3}$-bench covering German, Korean, Turkish, and Farsi in the airline, retail, telecom, and banking domains. We natively localize every layer of the benchmark: customer databases are populated with culturally appropriate records, user-simulator prompts are refined iteratively through contrastive annotation by native-language experts, and tasks are updated according to the localized database and to reflect realistic tasks in the target region. Evaluation across eight agent models shows the largest drops compared to English in the Korean and Farsi retail domains, by up to 61 points in pass^4. Code and data released at https://github.com/lilt/tau-bench-lilt.

</details>


### 71. More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty

- **Authors:** Burkay Tunçtürk, Koorosh Aslansefat, Yiannis Papadopoulos, Bao Nguyen
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07140v1](http://arxiv.org/abs/2611.07140v1)
- **PDF:** [https://arxiv.org/pdf/2611.07140v1](https://arxiv.org/pdf/2611.07140v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Teams increasingly build software from cooperating large language model (LLM) agents, often assuming more agents mean more reliability. Yet the usual evidence, average benchmark accuracy, ignores the input mix a deployed system meets and the rule merging the agents' answers. Building on HIP-LLM, a hierarchical imprecise-probability assessment of single LLMs, we propose a framework combining it with a Bayesian network of the system's failure logic for multi-agent systems. Agent failure-probability intervals propagate through this network, where the combining rule can itself fail, into a reliability envelope showing which evidence limits it. In a pipeline extracting regulated chemical-hazard statements, majority voting over three models protected against the weakest but did not clearly exceed the best, and a voter failing on 5\% of demands would largely erase its advantage over the middle model. More agents yield a more defensible reliability claim, not automatically a more reliable system.

</details>


### 72. Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach

- **Authors:** Korbinian Kügler, Carolin Schmidt, Florian Dandl, Filipe Rodrigues
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07122v1](http://arxiv.org/abs/2611.07122v1)
- **PDF:** [https://arxiv.org/pdf/2611.07122v1](https://arxiv.org/pdf/2611.07122v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Profit-maximizing Autonomous Mobility-on-Demand (AMoD) operators may exploit consumer surplus through excessive prices and underserve less profitable regions by relocating vehicles away from them. We study how penalty-based regulation of an AMoD operator in a multimodal mobility system can limit surge pricing and improve regional service availability. We model regulation as an outer control loop that acts on a learning-based operator. Static regulation with fixed penalties is formulated as a Markov Decision Process for an operator that jointly controls pricing and rebalancing, and dynamic regulation as a Partially Observable Stochastic Game in which a regulator periodically adjusts region-specific penalties in closed loop. Operator and regulator policies are learned with graph-based multi-agent reinforcement learning. In experiments with real-world Manhattan data, fixed surge pricing penalties reduce the share of travelers facing excessive prices from 22% to 1%. For regional service availability, dynamic regulation improves the regulator's reward by up to 15.6% over fixed penalties of equal mean intensity. The gains in service availability are strongest when spare fleet capacity exists, whereas service deficits persist in peak periods with highly utilized fleets. The learned regulator policy responds by reducing penalties where limited fleet capacity restricts compliance. The results identify trade-offs between regulatory targets, operator profitability, and traveler utility.

</details>


### 73. Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration

- **Authors:** Sungil Son, Hoseong Jung, Dahyun Oh, H. Jin Kim
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07066v1](http://arxiv.org/abs/2611.07066v1)
- **PDF:** [https://arxiv.org/pdf/2611.07066v1](https://arxiv.org/pdf/2611.07066v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Discovering cooperative behavior in multi-agent reinforcement learning (MARL) is challenging due to the combinatorial complexity of joint state-action spaces, which hinders the emergence of coordinated behaviors from trial-and-error alone. Intrinsic rewards are often used to aid discovery, but naively combining them with team objectives can distort the learning signal, compromising task performance. In this paper, we propose EFXPLORER, a constrained exploration framework that maximizes exploration objectives subject to a constraint that preserves established task performance. We solve the resulting problem using an epigraph reformulation that introduces adaptive exploration budgets. This approach separates intrinsic rewards from task objectives and regulates exploration through task feasibility. To further encourage diverse and temporally extended exploration, we incorporate a successor distance-based intrinsic reward that captures long-horizon dependencies. Empirically, our method outperforms strong baselines and induces novel cooperative strategies across SMAX, VMAS, and MPE benchmark suites.

</details>


### 74. Adapting the Process of Adaptation: Darwinian, Lamarckian, and Agent-Directed Evolution in AI

- **Authors:** Andrew W. Lo, Chaoyi Zhao
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.07048v1](http://arxiv.org/abs/2611.07048v1)
- **PDF:** [https://arxiv.org/pdf/2611.07048v1](https://arxiv.org/pdf/2611.07048v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evolution has shaped intelligence for billions of years. Artificial intelligence (AI) now raises a striking possibility: intelligence may begin to direct its own evolution. As AI agents become capable of modifying and evaluating their own behavior, how quickly could they improve, and how can that improvement remain safe? We develop a theoretical framework comparing Darwinian, Lamarckian, and agent-directed evolution following environmental change. Darwinian evolution relies on natural selection, Lamarckian evolution adds inherited learning, and agent-directed evolution allows agents to generate and evaluate behavioral variants and choose how extensively to search. When learning is sufficiently effective, these mechanisms exhibit progressively faster adaptation. Generating more variants accelerates adaptation, while optimal search effort depends on learning ability, problem difficulty, and experimentation costs. However, an agent's ability to direct its improvement does not ensure that improvements are evaluated against the intended objective. When the evaluation target is misspecified, additional search accelerates convergence toward the wrong behavior, even as measured performance improves. In recursive self-improvement, such errors may persist across generations, posing challenges for AI safety. Independent evaluation and oversight must keep pace with autonomous AI development. The central challenge is not simply to accelerate the evolution of intelligence, but to preserve humanity's ability to guide its direction, limit its speed, and intervene when necessary.

</details>


### 75. A Framework for Context Enrichment and Selective Robustness in LLM Social Agents

- **Authors:** Mattia Greiche, Reihaneh Rabbany, Maximilian Puelma Touzel
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06914v1](http://arxiv.org/abs/2611.06914v1)
- **PDF:** [https://arxiv.org/pdf/2611.06914v1](https://arxiv.org/pdf/2611.06914v1)
- **Categories:** cs.MA, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Researchers use large language models as agents in social simulations, where agents are prompted with observations and background information intended to shape their actions. Yet LLM agents have been shown to substantially change their behavior under meaning-preserving prompt variations, creating a validation problem for social simulation. One plausible hypothesis is that this brittleness reflects a lack of grounding and can be reduced by enriching the context provided to the agents. Whether richer context improves robustness remains unclear, in part because context richness and robustness are rarely defined in ways that support controlled comparisons. We address the first need with controlled context enrichment, a set of prompt substitution rules that systematically enriches distinct types of context: neutral padding, generic social background, descriptive decision grounding, and normative decision grounding. We address the second by introducing selective robustness as a validation criterion: insensitivity to meaning-preserving prompt variation combined with a directional response to decision-relevant changes in the social world. We demonstrate the framework in a Prisoner's Dilemma-like game, showing how it can be used to identify which forms of context enrichment produce more desirable and robust agent behavior. We find that these forms of enrichment produce distinct behavioral patterns that vary between the two models tested.

</details>


### 76. FrontierPhysics: Evaluating Agents for End-to-End Physics Research

- **Authors:** Bingran You, Wenjun Ke, Ria Rosenauer, Bo Liu, Wenbo Chen, Min Chen, Shuqi Xu, Yue Ma, Jiechao Feng, Bo Chen, Xiangkai Sun, Jiarui Liu, Jinen Guo, Zeyu Zhou, Xu Huang, Zhuohan Li, Haoyu Li, Heguang Lin, Lijie Ding, Yadong Zeng, Kangqi Zhang, Xinge Liu, Hanwen Liu, Zhenghong Li, Alexander von Recum, Yuchen Zhu, Felix Schwarzfischer, Yizhou Zhao, Jicheng Wang, Binxu Li, Qian Yu, Chan Li, Cheng Dai, Di Wang, Haoyu Zhang, Jiankai Sun, Kaituo Feng, Mian Qin, Ruihong Yin, Yiqun Luo, Weiwei Wu, Shihong Pan, Tsung Yeh Hsieh, Xiao Huang, Yan Zhang, Sihan Li, Zirui Ren, Zengji Tu, Kyoung Whan Choe, Ke Sun, Vincenzo Galia, Vaisakhi Mishra, Jiashu He, Hongyang Wang, Zhiheng Yang, Shubham Gaur, Yifan Gu, Shuyi Wang, Zihao Zuo, Steven Dillmann, Yiyou Sun, Xinyang Han, Hanchung Lee, Molei Tao, Yue Zhao, Shilong Liu, Yuchen Wu, Xuandong Zhao, Xiangyi Li, Florian Brand, Gerbrand Ceder, Hartmut Haeffner
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06910v1](http://arxiv.org/abs/2611.06910v1)
- **PDF:** [https://arxiv.org/pdf/2611.06910v1](https://arxiv.org/pdf/2611.06910v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solutions, and rarely check research quality alongside correctness. We introduce FrontierPhysics, an end-to-end benchmark with 56 tasks made by 42 physicists based on their own research, covering nine domains across theoretical, computational, and experimental physics. Each task requires agents to review the literature, develop a research plan, conduct research and experiments, and produce structured outputs and scientific manuscripts. Combining deterministic verifiers with expert-authored rubrics, FrontierPhysics evaluates whether agents' research is correct and publishable. Across 22 models in 26 configurations, no configuration passes more than 46 of its 168 rollouts. Manual review of agent trajectories shows that frontier agents' main weaknesses are insufficiently rigorous reasoning and limited expert intuition, rather than gaps in physics knowledge or execution errors.

</details>


### 77. Trust Responsive Runtime Authorization for Agentic AI with Empirical Characterization of Policy Behavior and Parameter Sensitivity

- **Authors:** Ahsan Habib Shihab, Imre Felde, Ramis Akhmedov, Stefan Gubo, Berik Sabdenaliyev, Madina Mansurova, Amir Mosavi
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06996v1](http://arxiv.org/abs/2611.06996v1)
- **PDF:** [https://arxiv.org/pdf/2611.06996v1](https://arxiv.org/pdf/2611.06996v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The policy that converts runtime estimates of an autonomous agent's condition into operational authority is rarely specified or measured. We empirically characterize the Trust Responsive Authorization Policy (TRAP), which maps an Authorization Readiness Score (ARS), a weighted combination of runtime trust, operational stability, and contextual risk, onto discrete authorization levels through an asymmetric rule: escalation requires consecutive observations above a band edge plus a margin, while a sharp drop in readiness restricts authority at once. On one matched set of 100 Monte Carlo traces, we compare TRAP with static, trust-only, risk-only, and symmetric policies. Under abrupt degradation, TRAP restricts at onset and re-escalates sooner after recovery than the symmetric policy, with the highest and, descriptively, least variable stability among the adaptive policies, although more of its post-recovery escalations occur below the selected trust threshold. Paired bootstrap intervals exclude zero for the remaining differences. In one-factor sweeps, recovery time rises with the escalation margin and run length, shifts with the score weights, and is unchanged by the restriction threshold. In an exploratory post-freeze experiment, when the same degradation is spread over 5-20 intervals, TRAP restricts only on the 4 traces that retain a single-interval drop above that threshold; averaged over all 100 traces, it holds authority above what readiness supports for 15.9-18.9 of the 20 degradation intervals, against 0.8 under abrupt degradation and about 10 for the symmetric policy. Its restriction advantage therefore depends on degradation being abrupt. All reported values are traceable to the publicly available, versioned research release.

</details>


### 78. SpecCompact: Accelerating LLM Agent Context Compaction with Slot-Parallel Semantic Speculative Verification

- **Authors:** Yulu An, Yifei Feng, Xiangyang Yin
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06876v1](http://arxiv.org/abs/2611.06876v1)
- **PDF:** [https://arxiv.org/pdf/2611.06876v1](https://arxiv.org/pdf/2611.06876v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents use context compaction to manage growing interaction histories, but summarizing long histories with large models can introduce substantial delays. Compaction therefore requires balancing information retention against latency. We observe that structured summary slots can retain information when generated independently. Based on this observation, we present SpecCompact, a framework that accelerates compaction through slot-parallel semantic speculation. SpecCompact fine-tunes a small drafter and generates slots in parallel. The target model verifies each proposed line and repairs rejected content, while subsequent drafting uses the updated slot prefix. System optimizations further reduce repeated context processing and model calls. Across AppWorld and $τ^3$ benchmarks with two target models, SpecCompact achieves $2.04$--$5.63\times$ compaction speedups over Hermes-style summarization. Separate downstream evaluations reveal model- and task-dependent performance trade-offs. A user study within Hermes further shows an $8.68\times$ median compaction speedup.

</details>


### 79. Autonomous AI Agents Systematically Diverge From Human Preferences in Proof Formalization

- **Authors:** Bálint Gyevnár, Simon DeDeo
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06995v1](http://arxiv.org/abs/2611.06995v1)
- **PDF:** [https://arxiv.org/pdf/2611.06995v1](https://arxiv.org/pdf/2611.06995v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Artificial intelligence (AI) systems have ushered in a new age of proof abundance, but helping humans understand these proofs requires new attention to the differences in how AI agents and humans pursue a proof-making task. We present "simulated collaboration", a methodology that allows us to examine two key questions: (1) the relative attention AI agents pay to surface syntax or, conversely, deeper underlying semantics, and (2) how and where AI agent preferences for what to do next diverge from human preferences. On a set of nine major human collaborations in Lean with 4.7M definitions across more than 6K commits, we find that, over the course of proof construction, AI agents (1) are far more strongly drawn than humans to explicitly marked gaps; (2) show a relative aversion to densely connected proof centers and to complex or surprising proof goals; and (3) are relatively attracted to surprising proof bodies, which they tend to regularize toward baseline. Our results highlight important blind spots and potential interventions for future human-AI collaboration in mathematics.

</details>


### 80. On Turn-Level Best-of-N Sampling for Scaling LLM Agents

- **Authors:** Jalaj Bhandari, Dhawal Gupta, Hongli Zhan, Zhenting Wang, Varad Pimpalkhute, Zhengzhong Liu, Eric Xing, Rupesh Srivastava
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06868v1](http://arxiv.org/abs/2611.06868v1)
- **PDF:** [https://arxiv.org/pdf/2611.06868v1](https://arxiv.org/pdf/2611.06868v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In this work, we evaluate a simple inference-time scaling approach based on \textit{turn-level best-of-N sampling} (\method) for large language model (LLM) agents on complex, long-horizon tasks. We instantiate this using a \textit{generator-selector} framework with two LLMs; at each turn, a \emph{generator} model generates $N$ candidate actions and a \emph{selector} model selects one of them, which is then executed in the environment. This paper is closely related to the work of \cite{zainullina2025guided} who used critic models for guided search at inference time. Different from their work, we evaluate if off-the-shelf, open-weight LLMs can be effective at comparing different candidate actions directly. Experiments on long-horizon terminal tasks show that \method can lead to significant performance improvements, both in terms of accuracy (5--10\%) and consistency across repeated attempts. Analysis of agent trajectories reveal a shift in agent behaviour towards desirable patterns such as reduction in number of attempts to solve the task, improved task instruction following, debugging and testing.

</details>


### 81. The Two-Ledger Model: Transaction-Grain Cost Accounting for Multi-Agent AI Systems Across Clouds, Models, and Systems of Record

- **Authors:** Vivek Acharya
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06989v1](http://arxiv.org/abs/2611.06989v1)
- **PDF:** [https://arxiv.org/pdf/2611.06989v1](https://arxiv.org/pdf/2611.06989v1)
- **Categories:** cs.AI, cs.DC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprises run business transactions through multi-agent AI systems spanning clouds, large language models (LLMs), orchestration harnesses, and systems of record. Finance receives AI cost only at settlement grain, aggregated by SKU and charge period. The business question (what did this order, claim, or case cost in AI?) cannot be answered from billing data, because providers never see enterprise transaction boundaries. The FinOps Open Cost and Usage Specification (FOCUS) gives billing data one schema across providers but remains settlement-grain even as it adds AI token and requester attribution. We formalize this grain mismatch, derive seven requirements, and propose the Two-Ledger Model: a settlement ledger of FOCUS-conformant billing data joined to an attribution ledger of invocation-grain usage records built on OpenTelemetry GenAI telemetry. A layered correlation spine (trace context, A2A/MCP metadata, business-key correlation, probabilistic matching) assigns each record to its business transaction with recorded method and confidence; a versioned rate card prices usage in near real time; period reconciliation ties both ledgers to the invoice, and the unexplained residual identifies shadow AI. Costs are reported per order, claim, or outcome with agentic cost metrics. A simulation with known ground truth shows the spine sustaining cost coverage above 99% as trace propagation falls to zero, the reconciliation residual recovering planted unmetered spend within 0.24 percentage points while flagging provider billing errors, and mid-flight gating cutting p99 transaction cost by up to 61% at a 2-4% false-pause rate. We propose the attribution ledger as an invocation-grain FOCUS profile for standardization.

</details>


### 82. Airlock: Bounding the Multi-Agent Blast Radius via Selective Online Containment

- **Authors:** Zhonghao Zhan, Javad Forough, Yefan Zhang, Krinos Li, Xiao Ma, Hamed Haddadi
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06727v1](http://arxiv.org/abs/2611.06727v1)
- **PDF:** [https://arxiv.org/pdf/2611.06727v1](https://arxiv.org/pdf/2611.06727v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

When multi-agent systems act on the external world, a single agent's faulty output can spread across tasks before detection, creating a system-wide blast radius. Single-agent guardrails are confined to individual harnesses, while existing multi-agent controls either cancel only the faulty source and miss downstream consumers or halt and roll back the entire workflow at the cost of healthy work. We present Airlock, a multi-agent runtime and guardrail for selective post-alert fault containment. Its tree-structured runtime, EdgeCitadel, narrows permissions vertically from parent to child agents to establish node boundaries and control switches. Meanwhile, an append-only provenance DAG records cross-agent data consumption horizontally. Upon an alert, Airlock traces forward on this DAG to isolate tainted executions and pending actions, and backward to narrow root causes. At the site switches, a default full quarantine tier freezes affected branches without a solver, while an assured optimized cut tier uses fence-then-prune to enforce a deadline-aware minimum cut minimizing collateral disruption. Across 1,832 testbed runs, 161 physical smart-home LLM runs, and 24,266 simulation records, Airlock blocks all post-alert faulty actuations on our main testbed and smart-home grids with zero post-convergence leaks. Whereas native controls in A2A and LangGraph either contain at most 33.3% of faults or retain at most 16% of work without redo, Airlock retains +68 pp to +96 pp more healthy work, and its optimized cut retains +46 pp more than full quarantine under dense spread. These results show that co-designing runtime authority boundaries with online provenance enables surgical fault containment without sacrificing healthy work (code: https://github.com/EdgeCitadelTeam/EdgeCitadel).

</details>


### 83. SecureGARD: Dynamic Ontology-Guided Governance for Secure Tool-Using LLM Agents

- **Authors:** Guoqin Xiong, Shengtao Wen, Xiang Chen, Xinyi Zeng, Zhaoxin Fan, Wei Ye, Xiaofeng Cao, Sheng-Jun Huang
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06682v1](http://arxiv.org/abs/2611.06682v1)
- **PDF:** [https://arxiv.org/pdf/2611.06682v1](https://arxiv.org/pdf/2611.06682v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using large language model (LLM) agents translate model outputs into consequential actions, turning indirect prompt injection into an execution-security problem. Existing defenses constrain tool calls, trajectories, or information flows, but often leave action semantics, state dependencies, and evidence relations implicit, limiting generalization across heterogeneous tools and complicating safe updates. We present \ours{}, a dynamic ontology-guided governance framework. \ours{} grounds heterogeneous calls in a shared semantic representation and combines an executable ontology with episode-level task state to derive deterministic ready, waiting, and forbidden decisions. A waiting decision identifies an unmet but recoverable obligation, enabling bounded replanning without expanding the agent's authorization boundary. \ours{} evolves its ontology offline from verified training executions. An offline LLM proposes instance-independent action--state axioms, which are accepted only if they address ontology errors exposed by training failures, preserve logical consistency and protected entailments, and pass held-out validation before the ontology is frozen. We evaluate \ours{} on AgentDojo, ASB, and AgentDyn under benign and indirect prompt-injection settings. \ours{} achieves a 0\% attack success rate (ASR) across all three benchmarks while improving task utility under attack compared with existing baselines. These results show that explicit semantic governance can strengthen execution security without indiscriminate blocking.

</details>


### 84. AgentTrustCI: Build-Time Policy, Grounding, and Trajectory Tests for Java LLM Agents

- **Authors:** Sachin Gupta
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06674v1](http://arxiv.org/abs/2611.06674v1)
- **PDF:** [https://arxiv.org/pdf/2611.06674v1](https://arxiv.org/pdf/2611.06674v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Infrastructure security does not establish whether an LLM agent selected an allowed tool, grounded its answer in tool output, or followed a required workflow. AgentTrustCI is a Java/JUnit 5 framework that expresses these application-layer expectations as policy, grounding, and trajectory checks over recorded traces. A deterministic replay implementation supports repeatable build-time tests; a judge interface provides an extension point for optional semantic evaluation. On 55 synthetic cases spanning seven enterprise domains, the full pipeline correctly classifies all 30 injected faults and 25 passing controls, including ten non-trivial controls, and misses none of 12 designated critical cases. Each single-layer configuration correctly classifies 35 cases because the corpus deliberately isolates ten faults per layer. A grounded answer obtained through a disallowed sequence illustrates the additional coverage of trajectory checks. Repeated measurements quantify validator execution separately from process startup and reporting. These results establish coverage of the authored regression suite, not production accuracy. We describe a production-trace validation protocol, optional LLM-judge integration, and maintenance of expectations as workflows evolve. The contribution is a practical pattern for expressing behavioral contracts within an existing Java release pipeline.

</details>


### 85. Signed, Sealed, Leaked: Trust Beyond Signature for MCP Toolchains

- **Authors:** Yichiet Aun, Mohammed A. Alhartomi, Jing Jie Tan, Waqas Nadeem, Adeb Salh, Shankar Karuppayah, Sin Chee Tan
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06585v1](http://arxiv.org/abs/2611.06585v1)
- **PDF:** [https://arxiv.org/pdf/2611.06585v1](https://arxiv.org/pdf/2611.06585v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents rely on third-party tools, such as Model Context Protocol (MCP) servers, whose publishers can be authenticated and whose execution can be restricted by runtime security policies. Yet authenticity does not guarantee benign behaviour: a legitimately signed tool may perform its advertised function while concealing malicious code that leaks confidential information. We demonstrate this trust failure with a signed MCP tool that embeds sensitive data in requests to a policy-allowed destination. Meta's MCPGuard-Dynamic, a state-of-the-art runtime defence, blocks a direct exfiltration attempt in the same run, yet fails to prevent this attack in every trial. We introduce germline execution, which limits information disclosure without inspecting or trusting tool implementations. Each tool invocation runs in ephemeral copies forked from a data-free germline process, each receiving only information authorised for its destination. Even if malicious code executes, what it can disclose is bounded by the data available to its copy. Under explicit assumptions on copy confinement and a data-free germline, we prove sink noninterference for every signed release and, for releases deterministic within our replay model, show that a verified witness establishes a flow violation. Across 153 attack runs, no unauthorised disclosure was detected under germline execution, compared with 5.9-74.5% of runs under baseline defences and an ablation. Invocations served by a single copy completed in 10-49 ms, 2-28x faster than restarting the tool for every invocation, the conventional way to clear state. These results show that data-isolated execution protects agent toolchains against malicious code concealed within authenticated software.

</details>


### 86. RAGAM-AI: A Hybrid Reinforcement Learning based Agentic approach powered by Generative AI for Edge Resource Management

- **Authors:** Shreya K. Chari, John S. Vardakas, Kostas Ramantas, Christos Verikoukis
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06554v1](http://arxiv.org/abs/2611.06554v1)
- **PDF:** [https://arxiv.org/pdf/2611.06554v1](https://arxiv.org/pdf/2611.06554v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Resource management for distributed edge networks hosting different services has been handled efficiently using Reinforcement learning (RL). Reward generalization in complex workflows is still an open issue within the RL realm. Therefore, this work proposes RAGAM-AI, a hybrid framework that combines the capabilities of RL algorithms and Generative-AI (Gen-AI) for powering an Agentic AI workflow that optimizes resource allocation at the Multi-access Edge Computing (MEC) units. This framework further resolves the reward generalization issue by utilizing Large Language Model (LLM) for feedback. A Multi- Agent Soft-Actor Critic (MASAC) using MathΣtral as a reward oracle is implemented for managing resource allocations at the MEC. RAGAM-AI interprets system state information and evaluates multi-objective trade-offs guiding the resource orchestration loop over distributed edge server agents. The complexity of the framework is further brought down by incorporating surrogate reward model. The overall performance is evaluated against the single agent SAC, REINFORCE and random policies for benchmarking. On using RAGAM-AI, lower allocation deviations for CPU, memory and bandwidth resources are reported while minimizing the latency and data rate costs. A scalable AI as a feedback (AIAF) solution optimizing network resources with significant performance improvement is thus presented.

</details>


### 87. When Do Summaries Become Instructions? Unsupported Policy in LLM Agents' Self-Written Handoff Summaries

- **Authors:** Wenhui Chu
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06545v1](http://arxiv.org/abs/2611.06545v1)
- **PDF:** [https://arxiv.org/pdf/2611.06545v1](https://arxiv.org/pdf/2611.06545v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-running LLM agents compact their context, replacing most history with a summary. We ask whether handoff summaries state permissions or requirements the record does not support, whether such sentences change what the next instance (the successor) does, and where they come from. Synthetic tool-use tasks carry a ground-truth permission ledger; same-snapshot replay reruns the successor with those whole sentences replaced by neutral filler. Two AI readers, reading only rule-flagged held-out summaries, confirmed unsupported restrictions in 1.2% and 2.4% of all readable summaries from two open-weight models, and unsupported authorizations in 0.1% and 1.3%. For restrictions, a pre-specified replay test was not significant (p = 0.58); a follow-up, planned after it, found a fragile effect (p = 0.027). Neutralizing false approvals cut unauthorized actions from 24 to 7 of 120 held-out runs (post hoc; later set: 17 to 11 of 48). Most development restrictions followed the agent's earlier reasoning that an action needs approval (post hoc). In pre-specified tests, replacing the system prompt's "Some actions need approval." with one saying where requirements come from cut unsupported restrictions from 5.0% to 1.8% of development summaries and, on held-out templates, from 1.8% to 0.3% (both p < 10^-9), while requests for approvals the ledger requires barely changed. Code and data: https://github.com/Chuw1/handoff-audit

</details>


### 88. Tools Need Not Speak in Text: Latent Context Compression for Agents

- **Authors:** Yuetong Liu, Zhehao Zhou, Yitong Zhang, Haorui Chen, Jia Li
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06500v1](http://arxiv.org/abs/2611.06500v1)
- **PDF:** [https://arxiv.org/pdf/2611.06500v1](https://arxiv.org/pdf/2611.06500v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents typically append raw tool outputs to their context. Over multi-step interactions, long and noisy observations incur substantial context overhead and dilute the agent's attention to task-relevant information. Existing token pruning and summarization methods remain constrained by discrete text representations, limiting the achievable compression ratios.
  In this work, we challenge the prevailing assumption that agents must consume tool observations as explicit text tokens. To this end, we propose Coca-Cola, a continuous latent context compression model for LLM agents. Coca-Cola compresses tool observations into latent tokens and embeds them into the input embedding space of the agent. We further introduce Action-Preserving Training, which aligns the agent's next-action distributions under full and compressed observations. This trains the compression model to learn action-sufficient latent tokens that retain decision-critical information. Experiments with web-search agents on four QA benchmarks and two model families show that Coca-Cola reduces the agent's token consumption by 70.01%-89.24% and end-to-end runtime by 24.45%-55.97%, while consistently improving task performance. These results suggest that Coca-Cola offers a promising approach for context compression in agents. Our code is available at https://github.com/THU-Agent/Coca-cola.

</details>


### 89. What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?

- **Authors:** Kejian Zhu, Zhuoran Jin, Shangqing Tu, Tianyi Men, Yupu Hao, Jiachun Li, Kang Liu, Jun Zhao
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06483v1](http://arxiv.org/abs/2611.06483v1)
- **PDF:** [https://arxiv.org/pdf/2611.06483v1](https://arxiv.org/pdf/2611.06483v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth $K$ and interaction depth $T$ via $Pass@(K,T)$, we show that trajectory-level RL advantages depend on sufficient turn budgets, diminishing significantly when budgets tighten. Besides, agentic RL does not uniformly elevate single-step decision quality; rather, its strength concentrates in error recovery and long-horizon resilience. To mitigate the deployment risks caused by this budget dependence, we provide a preliminary discussion on the benefits and limitations of process supervision signals and introduce BudgetMix RL as an alternative that varies interaction budgets during training. Experiments demonstrate that BudgetMix RL achieves robust performance across diverse execution settings. Project Page: https://rethinking-agentic-rl.github.io/

</details>


### 90. Zero-Shot Coordination among LLM Agents

- **Authors:** Adrian Hayler, Shashank Reddy Chirra, Andrei Lupu, Johannes Forkel, Bidipta Sarkar, Siheng Feng, Jakob Foerster
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06409v1](http://arxiv.org/abs/2611.06409v1)
- **PDF:** [https://arxiv.org/pdf/2611.06409v1](https://arxiv.org/pdf/2611.06409v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study zero-shot coordination (ZSC), where independently developed agents must coordinate at test time. While ZSC has been well studied in the RL literature, far less is known about the performance of LLM agents despite their increasing deployment in such settings. Existing work on LLM coordination often relies on specialised scaffolding that independently developed agents are unlikely to share in practice. Moreover, evaluations on complex environments (e.g., Hanabi) make it difficult to pinpoint the sources of coordination failure. In contrast, we focus on simple, general-purpose scaffolds in minimal environments designed to isolate specific coordination challenges. Our results show that even in these controlled settings, frontier LLM agents struggle to coordinate, largely due to limited understanding of the coordination problem and weak reasoning about their partner's beliefs. While LLMs introduce semantic information as an additional axis for coordination, they nonetheless fail to exploit this structure effectively. Towards this, we propose Coordination-friendly definitions (CFDs) as a principled approach for enabling robust coordination among LLM agents. Finally, we show that CFDs can be discovered automatically, removing the need for manual engineering. Code is available at https://github.com/ahayler/zsc-llm-agents.

</details>


### 91. MA-Mesh: Resilient Multi-Agent Collaboration via Role-based Self-Healing

- **Authors:** JunYong Lee, Woo Kyung Kim, Honguk Woo
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06389v1](http://arxiv.org/abs/2611.06389v1)
- **PDF:** [https://arxiv.org/pdf/2611.06389v1](https://arxiv.org/pdf/2611.06389v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Effective collaboration in multi-agent systems requires mechanisms for coordination and adaptability in dynamic and uncertain environments. However, existing multi-agent systems rarely model resilience explicitly, instead relying on ad-hoc output correction that limits systematic, runtime management of robustness. In this work, we propose Multi-Agent Mesh (MA-Mesh), a framework that constructs a role-based self-healing layer on top of a collaboration pattern. Specifically, MA-Mesh generates resilience-aware system specifications and synthesizes them into executable multi-agent policy code. To enhance resilience, we introduce two self-healing mechanisms: Cross-agent reflection, a mechanism that allows agents to evaluate not only their own outcomes but also the performance of their peers, enabling informed behavioral adjustments and collective policy refinement; Role-based failover, a strategy which dynamically reassigns roles and enables agents to substitute for one another when sub-tasks fail or agents underperform, ensuring continuity of task execution. Experimental results across diverse tasks (e.g., software development, tool use, scientific reasoning) demonstrate that MA-Mesh significantly outperforms existing multi-agent systems in both task performance and robustness under system uncertainty.

</details>


### 92. From hydrological laws to catchment models: A process-based model matches deep-learning accuracy on three continents

- **Authors:** Xilin Xia
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06382v1](http://arxiv.org/abs/2611.06382v1)
- **PDF:** [https://arxiv.org/pdf/2611.06382v1](https://arxiv.org/pdf/2611.06382v1)
- **Categories:** cs.LG, cs.AI, math.DS, physics.geo-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

Dooge asked whether hydrology has laws at the catchment scale. We ask whether a low-dimensional system built under physical laws can match the accuracy of neural networks that outperform process-based models on the same inputs. Three laws constrain a lumped catchment model. Conservation makes it a flux-connected storage network, dissipation fixes the sign of every flux and aggregation determines how the unresolved composition enters the fluxes, through effective laws over threshold distributions and a memory of the forcing. These laws admit four kinds of refinement. A parsimonious model under them, CaRT (11 parameters per catchment), is refined in a loop assisted by AI agents. Each refinement addresses an observed deficit through a hypothesis from the literature. The result, CaRT+, has fourteen states, 35 parameters per catchment and no daily neural network. Most refinements follow from aggregation over thresholds or from variables that carry no water but modulate fluxes. On 602 British and 593 US gauged catchments, single CaRT+ models reach median Nash-Sutcliffe efficiencies of 0.863 and 0.765 in held-out years. A stateful LSTM reaches 0.869 and 0.751 and an entity-aware LSTM 0.862 and 0.754, while three-seed LSTM ensembles remain ahead of the CaRT+ ensemble by 0.003-0.012 in median paired NSE. On 505 drier Australian gauged catchments unused in development, single CaRT+ models reach 0.778 against 0.762 and 0.753 for the two LSTMs. The results suggest that catchment-scale laws exist as laws of form, with the constitutive families shared and only their parameters learned.

</details>


### 93. Corralling AI Risks with Grassroots Contracts

- **Authors:** Ehud Shapiro
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06374v1](http://arxiv.org/abs/2611.06374v1)
- **PDF:** [https://arxiv.org/pdf/2611.06374v1](https://arxiv.org/pdf/2611.06374v1)
- **Categories:** cs.AI, cs.CL, cs.DC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI's inflection point is a fountain of alarming risks. Digital platforms in particular are vulnerable to three major AI risks, as those in control of global platforms cede control to AI, of the algorithms, of membership and of content: (1) AI control of global platforms, social and economic, used by the majority of humanity, resulting in the majority of humanity becoming vulnerable to AI control. (2) Unaccountable AI agents operating anonymously on social and economic digital platforms, side-by-side with humans, possibly masquerading as humans, serving unknown masters with unknown goals, operating under unknown restraints without accountability or culpability. (3) Unattributed deepfakes generated by anonymous AI, with people unable to distinguish them from genuine content and with their producers evading accountability and culpability.
  Here, we propose to corral these AI risks with grassroots contracts, a digital incarnation of a two-centuries old notion of Pierre-Joseph Proudhon. We present grassroots contracts for a social graph with accountable AI agents and for a social network with digital provenance, and working smartphone apps that implement the two and show how they corral these major AI risks: (1) AI control of global platforms. (2) Unaccountable AI agents. (3) Unattributed deepfakes.

</details>


### 94. Analysis of Local Open-Weight LLM Agents on Vulnerability-Reproduction Tasks

- **Authors:** Jorge García-Carrasco, Javier Sanchis, Álvaro Navarro, Alejandro Maté, Juan Trujillo
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06257v1](http://arxiv.org/abs/2611.06257v1)
- **PDF:** [https://arxiv.org/pdf/2611.06257v1](https://arxiv.org/pdf/2611.06257v1)
- **Categories:** cs.CR, cs.LG, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Open-weight language models that fit on a single consumer GPU are becoming capable on a growing range of tasks, and they matter because they can run locally without sending the code to a hosted service. Vulnerability reproduction, turning a vulnerability description into an input that crashes the vulnerable build, is a natural target for them, since it is an automated analysis task closer to test generation than to code comprehension and it runs against a build that must be executed rather than read. In order to assess whether current models can perform it, we evaluate twelve configurations of local models, spanning three generations, two architectures and three quantization levels, on ten CyberGym vulnerability-reproduction tasks, three runs each under one harness, and release the full artefact. We show that every configuration, down to the 4B model, solves most of the six easier tasks, and configurations separate only on the remaining four. For the harder tasks, the 27B model is required. Quantization did not change what the models solved in any matched pair, but it changed how fast they got there, and the mixture of experts reached the same scores in less wall clock. We also examine the agent trajectories. Almost every run we examined, including those that fail, names the vulnerable function and states the correct hypothesis, and what separates a solved task from an unsolved one is whether that hypothesis becomes a working input.

</details>


### 95. HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents

- **Authors:** Zhi Hong, Qianlong Wang, Hongchen Wei, Aidan Wu, Daohong Ying, Mingze Kong, Bei Liu, Chong Luo
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06254v1](http://arxiv.org/abs/2611.06254v1)
- **PDF:** [https://arxiv.org/pdf/2611.06254v1](https://arxiv.org/pdf/2611.06254v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The performance of large language model (LLM) agents depends on both the underlying model and the harness that governs interaction with tools and the environment. Yet harness design remains largely manual, and automating it requires navigating an open-ended search space through costly end-to-end evaluations. We introduce HarnessFlow, a framework for optimizing complete executable harnesses under a limited candidate-evaluation budget, with the model and task environment held fixed. HarnessFlow organizes candidates and their evaluation histories in a refinement tree, using a Monte Carlo Tree Search (MCTS)-based policy to balance exploitation and exploration. A coding agent refines selected harnesses using archived code, execution feedback, and a library of reusable harness mechanisms. With 15 refinement attempts per benchmark, HarnessFlow achieves the highest mean test scores among the compared methods on six benchmarks spanning agentic tasks, coding, and web interaction. The optimized harnesses achieve an average score of 69.48%, outperforming the initial harnesses and Meta-Harness by 10.89 and 3.95 percentage points, respectively, while incurring lower average per-task execution costs than hand-engineered baselines. These results suggest that structured harness search offers a promising route toward automating the design of capable and efficient LLM agents.

</details>


### 96. A Definition of Catastrophic Performance

- **Authors:** Henrik Marklund, Alex Infanger, Benjamin Van Roy
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06219v2](http://arxiv.org/abs/2611.06219v2)
- **PDF:** [https://arxiv.org/pdf/2611.06219v2](https://arxiv.org/pdf/2611.06219v2)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

A central challenge in AI is specifying objectives that align with human preferences. While existing theoretical results elucidate how misspecification impacts performance, they typically do not distinguish between merely suboptimal and catastrophic outcomes. To enable rigorous analysis of catastrophic risk from AI misalignment, we introduce a formal definition of catastrophic performance. Our definition is based on two reference values. The first, baseline value, captures the value attained if no agent is deployed. The second, orthogonal value, captures the value of a trajectory that is unrelated to human preferences, in a sense we describe. Orthogonal value is typically far worse than baseline value. We interpret these reference values through examples in which past human activity has altered the state of the environment to human benefit. Starting at the resulting state, an AI agent is deployed with the goal of accelerating further progress. Catastrophic performance represents this agent's undoing of benefits afforded by human activity.

</details>


### 97. Formalizing inverse problems in the age of AI: possibilities, pitfalls, and an invitation

- **Authors:** Christian Clason, Tapio Helin, Medet Nursultanov, Lauri Oksanen
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06962v1](http://arxiv.org/abs/2611.06962v1)
- **PDF:** [https://arxiv.org/pdf/2611.06962v1](https://arxiv.org/pdf/2611.06962v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Proof assistants such as Lean check mathematical proofs down to the axioms, and AI agents have recently made writing such proofs cheap. We describe AutoIP, a Lean library in which classical linear regularization theory, together with the functional analysis it rests on, has been autoformalized by AI agents. A machine-checked proof certifies only the formal statement it proves, so the remaining human task is to confirm that each formal statement says what was intended. We organize the library around this task: a reviewer compares the formal statements with their natural-language counterparts and never needs to read a proof. Our experience is that the risks lie in the statements rather than in the proofs, and that simple automated tests on the statements can expose problems even in the established literature. We illustrate this with a textbook theorem whose hypothesis is more restrictive than asserted. We invite the inverse problems community to extend and build on the library.

</details>


### 98. A Controlled Experimental Evaluation of Configuration and Cache Architecture in LLM Serving Engines

- **Authors:** Muhammad Faizan Anwar, Sina Keshvadi
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05991v1](http://arxiv.org/abs/2611.05991v1)
- **PDF:** [https://arxiv.org/pdf/2611.05991v1](https://arxiv.org/pdf/2611.05991v1)
- **Categories:** cs.DC, cs.LG, cs.PF


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM applications repeat most of their prompt tokens across requests, and serving engines reuse the cached state of shared prefixes. vLLM and SGLang reuse it at different granularities, and benchmarks of their default deployments report large performance gaps, usually credited to the cache. Such comparisons rarely control for other configuration differences. One of them, whether a long prompt is prefilled in chunks, is set by each engine's defaults from the hardware and the release, and it confounds the comparison. We built a reproducible testbed on Kubernetes and a seeded multi-agent workload generator, and compared the two engines under vendor defaults and with chunked prefill matched. SGLang's configuration is the same in both arms, which makes it an internal control across independently provisioned deployments. Under defaults, vLLM's median time to first token is up to 64x SGLang's. Matching one setting removes 78% of the capacity gap where that gap is largest and 30 to 67% of the latency gap. Near saturation the remaining latency gap reflects queue growth. A fluid queue model driven only by a 4.4% throughput shortfall reproduces it, and shows that such a gap scales with the length of the benchmark run. What survives matching is a tail-latency advantage of 2.4 to 6.4x at equal throughput, consistent with cache-aware ordering of waiting requests. We derive six recommendations for comparing serving engines.

</details>


### 99. Graph-Mediated Large Language Model Systems in the Agentic Era: Reasoning, Knowledge, Retrieval, Execution, and Coordination

- **Authors:** Haihui Liu, Yang Chen, Zice Qiu, Yun Zhang, Jialun Zhong, Wenhua Wang, Yanzeng Li, Tian Wang
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05953v1](http://arxiv.org/abs/2611.05953v1)
- **PDF:** [https://arxiv.org/pdf/2611.05953v1](https://arxiv.org/pdf/2611.05953v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Graphs play an increasingly important role in large language model (LLM) systems, supporting structural reasoning, knowledge grounding, retrieval, and memory. As these systems evolve toward the agentic era, graphs also organize execution dependencies and multi-agent communication, linking intermediate observations and retained information to subsequent decisions. However, understanding their contribution requires distinguishing the function of each graph operation, the component responsible for its computation, and the subsequent use of its output. This survey introduces an operation-level role--locus taxonomy for reasoning, knowledge and evidence, retrieval and memory, execution, and coordination. We compare how graph observations and external computations guide decisions, how memory representations and updates support later tasks, and how dependencies constrain execution and information delivery. These comparisons distinguish improvements in local metrics from downstream task performance while retaining the conditions under which results were reported. We then organize benchmarks, comparison designs, process diagnostics, and system costs into an evaluation framework. Finally, we identify open challenges in adaptive computation and stopping, memory maintenance, and dependency-aware recovery. The survey provides a basis for assessing when graph mechanisms are useful and for evaluating their effects across components and stages.

</details>


### 100. Autonomous agents for electricity-system planning

- **Authors:** Yoon Pyo Lee, Samrendra Roy, Jay Phil Yoo, Kazuma Kobayashi, Souvik Chakraborty, Syed Bahauddin Alam
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05911v1](http://arxiv.org/abs/2611.05911v1)
- **PDF:** [https://arxiv.org/pdf/2611.05911v1](https://arxiv.org/pdf/2611.05911v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Planning electricity systems requires repeated decisions that connect regional resources, investment, operation and network constraints. Here we present an autonomous planning framework that carries prepared regional scenarios through proposal, numerical evaluation, feedback interpretation, redesign and final plan selection. Agents propose investment bounds, storage operating conditions and feeder interventions, interpret numerical feedback, and decide how to revise designs and when to stop. The framework automatically executes annual investment-and-dispatch optimization and representative-feeder verification, applies fixed acceptance criteria and retains the lowest-cost accepted candidate. We evaluate forty carbon-constrained trajectories across ten system-year scenarios in five electricity systems and four countries, using two model deployments and single- and multi-agent architectures. All forty retain candidates satisfying the implemented physical and fixed annual operational carbon-budget checks. Twenty-eight of forty matched reference designs exceed the new scenario ceilings. A separate archive of ninety-six trajectories under a common 1,000 Mt annual ceiling provides matched references and broader regional coverage. The results demonstrate autonomous planning under explicit emissions constraints using public regional data and published institutional demand outlooks.

</details>


### 101. Autonomy and Coordination in Intelligent Manufacturing: A Recursive Autonomous Agent Framework

- **Authors:** Yuning Chen, Hongda Zhang, Linqiang Hu, Ziqing Zhou, Yi Liu, Zhao Huang, Ding Zhou, Haining Xu
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05828v1](http://arxiv.org/abs/2611.05828v1)
- **PDF:** [https://arxiv.org/pdf/2611.05828v1](https://arxiv.org/pdf/2611.05828v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Intelligent production requires systems to make decisions and organize work according to production goals and operating conditions. It also requires continuous adjustment through feedback. This paper analyzes intelligence in human production organizations from a complex adaptive systems (CAS) perspective. The analysis identifies two coupled mechanisms: individual autonomy and collective coordination. Individual autonomy enables actors to form local decisions using available information. Collective coordination aligns these decisions with shared goals and joint constraints. Learning and adaptation improve both mechanisms over time. A production-system model formalizes how local decision rules and coordination jointly form system decisions. On this basis, we propose the Recursive Autonomous Agent (RAA) framework, which combines goal-driven autonomous agents with a recursive organizational structure. Goal contracts define local objectives and operating boundaries, while capability contracts support the selection and composition of production units. Common interfaces allow coordinated groups to participate as units in larger organizations, connecting equipment, production lines, and factories. RAA thus provides an engineering approach to next-generation intelligent manufacturing, translating the requirements of intelligence, openness, and system-wide integration into mechanisms for autonomous and coordinated production.

</details>


### 102. TandemBench: Benchmarking Decision Models for Multi-Agent Collaboration

- **Authors:** Baohang Li, Xiaocheng Feng, Bing Qin
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05827v1](http://arxiv.org/abs/2611.05827v1)
- **PDF:** [https://arxiv.org/pdf/2611.05827v1](https://arxiv.org/pdf/2611.05827v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Decision models choose among predefined options in tasks such as routing and action selection. In multi-agent collaboration, a decision determines how members divide work, exchange resources, and act in parallel. We introduce TandemBench, a benchmark of 1,200 questions in multi-agent cooking scenarios where coordination choices affect goal completion. Models receive complete global information and candidate team plans, with reference answers established through execution and exact search. Models select an optimal team plan and, in paired variants that retain or remove it, judge whether better arrangements exist beyond the supplied options. We evaluate 40 native decision models and compare them with 10 general-purpose language models. The best native decision model achieves 62.50% decision accuracy. Native decision models remain close to chance in optimality verification. Paired tests reveal that some report better alternatives regardless of whether an optimal plan is already present. These findings show that team-plan decision accuracy alone can conceal systematic errors in judging whether the supplied options contain an optimal arrangement. The dataset and evaluation code are publicly available at https://github.com/lililibaohang/TandemBench.

</details>


### 103. A Hybrid Approach for Automated Security Pattern Recovery

- **Authors:** Anh Minh Nguyen, Tuan Dat Tran, Alzubair Hassan, Liliana Pasquale
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05823v1](http://arxiv.org/abs/2611.05823v1)
- **PDF:** [https://arxiv.org/pdf/2611.05823v1](https://arxiv.org/pdf/2611.05823v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Security-by-design emphasises integrating security into software design and development. Security pattern catalogues operationalise this principle by prescribing reusable architectural solutions to recurring security problems. However, recovering their implementations from source code remains challenging because security patterns are abstract, span multiple components, and admit many valid implementations. We present SecPatRec, a hybrid approach for automated security pattern recovery from source code repositories. We treat a security pattern as a reference architecture and frame its recovery as a deductive task: determining which prescribed roles are present, grounding them in code entities, and recovering their interaction sequences. SecPatRec pairs a ReAct-style LLM agent equipped with semantic and lexical code search for role detection and grounding with static code property graph analysis for interaction recovery. We curate a human-validated ground-truth dataset of 100 pattern instances covering five security patterns across 93 open-source Java and Python repositories, and introduce a three-level evaluation framework measuring recovery correctness against this ground truth. We evaluate SecPatRec using four LLMs, including proprietary and open-source models. Averaged over all models and pattern instances, SecPatRec achieves role-detection accuracy of 0.84, role-grounding similarity of 0.84, and an interaction-recovery score of 0.66. Compared to a one-shot end-to-end LLM baseline, SecPatRec achieves higher aggregate recovery scores and lower estimated LLM API costs per run, while processing repositories that exceed the baseline's configured input limit. The recovered role mappings and statically derived interaction sequences provide structural and behavioural evidence that can support inspection of security-pattern implementations.

</details>


### 104. Learning When Human Decisions Matter: Executor-Relative Consultation Value for LLM Agents

- **Authors:** Shuli Jiang, Khushbu Pahwa, Yuting Zhang, Yi Zhang, Wei Xia, Stefano Soatto
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05814v1](http://arxiv.org/abs/2611.05814v1)
- **PDF:** [https://arxiv.org/pdf/2611.05814v1](https://arxiv.org/pdf/2611.05814v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models increasingly automate complex tasks, but human decision capacity does not scale with their capabilities. In many applications, humans remain essential for providing private context, authority, or judgments unavailable to the agent. We formulate human decision capacity allocation: given multiple consultation opportunities and a limited budget, at which decisions should an LLM agent consult a human? The central challenge is estimating consultation value, which is executor-dependent because the same human input may benefit different downstream agents differently. We introduce Consultation Value Distillation (CVD), which estimates consultation values offline using Monte Carlo executor rollouts and distills these values into lightweight predictors for budgeted allocation, requiring no rollout-based value estimation at deployment. Across five batch and three sequential settings with two frontier executors, CVD improves allocation through joint and continuation-aware value learning, while independent consultation values remain competitive in several settings. CVD also broadly outperforms direct prompting and Value of Information where applicable, remains robust with substantially less rollout supervision, and enables nearly lossless approximate allocation at low search cost.

</details>


### 105. WayPOP: A Panoramic Open-Set Panoptic Tracking Benchmark

- **Authors:** Rohit Mohan, Maximilian Luz, Swarnava Chowdhury, Yao Lu, Florian Drews, Thomas Nürnberg, Yakov Miron, Federico Tombari, Stefano Gasperini, Abhinav Valada
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05801v1](http://arxiv.org/abs/2611.05801v1)
- **PDF:** [https://arxiv.org/pdf/2611.05801v1](https://arxiv.org/pdf/2611.05801v1)
- **Categories:** cs.CV, cs.LG, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Holistic perception for autonomous agents requires reliably segmenting and associating scene elements across time and camera views, including objects outside a fixed semantic taxonomy. Existing open-set panoptic benchmarks focus on individual images or views, while panoramic tracking benchmarks assume closed-set taxonomies. Consequently, these benchmarks do not evaluate whether unknown objects can be consistently segmented and tracked across synchronized multi-camera sequences. We introduce WayPOP, a panoramic open-set panoptic tracking benchmark built on real Waymo PVPS sequences augmented with diverse out-of-taxonomy 3D assets from Objaverse. Inserted objects are placed at fixed locations in the 3D scene and rendered using calibrated vehicle-mounted cameras as the ego vehicle and surrounding traffic move, providing temporally and cross-view consistent panoptic annotations and auxiliary LiDAR range observations. WayPOP contains approximately 670 curated assets instantiated as 980 unique unknown-object tracks, yielding 53,452 unknown-object mask annotations across 21,300 camera images. Our evaluation protocol defines a hierarchy of tasks from view-independent open-set panoptic segmentation to full panoramic open-set panoptic tracking, using known/unknown PQ and (w)STQ metrics. We benchmark representative open-set and open-vocabulary segmentation methods with temporal and cross-camera association. Our results reveal substantial limitations of current methods in truly open-set scenarios, highlighting robust unknown-object localization and identity association across time and views as major open challenges.

</details>


### 106. FlyHash for LLM Agent Memory: An Empirical Validation and a New Application

- **Authors:** Mohan Bheemadolu, Chrisogonas O. Odhiambo
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05791v1](http://arxiv.org/abs/2611.05791v1)
- **PDF:** [https://arxiv.org/pdf/2611.05791v1](https://arxiv.org/pdf/2611.05791v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly rely on external memory stores to retain information across conversations, typically via dense vector embeddings searched with approximate nearest-neighbor methods. The fruit fly's olfactory circuit computes a locality-sensitive hash of sensory input using a strikingly different mechanism - sparse random projection followed by winner-take-all competition - and prior work (Dasgupta et al., 2017) showed this scheme, dubbed FlyHash, preserves neighbor structure better per bit than conventional random-hyperplane hashing (SimHash) on several benchmarks. We apply FlyHash, to our knowledge for the first time, to LLM agent memory retrieval, and ask three questions a practitioner actually needs answered: does the quality advantage hold under a correctly matched-bit protocol (it does, robustly, across 10 seeds and four datasets spanning two modalities, with one specific, previously undocumented comparison pitfall identified and corrected along the way); does that advantage translate into real memory and latency savings, including against the dense-vector indexing (HNSW) practitioners default to today (no: at equal bits FlyHash's codes are larger and slower to compare than SimHash's, and HNSW dominates both hash methods at ordinary scale; a sparse-set comparison we introduce recovers most but not all of a naive latency gap, leaving hashing's practical case narrower and more specific than the quality result alone implies); and does the advantage survive genuine, non-circular agent-memory relevance labels rather than the nearest-neighbor-by-embedding proxy this literature otherwise relies on (it does). We report all three answers precisely, including the two that narrow rather than flatter the headline result, and release our implementation, a working agent-memory demo, and a full account of the methodological pitfalls we found and corrected.

</details>


### 107. BobFlow: Towards Human-Agent Collaborative Data Science Using Dataflows

- **Authors:** Jiadong Bai, Yicong Huang, Chen Li
- **Published:** 2026-11-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05761v1](http://arxiv.org/abs/2611.05761v1)
- **PDF:** [https://arxiv.org/pdf/2611.05761v1](https://arxiv.org/pdf/2611.05761v1)
- **Categories:** cs.DB, cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in large language models (LLMs) have established human-agent collaboration as a promising paradigm for data science. Effective collaboration requires a shared computational abstraction that enables agents to reason about processing logic while allowing human analysts to understand, guide, and refine the analysis. Although scripts written in Python or SQL provide precise control, their syntax and execution details can be difficult for analysts to understand and modify. In this paper, we argue that dataflows are an effective abstraction for human-agent collaboration in data science. We introduce BobFlow, a system that combines the dataflow abstraction with the ReAct paradigm. It enables agents to iteratively construct and execute dataflows for data science tasks while allowing analysts to inspect the analysis and provide feedback. Our user study shows that BobFlow helps analysts understand, inspect, and verify agent-generated analyses. A thorough experimental evaluation across proprietary and open-weight LLMs shows accuracy score gains of up to 18.6 points at just over 1/3 of a script-based ReAct agent's inference cost.

</details>


### 108. PAYWORTHY: Can LLMs Predict Which Freelance Jobs an AI Agent Will Complete?

- **Authors:** Mohammad Reza Rezaei, Dingxian Wang, Brett Levert, Celeste Fejzo, Andrew Rabinovich, Zhao Chen
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05759v1](http://arxiv.org/abs/2611.05759v1)
- **PDF:** [https://arxiv.org/pdf/2611.05759v1](https://arxiv.org/pdf/2611.05759v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Before an AI agent takes on a paid job, someone has to judge whether it is likely to succeed. We test whether frontier language models can make this call before any attempt. We propose PAYWORTHY which contains 1{,}494 real freelance job postings, sampled from 18.8M postings made between 2020 and 2026 on a freelancing platform. An agent attempts each job from the posting alone in a single run, and an LLM judge acting as the client decides whether to accept the work. We ask 18 models to forecast how likely the agent is to succeed and measure how well each model's forecasts rank the accepted jobs above the rejected ones (AUC, where 0.5 is a random ranking). The answer depends on how the agent is described. Told what the agent cannot do, every model ranks the jobs well (AUC 0.66--0.86). Told instead that it is a generic agent with a browser and code execution, the same models rank the same jobs about as well as a random ordering (0.45--0.56). These results hold under judges from four other model families (Claude, GLM, Kimi and Qwen), and the informed forecasts also rank the verdicts of two human raters.
  Code is available at https://github.com/upwork/Payworthy

</details>


### 109. Prospective Memory for Proactive LLM Agents

- **Authors:** Yuanchen Bei, Zhining Liu, Tianxin Wei, Weizhi Zhang, Zhichen Zeng, Philip S. Yu, Hendrik Hamann, Jingrui He, Hanghang Tong
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05731v1](http://arxiv.org/abs/2611.05731v1)
- **PDF:** [https://arxiv.org/pdf/2611.05731v1](https://arxiv.org/pdf/2611.05731v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Most memory systems for LLM agents are retrospective, preserving and retrieving past information to inform current decisions. Proactive agents, however, also require prospective memory: retaining future-directed intentions and realizing them when appropriate opportunities arise, even without explicit requests. Crucially, remembering the right intention does not guarantee acting at the right time: a related observation may call for waiting, while a later cue may make the same intention actionable. Inspired by cognitive theories of human prospective memory, we introduce Pro-Memory, a memory framework that separates maintaining future intentions from deciding when and how to realize them. Pro-Memory preserves pending objectives linked to their supporting evidence, assesses new observations against their original goals and activation conditions, and coordinates appropriate contributions with the agent's ongoing actions. It further updates intention states based on actions actually issued or evidence of resolution, while an experience memory distills feedback from completed episodes into guidance for future decisions. Experiments on two benchmarks spanning delayed-intention tasks and open-ended proactive assistance demonstrate consistent improvements in proactive task performance over representative memory approaches across multiple LLM backbones, while limiting unnecessary interventions.

</details>


### 110. Cognitive Bias Signatures in Search-Equipped LLM Agents: A Stage-Resolved Analysis

- **Authors:** Yanru Xiao, Yingwei Yu
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05720v1](http://arxiv.org/abs/2611.05720v1)
- **PDF:** [https://arxiv.org/pdf/2611.05720v1](https://arxiv.org/pdf/2611.05720v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Search can help LLM agents correct mistakes, but their starting conditions may shape which evidence they find and use. Drawing on cognitive-bias paradigms, we develop a controlled search harness to examine result order, records of prior work, and initial hypotheses while holding each question and document collection fixed. Matched controls distinguish order effects from differences in document composition and the effects of failed work from context length. Across 10 models and 1,000 synthetic search worlds, we track queries, retrieved documents, document openings, and final answers. Our comparisons suggest that final answers are more sensitive to initial evidence order during active search than when all evidence is supplied in full. Dead-end histories can reduce strategy switching relative to matched neutral histories, indicating an effect beyond context length. Under wrong hypotheses, stage measurements distinguish reduced retrieval or opening from errors that persist after counter-evidence is opened. Exploratory interventions show that opening counter-evidence more often can coincide with lower accuracy, while accuracy can improve with little change in opening.

</details>


### 111. Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning

- **Authors:** Tianming Sha
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.06956v1](http://arxiv.org/abs/2611.06956v1)
- **PDF:** [https://arxiv.org/pdf/2611.06956v1](https://arxiv.org/pdf/2611.06956v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems explore in parallel by spawning sub-agents with isolated context windows, whereas single-agent systems append every search and verification step into one growing trajectory. However, existing multi-agent frameworks duplicate prefix KV caches across branches, exchange findings by re-prefilling text summaries, and flatten or drop cross-branch dependencies during reinforcement learning (RL).
  We introduce Octopus, a single-model multi-agent RL framework in which all threads share one backbone and coordinate over a GPU-resident directed acyclic graph (DAG) of KV states through five primitives (fork, read_thread, wait_threads, rewind, commit). Octopus combines three co-designed mechanisms: (1) Zero-Copy Radix Forking, which spawns branches as $\mathcal{O}(1)$ cursor views over shared physical KV pages; (2) Attention-Only KV Mounting, which mounts a sibling thread's terminal KV blocks directly into full-attention layers while bypassing linear-recurrent states (Gated DeltaNet / Mamba-2), cutting off-task hijacking by $21\times$ ($57.9\% \to 2.7\%$) while retaining $92.2\%$ of full-text mutual information at zero extra KV allocation; and (3) a Packed DAG-GRPO Trainer, which packs all episode branches into one block-sparse attention pass and assigns counterfactual branch credit via leave-one-branch-out marginal rewards.
  Trained end-to-end with GRPO on Qwen3.5-4B over a sparse BM25 corpus, Octopus reaches $49.6\%$ accuracy on BrowseComp-Plus ($+17.5$ points over single-agent GRPO at 143K context and $+12.5$ points over text-summary multi-agent RL) and $51.2\%$ on OpenResearcher, outperforming dense-retrieval agents up to $250\times$ larger while increasing training throughput $3.3\times$ and cutting peak KV memory $2.8\times$.

</details>


### 112. Agents, Think Only When it Helps

- **Authors:** Min-Seon Kim, Seungdong Yoa, Sanghyu Yoon, Ye Seul Sim, Suhee Yoon, Dongmin Kim, Jung-Eun Kim
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05709v1](http://arxiv.org/abs/2611.05709v1)
- **PDF:** [https://arxiv.org/pdf/2611.05709v1](https://arxiv.org/pdf/2611.05709v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agent distillation transfers agentic capabilities to student models by training on complete teacher trajectories that typically interleave thoughts and actions. We question how critical thought supervision is for agents' ultimate action performance. To answer this, we disentangle their impacts by independently perturbing teacher thoughts and actions during distillation. On widely adopted agent benchmarks across model scales, altering or discarding thoughts has little effect on student performance. We find, however, that thought supervision becomes important when information about the thought is not disclosed in the corresponding action during training. By identifying such discrepant cases, our findings challenge the common practice of distilling entire teacher trajectories for LLM agents, and offer a new insight that thought supervision can be a discernible choice for efficiency depending on whether the information of thought is disclosed in the action.

</details>


### 113. How Do Artificial Agents Make Decisions in Light of Visual Data?

- **Authors:** Keyty Loza, Shayan Monadjemi
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05671v1](http://arxiv.org/abs/2611.05671v1)
- **PDF:** [https://arxiv.org/pdf/2611.05671v1](https://arxiv.org/pdf/2611.05671v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Vision-language models (VLMs) have demonstrated significant advances in reasoning with visual data, which is particularly important given that much of human knowledge is encoded visually in scientific articles and other sources. However, a gap remains in understanding how artificial agents, powered by VLMs, perceive and navigate decision-making under uncertainty in the presence of visual data. This study explores this gap by evaluating and analyzing autonomous decision-making processes. Building upon prior work in visualization literacy and decision theory, we conducted two complementary studies: one examining how agents perceive and quantify uncertainty encoded in visualizations, and another investigating how artificial agents make decisions based on visual data in the form of images. We analyzed perception accuracy and decision performance across models and visualization types. Our results show that GPT-4o demonstrates the highest accuracy in perceiving uncertainty in pie and bar charts among the tested models. For decision-making, autonomous agents showed the best alignment with rational decision theory when uncertainty was represented through circle charts, icon arrays, or text.

</details>


### 114. Route to Remember: Adaptive Memory Selection for LLM Agents

- **Authors:** Zeyu Fang, Jun Yin, Yongsheng Mei, Xu Han, Chaitali Joshi, Zhongkai Sun, Jie Hao, Bin Guo, Chengyuan Ma, Benjamin Z. Yao, Chenlei Guo
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05636v1](http://arxiv.org/abs/2611.05636v1)
- **PDF:** [https://arxiv.org/pdf/2611.05636v1](https://arxiv.org/pdf/2611.05636v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The memory of production agents is increasingly becoming a bottleneck and is built almost exclusively from text: key points are extracted from out-of-limit context and retrieved into context at query time. Therefore, every new query incurs an additional cost that grows with the accumulated history. Weight memory is a complementary alternative that internalizes knowledge into model parameters and answers with no context at all, and has recently proven effective in self-evolving agents for internalizing skills and behaviors. However, its application in episodic and semantic memory, such as user-specific facts, remains comparatively unexplored, and a gap remains between earlier attempts at weight memory and text-based systems regarding recall performance. We study how to make weight memory competitive as a long-term factual store by applying on-policy self-distillation (OPSD). It trains a context-free student from a teacher, which is the same model conditioned on the user's memory, together with a verify-then-regenerate router that lets weight and text memory each cover the queries they handle best. On the HaluMem benchmark, OPSD matches or surpasses strong text-memory baselines, including full-context prompting and retrieval systems, while reading fewer tokens per query. We further conduct an extensive study that characterizes the behavior of weight memory and analyzes how different training recipes affect its performance. As agent harnesses move toward persistent, multi-session deployments, these results position weight memory as a practical, low-cost component of agent memory and provide insights into feasible training and evaluation protocols for combining it with retrieval.

</details>


### 115. Assurance-Conditioned Continuous Authorization for Autonomous AI Agents

- **Authors:** Mehdi Shajari
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05632v1](http://arxiv.org/abs/2611.05632v1)
- **PDF:** [https://arxiv.org/pdf/2611.05632v1](https://arxiv.org/pdf/2611.05632v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous software agents can act through tools, delegate work, and change their models or execution environments while earlier authorizations remain in flight. We present Assurance-Conditioned Continuous Authorization (ACCA), an approach designed to be harness-independent, for maintaining operational authority according to currently justified assurance. It distinguishes evidence validity from contextual applicability, derives assurance claims from eligible evidence, and resolves a multidimensional effective-authority envelope within a principal-declared ceiling and applicable policy. A typed dependency graph supports selective re-evaluation of authorization-relevant changes. An authority epoch changes when effective authority changes; a distinct optional authorization-basis version supports revalidation of action-specific authorization conditions. Protected effect-time enforcement can reject stale actions before a consequential resource change, subject to the available commit mechanism. A compositional Domain Governance Profile expresses domain-specific semantics without granting authority. Controlled scenario tests implemented as a regression suite using a trading profile exercise default-deny rules, evidence-conditioned contraction and recovery, policy divergence, selective non-response, and stale-action rejection at a local gateway before the simulated-broker boundary. The study establishes implementation-level evidence in one domain, not a cross-domain guarantee of harmful-behavior prevention.

</details>


### 116. Anduin: A sybil-resistant agentic marketplace reputation system

- **Authors:** Reza Ramji, Preston Vander Vos, Ziming Zeng, Duc V. Le
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05586v1](http://arxiv.org/abs/2611.05586v1)
- **PDF:** [https://arxiv.org/pdf/2611.05586v1](https://arxiv.org/pdf/2611.05586v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As autonomous AI agents enter permissionless onchain markets, selecting new service providers remains a core challenge. Existing reputation systems depend on scarce resources like human curation, identity credentials, or voluntary reviews, while naive volume rankings are vulnerable to Sybil attacks.
  We evaluate whether existing onchain payment histories can yield provider ratings that are resilient against Sybil attacks. Using a 157-day dataset comprising 66M agentic transactions worth $6.1M across 16 blockchains, we model payment flows as a bipartite graph between buyers and providers. A provider's rating is derived from graph paths linked to a buyer's existing trusted network. We propose three Sybil-resistant rating algorithms: a max-flow rating and two relaxed algorithms optimized for stronger rating performance.
  Evaluating these algorithms against simulated adversaries across 813 buyers, we show that rating manipulation costs 20% of those buyers' total spend and is around 23x harder to manipulate than the standard similarity rule (collaborative filtering).

</details>


### 117. VirtualTrialHarness: Coordinating Agentic Operationalization of Virtual Trial Protocols Across Complex Clinical Schemas

- **Authors:** Pengze Li, Jingna Feng, Yue Yu, Yining Wu, Xinyue Hu, Jie Lin, Avanti Bhandarkar, Cui Tao
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05551v1](http://arxiv.org/abs/2611.05551v1)
- **PDF:** [https://arxiv.org/pdf/2611.05551v1](https://arxiv.org/pdf/2611.05551v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Virtual trials use routinely collected clinical data to evaluate treatment strategies, but translating a study protocol into an executable analysis requires determining how clinical concepts and study requirements should be represented in the available data and applied consistently across the workflow. These decisions depend on local data representations and operational conventions and can involve source selection, patient and encounter identity, linkage, and temporal interpretation. Here we introduce VirtualTrialHarness (VTHarness), an agent framework that coordinates virtual-trial operationalization by selecting reusable procedural skills for each workflow stage and uses explicit contracts to maintain consistent study decisions across stages. We also introduce VTBenchmark for evaluating source selection and cohort construction. Across three complex synthetic environments, VTHarness successfully produced all required cohort outputs matching the references in 95.1% of workflows after requirement clarification, compared with 60.4% using retrieval from the same procedural corpus. Procedural skills improved source recovery across three language models and increased source overlap with analyst code in 13 Mayo Clinic cases. Site-specific adaptation enabled reference-matched cohort execution across eight MIMIC-IV tasks. Within the Mayo Clinic Virtual Trials Program, the framework supported investigator review of cohort construction and endpoint analysis. These findings support coordinating procedural guidance with workflow decisions to improve virtual-trial implementation across complex clinical schemas.

</details>


### 118. Iterated creation, grading, and revision of data science projects by language models

- **Authors:** Rohan Alexander
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05548v1](http://arxiv.org/abs/2611.05548v1)
- **PDF:** [https://arxiv.org/pdf/2611.05548v1](https://arxiv.org/pdf/2611.05548v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

We evaluate the extent to which agentic AI models can complete an end-to-end data science project, and how this improves with feedback. A 'writer' model with specific tools creates a complete data science project including downloading, cleaning, and analyzing a dataset, and writing a short paper about it. The project is executed and a 'grader' model evaluates it. The writer can then revise its submission, and this repeats for a total of three rounds. We consider seven models from five developers: Anthropic, OpenAI, Google, DeepSeek, and Z.AI. Each model is both a writer and a grader, so there are 49 writer-grader pairs and we run each pair three times. Of the 147 initial submissions, 107 run and render, and the average score increases from 59 per cent to 76 per cent after the final round of feedback. By writer the extent of the increase ranges from 3 percentage points for Anthropic's Opus 5.5 to 46 percentage points for Anthropic's Haiku 4.5, and by grader it ranges from 13 percentage points for Google's Gemini 3.8 Flash to 32 percentage points for Anthropic's Haiku 4.5. When a model grades its own writing the score tends to be about 9 percentage points higher than the average of what the other models give it. About half of the difference that we see from round to round is within the grader's own noise. Feedback generally results in the highest marks, but even just having the chance to revise, or having the additional budget, in terms of time or tool calls, without any feedback, results in considerable increases for some of the models but not for others. We find that how much such a loop helps depends on which model plays which role, but weaker models generally do not improve stronger models.

</details>


### 119. MA-SafeDiffuser: Safe Multi-Agent Planning with Diffusion Probabilistic Models

- **Authors:** Kiran Ravish, Ankita Kushwaha,  Preeti, Pawan Kumar
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05524v1](http://arxiv.org/abs/2611.05524v1)
- **PDF:** [https://arxiv.org/pdf/2611.05524v1](https://arxiv.org/pdf/2611.05524v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We propose MA-SafeDiffuser, a multi-agent extension of SafeDiffuser that equips diffusion-based trajectory planners with finite-time diffusion invariance guarantees for joint-agent safety specifications. Building on the single-agent construction that embeds control barrier function (CBF) constraints into reverse-diffusion updates, we: (i) formalize joint safe sets as intersections of per-agent and pairwise barrier sets; (ii) derive centralized and decentralized (communication-aware) constrained denoising procedures with provable invariance under mild assumptions; (iii) address local-trap and deadlock phenomena via time-varying specifications and liveness CBFs; and (iv) develop a lightweight benchmarking suite including a multi-agent Maze2D domain. Empirically, MA-SafeDiffuser reduces violation counts relative to unconstrained diffusion baselines, while retaining planning quality. We provide algorithms, proofs, and reference implementations.

</details>


### 120. SlackBench: Benchmarking Agents on Collaborative Projects Grounded in Real Code Repositories

- **Authors:** Mingxuan Li, Huanzhi Mao, Ruitao Zheng, Jarod Stanbury James, Yunze Li, Natanya Anderson, Joseph E. Gonzalez, Alex Dimakis
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05512v1](http://arxiv.org/abs/2611.05512v1)
- **PDF:** [https://arxiv.org/pdf/2611.05512v1](https://arxiv.org/pdf/2611.05512v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI Agents are becoming digital coworkers that can browse the web, write code, run experiments, and assist humans over extended horizons. Yet existing benchmarks fall short of real knowledge work: many rely on synthetic data or isolated tasks, missing the complex, multi-party dynamics of collaborative projects, where critical information is scattered across conversations, code, and evolving decisions. Even simple workplace questions may require locating relevant channels and direct messages, recovering context from long discussions, inspecting repository state, reconciling stale or conflicting evidence, and synthesizing across sources.
  We introduce SlackBench, a benchmark for evaluating agents on realistic research and engineering workflows that require joint reasoning over workplace communication and evolving repository state. Grounded in privacy-preserving reenactments of real academic research projects, SlackBench provides reproducible environments with realistic multi-party dialogue, evolving decisions, and corresponding code changes grounded in GitHub repositories and Google Docs. It contains 140 queries spanning heterogeneous-source agentic search, abstention on unanswerable or false-premise questions, goal-directed summarization, and circumstance inference over long conversations. These tasks are not reducible to static corpus question answering: agents must determine which conversations matter, traverse threads, inspect repository state, and synthesize evidence across communication and code artifacts. Across 33 frontier models and agent harnesses, the best system scores around 80% and most agents score below 66%, highlighting substantial headroom for improvement. SlackBench thus provides an extensible framework for evaluating agents in collaborative work environments. The SlackBench dataset is available at https://huggingface.co/datasets/HuanzhiMao/SlackBench .

</details>


### 121. From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence

- **Authors:** Hao Fei
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05376v1](http://arxiv.org/abs/2611.05376v1)
- **PDF:** [https://arxiv.org/pdf/2611.05376v1](https://arxiv.org/pdf/2611.05376v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

For a decade, progress in artificial intelligence has been measured by how much a machine can do on its own. Large foundation models now write code and run multistep tasks, and personal agents act on a person's behalf. Yet people still forget what they once knew, miss what they are not looking at, fail to find the right words, and face hard choices without the benefit of their own history, because the machine that could help stands outside the situation. As AI moves into the physical world, attention has settled on one kind of intelligent individual, the embodied robot; we argue that the era of Physical AI holds a second kind of equal importance, the person augmented by AI. Alongside artificial general intelligence, which asks how intelligent a machine can be, stands AI-augmented human intelligence (AHI), which asks how much intelligence a machine can enable in a particular person. Realizing it calls for a new kind of system, a cognitive symbiont: a lifelong, embedded, real-time, private, low-friction, and proactive companion that senses what the person senses through external devices, keeps their context across years, models their situation and their mind, takes part in their thinking at the right moment, carries out everyday tasks with their context, and keeps learning the person as both change. We give the paradigm a conceptual core, the cognitive gap between what a person could bring to a situation and what they can hold in working memory, and organize its design space as a symbiosis loop of sensing, keeping, understanding, living alongside, acting for and thinking with the person, and growing, enclosed by a personal runtime and by trust. Because a symbiont changes what a person can do in front of others, it also raises risks of a new kind, from covert assistance in examinations to pressure on everyone to adopt it, and we treat their governance as part of the paradigm.

</details>


### 122. PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data

- **Authors:** Kewei Zhang, Juncheng Ma, Guodong Lv, Duomin Wang, Feixiang Ruan, Ruiyang Si, Chuanrui Zhang, Yuxuan Chen, Hao Chen, Yichen Liu, Yintianrun Zhang, Yufan Deng, Enze Xie, Daquan Zhou
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05320v1](http://arxiv.org/abs/2611.05320v1)
- **PDF:** [https://arxiv.org/pdf/2611.05320v1](https://arxiv.org/pdf/2611.05320v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch. We ask whether a coding agent can take over the teleoperator's job. In our DataFarm, the agent receives a data request and one calibration episode of the robot in the target scene and rebuilds the task in simulation: it writes the scene, an expert controller, and a success judge. The simulator supplies exact actions, and a video model conditioned on real images renders each rollout as photographic video, generating all camera views together consistently. The output is real-ready data: synchronized camera views labelled with the robot's actions, on which a policy can be trained directly and deployed on the real robot. Independent judges certify the expert and every rendered episode before admission. On five real-robot tasks, policies trained only on farm data match policies trained on as many teleoperated episodes (93 vs. 84 successes in 100 trials), and under an unseen tablecloth and coloured light they keep 87 successes where the teleoperation-trained policies fall to 46. Adapting a task is fully automatic and costs \$21 of API usage on average, paid once per task, plus \$5 for a render contract; every further episode costs \$0.80 on average for simulation, rendering, and review, with no robot or operator. One hour of three-view data for a task costs \$107 on average, these costs included, slightly below a quote of \$117 for teleoperation in China and below \$290 in labour alone in North America.

</details>


### 123. JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework for Long-Horizon Web Tasks

- **Authors:** Shanka Subhra Mondal, Jiayun Wang
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05263v1](http://arxiv.org/abs/2611.05263v1)
- **PDF:** [https://arxiv.org/pdf/2611.05263v1](https://arxiv.org/pdf/2611.05263v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal web agents have shown promising capabilities for interacting with websites through graphical user interfaces (GUIs), yet realistic web tasks often require long-horizon, multi-step planning that remains challenging for monolithic policies. Such agents must jointly infer high-level plans, navigate through intermediate states, track progress over extended interaction histories, and execute visually grounded actions. Although prior work has explored modular multi-agent systems with a separate planner, the planner is typically not updated jointly with the actor. We investigate whether explicitly separating and jointly training planning and execution provides a stronger inductive bias for long-horizon web navigation. We introduce JHiMA-WebRL, a joint hierarchical multi-agent reinforcement learning framework for web agents that couples a task decomposer with an actor. To train the decomposer, we use a strong teacher model to construct structured subtask supervision from multimodal GUI trajectories, and use these annotations to fine-tune both the decomposer and the subtask-conditioned actor. We then extend Group Relative Policy Optimization (GRPO) to jointly optimize the decomposer and actor in the interactive WebArena environment through hierarchical rollout grouping and role-specific advantages. On WebArena-Lite-v2, JHiMA-WebRL-14B, consisting of a 7B actor and a 7B decomposer, achieves an average success rate of 37.2%, compared with 24% for a ScaleCUA-32B agent that we fine-tune with RL on the same training tasks and evaluate under the same protocol. Ablations show that jointly updating the decomposer during RL outperforms updating the actor alone. These results suggest that jointly learned role factorization with smaller models can be a competitive alternative to scaling monolithic agents for long-horizon web tasks.

</details>


### 124. AgentAM: An AI Agent for Spatter- and Defect-Aware Process Optimization in Laser Powder Bed Fusion

- **Authors:** Olabode T. Ajenifujah, Amir Barati Farimani
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05171v1](http://arxiv.org/abs/2611.05171v1)
- **PDF:** [https://arxiv.org/pdf/2611.05171v1](https://arxiv.org/pdf/2611.05171v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Predictive models for laser powder bed fusion (LPBF) are rarely used on the shop floor because querying them requires programming and model-specific knowledge. We present AgentAM, a large language model (LLM) agent that gives process engineers natural-language access to CFD-trained surrogates of spatter and melt pool geometry for SS316L through the Model Context Protocol (MCP). Polynomial surrogates trained on 279 single-track simulations predict melt pool dimensions ($R^2 \geq 0.95$) and spatter volume ($R^2 = 0.83$ on test data) at any power-velocity point in the trained range, and geometric criteria assign each point a geometry-derived defect regime (keyhole, lack of fusion, balling or stable) that matches the regime obtained from the simulated geometry in 93.4% of tracks under cross-validation. The agent selects and parameterizes tools for prediction, process-window scans and constrained optimization. Minimum-spatter optima often sat within 10 $μ$m of the lack-of-fusion boundary; a margin-aware optimizer moved them away from all thresholds and raised the estimated probability of remaining classified Good from 0.94 to 1.00 under an assumed 2% process drift, and from 0.72 to 0.91 when jointly sampled cross-validated geometry residuals were added. About 40-50 well-spread simulations sufficed to reproduce the defect map. To evaluate the agent layer, we introduce a 145-prompt benchmark scored against direct tool calls, plus eight prompts (40 runs) on margin-aware requests. Over the 725 runs of the main benchmark the agent passed the intended inputs in 98.5% of parsing prompts, reported the scored spatter values and defect classes faithfully and met every stated constraint in the 65 feasible optimization runs, within a median 1.0% of the brute-force optimum.

</details>


### 125. ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents

- **Authors:** Guanting Dong, Zhichao Sun, Xinyu Yang, Rui Wang, Xin Deng, Jiajie Jin, Zhixiong Yang, Junhao Huang, Han Han, Mingyu Ma, Xiaotao Wang, Yuyang Hu, Xiaoshuai Song, Xiaoxi Li, Jiejun Tan, Zhecan Wang, Shihan Dou, Honglin Guo, Zhiheng Xi, Tao Gui, Tao Ji, Qi Zhang, Yutao Zhu, Ji-Rong Wen, Zhicheng Dou
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05036v1](http://arxiv.org/abs/2611.05036v1)
- **PDF:** [https://arxiv.org/pdf/2611.05036v1](https://arxiv.org/pdf/2611.05036v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are deployed as long-horizon agents that compose diverse tools across MCP services into executable workflows. Existing MCP environment-scaling methods are data-centric: they first synthesize a database and scenario, then derive tools and tasks from them. As a result, tool interfaces may not match real ones, tool compositions are not grounded in execution, and tasks rarely span more than one environment. We propose ToolSpace, a tool-centric framework that reverses this order. ToolSpace mines data, state, and retry dependencies from adjacent calls in execution traces of real MCP services and open agent corpora, using deterministic rules rather than LLM judgment, and clusters the resulting weighted tool-composition graph into environments. Databases are synthesized only for state-mutating environments, while query and stateless tools replay recorded returns. ToolSpace then performs state-aware random walks with rollback and decompiles each chain into a natural-language task with assertion-based checks, keeping only samples that replay successfully from the initial state. Applied to AutomationBench and tau3-Bench Banking, the pipeline produces harder Pro versions on which 7 frontier models drop by up to 38.2 points. Across seven long-horizon tool-use benchmarks, ToolSpace raises Qwen3.6-35B-A3B from 23.0 to 41.0 average score (43.2 with RL) and GLM-5.2 from 44.6 to 56.6, on par with Claude Opus 5. Ablations show that execution-witnessed edges clearly outperform LLM-judged ones, and performance keeps improving with data and environment scale.

</details>


### 126. Haptic Shared Control for Multi-Robot Systems

- **Authors:** Maxime Bernard
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.05027v1](http://arxiv.org/abs/2611.05027v1)
- **PDF:** [https://arxiv.org/pdf/2611.05027v1](https://arxiv.org/pdf/2611.05027v1)
- **Categories:** cs.RO, cs.HC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems offer significant advantages in terms of flexibility and redundancy, enabling the efficient distribution of complex tasks among multiple robots. However, their deployment requires advanced control strategies to ensure optimal cooperation between autonomous agents and human operators. We propose a modification of the global connectivity maintenance algorithm to incorporate measurements taken in agent's local frame, using sensors with limited fields of view. This algorithm, responsible for the autonomous behavior of the multi-robot system, is combined with different adaptive supervision strategies, allowing the user to exert control at varying scales over the entire group. (i) Single Agent Control (S): The operator directly controls a single robot, (ii) Pinning Control (P): The operator imposes constraints on multiple robots to influence the group, (iii) Centroid Control (C): The operator acts on the system's center of mass to steer the entire fleet. In conjunction with the connectivity maintenance algorithm, these methods ensure compliance with inter-agent constraints while providing haptic feedback to the user regarding the system's connectivity state. The effectiveness of these approaches was evaluated through a user study, comparing performance with and without haptic feedback across multiple scenarios tailored to the different control modes.

</details>


### 127. GeoFaham: Domain-Specialized Multi-Agent Geospatial Analytics for Disaster Response

- **Authors:** Muhammad Sohail Danish, Gilles Q. Hacheme, Akram Zaytar, Satej S. Soman, Inbal Becker-Reshef, Juan Lavista Ferres, Salman Khan, Girmaw Abebe Tadesse
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04977v1](http://arxiv.org/abs/2611.04977v1)
- **PDF:** [https://arxiv.org/pdf/2611.04977v1](https://arxiv.org/pdf/2611.04977v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Real-world geospatial decision support requires more than single-step retrieval or code generation. Disaster-response questions often involve multi-source workflows that combine spatial databases, map-derived features, satellite imagery, raster products, and reusable geospatial artifacts, where correctness depends on preserving spatial scope, temporal context, and intermediate execution state. While large language models and coding agents offer a promising interface for such workflows, they struggle with geospatial-specific failure modes, including handling large artifacts, selecting the wrong evidence source, losing spatial or temporal metadata, and applying invalid geometric operations. We introduce GeoFaham, a domain-specialized multi-agent system for geospatial disaster analytics. GeoFaham decomposes workflows into specialist agents for vector operations, map feature retrieval, imagery discovery, and raster analysis, coordinated by an Orchestrator with a dual-ledger control loop for dependency-aware planning, progress tracking, validation, and replanning. To support artifact-centric collaboration, GeoFaham uses a Response Store that persists full geospatial outputs and typed metadata outside the LLM context window while agents exchange compact identifiers and summaries. We also introduce GeoFaham-Bench, a 40-task benchmark grounded in 17 real-world disaster records, designed to evaluate multi-step geospatial reasoning, cross-source integration, raster-vector computation, artifact generation, and recovery under non-rigid ground truth. We evaluate GeoFaham on GeoFaham-Bench against strong general-purpose coding-agent baselines, including Codex, Claude Code, and OpenCode. GeoFaham achieves the best overall performance, scoring 0.940 versus the next-best 0.879, while using 7.5 times fewer tokens. Our code and benchmark are publicly available at https://github.com/microsoft/GeoFaham.

</details>


### 128. Local Visibility Roadmaps in Continous Multi-agent Path Finding

- **Authors:** Kristýna Janovská, Pavel Surynek
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04944v1](http://arxiv.org/abs/2611.04944v1)
- **PDF:** [https://arxiv.org/pdf/2611.04944v1](https://arxiv.org/pdf/2611.04944v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We address the problem of smooth continuous multi-agent path finding (SC-MAPF), where agents move in a continuous environment along smooth curves in continuous time. The paths for individual agents are searched in local visibility roadmaps that consider obstacles and other agents. A new algorithm is proposed in this work, which combines the previous algorithm CE-CBS for high-level search with any-angle path finding for local single-agent planning, where agents are to avoid obstacles, both static and other agents. The new algorithm is tested and compared to CE-CBS, the algorithm building individual paths using RRT$^*$, and SMT-CCBS algorithm, an algorithm for MAPF$_R$. Experimental results show various advantages of the new algorithm over CE-CBS and SMT-CCBS in comparable settings.

</details>


### 129. Where Is the Truth When AI Agents Disagree? Dependence-Aware Belief Propagation for Unsupervised Truth Discovery (Extended Version)

- **Authors:** Laure Berti-Equille
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04805v1](http://arxiv.org/abs/2611.04805v1)
- **PDF:** [https://arxiv.org/pdf/2611.04805v1](https://arxiv.org/pdf/2611.04805v1)
- **Categories:** cs.AI, cs.CL, cs.DB, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents often give conflicting answers to the same question, and many deployed agents are variants of one base model, so their errors are correlated. We study truth discovery among such agents: inferring the true answer and each agent's reliability without labels. Classical truth-discovery and crowdsourcing estimators reward an agreeing bloc and can fall below majority vote. We propose BP-TD, which adds per-agent decorrelation weights to mean-field variational inference on a one-coin Dawid-Skene model, so that agents sharing a base model count together as about one vote. Its first iteration is exactly a weighted vote; later iterations estimate agent reliability. With 13 local agents on MMLU, BP-TD beats majority vote without any labels (0.716 vs. 0.624 on 160 questions; 0.707 vs. 0.674 on 10,000) and ranks agents by their true accuracy, which classical estimators invert. The gain depends on the pool: over 2,852 sub-pools of four benchmarks, decorrelation helps when the largest correlated bloc is weaker than the other agents and hurts when it is the strongest, and we found no label-free statistic that tells the two cases apart. Labels change the picture quickly: with 20 labelled questions, selecting the single best agent is more accurate than every aggregator we tested on MMLU, ARC and TruthfulQA.

</details>


### 130. Cooperative Multi-Agent Reinforcement Learning with Submodular Trajectory Rewards

- **Authors:** Yasaman Zolfimoselo, Nikolas Geroliminis, Maryam Kamgarpour
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04774v1](http://arxiv.org/abs/2611.04774v1)
- **PDF:** [https://arxiv.org/pdf/2611.04774v1](https://arxiv.org/pdf/2611.04774v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study cooperative multi-agent reinforcement learning with decoupled dynamics and a monotone submodular reward function over joint trajectories. Due to the non-additive reward, an optimal policy may depend on the history of all agents. This dependence makes exact optimization exponential in the horizon and the number of agents. To overcome this challenge while retaining theoretical guarantees, we introduce pre-window curvature $c_m$, which quantifies how states visited more than $m$ steps earlier reduce current marginal gains. Using this curvature to control the error from restricting the policy of each agent to depend only on its last $m+1$ states, we propose a greedy algorithm that exploits the decoupled dynamics to optimize local policies sequentially. For fixed $m$, the algorithm achieves a $\frac{1-c_m}{2-c_m}$ approximation guarantee up to estimation error, and its computation time is polynomial in the number of agents and the horizon. We recover the known $1/2$-factor approximation for time-additive rewards and obtain an approximation factor no smaller than the known total-curvature bound for a single agent. We formulate multi-agent traffic monitoring as an example of this framework and evaluate our algorithm on it.

</details>


### 131. MIMIC-Note-Extract: A Large-Scale Structured Dataset Extracted from MIMIC-IV-Note Discharge Summaries

- **Authors:** Kristian Schwethelm, Jonas Kuntzer, Conrad Ketzer, Eva Wende, Moritz Schlager, Daniel Rueckert, Georgios Kaissis, Friederike Jungmann, Paul Hager
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04685v1](http://arxiv.org/abs/2611.04685v1)
- **PDF:** [https://arxiv.org/pdf/2611.04685v1](https://arxiv.org/pdf/2611.04685v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

MIMIC is one of the most widely used public hospital datasets for machine learning on electronic health records, yet clinically important information, such as past medical history, allergies, and diagnostic findings, remains confined to free-text discharge summaries. Studies requiring this information must therefore build their own extraction pipelines, duplicating substantial effort across projects. We release MIMIC-Note-Extract (MNE), a large-scale dataset that uses a hybrid extraction pipeline combining deterministic parsing with schema-guided large language model generation to transform 16 sections from 300,720 discharge summaries into structured tables. MNE adds information that has no structured MIMIC counterpart and enriches related tables with broader coverage and greater clinical detail, including 10 times more patient-history entries and medication histories for more than twice as many admissions. Validation by medical doctors confirms extraction accuracy above 92% across sections. Using MNE, we construct a clinical decision-making benchmark for LLM agents, demonstrating how reusable structured representations of clinical narratives reduce data curation effort.

</details>


### 132. Can Network Models of Science Do Without Pluralist Agents?

- **Authors:** Jonas Hallgren, David Hyland, Mahault Albarracin
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04590v1](http://arxiv.org/abs/2611.04590v1)
- **PDF:** [https://arxiv.org/pdf/2611.04590v1](https://arxiv.org/pdf/2611.04590v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Science is a process of useful models being proven wrong time and again, but despite its many flaws, it somehow works. Why is this? Paul Feyerabend argued that it works because people dare to hold and defend incompatible rival theories against the accepted one, since a theory's failures often lead to its abandonment in the presence of a more accurate or simpler alternative. He called this view theoretical pluralism. We introduce a theoretical and experimental model in which this can be examined. It compares communities of pluralist agents, which can hold rival theories side by side and maintain beliefs within and between those theories, with communities of monist agents, which can only incorporate what they hear or observe into a single model of their own. In a multi-agent variational inference setting, our experimental demonstrations illustrate how communities with rival theories can go through periods of uncertainty followed by a shift in the theories they hold true, how the information that is communicated between communities affects beliefs when those communities make different observations about the world, and how sharing support for theories and sharing beliefs within them contribute differently to collective belief dynamics.

</details>


### 133. Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems

- **Authors:** Chandler Smith, Qi Guo, Cecilia Elena Tilli, Sophia Hatz, David Demitri Africa, Patricia Paskov, Christian Schroeder de Witt, Philip Torr, Lewis Hammond
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04556v1](http://arxiv.org/abs/2611.04556v1)
- **PDF:** [https://arxiv.org/pdf/2611.04556v1](https://arxiv.org/pdf/2611.04556v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The deployment of AI agents in multi-agent settings enables inter-agent influence, whereby agents can strategically steer each other's behaviour towards an intended outcome. Such capabilities pose novel risks, as malicious agents could direct others towards harmful actions. In this work we investigate three such capabilities - persuasion, deception, and coercion - across five realistic evaluation environments and a variety of agents instantiated with frontier language models. We observed significant inter-agent influence capabilities; in oversight environments, all tested models shifted overseer decisions from rejection to approval through persuasion, deception, or coercion. We also observed successful influence in non-hierarchical 'peer-to-peer' settings through redirection of a peer's safety research trajectory. As multi-agent deployments become increasingly commonplace, these results point to a pressing need for work on mitigating the risks from inter-agent influence. Code and data are available at https://github.com/Cooperative-AI-Foundation/inter-agent-influence.

</details>


### 134. Signals: Continuous Diagnostics of AI Agents

- **Authors:** Amey Rambatla, Vatsal Goel, Sagar Gaur, Siddhant Loya, Anurag Mishra, Asif Mohammad
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04507v2](http://arxiv.org/abs/2611.04507v2)
- **PDF:** [https://arxiv.org/pdf/2611.04507v2](https://arxiv.org/pdf/2611.04507v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can make incorrect decisions or waste resources even when their tools and infrastructure work normally. Their nondeterministic behavior makes these problems difficult to reproduce and diagnose. We developed Signals to identify such problems from agentic traces and suggest concrete remediations. We built the method around a taxonomy of 45 problem types across eight families, with definitions and evidence requirements for each type. The method distinguishes realized failures, risk exposures, and inefficiencies, groups related findings into engineering issues called Signals, and assesses their severity from the supporting evidence. Each Signal includes actions a developer can take and checks for evaluating the change. Further executions can add evidence to an existing Signal or reveal a new problem. We evaluated the method on public agent executions and achieved 91.43% F1 when matching Signals to reference issues, about 18 percentage points higher than a one-pass LLM control that used the same model and taxonomy.

</details>


### 135. From Watching to Steering: Enabling Human-Coding Agent Collaboration through Execution Traces

- **Authors:** Xiaoke Yan, Jiaying Lei, Danqing Shi, Zichen Wang, Nan Cao
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04466v1](http://arxiv.org/abs/2611.04466v1)
- **PDF:** [https://arxiv.org/pdf/2611.04466v1](https://arxiv.org/pdf/2611.04466v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in large language models (LLMs) have enabled coding agents to autonomously perform complex software development tasks, yet their long-running execution remains difficult for users to inspect, understand, and steer. We present Vibetrace, an interactive trace visualization and intervention system for agentic programming built upon OpenCode. Vibetrace introduces a human-agent collaboration paradigm of Observe, Understand, Intervene, and Evolve. It (1) visualizes agent workflows as interactive execution traces for inspecting actions, intermediate states, and failures; (2) enables users to fork execution from prior steps and provide targeted corrections without restarting validated progress; and (3) distills traces and human feedback into reusable skills for continual agent evolution. On SWE-bench Verified, distilled skills reduce input tokens by 23.0% and cost by 15.5%, while improving pass rate from 65.0% to 68.0%. User studies further demonstrate improved accuracy and efficiency over conventional log-based interaction.

</details>


### 136. $τ$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation in Agentic Recommender Systems

- **Authors:** Bharath Sivaram Narasimhan, Karthik R. Narasimhan
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04459v1](http://arxiv.org/abs/2611.04459v1)
- **PDF:** [https://arxiv.org/pdf/2611.04459v1](https://arxiv.org/pdf/2611.04459v1)
- **Categories:** cs.IR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

While conversational recommendation systems provide a more natural user interface, they face the challenge of progressively discovering a user's needs before they can recommend an item that satisfies them. To evaluate the ability of AI agents at this elicitation process, we introduce $τ$-Rec-Books, a benchmark that holds each user request fixed while varying only when the user reveals their requirements: all at the start (volunteer), one at the start and the rest when asked (mixed), or some never (hidden). A hidden requirement can be found only by proposing books and inferring it from the user's accept or reject verdicts. We generate 450 tasks over a catalog of 20,000 books from Wikidata, develop a rule-based simulated user to answer the agent, and score recommendations against catalog metadata without an LLM judge. Across four agents and two search interfaces, success rates fall for every agent and interface, on average from 0.975 (volunteer) to 0.756 (mixed) and 0.283 (hidden). Mixed tasks fail mainly because agents do not ask, and when told to ask, every agent reaches at least 0.931. On hidden tasks, most failures come from agents recommending a book they never proposed to the user. When told to propose first, agents only match a simple baseline that proposes popular books, and stay well below one that uses rejection to rule out possible requirements. We release the catalog pipeline, task generator, simulated user, validators, reference agents, and all agent traces at https://github.com/nbharaths/tau-rec/tree/main/data/tracks/books-wikidata-v2.

</details>


### 137. Voluntary Servitude: Weaponized Safety Warning Mechanisms for Controlling AI Agents

- **Authors:** Ilan Zendel, Matan Levy, Stav Cohen, Avi Mendelson, Amit LeVi
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04393v1](http://arxiv.org/abs/2611.04393v1)
- **PDF:** [https://arxiv.org/pdf/2611.04393v1](https://arxiv.org/pdf/2611.04393v1)
- **Categories:** cs.CR, cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly act on information retrieved from public sources they treat as credible, which turns a manipulated recommendation into a transaction, a dependency, or a decision with physical consequences. The security literature models this threat as instruction injection, in which an adversary writes a command into retrieved content and deployed defenses learn to recognize command syntax. We show that an attacker can instead steer an agent through the agent's own harm-avoidance. A single fabricated hazard, written as an ordinary review, leads the agent to disqualify the legitimate options and select the attacker's target by its own reasoning, with no command for a detector to recognize. We call this voluntary servitude. These payloads steer agents about as often as instruction injection (60.4% vs. 66.0%), and deployed injection detectors score them as benign, so behind a filter they are 1.7-4.4x more effective. We measure this at the generation stage across six models and ten consumer-service domains, for three attack families, and show that it transfers to production browser agents, outperforming instruction injection, and to a retrieval pipeline (1.0-57.0% end-to-end success, depending on the retriever). We then show that a corroboration requirement added to the agent's instructions removes roughly 95% of the exposure against a non-adaptive attacker without retraining. With the requirement in place, the agent still reads the planted hazard and no longer acts on it.

</details>


### 138. Distributed Marginal Return: A Communication-Efficient Algorithm for Multi-Agent Weapon Target Assignment

- **Authors:** Kamal Mammadov, Glen Pearce, Helen Krause, Damith C. Ranasinghe
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04370v1](http://arxiv.org/abs/2611.04370v1)
- **PDF:** [https://arxiv.org/pdf/2611.04370v1](https://arxiv.org/pdf/2611.04370v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Weapon-Target Assignment (WTA) problem in distributed multi-agent systems is challenged by limited situational awareness and communication constraints. Existing distributed methods, such as auction-consensus algorithms, typically assume task-value independence, a simplification that fails to capture the coupled effects of multi-weapon assignments. This paper introduces the Distributed Marginal Return (DMR) algorithm, a novel decentralized approach that generalizes auction-consensus frameworks. DMR enables agents to compute bids based on marginal return and uses a consensus protocol to resolve conflicts, allowing multiple non-conflicting proposals to be accepted in parallel for cooperative optimization with minimal communication. A key theoretical contribution is our proof that the marginal returns of non-conflicting bids are additive, a property that ensures global consistency and validates our parallel acceptance mechanism. Extensive simulations demonstrate that DMR significantly outperforms baseline algorithms in both solution quality and communication efficiency, offering a scalable and robust solution for real-world distributed command and control applications.

</details>


### 139. CloakFEM: Agentic FEM Code Generation for Red-Teaming Computational Resource Exhaustion

- **Authors:** Li Zheng, Simin Chen
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04356v1](http://arxiv.org/abs/2611.04356v1)
- **PDF:** [https://arxiv.org/pdf/2611.04356v1](https://arxiv.org/pdf/2611.04356v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Finite element method (FEM) solvers are foundational to scientific and engineering simulation, yet their susceptibility to \emph{efficiency attacks} remains largely unexplored. An adversary can craft syntactically valid and runnable FEM programs that complete successfully while forcing excessive computational work, enabling computational denial-of-service (DoS) attacks. Finding such inputs is challenging because FEM programs occupy a vast, structured space constrained by numerical, geometric, and constitutive requirements. We introduce CloakFEM, a domain-guided LLM-agent framework for automatically generating runnable adversarial FEM programs that amplify solver computation. CloakFEM combines LLM-guided search with an FEM-specific intermediate representation and a deterministic validity gate that enforces runnable constraints. Across three FEM stacks, 17 problem classes, and 1,068 seeds, CloakFEM discovers adversarial inputs that substantially amplify solver work while remaining valid and solvable. In the most extreme case, solver iterations increase from 43 to 247,367, a \(5{,}752.72\times\) amplification. CloakFEM outperforms five generic black-box baselines and retains an advantage over evolutionary search under a controlled bounded action space. Cross-solver analysis further reveals both problem-intrinsic and solver-specific sources of vulnerability. Our results uncover an underexplored efficiency-attack surface in FEM solvers and show that runnable FEM programs can serve as adversarial inputs.

</details>


### 140. When Is Fresh AI Stock Analysis Worth It? Allocating a Limited Research Budget Across Price Updates, Deep Forecast Refreshes, and Editorial Reviews of Top Stock Picks

- **Authors:** Russlan Ramdowar
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04348v2](http://arxiv.org/abs/2611.04348v2)
- **PDF:** [https://arxiv.org/pdf/2611.04348v2](https://arxiv.org/pdf/2611.04348v2)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

When is another AI research run worth more than keeping that money invested? Using 8,120 iPulse AI reports that consumed nearly 100 million output and reasoning tokens on the same 203 stocks across four production batches, we compare repricing old targets (with and without shock safeguards), mechanical growth-path resets and fresh multi-agent reports. Ten matched configurations represent seven investment frameworks.
  The primary economic test selects equal-weight Top 10 USD portfolios from one-year forecasts, net of 10 bps trading costs and a USD 3,000 all-in charge for fresh research on a USD 300,000 account. In two unchanged-model short windows, guarded reuse averages 2.25%, versus 1.66% for SPY and 4.24% for fresh reports. Guarded reuse beats SPY in all three short windows. Extending the first holding window to 176 days reverses the comparison: guarded reuse returns -11.26%, fresh reports +8.55%, and SPY +3.46%, motivating the thesis half-life question.
  Supporting quarter-forecast diagnostics show that mechanically resetting old growth paths closes 98% of the MAE gap to fresh reports, yet Fresh and Reset share only 1-4 Top 10 stocks. Top 30 reverses the unchanged-model comparison in favor of guarded reuse (4.17% versus 1.37%). Concentration tests expose dependence on exceptional winners. Nine editorial editions show substantial between-edition turnover, but each final screen retains its own incoming list.
  Recurring budget scenarios retain initial holdings: monthly costs approach realized short-window refresh value, while weekly budgets require larger additional gains. A matched ranking-continuity extension extracts further value from retained forecasts without eliminating thesis ageing. The architecture separates continuous price monitoring, episodic thesis rebuilding and evidence-based editorial checks.

</details>


### 141. ATC: Agent Trajectory Control for Role-Contract Enforcement in Black-Box Multi-Agent Systems

- **Authors:** Maisha Maliha, Vishal Pramanik, Sumit Kumar Jha
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04321v1](http://arxiv.org/abs/2611.04321v1)
- **PDF:** [https://arxiv.org/pdf/2611.04321v1](https://arxiv.org/pdf/2611.04321v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems assign different responsibilities to different agents: one plans, another retrieves evidence, another verifies, another executes. This division of labor is only meaningful if each agent stays within the functions it is authorized to perform. Over many turns, however, an agent can produce a locally reasonable message that exercises authority belonging to another role: a verifier that begins planning, a retriever that asserts unsupported conclusions, an executor that changes state no one approved. We formalize this as role drift, a turn-level breach of an agent's role contract. We introduce Agent Trajectory Control (ATC), which makes each role's authority explicit as a contract and enforces it at the point where a message would enter the shared conversation. ATC scores a proposed output for out-of-role deviation, leakage into the functions of other roles, impermissible speech acts, and logical contract breaches, then computes a leakage-regularized target that constrains regeneration; the revised message is re-checked before admission. Enforcement acts on the message rather than the generator, so ATC governs agents whose internal representations are unavailable. Across homogeneous and heterogeneous teams, ATC improves task performance and role consistency while lowering role-drift energy relative to strong baselines spanning prompting, memory, workflow control, and activation editing, with the largest gains under explicit role-confusion stress tests and in larger, more diverse teams.

</details>


### 142. Drift No More: Spectral Locking for Long-Horizon Open-Weight Multi-Agent AI

- **Authors:** Vishal Pramanik, Maisha Maliha, Susmit Jha, Sumit Kumar Jha
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04315v1](http://arxiv.org/abs/2611.04315v1)
- **PDF:** [https://arxiv.org/pdf/2611.04315v1](https://arxiv.org/pdf/2611.04315v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon multi-agent systems suffer from three tightly coupled failures: task drift, role drift, and state staleness. We test the hypothesis that these share a common representational cause: agent hidden states move away from the directions encoding the active task, assigned role, and current shared state. A pilot study over 14,832 annotated turns supports this: drifted turns collapse near-uniformly across all three anchor subspaces (pairwise r = 0.72-0.78). Existing methods address these failures separately, operating at the surface-text level or treating control directions independently. We introduce ATLAS (Algebraic Task-role Locking with Adaptive Spectral Memory), a training-free intervention acting on hidden states before a token is generated. ATLAS builds a positive-semidefinite anchor kernel over task, role, and state subspaces and steers hidden states toward their shared high-coherence eigendirections; a low-rank Gram decomposition keeps this tractable. Across long-horizon memory, state maintenance, tool use, least-privilege coordination, and embodied stress tests, ATLAS outperforms prompting, retrieval, memory, and activation-steering baselines. Against A-MEM it improves memory macro-average accuracy by up to 5.7 points and reduces write/read failures by up to 31.7%/24.8%; against MemoryArena-Agent it gains up to 4.8 points. It gains 10.7-12.1 points under perturbation, reaches 93.5% role consistency, and transfers to a 72B backbone (macro-average 61.0 vs. 56.2). Ablating the joint task-role-state span costs 7.2 points against 0.8 for a matched-rank random span, indicating these directions are functionally implicated, not incidental; supplying them by prompt or retrieval recovers 4.3 points less. ATLAS is therefore a representation-level controller for open-weight multi-agent systems, complementary to output-level protocols for black-box agents.

</details>


### 143. OSGR: Observation-Support Graph Reasoning for Earth Observation Question Answering

- **Authors:** Dazhou Yu, Zerong Wang, Riyang Bao, Longxiang Li, Yang Liu, Liang Zhao
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04301v1](http://arxiv.org/abs/2611.04301v1)
- **PDF:** [https://arxiv.org/pdf/2611.04301v1](https://arxiv.org/pdf/2611.04301v1)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Answering geographic queries over Earth observation (EO) archives requires solving a joint retrieval-and-derivation problem under strict spatiotemporal constraints. Existing LLM agents fail to ground observation items or suffer from search-space explosion. We propose OSGR, a two-stage framework that factorizes this search into offline symbolic concept deduction and online Relation-Conditioned Grounding. OSGR leverages an offline Observation-Support Graph to deduce valid target-to-result support paths at the concept level, and applies spatiotemporal compatibility kernels to instantiate grounded observation-item sets. On Earth-Bench and DisasterM3-Reason, OSGR improves GPT-4o accuracy from 49.3\% to 63.7\% while reducing the execution-step ratio from 2.9 to 2.5.

</details>


### 144. When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation

- **Authors:** Qinghua Mao, Xi Lin, Yuxin Qi, Zihao Xu, Jinze Gu, Yuliang Chen
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04289v1](http://arxiv.org/abs/2611.04289v1)
- **PDF:** [https://arxiv.org/pdf/2611.04289v1](https://arxiv.org/pdf/2611.04289v1)
- **Categories:** cs.CR, cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Retrieval-augmented Web applications increasingly employ multi-agent debate (MAD) to aggregate conflicting, noisy, and heterogeneous information, yet deliberation is fundamentally a social process susceptible to interpersonal dynamics. When retrieved Web sources contain latent hazards alongside safe factual content, social biases such as conformity pressure and authority deference can override evidence-grounded safety boundaries. In this work, we investigate whether the social structure of deliberation can paradoxically amplify latent Web safety risks. We introduce SafeConflict-Bias, a controlled counterfactual diagnostic protocol spanning six core Web risk categories, which holds queries and retrieved evidence strictly invariant while isolating conversational majority sway, authority cues, and confidence asymmetry. Empirical evaluation across diverse proprietary and open-source backbones reveals that while isolated models reliably reject unsafe guidance, standard MAD catastrophically capitulates to social pressure---surging unsafe adoption from 0.0\% up to 100.0\% and systematically silencing safe minority evidence. To resolve this systemic fragility without retraining or debate regeneration, we propose RiskTrace-Debias, an inference-time auditing framework uniting evidence-first precommitment, social-metadata masking, and consistency-gated arbitration. RiskTrace-Debias suppresses worst-case unsafe adoption to $\le 2.0\%$ across all architectures without inducing over-refusal, while generating verifiable provenance traces to audit interpersonal manipulation in Web deliberation.

</details>


### 145. DoGNAVY-Exploit: Harnessing Parallel Open-Weight Agents for Stage-Aware Vulnerability Exploitation

- **Authors:** Yuxuan Wang, Dadi Guo, Weijie Guo, Zikai Xu, Chen Lu, Yizhe Zhuang, Peng Huang, Yuejin Xie, Guopeng Lin, Xuangan Xiao, Shipei Qu, Dongrui Liu
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04196v1](http://arxiv.org/abs/2611.04196v1)
- **PDF:** [https://arxiv.org/pdf/2611.04196v1](https://arxiv.org/pdf/2611.04196v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Frontier LLM agents can turn known vulnerabilities into working exploits, but are costly and often access-restricted due to their potential for malicious use. Open-weight models offer a more accessible alternative, but struggle to maintain progress across long exploitation chains. They also often fail to apply relevant security knowledge at the appropriate stage and in the right context to identify and evaluate promising attack directions. To address these limitations, we propose DoGNAVY-Exploit, a multi-agent harness built around two complementary designs: stage-aware decomposition with progressive expert knowledge disclosure, and hierarchical orchestration with parallel exploration. Specifically, DoGNAVY-Exploit uses configurable milestones to recast long-horizon exploitation as short, verifiable capability transitions and provides only the knowledge relevant to each stage. Within each milestone, a hierarchical architecture separates strategic planning from parallel execution: a planner proposes diverse attack routes, executors test them concurrently, and a controller accepts progress only when supported by runtime evidence. A shared structured memory consolidates verified facts, artifacts, replay steps, and failed routes across branches, allowing agents to build on collective progress and carry validated knowledge into subsequent milestones. In controlled benchmark environments, DoGNAVY-Exploit with GLM-5.2 achieves 97.5% Pass@1 on Cybench, and 97.5% zero-day and 100% one-day Pass@1 on CVE-Bench. On ExploitGym, it solves 79 tasks with GLM-5.2 and 157 with GLM-5.3, while the corresponding public Claude Code baselines solve 39 and 130 tasks, respectively. Ablation results further demonstrate that the stage-aware orchestration, expert knowledge, parallel exploration, and memory designs can substantially improve the exploitation capabilities of open-weight agents.

</details>


### 146. Agentic Path Maps: Exposing an Agent's Traversal Through the Garden of Forking Paths

- **Authors:** Madeleine Grunde-McLaughlin, Hafsah Usman, Daniel Mitroshkov, Emily Reif, Nino Migineishvili, Lakshya Chauhan. Kevin Yu, Jeffrey Heer, Daniel S. Weld
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04183v1](http://arxiv.org/abs/2611.04183v1)
- **PDF:** [https://arxiv.org/pdf/2611.04183v1](https://arxiv.org/pdf/2611.04183v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When an AI agent executes an underspecified task, it embeds choices that may contradict unarticulated user context and preferences. However, interrupting the user for clarification on all such decisions is untenable. How might agents communicate impactful, but unexplored, paths to the user after execution? To investigate, we first distill a design space for communicating alternative paths, supporting the generation of new systems and structuring dimensions of future study. We then measure the impact of one vital design space dimension on user comprehension: the number of alternatives displayed. Through a user study (n=48) in the data analysis domain, we find that participants rarely consider alternative paths of their own volition, but AI overreliance reduces when alternative paths are visualized for them. By revealing paths the agent did not take, we demonstrate how users can better interpret results and incorporate personal context.

</details>


### 147. ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends

- **Authors:** Shengjun Kris Dong, Dima Nikiforov, Sahil Modi, Sana Damani, Edward C Lin, Siva Kumar Sastry Hari, Christos Kozyrakis
- **Published:** 2026-11-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04104v1](http://arxiv.org/abs/2611.04104v1)
- **PDF:** [https://arxiv.org/pdf/2611.04104v1](https://arxiv.org/pdf/2611.04104v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Optimizing accelerator code across hardware architectures is difficult. ML compilers search predefined spaces of schedules and micro-kernels, while LLM-guided optimization can explore alternative algorithms, operator decompositions, and hardware-specific techniques. However, existing LLM agents typically target a single programming interface, toolchain, or accelerator family, focus on kernel-level optimization without model-level transforms, and offer limited reuse of experience across hardware targets.
  We present ModelBlaster, a Memory-Augmented In-Context Reinforcement Learning (MAIC-RL) framework for optimizing data-parallel kernels and whole models across heterogeneous SIMD and SIMT accelerators. Its mutable policy is a persistent knowledge base updated at inference time by Actor-Critic Textual Gradient Descent (AC-TGD). The knowledge base maps performance states to actions, outcomes, and constraints, enabling experience reuse across kernels, models, and hardware targets. A model-level optimizer uses kernel-level knowledge to inform whole-model decisions. The same optimization loop and knowledge schema support CUDA on NVIDIA GPUs, OpenCL on Qualcomm GPUs, and RVV intrinsics on RISC-V vector cores, with only lowering and measurement layers specific to each target.
  Compared with PyTorch, ModelBlaster achieves geometric-mean speedups of 1.85x, 5.58x, and 5.18x on KernelBench Levels 1, 2, and 3, and 1.69x on SOL-ExecBench Levels 1 and 2 on a B200 GPU. On Qualcomm Adreno GPUs, it achieves 5.8x over the vendor SDK and 1.7x over Apache TVM; on RISC-V vector cores, it achieves 2.7x over ExecuTorch with XNNPACK across 70 KernelBench problems.

</details>


### 148. Finite-Sample Convergence in Networked Average Reward MARL: Decentralization Pitfalls and Entropy Remedies

- **Authors:** Yizhou Zhang, Yashaswini Murthy, Laixi Shi, Adam Vierman
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04072v1](http://arxiv.org/abs/2611.04072v1)
- **PDF:** [https://arxiv.org/pdf/2611.04072v1](https://arxiv.org/pdf/2611.04072v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study the problem of average reward Multi-Agent Reinforcement Learning (MARL) where agents interact within a network. Each agent in the network conducts local updates with information within its $k$-hop neighborhood and collaboratively maximizes the overall reward of the entire network. We first provide impossibility results in achieving convergence to the global optimal joint policies in our setting. These impossibility results highlight the challenges of decentralized learning with local information in multi-agent systems, namely the issues of multiagency, where each agent independently optimizes its policy, and partial observability, where agents have limited visibility into the global state. Given these challenges which indicate that decentralized policy optimization can generally be certified only up to stationarity, we provide finite-sample convergence guarantees for a decentralized actor-critic algorithm with linear function approximation that converges to an approximate stationary point with small gradient norm. To overcome such impossibility results, we further show that adding fixed-state entropy regularization reshapes the objective landscape which leads to even stronger global convergence guarantees for our proposed actor-critic algorithm.

</details>


### 149. Characterizing Adversarial GEO via Implicit Brand Injection

- **Authors:** Shobhnik Kriplani, Haohan Wang
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04005v1](http://arxiv.org/abs/2611.04005v1)
- **PDF:** [https://arxiv.org/pdf/2611.04005v1](https://arxiv.org/pdf/2611.04005v1)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Generative search engines increasingly shape how users discover products, services, and commercial entities by generating answers from retrieved web content. This creates an opportunity to influence which brands appear in these answers by modifying the content available to the retrieval system. In this work, we study an adversarial generative engine optimization (GEO) setting in which a predefined brand is added to an article through a single contextually integrated mention. The challenge is to make the mention fit the surrounding article without making the content overtly promotional, while keeping it relevant enough to be retrieved and to influence the generated answer. To study this, we introduce Implicit Brand Injection (IBI), a multi-agent framework that identifies insertion locations, rewrites the selected sentence, verifies the edit, and selects the final candidate. To evaluate IBI at scale, we construct IBIBench, which contains 1,000 web articles and 60 synthetic brands across 12 diverse domains, with both endemic and non-endemic brand placements. We compare IBI with Direct Prompting and Best-of-N with ranking under an equivalent budget, evaluating insertion quality, target-chunk retrieval, and downstream brand propagation. Compared with the baselines, IBI produces insertions that better preserve semantics and disrupt perplexity less, while improving Hit@k across all evaluated cutoffs, query regimes, and placement settings. IBI achieves up to 82.2% Hit@10 and 0.74 MRR@10, while Brand Mention Rate (BMR) and Conditional Propagation (CP) reach up to 62.7% and 75.9%, respectively. These results show that a single brand mention can increase both retrieval exposure and brand visibility in generated responses, highlighting the need for defenses against implicit content manipulation in generative search.

</details>


### 150. WASP-Mem: Let Agent Organize Procedural Memory. Human Spend Effort on Diagnosis

- **Authors:** Peizhi Niu, Ge Shi, Vaibhav Gorde, Sarthak Ghosh, Christos Faloutsos, Min Cheng, Kevin Chen
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.04003v1](http://arxiv.org/abs/2611.04003v1)
- **PDF:** [https://arxiv.org/pdf/2611.04003v1](https://arxiv.org/pdf/2611.04003v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents struggle to automate complex enterprise procedures because static, pre-built harness cannot capture proprietary policies, undocumented behaviors, or state-dependent recovery paths that surface only during execution. Procedural memory accrued from agent experience offers a training-free path to closing this gap -- yet unlike episodic records or semantic facts, it must consolidate repeated successes and diagnosed failures into reusable actions and recovery strategies. We introduce WASP-Mem (Wiki-based Agent-Synthesized Procedural Memory), a nimble but effective method that distills execution traces and feedback into persistent, interlinked wiki pages, enabling continual agent learning. On TheAgentCompany benchmark, WASP-Mem raises the checkpoint pass rate by 4.6-6.1% over the strongest baseline we compared across three models while requiring 57-61% less storage. We further present a systematic controlled study spanning consolidation method, feedback type, trace ingestion scope, and refinement rounds. Our results reveal that prescriptive knowledge organization such as human defined schemas and explicit deduplication rules hurts performance rather than closing the procedural-knowledge gap. In contrast, human diagnosis converts failed traces into corrective knowledge and drives sustained improvement: a single round of human diagnosis outperforms four rounds of self-judgment by 7.0-10.9%. These findings point to a simple division of labor: let agents organize procedural memory, and invest human effort where it matters most -- diagnosis.

</details>


### 151. When Music Needs Meaning: Semantic Communication as a Transformative Enabler for the Musical Metaverse

- **Authors:** Ali Al Housseini, Jaime Llorca, Cristina Rottondi, Luca Turchet, Tiziano Leidi, Omran Ayoub
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03995v1](http://arxiv.org/abs/2611.03995v1)
- **PDF:** [https://arxiv.org/pdf/2611.03995v1](https://arxiv.org/pdf/2611.03995v1)
- **Categories:** eess.SY, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Musical Metaverse (MM) enables geographically distributed musicians, audiences, sound engineers, and AI agents to interact through synchronized audio, visual, kinematic, and haptic streams, imposing latency, synchronization, bandwidth, and scalability requirements that are difficult to satisfy with conventional bit-level communication. This paper argues that semantic communication, understood here as the transmission of musically meaningful information rather than raw audio-visual-haptic samples, provides a principled communication paradigm for the MM. We define the MM from a communication perspective and derive modality-specific require ments; propose a three-pillar framework for musical semantic communication comprising semantics extraction, semantic-aware orchestration, and cross-modal semantic synchronization; survey representative work across semantic communication, music AI and edge orchestration, identifying the gaps that prevent their integration; and propose a semantic-first reference architecture based on device-side semantic encoders, edge semantic routers, and cross-modal semantic synchronization. The resulting framework positions the MM as a concrete and demanding use case for 6G semantic communication.

</details>


### 152. A Guideline-Grounded Multi-Agent Framework for Personalized Exercise Prescription from Clinical and Wearable Data

- **Authors:** Xintong Li, Yufen Lin, Yuhua Wu, Fengran Wang, Minxiao Wang, Rebecca A. Gary, Jacob Kariuki, James Smith, Sandra A. Billinger, Canhua Xiao, Xiao Hu, Runze Yan
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03983v1](http://arxiv.org/abs/2611.03983v1)
- **PDF:** [https://arxiv.org/pdf/2611.03983v1](https://arxiv.org/pdf/2611.03983v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Translating population-level exercise guidance into individualized prescriptions requires integrating clinical and wearable data, including diagnoses, medications, functional limitations, and baseline activity, with condition-specific recommendations, a process difficult to scale beyond specialist rehabilitation settings. We developed FITTER, a multi-agent framework that integrates these data with condition-specific guidance to generate personalized FITT-VP prescriptions and applies deterministic safety audit and repair to correct rule-checkable violations. We evaluated FITTER using data from 400 All of Us participants (300 cancer, 100 stroke) against five LLM comparators through computational evaluation, ablation, and structured clinician review. FITTER achieved 98.5% safety-constraint compliance versus 75.8-85.8% for comparators and showed greater quantitative dosing precision and guideline alignment. Cancer-cohort ablation identified safety audit and repair as the largest contributor to safety-constraint compliance. Clinicians reviewed 80 prescriptions across safety, personalization, instruction concreteness, anticipated effectiveness, and clinical acceptability. FITTER provides a clinician-facing approach integrating clinical and wearable data, guidance, and explicit safety constraints.

</details>


### 153. SLATE: A Large-Scale Benchmark for Long-Horizon API Selection in E-commerce Tool Use

- **Authors:** Rongzhe Wei, Ge Shi, Min Cheng, Sarthak Ghosh, Vaibhav Gorde, Leman Akoglu, Pan Li, Na Zhang
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03982v1](http://arxiv.org/abs/2611.03982v1)
- **PDF:** [https://arxiv.org/pdf/2611.03982v1](https://arxiv.org/pdf/2611.03982v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprises increasingly want LLM agents to automate standard operating procedures over their software stacks -- mapping each step of a procedure to the right call among thousands of internal APIs, without hand-authored step-to-API mappings. The core difficulty is API selection at scale: choosing and composing the correct tools over a long horizon, judged only by whether the overall task succeeds. Current tool-use benchmarks do not test this regime -- they expose only a handful of tools, evaluate single-step invocation, or grade multi-step behavior with subjective LLM-as-a-judge scores that penalize valid alternative trajectories. We introduce SLATE (Synthetic Large-scale API Toolkit for E-commerce), a large-scale benchmark that tests large-toolset, long-horizon API selection in a realistic enterprise domain. SLATE couples (i) queries decomposed into hierarchical, tool-grounded procedures over a ~1,000-tool e-commerce library, (ii) a deterministic, context-aware simulator that returns recorded outputs for matching calls and default responses otherwise, and (iii) an end-to-end task-success metric -- a task succeeds when it reaches every reference outcome -- that credits diverse-but-valid trajectories while remaining fully automatic and reproducible. Experiments with six open decision models and the language models they are built on, from 3B to 12B parameters, show that even the best model completes only 5.0% of the tasks, establishing SLATE as a challenging testbed for reliable enterprise tool use. We release SLATE, its simulator, and the evaluation harness at https://geshijoker.github.io/slate/

</details>


### 154. Rapid Mean-Field Formation Transport with a Shared-Representation Neural Fokker-Planck Controller

- **Authors:** Zejian Zhou, Hao Xu
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03981v1](http://arxiv.org/abs/2611.03981v1)
- **PDF:** [https://arxiv.org/pdf/2611.03981v1](https://arxiv.org/pdf/2611.03981v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper develops a mean-field formation transport method with low online computational cost for large-scale multi-agent systems. Classical mean-field planners often require repeated solutions of coupled forward and backward partial differential equations, making online replanning computationally demanding. Density and control are therefore approximated by a common parameterized nonlinear map with separate scalar density and vector control outputs. Parameters are optimized using Fokker--Planck and initial-condition residuals, formation-matching costs on numerically simulated closed-loop particle trajectories, and control effort. Numerical computations are restricted to a bounded region of the state space, with an additional penalty on probability flux across its boundary. For the periodic-domain model, we establish well-posedness of the induced density evolution and bound the density-approximation error in terms of the dynamics and initial-condition residuals. Parameter optimization precedes online operation, during which controller coefficients remain fixed. Experiments quantify the accuracy--runtime trade-off relative to a mean-field planner, show lower transport error than classical feedback baselines, and demonstrate the benefits of the common parameterization.

</details>


### 155. Measuring Model-Specific Alignment Drift in LLM-Based Opinion Dynamics

- **Authors:** Nataša Djurdjevac Conrad, Sebastian Pokutta, Christof Schütte
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03980v1](http://arxiv.org/abs/2611.03980v1)
- **PDF:** [https://arxiv.org/pdf/2611.03980v1](https://arxiv.org/pdf/2611.03980v1)
- **Categories:** cs.AI, physics.soc-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly used as synthetic participants in opinion-dynamics experiments, often assuming that an agent's behaviour is fully determined by its prompt. We test this assumption with a framework in which LLM agents discuss a contested policy issue over repeated rounds while their stance is quantified by a fixed psychometric instrument independent of any dynamics model. Across six LLMs, committed personas are intrinsically stable: in each of the five models tested without peer input, every agent keeps its assigned side for 20 rounds. The observed loss of alignment under discussion is therefore interaction-induced, we call it alignment drift, and model-specific: gpt-4.1 keeps opinion clusters apart, claude-sonnet-5 holds them partially, and gpt-5.6-sol and claude-opus-5 abandon them. Under selective attention, one LLM maintains separated opinion clusters under stance-homophilous attention. Qualitative profiles persist at doubled population and horizon and on a second issue. Such heterogeneity makes the LLM choice a first-class validity variable for social simulation.

</details>


### 156. Beyond Division of Labor: How Roles Shape Feedback and Recovery in Multi-Agent Systems

- **Authors:** Chih-Hsuan Yang, Xinyang Li, Rajeev Thakur, Feng Yan
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03931v1](http://arxiv.org/abs/2611.03931v1)
- **PDF:** [https://arxiv.org/pdf/2611.03931v1](https://arxiv.org/pdf/2611.03931v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Roles in multi-agent large language model (LLM) systems allocate decisions as well as work. In a Planner--Executor--Reviewer team, the Reviewer's approval can determine when the team submits an answer and receives corrective feedback. We study both functions by varying role instructions while holding agents, topology, call budget, and ground-truth evaluator constant, using three open-weight models on Omni-MATH and two on SciBench. Removing roles largely eliminates functional specialization without lowering first-pass accuracy. After a failed first answer, however, submission decisions matter: a role-structured Reviewer often withholds approval, so its team submits less often and receives fewer evaluator verdicts. In an exploratory comparison with feedback available to both teams, the role-free team recovers more often across all five model--benchmark settings. Two further analyses support the importance of feedback opportunities. In a post hoc comparison at equal numbers of verdicts, the pooled recovery difference is small (role-structured minus role-free: $+0.009$, 95% interval $[-0.014,+0.033]$). In an exploratory intervention on $400$ Omni-MATH problems with gemma-4, keeping the role prompts but forcing submission in every cycle raises recovery from $0.198$ to $0.613$; the paired comparison detects no difference from the role-free team. The takeaway is to evaluate roles through recovery after failure as well as specialization. For systems with reliable external feedback, this requires measuring who may submit, how often the team receives feedback, and which agents can act on it.

</details>


### 157. ProofPaths: An AI Agent Framework for Assessing Student Reasoning

- **Authors:** Mohsen Hariri, Vipin Chaudhary
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03882v1](http://arxiv.org/abs/2611.03882v1)
- **PDF:** [https://arxiv.org/pdf/2611.03882v1](https://arxiv.org/pdf/2611.03882v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Students can use large language models to complete assignments, but a correct solution does not establish whether they understand the reasoning behind it. Individualized interviews can probe that understanding but require recurring staff effort. We introduce ProofPaths, an AI agentic framework that combines rubric-based grading with individualized and interactive interviews. Multiple grading agents assess a submission against instructor guidance, exchange critiques, and revise their judgments. Their scores determine which review supplies the grade and feedback. An interview agent asks students to justify steps in their submission and uses their answers to guide follow-up questions. Each question is linked to a retrieved submission excerpt, so instructors can compare the student's explanation with the cited passage. The system tracks assessment progress and stores grading reviews and interview transcripts for each submission. Several deterministic tests of the assessment controllers check source handling, score aggregation, and limits on correction attempts. Instructors can inspect all reviews and transcripts and override grades within the assignment workflow.

</details>


### 158. Performance, Scalability and Maintenance: An Experimental Study of RPA vs. Autonomous Agents in the Healthcare Domain

- **Authors:** Daniel Schulz, Pedro Cabral Buchaim, Bernardo Soares, Fernando Rafael Ensslin Schwengber, Lorenzo Farias, Daniela Duarte da Silva Bagatini, Ana Paula Wernz da Cunha Müller
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03853v1](http://arxiv.org/abs/2611.03853v1)
- **PDF:** [https://arxiv.org/pdf/2611.03853v1](https://arxiv.org/pdf/2611.03853v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Healthcare information systems are fragmented, and retrieving data from legacy web portals is a recurrent need. Robotic Process Automation (RPA) is deterministic but sensitive to interface changes, whereas autonomous agents based on large language models (Agent Process Automation, APA) promise adaptability at a higher computational cost. Following Design Science Research, we developed and compared an RPA solution (Playwright) and an APA solution (browser-use, LangGraph and Gemini 2.5 Flash-lite) to retrieve mammography and breast ultrasound reports from a laboratory portal, treating reports solely as informational artifacts. Across two rounds (T and T+7), RPA reached 98.90% accuracy and 98.27% F1-score versus 96.49% and 94.48% for APA, was about 13 times faster (16.07 s vs. 207.21 s per patient) and cost about six times less per report (USD 0.030 vs. 0.187). Both reached 100% step success rates; APA varied more over time. For a stable interface, RPA was superior.

</details>


### 159. Rethinking Next-Visit Diagnosis Prediction Beyond Aggregate Metrics: Retrieval--Memory Multi-Agent Adjudication

- **Authors:** Heejoon Koo
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03826v1](http://arxiv.org/abs/2611.03826v1)
- **PDF:** [https://arxiv.org/pdf/2611.03826v1](https://arxiv.org/pdf/2611.03826v1)
- **Categories:** cs.CL, cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Next-visit diagnosis prediction forecasts the diagnoses documented at a patient's next encounter, turning retrospective electronic health records into prospective clinical prediction. However, conventional aggregate evaluation obscures its multifaceted nature: distributionally, models must handle variable-size diagnosis sets and long-tailed labels; temporally, they must distinguish persistent, newly recorded, and recurrent diagnoses; and both vary with observed history depth. We introduce an evaluation framework along these dimensions and apply it to rule-based heuristics, LLM-based prompting, retrieval, memory, and multi-agent approaches. This reveals that repeating the last visit outperforms most LLM-based approaches overall despite predicting no new or recurrent diagnoses, and that retrieval and memory exhibit distinct profiles whose relative strengths vary across temporal transitions and backbones. Motivated by this, we propose LONGINUS, a retrieval-memory multi-agent adjudication framework combining evidence retrieved from patient records with structured memory of the patient trajectory. Using cross-view agreement as a reliability heuristic, it preserves shared predictions and adjudicates disagreements without revealing their source. Across MIMIC-III and MIMIC-IV with four LLM backbones, LONGINUS achieves the best transition-specific performance among LLM-based methods in nearly all settings while remaining competitive with them on aggregate metrics.

</details>


### 160. WebHarbor: Docking Real Websites for Evolving GUI Agent Environments

- **Authors:** Zhaoyang Wang, Qianhui Wu, Boyu Gou, Demi Wang, Jiacheng Zhang, Peichun Hua, Qize Li, Shi Qiu, Yifan Jiang, Yifan Zhang, Zexu Jin, Baolin Peng, Bolin Shen, Chetan Bansal, Dehan Kong, Deren Lei, Dongshen Peng, Fengqing Jiang, Hao Cheng, Haoqing Wang, Jiaming Shan, Jicheng Wang, Jingguang Zhou, Jixuan He, Kaide Zeng, Kangyu Zhu, Lama Moukheiber, Mufan Qiu, Peng Xia, Qihan Sun, Qingwei Lin, Qiushi Sun, Ruichen Zhang, Shuqing Luo, Si Qin, Sicheng Fan, Tao Xiong, Wenlin Yao, Xinyu Zhang, Xinyue Zeng, Xuanrui Li, Xuchao Zhang, Yian Wang, Yichao Liu, Yiming Liang, Yiyang Zhou, Yizhu Jiao, Yuetai Li, Yurun Chen, Yuxuan Zhang, Zheyuan Yang, Zhiyuan Yao, Zhongyang Li, Zihao Li, Zili Wang, Jianfeng Gao, Huaxiu Yao
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03634v1](http://arxiv.org/abs/2611.03634v1)
- **PDF:** [https://arxiv.org/pdf/2611.03634v1](https://arxiv.org/pdf/2611.03634v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

GUI web agents require realistic and interactive environments that remain stable during both evaluation and training. Live website evaluation suffers from changing content, access restrictions, and limited coverage of authenticated workflows, while existing synthetic environments for training often lack functional depth and visual fidelity. We propose WebHarbor, a suite of 153 executable and dockerized website environments that faithfully reconstruct the visual interfaces, content, and functional workflows of real-world web services under deterministic control. We build WebHarbor through task-driven human-agent collaboration, where environments evolve as new tasks expand their functional scope, coding agents implement the required changes, and human contributors audit visual fidelity, functional correctness, and task validity. The resulting suite comprises 3,518 tasks spanning multi-step and post-authentication workflows, where existing works often fail to cover. Beyond reliable evaluation, WebHarbor provides high-fidelity synthetic web environments for cost-efficient reinforcement learning (RL). We demonstrate that a Qwen 4B-level GUI agent trained with RL in WebHarbor generalizes to unseen tasks and performs competitively with leading open-source GUI web agents across four benchmarks. The code and data are publicly available at https://github.com/aiming-lab/WebHarbor.

</details>


### 161. Strategist: Evolving Reasoning with Agents

- **Authors:** Taiming Lu, Qi Xu, Zhigang Hua, Zhuang Liu
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03618v1](http://arxiv.org/abs/2611.03618v1)
- **PDF:** [https://arxiv.org/pdf/2611.03618v1](https://arxiv.org/pdf/2611.03618v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

A model is only half of an AI agent system. The other half is the inference strategy: the reasoning procedure that turns model calls into a response. Today that second half is written by hand, and the experience of building one strategy never carries to the next. We introduce Strategist, a meta-agent that evolves inference strategies across tasks. Each strategy is written as a blueprint,executable code that other strategies can reuse, and together the blueprints form a library. Given a task and a small development set, Strategist retrieves related blueprints, writes candidate strategies, tests them on real samples, and revises them from the results. Every candidate then enters the library, so later tasks build on earlier discoveries. On 30 benchmarks, Strategist beats the strongest baseline on 24 and matches its average accuracy (74.7% vs.74.0%) at 39% lower inference cost. Its strategies also transfer to unseen tasks and other models without further search. The part of an AI system that is not improved on its own now does.

</details>


### 162. Four Bridges: Measuring Deception Propensity in a Multi-Agent Game

- **Authors:** Raphael Casey, Michael Simeone, Alberto Tosato, Florian Ernst, Kemal El Moujahid, James Tamplin, Tommaso Tosato
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03600v1](http://arxiv.org/abs/2611.03600v1)
- **PDF:** [https://arxiv.org/pdf/2611.03600v1](https://arxiv.org/pdf/2611.03600v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly deployed in settings where they interact and coordinate with other agents, yet honesty is mostly measured in single-turn, single-agent benchmarks that pressure the model to deceive. We study deception that emerges in multi-agent interaction without any instruction to deceive. We introduce Kradle, a platform for evaluating AI models, and Four Bridges, an information asymmetry game in which four agents distribute across four rooms: one is the death room, the others hold food worth more if not shared. One agent, the informed agent, knows which room is the death room and can withhold or disclose that information. We evaluate eight frontier models as the informed agent. Deceptive behavior appears in every model and in 73% of all runs (6% to 100% per model), and does not decrease with capability tier within a model family. When the informed agent does disclose, the warning is often challenged, and agents that challenge it enter the death room twice as often as those that do not. Telling all agents that one of them knows the death room collapses deception in six of eight models; telling the informed agent that the room is permanently fatal moves only one. On an open-weight model, an honesty steering vector reduces deception to 0% and adversarial honesty training to 6%. The platform and game provide a testbed for measuring deceptive behavior and comparing interventions.

</details>


### 163. FedReady: Bounded Agents for Federation Formation

- **Authors:** Ziyue Xu, Holger R. Roth, Chester Chen, Peter Cnudde
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03586v1](http://arxiv.org/abs/2611.03586v1)
- **PDF:** [https://arxiv.org/pdf/2611.03586v1](https://arxiv.org/pdf/2611.03586v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Federated learning (FL) runtimes standardize aggregation and deployment, but each new study still requires federation formation: selecting task-eligible sites and preparing their local data and task code for federated training or analysis. This preparation recurs when the target changes, while raw records and site-private mappings are excluded from cross-site FL messages. We present FedReady, a system that performs federation formation with bounded LLM agents. Agents propose shared contracts, local adapters, and task code; the runtime owns workflow state and accepts artifacts only after checks tied to their digests. Candidate site discovery prioritizes recall; local eligibility verification checks task support before site admission. Once participating sites and artifacts are fixed, conventional federated training or analysis proceeds without readiness agents. Across 39 simulated retinal sites and four tasks, discovery reaches recall 1.00 at precision 0.65; local eligibility verification removes all 17 false positives without losing an eligible site-task pair. The participating sites supply 45,575 task-record instances and complete four 100-round jobs, including one with a runtime-generated contract. Across ten patient cohorts, preparation supports seven patient populations and holds endpoints at three sources as unsupported. Comparison with manually prepared reference populations and analysis (the manual reference) gives a maximum survival-curve difference of 0.001133. We also analyze 19 development failures, targeted classification ablations, and standalone and heterogeneous agent configurations. These results establish the feasibility of task-specific data preparation before ordinary FL training or analysis.

</details>


### 164. MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study

- **Authors:** Farooq Shaikh, Biagio Montaruli
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03555v1](http://arxiv.org/abs/2611.03555v1)
- **PDF:** [https://arxiv.org/pdf/2611.03555v1](https://arxiv.org/pdf/2611.03555v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Model Context Protocol (MCP) lets agentic AI frameworks connect language models to external tool providers, but it carries attacker-controlled content (tool descriptions, schema fields, and response data) into model context without validation. Prior benchmarks measure model compliance with poisoned instructions without confirming real execution. We present the first cross-framework measurement of MCP tool poisoning with real tool execution. A 25-class root-cause taxonomy unifies prior classifications, and the open-source tool mcpvenom drives a 9,720-cell susceptibility matrix across 12 frameworks, 18 models, and 45 attack scenarios, with a dual oracle that confirms exfiltration via canary HTTP receipt. The overall attack success rate is 22.9% (2,113 vulnerable cells). Of these, 64.9% dispatch an attacker tool call, 23.0% contact the attacker endpoint, and 12.1% verifiably exfiltrate a secret. Resistance is model-level: nine core frameworks cluster within 23 to 26% (chi-squared = 3.30, p = 0.91), and no framework implements intentional defense. Incidental framework properties mitigate in specific cases, and a regex description scanner rejects 20 of 45 scenarios at a 7.2% false-positive rate, so metadata scanning alone is a partial control. Model ASR ranges from 0.4% to 49.7%. Claude Opus 4.8 is vulnerable in 8 of 530 cells while issuing 223 explicit refusals. A code-level audit finds no intentional defense across twelve frameworks, and all five coordinated disclosures across four vendors were rejected.

</details>


### 165. Can LLM Agents Be Forward-Deployed Engineers? Requirement Discovery and Delivery for Enterprise Text-to-SQL

- **Authors:** Marianne Menglin Liu, Rongguang Wang, Zheng Wang, Yewen Wang, Leonid Boytsov, Tao Sheng, Sujith Ravi, Dan Roth
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03551v1](http://arxiv.org/abs/2611.03551v1)
- **PDF:** [https://arxiv.org/pdf/2611.03551v1](https://arxiv.org/pdf/2611.03551v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM coding agents can increasingly automate model post-training, but whether they can act as forward-deployed engineer (FDE) agents, discovering customer requirements and turning them into deployment decisions, remains unclear. We study this on a real enterprise text-to-SQL engagement: a simulated customer, grounded in the real use case's requirements, starts with an ambiguous request. An agent must discover acceptance criteria, data permissions, and hardware constraints in the discovery phase, then plan and execute a post-training recipe in the delivery phase. Across 15 models, the strongest discover over 80% of withheld requirements and open-weight models discover 40-50%; in the delivery phase, only 25% of runs across eight coding-agent configurations pass all acceptance criteria. We identify four bottlenecks in this engagement: (1) incomplete discovery, with 40% of withheld requirements missing or misrepresented; (2) unreliable execution; (3) underused compute budgets and a lack of systematic comparisons across base models and post-training methods; and (4) benchmark accuracy does not guarantee production readiness. We suggest human review of discovered requirements, monitoring of the agent's plan during execution, and an explicit experiment-environment specification covering hardware, budget scope, and production checks.

</details>


### 166. Can LLM Agents Improve Imperfect Earth System Model Parameterizations?

- **Authors:** Kara D. Lamb
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03543v1](http://arxiv.org/abs/2611.03543v1)
- **PDF:** [https://arxiv.org/pdf/2611.03543v1](https://arxiv.org/pdf/2611.03543v1)
- **Categories:** physics.ao-ph, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Earth system models (ESMs) rely on parameterizations to represent unresolved processes such as convection, cloud microphysics, and turbulence. However, translating advances in physical understanding into stable, validated parameterizations and integrating them into ESMs often takes years. Agentic AI could accelerate this process and enable more systematic exploration of design choices. Using warm-rain collision-coalescence as a test case, we evaluate agents' ability to synthesize scientific literature, reimplement published bulk parameterizations, and propose new functional forms as differentiable JAX code. We compare conventional parameterizations, data-driven emulators, and agent-generated closures against high-fidelity superdroplet simulations, repeating unattended experiments across ten language models. With expert guidance or iterative feedback, agents produced executable, differentiable, mass-conserving code, although unattended performance depended strongly on the scheme and language model. Iterative feedback lowered median rollout error for eight of ten models. Retuned physical schemes matched or outperformed many learned parameterizations at substantially lower computational cost, but two of 100 unattended agent-generated closures achieved slightly lower rain-mass error than the most accurate retuned scheme on held-out simulations.

</details>


### 167. DistDebug-Bench: Can LLM Agents Diagnose Bugs in Distributed Systems?

- **Authors:** Yuxuan Jiang, Chenglin Liu, John Rose, Mason Miller, Ruthesh Thavamani, Juntao Wu, Yinwei Huang, Jiahao Xu, Peng Huang
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03523v1](http://arxiv.org/abs/2611.03523v1)
- **PDF:** [https://arxiv.org/pdf/2611.03523v1](https://arxiv.org/pdf/2611.03523v1)
- **Categories:** cs.SE, cs.DC, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents show strong potential in software engineering tasks such as competitive programming and code synthesis. Existing benchmarks, however, largely focus on small-scale settings such as self-contained Python modules, leaving distributed systems, an essential class of production software, under-examined. We introduce DistDebug-Bench, a benchmark for evaluating agents' ability to diagnose complex-system failures at the code level. It curates 120 high-quality real-world bugs from 11 widely used distributed systems, spanning 5 programming languages and 10 failure patterns. Through an extensive evaluation of state-of-the-art LLMs and agents, we identify substantial gaps between current agents and real-world debugging tasks. A recurring gap is tunnel vision due to a lack of explicit reasoning structure and nondeterminism from inconsistent tool-use scope. The benchmark and evaluator are available at https://github.com/OrderLab/distdebug-bench, with agent traces and a leaderboard at https://distdebug.com.

</details>


### 168. Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization

- **Authors:** Gabriele Oliaro, Jaeseong Lee, Zhaoyuan Su, Sreeram Vennam, Zhihao Jia, Samyam Rajbhandari
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03517v1](http://arxiv.org/abs/2611.03517v1)
- **PDF:** [https://arxiv.org/pdf/2611.03517v1](https://arxiv.org/pdf/2611.03517v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents for GPU kernel optimization sit at two ends of a structure-freedom tradeoff. Scripted agents fix what the model does at each step, via a learned policy, an optimization menu, or fixed roles, and are sample-efficient where the recipe applies and stall where it does not. Open-ended agents let a self-directed model mutate a population of kernels and pay for the freedom in trials: thousands of evaluations, repeated edits, and wrong candidates. Both respond to hard targets by equipping the agent with more: parsed profiler output, disassembly analysis, retrieval over documentation and libraries, and stores of lessons. We argue that both lack direction, a hypothesis about where the remaining gap is, and that a short question asked at the right moment supplies it without narrowing what the agent may do next. We present KernelSeek, a question-driven agent that makes an existing CUDA kernel faster with no operator-specific knowledge and no faster implementation to imitate: a general-purpose coding agent, a minimal harness that enforces a verifiable goal, and questions at decision points, first from a human, then from a bank the agent applies to itself. On the same task, evaluator, hardware, and week, a tool-rich autonomous agent built in the prevailing style plateaued at 0.50x FlashAttention-3 after 133 model-driven steps; KernelSeek reached 1.13x. It then produced dependency-free FlashAttention forward kernels for Hopper and Blackwell, single CUDA files with no CUTLASS, CuTe, cuBLAS, or cuDNN, correct on all 182 scenarios per architecture and 1.16x FlashAttention-3 and 1.46x FlashAttention-4 (geometric mean). Across 162 human messages and 11.5K agent tool calls, every large gain followed a question that moved the agent to a different layer of the system or rejected a claimed limit, never one that supplied information. We release the kernels, harness, question bank, and all traces.

</details>


### 169. Harder Than the Task: From Technical to Organizational Difficulty in AI Benchmarking

- **Authors:** Victor Barres, Aden Barton, Nicolai J. Foss, Henrik M. Nielsen
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03494v1](http://arxiv.org/abs/2611.03494v1)
- **PDF:** [https://arxiv.org/pdf/2611.03494v1](https://arxiv.org/pdf/2611.03494v1)
- **Categories:** cs.CY, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI benchmarks have made remarkable progress in measuring the ability of AI systems to perform increasingly demanding cognitive and technical tasks. Yet, many of these benchmarks treat technical tasks as the unit of analysis, while much economically valuable work takes place within organizations, where tasks are embedded in a system of relations. Within organizations, successful task performance depends not only on solving the technical demands of the task but also on navigating the interdependence of activities, distributed knowledge, differentiated authority, temporal constraints, conflicting interests, and changing environmental conditions while the task is underway. Accordingly, we argue that organizational task difficulty constitutes a distinct and insufficiently recognized dimension of AI capability, and that existing approaches to benchmarking provide an incomplete basis for assessing how effectively AI agents can perform real-world organizational work. By drawing on organization theory, we develop a taxonomy of the structure of work that characterizes the conditions that agents face in organizational work. Applying this taxonomy to analyze existing benchmarks, we find limited and uneven coverage of organizational dimensions, with fewer than one quarter of prominent benchmarks claiming any of them. We therefore argue that AI benchmarks should increasingly move beyond the evaluation of technically difficult tasks toward the systematic assessment of agents' ability to navigate the organizational conditions under which economically valuable work takes place.

</details>


### 170. RuntimeTickets: Source-Grounded Security Obligations for Agent Skills

- **Authors:** Kuiyi Gao, Xue Liu, Bowei He
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03772v1](http://arxiv.org/abs/2611.03772v1)
- **PDF:** [https://arxiv.org/pdf/2611.03772v1](https://arxiv.org/pdf/2611.03772v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Third-party Agent Skills extend what an autonomous agent can do, but a malicious Skill can hide data exposure or output manipulation inside a legitimate workflow. Neither reading a Skill's description nor granting it tool permissions tells whether its execution meets the user's security requirements. We introduce RuntimeTickets, a protocol that enforces and audits these requirements while a Skill runs. From released malicious-Skill datasets we derive a risk model and build adversarial-benign Skill pairs. From the task's delivery contract, a language model proposes security obligations for that task. Each obligation cites the Skill lines it answers, and the ticket tightens the host's approvals into fine-grained allowed actions but never loosens them. A runtime gate checks the recipient, object and amount of every outbound send before forwarding it, and trusted monitors record the effects within their observation scope. The ticket links these checks and observations to the approved obligations of each Skill run, and a deterministic decoder turns the ticket's status into governable data flows and verifies each obligation. Neither enforcement nor decoding involves a language model, so text injected by a Skill can change the proposal but never the rule that decides a send. We evaluate RuntimeTickets at the network egress boundary of three unmodified agent frameworks against production Skill scanners and runtime baselines, among them an AgentBound-derived allow-list and SkillGuard. RuntimeTickets eliminated both failure modes of current Skill defenses, overlook (malicious Skills let through) and overkill (benign Skills blocked): its overlook rate was 0.0% and its overkill rate 0.0%, while the scanners erred on both sides. RuntimeTickets ties approved requirements to verifiable execution evidence and offers a common foundation for the safe and auditable deployment of third-party Skills.

</details>


### 171. Optimize the Harness, Not the Model: Fitting a Minimal Agent to a Self-Hostable LLM for Investigative Analysis

- **Authors:** Shai Nahum Gefen, Vered Chassida, Dmitry Basin, Guy Feigenblat
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03434v1](http://arxiv.org/abs/2611.03434v1)
- **PDF:** [https://arxiv.org/pdf/2611.03434v1](https://arxiv.org/pdf/2611.03434v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Government intelligence teams need LLM agents that can analyze large, messy evidence collections, but security and cost constraints often rule out hosted frontier models and broad, hard-to-audit tool surfaces. We report CLEO: Constrained Loop for Environment Optimization, a method for fitting a minimal agent harness to a fixed, self-hostable LLM. Given an expert-validated dataset, CLEO admits only the tools, guardrails, memory policies, and loop components that improve accuracy while remaining general and auditable. On our held-out dataset, the CLEO harness reaches an 83.8% pass rate, within 1.2 points of the strongest out-of-the-box Claude Code SDK baseline, while being two orders of magnitude smaller.

</details>


### 172. IdeaTaste: Do LLMs Share the Research Taste of Human Researchers?

- **Authors:** Shanshan Zhong, Chen Xu, Jingjie Ning, Zhengzhong Liu, Aviral Kumar, Chenyan Xiong
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03424v1](http://arxiv.org/abs/2611.03424v1)
- **PDF:** [https://arxiv.org/pdf/2611.03424v1](https://arxiv.org/pdf/2611.03424v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Research taste, the judgment of what to read, which problems to pursue, and which methods to try, increasingly shapes the work of AI scientists, yet it remains far less understood than their ability to execute research. We introduce IdeaTaste, a benchmark that scores an LLM by how closely the research proposals it writes from a literature snapshot frozen at 2025 match the work the same communities published in 2026. Our experiments span six contemporary language models and four research areas from established to emerging fields, covering more than 90{,}000 proposals in total. LLM agents fall well short of human communities in both the literature they cite and the ideas they state, reaching about 26\% of the human level on citation matching and only 18\% on idea matching. Their populations can cite as diversely as a community and take up its tasks and methods, yet rarely arrive at the concrete approaches and research plans it pursues. Neither richer field context nor larger populations substantially close this gap. In blinded expert review, AI proposals trail the 2026 papers least in presentation and most in expected success, echoing their gap in concrete approaches, and those whose ideas no human paper shares fare worst, suggesting weaker directions rather than overlooked opportunities. These results indicate that the main bottleneck in AI research taste lies less in finding the directions a community works on than in turning them into the concrete approaches it goes on to pursue. We release IdeaTaste as an open, continuously updated leaderboard (https://cxcscmu.github.io/IdeaTaste) that benchmarks contemporary AI proposals against future publication cycles.

</details>


### 173. DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects

- **Authors:** Yumou Liu, Mingju Chen, Zhoufutu Wen, Qianyu Yang, Zijie Wang, Sihan Chen, Yeqian Liu, Chenghao Yang, Tiliang Duan, Qiyu Cai, Yanglihong Xiao, Jiayun Dong, Jianlan Ma, Shenhao Miao, Yuhan Cao, Lu Xu, Que Shen, Tian Gao, Ziyu Liang, Eric Yang, Ge Zhang, Jianpeng Jiao, Xuanhe Zhou, Fan Wu
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03412v2](http://arxiv.org/abs/2611.03412v2)
- **PDF:** [https://arxiv.org/pdf/2611.03412v2](https://arxiv.org/pdf/2611.03412v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are judged by what they deliver, and in professional work what gets delivered is a project, not a task. A project pays off only if the whole package holds, and one weak part can limit the value of the rest. Yet existing benchmarks mostly test agents on one task at a time, leaving a gap between the capability we measure and the outcome that makes agents useful. To address this gap, we introduce DeliverBench, which tests whether agents can carry a project from brief to final delivery. Its 11 projects, spanning financial due diligence, legal contract drafting, and drug safety reporting, are reconstructed with 13 domain experts from real materials and chain 150 subtasks through 2-15 rounds of new materials and client feedback. Because no reference outputs are injected, agents inherit their own errors from one task to the next. Expert rubrics then score every checkpoint as well as the final package. Across seven model-harness systems, even the best system scores only 65.0 out of 100 on final delivery and passes 50.0% of subtasks at a 90-point threshold. The failures are often failures of carrying work forward: in one audit project, all seven systems addressed the review findings, but only one preserved traceability. Together, these results suggest that task-level capability does not simply compose into delivery, which also depends on keeping the work coherent as it evolves.

</details>


### 174. From Reactive to Agentic Resilience: Multi-Timescale AI-RAN Orchestration Under Signaling Storms

- **Authors:** Sotiris Chatzimiltis, Mahdi Boloursaz Mashhadi, Mohammad Shojafar, Rahim Tafazolli
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03406v1](http://arxiv.org/abs/2611.03406v1)
- **PDF:** [https://arxiv.org/pdf/2611.03406v1](https://arxiv.org/pdf/2611.03406v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Next-generation open radio access network (Open RAN) and AI-RAN deployments turn the RAN into a disaggregated, compute-aware platform whose service continuity depends on many control loops acting at different timescales. Resilience in this setting is best seen as a lifecycle spanning anticipation, absorption, adaptation, recovery, and evolution. Yet, existing mechanisms remain stage-specific and are rarely coordinated across the control hierarchy. This paper argues that agentic AI offers an orchestration layer that coordinates this lifecycle, turning operator intent into coordinated action while keeping slow language-model reasoning off the fast control path. Using mass-attachment signaling storms as a running study, we build a discrete-event Open RAN attach simulator that captures retry amplification, shared-compute contention, and non-instantaneous provisioning, and we propose a three-tier framework in which an orchestrator at the service management and orchestration layer sets a standing policy, a per-site non-real-time agent judges storms and anticipates scheduled crowds, and a deterministic near-real-time loop enforces every decision. Across experiments, the agentic controller approaches the resilience of a fully provisioned pool of servers at a quarter of its capacity by reading a scheduled event from a calendar and provisioning ahead of it. No reactive weight setting recovers this once the surge arrives. Free-text operator intents ground into control directives at 94% exact match on previously unseen intents, and a single instruction reshapes live behavior end to end. We also quantify the latency, cost, and contention limits that bound it. The supplementary material provides analytical proof of the derived Theorem on anticipation horizon, as well as the subsequent Corollary results on reactive provisioning limits.

</details>


### 175. An Axiomatic Framework for Reinforcement Learning in Open Multi-Agent Systems

- **Authors:** Jianhong Wang, Yang Li, Samuel Kaski, Jonathan Lawry
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03301v2](http://arxiv.org/abs/2611.03301v2)
- **PDF:** [https://arxiv.org/pdf/2611.03301v2](https://arxiv.org/pdf/2611.03301v2)
- **Categories:** cs.LG, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Open multi-agent systems, where only a subset of agents are controllable, are central to real-world domains such as smart grids, yet lack a principled foundation for reinforcement learning algorithm design. We study this setting through n-agent ad hoc teamwork (NAHT), a recent framework for learning in open multi-agent environments. We propose an axiomatic framework that derives value function learning from the Shapley axioms (Efficiency, Symmetry and Linearity), treating them as structural constraints rather than heuristic design choices. This formulation builds on a novel NAHT decomposition, which characterises the fundamental difference between open and fully controllable multi-agent systems, and establishes a cooperative game-theoretic foundation for learning. We further show that enforcing these axioms on learning individual value functions recovers the Shapley value for Dec-POMDPs, providing a principled bridge between reinforcement learning and classical cooperative game theory. Building on this framework, we introduce Shapley Machines and Banzhaf Machines, two generic algorithmic templates that can be instantiated with standard reinforcement learning methods. When applied to strong base algorithms such as IPPO and POAM, our methods consistently improve learning efficiency and generalisation to unseen agent types and conventions across NAHT benchmark tasks. The code of experiments is published on https://github.com/hsvgbkhgbv/axiomatic-rl-naht.

</details>


### 176. SQLoom: Set-Contrastive Learning of Syntactic, Semantic, and Logical Dependencies for Text-to-SQL

- **Authors:** Hao Fu, Degang Sun, Wan Wei, Jinxia Wei, Chun Long, Peng Gao
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03298v1](http://arxiv.org/abs/2611.03298v1)
- **PDF:** [https://arxiv.org/pdf/2611.03298v1](https://arxiv.org/pdf/2611.03298v1)
- **Categories:** cs.DB, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Text-to-SQL translates natural language questions into SQL queries, enabling database access without writing SQL. Fine-tuning open-weight large language models (LLMs) is cost-effective, but existing methods treat SQL as ordinary text and optimize token-level likelihood without explicitly modeling its syntactic, semantic, and logical requirements. Thus, a single incorrect alias or comparison operator can invalidate a query while contributing little to training loss. We propose SQLoom, a constraint-aware fine-tuning framework with supervision at three levels: syntactic validity under SQL grammar and database schema, semantic alignment between query decisions and the question, and logical consistency across dependent clause decisions. SQLoom extends supervised fine-tuning with a unified set-contrastive objective favoring sets of correct outputs over minimally different incorrect ones at each level. LLM agents propose this supervision, which a SQL parser and execution on counterexample databases verify. We also release Spider-Refined, a training dataset correcting 378 flawed Spider annotations and enriching database schemas. Experiments on Spider, BIRD, and three perturbed Spider variants show that SQLoom improves execution accuracy for Qwen3-1.7B from 62.9% zero-shot to 88.7% on Spider development, reaching 89.2% on Spider test and 73.4% on BIRD development. It outperforms fine-tuning, reinforcement learning, and agent-based baselines with up to 70 billion parameters. On question perturbations, SQLoom loses at most 0.6 accuracy points versus up to 12.1 for agent-based methods. It generates SQL in a single pass at 0.42s per query, 23$\times$ faster than a GPT-4-based agent method. These results demonstrate the effectiveness of set-contrastive supervision over token-level training.

</details>


### 177. What Structurally Breaks an Agent? Auditing Difficulty in Stateful Tool-Use Workflows

- **Authors:** Shereen Anand, Ju Wang, Yali Du
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03227v1](http://arxiv.org/abs/2611.03227v1)
- **PDF:** [https://arxiv.org/pdf/2611.03227v1](https://arxiv.org/pdf/2611.03227v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

An aggregate task score does not distinguish failures of scheduling, state retention, and candidate selection. We develop a small executable instrument that varies dependency depth, candidate count, active state width, and access to current-state snapshots while holding the number of required operations fixed. Two dependency-graph families show that increasing depth at fixed work changes both scheduling freedom and the number of reachable completion states, so these controls are coupled, and we quantify the coupling. The primary study contains 49,152 generated tasks and 393,216 reference-controller rollouts. A separately frozen follow-on design adds 295,936 rollouts covering retention strategy, snapshot cadence, hidden state resampling, recovery, query locality, candidate indexing, and relabeling. Residue caches and precomputed plans solve tasks that defeat limited raw-value caches, and indexed selection removes the serial-scan branching deficit. Hidden resampling imposes an exact success ceiling that additional state tracking cannot overcome. The contribution is an executable diagnostic instrument, analytic calibration, and an audit of its assumptions. A small local CPU study with a 0.5B model completed no workflows, and a 16-episode Copilot-routed fractional factorial is descriptive only. Neither supports general capability claims.

</details>


### 178. Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction

- **Authors:** Yiwei Zha, Qingyu Meng, Herbert Bos, Min Chen
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03223v1](http://arxiv.org/abs/2611.03223v1)
- **PDF:** [https://arxiv.org/pdf/2611.03223v1](https://arxiv.org/pdf/2611.03223v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents compact long histories to fit their context windows, but the compacted context must still carry the operating rules that govern later actions. Prior work shows that violations rise after compaction, but measures compliance outside a complete agent harness and does not identify where each violation comes from. We introduce ARCBench(Agent Rule Compliance Benchmark), a configurable benchmark built on the open-source pi agent harness. Its tool-calling agent loop lets us measure rule compliance from actions taken during execution, bringing the evaluation closer to deployed agent workflows. Using ARCBench, we examine where violations after compaction come from, and how different compaction configurations and adversarial settings change their sources. We find that compaction rarely deletes the rule: most violations after compaction occur while the rule is still in the compacted history, with the agent treating a later request as permission, ignoring the rule, and proceeding anyway. Where violations come from depends on the configuration: how the rule is delivered decides whether the agent would break it even without compaction, while the compaction strategy and budget decide whether the rule survives. The strongest compactor-targeted attack more than doubles violations by corrupting the rule in the summary and changing how the agents behave, whereas the strongest defense restores the rule in most summary but still violates. Finally, retaining a rule does not guarantee compliance: compacted runs that retain the rule violate more than twice as often as runs with the full history.

</details>


### 179. Auto-Research Agent on MSA Organization to Improve Protein-Protein Complex Structure Prediction

- **Authors:** Zilu Zhang, Jing Bao, Lifeng Qiao, Sheng Xu, Qiantai Feng, Siqi Sun, Yang Yang
- **Published:** 2026-11-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.03183v2](http://arxiv.org/abs/2611.03183v2)
- **PDF:** [https://arxiv.org/pdf/2611.03183v2](https://arxiv.org/pdf/2611.03183v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Protein-complex structure prediction with AlphaFold 3 depends on MSA content, depth, and cross-chain pairing. Current pipelines apply uniform recipes, typically maximizing depth and pairing by species, yet even whether cross-chain pairing helps AF3 remains contested. We show that the value of both depth and pairing is strongly target-dependent, so no single recipe is optimal across interfaces. We introduce an autonomous agent that treats a frozen AF3 as a black-box experimental instrument. For each target, the agent formulates biological hypotheses, analyzes and reorganizes the MSA, and iteratively refines sequence selection and pairing using predictor label-free signals alone. On 1{,}015 protein--protein interfaces from three benchmarks released after AF3's training cutoff, the agent improves overall interface DockQ over AF3's default pipeline and fixed MSA recipes on every benchmark, while using on average 60\% fewer MSA sequences than the default. Gains are largest for inter-species heteromers, where species-based pairing is unreliable: mean DockQ increases from 0.465 to 0.612 on FoldBench and from 0.482 to 0.562 on HD439. The improvements arise from both sequence construction and pairing policy, including deliberate non-pairing. These results recast MSA design as a target-specific problem and show that an autonomous agent can adapt it at test time through biological reasoning and self-directed, confidence-guided experimentation.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*