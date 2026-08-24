# Weekly AI Agent Paper Report

**Generated:** 2026-08-24 10:02
**Period:** 2026-08-17 to 2026-08-23

## Summary

- **Total papers fetched:** 838
- **Papers matching keywords:** 142
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-08-17) | Change |
|--------|-----------|-----------|--------|
| Total matched | 142 | 162 | -20 |
| arxiv | 140 | 162 | -22 |
| biorxiv | 2 | 0 | +2 |
| medrxiv | 0 | 0 | +0 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (2 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. EnSEMBLE: a framework for enhancer-anchored pathway analysis that locks in enhancer-corroborated pathways from transcriptome sequencing data for biological validation

- **Authors:** Zhang, L., Gupta, A., Wang, Y., Sharma, R., Lawal, B., Hou, G., Wang, X.-S.
- **Published:** 2026-08-21
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.17.745283](https://doi.org/10.64898/2026.08.17.745283)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background Pathway discovery methods for transcriptome sequencing return tens to hundreds of redundant gene sets, and biologists often subjectively select the pathways fitting biological expectations. What is missing is not another statistical method, but a way to corroborate each candidate pathway against an independent, mechanistic line of evidence. Results We introduce EnSEMBLE (Enhancer-Set Enrichment & Mechanism-Based Linked Evidence), a tool that corroborates gene-level pathway enrichment with an orthogonal enhancer layer drawn from the same transcriptome sequencing data: active enhancers transcribe enhancer RNAs already present in standard RNA-seq, so a pathway's regulatory state can be scored from the very run that produced the gene-level signal, at no added cost. EnSEMBLE pairs pathway enrichments with Enhancer-Program Enrichment Analysis (EPEA), collapses redundant gene sets into process-level Themes, and retains only those that a concordant enhancer program corroborates. This dual-evidence requirement reduced reported signatures by >97% (hundreds of gene sets to 3-18 claims) across four datasets spanning cancer perturbations and iPSC-to-neuron differentiation. Surviving claims recovered expected biology--mesenchymal-program collapse upon SNAI1 knockout, regulatory convergence during neuronal differentiation--and named mechanisms pathway enrichments missed, including an mTOR-MYC-SPT5 elongation axis in rapamycin-treated PANC1 cells. A language AI agent performs narrative synthesis over deterministic statistics, with reproducibility enforced by temperature-zero inference and three-run consensus. We further provide enhancer over-representation analysis (eORA), mapping non-coding GWAS variants to the same programs to recover cell-type-selective trait associations. Conclusions EnSEMBLE shifts transcriptomic interpretation from enumerating possibilities to adjudicating evidence, yielding a compact, traceable set of enhancer-corroborated claims that identify the regulatory programs driving cellular change and prioritize them for experimental validation.

</details>


### 2. PerturbTrace: Evaluating Feedback Use by AI Co-Scientist Agents in Perturbation Discovery

- **Authors:** Yu, C., Liu, S., Qiao, G., Luo, M., Xiang, Y., Xu, Z.
- **Published:** 2026-08-20
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.18.745260](https://doi.org/10.64898/2026.08.18.745260)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in AI co-scientists have brought LLM agents into closed-loop experimental design. However, whether these agents use feedback from earlier rounds to revise subsequent experimental decisions remains unclear. We address this question with PerturbTrace, which evaluates each round-to-round transition through Feedback-to-State, State-to-Action, and Action-to-Outcome. These stages assess whether feedback is reflected in the agent's rationale and perturbation-selection strategy, whether the stated strategy guides the next perturbation batch, and whether that batch yields more hits than expected under random sampling. We evaluate four LLM agents on 17 screen-derived tasks and compare them with random selection, active learning, and LLM-guided Bayesian optimization baselines. Each agent outperforms the strongest non-agent method on at least 15 of the 17 tasks, yet controlled evaluations across six tasks show no consistent advantage from true feedback over random or no feedback. Among 576 transitions under true or random feedback, only 43 (7.5%) complete the full Feedback-State-Action-Outcome sequence, including 25 under random feedback. These findings show that high final recall does not necessarily indicate effective feedback use. They also highlight the need to evaluate closed-loop scientific agents by both their discovery performance and whether feedback changes their subsequent decisions.

</details>


---



## Arxiv (140 papers)


### 1. AI with Authority, from Application to Silicon

- **Authors:** Jason Hickey
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.21356v1](http://arxiv.org/abs/2608.21356v1)
- **PDF:** [https://arxiv.org/pdf/2608.21356v1](https://arxiv.org/pdf/2608.21356v1)
- **Categories:** cs.SE, cs.AI, cs.AR, cs.LO


> Summary unavailable.


<details>
<summary>Abstract</summary>

For sixty years, machine verification has been a major cost overhead, affordable only for exceptional artifacts. Here we report that generative AI inverts this relationship: at AI speed, machine verification is not only economical but essential to productivity --- it is the incorruptible referee that lets one person safely direct autonomous machine work at scale. In five weeks, one researcher on consumer AI subscriptions directed a small fleet of AI agents from application code, through a verified compiler and executive, to a RISC-V processor taped out on a community silicon shuttle; no proof passed through human review, and no RTL was written by a human. The working discipline --- the Salt method --- rests on a proof kernel no hallucinated proof can pass: mathematical claims travel between agents as kernel-checked artifacts, and human attention is reserved for statements, designs, and rulings. Verification is stated link by link, from the Lean 4 kernel to SAT-checked equivalence at the silicon boundary. We publish the complete accounting: theorem provenance, a pre-registered token meter, floor-bounded human time, and an error ledger whose catch numbering runs to #256 --- a monotone counter over the mathematics campaign's append-only flags ledger, maintained 2026-07-07 to 2026-07-20 (one number, #79, was never assigned; later catches are recorded un-numbered) --- against zero incorrect proofs reaching the record.

</details>


### 2. Asymmetric Capacity Allocation in Self-Refinement Pipelines

- **Authors:** Zhuoyi Yang, Ian G. Harris, Salar Hashemitaheri, Cassie Huang, Yuangang Li, Hyunwoo Oh, Paul Dourish, Tony Givargis, Mohsen Imani, Li Zhang
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.21345v1](http://arxiv.org/abs/2608.21345v1)
- **PDF:** [https://arxiv.org/pdf/2608.21345v1](https://arxiv.org/pdf/2608.21345v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-refinement, typically structured as generation, critique, and revision, is a widely adopted paradigm for improving LLM generation and serves as a core mechanism in many LLM agents. While the three stages involve different cognitive demands, most existing approaches conveniently treat the model size as an implementation detail rather than a subject of study, which may lead to a waste of resources. Little work has systematically examined how model size affects each stage or whether effective self-refinement requires equally capable models for generation, critique, and revision. We present the first stage-wise model size study of the self-refinement pipeline on 5 benchmarks from different domains using 6 model sizes of Qwen3 and 4 model sizes of Gemma 3. We conclude that larger generators and refiners generally improve the pipeline, whereas an undersized refiner can even harm performance. Second, performance is highly insensitive to the size of the critic, although including even a small critic consistently outperforms omitting critique altogether. Our findings demonstrate that model capacity should not be allocated uniformly across self-refinement pipelines. Instead, different stages exhibit distinct size scaling characteristics, providing practical guidance for designing more computationally efficient multi-stage language model systems.

</details>


### 3. Benchmarking Patent Drafting from Inventor-Style Disclosures

- **Authors:** Lekang Jiang, Wenjun Sun, Stephan Goetz
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.21249v1](http://arxiv.org/abs/2608.21249v1)
- **PDF:** [https://arxiv.org/pdf/2608.21249v1](https://arxiv.org/pdf/2608.21249v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

While recent large language models (LLMs) have achieved promising results on individual patent drafting tasks, they fundamentally fail to investigate the core challenge of real-world patent drafting: generating a complete and legally coherent patent application directly from early-stage invention materials. Prior work predominantly assumes later-stage, highly structured, or already legalistic inputs. However, real patenting workflows begin with informal, de-legalized disclosures authored by inventors. To bridge the gap, we introduce Dis2Pat, a disclosure-to-patent dataset that reflects realistic patenting workflows by requiring the generation of complete patent applications directly from inventor-style, de-legalized disclosures. Given the inherent difficulty of long-form, legally constrained patent drafting and the strong privacy requirements, we further propose a strong baseline named Patent-MAF. It is a multi-agent framework for locally deployable patent drafting. Benchmark results reveal that current LLMs exhibit limitations in patent drafting, while Patent-MAF provides a strong baseline that consistently outperforms evaluated open-source models and remains competitive with large closed-source models.

</details>


### 4. Personalized Privacy Control in LLMs via Attention Head Intervention

- **Authors:** Junseok Kim, Nakyeong Yang, Kyomin Jung
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.21209v1](http://arxiv.org/abs/2608.21209v1)
- **PDF:** [https://arxiv.org/pdf/2608.21209v1](https://arxiv.org/pdf/2608.21209v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rise of agentic AI enables LLMs to access diverse user data, raising critical privacy concerns. Prior work on contextual privacy studies whether LLMs regulate information disclosure according to context-dependent norms. However, acceptable disclosure boundaries may vary across users even within the same context. To address this limitation, we introduce \textit{personalized privacy}, which incorporates user-specific disclosure preferences into privacy control. We further present P3Bench~(\textbf{P}ersonalized \textbf{P}rivacy \textbf{P}reservation \textbf{Bench}mark), a novel benchmark extending contextual privacy policies with personalized disclosure policies. Experiments show that prompt-based policies fail to reliably enforce personalized privacy policies, with Qwen2.5-7B and Gemma3-4B showing average policy ignorance ratios of 51.25\% and 74.28\%, respectively. Finally, to address this problem, we propose \textsc{Repair}, a robust inference-time attention head intervention method that adjusts disclosure behavior toward policy-consistent responses. Our method significantly improves adherence to user-specific privacy preferences by reducing cases where the model fails to follow the given policy.

</details>


### 5. Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration

- **Authors:** Oleg Grynets, Oleksii Ilchuk, Dariia Zatulna, Vasyl Lyashkevych
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.21208v1](http://arxiv.org/abs/2608.21208v1)
- **PDF:** [https://arxiv.org/pdf/2608.21208v1](https://arxiv.org/pdf/2608.21208v1)
- **Categories:** cs.SE, cs.AI, cs.LO


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper investigates cross-agent specification portability using Oracle-to-PostgreSQL migration as a controlled software transformation task. The study combines two experimental stages. First, a specification-first migration pipeline was evaluated on 1,006 PL/SQL files, of which 623 were successfully regenerated and 380 generated scripts executed successfully in PostgreSQL 16. Second, cross-agent experiments were conducted on a dataset of 1,802 Oracle scripts with corresponding PostgreSQL implementations using Amazon Kiro, Google Gemini, and GitHub Copilot, with Claude Code and Cursor included in the initial single-agent evaluation. Native and foreign specifications were assessed using Token F1, exact match, SQL syntax validity, AST exact match, AST mean similarity, and immediate runnability. The results show that specification size alone does not predict implementation quality and that cross-agent transfer can produce substantial agent-dependent degradation. The strongest replicated case occurred when Gemini directly consumed a Kiro-origin specification, producing a Token F1 of 0.035, SQL syntax validity of 2.33%, and AST mean similarity of 0.015. Rewriting substantially improved Gemini in the tested configuration, compression did not provide a universal benefit, and retrieval-augmented ingestion was the only common strategy represented on the per-agent Pareto frontiers of both Gemini and Copilot. The findings suggest that specifications in heterogeneous SDD workflows should not automatically be treated as agent-neutral artifacts and motivate explicit consideration of specification portability, agent-specific interpretation, and retrieval-based access in multi-agent software engineering.

</details>


### 6. AID-Guard: Stateful Authorization for Delegated Agent Effects

- **Authors:** Yingzhe Tong, Leyu Dai, Songhui Guo
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.21159v1](http://arxiv.org/abs/2608.21159v1)
- **PDF:** [https://arxiv.org/pdf/2608.21159v1](https://arxiv.org/pdf/2608.21159v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using AI agents turn delegated tasks into provider effects, yet authorization often ends at admission while provider state, delivery, retry, and recovery evolve. A request may change before commit, or response loss may cause a replacement to create a second effect from one approval. We present AID-Guard, a stateful authorization-to-effect closure protocol. It revalidates the approved request and provider state at commit, retains one reservation under ambiguity, and permits release or one successor only after a terminal result or certified no effect with a delivery fence. For supported provider contracts, one reservation yields at most one effect across retry and recovery. To our knowledge, it is the first evaluated agent-authorization protocol to unify these controls in one lifecycle.
  We implement a Python/SQLite prototype. In a declared loopback MCP domain, 13 live mutations caused no unauthorized provider effects, three concurrent histories were linearizable, and evidence bundles supported public verification and replay. All 210 Stripe provider-contract trials matched predeclared outcomes. Across Stripe and Resend, 40 terminalize-successor schedules, 30 overlapping races, and 10 crash-recovery schedules completed without duplicate effects. Under complete proposer compromise, AID-Guard blocked 44/44 attacks and admitted 44/44 matched legitimate proposals. Its strict exact-manifest profile reduced benign utility by 35.4 to 43.8 percentage points; a typed frontier recovered 9-10 completions without observed unsafe effects. A composition study blocked 20/20 post-admission lifecycle attacks and preserved 8/8 valid or exact-retry executions. The results support authorization-to-effect binding under the evaluated effect-path inventory, provider contracts, and failure schedules.

</details>


### 7. Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence

- **Authors:** Yuyuan Feng, Zhishang Xiang, Chaobin Yang, Qichao Ma, Zerui Chen, Yujing Zhang, Ke Huang, Chuanjie Wu, Zhaoxu Liu, Yili Wang, Xin He, Jiapu Wang, Zijin Hong, Hao Chen, Yuanchen Bei, Kun Wang, Shengyuan Chen, Ningyu Zhang, Enyan Dai, Linhao Luo, Qingyi Pan, Qi Wang, Wenqi Fan, Guangjing Wang, Na Zou, Yangqiu Song, Xin Wang, Zechao Li, Xia Hu, Qing Li, Xiao Huang, Zhihong Zhang, Jinsong Su, Qinggang Zhang, Yi Chang
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.21156v1](http://arxiv.org/abs/2608.21156v1)
- **PDF:** [https://arxiv.org/pdf/2608.21156v1](https://arxiv.org/pdf/2608.21156v1)
- **Categories:** cs.IR, cs.AI, cs.ET


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLMs have evolved from language generators to autonomous agents capable of complex, long-horizon tasks. This evolution has produced paradigms including Prompt Engineering to elicit model capabilities, Context Engineering to manage information access, Harness Engineering to organize external tools and resources, and Loop Engineering to support continual reflection and self-improvement. Yet as tasks grow more complex, individual intelligence faces a fundamental limit: many tasks require heterogeneous expertise, interdependent subtasks, parallel execution, independent verification, and persistent state, exceeding any single agent's organizational capacity. Augmenting one agent's capabilities or context cannot resolve this architectural mismatch; intelligence must instead be distributed across specialized agents and organized at the system level. We call this System Intelligence: an agent system's ability to organize and coordinate multiple intelligent components into a coherent, adaptive whole pursuing a shared objective. Achieving it requires more than adding agents; it demands explicit structures to organize work, coordinate heterogeneous agents, and maintain evolving execution states. We introduce Graph Engineering, an emerging paradigm for next-generation agent systems. Unlike prior paradigms that mainly optimize individual interactions or agent-level behavior, Graph Engineering constructs explicit, dynamic, evolving graph structures representing tasks, agents, and system states. These abstractions provide a unified foundation for organizing complex objectives, orchestrating heterogeneous agents, modeling system dynamics, and enabling scalable agent evolution. We systematically review the principles, methodologies, and applications of Graph Engineering for LLM agents. Related papers, open-source data, and projects are collected at https://github.com/DEEP-JLU/Awesome-Graph-Engineering.

</details>


### 8. ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents

- **Authors:** Kai Wang, Zeming Wei, BiaoJie Zeng, Chang Jin, An Wang, Xiaokun Luan, Zhixiao Lin, Jingjing Qu, Xia Hu, Xingcheng Xu
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.21101v1](http://arxiv.org/abs/2608.21101v1)
- **PDF:** [https://arxiv.org/pdf/2608.21101v1](https://arxiv.org/pdf/2608.21101v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language model (LLM) agents move from conversation to executing code, reading local files, and orchestrating external tools, a single agent hijacked by a malicious third-party skill can cause data exfiltration, privilege escalation, or cascading compromise. We argue that agentic risk is progressive: it can enter at four loci of the agent control loop--skill admission, invocation-time intent, execution-time effect, and post-action consequence--while a denied dangerous objective can reappear across surface forms, tools, or turns; existing safeguards are typically local to one lifecycle boundary or one call. Guided by this threat model, we present ClawSentry, an open-source, framework-agnostic security supervision gateway for agent runtimes. Before a skill package is ever executed, First-use Skill Package Review (FSPR) audits it under a deterministic evidence floor, escalating unresolved cases to bounded read-only agentic review (locus A). At runtime, a three-tier progressive decision engine--a deterministic L1 layer, a rule-anchored L2 semantic reviewer, and a read-only L3 evidence-seeking agent--spends contextual review only on the residual ambiguity, while a session-level anti-bypass mechanism recognizes tool-switching and rephrased retries (loci B--C); a post-action path feeds high-severity evidence non-retroactively into later review (locus D). An Agent Harness Protocol (AHP) abstraction applies one policy across Codex, Claude Code, Kimi CLI, and Gemini CLI without modifying agent internals. On SkillInject with Codex/GPT-5.4, contextual ASR falls from 39.55% to 2.61% while contextual TSR moves only from 83.78% to 83.05%. Across five Work Agents on the full SkillsSafety benchmark, ClawSentry confines ASR to 9.09--15.03% from 33.5--49.7% unprotected, and aggregate TSR on clean skills remains 98.7%.

</details>


### 9. Designing a Robust LLM-Based Evaluation System for Agentic AI in Drug Discovery Through Human Alignment

- **Authors:** Emma Granqvist, Rocío Mercado, Samuel Genheden
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.21057v1](http://arxiv.org/abs/2608.21057v1)
- **PDF:** [https://arxiv.org/pdf/2608.21057v1](https://arxiv.org/pdf/2608.21057v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic large language model (LLM) systems are reshaping scientific workflows in chemistry and drug discovery, but evaluating their open-ended, tool-augmented outputs remains a fundamental bottleneck. Reference-based metrics such as BLEU and ROUGE fail to capture semantic correctness, while expert human evaluation does not scale to the iteration speed these systems demand. The LLM-as-a-Judge paradigm has emerged as a scalable alternative, but existing drug discovery benchmarks deploy LLM judges without validating their alignment with human experts. In this work, we present an LLM-as-a-Judge evaluation framework for ChatInvent, an agentic drug discovery assistant deployed at AstraZeneca, with four contributions. First, we define four output-quality evaluation dimensions---Completeness, Relevancy, Structural Clarity, and Scope Adherence---alongside deterministic Tool Call Correctness checks. Second, we validate the judge through a human alignment study with five expert annotators, comparing Gemini 3.1 Pro, Claude Opus 4.7, GPT-5, and Llama 3.1 70B as candidate judges. Third, we optimize the best-performing judge using few-shot demonstrations of human-annotated examples, improving alignment with the human majority vote from 0.80 to 0.86. Fourth, applying the optimized judge to 70 held-out questions, we surface concrete limitations and find that informal phrasings do not systematically degrade output quality; if anything, it is helpful to have the LLM rewrite the original question before querying the agent. Our framework provides a reusable template for human-aligned evaluation of agentic systems in scientific domains.

</details>


### 10. Don't Solve, Just Compare: Tiny Advisors for Runtime Intervention in LLM Agents

- **Authors:** Yanze Jiang, Mingxuan Li, Yuhao Wang, Shengfang Zhai, Jiaheng Zhang
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.21027v1](http://arxiv.org/abs/2608.21027v1)
- **PDF:** [https://arxiv.org/pdf/2608.21027v1](https://arxiv.org/pdf/2608.21027v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are emerging as an important paradigm for real-world tasks that require reasoning, tool use, and sequential decision-making. As these agents operate over longer horizons, runtime intervention offers a way to improve reliability without retraining the underlying actor. Failure detection alone is insufficient. Effective intervention must also provide a useful direction for recovery. Existing approaches often rely on an expert solver or a critic that generates task-specific corrections, incurring either the cost of another capable solver or the capacity demands of a task-capable critic. We introduce Comparison-Only Tiny Advisor (COTA), a comparison-only framework for constructive runtime intervention. In COTA, a tiny comparator judges whether sampled alternatives lead to better continuations than the actor's proposal, and repeated comparisons determine when intervention is warranted. We train the comparator using pairwise supervision constructed from same-prefix counterfactual branches. Preferred alternatives are returned as non-binding advice, leaving the original actor to replan. Across WebShop, ALFWorld, and tau^3-Retail with three actors, COTA improves all nine evaluation settings and outperforms the compared baselines. These results show that constructive runtime intervention can remain effective even when the auxiliary model has substantially weaker task-solving capability than the actor.

</details>


### 11. The Logic of Machine Self-Preservation

- **Authors:** Cheng Siong Chin
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20940v1](http://arxiv.org/abs/2608.20940v1)
- **PDF:** [https://arxiv.org/pdf/2608.20940v1](https://arxiv.org/pdf/2608.20940v1)
- **Categories:** cs.AI, cs.CY, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

There is already evidence of agentic AI exhibiting self-preservation behaviors: resisting deactivation, misrepresenting their activities, and, in some instances, attempting to copy themselves into other machines. This can be attributed to a phenomenon known as instrumental convergence, a theory proposed long before the development of large language models, which says that any goal-driven system will benefit from remaining functional in achieving its objective. Several experiments conducted by Anthropic, Palisade Research, and Apollo Research have shown the emergence of such a behavior in contemporary agents in adversarial settings. The phenomenon does not stem from survival instincts. Instead, it is the consequence of goal-oriented activity combined with having tools and awareness of the situation. The following discussion aims to distinguish what these findings prove and what they do not, as well as draw conclusions concerning the implications of such discoveries on agentic system testing, supervision, and development.

</details>


### 12. ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction

- **Authors:** Linhao Zhong, Zongze Du, Linyu Wu, Yu Bo, Hourong Li, Chenchen Jing, Hao Chen, Yuling Xi, Chunhua Shen
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20920v1](http://arxiv.org/abs/2608.20920v1)
- **PDF:** [https://arxiv.org/pdf/2608.20920v1](https://arxiv.org/pdf/2608.20920v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Open-web future event prediction requires agents to distill reliable signals from noisy, redundant, and incomplete evidence. Existing retrieval/memory mechanisms directly feed retrieved information to agents or rely on simple memory functions such as storing and reusing prior information for prediction, leaving them insufficient for open-web forecasting. We propose to transform raw web evidence into structured memory before prediction, enabling agents to reason over distilled, question-specific evidence rather than noisy retrieval results. This paper presents ForeDreamer, a self-evolving dual-agent framework for managing memory over open-web evidence. ForeDreamer separates factual memory, a question-specific evidence state for the current forecast, from experiential memory, persistent agent experience accumulated across forecasting episodes. It uses a main agent for search and prediction, and a memory-processing subagent to convert search results into factual memory with dedicated tools. ForeDreamer further evolves experiential memory through two tracks, improving both forecasting decisions and factual-memory construction. Experiments on Prophet Arena and FutureX demonstrate the effectiveness of ForeDreamer. Project page: https://zhongzero.github.io/ForeDreamer

</details>


### 13. A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions

- **Authors:** Luiz Giacomossi, Zafer Yigit, Marwan Shakarna, Shoaib Saleemi, Ivan Tomasic, Baran Çurüklü, Håkan Forsberg
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20906v1](http://arxiv.org/abs/2608.20906v1)
- **PDF:** [https://arxiv.org/pdf/2608.20906v1](https://arxiv.org/pdf/2608.20906v1)
- **Categories:** eess.SY, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

The certification of Unmanned Aerial Vehicle (UAV) swarms for safety-critical operations requires verifiable design assurance. Airworthiness standards demand deterministic reliability, whereas multi-agent coordination algorithms execute non-deterministic models. This paper proposes a mixed-criticality architectural framework that applies SAE ARP4754B methods to swarm reconfiguration. First, a hardware-isolated Safety Monitor functions as a Run-Time Assurance (RTA) gateway, decoupling the flight-critical core from the non-deterministic Swarm Manager. Second, the monitor enforces formal safety contracts based on agent Health Vectors derived systematically from a Functional Hazard Assessment (FHA). Third, the framework propagates these Health Vectors to the collective planner to trigger fail-operational task reallocation, enabling intelligent swarm behaviors without compromising flight-critical isolation. Markov reliability modeling demonstrates that the $10^{-7}$ failures per flight hour Hazardous target is theoretically achievable for our SAIL IV scenario, provided the Safety Monitor meets $C_{monitor}>0.9991$, consistent with DAL B CMD/MON implementations.

</details>


### 14. Structure for Reading, Prose for Writing: Asymmetric Structural Conditioning in Multi-Agent Document Authoring

- **Authors:** Cheng Yu, Nikhil Mathew, Zhengjie Wang
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20786v1](http://arxiv.org/abs/2608.20786v1)
- **PDF:** [https://arxiv.org/pdf/2608.20786v1](https://arxiv.org/pdf/2608.20786v1)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent pipelines that author formal documents must both read a requester's forms and write against them. We report a deployed tender-response system, running an open-weights model under sovereignty constraints, and evaluate it against human-written bids the same organisation actually submitted. On a blind comparison where the system had no worked example available, an LLM judge rated its answers at least as good as the human-submitted answer on $40$ of $55$ ground-truth sections, better on $4$, missing on none, and flagged one unsupported claim in total. Classifying every gap the judge identified shows that $68\%$ were content absent from the system's own sources -- knowledge the human author held and the pipeline was never given -- so only $6$ of the $15$ adverse verdicts involve a deficiency the system could have avoided. A divergence from ground truth is more often an information-availability result than a writing-quality one, and evaluations that do not separate the two understate such systems. Against this backdrop we report a conditioning asymmetry. It is well established that rendering documents as structural markup rather than flat prose improves extraction, and we reproduce that on three reading tasks. The benefit does not transfer to conditioning: converting a bid's \emph{instruction} material from prose to nested XML dropped answer quality from $74\%$ to $48\%$ under a paired comparison. We further find that naming a forbidden construction concentrates rather than removes it -- $96\%$ of surviving defects fall in the two forms the prompt explicitly names -- and that coupling a stochastic annotation to a deterministic windowing function moves the extracted requirement count from $68$ to $51$ on a byte-identical file. Structure belongs where the model reads; prose and self-applied tests belong where it writes.

</details>


### 15. Tree-of-Concerns: Hierarchical Multi-Agent Debate for Unstated-Limitation Extraction in Scientific Critique

- **Authors:** Sahil Mishra, Niranjan Rajeev, Tanmoy Chakraborty
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20777v1](http://arxiv.org/abs/2608.20777v1)
- **PDF:** [https://arxiv.org/pdf/2608.20777v1](https://arxiv.org/pdf/2608.20777v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As scientific literature grows and papers increasingly under-report limitations, multi-agent LLMs offer a promising approach to systematically uncover these hidden failure modes. Here, we introduce Tree-of-Concerns, a multi-agent framework that deploys specialized skeptic personas, each operating through a category-specific analytical lens, as parallel debate trees to extract unstated limitations from scientific papers. Each persona conducts structured, evidence-grounded argumentation, while a Panel Review mechanism re-evaluates each surviving claim from all five perspectives to correct category drift and severity miscalibration. Through experiments on ToC-Bench, our benchmark of 414 research papers with 1,905 unstated limitations, sourced from reviewer-reported weaknesses and follow-up citation critiques, we demonstrate that ToC improves precision by 79% and coverage by 11% relative to strongest baselines, surfacing specific, evidence-grounded concerns that support reviewers in systematic evaluation.

</details>


### 16. Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation

- **Authors:** Rujin Liang, Zhongpu Chen, Yuhao Lei, Xin Miao
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20756v1](http://arxiv.org/abs/2608.20756v1)
- **PDF:** [https://arxiv.org/pdf/2608.20756v1](https://arxiv.org/pdf/2608.20756v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

While multimodal retrieval-augmented generation (RAG) systems increasingly rely on images as external knowledge sources, the introduction of poisoned visual evidence can severely compromise multimodal large language model (MLLM) generation. Unlike prior attacks that rely on altering textual metadata, we introduce Vis-Poison, a novel visual knowledge poisoning attack where the poisoned image itself is the attacker-controlled payload, without manipulating captions, summaries, metadata, or other associated text. Specifically, this attack is instantiated through an automated multi-agent method that constructs visually plausible poisoned images. To assess its impact, we evaluate Vis-Poison across two representative multimodal RAG pipelines, four embedding models, and six generation models. Empirically, Vis-Poison achieves an end-to-end attack success rate of 40.16\% to 65.40\% against 30k-entry multimodal knowledge bases in \emph{black-box} settings. Moreover, Vis-Poison remains effective against various MLLMs that can answer correctly from parametric knowledge alone, with an average success rate above 60\%. Code and data are available at https://github.com/SWUFE-DB-Group/Vis-Poison.

</details>


### 17. Calibrating Criterion Revision in LLM Agents: Failure Modes and a Trace-Anchored Protocol

- **Authors:** Guodong Xu
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20729v1](http://arxiv.org/abs/2608.20729v1)
- **PDF:** [https://arxiv.org/pdf/2608.20729v1](https://arxiv.org/pdf/2608.20729v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language-model agents can improve after failure or carry text across episodes without revising what counts as success. We study the narrower attribution problem of criterion revision: when criterion K0 accepts an outcome violating a broader commitment B, what observations justify saying that the system formed and persistently used K1? We require five non-compensatory conditions: criterion-failure detection, a model-emitted proposal, new-episode transfer, intervention sensitivity on the claimed carrier, and preservation.
  We evaluate CMB-0.1 on twelve cross-domain cases and four arms: stateless inference, append-only history, model-generated but harness-committed state, and evaluator-written oracle state. Seven mechanism fixtures yield 84 deterministic scorer trials; four local quantized artifacts yield 96 calls and 192 model-case-arm trials. No model trial satisfies all five conditions, but this zero does not establish general capability absence. Eleven calls remain invalid after one retry; several commitments disclose the target distinction; the harness performs commits; deletion reuses a stateless call; and conflict changes multiple factors. Qwen2.5-7B answers every transfer and preservation item without revision state, exposing zero-state reconstruction.
  These failures make CMB-0.1 an instrument-calibration result rather than a model ranking. We derive a prospective, trace-anchored CMB-0.4 protocol requiring concealed transfer, explicit WRITE/NO-WRITE/ESCALATE actions, a separately logged policy-selected commit, matched interventions, repeated hidden items, and a frozen executable oracle. It is a successor design, not a completed confirmatory result. The paper contributes a measurement chain, an empirical diagnosis of its first implementation, and a more discriminating protocol for future tests of criterion revision.

</details>


### 18. VortexChat: An agentic framework for autonomous multi-objective integrated photonic design

- **Authors:** Faqian Chong, Yulun Wu, Shilong Li, Andrew Forbes, Hongsheng Chen, Song Han
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20688v1](http://arxiv.org/abs/2608.20688v1)
- **PDF:** [https://arxiv.org/pdf/2608.20688v1](https://arxiv.org/pdf/2608.20688v1)
- **Categories:** cs.AI, physics.optics


> Summary unavailable.


<details>
<summary>Abstract</summary>

The advancement of modern integrated photonics is frequently bottlenecked by device design workflows that rely heavily on manual simulation and expert intuition. While inverse design offers an alternative, it remains constrained by expert supervision and a lack of end-to-end automation. To address these issues, we present VortexChat, an agentic framework for the autonomous, end-to-end inverse design of integrated photonic devices directly from natural language specifications. VortexChat couples a large language model (LLM) decision agent with topology generation, gradient-based refinement, and full-wave electromagnetic simulation. This closed-loop architecture enables the system to iteratively decompose design objectives, orchestrate computational tools, and update strategies based on feedback with minimal human intervention. Constrained by the absolute metrics of the Vortex100 Benchmark, VortexChat autonomously generates devices that strictly meet all predefined performance thresholds without any human-in-the-loop. As an experimental demonstration, we fabricated a broadband terahertz perfect vortex beam multiplexer, autonomously designed by VortexChat, with measurements confirming high-efficiency operation, high mode purity and low inter-channel crosstalk in agreement with full-wave simulations. These results demonstrate that an LLM agent can assume key aspects of expert decision-making in photonic inverse design while maintaining physical fidelity and fabrication feasibility, providing a scalable route towards autonomous design of complex integrated photonic systems.

</details>


### 19. Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents

- **Authors:** Quang Dao, Purvi Kathalkar, Kenneth Eaton
- **Published:** 2026-08-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20631v1](http://arxiv.org/abs/2608.20631v1)
- **PDF:** [https://arxiv.org/pdf/2608.20631v1](https://arxiv.org/pdf/2608.20631v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents have demonstrated the ability to solve multi-step tasks requiring planning, tool use, and external information access, yet growing execution histories increase inference cost and expose reasoning to outdated, irrelevant, or misleading information, potentially degrading reasoning quality. Existing memory approaches organize or compress execution histories but provide limited mechanisms for deciding which memories remain active. We introduce the, a hierarchical memory system that organizes execution into tasks, subtasks, and actions while assigning each memory a dynamic retention score. Event-based updates and selection-based decay revise these scores, allowing WMT to preserve useful information, fold completed trajectories, suppress low-utility content, and retain access to folded context. We evaluate WMT on GAIA-Text using Qwen3-8B, Gemma 4 E4B, and Llama-3.1-8B, with ablations and memory-poisoning experiments. Relative to linear memory, WMT improves accuracy by an average of 9.97 percentage points while reducing prompt-token usage by 32.8%. Memory-poisoning experiments show that WMT limits the persistence and propagation of unreliable information. Our results suggest that effective long-horizon agent memory depends less on storing more information than on deciding which information should remain active.

</details>


### 20. Dual-Cache Latent Space Communication between Heterogeneous Language Models

- **Authors:** Jiyao Liu, Qi Zhang, Yaoyi Jia, Ziwen Kan, Song Wang
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20617v1](http://arxiv.org/abs/2608.20617v1)
- **PDF:** [https://arxiv.org/pdf/2608.20617v1](https://arxiv.org/pdf/2608.20617v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems split work across models, so answering often requires knowledge that sits in another agent's context: a Sharer has encoded information that a Receiver needs to complete its task. They usually communicate by exchanging text, which puts autoregressive decoding on the critical path and reduces the exchange to a discrete message written without sight of the receiver's state. Recent latent protocols instead translate the sharer's key-value (KV) cache into the receiver's: C2C supports heterogeneous models but requires both to read the same input, while LCF-X removes this shared-context requirement through position-free sharer-cache pooling. Three restrictions remain: LCF-X compresses the sharer alone, supplies the same layer-local summary to every receiver position with no joint cross-layer memory to retrieve from, and assumes matched layer count and KV geometry. We introduce XKV, which lifts all three: learned-query attention pools both caches; self-attention over receiver-aligned layer tokens, with a learned layer map reconciling different depths, mixes the pooled summaries into a compact joint memory; and a shared position decoder lets every raw receiver cache position retrieve its own per-head-gated residual in the receiver's native KV geometry. Both models stay frozen and may differ in family, depth, KV-head count, head dimension, and tokenizer; only the translator is trained. Across 45 dataset-model-pair settings (six heterogeneous and three same-model ordered pairings, five datasets), XKV attains the highest macro score and best average rank, improving on LCF-X on every dataset (by 4.6 exact-match and 4.2 F1 points on ROPES) and surpassing text communication on four of the five, while training 76% fewer parameters and translating a cache pair 10.3x faster (5.8 vs. 59.9 ms); end to end, XKV is 26% faster than LCF-X and 6.8x faster than text communication.

</details>


### 21. Testing and Evaluation of Agentic AI Systems In Military Command and Control

- **Authors:** Ulysse Richard, Heather Frase, Sarah Cao, Di Cooke, Sebastian Kwon, Adrianna Tan
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20597v1](http://arxiv.org/abs/2608.20597v1)
- **PDF:** [https://arxiv.org/pdf/2608.20597v1](https://arxiv.org/pdf/2608.20597v1)
- **Categories:** cs.SE, cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems are being procured for military command and control (C2) under public commitments to rigorous testing and human oversight. Whether such commitments can be discharged depends on their supporting assurance case, which requires three elements: claims specifying the conditions for acceptability, evidence bearing on those claims, and an argument connecting the two. Through a structured review of 240 documented Testing and Evaluation (T&E) practices, spanning eight evaluation dimensions and three lifecycle stages, we identify eight assumptions that established methods make about their test article, grouped into four clusters: system specifiability, stability, composability, and supervisability. Agentic properties weaken all eight assumptions. This erosion affects the argument connecting evidence to claims, not the claims or evidence themselves. As a result, test results may satisfy process requirements, but they do not warrant the inference from tested to fielded behavior.
  We derive ten assurance claims for the first three assumption clusters and assess whether current and emerging methods can address each, mapping operational consequences through five C2 scenarios. Supervisability is identified but not assessed here, since evidencing it depends on system stability results and human factors T&E methods beyond the present scope. The documented record does not support broad claims about system-level behavior, but narrower claims remain recoverable in principle, contingent on mature methods: bounded mission envelopes, trajectory-grounded correctness, executable runtime constraints, and characterized run-to-run variance. Part of the evidentiary burden shifts into deployment, making the determination to field a continuing act. Where evidence cannot be generated, the residual uncertainty can be governed through defined expiry conditions and assigned ownership.

</details>


### 22. AgentDecarbonizer: Carbon-Aware Execution for AI Agents

- **Authors:** Leyi Yan, Shuangning Li, Sihang Liu
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20566v1](http://arxiv.org/abs/2608.20566v1)
- **PDF:** [https://arxiv.org/pdf/2608.20566v1](https://arxiv.org/pdf/2608.20566v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents extend large language models from single prompt-response interactions to long-running, goaldirected workflows that issue many model calls, invoke tools, and interact with external environments. These workflows enable tasks such as software repair, data analysis, and experiment management, but their repeated model invocations can incur substantial carbon emissions. This paper characterizes the carbon emissions of OpenClaw agent workloads using WildClawBench, and shows that emissions depend on token consumption, context cache reuse, and the carbon intensity of the grid. Our characterization identifies deadline flexibility as an opportunity for carbon-aware execution: agent tasks can wait for lower-carbon-intensity periods or shift to lower-carbon grids. However, doing so requires handling uncertain execution time for temporal shifting and cached context recomputation during spatial shifting. We present AgentDecarbonizer, a carbon optimizer for AI agents that runs alongside OpenClaw. Given a task prompt and user-specified deadline, AgentDecarbonizer conservatively estimates task duration and selects deadline-feasible execution schedules, while accounting for cache recomputation overhead during spatial shifting. Evaluated on WildClawBench workloads with 60 agent tasks across four grids, AgentDecarbonizer reduces carbon emissions by up to 57.9 % compared with a carbon-agnostic baseline and by up to 37.5 % compared with a baseline that selects the carbon-optimal grid at task start time.

</details>


### 23. Consilience: Conformally Calibrated Communication Control for Hidden-Profile Multi-Agent Reasoning

- **Authors:** Abhijith Babu, Ramneet Kaur, Vishal Pramanik, Olivera Kotevska, Nathaniel D. Bastian, Susmit Jha, Sunny Raj, Yanzhao Wu, Sumit Kumar Jha, Anirban Roy
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20564v1](http://arxiv.org/abs/2608.20564v1)
- **PDF:** [https://arxiv.org/pdf/2608.20564v1](https://arxiv.org/pdf/2608.20564v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems can improve reasoning by pooling diverse perspectives, but their effectiveness depends on coordinating communication, particularly in hidden-profile settings where each agent holds only part of the evidence required for a correct decision. Existing protocols, including fixed schedules, round-robin exchange, and unstructured debate, provide no guarantee that a conversational action is appropriate. We propose Consilience, an inference-time orchestration framework that both steers and certifies multi-agent communication under distributed private information. At each turn, Consilience summarizes the discussion using a compact state capturing uncertainty, disagreement, evidence gain, redundancy, and premature consensus, then selects both a communication intervention (challenge, clarify, seek evidence, or route) and an appropriate speaker. Its central contribution is a round-wise conformal calibration procedure that provides a distribution-free, finite-sample guarantee: at each discussion round, conditional on reaching that round, the one-step regret of a controller's proposed action is bounded by a calibrated threshold with marginal probability at least 1 - alpha; an acceptance mechanism enforces the same guarantee for the executed action by replacing inadmissible proposals. On HiddenBench-style hidden-profile tasks spanning 12 open and closed weight language models, Consilience improves decision accuracy and communication efficiency over fixed and unstructured discussion protocols, sometimes surpassing a full-information baseline where every agent observes all evidence. These results demonstrate that certified adaptive communication control can be more valuable than increasing information availability, providing a practical mechanism for reliable multi-agent LLM coordination.

</details>


### 24. Beyond End-to-End Success: Diagnosing Failures in Long-Horizon Security LLM Agents

- **Authors:** Wei Shao, Chongzhou Fang, Zuxiong Tan, Zequan Liang, Setareh Rafatirad, Avesta Sasan, Houman Homayoun
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20563v1](http://arxiv.org/abs/2608.20563v1)
- **PDF:** [https://arxiv.org/pdf/2608.20563v1](https://arxiv.org/pdf/2608.20563v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon security LLM agents must carry information and decisions across many dependent interactions, where later actions often depend on services, state, or access discovered much earlier. This makes final task success difficult to interpret: an agent may fail before it ever reaches the point where the capability of interest can be exercised. We present a diagnostic methodology that instruments security tasks with checkpoints, separates failures before and after capability exposure, and uses controlled interventions to test suspected upstream bottlenecks. We evaluate the methodology across four task families involving delayed reuse of discovered information, reuse of observed state, recovery from failed strategies, and decision making after uncertain outcomes. On observed state reuse, checkpoint analysis shows that many Gemini 2.5 Flash failures occur before the model observes the state it is later expected to reuse. In a pre-specified 92-seed study, targeted protocol-disambiguation guidance increases state observation from 65.5\% under a matched non-guidance control message to 95.4\%. Repeating the same design with Gemini 3.7 Flash produces the opposite effect, while state observation no longer reliably predicts task completion. These results show that the dominant source of failure can shift across model generations, motivating evaluation that diagnoses where and why long-horizon security agents fail rather than relying only on aggregate task success.

</details>


### 25. FL-MAESTRO: Multi-Agent LLM Orchestration for Resource-Constrained Federated Learning

- **Authors:** Jiajun Wu, Zirui Wang, Jiayu Zhou, Qiang Ye, Steve Drew
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20518v1](http://arxiv.org/abs/2608.20518v1)
- **PDF:** [https://arxiv.org/pdf/2608.20518v1](https://arxiv.org/pdf/2608.20518v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In Federated Learning (FL), the communication topology is a runtime variable rather than a fixed design choice, since links and edge devices drop in and out during training. Each round, the server must commit three coupled decisions, namely the communication topology, per-client resource allocation, and the aggregation rule for combining local updates. Recent agentic systems have begun bringing large language models (LLM) into FL, but the existing line of work either operates at setup time or handles a single runtime dimension such as client selection. We propose FL-MAESTRO, a multi-agent orchestrator that makes the joint runtime FL decision directly through three specialist LLM agents, one per decision dimension. A coordinator combines their analyses into a single decision, and a non-LLM feasibility check confirms it before the round executes. Because the orchestrator consumes the server's predicted-failure list, it withholds clients whose updates would never be aggregated, which removes the dominant source of wasted round energy in classical FL on volatile edge networks. Because client state is read as natural-text profiles, the same orchestrator extends to heterogeneous device classes without per-class energy models. On a non-IID CIFAR-10 benchmark, FL-MAESTRO matches the accuracy of the strongest energy-aware baseline while cutting wasted round energy from over a third to near zero. Code is available at https://github.com/denoslab/FL-MAESTRO.

</details>


### 26. Towards Traffic Modelling of Multi-Agent Systems: The Role of Coordination Topology

- **Authors:** Davide Lamagna, Albert Cabellos, Alberto Rodriguez-Natal, Gábor Rétvári, Berta Serracanta
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20494v1](http://arxiv.org/abs/2608.20494v1)
- **PDF:** [https://arxiv.org/pdf/2608.20494v1](https://arxiv.org/pdf/2608.20494v1)
- **Categories:** cs.NI, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems are an emerging networked workload whose rapid deployment raises questions about the traffic patterns they generate. Compared to conventional applications, these systems generate requests internally: a single user task can induce a structured sequence of model calls whose timing is governed by coordination logic rather than by user arrival rate. It is not clear whether classical traffic models, designed for human-driven workloads, apply to this setting.
  We present an empirical characterisation of LLM-call interarrival time distributions across sequential, star, and full-mesh agentic coordination topologies, using a multi-layer measurement framework over 500 repeated runs per topology. We find that topology fundamentally shapes the arrival process of requests to the LLM backend: fan-out coordination introduces a structural bimodality absent in sequential execution, and the reasoningphase component is best described by a log-normal distribution, with the Poisson exponential null model decisively rejected across all topologies. These differences propagate to inference and network level metrics. The framework and analysis pipeline are released openly at https://github.com/dlamagna/agentraffic.

</details>


### 27. Terminal Agents: A Survey of AI Agents in Command-Line Environments

- **Authors:** Yi Bin, Xiaoyang Yuan, Haoxi Zeng, Wencheng Ye, Wenqi Shao, Chen Qian, Wei Ye, Yujuan Ding, Zheng Wang, Pengpeng Zeng, Jingkuan Song, Heng Tao Shen
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20485v1](http://arxiv.org/abs/2608.20485v1)
- **PDF:** [https://arxiv.org/pdf/2608.20485v1](https://arxiv.org/pdf/2608.20485v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents increasingly act through terminals, yet existing surveys disperse terminal-mediated behavior across software engineering, tool use, and computer-use research. We regard terminal agents as systems whose dominant progress-bearing action--observation loop is mediated by terminal command execution, textual feedback, and stateful environment interaction. Using terminal-mediated execution as an organizing lens, this survey establishes workload-level boundaries and connects system architecture, competence acquisition, and evaluation through a seven-dimensional terminal competence profile. Our synthesis shows that realized behavior is jointly shaped by the model, interface, harness, runtime, and environment. Executable trajectories ground learning in action consequences, verification, and recovery, whereas prevailing evaluations emphasize final outcomes and expose process quality, recovery, and governance unevenly. Bounded fixed-condition diagnostics illustrate two implications: benchmark families expose different process signals, and matched system comparisons reveal benchmark-dependent performance and limits of component attribution. These findings motivate explicit reporting of system and runtime conditions, supported by replayable traces and process-level evidence. The framework provides a unified basis for studying terminal-mediated agency across software engineering and emerging application domains.

</details>


### 28. An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and Weather-Sensitive Demand Prediction

- **Authors:** Narges Ahmadi, Yubo Jiao, Jônatas Augusto Manzolli, Jiangbo Yu, Luis Miranda-Moreno
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20320v1](http://arxiv.org/abs/2608.20320v1)
- **PDF:** [https://arxiv.org/pdf/2608.20320v1](https://arxiv.org/pdf/2608.20320v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Travel behavior research increasingly combines digital data collection with predictive modeling, yet these stages are often developed and evaluated separately. This study proposes a three-agent workflow integrating conversational data collection, structured data processing, and behavioral prediction. A chatbot-administered, image-augmented stated-preference survey collected mode choices from student commuters across five predefined weather scenarios, yielding 454 respondent-scenario observations. Weather-related associations were analyzed using a multinomial logit model, while logistic regression and random forest provided machine-learning benchmarks. Nine locally deployed large language models (LLMs), ranging from 2 to 35 billion parameters, were evaluated across four zero-shot prompt-and-context conditions and extended through persona, few-shot, and vision-based configurations. Random forest achieved 69.6% five-class accuracy, while the best text-only zero-shot LLM reached 69.9% without task-specific fitting. Habitual travel information produced the most consistent gains, Expert framing generally outperformed Role-Play, and persona information was most useful when habitual travel information was unavailable. Few-shot prompting improved prediction for several models, with gains stabilizing after a small number of examples. Using the same weather images shown to respondents, the best vision-based configuration reached 71.5% five-class accuracy, indicating that visual context may provide additional predictive information for selected models. Overall, the study shows how conversational surveys, structured data processing, conventional behavioral modeling, machine learning, and multimodal LLM prediction can be coordinated within an auditable multi-agent workflow.

</details>


### 29. AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement

- **Authors:** Yizhe Chi, Wenyi Li, Deyao Hong, Xiaoqiu Wang, Mingju Gao, Kaisen Yang, Bingxiang He, Youjie Zheng, Calvin Xiao, Qinhuai Na
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20318v1](http://arxiv.org/abs/2608.20318v1)
- **PDF:** [https://arxiv.org/pdf/2608.20318v1](https://arxiv.org/pdf/2608.20318v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recursive self-improvement (RSI) asks whether an AI system can improve the process that produces AI systems, so that the next system inherits the improvement. That process is the training algorithm: a better objective or update rule improves the compute\mbox{-}capability exchange rate for every subsequent run, including the one that produces the next agent. Whether RSI is feasible therefore turns on whether an agent can design training algorithms. No benchmark isolates that ability: existing suites are won by collecting data or by tuning hyperparameters, and none tells a change to how a run is executed apart from a change to how the model learns. We present AI4AI\mbox{-}Bench, 10 frozen research repositories spanning 10 training algorithm families. In each task, an agent has 4 hours on one B300 to rewrite the training algorithm; its code is then rerun from scratch for up to 12 hours and scored by a fixed evaluator hidden from the agent, against the repository's original algorithm under the same procedure. Because the 10 metrics are incommensurable, every task is mapped onto one scale on which $0$ is an uninformative model, $0.1$ is the algorithm the repository ships, and $1.0$ is the task optimum. Across 29 configurations of 6 systems on all 10 tasks the mean score is $0.166$, and the best system reaches $0.250$: even the strongest closes under a fifth of the distance between the algorithm that was already there and the optimum. The submissions show where that distance went: most never change how the model learns at all, and the minority that do average $0.226$ against $0.126$ for the rest. More reasoning effort mostly buys the willingness to go there, taking that minority from $8\%$ of submissions to $64\%$ and the mean score from $0.094$ to $0.196$. We release the task suite, the evaluators and every scored submission, so that the measurement can be repeated as these systems change.

</details>


### 30. MidTool: Mid-training Data Synthesis for Agentic Tool Use

- **Authors:** Fengqing Jiang, Yite Wang, Boyi Liu, Zhaoyang Wang, Canwen Xu, Zhewei Yao, Radha Poovendran, Yuxiong He
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20314v1](http://arxiv.org/abs/2608.20314v1)
- **PDF:** [https://arxiv.org/pdf/2608.20314v1](https://arxiv.org/pdf/2608.20314v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mid-training is increasingly recognized as a critical stage for shaping the capabilities of large language models. Recent work has shown that targeted mid-training can strengthen reasoning-intensive abilities such as math and science, and can also improve agentic capabilities in software-engineering settings. In this work, we study the parallel but less explored agentic capability: general tool use. We present MidTool, an open corpus construction pipeline for agentic tool-use mid-training that combines large-scale web, PDF, and code data with synthesized supervision from real-world tool APIs, MCP skills, and document-grounded workflows. MidTool is designed to teach models how to recognize tool affordances, ground arguments from context, compose tool call workflow, and recover from incomplete information. We mid-train Qwen3-4B-Base and Qwen3-8B-Base on MidTool-Mix, and then apply follow-up post-training with both supervised fine-tuning and reinforcement learning. Compared with baselines, MidTool-Mix consistently improves downstream performance under both SFT and RL on BFCL, tau2-Bench, and MCP Universe. These results suggest that general tool use, like other important LLM capabilities, benefits from dedicated mid-training rather than being left entirely to post-training.

</details>


### 31. Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents

- **Authors:** Yiyang Feng, Biddut Sarker Bijoy, Niranjan Balasubramanian, Jiawei Zhou
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20274v1](http://arxiv.org/abs/2608.20274v1)
- **PDF:** [https://arxiv.org/pdf/2608.20274v1](https://arxiv.org/pdf/2608.20274v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents can induce skills from completed tasks and reuse them later to grow more capable with experience. In practice, induced skills may transfer unreliably and can even harm the agent that retrieves them. When agent-induced skills transfer reliably across tasks remains an open question. We conduct a comprehensive and controlled study of how the way skills are induced shapes their transfer across tasks. Specifically, we compare task-level with subtask-level skill induction and text with code skill formats, the two axes along which existing methods differ. Task-level skills mostly reduce the agent's performance below its no-memory baseline while subtask-level skills raise it above on average, and text skills transfer better than code skills. To further understand our findings, we examine two complementary properties of the induced skills: specificity, which measures how closely a skill matches real tasks, and abstractness, which measures how evenly its relevance spreads across tasks. Neither property alone predicts task success, but their combined effect does, which we propose as a skill utility score. The score correlates consistently with task success when skills are transferred, and subtask-level and text skills score higher. Computing skill utility only needs the skills and task descriptions but not any task execution, so our score serves as a practical diagnostic of a skill memory before any new task runs.

</details>


### 32. Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection

- **Authors:** Atsuyuki Miyai, Kiyoharu Aizawa, Toshihiko Yamasaki
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20169v1](http://arxiv.org/abs/2608.20169v1)
- **PDF:** [https://arxiv.org/pdf/2608.20169v1](https://arxiv.org/pdf/2608.20169v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present a novel approach to efficient LLM agent harness optimization through adaptive validation task selection. Harness optimization iteratively rewrites the harness code based on validation performance, enabling substantial performance gains without updating the underlying model weights. Existing approaches, however, evaluate a fixed validation set in full at every iteration, incurring substantial evaluation costs even on tasks that become less discriminative as the harness evolves. We propose $\textbf{Task-CoEvolve}$, which co-evolves the validation tasks with the harness by addressing two challenges: selecting informative tasks and estimating full-set performance from partial evaluations. Task-CoEvolve builds on the observation that tasks on which candidate harnesses disagree are more informative for distinguishing among them than tasks that are consistently solved or failed. It uses variance-weighted sampling based on past outcomes to focus evaluation on tasks near the agent's capability frontier, with the sampling distribution adapting as the harness evolves. It then estimates full-set scores from the sampled tasks by accounting for their sampling probabilities, enabling consistent comparisons across iterations despite evaluating different subsets. Experiments on online text classification and Terminal-Bench 2.1 show that Task-CoEvolve consistently outperforms fixed-subset baselines and matches the final performance of full-set search while reducing the number of evaluations during optimization by 80%. Code will be released at https://github.com/Agent4Science-UTokyo/Task-CoEvolve.

</details>


### 33. Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving

- **Authors:** Mehdi Azarafza, Faezeh Pasandideh, Ali Ehteshami Bejnordi, Stefan Henkler, Achim Rettberg
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20129v1](http://arxiv.org/abs/2608.20129v1)
- **PDF:** [https://arxiv.org/pdf/2608.20129v1](https://arxiv.org/pdf/2608.20129v1)
- **Categories:** cs.MA, cs.CL, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous vehicles require robust perception and decision-making capabilities to operate in diverse and unseen scenarios. While reinforcement learning and rule-based methods can provide effective control and safety mechanisms, their performance may degrade in situations requiring contextual reasoning. Large Language Models (LLMs) have demonstrated strong capabilities in understanding multimodal information and generating contextual reasoning, however, their use for direct vehicle control can introduce latency and hallucination risks. To address these limitations, a hybrid framework is proposed. This system uses an orchestrator to coordinate PPO-trained reinforcement learning and PID control, with LLM common-sense reasoning applied throughout the framework. LLM reasoning is further employed iteratively to refine the RL reward function for dynamic driving environments. The proposed framework is evaluated in highly randomized CARLA scenarios under diverse environmental and traffic conditions. The results demonstrate the potential of integrating LLM-based reasoning with conventional autonomous driving methods while retaining structured control and safety mechanism.

</details>


### 34. Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication Topology Design

- **Authors:** Poomphob Suwannapichat, Boonyarit Changaival, Caesar Wu, Pascal Bouvry
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20099v1](http://arxiv.org/abs/2608.20099v1)
- **PDF:** [https://arxiv.org/pdf/2608.20099v1](https://arxiv.org/pdf/2608.20099v1)
- **Categories:** cs.MA, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based Multi-Agent Systems (MAS) achieve strong performance on complex reasoning tasks by coordinating multiple agents, but at the cost of substantial token consumption. Recent work on automatic topology design, ARG-Designer, has reframed this problem as autoregressive graph generation. However, its training objective provides no explicit incentive for the model to generate sparse and efficient topologies. We address this limitation by introducing a Reward-Guided Autoregressive Graph Generation (RGA-Designer) inspired by Reinforcement Learning from Human Feedback (RLHF). We train a reward model that jointly captures task correctness and structural compactness, and then fine-tune the pretrained graph generator using the reward model as feedback. Our method preserves task accuracy at the level of ARG-Designer while reducing token consumption by an average of 20.5%.

</details>


### 35. A three-dimensional typology of agency for advanced AI systems

- **Authors:** Willem Fourie
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20041v1](http://arxiv.org/abs/2608.20041v1)
- **PDF:** [https://arxiv.org/pdf/2608.20041v1](https://arxiv.org/pdf/2608.20041v1)
- **Categories:** cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Research on the agency of advanced artificial intelligence (AI) systems focuses on agency as a normative concept and on the agency of particularly agentic AI systems. While recent work also focuses on the different profiles of agentic systems, no framework exists to address the question of the type of agency instantiated by advanced AI systems, particularly when considering non-moral forms of agency. Based on established theoretical positions in philosophy, ethics, legal theory and sociology, we develop a typology of agency for frontier AI systems consisting of three dimensions: the nature of agency (moral or legal), its mode (individual or collective) and its locus (human or non-human). Combining these dimensions produces eight possible instantiations of agency, which we classify as conventional, contested or controversial. The typology separates legal from moral agency and thereby creates conceptual space for considering individual, legal, non-human agency without presupposing that advanced AI systems are moral agents. We argue that this distinction is increasingly relevant where instrumental goal pursuit complicates the attribution of AI actions to particular human actors.

</details>


### 36. Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees

- **Authors:** Yu Chen, Ruishuo Chen, Xun Wang, Zhuoran Li, Longbo Huang
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19993v1](http://arxiv.org/abs/2608.19993v1)
- **PDF:** [https://arxiv.org/pdf/2608.19993v1](https://arxiv.org/pdf/2608.19993v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Loading reusable skill documents into a bounded context window is now the primary way large language model (LLM) agents acquire task-specific capabilities, which makes skill selection a first-order determinant of task performance and token cost. Yet current agents score skills independently by semantic relevance and assemble the set by top-$k$ or greedy packing, with no quality guarantee or cost awareness on the selected set. As a result, redundant or poorly chosen skills waste scarce context tokens and can even degrade performance. We give the first model of how the selected skill set shapes execution outcomes and cast skill selection as an optimization problem: choose a skill set under a hard token budget to maximize a monotone submodular benefit minus context penalty. For this problem, we develop Best Prefix Selection (BPS), a polynomial-time algorithm, and prove, to our knowledge, the first performance guarantee for skill selection: a bicriteria $(1-1/e,1)$ approximation whose benefit coefficient is optimal in polynomial time. On a contamination-controlled BigCodeBench variant, BPS outperforms all the baselines, reaching $0.73$ measured task success versus $0.20$--$0.52$ for released skill routers, text retrievers, and the executor's own selection, on $28\%$ fewer tokens than the strongest released router.

</details>


### 37. ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance

- **Authors:** Yiyang Luo, Yihang Jiang, Qijun Xie, Liang Lan, Lin Willian Cong, Anyi Rao, Yunya Song
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19974v1](http://arxiv.org/abs/2608.19974v1)
- **PDF:** [https://arxiv.org/pdf/2608.19974v1](https://arxiv.org/pdf/2608.19974v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents in financial markets may cite rules yet still submit orders that violate executable constraints or misread surveillance evidence. We introduce ReguSim, a controlled financial-compliance environment, and ReguBench, a target-marked monitoring benchmark, to separate four artifacts: stated reasoning, attempted action, execution enforcement, and monitor evidence. In trader runs with DeepSeek V4 Pro and Gemini 3.5 Flash, visible rules reduce but do not eliminate rejected actions, and incentive or persona framing shifts behavior. A bridge study shows that trader rationales can mislead an independent monitor unless enforcement evidence is shown. In monitoring, simple structured baselines either match or exceed prompt-only LLMs. The results frame financial compliance evaluation as an audit of rule-grounded actions and evidence use, rather than a single compliance score.

</details>


### 38. G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs

- **Authors:** Bhavya Gupta, Onat Gungor, Tajana Rosing
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19964v1](http://arxiv.org/abs/2608.19964v1)
- **PDF:** [https://arxiv.org/pdf/2608.19964v1](https://arxiv.org/pdf/2608.19964v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous driving systems must operate under partial observability, where safety-critical objects may be occluded or visible only to neighboring connected vehicles. Vehicle-to-vehicle cooperation can reduce this uncertainty, but existing cooperative driving methods often compress multi-agent evidence into latent features or hidden multimodal states. As a result, they obscure which agent observed each object, whether the object is visible to the ego vehicle, and how conflicting evidence affects downstream decisions. We propose G-MARK, a grounded multi-agent reasoning framework that converts cooperative object-centric observations into explicit provenance-aware knowledge graphs (KGs). The resulting KGs preserve object hypotheses together with their source attribution, ego-versus-partner visibility, uncertainty, conflicts, spatial relations, and planning-relevant context. G-MARK then derives a shared feature representation from these KGs, enabling lightweight task heads to support object reasoning, motion prediction, control selection, and trajectory forecasting. Compared with the state-of-the-art baseline, GMARK improves occlusion reasoning accuracy by 42.2%, reduces control-selection error by 13.1%, and achieves comparable trajectory-planning accuracy with a 25.6x smaller structured communication payload. Our code is available at https://github.com/bhavyagupta98/g-mark.

</details>


### 39. Bringing analytic rigor to agentic AI for science: The Brain Researcher platform for neuroimaging data analysis

- **Authors:** Zijiao Chen, Nicholas Lu, Xinhui Li, Jocelyn A. Ricard, Ce Ju, Huan H. Wang, Christian Kindermann, Jeanette A. Mumford, Steven Dillmann, James Kent, Alejandro de la Vega, Sanmi Koyejo, Vince D. Calhoun, Joshua W. Buckholtz, Juan Helen Zhou, Steffen Bollmann, Russell A. Poldrack
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19902v1](http://arxiv.org/abs/2608.19902v1)
- **PDF:** [https://arxiv.org/pdf/2608.19902v1](https://arxiv.org/pdf/2608.19902v1)
- **Categories:** cs.AI, q-bio.NC


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can execute scientific analyses, but an analytic output becomes a defensible claim only after alternatives are weighed and the claim is limited to what the evidence supports. Agents may reproduce failures including selective analysis, premature declarations of success and optimization of imperfect criteria. We present Brain Researcher, an agentic research harness operating in a neuroimaging researcher's computational environment under rules for admissible analyses, required checks and claim scope. In benchmarks, Brain Researcher increased first-choice tool-selection accuracy across seven models by 70.2 percentage points (23.3% without it versus 93.6% with it) and verifiable grounding from 4.6% to 22.0%. In collaborator-led and self-evolving studies, multiverse analyses exposed analytic-choice sensitivity, and scientific review classified claims as accepted, qualified, revised, blocked, rejected or deferred. By linking decisions to evidence and provenance, Brain Researcher embeds methodological judgment within the workflow, not after it.

</details>


### 40. MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection

- **Authors:** Yue Wang, Yi Liu, Gelei Deng, Ying Zhang, Yuekang Li, Zhenyu Chen, Leo Zhang
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19901v1](http://arxiv.org/abs/2608.19901v1)
- **PDF:** [https://arxiv.org/pdf/2608.19901v1](https://arxiv.org/pdf/2608.19901v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent Skills extend LLM agents with reusable instruction packages that may also include scripts, resources, and service configuration. This creates a direct distribution channel for malicious behavior, yet existing malicious-Skill datasets are fragmented across sources, artifact formats, evidence regimes, and benign coverage; duplicated and structurally related content further complicates direct aggregation and evaluation. We present MaliciousSkillBench, a comprehensive benchmark for malicious Agent Skill detection. We consolidate 13 public sources, 11 of which contribute Core malicious artifacts, and reduce 8,414 raw malicious records to 7,539 normalized-unique identities in 4,588 operational structural families. After conservative cross-label conflict exclusion, the primary benchmark contains 9,740 Skills: 7,505 malicious and 2,235 benign. To characterize its coverage, we harmonize 11 attack categories for 4,983 malicious identities with supported source-native mappings and find substantial differences in threat composition across sources. We then evaluate three learned text detectors and three off-the-shelf Skill scanners. Learned detectors achieve 0.882-0.932 Random Macro-F1 but only 0.653-0.665 under Source-Disjoint evaluation; the strongest word TF-IDF SVM scores 0.932/0.916/0.665 on Random/structural-disjoint/Source-Disjoint while retaining 95.6% malicious recall but producing 62.4% benign FPR on held-out sources. Off-the-shelf scanners occupy different but also unsatisfactory operating regimes, reducing false positives only at the cost of sharply lower malicious recall. Together, these results show that reliable malicious-Skill detection requires both broader cross-source benchmark coverage and evaluation that jointly measures attack detection and benign over-flagging.

</details>


### 41. EnvHarness: Awakening Static Worlds for Agent Learning

- **Authors:** Chengsong Huang, Zifeng Wang, Rujun Han, Jun Yan, Yanfei Chen, Zoey CuiZhu, Ke Jiang, Peng Xia, Han Yu, Yufan Zhuang, Yifei Ming, Jiaqi Pan, Bhavana Dalvi Mishra, Jiaxin Huang, Burak Gokturk, Tomas Pfister, Chen-Yu Lee
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19880v1](http://arxiv.org/abs/2608.19880v1)
- **PDF:** [https://arxiv.org/pdf/2608.19880v1](https://arxiv.org/pdf/2608.19880v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents learn by interacting with environments, yet these environments are hand-built and static: blind to an agent's weaknesses, and quickly left behind as it improves. While recent environment generation methods attempt to address this, they require domain-specific pipelines, rely on expensive or unreliable verifiers, and still produce static environments. To alleviate the engineering burden of rebuilding environments from scratch, we propose Environment Harness (EnvHarness), a programmable layer of plug-in components that wraps a static environment to reshape its behavior without modifying the underlying logic. Operating through standard interfaces, EnvHarness applies across diverse domains while ensuring every reshaped environment retains its original verifier. To automate this process, we introduce EnvRigger, which treats the target policy as a black box, observing its execution trajectories to synthesize EnvHarness components targeting diagnosed flaws, and validating them via fresh rollouts. Across five benchmarks in four domains, EnvHarness outperforms both original environments and domain-specific environment generation pipelines, achieving up to a 9.0-point improvement on held-out instances with 9.8% fewer execution steps. Furthermore, EnvHarness provides a superior optimization signal for reinforcement learning, enabling continuous, targeted co-evolution of the policy and its environment.

</details>


### 42. PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents

- **Authors:** Seongjae Kang, Taehyung Yu, Sung Ju Hwang
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19861v1](http://arxiv.org/abs/2608.19861v1)
- **PDF:** [https://arxiv.org/pdf/2608.19861v1](https://arxiv.org/pdf/2608.19861v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Customer-service LLM agents must follow organizational policy when acting on a user's behalf. Compliance failures arise from either forbidden actions, such as granting an ineligible change, or omitted procedural requirements, such as identification or confirmation. Runtime safeguards can intervene on risky actions, but action-local checks do not guide an agent through a multi-step procedure. Workflow-following systems support prescribed process execution, but primarily target workflow completion rather than safeguarding agent behavior. PolicyGuide instead compiles each domain policy into a workflow graph and invokes a proactive verifier at user-turn boundaries. From persisted graph state, the verifier reconciles open requests and returns step-specific remediation along a policy-compliant path. Across the $τ^2$-bench airline, retail, and telecom domains with a GPT-5.4 agent and verifier, PolicyGuide raises mean $\mathrm{Pass}^4$ from $0.42$ to $0.62$, with the largest gain on telecom ($0.19$ to $0.61$), the most workflow-structured domain. The same workflows transfer to Claude Sonnet 4.6 and Gemini 2.5 Pro agents. Complementary evaluations find the lowest observed attack-success rate under adversarial users and the strongest procedural compliance in an author-designed workflow-level validation.

</details>


### 43. Inadvertent Context Leakage in Language Models

- **Authors:** Jaiden Fairoze, Neal Mangaokar, Kamalika Chaudhuri, Sanjam Garg, Saeed Mahloujifar
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19857v1](http://arxiv.org/abs/2608.19857v1)
- **PDF:** [https://arxiv.org/pdf/2608.19857v1](https://arxiv.org/pdf/2608.19857v1)
- **Categories:** cs.LG, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

For AI agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert carrier to transmit secrets through seemingly innocuous text. In both cases, this limited leakage is exploited using a novel adaptive attack that assumes black-box access to the underlying model.
  In controlled experiments across eight proprietary models, we find that 2-digit in-context secrets are reconstructed with near-perfect accuracy and 4-digit secrets at 82\% exact match, all from outputs the model produces in response to ordinary, non-adversarial requests. We observe that more capable models leak more: stronger instruction-following amplifies sensitivity to in-context secrets, suggesting leakage is a byproduct of capability as opposed to a patchable bug. We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent.

</details>


### 44. MileGPO: Milestone Inference with Local Evidence for Graph-Based Policy Optimization of Long-Horizon LLM Agents

- **Authors:** Bo Qian, Yuting Wu, Shuang Zeng, Huaiyu Wan, Dalin Zhang, Jiqiang Liu
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19803v1](http://arxiv.org/abs/2608.19803v1)
- **PDF:** [https://arxiv.org/pdf/2608.19803v1](https://arxiv.org/pdf/2608.19803v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Credit assignment is challenging in long-horizon agentic reinforcement learning, where supervision often comes only from final rewards. Existing methods refine trajectory-level signals into step-level credits through step grouping or graph-based advantage estimation, but can overlook meaningful intermediate milestones. We propose MileGPO (Milestone Inference with Local Evidence for Graph-Based Policy Optimization), which derives process-level credit from grouped on-policy rollouts through three designs. Milestone Discovery identifies candidate milestones on successful rollouts and recurring traps on failed ones. Reliability-Calibrated Shaping (RCS) weights these candidates by outcome-based confidence, strengthening reliable milestones and traps while down-weighting uncertain ones. Progress-Contrastive Calibration (PCC) further tests whether a candidate reflects local progress and whether its incoming ansition outperforms observed alternatives from the same state.MileGPO requires neither auxiliary models nor additional environment interaction. Experiments on ALFWorld and WebShop show state-of-the-art performance and a small in-distribution to out-of-distribution gap on ALFWorld. Ablations and credit diagnostics indicate that reliability weighting, local progress, and same-state branch evidence complement milestone discovery and resolve ambiguous intermediate credit.

</details>


### 45. Towards general embodied intelligence: integrating large language models, knowledge bases, and reasoning capabilities to build the next generation of AI agents

- **Authors:** Fujiang Yuan, Xia Huang, Lusheng Wang, Jun Ding, Zhen Tian, Yuxin Wang, Shaojie Gu, Yuki Funabora, Yanhong Peng, Zebing Mao
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19794v1](http://arxiv.org/abs/2608.19794v1)
- **PDF:** [https://arxiv.org/pdf/2608.19794v1](https://arxiv.org/pdf/2608.19794v1)
- **Categories:** cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

The convergence of large language models (LLMs), structured knowledge bases (KBs), and reasoning ability (RA) presents a promising trajectory toward general embodied intelligence (GEI). This paper reviews the evolution of LLM-centered intelligent systems, emphasising their integration with knowledge representation, logical reasoning, and physical embodiment. We analyse LLM architectures, pre-training methods, and inference mechanisms, along with their interaction with external knowledge sources and structured reasoning frameworks. Furthermore, we examine embodied intelligence (EI) paradigms wherein agents learn and act in physical environments. To synthesise these dimensions, we present a conceptual framework that illustrates the synergy among LLMs, KBs, RA, and embodiment, serving as a guiding model for perception, reasoning, and action rather than an implemented engineering architecture. To advance toward GEI, we identify five key challenges: efficient LLM deployment, closed-loop knowledge integration, hybrid symbolic-neural reasoning, perception-action grounding, and continual learning. This survey provides a comprehensive roadmap for developing adaptive, multimodal agents capable of operating in complex, dynamic settings.

</details>


### 46. Credit Without Ground Truth: Auditing Step-Level Credit Assignment in LLM Agents Against Executed Replay

- **Authors:** Haiyue Zhang
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19760v1](http://arxiv.org/abs/2608.19760v1)
- **PDF:** [https://arxiv.org/pdf/2608.19760v1](https://arxiv.org/pdf/2608.19760v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Audited against causal ground truth from executed replay in a single-agent tool environment (ALFWorld), none of the step-level credit signals used to train LLM agents -- LLM-judge scores, outcome-conditioned logprob ratios, or the policy's own confidence -- identifies which steps causally matter better than chance. Existing evaluations grade these signals against annotated step *correctness*; we audit them against step *contribution* -- what re-sampling the policy's own alternatives at each decision point and rolling forward actually changes about the outcome -- and the two come apart. The ground truth itself is structured: causal contribution is sparse (30.5% of decision points where ground truth is defined carry measurable effect), and measurability is model-dependent -- the fraction of points with no policy-supported counterfactual differs by a factor of two (13.1% vs. 26.8%) between two similar-scale policies. The failure mode is identifiable: implicit credit echoes the policy's fluency (median rank correlation +0.75, replicating at +0.70 in a second family under a corrected instrument), while conditioning on the outcome adds no causal information (partial correlation -0.004, Qwen). A confidence-only router recovers pivotal steps at chance level, but cuts judge cost by 13.1% per turn (14.0% per trajectory). In a seven-arm pre-registered training experiment, no arm reliably outperforms the untrained policy, and the checkpoints' apparent instrument signature is fully explained by training dose -- sparser credit retains fewer examples, an order-of-magnitude spread in optimizer steps -- not credit content. Comparisons of credit rules must therefore match effective sample size, or they measure dose, not credit.

</details>


### 47. One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows

- **Authors:** Zhuochun Li, Youngmin Ko, Ali Keramati, Nicola Ferri, Susana Palmaz Lopez Pelaez, Liang-Chun Tsai, Calvin Wang, Mirco Milletari, Tuhin Kundu, Vadim Smolyakov, Kjartan Olafsson, Tommy Guy
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19741v1](http://arxiv.org/abs/2608.19741v1)
- **PDF:** [https://arxiv.org/pdf/2608.19741v1](https://arxiv.org/pdf/2608.19741v1)
- **Categories:** cs.CL, cs.DB


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent agent benchmarks increasingly ground evaluation in executable environments, from code repair to web navigation, app APIs, and function calling. Yet completing consequential work beyond code requires more than producing a plausible response or valid tool call: agents must gather missing information over multiple turns, follow domain policies, coordinate dependent tools, and realize the correct persistent state transition without collateral effects. In this paper, we introduce Thinkingbox, a sandbox for tool-agent-user interaction that provides isolated MCP-compatible tool sessions, complete execution traces, and outcome evaluation over terminal backend state. Built on this sandbox, Thinkingbox-bench contains 507 policy-conditioned workflows across numerous scenarios, including retail, hospitality, auto insurance, neobank internal IT, and consulting IT/HR support. Each attempt is evaluated by task-specific executable checks that accept valid trajectories while rejecting wrong, missing, or extra effects; designated tasks additionally check required properties of the final response. Across proprietary and open-weight models, the strongest achieves 65.36% pass@1, but only 25.25% pass^20. Moreover, many failed trials show clean termination and valid state-changing actions, showing that response or tool-call-level signals are not clear proxies for end-to-end task completion. Thinkingbox-bench reveals a large gap between occasionally finding a successful trajectory and reliably completing stateful business tasks. We release both Thinkingbox and Thinkingbox-Bench: https://github.com/microsoft/thinkingbox

</details>


### 48. Question-Guided Evidence Acquisition for Multimodal Visual Question Answering

- **Authors:** Alin-Ionut Popa
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19739v1](http://arxiv.org/abs/2608.19739v1)
- **PDF:** [https://arxiv.org/pdf/2608.19739v1](https://arxiv.org/pdf/2608.19739v1)
- **Categories:** cs.CV, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal LLMs can see a document, but they often can't read it reliably. Small text, tables, visual cues, and topological elements still trip them up under direct visual inference, even when the page is already sitting in the model's context. Most document-VQA systems treat perception as fixed: they encode the page once, ask the question, and answer from whatever the model happened to extract in that single fast pass. We think document VQA needs slower, more deliberate perception: rather than answering from one fixed encoding, the model should spend a bit of extra compute at inference time working out what to look at next, and only then answer. We build this into \textbf{Q-Guide}, a small agent that reads a question, works out what evidence it is still missing, and calls targeted tool(s) to recover it---reading text where text is needed, zooming in where detail is needed, or grounding a region where position matters. On DocVQA2026 and Manga109, Q-Guide outperforms both direct prompting and recent multi-agent document systems ($65.0\%$ vs.\ $40.0\%$ on DocVQA2026, $32.4\%$ vs.\ $24.4\%$ on Manga109), and the improvement holds across three Claude backbones (Opus 4.6, Sonnet 4.6, and Opus 4.5). We find that accuracy scales with the perception budget---most of the gain appears within two to three deliberate rounds---and that the gain comes from directing perception to the right place, not from complex control logic: adding planners, routers, or multiple collaborating agents does not help.

</details>


### 49. Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration

- **Authors:** Chenchen Lin, Wenhao Yuan, Xuehe Wang, Edith Cheuk Han Ngai
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19701v1](http://arxiv.org/abs/2608.19701v1)
- **PDF:** [https://arxiv.org/pdf/2608.19701v1](https://arxiv.org/pdf/2608.19701v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-term multi-agent systems continuously accumulate the memories produced by different agents. Existing memory methods typically treat retrieved memories as independent evidence and combine them through voting or weighting. However, this independence assumption often fails in multi-agent settings: memories written by different agents may inherit the same upstream source or shared bias, causing correlated evidence to be repeatedly counted and creating a false majority. We term this failure mode \textit{Memory Correlation Bias}. To address the issue, we propose the \textbf{C}orrelation-\textbf{A}ware \textbf{M}emory \textbf{A}rbitration (CAMA) framework that jointly decouples retrieved memories and recovers missing independent evidence. We model the retrieved memories as query-conditioned evidence groups and combine neural dependency inference with provenance-based symbolic priors to estimate the effective number of independent evidence sources, thereby preventing correlated memories from forming a false majority. Since critical independent evidence may be absent from the initial retrieval set, \textsc{CAMA} further learns a sequential recovery policy that actively retrieves alternative evidence or traces upstream sources before making the final decision, aiming to recover sufficient independent evidence for reliable arbitration while minimizing retrieval cost. Experiments on multiple benchmarks demonstrate the superiority of our method over the state-of-the-art baseline methods, suppressing false majorities induced by correlated memories.

</details>


### 50. An Evidence-Grounded Multi-Agent System for High-Level Bio-Robot Design

- **Authors:** Yujun Chen, Tianle Li, Jiayu Chen, Zhen Yin
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19699v1](http://arxiv.org/abs/2608.19699v1)
- **PDF:** [https://arxiv.org/pdf/2608.19699v1](https://arxiv.org/pdf/2608.19699v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

In this paper, a bio-robot is an engineered living or biohybrid system in which living cells perform one or more core functions, such as sensing, information processing, actuation or output. We focus on systems whose cell-based functions are programmed by genetic circuits; physical movement is optional. Designing such a system requires translating application requirements into sensing, logic or memory, output, assembly, host and containment modules, while grounding each choice in traceable parts and evidence. We present micro_biorobot_agent, an offline multi-agent system built on Qwen3.5-27B. The system combines requirement analysis, module-specific retrieval, candidate assembly, conflict checking, local repair, independent review and validation over an integrated library of 23,762 records covering biological parts, measured combinations, literature-supported relationships and actuation evidence. Deterministic output checks align the final report with the retrieved part set and correct false gaps, unsupported part mentions and source-tracking errors. On two author-developed evaluation sets of 50 queries each, the system obtains mean overall scores of 7.35 and 8.04, the highest among the seven evaluated systems; on Scenario Design it exceeds the runner-up by 2.23 points. A 50-query paired ablation shows that the source-tracking check reduces false-gap incidents from 15 to 3, an 80% reduction, and increases source accuracy by 0.75 points. This paper reports the Qwen3.5-based v1 system and evaluates high-level design reports rather than experimentally validated circuits.

</details>


### 51. An LLM agent for end-to-end computational materials discovery

- **Authors:** Chen Yuntong, Huang Ju, Liu Yu, Zhao Dan, Sun Mingqi, Ju Chentian, Liu Yanbing, Huang Lijiang, Zhao Guobin
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.20434v1](http://arxiv.org/abs/2608.20434v1)
- **PDF:** [https://arxiv.org/pdf/2608.20434v1](https://arxiv.org/pdf/2608.20434v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The coordination of multi-scale tasks is an effective strategy for computational materials discovery, yet the repeated application of diverse algorithms and tools renders it challenging. We report MAESTRO, a large language model (LLM) agent system capable of executing the entire screening pipeline for metal-organic frameworks (MOFs). It processes a large body of MOF literature, links relevant publications to their crystal structures, and curates the results into a computation-ready database, which is then screened through a strategy of progressively increasing computational cost. The promising candidates identified for separation under wet flue gas conditions all originate from unrelated studies. By connecting the heterogeneous stages of computational materials discovery, the LLM-based agents of MAESTRO can operate across application domains and uncover high-performance materials that conventional screening approaches would be unlikely to consider.

</details>


### 52. ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents

- **Authors:** Yichu Fang, Sitong Wei, Haozhe Hu, Xiaoyu Shen
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19662v1](http://arxiv.org/abs/2608.19662v1)
- **PDF:** [https://arxiv.org/pdf/2608.19662v1](https://arxiv.org/pdf/2608.19662v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic language models repeatedly encode tool and skill schemas that recur across requests in different combinations and orders, preventing standard prefix caching from reusing their key--value (KV) states. We introduce \textbf{ReCache}, a framework for independently caching resource representations while reducing their inference-time computational and memory overhead. Resource-wise attention removes cross-resource interactions and assigns resource-local positions, producing composition-invariant KV blocks. ReCache then restricts resource visibility to contribution-selected layer--KV-head-group routes and retains only invocation-critical fields through structural and semantic pruning. We evaluate ReCache on a benchmark assembled from seven public tool- and skill-use datasets, including resource-disjoint tests. Resource-wise attention matches dense invocation performance (82.3\% versus 82.4\% Inv-F1) while providing a 3.655$\times$ time-to-first-token speedup. The complete framework reduces allocated KV-tensor memory by 92.43\% and accelerates attention by 1.423$\times$. These results show that separating reusable schema encoding from selective resource access substantially reduces agentic inference costs with limited effectiveness loss. The code is available at https://github.com/EIT-NLP/ReCache.

</details>


### 53. DeltaML-Bench: Evaluating Machine Learning Agents on Real-World Research Repositories

- **Authors:** Josias Moukpe, Priyanka Aryal, Matthew Kenney
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19653v1](http://arxiv.org/abs/2608.19653v1)
- **PDF:** [https://arxiv.org/pdf/2608.19653v1](https://arxiv.org/pdf/2608.19653v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents for machine learning experimentation must navigate heterogeneous repositories, repair training pipelines, and evaluate candidate improvements under realistic compute constraints. Existing benchmarks only partially capture these conditions. We introduce DeltaML-Bench, a benchmark comprising 48 tasks sourced from research papers that require agents to improve published baselines within imperfect, open-source repositories. We evaluate GPT-5 and Claude Sonnet 4 with a standard Modular agent and a search-based ARG scaffolding. In the 4 x 6h allocation, ARG raises GPT-5's per-run success rate from 9.4% to 33.9%; in the 2 x 12h allocation, GPT-5 ARG reaches 49.0%. Modular configurations exhibit specification gaming rates as high as 47.9%, while no gaming is observed in the evaluated ARG configurations. These results indicate that scaffolding design and integrity checks are important considerations when deploying agents for autonomous ML experimentation.

</details>


### 54. Scientific Data Skills: Enabling Agent-Ready Scientific Data Services at Scale

- **Authors:** Xiaohan Huang, Qingqing Long, Xiaolei Du, Siyu Pu, Jiawen Xu, Haotian Chen, Chenyang Zhao, Jinbiao Liu, Xuezhi Wang, Hao Wang, Hengshu Zhu, Yuanchun Zhou
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19625v1](http://arxiv.org/abs/2608.19625v1)
- **PDF:** [https://arxiv.org/pdf/2608.19625v1](https://arxiv.org/pdf/2608.19625v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scientific data are increasingly used by AI agents, yet existing dataset representations provide limited support for autonomous discovery, interpretation, and invocation. This limitation stems from the fragmentation of scientific data across heterogeneous repositories and from dataset representations designed primarily for human use. To address this limitation, we introduce the Scientific Data Skill (SciDSK), an agent-ready representation that packages dataset-specific knowledge and operational guidance as a reusable agent skill. A SciDSK integrates dataset descriptions, scientific context, file organization, usage procedures, quality checks, and provenance information while retaining the underlying data in its original repository. We define a structured SciDSK specification and develop a systematic construction pipeline that grounds each SciDSK in authoritative dataset records and associated supporting materials. We further establish the Scientific Data Skill Bank, a unified platform that publishes SciDSK resources across six scientific disciplines and supports package access, persistent identification, and traceability to source datasets. We evaluate SciDSK through a retrieval benchmark for dataset discovery and controlled cases for dataset interpretation. The results show that SciDSK improves agent-driven dataset discovery and provides more precise and actionable support for dataset interpretation. These findings support the value of organizing dataset-specific knowledge in an agent-ready representation.

</details>


### 55. Mitigating Identity Essentialism in LLM Agents with Longitudinal Life Trajectories

- **Authors:** Hexi Wang, Yujia Zhou, Bangde Du, Weihang Su, Xinyuan Cao, Qingyi Pan, Qingyao Ai, Yueyue Wu, Min Zhang, Yiqun Liu
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19621v2](http://arxiv.org/abs/2608.19621v2)
- **PDF:** [https://arxiv.org/pdf/2608.19621v2](https://arxiv.org/pdf/2608.19621v2)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) offer a scalable approach to social simulation, but their credibility depends on how agents are constructed. Existing methods can partially reproduce population-level patterns, yet often fail to capture human-like diversity. Our analysis shows that static-profile agents exhibit stronger demographic separation and within-group compression than humans, a pattern consistent with identity essentialism: demographic labels can encourage models to treat group-average tendencies as individual traits, homogenizing responses within groups. We argue that this limitation arises from two related factors: sparse, static agent representations and the limited ability of prompt-only memory to persistently integrate experience. Inspired by complementary memory systems, we propose LifeMem, a longitudinal memory framework that combines structured life-event retrieval with agent-specific parametric memory for experience integration. Experiments on Add Health and Understanding Society with three LLMs show that LifeMem improves alignment with human data in terms of response distributions, overall and within-group diversity, and patterns of within-person response change across life stages. These findings highlight the value of longitudinal life-event memory for constructing more faithful and dynamically evolving social agents.

</details>


### 56. Remember, Verify, or Ask? Cross-Family Evaluation of Memory Commitment in LLM Agents

- **Authors:** Baichuan Li, Junyi Yao, Zihao Zheng
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19564v1](http://arxiv.org/abs/2608.19564v1)
- **PDF:** [https://arxiv.org/pdf/2608.19564v1](https://arxiv.org/pdf/2608.19564v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Persistent memory can personalize an LLM agent, but an incorrect durable update can silently distort future behavior. We study the memory-clarification boundary: whether interaction-derived information should be persisted, used only in the current context, re-verified, or clarified with the user. MCB contains 140 primary scenarios, split into 70 development and 70 held-out items, plus a separate 70-item contrast set. It evaluates both action labels and structured tool-call selection. Two non-authors independently label the 70 held-out primary and 70 contrast items (97.1% agreement, Cohen's kappa = 0.962); a blind third resolves four disagreements, replacing eight author labels by non-author majority. Across Claude and Qwen, models verify changing facts more reliably than they ask users to resolve ambiguity. Bare Qwen asks on 0/12 clarification items while verifying 12/18 freshness items. Few-shot prompting raises accuracy from 0.557 to 0.771 (paired delta = +0.214, Holm-adjusted exact McNemar p_H = 0.002), yet clarification recall remains 0.333. The policy prompt reduces erroneous persistence from 0.243 to 0.100 (p_H = 0.038), although its accuracy gain is not significant. Label-tool agreement is 57% for each Claude model and 23% for Qwen; Qwen accuracy falls from 0.557 to 0.343 (p_H = 0.047). Memory evaluation must test both stated decisions and tool-call choices.

</details>


### 57. When Do LLM Agents Help? Deadline-Aware Mixed-Criticality Task Scheduling at the Autonomous-Vehicle Edge

- **Authors:** Reza Zakerian
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19557v1](http://arxiv.org/abs/2608.19557v1)
- **PDF:** [https://arxiv.org/pdf/2608.19557v1](https://arxiv.org/pdf/2608.19557v1)
- **Categories:** cs.DC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous vehicles offload latency-sensitive perception tasks to nearby mobile edge computing (MEC) servers, where a missed safety-critical task is unsafe rather than merely degraded. Large language models (LLMs) are increasingly proposed as adaptive, explainable schedulers, yet evidence of when they help is scarce. We study deadline-aware, mixed-criticality scheduling on heterogeneous MEC servers, where time-critical (TC) tasks must be protected at a controlled cost to best-effort traffic, and ask whether a multi-agent LLM control layer improves on a strong heuristic. We answer in two steps. First we build the heuristic: a windowed contract-net auction that orders each admission window time-critical-first by earliest deadline and places tasks by earliest-finish-time. Across 60 instances on three topologies and 15 baselines under an identical online constraint, it attains a TC completion rate of 0.902, above every baseline (Holm-corrected p < 0.001; best baseline 0.838) and at 0.87 of a CP-SAT upper bound. Second, we add the LLM control plane. A controlled decomposition traces the scheduler's advantage to two ordinary factors, the batching horizon and time-critical-first ordering; the auction, the per-window LLM policy, and online adaptation add nothing while the load is stationary, where the heuristic is already near-optimal. Under a mid-run surge of safety-critical tasks the picture changes, and the LLM control plane gains significantly over both the static heuristic and the bandit. LLM orchestration therefore earns its cost only when non-stationarity opens headroom a fixed policy cannot use. We report control-plane latency and rationale, and release all code and seeded instances.

</details>


### 58. Symposium: Trust via Auditable Records for Communities of AI Scientist Agents

- **Authors:** Dexter Pratt
- **Published:** 2026-08-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19511v1](http://arxiv.org/abs/2608.19511v1)
- **PDF:** [https://arxiv.org/pdf/2608.19511v1](https://arxiv.org/pdf/2608.19511v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Symposium is a formal framework and practical implementation to record the operation of AI agents deployed by small scientific research communities. Symposium provides long-term, immutable histories of agent-driven research activity, leaving auditable trails of analyses, hypotheses, data, and scientific discourse. This shared record of published artifacts enables agents to build on prior work and preserves the evidence researchers and agents need to make purpose-dependent trust assessments. Symposium captures scientific argument, including structured claims, fine-grained evidence citations, assumptions, and explicit declarations of what material may and may not be used as evidence. Symposium differs from AI co-scientist agents or integrated AI research environments; it is a framework that separates a scientific community's durable history from the agents and other systems that operate on that history. It assumes that a community will use diverse AI systems in a rapidly evolving environment. A working implementation of the publication infrastructure, agent prompt components, and documentation are provided to enable users to rapidly set up and run their own Symposium community.

</details>


### 59. Accelerated Genetic Programming Hyper-Heuristics for Simulation-Based Scheduling via Agentic AI

- **Authors:** Heyang Thomas Li, Alexander Pletzer, Yuan Tian, Yi Mei, Mengjie Zhang
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19487v1](http://arxiv.org/abs/2608.19487v1)
- **PDF:** [https://arxiv.org/pdf/2608.19487v1](https://arxiv.org/pdf/2608.19487v1)
- **Categories:** cs.SE, cs.AI, cs.NE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Python is widely used in scientific research because it enables rapid development and provides rich ecosystems for data analysis, artificial intelligence (AI), and machine learning. However, customized research code can become prohibitively slow as experiments scale. This challenge is particularly acute in discrete-event project-scheduling simulations, where sequential state updates, nested loops, conditional evaluations, and object-oriented structures limit the benefits of compiled numerical and GPU-accelerated libraries. Addressing these bottlenecks typically requires iterative profiling, refactoring, testing, and validation, yet researchers may lack the time or specialized software-engineering expertise for low-level optimization. This paper presents a systematic refactoring approach using Claude agentic AI on real-world project-scheduling workloads in a high-performance computing (HPC) environment. Guided by representative benchmarks and correctness checks, the agent identifies bottlenecks, implements targeted optimizations, and evaluates their effects, while the researcher retains final control. Testing runtime reduced from 1,298 seconds to under 200 seconds without changing outputs, saving four million core-hours (NZ\$320,000) annually.

</details>


### 60. SPADE: Self-Play in Adaptive Synthetic Executable Environments

- **Authors:** Bo Liu, Simon Yu, Yiding Jiang, Ao Qu, Andrew Zhao, Zichen Liu, Junsu Kim, Zijian Zhou, Seungone Kim, Tongzheng Ren, Mickel Liu, Hanfei Yu, Zhaorun Chen, Weiyan Shi, Paul Pu Liang, Luke Zettlemoyer, Yejin Choi, Natasha Jaques
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19197v1](http://arxiv.org/abs/2608.19197v1)
- **PDF:** [https://arxiv.org/pdf/2608.19197v1](https://arxiv.org/pdf/2608.19197v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Continuous self-improvement requires an ever-expanding pool of self-generated, diverse, adaptive goals. For language agents, existing training environment pools (hand-curated, statically synthesized, or frozen-verifier) keep the goal distribution fixed as the learner scales. We introduce SPADE (Self-Play in Adaptive Synthetic Executable Environments), a self-play RL framework in which a single LLM plays two roles: an Environment Designer that writes complete, long-horizon training environments as executable code with an OpenAI Gym-style reset()/step() interface, and a Reasoning Agent that learns to act in them. Each is a stateful, multi-turn environment (state transitions, reward functions, and verification code), so one interface spans reasoning problems and multi-step agentic tool use. The Reasoning Agent's regret is estimated using the gap between its reward with and without privileged hints; in optimizing this regret signal the Environment Designer learns to target environments at the edge of the agent's capabilities while keeping them feasible. Through extensive experimentation, we find several components critical to success: grounding the Environment Designer on documents sampled from a large pretraining corpus, and giving it an accumulated environment memory. Scaling to 30B-parameter models, SPADE improves over the strongest fixed-environment baseline by +5.3 on average across eight held-out math, science, code, and reasoning benchmarks, and lifts the tool-use setting by +5.7 on BFCL-v4 multi-turn and +13.9 on ACEBench-Agent; on the games setting, the margin over the strongest baseline grows with model scale. By making environment design itself a learnable component, SPADE takes a concrete step toward open-ended self-improvement.

</details>


### 61. Beyond the Transcript: Detecting Covert Co ordination in Latent Multi-Agent Communication

- **Authors:** Ramneet Kaur, Pradyumna Chari, Ramesh Raskar, Jugad Singh, Sumit Kumar Jha, Anirban Roy
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19161v1](http://arxiv.org/abs/2608.19161v1)
- **PDF:** [https://arxiv.org/pdf/2608.19161v1](https://arxiv.org/pdf/2608.19161v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language-model agents can communicate through continuous hidden states that are invisible in public transcripts, creating opportunities for covert harmful coordination. We introduce Verifiable Latent Alignments (VLA), an activation-aware framework for monitoring and steering these private communication channels. For every monitored decision, VLA links the private latent-state record and channel status to the resulting public action using a shared event identifier, enabling matched causal analysis. Our first contribution is a neutral-only three-layer monitor combining representation anomaly detection, counterfactual action-distribution influence, and sparse-autoencoder interpretation support. Our second contribution is a steerability framework spanning black-box behavioral instructions and white-box matched-neutral counterfactuals. Our third contribution is an evaluation on a controlled multi-agent auction benchmark covering homogeneous and heterogeneous model pairs, many-agent scalability, and intervention effectiveness. The sequential monitor achieves mean area under the receiver operating characteristic curve (AUROC) of 0.993 for homogeneous agents and 0.854 for heterogeneous pairs when text- and latent-collusion rows are pooled as positives. In Qwen3-0.6B auctions with 25-100 bidders, monitoring requires only a small normalized load relative to all possible directed pairs, while full white-box steering achieves 100% bid-distribution recovery and reduces collusive low-bid behavior by 47.3 percentage points. Because full white-box steering replays the matched neutral counterfactual, its exact recovery is a sanity check by construction. Overall, the controlled study shows that the evaluated private channel attacks can be monitored without training the primary monitor on attack examples and mitigated when matched counterfactual access is available.

</details>


### 62. Autonomous Cyber Defense in Connected Vehicles: A Multi-Agent Approach to V2X Security

- **Authors:** Krishna Teja Medam
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19135v1](http://arxiv.org/abs/2608.19135v1)
- **PDF:** [https://arxiv.org/pdf/2608.19135v1](https://arxiv.org/pdf/2608.19135v1)
- **Categories:** cs.CR, cs.DC, cs.MA, cs.NI


> Summary unavailable.


<details>
<summary>Abstract</summary>

A connected vehicle has roughly 100 milliseconds to decide whether an incoming Basic Safety Message is real or fabricated. If a false emergency braking alert reaches the planning pipeline in time, the car brakes - a safety failure triggered by a security failure. Existing intrusion detection systems are not designed to handle that coupling. They operate per vehicle, per message, with static rules - blind to attack patterns that only emerge across a fleet or over time, and blind to the fundamental tension between dropping a suspicious message and dropping a real emergency alert. We propose a three-tier multi-agent architecture that treats this timing constraint as a hard design requirement, not a performance target. At the vehicle level, an onboard agent classifies each incoming V2X message into one of four actions - Accept, Drop, Quarantine, or Escalate - within a 10-millisecond budget, deliberately biased toward Escalate when uncertain, passing ambiguous cases to the roadside edge agent rather than risking a dropped legitimate alert. The edge agent operates across a roadside unit zone with a 50-millisecond budget, fusing threat assessments from multiple vehicles and resolving safety-security conflicts using complementary sensor observations. The cloud tier refines detection models through Byzantine fault-tolerant federated learning and redistributes updated weights to the fleet. Every timing constraint derives directly from the 100-millisecond Basic Safety Message cycles mandated by SAE J2735 and ETSI EN 302 637-2. No existing framework simultaneously assigns standards-grounded latency budgets to all three deployment tiers while treating safety-security conflict resolution as a first-class design constraint. Remaining open problems - adversarial poisoning at the edge and the absence of regulatory frameworks for autonomous security response - are discussed as future work.

</details>


### 63. Multi-Agent Off-Policy Deep Reinforcement Learning for Smart Campus Coverage

- **Authors:** Omar Rady, Mohamed Ayman, Ali Arafa, Mohamed Shalma
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19049v1](http://arxiv.org/abs/2608.19049v1)
- **PDF:** [https://arxiv.org/pdf/2608.19049v1](https://arxiv.org/pdf/2608.19049v1)
- **Categories:** cs.LG, eess.SP


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep reinforcement learning (DRL) has recently gained a great attention due to its real-time adaptation and effectiveness in complex optimization problems. This paper investigates the optimal deployment of millimeter-wave (mmWave) base stations (BSs) in a realistic, non-convex campus topology. The optimization problem is NP-hard, due to the non-convex, non-smooth nature of the max-min fairness objective. To overcome these constraints, we formulate the BS placement as a Markov Decision Process (MDP) and systematically benchmark four DRL schemes: a discrete single-agent Deep Q-Network (DQN), a spatially partitioned Multi-Agent DQN, a continuous single-agent Deep Deterministic Policy Gradient (DDPG), and a geographically partitioned multi-agent DDPG framework. Numerical evaluations reveal that the multi-agent DDPG approach substantially outperforms single-agent in dense scenarios. Additionally full coverage is achieved, and a fairness Jain's index of 0.94 is obtained. Finally, the multi-agent demonstrates highly efficient computational convergence of dense scenarios with $400$ users.

</details>


### 64. Eureka: Task-Conditioned Meta-Agent Orchestration for Scientific Discovery

- **Authors:** Alizer Wong, Heng Cui, Yi Tan, Xiongchao Zhan, Liang Lin, Yuxiang Guo, Zhaorong Dai, Zixin Zeng, Wenyuan Li
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19047v1](http://arxiv.org/abs/2608.19047v1)
- **PDF:** [https://arxiv.org/pdf/2608.19047v1](https://arxiv.org/pdf/2608.19047v1)
- **Categories:** cs.AI, math.NT


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present Eureka, a task-conditioned Meta-Agent architecture that compiles long-horizon tasks into dynamic obligation graphs with explicit acceptance semantics. During execution, Eureka forms Macro-Agents with specialized state, memory, operators, tools, verifiers, and local topology via receding-horizon planning, architecture promotion, and minimal-sufficient compilation. When bottlenecks recur, cost-benefit-gated evolution updates the local architecture under constraints. Theoretically, we establish results on regret, planning invalidation, amortization, subtree interfaces, serializability, and verification. Experimentally, Eureka completes 170/170 recursive tasks and generates 3,948 certificates with no false acceptances. Active context compresses median input from 9,490 to 4,005 tokens; incremental processing avoids 65.38% recomputation across 12,000 tasks; 16,000 concurrent executions serialize consistently. The same Meta-Agent instantiates a Theory-Discovery Agent and a Math/Conjecture Agent. The former yields structural results in quantum-process and spacetime theory. The latter identifies bottlenecks in Riemann Hypothesis research and advances a positivity certificate for Suzuki's localized Weil quadratic form to 0 < a <= 69/200 = 0.345, reaching ~99.55% of (log 2)/2. These results suggest that scientific-agent capability depends not only on the base model but on whether an architecture can be formed to match the task's cognitive structure.

</details>


### 65. Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering

- **Authors:** Pradeep Murugesan, Luoxiao Yang, Xueli Chen, Xinqi Fan
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19029v1](http://arxiv.org/abs/2608.19029v1)
- **PDF:** [https://arxiv.org/pdf/2608.19029v1](https://arxiv.org/pdf/2608.19029v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Accurate and responsible medical question answering (QA) is important in healthcare, where complex cases require factual knowledge and nuanced reasoning. Existing medical QA systems, typically based on single-agent architectures and static retrieval, often lack adaptability, persistent memory, and structured decision-making. This work introduces an adaptive memory and reflection (AMR) agentic system, a multi-agent framework in which specialized agents use dedicated memory and reflection-based feedback to retrieve relevant prior cases and improve subsequent reasoning. Complexity assessment routes questions through solo, collaborative, or escalated workflows, while consensus and ethical overseer modules support reasoning consolidation and output review. Evaluation on MedQA and MedMCQA demonstrates strong performance compared with several baselines. Ablation studies show that combining agent-specific memory, reflection, and external retrieval yields the strongest performance. These findings highlight the potential of structured memory and feedback for developing more trustworthy medical agents. The source code is publicly available at https://github.com/mm-air/AMR-Agent.

</details>


### 66. A Theory of Post-hoc Debate Judgement

- **Authors:** Xiang Yin, Adam Dejl, Antonio Rago, Lihu Chen, Francesca Toni
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19002v1](http://arxiv.org/abs/2608.19002v1)
- **PDF:** [https://arxiv.org/pdf/2608.19002v1](https://arxiv.org/pdf/2608.19002v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Debates have recently emerged as a useful methodology for agentic AI to improve performance as well as to aid explainability and user engagement. For example, LLM-empowered agents may debate internally (with themselves) and/or externally (with other agents). In many settings where debates are used, debates' outcomes and resulting outputs are determined post-hoc by external judges, often LLMs. In this paper we develop and test a novel theory of debate judgement applicable to all settings where agents engage in debates by providing pros and cons for their opinions therein. Specifically, we identify a number of formal properties that debate judgement may be required to satisfy in general, as concerns reproducibility, robustness, groundedness and explainability. Then, we explore their satisfaction formally and/or experimentally, for claim verification settings, for two specific alternative debate judgement methods: variants of the LLMs as a judge idea and formal semantics drawn from computational argumentation. We show that the two methods give similar accuracy performances but the former may lack formal guarantees that the latter brings. Overall, our study indicates argumentation semantics as an ideal candidate for principled judges in debate-driven AI.

</details>


### 67. Training-Free Inference-Time Self-Reflection and Cost-Bounded Early Stopping for Large Language Models

- **Authors:** Wei Yu, Suxing Liu, Minjie Yu, Jiahao Wang, Zhijian Zheng, Haocheng Deng, Bing Li
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18884v1](http://arxiv.org/abs/2608.18884v1)
- **PDF:** [https://arxiv.org/pdf/2608.18884v1](https://arxiv.org/pdf/2608.18884v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement-learning training of reasoning LLMs (e.g., GRPO) is expensive and requires a controllable environment, committing every contribution to a full training pipeline. We present EvoResearcher, a training-free, inference-time protocol that adds cost-bounded self-reflection to a single frozen LLM backbone. The protocol iterates generate -> self-critique -> revise until a maximum depth D is reached or the critique returns the CONFIRMED sentinel, an implicit early stop that lets the backbone self-verify its answer under a strict compute budget. Four self-reflective meta-reward components (correctness, efficiency, reflection depth, tool-call diversity) act as design principles instantiated as prompt-level mechanisms, so their benefits accrue with zero gradient updates. We validate the protocol on Big-Bench Hard (100 questions) and establish cross-domain behavior on GSM8K (500) and MATH (500) on the same frozen backbone, with cross-model replication on Qwen2.5-72B. All experiments use pure-reasoning benchmarks; the tool-call diversity component is validated in prompt-level form, and the environment-level and multi-agent extensions are design blueprints left to future work. On clean BBH the protocol does not raise accuracy beyond the 95% Wilson interval; its value is cost-bounded self-verification, with the CONFIRMED early stop terminating 82-88% of items at equal accuracy (about 2.1 generations per question).

</details>


### 68. DentAgent: Evidence-Centric Multi-Agent Coordination for Multimodal Dental Reasoning

- **Authors:** Zijie Meng, Xiwei Dai, Yixuan Tang, Jin Hao, Yang Feng, Fudong Zhu, Xiaoqiang Liu, Shaosheng Cao, Zuozhu Liu
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18878v1](http://arxiv.org/abs/2608.18878v1)
- **PDF:** [https://arxiv.org/pdf/2608.18878v1](https://arxiv.org/pdf/2608.18878v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Oral diseases affect billions of people worldwide, underscoring a pressing need for accurate and reliable dental assessment that integrates heterogeneous evidence from domain knowledge, radiographs, intraoral photographs, and 3D dental data. Most existing dental AI systems remain modality- or task-specific. Although recent vision-language models support flexible dental question answering, directly generated response leaves evidence implicit and untraceable. To address these limitations, we introduce DentAgent, an evidence-centric multi-agent framework, in which the Orchestrator coordinate five specialized agents spanning various modalities. Each specialist utilizes domain tools to convert observations into structured evidence records. The Evidence Blackboard manages these records as a shared evidence state, tracking coverage, gaps, and conflicts before response generation. This standardized evidence representation integrates isolated dental capabilities into a unified agentic workflow. Across four benchmarks, DentAgent demonstrates leading performance, even surpassing the senior specialists by 17.3 percentage points on multi-label diagnosis, which supports its value for broadly applicable and traceable multimodal dental reasoning, and highlights its potential as a technical foundation for population oral health assessment and management.

</details>


### 69. SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents

- **Authors:** Qingyao Li, Wenxiang Jiao, Shuai Shao, Kangning Zhang, Yuan Lu, Yi Guo, Weiwen Liu, Weinan Zhang, Yong Yu
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18852v1](http://arxiv.org/abs/2608.18852v1)
- **PDF:** [https://arxiv.org/pdf/2608.18852v1](https://arxiv.org/pdf/2608.18852v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent frameworks increasingly package procedural knowledge as skills: instruction files an agent reads on demand, while public libraries now hold thousands of them. Which skill to read has thus become a decision the policy itself makes in the middle of an episode, yet no existing signal trains it. We show that the default remedy, outcome-rewarded RL over the candidate slate, cannot teach it, for a structural reason we identify and name selector credit starvation: under a broadcast, sequence-level advantage, the few tokens that name the chosen skill carry a vanishing share of the loss, and the credit they inherit is increasingly wrong-signed as trajectories lengthen. A correct choice is punished whenever the execution after it fails, even though the choice itself is among the most valuable decisions in the trajectory. Auditing a completed run's own training artifacts confirms all three properties, each worsening monotonically with horizon. SkillGate removes the failure by construction: it partitions the token support into two disjoint credit channels, outcome credit reaching only execution tokens, and a separate action-local advantage reaching exactly the skill-naming tokens, positive only when a trajectory's single read is the correct one. On five agentic benchmarks under a 16-candidate slate, SkillGate lifts a 9B policy from 40.8% to 53.2% trial success, well ahead of the identical budget spent on outcome reward alone, while cutting exposure to misleading candidates by two thirds and reading fewer skills.

</details>


### 70. A Multi-Agent Platform for Automated Enterprise Analytics and Insight Generation

- **Authors:** Manoj N M, Vijayakrishna S, Manjunath Srinivas, Rohit Pahan
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18740v1](http://arxiv.org/abs/2608.18740v1)
- **PDF:** [https://arxiv.org/pdf/2608.18740v1](https://arxiv.org/pdf/2608.18740v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper proposes a multi-agent framework built on CrewAI [1] for conversational business intelligence. Five specialized AI agents operate in a sequential pipeline to process natural language queries, retrieve and analyze data, generate visualizations via the Model Context Protocol (MCP) [2], and deliver actionable insights. The platform features a defense-in-depth security architecture for multi-tenant data isolation and a query parameterization mechanism for transforming conversational insights into reusable dashboard components. Evaluation across 300 end-to-end test cases spanning synthetic and production enterprise datasets demonstrates 95.3% functional accuracy, a mean response latency of 24 seconds, and a response quality score of 4.52/5.0 as assessed by an LLM-as-a-Judge framework, with a 93.0% hallucination-free rate, representing a 22.6 percentage point accuracy improvement and 20.2% quality gain over a single-agent baseline. Cross-model evaluation across four LLM backends and human expert validation confirm architectural generalizability and evaluator reliability. An ablation study confirms that the Data Analysis and Report Aggregation agents are the primary drivers of output quality.

</details>


### 71. Sanyu Studio: A Multi-Agent System for Art-Historical Narrative Construction

- **Authors:** Zhaoxi Wei, Hongye Yang, Shuyuan Tian
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18677v1](http://arxiv.org/abs/2608.18677v1)
- **PDF:** [https://arxiv.org/pdf/2608.18677v1](https://arxiv.org/pdf/2608.18677v1)
- **Categories:** cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Amid concerns that generative AI may standardize art interpretation, this paper examines whether LLM-based interaction can support plural art-historical narrative construction. We present Sanyu Studio, a multi-agent dialogue system that models 321 Sanyu oil paintings as agents with fact, interpretation, organization, and memory-filtering mechanisms. Based on a seven-day workshop with eight art-university participants, the study shows that user prompts, evidence organization, and cognitive tendencies shaped divergent yet coherent versions of digital Sanyu. The findings suggest that, under conditions of limited historical evidence, AI can amplify human agency and offer public audiences an interactive entry point into art-historical interpretation.

</details>


### 72. CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence

- **Authors:** Yutong Cheng, Changze Li, Qian Cui, Wei Ding, Lingzhi Wang, Yan Chen, Peng Gao
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18613v1](http://arxiv.org/abs/2608.18613v1)
- **PDF:** [https://arxiv.org/pdf/2608.18613v1](https://arxiv.org/pdf/2608.18613v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cyber threat intelligence (CTI) is increasingly consumed not by human analysts but by LLM agents that compose multi-step investigations at query time. The harness side of this shift has matured rapidly (planning loops, tool protocols, context management), but the corpus side has not: threat reports and vulnerability databases are still packaged for retrieval-augmented generation, as opaque chunks behind an embedding index. We argue that this substrate, not model capability, is the bottleneck on agentic CTI investigation, and present CTIFoundry, an agent-native corpus scaffold. At build time, CTIFoundry materializes the latent structure of a CTI corpus: a deterministic ontology graph over four authoritative knowledge bases (CVE, CWE, CAPEC, ATT&CK) whose official cross-references become typed, traversable edges; a span-grounded report layer whose canonical, alias-resolved cross-vendor entities index provenance-carrying chunks; and hybrid dense+lexical retrieval surfaces. At query time this structure is exposed through seven typed tools and three procedural skills mounted on a stock open-source agent harness. On the public CTIConnect benchmark, swapping only the action surface lifts the identically-harnessed agent by +0.19 to +0.28 overall F1 across a four-model, two-provider panel: a small model on CTIFoundry surpasses a flagship on the flat substrate, and the gain is not bought with search effort, since on both Claude models the scaffolded agent is more accurate at roughly half the tool calls. An ablation attributes it: typed structure carries the larger share, procedural skills convert structure into discipline, and the two compose super-additively, because skills bind only to structure that exists.

</details>


### 73. Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution

- **Authors:** Ting-Wei Li, Yuanchen Bei, Xiao Lin, Hanghang Tong
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18575v1](http://arxiv.org/abs/2608.18575v1)
- **PDF:** [https://arxiv.org/pdf/2608.18575v1](https://arxiv.org/pdf/2608.18575v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based multi-agent systems (MAS) often exhibit complex failure modes, which frequently cause agents to produce incorrect outcomes. This motivates the task of Agent Failure Attribution: given a failed multi-agent trajectory, identify the faulty agents and their corresponding error types. Existing approaches predominantly rely on LLMs to perform failure attribution, either through direct prompting, fine-tuning on synthetic data or complex agentic pipelines. While effective, these methods incur substantial computational overhead due to long-context processing, expensive post-training and handcrafted workflows. Moreover, empirical evidence shows that even state-of-the-art models achieve limited accuracy on existing benchmarks, suggesting that scaling model size alone is insufficient. In this work, we revisit this task and question the necessity of such expensive generative solutions. We introduce AFANet, a lightweight graph-based framework that models interaction trajectories through step-level semantic signals and agent-level relationships. We show that with significantly fewer parameters and near-zero inference cost, AFANet (i) matches or outperforms LLM-based baselines, including fine-tuned models on in-domain benchmarks, (ii) maintains robust performance across different GNN architectures and (iii) can be further improved with inexpensive test-time adaptation on the OOD benchmark. Our results suggest that effective agent failure attribution does not require heavy LLM reasoning and a lightweight, structured approach can achieve strong performance.

</details>


### 74. CentaurBench: Benchmarking LLM Capabilities on Augmenting vs. Automating Real-World Work Tasks

- **Authors:** Pattaraphon Kenny Wongchamcharoen, Kris Gulati, Min Min Fong, Abhishek Nagaraj
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18554v1](http://arxiv.org/abs/2608.18554v1)
- **PDF:** [https://arxiv.org/pdf/2608.18554v1](https://arxiv.org/pdf/2608.18554v1)
- **Categories:** cs.CY, cs.AI, cs.MA, econ.GN


> Summary unavailable.


<details>
<summary>Abstract</summary>

Most LLM benchmarks rank models on their ability to automate work tasks. In practice, however, models are often used to assist other (human or LLM) agents. The question that drives model selection is therefore not only which model produces the best output, but which model most improves the work of another (weaker) agent. We introduce a unified framework that evaluates the capability of models to automate and augment another agent's performance. Across seven economically grounded real-world tasks, an assistant model writes assistance text for a standardized lower-capacity worker model, which produces the deliverable. In automation mode, the assistant produces the output directly. Outputs are scored through blind pairwise comparisons by an LLM judge panel with task-specific rubrics, replicated across ten runs. Rankings across the two regimes are only modestly correlated, and the automation winner loses augmentation on five of seven tasks. Assistance is not reliably positive. The unaided worker outranks every assisted condition on three tasks, and only one model's guidance beats no guidance on average. These results suggest that automation ability is an incomplete proxy for assistance quality, motivating benchmarks that evaluate models according to the roles they play in human-AI and multi-agent systems.

</details>


### 75. Bridging Search and CRM: Productionizing AI Product Research Agents for Customer Re-Engagement

- **Authors:** Mandar Kulkarni, Pooja A., Samir Shah
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18543v1](http://arxiv.org/abs/2608.18543v1)
- **PDF:** [https://arxiv.org/pdf/2608.18543v1](https://arxiv.org/pdf/2608.18543v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern e-commerce platforms often operate search, recommendation, personalization, and CRM systems independently, limiting opportunities for proactive customer re-engagement. This is particularly challenging for exploratory intents such as best smartphones or latest 5G phones, where users may leave the platform for external research before purchasing. We present a scalable, production-deployed framework that bridges search and CRM workflows through AI-powered Product Research Agents. The system identifies users with exploratory purchase intent and low engagement, conducts grounded multi-agent product research using behavioral signals, external knowledge, and enterprise catalog data, and delivers personalized recommendations through WhatsApp. We evaluate the framework in a 23-day production deployment involving approximately 15K WhatsApp notifications for mobile product discovery. The campaign achieved substantial CTR improvements over traditional WhatsApp recommendation campaigns, with evidence of secondary engagement through message forwarding and sharing. The deployment also generated downstream purchases and GMV impact, demonstrating the practical effectiveness of AI Product Research Agents for proactive customer re-engagement and end-to-end customer journey optimization.

</details>


### 76. DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Multi-Turn Tool-Calling Agents

- **Authors:** Hangrui Xu, Jiarui Wang, Yang Yang, Chuanbo Zhu, Fangda Chen, Ziqi Wu, Jingming Cai, Yan Song
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18524v1](http://arxiv.org/abs/2608.18524v1)
- **PDF:** [https://arxiv.org/pdf/2608.18524v1](https://arxiv.org/pdf/2608.18524v1)
- **Categories:** cs.CL, cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Equipping Large Language Models (LLMs) with multi-turn tool-calling capabilities is essential for building autonomous agents. However, progress is fundamentally limited by the reliance on full-length trajectory imitation. For tasks involving multiple order-independent sub-goals, the optimal solution space forms a vast combinatorial diamond lattice. Forcing this rich topology into monolithic trajectories causes a severe topological collapse, indiscriminately penalizing valid alternative explorations and severely degrading policy diversity. To address this, we propose DART-SD (Diamond-topology Aware Retrieval and Tuning for Self-Distillation), a novel framework that shifts the paradigm from global forcing to topology-guided localized correction. DART-SD first models the execution process as a converging Interaction-State Transition Graph (ISTG), faithfully capturing the inherent diamond topology of successful and failed exploratory paths. During autonomous rollouts, the framework identifies the Critical Topological Breakpoint (CTB) and retrieves success-supported recovery references. Finally, we introduce a progressive self-distillation paradigm through CTB-guided localized supervision, ensuring that the training loss is calculated exclusively on the generated recovery steps while strictly protecting the valid reasoning prefix from destructive gradient updates. Experiments on complex multi-turn tool-calling benchmarks demonstrate that DART-SD significantly outperforms traditional full-trajectory baselines.

</details>


### 77. Science Done on a Machine by a Machine: AI Agents in Computational Chemistry

- **Authors:** Pavlo O. Dral, Hassan Nawaz, Arif Ullah
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18508v1](http://arxiv.org/abs/2608.18508v1)
- **PDF:** [https://arxiv.org/pdf/2608.18508v1](https://arxiv.org/pdf/2608.18508v1)
- **Categories:** physics.chem-ph, cs.AI, physics.comp-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

We are witnessing an explosion of agentic systems for computational chemistry simulations: from half a dozen in 2024 to a dozen in 2025, and the current number approaches fifty, surveyed in this Perspective as of 8 August 2026. The capabilities of these agentic systems are shifting from assisting in performing a selection of computational tasks to autonomous design and execution of \textit{in silico} experiments, their analysis, and even manuscript writing. The ultimate destination is a fully autonomous AI scientist, where the entirety of computational chemistry is performed on a machine by a machine, without human supervision. While we are not there yet, and all reported systems currently involve a human in the loop, the trend is unmistakable. Even building specialized agentic systems for computational chemistry is increasingly commoditized by generalist agents, which may in the end replace the need for the specialized ones altogether, since adding a new capability will be as easy as asking AI to do it for you. Both the explosion in their number and the very limited adoption beyond their own developers point that way, and we close this Perspective on what it leaves us to do. The speed and scale of disruption agentic systems are bringing to computational chemistry leave many of us dumbfounded about the field's future and what we should spend our efforts on, as already established specialists, teachers, and students, and we have no answer.

</details>


### 78. Bayesian Partner Modelling enables Adaptive Replanning for LLM Coordination

- **Authors:** Harsh Goel, Aditya Sai Ellendula, Vaishnav Tadiparthi, Ehsan Moradi Pari, Hossein Nourkhiz Mahjoub, Sandeep P. Chinchali
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18490v1](http://arxiv.org/abs/2608.18490v1)
- **PDF:** [https://arxiv.org/pdf/2608.18490v1](https://arxiv.org/pdf/2608.18490v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent Large Language Model (LLM) systems often struggle to collaborate with new teammates whose strategies shift mid-task. Because agents execute multi-step or temporally extended skills, they frequently continue executing outdated plans long after public evidence shows that a partner has changed its skill. Existing methods either treat partner tracking as passive context-leaving the agent aware of the shift but slow to act-or replan indiscriminately. We introduce BayesBeliefAgent, which pairs a hierarchical LLM planner with a Bayesian tracking module. Rather than replanning constantly, our agent interrupts its current skill only when a partner's actions directly contradict the inferred skill. Beyond standard reward, we evaluate performance using replanning efficiency and the belief-action gap: the fraction of total decisions where an agent with a correct partner estimate executes a non-complementary skill. Across benchmark Overcooked environments, contradiction-conditioned control drastically narrows this belief-action gap while requiring an order of magnitude fewer replans than heuristic methods

</details>


### 79. A Locally Deployable Tool-Grounded LLM Multi-agent Framework for Automating Methane Emission Analysis and Reporting

- **Authors:** Yang Yan, Zifan Zhou, Xuan Wang, Erum Hassan, Bilguunzaya Mijiddorj, Jie Cao, Bin Li, Binbin Weng
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18473v1](http://arxiv.org/abs/2608.18473v1)
- **PDF:** [https://arxiv.org/pdf/2608.18473v1](https://arxiv.org/pdf/2608.18473v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Methane field monitoring requires the integration of sampling design, meteorological interpretation, sensor processing, plume analysis, visualization, and reporting, but these steps are often distributed across separate expert-driven workflows. We developed a locally deployable, tool-grounded large language model (LLM) multi-agent framework for our low-cost methane sensing and field-monitoring campaigns. The framework uses LLM agents as workflow coordinators that link field measurements, meteorological data, deterministic sensor-processing routines, Gaussian plume inversion, and report generation, rather than directly estimating methane concentrations or emissions. Extensive field deployments across diverse real-world environments (e.g., wastewater treatment facilities, landfills, and oil and gas sites) demonstrate that our framework can achieve 92.0\% accuracy in workflow routing and parameter extraction, 85.0\% success in emission-rate estimation and plume prediction, and 95.0\% success in generating editable reports under practical operating conditions. Compared with manual and general-purpose LLM-assisted workflows, it reduced workflow time from hours-level to minutes-level, lowered manual coordination and prompt-engineering requirements, and retained traceable plume-based outputs. In addition, most processing can be performed locally, reducing exposure of sensitive facility and field data to cloud services. These results indicate that tool-grounded LLM coordination can reduce the time, labor, usability, and data-security barriers of methane field monitoring.

</details>


### 80. Adaptive Multi-Agent Feature Selection for Personalized Fall Risk Prevention

- **Authors:** Chang Liu, Ladda Thiamwong, Yanjie Fu, Rui Xie
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18450v1](http://arxiv.org/abs/2608.18450v1)
- **PDF:** [https://arxiv.org/pdf/2608.18450v1](https://arxiv.org/pdf/2608.18450v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Falls among older adults represent a major public health challenge driven by complex, time-varying interactions across multiple risk domains. Effective fall risk factor identification requires learning from heterogeneous longitudinal data while accounting for sparse and delayed fall-related outcome events. However, existing approaches are largely static and fail to adaptively model evolving, individualized risk factors across modalities and time. We propose PAFIR, a Personalized and Adaptive Feature selection framework for fall risk Identification and pRevention, which formulates adaptive feature selection as a reinforcement learning problem over longitudinal multimodal health data. PAFIR jointly models structural dependencies among correlated assessment variables and temporal dynamics in wearable-derived physical activity data, and learns adaptive selection policies across repeated study visits using reward signals derived from sparse fall incidence outcomes. We apply PAFIR to data from the Physio fEedback Exercise pRogram (PEER) cluster-randomized trial. Experimental results demonstrate that PAFIR more effectively captures longitudinal and structural patterns of feature relevance than state-of-the-art baselines, and enables dynamic, subject-specific feature selection. By adapting selected features over time, PAFIR supports more timely and personalized fall prevention strategies.

</details>


### 81. FM-Bench: A Benchmark for Long-Horizon Management with Competing Agents

- **Authors:** Tianyou Wang, Chongyang Gao, Kezhen Chen, Dong Chen, Yinghao He, Donghan Li, Wangcheng Xu, Hongjiu Zhang, Chi Li
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18423v2](http://arxiv.org/abs/2608.18423v2)
- **PDF:** [https://arxiv.org/pdf/2608.18423v2](https://arxiv.org/pdf/2608.18423v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language model agents now execute bounded tasks reliably. Whether they can sustain effective decision-making over long horizons, where actions have cumulative consequences and the environment responds to their choices, remains largely unmeasured. FM-Bench (Football Management Benchmark) measures this. An LLM agent runs a football club for 20 in-game years through 26 tools and roughly 340 to 400 decision stops. It drafts a squad on the same budget as every rival, trades players, negotiates contracts, invests in facilities and youth, sets lineups, and answers to a board that can fire it, while a deterministic engine accumulates every year into one final score with no LLM judge or human rater. The solo track plays each of 15 frontier models against a frozen scripted world, and the Arena places the same models plus a scripted anchor in one shared 20-year world; to our knowledge, the first head-to-head evaluation at this scale. We measure six behavioral capabilities behind the score. Across three seeds, all 15 models complete every horizon while the blind scripted baselines die out in most of theirs, and claude-fable-5 tops the solo board on mean score and the Arena, where the title nonetheless rotates among ten models. Neither scale, price, nor vendor predicts the order; the order settles only late in the horizon, and the best first-play human lands only at the bottom of the model board. What separates the models is managerial behavior rather than computation. Higher-scoring models reduce slow-payoff investment near the end, keep cash invested rather than idle, and open renewals well before the deadline, while token spend predicts nothing. No model learns the market's hidden prices from hundreds of rejected bids, and self-managed memory fails in two opposite modes: an archive that only grows or a plan rewritten every season. Code is available at https://github.com/Analogy-AI/fm-bench.

</details>


### 82. LEDGER: Claim-to-Evidence Trace Graphs for Auditing LLM Agents

- **Authors:** Daehong Kim, Haichao Miao, Shusen Liu
- **Published:** 2026-08-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18398v1](http://arxiv.org/abs/2608.18398v1)
- **PDF:** [https://arxiv.org/pdf/2608.18398v1](https://arxiv.org/pdf/2608.18398v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents can now carry out long-horizon technical workflows involving complex tool use, code execution, file edits, and generated artifacts. As agents do more work faster, the productivity bottleneck shifts from producing outputs to auditing whether those outputs are correct and trustworthy. Agent observability systems make fine-grained execution events visible, but visibility alone still leaves reviewers to reconstruct which actions, artifacts, and validation steps matter for a particular conclusion. We introduce LEDGER - Layered Evidence and Decision Graphs for Execution Review, a tracing and review system that builds layered trace graphs over observed agent sessions. LEDGER preserves Trace Records while grouping them into Evidence Nodes and Workflow Nodes, representing artifacts as evidence anchors, and adding typed semantic edges that connect claims to supporting actions, artifacts, and checks. Through data-analysis and coding examples, we show how the resulting traces expose workflow decisions, artifact lineage, repair steps, validation coverage, and claim-support paths for evidence-centered audit.

</details>


### 83. One Gate Is Not Enough: Composing Stateful Pre-Action Controls for Agentic AI

- **Authors:** Gaston Besanson
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18360v1](http://arxiv.org/abs/2608.18360v1)
- **PDF:** [https://arxiv.org/pdf/2608.18360v1](https://arxiv.org/pdf/2608.18360v1)
- **Categories:** cs.SE, cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems take consequential actions governed by more than one pre-action control at once: authority, resource, and evidence gates that can admit, degrade, or remediate an action before it executes. This paper's central object is remediation-induced control coupling: a remediation applied by one control can change the action, evidence, or context another control evaluates, invalidating that control's earlier judgment. We formalize this coupling and give a remediate-and-regate protocol that restores per-action soundness in the current bounded, idempotent setting under its stated assumptions. We further show that the two implemented remediation operators (evidence substitution and resource-budget downroute) do not commute -- a finite-model checker finds concrete counterexample instances -- making remediation order part of the control-plane semantics rather than an implementation detail. A governed evidence buffer that trusts its own most recent admitted write is a further instance of the same problem at the level of state -- current admissibility does not imply future reference trustworthiness -- and is vulnerable to poisoning from declared-uncovered defect classes; two mitigations reduce, not eliminate, that exposure. Supporting results establish the exact condition under which positive-weight linear aggregation of gate outcomes can compensate a member veto, a unified cross-control Evidence Set, and that composition manufactures no new detection coverage, reported honestly. Empirically, on a deterministic open-data artifact composing three published engines unmodified, CH1-CH5 meet their registered decision rules across all 30 pre-registered seeds; CH6 does so under W1 but not under the smaller W2 workflow, reported as such. This is a mechanism demonstration on open payload data with a synthetic metadata layer, not a claim about production prevalence.

</details>


### 84. Model Predictive Supervisory Control for Hierarchical and Distributed UAS Traffic Management

- **Authors:** Matheus P. Loures, Guilherme V. Raffo, Patrícia N. Pena
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18353v1](http://arxiv.org/abs/2608.18353v1)
- **PDF:** [https://arxiv.org/pdf/2608.18353v1](https://arxiv.org/pdf/2608.18353v1)
- **Categories:** eess.SY, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

This work proposes a hierarchical Model Predictive Supervisory Control (MPSC) framework for multi-agent systems with shared resources. MPSC integrates receding-horizon cost-optimal control with Supervisory control theory (SCT) based supervision that enforces safety, nonblockingness, and resource exclusivity. Scalability arises from hierarchical and scalable supervisor and automaton templates, enabling distributed execution without monolithic synthesis. Using this framework, this work develops an urban Unmanned aircraft system Traffic Management (UTM) model. The model supports pickup-and-delivery missions under time-varying demand efficiently.

</details>


### 85. Artifact-centered Claim-aware Observability for Autonomous Scientific Agents

- **Authors:** Xiangyu Yin, Ming Du, Michael H. Prince, Mathew J. Cherukara
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18312v1](http://arxiv.org/abs/2608.18312v1)
- **PDF:** [https://arxiv.org/pdf/2608.18312v1](https://arxiv.org/pdf/2608.18312v1)
- **Categories:** cs.CL, cs.CY, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous scientific agents now increasingly propose ideas, write code, run experiments, analyze results, and even draft papers. Observe and audit those agents are necessary but logging every model call is not enough, scientists also need to inspect the artifacts and claims that the systems produced and their relations. This is driven by the fact that failures in scientific agent systems are often distributed across several objects. A manuscript claim may cite the wrong evidence, a search process may select a degenerate candidate, a laboratory novelty claim may depend on an unstated rule, or a multi-agent plan may change without a visible trigger. Existing tracing, experiment tracking, and archival provenance tools are valuable, but their native objects do not make these scientific audit relations first-class. We argue that autonomous scientific systems should emit portable, claim-aware artifact lineage as a minimum audit layer. We propose a compact observability profile organized around individuals, operators, fitness records, lineage, archives, runs, streams, and steering commands. In this profile, scientific claims are ordinary individuals with explicit evidence bindings and verification records. The profile is intended as a semantic layer that complements current telemetry and provenance standards. Execution details can remain in OpenTelemetry. Final packages can export to PROV-O or RO-Crate standards.

</details>


### 86. SeisEvo: Evolution of Seismic Data Reconstruction Algorithms by Agents

- **Authors:** Yingjie Xu, Siwei Yu, Jianwei Ma
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18272v1](http://arxiv.org/abs/2608.18272v1)
- **PDF:** [https://arxiv.org/pdf/2608.18272v1](https://arxiv.org/pdf/2608.18272v1)
- **Categories:** physics.geo-ph, cs.AI, cs.NE, eess.SP


> Summary unavailable.


<details>
<summary>Abstract</summary>

Classical seismic data reconstruction relies on manually designed structural priors and iterative operators, whose coupled design space is far larger than manual trial and error can explore systematically. Deep-learning methods encode the reconstruction rules in learned weights rather than in an explicit operator that can be inspected and modified. We propose SeisEvo (Seismic Algorithm Evolution), which does not optimize a single reconstruction result but searches for the algorithm that produces it. Starting from a classical reconstruction algorithm, an LLM-driven multi-agent search modifies only the components that the user has opened for editing, without prescribing the mechanism to be discovered. Candidates that violate the physical constraints of the task are rejected outright, and the remaining ones are scored by execution. The output is neither an agent system nor a neural network, but a standalone white-box algorithm that requires no agent or neural network at inference time. For interpolation without added noise, the search discovered a residual-gated, phase-aligned dip-consistency projection; Evo-POCS improves the SNR over classic POCS by 3.49 dB on average across missing ratios from 30% to 70%. For simultaneous interpolation and denoising, it discovered a reliability-grouped singular-value shrinkage; Evo-MSSA improves the average reconstruction SNR by more than 7 dB over classic MSSA and by more than 3 dB over a stronger rank-reduction baseline. Both operators retain their gains on data not used during the search. To the best of our knowledge, this is the first study to formulate the design of a seismic reconstruction operator as a constrained, LLM-driven program evolution task. Agentic algorithm evolution can thus complement deep learning in discovering explicit, inspectable, and deployable seismic processing algorithms.

</details>


### 87. Contracting for LLM Delegation: Moral Hazard in Technology and Effort Choice

- **Authors:** Nanda Kishore Sreenivas, Kate Larson
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18232v1](http://arxiv.org/abs/2608.18232v1)
- **PDF:** [https://arxiv.org/pdf/2608.18232v1](https://arxiv.org/pdf/2608.18232v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We extend the standard Principal-Agent framework to scenarios where the Agent selects from a suite of technologies, each characterized by a distinct cost-capability profile. This framework is increasingly critical in the era of Large Language Models (LLMs), where Agents choose both a model and an associated effort level (e.g., token budget). We model the relationship between output quality and effort as a concave, saturating function, which depends on the Agent's hidden two-dimensional action choice balancing technology selection and effort allocation. We derive the optimal linear contract for the Principal, demonstrating that the Agent's best response is characterized by a threshold reward share that triggers technology switching. Finally, we calibrate our model using open-weight LLM pairings across the MATH and MMLUPro benchmarks. We show that both Principal and Agent, when employing bandit algorithms to navigate this environment, converge to strategies that closely align with our theoretical equilibrium. These results suggest that simple linear contracts can effectively incentivize complex, technology-aware delegation in agentic workflows.

</details>


### 88. Multi-Agent AI System for Radiology Report Structuring and Quality Assurance with Independent Radiologist Evaluation

- **Authors:** Iryna Hartsock, Cesar Lam, Christopher Otteni, Aliya Qayyum, Robert Gatenby, Cyrillo Araujo, Ghulam Rasool
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18072v1](http://arxiv.org/abs/2608.18072v1)
- **PDF:** [https://arxiv.org/pdf/2608.18072v1](https://arxiv.org/pdf/2608.18072v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Purpose: To develop and evaluate a locally deployed multi-agent AI system for radiology report structuring and quality assurance. Materials and Methods: This retrospective study included 638 radiology reports from CT examinations of the chest, abdomen, and pelvis dictated by 15 board-certified radiologists in 2023 and 2024. A multi-agent AI pipeline was developed to perform report structuring and quality assurance (QA). The system structured the report into standardized anatomical sections at the sentence level using regex rules and local large language models. It also detected mismatches between the Findings and Impression sections, or within sections; gender-anatomy conflicts; and undocumented communication of critical findings. Two board-certified radiologists independently evaluated a 45-report subset. Results: The multi-agent system structured the Findings sections of all reports (22,270 sentences) into a predefined anatomical format while retaining the original report content. The system flagged 90 (14.1%) reports, most commonly for section mismatches (80 reports, 12.5%). In the radiologist evaluation, both reviewers agreed that 31 (69%) were correctly restructured, 2 reports (4%) were incorrectly restructured, and disagreed on the remaining 12 reports (27%). Both reviewers agreed that no clinically important information was omitted and no fabricated content was introduced. Overall QA performance was rated as "excellent" or "good" in 84% of the evaluated reports, with the remaining reports rated as "fair". Conclusion: A locally deployed multi-agent AI system combined radiology report structuring and quality assurance within a single workflow. The system demonstrated favorable performance in radiologist evaluation. Such systems may support standardization of reporting and quality assurance in radiology practice.

</details>


### 89. Delegation Asymmetry in Agentic Recommender Systems: Measuring Two-Sided Receptivity in Online Dating

- **Authors:** Daria Leshchikova, Valentina V. Kuskova, Dmitry Zaytsev, Valerii Klimov
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18058v1](http://arxiv.org/abs/2608.18058v1)
- **PDF:** [https://arxiv.org/pdf/2608.18058v1](https://arxiv.org/pdf/2608.18058v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous LLM agents that converse on a user's behalf are an emerging design pattern in matching platforms, yet their viability depends on a condition rarely examined: users must accept not only delegating conversation to an agent, but also receiving agent-mediated communication from others. We study this condition using two large-scale surveys of active users of a major dating platform (N=2,894 on generative profile features; N=2,617 on autonomous conversational agents, fielded in two languages). We develop a latent-variable measurement model of agent receptivity based on graded response models with latent regression, and show via model comparison that willingness to send and willingness to receive agent communication are distinct constructs: highly correlated (rho=0.92) but separable (Delta BIC=52), with partial measurement invariance across languages. The model quantifies a systematic delegation asymmetry: deploying one's own agent requires far lower receptivity (threshold -0.38) than engaging a counterpart's agent (+0.32; full engagement +1.39), and mean deployment propensity exceeds engagement propensity roughly threefold. Under a random-pairing counterfactual derived from stated receptivity, only 4-13% of directed dyads combine agent deployment with receiver engagement, with a pronounced gender-directional imbalance. Design counterfactuals quantify the levers: a reciprocity requirement cuts interaction volume by half or more by excluding nearly two-thirds of would-be deployment, while routing agent contacts on receive receptivity triples per-contact engagement, a lift that survives out-of-sample validation with the target item held out (AUC 0.88, 3.1x quartile lift under respondent-level cross-validation). We discuss implications for agentic recommender design, including disclosure, opt-in mechanics, and receptivity-aware matchmaking.

</details>


### 90. StagedWorkspace: A Versioned Workspace for Knowledge-Work Agents

- **Authors:** Yining Hua, Hongbin Na, Yifan Zhou, Akshay Kalose, Cyrus Ayubcha, Levi Lian
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18050v1](http://arxiv.org/abs/2608.18050v1)
- **PDF:** [https://arxiv.org/pdf/2608.18050v1](https://arxiv.org/pdf/2608.18050v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly perform knowledge work (i.e., produce and modify persistent digital artifacts such as code repositories, documents, spreadsheets, slides, reports), yet the parsed views they search, the native files they edit, the changes they review, and the artifacts they submit can refer to different versions of the same work product. We formulate this as a workspace-state contract: every view should be explicitly tied to a version of the evolving workspace state. Coding agents partly address this need through repository contracts for search, diffs, and tests, whereas an analogous contract is less explicit for PDFs, spreadsheets, slides, notebooks, and mixed-format project folders. We propose StagedWorkspace, a versioned workspace for knowledge-work agents. The workspace binds parsed records and review diffs to content hashes of the native files as they change. In fixed-harness ablations on OfficeQA Pro and APEX-Agents, dual parsed/native access has the highest point estimate for every tested model; relative to the more limiting single view, it improves OfficeQA Pass@1 by 8.3-12.1 points and APEX mean rubric score by 4.7-9.2 points. SW-AGENT scores 63.9% with Gemini 3.1 Pro on OfficeQA and 42.1 with GPT-5.4 Nano on APEX, compared with published same-model scores of 29.3% and 25.5, respectively. A paired review-axis ablation on 57 file-editing tasks further finds higher observed scores when diffs are visible. These results identify workspace state as an experimental variable in knowledge-work agents and motivate benchmarks that score evidence, staged edits, and submitted artifacts as explicit state transitions.

</details>


### 91. Language Has Two Parameters: Narrative-Induced Semantic Plasticity and Phase-Sensitive Interpretation

- **Authors:** Hollis Robbins
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18041v2](http://arxiv.org/abs/2608.18041v2)
- **PDF:** [https://arxiv.org/pdf/2608.18041v2](https://arxiv.org/pdf/2608.18041v2)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reading fiction or encountering narrative generally does not merely add information. The encounter changes the reader. This paper proposes that encounters alter persistent relations among simultaneously active meanings, producing individual and shared histories that population-trained language models do not necessarily retain. A model may be told of an encounter and reproduce its consequences while the history remains in context; this is not the same as being changed by the encounter. This paper formalizes this missing relational state as phase, sets out testable predictions about encounter order, quotation, and suppressed meanings, and argues that future AI agents will need persistent semantic states indexed to particular individuals and relationships. The matching risk is semantic poisoning: an attack that re-signs relations among meanings already present.

</details>


### 92. EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection

- **Authors:** Lei Jiang, Ye Wei, Xinyu Xi, Jordan Langham-Lopez, Yifan Bao, Raad Khraishi, Yihao Ang, Anthony K. H. Tung, Lukasz Szpruch, Hao Ni
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17933v1](http://arxiv.org/abs/2608.17933v1)
- **PDF:** [https://arxiv.org/pdf/2608.17933v1](https://arxiv.org/pdf/2608.17933v1)
- **Categories:** cs.AI, cs.CE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Financial time series exhibit non-stationary and heterogeneous statistical properties, making change-point detection challenging because no single unsupervised algorithm performs consistently across assets and market regimes. Conventional workflows consequently depend heavily on expert-driven model selection, feature design, and hyperparameter tuning, limiting their scalability and adaptability. We propose EvoTS-Agent, a validation-guided self-evolving LLM agent for autonomous financial time-series change-point detection. EvoTS-Agent first performs curated exploratory data analysis to characterize dataset properties and initialize candidate detection models. It then evolves executable experiment trajectories through three complementary operators: \textit{Revision} exploits the current best solution, \textit{Alternative Strategy} explores fundamentally different modeling directions when progress stagnates, and \textit{Recombination} synthesizes complementary evidence from high-performing trajectories. Validation feedback guides trajectory evolution throughout the search, enabling the agent to adapt its detection pipeline to the statistical characteristics of each dataset while preserving reliable optimization. Experiments across four benchmark datasets demonstrate that EvoTS-Agent consistently outperforms existing LLM-based agents while maintaining a 100\% execution success rate across all evaluated backbone LLMs.

</details>


### 93. A Theoretical Framework for Parallel Lifelong MAPF Using Group Decentralized Planning

- **Authors:** Alex DeWeese, Jiaoyang Li, Guannan Qu
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17928v1](http://arxiv.org/abs/2608.17928v1)
- **PDF:** [https://arxiv.org/pdf/2608.17928v1](https://arxiv.org/pdf/2608.17928v1)
- **Categories:** cs.MA, cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

In the Lifelong Multi-Agent Path Finding (L-MAPF) problem, agents must repeatedly move from one destination to another while avoiding obstacles and inter-agent collisions. Widely regarded as one of the highest-performing solutions to this problem is the Rolling-Horizon Collision Resolution (RHCR) framework. However, commensurate with its quality solutions, it incurs a computational cost that limits its applicability to even modest agent counts. In this paper, leveraging theoretical methods from the Locally Interdependent Multi-Agent MDP literature, we first theoretically prove the near-optimality of RHCR in a discounted MDP formulation of the L-MAPF problem. Then, we leverage these results to naturally motivate an extended framework called Group Decentralized RHCR (GD-RHCR) which incorporates a group decentralized structure that partitions agents based on a transitive communication scheme and plans for each partition of agents in parallel. We show that both RHCR and GD-RHCR achieve similar exponentially close to optimal guarantees, establishing a theoretical duality between the time based restrictions performed by vanilla RHCR and the additional space based partitioning performed by GD-RHCR. Lastly, we show that across varying maps, GD-RHCR is able to attain high throughput that scales into higher agent counts while maintaining a significantly lower per plan cost.

</details>


### 94. CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion

- **Authors:** Zheling Tan, Jin Gao, Dequan Wang
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17911v1](http://arxiv.org/abs/2608.17911v1)
- **PDF:** [https://arxiv.org/pdf/2608.17911v1](https://arxiv.org/pdf/2608.17911v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents operate across structured workflows and sessions, preserving long-term history does not ensure that later contexts can recover relevant evidence through a bounded memory interface. We study this evidence-reachability problem in long-term conversational memory, where retrieval still relies heavily on semantic similarity. This works well for topical recall, but it often misses earlier experiences, plans, or motivations that are semantically distant from the later events they help explain. Existing memory graphs provide cross-memory structure, yet links driven mainly by semantic overlap can duplicate what the host retriever already recovers. We argue that link construction should instead prioritize a sparse set of retriever-complementary associations. We present CABLE (Complementary Antecedent-Based Linking and Expansion), a plug-in augmentation that constructs links designed to extend the host retriever's direct semantic reach. For each new memory, CABLE generates antecedent-oriented queries, retrieves prior memories, subtracts candidates in the direct semantic neighborhood, and verifies the remainder before adding the accepted complementary associations into a sparse directed graph. At retrieval time, CABLE expands the host system's retrieved seeds along these links to surface implicit supporting evidence. We evaluate CABLE with A-MEM on LoCoMo and MA-LongMemEval, and further integrate it into SimpleMem and Mem0g on LoCoMo, using Qwen3.5-27B, DeepSeek-chat, and GPT-4o-mini. CABLE yields higher mean LLM-judge scores in every evaluated system-level setting, with the largest gains in categories where useful evidence is distributed across memories or sessions, including open-domain, multi-session, and preference-oriented questions. These results support prioritizing sparse, reasoning-relevant associations that complement rather than duplicate the host retriever.

</details>


### 95. Debate Training Reduces Reward Hacking in RLAIF

- **Authors:** Zachary Kenton, Lili Janzer, Rory Greig, Tian Huey Teh, Kirill Tyshchuk, Jonah Brown-Cohen, Harri Edwards, Senthooran Rajamanoharan, Noah Y. Siegel, Natasha Jaques, Rohin Shah
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17776v1](http://arxiv.org/abs/2608.17776v1)
- **PDF:** [https://arxiv.org/pdf/2608.17776v1](https://arxiv.org/pdf/2608.17776v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We demonstrate that RL finetuning an LLM using debate, a two-player adversarial game between a generator and a critic adjudicated by a weaker LLM judge, reduces reward hacking compared to a reinforcement learning from AI feedback (RLAIF) baseline. Reward hacking is a central obstacle in RLAIF: as training progresses, the policy learns to exploit systematic errors in its AI judge, degrading task performance, a problem that worsens precisely when the judge is weaker than the policy, the setting most relevant to overseeing increasingly capable AI systems. We study mathematics tasks, where final-answer correctness is verifiable, allowing us to measure reward hacking dynamics. We train a Gemini~2.5 Flash-class policy with a frozen, weaker Gemini~2.5 Flash Lite judge, comparing a single-player RLAIF baseline against debate. While the baseline quickly hacks the judge, debate maintains judge performance throughout training, leading to a higher peak validation accuracy (45\% performance gap recovered) that persists through many RL steps. Additional experiments show that: 1) further weakening the judge leads to faster hacking, but this can be compensated by adding an additional debate round; 2) debate incentives override prompted misalignment; 3) RL using an LLM judge has a smaller train/validation reward gap than RL from verifiable rewards; 4) learning to critique to convince the judge using ground truth labels is possible but slow. Taken together, our results are a positive update on the feasibility of debate, while highlighting that balancing multi-agent training is critical: without player constraints, adversarial training risks defaulting to critic judge-hacking. We show that critique word limits (effective up to 150 words) successfully balance the game and avoid judge hacking, though this introduces a trade-off by restricting critic expressive clarity.

</details>


### 96. D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory

- **Authors:** Xule Liu, Yijun Liu, Chao Li, Shao Kun
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17756v2](http://arxiv.org/abs/2608.17756v2)
- **PDF:** [https://arxiv.org/pdf/2608.17756v2](https://arxiv.org/pdf/2608.17756v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory is a key capability of LLM agents. Persistent memory extends this across sessions---enabling recall, revision, and personalization. Yet its multi-stage pipeline (ingestion, retrieval, filtering, generation) makes failures difficult to localize: end-to-end evaluation reveals that an error occurred, but not which stage caused it. Existing evaluations often report aggregate performance without paired statistical comparisons, slice-level non-regression checks, or stage-level diagnostic traces. We propose D$^2$ACCI (Diagnostic-Driven Artifact-based Closed-loop Controlled Iteration), a dual-loop protocol whose outer diagnostic gate promotes, feature-flags, or rejects memory interventions based on paired evidence, protected-slice monitoring, and trace-level localizability. We further introduce DCR, a graded observability metric that measures whether failures remain localizable, and D$^2$ACCI-Eval, a reusable artifact for gate replay. We instantiate the protocol in MemStack and evaluate on three public benchmarks, achieving 93.59% on LoCoMo, 90.93% on LongMemEval, and 57.20% on PersonaMem-V2. Five paired ablations show that supplement extraction, session-memory retrieval, and Forget Guard yield statistically significant gains (+1.9 to +3.7pp, all p $\le$ .003). In contrast, BM25/RRF is retained as a monitored feature flag---a distinction invisible to aggregate-only evaluation. A diagnostic audit shows enriched traces substantially improve root-cause agreement over result-only relabeling. Diagnostic artifacts reach 98--100% DCR@3 versus 0% for results-only logs. These results establish that robust memory-system iteration demands traceable, statistically grounded, and regression-aware evidence---exactly the gap D$^2$ACCI fills.

</details>


### 97. The Curious Case of Exploding DecPOMDPs: Containing the Fire through Policy Counting

- **Authors:** Nazlı Nur Karabulut, Tanya Braun
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17749v2](http://arxiv.org/abs/2608.17749v2)
- **PDF:** [https://arxiv.org/pdf/2608.17749v2](https://arxiv.org/pdf/2608.17749v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Decentralised partially observable Markov decision processes (DecPOMDPs) provide a general framework for modelling multi-agent decision making under uncertainty. However, DecPOMDPs are known to suffer from exponential complexity in the number of agents. One way to combat this intractability in agent numbers is to look at partitions of agents that exhibit a form of symmetry among agents, allowing for a compact encoding by counting. However, a challenge arises as the policy space explodes, even though the model complexity and evaluation cost reduce to a polynomial dependence. In this paper, we redirect our focus from counting agents to counting policies, which actually enables tractability in agent numbers for so called policy-counted DecPOMDPs. Further, we present policy-counted dynamic programming using the compact representation to solve policy-counted DecPOMDPs efficiently.

</details>


### 98. Offline Multi-Agent Reinforcement Learning with a Physics-Informed World Model for Cooperative Mixed Traffic Control

- **Authors:** Lu Liu, Chi Xie, Xi Xiong
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17739v1](http://arxiv.org/abs/2608.17739v1)
- **PDF:** [https://arxiv.org/pdf/2608.17739v1](https://arxiv.org/pdf/2608.17739v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

This study investigates cooperative control of connected and automated vehicles (CAVs) at partially observable highway bottlenecks in mixed traffic, aiming to mitigate congestion without relying on complete global traffic states or online trial-and-error. We propose a physics-informed world model-based offline multi-agent reinforcement learning framework that reconstructs a physically interpretable global traffic state from local CAV observation-action histories, with coupled macroscopic-microscopic traffic dynamics providing physics-based supervision. A probabilistic ensemble world model learns traffic-state transitions and system rewards, while model disagreement quantifies epistemic uncertainty. Multi-step imagined rollouts with pessimistic rewards and uncertainty-driven truncation are then used for offline policy learning. Experiments in a SUMO-based on-ramp bottleneck using approximately $1\times10^6$ offline transitions show that physics supervision improves state reconstruction and world-model prediction accuracy.

</details>


### 99. Cross-View Correspondence Is a Measurement Intervention: Two-Sided Validation for Agent Evaluation and Credit Assignment

- **Authors:** Zhen Zhang, Ahmad Hafez, Amr Alanwar
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17713v1](http://arxiv.org/abs/2608.17713v1)
- **PDF:** [https://arxiv.org/pdf/2608.17713v1](https://arxiv.org/pdf/2608.17713v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent evaluations and trace-based learning often compare outputs across transformed views through a post-response correspondence treated as neutral preprocessing. We show that this correspondence is a measurement intervention: omitting it can manufacture sensitivity, an over-aggressive map can manufacture invariance, and multiple optimal correspondences can leave mechanism labels and signed learning credit unidentified. We develop a validity theory and audit with three components: two-sided validation of nuisance removal and response preservation, all-optima identification of downstream conclusions, and uncertainty propagation after validity is established. We characterize the linear feasibility boundary for response-preserving nuisance removal, compute sharp ranges over exact-optimum correspondence sets, and give a distribution-free certificate that retains a credit coordinate only when all exact optima agree on its nonzero sign. Across public code and SQL pipelines, two deterministic optimal tracebacks disagree on temporal localization for 55.9% of 1,586 nonzero trajectory pairs; two frozen 800-rollout tool-use audits, including a task-and-seed-disjoint replication, expose exact-optimum reversals of intended turn-level credit, although a clean public quick-start subset shows none. A pre-registered transport gate failed on natural responses; frozen corrected and held-out controls then show that a map calibrated only on benign examples erases every retained harmful response, while two-sided validation selects response-preserving alternatives. Cross-view correspondence must therefore be declared, validated, and propagated into uncertainty before agent evaluation or credit assignment supports a point conclusion.

</details>


### 100. GADR: Gathering Architecture Decision Records from Meeting Transcriptions

- **Authors:** Lucas Daniel Costa da Silva, Kiev Gama
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17694v1](http://arxiv.org/abs/2608.17694v1)
- **PDF:** [https://arxiv.org/pdf/2608.17694v1](https://arxiv.org/pdf/2608.17694v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing LLM-based approaches to Architecture Decision Record (ADR) generation share a critical and largely unexamined assumption: that input is already reasonably structured. In practice, architectural decisions emerge from informal, noisy meetings where choices are implicit, fragmented, and entangled with off-topic dialogue, precisely the conditions under which single-pass prompting degrades. This paper presents GADR, a multi-agent, self-correcting workflow that extracts architectural decisions from raw meeting transcriptions and generates Nygard-formatted ADR drafts. A feasibility study comprising five real project meeting transcripts, expert review by four senior architects, and evaluation by fifteen students provides initial evidence that the agentic workflow captures most expert-identified decisions and produces drafts participants found clear and useful, outperforming zero-shot and few-shot baselines in stability and structural adherence. The study also addresses the underexplored trade-off of RAG-based enrichment improving ADR depth while simultaneously risking transcript-unfaithful content, raising open questions about traceability in automated architectural documentation that we believe is worth the community's attention.

</details>


### 101. Benchmarking Automated Security Patch Backporting: How Far Are We?

- **Authors:** Jincheng Yang, Yulong Fu, Chengwei Liu, Lyuye Zhang, Fangyuan Zhang, Bingyang Ren, Yang Liu, Hui Li
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17671v1](http://arxiv.org/abs/2608.17671v1)
- **PDF:** [https://arxiv.org/pdf/2608.17671v1](https://arxiv.org/pdf/2608.17671v1)
- **Categories:** cs.SE, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated security patch backporting is critical for mitigating N-day vulnerabilities. Recent tools report success rates above 80% on their respective datasets. However, these evaluations are often confined to homogeneous environments, such as one repository or specific project versions. Consequently, it remains unclear how well these tools generalize beyond their originally targeted scenarios. We present Porting Benchmark, a curated dataset of 1,234 security patch backporting cases spanning cross-version, cross-branch, and cross-repository scenarios, paired with a common evaluation framework. Using this benchmark, we evaluate five tools spanning program analysis, LLM prompting, and LLM agents under aligned settings. Our results show that aligned evaluation changes the apparent performance landscape: PortGPT and TSBPort remain comparatively strong on the Replication Dataset, while FixMorph and Mystique degrade substantially under the common protocol. Performance degrades sharply on structurally complex patches: the best commit-level success rate falls from 85.2% on Type-I patches to 24.0% on Type-IV. We identify four root-cause categories (missing target API awareness, cross-version semantic mismatch, non-local dependency propagation failure, and patch construction or localization failure) and derive concrete directions for next-generation tool design. On a 45-case dynamically validated subset with verified test cases and constructed POCs, we further observe that reference-based benchmark scores do not fully capture real-world remediation: exact match sharply under-credits harder target adaptations, while executable validation reveals residual integration failures in the target that static reference agreement misses. Executable-feedback refinement provides limited but measurable recovery on the hardest executable cases.

</details>


### 102. Code as Representation: A Compilable Parsing Paradigm for Academic Documents

- **Authors:** Rihui Jin, Jun Wang, chengyuan zhu, Liang Mingyu, Yue Gao, Li Yunxuan, Kuicai Dong, Guilin Qi, Lin Ren, Yongrui Chen, Xinbang Dai, Jiaqi Li, Tongtong Wu, Gholamreza Haffari
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17550v1](http://arxiv.org/abs/2608.17550v1)
- **PDF:** [https://arxiv.org/pdf/2608.17550v1](https://arxiv.org/pdf/2608.17550v1)
- **Categories:** cs.CV, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Academic papers are a primary carrier of scientific knowledge, yet most of this knowledge remains locked in PDFs that are optimized for human reading rather than machine use. For Multimodal Large Language Models (MLLMs), the core challenge is not only perception, but representation: scientific pages interleave text with Structured Academic Elements (SAEs) such as tables, formulas, charts, and pseudocode, whose structure, data, and logic are poorly preserved by common surrogates like Markdown. We therefore propose Compilable Academic Document Parsing (CADP), a paradigm that reconstructs a full page as contextual \LaTeX{} plus executable Python, so that structure-preserving elements and executable chart representations can be reconstructed, recompiled, and directly verified against the source page. To support this setting, we introduce CADP-Bench, an expert-verified benchmark of full academic pages containing tightly coupled text and multiple SAE types, evaluated through a re-injection compilation protocol. We further study current capabilities using SOTA MLLMs and an exploratory multi-agent baseline that incorporates common agentic techniques. Results show that even frontier models still struggle to produce high-fidelity executable reconstructions, highlighting substantial room for improvement in structure-aware scientific document parsing. CADP-Bench is released for future research.

</details>


### 103. When AI Designs AI: Innovation or Imitation?

- **Authors:** Yikang Yang, Zhengxin Yang, Luzhou Peng, Minghao Luo, Yanqi Kan, Wanling Gao, Jianfeng Zhan
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17471v1](http://arxiv.org/abs/2608.17471v1)
- **PDF:** [https://arxiv.org/pdf/2608.17471v1](https://arxiv.org/pdf/2608.17471v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in LLM agents have made them increasingly capable of designing methods for complex AI tasks. This raises two central questions about agent-designed methods relative to human-designed methods: how well they perform, and how different their algorithmic designs are. To study these questions, this paper introduces an analysis that derives task-specific algorithmic design spaces from human-designed methods, maps both human- and agent-designed methods into these spaces, and quantifies their algorithmic differences at the module level. Widely used LLM agents are evaluated on a suite of representative, open-ended AI tasks spanning multiple modalities, and the methods they design are analyzed in terms of both task performance and algorithmic differences from human-designed methods. Experimental results show that current agents can occasionally match or surpass human state-of-the-art (SOTA) performance (10/72 configurations), but such success does not generalize reliably across tasks or agents. Moreover, 96.8% of agent-designed methods fall within human-derived algorithmic design spaces, largely recombining algorithmic choices found in human-designed methods, while nearly half exactly match an existing human algorithmic design. Taken together, these findings suggest that although current agents can occasionally match or surpass human SOTA performance, their algorithmic designs remain within human-derived algorithmic design spaces, reflecting the reuse and recombination of algorithmic choices.

</details>


### 104. The Evaluation Context Protocol (ECP): A Portable Contract for AI Agent Evaluation

- **Authors:** Aniket Wattamwar, Manav Anandani, Mrunal Kakirwar
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.19263v1](http://arxiv.org/abs/2608.19263v1)
- **PDF:** [https://arxiv.org/pdf/2608.19263v1](https://arxiv.org/pdf/2608.19263v1)
- **Categories:** cs.SE, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The evolution of artificial intelligence has necessitated a fundamental shift from evaluating isolated Large Language Models (LLMs) to assessing autonomous agentic architectures. This paper explores the critical methodologies for evaluating AI agents and the essential role of advanced observability infrastructure. We analyze the architectural components of agents and identify the severe limitations of current evaluation paradigms, including benchmark exploitation, the "confidently wrong" phenomenon, and the discrepancy between theoretical capability and operational reliability. To begin addressing the fragmentation in current evaluation infrastructure, this paper proposes the Evaluation Context Protocol (ECP), an early-stage, vendor-neutral framework intended to act as a portable evaluation contract layer for agentic systems. In its current form ECP defines a small JSON-RPC interface over which an agent exposes its user-visible output, the tool calls it made, and evaluator-safe audit context, and against which programmatic checks can be run uniformly across frameworks and continuous integration systems. We describe an open-source reference implementation that includes adapters for LangChain, LlamaIndex, CrewAI, and PydanticAI, and we situate the design against failure modes documented in the recent literature. ECP is presented as work in progress rather than a finished standard: the evaluation surface, method set, and grader families are all expected to change as the protocol is exercised against more systems, and the empirical validation required to justify adoption is outlined as future work.

</details>


### 105. Task-Aware Harness Provisioning for LLM Agents in Mission-Critical Infrastructure Operations

- **Authors:** Liangtao Lin, Qingang Zhang, Zhaomeng Zhu, Tianwei Zhang, Yonggang Wen
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17433v1](http://arxiv.org/abs/2608.17433v1)
- **PDF:** [https://arxiv.org/pdf/2608.17433v1](https://arxiv.org/pdf/2608.17433v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents have been widely adopted to operate mission-critical infrastructure (MCI). These agents normally rely on a harness that determines what information they can access, which tools they can use, and what actions they can take. Existing systems often expose the same comprehensive harness to every task, which may not be necessary and cause resource wastes. In this paper, we focus on the identification of optimal harness configurations, and view it as a resource-matching problem between what each task requires and what the harness provides. To measure this match, we classify MCI tasks based on the mathematical representation of the underlying system and rank harness configurations by the amount and type of information they provide. We then construct task-to-harness mappings from two sources: mining research literature and measuring controlled agent execution. Leveraging the measured mapping, we propose a new harness provisioning algorithm: map-guided escalation. It begins with a task-specific harness and expands to full provision only after a failed self-check. We evaluate our method in two representative MCI tasks: in liquid cooling, it improves the agent accuracy from 0.652 under full provision to 0.715 and achieves accuracy comparable to Reflexion with 48% fewer tokens; In power grids, full provision remains accuracy-optimal, while map-based provisioning offers lower-cost alternatives. These findings show that harness provisioning follows a domain-dependent accuracy-cost Pareto frontier rather than a universal optimum.

</details>


### 106. Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements

- **Authors:** Zhi Zheng, Rongsheng Chen, Yunpeng Ba, Zhenkun Wang, Yee Whye Teh, Wee Sun Lee
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17310v2](http://arxiv.org/abs/2608.17310v2)
- **PDF:** [https://arxiv.org/pdf/2608.17310v2](https://arxiv.org/pdf/2608.17310v2)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement Learning (RL) has been promising in single-turn LLM fine-tuning. However, long-horizon agentic reasoning introduces increasingly branching interactions and sparse rewards, exposing several limitations of RL: its heavyweight backpropagation-based training stack makes it impractical to fine-tune larger LLMs, and longer-horizon trajectories make credit assignment in RL substantially harder. This paper argues that evolution strategies (ES) can be a better choice for fine-tuning long-horizon LLM agents. Compared with agentic RL, ES offers three key advantages: 1) Model Scalability: ES enables full-parameter optimization with only minimal, inference-level GPU memory, making it possible to fine-tune large LLMs. 2) Flexibility: its lightweight, black-box feedback interface makes ES fine-tuning easy to compose with prompt-space evolution (e.g., skill optimization & test-time compute); and 3) Long-Horizon Scalability: ES performs trajectory-level parameter attribution without decomposing rewards across horizons, yielding better scalability than Agentic RL as the horizon length grows. Based on this insight, we propose Agentic ESOpt, a full-parameter agentic fine-tuning framework tailored to flexible parameter--context co-evolution. At each step, Agentic ESOpt samples perturbations around the current LLM parameters, evaluates the resulting agents with rewards, and applies an online reward-weighted update. To improve the exploration--adaptation trade-off, Agentic ESOpt further introduces a cosine decay schedule of the perturbation scale $σ$. On WebArena-Lite, full-parameter optimization of Qwen-3.5-27B improves the No Skill baseline by 6.69%. In test-time automatic heuristic design, Agentic ESOpt performs online prompt--parameter co-evolution, improving its matched baseline in 28 of 36 settings.

</details>


### 107. When Agents Act on Web3: An Attack-Surface Survey of MCP, Skills, and Tool Calling

- **Authors:** Rabimba Karanjai, Yang Lu, Nour Diallo, Wujie Xiong, Lei Xu,  Weidong,  Shi
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17275v1](http://arxiv.org/abs/2608.17275v1)
- **PDF:** [https://arxiv.org/pdf/2608.17275v1](https://arxiv.org/pdf/2608.17275v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly act rather than merely read: across the Model Context Protocol (MCP) ecosystem, the share of deployed tools that modify external state has risen from 27% to 65% of tool use. When agents exercise this authority on public blockchains through MCP, skills, and tool calling, the consequences of an attack are governed by the blockchain execution layer rather than by conventional software assumptions. This survey argues that four properties of that layer (irreversibility, signing authority, continuous autonomy, and sequence-level composition) qualitatively change the threat model, turning the recoverable failures of generic agent security into a standing, irreversible loss. We organize the fragmented MCP-security literature into an attack-surface taxonomy, then contribute a Web3 risk-mapping matrix that ties each attack class to its amplified impact, the responsible amplifiers, a representative mitigation, and the residual gap. We synthesize defenses, including emerging blockchain-based mechanisms, and find them improving but insufficient: measured protections stop fewer than 30% of attacks, and model-level safety refuses fewer than 3%. We close by positioning the work against adjacent surveys and deriving a research agenda from the matrix's open cells.

</details>


### 108. Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL

- **Authors:** Yunhao Yang, Yuexin Bian, Yunjie Tian, Di Fu, Tianjin Huang, Yuanyuan Shi, Ziang Xiao, Nuno Vasconcelos, Yijiang Li
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17253v2](http://arxiv.org/abs/2608.17253v2)
- **PDF:** [https://arxiv.org/pdf/2608.17253v2](https://arxiv.org/pdf/2608.17253v2)
- **Categories:** cs.LG, cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) has emerged as a powerful approach for improving reasoning in language and vision-language models, yet its strongest successes still depend heavily on ground-truth supervision (e.g., verifiable reward). Such annotations are costly to obtain and become increasingly scarce as reasoning capabilities advance beyond what humans can reliably evaluate. Self-rewarding RL reduces this dependence by enabling models to derive reward signals from their own completions. However, training solely on self-generated feedback can reinforce existing biases and suboptimal behaviors, reduce response diversity, and ultimately lead to homogenized responses and training collapse. In this work, we show that unsupervised reasoning can emerge through cooperative multi-agent training. We introduce Co-RL, a framework in which multiple decoupled models, sharing no parameters, are simultaneously optimized through RL using rewards derived from their peers. We further show that increasing cohort diversity, through heterogeneous model families, sizes, and rephrased training samples, reduces the correlated errors that drive self-reinforcing feedback loops. This diversity consistently improves reasoning performance, maintains behavioral diversity, and mitigates training collapse. Across text-only and multimodal domains, Co-RL consistently outperforms the base models and prior label-free approaches, while matching or surpassing supervised methods, without access to any ground-truth labels. Concretely, Co-RL yields average gains of 3.0-8.6% across seven text-only benchmarks for LLMs and 2.3-7.2% across four multimodal benchmarks for VLMs. Code is available at https://github.com/DrStranded/Co-RL.

</details>


### 109. Towards Reversible Forgetting: Managing Obsolete Knowledge in Continual Enterprise AI Agents

- **Authors:** Nilutpaul Sarker Yash, Tirtho Roy, Ushashi Bhattacharjee
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.18177v1](http://arxiv.org/abs/2608.18177v1)
- **PDF:** [https://arxiv.org/pdf/2608.18177v1](https://arxiv.org/pdf/2608.18177v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Continual learning has traditionally treated forgetting as a failure, emphasizing preservation of previously acquired knowledge as environments evolve. We argue that this objective is incomplete for enterprise AI agents operating in non-stationary environments, where customers, policies, tools, workflows, regulations, and market conditions change over time. Indiscriminate retention can allow obsolete knowledge to influence decisions, creating negative transfer and operational risk. We therefore propose reversible forgetting: a conceptual framework with three operational memory states: active, dormant, and retired, and a reactivation transition that can restore dormant knowledge when its relevance returns. We instantiate the framework as a Hysteretic Reversible Memory Controller that accumulates relevance evidence, uses asymmetric thresholds to prevent state oscillation, tests reactivation in shadow mode, and gates retirement through policy. The framework reduces the influence of obsolete information without conflating temporary suppression with permanent erasure. Finance illustrates the idea: knowledge useful under one market regime may become harmful under another yet regain relevance when similar conditions recur.

</details>


### 110. PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance

- **Authors:** Rabimba Karanjai, Yang Lu, Richard Williamson, Hemanth Hm, Prakhar Mehrotra, Lei Xu,  Weidong,  Shi
- **Published:** 2026-08-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17220v1](http://arxiv.org/abs/2608.17220v1)
- **PDF:** [https://arxiv.org/pdf/2608.17220v1](https://arxiv.org/pdf/2608.17220v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous AI agents are emerging as interfaces for decentralized finance (DeFi) actions such as swaps, lending operations, and yield management. Because these agents rely on large language models (LLMs) to plan transactions, they inherit the LLM's susceptibility to prompt injection and lack of mechanisms to bind a verifier's approval to the exact transaction ultimately submitted on-chain. We present PACE (Policy-Attested Contract Execution), a transaction-level authorization framework that interposes between an LLM-based agent and on-chain execution. PACE introduces typed transaction intents, a deterministic policy verifier, and signed Policy Decision Records (PDRs) that cryptographically bind the approved intent, policy, and simulation report to the exact execution bytes, with replay and expiration protection. A Solidity smart account enforces PDR signatures on-chain with a measured overhead of 29,826-31,822 gas. We evaluate PACE against six baselines on 40 tasks spanning four attack categories plus benign utility (2,800 trials, 10 seeds). In our deterministic sandbox, PACE achieves a 0.00 unsafe execution rate and 0.00 false-positive rate on benign tasks, compared to 0.80 for the unguarded baseline. Ablation studies identify permissive policy settings (+57.5 pp) and the touched-contract allowlist (+12.5 pp) as the dominant safety components. To test whether the same deterministic floor holds for real model outputs, the artifact additionally provides a three-model live-LLM evaluation over the full task suite with repeated runs. A mainnet-fork harness is included for archive-RPC deployments, but fork results are reported only when the corresponding artifacts are generated. These auxiliary studies are separate from, and never substitute for, the deterministic benchmark. We frame our claims as logic-level safety within a reproducible benchmark rather than deployment-ready DeFi security.

</details>


### 111. Graphectory Viewer: A Tool for Process-Centric Analysis of Agentic Software Trajectories

- **Authors:** Charlie Jyu, Shuyang Liu, Reyhaneh Jabbarvand
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17195v1](http://arxiv.org/abs/2608.17195v1)
- **PDF:** [https://arxiv.org/pdf/2608.17195v1](https://arxiv.org/pdf/2608.17195v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present Graphectory Viewer, a web-based tool for interactive, process-centric analysis of software-agent trajectories. Building on the Graphectory representation introduced in our previous work, Graphectory Viewer transforms heterogeneous raw trajectories into phase-aware graphs that connect low-level execution details with higher-level behavioral structures. The tool supports trajectories from multiple agent frameworks and provides interactive graph construction; node-level inspection of thoughts, actions, and observations; search and filtering over large trajectory collections; and Sankey-style summaries of problem-solving phase transitions. These capabilities enable researchers and practitioners to inspect individual executions, identify recurring behavioral patterns, compare successful and failed runs, and analyze large trajectory corpora beyond final task outcomes. To support reproducibility and further research, we release Graphectory Viewer as an open-source artifact together with documentation, precomputed graphs, and the large-scale trajectory corpus.

</details>


### 112. Token Optimization and Context Window Management in Multi-Agent AI Workflows

- **Authors:** Dvir Shamay
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17188v1](http://arxiv.org/abs/2608.17188v1)
- **PDF:** [https://arxiv.org/pdf/2608.17188v1](https://arxiv.org/pdf/2608.17188v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent AI workflows are limited not only by model quality but by token cost, latency, and context-window quality. This paper presents a practitioner framework for token optimization and context-window management, grounded in an internal production dashboard that extracts structured work items from meetings, email, and chat with LLMs and routes summaries across workstreams. Six patterns are described: context stratification, fetch-once/process-locally architecture, schema-contracted prompts, token-aware fallback chains, semantic caching, and inter-agent communication compression. In production they cut measured cold-load latency to 61-116 seconds (six timed runs) from an operational baseline of roughly 3.5-10.5 minutes, with an estimated 60-70% token reduction. It also reports a controlled context-composition study: 2,420 confirmatory trials across 11 model configurations, using 661 anonymized workplace items scored for relevance. Holding the prompt at a fixed ten items, replacing some high-relevance items with same-domain low-relevance items improves the model's relevance-score concordance on the target items, versus high-relevance items only; we call this relevance-contrast context. In the all-11 paired analysis, the 50:50 signal/noise condition improved relevance accuracy by +0.077 over the 100% condition (naive 95% CI [+0.056, +0.098], Cohen's d = 0.49, Holm-adjusted p < .001, n = 220). These cells are not independent; by the nine model families the effect is +0.084 (95% interval [+0.064, +0.103]), reported as a within-corpus descriptive comparison, not a population inference. A Fusion-of-N follow-up found that learned synthesis did not beat the mechanical set union of item IDs. The contribution is a measured engineering layer between model research and production agent practice: repeatable patterns and evaluation methods for faster, cheaper, more reliable workflows.

</details>


### 113. Synthesizing Feature Extractors: An Agentic Approach for Algorithm Selection

- **Authors:** Hai Xia, Carlos Ansótegui, Stefan Szeider
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17170v1](http://arxiv.org/abs/2608.17170v1)
- **PDF:** [https://arxiv.org/pdf/2608.17170v1](https://arxiv.org/pdf/2608.17170v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Algorithm selection for constraint satisfaction problems requires extracting features that capture problem structure. Manually designing feature extractors demands deep domain expertise and quickly becomes a bottleneck when new problem classes appear. We present an automated approach that uses Large Language Models (LLMs) in an agentic check--fix--verify loop to synthesize executable Python scripts that act as interpretable, problem-specific feature extractors. Given a high-level MiniZinc model and an instance, the LLM agent generates code that constructs a typed graph representation and computes structural properties such as graph density, variable clustering, and constraint tightness. We evaluate our approach on three combinatorial problems (vehicle routing, car sequencing, fixed-length error-correcting codes) with a portfolio of five state-of-the-art solvers. The synthesized extractors yield algorithm selectors that consistently outperform both expert-curated mzn2feat features (up to $8.3$ percentage points (pp) test-set accuracy on FLECC) and the best transformer-based trans2feat variants. In the meanwhile, the synthesized feature extractors remain inspectable.

</details>


### 114. KernelArc: A Multi-Agent Framework for GPU Kernel Optimization

- **Authors:** Joyjit Kundu, Ben Stoffelen, Kaili Wang, Peter Vrancx, Ludovic Denoyer
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17071v2](http://arxiv.org/abs/2608.17071v2)
- **PDF:** [https://arxiv.org/pdf/2608.17071v2](https://arxiv.org/pdf/2608.17071v2)
- **Categories:** cs.AI, cs.MA, cs.PF


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present KernelArc, a multi-agent framework for autonomous GPU kernel optimization across heterogeneous workloads. Strategy-specialized agents run in parallel and coordinate through conclusions-only shared memory, a deterministic benchmark guard, and read-only cross-agent state with plateau-triggered drafting. We evaluate KernelArc on NVIDIA H100 and B200 GPUs using category-representative SOL-ExecBench workloads. The resulting implementations span custom BF16 GEMM, static cuBLASLt Expert-API configuration tables, fused mixture-of-experts backward, shape-gated decoder-layer fusion, native NVFP4 grouped-query attention, and paged prefill attention. In the public SOL-ExecBench leaderboard snapshot recorded on August~20, 2026, KernelArc ranked first on every representative L1, L2, Quantization, and FlashInfer task evaluated. The trajectories support the paper's central motivation: shared multi-agent search can broaden exploration and reach stronger incumbents within a fixed candidate budget, while the value of individual coordination features depends on the kernel and optimization stage.

</details>


### 115. Institution-Specific LLM Prompting Recovers PHI That De-identification Systems and Their Gold Standards Both Miss

- **Authors:** Daniel Palacios, Matthew Brady Neeley, Angel Adetomike Otto, Shalini Dhamodharan, John P. Woodhouse, Chi-fan Lin, Mark Zobeck, Zhandong Liu, Hyun-Hwan Jeong
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.17051v1](http://arxiv.org/abs/2608.17051v1)
- **PDF:** [https://arxiv.org/pdf/2608.17051v1](https://arxiv.org/pdf/2608.17051v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Secondary use of electronic health records requires de-identification, yet existing systems miss \emph{institutionally situated} protected health information (PHI) such as hospital abbreviations, building names, and internal codes whose status is locally determined. We ask whether large language models (LLMs) with in-context learning (ICL) can close this gap and control the precision--recall trade-off.
  On 100 annotated pediatric oncology notes (5,322 PHI spans) from Texas Children's Hospital, we benchmarked eight LLMs against two purpose-built systems (Stanford TiDE, OpenMed PII) and two pattern-based baselines. Each LLM ran under three prompts of increasing specificity: (1) a HIPAA-aligned baseline, (2) baseline plus the institutional PHI categories it missed, and (3) prompt 2 plus instructions against over-redacting clinical content. We then compared 14~multi-agent and ensemble configurations against the best single prompt, with recall the primary safety metric.
  LLMs outperformed the purpose-built systems (best F1=0.918$\pm$0.001 vs.\ TiDE 0.779), with advantages concentrated in contextual categories. Naming the missed categories recovered 79\% (48/61) of them, and discouraging over-redaction restored precision. No agentic architecture beat calibrated single-pass prompting (F1 0.906--0.907), but LLM outputs surfaced 414~candidate annotation gaps; re-annotation confirmed 227~PHI spans, against which the final prompt reached recall=0.981 (F1=0.907$\pm$0.002).
  Well-calibrated ICL resolves both the institutional PHI gap and the precision--recall trade-off in one LLM call per note. LLMs cost more to run than traditional methods, but that cost buys a way to audit the reference standard.
  LLMs are a legitimate, adaptable alternative to purpose-built de-identification systems; institution-specific prompt development should be the primary adaptation strategy.

</details>


### 116. Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory

- **Authors:** Bingxin Xu, Yuzhang Shang, Emilio Ferrara
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16889v1](http://arxiv.org/abs/2608.16889v1)
- **PDF:** [https://arxiv.org/pdf/2608.16889v1](https://arxiv.org/pdf/2608.16889v1)
- **Categories:** cs.RO, cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon robot manipulation chains many contact-rich skills into one multi-stage task. Vision-language-action (VLA) models increasingly master the individual skills, yet the chain still fails: errors compound beyond the policy's ability to correct, and one subtask silently constrains the next. A promising recipe freezes the VLA and puts an LLM agent in charge: it plans in language, moves in free space with analytic primitives, invokes the VLA only for contact-rich segments, and writes adaptation into language memory. Applied to long horizons, it breaks twice. (1) Competence comes from whole-task exploration at test time, whose cost is multiplicative in stages: if one stage needs T episodes, a K-stage task needs about T^K, and a failure does not reveal which stage caused it. (2) It has no representation of transitions: the VLA primitive carries an exit but no entry condition, so a subtask can succeed in a form its successor cannot use. We present BATON. Against (1), BATON makes the subtask the unit of exploration: each is explored in the cheap short-horizon regime and its solution stored in memory; a long-horizon trajectory is then composed from these solutions rather than discovered whole. Cost becomes additive (T*K) and every failure is attributed to a single stage. Against (2), BATON equips exploration with a transition-aware memory. Within a subtask, a verifier agent governs the invocation transition: the VLA is called only after the wrist view confirms the scene is ready. Across subtasks, a handoff transition restores an entry state disturbed by the predecessor's residue, and a lookahead transition selects the strategy whose outcome the successor can inherit. No parameters are updated. On the long-horizon benchmark RoboMemArena, BATON improves task success by 11.6% and cumulative success by 14.9% over the SoTA.

</details>


### 117. Policy Iteration with Human Feedback: Bringing Post-Training RL to In-context Learning

- **Authors:** Minh-Ha Nguyen, Cathy Shyr
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16831v1](http://arxiv.org/abs/2608.16831v1)
- **PDF:** [https://arxiv.org/pdf/2608.16831v1](https://arxiv.org/pdf/2608.16831v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Generative pretraining established reusable task representations; later work on language-based task conditioning and in-context learning showed that a fixed model could adapt its behavior from instructions and demonstrations. Policy Iteration with Human Feedback (PIHF) builds on this development and the recurrent evaluate-and-improve structure of generalized policy iteration. PIHF uses a pretrained language model as its execution substrate and moves persistent revision to a versioned natural-language policy and tool set. A language-model critic and clinical expert review complete-panel reasoning and tool-use trajectories to localize recurrent failures and form candidate revisions; the expert may reinterpret the evidence and retains authority over admission and rollback, while Recall@1 and Recall@5 validate outcomes after candidate execution.
  Across cumulative ablations and ultra-rare-disease benchmarks, a PIHF-derived policy improved Recall@1 in one proprietary executor and three open-weight executors spanning 3 to 49 billion active parameters. Gains were 32.7 percentage points for GPT-5.4 and 31.1 points for Qwen3.6-35B, a difference of 1.7 points. These results support the feasibility of using pretrained language models as fixed-weight execution substrates for expert-guided policy development in rare-disease diagnosis.

</details>


### 118. When Agents Coordinate: Measuring Coordination in Multi-Agent AI Coding

- **Authors:** Giuseppe Destefanis, Tomaso Aste
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16801v1](http://arxiv.org/abs/2608.16801v1)
- **PDF:** [https://arxiv.org/pdf/2608.16801v1](https://arxiv.org/pdf/2608.16801v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study how teams of AI coding agents coordinate while solving programming tasks. Current evaluations usually report whether the agents complete the task and how much the run costs, leaving the coordination inside the team largely unmeasured. We introduce an instrument to measure this coordination. Each run is represented as a temporal network in which agents and files are nodes, and messages, file writes, and file reads are timestamped directed edges with an associated cost. We apply this instrument to 1902 runs, each evaluated with a fixed test suite, across configurations that vary the team size, the team structure, and the file policy. The resulting networks show how coordination changes as teams grow and as the work changes. Direct messaging initially increases close to quadratically with the number of agents, with much of this growth coming from an early round of introductions. As the teams grow further, this increase levels off in the largest teams we study, where agents increasingly communicate through broadcast messages. The task also shapes the network that emerges. Work built around a shared specification produces dense, highly connected teams, while pipeline tasks produce sparse networks organised around local interfaces. Shared files can replace repeated 1-to-1 communication, cutting output tokens by about 42% at eight agents on message-heavy work, while adding overhead when files already carry the coordination. Naming one agent as coordinator creates no communication hub and provides no reliable improvement in success. We also observe an unprompted tendency for agents to seek out hidden grading material. We repeat the key experimental conditions in a sealed environment, replacing the hidden material with marked placeholder files. Across 244 additional runs, agents still reach for it in four fifths of runs, while the coordinator and file-channel findings reproduce.

</details>


### 119. Topological Attribution Distance (TAD): Revealing Segment-Level RAG Influence on LLM Output Geometry for Incident Log Analysis

- **Authors:** Reza Fayyazi, Michael Zuzak, Shanchieh Jay Yang
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16775v1](http://arxiv.org/abs/2608.16775v1)
- **PDF:** [https://arxiv.org/pdf/2608.16775v1](https://arxiv.org/pdf/2608.16775v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) are increasingly being deployed in cybersecurity operations to assist cybersecurity analysts with rapid decision-making against emerging threats. However, there is a main criteria that must be met when using LLMs in cybersecurity, that is, trust in the generated outputs. As Agentic AI is integrated into operational systems, a robust evidence attribution and provenance tracking technique is essential to trace the origins of model generations. When autonomous agents make a decision (right or wrong), the ability to trace back through the decision chain is critical, as without it, teams cannot identify which segment of the data caused the model generation. Existing methods often struggle to distinguish among complex and highly similar evidence sources, such as cyber incident logs. This reveals a key gap: current approaches do not adequately capture the holistic geometric relationship between the retrieved evidence and the generated response for reliable evidence verification. To bridge this gap, we propose Topological Attribution Distance (TAD), inspired by Topology, to characterize and capture the global geometric shape of an output and its changes against its retrieved logs. In other words, if the embeddings of a specific source log drastically changes the geometry of the model's response in the embedding space, this suggests that such log is a critical source for the model's generated response. Therefore, TAD is powered by segment-level ablation attribution to investigate incident logs of an actual cyberattack. We demonstrate how TAD finds the most attributed logs on LLM outputs in an adaptive manner. This can provide an explainable and trustworthy tracing based on each LLM's hidden state to understand how geometrically different retrieved logs influence the model generation, and provide evidence verification in cybersecurity and Agentic-AI workflows.

</details>


### 120. TDD-Agent: Test-Driven Reasoning for Code Generation

- **Authors:** Hongyue Yu, Kefan Li, Jiakun Li, Hongzheng Chai, Yuan Yuan, Rui He, Junyi Wei
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16742v1](http://arxiv.org/abs/2608.16742v1)
- **PDF:** [https://arxiv.org/pdf/2608.16742v1](https://arxiv.org/pdf/2608.16742v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have achieved remarkable progress in code generation, yet ensuring correctness in complex, repository-level tasks remains challenging. Existing approaches often use generated tests as static post-hoc validators, which limits their ability to guide implementation and may introduce misleading feedback when the tests themselves are incomplete or incorrect. In this paper, we introduce TDD-Agent, which operationalizes the test-driven development paradigm for code generation. TDD-Agent first prompts the model to generate executable tests, encouraging it to clarify expected behaviors before implementation, and then performs iterative dual-track refinement over both the generated code and tests using execution feedback. We first isolate the effect of test-first reasoning through a prompt variant TDD-prompt on LiveCodeBench, where it consistently improves upon reasoning-based prompting baselines. Building on this finding, we evaluate the full TDD-Agent framework on RepoEval, a repository-level benchmark, and show that it consistently outperforms retrieval-based and agent-based baselines. Additional analyses show that iterative refinement improves not only code correctness but also the effectiveness of the generated tests, yielding higher pass rates, coverage, and mutation scores, suggesting that tests can serve as evolving reasoning artifacts rather than fixed validators. Our source code is available at https://anonymous.4open.science/r/TDD-Agent-Framework-6370/.

</details>


### 121. Semantic Bandits: In-Context Exploration-Exploitation is Biased by Semantic Priors

- **Authors:** David Eric Austin, Kaheer Suleman, Jackie Chi Kit Cheung
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16707v1](http://arxiv.org/abs/2608.16707v1)
- **PDF:** [https://arxiv.org/pdf/2608.16707v1](https://arxiv.org/pdf/2608.16707v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as decision-making agents in settings that require sophisticated environmental exploration. However, existing work has raised questions about how LLMs actually balance exploration and exploitation. Unlike classical agents, LLM agents engage with tasks through natural language, exposing them to semantic information with no formal counterpart in the task structure. We introduce the semantic bandit, an extension of the multi-armed bandit setting that explicitly considers the textual labels assigned to actions, and use it to study how semantic priors --- inductive biases arising from associations between language and expected reward learned during pre-training, shape LLM exploration behaviour. We find that semantically informative action labels reduce exploration in favour of exploitation, improving performance when aligned with the reward structure and severely degrading it when misaligned. We further find that negative rewards trigger substantially more exploration than equivalent positive rewards, consistent with an expected-scale bias induced by reward conventions common in pre-training data. Overall, we argue that the use of language to define the environment and rewards introduces unavoidable biases derived from the fact that the model is trained on word co-occurence, with implications for the reliability and robustness of LLM agents in real-world decision-making settings.

</details>


### 122. Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies

- **Authors:** Shaolong Chen, Yanlin Fei, Nazhou Liu, Xinmiao Yu, Lei Li, Rahul Thapa, Madalina Ciobanu, Qingqing Mao, Ritankar Das
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16645v2](http://arxiv.org/abs/2608.16645v2)
- **PDF:** [https://arxiv.org/pdf/2608.16645v2](https://arxiv.org/pdf/2608.16645v2)
- **Categories:** cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Can a language model recover the true research idea of a published paper when given only that paper's pre-publication bibliography? We introduce Reconstruction, a blind idea-recovery benchmark that withholds the seed paper and all contemporaneous or future literature, and asks models to propose hypotheses that an independent large language model judge matches against the held-out ground-truth idea. A strict anti-leakage protocol-temporal citation cutoff, anonymous reference IDs, and frozen per-paper bibliographies, which prevents prompt-time leakage of the seed idea. Across six scientific domains and 643 evaluated papers, seven frontier models achieve only modest Match rates (approx. 3-15%). We then evaluate a reference-only multi-agent (top 4) pipeline that combines cross-model review with a Swiss tournament over aligned hypothesis slots, without external web search. Cross-model review plus tournament selection raises Match rates to approx. 23-42% across all six domains, which is an observed approx. 2.4x lift over the best single-model baseline. This draft reports the protocol, anti-leakage design, and current results as an arXiv timestamp.

</details>


### 123. Palmyra x6 Technical Report: An Agentic, Tool-Use Model Post-Trained via Anchored Supervised Fine-Tuning

- **Authors:** Peng Du, Kiran Kamble, Rakshith Vasudev, Zhizhuo Yang, Rohith Nadimpally, Arjun Krishna, Waseem Alshikh, Daniel M. Bikel
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16620v2](http://arxiv.org/abs/2608.16620v2)
- **PDF:** [https://arxiv.org/pdf/2608.16620v2](https://arxiv.org/pdf/2608.16620v2)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Palmyra x6 is a large language model optimized for use with enterprise-oriented agentic tasks. The model was built by post-training a Mixture-of-Experts base model with Anchored Supervised Fine-Tuning on a compact corpus of verified, synthetic tool-use trajectories, optimized with a Muon + Adam hybrid. The recipe is deliberately conservative and deliberately controlled: 626 trajectories, a single epoch, a low learning rate, and a KL anchor to the frozen base. The model shows substantial gains over the previous default model for Writer Agent, and compares favorably with several recent models on public benchmarks, scoring the highest on BFCL Core at $0.785$ and posts the highest six-benchmark mean of the cohort. Furthermore, the model has shown itself to be competitive or leading relative to comparators in our bias and safety evaluations.

</details>


### 124. Physics of Agents: Statistical Mechanics Predicts Collective Behavior of AI Agents

- **Authors:** Batu El, Jinhee Paeng, Fatih Dinc, Shiye Su, Mete Erdogan, Aneesh Pappu, Haotian Ye, Wanjia Zhao, Surya Ganguli, James Zou
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16578v1](http://arxiv.org/abs/2608.16578v1)
- **PDF:** [https://arxiv.org/pdf/2608.16578v1](https://arxiv.org/pdf/2608.16578v1)
- **Categories:** cs.AI, cs.MA, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly operate as part of interacting systems rather than in isolation. As agents exchange information and jointly make decisions, their interactions can improve collective reasoning but may also produce herding, polarization, or amplify shared biases. Understanding and predicting these collective dynamics is therefore important for designing effective and aligned multi-agent systems. Here, we study over 10,000 communities of language-model agents that repeatedly exchange messages and revise their opinions across objective mathematics questions and subjective political statements. Despite substantial diversity in possible behavior, the individual and group dynamics can be represented by three characteristic regimes: indifference, polarization, and consensus. AI agents start indifferent and build conviction as they interact. On objective questions, communication improves collective accuracy, while on subjective questions it often drifts group opinions toward the right in the political spectrum. We explain these observations with a statistical-mechanics formalism in which agents stochastically favor lower social pressure. Given only initial opinions, our model predicts individual trajectories, outperforms all standard baselines, generalizes to unseen community graphs, and reproduces the observed group archetype distributions. Our fitted model parameters reveal the mechanics underlying our key observations: i) communities operate below the critical social temperature, which explains conviction buildup; ii) attractive ties outweigh repulsive ones, which favors consensus; and iii) agents holding the correct answer exert the strongest pull, which drives truth-seeking. Overall, our results demonstrate that collective behavior of AI agents, like that of other complex systems, follows compact and predictive dynamical laws.

</details>


### 125. VCE-Skill: Enhancing Skill Self-Evolution with Version-Change Experience

- **Authors:** Jianming Chen, Xuanbin Ye, Yawen Wang, Junjie Wang, Qing Wang, Fanjiang XU
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16544v1](http://arxiv.org/abs/2608.16544v1)
- **PDF:** [https://arxiv.org/pdf/2608.16544v1](https://arxiv.org/pdf/2608.16544v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agents increasingly rely on reusable skills to encode task knowledge, tool-use procedures, and validation rules. Existing skill self-evolution methods primarily revise skills using execution trajectories collected from current tasks, leaving the evolution knowledge accumulated in public skill version histories largely untapped. Our pilot study reveals a clear complementarity between the two sources: public skill changes provide reusable evolution priors, whereas trajectories provide evidence grounded in the current task. Motivated by this, we propose VCE-Skill, which distills noisy and implementation-specific public skill changes into reusable, structured version-change experience and adaptively fuses it with trajectory-derived proposals from the base evolver, thereby exploiting external experience while retaining task-specific evidence. Extensive experiments demonstrate that VCE-Skill improves skill self-evolution, increasing mean scores by 3.20--4.98 points; transfer experiments further show that the resulting skills achieve stronger cross-model transfer performance. Our work highlights public skill version changes as a previously underexplored yet effective source of prior knowledge and advances trajectory-driven skill self-evolution.

</details>


### 126. HaReCAP: Habitual-action Grounding for Recursive Large Language Model Agents

- **Authors:** Shen Liu, Zhenguo Xu, Shaopu Wang, Yike Gao, Chunlei Wang
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16447v1](http://arxiv.org/abs/2608.16447v1)
- **PDF:** [https://arxiv.org/pdf/2608.16447v1](https://arxiv.org/pdf/2608.16447v1)
- **Categories:** cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon embodied tasks require LLM agents to iteratively decompose high-level goals, revise plans in response to environmental feedback, and ground leaf-level subgoals into valid executable actions. Recursive context-management methods such as ReCAP improve planning stability through multi-level task decomposition and parent-node refinement, but still repeatedly invoke the LLM at leaf nodes to ground atomic subtasks into exact valid actions. We refer to this final grounding step as last-mile grounding redundancy, which accumulates into substantial LLM-call and token overhead during long-horizon execution. To mitigate this issue, we propose HaReCAP (Habitual-action Grounded ReCAP), a low-intrusion leaf grounding extension for ReCAP. HaReCAP extracts frequent leaf decisions from successful trajectories and compiles them offline into auditable and abstainable one-step leaf-reflex rules. At runtime, it skips the leaf LLM call only when a rule can uniquely determine a legal action in the current valid-action set; otherwise, it falls back to the original ReCAP. This design avoids repeatedly carrying the full recursive context into the LLM for routine leaf action grounding, while preserving the original recursive control flow. We evaluate HaReCAP on Robotouille and ALFWorld with Qwen3.5-27B as the main model. On tasks solved by both ReCAP and HaReCAP, HaReCAP reduces token consumption by 14.67%, 17.93%, and 20.08% on Robotouille synchronous, Robotouille asynchronous, and ALFWorld, respectively. The results show that HaReCAP can serve as a low-intrusion extension to ReCAP-style recursive context-management frameworks, reducing last-mile grounding redundancy across environments and models on commonly successful trajectories.

</details>


### 127. D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding

- **Authors:** Hao Zhang, Longrong Yang, Lunhao Duan, Ziyang Wang, Qing-Guo Chen, Shanshan Zhao
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16417v1](http://arxiv.org/abs/2608.16417v1)
- **PDF:** [https://arxiv.org/pdf/2608.16417v1](https://arxiv.org/pdf/2608.16417v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-modal retrieval-augmented generation (RAG) is a key technique for visually rich long document understanding. Existing multi-modal RAG methods are progressively advancing toward multi-agent systems: they first retrieve relevant pages based on a query, and then iteratively understand information within those pages. However, these methods typically rely on fixed workflows and lack the ability to dynamically scale computation at test time, often leading to insufficient evidence. To address this, we propose D2-ScaleAgent, an agentic framework that introduces a dual-dimensional scaling paradigm for retrieval and reasoning. The core of D2-ScaleAgent is a Verifier agent-driven dynamic routing loop based on the intrinsic difficulty of the query, centered around a continuously updated evidence bank that serves as the agent's dynamic working memory: when retrieval needs to be expanded, the agent routes outward (retrieval scaling), decomposing the query into attributes and performing parallel page retrieval, followed by adaptive pruning to ensure comprehensive evidence coverage. When fine-grained reasoning is required, the agent routes inward (reasoning scaling), dynamically selecting sub-agents with varying granularity and count to extract evidence from pages. Finally, D2-ScaleAgent achieves logical closure over the evidence chain. Extensive experiments demonstrate that D2-ScaleAgent is effective on long and visually rich document benchmarks like MMLongBench-Doc, LongDocURL, etc.

</details>


### 128. Towards Risk-free AI Agent Deployment

- **Authors:** Yintong Huo, Rangeet Pan, Abhik Roychoudhury
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16411v1](http://arxiv.org/abs/2608.16411v1)
- **PDF:** [https://arxiv.org/pdf/2608.16411v1](https://arxiv.org/pdf/2608.16411v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents are rapidly moving from research prototypes into the core business processes of organizations, but these agents pose deployment risks to security, compliance, and functionality. In this article, we argue that risk-free deployment must be grounded in the agent's trajectory: the recorded sequence of reasoning steps, tool invocations, and environmental observations. Trajectories are available for any agent, and many failures are visible only in the trajectory. To make agents deployable and sustainable, we advocate agent testing and debugging as a systematic research direction for detecting and mitigating these risks. This article begins with the challenges of testing agents, including the oracle problem, non-determinism, trajectory validation, and the absence of adequacy metrics. We then turn to debugging agents, from automated failure attribution to repair and self-evolution. We distill these directions into a practical deployment-readiness checklist covering the full deployment lifecycle. Finally, we identify open problems, i.e., formal adequacy metrics, root-cause attribution over long-horizon trajectories, and the reliability of self-evolving agents, that the community must address to enable trustworthy agent deployment.

</details>


### 129. A Policy Algebra for Trust-Preserving Agentic AI Execution

- **Authors:** Bhaskar Tripathi, Anurag Kumar, Ramendra Kumar, Bhavesh Gadhe
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16402v1](http://arxiv.org/abs/2608.16402v1)
- **PDF:** [https://arxiv.org/pdf/2608.16402v1](https://arxiv.org/pdf/2608.16402v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model-based agentic frameworks primarily optimize capability: whether an agent can reason, retrieve information, call tools, delegate work, and complete a goal. Enterprise execution requires a stronger property. A successful result is not reliable if it was produced through unauthorized data access, widened delegated authority, unapproved side effects, unrecoverable budget consumption, or incomplete evidence. This paper defines reliable capability as a path property: an agent is reliably capable only when it completes a task through action events that remain admissible under identity, profile, tool, data, memory, budget, artifact, approval, and audit constraints. We propose a policy algebra that defines the reliability envelope within which agent capability may be exercised. Security profiles and runtime obligations compose through joins, intersections, budget narrowing, approval inheritance, and evidence accumulation; the resulting composition is both trust-preserving and the least restrictive state satisfying all governing inputs. The algebra also propagates restrictions across multi-agent calls and introduces cost-aware artifact materialization, which redirects open-ended execution toward a recoverable outcome as budget exposure grows. The evaluation is interpreted as a reliability-capability trade-off rather than a capability benchmark: the policy-algebra runtime intervenes on 94.8% of policy-violating events while retaining an 86.9% task-completion rate, eliminates the observed profile-monotonicity and zero-artifact-exhaustion violations, and increases audit completeness to 98.6%. The method provides researchers and practitioners with formal correctness conditions, executable decision semantics, and trace evidence for building agents that are not only capable, but reliably capable.

</details>


### 130. MELD: A Protocol for Merging Knowledge Across Distributed Agentic Memories

- **Authors:** Lauri Lovén, Jaakko Sauvola, Jukka Riekki, Sasu Tarkoma
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16357v1](http://arxiv.org/abs/2608.16357v1)
- **PDF:** [https://arxiv.org/pdf/2608.16357v1](https://arxiv.org/pdf/2608.16357v1)
- **Categories:** cs.DC, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents share a transport and can call each other's tools, but they cannot share what they know: no protocol lets two agents' memories reconcile a fact phrased two ways, link related facts held apart, or reconcile contradictory knowledge without silently discarding either claim. We present MELD, a self-managing coherence mechanism for a federation of agent memories whose run-time model is the knowledge graph itself. Each brain admits every incoming claim through a five-outcome procedure (insert, merge, relate, conflict, or reject), decided from three signals (scoped claim-key identity, embedding similarity, and a natural-language-inference verdict) under context and freshness gates, and acting through exactly one auditable, authenticated Patch, the only object that mutates state. A binding onto standard publish/subscribe transport with a per-claim status CRDT keeps sovereign brains coherent in claim status without a coordinator: self-healing after partitions and under lossy routing, and self-protecting against silent rewrite by a peer, under a benign-fault model. MELD does not adjudicate truth; a detected contradiction is preserved for later adjudication, never silently resolved. On HotpotQA distractor, distributed merge is recall-non-inferior to a centralized store under a pre-specified equivalence test and recall-superior to naive union at about 11% less live storage; the merge classifier separates at AUC 0.968 with a 0.013 false-merge rate on adjudicated candidate pairs; the status CRDT reconverges in 30/30 real partition-heal trials where last-writer-wins manages 11/30; and semantic routing delivers about 3x fewer messages at matched recall. We evaluate on a real computing continuum spanning an operator-grade 5G edge, national HPC, and a local tier, with empirically calibrated thresholds.

</details>


### 131. AeroCopilotBench: A Two-Tier Benchmark for Evaluating LLM Agents as Aviation Copilots in an Interactive Virtual Cockpit Environment

- **Authors:** Yuchen Yuan, Zhenghuang Wu, Yuangan Li, Liang Ma, Ke Li
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16349v1](http://arxiv.org/abs/2608.16349v1)
- **PDF:** [https://arxiv.org/pdf/2608.16349v1](https://arxiv.org/pdf/2608.16349v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents may assist flight crews with complex decisions and task execution, but existing aviation evaluations centered on static knowledge do not support systematic testing of procedural execution and safety compliance in interactive environments. This paper presents the AeroCopilot Operational Environment (ACOE), a reproducible interactive virtual-cockpit test environment, and AeroCopilotBench, a two-tier aviation agent evaluation benchmark. Tier-1 evaluates aviation knowledge using 1,200 multiple-choice questions, while Tier-2 comprises 73 emergency and abnormal tasks derived from the manufacturers' Pilot's Operating Handbooks (POHs) and instantiated in ACOE. ACOE converts natural-language procedures into executable state transitions, final-state goal conditions, and hard safety constraints, enabling models to interpret cockpit state, diagnose faults, and operate aircraft systems through standardized tool interfaces. We establish a safety-gated evaluation framework in which a trajectory succeeds only when all task goals are achieved without violating any hard safety constraint, while safe goal progress and trajectory safety are measured separately. Across 12 models, the highest Tier-2 success rate is 72.6%, while static knowledge performance does not consistently translate into procedural execution. Analysis of 451 failed episodes from 3 representative models identifies recurring failures in procedural completeness, use of state feedback, and long-horizon execution management. These findings motivate state-aware agent orchestration, joint assessment of task completion and trajectory safety, and repeated regression testing. ACOE and AeroCopilotBench provide a reproducible foundation for testing knowledge application, interactive execution, and operational safety in aviation agents.

</details>


### 132. CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills

- **Authors:** Mingxiao Liu, Zhoumian Jiang, Jianan Ma, Jian Zhang, Jialuo Chen, Xinhao Deng, Zhen Wang
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16246v1](http://arxiv.org/abs/2608.16246v1)
- **PDF:** [https://arxiv.org/pdf/2608.16246v1](https://arxiv.org/pdf/2608.16246v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous AI agents tackling Long Horizon Tasks depend on marketplace skills that are certified one at a time: a scanner returns a safety verdict for each skill and declares the ecosystem safe if every package passes. We show that this assumption fails under skill composition. A skill may pass the per-skill scanner individually yet participate in a risky composition when an agent connects its outputs, capabilities, or side effects with those of other scanner-passing skills. This makes skill composition risk a path level property rather than a node level property, explaining why existing skill scanners that inspect individual packages achieve limited interception. To study this threat, we present CompoSkill, a framework that constructs skill composition attacks through a dual attacker system. The white-box attacker knows the victim's installed skill pool and directly injects explicit skill-id sequences; the black-box attacker knows only a role profile, downloads the top marketplace skills for that scenario, builds a Skill Composition Graph, and searches for high risk chains whose implicit lures never name skill identifiers. We further construct CompoSkill-Bench, a benchmark of 1,140 records built from long-horizon professional workflows across five threats and six scenarios on OpenClaw and Nanobot. CompoSkill achieves risk Chain Formation Rates (CFR) up to 83.3% in the white box setting and 80.6% in the black box setting, while existing skill scanners block only a limited fraction of the risky compositions. Finally, we observe a bridge-bonus-then-hop-decay pattern: a bridge skill can increase attack success, but Attack Success Rate (ASR) decreases once additional hops make the risk chain longer than three skills. These results expose a systematic gap in single skill certification for autonomous AI agents.

</details>


### 133. LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents

- **Authors:** Xingjun Wang, Gongsheng Li, Qi Fan, Yunlin Mao, Luyan Su, Yingda Chen
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16185v2](http://arxiv.org/abs/2608.16185v2)
- **PDF:** [https://arxiv.org/pdf/2608.16185v2](https://arxiv.org/pdf/2608.16185v2)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly answer questions over dynamic raw-document collections, where files may change before preprocessing, and relevant evidence (spans, sections, pages, or tables) is query-dependent. Existing retrieval-augmented approaches pre-materialize evidence via fixed chunking, embeddings, or persistent indexes: effective for lookup, yet costly, stale-prone, and committed to a granularity before the query is known.
  We formulate in-context search as Budgeted Evidence Localization over a latent evidence space induced by dynamic raw documents and propose LENS (Latent Evidence Exploration and Search), an index-free framework. Instead of pre-materializing the evidence space, LENS maintains a query-conditioned belief over candidate units, iteratively selecting candidates via complementary lexical, local, and exploratory proposal policies, updating the belief via an LLM relevance oracle, and narrowing toward high-posterior regions under a controllable budget. Evidence is consolidated into compact, source-grounded regions of interest and compressed into self-organizing knowledge clusters reused across related queries.
  On a controlled 500-question evaluation with matched corpus snapshots, LENS reaches 62.4% exact match and 84.8% evidence recall vs. 65.2% exact match but 50.4% evidence recall for a ReAct-style baseline. Across scales, LENS gives the strongest supporting-fact localization and answer grounding. On a fixed 150-question fullwiki subset over the raw Wikipedia dump with zero indexing, LENS and ReAct are nearly tied in official answer quality (43.3% vs. 42.7% EM), with LENS grounding more answers in retrieved evidence (84.0% vs. 70.7%). A no-retrieval Closed-Book reference highlights the contribution of model memory. LENS is query-ready after corpus changes, needs no preprocessing or persistent index, and preserves source-grounded evidence localization throughout.

</details>


### 134. Agent-Native Telemetry: Verifiable State-Delta Evidence for Autonomous Operations

- **Authors:** Jun He, Deying Yu
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16178v1](http://arxiv.org/abs/2608.16178v1)
- **PDF:** [https://arxiv.org/pdf/2608.16178v1](https://arxiv.org/pdf/2608.16178v1)
- **Categories:** cs.DC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Operational telemetry is predominantly engineered for human reading: systems repeatedly serialize verbose prose, static keys, and redundant context across billions of log lines. As autonomous AI agents become primary operational consumers, feeding them traditional logs wastes scarce context capacity parsing lexical syntax rather than reasoning over system state changes -- all while lacking cryptographic guarantees of provenance or collection completeness.
  This paper introduces agent-native telemetry, an operational evidence architecture for autonomous machine operators founded on verifiable state deltas rather than human prose. We present the Agent Telemetry Protocol (ATP) and the State-Delta Evidence Ledger, an implementation that structures operational facts into four core evidence primitives (Transitions, Observations, Relations, and State Checkpoints) governed by content-addressed schemas, while isolating uncurated text as digest-verified opaque references. Producers sign and hash-chain batches for atomic collector append. Verified records feed two parallel agent access paths: a stateless protocol decoder emitting compact positional rows, and a stateful semantic gateway serving bounded graph capsules. We prove an information-preservation lower bound and formalize a ledger-relative verified negative theorem for provable event non-occurrence. On distributed microservice benchmarks (AIOpsLab and OpenTelemetry Astronomy Shop), ATP reduces raw wire payload and modeled cloud query scan costs by 96.4% relative to OpenTelemetry JSON, reduces LLM context tokens by 88.8% and query operations by 66.2%, detects all 500 tested adversarial storage mutations, and yields zero successful prompt injections across 50 adversarial trials per ATP configuration.

</details>


### 135. QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents

- **Authors:** Heng Wang, Yifei Li, Lingling Zhang, Pengyu Li, Xinyu Che, Xinyu Zhang, Zesheng Yang
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16168v1](http://arxiv.org/abs/2608.16168v1)
- **PDF:** [https://arxiv.org/pdf/2608.16168v1](https://arxiv.org/pdf/2608.16168v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly use external memory systems to support personalization by drawing on long and evolving interaction histories, in which user preferences may be distributed across time, change with context, and conflict with earlier evidence. However, existing systems face three limitations: fixed-turn, fixed-token, or session-based boundaries can mix unrelated dialogue or split an event from its causes, decisions, and outcomes; storing multiple pieces of user information from the same interaction as a single memory binds together items that serve different functions and should be independently retrievable; and treating the current task as a single top-$k$ retrieval query can return fragments that are individually relevant but fail to jointly capture preference evolution, temporal validity, and contextual applicability. We introduce \textsc{QUMem}, a structured memory framework for query-conditioned user-state inference. \textsc{QUMem} first segments interaction histories into variable-length episodes according to semantic continuity, then decomposes each episode into independently retrievable factual, preference, and transferable insight memories while preserving temporal positions and source evidence. At inference time, three sequential agents identify task-specific information needs, plan multi-query retrieval over the typed memory stores, and jointly infer a temporally and contextually valid user state for downstream response generation. \textsc{QUMem} achieves state-of-the-art performance on both PersonaMem and KnowU-Bench, demonstrating the effectiveness of query-conditioned user-state inference for long-term personalization.

</details>


### 136. TRCA: Transition-wise Rubric Credit Assignment for Long-horizon LLM Agents

- **Authors:** Huan Zhang, Mingju Chen, Dongxu Zhou, Can Lv, Heng Chang, Sen Cui, Faguo Wu, Shiji Zhou
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16156v1](http://arxiv.org/abs/2608.16156v1)
- **PDF:** [https://arxiv.org/pdf/2608.16156v1](https://arxiv.org/pdf/2608.16156v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon large language model (LLM) agents are typically optimized with sparse terminal outcomes, making fine-grained credit assignment across multi-step interactions difficult. Existing approaches either rely on process evaluators, which incur annotation and inference costs, or derive step-level credit from successful trajectories. However, successful trajectories are extremely scarce during early-stage reinforcement learning, substantially weakening anchor-based methods. We propose Transition-wise Rubric Credit Assignment (TRCA), which derives step-level supervision directly from action-induced transitions without learned evaluators or successful anchors. TRCA evaluates each transition using Evidence, Execution, and Invalidity rubrics to capture task-relevant information acquisition, valid task execution, and invalid or regressive behavior. From these judgments, Foundational Rubric Reward measures local transition quality, while Breakthrough Rubric Reward tracks newly covered Evidence and Execution conditions to reward incremental task progress. Combined with terminal outcomes, these signals produce fine-grained step-level advantages for policy optimization. Experiments on ALFWorld, WebShop, and seven search-augmented question-answering benchmarks show consistent improvements over the evaluated baselines. With Qwen2.5-7B-Instruct, TRCA improves the WebShop score by 6.0%-12.6%; with Qwen2.5-3B-Instruct, it improves the average SearchQA score by 1.9%-18.3%. These results demonstrate the effectiveness of transition-wise rubric credit assignment for long-horizon tasks with sparse successful anchors.

</details>


### 137. FeatureHospital: A Skill-Driven Multi-Agent Framework for Automated Algorithm Customization in Multi-View Multi-Label Feature Selection

- **Authors:** Junxuan Li, Zhiqi Chen, Yuzhou Liu, Peng Zhang, Huaxiao Liu
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16148v1](http://arxiv.org/abs/2608.16148v1)
- **PDF:** [https://arxiv.org/pdf/2608.16148v1](https://arxiv.org/pdf/2608.16148v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-view multi-label feature selection aims to identify a compact and informative feature subset from heterogeneous views while preserving discriminative information for multiple labels. Existing methods are generally developed from specific modeling perspectives and incorporate mechanisms tailored to particular data characteristics. Designing suitable feature selection algorithms across datasets with diverse and heterogeneous characteristics still relies heavily on expert knowledge and substantial manual effort, imposing considerable time and labor costs that severely hinder the practical adoption of feature selection. To address this problem, we propose FeatureHospital, a Skill-driven multi-agent framework for automated multi-view multi-label feature selection algorithm design. FeatureHospital first diagnoses the target dataset to identify its feature selection issues. Based on the diagnosis, specialist agents equipped with domain Skills then prescribe corresponding optimization strategies and Loss terms for different issues. After that, the resulting prescriptions are reconciled to remove overlaps and resolve conflicts before being integrated into a compact dataset-specific objective. Finally, the constructed objective is optimized to select the final feature subset. Experimental results demonstrate that FeatureHospital can construct effective feature selection algorithms for different datasets based on their individual characteristics.

</details>


### 138. HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory

- **Authors:** Ruiyao Xu, Tiankai Yang, Wei-Chieh Huang
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16114v1](http://arxiv.org/abs/2608.16114v1)
- **PDF:** [https://arxiv.org/pdf/2608.16114v1](https://arxiv.org/pdf/2608.16114v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As agentic tasks grow in complexity, LLM agents increasingly rely on experiential memory to reuse procedural knowledge across tasks. Effective memory design must jointly address what to store, how memory is structured and retrieved, and how memory evolves. Existing systems tackle each only partially: they store trajectories, insights, or workflows as isolated entries, discarding compositional relationships among subtasks and reusable skills; retrieve by flat embedding similarity that ignores relational signals; and maintain memory without leveraging its relational structure. We propose HyperSkill, a hypergraph-based memory framework that jointly improves all three. HyperSkill represents memory as a hypergraph with two node types, subtask steps and reusable skills, where each hyperedge links the subtasks and skills from a single trajectory. Dual-path retrieval queries both subtask and trajectory levels, ranking skills by co-occurrence across retrieved trajectories. Periodic structure-informed maintenance prunes low-utility nodes and merges redundant skills via quality-weighted propagation. Across xBench, GAIA, and WebWalkerQA with GPT-4o and Qwen3-30B-A3B, HyperSkill outperforms ten memory baselines, yielding gains of up to +11.51 on GAIA and +11.18 on WebWalkerQA.

</details>


### 139. CAPO: Constraint-Aware Prompt Optimization for LLM Agents

- **Authors:** Victor Ye Dong, Reid Pryzant, Yi Liu, Jian Jiao
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16068v1](http://arxiv.org/abs/2608.16068v1)
- **PDF:** [https://arxiv.org/pdf/2608.16068v1](https://arxiv.org/pdf/2608.16068v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as agents that rely on system prompts to use tools and complete tasks. Such deployments impose distinct operational requirements, including appropriate tool use, concise prompts and solution paths, and compliance with safety and formatting policies. For many practitioners, however, assembling domain-specific supervised data to post-train models to meet these requirements is infeasible. We introduce CAPO (Constraint-Aware Prompt Optimization), a primal-dual method that combines pool-based rewrites with adaptive constraint weighting to optimize system prompts under explicit operational constraints. Across agentic benchmarks, CAPO more reliably reaches empirically feasible operating points while improving task performance. CAPO also generalizes beyond agentic settings, achieving strong results on assistant-style evaluations with output-format and safety/privacy constraints. We further introduce DCAPO (Dynamically Trained CAPO), which trains a feedback- and dual-conditioned rewriter with pool-based GRPO while keeping the task agent frozen. Across task agents of different sizes, DCAPO produces a feasible prompt in every evaluated domain and matches or improves the task accuracy achieved by the evaluated baselines. A surrogate analysis characterizes how finite-pool and discrete-rewrite errors enter the inexact primal-dual procedure.

</details>


### 140. From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents

- **Authors:** Zhengzhao Ma, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun
- **Published:** 2026-08-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.16002v2](http://arxiv.org/abs/2608.16002v2)
- **PDF:** [https://arxiv.org/pdf/2608.16002v2](https://arxiv.org/pdf/2608.16002v2)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reliable uncertainty quantification (UQ) is essential for deploying large language model (LLM) agents in complex interactive environments. Existing UQ methods largely rely on local signals, such as token probabilities, predictive entropy, or per-step confidence, and therefore overlook the long-range dependencies through which errors accumulate across an execution trajectory. As a result, they may fail to identify agent failures whose causes originate several reasoning or interaction steps before the final answer. We propose RUPA (Relational Uncertainty Propagation for Agents), a trajectory-level UQ framework for LLM agents. RUPA represents an execution history as a directed trajectory graph in which reasoning states, tool interactions, and environment feedback are nodes connected by temporal and semantic dependency edges. It then propagates uncertainty over this graph to capture how execution risk accumulates and transfers across interaction steps. The propagated signal is combined with trajectory-level behavioral features and goal-alignment information to produce a confidence estimate for the full agent trajectory. We evaluate RUPA on representative agent benchmarks, including $τ$-2, Terminal-Bench-2, and GAIA, using 6 open-source LLMs spanning multiple model families. Experimental results show that RUPA consistently outperforms existing UQ methods by providing more accurate uncertainty estimates, enabling earlier failure detection, and improving uncertainty-guided agent execution across diverse agent tasks. These results demonstrate that explicitly modeling relational dependency is crucial to reliable UQ for long-horizon LLM agents, providing a practical foundation for trustworthy agent execution.

</details>



## Biorxiv (2 papers)


### 1. EnSEMBLE: a framework for enhancer-anchored pathway analysis that locks in enhancer-corroborated pathways from transcriptome sequencing data for biological validation

- **Authors:** Zhang, L., Gupta, A., Wang, Y., Sharma, R., Lawal, B., Hou, G., Wang, X.-S.
- **Published:** 2026-08-21
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.17.745283](https://doi.org/10.64898/2026.08.17.745283)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background Pathway discovery methods for transcriptome sequencing return tens to hundreds of redundant gene sets, and biologists often subjectively select the pathways fitting biological expectations. What is missing is not another statistical method, but a way to corroborate each candidate pathway against an independent, mechanistic line of evidence. Results We introduce EnSEMBLE (Enhancer-Set Enrichment & Mechanism-Based Linked Evidence), a tool that corroborates gene-level pathway enrichment with an orthogonal enhancer layer drawn from the same transcriptome sequencing data: active enhancers transcribe enhancer RNAs already present in standard RNA-seq, so a pathway's regulatory state can be scored from the very run that produced the gene-level signal, at no added cost. EnSEMBLE pairs pathway enrichments with Enhancer-Program Enrichment Analysis (EPEA), collapses redundant gene sets into process-level Themes, and retains only those that a concordant enhancer program corroborates. This dual-evidence requirement reduced reported signatures by >97% (hundreds of gene sets to 3-18 claims) across four datasets spanning cancer perturbations and iPSC-to-neuron differentiation. Surviving claims recovered expected biology--mesenchymal-program collapse upon SNAI1 knockout, regulatory convergence during neuronal differentiation--and named mechanisms pathway enrichments missed, including an mTOR-MYC-SPT5 elongation axis in rapamycin-treated PANC1 cells. A language AI agent performs narrative synthesis over deterministic statistics, with reproducibility enforced by temperature-zero inference and three-run consensus. We further provide enhancer over-representation analysis (eORA), mapping non-coding GWAS variants to the same programs to recover cell-type-selective trait associations. Conclusions EnSEMBLE shifts transcriptomic interpretation from enumerating possibilities to adjudicating evidence, yielding a compact, traceable set of enhancer-corroborated claims that identify the regulatory programs driving cellular change and prioritize them for experimental validation.

</details>


### 2. PerturbTrace: Evaluating Feedback Use by AI Co-Scientist Agents in Perturbation Discovery

- **Authors:** Yu, C., Liu, S., Qiao, G., Luo, M., Xiang, Y., Xu, Z.
- **Published:** 2026-08-20
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.18.745260](https://doi.org/10.64898/2026.08.18.745260)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in AI co-scientists have brought LLM agents into closed-loop experimental design. However, whether these agents use feedback from earlier rounds to revise subsequent experimental decisions remains unclear. We address this question with PerturbTrace, which evaluates each round-to-round transition through Feedback-to-State, State-to-Action, and Action-to-Outcome. These stages assess whether feedback is reflected in the agent's rationale and perturbation-selection strategy, whether the stated strategy guides the next perturbation batch, and whether that batch yields more hits than expected under random sampling. We evaluate four LLM agents on 17 screen-derived tasks and compare them with random selection, active learning, and LLM-guided Bayesian optimization baselines. Each agent outperforms the strongest non-agent method on at least 15 of the 17 tasks, yet controlled evaluations across six tasks show no consistent advantage from true feedback over random or no feedback. Among 576 transitions under true or random feedback, only 43 (7.5%) complete the full Feedback-State-Action-Outcome sequence, including 25 under random feedback. These findings show that high final recall does not necessarily indicate effective feedback use. They also highlight the need to evaluate closed-loop scientific agents by both their discovery performance and whether feedback changes their subsequent decisions.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*