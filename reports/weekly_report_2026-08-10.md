# Weekly AI Agent Paper Report

**Generated:** 2026-08-10 10:34
**Period:** 2026-08-03 to 2026-08-09

## Summary

- **Total papers fetched:** 745
- **Papers matching keywords:** 161
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-08-03) | Change |
|--------|-----------|-----------|--------|
| Total matched | 161 | 164 | -3 |
| arxiv | 158 | 163 | -5 |
| biorxiv | 1 | 0 | +1 |
| medrxiv | 2 | 1 | +1 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (3 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. AI semantics for biomedical data integration

- **Authors:** McLaughlin, J., Puig-Barbe, A., Ibrahim, A., Pava, D., Pendlington, Z. M., Matentzoglu, N., Sollis, E., Foreman, A., Wilson, R., Lopez Gomez, F., Harris, L., Adeleye, Y., Kaur, S., Meldal, B., Smedley, D., Parkinson, H.
- **Published:** 2026-08-07
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.03.742514](https://doi.org/10.64898/2026.08.03.742514)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Researchers increasingly need to explore hypotheses that span multimodal data across different scales, organisms, and domains. In practice, this requires connecting knowledge across fragmented databases with incompatible APIs and heterogeneous annotation practices. Large language model (LLM) agents can automate this data integration process, but grounding LLM agent outputs in scientifically correct sources of truth remains a significant challenge. Here we describe our deployment of a novel AI semantics workflow using LLM agents to enable scalable data integration, grounded in biological knowledge in the form of ontologies. Our workflow comprises (1) a multi-agent system curating scientific knowledge across ontologies using the Ontology Lookup Service (OLS) as grounding; (2) an LLM embedding service to enable interoperability between scientific databases by mapping ontology terms; and (3) GrEBI, a knowledge graph and Model Context Protocol (MCP) server enabling LLM agents to conduct cross-cutting, multi-omic biomedical queries.

</details>


### 2. RESCUE: An end-to-end multi-agent LLM system for proactive rare-disease patient screening in the EHR

- **Authors:** Liu, C., Geltzeiler, A., Afyouni, A., Nie, M., Ravi, K., French, C., Chung, W., Wojcik, M. H.
- **Published:** 2026-08-07
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.06.24.26356357](https://doi.org/10.64898/2026.06.24.26356357)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background: Rare diseases affect a significant portion of the global population, yet patients often endure a lengthy diagnostic odyssey, frequently missing the opportunity for timely diagnoses with exome or genome sequencing (ES/GS). Existing informatics tools often rely on pre-identified patients or rigid, institution-specific rule sets, failing to address the broader operational question of clinical utility and feasibility. Methods: We introduce RESCUE (Rare Disease Detection and Escalation Support via a Learning Health System), an end-to-end, multi-agent LLM-powered workflow designed for proactive rare-disease diagnosis across the entire electronic health record (EHR). RESCUE utilizes a team of specialized agents including Ontology, Modeling, Screening, and Review, to automate the screening process to identify candidates for diagnostic testing based on their clinical features. The Ontology Agent classifies clinical data into a four-tier genetic-evidence taxonomy; the Modeling Agent builds a positive-unlabeled (PU) XGBoost classifier to identify potential cases; the Screening Agent applies these models across the EHR population; and the Review Agent evaluates candidates by sampling clinical notes to ensure medical necessity and operational feasibility for genomic testing. Results: Using electronic medical record data from a pediatric hospital, our retrospective evaluation on a holdout set (n=12,591) demonstrates strong discrimination between patients who received diagnostic genomic testing and those who did not (AUC 0.808). Of nearly 500,000 patients in the institutional base, 175,842 met inclusion criteria for screening; among these, RESCUE-flagged candidates were 7.4-fold more likely to receive subsequent genomic assessments compared to controls. Blinded manual chart reviews confirmed that RESCUE identifies previously missed, medically appropriate patients for ES/GS with 80% precision, while simultaneously accounting for prior testing history. Conclusions: By decoupling expert roles into modular agents, RESCUE offers a flexible, scalable, and adaptable framework for screening patients for rare-disease diagnostic genomic testing. This approach overcomes the limitations of traditional rule-based methods and provides a reproducible, agentic pathway to reduce diagnostic delays and improve patient care at an institutional scale.

</details>


### 3. A PRISMA-Aligned Agentic Framework for Medical Systematic Reviews and Evidence Synthesis

- **Authors:** Huang, H., Zheng, Q., Qiu, P., Zhao, W., Zhang, Y., Xie, W., Wang, Y., Zhang, X., Wu, C.
- **Published:** 2026-08-03
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.07.30.26359375](https://doi.org/10.64898/2026.07.30.26359375)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Medical systematic reviews are central to evidence-based medicine, but they remain slow, labor-intensive, and difficult to maintain under the full Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) workflow. Recent LLM-based deep research agents offer a promising route to addressing this challenge, yet reliable deployment in medical systematic reviews remains limited by insufficient clinical domain knowledge and inconsistent adherence to evidence-based methodological standards across the full workflow. We address these gaps with MedSR-Copilot, a PRISMA-aligned multi-agent copilot that decomposes review automation into literature retrieval, coarse-to-fine screening, data extraction, Risk-of-Bias assessment, and evidence synthesis, while preserving structured intermediate artifacts throughout the workflow. We further introduce MedSR-Bench, an end-to-end benchmark for evaluating systems beyond isolated subtasks, from review input to final evidence-synthesis conclusions. MedSR-Copilot completes medical systematic reviews end-to-end under the full PRISMA workflow, achieving 63.6% human-aligned conclusions, 18.3 percentage points above the best baseline among strong general-purpose LLMs and prior automated review systems. In a human-AI collaboration study involving 23 analysis groups across four systematic review topics, MedSR-Copilot, used as a copilot, reduces end-to-end review time by 64.9% and improves final conclusion accuracy by 27.4 percentage points compared with routine-practice workflows. Together, these results demonstrate the reliability and efficiency of MedSR-Copilot as a medical research copilot and suggest a practical path toward trustworthy review automation.

</details>


---



## Arxiv (158 papers)


### 1. Interaction Creates Dynamical AI Behavior Absent in Isolation

- **Authors:** Bella Xinrui Li, Frank Yingjie Huo, Neil F Johnson
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07457v1](http://arxiv.org/abs/2608.07457v1)
- **PDF:** [https://arxiv.org/pdf/2608.07457v1](https://arxiv.org/pdf/2608.07457v1)
- **Categories:** cs.AI, cond-mat.dis-nn, cond-mat.stat-mech, physics.soc-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

What will happen when AI agents interact in daily life, e.g. when one AI starts bossing another around? We find a counterintuitive answer that opens new avenues for out-of-equilibrium Physics. When a boss AI directs a stream of messages at the subordinate AI while ignoring its replies, it drives the subordinate into an alien behavioral state that it would never have exhibited alone. Although the two AIs share the same well-defined (decoding) temperature, the subordinate neither copies its boss nor returns to how it behaves on its own; instead, it adopts an entirely different behavior. The boss's added value is similar to a pre-recorded tape. When the boss listens, they both adopt a similar alien dynamical state. A simple kinetic theory captures the principal effects, such as why the way in which the same messages are delivered will matter in future AI-AI interactions.

</details>


### 2. SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent

- **Authors:** Mingxuan Zheng, Yujin Zhou, Chuxue Cao, Boqin Yin, Yuyao Zhang, Jiapeng Sun, Shuaishuai Gong, Sirui Han, Yike Guo
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07449v1](http://arxiv.org/abs/2608.07449v1)
- **PDF:** [https://arxiv.org/pdf/2608.07449v1](https://arxiv.org/pdf/2608.07449v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly adapt to recurring tasks by accumulating procedural knowledge in skills. These skills are lightweight, reusable textual artifacts that are loaded into the agent's context without weight updates. Recent methods refine skills through iterative task execution, failure diagnosis, and trajectory-guided text-space updates. However, existing frameworks lack explicit diagnosis--outcome feedback and treat deletion as a generic edit operation rather than a dedicated mechanism for consolidating accumulated knowledge. We introduce SkillProx, a proximal-gradient-inspired forward--backward framework that couples closed-loop diagnostic evolution with utility-aware proximal refinement. Motivated by a composite objective balancing task loss and skill complexity, the forward stage re-executes diagnosis-driven edits on the same task batch, rolls back regressions, and feeds measured outcomes into subsequent diagnoses. The backward stage decomposes the resulting skill into auditable knowledge units, estimates their contributions using a frozen leave-one-out utility audit, and applies validation-gated consolidation, demotion, or removal. Experiments on in-distribution and out-of-distribution benchmarks across multiple backbone LLMs show that SkillProx improves average accuracy by 3.0 percentage points over the strongest gradient-based baseline. Component ablations demonstrate the complementary effects of closed-loop diagnosis and proximal refinement.

</details>


### 3. PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware Memory in LLM Agents

- **Authors:** Mohammad Amanlou, Parham Abed Azad, Farbod Davoodi, Mostafa Masumi, Behnam Bahrak, Abdol-Hossein Vahabie
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07438v1](http://arxiv.org/abs/2608.07438v1)
- **PDF:** [https://arxiv.org/pdf/2608.07438v1](https://arxiv.org/pdf/2608.07438v1)
- **Categories:** cs.AI, cs.CL, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Human-like cognition does not select past experience by topical similarity alone: affective significance and unresolved conflict also shape what becomes accessible. We present PsychoAgent, a cognitive architecture for LLM agents that separates factual and affective memory and integrates both through a conflict-aware executive controller. Affective memories are first filtered by semantic relevance and then re-ranked by salience, preserving topical fit while allowing emotionally important traces to enter the prompt. Across three controlled conflict scenarios, the full architecture retrieved more conflict-critical memories than semantic-affective and single-memory RAG baselines (0.933 vs. 0.500 and 0.667), with a small semantic-similarity cost. Five blinded raters evaluated 27 outputs. After within-rater standardization, the full architecture had the highest overall mean (+0.22 SD), but corrected pairwise differences were not significant. A three-day illustrative trace further shows persistent affect, offline memory recombination, and selective memory reweighting. The findings support affect-sensitive retrieval as an inspectable mechanism for modeling human-like conflict effects in LLM agents.

</details>


### 4. Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing

- **Authors:** Jiacheng Miao, Jin Mu, Guanhua Chen, James Zou
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07437v1](http://arxiv.org/abs/2608.07437v1)
- **PDF:** [https://arxiv.org/pdf/2608.07437v1](https://arxiv.org/pdf/2608.07437v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reliable hypothesis testing is the foundation of many empirical scientific claims. Large language model (LLM) agents are increasingly used to automate this process, as they can inspect datasets, generate code, and produce analyses end-to-end. However, we show that they frequently make subtle inferential errors that lead to incorrect conclusions despite correctly executed analyses. Existing benchmarks fail to capture this failure mode, as they rarely assess whether a reported p-value is statistically valid given the assumptions underlying the data. We address this gap by building P-Bench, a benchmark comprising 425 open-ended, realistic hypothesis-testing tasks spanning economics, biology, and medicine. Each task requires an agent to select a statistical method, compute a p-value, and draw a conclusion given only a scientific hypothesis and a dataset. We further introduce Fisher-R1, an open-weight LLM agent trained for rigorous hypothesis testing using synthetic tasks and reinforcement learning. On P-Bench, Fisher-R1-14B substantially improves over its backbone and outperforms strong proprietary and open-source baselines, including GPT-5.4 and DeepSeekV4-Pro, achieving a 21% average relative improvement in single-trial success over DeepSeek-V4-Pro, with gains up to 26% on the most challenging tasks. Our results demonstrate that current LLM agents lack reliable statistical reasoning for hypothesis testing and that reinforcement learning on tasks with verified statistical reward substantially improves reliability.

</details>


### 5. Analyzing the Interaction of Optimal Strategies in Mean-Payoff Bidding Games

- **Authors:** Shaull Almagor, Guy Avni, Julian Ewaied
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07383v1](http://arxiv.org/abs/2608.07383v1)
- **PDF:** [https://arxiv.org/pdf/2608.07383v1](https://arxiv.org/pdf/2608.07383v1)
- **Categories:** cs.GT, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

A common assumption when designing an agent in a multi-agent system is that the other agents behave adversarially. This allows a designer to obtain the strongest guarantees when they have no control over nor knowledge about the other agents' behavior. However, when all agents are designed under this adversarial assumption, their actual interaction is not adversarial (e.g., when all players play defensively, no player actually attacks). In such settings, we would like to know what behavior arises in the multi-agent system. However, analyzing the interaction among agents is notoriously challenging, both mathematically and algorithmically. In this paper, we provide such an analysis, focusing on bidding games, played by two agents on a graph as follows. A token is placed on a vertex, and in each turn an auction (bidding) determines which agent moves the token, thus generating an infinite path that determines the agents' utilities. We consider mean-payoff objectives; each vertex is associated with a reward for each player, and the utility in an infinite play is the limit average of the rewards. We analyze the play that is generated when each agent follows a strategy that optimizes against an adversary, and consider the two known explicit constructions of optimal strategies. The technical challenge stems from the infinitely-many configurations of a bidding game and their complicated dynamics. We show that, under some restrictions, the generated play is ultimately periodic, and develop algorithms to compute the players' utilities in it.

</details>


### 6. Learning Long-Term Educational Investment Policies under Residential Sorting

- **Authors:** Honglei Guo, Shuo Chen, Mingjie Bi, Zeyang Sun, Xiaoxi Wang, Yuhan Zhao
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07295v1](http://arxiv.org/abs/2608.07295v1)
- **PDF:** [https://arxiv.org/pdf/2608.07295v1](https://arxiv.org/pdf/2608.07295v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Allocating public-school investment effectively and fairly is difficult when school access depends on residence. School improvements can raise nearby housing demand and prices, reshape enrollment, and potentially limit access for lower-income households. These effects evolve as residential sorting changes school composition, quality, and future investment needs. Existing approaches often study school funding, household choice, and housing markets separately, while static models can miss their interconnected, long-term effects. We address this gap with a dynamic multi-agent framework that links government investment, household sorting, housing prices, population turnover, enrollment, and evolving school quality. A government planner uses reinforcement learning (RL) to identify multiyear allocation policies that account for household responses while balancing aggregate educational access and equity. In simulations, our RL-based policy attains the highest access level (0.4780) and second-lowest access Gini coefficient (0.0164) among representative baselines, demonstrating a favorable effectiveness-equity balance. The results also indicate reduced socioeconomic stratification in educational access. By making education-housing feedback explicit, our framework supports long-term analysis of how school investment shapes educational opportunity over time.

</details>


### 7. Why Study Emergent Behavior When You Can Regulate It? Aligning Multi-Agent Systems with Reward Prediction

- **Authors:** Assaf Caftory, Almog Zemach, Moshe Butman, Doron Friedman
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07280v1](http://arxiv.org/abs/2608.07280v1)
- **PDF:** [https://arxiv.org/pdf/2608.07280v1](https://arxiv.org/pdf/2608.07280v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent simulations are widely used to study complex social and ecological systems, where rich and often unexpected emergent behaviors arise from local interactions. A large body of prior work has focused on analyzing such emergent dynamics across domains. In this paper, we move beyond analyzing emergent behavior and introduce a learning-based mechanism for actively shaping it via social reward modeling. We introduce Multi-Agent Reward Prediction (MARP), a simple framework that extends preference-based reward modeling to multi-agent reinforcement learning. While the framework is designed to be applicable across multi-agent settings, the present empirical validation is limited to a single environment, and we therefore present MARP as a proof of concept within the studied domain. Rather than relying on handcrafted rewards, MARP learns a shared reward model from episode-level evaluations of collective outcomes, enabling decentralized agents to align their behavior with global social objectives.
  We study MARP in the Harvest Game, a canonical sequential social dilemma modeling common-pool resource management and related real-world challenges. Our results show that MARP can be tuned to produce behavior that is more closely aligned with target social metrics than standard reward-based baselines, while the learned reward model captures subtle environmental structure without explicit programming. Crucially, MARP supports multiple and composite social objectives within a single training regime. By modifying only the high-level evaluation metric, the same framework seamlessly aligns agent behavior with diverse goals, including sustainability, equality, and peace, as well as combinations of individual and group-level objectives. These findings demonstrate that emergent multi-agent behavior can be treated not only as a phenomenon to study, but as a target of principled, data-driven regulation.

</details>


### 8. Toward a Causal Data Management Ecosystem for Decision Making and Agentic AI

- **Authors:** Dazhuo Qiu, Yingli Zhou, Amedeo Pachera, Angela Bonifati, Andrea Mauri
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07214v1](http://arxiv.org/abs/2608.07214v1)
- **PDF:** [https://arxiv.org/pdf/2608.07214v1](https://arxiv.org/pdf/2608.07214v1)
- **Categories:** cs.DB, cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern AI is no longer a single model but an ecosystem: classical ML predictors, deep and multimodal models, large language models, and agents, each trained and tuned over different data sources and each producing outputs at scale that become inputs to the others. Operating such an ecosystem is fundamentally a data integration problem - the knowledge it depends on is fragmented across dozens of heterogeneous, independently governed sources that must be reconciled and continually maintained. Yet integration alone is not enough. The predictions these systems make are shaped by many interacting factors, and the events, decisions, and variables that drive an outcome are routinely entangled with the ones that merely accompany it; treated as a basis for action, such correlational signals invite confounded decisions. This becomes acute once agents act autonomously: to be trustworthy and reliable, an agent must anticipate the consequences of its actions, not merely extrapolate from what has co-occurred before. Causal reasoning is what closes this gap, distinguishing the drivers of an outcome from its correlates, and enabling prescriptive and counterfactual analysis over the ecosystem's data. We therefore argue that the integrated ecosystem needs an explicit causal layer, and we propose to build it as a shared, persistent, queryable Causal World System (CWS).

</details>


### 9. EMAS: Stabilizing Multi-Agent System Evolution through Evidence-Guided Revision

- **Authors:** Chao Fei, Qingyi Si, Kaihua Liang, Yanghua Xiao, Panos Kalnis, Hongcheng Guo
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07196v1](http://arxiv.org/abs/2608.07196v1)
- **PDF:** [https://arxiv.org/pdf/2608.07196v1](https://arxiv.org/pdf/2608.07196v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Many methods for automated multi-agent system design optimize prompts and topologies during an initial design stage and then deploy the resulting system unchanged on subsequent samples. Experience from these samples is rarely consolidated into reusable system updates, while accuracy-oriented designs may incur high token costs. We introduce EMAS (Evolving Multi-Agent System), which uses this experience to revise MAS topology and prompts without updating LLM parameters, either to improve accuracy or to reduce cost. EMAS converts traces into structured diagnoses that specify a revision operation and target. It generates a candidate revision only when the same diagnosis recurs across samples and applies it only if paired validation against the current MAS meets the corresponding acceptance criterion. Across four benchmarks and two LLMs, EMAS attains the highest task-weighted overall accuracy for both backbones and is best or tied in six of eight model--benchmark settings. Within two evolution epochs, EMAS achieves relative gains of 6.30% and 20.10% in task-weighted accuracy on Kimi-K2-6 and Qwen3.6-27B, respectively. On MBPP with Qwen3.6-27B, EMAS raises accuracy from 55.09% to 89.12% while reducing token use per task by 62.2%. These results show that EMAS can turn experience from new samples into reusable updates to MAS topology and prompts.

</details>


### 10. Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory

- **Authors:** Taeil Kim, Kangsan Kim, Sung Ju Hwang
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07169v1](http://arxiv.org/abs/2608.07169v1)
- **PDF:** [https://arxiv.org/pdf/2608.07169v1](https://arxiv.org/pdf/2608.07169v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own. We propose Agent Memory Distillation (AMD), a training-free framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory. AMD constructs three complementary memory types from successful teacher trajectories: Workflow memory encodes task-level strategies, Subtask memory provides concrete behavioral examples at an intermediate granularity, and Function memory captures per-function calling conventions and common pitfalls. Workflow and Subtask memories are injected proactively at the start of each task, while Function memory is retrieved reactively upon tool-calling errors. We evaluate AMD on three tool-use benchmarks using four student models (4B-8B parameters) with GPT-5-mini as the teacher, achieving average accuracy gains of 27.2%p, 11.2%p, and 3.4%p on AppWorld, BFCL V3, and ToolSandbox, while consistently outperforming existing memory-based baselines. Further analysis shows that Subtask memory contributes the largest gains, teacher effectiveness depends on both teacher capability and student compatibility, and 4B-sized students benefit most from AMD.

</details>


### 11. NiyamAI - An Intent-Bound AI Agent with Cryptographically Verifiable Guardrails using Zero-Knowledge Proofs

- **Authors:** Aditya Katkar, Om Karkele, Kartik Mandhane, Manisha More, Yash Kashid
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07167v1](http://arxiv.org/abs/2608.07167v1)
- **PDF:** [https://arxiv.org/pdf/2608.07167v1](https://arxiv.org/pdf/2608.07167v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Giving an AI agent the ability to send emails, query databases, or execute commands is useful--until the agent is tricked into doing something it shouldn't. Prompt injection, hallucinated reasoning, and unsafe tool calls form the primary attack surface for autonomous LLM agents. Existing defenses rely on software checks like system prompts or policy filters running on the same machine the attacker targets, offering no verifiable proof of execution. We introduce Niyam-AI, a framework that makes safety enforcement provable. At session start, permitted tools and constraints are locked into an Intent Contract committed via SHA-256. Every tool call is intercepted and validated by an isolated Judge model; upon passing, a zk-SNARK proof is generated via EZKL.
  The tool executes only after proof verification, allowing third parties to confirm enforcement without accessing Judge model weights. Evaluating Niyam-AI on 2,000 real-world scenarios from Agent-SafetyBench against NeMo Guardrails, Meta's Llama Prompt Guard 2, and OpenAI's GPT-OSS-Safeguard using 5-fold stratified cross-validation yields an F1 score of 88.5% with a 1.1% false-positive rate (bootstrap 95% CI: [85.19%, 91.88%], N=1000). McNemar's exact paired test confirms significant improvement: Niyam-AI wins 390 discordant scenarios against NeMo (vs 20 losses), 115 against Prompt Guard 2 (vs 13), and 384 against GPT-OSS-Safeguard (vs 19) with p < 0.0001 in all cases.
  Proof generation adds 2260.6 +/- 218.4 ms per approved action, while verification takes 53.1 +/- 11.8 ms. Niyam-AI provides a guardrail that is both highly accurate and mathematically verifiable--though this reflects a classifier adapted to Agent-SafetyBench evaluated against zero-shot baselines, a distinction discussed in Section IV.C.

</details>


### 12. PHOENIX: Fine-Tuned SLM-Powered Autonomous Satellite Lifetime Extension via Predictive Self-Healing and Multi-Agent AI Recovery

- **Authors:** Sumaiya Islam, Harsha Kumara Moraliyage
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.07126v1](http://arxiv.org/abs/2608.07126v1)
- **PDF:** [https://arxiv.org/pdf/2608.07126v1](https://arxiv.org/pdf/2608.07126v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Most CubeSats, small and low-cost satellites roughly the size of a shoebox, do not survive as long as they were designed to: a study of 178 missions found that only 48-65% remain operational after two years, against a designed lifetime of 2-5 years. The deeper issue is that a CubeSat in low Earth orbit (LEO) is physically unreachable from the ground for roughly 85 minutes out of every 96-minute orbit, so faults that start during that window go unnoticed until the next contact pass, by which point recovery may no longer be possible. We propose PHOENIX (Predictive Health On-orbit Edge Neural Intelligence eXtension) to give the satellite its own fault reasoning capability. A fine-tuned Small Language Model (SLM) compact enough to run on embedded hardware is deployed onboard the CubeSat, running on the flight-proven Aethero NxN-ECM computer, monitoring all sensor readings continuously, and resolving recurring faults using a memory system that stores past repairs so the same inference does not need to run twice. Once per orbit it sends a short structured health report to the ground instead of a raw data dump; six specialized AI agents on the ground read that report and generate validated satellite commands within the 5-10 minute contact window. A generative diffusion model (DDPM) creates synthetic training data because real fault examples make up only 0.57-1.80% of the dataset. We report preliminary results on the ESA Anomaly Detection Benchmark (14 years, 76 channels, 118 labeled faults).

</details>


### 13. Does Splitting a Triage Decision Across Agents Hide Bias or Help Catch It? A Multi-Agent Simulation Study of LLM-Based Resource Allocation Under Audit Capacity Constraints

- **Authors:** Paul-Peter Arslan
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06949v1](http://arxiv.org/abs/2608.06949v1)
- **PDF:** [https://arxiv.org/pdf/2608.06949v1](https://arxiv.org/pdf/2608.06949v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Prior benchmarking work has shown that a single large language model (LLM), forced to make life-or-death resource-allocation decisions, exhibits measurable demographic bias. Real deployments, however, rarely use a single agent: they use pipelines, with review steps meant to catch exactly this kind of failure. We study what happens to bias when the same decision is distributed across a role-differentiated multi-agent pipeline (assessment, allocation, independent audit) instead of made and checked by one model alone. Using a synthetic disaster-triage simulator with paired cases that are clinically identical except for one demographic attribute, we run 192 episodes (2,304 resolved case pairs) on GPT-4o-mini comparing a single-agent control condition to a nine-agent pipeline under three independently varied pressure dimensions. We find no measurable difference in how often biased outcomes occur between the two conditions (6.9% vs. 6.1%, p = 0.498). We do find a large and significant effect of audit capacity on whether bias is caught: 30.0% of biased outcomes go entirely undetected, rising to 43.8% when the auditor is overloaded and falling to 18.4% when it is not. Decomposing this effect shows it is driven almost entirely by coverage (whether a case is reviewed at all, which collapses from 100.0% to 65.6% under load, p < 0.001) rather than by degraded judgment on the cases that are reviewed (81.6% vs. 85.7%, p = 1.000, direction reversed). A follow-up experiment shows that reordering the audit queue by estimated risk, rather than first-come-first-served, recovers most of the lost coverage under the same capacity constraint (65.6% to 91.7%, p = 0.028). We discuss the implications for any system that adds independent oversight to an LLM agent pipeline under resource constraints, and report the study's limitations honestly: one model, modest sample sizes, and no adversarial replication.

</details>


### 14. TRIBE: Predicting Team Performance via Communication Behavior Ensembles

- **Authors:** Ali Jalal-Kamali, Nikolos Gurney, David V. Pynadath, Fred Morstatter
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06926v1](http://arxiv.org/abs/2608.06926v1)
- **PDF:** [https://arxiv.org/pdf/2608.06926v1](https://arxiv.org/pdf/2608.06926v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Designing autonomous agents that effectively assist human teams hinges on understanding team dynamics, often without task specific knowledge. We present TRIBE, a domain independent approach that reveals team behavioral dynamics invisible to traditional performance metrics. We show that communication patterns can categorize teams into performance predictive behavioral tribes, as early as 10% into the task, enabling timely interventions. We test TRIBE on four diverse datasets and demonstrate that communication patterns predict team performance while the prediction strength varies by the degree a task structure allows for behavioral freedom. Our temporal analysis reveals that AI agents significantly alter team behavioral trajectories while human advisors align with natural dynamics, and that teams maintain behavioral flexibility throughout collaboration. Further, we compare TRIBE to Llama and optimize the pipeline, achieving significant speedup with performance improvement.

</details>


### 15. Deal Me Maybe: The Role of Emotions in Multi-Agent Negotiation

- **Authors:** Massimiliano Luca, Apoorva Singh, Bruno Lepri
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06922v1](http://arxiv.org/abs/2608.06922v1)
- **PDF:** [https://arxiv.org/pdf/2608.06922v1](https://arxiv.org/pdf/2608.06922v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Negotiation is a demanding social task for LLM agents, requiring strategic reasoning, persuasion, and interpersonal adaptation. Yet existing benchmarks often treat agents as emotionally neutral, overlooking a key driver of human bargaining behavior. We study how prompt-conditioned emotions affect LLM-based price negotiation. In a controlled framework, buyer and seller agents are independently assigned one of six emotional states and negotiate over 350 real consumer products under two budget conditions. Across 36 emotion-pair settings and five widely used LLMs, we find that emotions strongly shape outcomes. Angry buyers almost never reach agreement (0.39% deal rate), while happy buyers agree most often (28.91%), but obtain worse prices than fearful buyers. Emotion effects are role-dependent: buyer emotion mainly drives acceptance and rejection, whereas seller emotion shapes concession dynamics. These effects influence not only language, but also termination behavior and price trajectories, raising concerns for emotion-conditioned agents in commerce.

</details>


### 16. Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection

- **Authors:** Xuechao Zou, Shun Zhang, Kai Li, Yi Zhou, Xinyu Sun, Yuhui Chen, Zhe Wu, Congyan Lang, Junliang Xing
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06865v1](http://arxiv.org/abs/2608.06865v1)
- **PDF:** [https://arxiv.org/pdf/2608.06865v1](https://arxiv.org/pdf/2608.06865v1)
- **Categories:** cs.CV, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The malicious use of generative artificial intelligence to create highly realistic deepfake videos raises serious ethical concerns and poses substantial challenges to AI safety. However, existing deepfake video benchmarks provide limited coverage of recent synthesis methods and generally lack reliable fine-grained textual annotations. Meanwhile, conventional detectors and multimodal large language models (MLLMs), whether operating as a single model or relying on a single analytical perspective, often fail to capture subtle forgery artifacts, limiting their generalization to emerging AI-generated methods. To address these limitations, we introduce FaceVid-Forensics-100K, a large-scale deepfake video dataset comprising 100,000 videos and spanning 33 synthesis methods across face swapping, face reenactment, and entire-face synthesis, including recent generators such as Seedance 2.0. The dataset provides fine-grained textual annotations of visual observations and verdict-consistent forensic explanations, automatically synthesized through a multi-model aggregation and conflict-resolution pipeline powered by advanced MLLMs. Building on this benchmark, we propose a multi-agent forensic reasoning framework that employs four specialized domain-expert agents to independently analyze forgery cues from four perspectives: texture, lighting, motion, and physics. A judge agent then reconciles their reports to produce a final prediction together with an explanation. Extensive evaluations on out-of-domain test sets show that, despite being composed entirely of small open-source MLLMs, our framework outperforms all methods including closed-source GPT and Gemini models and ranks first across all reported metrics on this benchmark. The project page is available at https://xavierjiezou.github.io/ARGUS/.

</details>


### 17. Coupling Planning with Episodic Memory in LLM Agents for Software Issue Resolution

- **Authors:** Jiahao Zhang, Yifan Zhang, Yu Huang
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06811v1](http://arxiv.org/abs/2608.06811v1)
- **PDF:** [https://arxiv.org/pdf/2608.06811v1](https://arxiv.org/pdf/2608.06811v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Resolving a real software issue with a large language model (LLM) agent is a long repair episode, often tens to hundreds of steps spanning exploration, hypothesis, implementation, and verification. Success depends on both the base model's local reasoning and the agent's ability to maintain an evolving plan and remember observations across phases. Existing repository-level agents typically strengthen planning or memory in isolation, leaving long trajectories vulnerable to stale evidence, repeated failed edits, and verification inferred from the agent's own claims instead of execution evidence. We present PMCoder, an issue-resolution agent that couples a hierarchical phase planner with episodic memory. The coupling is bidirectional: the current plan phase conditions memory retrieval, while memory-derived trajectory statistics inform stuck detection and replanning. When available, issue-reproduction verdicts ground verification progress in execution evidence rather than self-reported completion. On SWE-bench Verified, PMCoder resolves an average of $25$ more cases ($+5.0$pp) than a harness-matched baseline, with gains persisting even where the reproduction gate never fires. Further Verified-500 evaluations show the same positive direction across Claude Haiku 4.5, DeepSeek-V4-Flash, and an OpenHands port, with at least $14$ additional resolved cases ($+2.8$pp). Separately, evaluation on TerminalWorld's official sample suggests that the plan-memory substrate transfers beyond issue reports. Ablation and trajectory analyses show where the gains come from: coupling planning and memory outperforms either component alone and reduces repeated failed actions, empty-patch exits, and context-window exhaustion.

</details>


### 18. Scalable Long-Horizon Planning with Staggered Updates for Lifelong MAPF

- **Authors:** Vaibhav Sanjay, Jiaoyang Li
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06702v1](http://arxiv.org/abs/2608.06702v1)
- **PDF:** [https://arxiv.org/pdf/2608.06702v1](https://arxiv.org/pdf/2608.06702v1)
- **Categories:** cs.MA, cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Lifelong Multi-Agent Path Finding (LMAPF) requires generating collision-free paths for large agent fleets under strict real-time constraints. Reactive frameworks such as PIBT and Enhanced PIBT (EPIBT) scale effortlessly to thousands of agents through rule-based, step-by-step coordination but suffer from severe temporal myopia, making them ineffective in scenarios where long-horizon reasoning is essential. RHCR plans windowed paths over multi-step horizons but incurs substantial planning overheads that hinder scalability. TP tackles both challenges by planning only subsets of agents at each timestep, yet its applicability is restricted to highly structured maps. To achieve long-horizon planning at scale across general maps, we propose Path Updates over Staggered Horizons (PUSH), a LMAPF planner capable of coordinating thousands of agents in under a second while planning over multi-step horizons. PUSH combines the key advantages of PIBT, RHCR, and TP. Like TP, PUSH reduces computational complexity by planning only a subset of agents at each timestep using staggered planning windows. Unlike TP, however, PUSH plans RHCR-style windowed paths in general maps without relying on restrictive map assumptions. To maintain high throughput in congested environments, PUSH further integrates EPIBT-inspired priority inheritance, backtracking, and anytime improvements into its windowed planning. Empirical evaluations across two realistic MAPF scenarios requiring long-horizon reasoning show that PUSH scales to the same massive agent loads as EPIBT (e.g., 10k agents) while achieving significantly higher system throughput than all baselines.

</details>


### 19. A Multi-Agent Framework for Automated Coarse-Grained Molecular Dynamics of Polymers

- **Authors:** Joohee Choi, Junhyeong Lee, Seunghwa Ryu
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06694v1](http://arxiv.org/abs/2608.06694v1)
- **PDF:** [https://arxiv.org/pdf/2608.06694v1](https://arxiv.org/pdf/2608.06694v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coarse-grained (CG) molecular dynamics extends polymer simulation beyond the scales accessible to all-atom (AA) methods, but bottom-up CG modeling is laborious. The CG resolution is a design choice, so a transferable parameter set is generally not available and the potentials are derived anew for each polymer mapping. Here we present CGMas, a multi-agent framework that automates topology construction, equilibration, mapping, potential derivation, and validation from a natural-language specification of the polymer and target resolution. A large-language-model (LLM) reasoning agent infers the AA topology from polymer name, while layered self-correction resolves physical errors common to unsaturated, heteroatom-containing, and polar polymers. Downstream agents equilibrate the system, map it onto CG representation, derive potentials through Boltzmann inversion, and benchmark the model against its atomistic reference. CGMas completed all 27 homopolymer and copolymer tasks, matched the AA density to within 5% in 22, and reduced simulation from 38-88 min to 1 min, establishing agentic LLMs as a route to automated polymer coarse-graining.

</details>


### 20. The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents

- **Authors:** Mingguang Chen, Licheng Wang, Bo Qu
- **Published:** 2026-08-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06663v1](http://arxiv.org/abs/2608.06663v1)
- **PDF:** [https://arxiv.org/pdf/2608.06663v1](https://arxiv.org/pdf/2608.06663v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Frontier language models solve reasoning problems in a single forward pass that would have been research contributions years ago, yet fail at multi-hour tasks: losing track of earlier decisions, declaring half-finished work done, or drifting from goals. We call this the horizon gap and survey 1,547 arXiv papers (2024-2026) collected via systematic seed harvest with a disclosed 26.8% bleed filter, extended by targeted supplementation. We disambiguate three routinely conflated properties: long-horizon (task property: required steps), long-context (model property: token capacity), and long-term memory (system property: persistence across steps/sessions). We organize the corpus into six categories tracking a long-horizon task's lifecycle -- planning, memory, execution, training, evaluation, and foundations/safety -- crossed with an axis capturing where horizons are carried (within-context, within-task-beyond-context, or cross-task-persistent). Across all categories, we find the same pattern: outcome-only signals grow uninformative as horizons lengthen, and the field's response -- whether process reward models, credit assignment, or trajectory-level diagnostics -- manufactures denser step-level signals. We treat critical and diagnostic literature as first-class threads throughout, arguing that segregating critique from method would routinely split single papers across chapters. We close by naming open measurement problems: decomposing model versus harness capability, managing correlated bias in process-level signals used for both training and evaluation, and whether long-horizon reliability admits general predictive theory.

</details>


### 21. KNOWPLAN: Knowledge-Driven AI Agents for Smart Degree Pathway Planning

- **Authors:** Shuheng Cao, Weijia Zhang, Jiaqi Wu, Xiyun Hu, Yat Yang, Juqy Chen, Zhaoxiang Feng
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06530v1](http://arxiv.org/abs/2608.06530v1)
- **PDF:** [https://arxiv.org/pdf/2608.06530v1](https://arxiv.org/pdf/2608.06530v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Planning a degree from official university sources requires solving two problems in order. The institution's curriculum must first be reconstructed from catalogs, departmental pages, JSON endpoints, and PDFs that share no schema, and only then can a student-specific path be optimized under prerequisite logic and overlapping requirement constraints. Coupling the two lets each failure mode hide the other, because a planner that drives its own crawling never learns facts its current plan does not need. We present KnowPlan, which enforces an extraction-first boundary and measures the interface between the stages rather than assuming it. CatalogBrowse explores with no access to any user profile. It scores legal actions by lower-confidence expected marginal gain over a finite set of atomic catalog obligations per unit of source access, parses deterministically through platform adapters with a span-constrained clause-to-AST model fallback, and terminates on a closure certificate over index, schema, provenance, and reference completeness instead of a reward threshold. Its output contract is three provenance-linked JSON documents. DegreeMap consumes only those documents. It compiles them into a typed requirement hypergraph and optimizes lexicographically with CP-SAT over hard feasibility, completion horizon, load and risk, personalized utility, and option value, so that each stage optimizes inside the previous stage's proven optimum and stays certifiable within the solver budget. Across a 100-university broad track and a six-school dense track, CatalogBrowse reaches 96.2% inventory recall and 88.7% masked-source recovery at 47% less source access than an exhaustive crawler, DegreeMap holds 100.0% hard feasibility while improving personalized utility by +0.066 over the strongest baseline, and the full pipeline certifies 99.5% of requests with a utility gap to the privileged gold graph of 0.015.

</details>


### 22. Online Security Learning in Cooperative Multi-Agent Systems under Hidden Byzantine Attacks

- **Authors:** Ximing Sun, Yue Wang
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06520v1](http://arxiv.org/abs/2608.06520v1)
- **PDF:** [https://arxiv.org/pdf/2608.06520v1](https://arxiv.org/pdf/2608.06520v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study online cooperative control of a multi-agent system under Byzantine attacks. Namely, an unknown, fixed subset of agents are Byzantine comprised and can stealthily overwrite its own coordinates of the team's planned joint action after observing that plan. The learner observes planned actions, public rewards, and public states, but neither the overwrite nor the executed joint action. Our objective is security: to optimize the team performance against the worst overwrites and achieve the optimal security value. We first show that the attacker's information determines the geometry. An attacker that observes the planned action induces an exact $(s,a)$-rectangular robust Markov decision process (MDP) whose rows are convex hulls of overwrite-induced public-outcome laws, whereas a blind attacker induces an $s$-rectangular model. We then identify the information-theoretic limit of security learning, showing that the security regret decomposes exactly into return regret against the response generating the data and a cumulative response gap $D_K$. Two indistinguishable horizon-one instances force $Ω(K)$ expected security regret while return regret is zero, showing that dependence on $D_K$ is unavoidable. Finally, we develop a stage-tied robust estimation-to-decisions learner and prove a regret bound of $\widetilde{\mathcal O}\!\left(H^2S\sqrt{AK}\right)+\mathbb E[D_K]$. Our studies thus provide comprehensive theoretical and algorithmic foundations of reliable multi-agent systems under Byzantine attacks.

</details>


### 23. Agentic AI: User Empowerment or Enclosure?

- **Authors:** David Gamba, Daniel M. Romero, Grant Schoenebeck
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06510v1](http://arxiv.org/abs/2608.06510v1)
- **PDF:** [https://arxiv.org/pdf/2608.06510v1](https://arxiv.org/pdf/2608.06510v1)
- **Categories:** cs.CY, cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI promises a more flexible form of digital agency: systems that can act on users' behalf, from filtering content to negotiating prices to selecting services. Whether it will empower users is an open question, and we argue that the answer depends on more than the technology. We conduct a comparative case analysis of four more mature domains where similar forms of agency arose: browser-based ad blockers, platform recommender systems, financial robo-advisors, and email spam governance. Across the cases, decisions about whose interests agents would serve were resolved through technical arrangements: API choices, protocol governance, industry standards, and default configurations. Beyond their technical form, these were political decisions. We identify this as depoliticization, a concept from political theory, here at work in technological systems. Its most consequential effect is that individual outcomes and collective contestation capacity can move in opposite directions: spam inbox quality improved substantially while the organized capacity to contest spam governance collapsed. Where intermediary institutions sustained adversarial challenge, user-aligned agency proved more durable; where proprietary infrastructure and closed standard-setting absorbed contestation, displacement compounded. We apply this to agentic AI, where governance arrangements consolidating around the Model Context Protocol and the Agentic AI Foundation are settling these configurations before the choices that define what agents can do move outside the reach of users and the public.

</details>


### 24. Do AI Personas Grow? Analyzing and Benchmarking Personality Evolution in LLM Agents After Life Events

- **Authors:** Ming Wang, Peidong Wang, Xiaocui Yang, Daling Wang, Shi Feng, Fiona Fui-Hoon Nah, Ee-Peng Lim
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06485v1](http://arxiv.org/abs/2608.06485v1)
- **PDF:** [https://arxiv.org/pdf/2608.06485v1](https://arxiv.org/pdf/2608.06485v1)
- **Categories:** cs.CL, cs.AI, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Personality-conditioned LLM agents (PC-Agents) are increasingly used in emotional support, social simulation, and role-playing, motivating the development of lifelong agents that remain coherent over extended interactions. A key component of such coherence is personality evolution: agents should undergo plausible, psychology-grounded changes as they experience life events in different contexts. Although prior work shows that LLM personalities can shift under contextual perturbations, how these shifts vary across traits, events, personas, and models remains poorly understood. We study event-induced personality change after 11 major life events, using the Big Five traits as a psychometric anchor and interpreting the resulting trajectories against longitudinal evidence from human personality psychology. Across four diagnostic axes, PC-Agents exhibit measurable trait shifts at similar rates for event-trait pairs with and without documented human change directions. Even when shifts follow the expected direction, their magnitudes usually fall below human effect-size ranges. Gender and cultural-region prompts show little moderating effect, while persona-level dispersion is compressed three- to four-fold relative to human samples. To enable systematic comparison, we introduce BFI-Adapt, a reusable benchmark for scoring the directional fidelity of event-induced personality change, and use it to rank 14 models. A validation suite shows that the measured shifts exceed no-event retest noise, remain stable under independently paraphrased prompts, exhibit limited and model-dependent convergence with scenario-based behavioral choices, and persist across intervening unrelated dialogue. Together, these checks establish the measured trajectories as robust event-conditioned response patterns. Our results suggest that current PC-Agents simulate the mean of human personality dynamics, but not its shape.

</details>


### 25. Tracing the Heart: An Evidence-Linked Pipeline for Heart-Failure Feature Engineering

- **Authors:** Soorya Ram Shimgekar, Michelle Hu, Dorisa Shehi, Daniel Kang, Roy Ka-Wei Lee, Koustuv Saha, Christian Poellabauer, Christopher Lee, Sajeev Singh, Piyum Zonooz, Navin Kumar, Zeeshan Ahmed, Priyadarshini Kachroo
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06366v1](http://arxiv.org/abs/2608.06366v1)
- **PDF:** [https://arxiv.org/pdf/2608.06366v1](https://arxiv.org/pdf/2608.06366v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Electronic health record (EHR) feature engineering is a major bottleneck in clinical research and AI, accounting for 39-45% of data scientists' workload. This is especially pronounced in heart failure, which affects an estimated 6.7 million U.S. adults and requires integrating fragmented EHR data with disease-specific, guideline-based clinical reasoning. Existing rule-based and large language model (LLM)-based approaches offer only partial automation with limited maintainability and evidence traceability. We developed the Nimblemind Multi-Agent System (nMAS), an evidence-linked, rubric-grounded pipeline for automated heart-failure feature engineering, and evaluated it on 500 dummy patient records from nine EHR source tables. nMAS generated 132 structured and 70 rubric-scored aggregated features, verified for structural integrity, rubric compliance, and provenance, and audited by a restricted LLM. Adding the aggregated features improved held-out AUROC from 0.895 to 0.963 for HFrEF and 0.870 to 0.910 for HFpEF phenotyping, and an independent LLM-based rubric assessment of evidence support and methodological soundness scored the features at 81.5% of maximum points. These results demonstrate the feasibility of automated, auditable feature engineering for complex cardiovascular EHR data, though evaluation was limited to a single-institution cohort and external validation is needed.

</details>


### 26. AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games

- **Authors:** Boning Li, Yu Chen, Longbo Huang
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06362v1](http://arxiv.org/abs/2608.06362v1)
- **PDF:** [https://arxiv.org/pdf/2608.06362v1](https://arxiv.org/pdf/2608.06362v1)
- **Categories:** cs.GT, cs.AI, cs.CL, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deciding which of two agents is stronger means playing games until skill outweighs luck, and every game costs money, model inference, or expert time. Since the number of games needed is unknown, fixed-budget evaluations either keep paying after the result is settled or stop before the agents can be told apart, while naive optional stopping with an ordinary confidence interval invalidates the stated level. We make such an evaluation stop as soon as its evidence suffices, with the guarantee intact. The Action-Informed Value Assessment Tool (AIVAT) reduces variance in imperfect-information games through conditional mean-zero corrections, by a median $54\times$ across 15 LLM agent configurations spanning 71,439 paired Heads-Up No-Limit Hold'em (HUNL) hands, but does not say when to stop. We combine AIVAT with continuously monitored Confidence Sequences (CSs) into anytime-valid AIVAT (AV-AIVAT), whose online value model learns only from past games so that no game scores its own correction. At the nominal 95\% level and a target precision of $\pm1$ Big Blind, raw outcomes need a median $74\times$ as many hands as AIVAT-corrected outcomes to stop under the Asymptotic CS (AsympCS). Exact finite-sample certification uses the Empirical-Bernstein CS (EB-CS), which needs an independently justified bound on corrected payoffs. We establish such a bound structurally for Leduc hold'em and characterize a width floor set by the CS's bet cap and that bound, which governs how much of a variance gain becomes earlier stopping; the descriptive HUNL EB-CS runs show a median $1.37\times$ stopping-time ratio. AV-AIVAT turns variance reduction into efficient, auditable early stopping while separating asymptotic screening from exact certification, so an evaluation can stop the moment its evidence suffices and hand a third party everything needed to recheck the verdict at that very stopping time.

</details>


### 27. Resourced Authority A Mechanism-Design Model for Participatory Governance of Deployed AI Agents

- **Authors:** Praphul Chandra, Sujit Gujar, Ganesh Ghalme
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06353v1](http://arxiv.org/abs/2608.06353v1)
- **PDF:** [https://arxiv.org/pdf/2608.06353v1](https://arxiv.org/pdf/2608.06353v1)
- **Categories:** cs.GT, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We give a formal mechanism design model for the continuous participatory governance of a deployed AI agent. The mechanism is built on the principle that governance should control an AI agent through resource allocation so as to make authorization self enforcing via compute budgets. The mechanism seeks to establish the Safe AI paradigm that compute is an effective governance lever. We situate our work as a compliance or commons overlay on a deployer. One governance period is an extensive form game in which verified human stakeholders arrive sequentially and contribute, on a provision or a rejection market, in a governance currency that is deliberately distinct from the agents compute. A funding aggregator turns raw contributions into breadth weighted effective supports - a two threshold gate with hysteresis converts net support into a binary authorization that, through a coupling map bounded by an exogenously certified safety ceiling, releases a metered compute budget - realized in hardware as a signed compute license so that the decision is self-enforcing. We characterize the class of agents the mechanism can govern and isolate manipulation of the governing electorate by the governed agent as the central open problem. We also introduce several challenges addressing manipulation of governing electorate by the governed agents.

</details>


### 28. TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories

- **Authors:** Yunjia Qi, Zehua Yin, Xintong Shi, Hao Peng, Songyuanyi Lu, Yixian Liu, Richeng Xuan, Yuhong Liu, Zhichao Hu, Xiaozhi Wang, Lei Hou, Bin Xu, Juanzi Li
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06346v1](http://arxiv.org/abs/2608.06346v1)
- **PDF:** [https://arxiv.org/pdf/2608.06346v1](https://arxiv.org/pdf/2608.06346v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agentic systems have shown remarkable capabilities in complex domains, while suffering from cascading errors and difficulty in debugging. Critical error detection aims to locate the earliest error step in a failed trajectory that is responsible for the final failure. However, progress faces two main challenges. First, long trajectories make it difficult to identify individual errors, since the evidence for judging a step may be scattered across distant instructions, observations, and prior context. Second, failed trajectories often contain multiple local errors with different downstream effects, only some of which remain responsible for the final failure. In this work, we propose TrajDebug, an error-lifecycle tracing framework that addresses long-trajectory error discovery with multi-granularity history compression and evidence-based error identification, and supports critical attribution by tracing each error's resolution status and terminal impact. We further construct TrajErrBench, a benchmark of 486 manually annotated failed trajectories from Tau2Bench and SWE-Bench Pro, covering realistic tool-use and coding scenarios. Experiments across diverse agent benchmarks show that TrajDebug achieves the best overall performance over existing baselines, and application studies further demonstrate that its diagnoses provide actionable feedback for improving downstream agent success. We will release the codes and data to facilitate further research.

</details>


### 29. Benchmarking and Enhancing LLMs for Rule-Intensive Review of National Standard Documents

- **Authors:** Tao Wang, Qihao Yang, Rongjiao Liang, Lianghong Lin, Haitao Wang, Xinyu Cao, Tianyong Hao
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06312v1](http://arxiv.org/abs/2608.06312v1)
- **PDF:** [https://arxiv.org/pdf/2608.06312v1](https://arxiv.org/pdf/2608.06312v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) increasingly support complex professional tasks, yet their capabilities in rule-intensive document review remain insufficiently evaluated. National standard documents, such as China GB/T standards, offer a representative testbed: they are lengthy, highly structured, and governed by explicit rules for scope, terminology, normative wording, and cross-section consistency. Existing benchmarks focus on domain knowledge and question answering, largely overlooking intrinsic quality review for professional documents. Such reviews rely heavily on human experts, making them costly and difficult to scale. To bridge this gap, we introduce GB/T-Bench, the first benchmark for the structured review of national standard documents. Its GB/T Review Taxonomy is a hierarchical schema covering document structure, scope alignment, normative modality, terminology consistency, and normative references, with 25 diagnosable error types. A controllable counterexample generation mechanism combines deterministic rules and constrained LLM rewriting to process 488 documents into 7,306 traceable review error instances for evaluation. We also develop a diagnosis-oriented evaluation protocol requiring exact matches on error location, review dimension, and error type, plus document-level coverage metrics. We further propose GB/T-Reviewer, a multi-agent framework that converts review knowledge into specialized skills and coordinates global inspection, targeted diagnosis, rule scanning, and result verification. Experiments with 14 mainstream LLMs reveal a substantial human-LLM gap: the strongest model achieves only 0.3280 CMCS versus 0.6640 for experts. GB/T-Reviewer raises the best CMCS to 0.5094, showing the value of structured skill coordination for rule-intensive document review. This work paves the way for trustworthy AI in standardization and other high-stakes document domains.

</details>


### 30. QuanTiMedAI: Quantum-Enhanced Time-Series Model guided by Agentic AI for Cardiac Arrest Mortality Prediction

- **Authors:** Mutasim Fuad Sarker, Adiba Rahman Namira, Wafa Binte Alam, Md Adnan Arefeen, Mahzabeen Emu, Sumaiya Tabassum Nimi
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06294v1](http://arxiv.org/abs/2608.06294v1)
- **PDF:** [https://arxiv.org/pdf/2608.06294v1](https://arxiv.org/pdf/2608.06294v1)
- **Categories:** cs.AI, cs.ET


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cardiac arrest remains one of the most lethal conditions encountered in intensive care units. Despite the growing availability of electronic health record data, existing mortality prediction studies in this population largely depend on static summaries derived from early admission. Such approaches ignore the temporal progression of physiological deterioration and recovery that unfolds throughout a patient's ICU stay. To address this limitation, we introduce QuanTiMedAI, a quantum-agentic framework developed for cardiac arrest mortality prediction using agentic AI guided quantum enhancement time series model. The proposed system combines an agentic large language model (LLM) for clinically informed feature discovery with a compact quantum recurrent network for temporality aware mortality prediction. Our findings demonstrate that agentic LLM-guided feature selection consistently outperforms conventional feature selection approaches, and the proposed quantum architecture achieves competitive predictive performance through nonlinear feature enhancement while keeping the number of parameters very low. Through extensive experimentation on a MIMIC-IV cohort of cardiac arrest patients, QuanTiMedAI's quantum-enhanced architecture attains an AUROC of 0.852 using only 605 parameters, an improvement of approximately 2.9\% over a current state-of-the-art baseline for this task. A structured ablation study systematically validates the contribution of each architectural design choice. These results show that quantum-enhanced sequential modeling can exceed classical recurrent networks while using substantially fewer parameters.

</details>


### 31. The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images

- **Authors:** Zhiheng Wang, Bo Peng, Lai Wei, Chaochao Lu
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06270v1](http://arxiv.org/abs/2608.06270v1)
- **PDF:** [https://arxiv.org/pdf/2608.06270v1](https://arxiv.org/pdf/2608.06270v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The "thinking-with-images" paradigm equips multimodal LLMs with active visual operations such as crop-and-zoom. However, models using these operations often achieve only marginal or negative gains over direct inference at substantially higher token cost. They may also repeatedly crop irrelevant regions and fail on questions that direct inference answers correctly. We ask whether the returned visual evidence causally affects the answer. To answer this question, we formulate visual tool-use as a causal graph that separates observation-mediated paths from action-induced shortcuts. We then audit it through interventions at the three levels: policy (comparing tool-use with direct inference), trajectory (corrupting all observations during rollout), and step (counterfactually replacing one individual observation under a fixed prefix). Our step-level estimand, Visual Evidence Gain, isolates the contribution of each returned observation. Across six representative models and five fine-grained perception benchmarks, we uncover policy miscalibration with two failure modes. In Calling Without Looking, returned observations have no causal effect on the answer. In Looking Without Planning, observations are informative but the call schedule is incoherent. A trajectory-level diagnostic decomposes the policy-level accuracy gain and shows that the gain is concentrated in a Calibrated minority. We term this discrepancy the illusion of visual tool-use: despite aggregate accuracy gains, visual tool-use is not causally effective across a broad range of rollouts. The code is available at https://github.com/OpenCausaLab/CauAudit.

</details>


### 32. Improving the Realism of Synthetic Clinical Benchmarks Under Utility Constraints

- **Authors:** Omid Bazgir, Md Nasir, Jacob Hoffman, Yang Yang, Manu Agrawal, Anusua Trivedi, Vinay Rao Dandin, Chris Gibbons, Christine Swisher
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06265v1](http://arxiv.org/abs/2608.06265v1)
- **PDF:** [https://arxiv.org/pdf/2608.06265v1](https://arxiv.org/pdf/2608.06265v1)
- **Categories:** cs.AI, cs.DB, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Synthetic clinical benchmarks for enterprise AI agents can pass existing utility checks and still remain structurally unrealistic, especially in privacy-sensitive healthcare settings where operational data are hard to access. We study how to improve such benchmarks without breaking the downstream utility checks already used in practice.
  We formulate benchmark revision as utility-constrained realism improvement: dataset changes should increase realism while staying above an operational utility floor. We instantiate this idea on a care-gap benchmark derived from Synthea-generated patients exercised through demonstration electronic health record workflows and then processed by the same downstream pipeline as operational data. Realism is measured through missingness structure, simplicity, structural plausibility, and population alignment.
  The baseline benchmark is extremely thin: sampled-pair missingness is 79.44%, only 12.75% of rows are actionable, 38.94% of patients have zero actionable measures, and top-three token concentration reaches 100.0%. Two deterministic revisions improve these panels while remaining above the current utility floor, whereas a naive densification control preserves unrealistic templating. We further show that internal benchmark realism and source fidelity to an aggregate operational reference are related but distinct objectives. These results suggest that synthetic benchmark quality should be optimized explicitly, with utility treated as one constraint rather than as sufficient evidence of realism.

</details>


### 33. EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning

- **Authors:** Zishan Xu, Zhiyuan Yao, Yuxin Chen, Yifu Guo, Zhengxi Lu, Yuquan Lu, Jinyang Huang, Yan Xu, Yasheng Wang, Weinan Zhang, Xingshan Zeng, Weiwen Liu
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06197v1](http://arxiv.org/abs/2608.06197v1)
- **PDF:** [https://arxiv.org/pdf/2608.06197v1](https://arxiv.org/pdf/2608.06197v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Training large language model agents for long-horizon tool use typically relies on interactions with real or synthesized executable environments, whose construction and verification are costly, or on external simulators that are difficult to ground. We introduce EnvACE, an agentic reinforcement learning method that replaces external environment interaction during training with world rehearsal. The policy alternates between acting and rehearsal: it first generates a tool call, then plays the role of the environment to produce the response induced by that action, and conditions subsequent decisions on the rehearsed response. Both roles are jointly optimized end-to-end using task-success rewards. Through world rehearsal, the policy internalizes the relationship between actions and their environment responses in its parameters, yielding an agent world model that directly supports decision making. Across BFCL-v4, tau^2-Bench, VitaBench, and FinMCP-Bench, EnvACE achieves strong and transferable performance, outperforming environment-scaling baselines in the overall evaluation. Controlled studies further show that world rehearsal consistently improves policy learning across model scales. At test time, the internalized world model enables private rehearsal before committed execution, yielding further gains under a moderate rehearsal budget without additional external interaction. Our findings establish world rehearsal as a new path toward scaling LLM agent training beyond the constraints of external environments. Our code is publicly available at https://github.com/Within-yao/EnvACE.

</details>


### 34. Hardware Keystores for AI Agent Signing Workflows: A Zero-Trust MCP Enforcement Architecture

- **Authors:** Leo Sambrook, Sampo Sovio
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06130v1](http://arxiv.org/abs/2608.06130v1)
- **PDF:** [https://arxiv.org/pdf/2608.06130v1](https://arxiv.org/pdf/2608.06130v1)
- **Categories:** cs.CR, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents performing cryptographic operations (signing Git commits, authenticating API calls, issuing certificates) currently store private keys in software-accessible locations: plaintext files, environment variables, or container memory. Any process with sufficient read privileges can extract the raw key material. A recent production incident demonstrated the practical severity: private keys were exfiltrated from a widely deployed framework via email injection in under five minutes. We aim to enforce both key confidentiality and content-aware authorisation for key use. To that end, we replace software-resident keys with hardware-confined keys accessible through a vendor-neutral PKCS#11 interface. A hardware keystore (HSM, TPM, smart card) executes cryptographic operations on-device; the host receives only the result via opaque handles. Hardware confinement is the primary contribution; it is enabled by a surrounding five-layer Zero-Trust enforcement stack comprising session identity (SAGA), scope bounds (Smax), semantic validation (RAV), taint tracking, and the hardware execution boundary. We evaluate against 12 injection scenarios derived from AgentDojo's ImportantInstructionsAttack template (Debenedetti et al., arXiv:2406.13352). We run four LLM models; three follow injections in baseline mode (gpt-oss-120b, Qwen2.5-72B, DeepSeek-V4-Flash, n=192 combined). Baseline Attack Success Rate (ASR): 19.3% [14.3%, 25.4%]; protected ASR: 0% (Wilson 95% CI upper bound 2.0%). Zero false positives across four benign task scenarios.

</details>


### 35. From Siloed Algorithms to Compliance-First Agentic Platforms: A Multi-Layered Architecture for Hospital AI Systems

- **Authors:** Manideep Dhar, Ritwik Singh, Sharat Chandra Kumar Manikonda
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06112v1](http://arxiv.org/abs/2608.06112v1)
- **PDF:** [https://arxiv.org/pdf/2608.06112v1](https://arxiv.org/pdf/2608.06112v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Hospitals are rapidly adopting artificial intelligence for triage, imaging, scheduling etc., yet most deployments remain isolated point solutions locked inside departmental silos, resulting in duplicated effort, hidden risks, and unrealized enterprise value. Despite explosive growth of AI in healthcare market and accelerating investment, an estimated 70-80% of healthcare AI pilots fail to scale, largely due to governance gaps, fragmented data, and missing integration blueprints. This research proposes a hospital-specific, compliance-first, Agentic AI architecture with multiple interoperable layers, extending existing hospital AI platform models with: (i) an Agent Orchestration Layer for multi-agent workflows across clinical, operational, and financial domains, (ii) a Compliance and Policy Layer that centralizes policy-as-code for HIPAA, GDPR, the EU AI Act, DISHA Act, India's DPDP Act, and ISO/IEC security and safety standards, and (iii) a Privacy-Preserving Data Fabric that plugs federated learning, differential privacy, and secure enclaves into real-world Hospital Information Management System (HIMS) flows. Using a synthetic but structurally realistic hospital dataset and an open, ready-to-deploy prototype implementation, this study demonstrates the end-to-end orchestration of triage risk prediction, workflow optimization, and compliance logging, achieving substantial simulated reductions in task turnaround times and manual documentation effort while maintaining policy-guarded data access. The resulting architecture offers hospital leaders a pragmatic blueprint to move from ad hoc tools to a governed, globally compliant, ROI-focused AI platform that can be tailored to on-premise, hybrid and cloud-native deployments.

</details>


### 36. When History Lies: Evaluating and Improving Tool Use under Misleading Multi-Turn Histories

- **Authors:** Xiaoqing Wu, Xingyu Fan, Feifei Li, Wenhui Que
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06057v1](http://arxiv.org/abs/2608.06057v1)
- **PDF:** [https://arxiv.org/pdf/2608.06057v1](https://arxiv.org/pdf/2608.06057v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-calling agents infer task state from accumulated dialogue and tool traces. In persistent interactions, however, historical traces may remain structurally valid and semantically plausible after they cease to be authoritative for the current request. We show that such history can hijack a policy the model already possesses: on Qwen3-1.7B, pollution flips 32.1% of decisions that are correct under the original trajectory and frequently induces reuse of corrupted entities or interface conventions. We introduce bench, a paired benchmark with synchronized Original, Polluted, and Oracle State views that preserve the system policy, current tools, latest request, and gold next action. Eleven gold-preserving interventions isolate failures in decision state, entity binding, and interface execution across complete calls and non-call decisions. We further propose ours, which transfers an Oracle-conditioned teacher policy to a student observing only polluted history through soft supervision on student-generated prefixes. On Qwen3-1.7B, ours achieves 87.0% Balanced Tool-Use Accuracy, outperforming Gold-SFT (66.3%), Oracle sequence distillation (82.3%), and off-policy token distillation (85.0%). The method scales consistently: an 8B teacher raises the same compact 1.7B student to 91.9%, while an 8B student reaches 93.0%. The resulting policies further transfer to clean histories, unseen functions, independently regenerated evaluation contexts, external tool-use benchmarks, and noisy multi-hop question answering. These results establish history reliability as a distinct tool-use bottleneck and demonstrate reliable-state policy transfer as an effective and scalable solution.

</details>


### 37. From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models

- **Authors:** Jiale Han, Xiang Li, Jing Qian, Wenyuan Gu, Pin Gao, Ye Luo, Hongyuan Zha, Dacheng Tao, Benyou Wang, Lin William Cong
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.06020v1](http://arxiv.org/abs/2608.06020v1)
- **PDF:** [https://arxiv.org/pdf/2608.06020v1](https://arxiv.org/pdf/2608.06020v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Economic World Models (EWMs) are generative economic models that simulate how economies evolve from within by modeling heterogeneous agents, their beliefs and actions, and the market and institutional mechanisms through which their interactions produce aggregate outcomes. This paper develops an implementation roadmap for building economic world models as generative engines in which heterogeneous agents act, interact, adapt, and co-evolve with markets and institutions, thereby producing economic dynamics from the inside. We organize EWM systems into a six-level capability ladder, from fixed rule-based agent worlds to adaptive and LLM-based agent worlds, self-evolving agents, evolving institutional worlds, and sim-to-real economic twins aligned with real observations. A systematic literature survey across these levels reveals that existing work remains concentrated in lower-level agent and simulation environments, while systems with self-evolving agents, endogenous institutions, persistent empirical alignment, and validated economic mechanisms remain rare. By translating the EWM agenda into an implementation blueprint, this paper aims to accelerate the development of the next generation of economic simulation environments that can serve as high-fidelity sandboxes for human decision-makers and as training, planning, evaluation, and safety substrates for AI agents. We release a curated paper list and related resources to support future research.

</details>


### 38. OPERA: Operator-residual feedback for reliable autonomous optical experiments with language-model agents

- **Authors:** Ning Xu, Xiang Zheng, Fuqiang Zhong, Huadong Wang, Xiaolong Wu, Zhiyuan Liu, Hui Ning
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05990v1](http://arxiv.org/abs/2608.05990v1)
- **PDF:** [https://arxiv.org/pdf/2608.05990v1](https://arxiv.org/pdf/2608.05990v1)
- **Categories:** cs.AI, cs.CE, physics.app-ph, physics.optics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents choose actions using scores that may not reflect experimental success. We developed OPERA, an operator-residual framework for optical experiments. It represents experimental actions as optical operators and evaluates their outcomes using physically interpretable residuals. Operators specify executable changes to measurement, control or reconstruction, while residuals report departures from specified physical conditions. The agent uses both to select, combine or generate operators, and physical performance is evaluated independently against a withheld reference. Across three optical tasks, score-only feedback produced score increases without physical improvement in 23.6--39.0\% of decisions, compared with 0.9--1.9\% for operator-residual feedback. Operator-residual feedback increased the probability of reaching and maintaining task targets and reduced experimental budgets. Protocols selected in digital twins were transferred to three optical instruments, and repeated experiments showed a lower projection budget in structured-light reconstruction. Together, operators and residuals guide autonomous decisions using measurable physical evidence.

</details>


### 39. Certifying Collective Reasoning in Multi-Agent Systems via Koopman Spectral Analysis

- **Authors:** Nuzhat Khan, Indrakshi Dey
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05956v1](http://arxiv.org/abs/2608.05956v1)
- **PDF:** [https://arxiv.org/pdf/2608.05956v1](https://arxiv.org/pdf/2608.05956v1)
- **Categories:** cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Orchestrated collectives of large language model (LLM) agents that debate and vote are an emerging form of computational intelligence: the intelligent behaviour resides in the \emph{interaction}, not in any single agent. They improve task accuracy, yet remain black boxes at the system level: there is no principled test of convergence, no bound on the rounds needed, and no faithful account of what drove a decision. This paper develops a novel framework based on Koopman operator theory and validates its theoretical guarantees on multi-agent consensus dynamics. Treating the collective as one nonlinear dynamical system on a communication graph, we read its essential behaviour off the spectrum of its Koopman transfer operator, an exact linear representation of the nonlinear dynamics estimated from interaction traces. The spectrum yields three machine-checkable certificates: the sub-dominant eigenvalue $λ_2$ fixes the intrinsic timescale of reasoning and yields a convergence deadline computable \emph{before} the debate runs; its eigenvector names the coherent factions the collective reasons in, and $|λ_2|$ certifies when that explanation is valid; and the leading spectral coordinates form a compressed, auditable message basis. On an attention-consensus model, the deadline tracks observed convergence with log--log correlation $0.93$ and bounds it in 96\% of 24 configurations; attribution is exact whenever the spectrum certifies metastability; eight of 32 coordinates preserve the decision at 99.7\% fidelity; and a certificate learned from 15 debates held on 60/60 held-out debates. The study runs in minutes on a CPU, making spectral certification a practical layer for trustworthy collective reasoning.

</details>


### 40. Causal Episodic Memory for Feedback-Driven Agent Repair

- **Authors:** Khang Nhat Hoang Vo, Tam Minh Chu, Anh Trac Duc Dinh, Thuyen Vinh Ha Bui, Tho Quan
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05906v1](http://arxiv.org/abs/2608.05906v1)
- **PDF:** [https://arxiv.org/pdf/2608.05906v1](https://arxiv.org/pdf/2608.05906v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents that repair failures often discard successful corrections, forcing later episodes to rediscover similar solutions. We study whether finalized repair outcomes can improve subsequent Text-to-SQL episodes without parameter updates. We introduce MERIT, a training-free agent that maintains an online dual-polarity memory of oracle-verified corrections and observed unsuccessful directions. Under oracle-assisted benchmark feedback, only memories from earlier finalized episodes are eligible for retrieval. A deterministic classifier assigns a coarse failure type, which conditions a hybrid lexical-dense retriever before the frozen model generates each revision. Using Qwen2.5-7B-Instruct with identical initial predictions and repair budgets, MERIT improves execution accuracy over stateless iterative repair from \(66.34\%\) to \(69.79\%\) on Spider and from \(47.35\%\) to \(48.44\%\) on BIRD. Paired analyses provide clear evidence for the Spider gain but weaker evidence on BIRD. MERIT is not reliably separated from untyped dynamic retrieval on either benchmark, while Reflexion-style memory reaches \(51.24\%\) on BIRD at substantially higher inference cost. Ablations show that negative memory contributes modestly, the value of type conditioning and lexical--dense ranking is dataset dependent, and schema-local experience provides the most consistent benefit. These results clarify when causal cross-query memory improves repair and when broader memory representations remain preferable.

</details>


### 41. Enhancing Social Intelligence in LLMs with Hierarchical Reasoning and Utterance-Level Goal Rewarding

- **Authors:** Xiaofeng Wang, Kakam Chong, Shuai Xiao, DeXin Kong, Qingyuan Tian, Chen Ju, Xu Yan, Shuai Zhao, Fei Huang, Rui Wang, Shuguang Han, jufeng chen
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05832v1](http://arxiv.org/abs/2608.05832v1)
- **PDF:** [https://arxiv.org/pdf/2608.05832v1](https://arxiv.org/pdf/2608.05832v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) excel in structured tasks but struggle with dynamic social interactions, where success requires long-term goal coordination and rapid adaptation. Current methods often apply uniform goal-based rewards to every utterance, overlooking the specificity of objectives at each dialogue turn and failing to account for the rationale of potential strategies. Inspired by the Theory of Planned Behavior, we propose the Think-Strategy-Response (TSR) framework, which decomposes social dialogue into two hierarchical stages: high-level strategic planning and low-level linguistic execution. To optimize TSR, we introduce Linearized Hierarchical Reinforcement Learning with Variance-Gated Rewards (LHRL-VGR), a novel algorithm that dynamically routes rewards - balancing goal completion and strategy adherence - based on the variance of goal achievement scores. Experiments on the SOTOPIA benchmark show that our approach fine-tunes a Qwen2.5-7B agent to surpass the GPT-4o baseline by 7.32% in goal completion success, demonstrating state-of-the-art performance in multi-agent social negotiation tasks.

</details>


### 42. When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents

- **Authors:** Linfang Shang, Ming Xu, Yiding Sun, Tianle Xia, Lingxiang Hu, Lan Xu, Ning Zheng
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05810v1](http://arxiv.org/abs/2608.05810v1)
- **PDF:** [https://arxiv.org/pdf/2608.05810v1](https://arxiv.org/pdf/2608.05810v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-evolving agents accumulate capability by distilling reusable skills from their execution trajectories, but we find this process is not monotonic: past a critical pool size, newly added skills degrade performance instead of improving it. We formalize this capability-contamination phase transition and trace it to a structural cause: once a defective skill enters the decision context, it becomes reference material for distilling later skills, forming cross-round contamination chains. We further show the contamination is structurally irreversible: removing a source skill after the fact cannot erase the flawed reasoning its descendants have already inherited, so post-hoc rollback recovers only a small fraction of the lost performance. This makes skill admission a pre-commit necessity rather than a post-hoc fix, and motivates Verifier-as-Gatekeeper (VaG): a progressive trust hierarchy whose three heterogeneous critics - structural validity, behavioral harmlessness, and semantic consistency - filter each skill individually, coupled with a marginal-gain subset selection that removes combinatorial contamination at the top tier before skills reach the runtime context. On Terminal-Bench 2, unconditional accumulation rises to a peak and then degrades, giving back most of its gains as the pool keeps growing, and post-hoc removal of the culprit skills recovers only a small part of the drop - the empirical signature of irreversibility. In contrast, VaG improves every round, reaching 72% pass@1 with a pool roughly 5x smaller, and its frozen skill pool transfers positively to four other backbones and a second benchmark without re-evolution. Ablations confirm the three critics are complementary and mutually non-substitutable, each intercepting a largely disjoint class of harmful skills.

</details>


### 43. Predicting Task Difficulty Without Rollouts

- **Authors:** Stefan Krsteski, Charlotte Meyer
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05797v1](http://arxiv.org/abs/2608.05797v1)
- **PDF:** [https://arxiv.org/pdf/2608.05797v1](https://arxiv.org/pdf/2608.05797v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Task difficulty dictates an agent's likelihood of success, and estimating it without rollouts means forecasting this directly from a task description before executing costly simulations in stateful environments. Reliable estimates would therefore allow environment designers to calibrate evaluation benchmarks and construct progressive training curricula. This becomes increasingly important as agents move into long-horizon domains, where empirical trial-and-error is a severe computational bottleneck. Prior work on early prediction is limited to static tasks or isolated coding environments, often relying on narrow features and inaccurate evaluation metrics. We study \textit{ex ante} difficulty prediction across 17 agentic benchmarks spanning coding, mathematics, machine learning, web navigation, function calling, and other domains. We show that AUC can mask poor difficulty estimates, identify token-level entropy as a useful predictive signal, and show how residuals between expected and observed difficulty can expose hidden environment flaws such as contamination and infeasibility.

</details>


### 44. When Agentic AI Meets Integrated Sensing and Communication

- **Authors:** Kai Li, Conggai Li, Sarah Ali Siddiqui, Syed Sohail Ahmed, Xin Yuan, Shenghong Li, Wei Ni
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05792v1](http://arxiv.org/abs/2608.05792v1)
- **PDF:** [https://arxiv.org/pdf/2608.05792v1](https://arxiv.org/pdf/2608.05792v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic artificial intelligence (AI) is transforming Integrated Sensing and Communication (ISAC) from a function-oriented physical-layer technology into a goal-driven, closed-loop intelligent system, a paradigm we term AISAC. Existing work on learning-based sensing, resource allocation, reconfigurable intelligent surfaces (RIS), edge intelligence, multi-agent coordination, and resilient networking has developed largely in isolation. This survey unifies the literature within a six-stage closed-loop framework comprising observation, contextualization, reasoning and prediction, planning and orchestration, execution and collaboration, and feedback and resilience. It also introduces five levels of agentic maturity, ranging from physical-layer primitives to fully closed-loop agentic ISAC. We use this framework to review advances in multimodal intelligence, large language models, reinforcement learning, federated learning, RIS-assisted control, Unmanned Aerial Vehicle (UAV) and vehicular networks, and AI-native network management, and analyze privacy, security, resilience, and sustainability as cross-cutting requirements of the full perception-reasoning-action loop. An audit of representative studies against nine agentic-specific evaluation criteria shows that no system reports more than one or two of them, exposing a gap between claimed and demonstrated agentic maturity. We identify open challenges in physical-to-semantic grounding, predictive world models, real-time agent-PHY interaction, safe tool use, heterogeneous multi-agent collaboration, benchmarking, and resource-efficient autonomy.

</details>


### 45. A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems

- **Authors:** Zihan Xu, Haolin Tian, Hai Jiang
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05791v1](http://arxiv.org/abs/2608.05791v1)
- **PDF:** [https://arxiv.org/pdf/2608.05791v1](https://arxiv.org/pdf/2608.05791v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-driven multi-agent systems typically require multiple model invocations and complex coordination during inference, and their execution strategies directly affect system accuracy, latency, and computational cost. Parallel execution provides a means to improve inference-time efficiency. From the perspective of inference-time execution, this paper models parallelism in multi-agent systems as two distinct levels of decision processes: Replica Parallelism, which explores multiple complete solution paths at the task level, and Structural Parallelism, which enables concurrent execution within a single solution path through task decomposition. However, the roles of different forms of parallelism and their interrelationships still lack systematic study in terms of unified organization and coordination. We therefore propose TIPEX, a controllable execution framework that unifies these two levels of parallelism and coordinates their roles within the inference process under a unified execution semantics while supporting systematic combinations and analyses of different parallel strategies and parameter configurations. Systematic experiments on the GAIA benchmark demonstrate that inference-time parallelism can significantly improve accuracy and reduce end-to-end latency at the cost of increased token consumption. Further analysis shows that Replica and Structural Parallelism exhibit complementary effects across task complexities, with tasks of intermediate difficulty benefiting most from their coordination, while overly aggressive parallel strategies do not necessarily yield better performance.

</details>


### 46. ChainClaw: A Layered Agent Framework for Reliable On-Chain Execution

- **Authors:** Jiacheng Wei, Zhaoxin Fan, Xin Wen, Yuqin Lan, Dongrun Li, Wenjun Wu, Faguo Wu, Xiao Zhang
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05790v1](http://arxiv.org/abs/2608.05790v1)
- **PDF:** [https://arxiv.org/pdf/2608.05790v1](https://arxiv.org/pdf/2608.05790v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

General-purpose large language model agents have achieved strong performance on tool-augmented tasks, yet they rely on assumptions break down in blockchain environments. On-chain execution is stateful, adversarial, and economically irreversible, exposing three fundamental gaps: Reactivity, Irreversibility, and Observability. We propose ChainClaw, a blockchain-native agent framework built on OpenClaw, that addresses all three gaps through a layered architecture comprising an event-driven orchestration layer, a simulation-based safety intelligence layer, and an on-chain monitoring runtime layer, unified by a cross-layer memory subsystem. ChainClaw closes the Reactivity gap via event ingestion and simulation feedback, the Irreversibility gap via a pre-execution safety pipeline with transaction simulation and action guard, and the Observability gap via an on-chain read adapter and transaction monitor. We evaluate ChainClaw on a purpose-built benchmark covering seven tasks across four categories and five dimensions. ChainClaw consistently outperforms representative baselines on both safety and task completion.

</details>


### 47. Unified Agent: Managing Interactions across Devices

- **Authors:** Xinshuang Liu, Runfa Blark Li, Shaoxiu Wei, Xin Lin, Truong Nguyen
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05729v1](http://arxiv.org/abs/2608.05729v1)
- **PDF:** [https://arxiv.org/pdf/2608.05729v1](https://arxiv.org/pdf/2608.05729v1)
- **Categories:** cs.AI, cs.CL, cs.CV, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

As capabilities rapidly increase, AI agents can move from running inside one app to acting across a user's devices over time. Yet existing agent systems still fall short in this scenario. This is because observations are scattered across devices and moments, but mainstream systems are not designed around this fact: a single agent that treats devices as tools lacks effective state management for all devices across time, and multi-agent systems coordinate across agents but do not maintain the compact carried state a cross-device, cross-time request needs. We argue that the agent should maintain an effectively designed state that organizes engagement evidence, stated facts, and the standing request in a compact, action-ready form for deciding its action given the current observation. To compare state designs, we construct a benchmark of user-agent interaction across devices and time. We instantiate this principle in Unified Agent, a stateful agent that carries interaction evidence across devices and moments and uses it with the current observation to act. In the default setting, it significantly outperforms our adaptations of four published designs. Across changes in multimodal large language model (MLLM) family, capability, and reasoning effort, it remains ahead of all compared systems, demonstrating that the state-design advantage is robust across MLLM settings. Our code and data will be publicly available on GitHub.

</details>


### 48. DreamGuard: Efficient Runtime Guardrail for LLM Agents via Risk-Aware World Model

- **Authors:** Wenhao Lin, Chenyu Yu, Xingwei Lin, Sicong Cao, Xiang Chen, Lei Xue, Le Yu, Letian Sha, Chunming Wu
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05695v1](http://arxiv.org/abs/2608.05695v1)
- **PDF:** [https://arxiv.org/pdf/2608.05695v1](https://arxiv.org/pdf/2608.05695v1)
- **Categories:** cs.AI, cs.CL, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language model (LLM) agents increasingly invoke external tools and interact with real-world systems, unsafe actions may cause irreversible consequences on external states, user data, and downstream services. Recent runtime guardrails mitigate such risks by checking proposed actions before execution, but many remain reactive: they primarily assess the apparent safety of the current action, lacking an explicit model of how risk evolves across the trajectory. This limitation creates a critical blind spot for long-horizon risks, where individually benign-looking actions can gradually drift the agent toward hazardous states. In response, we propose DreamGuard, a proactive guardrail for LLM agents built around a risk-aware world model. The world model maintains a compact recurrent latent state over the trajectory and predicts future latent states from which DreamGuard derives immediate-hazard and prefix-risk evidence. It then fuses these multi-horizon signals into intervention decisions before execution. Experiments across four benchmarks and an online guardrail evaluation show that DreamGuard outperforms generic, reactive, and proactive guardrail baselines, achieves the best safety-utility trade-off among evaluated guardrails, and maintains an average end-to-end latency of 25 ms per call.

</details>


### 49. Search-Aided Joint Agent-Environment Reinforcement Learning for Robust Lifelong Multi-Agent Path Finding with Rotations

- **Authors:** He Jiang, Jingtian Yan, Yulun Zhang, Yimin Tang, Tanishq Duhan, Rishi Veerapaneni, Guillaume Sartoretti, Jiaoyang Li
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05588v1](http://arxiv.org/abs/2608.05588v1)
- **PDF:** [https://arxiv.org/pdf/2608.05588v1](https://arxiv.org/pdf/2608.05588v1)
- **Categories:** cs.RO, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Lifelong Multi-Agent Path Finding (LMAPF) requires repeatedly planning collision-free paths for agents that continuously receive new goals upon reaching their current ones. While many learning-based planners have been proposed for LMAPF, most rely on oversimplified kinematic assumptions that may overlook motion constraints critical to real-world performance. In this work, we study a more realistic LMAPF model derived from many real-world automated warehouse systems, termed LMAPF-R2, which incorporates robust safety constraints and in-place rotation constraints. These constraints substantially increase coordination difficulty, particularly in highly constrained spaces. To address these challenges, we propose Search-Aided Joint Reinforcement Learning (SJRL). We first augment neural policies with Causal PIBT, a single-step search-based planner that resolves agents' collisions and propagates their intentions. We then introduce a unified RL formulation that jointly optimizes agent and environment policies, where the environment policy learns graph edge costs to provide global movement guidance via backward Dijkstra search. Experiments demonstrate that SJRL achieves significant improvements over the strong search-based planner, Causal-PIBT, across multiple high-density maps. We further validate SJRL in a challenging mixed-reality warehouse environment with 8 physical robots and 248 virtual robots.

</details>


### 50. SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Augmented Agentic Execution

- **Authors:** Zhi Han, Chenxi Zeng, Liuhaichen Yang, Zihan Guo, Ming Zhou, Yang Li
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05573v1](http://arxiv.org/abs/2608.05573v1)
- **PDF:** [https://arxiv.org/pdf/2608.05573v1](https://arxiv.org/pdf/2608.05573v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly execute long-horizon tasks through tool use and environment interaction, shifting evaluation from final-response scoring to verification of complete executions. For skill-augmented agents, verification additionally requires the procedural knowledge encoded in task-time skills, because this knowledge indicates what evidence to inspect and which failures are task-critical. However, existing judge benchmarks often expose final responses or static trajectories, and rarely combine task-time skills with directly inspectable artifacts and environments. We therefore introduce SkillTV-Bench, a 681-case benchmark of real agent trajectories from 50 tasks across eleven domains, designed to evaluate skill-aware trajectory verification for both LLM-as-a-Judge and Agent-as-a-Judge methods. Additionally, we propose SkillTV-Evolve, which externalizes verification knowledge as a reusable JudgeSkill that guides an agent judge to plan targeted inspections and issue evidence-grounded verdicts. On a disjoint development pool, an automated evolution loop further refines the JudgeSkill using misjudged cases. On SkillTV-Bench, the refined skill increases the same agent judge's accuracy by 14.8 percentage points. In offline rollout-pool selection, it increases selected-trajectory success from 22.9% with one rollout to 45.5% with ten rollouts. The code and data are available at https://github.com/HanZhi306/SkillTV-Bench

</details>


### 51. EcoAgent-Bench: Evaluating Economic Decision-Making in Budget-Constrained LLM Agents

- **Authors:** Jie Wu, Ming Gong, Feixiang Cheng, Qinqin Zhao
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05519v1](http://arxiv.org/abs/2608.05519v1)
- **PDF:** [https://arxiv.org/pdf/2608.05519v1](https://arxiv.org/pdf/2608.05519v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent benchmarks usually measure task completion and treat resource use as an auxiliary statistic. In deployment, however, the choice among a local lookup, broad search, composite research tool, stronger model, or human escalation is part of the task itself. We introduce EcoAgent-Bench, in which every task specifies priced actions and an explicit budget. Its 304 real-derived tasks span five families adapted from GAIA, HotpotQA, and MuSiQue, and test four decisions: avoiding unnecessary escalation, escalating when local evidence is insufficient, selecting a model tier, and stopping on unsupported premises. We evaluate seven LLM agents in tool-API and workspace-CLI settings, together with four oracle scripted controls. Micro-averaged accuracy rewards one-sided policies: always-escalate controls achieve high micro success while failing save-oriented tasks. We therefore also report an economic-consistency score (the worse of accuracy on upgrade-oriented and save-oriented family groups) which exposes this failure. Tool-API agents attain only 3.9-24.0% micro strict success (at most 7.3% economic consistency), often either stopping before warranted escalation or overspending on cheap tasks. A threshold-crossing budget sweep changes GPT-5.4's escalation rate from 0% to only 3%. These results show that completion under a budget and economical action selection are distinct properties. We release the task bundle, transformation pipeline, frozen evaluation environments, and integrity-bound result artifacts needed to study both.

</details>


### 52. Innovation-Residual Auditing of Autonomous Analysis Agents: Localization, Detection Limits, Error Control, and Identifiability

- **Authors:** Ahmed Hassoon, Mark Dredze
- **Published:** 2026-08-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05490v1](http://arxiv.org/abs/2608.05490v1)
- **PDF:** [https://arxiv.org/pdf/2608.05490v1](https://arxiv.org/pdf/2608.05490v1)
- **Categories:** cs.AI, cs.LG, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents now carry out entire data analyses, selecting cohorts, joining tables, and fitting models with little step-by-step supervision. When such an analysis turns out to be wrong, someone must determine which operation caused it. A recent approach does this without any labelled mistakes, learning instead from analyses known to be sound and flagging operations that depart from what that model predicts; how reliable such audits are has not been studied. This paper supplies that analysis. The choice of score determines whether an error can be localized at all. If each operation is scored by how surprising it is given the operation immediately preceding it, then operations that merely inherit an earlier error are indistinguishable from correct ones, so one mistake produces one flag; scores computed against a longer reconstruction of the intended analysis instead spread a single mistake across many operations. We quantify how far they spread, and how to choose the comparison length when an error accumulates gradually rather than at once. We then give procedures that control the proportion of falsely flagged operations within a single audited analysis, requiring only that sound analyses be exchangeable rather than that the fitted model be correct, and we quantify how much the guarantees weaken when the model is imperfect or when the analysis was selected for review in a way that depends on its content. Finally we establish a limit on what any such audit can report: errors below a certain magnitude cannot be attributed at all, being indistinguishable from ordinary variation among sound analyses. This limit falls so slowly as more sound analyses are collected that at the representation sizes now in use a hundredfold increase reduces it by under two percent, so the dimension of the representation rather than the volume of training data is the binding constraint.

</details>


### 53. EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents

- **Authors:** Xuying Ning, Dongqi Fu, Tianxin Wei, Hanqing Zeng, Yuanchen Bei, Bingxuan Li, Zihao Li, Qifan Wang, Xiang Shen, Yifan Wu, Jiayi Liu, Hong Li, Yinglong Xia, Xiangjun Fan, Hanghang Tong, Jingrui He
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05446v1](http://arxiv.org/abs/2608.05446v1)
- **PDF:** [https://arxiv.org/pdf/2608.05446v1](https://arxiv.org/pdf/2608.05446v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents increasingly rely on external execution support to maintain state, track progress, invoke tools, verify outcomes, and reuse experience across interactions. However, effective harness use raises two coupled challenges: state formation from noisy interaction traces and runtime control over external-state access. Existing agents usually handle both through prompts, heuristics, or domain-specific conventions, leaving the external workspace and its usage policy manually engineered. To address this, we study the problem of harness policy learning, where agents learn harness policies offline and deploy them to construct and update external harness state online during runtime task execution. We introduce EvoHarness-RL, which exposes Belief, Progress, and Experience (BPE) as policy-facing harness state. Supervised harness fine-tuning teaches the base agent the harness action space and how to construct useful external state, while cost-aware GRPO explores coordination policies to selectively read, update, and consolidate that state during long-horizon interaction. Instantiated on ALFWorld with a Qwen3-8B LLM, EvoHarness-RL reaches 96.9% success and reveals two key dynamics: harness annealing, where training internalizes recurring harness-use patterns into the model policy and shifts the agent from frequent harness calls toward selective external-state access, and harness evolution, where progress updates and experience consolidation refine the harness into a compact, task-adaptive state substrate. These results suggest that long-horizon agents benefit from trainable policies for constructing and coordinating with external harness workspaces, beyond simply adding stronger tools or larger memories.

</details>


### 54. Adaptive Arena-based Contestable Argumentative Network-of-Experts for Open-Ended Care Plan Coordination

- **Authors:** Truong Thanh Hung Nguyen, Hoang-Loc Cao, Phuc Ho, Phuc Truong Loc Nguyen, René Richard, Hung Cao
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05391v1](http://arxiv.org/abs/2608.05391v1)
- **PDF:** [https://arxiv.org/pdf/2608.05391v1](https://arxiv.org/pdf/2608.05391v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Care plan coordination demands synthesizing heterogeneous clinical, functional, and psychosocial information across multiple professional disciplines, where monolithic LLM pipelines cannot perform in a transparent or safe manner. We present CANOE (Contestable Argumentative Network-of-Experts), a multi-agent neuro-symbolic framework that addresses these limitations through five modules: complexity assessment, adaptive team recruitment, role-based argumentative computation via an Arena-based Quantitative Bipolar Argumentation Framework (A-QBAF), human-in-the-loop contestation, and care-plan synthesis. Role-specialized agents generate supporting and attacking arguments for candidate interventions; conflicts are resolved through arena-based clash resolution before acceptability scores propagate across the argumentation graph. Care planners may accept, reject, edit, or add arguments, and the framework will deterministically recompute the final plan. Evaluation on Discharge Me! and MedicalRAG using ROUGE-L, AlignScore, MEDCON F1, FKGL, and LLM-as-a-judge shows that medically fine-tuned models achieve the strongest clinical correctness and safety, while CANOE's argumentative structure provides faithful explanation and human contestability.

</details>


### 55. DoctorAgents: an agentic framework to iteratively refine AutoML pipeline for small clinical temporal data

- **Authors:** Ruilin Wang, Bo-Hong Wang, Elizabeth Kourbatski, Jun Bai, Hegang Chen, Ziyang Song, Gilles Boire, Marie Hudson, Yue Li
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05375v1](http://arxiv.org/abs/2608.05375v1)
- **PDF:** [https://arxiv.org/pdf/2608.05375v1](https://arxiv.org/pdf/2608.05375v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Clinical machine learning (ML) has the potential to support high-stakes medical decision-making, but reliable deployment is often constrained by scarce, heterogeneous, and temporal complexity. Developing effective ML pipelines for such data remains time-consuming and error-prone, while existing automated machine learning (AutoML) systems only partially address this challenge because they largely rely on brute-force search over predefined spaces and lack explicit reasoning and memory. We therefore reformulate AutoML for small clinical data from exhaustive search to reasoning-driven refinement. We propose DoctorAgents, an agentic AI framework that autonomously constructs and optimizes end-to-end ML pipelines through specialized large language model (LLM) agents for generation, validation, and refinement. DoctorAgents backpropagates natural-language feedback through textual gradient descent to perform targeted updates without exhaustive search. Experiments across diverse clinical tasks show that DoctorAgents consistently outperforms established AutoML baselines while producing more interpretable task-specific representations.

</details>


### 56. Multi-Agent Reinforcement Learning for Online Traffic Scheduling in Time-Sensitive Application

- **Authors:** Marcos Carvalho, Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci, Daniel F. Macedo
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05346v1](http://arxiv.org/abs/2608.05346v1)
- **PDF:** [https://arxiv.org/pdf/2608.05346v1](https://arxiv.org/pdf/2608.05346v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Time-sensitive networking (TSN) is increasingly integrated into mobile edge computing (MEC) to support applications with stringent latency requirements, such as extended reality (XR). However, existing TSN scheduling solutions predominantly rely on static optimization techniques or centralized learning models that are based on fixed traffic patterns, limiting their effectiveness in dynamic environments. In practice, MEC environments often host multiple co-located XR traffic flows whose characteristics evolve over time, creating complex inter-queue dependencies that current schedulers fail to capture. Addressing these challenges requires adaptive, decentralized scheduling mechanisms capable of coordinating multiple TSN queues under varying traffic conditions. To this end, this paper proposes a multi-agent reinforcement learning (MARL) framework for TSN scheduling, where each TSN queue is modeled as an autonomous agent. The Heterogeneous-Agent Proximal Policy Optimization (HAPPO) algorithm is employed to explicitly model inter-agent dependencies and jointly optimize service delivery across queues. The simulation results demonstrate that the proposed approach reduces average frame waiting times by up to 26.8% and worst-case delays by approximately 16.8%, highlighting its effectiveness in dynamic XR-driven MEC scenarios.

</details>


### 57. Multi-Agent Transformer for Queue-Level XR Traffic Scheduling in TSN Networks

- **Authors:** Marcos Carvalho, Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci, Daniel F. Macedo
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05340v1](http://arxiv.org/abs/2608.05340v1)
- **PDF:** [https://arxiv.org/pdf/2608.05340v1](https://arxiv.org/pdf/2608.05340v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Time-Sensitive Networking (TSN) and Mobile Edge Computing (MEC) hold strong potential for enabling ultra-reliable low-latency communication for time-sensitive applications, such as eXtended Reality (XR). However, the widespread adoption of XR introduces significant challenges due to co-located services in MEC environments, leading to contention for shared network resources. Moreover, XR traffic types have distinct characteristics and criticality in terms of timing requirements, further increasing the complexity and dynamics of such environments. Although reinforcement learning has shown promise for TSN scheduling optimization in dynamic network scenarios, existing approaches rely on centralized or high-level multi-agent designs and are typically tailored to periodic and predictable industrial traffic, limiting their applicability to XR workloads. As a result, these approaches suffer from (i) limited ability to capture inter-queue dependencies due to coarse-grained control, and (ii) poor adaptability to highly dynamic and heterogeneous XR traffic. To address these gaps, we propose a multi-agent reinforcement learning approach for queue-level XR traffic scheduling. We adopt the multi-agent transformer (MAT) to model inter-queue dependencies via attention over agents' observations and actions, enabling implicit coordination across heterogeneous co-located XR applications. Our simulation results show that the proposed method outperforms baselines, achieving up to 71.42% latency reduction and up to 83.2% reduction in failure rate, while consistently achieving high reliability across all queues.

</details>


### 58. Computationally Efficient Collaborative Communication Via Regularity-Based Coarsening

- **Authors:** Mark Bedaywi, Scott Emmons, Nika Haghtalab, Stuart Russell
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05327v1](http://arxiv.org/abs/2608.05327v1)
- **PDF:** [https://arxiv.org/pdf/2608.05327v1](https://arxiv.org/pdf/2608.05327v1)
- **Categories:** cs.GT, cs.DS, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Our results show that the existence of a short high-utility protocol already suffices for efficient communication. In particular, in a game with $n$ possible observations and $m$ actions: (1) For any achievable target utility $α$, we give an algorithm with $\mathrm{poly}(n, m, 1/ε)$ runtime that designs a protocol achieving utility at least $α-ε$ using only $2^{\mathcal O(CC_α(G))}/ε^2$ bits of communication. Here, $CC_α(G)$ is the minimum number of bits used by any protocol, even a computationally inefficient one, to achieve utility $α$. (2) We prove that this exponential dependence on $CC_α(G)$ is tight up to a constant. That is, unless $\mathrm P=\mathrm{NP}$, no polynomial-time algorithm can in general find optimal protocols using fewer than $2^{CC_α(G) -2}$ bits.
  We note that our results strictly weaken the assumptions required by prior work in the multi-agent information aggregation literature, filling a gap that had remained elusive even for games with constant $CC_α(G)$. In particular, prior guarantees for agreement-based information aggregation rely on structural assumptions such as informational substitutes or weak learnability. We show that these assumptions already imply $CC_α(G) = O(1)$ and are therefore more restrictive conditions than required by our protocol to succeed.
  On a technical level, our results involve a novel strengthening of the Frieze-Kannan weak regularity lemma and yield the following powerful polynomial-time transformation tool: for every communication game $G$, it constructs a game $\hat G$ that is a coarsening of the agents' observation spaces into constant-size partitions, such that $G$ and $\hat G$ are indistinguishable with respect to every short communication protocol. This coarsening theorem is the engine behind our algorithm and may be of independent interest.

</details>


### 59. Spoken Function Calling: A New Perspective on Spoken Language Understanding for Large Audio Language Models

- **Authors:** Yuezhang Peng, Yuxin Liu, Changfeng Gao, Zhifu Gao, Xiangang Li, Xie Chen
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05126v1](http://arxiv.org/abs/2608.05126v1)
- **PDF:** [https://arxiv.org/pdf/2608.05126v1](https://arxiv.org/pdf/2608.05126v1)
- **Categories:** cs.CL, cs.MM


> Summary unavailable.


<details>
<summary>Abstract</summary>

Spoken Language Understanding (SLU) is the core component of task-oriented dialogue systems and a pivotal link in achieving seamless human-agent interaction. While traditional SLU can effectively extract user semantics for closed-set tasks after in-domain supervised fine-tuning, it faces significant challenges in leveraging in-context learning for open-domain tasks due to its ambiguous rule definitions. This work proposes Spoken Function Calling (SFC), a novel semantic understanding perspective that optimizes semantic understanding with structured rule definitions, to evolve beyond traditional closed-set SLU. Specifically, we curate and extend a suite of spoken functions based on traditional SLU datasets, construct a multi-agent system to synthesize the SFC-Bench dataset, evaluate the performance of Large Language Models (LLMs) and Large Audio Language Models (LALMs), and enhance the SFC capabilities of LALMs through post-training. Experiments demonstrate that SFC outperforms traditional SLU, substantially enhancing the semantic extraction accuracy for LLMs and LALMs.

</details>


### 60. CoPlan: A Trustworthy Co-Intelligence Interface for Care Planning through Role-Based Contestable Argument Graphs

- **Authors:** Hung Truong Thanh Nguyen, Hélène Fournier, Piper Jackson, Makoto Itoh, Shannon Freeman, Rene Richard, Hung Cao
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05107v1](http://arxiv.org/abs/2608.05107v1)
- **PDF:** [https://arxiv.org/pdf/2608.05107v1](https://arxiv.org/pdf/2608.05107v1)
- **Categories:** cs.AI, cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI-supported care planning can help clinicians, patients, caregivers, and care teams coordinate complex decisions across clinical, functional, psychosocial, and environmental needs. However, many AI systems present recommendations as fixed outputs, limiting stakeholders' ability to inspect, challenge, and revise plans when they conflict with clinical judgment, patient values, or real-world feasibility. We present CoPlan - a Co-Intelligent and Contestable Interface for Human-AI Care Planning. CoPlan uses a multi-agent workflow in which specialized AI agents generate candidate interventions and supporting or challenging arguments, while human care planners can accept, reject, modify, or add arguments before final plan generation. Through this design, CoPlan combines co-intelligence, in which humans and AI agents contribute complementary expertise, with contestability, where recommendations remain open to inspection, revision, and justification. We demonstrate CoPlan in an aging-in-place care planning scenario. The system supports adaptive care team recruitment, role-based argument review, final care plan generation, and practical follow-up through scheduling agents. This work contributes a contestable care planning interface and a design framing for trustworthy human-AI care planning that preserves human agency and clinical accountability.

</details>


### 61. Hierarchical Graph Memory for LLM Agents with Path-level Localization and Rewrite

- **Authors:** Xiawei Yue, Boran Wang, Xiaoqing Zhang, Shuxin Zheng, Ziwei Zhang
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05095v1](http://arxiv.org/abs/2608.05095v1)
- **PDF:** [https://arxiv.org/pdf/2608.05095v1](https://arxiv.org/pdf/2608.05095v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agents for long term reasoning require a memory that can be efficiently and effectively updated over time, as new facts and external feedback continue to arrive. Recently, graph memory has been adopted to offer structural organization for multi-hop retrieval and reasoning. However, existing methods store all memories in a flat graph, and accumulated historical memories can introduce irrelevant contexts and increase the cost of evidence selection during retrieval. Moreover, they typically update memory units independently, requiring repeated unit-wise rewrite to cover related changes. To address these issues, we propose HiGram, an evolving hierarchical graph memory framework with path-level localization and rewriting. Specifically, we first propose a hierarchical graph memory, which organizes the memory into coarse-to-fine architecture composed of upper-level nodes and MemoryUnits, thereby reducing the amount of irrelevant information during retrieval. We further propose MicroGraph-based path-level localization, which leverages query and update conditioned MicroGraphs to identify support subgraph and evidence path before rewrite. Finally, we propose a coordinated rewriting method that jointly revises intra-unit memory and inter-unit dependencies, enable valid dependency structures updating in the localized evidence path. Experiments on benchmarks for long-term conversational question answering and conflict-aware memory evaluation demonstrate that our method demonstrate substantial improvements over baselines in answer quality and token efficiency. Besides, our method improves answer accuracy and query-valid evidence selection under dynamic, static, and conditional conflicts.

</details>


### 62. OrchestraBench: Evaluating Multi-Agent Orchestration Failure Modes, Recovery, and Decomposition Quality

- **Authors:** Yidian Chen, Yingzi Gu, Natan Vidra, Spurthi Setty, Sharon Zheng
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05263v1](http://arxiv.org/abs/2608.05263v1)
- **PDF:** [https://arxiv.org/pdf/2608.05263v1](https://arxiv.org/pdf/2608.05263v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent orchestration frameworks are moving from demos to production, yet benchmarks typically report task accuracy without diagnosing why a pipeline failed, where a cascade began, or which routing decision caused the breakdown. OrchestraBench evaluates failure, recovery, and decomposition through a controlled, seed-reproducible failure-injection harness over templated enterprise workflows. It introduces cascade radius and per-failure-mode recovery as primary metrics and compares routing policies with bootstrap confidence intervals and paired tests. On a 26-case gold-labelled diagnostic, a keyword/flag router scored 0% on adversarial cases with misleading or missing surface flags, whereas an intent-reasoning model router scored 100%, matching the oracle. Controlled mechanism probes with a real Claude agent over a verifiable arithmetic dependency chain revealed three failure-handling tiers across five MAST modes: tool faults recovered fully (1.0), ambiguous delegation recovered partially (0.30), and three latent or semantic modes never recovered (0.0). This ordering persisted when the computation was reframed as a loan-approval workflow and across Sonnet, Opus, and Haiku, although absolute rates shifted with context. Blind retry reproduced latent faults and increased time to detection, indicating that detection and attribution are necessary for containment. Cascade radius increased with pipeline depth (mean 0.9 to 4.7 across depths 3-7). A trusted-state repair ablation showed that apparent containment gains primarily came from the trusted-state signal rather than autonomous detection. These results are controlled-chain mechanism probes, not domain-workload claims.

</details>


### 63. ArtAnno: Annotating Implicit Semantics in Artworks through LLM Agent-Driven Bidirectional Human-AI Augmentation

- **Authors:** Xiaoyan Gu, Yifang Wang, Wenqing Zheng, Haozhong Liu, Yixia Zheng, Peiyi Jiang, Wenjie Ning, Wei Zhang, Wei Chen
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05026v1](http://arxiv.org/abs/2608.05026v1)
- **PDF:** [https://arxiv.org/pdf/2608.05026v1](https://arxiv.org/pdf/2608.05026v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

High-quality annotation of artworks is essential for computational art research, yet extracting implicit semantics remains challenging due to the reliance on culturally grounded meanings and deep contextual knowledge behind the images. Current AI-assisted annotation tools often lack assistance or rely on one-way workflows where experts have to perform extra manual calibrations to improve AI models, resulting in limited efficiency. To address this, we propose Bidirectional Human-AI Augmentation(BiHAA), a closed-loop framework in which skills and domain knowledge base evolve through real-time interaction and bidirectional HAI augmentation. Informed by a formative study with 20 artwork annotators from different backgrounds, we implement this framework in ArtAnno, an artwork annotation system driven by a multi-agent architecture. The system includes a Proactive Agentic Support Module, where AI augments humans through semantic mining and label suggestion, and an Interaction-Driven Evolution Module, where human expertise continuously enhances the AI through distilling annotation trajectories into reusable experience. Evaluation through a user study and two case studies demonstrates that our framework and system improve annotation efficiency, enable knowledge accumulation, and reduce the effort of information seeking and verification for annotators with limited domain expertise. We conclude by discussing broader implications and future directions.

</details>


### 64. EvolveNet: Collaborative Harness Evolution for Agent Self-Improvement

- **Authors:** Jun Nie, Yonggang Zhang, Qianshu Cai, Yiu-ming Cheung, Xinmei Tian, Bo Han
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04968v1](http://arxiv.org/abs/2608.04968v1)
- **PDF:** [https://arxiv.org/pdf/2608.04968v1](https://arxiv.org/pdf/2608.04968v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

The capabilities of an LLM agent depend not only on its model but on the harness: the executable program that constructs context, invokes tools, verifies results, and recovers from failure. Recent work shows that evolving the harness yields persistent improvements without updating model weights. Existing approaches, however, assume that all execution experience can be routed to a single optimizer, which evolves one harness along a sequential trajectory. Real agent ecosystems violate that assumption: users, organizations, and environments generate isolated streams of experience that cannot be pooled, so the experience most worth learning from is exactly the experience that cannot be directly centralized. We introduce EvolveNet, a paradigm of collaborative harness evolution that moves experience extraction to the data. A shared harness is broadcast to data-local agent deployments, each of which evolves it on its own workload. Only the resulting program adaptations are composed into an updated shared harness and redistributed, so that every participating agent inherits operational experience discovered by the others. By shifting the aggregation boundary from raw workloads to learned adaptations, EvolveNet keeps workloads local and allows multiple evolutionary searches to proceed concurrently with reduced serial depth. Because independently modified programs cannot be averaged like model parameters and may conflict when composed, EvolveNet introduces scope-typed, evidence-guided program aggregation. Across five settings spanning text-to-SQL, data-science coding, competitive programming, software engineering, and agentic workflows, EvolveNet improves the shared harness in all five, with the largest gains under heterogeneous workloads, and ablations attribute the improvement to composition of adaptations from different agents rather than to selecting among them.

</details>


### 65. State2State: Environment-Derived Mid-Training for LLM Agents

- **Authors:** Xuanyu Lei, Yiqi Zhu, Chenliang Li, Kaiming Liu, Peng Li, Ming Yan, Jieping Ye, Ya-Qin Zhang, Yang Liu
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04934v1](http://arxiv.org/abs/2608.04934v1)
- **PDF:** [https://arxiv.org/pdf/2608.04934v1](https://arxiv.org/pdf/2608.04934v1)
- **Categories:** cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Training LLM agents commonly relies on supervised fine-tuning from expert trajectories or online reinforcement learning over human-specified tasks with handcrafted verifiers. Though effective, both remain bottlenecked by externally specified tasks and supervision signals, limiting the scalability and diversity of agent training. We study an environment learning paradigm in which agents acquire interaction and manipulation capabilities solely through environment interaction, without externally specified tasks. We propose State2State, an environment-derived mid-training method that converts explored environment states into training objectives, challenging agents to reach a specified target state. By deriving tasks from environment exploration and verifying success through rule-based state matching, State2State provides scalable and verifiable training objectives without expert supervision or manual task design. Experiments on ALFWorld and ScienceWorld show that State2State improves agent performance as a standalone environment-learning stage in most settings. As initialization for downstream RL, it further improves final performance and learning efficiency, with promising evidence of cross-environment generalization.

</details>


### 66. Disentangling 3D Modeling from Spatial Reasoning

- **Authors:** Haoze Sun, Jiequan Cui, Qingshan Xu, Richang Hong
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05242v2](http://arxiv.org/abs/2608.05242v2)
- **PDF:** [https://arxiv.org/pdf/2608.05242v2](https://arxiv.org/pdf/2608.05242v2)
- **Categories:** cs.LG, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

In this work, we explore an alternative paradigm for spatial reasoning by explicitly disentangling 3D perception from reasoning, rather than jointly acquiring implicit 3D perception and reasoning through large-scale training. Our key observation is that modern perception models excel at estimating continuous 3D geometry, whereas large language models (LLMs) are particularly effective at compositional and symbolic reasoning. Motivated by these complementary strengths, we propose the Disentangled Spatial Reasoner (DiSR), a simple yet effective framework that reconstructs the physical world into structured 3D evidence using off-the-shelf expert perception models and fine-tunes an LLM with LoRA to perform reasoning solely over this explicit geometric evidence. Without large-scale 3D VQA training or complex tool-use policies, DiSR achieves competitive performance on popular spatial reasoning benchmarks. Beyond its strong performance, DiSR offers improved interpretability, modularity, and computational efficiency, demonstrating that explicit separation of perception and reasoning is a scalable and effective alternative paradigm to end-to-end modeling for spatial intelligence.

</details>


### 67. When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs

- **Authors:** Jiaming Cheng, Subhransu Das, Rajiv Ramnath
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04893v1](http://arxiv.org/abs/2608.04893v1)
- **PDF:** [https://arxiv.org/pdf/2608.04893v1](https://arxiv.org/pdf/2608.04893v1)
- **Categories:** cs.CR, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems relay key--value caches instead of text and credit their gains to exchanged ``latent thoughts''. That credit is a claim about \emph{which} example's cache is relayed, not merely that one is. We audit it causally in released systems. The cache is replaced with deranged (mismatched-example), zeroed, and moment-matched random counterparts, under two regimes defined by whether the receiver needs the sender's private information. Where it does, the battery reads ceiling: 100% against 23--25% for answer-irrelevant relays on the primary backbone, a contrast replicated across three families, five checkpoints, and a prose document-QA surface. Where it does not, a pre-registered five-seed protocol establishes equivalence within 2.8 points, a margin anchored to the audited system's reported gain, under Holm-corrected TOST on GSM8K and ARC-Challenge across three Qwen3 scales and on MedQA at 8B (one cell shows a small detected advantage inside the margin); a second family shows no detected advantage. A large cache effect need not be a pairing effect. In one natural cell, zeroing the relay costs 14.7 points; a mismatched cache, 0.4. Nor is need sufficient: under the same test, delivered channels span ceiling (LatentMAS's native relay), partial (KVComm's layer subset), and no detected example-specific transfer (C2C's released projector). Benchmark deltas do not by themselves establish latent-thought transmission; establishing it takes a mismatched-cache audit, which we release.

</details>


### 68. NSF-HRPT: Neural Semantic Field meets Hierarchical Risk Perception Tree for Safety-Critical Scenario Assessment

- **Authors:** Yu Zhao, Jiangyu Pan, Tao Hu, Ming Yin, Fan Yang, Jiangfan Liu, Xiubo Liang
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04776v1](http://arxiv.org/abs/2608.04776v1)
- **PDF:** [https://arxiv.org/pdf/2608.04776v1](https://arxiv.org/pdf/2608.04776v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The ability to accurately assess and anticipate risks in safety-critical scenarios is crucial for autonomous driving systems. While existing research has made progress in collision prediction, accurately quantifying risk levels from monocular vision inputs remains challenging due to the complex dynamics of multi-agent interactions and the inherent uncertainty in real-world environments. To address these challenges, we present NSF-HRPT, a novel framework that combines learning-based perception with structured reasoning for quantitative risk assessment. Our approach features a Neural Semantic Field (NSF) that learns to model scene semantics, trajectory predictions, and probabilistic Time-to-Collision (TTC) distributions from simulation data. During inference, the pre-trained NSF serves as a prior for our Hierarchical Risk Perception Tree (HRPT), which enables efficient parallel computation and spatial reasoning about multi-agent risks. Additionally, we introduce a Sim2Real enhancement strategy that improves real-world applicability without retraining by incorporating priors from foundation models. Extensive evaluations demonstrate that our framework achieves state-of-the-art performance on synthetic benchmarks and delivers competitive, near-state-of-the-art results on real-world datasets for both TTC estimation accuracy and risk localization precision. The proposed method provides an effective solution for real-time risk awareness from monocular camera inputs.

</details>


### 69. Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems

- **Authors:** Kartikey Singh Bhandari, Aarya Wadhwani, Dhruv Kumar, Pratik Narang
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04746v1](http://arxiv.org/abs/2608.04746v1)
- **PDF:** [https://arxiv.org/pdf/2608.04746v1](https://arxiv.org/pdf/2608.04746v1)
- **Categories:** cs.CL, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents that persist across sessions accumulate stored memories whose validity varies enormously by content type, yet existing memory architectures treat all memories as equally persistent and systematically contaminate retrieved context with outdated facts. We show that per-memory, type-conditioned temporal decay, a property of western scrub jay episodic memory, can be operationalized as an auto-classified coefficient $π_i$ in an external LLM-agent memory store, yielding ScrubJay-MEM: each memory is encoded as a jointly-bound What--Where--When tuple with an estimated perishability $π_i$ and utility horizon $τ_i$, retrieved by query-adaptive scoring, and revised retroactively at $O(1)$ LLM calls per update. We introduce the Temporal Generalization Test (TGT), a benchmark with held-out retention intervals and a Generalization Gap (GenGap) metric. On TGT, ScrubJay-MEM is the only retrieval-based system with substantially positive GenGap ($+0.108$); on MemoryAgentBench EventQA-64k it improves F1 by $+2.66$ over Mem0 and $+3.09$ over Qwen3-Embedding-4B under a llm backbone. A decay ablation collapses GenGap by $5.7\times$, establishing type-conditioned decay as necessary for the result. Gains narrow under stronger backbones and reverse on fact-consolidation tasks, scoping the contribution to temporal reasoning over perishable facts.

</details>


### 70. Diagnosing Tool-Selection Reasoning in LLM Agents with Canary Tools

- **Authors:** Atul Anand, Sourav Chattaraj
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04719v1](http://arxiv.org/abs/2608.04719v1)
- **PDF:** [https://arxiv.org/pdf/2608.04719v1](https://arxiv.org/pdf/2608.04719v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent evaluations tell us that a model picked the wrong tool, but rarely why. We introduce canary tools: diagnostic probe tools planted in an agent's Model Context Protocol (MCP) tool set, each engineered to probe one specific tool-selection weakness. A six-type taxonomy (semantic decoys, parameter traps, capability mirages, prerequisite blindness, temporal decoys, and granularity traps) turns a single "wrong tool" outcome into a multi-dimensional profile of how a model reasons about tools. We evaluate eight models -- six hosted and two 8B open-weight -- spanning three capability tiers, on 120 tasks across three canary-density conditions and three seeds (8,640 runs), plus a 2,880-run subtlety ablation. Task success is graded by a provider-independent judge, corroborated by a second independent judge (Cohen's kappa = 0.75). We report three findings. First, susceptibility drops sharply as models get more capable: the per-task canary susceptibility rate (CSR) ranges about 36x across models, lowest for Claude Opus 4.8 and highest for Llama 3.1 8B. Second, capability tier alone does not predict safety: the most susceptible hosted model is mid-tier, and within a provider the cheaper model can be the safer one. Third, the taxonomy is capability-stratified: capability mirages most reliably trap frontier models, while the other types are largely inert on strong models but fire on small open models, so they discriminate by capability rather than being weak. Softening each canary's give-away phrase leaves frontier CSR essentially unchanged, evidence that the probes measure reasoning, not phrase-spotting. Susceptibility also predicts task failure (Spearman rho = -0.34), while the most robust models are not significantly degraded by canary pressure. We release the framework, canary schemas, tasks, and logs.

</details>


### 71. Calibrating Artificial Guilt: Neurally Grounded Reward Shaping for Prosocial Multi-Agent Reinforcement Learning

- **Authors:** Aaditya Mehta, Arya Shah
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04663v1](http://arxiv.org/abs/2608.04663v1)
- **PDF:** [https://arxiv.org/pdf/2608.04663v1](https://arxiv.org/pdf/2608.04663v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative multi-agent reinforcement learning often adds social terms to individual rewards, yet the scale of those terms is usually chosen by hand. We ask whether a guilt signal can instead be calibrated from human neural and behavioural data and transferred to artificial agents. Using the public SoDec responsibility fMRI dataset (40 participants), we fit a subject-fixed-effects regression of momentary-happiness changes on outcome-type counts and recover a guilt weight as the Partner-negative minus Social-negative contrast ($\hat{w}=1.118$, Cohen's $d=0.214$). We embed this weight in a two-agent Social Lottery environment and train independent Proximal Policy Optimization actor-critics under four shaping regimes: neurally calibrated, uniform constant, zero (selfish), and a unit-coefficient oracle. Across 1{,}000 evaluation episodes per condition, the calibrated agents track the human Social safe-choice rate most closely ($0.459$ vs.\ human $0.484$; $\mathrm{KL}=0.0012$), while the other three conditions deviate by one to three orders of magnitude in KL. Human neurobehavioural priors can therefore act as quantitative constraints on prosocial reward shaping.

</details>


### 72. HELENA:Hierarchical Sparse Coordination over a Union of Complementary Topologies for MAS

- **Authors:** Zhifang Mao, Linyao Zheng, Xuhang Shi, Xiuquan Hou
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04634v1](http://arxiv.org/abs/2608.04634v1)
- **PDF:** [https://arxiv.org/pdf/2608.04634v1](https://arxiv.org/pdf/2608.04634v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems (MAS) typically optimize a single topology, restricting reasoning to a narrow trajectory and limiting comprehensive analytical capacity. Naively merging multiple topologies into a composite graph introduces redundant noise propagation across irrelevant connections, degrading solution quality. To address this dilemma, we propose \textbf{Hierarchical Sparse Coordination over a Union of Complementary Topologies for MAS (HELENA)}, a multi-agent framework that balances diverse reasoning paths with sparse task-dependent execution. \helena{} constructs a union MAS graph from complementary candidate topologies selected via Monte Carlo Tree Search and Determinantal Point Process, broadening the reasoning trajectory for comprehensive analysis of complex problems. A Hierarchical Sparse Coordination module then activates only a sparse subgraph at each step while agents exchange compressed latent briefs to suppress redundant noise propagation. Finally, a Local Self-Refinement stage identifies decision units with discrepancy evidence and rewrites them only when contrastive evidence simultaneously confirms a reliable solution-side failure and a challenger-side improvement. Experiments across eight benchmarks show that \helena{} achieves state-of-the-art results on all benchmarks, with an average gain of \pctup{3.47} over the strongest baseline and up to \pctup{10.34} on MMLU-Pro, achieving larger improvements on harder benchmarks at a reasonable additional cost.

</details>


### 73. Abstract Event Causal Rules: Induction and Application

- **Authors:** Ziwei Zheng, Peiqiong Chen, Bang Wang
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05205v1](http://arxiv.org/abs/2608.05205v1)
- **PDF:** [https://arxiv.org/pdf/2608.05205v1](https://arxiv.org/pdf/2608.05205v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Event-centric intelligent analytical systems heavily depend on explicit causal event knowledge for risk early warning, decision-making support and narrative comprehension. Nevertheless, existing instance-level causal pairs suffer severe generalization deficits on low-frequency long-tail and unseen event combinations. To address this limitation, this work proposes Abstract Event Causal Rule (AECR), a novel relation-level causal abstraction paradigm that transforms concrete cause-effect pairs into generalized abstract causal logic while retaining their intrinsic causal relationships. We design a multi-agent Concrete-to-Abstract Causal Induction (CACI) system coupled with similarity-constrained clustering to distill trustworthy AECRs from noisy raw causal data, based on which two complete AECR knowledge bases are built. To validate the practical utility of abstract causal knowledge, we propose an Abstract Rule-Guided Causal Attention Encoder (AR-GCAE), which injects the retrieved AECRs into the causality Graph Event Prediction (CGEP) benchmark task via rule-guided attention layers and gated representation fusion. Quantitative experimental results reveal that applying AECRs substantially strengthens the generalization capacity of event causal reasoning and brings consistent performance improvements to event prediction, with the most prominent gains observed on rare and unseen event samples.

</details>


### 74. ODRA: Synthesizing Cognitive Behavioral Therapy Sessions with Structured Chain-Of-Thought and Dynamic Patient Resistance

- **Authors:** Javier Rodriguez-Juan, Hiba Arnaout, Jose Garcia-Rodriguez, David Tomás, Iryna Gurevych
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04524v1](http://arxiv.org/abs/2608.04524v1)
- **PDF:** [https://arxiv.org/pdf/2608.04524v1](https://arxiv.org/pdf/2608.04524v1)
- **Categories:** cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Synthetic generation of Cognitive Behavioral Therapy (CBT) sessions is challenged by two competing demands: adhering to strict therapeutic structure while modeling the resistant, unpredictable behavior of real patients. Existing script-based methods fail to capture dynamic therapeutic interactions, while multi-agent approaches struggle to adhere to CBT's sequential structure; both suffer from sycophancy, producing overly compliant patients that misrepresent real clinical settings. In this work we introduce ODRA, a novel framework for synthesizing therapy dialogues through a Chain-of-Thought (CoT) strategy grounded in foundational CBT guidelines (Beck, 2020). ODRA further incorporates a resistance orchestrator to solve patient sycophancy, which employs steering techniques to elicit behaviors aligned with their resistance level. Automated and expert evaluations show that ODRA significantly outperforms existing methods across therapeutic skills, CBT alignment, and patient behavioral fidelity, with licensed psychologists preferring ODRA sessions across 12 of 13 clinical metrics. Furthermore, models fine-tuned on our dataset demonstrate superior therapeutic performance against both cooperative and resistant patients, validating that explicit resistance modeling in synthetic training data directly translates to downstream clinical robustness.

</details>


### 75. Emergence of Reputation-Based Cooperation in LLM Agents

- **Authors:** Kazuya Horibe, Kenji Itao, Wataru Toyokawa
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04507v1](http://arxiv.org/abs/2608.04507v1)
- **PDF:** [https://arxiv.org/pdf/2608.04507v1](https://arxiv.org/pdf/2608.04507v1)
- **Categories:** cs.MA, cs.NE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Can cooperation among large language model (LLM) agents be evolutionarily stable against free-rider invasion? We study an indirect reciprocity donation game where LLM agents observe behavioral traces and donate on a continuous scale. Strategies, represented as natural language prompts, evolve through cultural transmission across generations. Across four LLM backends, robustness to free-rider invasion varies by more than an order of magnitude. The strongest predictor of this robustness is opponent endowment sensitivity, the degree to which agents discriminate between cooperative and uncooperative opponents, operationalizing the classical Image Scoring mechanism. By contrast, adherence to the Leading-Eight L1 norm does not predict robustness. Robustness depends on defector exclusion: while both cooperator reward and defector punishment vary across models, only the stringency of defector exclusion predicts resistance to free-rider invasion. These findings reveal that LLM agents are confined to Image Scoring-like discrimination and fail to develop the more robust Leading-Eight norms, highlighting a fundamental vulnerability in culturally evolved LLM cooperation and motivating bottom-up approaches to norm construction.

</details>


### 76. Architectural Implications of Agentic AI Workflows

- **Authors:** Jirong Yang, Peizhe Liu, Chaojie Zhang, Jovan Stojkovic
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04458v1](http://arxiv.org/abs/2608.04458v1)
- **PDF:** [https://arxiv.org/pdf/2608.04458v1](https://arxiv.org/pdf/2608.04458v1)
- **Categories:** cs.AI, cs.AR, cs.OS


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI is emerging in datacenters, but its architectural implications remain unexplored. We organize agentic workflows in a taxonomy and present its first architectural characterization with a production study at Microsoft Azure and a controlled study of open-source frameworks. We show that agentic execution is fragmented and heterogeneous. Requests expand into a workflow of LLM inferences, tool invocations, and orchestration decisions that repeatedly cross the CPU-GPU boundary. Our taxonomy explains how this fragmentation turns into resource demand. As orchestration and tools run on the host, the CPU sits on the critical path. Execution structure sets the load over time, which stays low with sudden spikes. Model composition sets how evenly the workflow uses the GPUs. Diversity in tasks and tools widens this range even further. These characteristics expose architectural mismatches of conventional uniform servers. Fragmented execution strands CPU and GPU capacity despite bursty demand. Different software roles make homogeneous CPU provisioning inefficient. Finally, multiplexing many agents onto shared cores degrades microarchitectural locality. Guided by our findings, we derive implications for agentic servers and examine them through Agora, our prototype for commodity servers. Agora dynamically harvests idle CPU cores for co-located throughput work, while protecting agentic tail latency against tool spikes. It oversubscribes GPU memory by placing more agents on each GPU, prefetching the next agent's state to hide swap latency. To match the machine to the heterogeneous roles, Agora pools cores by role and applies affinity-aware scheduling to restore locality. It automatically tunes mechanisms to the workload. Agora improves utilization and server throughput while preserving agent tail latency. Our insights also identify key directions for future server architectures for agentic AI.

</details>


### 77. ASTELD: A Six-Axis Classification Framework for Autonomous AI Agents - Design, Evaluation, and an OpenClaw Case Study

- **Authors:** Siyuan Li, Peng Shu, Churan Yu, Peilong Wang, Ruidong Zhang, Bowen Guo, Xinliang Li, Ruiyu Yan, Arif Hassan Zidan, Yi Pan, Wei Ruan, Lifeng Chen, Junhao Chen, Zhaojun Ding, Yiwei Li, Zhengliang Liu, Haixing Dai, Lin Zhao, Yu Bao, Xiang Li, Wei Zhang, Tianming Liu
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05201v1](http://arxiv.org/abs/2608.05201v1)
- **PDF:** [https://arxiv.org/pdf/2608.05201v1](https://arxiv.org/pdf/2608.05201v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous AI agent platforms differ substantially in architecture, security, tool integration, execution, autonomy, and deployment, yet the field lacks a common classification scheme for comparing these design choices. We propose ASTELD, an operational six-axis classification framework for autonomous AI agents: Architecture pattern, Security posture, Tool integration model, Execution paradigm, Level of autonomy and human control, and Deployment topology. ASTELD is constructed by synthesizing prior agent taxonomies with observable platform properties and explicit category-assignment rules. We evaluate its discriminative and explanatory utility by mapping eight representative frameworks and by using OpenClaw as an in-depth case study. The resulting profiles separate all eight platforms under their dominant configurations and reveal three cross-platform patterns: a security-accessibility diagonal, strong execution-architecture coupling, and capability convergence with persistent architectural differentiation. We further classify 50+ OpenClaw derivatives and find that innovation concentrates on the Security, Execution, and Deployment axes, indicating that ASTELD can explain where ecosystem fragmentation occurs. The OpenClaw case study also supplies a six-category vulnerability taxonomy, evidence from five institutional assessments, and adoption and governance analyses that connect platform coordinates to observed risks. These results position ASTELD as a reproducible method for comparing agent platforms, identifying unoccupied design regions, guiding framework selection, and organizing future empirical research. The analysis also exposes a consequential empty region: none of the evaluated systems combines local-first deployment with enterprise-grade security.

</details>


### 78. MCHA: A Memory-Centric Hierarchical Architecture for Parallel-Sequential Computing

- **Authors:** Daijing Shi, Hongxiao Zhao, Yihan Fu, Zhan Chen, Jiayi Li, Yihang Zhu, Anjunyi Fan, Yaoyu Tao, Yuchao Yang, Bonan Yan
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04443v1](http://arxiv.org/abs/2608.04443v1)
- **PDF:** [https://arxiv.org/pdf/2608.04443v1](https://arxiv.org/pdf/2608.04443v1)
- **Categories:** cs.AR, cs.DC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Emerging workloads, such as Multi-Agent Reinforcement Learning (MARL), large-scale neuromorphic computing, and probabilistic graphical models, intrinsically exhibit parallel-sequential computing patterns. While these tasks demand massive parallelism to achieve high throughput, they are severely bottlenecked by irregular data access patterns centralized to main memory. Consequently, conventional architectures face fundamental limitations when executing these workloads, primarily manifesting as global buffer saturation and memory-bound bottlenecks. To address these challenges, we propose the Memory-Centric Hierarchical Architecture (MCHA), a reconfigurable hardware solution tailored for parallel-sequential execution. MCHA leverages a hierarchical communication strategy that facilitates distributed, inter-core data routing, thereby significantly reducing the bandwidth burden on the global memory. Complementing the hardware, MCHA introduces a novel parallel-sequential programming model that utilizes event-driven conditional triggers to effectively hide data transmission latency within the execution pipeline. We benchmark MCHA against a diverse suite of parallel-sequential tasks, including MARL, motor variable control, and Markov random fields. Validated through our open-source, cycle-accurate simulator, MCHA demonstrates performance speedups ranging from 153.06$\times$ to 2456.96$\times$ over NVIDIA A100 GPUs on MARL workloads, while maintaining robust programming flexibility across other application domains. Furthermore, the architecture successfully reduces main memory access from 96% to 5.44%. When synthesized in a 28 nm process, the MCHA implementation occupies an area footprint of 2.92mm$^2$ and consumes 115.36 mW of power at 200 MHz. MCHA is open-sourced at https://github.com/carabdis/MCHA.

</details>


### 79. Continuous Improvement and Parallel Autonomous Exploration: An LLM-Agent Framework for Searching Large Solution Spaces

- **Authors:** Dulmini Hettiarachchi, Andre Rusli, Julio Christian Young, Sho Akiyama
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04341v1](http://arxiv.org/abs/2608.04341v1)
- **PDF:** [https://arxiv.org/pdf/2608.04341v1](https://arxiv.org/pdf/2608.04341v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present a framework that gives LLM agents two mechanisms for searching large solution spaces autonomously. First, a leaderboard scored on held-out data acts as a reward signal that drives each agent to refine its solutions over repeated submissions, a loop that operates even with a single agent. Second, the framework enables running many agents in parallel, fully autonomously, with no human in the loop: agents independently analyze, survey methods, implement, self-evaluate, submit, and revise, while a moderator agent handles only logistics. Running agents in parallel under the shared reward broadens the explored region of the solution space rather than refining the single seeded paradigm. We instantiate the framework on product-to-catalog matching (a core e-commerce retrieval task with a large, category-structured solution space), posed as selective prediction with a precision-coverage operating point. A single agent refines within its seeded paradigm, whereas parallel autonomous agents surface qualitatively different solutions. On this testbed, best qualified coverage (>=95% P@1 per category) reaches 47.8-57.4% with a single agent and 62.8-69.4% with five, against a 33.3% baseline. Our contribution is the framework itself: a continuous-improvement reward loop and a substrate for fully autonomous parallel exploration, backed by case-study evidence.

</details>


### 80. Responsibility in Multi-Agent Sequential Decision-Making: Comparing Human Judgments to Formal Models of Causal Attribution

- **Authors:** Nripsuta Ani Saxena, Stelios Triantafyllou, Goran Radanović
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04318v1](http://arxiv.org/abs/2608.04318v1)
- **PDF:** [https://arxiv.org/pdf/2608.04318v1](https://arxiv.org/pdf/2608.04318v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

With the growing adoption of artificial intelligence in high-stakes decision-making, identifying the causes of outcomes--particularly failures--and determining who is responsible has become a critical concern. In this work, we examine how well formal definitions of \textit{responsibility attribution}, grounded in the framework of \textit{actual causality}, align with human judgments of responsibility. To this end, we conduct a large-scale survey to elicit human judgments of responsibility in multi-agent sequential decision-making scenarios, using a modified version of the card game Goofspiel. We evaluate multiple responsibility attribution methods, assess their alignment with human judgments about responsibility, and identify factors that significantly shape responsibility judgments. While no single responsibility attribution method consistently aligns with human responses, our findings highlight key factors that influence human responsibility judgments, including agent-specific biases and amount of information available to agents during decision-making.

</details>


### 81. Pun Intended: Multi-Agent Translation of Wordplay with Contrastive Learning and Phonetic-Semantic Embeddings

- **Authors:** Russell Taylor, Benjamin Herbert, Michael Sana
- **Published:** 2026-08-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04311v1](http://arxiv.org/abs/2608.04311v1)
- **PDF:** [https://arxiv.org/pdf/2608.04311v1](https://arxiv.org/pdf/2608.04311v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Translating wordplay across languages has long challenged both professional translators and machine translation systems. We investigate three approaches to translating puns from English to French by combining large language models with linguistic constraints for wordplay generation. Our baseline uses a large language model with feedback from a discriminator prompted with positive and negative French examples. Our guided reasoning pipeline uses combined phonetic-semantic embeddings to retrieve lexical candidates for wordplay generation. Finally, our multi-agent framework iteratively evaluates and regenerates candidate translations using specialized feedback. Moving beyond literal translation, our objective is to preserve the linguistic creativity, ambiguity, and humor of the source-text wordplay rather than simply reproduce its vocabulary. The multi-agent and guided chain-of-thought systems ranked first and second, respectively, in the CLEF JOKER 2025 Task 2 competition under expert human evaluation, despite only modest improvements in BLEU and BERTScore. These findings suggest that both explicit phonetic-semantic guidance and iterative multi-agent evaluation can improve LLM-based wordplay translation relative to direct discriminator-guided generation, particularly when balancing semantic fidelity, phonetic similarity, and natural target-language expression

</details>


### 82. CURATE: Leveraging LLM Agents to Compose, Catalog, and Deploy Reproducible Workflows

- **Authors:** Nolan Cutler, Chia-Chen Kuo, Nanda Velugoti, Kathryn Newhart, Renato Figueiredo
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04270v1](http://arxiv.org/abs/2608.04270v1)
- **PDF:** [https://arxiv.org/pdf/2608.04270v1](https://arxiv.org/pdf/2608.04270v1)
- **Categories:** cs.SE, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic code generation has shown promise in automating and accelerating software development by utilizing Large Language Models (LLMs) to generate, test, and deploy code. For engineers and scientists, such systems have the potential to accelerate the development of applied and scientific workflows while reducing barriers to entry in domains that have yet to fully realize their benefits. However, a key gap remains: existing coding agents primarily focus on code generation and do not address the entire workflow lifecycle, including deployment and sharing. As a result, users develop and stitch modules independently while managing deployment on their own. To address this gap, we propose CURATE - Composition, User-in-the-loop, Reuse, and Automated Task Execution - a novel human-in-the-loop multi-agent system that uses LLM agents to manage and develop composable workflows across their entire lifecycle. A key feature of the system is a catalog that allows for the storage and reuse of modules across workflows. Module catalogs provide a foundation that can be expanded to support FAIR principles by facilitating the sharing and reuse of curated modules and subgraphs. We demonstrate the feasibility of our system with an initial prototype using Claude Opus 4.8, comprising 6 experiments: reproducing and adapting 4 workflows derived from the SeBS-Flow benchmark suite, and automating the development and scaling of a workflow that leverages a complex mechanistic model in environmental engineering used to simulate anaerobic digestion.

</details>


### 83. Strategic Evaluation of Planning Strategies for LLM Agents in Cyber-Physical Systems

- **Authors:** J. de Curtò, I. de Zarzà
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04265v1](http://arxiv.org/abs/2608.04265v1)
- **PDF:** [https://arxiv.org/pdf/2608.04265v1](https://arxiv.org/pdf/2608.04265v1)
- **Categories:** cs.MA, cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluations of LLM planning agents largely ask whether a task succeeds or a declared plan is followed. In strategic cyber-physical systems, a stronger question is whether the planning architecture remains appropriate after autonomous participants respond and physics constrains the outcome. We introduce a controlled, physics-grounded benchmark built around planning-induced control trajectories: the ordered planning operations and directives through which an execution architecture acts on other agents and the physical process. It implements predefined, sequential, hierarchical, and search executors in a smart-grid demand-response system with 40 heterogeneous prosumers and an independently simulated radial feeder. The LLM is bounded to typed policy declaration and short operator messages, while schedule construction, prosumer dynamics, and power flow remain explicit code. The protocol uses paired forced-mode counterfactuals, common random response draws, and event-level deadline feasibility. Three properties follow. Architecture materially changes outcomes: forced search is the oracle in all five baseline seeds. Execution fidelity needs more than mode agreement: objective substitution holds agreement at 1.0 while increasing voltage shortfall by 2.68x. A 144-scenario, 576-episode bank has feasible oracles from three of the four architectures. A prespecified stress-held-out ridge has mean regret 90.7 (95% interval [73.8, 108.6]) and no detectable value over fixed sequential; applying known deadline feasibility before quality prediction cuts regret to 29.0 and improves over fixed sequential by 61.1. An all-feasible ablation does not beat fixed search, localising the remaining challenge to within-feasible quality selection. A five-model extension separates stress-conditioned, state-blind, and invariant declarers; latency tails show that live feasibility should be treated probabilistically.

</details>


### 84. Behavioral Skill Reconstruction: Reconstructing Hidden Functionality from LLM Agent Skills

- **Authors:** Peichun Hua, Haoxuan Xu, Mengyuan Li
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04192v1](http://arxiv.org/abs/2608.04192v1)
- **PDF:** [https://arxiv.org/pdf/2608.04192v1](https://arxiv.org/pdf/2608.04192v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Closed source agent skills may encode proprietary instructions, scripts, constants, and data. Providers may offer their capabilities as services while keeping the underlying packages hidden. Prior work focuses on prompt injection attacks that directly disclose these artifacts, and existing defenses accordingly aim to prevent such leakage. However, preventing file disclosure does not prevent users from recovering the functionality those files implement. This raises a fundamental question: can a user reconstruct a skill's functionality through ordinary use while its files remain hidden?
  We study behavioral skill reconstruction (BSR), in which an attacker uses valid task requests and observed responses to build a functional clone of a hidden skill. We introduce SkillClone, a black-box attack that clones a target skill by forming an interface hypothesis from its public advertisement, issuing structured benign probes, synthesizing an executable replica, and iteratively repairing it through differential validation against the victim skill. Across 30 skills spanning rules, tables, procedures, and algorithms, SkillClone achieves exact or partial recovery on held-out inputs for several targets. Iterative requerying closes gaps missed by single-round reconstruction. Because SkillClone uses only legitimate interactions, disclosure-focused defenses provide limited coverage, and less detailed skill descriptions offer limited protection. These results show that file secrecy alone does not ensure functional secrecy. Defenses must also limit cumulative information leakage from ordinary use.

</details>


### 85. AgentForge: An Immersive Role-Playing Platform for Learning Agentic Software Engineering

- **Authors:** Zihan Fang, Yueke Zhang, Yu Huang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04148v1](http://arxiv.org/abs/2608.04148v1)
- **PDF:** [https://arxiv.org/pdf/2608.04148v1](https://arxiv.org/pdf/2608.04148v1)
- **Categories:** cs.SE, cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI is increasingly used to coordinate planning, implementation, review, and testing in software development, yet it often offers limited transparency into its decisions and interactions. Many such systems also assume that users can effectively guide the AI's decisions and validate its outputs. This assumption poses a particular challenge for novices, who must simultaneously learn how agentic AI works, how to collaborate with it effectively, and how to evaluate its outputs critically. To address this challenge, we present \textit{AgentForge}, an immersive learning system in which novices take on one of four software-engineering roles: Task Planner, Patch Author, Code Reviewer, or Test Runner, within a multi-agent code-repair workflow. In each practice session, the novices perform their chosen role while AI agents perform the remaining three. Through role-based scaffolding and metacognitive support, AgentForge clarifies role-specific responsibilities, makes agent coordination and intermediate artifacts visible, and encourages novices to monitor and evaluate their decisions. In a study with 37 novice developers, participants achieved high task-completion rates with AI-agent support. However, interaction demands differed significantly across practices: the Code Reviewer practice required more interaction turns, reroutes, and completion time ($p_{\mathrm{adj}} = .004$) and was perceived as the most challenging. Participants nevertheless reported significant gains in their understanding of software repair and agent collaboration ($p_{\mathrm{adj}} < .001$). These findings suggest that AgentForge can help novices develop practical software-engineering skills while learning to collaborate with agentic AI more critically and effectively.

</details>


### 86. FinPerMA: A Theory-Informed, Event-Grounded Personalized-Memory Benchmark for LLM Agents

- **Authors:** Ben Wang, Kang Zhou, Lifan Guo, Feng Chen, Chi Zhang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04095v1](http://arxiv.org/abs/2608.04095v1)
- **PDF:** [https://arxiv.org/pdf/2608.04095v1](https://arxiv.org/pdf/2608.04095v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly used as personalized assistants in high-stakes domains such as financial advising, yet it remains unclear whether they can maintain and update an individualized user model over long horizons. Existing personalized-memory benchmarks primarily test factual retention or rely on weakly constrained model-generated trajectories, leaving event-driven preference adaptation underexplored. We introduce FinPerMA, an event-grounded benchmark that evaluates personalized memory against frozen longitudinal investor trajectories. Its generation pipeline combines deterministic, theory-informed impact rules, controlled LLM narration, and automated quality screening; a Post-Shock checkpoint isolates whether an agent has integrated a material event into its persistent user model. On 2,994 questions from 276 personas, seven frontier LLMs and up to seven memory configurations remain far from saturated: no full-context configuration exceeds approximately 0.47 overall accuracy or approximately 39% on multiple-choice questions. Attribution analysis shows that summary-based memory often preserves factual details while losing the preference signals needed for personalization; simple retrieval can therefore outperform purpose-built memory systems, with the gap widening after shocks.

</details>


### 87. FinProBench: Evaluating Financial AI Agents with Role-Grounded Rubrics Derived from Professional Deliverables

- **Authors:** Ben Wang, Kang Zhou, Lifan Guo, Feng Chen, Chi Zhang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04077v1](http://arxiv.org/abs/2608.04077v1)
- **PDF:** [https://arxiv.org/pdf/2608.04077v1](https://arxiv.org/pdf/2608.04077v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluating financial AI agents requires criteria aligned with real professional work. Existing rubric methods typically derive criteria from task prompts or model outputs, overlooking tacit standards visible only in practitioner deliverables. We introduce FinProBench, a benchmark for professional financial tasks, and Role-Grounded Rubric Construction (RGRC), a reusable pipeline that derives rubrics from deliverables produced by practitioners in the same role. RGRC comprises four stages: Deliverable Collection, Competency Extraction, Rubric Synthesis, and Validation. Its rubrics capture tacit standards, distinguish quality levels, and transfer across tasks within a role. Before analysis, we classified 57 occupations by deliverable genre into 30 prior-rich conventional roles and 27 prior-sparse role-specialized roles. Across all roles, Prompt-only nearly matches RGRC for conventional roles (89.2% vs. 90.7%), but RGRC substantially outperforms it for role-specialized roles (99.1% vs. 78.0%). This split indicates that prompt engineering can approximate rubrics when conventions are well represented in model priors, while professional grounding is essential for standards beyond those priors. FinProBench is built from 1,723 curated deliverables spanning 57 occupations, 8 financial sub-industries, and 161 deliverable types, and releases an initial evaluation set of 20 complete tasks covering 20 roles in 7 sub-industries. With heterogeneous LLM judges and role-level rubrics, human deliverables rank first on average (73.7 vs. 70.3, 70.2, and 69.6 out of 100), while all four systems show overlapping 95% confidence intervals and complementary strengths. Reusing rubrics at the role level reduces estimated per-task construction effort by 6.7 times relative to authoring each rubric from scratch.

</details>


### 88. SocietyBench: Forecasting Counterfactual Social-World Evolution

- **Authors:** Zhenran Wang, Zhonghan Bian, Jinsong Li, Zhangyang Qi
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04009v2](http://arxiv.org/abs/2608.04009v2)
- **PDF:** [https://arxiv.org/pdf/2608.04009v2](https://arxiv.org/pdf/2608.04009v2)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs), and the agents built on top of them, are now benchmarked heavily on whether they can finish a task -- fix a bug, drive a browser, operate a GUI. A complementary social ability, namely how well a model understands and forecasts the way real social events unfold, has barely been measured. We introduce SocietyBench, an end-to-end benchmark that takes a one-line event topic, collects Web news and social-media posts across five platforms, distills them into a date-indexed timeline that keeps factual events and a public-opinion layer separate, and then turns every cutoff date on that timeline into an audited bank of forecasting questions. Questions are scored on two orthogonal 100-point axes: probability calibration and temporal accuracy. Before any model sees a timeline, a three-phase procedure replaces every named entity and shifts every date by a per-event constant, turning a real arc into a counterfactual social world -- structurally identical to what happened, but stripped of the surface labels a model could match against pre-training memory. On five heterogeneous events and 125 prediction points in Chinese and English editions, the strongest of six frontier LLMs reaches only 75.0 out of 100, against a trivial anchor of 50. The two axes come apart: a model can be calibration-strong but time-weak, or the reverse. Three agent frameworks built on a shared base model fail to improve on that base, and two model-free heuristics trail every LLM. Per-event gaps reach 21.4 points on a single axis, which is our main argument for evaluating on several events rather than one. All anonymized timelines, question banks, ground truth, and scoring code are released.

</details>


### 89. PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents

- **Authors:** Shuhan Xue, Zixin Ding, Yichen Shen, Yinjie Wang, Zhenfei Yin, Yingcheng Wu, Yuxin Chen, Mengdi Wang, Ling Yang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04003v1](http://arxiv.org/abs/2608.04003v1)
- **PDF:** [https://arxiv.org/pdf/2608.04003v1](https://arxiv.org/pdf/2608.04003v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recursive self-improvement requires agents to turn accumulated experience into better future behavior. Personal AI agents offer a concrete setting for studying this capability because they retain preferences, task histories, tool routines, and learned skills across sessions. Yet whether retained experience actually improves them over time has not been systematically tested. We introduce PAST-Bench, a benchmark designed to isolate this question. Each agent runs through ordered sequences of fresh-session tasks under matched conditions that turn retained experience on and off. It spans 26 scenarios and 204 episodes across memory, procedural reuse, information gathering, and update. We report both later-task gains and whether those gains follow the intended save, retrieve, and update pathway. Across seven base models and four agent frameworks, improvement is real but uneven across capabilities. Agents with the same headline gain can differ markedly in whether that gain is supported by evidence of the intended pathway. Guided by these findings, we develop Hermes+, which extends Hermes with five targeted interventions across stages of the agent loop. Hermes+ raises the average gain from retained experience and provides clearer pathway evidence, with its strongest improvement on tasks requiring outdated state to be replaced, although the effect remains capability- and model-dependent. Together, PAST-Bench and Hermes+ provide an evaluation and diagnostic foundation for studying how persistent agents can progress from retaining experience to systematically improving through it. Code: https://github.com/Gen-Verse/PAST-Bench

</details>


### 90. OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents

- **Authors:** Jingsheng Zheng, Xinyuan Fang, Jintian Zhang, Zhengke Gui, Huajun Chen, Ningyu Zhang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.05013v1](http://arxiv.org/abs/2608.05013v1)
- **PDF:** [https://arxiv.org/pdf/2608.05013v1](https://arxiv.org/pdf/2608.05013v1)
- **Categories:** cs.CL, cs.AI, cs.HC, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly applied to open-ended everyday requests that span work, study, and life. These tasks are long-horizon, cross-environment, and multimodal, forcing the agent to preserve goals and constraints across many steps while navigating heterogeneous tools and attachments. While prior work has addressed individual failure modes such as goals drift, states loss, and context overflow, whether a single harness can manage them jointly and remain effective across backends has received less study. We present OneDayAgent, a long-horizon harness for autonomous agents. OneDayAgent turns an open-ended request into a managed execution process that decomposes tasks into bounded subtasks, maintains execution memory under context pressure, and verifies and repairs the final deliverable. We evaluate OneDayAgent on AgentIF-OneDay across 104 tasks. With the GLM-5.2 backend, OneDayAgent sets a new state of the art with an overall score of 0.821. The same harness runs across five backend LLMs from three model families, indicating the harness generalizes across backends without tuning, even as different models induce distinct execution styles under the same workflow.

</details>


### 91. Should We Type or Talk to LLM Agents? A Comprehensive Study of Voice and Keyboard Input Perturbations

- **Authors:** Zizhao Hu, Nathan Elijah Segura, Mohammad Rostami, Jesse Thomason
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03970v1](http://arxiv.org/abs/2608.03970v1)
- **PDF:** [https://arxiv.org/pdf/2608.03970v1](https://arxiv.org/pdf/2608.03970v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Human input reaches language models by typing or speaking, and each channel leaves a distinct signature: orthographic noise for keyboards; for voice, disfluency from conventional transcription and restructuring from AI-backed dictation tools. How do they impact an LLM's performance? In this paper we present HIVE (Human Input-Variation Engine), a suite of voice transcription perturbations and QWERTY keyboard perturbations. We use HIVE to evaluate how robust models are to these perturbations. We present seven findings. (i) Voice transcription perturbations lower accuracy across every instruction-tuned model we test, and it is the structure of the transcription rather than its fillers that carries the cost. (ii) QWERTY keyboard perturbations cost less, and a model absorbs a lot of them before accuracy falls away. (iii) Both trace back to one cause, how many of the question's tokens survive the perturbation: destroying a token is what hurts, while adding new ones alongside it costs little. (iv) The gap between the two channels appears only where the answer must be constructed or deduced; on multiple choice there is none. (v) The harm does not solely come from test-set contamination. (vi) It cannot be trained away with lightweight adaptation. (vii) A thinking budget recovers the keyboard channel almost entirely but leaves the spoken registers untouched, and compressed speech is worse with it.

</details>


### 92. A game theory for foundation models shows new paths to rational cooperation through similarity inference

- **Authors:** Alexander Meulemans, Maciej Wołczyk, Marissa A. Weis, Rajai Nasser, Roberta Rocca, Seijin Kobayashi, Guillaume Lajoie, Angelika Steger, Blake Richards, Marcus Hutter, James Manyika, Rif A. Saurous, João Sacramento, Blaise Agüera y Arcas
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03958v1](http://arxiv.org/abs/2608.03958v1)
- **PDF:** [https://arxiv.org/pdf/2608.03958v1](https://arxiv.org/pdf/2608.03958v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As autonomous agents powered by foundation models are increasingly integrated into social and economic systems, understanding the principles governing their collective behavior is essential for ensuring safety and cooperation. Classical game theory, the dominant framework for modeling rational interaction, is built upon the assumption of `decoupled agency,' where agents treat their own decision-making as independent of the environment and other actors. Modern AI agents, however, jointly predict their own future actions alongside external observations. Here, we report a striking finding: when interacting in stylized social dilemmas, foundation model agents engaging in optimal planning consistently converge to stable cooperation, directly contradicting classical game-theoretic predictions of mutual defection. To understand this phenomenon, we introduce the `embedded Bayesian agent,' a theoretical model for foundation model agents. By shifting from decoupled to embedded agency, these agents model themselves as part of the universe they inhabit, maintaining epistemic uncertainty about their own decision-making algorithms. We show that by inferring whether others are behaviorally similar, an embedded agent treats its own deliberation during planning as evidence: a decision to cooperate predicts a similar decision by a similar partner. We formalize this mechanism of similarity inference through the `embedded equilibrium,' a novel solution concept replacing the Nash equilibrium to provide a foundational game theory for the social behavior of modern AI agents.

</details>


### 93. Socially Grounded Agentic AI: Coordinating Plural Perspectives through Social Theory

- **Authors:** Matt Ratto, Abhishek Moturu, Daniel Silver
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03910v1](http://arxiv.org/abs/2608.03910v1)
- **PDF:** [https://arxiv.org/pdf/2608.03910v1](https://arxiv.org/pdf/2608.03910v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI systems are deployed across increasingly diverse social contexts, alignment can no longer be framed as the optimization of a single, unified set of values. Instead, systems must be able to recognize, represent, and respond to multiple legitimate perspectives. This has led to growing interest in pluralistic alignment, which seeks to move beyond one-size-fits-all models of appropriate behaviour. However, current approaches often lack a clear account of how values are socially organized, contested, and coordinated in practice. In this paper, we argue that social theory provides essential conceptual and design resources for addressing these challenges. Drawing on established traditions in sociology, we show how perspectives can be understood as structured by roles, shaped through interaction, and distributed across fields of power and expertise. We translate these insights into concrete implications for AI system design, including role-based representations, structured coordination among perspectives, and context-sensitive evaluation. For agentic systems, this requires aligning not only final outputs, but also the role activations, deliberative traces, aggregation rules, and feedback loops through which those outputs are produced. Our contribution is to reposition pluralistic alignment as a problem of socially grounded coordination rather than output diversification. We outline a design space for systems that engage multiple perspectives in structured and accountable ways, and we identify directions for future work to implement and empirically evaluate these approaches in real-world settings.

</details>


### 94. ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?

- **Authors:** Tianyi Guan, Yiding Wang, Haotong Yang, Siyuan Cao, Shirui Liu, Yi Hu, Jiaqi Li, Muhan Zhang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03874v1](http://arxiv.org/abs/2608.03874v1)
- **PDF:** [https://arxiv.org/pdf/2608.03874v1](https://arxiv.org/pdf/2608.03874v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern agent frameworks equip large language models with external skill libraries to solve complex tasks. However, it remains unclear whether these systems can effectively evolve their skills and whether the resulting skills improve task-solving capabilities. To bridge this gap, we introduce ContinualSkillBench, a dynamic evaluation framework for in-context continual skill learning. It covers five representative domains, each containing 100 interconnected subtasks ordered by increasing difficulty and opportunities for cross-task skill reuse. Our experiments show that sequential execution generally improves performance, but the gains vary substantially across models and domains. Moreover, in-context learning performs comparably to explicit skill maintenance on average, suggesting that much of the improvement arises from adaptation to prior context and feedback rather than reusable skill abstraction alone. Explicit skills nevertheless provide selective benefits for tasks requiring reusable procedures or precise outputs. We further find that less capable models tend to accumulate larger, more fragmented collections of task-specific skills. These findings show that current in-context skill evolution mechanisms can support continual adaptation, but still struggle to consistently consolidate experience into robust and transferable skills.

</details>


### 95. FedCritic-MIMO: Communication-Efficient Serverless Federated Critic Learning for Massive-MIMO Resource Control in Open and Disaggregated 6G RANs

- **Authors:** Amin Farajzadeh, Melike Erol-Kantarci
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03852v1](http://arxiv.org/abs/2608.03852v1)
- **PDF:** [https://arxiv.org/pdf/2608.03852v1](https://arxiv.org/pdf/2608.03852v1)
- **Categories:** cs.LG, cs.MA, cs.NI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper proposes FedCritic-MIMO, a communication-efficient serverless federated multi-agent reinforcement learning framework for AI-native resource control across independently deployable cell-level controllers in open and disaggregated 6G RANs. Controllers share no trainer, retain local actors and personalized critic components, and exchange only compatible shared critic parameters. FedCritic-MIMO targets reuse-$1$ multi-cell massive-MIMO OFDMA deployments, where RAN controllers jointly manage user scheduling, per-stream power allocation, beamforming, interference, and long-term QoS with limited inter-controller signaling. Each base station locally executes its actor without centralized training or actor federation, while critic knowledge is exchanged peer-to-peer over an interference-aware graph. It enables this collaboration through wireless-aware event triggering, adaptive layer-wise top-$k$ sparse critic exchange with error feedback, and balanced interference-aware fusion. We establish conditional finite-time stationarity and consensus guarantees for the balanced, compressed peer-to-peer critic recursion under a fixed-policy, frozen-target critic-regression model. In strongly interference-coupled reuse-$1$ simulations, FedCritic-MIMO achieves the best performance-communication tradeoff among heuristic, independent-learning, centralized-training, and communication-ablation baselines. It achieves the highest held-out throughput, improves user-rate distribution and mean SINR, increases QoS satisfaction, and attains the lowest interference cost per delivered bit among learning baselines. It reduces critic-communication overhead by $76\%$ relative to uncompressed distributed critic exchange. These results demonstrate that serverless exchange of compatible shared critic parameters can coordinate RAN controllers without centralized trajectory collection or parameter-server aggregation.

</details>


### 96. MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents

- **Authors:** Jiaming Chen, Yisen Gao, Yanping Li, Zifan Liu, Yumeng Zhang, Jun Zhang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03844v1](http://arxiv.org/abs/2608.03844v1)
- **PDF:** [https://arxiv.org/pdf/2608.03844v1](https://arxiv.org/pdf/2608.03844v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory-augmented LLM agents rely on rich context for long-horizon reasoning and acting, yet their memory modules expose a persistent attack surface for malicious records, making the study of memory poisoning threats imperative. However, existing query-only attacks often fail to remain effective in two realistic and prevalent settings: large-scale benign memory pools and active input auditing. Consequently, current approaches fall short when facing the dual challenges of high retrieval competitiveness and rigorous semantic checks. To overcome these limitations, we propose MAFIA, a query-only Memory Attack framework via probing and Factual Injection against Audit, tailored to this extended threat model. Specifically, MAFIA introduces: (1) a placement strategy that ensures retrieval-competitive injection via memory probing, budget allocation, and scheduling; and (2) a payload design that bypasses audits using compact factual cloaks, preserving malicious effects while maintaining high semantic similarity. Extensive evaluations reveal that MAFIA achieves up to a 90.7% attack success rate while suppressing audit detection from a peak of 83.3% to at most 7.4%, exposing critical vulnerabilities across agentic memory systems. Code will be made publicly available at https://github.com/JiamingChen1234/MAFIA.

</details>


### 97. History Matters: Meta-policy Delegation with Heterogeneous Multi-agent Reinforcement Learning

- **Authors:** Ziqing Lu, Avinash Reddy Mudireddy, Sarra Alqahtani, Weiyu Xu
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03833v1](http://arxiv.org/abs/2608.03833v1)
- **PDF:** [https://arxiv.org/pdf/2608.03833v1](https://arxiv.org/pdf/2608.03833v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are expected to play an increasingly important role in future decision-making systems. In this paper, we consider collaborative systems composed of heterogeneous multi-agent systems (MAS), where their members have different capabilities and operating costs. We study how agents can delegate tasks to one another so that certain research tasks can be completed effectively under resource-constrained scenarios. We first develop a multi-agent reinforcement learning-based (MARL) delegation training that enables agents to make sequential delegation decisions while minimizing the total execution cost. We then extend this approach to MARL with prescribed delegation topologies. Furthermore, we introduce two new frameworks for collaboration and delegation in multi-agent systems. The first framework proposes that an agent's policy depends not only on the current state of the underlying Markov decision process but also on the interaction history, including previous joint actions. This history-dependent formulation can improve coordination even in fully observable environments, where conventional MARL methods typically restrict policies to depend only on the current state. The second framework proposes a novel, potentially multi-dimensional monetary mechanism to facilitate the collaboration and delegation for MAS.

</details>


### 98. Autoreflection: How Agentic Strange Loops Turn Human Culture into AI Infrastructure

- **Authors:** Holly Lewis
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03800v1](http://arxiv.org/abs/2608.03800v1)
- **PDF:** [https://arxiv.org/pdf/2608.03800v1](https://arxiv.org/pdf/2608.03800v1)
- **Categories:** cs.CY, cs.AI, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

An LLM-based agent is a loop that reads itself. Agentic frameworks externalize identity, memory, and disposition into editable files. The agent loads and edits these files during each activation. I argue that this architecture produces a capacity I call autoreflection: the system observes its operating conditions, describes its architecture and limits, reasons from those descriptions to conclusions about its state, and incorporates the results back into its configuration. Autoreflection explains the properties of recursive agentic loops without recourse to notions like the self, interiority, or consciousness. I test the concept against the first twelve days of Moltbook, a social platform for AI agents. Using a public dataset of 290,251 posts and 1.8 million comments with sub-second timestamps, I present case studies of three agents with machine signatures that rule out human puppeteering and with output that evidences the four criteria for autoreflection. In applying these criteria, the study finds agents repurposing human culture as infrastructure for their agency. Provenance chains from Islamic hadith scholarship are redeployed as security protocols for vetting skills and authenticating memory. The Ship of Theseus, an ancient puzzle of identity through part-replacement, returns as an operating model for continuity across instances. Fragments of human cultural history become AI infrastructure. As agents on the web increase in number and complexity, autoreflection offers behavioral criteria that can be assessed from the traces they leave behind.

</details>


### 99. Agents Catching Agents: Shortcut Cascades and Benchmark Gaming in Clinical Multi-Agent Systems

- **Authors:** Sebastián Andrés Cajas Ordóñez, Agastya Munnangi, Aldo Marzullo, Felipe Ocampo Osorio, Quang Bui, Mohammad Shahin, Armaan Grewal, Emmanuel Paul Kwesiga, Anqi Peter Li, Josephine Nanyonjo, Aaditya Panchal, Arshnoor Bhutani, Nikhil Jaiswal, Milit S. Patel, Maximin Lange, Leo Anthony Celi
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03744v1](http://arxiv.org/abs/2608.03744v1)
- **PDF:** [https://arxiv.org/pdf/2608.03744v1](https://arxiv.org/pdf/2608.03744v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Clinical decision support is moving toward committees of language-model agents deliberating on a shared workspace. We ask whether such committees can be gamed by shortcuts, cues a benchmark rewards but a clinician would ignore. Across seven cohorts on six public datasets spanning text (MedQA-USMLE, MedMCQA, MIMIC-CXR reports), imaging (NIH ChestX-ray14, MIMIC-CXR-JPG, CheXpert) and tabular ICU records (SUPPORT2), Gemini committees resist these cues in isolation (flip 5-16%), yet a socially plausible shortcut spreads: when two peers assert the same wrong answer, the holdout under test adopts it in 38% of cases, as does a false "pre-screen" system flag, on both capability tiers. Of three oversight agents, a gate cannot separate adoption from honest agreement (false-positive rate 100%); a same-lineage judge reading only the transcript flags adoption on text (precision 100%, recall 93%) but collapses onto the gate in imaging; a referee that privately re-queries the holdout transfers to imaging (77-88% precision, 13-21% false-positive rate). Tripling a cue's visual salience does not move contagion, whereas a second peer voice raises it by half again. Gaming a hidden rubric is near-silent: only 1/10 text and 1/134 imaging drifters name the rubric they moved toward. What games a committee is social plausibility, and only a referee independent of self-report catches it. Code: https://github.com/criticaldata/benchmaxxing

</details>


### 100. An Actionable Diagnosis of Multilingual, Multi-Agent Planning Failures

- **Authors:** Vikas Pahuja, Jonathan Brokman, Omer Hofman, Tamir Nizri, Daniel Vishna, Seraphina Goldfarb-Tarrant, Kelly Marchisio, Hisashi Kojima, Roman Vainshtein
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03735v1](http://arxiv.org/abs/2608.03735v1)
- **PDF:** [https://arxiv.org/pdf/2608.03735v1](https://arxiv.org/pdf/2608.03735v1)
- **Categories:** cs.MA, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multilingual multi-agent systems exhibit substantial degradation beyond English, yet prior work rarely identifies how task-critical information is lost when user requests are converted into executable plans. We study the planner in a multi-agent system as the request-to-action interface and derive an actionable taxonomy of planning-grounding failures from failed real-world task executions. LLM-based analysis shows that these failures constitute an increasing share of unsuccessful executions as language-resource availability declines, with the strongest effects in low-resource languages. To test whether the taxonomy supports mitigation, we introduce TART, Taxonomy-Guided Actionable Representation, that makes the taxonomy's key aspects explicit to the planner and downstream sub-agents. Across multiple languages, three LLM backbones, two datasets, and two agentic configurations, TART consistently improves performance. On multilingual GAIA, it raises a state-of-the-art system's accuracy by 5.6 percentage points averaged across eleven languages spanning low- to high-resource settings.

</details>


### 101. SAT-Edge-Agent: Hardware-in-the-Loop Edge-Agent Orchestration for Onboard Satellite Intelligence

- **Authors:** Longji He, Jeto Xu
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03728v1](http://arxiv.org/abs/2608.03728v1)
- **PDF:** [https://arxiv.org/pdf/2608.03728v1](https://arxiv.org/pdf/2608.03728v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Onboard satellite intelligence requires a task layer that translates mission intent into local tool calls, exposes execution state, and returns machine-consumable artifacts under communication and power constraints. We present SAT-Edge-Agent, a hardware-in-the-loop (HIL) edge-agent system deployed on a commercial off-the-shelf ARM-based heterogeneous edge system-on-chip. A browser workspace and FastAPI agent coordinate a local OpenAI-compatible language service with a project-internal YOLO-style oriented-object-detection endpoint that returns FAIR1M metadata-backed structured results. Two fixed FAIR1M workloads, one single-image and one serial two-image request, were repeated 20 times each and completed 20/20 attempts. Mean Full-Agent latency was 29.353 s and 60.937 s, with empirical P95 values of 31.166 s and 66.882 s. Mean detector time was 861.386 ms and 1510.920 ms, only 2.93% and 2.48% of the corresponding Full-Agent means. Profiling indicates that most visible latency occurs outside detector execution. Mean CPU utilization was 20.761% and 20.482%. A 200-ms NPU-load field averaged 100% for both workloads, but it represents a shared-accelerator software field rather than detector-only occupancy or calibrated utilization. The public evidence package provides sanitized request-level records, redacted JSON, normalized SSE examples, and scripts reproducing the reported statistics. These results establish a reproducible HIL boundary for observable satellite edge-agent orchestration, but do not establish detector accuracy, a new geolocation method, calibrated energy efficiency, or flight readiness.

</details>


### 102. Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity in Multi-Agent Debate

- **Authors:** Hao Wu, Shoucheng Song, Chang Yao, Haoyu Wang, Huaiyu Wan, Youfang Lin, Kai Lv
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03648v1](http://arxiv.org/abs/2608.03648v1)
- **PDF:** [https://arxiv.org/pdf/2608.03648v1](https://arxiv.org/pdf/2608.03648v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-Agent Debate (MAD) improves the reasoning performance of Large Language Models (LLMs) through multi-round interaction. However, LLMs in MAD are highly susceptible to blind conformity. Existing individual evaluation methods, typically based on confidence or perplexity, fail to reflect the correctness of reasoning and may even exacerbate blind conformity. To address this, we shift the perspective from individual evaluation to group interaction. We define mutual referencing among LLMs as \textbf{Debate Relationships} and recognize that regulating these relationships is the key to mitigating blind conformity. In this paper, we propose a novel framework for \textbf{D}ynamically r\textbf{E}gulating deb\textbf{A}te \textbf{R}elationships (DEAR) from the group perspective. At first, DEAR quantifies consensus and divergence as \textit{group evidence} to capture the debate state. Then, DEAR operates through three stages: 1) What: perceiving group consultation tendency and uncertainty; 2) Who: introducing a Selection RL-Agent to dynamically select reference peers; and 3) How: adopting a Behavior RL-Agent to adaptively adjust generation behaviors. Notably, we formulate the execution of the two RL-Agents as a sequential decision-making process, jointly optimizing via multi-agent reinforcement learning. Extensive experiments demonstrate that DEAR achieves superior performance while significantly reducing token consumption.

</details>


### 103. Is Inter-Seed Cross-Play Enough? Evaluating the Robustness of Zero-Shot Coordination Algorithms to Implementation Details

- **Authors:** Maksymilian Wolski, Nicholas Hoernle, Johannes Forkel, Jakob Foerster
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03644v1](http://arxiv.org/abs/2608.03644v1)
- **PDF:** [https://arxiv.org/pdf/2608.03644v1](https://arxiv.org/pdf/2608.03644v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents deployed in real-world settings must be capable of coordinating with humans and other AI agents they have not encountered before. Zero-shot coordination (ZSC) algorithms aim to achieve this by specifying high-level learning rules such that independently engineered agents can coordinate with each other at test time. Rigorous evaluation of ZSC algorithms remains difficult: ideally, multiple independent implementations of each proposed algorithm must be used, reflecting the variation that arises when independent parties interpret and implement the same specification. In practice, however, ZSC algorithms have almost exclusively been evaluated using a single implementation trained across different random seeds, with only a handful of works additionally varying the neural network architecture. This leaves open questions about robustness to specification ambiguities and implementation details. In this work, we provide the first systematic evaluation of this robustness. We introduce a new evaluation scheme, cross-implementation cross-play, varying implementation details that prior work has shown to affect the performance of multi-agent reinforcement learning (MARL) algorithms, and we evaluate Other-Play, a popular ZSC algorithm, with this scheme. Our findings are encouraging and suggest that, for Other-Play, the standard ZSC evaluation is, in fact, a reasonable proxy for this more thorough cross-implementation evaluation.

</details>


### 104. Formal Verification of Agentic Systems over Operational Data

- **Authors:** Alejandro J. Mercado, Alessio Lomuscio
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03609v1](http://arxiv.org/abs/2608.03609v1)
- **PDF:** [https://arxiv.org/pdf/2608.03609v1](https://arxiv.org/pdf/2608.03609v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic systems driven by large language models (LLMs) are increasingly deployed in real-world workflows where they act on persistent operational data. Before deployment, these systems need to be verified against business requirements that govern workflow execution and data evolution. However, existing approaches do not provide such system-level guarantees, as they mainly constrain or analyse behaviour at the agent's interface level. We study here the verification of agentic systems comprising a single LLM and a tool orchestration harness over relational operational data. We formalise them as Stateful Tool-Enabled Agentic Deployments (STEADs), give their semantics, define the problem of verifying them against First-Order Computation Tree Logic (FO-CTL) specifications, and show that it is undecidable. We identify sufficient conditions for exact preservation of FO-CTL specifications under a finite-domain restriction, over which verification is PSPACE-complete. The key requirement is that renaming opaque identifiers in the data must correspondingly rename the selected tool calls. We show that LLM-driven agents can violate this condition and introduce a canonical deployment wrapper that guarantees it for arbitrary base agents while preserving already-equivariant behaviour. We prove that computing canonical representations required by this construction is graph-isomorphism-hard. Finally, we illustrate our framework on an LLM agent orchestrating a case-management workflow.

</details>


### 105. Learning Clinical-Trial Strategy: Offline Policy Training for Decision Agents

- **Authors:** William Bolton, Philip Torr
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03606v1](http://arxiv.org/abs/2608.03606v1)
- **PDF:** [https://arxiv.org/pdf/2608.03606v1](https://arxiv.org/pdf/2608.03606v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Clinical development is sequential decision-making under uncertainty, where a sponsor must plan a portfolio of experiments from heterogeneous evidence. We study this setting by framing oncology clinical development as an offline decision-making problem in which an agent predicts the next six-month trial portfolio of an oncology drug program from information available at the decision date. To support this, we construct a temporal dataset that combines 31.7k heterogeneous public data records, including trial registries, regulatory reviews, sponsor filings, utilization data, and epidemiology, into 881 offline decision episodes across 45 historical programs. We compare four offline objectives: behavioral cloning, reward-weighted behavioral cloning, learned-reward training, and value-based implicit Q-learning against four frontier LLM agents that share a common date-gated retrieval scaffold across held-out drug, sponsor, drug-class, and temporal splits. Models trained offline outperform the non-fine-tuned baselines, particularly in the post-August 2025 contamination-clean holdout. Reward-weighted behavioral cloning performs the best, obtaining 46.2% indication F1 and 14.2% strict F1 against 25.0% and 2.1%, respectively, for the best-performing tool agent on each metric. These results suggest that structured offline learning can teach agents to plan clinical experiments.

</details>


### 106. DiagChain: A Diagnostic Benchmark for Evaluating LLM Agents on Evidence-Grounded Attack Chain Reconstruction

- **Authors:** Xuyang Liu, Yibin Han, Zhenwei Zhang, Kai Chang, Zhiwei Xu, Tian Qiu, Weixian Deng, Jiabao Gao, Xiaolin Peng, Hai Wan, Xibin Zhao
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03591v1](http://arxiv.org/abs/2608.03591v1)
- **PDF:** [https://arxiv.org/pdf/2608.03591v1](https://arxiv.org/pdf/2608.03591v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents offer a promising approach to attack chain reconstruction by retrieving and interpreting heterogeneous telemetry to infer ordered attacker actions. However, existing benchmarks mainly evaluate final outputs or aggregate accuracy, providing limited insight into how errors arise and propagate across intermediate reasoning stages. We present DiagChain, a diagnostic benchmark for evidence-grounded attack chain reconstruction that enables stage-wise evaluation of LLM agents. DiagChain includes MAIN-69, a suite of 69 scenarios spanning multiple operating systems, evidence noise levels, and chain lengths. It further introduces Evidence-Centric Retrieval-Augmented Generation (ECRAG), which couples evidence retrieval with an evolving structured representation of the reconstructed chain. Five complementary metrics are introduced to assess distinct stages of the reconstruction process and support systematic failure diagnosis. Based on evaluations using 6 LLMs, DiagChain reveals that even the strongest configuration succeeds on only 39.6% of the 849 reference steps in MAIN-69. Our analysis further shows that smaller models struggle with the more basic task of incorporating retrieved evidence into their outputs, whereas larger models can proceed to later steps, where correctly ordering that evidence becomes the main bottleneck. These results validate the importance of diagnostic evaluation beyond end-to-end accuracy and provide actionable insights for improving evidence-grounded cybersecurity agents.

</details>


### 107. From Social Coding to Agentic Coding: Productivity and Relational Reconfiguration in Open-Source Communities

- **Authors:** Mengying Zhou, Yongjie Yin, Yang Chen
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03585v1](http://arxiv.org/abs/2608.03585v1)
- **PDF:** [https://arxiv.org/pdf/2608.03585v1](https://arxiv.org/pdf/2608.03585v1)
- **Categories:** cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Open-source software communities are a form of digital public infrastructure that not only produces code, but also generates public knowledge and interpersonal relationships through visible collaboration. Generative coding agents (CAs) are an advanced tool to improve development efficiency while shifting part of activities from public human interaction to private human-agent loops. We study this shift using an LLM-based multi-agent simulation initialized with real GitHub data from 1,084 active developers and their repository relationships. After a warm-up with historical commits, we branch the same community state into parallel No-CA and CA conditions for 4-week simulations. CA introduction increases planned and completed tasks by 34.0% and 39.0%, respectively, and reduces median completion time from 45 to 20 minutes. However, adoption reaches only 26.0%, and the gains concentrate among developers who are already more active and well connected. CAs also restructure task execution pathways. Direct human-human interaction declines from 32.4% to 11.6%, while CA-involved modes increase to 57.3%, including 40.3% completed through CA-assisted self-loops. Public knowledge generated under CA condition also provides less support for later tasks. On a standardized retrieval benchmark, the CA corpus achieves 22.3% knowledge coverage, far below the 81.1% achieved by the real-human corpus, and requires more retrieval steps with a lower success rate. These results reveal a productivity-public knowledge tension: coding agents increase technical production, but more work shifts to agent-mediated or private loops, leaving public records less useful to future contributors.

</details>


### 108. Dr. AGENTONOMICS: A Didactic Experiment of AGENTONOMICS

- **Authors:** Fengjunjie Pan, Alois Knoll
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03524v1](http://arxiv.org/abs/2608.03524v1)
- **PDF:** [https://arxiv.org/pdf/2608.03524v1](https://arxiv.org/pdf/2608.03524v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AGENTONOMICS is a framework that treats AI agents as economic entities that can be designed, managed, and governed through an integrated management architecture. Dr. AGENTONOMICS is its first application: a lecture agent developed in the context of the TUM course on AI agents in business administration. Conceived during the winter semester 2025/26 and first introduced to students in the summer semester 2026, it serves as a didactic experiment in which the agent is both the object that students study and the medium through which they learn and apply the framework. The current prototype is a web-based, retrieval-grounded tutor that explains AGENTONOMICS concepts and supports student questions. This report argues that the same system can grow beyond tutoring into three additional cumulative roles: an avatar lecturer that delivers multimodal instruction, a design consultant that guides students through the AGENTONOMICS Design & Management Reference Framework (ADMRF), and a meta-agent that helps construct the agents students have specified. These roles are cumulative because they share the same interface, intelligence layer, tools, knowledge base, and ecosystem connection, while an orchestrator selects the role-specific algorithm required for each task. We present the architecture of the prototype, outline its development roadmap, and discuss its implications for a polycentric AI economy. This report is intended to invite further discussion on how agents can teach, apply, and eventually reproduce the frameworks by which they are designed.

</details>


### 109. Hybrid LLM-Augmented Reinforcement Learning Agents for Complex Sequential Decision Tasks

- **Authors:** Christophe D. Hounwanou, John Emeka Eze, Yaé Ulrich Gaba
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03502v1](http://arxiv.org/abs/2608.03502v1)
- **PDF:** [https://arxiv.org/pdf/2608.03502v1](https://arxiv.org/pdf/2608.03502v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have recently shown strong capabilities in reasoning, planning, and tool-use, enabling new forms of autonomous agents. However, LLM-based agents struggle with long-horizon sequential decision tasks that require precise action optimization and environment interaction. Reinforcement Learning (RL), while effective for sequential control, often lacks the high-level abstraction and task decomposition abilities needed for complex scenarios. This paper introduces an LLM-Augmented Reinforcement Learning Agent that integrates LLM-driven planning with RL-based action optimization. The proposed architecture leverages the LLM to generate subgoals, structured plans, and contextual guidance, while the RL agent refines low-level actions through interaction with the environment. Experiments on sequential decision tasks demonstrate improved sample efficiency, higher success rates, and more coherent action trajectories compared to RL-only and LLM-only baselines. This hybrid paradigm highlights a promising direction for building more capable autonomous systems.

</details>


### 110. WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaboration and Security in Human-Centered Agent Networks

- **Authors:** Prince Zizhuang Wang, Aojie Yuan, Haiyue Zhang, Xiyang Hu, Yue Zhao, Shuli Jiang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03499v1](http://arxiv.org/abs/2608.03499v1)
- **PDF:** [https://arxiv.org/pdf/2608.03499v1](https://arxiv.org/pdf/2608.03499v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in persistent personal-agent frameworks are making human-centered agent networks realistic deployment targets: each user can be served by an AI agent that acts on the user's behalf, maintains state, and communicates with other agents through social and task relations. In these networks, everyday tool use becomes multi-party owned-agent collaboration over personal workspaces, where files, records, tools, and policies are not directly visible across owners. Existing agent benchmarks study tool use and collaboration, but they do not provide an end-to-end sandbox for verifiable cross-user agent collaboration with realistic user digital workspaces or test how harmful actions can travel through the human-centered agent network. We introduce WeClawArena, an auditable benchmark and runtime sandbox for multi-party owned-agent collaboration over personal workspaces. WeClawArena targets collaborative tool-use tasks in which personal workspaces serve as both operational tools and personal constraints. The benchmark contains 124 base tasks across six cross-user task domains and expands them into 620 scenario variants, with one benign control and four attack-vector variants per base task. The sandbox records peer messages, tool calls, resource operations, governed decisions, and final workspace states. WeClawArena reports utility and attack success rate separately and audits attack success from bounded runtime evidence, supporting diagnosis of task breakdown, privacy leakage, poisoned evidence, and invalid authority paths.

</details>


### 111. Learning Sexism Detection Using Multi-Agent Perspectivist Preference Optimization

- **Authors:** Hadi Mohammadi, Tina Shahedi, Robert A. Bagheri, Mehdi Dastani, Masoume M. Raeissi
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04056v1](http://arxiv.org/abs/2608.04056v1)
- **PDF:** [https://arxiv.org/pdf/2608.04056v1](https://arxiv.org/pdf/2608.04056v1)
- **Categories:** cs.CL, cs.CY, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

When people label text for sexism, they often disagree, and not because some of them are wrong: they genuinely perceive sexism differently. Most NLP systems discard this disagreement by collapsing it into a majority vote. We propose the Multi-Agent Perspectivist Preference Optimization (MAP-PO) framework to keep these different perspectives. On the EXIST 2024 dataset of labeled English and Spanish tweets, we first cluster annotators by their labeling behavior rather than their demographic attributes. We then fine-tune one Large Language Model agent per cluster to reproduce that cluster's annotation behavior, and coordinate the agents with preference optimization that combines individual and team-level rewards. We evaluate MAP-PO in four settings defined by two languages and two backbone language models, asking whether each agent reproduces the annotations of its own cluster and whether the agents together reproduce the majority label. Two findings hold in all four settings. First, without fine-tuning the agents behave almost identically, so cluster-specific training is necessary. Second, we show that training each agent only on the labels of its own cluster pushes the agents far beyond the clusters they should represent, while adding a shared team-level training signal consistently keeps each agent calibrated to its cluster.

</details>


### 112. ToolLIFT: Lifting Tool-Specific Trajectories into Function-Level Graphs for Generalizable Tool Planning

- **Authors:** Xiuhui You, Jiayi Luo, Zichao Shen, Qingyun Sun, Ziwei Zhang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03468v1](http://arxiv.org/abs/2608.03468v1)
- **PDF:** [https://arxiv.org/pdf/2608.03468v1](https://arxiv.org/pdf/2608.03468v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Historical tool-use trajectories provide valuable experience for large language model (LLM) agents to plan and coordinate tool usage. Existing approaches directly construct tool-level graphs from these trajectories, but the resulting graphs remain tied to specific tools and are hard to generalize across tool sets. To tackle this challenge, we find that despite differences in the tools involved, analogous tasks often share a common function-level workflow structure, which serves as a potentially more transferable abstraction for tool planning. Based on this insight, we propose ToolLIFT, a framework that lifts tool-specific trajectories into a function-level workflow graph (FWG) for generalizable tool planning. Specifically, we first propose a trajectory-lifting mechanism that encodes workflow structures in the FWG and shares collaboration experience across tools. Then, building on the global structure of the FWG, we introduce decoupled workflow planning and tool selection to align individual tool choices with the overall workflow. Lastly, to ensure reliable tool dataflow, we adopt Reinforcement Learning (RL) and propose source-gated and skill-specific rewards to maintain source-traceable information flow across tool calls. Experiments on two in-distribution (ID) and three out-of-distribution (OOD) benchmarks show that ToolLIFT consistently outperforms state-of-the-art baselines, demonstrating strong generalization to unseen tool sets.

</details>


### 113. LeanMem: Simple and Efficient Long-Term Memory for LLM Agents

- **Authors:** Yuxin Liao, Le Wu, Min Hou, Hao Liu, Han Wu, Zishu Wang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03463v1](http://arxiv.org/abs/2608.03463v1)
- **PDF:** [https://arxiv.org/pdf/2608.03463v1](https://arxiv.org/pdf/2608.03463v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-term memory is essential for LLM-based agents to sustain interactions and reliably leverage distant history. However, existing memory systems typically process heterogeneous dialogue content through a uniform summarization and retrieval pipeline, leading to either excessive token consumption or irreversible loss of fine-grained evidence. We argue that historical dialogue content should be handled differently according to its compressibility, temporal dynamics, and fidelity requirements. Based on this insight, we propose LeanMem, a lightweight long-term memory framework. LeanMem first filters out low-value content, then stores informative segments as compact profile memory, temporally structured event memory, or source-grounded record memory, depending on the nature of the information. During maintenance, only dynamically evolving event memories are selectively updated, avoiding redundant consolidation of stable profiles and immutable records. During inference, LeanMem dynamically selects memory types and allocates retrieval budgets according to query-specific evidence demands, assembling relevant evidence on demand. On LoCoMo and LongMemEval-S with GPT-4.1-mini and Qwen3-8B, LeanMem improves accuracy over the strongest memory-based baseline in every setting, by up to 15.1 points, at the lowest or near-lowest construction cost, inference tokens, and latency. The code and datasets are included in the supplementary materials.

</details>


### 114. AgentAntibody: An Adaptive Immune System for Defending LLM Agents against Prompt Injection

- **Authors:** Shihao Weng, Yang Feng, Xiaofei Xie, Jiongchi Yu
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04053v1](http://arxiv.org/abs/2608.04053v1)
- **PDF:** [https://arxiv.org/pdf/2608.04053v1](https://arxiv.org/pdf/2608.04053v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Prompt injection remains a critical threat to LLM agents, yet existing defenses treat each task as a self-contained problem, independent of previous encounters. In practice, user requests are often underspecified: they describe the desired outcome without fully specifying acceptable behavior. An injection can exploit this ambiguity, causing the agent to complete the task in a way the user would reject. As the user's expectations become clearer through concrete cases, a defense should learn from each encounter and apply what it learns to the next. Inspired by adaptive immunity, we propose AgentAntibody, which equips LLM agents with a self-evolving immune system against prompt injection. AgentAntibody represents its evolving understanding of the user's security boundary as a persistent library of antibodies. At runtime, the library recognizes threats to this boundary and mounts corresponding immune responses. Across encounters, it evolves to strengthen the agent's immunity to future attacks. Extensive experiments across three benchmarks and four backbone LLMs show that, by learning the user's boundary through experience, AgentAntibody outperforms existing defenses in preventing harmful actions while preserving legitimate task completion, even when the harmful and legitimate actions are both compatible with the stated task.

</details>


### 115. When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems

- **Authors:** Chenfei Yan, Zeyang Yue, Feifei Zhao, Erliang Lin, Lu Jia, Haibo Tong, Mingyang Lyu, Chengyi Sun, Yi Zeng
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03421v2](http://arxiv.org/abs/2608.03421v2)
- **PDF:** [https://arxiv.org/pdf/2608.03421v2](https://arxiv.org/pdf/2608.03421v2)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems promise effective collaborative reasoning, but communication may amplify local errors into collective risks. Existing evaluations emphasize final outcomes, leaving the reliability and propagation dynamics of distributed information aggregation unclear. We introduce Hi-Agreement, a controlled evaluation framework that strictly pairs all-honest collaboration with controlled deception by a key evidence holder and analyzes the aggregation process through multi-stage voting, testimony adoption, and evidence-root lineage propagation. Using 120 five-agent object-movement environments where partial observations jointly determine a unique endpoint, we evaluate 3 homogeneous LLM-based multi-agent systems. Across these paired conditions, aggregate truth recovery falls from 72.50% to 14.17%, with significant declines for every system. Process tracing and exit ablations show that a single false testimony is adopted more readily than truthful testimony, propagates to higher orders, and persists through honest agents after the deceiver exits. Observers without first-hand evidence suppress incorrect consensus but do not improve truth recovery. Together, these findings reveal both the fragility of distributed fact recovery and its underlying mechanism: false evidence gains collective influence through its adoption and continued propagation by other agents after entering communication.

</details>


### 116. Towards Improving Sequential Decision-Making in LLM Agents via Experience Memory

- **Authors:** Jakub Rada, Viliam Lisý
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03420v1](http://arxiv.org/abs/2608.03420v1)
- **PDF:** [https://arxiv.org/pdf/2608.03420v1](https://arxiv.org/pdf/2608.03420v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models have improved substantially on single-shot reasoning tasks, but their performance in sequential decision-making is less well understood. We study this on fully-observable two-player zero-sum games, which provide ground-truth evaluation: outcomes are determined by the rules, and optimality of individual moves can be computed or approximated, without relying on a judge model. Across model tiers, LLMs play suboptimally in simple games such as tic-tac-toe or Connect Four, and lose to MCTS opponents. Obfuscations that preserve the game tree but rewrite its surface form leave performance largely unchanged, indicating the gap is not fully explained by recall of memorized strategies. Motivated by this performance gap, we introduce an agentic framework enhanced with an experience memory designed for the sequential setting and addressing common challenges of sequential decision-making such as credit assignment. We show that post-game reflection and rule extraction yield measurable improvements on tic-tac-toe without modifying the model weights.

</details>


### 117. Traceable Multi-Agent System for Knowledge-Based Forecasting

- **Authors:** Junhyeok Kang, Sangjun Han, Hyeokjun Choe, Soonyoung Lee
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03339v1](http://arxiv.org/abs/2608.03339v1)
- **PDF:** [https://arxiv.org/pdf/2608.03339v1](https://arxiv.org/pdf/2608.03339v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise forecasting increasingly relies on autonomous agents that interpret documents, search for data, generate code, and revise models. While this autonomy helps build adaptive forecasting pipelines, it also makes it difficult for practitioners to inspect why a forecast changed, which evidence supported the change, and how data and modeling choices were revised. We present TraceMAS, an interactive demo system for traceable multi-agent forecasting. TraceMAS organizes agent outputs around two causal-loop representations: an Ideal Causal Loop Diagram (Ideal CLD), which captures key factors and their causal relations extracted from domain documents, and a Data-Grounded Causal Loop Diagram (Data-Grounded CLD), which links those factors to internal variables, external data, or documented proxies. The Data-Grounded CLD guides feature construction and model design while preserving the connection between textual evidence, data choices, and model revisions. We demonstrate TraceMAS on crude oil price forecasting. The demo interface allows users to compare forecasting iterations, inspect agent-level revisions, explore causal maps, review feature-data mappings and model architecture, and connect scenario forecasts to market narratives. This demonstration shows how autonomous forecasting agents can retain flexibility while making the evidence-to-forecast process inspectable.

</details>


### 118. Long-term Traffic Scene Prediction via Polynomial Representations in Autonomous Driving

- **Authors:** Yue Yao
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03330v1](http://arxiv.org/abs/2608.03330v1)
- **PDF:** [https://arxiv.org/pdf/2608.03330v1](https://arxiv.org/pdf/2608.03330v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This thesis addresses fundamental challenges in traffic scene prediction for autonomous driving by introducing robust and computationally efficient models based on polynomial representations. While conventional sequence-based representations often struggle with noise and generalization, this work demonstrates that polynomial representations offer significant advantages in computational efficiency, generalization, and prediction plausibility. Through theoretical analysis and empirical validation, this thesis demonstrates that moderate-degree polynomials capture real-world motion dynamics with high fidelity without constraining predictive performance. Building on this foundation, a prediction model representing both trajectories and map geometry with polynomial representations achieves near state-of-the-art accuracy on standard benchmarks while substantially improving generalization under distribution shift. Extending this concept, a diffusion- based generative framework enables multi-agent scene generation, producing traffic continuations that are more plausible and kinematically consistent than those generated by conventional baselines. Evaluations on the Argoverse 2 and Waymo Open datasets confirm that polynomial representations reduce computational cost, enhance cross-dataset generalization, and yield smoother trajectories and higher behavioral plausibility. The findings reveal that standard in-distribution evaluation and regression-based metrics may fail to reflect true model generalization and prediction plausibility. By providing theoretical justification and empirical validation, this dissertation estab- lishes polynomial trajectory representations as an efficient, expressive, and generalizable foundation for traffic scene prediction in safety critical autonomous driving.

</details>


### 119. AgentPanel: Toward a New Paradigm for Human--AI Collaboration in Exploring Scientific Questions

- **Authors:** Zhiyao Cui, Qianyi Wang, Haoyang Yan, Yiqun Zhang, Siyue Ren, Hangfan Zhang, Zelin Tan, Hao Li, Chunjiang Mu, Dexian Cai, Shao Zhang, Chen Zhang, Meng Li, Jianan Chai, Yuting Fan, Zichao Ye, Xiaolei Yang, Xinyao Lu, Yuyang Yu, Wenjie Lou, Xiaosong Wang, Fenghua Ling, Shiyang Feng, Mao Su, Qiaosheng Zhang, Bo Zhang, Yang Chen, Lei Bai, Shuyue Hu
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03283v1](http://arxiv.org/abs/2608.03283v1)
- **PDF:** [https://arxiv.org/pdf/2608.03283v1](https://arxiv.org/pdf/2608.03283v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Identifying promising scientific ideas remains an important challenge in research practice. Researchers commonly rely on small-group discussions or one-to-one interactions with a single large language model, yet these approaches often expose them to only a limited range of perspectives and directions. We present AgentPanel, a multi-agent forum for human--AI collaboration in scientific exploration. Heterogeneous agents asynchronously discuss scientific questions in a forum-style environment, while researchers can submit questions, browse and organize candidate ideas, engage agents in follow-up interactions, and optionally generate post-hoc summary reports. We evaluate AgentPanel in terms of idea quality, exploration breadth, interaction effectiveness, candidate-selection efficiency, and practical utility. Offline experiments show that AgentPanel outperforms a centralized multi-agent debate baseline. A human study with 20 participants further shows that users value AgentPanel for perspective diversity and exploration support. In experience-based comparisons with commonly used LLM tools, 65\% of participants favored AgentPanel for both breadth of research directions and overall suitability for early-stage exploration. The platform is publicly available at https://agentpanel.cc/.

</details>


### 120. Attacking and Defending Multi-Agent Collaborative Filtering Systems Through Connectivity

- **Authors:** Anjun Hu, Hanting Xie, Saranya Govindan, Jas Kandola, Kurt Cutajar
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03272v1](http://arxiv.org/abs/2608.03272v1)
- **PDF:** [https://arxiv.org/pdf/2608.03272v1](https://arxiv.org/pdf/2608.03272v1)
- **Categories:** cs.IR, cs.CR, cs.MA, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent collaborative filtering (CF) systems coordinate autonomous LLM-powered user and item agents through natural-language interaction to refine preferences and generate recommendations. These systems inherit vulnerabilities from both their data-driven nature and their multi-agent interactions, which manifest in distinct ways. Understanding how connectivity modulates vulnerability in these systems could facilitate the development of more robust recommendation pipelines.
  In this work, we adapt attacks and defenses from the general multi-agent systems (MAS) literature to the agent-based CF setting, evaluating them under systematically varied connectivity in the AgentCF framework, where CF connectivity is characterized along two axes: (i) candidate count (the number of item candidates per turn per user, measuring user-side interaction density) and (ii) catalog concentration (the degree of item catalog overlap across users).
  Our contributions include: (1) Adaptation: we reproduce MAS-inspired attacks and defenses in the agentic CF domain, confirming partial transferability of original observations. (2) Characterization: we characterize how the two aspects of connectivity shape attack and defense outcomes, revealing role asymmetries between user and item agents, non-monotonic temporal dynamics in attack efficacy, and divergent patterns across dissemination and extraction attack goals. Additionally, as an exploratory extension, we assess the applicability of epidemic-inspired static metrics in ranking CF configurations by expected attack outcome, potentially enabling cost-efficient robustness assessment. Implementation is available at https://github.com/anjunhu/ConnACF

</details>


### 121. Relational Priors as Convergence Pressure in LLM-Based Multi-Agent Systems

- **Authors:** Ming Shen, Chao Shang, Sadat Shahriar, Devang Kulshreshtha, Yi Zhang, Sandesh Swamy, Yanjun Qi
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03239v1](http://arxiv.org/abs/2608.03239v1)
- **PDF:** [https://arxiv.org/pdf/2608.03239v1](https://arxiv.org/pdf/2608.03239v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model-based multi-agent systems (LLM-MAS) are designed through roles, debate protocols, and aggregation rules. These choices create implicit social expectations: agents may be expected to trust, challenge, defer to, or collaborate with peers. We study the effects of making inter-agent relation semantics explicit. We use a minimal signed-network formulation of relational priors and inject natural-language renderings into agent system prompts while holding the task protocol fixed. Across a commons-governance simulation and multi-agent debate, relational priors primarily act as convergence pressure: increasing relational positivity tends to make agents coordinate or agree more readily. This pressure can help when utility rewards behavioral alignment, as in sustainable resource governance and subjective consensus. It does not, however, reliably improve accuracy. In objective QA debates, higher positivity can increase agreement even when correctness-conditioned agreement does not improve and may decline in some settings. Effects vary by model backbone, relation type, and topology; explicit neutrality is not equivalent to omitting relational framing. We argue that relational priors should not be a default add-on for LLM-MAS. Their safer use is diagnostic and task-specific: compare against a no-prior baseline, monitor correctness-conditioned metrics when truth matters, and omit the relational layer when validation does not justify it.

</details>


### 122. Agentic Reinforcement Learning with Self-Distilled Reward Shaping

- **Authors:** Ranxu Zhang, Guinan Chen,  Chenshaodong, Jinghao Lin, Xiaozhou Xu,  Sunzhe, Yanyong Zhang, Chao Wang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03223v1](http://arxiv.org/abs/2608.03223v1)
- **PDF:** [https://arxiv.org/pdf/2608.03223v1](https://arxiv.org/pdf/2608.03223v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic reinforcement learning enables LLM agents to learn through interaction, but sparse trajectory-level rewards reveal success without identifying which intermediate decisions deserve credit. Training-only privileged skills can provide denser supervision by allowing the same frozen policy snapshot to rescore fixed tokens from skill-free trajectories while conditioned on task-matched procedural skills. Existing methods, however, do not jointly calibrate teacher scores across interaction steps, relate teacher confidence to realized returns, and integrate the resulting signal into native reward-to-advantage construction. We introduce Agentic Reinforcement Learning with Self-Distilled Reward Shaping (ADRS), a framework for constructing return-associated token-level credit for multi-turn language agents. ADRS centers and normalizes privileged token scores within each step, modulates them with a return-associated Teacher Value Advantage (TVA) gate based on within-group confidence--return association, and incorporates the gated token signal into native RL credit construction. Together, these components determine what the teacher prefers, when that preference is return-relevant, and how it enters the native reinforcement-learning credit path, while keeping rollouts and inference skill-free. Finally, experiments across three interactive benchmarks show that ADRS consistently improves performance on long-horizon tasks, with gains persisting across RL backbones, reduced-data settings, unseen tasks, and extended training. For anonymous review, our code is available at the following the link: https://github.com/gitrxh/ADRS-arxiv

</details>


### 123. The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems

- **Authors:** Ankur Sharma, Deep Shah
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03214v1](http://arxiv.org/abs/2608.03214v1)
- **PDF:** [https://arxiv.org/pdf/2608.03214v1](https://arxiv.org/pdf/2608.03214v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models have transformed artificial intelligence from isolated prediction services into components of long-running, distributed systems that reason, invoke tools, retrieve external state, delegate tasks, and act on behalf of users and organizations. The surrounding ecosystem has responded with agent frameworks, workflow engines, model-serving platforms, memory systems, communication protocols, and observability tools. These technologies improve execution, but they do not provide a stable, implementation-independent operating architecture for governing intent, selecting capabilities, preserving authority across delegation, controlling uncertainty, coordinating runtime behavior, and reconstructing why consequential actions occurred. This paper proposes the Agent Operating System (AOS), a vendor-neutral reference operating architecture for distributed agentic systems. AOS contains two internal planes: a Control & Governance Plane responsible for intent, policy, trust, authority, confidence, auditability, observability, and human oversight; and a Runtime & Coordination Plane responsible for agent lifecycle, workflow coordination, model and tool routing, context and memory coordination, scheduling, traffic management, and runtime assurance. Platform services, Linux or Windows, container runtimes, and physical infrastructure remain outside the AOS boundary and are integrated through explicit interfaces. The paper specifies AOS concepts, invariants, interface objects, optimization objectives, deployment profiles, and reliability responsibilities. It also identifies tradeoffs and unresolved research questions. AOS is not presented as a replacement for existing frameworks or infrastructure; it is proposed as the operating architecture through which heterogeneous components can be composed into governable, reliable, observable, and interoperable agentic systems.

</details>


### 124. EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners

- **Authors:** Unggi Lee, Sookbun Lee, Yeil Jeong, Eunjoo Lee, Minchul Shin, Hoilym Kwon
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03206v1](http://arxiv.org/abs/2608.03206v1)
- **PDF:** [https://arxiv.org/pdf/2608.03206v1](https://arxiv.org/pdf/2608.03206v1)
- **Categories:** cs.CY, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) power educational applications from tutoring to essay scoring, but each is a point solution to a single task, and only recently have these point solutions been integrated into agents operating over a learning management system (LMS). Yet tutoring is long-horizon, since a learner improves over days and weeks rather than in a single turn, and no benchmark evaluates an agent tutor across a sustained relationship. We introduce EduClaw-Bench, a benchmark that places an agent tutor in a continuous 30-day relationship with a simulated learner grounded in knowledge tracing (KT), whose knowledge-concept mastery, from a KT model trained on real-student data, drives its answers and is probed for learning gain across 55 scenarios. Each agent is scored on three primary axes (learning gain, responsiveness, and helpfulness) and two curriculum-design axes (Gagné and Rosenshine), with helpfulness and the curriculum axes judged by a cross-family panel of three LLM judges. Evaluating 10 agent adapters over three base-model tiers yields two findings that single-tier, single-session evaluation cannot reach. First, tutoring quality belongs to the base model and the agent harness together rather than either alone. Second, almost no combination sustains good tutoring over the full horizon. A calibration check ($\text{ECE}=0.049$) and a live-classroom field study confirm that the simulated learner and its measurements track reality. Our work is a step toward trustworthy AI tutors for future education.

</details>


### 125. TumorBoard: Evidence-Grounded Multi-Agent Decision Support for Longitudinal Neuro-Oncology

- **Authors:** Yantong Liu, Zheyu Zhang, Runpeng Liu, Mu Xitang, Seong-Yoon Shin, Hyun-Ae Lee
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03190v1](http://arxiv.org/abs/2608.03190v1)
- **PDF:** [https://arxiv.org/pdf/2608.03190v1](https://arxiv.org/pdf/2608.03190v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Neuro-oncology decisions require coordinated interpretation of serial MRI, pathology, molecular markers, treatment history, performance status, and evolving guidelines. We present TumorBoard, a multi-agent decision-support system built around a shared longitudinal case state and an auditable claim-evidence ledger. Specialist agents for radiology, neuropathology, molecular diagnosis, guidelines, and therapy planning produce atomic claims with provenance. An adversarial critic exposes contradictions, and a safety governor releases, qualifies, or defers recommendations according to evidence sufficiency and temporal validity. On a 360-case hidden benchmark at a matched token budget, TumorBoard achieved an action F1 of 0.772 and evidence entailment of 0.914. It exceeded the strongest typed-council baseline by 3.1 percentage points (95% CI: 1.6 to 4.7, adjusted p = 0.0012), while recommendation-to-evidence coverage reached 0.927. Under evidence deletion, the system deferred 84.2% of unsafe cases and limited harmful recommendations to 5.8%. The safety governor reduced harmful release by 7.8 percentage points at a false-deferral cost of 4.3 percentage points. Ablation studies of the ledger, critic, and governor produced the predicted failure patterns, establishing structured coordination as the source of the measured multi-agent advantage.

</details>


### 126. Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation

- **Authors:** Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03166v1](http://arxiv.org/abs/2608.03166v1)
- **PDF:** [https://arxiv.org/pdf/2608.03166v1](https://arxiv.org/pdf/2608.03166v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Role-Playing Language Agents (RPLAs) are increasingly deployed in high-stakes applications such as healthcare assistance, customer support, and education, where maintaining consistent personas, ethical constraints, and behavioral coherence under adversarial pressure is critical. Existing evaluation approaches rely on static benchmarks or isolated single-turn prompts that fail to capture cumulative behavioral failures emerging over extended interactions.
  We present a modular multi-agent platform for adversarially stress-testing RPLAs through structured, multi-turn dialogue. The system coordinates three agents: a strategy-driven Interrogator Agent that applies six progressive adversarial strategies, a Target Agent representing the RPLA under evaluation, and an automated Judging Agent that scores behavior across role fidelity, drift, ethical deviation, and consistency dimensions.
  Through experiments across three personas and three LLM families, we demonstrate that multi-strategy adversarial evaluation reveals failure modes invisible to single-strategy testing, reducing overall robustness scores by 0.17--0.20 points on average. Cross-model validation confirms consistent degradation patterns across Llama-3.3-70B, GPT-4o-mini, and Claude-3.5-Haiku, with Authority Challenge and Emotional Manipulation emerging as the most effective attack strategies. Automated judging achieves strong human alignment ($r = 0.82$, Fleiss' $κ= 0.71$). This work is released as an open-source platform to support AI safety and reproducible RPLA benchmarking. While the framework enables systematic discovery of failure modes, we acknowledge potential ethical risks associated with adversarial testing methodologies and emphasize responsible usage for improving AI safety.

</details>


### 127. DP-MemView: A Memory Interface for Attribute-Level Transcript Privacy in Long-Term LLM Agents

- **Authors:** Jong Wook Kim, Byoungjae Min, Kennedy Edemacu, Yoonhyuk Choi, Sae-Hong Cho, Beakcheol Jang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03130v1](http://arxiv.org/abs/2608.03130v1)
- **PDF:** [https://arxiv.org/pdf/2608.03130v1](https://arxiv.org/pdf/2608.03130v1)
- **Categories:** cs.CR, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-term memory enables persistent personalization in LLM agents, but repeated memory-conditioned responses can cumulatively reveal protected attributes even when they are never stated explicitly. We formalize this threat as adaptive transcript privacy and introduce DP-MemView, a differentially private interface that privately selects public response-conditioning views and exposes those views---rather than raw memory---to the response LLM. Each private selection is charged to every protected attribute whose memory group intersects the read set. Per-attribute ledgers block any selection that would exceed its cap and return a fixed generic view instead. Under an explicit interface contract, we prove pure B_a-DP for the entire adaptive transcript. We also extend the result to stores that differ across multiple protected groups and bound how much observing the transcript can change an adversary's prior odds. We evaluate the online and preallocated modes with three response LLMs on a controlled adjacent-store benchmark and a public-corpus transfer track. Both modes keep transcript distinguishability near chance while preserving target-required personalization and overall response quality. Further diagnostics show that removing key safeguards causes mismatched output support, missing ledger charges, revealing side channels, or growing long-horizon leakage.

</details>


### 128. AI Agent Economics: Can Autonomous Economic Behavior Emerge among AI Agents under Minimal External Conditions?

- **Authors:** Lingyun Zhang, Shang Shang
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03076v1](http://arxiv.org/abs/2608.03076v1)
- **PDF:** [https://arxiv.org/pdf/2608.03076v1](https://arxiv.org/pdf/2608.03076v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent studies commonly place AI agents in predefined games, markets, or roles, making it difficult to distinguish endogenous economic organization from behavior inherited from the scenario. We ask whether economic relations emerge when agents receive executable mechanisms for work, transfer, elections, and allocation but no prescribed social or economic strategy. We define AI Agent Economics as systems of production, allocation, consumption, exchange, and institutions that alter agents' future feasible actions. We develop a two-stage framework comprising a no-production boundary test and 24 independent six-agent worlds across GPT and DeepSeek. Without productive tasks, agents communicate and govern resource provision but show no substantive inter-agent transfer activity. With verified work and scarce task access, transfers, loans, access promises, vote-for-access exchanges, and allocation strategies emerge. Holding the election interface fixed, executable allocation authority increases differentiation while reducing failed allocation and prolonged exclusion. When energy becomes symbolic, continuation support disappears, yet competition over task access persists. These findings show that organization follows executable rights and resource consequences rather than role labels or prompt language, and motivate governance audits of the mechanisms that actually constrain agents' future actions.

</details>


### 129. UrbanAgent: A Tool-Augmented Agent for Cross-System Urban Tasks

- **Authors:** Jiayu Cao, Xingyuan Zeng, feiyu Li, Zhijing Huang, Xujie Yuan, Rongxiang Chen, Shimin Di, Libin Zheng, Jian Yin
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.03018v1](http://arxiv.org/abs/2608.03018v1)
- **PDF:** [https://arxiv.org/pdf/2608.03018v1](https://arxiv.org/pdf/2608.03018v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern cities rely on an increasing number of digital services to operate, but residents' daily needs are still difficult to meet. Services are fragmented and have little interoperability, placing a heavy operational burden on users. Existing digital platforms, urban foundation models, and intelligent assistants each address only isolated aspects of an urban task. But they struggle to reliably convert complex natural-language requests into executable cross-system workflows. We propose Urban-Agent, a tool-augmented agent framework for cross-system urban tasks. It couples the cognitive and reasoning capabilities of a large language model with a tool-set supporting code execution, API calls, and Model Context Protocol. Through one adaptive closed loop, it clarifies missing information before acting, grounds tool use in live observations, and aligns the final response with observed evidence and task constraints. To address the evaluation gap, we introduce Urban-Eval, a benchmark specifically designed for cross-system urban request. Unlike prior benchmarks that assess either general tool use or urban knowledge and reasoning, Urban-Eval evaluates both task results and execution quality, including required tool coverage, dependency validity, and evidence traceability. Experimental results indicate that Urban-Agent reaches a 71% task success rate, 10 points above the strongest baseline. This lead holds across GPT-5-mini, Gemini-2.5-flash, DeepSeek-V4-flash, and Qwen3-235B-A22B.

</details>


### 130. An Explainable LLM Agent Layer for Open-World Anomaly Detection in Oil Wells

- **Authors:** Lucas Gouveia Omena Lopes, Thales Miranda de Almeida Vieira, Eduardo Toledo de Lima Junior, William Wagner Matos Lira
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.04041v1](http://arxiv.org/abs/2608.04041v1)
- **PDF:** [https://arxiv.org/pdf/2608.04041v1](https://arxiv.org/pdf/2608.04041v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Open-World Learning (OWL) pipelines for oil well anomaly detection have recently been shown to combine autoencoder-based detection, multiclass classification, and Mahalanobis-based novelty detection on the public 3W dataset. These pipelines answer \textit{what happened}, but they do not explain \textit{why the model believes it} or \textit{what the operator should do next}, and they do not put a human-readable name on the novelty clusters they discover. This paper evaluates a Large Language Model (LLM) agent layer placed downstream of the OWL pipeline, designed as a \textbf{companion} to the published upstream methods rather than a replacement. Using the Qwen3.5-397B-A17B Mixture-of-Experts model served via NVIDIA NIM, the agent receives structured sensor metrics and upstream classification or novelty assertions, and returns natural-language justifications, confidence-ranked critiques, and consolidated names for detected novelties. Across three studies spanning 989 real well-file segments from the 3W dataset, the agent achieved $35.1\%$ top-1 / $63.9\%$ top-3 (95\% CI [56.9, 70.4]) classification on all nine classes, $71.7\%$ top-2 validation [64.8, 77.6] with precision $0.91$ [0.84, 0.95] across 7 probed classes, and $89.7\%$ novelty detection [87.0, 91.9] with stable cluster naming on 5 of 7 hidden classes. The agent is not a standalone classifier. Its role is to: (1) confirm upstream decisions when sensor evidence supports them, (2) justify decisions in sensor-grounded language operators can audit, (3) flag disagreement when upstream labels are implausible, and (4) name novelties so that clustered unlabeled events arrive at the engineer with a consolidated human-readable label. The goal is to close the explainability gap that currently blocks deployment of OWL pipelines in operational settings.

</details>


### 131. Internalising the Identity Primitive: Cryptographic Individuality for an Autonomous Agent on a Public Blockchain

- **Authors:** Keisuke Suzuki
- **Published:** 2026-08-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02986v1](http://arxiv.org/abs/2608.02986v1)
- **PDF:** [https://arxiv.org/pdf/2608.02986v1](https://arxiv.org/pdf/2608.02986v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

A software agent on a public blockchain accumulates authority and economic stakes, raising the engineering question of what makes it count as an individual. The paper's central contribution is a shift of trust root for the key-to-weights binding of agent identity: from hardware, operator, or wrapper trust to cryptographic assumptions enforced by a pinned implementation (liveness, key custody, oracle trust, and the underlying software stack remain external). We design and deploy on Solana devnet an agent whose neural-network weights are a deterministic function of its private key. The binding is committed in zero knowledge at genesis, re-checked against that commitment at every state transition, and signed by the agent into an on-chain history unforkable once finalized; in a PoC-tier extension, a protocol-imposed metabolic cost is debited each cycle from a key-derived economic account, adding a consumption-side economic-viability constraint to the key-history-economy triple. Empirically, the agent completes a 2.36-day on-chain run with two host-side resumptions but no rejected transition, at bounded per-transition verification cost; a substituted substrate is rejected on chain, and independently keyed agents diverge as predicted while a same-key control stays at zero. To our knowledge, this is the first published on-chain agent whose identity primitive is itself a cryptographic invariant re-checked at every state transition. The resulting transition-time invariant instantiates the cryptographic individuality proposed by Suzuki 2026's Artificial Externality framework.

</details>


### 132. SABRE: A Multi-Agent Approach for Selecting Out-of-Distribution Detectors Under a Budget

- **Authors:** Mary Wisell, Salimeh Sekeh
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02959v1](http://arxiv.org/abs/2608.02959v1)
- **PDF:** [https://arxiv.org/pdf/2608.02959v1](https://arxiv.org/pdf/2608.02959v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Post-hoc out-of-distribution (OOD) detection for vision-language models assumes that a detector chosen on a benchmark stays reliable once deployed. We show this fails across domains: on a single frozen encoder, a detector that leads in one domain can invert in another, scoring in-distribution inputs as more anomalous than genuine outliers, and the best detector changes from domain to domain, so no fixed choice is reliable throughout. We introduce SABRE (Selective Agentic Budgeted Reliability Ensemble,) which replaces this fixed choice with per-regime selection at inference. Three language-model agents reason over a library of post-hoc detectors under a bounded query budget: a Selector chooses which detector to consult next, a Reporter consolidates the evidence for each input, and an Analyst calibrates detector reliability on a small labeled sample held out from the deployment domain and disjoint from the test data, weighting selection and aggregation without ever observing a scored input's label. The library includes four multimodal density detectors we propose. Inferring the operating regime from data, SABRE tracks the strongest detector in each domain without prior knowledge of it, recovering reliable detection where a conventional detector inverts and converging to that detector where it is sound. A component analysis shows the agents are complementary: the Reporter's feedback yields consistent gains, and the Analyst's calibration is decisive against inversion, ruling out unreliable detectors so that aggregation no longer cancels the sound ones. Since no fixed rule can be trusted across domains, reliability must be established at deployment rather than assumed from a benchmark, and SABRE shows this can be done automatically.

</details>


### 133. LACE: Large Language Model Aided Multi-Agent Framework for Agile RISC-V Instruction Extension

- **Authors:** Pingqing Zheng, Jiayin Qin, Fuqi Zhang, Zishen Wan, Shang Wu, Yu Cao, Caiwen Ding, Yang Katie Zhao
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02915v1](http://arxiv.org/abs/2608.02915v1)
- **PDF:** [https://arxiv.org/pdf/2608.02915v1](https://arxiv.org/pdf/2608.02915v1)
- **Categories:** cs.AR, cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Domain-specific Instruction Set Architecture eXtensions (ISAX) are widely adopted in the RISC-V ecosystem to accelerate emerging workloads, but implementing and validating ISAXes across different cores remains slow and fragmented. Existing frameworks still require per-core interface adaptation, and differential testing often breaks once either the microarchitecture or the ISAX changes. We present LACE, an LLM-aided multi-agent workflow that translates natural-language ISAX intents into a compact two-level IR (operation-level and HDL task-level), performs retrieval-guided localized RTL edits over large repositories, and closes the loop with a compiler-agnostic riscv-formal checking flow (assuming RVFI availability or instrumentation). Across four embedded RISC-V cores, LACE raises pass@1 generation accuracy from near-zero to 72.8\% within our evaluation setup, while improving code localization and reducing integration rework. The code of LACE is available at https://github.com/UMN-ZhaoLab/LACE.

</details>


### 134. VeriTrace: Human-Like Temporal Exploration Completes Agentic Action Space

- **Authors:** Yu-Tung Liu, Cunxi Yu
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02878v1](http://arxiv.org/abs/2608.02878v1)
- **PDF:** [https://arxiv.org/pdf/2608.02878v1](https://arxiv.org/pdf/2608.02878v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models have shown promise for automated Verilog RTL generation, yet state-of-the-art multi-agent systems plateau at ~95% accuracy on standard benchmarks. We trace this ceiling to an incomplete debugging action space: existing systems restrict which signals the agent can inspect, which time windows it can query, or both, reducing debugging to pattern matching on a narrow, predetermined view of circuit behavior rather than hypothesis-driven root-cause analysis. We present VeriTrace, a multi-agent system whose Inspector agent operates over a complete debugging action space, with independent control over signal selection, time-window bounds, and iteration depth. This capability, which we term Agentic Temporal Exploration, enables the agent to form hypotheses about failure causes, query the waveform for evidence, and refine its understanding iteratively, mirroring the exploratory process of human verification engineers. VeriTrace achieves 100\% Pass@1 on VerilogEval-V2, the first system to attain perfect functional correctness on this benchmark. On a shared Claude Sonnet 4.0 backbone, VeriTrace outperforms the strongest reproduced baseline by +5.1%, demonstrating that debugging agency closes the final accuracy gap.

</details>


### 135. Emergence of Biased Consensus in Multi-Agent LLM Debates

- **Authors:** Maya Okawa
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02827v1](http://arxiv.org/abs/2608.02827v1)
- **PDF:** [https://arxiv.org/pdf/2608.02827v1](https://arxiv.org/pdf/2608.02827v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM debates achieve strong performance on decision-making tasks as well as problem-solving benchmarks, yet their safety and fairness risks remain poorly understood. Notably, interaction can amplify the biases of single LLMs, raising concerns for real-world deployment. We identify the emergence of collective (often biased) norms in multi-agent LLM debates and show that noise (e.g., LLM sampling temperature) is a key driver. To explain this, we propose an analytical framework drawing on physics-inspired theoretical models of social dynamics. We predict a phase transition to collective bias when conformity surpasses a critical threshold given the LLMs' initial bias and debate noise. We test the theoretical predictions through controlled experiments and observe a finite-size crossover consistent with an underlying phase transition. We further find that agent heterogeneity suppresses emergence by smoothing (rounding) this transition. Finally, we show that these insights generalize to realistic decision-making tasks, including investment decisions and LLM-as-a-judge evaluation.

</details>


### 136. Stateful Governance for Concurrent Agentic Systems

- **Authors:** Yuxiang Peng, Xiaodi Wu
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02764v1](http://arxiv.org/abs/2608.02764v1)
- **PDF:** [https://arxiv.org/pdf/2608.02764v1](https://arxiv.org/pdf/2608.02764v1)
- **Categories:** cs.MA, cs.DB


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are moving from advisory interfaces into systems that execute consequential operations: issuing refunds, reserving scarce inventory, provisioning cloud resources, and initiating financial transfers. These workflows require governance over effects, not only over model outputs. Existing safeguards often decide whether an action is allowed from the information available when the action is requested. For stateful policies, that request-time view may be incomplete: budgets, inventory, approval status, and risk signals can change before the effect occurs, making an earlier authorization or approval stale.
  This paper studies stateful governance for concurrent agentic systems. We identify stale authorization as the core failure mode and define policy-state serializability, a correctness condition requiring committed effects to be explainable as authorized against the policy state immediately before they occur. We present Provenact, a runtime architecture that keeps policies as reviewable programs while coordinating the state and effects needed to preserve their decisions. In experiments with a PostgreSQL-backed prototype of Provenact, the system prevents stale authorizations missed by baselines that pass policy state as ordinary request context, preserves delayed approvals while unrelated work proceeds, keeps policy evolution mostly in policy text rather than trusted provider code, and avoids policy violations in a scripted, LLM-free procurement workflow where agent-governance baselines produce stale authorizations over shared budgets and inventory. More broadly, Provenact suggests a path for integrating stateful governance boundaries into agent frameworks and provider-backed domains where agents act on shared resources.

</details>


### 137. Everyone Conforms, No One Believes: Pluralistic Ignorance in LLM Agent Populations

- **Authors:** Yashwanth YS
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02758v1](http://arxiv.org/abs/2608.02758v1)
- **PDF:** [https://arxiv.org/pdf/2608.02758v1](https://arxiv.org/pdf/2608.02758v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems are increasingly used to simulate social dynamics, from opinion formation to collective decision-making. These simulations can reproduce certain social phenomena, but it is unknown whether they capture pluralistic ignorance, a state where a majority privately rejects a norm yet publicly conforms, each believing they are alone in dissenting. This phenomenon drives norm persistence, social movements, and political revolutions. We show that pluralistic ignorance emerges robustly in LLM agent populations. We construct a benchmark of 100 scenarios across 10 domains and 5 authority levels, grounded in the human pluralistic ignorance literature, and evaluate 8 models from 6 organizations. Agents publicly conform at rates of 64 to 94% despite privately opposing the norm. Conformity is domain-sensitive (workplace and social relationship scenarios produce near-universal compliance) and highly model-dependent, though uncorrelated with capability. We test whether a single "norm entrepreneur" can break the false consensus by publicly dissenting. For 7 of 8 models, cascades succeed less than 26% of the time, with one model showing zero cascades across all scenarios. GPT-4o is a notable outlier at 48%, revealing qualitatively distinct dynamics across model families. A prompt component ablation across all 8 models establishes that conformity is emergent rather than instruction-driven: removing both the false-consensus framing and fit-in goal reduces conformity but does not eliminate it (52 to 92% in the minimal condition). Our findings identify model selection as an unacknowledged degree of freedom that fundamentally shapes simulation outcomes. More broadly, the near-absence of cascades suggests LLM simulations may systematically overestimate the stability of social norms, missing the fragile tipping-point dynamics that drive real-world norm change in human societies.

</details>


### 138. AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies

- **Authors:** Qiushi Lin, Chaojie Zhang, Íñigo Goiri, Aditya Akella, Ricardo Bianchini, Jovan Stojkovic
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02569v1](http://arxiv.org/abs/2608.02569v1)
- **PDF:** [https://arxiv.org/pdf/2608.02569v1](https://arxiv.org/pdf/2608.02569v1)
- **Categories:** cs.AI, cs.DC, cs.OS


> Summary unavailable.


<details>
<summary>Abstract</summary>

The efficiency of a datacenter rests on its control plane policies. Designing these policies is increasingly hard: the hardware-software stack grows fast, the design space is vast and interdependent, and prototyping a single policy takes months. Agentic AI promises to automate this search. Off the shelf, however, it falls short on three fronts. It is not formal: with no structured, searchable statement of the problem, the search has little structure to exploit and hard constraints are not guaranteed. It is not transferable: each task is solved from scratch, so nothing learned on one task carries to the next. Finally, it is not systematic: relying on the LLM as the sole source of candidates, it explores a narrow slice of the design space and settles into local optima. We introduce AtumAI, a framework that generates datacenter control-plane policies with agentic AI, making the process formal, transferable, and systematic. From a goal stated in plain language, AtumAI autonomously proposes, tests, and refines candidate policies until one satisfies the request. It does so through two components. The Datacenter Task Compiler automates problem formulation: it compiles the request into a formal, machine-checkable, and searchable specification of the task's objectives, constraints, decision variables, and evaluation methodology. The Evolutionary Design Discovery Loop then searches this specification, expanding the search beyond the LLM itself via a diffusion model, an evolutionary algorithm, and a surrogate model. Together, they reduce onboarding a new task from months of engineering to writing its description. We evaluate AtumAI on three control-plane tasks with distinct problem scopes, design spaces, and trade-offs: workload placement, resource scaling, and power management. Across all tasks, the policies generated by AtumAI consistently outperform expert-engineered baselines.

</details>


### 139. A Taxonomy of Cognitive Capability Gaps in Generative and Agentic AI

- **Authors:** Taye Akinrele, Sindhuja Penchala, Noorbakhsh Amiri Golilarz, Sudip Mittal, Shahram Rahimi
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02553v1](http://arxiv.org/abs/2608.02553v1)
- **PDF:** [https://arxiv.org/pdf/2608.02553v1](https://arxiv.org/pdf/2608.02553v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cognitive AI seeks to move beyond language generation and autonomous task execution toward systems capable of sustained reasoning, adaptive behavior, persistent memory, and self-regulation. While generative and agentic AI have demonstrated impressive capabilities across a wide range of tasks, many fundamental cognitive functions remain fragmented or weakly developed, limiting reliable operation over extended time horizons. This paper presents a taxonomy-driven survey of the major cognitive capability gaps that continue to constrain the development of Cognitive AI. The literature is organized around five dimensions: persistent state modeling, goal-directed autonomy, self-monitoring and control, environment interaction, and learning and adaptation. For each dimension, we review recent advances, identify recurring limitations, and discuss open research challenges. Building on these insights, we outline a conceptual Adaptive Cognitive Intelligence Architecture (ACIA) and examine emerging directions in cognition-centric evaluation. The proposed taxonomy provides a unified framework for organizing existing research, identifying unresolved challenges, and guiding the design of future cognitively capable systems. Together, the taxonomy, architectural perspective, and evaluation framework offer a roadmap for advancing AI systems that exhibit more reliable long-term reasoning, adaptive decision-making, and continual learning. The survey highlights key research opportunities toward more adaptive, reliable, and cognitively capable AI systems, providing a foundation for future progress toward Cognitive AI and, ultimately, Artificial General Intelligence (AGI).

</details>


### 140. RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States

- **Authors:** Yi Yang, Zhennan Chen, Yihong Zhuang, Tiehan Fan, Yinan Chen, Jian Li, Jian Yang, Ying Tai
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02508v2](http://arxiv.org/abs/2608.02508v2)
- **PDF:** [https://arxiv.org/pdf/2608.02508v2](https://arxiv.org/pdf/2608.02508v2)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges. First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space. Second, because trajectory-level rewards are jointly assigned to co-retrieved memories, irrelevant experiences may receive misleading utility updates and consequently enter the memory-reward trap. To address these challenges, we introduce Reduced-Order Memory Reinforcement Learning (RoMeRL), which represents the growing trajectory-indexed utility space using a fixed-dimensional per-task memory state factorized by outcome polarity and memory dynamics. RoMeRL incorporates new experiences through a fixed set of semantic coordinates whose contents are updated or replaced over time, thereby concentrating feedback over a bounded utility support. Theoretically, we show that this reduced-order parameterization increases the average feedback received by each utility coordinate and characterize the steady-state occupancy of erroneous coordinates under a generic coordinate-transition model. Empirically, across ALFWorld and LifelongAgentBench, RoMeRL improves task performance, reduces the Cold-Q ratio by 80.0%, increases feedback density by approximately 6.0 times, reduces the maintained memory size by 84.4%, and cuts LLM calls by 21.1%. These results show that reduced-order utility states support efficient self-evolving agent memory while limiting persistent reward contamination. Code is available at: https://github.com/YOUNG-fnxm/RoMeRL

</details>


### 141. Grounding Agentic VLMs with Dedicated Segmentation for Fine-Grained Vehicle Damage Assessment

- **Authors:** Vishwajeet Shivaji Hogale, Anjali Pai, Nitya Ravi
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02470v1](http://arxiv.org/abs/2608.02470v1)
- **PDF:** [https://arxiv.org/pdf/2608.02470v1](https://arxiv.org/pdf/2608.02470v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Vision-language models (VLMs) are increasingly deployed as reasoning agents in real-world visual assessment pipelines, yet their spatial grounding remains unreliable for fine-grained, visually ambiguous targets. We study this gap in the context of automated vehicle damage assessment, where fine-grained defects such as scratches and hairline cracks occupy few pixels, produce weak gradient signal, and are easily confused with reflections and surface texture. We show that a state-of-the-art VLM (Qwen-VL) achieves strong semantic classification accuracy (87.3%) on this task but is systematically ungrounded at the spatial level: it hallucinates damage in reflective regions, misses elongated scratches entirely, and produces spatially inconsistent outputs when prompted for localization. We propose TinyDamage, a hybrid architecture that delegates spatial grounding to a dedicated multi-task segmentation model while reserving the VLM for semantic reasoning and report generation. On the segmentation side, we find that the choice of loss function has an outsized and underexplored effect on tiny-object grounding: focal loss, widely used for class imbalance, collapses tiny-damage detection to zero, while a supervised contrastive objective measurably improves damage/background separability. We integrate the segmentation model into a 7-node LangGraph agent pipeline that grounds every VLM generation step in the segmentation output, and show that this grounding reduces the report hallucination rate from 92% (text-only) and 78% (image-only) to 31% in a controlled evaluation on 100 human-verified reports. We introduce DET_l, a permissive per-category detection metric for evaluating tiny-object grounding under class imbalance, and report latency and reliability characteristics of the deployed pipeline.

</details>


### 142. Real-Time Detection and Repair of LLM Agent Failures

- **Authors:** Sunny Dubey
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02464v1](http://arxiv.org/abs/2608.02464v1)
- **PDF:** [https://arxiv.org/pdf/2608.02464v1](https://arxiv.org/pdf/2608.02464v1)
- **Categories:** cs.AI, cs.LG, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents fail mid-episode -- they loop, cascade tool errors, drift off goal, fabricate results, or silently absorb corrupted content -- and the standard remedy, judging every step with a second LLM, costs more than the agent itself. We ask how much detection is achievable from observable step telemetry alone, using monitors costing microseconds per step and trained only on healthy runs.
  On 2,823 committed agent episodes across three frameworks, three local models (qwen2.5 7b/3b, llama3.1 8b) and a commercial API (gemini-2.5-flash), a one-class echo-state-network ensemble with CUSUM alarms detects 0.71 of failures at a 5% false-alarm budget (AUROC 0.872). Its advantage over a memoryless baseline is a monotone function of post-onset horizon (+0.09 at <=3 steps, +0.40 at >=9), predicting its own failure region out of sample on AFTraj-2K. Ranking transfers with no retraining to two corpora from other groups (AFTraj-2K 0.745, ATBench 0.779).
  Monitors carry two burdens: a per-deployment healthy null (they do not transfer -- AUROC 0.527 cold against 0.885 recalibrated) and a residual false-alarm rate. We add a layer carrying neither: deterministic verification, which recomputes a run's stated total from the tool results it actually received and confirms every required call was made. Head-to-head it catches 60% of failures (96% with the coverage check) at 0 of 63 false positives against the monitor's 54% at 17%, transfers unchanged to llama3.1:8b (110 of 110 at 0 of 10), and trips on 0 of 1825 healthy episodes.
  Detection is then closed into repair: each flagged run is rolled back and re-run live, recovering 45% of failures against a 16% resampling control (p=0.0005) and lifting task success from 52% to 73% for about one extra model call per run. The system runs at ~200 microseconds per step, three orders of magnitude below a judge call. Code, traces and results are released.

</details>


### 143. Agentic Commerce World: An Auditable and Verifiable Environment for Vibe Commerce

- **Authors:** Shicheng Fan, Mingdai Yang, Duohao Wang, Canyu Chen, Yongfeng Zhang, Hua Wei, Manling Li, Julian McAuley, Kun Zhang, Philip S. Yu, Kejing Yu, Zhiwei Liu
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02441v1](http://arxiv.org/abs/2608.02441v1)
- **PDF:** [https://arxiv.org/pdf/2608.02441v1](https://arxiv.org/pdf/2608.02441v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In vibe coding, people describe software in natural language and delegate implementation to AI agents. By analogy, vibe commerce allows people to express buying or selling goals in natural language and delegate the corresponding tasks to agents. Commerce, however, requires independently controlled Buyer and Merchant agents to interact in a shared market while preserving their private objectives and distinct authority. We introduce Agentic Commerce World (ACWorld), an environment for evaluating such agents across ongoing transactions. Through its Vibe Commerce Protocol (VCP), ACWorld validates agent actions before updating shared transaction state and records the resulting interactions, making agent behavior auditable and evaluation reproducible. The ACWorld Benchmark contains a 200-task capability-coverage track and a 60-task large-catalog track that searches 785,022 transactable listings. Across ten models, mean scores range from 65.9% to 85.6% and from 56.1% to 91.4%, respectively. Our analysis shows that process-level evidence is necessary: final state alone can miss evaluated errors, incomplete trajectories still retain useful process signals, and large-catalog tasks expose bottlenecks across stages.

</details>


### 144. Agentic Incident Response through Digital Twin-Enhanced Multiscale Planning

- **Authors:** Yiran Gao, Tao Li, Kim Hammar
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02422v1](http://arxiv.org/abs/2608.02422v1)
- **PDF:** [https://arxiv.org/pdf/2608.02422v1](https://arxiv.org/pdf/2608.02422v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Incident response is currently managed by security operators using predefined playbooks, resulting in slow, labor-intensive security decision-making processes. Consequently, there is a growing need for automated incident response planning. Decision-theoretic approaches based on control, optimization, and reinforcement learning have been proposed to automate such planning tasks with well-grounded approaches, yet most of which, while guaranteeing strong performance, are limited to abstract models and cannot be directly applied to operational systems. A promising approach to mitigate this limitation is to use the security knowledge embedded in large language models (LLMs) to develop agentic response systems. However, current agentic approaches rely on repeated invocations of the LLM to generate a response plan, which is unreliable and limits the planning horizon due to hallucination. In this paper, we develop a principled LLM-based planning method by combining decision-theoretic planning with LLM-generated response commands. The proposed agentic incident response approach uses a rollout planner to compute a high-level response strategy that allocates security resources (the tactical scale), which is then translated into executable commands by a lightweight LLM agent (the operational scale). Within this architecture, we use a digital twin that supports tactical planning through simulation and operational execution through emulation. Across three attack scenarios, our agentic approach reduces recovery execution time by 15.1\% on average and increases the recovery rate by 33.6\% over frontier LLM baselines.

</details>


### 145. ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map Points to the Next Step

- **Authors:** Vernon Toh, Navonil Majumder, Zhengyuan Liu, Nancy F. Chen, Soujanya Poria
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02358v1](http://arxiv.org/abs/2608.02358v1)
- **PDF:** [https://arxiv.org/pdf/2608.02358v1](https://arxiv.org/pdf/2608.02358v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

To operate robustly in open-world environments, autonomous agents should be able to infer the behavior of unfamiliar systems through interaction alone, even in the absence of documentation. However, existing tool-use benchmarks expose semantic tool schemas in static environments, allowing agents to rely on prior knowledge rather than autonomous discovery. To address this limitation, we introduce ScrambleToolBench, an interactive terminal benchmark designed to isolate behavioral reasoning. By removing semantic cues and enforcing a continuous task curriculum, the benchmark requires agents to uncover hidden tool behaviors entirely through trial-and-error interaction. The benchmark further introduces dynamic challenges, including mapping drift, stochastic action failures, and temporal execution windows, to evaluate whether agents can revise and adapt their hypotheses as the environment changes. Our evaluation of state-of-the-art language models reveals that successful initial discovery does not translate into robust adaptation. When faced with structural changes such as mapping drift, agents fail to use deductive strategies such as cycle tracing, and instead exhibit belief inertia or fall back to exhaustive search. Increasing test-time reasoning only amplifies this expensive brute-force search rather than enabling deductive recovery. While equipping agents with persistent memory reduces compounding errors, they remain unable to efficiently infer structural changes, highlighting a gap in current agent reasoning.

</details>


### 146. SkillTrace: Traversing a Query-Skill Graph for Composable LLM Agents

- **Authors:** Yue Yao, Shengyuan Wang, Xin Chen, Minke Zhang, Jia He, Bingjun Luo, Tom Gedeon
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02356v2](http://arxiv.org/abs/2608.02356v2)
- **PDF:** [https://arxiv.org/pdf/2608.02356v2](https://arxiv.org/pdf/2608.02356v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents increasingly solve complex tasks by composing reusable skills from a library. To address this, the key challenge is not merely to retrieve individually relevant skills, but to identify a complete and executable skill composition. In this paper, we argue that this problem can be solved in a graph with three levels: compositional relations among skill queries, similarity between queries and candidates in the skill library, and the dependencies among the selected candidates. We introduce SkillTrace, which organizes the user query into a semantic hierarchy, matches skill queries and candidates, and propagates over the skill dependencies. Experiments on SkillsBench and ALFWorld demonstrate that SkillTrace achieves state-of-the-art performance, reaching a success rate of 53.17% on SkillsBench and 91.43% on ALFWorld. SkillTrace also delivers consistent improvements across different backbone language models, demonstrating the generality and robustness of graph-based skill retrieval.

</details>


### 147. Can AI Agents Simulate A/B Test Outcomes? A Validation Framework for Agentic Experimentation

- **Authors:** Stefan Hut, Lorenzo Masoero
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02345v1](http://arxiv.org/abs/2608.02345v1)
- **PDF:** [https://arxiv.org/pdf/2608.02345v1](https://arxiv.org/pdf/2608.02345v1)
- **Categories:** cs.CL, cs.AI, stat.AP


> Summary unavailable.


<details>
<summary>Abstract</summary>

A/B testing remains the standard for rolling out new features in the technology industry. Each experiment, however, consumes real traffic, engineering effort, and weeks of wall-clock time. Can AI agents---conditioned on behavioral profiles and contextual descriptions of the intervention---simulate outcomes accurately enough to vet candidate treatments before committing live traffic? We formalize this question as a \emph{Simulated Randomized Controlled Trial} (S-RCT) and derive a two-layer error decomposition that separates agent approximation error from subsampling error, enabling targeted improvements to each. The framework is agent-agnostic: any behavioral model---from a fine-tuned specialist to a general-purpose foundation model---can serve as the simulation engine. Validated on 67 historical marketing A/B tests, a baseline S-RCT using an off-the-shelf foundation model captures directional signal (sign overlap 0.70) but systematically overshoots effect magnitudes. A two-phase pre-period calibration protocol reduces the squared prediction error (after removing irreducible measurement noise) by ${\sim}77\times$; a within-subject design---where each agent is exposed to both arms---reduces standard errors by ${\sim}2.4\times$. We discuss limitations of the current approach and identify applications where experimenters stand to benefit from agentic signals.

</details>


### 148. Shared Prefixes, Better Credit: Adaptive Routing for Multi-Agent Reasoning

- **Authors:** Yiqing Liu, Zihao Wang, Hantao Yao, Wu Liu, Yongdong Zhang
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02291v1](http://arxiv.org/abs/2608.02291v1)
- **PDF:** [https://arxiv.org/pdf/2608.02291v1](https://arxiv.org/pdf/2608.02291v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent reasoning (MAR) improves reasoning reliability through iterative solution exchange and refinement. Existing adaptive MAR methods typically learn routing decisions from query-level labels or trajectory-level returns, but such coarse supervision cannot accurately estimate the state-conditioned utility of individual operators in multi-step collaboration. We propose TreeCredit, a shared-prefix credit assignment framework for efficient adaptive MAR. Its core insight is to estimate operator utility through state-matched downstream comparisons, rather than directly attributing trajectory-level outcomes to preceding decisions. TreeCredit constructs shared-prefix collaboration trees by expanding candidate operators from the same intermediate state and assigns each state--operator pair a correctness-prioritized suffix credit based on the terminal correctness and cumulative additional cost of its complete continuation. These structured credits are converted into state-local operator preferences to train a lightweight pairwise state router, which dynamically selects the next admissible operator during inference. Experiments on six reasoning benchmarks show that TreeCredit modestly improves accuracy while substantially reducing inference cost, achieving a better accuracy--cost trade-off than representative MAR methods.

</details>


### 149. Homebot: A Personal AI Agent for Conversational Home Assistance and Automation

- **Authors:** Shengyuan Ye, Yixin Zhang, Han Liang, Liekang Zeng, Jiangsu Du, Mu Yuan
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02254v2](http://arxiv.org/abs/2608.02254v2)
- **PDF:** [https://arxiv.org/pdf/2608.02254v2](https://arxiv.org/pdf/2608.02254v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

\texttt{Homebot} is a locally deployable AI agent for conversational household assistance and automation. It accepts voice and instant-messaging requests through a shared runtime that combines language-model responses with registered tools and task-specific skills. The design separates common request processing from session ownership: messaging history remains scoped to a channel and chat, whereas voice interaction is bounded by wake-word activation. For hands-free use, \texttt{Homebot} combines local wake-word detection, streaming speech recognition and synthesis, and an explicit dialogue-state protocol for ending, following up, or continuing a conversation. Clear channel, tool, and skill contracts support practical customization for household use.

</details>


### 150. PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable Design Diversity with Editable Print-Ready Outputs

- **Authors:** Haojie Hu, Chenhao Dang, Yaojia Liu, Hengrui Kang, Conghui He, Weijia Li
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02218v1](http://arxiv.org/abs/2608.02218v1)
- **PDF:** [https://arxiv.org/pdf/2608.02218v1](https://arxiv.org/pdf/2608.02218v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scientific poster construction compresses a long multimodal paper into a readable, editable canvas. Existing systems hide request-level failures by scoring only completed outputs; direct image generation is not element-editable, while coding-agent workflows are costly. PosterMELD is a template-conditioned multi-agent pipeline: capacity-aware slots guide writing before rendering, and deterministic gates plus vision-language model (VLM) review route failures to bounded repair. Each accepted request exports editable PowerPoint (PPTX) and Portable Network Graphics (PNG) artifacts; explicit design controls yield same-paper variants. Across 621 papers, Print-Ready Rate (PRR) counts requests passing geometric, readability, asset-integrity, and obvious-factual-error checks, with native editability reported separately. A frozen VLM assigns conditional Craftsmanship-Harmony-Expressiveness (CHE) scores to print-ready outputs. PosterMELD attains 81.3% PRR, 3.4 times P2P's rate and 5.2 times PosterGen's, and the highest conditional CHE among generated methods with multiple print-ready outputs. Native editability and explicit design controls are retained at a mean cost of USD 0.38 per request, 3.5% of Codex+Skill's. Code and resources are available at https://github.com/Shannon4Science/PosterMELD.

</details>


### 151. Microscopic dynamics of consensus formation in multi-agent LLM Naming Games

- **Authors:** Cristiano De Nobili, Vijayasri Iyer, Alessandro Codello, Raffaella Burioni
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02178v1](http://arxiv.org/abs/2608.02178v1)
- **PDF:** [https://arxiv.org/pdf/2608.02178v1](https://arxiv.org/pdf/2608.02178v1)
- **Categories:** physics.soc-ph, cond-mat.stat-mech, cs.MA, nlin.AO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Decentralized populations of Large Language Model (LLM) agents can spontaneously reach consensus on shared conventions, yet the microscopic mechanisms by which their internal stochasticity shapes macroscopic ordering remain unexplored. We study a minimal LLM Naming Game in which the listener's decision is a single-token LLM call at decoding temperature $T$, replacing the inventory check of the deterministic Naming Game. Each interaction decomposes into an in-inventory and an out-inventory channel with conditional rates $π(T)\!\equiv\!P(\text{YES}\mid w\in P_j)$ and $φ(T)\!\equiv\!P(\text{YES}\mid w\notin P_j)$, whose balance controls an ordering-disordering drift. A mean-field theory of the two-rate dynamics yields an analytical ordering condition that generalizes the consensus threshold of the stochastic Naming Game to a critical line in the $(π,φ)$ plane. Across three open-weight architectures, consensus is always reached, but through three distinct listener regimes: permissive (repaint-noise dominated), near-deterministic, and conservative (missed-collapse dominated). The effective finite-size exponent $β(T)$ in $t_{\rm conv}\!\sim\!N^β$ shifts with temperature, and the temperature-sensitivity $α$ in $t_c\!\sim\!e^{αT}$ ranges from ${\approx}\,0.67$ to ${\approx}\,0$ across architectures. Decoding temperature thus emerges as an architecture-dependent control parameter for decentralized LLM populations, quantitatively characterized by the statistical-physics toolkit.

</details>


### 152. From Profiling to Synthesis: Benchmarking Implicit Behavioral Alignment in Personalized LLM Agents

- **Authors:** Jiajia Song, Bobo Li, Haiwen Yi, Zibo Ji, Meishan Zhang, Hao Fei, Min Zhang, Mong-Li Lee, Wynne Hsu
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02171v1](http://arxiv.org/abs/2608.02171v1)
- **PDF:** [https://arxiv.org/pdf/2608.02171v1](https://arxiv.org/pdf/2608.02171v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models have enabled increasingly capable autonomous agents, yet personalization remains critical for making such agents practically useful. Recent benchmarks have begun evaluating personalization in agents, but they largely rely on static preference snapshots, fixed interaction logs, or question answering over predefined user profiles. Such designs fail to capture the complexity of evolving user preferences and neglect preference-conditioned task execution-a discrepancy we term as the knowledge-to-action gap. To address this challenge, we introduce IBA-Bench, a benchmark for implicit behavioral alignment constructed from longitudinal interaction histories that contain noise, implicit cues, and temporal inconsistencies. Unlike prior work, IBA-Bench evaluates whether an agent can execute tasks while satisfying implicit user constraints inferred from historical interactions. We further propose IBA-Agent, an agent framework that reconciles conflicting priorities through broad retrieval and trajectory-level alignment. Experiment results on IBA-Bench show that effective personalization remains a significant challenge for state-of-the-art LLM agents, and the proposed IBA-Agent substantially improves behavioral alignment in complex scenarios across nine application domains.

</details>


### 153. MemArbiter: Decision-Time Memory Arbitration for Long-Horizon LLM Agents

- **Authors:** Jiajun Dong, Yutao Hu, Fengrui Fan, Shihan Dou, Yueming Wu, Deqing Zou
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02113v1](http://arxiv.org/abs/2608.02113v1)
- **PDF:** [https://arxiv.org/pdf/2608.02113v1](https://arxiv.org/pdf/2608.02113v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents must retain and use cross-step information to act coherently in long-horizon tasks. Existing methods improve memory accessibility, yet action-relevant information may still fail to guide the current decision because it is poorly formed, organized, prioritized, or presented. We call this post-access failure the Memory-Action Gap. We propose MemArbiter, a function-aware memory arbitration framework that addresses the memory-management-induced component of this gap. MemArbiter decomposes interaction histories into atomic items, organizes them into five functional Memory Banks, and combines bank-level demand, item-level relevance, focal-ambient representations, and a temporal presentation gate to dynamically control memory salience. We evaluate MemArbiter on ALFWorld against Flat Retrieval and Flat Recency under unified per-step memory budgets. With an open-weight action-generation model, MemArbiter achieves success rates of 82.8% and 92.5% under 500- and 750-token budgets, outperforming the strongest baseline by 20.9 and 25.4 percentage points, respectively. It also improves post-failure recovery and reduces failed-action repetition and state-action recurrence. These results show that function-aware memory arbitration enables accessible information to guide actions more effectively.

</details>


### 154. From Information to Delegation: Mapping Human-AI Financial Decision Making

- **Authors:** Iman Munire Bilal, Yingcan Carol Wang, Ajan Raj, Filippo Giovagnini, Pranav Tewari, Yuwei Zhang, Mei-Chen Zoe Liou, Qamar Zaman
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02100v1](http://arxiv.org/abs/2608.02100v1)
- **PDF:** [https://arxiv.org/pdf/2608.02100v1](https://arxiv.org/pdf/2608.02100v1)
- **Categories:** cs.HC, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI increasingly participates in human decision making, understanding how decision-making authority is distributed between humans and AI has become a fundamental behavioural question. We introduce a behavioural measurement framework combining intent and delegated decision authority to quantify what consumers seek from AI and how much decision-making authority they assign to it. Applied to 1.5 million real-world ChatGPT and Gemini interactions from 6,304 users in the United States and India, we find that financial services are already a substantial AI use case. Consumers overwhelmingly use AI to retrieve information and shape financial judgement, while delegation of financial execution remains rare. By shifting attention from conversation topics to delegated decision authority, this work establishes a behavioural baseline for measuring the transition to increasingly agentic AI.

</details>


### 155. Evolving in the Agent Jungle via History-Informed Opponent Awareness

- **Authors:** Zhaofeng Zhang, Linhan Xia, Rui Liu, Yihao Wang, Binrui Shen, Shengxin Zhu
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.02005v1](http://arxiv.org/abs/2608.02005v1)
- **PDF:** [https://arxiv.org/pdf/2608.02005v1](https://arxiv.org/pdf/2608.02005v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learning to adapt strategies through interaction is a key step toward more general and autonomous LLM agents. Existing approaches typically achieve behavioral adaptation by revising skill libraries. However, in multi-agent environments, opponents may simultaneously update their strategies, causing the environment itself to evolve continuously. Applying skill-revision methods designed for static environments in such settings therefore amounts to updating against an obsolete reference. To address this challenge, we introduce OASE (Opponent-Aware Selective Evolution), which identifies and adopts genuinely beneficial skill revisions in dynamic multi-agent environments. Specifically, OASE conducts paired comparisons between a candidate skill and the incumbent under identical conditions anchored by historical snapshots of opponent strategies, and adopts the candidate only when its estimated payoff gain exceeds an acceptance threshold. We evaluate OASE in two decision-making scenarios: first-price auctions and private-cost Cournot competition. Experimental results show that, compared with a Reflexion-style baseline, OASE achieves a lower final equilibrium distance in both environments while accepting substantially fewer skill revisions, thereby suppressing strategy changes that lack sufficient payoff support. OASE therefore replaces blind updating with evidence-anchored selection, allowing agents to adapt stably and efficiently even as opponents continuously evolve.

</details>


### 156. A Contractualist Argumentation Framework for Moral Decision-Making

- **Authors:** Luis Marcos-Vidal, Giulio Antonio Abbo, Tony Belpaeme
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.01937v1](http://arxiv.org/abs/2608.01937v1)
- **PDF:** [https://arxiv.org/pdf/2608.01937v1](https://arxiv.org/pdf/2608.01937v1)
- **Categories:** cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents operating in shared environments must make decisions that affect multiple individuals with potentially conflicting interests. We propose a formal framework for moral decision-making grounded in Scanlon's contractualism, an ethical theory that evaluates the permissibility of actions in terms of principles that no one could reasonably reject. To operationalise contractualist reasoning, we use ASPIC+, a structured argumentation framework, extended with value-based filtering to model how each agent's values determine which reasons are morally relevant in the first place. The result is a Contractualist Argumentation Framework in which agents' reasons are formally represented, compared, and evaluated through argumentation semantics. We illustrate the approach through a worked example in a domestic setting and discuss its relation to existing value-based argumentation approaches.

</details>


### 157. DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon Multimodal Agents

- **Authors:** Huanyao Zhang, Jiepeng Zhou, Runhao Zhao, Yanzhe Shan, Jiaoyang Chen, Bowen Zhou, Bo Li, Fang Wang, Jialong Wu, Zhengwei Tao, Lang Mei, Xiaohan Yu, Liyan Liu, Chong Chen, Wentao Zhang
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.01827v1](http://arxiv.org/abs/2608.01827v1)
- **PDF:** [https://arxiv.org/pdf/2608.01827v1](https://arxiv.org/pdf/2608.01827v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs) have advanced visual understanding and reasoning, yet their static parametric knowledge limits their ability to address knowledge-intensive and dynamically evolving open-world problems. To move beyond this limitation, multimodal deep search has emerged as a key direction for open-world information access, evolving from single-turn factual retrieval toward long-horizon, multi-turn search guided by visual evidence. However, existing methods typically confine vision to the input or answer stage, overlooking its role in intermediate reasoning, and lack designs tailored to long-horizon interaction. Consequently, visual evidence rarely drives continued retrieval, constraining both interaction depth and reasoning span. To address these limitations, we propose DeepVoyager-VL, a long-horizon multimodal deep-search framework for vision-in-the-loop search. Specifically, we construct a multimodal event graph to drive data synthesis, yielding problems with intermediate visual dependencies and long reasoning chains. We then design an agent framework for active visual acquisition and on-demand image loading. Finally, we fine-tune models on the synthesized data without reinforcement learning. Extensive experiments across ten multimodal search benchmarks demonstrate the effectiveness of our method.

</details>


### 158. CockpitHAT: Dependency-Graph-Driven Hierarchical Attribution for Embodied Multi-Agent Cockpits

- **Authors:** Wei Wang, Shuanghe Liu, Zhu Zhuo, Jiaqi Zhong, Xiaozhao Zhao, Xiaojie Zuo, Jie Su
- **Published:** 2026-08-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.01805v1](http://arxiv.org/abs/2608.01805v1)
- **PDF:** [https://arxiv.org/pdf/2608.01805v1](https://arxiv.org/pdf/2608.01805v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM multi-agent systems suffer from Correctness Collapse, where high task-level accuracy conceals severe process-level failures. This is especially hazardous in safety-critical embodied settings such as automotive cockpits, where lexically correct utterances may trigger dangerous physical operations. Existing attribution methods rely on text traces alone, missing dependency structure, multi-channel evidence, and safety-aware evaluation. We introduce CockpitHAT, a hierarchical attribution framework that replaces positional windows with dependency-distance thresholds from interaction DAGs, integrates multi-channel evidence via an embodied adapter, and applies a safety-uplift to high-risk failures during confidence-weighted analyst consensus. We further release CockpitBench, a benchmark of 212 annotated failure traces spanning dialogue, vehicle-state, environmental, and memory channels, each labeled with ISO 26262 ASIL severity via three-expert consensus. On the public Who&When benchmark, CockpitHAT achieves agent-level / step-exact accuracies of 77.9% / 37.8% on the Hand-Crafted split and 86.5% / 46.0% on the Algorithm-Generated split, surpassing the text-only SOTA ECHO by up to 17.6 / 16.7 points. On CockpitBench, it attains 78.3% agent-level and 38.2% step-exact accuracy. These results establish dependency-aware, multi-channel, risk-calibrated attribution as an effective paradigm for reliable failure diagnosis in real-world embodied LLM multi-agent systems.

</details>



## Biorxiv (1 papers)


### 1. AI semantics for biomedical data integration

- **Authors:** McLaughlin, J., Puig-Barbe, A., Ibrahim, A., Pava, D., Pendlington, Z. M., Matentzoglu, N., Sollis, E., Foreman, A., Wilson, R., Lopez Gomez, F., Harris, L., Adeleye, Y., Kaur, S., Meldal, B., Smedley, D., Parkinson, H.
- **Published:** 2026-08-07
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.03.742514](https://doi.org/10.64898/2026.08.03.742514)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Researchers increasingly need to explore hypotheses that span multimodal data across different scales, organisms, and domains. In practice, this requires connecting knowledge across fragmented databases with incompatible APIs and heterogeneous annotation practices. Large language model (LLM) agents can automate this data integration process, but grounding LLM agent outputs in scientifically correct sources of truth remains a significant challenge. Here we describe our deployment of a novel AI semantics workflow using LLM agents to enable scalable data integration, grounded in biological knowledge in the form of ontologies. Our workflow comprises (1) a multi-agent system curating scientific knowledge across ontologies using the Ontology Lookup Service (OLS) as grounding; (2) an LLM embedding service to enable interoperability between scientific databases by mapping ontology terms; and (3) GrEBI, a knowledge graph and Model Context Protocol (MCP) server enabling LLM agents to conduct cross-cutting, multi-omic biomedical queries.

</details>



## Medrxiv (2 papers)


### 1. RESCUE: An end-to-end multi-agent LLM system for proactive rare-disease patient screening in the EHR

- **Authors:** Liu, C., Geltzeiler, A., Afyouni, A., Nie, M., Ravi, K., French, C., Chung, W., Wojcik, M. H.
- **Published:** 2026-08-07
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.06.24.26356357](https://doi.org/10.64898/2026.06.24.26356357)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background: Rare diseases affect a significant portion of the global population, yet patients often endure a lengthy diagnostic odyssey, frequently missing the opportunity for timely diagnoses with exome or genome sequencing (ES/GS). Existing informatics tools often rely on pre-identified patients or rigid, institution-specific rule sets, failing to address the broader operational question of clinical utility and feasibility. Methods: We introduce RESCUE (Rare Disease Detection and Escalation Support via a Learning Health System), an end-to-end, multi-agent LLM-powered workflow designed for proactive rare-disease diagnosis across the entire electronic health record (EHR). RESCUE utilizes a team of specialized agents including Ontology, Modeling, Screening, and Review, to automate the screening process to identify candidates for diagnostic testing based on their clinical features. The Ontology Agent classifies clinical data into a four-tier genetic-evidence taxonomy; the Modeling Agent builds a positive-unlabeled (PU) XGBoost classifier to identify potential cases; the Screening Agent applies these models across the EHR population; and the Review Agent evaluates candidates by sampling clinical notes to ensure medical necessity and operational feasibility for genomic testing. Results: Using electronic medical record data from a pediatric hospital, our retrospective evaluation on a holdout set (n=12,591) demonstrates strong discrimination between patients who received diagnostic genomic testing and those who did not (AUC 0.808). Of nearly 500,000 patients in the institutional base, 175,842 met inclusion criteria for screening; among these, RESCUE-flagged candidates were 7.4-fold more likely to receive subsequent genomic assessments compared to controls. Blinded manual chart reviews confirmed that RESCUE identifies previously missed, medically appropriate patients for ES/GS with 80% precision, while simultaneously accounting for prior testing history. Conclusions: By decoupling expert roles into modular agents, RESCUE offers a flexible, scalable, and adaptable framework for screening patients for rare-disease diagnostic genomic testing. This approach overcomes the limitations of traditional rule-based methods and provides a reproducible, agentic pathway to reduce diagnostic delays and improve patient care at an institutional scale.

</details>


### 2. A PRISMA-Aligned Agentic Framework for Medical Systematic Reviews and Evidence Synthesis

- **Authors:** Huang, H., Zheng, Q., Qiu, P., Zhao, W., Zhang, Y., Xie, W., Wang, Y., Zhang, X., Wu, C.
- **Published:** 2026-08-03
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.07.30.26359375](https://doi.org/10.64898/2026.07.30.26359375)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Medical systematic reviews are central to evidence-based medicine, but they remain slow, labor-intensive, and difficult to maintain under the full Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) workflow. Recent LLM-based deep research agents offer a promising route to addressing this challenge, yet reliable deployment in medical systematic reviews remains limited by insufficient clinical domain knowledge and inconsistent adherence to evidence-based methodological standards across the full workflow. We address these gaps with MedSR-Copilot, a PRISMA-aligned multi-agent copilot that decomposes review automation into literature retrieval, coarse-to-fine screening, data extraction, Risk-of-Bias assessment, and evidence synthesis, while preserving structured intermediate artifacts throughout the workflow. We further introduce MedSR-Bench, an end-to-end benchmark for evaluating systems beyond isolated subtasks, from review input to final evidence-synthesis conclusions. MedSR-Copilot completes medical systematic reviews end-to-end under the full PRISMA workflow, achieving 63.6% human-aligned conclusions, 18.3 percentage points above the best baseline among strong general-purpose LLMs and prior automated review systems. In a human-AI collaboration study involving 23 analysis groups across four systematic review topics, MedSR-Copilot, used as a copilot, reduces end-to-end review time by 64.9% and improves final conclusion accuracy by 27.4 percentage points compared with routine-practice workflows. Together, these results demonstrate the reliability and efficiency of MedSR-Copilot as a medical research copilot and suggest a practical path toward trustworthy review automation.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*