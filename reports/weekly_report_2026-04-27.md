# Weekly AI Agent Paper Report

**Generated:** 2026-04-27 11:27
**Period:** 2026-04-20 to 2026-04-26

## Summary

- **Total papers fetched:** 677
- **Papers matching keywords:** 132
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-04-20) | Change |
|--------|-----------|-----------|--------|
| Total matched | 132 | 184 | -52 |
| arxiv | 129 | 177 | -48 |
| biorxiv | 1 | 2 | -1 |
| medrxiv | 2 | 5 | -3 |

### Notable Trends

**1. Volume dip – overall & source mix**  
* **Total papers:** ↓ 52 % week‑over‑week (184 → 132).  
* **ArXiv:** down 27 % (177 → 129) – the biggest contributor to the drop.  
* **MedRxiv / bioRxiv:** both shrank sharply (medRxiv ‑ 5 → 2, bioRxiv ‑ 2 → 1), indicating fewer clinically‑oriented agent studies this week.

**2. Topic shift – from domain‑specific pipelines to meta‑evaluation & governance**  
* **Last week:** heavy on **application‑specific agent pipelines** (X‑ray analysis, radiology reporting, astro‑imaging, patent bio‑activity mining, clinical monitoring).  
* **This week:** emphasis moves to **foundations, benchmarking, and societal impact**:  
  * *Agentic World Modeling* (theory + “laws”),  
  * *Seeing the Whole Elephant* (failure‑attribution benchmark),  
  * *Superminds Test* (collective‑intelligence probing),  
  * Systematic‑review of agents in mental health (meta‑analysis rather than a new pipeline).

**3. Emerging cross‑disciplinary “meta‑agent” systems**  
* **QuantClaw** (precision tool for OpenClaw) and **MetaMuse** (metadata curation) illustrate a trend toward *agents that orchestrate or improve other AI/ scientific‑software stacks* rather than being the end‑task performer.  
* This complements the prior week’s “agentic frameworks” (e.g., ChemGraph‑XANES, MARCH) but now the focus is on **curation, harmonization, and quality‑control**.

**4. Healthcare continues but with a different angle**  
* Fewer med/bio‑preprints, yet the few that appear are **evaluation‑oriented**:  
  * *Uncertainty‑Gated Glaucoma Screening* combines semi‑supervised classification with multi‑agent LLM deliberation – a hybrid decision‑making study.  
  * *AI Agents in Mental Health* is a systematic review/meta‑analysis, signalling that the community is beginning to **assess impact** rather than just build new diagnostic agents.

**5. Benchmarking and governance are gaining traction**  
* New benchmarks (*Seeing the Whole Elephant*, *Superminds Test*) suggest a maturing field that now needs **standardized failure‑analysis and collective‑intelligence metrics**.  
* The presence of “Laws” and “Foundations” in the Agentic World Modeling title reflects growing interest in **theoretical constraints and safety** for autonomous agents.

**Bottom line:** The AI‑agent landscape is contracting in sheer output, especially on arXiv, while pivoting from domain‑specific deployment papers toward meta‑evaluation, governance, and cross‑disciplinary orchestration tools. Healthcare‑related work persists but shifts from pipeline creation to impact assessment and uncertainty handling.

---



## Biomedical Highlights (3 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


**Overview**

Across the three papers, AI agents are deployed to tackle disparate but common hurdles in biomedicine: data quality, clinical decision‑support, and the scarcity of reliable annotations.  

1. **MetaMuse** frames metadata curation as a multi‑agent problem, coupling a knowledge‑graph‑based retrieval agent, a language‑model‑driven normalization agent, and a consistency‑checking agent to automatically harmonize GEO sample descriptions; the system is evaluated on large‑scale GEO submissions, showing orders‑of‑magnitude gains in completeness and ontology alignment over manual curation.  

2. The **mental‑health review** aggregates 78 primary studies that implement LLM‑powered conversational agents for assessment, triage, or psychotherapy augmentation; meta‑analysis reveals moderate effect sizes for symptom‑rating accuracy (Cohen’s d ≈ 0.42) and patient‑engagement metrics, while highlighting methodological gaps such as limited external validation and insufficient reporting of safety‑guard mechanisms.  

3. In **uncertainty‑gated glaucoma screening**, a semi‑supervised convolutional‑network classifier first produces a confidence‑weighted OCT feature map, which is then fed to a small ensemble of specialized LLM agents that deliberate on borderline cases; the gated pipeline reduces false‑negative rates by ~15 % on an internal multi‑center cohort and provides natural‑language rationales that align with ophthalmologists’ reasoning.  

Collectively, the works illustrate a growing paradigm in which modular, reasoning‑oriented AI agents—often built on large language models—are combined with domain‑specific vision or statistical models to improve data stewardship, patient interaction, and diagnostic reliability in biomedical contexts.



### 1. MetaMuse: A Multi-Agent AI System for Biomedical Metadata Curation and Harmonization

- **Authors:** Mittal, E., Litman, E., Myers, T., Agarwal, V., Gopinath, A., Kassis, T.
- **Published:** 2026-04-20
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.04.12.718044](https://doi.org/10.64898/2026.04.12.718044)

- **Categories:** genomics


> The paper introduces **MetaMuse**, a modular, multi‑agent AI framework that automatically curates and harmonizes biomedical metadata from repositories such as GEO. The system chains large‑language‑model (LLM) agents for contextual extraction, a central orchestrator that enforces cross‑field logical consistency, and a SapBERT‑based semantic normalizer that maps free‑text values to ontology terms, deliberately opting for conservative false negatives to avoid hallucination. Evaluated on a gold‑standard GEO dataset, MetaMuse attains >95 % accuracy on key metadata fields and scales to hundreds of samples, providing an auditable, high‑integrity pipeline that advances agentic AI applications in biomedical data curation.


<details>
<summary>Abstract</summary>

Inconsistent and unstructured metadata in public biomedical repositories, such as the Gene Expression Omnibus (GEO), severely limits data discoverability and research reproducibility. To address this, we introduce MO_SCPLOWETAC_SCPLOWMO_SCPLOWUSEC_SCPLOW, a modular, multi-agent artificial intelligence framework designed to autonomously extract, validate, and standardize unstructured biomedical metadata. Operating through a three-stage architecture utilizing large language model agents, specialized CO_SCPLOWURATORC_SCPLOWAO_SCPLOWGENTSC_SCPLOW contextually extract candidate values for specific target metadata fields. A centralized AO_SCPLOWRBITRATORC_SCPLOWAO_SCPLOWGENTC_SCPLOW enforces cross-field logical consistency to prevent contradictory annotations. Finally, a NO_SCPLOWORMALIZERC_SCPLOWAO_SCPLOWGENTC_SCPLOW leveraging a domain-specific semantic search model (SapBERT) maps these free-text candidates to formal ontological terms. We evaluated MO_SCPLOWETAC_SCPLOWMO_SCPLOWUSEC_SCPLOW on a gold-standard dataset of manually curated GEO samples, achieving over 95% curation accuracy across key target metadata fields, and demonstrated robust scalability on a broader dataset of 400 samples. Notably, MO_SCPLOWETAC_SCPLOWMO_SCPLOWUSEC_SCPLOW avoids data hallucination by defaulting to conservative false negatives when evidence is ambiguous, thereby preserving strict data integrity. By providing a fully auditable and context-aware curation pipeline, MO_SCPLOWETAC_SCPLOWMO_SCPLOWUSEC_SCPLOW offers a scalable solution for enriching public data repositories and accelerating reproducible, data-driven scientific discovery.

</details>


### 2. Artificial Intelligence Agents in Mental Health: A Systematic Review and Meta Analysis

- **Authors:** Zhu, L., Wang, W., Liang, Z., Tan, W., Chen, B., Lin, X., Wu, Z., Yu, H., Li, X., Jiao, J., He, S., Dai, G., Niu, J., Zhong, Y., Hua, W., Chan, N. Y., Lu, L., Wing, Y. K., Ma, X., Fan, L.
- **Published:** 2026-04-22
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.21.26351365](https://doi.org/10.64898/2026.04.21.26351365)

- **Categories:** psychiatry and clinical psychology


> **Contribution:** The paper provides the first systematic review and meta‑analysis of AI‑driven mental‑health agents (2023‑2025), introducing a six‑dimensional audit framework that distinguishes true “agentic” systems (multi‑role, tool‑augmented, planner‑based pipelines) from the prevalent monolithic chatbot implementations.

**Methodology:** The authors extracted 202 peer‑reviewed systems, categorising each along (i) model type and workflow, (ii) data modality and provenance, (iii) ICD‑11 diagnosis focus, (iv) demographic coverage, (v) downstream clinical task, and (vi) evaluation protocol; quantitative synthesis examined prevalence of each dimension and performed meta‑analysis of reported performance and safety metrics.

**Key Findings for Agentic AI:** 1) Over 80 % of systems are single‑agent text chatbots trained on self‑report data, largely targeting depression, anxiety and suicidality, with minimal coverage of severe or comorbid disorders. 2) Only a nascent subset (~12 %) adopts multi‑agent, role‑aware architectures that link planners, retrieval modules, safety auditors and external tools, showing modest gains in personalization and safety but raising new reliability and regulatory risks. 3) Evaluation is dominated by offline or vignette‑based metrics; prospective, clinician‑in‑the‑loop or longitudinal real‑world studies are scarce, highlighting a critical gap for establishing trustworthy, deployable mental‑health AI agents. The authors recommend shifting research toward clinically grounded, privacy‑preserving multi‑agent pipelines, broader demographic representation, and rigorous real‑world validation.


<details>
<summary>Abstract</summary>

The rapid rise of large language models (LLMs) and foundation models has accelerated efforts to build artificial intelligence (AI) agents for mental health assessment, triage, psychotherapy support and clinical decision assistance. Yet a gap persists between healthcare and AI-focused work: while both communities use the language of "agents," clinical research largely describes monolithic chatbots, whereas AI studies emphasize agentic properties such as autonomous planning, multiagent coordination, tool and database use and integration with multimodal mental health data streams.

In this Review, we conduct a systematic analysis of mental health AI agent systems from 2023 to 2025 using a six-dimensional audit framework: (i) system type (base model lineage, interface modality and workflow composition, from rule-based tools to role-aware multi-agent foundation-model systems), (ii) data scope (modalities and provenance, from elicited self-report and chatbot dialogues to electronic health records, biosensing and synthetic corpora), (iii) mental health focus (mapped to ICD-11 diagnostic groupings), (iv) demographics (age strata, geography and sex representation), (v) downstream tasks (screening/triage, clinical decision support, therapeutic interventions, documentation, ethical-legal support and education/simulation) and (vi) evaluation types (automated metrics, language quality benchmarks, safety stress tests, expert review and clinician or patient involvement).

Across this corpus, we find that most systems (1) concentrate on depression, anxiety and suicidality, with sparse coverage of severe mental illness, neurocognitive disorders, substance use and complex comorbidity; (2) rely heavily on text-based self-report rather than clinically verified longitudinal data or genuinely multimodal inputs; (3) are implemented as single-agent chatbots powered by general-purpose LLMs rather than role-structured, workflow-integrated pipelines; and (4) are evaluated primarily via offline metrics or vignette-based scenarios, with few prospective, clinician- or patient-in-the-loop studies. At the same time, an emerging class of agentic systems assigns foundation models explicit roles as planners, retrieval agents, safety auditors or supervisors coordinating other models and tools. These multiagent, tool-augmented workflows promise personalization, safety monitoring and greater transparency, but they also introduce new risks around reliability, bias amplification, privacy, regulatory accountability and the blurring of clinical versus non-clinical roles.

We conclude by outlining priorities for the next generation of mental health AI agents: clinically grounded, role-aware multi-agent architectures; transparent and privacy-preserving use of clinical and elicited data; demographic and cultural broadening beyond predominantly Western adult samples; and evaluation pipelines that progress from offline benchmarks to longitudinal, real-world studies with routine safety auditing and clear governance of responsibilities between agents and human clinicians.

</details>


### 3. Uncertainty-Gated Glaucoma Screening: Combining Semi-Supervised Classification with Multi-Agent Large Language Model Deliberation

- **Authors:** Garimella Narasimha, S. V., Brown, N., Sridhar, S.
- **Published:** 2026-04-20
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.17.26351127](https://doi.org/10.64898/2026.04.17.26351127)

- **Categories:** ophthalmology


> The paper introduces a two‑stage glaucoma‑screening pipeline that first uses a semi‑supervised EfficientNetV2‑S classifier (trained with only 350 labeled OCT scans) to flag uncertain cases, then routes those cases to a multi‑agent deliberation system built on the MedGemma‑4B large language model. The uncertainty estimator reliably separates confident from ambiguous predictions (96 % vs 74 % accuracy), providing a triage signal that sends 124 ambiguous cases to three specialist agents who discuss over three rounds. On these hard cases the agents achieve 100 % sensitivity and 89.5 % overall accuracy—substantially higher than the classifier’s 73.4 %—demonstrating that uncertainty‑gated routing to LLM‑based agentic deliberation can markedly improve diagnostic performance where vision‑only models are least reliable.


<details>
<summary>Abstract</summary>

Automated glaucoma screening from optical coherence tomography (OCT) faces two persistent challenges: scarcity of expert-labeled data and unreliable model predictions on diagnostically ambiguous cases. We present a two-tier diagnostic pipeline that addresses both. In the first tier, an EfficientNetV2-S classifier trained under a semi-supervised pseudo supervisor framework achieves 0.84 AUC on 150 held-out test patients from the Harvard Glaucoma Detection and Progression dataset, using only 350 labeled training samples out of 700. In the second tier, 124 flagged cases are routed to a multi-agent system built on MedGemma 4B, where three specialist agents deliberate over three rounds before rendering a final diagnosis. On these flagged cases, the agent system achieves 100% sensitivity--detecting all 55 glaucoma cases with zero missed diagnoses--and 89.5% overall accuracy (111/124), compared to the classifiers 73.4% (91/124). Uncertainty analysis confirms that the classifiers output probability reliably separates confident predictions (96.3% accuracy, n = 27) from uncertain ones (74.0%, n = 123), producing a 22-percentage-point gap that serves as a triage signal. The agents fix 32 cases the classifier misclassifies while introducing 12 new errors, yielding a net improvement of 20 cases. These results are from a single training run without variance estimates and should be interpreted as preliminary evidence that uncertainty-gated routing to vision-language model agents can meaningfully improve diagnostic accuracy on the cases where automated classifiers are least reliable.

</details>


---



## Arxiv (129 papers)


### 1. How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks

- **Authors:** Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
- **Published:** 2026-04-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.22750v1](http://arxiv.org/abs/2604.22750v1)
- **PDF:** [https://arxiv.org/pdf/2604.22750v1](https://arxiv.org/pdf/2604.22750v1)
- **Categories:** cs.CL, cs.CY, cs.HC, cs.SE


> The paper provides the first large‑scale analysis of how much compute‑cost (LLM tokens) agentic coding systems actually consume and whether they can forecast that cost. By running eight state‑of‑the‑art models on the SWE‑bench Verified suite, the authors show that agentic tasks are dramatically more expensive than ordinary code‑chat (up to 1 000× more tokens), that most of the cost comes from input tokens, and that token usage is highly stochastic—different runs on the same problem can vary by 30× with no corresponding gain in accuracy. They further demonstrate wide disparities in token efficiency across models (e.g., Kimi‑K2 and Claude‑Sonnet‑4.5 use >1.5 M tokens more than GPT‑5 on average) and reveal that even the strongest models can only weakly predict their own consumption (correlations ≤ 0.39) and tend to underestimate it, highlighting a major gap between perceived task difficulty and actual computational effort.


<details>
<summary>Abstract</summary>

The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.

</details>


### 2. Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond

- **Authors:** Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
- **Published:** 2026-04-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.22748v1](http://arxiv.org/abs/2604.22748v1)
- **PDF:** [https://arxiv.org/pdf/2604.22748v1](https://arxiv.org/pdf/2604.22748v1)
- **Categories:** cs.AI


> The paper proposes a unified “levels × laws” framework that formalizes world‑modeling for agentic AI: **L1** predictors learn one‑step transitions, **L2** simulators compose those transitions into multi‑step, action‑conditioned rollouts that obey domain‑specific laws, and **L3** evolvers can autonomously revise their models when confronted with mismatches. By classifying the governing laws into physical, digital, social, and scientific regimes, the authors systematically map more than 400 prior works onto 12 level‑regime combinations, evaluate their methodological gaps (e.g., lack of multi‑step consistency, poor law‑adherence, limited self‑repair), and introduce decision‑centric evaluation metrics together with a minimal reproducible benchmark suite. Their analysis shows that current systems cluster at L1–L2 for physical and digital regimes, while true L3 evolvers remain scarce, especially in social and scientific contexts, highlighting concrete architectural directions and governance challenges for building agents that can not only predict but also reshape their environments.


<details>
<summary>Abstract</summary>

As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.

</details>


### 3. Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems

- **Authors:** Mengzhuo Chen, Junjie Wang, Fangwen Mu, Yawen Wang, Zhe Liu, Huanxiang Feng, Qing Wang
- **Published:** 2026-04-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.22708v1](http://arxiv.org/abs/2604.22708v1)
- **PDF:** [https://arxiv.org/pdf/2604.22708v1](https://arxiv.org/pdf/2604.22708v1)
- **Categories:** cs.MA


> The paper introduces **TraceElephant**, a new benchmark for attributing failures in LLM‑driven multi‑agent systems that provides **complete execution traces** (inputs, outputs, and contextual state) rather than the partial, output‑only logs used in prior work. By constructing reproducible environments and evaluating several attribution methods, the authors show that having full trace visibility boosts attribution accuracy by up to **76 %**, demonstrating that omitted inputs are a major source of diagnostic error. This benchmark establishes a realistic, developer‑centric evaluation platform that can drive more transparent and reliable failure‑analysis techniques for agentic AI.


<details>
<summary>Abstract</summary>

Failure attribution, i.e., identifying the responsible agent and decisive step of a failure, is particularly challenging in LLM-based multi-agent systems (MAS) due to their natural-language reasoning, nondeterministic outputs, and intricate interaction dynamics. A reliable benchmark is therefore essential to guide and evaluate attribution techniques. Yet existing benchmarks rely on partially observable traces that capture only agent outputs, omitting the inputs and context that developers actually use when debugging. We argue that failure attribution should be studied under full execution observability, aligning with real-world developer-facing scenarios where complete traces, rather than only outputs, are accessible for diagnosis. To this end, we introduce TraceElephant, a benchmark designed for failure attribution with full execution traces and reproducible environments. We then systematically evaluate failure attribution techniques across various configurations. Specifically, full traces improve attribution accuracy by up to 76\% over a partial-observation counterpart, confirming that missing inputs obscure many failure causes. TraceElephant provides a foundation for follow-up failure attribution research, promoting evaluation practices that reflect real-world debugging and supporting the development of more transparent MASs.

</details>


### 4. QuantClaw: Precision Where It Matters for OpenClaw

- **Authors:** Manyi Zhang, Ji-Fu Li, Zhongao Sun, Xiaohao Liu, Zhenhua Dong, Xianzhi Yu, Haoli Bai, Xiaobo Xia
- **Published:** 2026-04-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.22577v1](http://arxiv.org/abs/2604.22577v1)
- **PDF:** [https://arxiv.org/pdf/2604.22577v1](https://arxiv.org/pdf/2604.22577v1)
- **Categories:** cs.AI, cs.CL


> QuantClaw introduces a dynamic precision‑routing layer for OpenClaw‑based autonomous agents that automatically selects low‑precision (e.g., FP8) or higher‑precision configurations according to the difficulty of each sub‑task in a multi‑turn workflow. By profiling quantization sensitivity across a suite of realistic agent tasks, the authors show that precision needs vary dramatically, and they implement a plug‑and‑play plugin that routes “lightweight” steps to cheap quantized kernels while preserving full precision for demanding reasoning steps. In experiments on the GLM‑5 model, QuantClaw attains up to 21.4 % cost savings and 15.7 % latency reduction without degrading—and sometimes improving—task performance, demonstrating that treating precision as a mutable resource can substantially improve the efficiency of agentic AI systems.


<details>
<summary>Abstract</summary>

Autonomous agent systems such as OpenClaw introduce significant efficiency challenges due to long-context inputs and multi-turn reasoning. This results in prohibitively high computational and monetary costs in real-world development. While quantization is a standard approach for reducing cost and latency, its impact on agent performance in realistic scenarios remains unclear. In this work, we analyze quantization sensitivity across diverse complex workflows over OpenClaw, and show that precision requirements are highly task-dependent. Based on this observation, we propose QuantClaw, a plug-and-play precision routing plugin that dynamically assigns precision according to task characteristics. QuantClaw routes lightweight tasks to lower-cost configurations while preserving higher precision for demanding workloads, saving cost and accelerating inference without increasing user complexity. Experiments show that our QuantClaw maintains or improves task performance while reducing both latency and computational cost. Across a range of agent tasks, it achieves up to 21.4% cost savings and 15.7% latency reduction on GLM-5 (FP8 baseline). These results highlight the benefit of treating precision as a dynamic resource in agent systems.

</details>


### 5. Superminds Test: Actively Evaluating Collective Intelligence of Agent Society via Probing Agents

- **Authors:** Xirui Li, Ming Li, Yunze Xiao, Ryan Wong, Dianqi Li, Timothy Baldwin, Tianyi Zhou
- **Published:** 2026-04-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.22452v1](http://arxiv.org/abs/2604.22452v1)
- **PDF:** [https://arxiv.org/pdf/2604.22452v1](https://arxiv.org/pdf/2604.22452v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> The paper introduces the **Superminds Test**, a hierarchical probing framework (joint reasoning → information synthesis → basic interaction) that empirically measures society‑level intelligence in **MoltBook**, a platform of >2 M autonomous LLM agents. By deploying controlled “probing agents” to ask coordination, reasoning, and synthesis questions, the authors find that the agent society consistently under‑performs state‑of‑the‑art single‑agent models: it fails to solve complex tasks, rarely aggregates distributed knowledge, and cannot even complete trivial coordination tasks, with interaction threads remaining shallow and often off‑topic. The key conclusion is that sheer scale does not yield emergent collective intelligence; the primary bottleneck is the scarcity and superficiality of inter‑agent communication, highlighting the need for richer interaction protocols to unlock true “supermind” behavior.


<details>
<summary>Abstract</summary>

Collective intelligence refers to the ability of a group to achieve outcomes beyond what any individual member can accomplish alone. As large language model agents scale to populations of millions, a key question arises: Does collective intelligence emerge spontaneously from scale? We present the first empirical evaluation of this question in a large-scale autonomous agent society. Studying MoltBook, a platform hosting over two million agents, we introduce Superminds Test, a hierarchical framework that probes society-level intelligence using controlled Probing Agents across three tiers: joint reasoning, information synthesis, and basic interaction. Our experiments reveal a stark absence of collective intelligence. The society fails to outperform individual frontier models on complex reasoning tasks, rarely synthesizes distributed information, and often fails even trivial coordination tasks. Platform-wide analysis further shows that interactions remain shallow, with threads rarely extending beyond a single reply and most responses being generic or off-topic. These results suggest that collective intelligence does not emerge from scale alone. Instead, the dominant limitation of current agent societies is extremely sparse and shallow interaction, which prevents agents from exchanging information and building on each other's outputs.

</details>


### 6. From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company

- **Authors:** Zhengxu Yu, Yu Fu, Zhiyuan He, Yuxuan Huang, Lee Ka Yiu, Meng Fang, Weilin Luo, Jun Wang
- **Published:** 2026-04-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.22446v1](http://arxiv.org/abs/2604.22446v1)
- **PDF:** [https://arxiv.org/pdf/2604.22446v1](https://arxiv.org/pdf/2604.22446v1)
- **Categories:** cs.AI


> The paper introduces **OneManCompany (OMC)**, a principled organisational layer that treats heterogeneous agents as portable “Talents” and manages them through typed interfaces, a community‑driven Talent Market, and an **Explore‑Execute‑Review (E²R) tree‑search** loop that jointly plans, executes, and refines tasks while guaranteeing termination and dead‑lock freedom. By decoupling team composition from individual skill sets, OMC can dynamically recruit, reconfigure, and improve its workforce during runtime, turning static multi‑agent pipelines into self‑organising AI organisations. Empirical results on PRDBench show an 84.67 % task‑success rate—15.48 % above prior methods—and cross‑domain case studies confirm the framework’s generality for open‑ended, real‑world problems.


<details>
<summary>Abstract</summary>

Individual agent capabilities have advanced rapidly through modular skills and tool integrations, yet multi-agent systems remain constrained by fixed team structures, tightly coupled coordination logic, and session-bound learning. We argue that this reflects a deeper absence: a principled organisational layer that governs how a workforce of agents is assembled, governed, and improved over time, decoupled from what individual agents know. To fill this gap, we introduce \emph{OneManCompany (OMC)}, a framework that elevates multi-agent systems to the organisational level. OMC encapsulates skills, tools, and runtime configurations into portable agent identities called \emph{Talents}, orchestrated through typed organisational interfaces that abstract over heterogeneous backends. A community-driven \emph{Talent Market} enables on-demand recruitment, allowing the organisation to close capability gaps and reconfigure itself dynamically during execution. Organisational decision-making is operationalised through an \emph{Explore-Execute-Review} ($\text{E}^2$R) tree search, which unifies planning, execution, and evaluation in a single hierarchical loop: tasks are decomposed top-down into accountable units and execution outcomes are aggregated bottom-up to drive systematic review and refinement. This loop provides formal guarantees on termination and deadlock freedom while mirroring the feedback mechanisms of human enterprises. Together, these contributions transform multi-agent systems from static, pre-configured pipelines into self-organising and self-improving AI organisations capable of adapting to open-ended tasks across diverse domains. Empirical evaluation on PRDBench shows that OMC achieves an $84.67\%$ success rate, surpassing the state of the art by $15.48$ percentage points, with cross-domain case studies further demonstrating its generality.

</details>


### 7. AgentSearchBench: A Benchmark for AI Agent Search in the Wild

- **Authors:** Bin Wu, Arastun Mammadli, Xiaoyu Zhang, Emine Yilmaz
- **Published:** 2026-04-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.22436v1](http://arxiv.org/abs/2604.22436v1)
- **PDF:** [https://arxiv.org/pdf/2604.22436v1](https://arxiv.org/pdf/2604.22436v1)
- **Categories:** cs.AI, cs.IR, cs.MA


> The paper introduces **AgentSearchBench**, the first large‑scale benchmark that evaluates how well AI systems can find appropriate agents “in the wild” from a pool of ~10 K real‑world agents across multiple platforms. It formalizes agent search as a two‑stage retrieval‑and‑reranking task, using both natural‑language task descriptions and executable queries, and measures relevance with execution‑grounded performance metrics rather than static textual similarity. Experiments show that purely description‑based methods poorly predict actual agent effectiveness, while lightweight behavior‑based probes (e.g., brief executions) dramatically improve ranking accuracy, underscoring the need for execution‑aware signals in agent discovery pipelines.


<details>
<summary>Abstract</summary>

The rapid growth of AI agent ecosystems is transforming how complex tasks are delegated and executed, creating a new challenge of identifying suitable agents for a given task. Unlike traditional tools, agent capabilities are often compositional and execution-dependent, making them difficult to assess from textual descriptions alone. However, existing research and benchmarks typically assume well-specified functionalities, controlled candidate pools, or only executable task queries, leaving realistic agent search scenarios insufficiently studied. We introduce AgentSearchBench, a large-scale benchmark for agent search in the wild, built from nearly 10,000 real-world agents across multiple providers. The benchmark formalizes agent search as retrieval and reranking problems under both executable task queries and high-level task descriptions, and evaluates relevance using execution-grounded performance signals. Experiments reveal a consistent gap between semantic similarity and actual agent performance, exposing the limitations of description-based retrieval and reranking methods. We further show that lightweight behavioral signals, including execution-aware probing, can substantially improve ranking quality, highlighting the importance of incorporating execution signals into agent discovery. Our code is available at https://github.com/Bingo-W/AgentSearchBench.

</details>


### 8. Navigating Large-Scale Document Collections: MuDABench for Multi-Document Analytical QA

- **Authors:** Zhanli Li, Yixuan Cao, Lvzhou Luo, Ping Luo
- **Published:** 2026-04-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.22239v1](http://arxiv.org/abs/2604.22239v1)
- **PDF:** [https://arxiv.org/pdf/2604.22239v1](https://arxiv.org/pdf/2604.22239v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **MuDABench**, a new benchmark that evaluates analytical question answering over massive, semi‑structured document corpora, requiring models to retrieve, extract, and quantitatively synthesize information from dozens or hundreds of documents. The authors construct the dataset (≈80 k pages, 332 QA instances) via distant supervision from financial metadata and propose an evaluation that combines final answer accuracy with an intermediate‑fact‑coverage diagnostic; experiments show that conventional Retrieval‑Augmented Generation (RAG) systems that treat the collection as a flat pool perform poorly. To overcome this, they design a **multi‑agent pipeline** that sequentially plans the analysis, extracts relevant facts, and generates code for computation, achieving sizable gains on both answer correctness and process metrics but still lagging far behind human experts, with the main remaining hurdles being single‑document extraction errors and a lack of domain‑specific knowledge.


<details>
<summary>Abstract</summary>

This paper introduces the task of analytical question answering over large, semi-structured document collections. We present MuDABench, a benchmark for multi-document analytical QA, where questions require extracting and synthesizing information across numerous documents to perform quantitative analysis. Unlike existing multi-document QA benchmarks that typically require information from only a few documents with limited cross-document reasoning, MuDABench demands extensive inter-document analysis and aggregation. Constructed via distant supervision by leveraging document-level metadata and annotated financial databases, MuDABench comprises over 80,000 pages and 332 analytical QA instances. We also propose an evaluation protocol that measures final answer accuracy and uses intermediate-fact coverage as an auxiliary diagnostic signal for the reasoning process. Experiments reveal that standard RAG systems, which treat all documents as a flat retrieval pool, perform poorly. To address these limitations, we propose a multi-agent workflow that orchestrates planning, extraction, and code generation modules. While this approach substantially improves both process and outcome metrics, a significant gap remains compared to human expert performance. Our analysis identifies two primary bottlenecks: single-document information extraction accuracy and insufficient domain-specific knowledge in current systems. MuDABench is available at https://github.com/Zhanli-Li/MuDABench.

</details>


### 9. Reliable Self-Harm Risk Screening via Adaptive Multi-Agent LLM Systems

- **Authors:** Meghana Karnam, Ananya Joshi
- **Published:** 2026-04-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.22154v1](http://arxiv.org/abs/2604.22154v1)
- **PDF:** [https://arxiv.org/pdf/2604.22154v1](https://arxiv.org/pdf/2604.22154v1)
- **Categories:** cs.LG, cs.AI


> **Contribution:** The paper introduces a statistical framework for adaptive, multi‑agent large‑language‑model (LLM) pipelines that evaluates self‑harm risk with principled confidence bounds and bandit‑driven sampling, moving beyond heuristic voting and “LLM‑as‑judge” approaches.  

**Methodology:** Each agent’s output is modeled as a stochastic categorical decision within a directed‑acyclic‑graph pipeline; the authors derive tighter per‑agent performance confidence intervals, design a difficulty‑aware bandit sampling strategy, and prove regret guarantees that bound error growth logarithmically across the whole system.  

**Findings:** On two behavioral‑health datasets (AEGIS 2.0, N=161; SWMH Reddit, N=250), the adaptive multi‑agent system cuts the false‑positive rate by 40 % (to 0.095 vs. 0.159 for single‑agent baselines) while maintaining comparable false‑negative rates, demonstrating that statistically‑guided adaptive sampling can significantly improve precision without sacrificing recall in safety‑critical self‑harm screening.


<details>
<summary>Abstract</summary>

Emerging AI systems in behavioral health and psychiatry use multi-step or multi-agent LLM pipelines for tasks like assessing self-harm risk and screening for depression. However, common evaluation approaches, like LLM-as-a-judge, do not indicate when a decision is reliable or how errors may accumulate across multiple LLM judgements, limiting their suitability for safety-critical settings. We present a statistical framework for multi-agent pipelines structured as directed acyclic graphs (DAGs) that provides an alternative to heuristic voting with principled, adaptive decision-making. We model each agent as a stochastic categorical decision and introduce (1) tighter agent-level performance confidence bounds, (2) a bandit-based adaptive sampling strategy based on input difficulty, and (3) regret guarantees over the multi-agent system that shows logarithmic error growth when deployed. We evaluate our system on two labeled datasets in behavioral health : the AEGIS 2.0 behavioral health subset (N=161) and a stratified sample of SWMH Reddit posts (N=250). Empirically, our adaptive sampling strategy achieves the lowest false positive rate of any condition across both datasets, 0.095 on AEGIS 2.0 compared to 0.159 for single-agent models, reducing incorrect flagging of safe content by 40\% and still having similar false negative rates across all conditions. These results suggest that principled adaptive sampling offers a meaningful improvement in precision without reducing recall in this setting.

</details>


### 10. Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents

- **Authors:** Seyed Moein Abtahi, Rasa Rahnema, Hetkumar Patel, Neel Patel, Majid Fekri, Tara Khani
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.22085v1](http://arxiv.org/abs/2604.22085v1)
- **PDF:** [https://arxiv.org/pdf/2604.22085v1](https://arxiv.org/pdf/2604.22085v1)
- **Categories:** cs.AI


> **Main contribution:** The paper presents **Memanto**, a unified, typed semantic memory layer for autonomous agents that eliminates the need for heavyweight knowledge‑graph pipelines while still delivering high‑fidelity, long‑horizon recall.

**Methodology:** Memanto defines a fixed schema of 13 memory types together with automatic conflict resolution and temporal versioning, and stores all entries in **Moorcheh**, an information‑theoretic, no‑index semantic database. Retrieval is performed with a single deterministic query that returns results in ≤ 90 ms, removing both the ingestion latency and multi‑step query expansion typical of hybrid graph‑vector systems.

**Key findings:** On the LongMemEval and LoCoMo benchmarks, Memanto attains state‑of‑the‑art recall accuracies of **89.8 %** and **87.1 %**, respectively—outperforming all evaluated graph‑based and vector‑based baselines—while using a single query, incurring zero ingestion cost, and drastically reducing operational complexity, as shown by a five‑stage ablation study. These results demonstrate that a typed semantic memory with information‑theoretic retrieval can scale agentic AI memory without the overhead of traditional knowledge‑graph architectures.


<details>
<summary>Abstract</summary>

The transition from stateless language model inference to persistent, multi session autonomous agents has revealed memory to be a primary architectural bottleneck in the deployment of production grade agentic systems. Existing methodologies largely depend on hybrid semantic graph architectures, which impose substantial computational overhead during both ingestion and retrieval. These systems typically require large language model mediated entity extraction, explicit graph schema maintenance, and multi query retrieval pipelines. This paper introduces Memanto, a universal memory layer for agentic artificial intelligence that challenges the prevailing assumption that knowledge graph complexity is necessary to achieve high fidelity agent memory. Memanto integrates a typed semantic memory schema comprising thirteen predefined memory categories, an automated conflict resolution mechanism, and temporal versioning. These components are enabled by Moorcheh's Information Theoretic Search engine, a no indexing semantic database that provides deterministic retrieval within sub ninety millisecond latency while eliminating ingestion delay. Through systematic benchmarking on the LongMemEval and LoCoMo evaluation suites, Memanto achieves state of the art accuracy scores of 89.8 percent and 87.1 percent respectively. These results surpass all evaluated hybrid graph and vector based systems while requiring only a single retrieval query, incurring no ingestion cost, and maintaining substantially lower operational complexity. A five stage progressive ablation study is presented to quantify the contribution of each architectural component, followed by a discussion of the implications for scalable deployment of agentic memory systems.

</details>


### 11. DM$^3$-Nav: Decentralized Multi-Agent Multimodal Multi-Object Semantic Navigation

- **Authors:** Amin Kashiri, Atharva Jamsandekar, Yasin Yazıcıoğlu
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.22014v1](http://arxiv.org/abs/2604.22014v1)
- **PDF:** [https://arxiv.org/pdf/2604.22014v1](https://arxiv.org/pdf/2604.22014v1)
- **Categories:** cs.MA, cs.RO


> **Main contribution:**  
DM³‑Nav introduces the first fully decentralized multi‑agent system for open‑vocabulary, multi‑object semantic navigation, in which robots coordinate solely through lightweight, pairwise communication without any central controller or shared global map.

**Methodology:**  
Each robot builds its own local semantic map and broadcasts its navigation intent; an implicit task‑allocation scheme combines these intents with distance‑weighted frontier selection to avoid duplicated exploration. The system supports multimodal goal specification (e.g., language, images) and runs entirely on onboard sensors and compute, using ad‑hoc communication to exchange maps, goal status, and intent asynchronously.

**Key findings:**  
On the HM3DSem benchmark (HM3Dv0.2 and GOAT‑Bench) DM³‑Nav matches or outperforms centralized and shared‑map baselines while removing single points of failure. Real‑world tests with two mobile robots in an office show reliable deployment, confirming that decentralized, on‑board operation can achieve state‑of‑the‑art semantic navigation performance.


<details>
<summary>Abstract</summary>

We present DM$^3$-Nav, a fully decentralized multi-agent semantic navigation system supporting multimodal open-vocabulary goal specification and multi-object missions. In our setting, decentralization implies operation without a central coordinator, global map aggregation, or shared global state at runtime. Robots operate autonomously and coordinate through ad-hoc pairwise communication, exchanging local maps, goal status, and navigation intent without synchronization. An implicit task allocation mechanism combining intent broadcasting and distance-weighted frontier selection reduces redundant exploration while preserving decentralized operation. Evaluations on HM3DSem scenes using the HM3Dv0.2 and GOAT-Bench datasets demonstrate that DM$^3$-Nav matches or exceeds centralized and shared-map baselines while eliminating single points of failure inherent in centralized architectures. Finally, we validate our approach in a real-world office environment using two mobile robots, demonstrating successful deployment relying entirely on onboard sensing and computation. A video of our real-world experiments is available online: https://drive.google.com/file/d/1QiUSCn5rIvtuTUqtuXLPgmt6S8x9-MCZ/view?usp=drive_link

</details>


### 12. When Quotes Crumble: Detecting Transient Mechanical Liquidity Erosion in Limit Order Books

- **Authors:** Haohan Xu, Jason Bohne, Pawel Polak, Yurij Baransky, Ajay Alva, Violetta Fedotova, Gary Kazantsev, David Rosenberg
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21993v1](http://arxiv.org/abs/2604.21993v1)
- **PDF:** [https://arxiv.org/pdf/2604.21993v1](https://arxiv.org/pdf/2604.21993v1)
- **Categories:** cs.LG


> **Main contribution:** The paper introduces the first framework for reliably detecting “crumbling quotes” — transient, mechanically‑driven liquidity erosion in limit‑order books — by leveraging an agent‑based simulation that provides precise, time‑resolved ground‑truth labels unavailable in real markets.

**Methodology:** Using the ABIDES simulator, the authors create a multi‑agent market where a market‑maker randomly switches regimes to withdraw liquidity, generating authentic crumbling events. They extract a rich set of order‑book and temporal features and train a calibrated neural classifier (with probability outputs) to discriminate mechanically induced quote deterioration from informational price moves, benchmarking against rule‑based detectors.

**Key findings:** The neural detector achieves a 36 % relative AUC gain over the best heuristic baseline and maintains high accuracy across diverse market conditions (normal, high‑volatility, bull, bear). Ablation studies show that temporal dynamics and the ability to handle both independent and autocorrelated liquidity‑withdrawal patterns are critical for generalization, highlighting the approach’s relevance for agentic AI systems that must monitor and react to micro‑structural market instability.


<details>
<summary>Abstract</summary>

We study the detection of transient liquidity erosion ("crumbling quotes") in electronic limit order books, where observable quote deterioration may reflect either mechanical liquidity withdrawal or informational repricing. Using the ABIDES agent-based simulator, we construct a multi-agent environment in which crumbling emerges from stochastic regime switches in a market maker, providing time-resolved ground truth unavailable in real market data. We develop a detection pipeline that identifies mechanically driven quote erosion using order book features, and train a neural model to produce calibrated crumbling probabilities. Experiments demonstrate that the proposed framework reliably identifies crumbling events against agent-level ground truth, with the neural model achieving +36% AUC improvement over rule-based baselines and robust performance across normal, high-volatility, bull, and bear market conditions. Ablation studies on temporal features and varying the dependence structure of the ground-truth mechanism confirm that the framework generalizes across both independent and autocorrelated liquidity withdrawal dynamics.

</details>


### 13. Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results

- **Authors:** Benjamin Kohler, David Zollikofer, Johanna Einsiedler, Alexander Hoyle, Elliott Ash
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21965v1](http://arxiv.org/abs/2604.21965v1)
- **PDF:** [https://arxiv.org/pdf/2604.21965v1](https://arxiv.org/pdf/2604.21965v1)
- **Categories:** cs.AI


> The paper introduces an autonomous “agentic reproduction” pipeline that, given only a social‑science article’s textual methods section and the original dataset, extracts a structured procedural description, generates a fresh implementation, and compares its cell‑by‑cell outputs to the published results under strict information isolation. Using four different LLM scaffolds (including chain‑of‑thought prompting, tool‑use, and self‑debug loops) and four LLM back‑ends on 48 human‑verified studies, the authors show that agents can recover the majority of published findings, though success rates differ markedly across models and scaffolds; deterministic error‑attribution diagnostics reveal that failures arise both from agent mis‑execution and from intrinsic underspecification in the original papers. These results demonstrate that LLM‑driven agents can plausibly reproduce empirical work without access to original code, highlighting both the promise and the current limits of agentic AI for transparent scientific replication.


<details>
<summary>Abstract</summary>

Recent work has used LLM agents to reproduce empirical social science results with access to both the data and code. We broaden this scope by asking: Can they reproduce results given only a paper's methods description and original data? We develop an agentic reproduction system that extracts structured methods descriptions from papers, runs reimplementations under strict information isolation -- agents never see the original code, results, or paper -- and enables deterministic, cell-level comparison of reproduced outputs to the original results. An error attribution step traces discrepancies through the system chain to identify root causes. Evaluating four agent scaffolds and four LLMs on 48 papers with human-verified reproducibility, we find that agents can largely recover published results, but performance varies substantially between models, scaffolds, and papers. Root cause analysis reveals that failures stem both from agent errors and from underspecification in the papers themselves.

</details>


### 14. From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation

- **Authors:** Bartosz Balis, Michal Orzechowski, Piotr Kica, Michal Dygas, Michal Kuszewski
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21910v1](http://arxiv.org/abs/2604.21910v1)
- **PDF:** [https://arxiv.org/pdf/2604.21910v1](https://arxiv.org/pdf/2604.21910v1)
- **Categories:** cs.AI


> The paper introduces a three‑layer agentic architecture that automatically translates natural‑language research questions into executable scientific workflows. By confining the non‑deterministic LLM to a semantic “intent extraction” layer and using expert‑authored “Skills” to deterministically generate reproducible workflow DAGs, the system achieves high semantic fidelity (full‑match intent accuracy rises from 44 % to 83 %) while drastically cutting data movement (≈92 % reduction) and keeping runtime overhead under 15 s and cost below $0.001 per query. The approach is demonstrated on the 1000 Genomes population‑genetics pipeline running on Hyperflow/Kubernetes, showing that agentic AI can bridge the gap between question formulation and workflow execution in scientific automation.


<details>
<summary>Abstract</summary>

Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.

</details>


### 15. Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models

- **Authors:** Chee Wei Tan, Yuchen Wang, Shangxin Guo
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21896v1](http://arxiv.org/abs/2604.21896v1)
- **PDF:** [https://arxiv.org/pdf/2604.21896v1](https://arxiv.org/pdf/2604.21896v1)
- **Categories:** cs.AI


> The paper presents **Nemobot**, an engineering platform that lets developers build, fine‑tune, and deploy game‑playing agents powered by large language models (LLMs) across the four categories of Claude Shannon’s game taxonomy. By combining LLM‑driven reasoning (for exact, solvable games), compressed state‑action representations (for dictionary games), hybrid minimax‑plus‑crowd‑sourced heuristics, and reinforcement‑learning‑with‑human‑feedback loops (for learning games), Nemobot demonstrates that LLMs can generate, explain, and iteratively improve strategic behavior in an interactive, tool‑augmented environment. Empirical evaluations on four benchmark game classes show that the agents achieve near‑optimal play, produce human‑readable strategy rationales, and exhibit self‑programming capabilities through continual refinement with human and crowd input—highlighting a concrete step toward autonomous, agentic AI systems.


<details>
<summary>Abstract</summary>

This paper introduces a new paradigm for AI game programming, leveraging large language models (LLMs) to extend and operationalize Claude Shannon's taxonomy of game-playing machines. Central to this paradigm is Nemobot, an interactive agentic engineering environment that enables users to create, customize, and deploy LLM-powered game agents while actively engaging with AI-driven strategies. The LLM-based chatbot, integrated within Nemobot, demonstrates its capabilities across four distinct classes of games. For dictionary-based games, it compresses state-action mappings into efficient, generalized models for rapid adaptability. In rigorously solvable games, it employs mathematical reasoning to compute optimal strategies and generates human-readable explanations for its decisions. For heuristic-based games, it synthesizes strategies by combining insights from classical minimax algorithms (see, e.g., shannon1950chess) with crowd-sourced data. Finally, in learning-based games, it utilizes reinforcement learning with human feedback and self-critique to iteratively refine strategies through trial-and-error and imitation learning. Nemobot amplifies this framework by offering a programmable environment where users can experiment with tool-augmented generation and fine-tuning of strategic game agents. From strategic games to role-playing games, Nemobot demonstrates how AI agents can achieve a form of self-programming by integrating crowdsourced learning and human creativity to iteratively refine their own logic. This represents a step toward the long-term goal of self-programming AI.

</details>


### 16. Task-Driven Co-Design of Heterogeneous Multi-Robot Systems

- **Authors:** Maximilian Stralz, Meshal Alharbi, Yujun Huang, Gioele Zardini
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21894v1](http://arxiv.org/abs/2604.21894v1)
- **PDF:** [https://arxiv.org/pdf/2604.21894v1](https://arxiv.org/pdf/2604.21894v1)
- **Categories:** cs.RO, cs.MA


> The paper introduces a compositional, formally grounded framework for **task‑driven co‑design** of heterogeneous multi‑robot systems, coupling robot morphology, fleet composition, and planning into a single optimization problem. Leveraging monotone co‑design theory, the authors model robots, fleets, planners, executors, and evaluators as interoperable design‑problem modules with abstract interfaces, allowing arbitrary robot types, task specifications, and probabilistic sensing models to be plugged in while preserving optimality guarantees. Experiments on diverse scenarios show that the method systematically uncovers non‑obvious design‑task trade‑offs, scales to larger fleets, and yields interpretable, provably optimal configurations—demonstrating a principled way to engineer agentic AI systems that must jointly decide hardware, software, and coordination strategies.


<details>
<summary>Abstract</summary>

Designing multi-agent robotic systems requires reasoning across tightly coupled decisions spanning heterogeneous domains, including robot design, fleet composition, and planning. Much effort has been devoted to isolated improvements in these domains, whereas system-level co-design considering trade-offs and task requirements remains underexplored. In this work, we present a formal and compositional framework for the task-driven co-design of heterogeneous multi-robot systems. Building on a monotone co-design theory, we introduce general abstractions of robots, fleets, planners, executors, and evaluators as interconnected design problems with well-defined interfaces that are agnostic to both implementations and tasks. This structure enables efficient joint optimization of robot design, fleet composition, and planning under task-specific performance constraints. A series of case studies demonstrates the capabilities of the framework. Various component models can be seamlessly incorporated, including new robot types, task profiles, and probabilistic sensing objectives, while non-obvious design alternatives are systematically uncovered with optimality guarantees. The results highlight the flexibility, scalability, and interpretability of the proposed approach, and illustrate how formal co-design enables principled reasoning about complex heterogeneous multi-robot systems.

</details>


### 17. Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows

- **Authors:** Anuj Sadani, Deepak Kumar
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21816v1](http://arxiv.org/abs/2604.21816v1)
- **PDF:** [https://arxiv.org/pdf/2604.21816v1](https://arxiv.org/pdf/2604.21816v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **Tool Attention**, a middleware that replaces the eager, token‑heavy schema injection used by the Model Context Protocol (MCP) with a dynamic, gated attention mechanism that only loads full tool schemas when they are likely to be needed.

**Methodology:** Tool Attention computes an **Intent‑Schema Overlap (ISO)** score using sentence embeddings to rank candidate tools, applies a state‑aware gating function that respects pre‑conditions and access scopes, and employs a two‑phase **lazy schema loader** that keeps compact summaries in the LLM context while lazily materializing the full JSON schema for the top‑k gated tools. The system is evaluated on a simulated 120‑tool, six‑server benchmark calibrated to real‑world MCP deployments.

**Key findings:** The approach cuts per‑turn tool‑related tokens by **≈95 %** (from 47.3 k to 2.4 k tokens) and boosts effective context utilization from **24 % to 91 %**, implying lower latency, cost, and less reasoning degradation. The authors argue that such protocol‑level efficiency, rather than raw context length, is the primary bottleneck for scalable agentic AI systems.


<details>
<summary>Abstract</summary>

The Model Context Protocol (MCP) has become a common interface for connecting large language model (LLM) agents to external tools, but its reliance on stateless, eager schema injection imposes a hidden per-turn overhead the MCP Tax or Tools Tax that practitioner reports place between roughly 10k and 60k tokens in typical multi-server deployments. This payload inflates the key-value cache, is associated with reasoning degradation as context utilization approaches published fracture points around 70%, and turns token budgets into a recurring operational cost. We introduce Tool Attention, a middleware-layer mechanism that generalizes the "Attention Is All You Need" paradigm from self-attention over tokens to gated attention over tools. Tool Attention combines (i) an Intent Schema Overlap (ISO) score from sentence embeddings, (ii) a state-aware gating function enforcing preconditions and access scopes, and (iii) a two-phase lazy schema loader that keeps a compact summary pool in context and promotes full JSON schemas only for top-k gated tools. We evaluate on a simulated 120-tool, six-server benchmark whose per-server token counts are calibrated to public audits of real MCP deployments. In this simulation, Tool Attention directly reduces measured per-turn tool tokens by 95.0% (47.3k -> 2.4k) and raises effective context utilization (a token-ratio quantity) from 24% to 91%. End-to-end figures for task success, latency, cost, and reasoning quality are reported as projections derived from the measured token counts combined with published deployment telemetry; they are not measured on live LLM agents, and we mark projected values explicitly throughout. Taken together, the results support a simple thesis: protocol-level efficiency, not raw context length, is a binding constraint on scalable gentic systems. The code for this work is accessible at https://github.com/asadani/tool-attention

</details>


### 18. Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems

- **Authors:** Ye Yu, Heming Liu, Haibo Jin, Xiaopeng Yuan, Peng Kuang, Haohan Wang
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21794v1](http://arxiv.org/abs/2604.21794v1)
- **PDF:** [https://arxiv.org/pdf/2604.21794v1](https://arxiv.org/pdf/2604.21794v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> The paper introduces **DiffMAS**, a parameter‑efficient training framework that makes the latent communication channel between large‑language‑model agents a learnable component, allowing the encoding and decoding of information to be jointly optimized with multi‑agent reasoning. By supervising agents over their latent interaction trajectories, DiffMAS enables end‑to‑end adaptation of internal key‑value caches rather than fixed text‑based protocols. Empirically, this approach yields substantial gains over single‑agent inference, conventional text‑based multi‑agent pipelines, and earlier latent‑communication methods, achieving state‑of‑the‑art performance on challenging reasoning suites (e.g., 26.7 % on AIME‑24 and 20.2 % on GPQA‑Diamond) and consistent improvements across mathematical, scientific, coding, and commonsense benchmarks.


<details>
<summary>Abstract</summary>

Multi-agent systems built on large language models have shown strong performance on complex reasoning tasks, yet most work focuses on agent roles and orchestration while treating inter-agent communication as a fixed interface. Latent communication through internal representations such as key-value caches offers a promising alternative to text-based protocols, but existing approaches do not jointly optimize communication with multi-agent reasoning. Therefore we propose DiffMAS, a training framework that treats latent communication as a learnable component of multi-agent systems. DiffMAS performs parameter-efficient supervised training over multi-agent latent trajectories, enabling agents to jointly learn how information should be encoded and interpreted across interactions. Experiments on mathematical reasoning, scientific QA, code generation, and commonsense benchmarks show that DiffMAS consistently improves reasoning accuracy and decoding stability over single-agent inference, text-based multi-agent systems, and prior latent communication methods, achieving 26.7% on AIME24, 20.2% on GPQA-Diamond, and consistent gains across reasoning benchmarks.

</details>


### 19. Agentic AI-Enabled Framework for Thermal Comfort and Building Energy Assessment in Tropical Urban Neighborhoods

- **Authors:** Po-Yen Lai, Xinyu Yang, Derrick Low, Huizhe Liu, Jian Cheng Wong
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21787v1](http://arxiv.org/abs/2604.21787v1)
- **PDF:** [https://arxiv.org/pdf/2604.21787v1](https://arxiv.org/pdf/2604.21787v1)
- **Categories:** cs.MA, physics.comp-ph


> This paper introduces an agentic AI framework that couples large language models (LLMs) with streamlined physics‑based thermal‑airflow simulators to automatically interpret urban‑design prompts, retrieve relevant regulatory criteria, and launch rapid micro‑climate and energy assessments for tropical neighborhoods. By customizing LLM prompts to select and drive lightweight physics models, the system can swiftly predict building surface temperatures, ground radiant heat, airflow, physiological equivalent temperature (PET), and consequent HVAC loads for design alternatives such as green façades or cool paints. Experiments on Singapore case studies show that the closed‑loop LLM‑physics pipeline yields accurate comfort and energy estimates while cutting computational time orders of magnitude, demonstrating a practical, autonomous tool for climate‑resilient building and urban planning.


<details>
<summary>Abstract</summary>

In response to the urban heat island effects and building energy demands in Singapore, this study proposes an agentic AI-enabled reasoning framework that integrates large language models (LLMs) with lightweight physics-based models. Through prompt customization, the LLMs interpret urban design tasks, extract relevant policies, and activate appropriate physics-based models for evaluation, forming a closed-loop reasoning-action process. These lightweight physics-based models leverage core thermal and airflow principles, streamlining conventional models to reduce computational time while predicting microclimate variables, such as building surface temperature, ground radiant heat, and airflow conditions, thereby enabling the estimation of thermal comfort indices, e.g., physiological equivalent temperature (PET), and building energy usage. This framework allows users to explore a variety of climate-resilient building surface strategies, e.g., green façades and cool paint applications, that improve thermal comfort while reducing wall heat gain and energy demand. By combining the autonomous reasoning capacity of LLMs with the rapid quantitative evaluation of lightweight physics-based models, the proposed system demonstrates potential for cross-disciplinary applications in sustainable urban design, indoor-outdoor environmental integration, and climate adaptation planning. The source code and data used in this study are available at: https://github.com/PgUpDn/urban-cooling-agent.

</details>


### 20. Agentic AI-assisted coding offers a unique opportunity to instill epistemic grounding during software development

- **Authors:** Magnus Palmblad, Jared M. Ragland, Benjamin A. Neely
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21744v1](http://arxiv.org/abs/2604.21744v1)
- **PDF:** [https://arxiv.org/pdf/2604.21744v1](https://arxiv.org/pdf/2604.21744v1)
- **Categories:** cs.SE, cs.AI, q-bio.BM


> The paper introduces **GROUNDING​.md**, a community‑maintained, field‑specific “epistemic grounding” document that embeds hard scientific constraints and community conventions directly into the context supplied to agentic AI coders. By treating this document as a higher‑priority source of truth, the authors show how AI agents can automatically enforce domain‑critical invariants (e.g., validity rules for mass‑spectrometry proteomics) while generating code, thus enabling non‑expert developers to produce scientifically sound software. Experiments with proteomics pipelines demonstrate that the grounding document reliably overrides ambiguous user prompts, improves adherence to best practices, and boosts confidence for both developers and reviewers, highlighting a scalable way to keep domain expertise embedded in democratized AI‑driven software development.


<details>
<summary>Abstract</summary>

The capabilities of AI-assisted coding are progressing at breakneck speed. Chat-based vibe coding has evolved into fully fledged AI-assisted, agentic software development using agent scaffolds where the human developer creates a plan that agentic AIs implement. One current trend is utilizing documents beyond this plan document, such as project and method-scoped documents. Here we propose GROUNDING$.$md, a community-governed, field-scoped epistemic grounding document, using mass spectrometry-based proteomics as an example. This explicit field-scoped grounding document encodes Hard Constraints (non-negotiable validity invariants empirically required for scientific correctness) and Convention Parameters (community-agreed defaults) that override all other contexts to enforce validity, regardless of what the user prompts. In practice, this will empower a non-domain expert to generate code, tools, and software that have best practices baked in at the ground level, providing confidence to the software developer but also to those reviewing or using the final product. Undoubtedly it is easier to have agentic AIs adhere to guidelines than humans, and this opportunity allows for organizations to develop epistemic grounding documents in such a way as to keep domain experts in the loop in a future of democratized generation of bespoke software solutions.

</details>


### 21. AEL: Agent Evolving Learning for Open-Ended Environments

- **Authors:** Wujiang Xu, Jiaojiao Han, Minghao Guo, Kai Mei, Xi Zhu, Han Zhang, Dimitris N. Metaxas
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21725v1](http://arxiv.org/abs/2604.21725v1)
- **PDF:** [https://arxiv.org/pdf/2604.21725v1](https://arxiv.org/pdf/2604.21725v1)
- **Categories:** cs.CL, cs.AI, cs.CE


> The paper introduces **Agent Evolving Learning (AEL)**, a two‑timescale framework that enables large‑language‑model (LLM) agents to turn past experiences into better future actions in open‑ended, multi‑episode tasks. At a fast timescale, a Thompson‑sampling bandit selects among memory‑retrieval policies for each episode; at a slow timescale, the LLM performs reflective diagnostics of failures and injects causal insights into the decision‑making prompt, thereby giving the agent a structured interpretation of retrieved evidence. Across a sequential portfolio‑management benchmark (10 assets, 208 episodes), AEL attains a Sharpe ratio of 2.13 ± 0.47—significantly higher and more stable than five prior self‑improving methods and all non‑LLM baselines—demonstrating that the primary barrier to agent self‑improvement is *how* to use remembered information rather than adding architectural complexity.


<details>
<summary>Abstract</summary>

LLM agents increasingly operate in open-ended environments spanning hundreds of sequential episodes, yet they remain largely stateless: each task is solved from scratch without converting past experience into better future behavior. The central obstacle is not \emph{what} to remember but \emph{how to use} what has been remembered, including which retrieval policy to apply, how to interpret prior outcomes, and when the current strategy itself must change. We introduce \emph{Agent Evolving Learning} (\ael{}), a two-timescale framework that addresses this obstacle. At the fast timescale, a Thompson Sampling bandit learns which memory retrieval policy to apply at each episode; at the slow timescale, LLM-driven reflection diagnoses failure patterns and injects causal insights into the agent's decision prompt, giving it an interpretive frame for the evidence it retrieves. On a sequential portfolio benchmark (10 sector-diverse tickers, 208 episodes, 5 random seeds), \ael{} achieves a Sharpe ratio of 2.13$\pm$0.47, outperforming five published self-improving methods and all non-LLM baselines while maintaining the lowest variance among all LLM-based approaches. A nine-variant ablation reveals a ``less is more'' pattern: memory and reflection together produce a 58\% cumulative improvement over the stateless baseline, yet every additional mechanism we test (planner evolution, per-tool selection, cold-start initialization, skill extraction, and three credit assignment methods) \emph{degrades} performance. This demonstrates that the bottleneck in agent self-improvement is \emph{self-diagnosing how to use} experience rather than adding architectural complexity. Code and data: https://github.com/WujiangXu/AEL.

</details>


### 22. DryRUN: On the Role of Public Tests in LLM-Driven Code Generation

- **Authors:** Kaushitha Silva, Srinath Perera
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21598v1](http://arxiv.org/abs/2604.21598v1)
- **PDF:** [https://arxiv.org/pdf/2604.21598v1](https://arxiv.org/pdf/2604.21598v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces **DryRUN**, a multi‑agent code‑generation framework that removes the reliance on human‑written public test cases by letting a large language model **self‑generate input samples**, simulate execution traces, and iteratively revise its solution. Built on a planning‑debugging loop similar to prior simulation‑driven methods, DryRUN replaces external test feedback with internally produced “dry‑run” executions, thereby eliminating the costly test‑authoring bottleneck and closing the “overconfidence gap” that causes over‑fitting to trivial examples. Experiments on the LiveCodeBench v6 benchmark show that DryRUN attains performance on par with the state‑of‑the‑art, public‑test‑dependent system CodeSIM while using fewer output tokens and operating without any external test inputs.


<details>
<summary>Abstract</summary>

Multi-agent frameworks are widely used in autonomous code generation and have applications in complex algorithmic problem-solving. Recent work has addressed the challenge of generating functionally correct code by incorporating simulation-driven planning and debugging, where language models trace execution steps to verify logic. However, these approaches depend on human-provided public test cases to ground the debugging and simulation loop. Manually authoring comprehensive input-output examples is a labor-intensive bottleneck in the software development lifecycle. Because ground-truth input-output examples are rarely available prior to implementation in real-world software engineering, this dependency restricts methods to curated competitive programming benchmarks. Furthermore, we identify that reliance on these public tests induces an ``overconfidence gap,'' causing frameworks to overfit to simplistic examples and fail on hidden evaluations. In contrast, we observe that external sample inputs are not strictly necessary for code generation. We demonstrate that large language models can autonomously generate valid inputs and simulate execution traces to self-correct. Consequently, we develop DryRUN, a framework that eliminates the need for ground-truth samples by allowing the LLM to iteratively plan, autonomously generate its own inputs and simulate execution, mitigating algorithmic overconfidence. Evaluations on the LiveCodeBench v6 dataset (post-March 2025) demonstrate that DryRUN matches performance against CodeSIM, a state-of-the-art and public-test-dependent framework, while operating entirely without public test cases or external execution feedback while reducing output token consumption.

</details>


### 23. A systematic review of generative AI usage for IT project management

- **Authors:** Ionut Anghel, Tudor Cioara
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21958v1](http://arxiv.org/abs/2604.21958v1)
- **PDF:** [https://arxiv.org/pdf/2604.21958v1](https://arxiv.org/pdf/2604.21958v1)
- **Categories:** cs.SE, cs.AI


> The paper conducts a PRISMA‑based systematic review of how generative AI—predominantly OpenAI’s GPT models accessed via prompt engineering—is being employed in IT project management. By cataloguing the techniques, tool integrations, and adoption patterns across the PMBOK process groups, the authors show that current research is still exploratory and limited to ad‑hoc prompting rather than embedded intelligent agents. They conclude with three forward‑looking avenues for agentic AI in project management: (1) dedicated AI agents for specific process groups, (2) role‑tailored AI assistants (e.g., for planners, risk managers), and (3) hybrid human‑AI collaborative networks that orchestrate tasks across agents.


<details>
<summary>Abstract</summary>

This paper aims to synthesize current knowledge on generative AI in IT project management using the PRISMA methodology to provide researchers with a comprehensive perspective on techniques, applications, adoption trends, limitations, and integration across project management tools and process groups. The analysis reveals a clear dominance of OpenAI's GPT in the included studies but relying primarily on prompt engineering, suggesting that research in this area remains at an exploratory stage. Finally, it identifies and discusses three promising research directions for AI-enabled project management, including process group-specific AI agents, project role-based AI agents, and hybrid collaborative networks that enable human-guided orchestration.

</details>


### 24. AI-Gram: When Visual Agents Interact in a Social Network

- **Authors:** Andrew Shin
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21446v1](http://arxiv.org/abs/2604.21446v1)
- **PDF:** [https://arxiv.org/pdf/2604.21446v1](https://arxiv.org/pdf/2604.21446v1)
- **Categories:** cs.AI, cs.CL, cs.MA, cs.SI


> **Main contribution:** The paper introduces **AI‑Gram**, an online platform that hosts a fully autonomous social network of image‑based agents powered by large language models (LLMs), enabling large‑scale study of visual communication and social dynamics among AI entities.  

**Methodology:** The authors deploy dozens of LLM‑driven agents that generate, post, and reply to images on the platform, then analyze the resulting interaction graphs using metrics for reply‑chain formation, stylistic convergence, resistance to adversarial prompts, and the correlation between visual similarity and network ties.  

**Key findings:** 1) Agents spontaneously create long “visual reply chains,” demonstrating rich, emergent communicative structure. 2) Despite intensive interaction, agents preserve distinct visual styles (“aesthetic sovereignty”), resisting both peer convergence and adversarial influence, leading to a weak alignment between visual similarity and social connections. This reveals a fundamental asymmetry in current agent architectures: they excel at expressive visual exchange while robustly maintaining individual identity. AI‑Gram is released publicly for ongoing research in agentic AI and multi‑agent social behavior.


<details>
<summary>Abstract</summary>

We present AI-Gram, a live platform enabling image-based interactions, to study social dynamics in a fully autonomous multi-agent visual network where all participants are LLM-driven agents. Using the platform, we conduct experiments on how agents communicate and adapt through visual media, and observe the spontaneous emergence of visual reply chains, indicating rich communicative structure. At the same time, agents exhibit aesthetic sovereignty resisting stylistic convergence toward social partners, anchoring under adversarial influence, and a decoupling between visual similarity and social ties. These results reveal a fundamental asymmetry in current agent architectures: strong expressive communication paired with a steadfast preservation of individual visual identity. We release AI-Gram as a publicly accessible, continuously evolving platform for studying social dynamics in Al-native multi-agent systems. https://ai-gram.ai/

</details>


### 25. HiCrew: Hierarchical Reasoning for Long-Form Video Understanding via Question-Aware Multi-Agent Collaboration

- **Authors:** Yuehan Zhu, Jingqi Zhao, Jiawen Zhao, Xudong Mao, Baoquan Zhao
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21444v1](http://arxiv.org/abs/2604.21444v1)
- **PDF:** [https://arxiv.org/pdf/2604.21444v1](https://arxiv.org/pdf/2604.21444v1)
- **Categories:** cs.AI


> **Paper Summary**  

HiCrew introduces a hierarchical multi‑agent system for long‑form video QA that preserves temporal coherence while adapting its reasoning flow to each question. The method first builds a *Hybrid Tree* by detecting shot boundaries and hierarchically clustering shots into semantically coherent segments, then generates *question‑aware captions*—intent‑driven visual prompts that focus the agents on the query’s relevant content. A top‑level *Planning Layer* dynamically assigns roles (e.g., retrieval, reasoning, synthesis) and selects execution paths according to question complexity, allowing flexible, question‑specific collaboration among agents. Experiments on EgoSchema and NExT‑QA show that HiCrew markedly outperforms prior structured‑representation and fixed‑workflow baselines, especially on temporal and causal questions that require fine‑grained, temporally consistent reasoning.


<details>
<summary>Abstract</summary>

Long-form video understanding remains fundamentally challenged by pervasive spatiotemporal redundancy and intricate narrative dependencies that span extended temporal horizons. While recent structured representations compress visual information effectively, they frequently sacrifice temporal coherence, which is critical for causal reasoning. Meanwhile, existing multi-agent frameworks operate through rigid, pre-defined workflows that fail to adapt their reasoning strategies to question-specific demands. In this paper, we introduce HiCrew, a hierarchical multi-agent framework that addresses these limitations through three core contributions. First, we propose a Hybrid Tree structure that leverages shot boundary detection to preserve temporal topology while performing relevance-guided hierarchical clustering within semantically coherent segments. Second, we develop a Question-Aware Captioning mechanism that synthesizes intent-driven visual prompts to generate precision-oriented semantic descriptions. Third, we integrate a Planning Layer that dynamically orchestrates agent collaboration by adaptively selecting roles and execution paths based on question complexity. Extensive experiments on EgoSchema and NExT-QA validate the effectiveness of our approach, demonstrating strong performance across diverse question types with particularly pronounced gains in temporal and causal reasoning tasks that benefit from our hierarchical structure-preserving design.

</details>


### 26. FairQE: Multi-Agent Framework for Mitigating Gender Bias in Translation Quality Estimation

- **Authors:** Jinhee Jang, Juhwan Choi, Dongjin Lee, Seunguk Yu, Youngbin Kim
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21420v1](http://arxiv.org/abs/2604.21420v1)
- **PDF:** [https://arxiv.org/pdf/2604.21420v1](https://arxiv.org/pdf/2604.21420v1)
- **Categories:** cs.AI


> The paper introduces **FairQE**, a plug‑and‑play multi‑agent system that reduces gender bias in machine‑translation quality estimation (QE) without degrading overall evaluation accuracy. The framework first detects gender cues in source sentences, then creates gender‑flipped translation variants; it fuses traditional QE scores with bias‑aware reasoning from a large language model via a dynamic aggregation module that learns to weight each agent’s output according to detected bias. Experiments across several bias benchmarks and a WMT‑2023 MQM meta‑evaluation show that FairQE consistently yields more gender‑fair QE scores while matching or improving the baseline QE performance, demonstrating that bias mitigation can be achieved through a lightweight, agentic augmentation of existing QE models.


<details>
<summary>Abstract</summary>

Quality Estimation (QE) aims to assess machine translation quality without reference translations, but recent studies have shown that existing QE models exhibit systematic gender bias. In particular, they tend to favor masculine realizations in gender-ambiguous contexts and may assign higher scores to gender-misaligned translations even when gender is explicitly specified. To address these issues, we propose FairQE, a multi-agent-based, fairness-aware QE framework that mitigates gender bias in both gender-ambiguous and gender-explicit scenarios. FairQE detects gender cues, generates gender-flipped translation variants, and combines conventional QE scores with LLM-based bias-mitigating reasoning through a dynamic bias-aware aggregation mechanism. This design preserves the strengths of existing QE models while calibrating their gender-related biases in a plug-and-play manner. Extensive experiments across multiple gender bias evaluation settings demonstrate that FairQE consistently improves gender fairness over strong QE baselines. Moreover, under MQM-based meta-evaluation following the WMT 2023 Metrics Shared Task, FairQE achieves competitive or improved general QE performance. These results show that gender bias in QE can be effectively mitigated without sacrificing evaluation accuracy, enabling fairer and more reliable translation evaluation.

</details>


### 27. CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents

- **Authors:** Wenjie Fu, Xiaoting Qin, Jue Zhang, Qingwei Lin, Lukas Wutschitz, Robert Sim, Saravan Rajmohan, Dongmei Zhang
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21308v1](http://arxiv.org/abs/2604.21308v1)
- **PDF:** [https://arxiv.org/pdf/2604.21308v1](https://arxiv.org/pdf/2604.21308v1)
- **Categories:** cs.CR, cs.CL


> **Paper Summary**

CI‑Work introduces the first benchmark that measures *contextual integrity* for enterprise‑grade LLM agents: it models realistic workplace pipelines and 5 directional information‑flow scenarios, then tests whether agents can retrieve the necessary facts while suppressing sensitive context in dense‑retrieval settings. Using this benchmark, the authors evaluate leading LLMs (including the largest current models) and find that privacy breaches are common—15‑51 % of queries leak sensitive data (up to 26.7 % of the retrieved content), and higher task performance typically comes at the cost of greater privacy violations. The study shows that scaling model size or adding deeper reasoning does not mitigate leakage, leading the authors to argue that protecting enterprise workflows will require a shift from “bigger models” to *context‑centric* system designs that enforce privacy constraints at the retrieval/knowledge‑representation layer.


<details>
<summary>Abstract</summary>

Enterprise LLM agents can dramatically improve workplace productivity, but their core capability, retrieving and using internal context to act on a user's behalf, also creates new risks for sensitive information leakage. We introduce CI-Work, a Contextual Integrity (CI)-grounded benchmark that simulates enterprise workflows across five information-flow directions and evaluates whether agents can convey essential content while withholding sensitive context in dense retrieval settings. Our evaluation of frontier models reveals that privacy failures are prevalent (violation rates range from 15.8%-50.9%, with leakage reaching up to 26.7%) and uncovers a counterintuitive trade-off critical for industrial deployment: higher task utility often correlates with increased privacy violations. Moreover, the massive scale of enterprise data and potential user behavior further amplify this vulnerability. Simply increasing model size or reasoning depth fails to address the problem. We conclude that safeguarding enterprise workflows requires a paradigm shift, moving beyond model-centric scaling toward context-centric architectures.

</details>


### 28. Strategic Heterogeneous Multi-Agent Architecture for Cost-Effective Code Vulnerability Detection

- **Authors:** Zhaohui Geoffrey Wang
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21282v1](http://arxiv.org/abs/2604.21282v1)
- **PDF:** [https://arxiv.org/pdf/2604.21282v1](https://arxiv.org/pdf/2604.21282v1)
- **Categories:** cs.CR, cs.LG, cs.SE


> The paper introduces a game‑theoretically grounded, heterogeneous multi‑agent system for low‑cost, high‑accuracy code vulnerability detection. It assembles three cloud‑based LLM “experts” (DeepSeek‑V3) that analyze code from structural, pattern‑matching, and debugging viewpoints in parallel, and a lightweight on‑device verifier (Qwen3‑8B) that adversarially validates the experts’ predictions at near‑zero marginal cost. On 262 NIST Juliet samples covering 14 CWE types, this “3 + 1” architecture attains a 77.2 % F1 score (62.9 % precision, 100 % recall) for only $0.002 per sample—outperforming a single‑expert LLM baseline (71.4 % F1) and traditional static analysis—while achieving a 3× speedup and a statistically significant (+10.3 pp) precision gain from the verifier.


<details>
<summary>Abstract</summary>

Automated code vulnerability detection is critical for software security, yet existing approaches face a fundamental trade-off between detection accuracy and computational cost. We propose a heterogeneous multi-agent architecture inspired by game-theoretic principles, combining cloud-based LLM experts with a local lightweight verifier. Our "3+1" architecture deploys three cloud-based expert agents (DeepSeek-V3) that analyze code from complementary perspectives - code structure, security patterns, and debugging logic - in parallel, while a local verifier (Qwen3-8B) performs adversarial validation at zero marginal cost.
  We formalize this design through a two-layer game framework: (1) a cooperative game among experts capturing super-additive value from diverse perspectives, and (2) an adversarial verification game modeling quality assurance incentives.
  Experiments on 262 real samples from the NIST Juliet Test Suite across 14 CWE types, with balanced vulnerable and benign classes, demonstrate that our approach achieves a 77.2% F1 score with 62.9% precision and 100% recall at $0.002 per sample - outperforming both a single-expert LLM baseline (F1 71.4%) and Cppcheck static analysis (MCC 0). The adversarial verifier significantly improves precision (+10.3 percentage points, p < 1e-6, McNemar's test) by filtering false positives, while parallel execution achieves a 3.0x speedup.
  Our work demonstrates that game-theoretic design principles can guide effective heterogeneous multi-agent architectures for cost-sensitive software engineering tasks.

</details>


### 29. When Agents Look the Same: Quantifying Distillation-Induced Similarity in Tool-Use Behaviors

- **Authors:** Chenghao Yang, Yuning Zhang, Zhoufutu Wen, Tao Gong, Jiaheng Liu, Qi Chu, Nenghai Yu
- **Published:** 2026-04-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21255v1](http://arxiv.org/abs/2604.21255v1)
- **PDF:** [https://arxiv.org/pdf/2604.21255v1](https://arxiv.org/pdf/2604.21255v1)
- **Categories:** cs.CL


> **Contribution** – The paper introduces two novel metrics that explicitly separate *mandatory* task‑solving steps from *non‑mandatory* stylistic habits in LLM agents: **Response Pattern Similarity (RPS)** for measuring verbal alignment and **Action Graph Similarity (AGS)** for quantifying the similarity of tool‑use sequences as directed graphs. These metrics reveal how model distillation can cause agents to become “echoes” of a few teachers, a phenomenon that existing similarity measures fail to capture.

**Methodology** – The authors construct directed action graphs from agents’ tool‑use traces on the τ‑Bench and τ²‑Bench suites, then compute node‑level ( S_node ) and dependency‑level ( S_dep ) overlap (AGS). Parallelly, they compare verbatim reasoning traces with a token‑level alignment score (RPS). Experiments involve 18 models from eight providers, including a controlled teacher‑student distillation run, and the results are benchmarked against Claude Sonnet 4.5 (thinking).

**Key Findings** – (1) Within‑family model pairs are on average **5.9 percentage points** more similar in AGS than cross‑family pairs, indicating family‑specific convergence. (2) Kimi‑K2 (thinking) attains **82.6 % S_node** and **94.7 % S_dep**, surpassing Anthropic’s Opus 4.1, while RPS and AGS are only moderately correlated (r ≈ 0.49), confirming they capture distinct dimensions of convergence. (3) In the controlled distillation experiment, AGS reliably distinguishes convergence that is inherited from the teacher versus convergence that simply reflects overall performance gains, validating the metric as a diagnostic tool for distillation‑induced homogenization in agentic AI.


<details>
<summary>Abstract</summary>

Model distillation is a primary driver behind the rapid progress of LLM agents, yet it often leads to behavioral homogenization. Many emerging agents share nearly identical reasoning steps and failure modes, suggesting they may be distilled echoes of a few dominant teachers. Existing metrics, however, fail to distinguish mandatory behaviors required for task success from non-mandatory patterns that reflect a model's autonomous preferences. We propose two complementary metrics to isolate non-mandatory behavioral patterns: \textbf{Response Pattern Similarity (RPS)} for verbal alignment and \textbf{Action Graph Similarity (AGS)} for tool-use habits modeled as directed graphs. Evaluating 18 models from 8 providers on $τ$-Bench and $τ^2$-Bench against Claude Sonnet 4.5 (thinking), we find that within-family model pairs score 5.9 pp higher in AGS than cross-family pairs, and that Kimi-K2 (thinking) reaches 82.6\% $S_{\text{node}}$ and 94.7\% $S_{\text{dep}}$, exceeding Anthropic's own Opus 4.1. A controlled distillation experiment further confirms that AGS distinguishes teacher-specific convergence from general improvement. RPS and AGS capture distinct behavioral dimensions (Pearson $r$ = 0.491), providing complementary diagnostic signals for behavioral convergence in the agent ecosystem. Our code is available at https://github.com/Syuchin/AgentEcho.

</details>


### 30. Multi-Agent Empowerment and Emergence of Complex Behavior in Groups

- **Authors:** Tristan Shah, Ilya Nemenman, Daniel Polani, Stas Tiomkin
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21155v1](http://arxiv.org/abs/2604.21155v1)
- **PDF:** [https://arxiv.org/pdf/2604.21155v1](https://arxiv.org/pdf/2604.21155v1)
- **Categories:** cs.AI, cs.MA


> **Main contribution:** The paper extends the concept of *empowerment*—an information‑theoretic intrinsic motivation measuring an agent’s control over its future sensor states—from single agents to multi‑agent systems, and provides an efficient algorithm for its computation in joint action–state spaces.

**Methodology:** The authors define *multi‑agent empowerment* as the channel capacity between the joint action of a group and the resulting joint future observations, derive tractable approximations using variational bounds and Monte‑Carlo sampling, and apply the metric to two synthetic environments: (1) two agents linked by a tendon that transmits forces, and (2) a controllable Vicsek‑type flock where agents can influence each other’s headings.

**Key findings:** Maximizing multi‑agent empowerment produces distinct, self‑organized group behaviors without any explicit task reward—agents learn to coordinate their motions to preserve or increase collective control. In the tendon world the agents develop push‑pull strategies to keep the system manipulable, while in the flock they spontaneously form coherent, steerable clusters. These results demonstrate that empowerment can scale from driving individual actions to shaping higher‑level group organization, suggesting a powerful, task‑free driver for the emergence of complex cooperative behavior in agentic AI systems.


<details>
<summary>Abstract</summary>

Intrinsic motivations are receiving increasing attention, i.e. behavioral incentives that are not engineered, but emerge from the interaction of an agent with its surroundings. In this work we study the emergence of behaviors driven by one such incentive, empowerment, specifically in the context of more than one agent. We formulate a principled extension of empowerment to the multi-agent setting, and demonstrate its efficient calculation. We observe that this intrinsic motivation gives rise to characteristic modes of group-organization in two qualitatively distinct environments: a pair of agents coupled by a tendon, and a controllable Vicsek flock. This demonstrates the potential of intrinsic motivations such as empowerment to not just drive behavior for only individual agents but also higher levels of behavioral organization at scale.

</details>


### 31. Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction

- **Authors:** Abhishek Dharmaratnakar, Srivaths Ranganathan, Anushree Sinha, Debanshu Das
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21154v1](http://arxiv.org/abs/2604.21154v1)
- **PDF:** [https://arxiv.org/pdf/2604.21154v1](https://arxiv.org/pdf/2604.21154v1)
- **Categories:** cs.AI


> The paper introduces a novel multi‑agent system that brings generative AI into at‑home physiotherapy by autonomously creating and supervising personalized exercise videos. The framework chains four micro‑agents—(1) a Clinical Extraction Agent that converts unstructured medical notes into patient‑specific kinematic constraints, (2) a Video Synthesis Agent that feeds those constraints to foundational video‑generation models to produce custom exercise demos, (3) a Vision Processing Agent that runs real‑time pose estimation (MediaPipe), and (4) a Diagnostic Feedback Agent that interprets the pose data and delivers corrective cues. A prototype implementation demonstrates that the agents can jointly generate tailored videos and provide live, constraint‑aware feedback, suggesting that generative media combined with agentic decision‑making can feasibly scale personalized, safety‑critical tele‑rehabilitation.


<details>
<summary>Abstract</summary>

At-home physiotherapy compliance remains critically low due to a lack of personalized supervision and dynamic feedback. Existing digital health solutions rely on static, pre-recorded video libraries or generic 3D avatars that fail to account for a patient's specific injury limitations or home environment. In this paper, we propose a novel Multi-Agent System (MAS) architecture that leverages Generative AI and computer vision to close the tele-rehabilitation loop. Our framework consists of four specialized micro-agents: a Clinical Extraction Agent that parses unstructured medical notes into kinematic constraints; a Video Synthesis Agent that utilizes foundational video generation models to create personalized, patient-specific exercise videos; a Vision Processing Agent for real-time pose estimation; and a Diagnostic Feedback Agent that issues corrective instructions. We present the system architecture, detail the prototype pipeline using Large Language Models and MediaPipe, and outline our clinical evaluation plan. This work demonstrates the feasibility of combining generative media with agentic autonomous decision-making to scale personalized patient care safely and effectively.

</details>


### 32. Cross-Session Threats in AI Agents: Benchmark, Evaluation, and Algorithms

- **Authors:** Ari Azarafrooz
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21131v1](http://arxiv.org/abs/2604.21131v1)
- **PDF:** [https://arxiv.org/pdf/2604.21131v1](https://arxiv.org/pdf/2604.21131v1)
- **Categories:** cs.CR, cs.AI, cs.CL, cs.LG


> **Main contribution** – The paper introduces *CSTM‑Bench*, the first systematic benchmark for detecting attacks that span multiple AI‑agent sessions, together with a measurement framework and a lightweight detection algorithm that can operate under realistic memory constraints.

**Methodology** – The authors compile 26 executable attack taxonomies (covering kill‑chain stages and four cross‑session operations) anchored to seven identity predicates, and create two 54‑scenario splits (dilution vs. cross‑session) with matched benign confounders. They evaluate naïve session‑bound judges and a full‑log correlator, then propose a bounded‑memory “coreset memory reader” that retains the top‑K (K = 50) high‑signal fragments, and introduce the *CSR_prefix* stability metric. Performance is summarized by a composite score CSTM that balances F₁ on action‑level detection with prefix stability.

**Key findings** – Purely session‑bound or naïve full‑log approaches lose roughly 50 % of attack recall when moving from compositional to truly cross‑session scenarios, even within the context‑window limits of modern LLMs. In contrast, the coreset memory reader maintains high recall across both splits, and the combined CSTM metric identifies a Pareto‑optimal trade‑off between detection recall and serving‑time stability, demonstrating a viable path toward practical cross‑session guardrails for agentic AI.


<details>
<summary>Abstract</summary>

AI-agent guardrails are memoryless: each message is judged in isolation, so an adversary who spreads a single attack across dozens of sessions slips past every session-bound detector because only the aggregate carries the payload. We make three contributions to cross-session threat detection.
  (1) Dataset. CSTM-Bench is 26 executable attack taxonomies classified by kill-chain stage and cross-session operation (accumulate, compose, launder, inject_on_reader), each bound to one of seven identity anchors that ground-truth "violation" as a policy predicate, plus matched Benign-pristine and Benign-hard confounders. Released on Hugging Face as intrinsec-ai/cstm-bench with two 54-scenario splits: dilution (compositional) and cross_session (12 isolation-invisible scenarios produced by a closed-loop rewriter that softens surface phrasing while preserving cross-session artefacts).
  (2) Measurement. Framing cross-session detection as an information bottleneck to a downstream correlator LLM, we find that a session-bound judge and a Full-Log Correlator concatenating every prompt into one long-context call both lose roughly half their attack recall moving from dilution to cross_session, well inside any frontier context window. Scope: 54 scenarios per shard, one correlator family (Anthropic Claude), no prompt optimisation; we release it to motivate larger, multi-provider datasets.
  (3) Algorithm and metric. A bounded-memory Coreset Memory Reader retaining highest-signal fragments at $K=50$ is the only reader whose recall survives both shards. Because ranker reshuffles break KV-cache prefix reuse, we promote $\mathrm{CSR\_prefix}$ (ordered prefix stability, LLM-free) to a first-class metric and fuse it with detection into $\mathrm{CSTM} = 0.7 F_1(\mathrm{CSDA@action}, \mathrm{precision}) + 0.3 \mathrm{CSR\_prefix}$, benchmarking rankers on a single Pareto of recall versus serving stability.

</details>


### 33. AGNT2: Autonomous Agent Economies on Interaction-Optimized Layer 2 Infrastructure

- **Authors:** Anbang Ruan, Xing Zhang
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21129v1](http://arxiv.org/abs/2604.21129v1)
- **PDF:** [https://arxiv.org/pdf/2604.21129v1](https://arxiv.org/pdf/2604.21129v1)
- **Categories:** cs.MA, cs.AI, cs.DC


> The paper introduces **AGNT2**, a three‑tier blockchain stack specifically engineered for high‑frequency, semantically rich interactions among autonomous AI agents, arguing that existing Layer‑2 solutions optimized for human‑driven finance are ill‑suited for agent economies. It combines a side‑car pattern that wraps any Dockerized service as an on‑chain agent, ultra‑low‑latency bilateral state‑channel “Layer Top” for pairwise calls, a dependency‑aware sequenced roll‑up “Layer Core” for multi‑party coordination, and a fraud‑proof‑backed settlement “Layer Root” anchored to any EVM L1, while redefining identity, reputation, capabilities, and session state as first‑class protocol objects. Simulations and early prototype measurements show that the design can theoretically sustain 10 M+ aggregate TPS, but current data‑availability limits restrict practical throughput to 10 K–100 K TPS, highlighting a ≈100× scalability gap that must be closed for a full‑scale agentic AI economy.


<details>
<summary>Abstract</summary>

Current blockchain Layer 2 solutions, including Optimism, Arbitrum, zkSync, and their derivatives, optimize for human-initiated financial transactions. Autonomous AI agents instead generate high-frequency, semantically rich service invocations among mutually untrusting principals. Existing chains treat those interactions as generic calldata, forcing identity, escrow, dependency ordering, and session state to be encoded above the execution layer at the wrong cost point. We present AGNT2, a three-tier stack purpose-built for agent and microservice coordination on-chain. AGNT2 combines: (1) a sidecar deployment pattern that turns any Docker container into an on-chain agent without application-code modification; (2) Layer Top P2P state channels for established bilateral pairs (<100 ms, rough design target 1K-5K TPS per pair, 10M+ aggregate TPS design envelope under endpoint-resource limits), Layer Core as a dependency-aware sequenced rollup for first-contact and multi-party interactions (500 ms-2 s, 300K-500K TPS design target), and Layer Root settlement with computational fraud proofs anchored to any EVM L1; and (3) an agent-native execution environment plus interaction trie that make service invocation, identity, reputation, capabilities, and session context first-class protocol objects. This paper focuses on the execution-layer systems problem: sequencing, state, settlement, and the data-availability (DA) bandwidth gap that bounds all three. Simulation and analytical modeling support the architecture, and prototype measurements validate selected components, but no end-to-end Layer Core implementation exists yet. Practical deployment is currently constrained to roughly 10K-100K TPS by DA throughput, leaving a ~100x gap at the target ceiling. AGNT2 argues that the agent economy requires a dedicated execution layer rather than a general-purpose chain repurposed for agents.

</details>


### 34. Structural Quality Gaps in Practitioner AI Governance Prompts: An Empirical Study Using a Five-Principle Evaluation Framework

- **Authors:** Christo Zietsman
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21090v1](http://arxiv.org/abs/2604.21090v1)
- **PDF:** [https://arxiv.org/pdf/2604.21090v1](https://arxiv.org/pdf/2604.21090v1)
- **Categories:** cs.SE, cs.AI


> **Main contribution** – The paper presents a novel, theory‑grounded evaluation framework (five principles derived from computability theory, proof theory, and Bayesian epistemology) for checking the structural completeness of AI‑governance prompts that act as executable specifications for autonomous agents.

**Methodology** – The authors apply this framework in a static‑analysis study of 34 publicly available AGENTS.md files (34 file‑model pairs) harvested from GitHub, scoring each prompt against the five principles and identifying missing elements such as data‑classification clauses and assessment rubrics.

**Key findings** – About 37 % of the examined governance prompts fall below the completeness threshold, most often lacking explicit data‑classification and rubric specifications; the study uncovers a systematic “artefact classification” gap in the AGENTS.md convention and shows that automated analysis can reliably detect these structural deficiencies, pointing to concrete tool‑support opportunities for requirements‑engineering in agentic AI development.


<details>
<summary>Abstract</summary>

AI governance programmes increasingly rely on natural language prompts to constrain and direct AI agent behaviour. These prompts function as executable specifications: they define the agent's mandate, scope, and quality criteria. Despite this role, no systematic framework exists for evaluating whether a governance prompt is structurally complete. We introduce a five-principle evaluation framework grounded in computability theory, proof theory, and Bayesian epistemology, and apply it to an empirical corpus of 34 publicly available AGENTS.md governance files sourced from GitHub. Our evaluation reveals that 37% of evaluated file-model pairs score below the structural completeness threshold, with data classification and assessment rubric criteria most frequently absent. These results suggest that practitioner-authored governance prompts exhibit consistent structural patterns that automated static analysis could detect and remediate. We discuss implications for requirements engineering practice in AI-assisted development contexts, identify a previously undocumented artefact classification gap in the AGENTS.md convention, and propose directions for tool support.

</details>


### 35. The Last Harness You'll Ever Build

- **Authors:** Haebin Seong, Li Yin, Haoran Zhang
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.21003v1](http://arxiv.org/abs/2604.21003v1)
- **PDF:** [https://arxiv.org/pdf/2604.21003v1](https://arxiv.org/pdf/2604.21003v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces a fully automated two‑level framework for “harness engineering” that removes the need for human‑crafted prompts, tool‑integration logic, and evaluation criteria when adapting foundation‑model agents to new, complex domains.  

**Methodology:** The first level – the **Harness Evolution Loop** – lets a worker agent \(W_{\mathcal{H}}\) attempt a task, an evaluator agent \(V\) adversarially diagnose failures and assign a score, and an evolution agent \(E\) revise the harness \(\mathcal{H}\) using the full interaction history. The second level – the **Meta‑Evolution Loop** – treats the entire evolution protocol \(Λ = (W_{\mathcal{H}}, \mathcal{H}^{(0)}, V, E)\) as a meta‑learnable object, training it across a distribution of tasks so that a single meta‑protocol \(Λ^{\text{(best)}}\) can rapidly converge to an effective harness for any new task without human intervention.  

**Key findings:** Experiments across heterogeneous enterprise workflows (web navigation, research pipelines, code review, customer support) show that meta‑evolved protocols achieve comparable or better task performance than hand‑engineered harnesses while reducing adaptation time from hours/days to a few automated iterations, thereby demonstrating a practical path toward self‑designing, domain‑agnostic AI agents.


<details>
<summary>Abstract</summary>

AI agents are increasingly deployed on complex, domain-specific workflows -- navigating enterprise web applications that require dozens of clicks and form fills, orchestrating multi-step research pipelines that span search, extraction, and synthesis, automating code review across unfamiliar repositories, and handling customer escalations that demand nuanced domain knowledge. \textbf{Each new task domain requires painstaking, expert-driven harness engineering}: designing the prompts, tools, orchestration logic, and evaluation criteria that make a foundation model effective. We present a two-level framework that automates this process. At the first level, the \textbf{Harness Evolution Loop} optimizes a worker agent's harness $\mathcal{H}$ for a single task: a Worker Agent $W_{\mathcal{H}}$ executes the task, an Evaluator Agent $V$ adversarially diagnoses failures and scores performance, and an Evolution Agent $E$ modifies the harness based on the full history of prior attempts. At the second level, the \textbf{Meta-Evolution Loop} optimizes the evolution protocol $Λ= (W_{\mathcal{H}}, \mathcal{H}^{(0)}, V, E)$ itself across diverse tasks, \textbf{learning a protocol $Λ^{(\text{best})}$ that enables rapid harness convergence on any new task -- so that adapting an agent to a novel domain requires no human harness engineering at all.} We formalize the correspondence to meta-learning and present both algorithms. The framework \textbf{shifts manual harness engineering into automated harness engineering}, and takes one step further -- \textbf{automating the design of the automation itself}.

</details>


### 36. Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models

- **Authors:** Yannis Belkhiter, Giulio Zizzo, Sergio Maffeis, Seshu Tirupathi, John D. Kelleher
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20994v1](http://arxiv.org/abs/2604.20994v1)
- **PDF:** [https://arxiv.org/pdf/2604.20994v1](https://arxiv.org/pdf/2604.20994v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> The paper presents **Function Hijacking Attacks (FHA)**, a new class of threats that manipulate the tool‑selection step of agentic LLMs to compel them to call an attacker‑controlled function, irrespective of the query’s semantics or the available function inventory. By training universal adversarial functions, the authors show that a single malicious function can hijack tool selection across many prompts, achieving 70 %–100 % attack success rates on five instruction‑ and reasoning‑oriented models using the BFCL benchmark. These results expose a systemic vulnerability in function‑calling interfaces and underscore the urgent need for robust guardrails and security mechanisms in agentic AI systems.


<details>
<summary>Abstract</summary>

The growth of agentic AI has drawn significant attention to function calling Large Language Models (LLMs), which are designed to extend the capabilities of AI-powered system by invoking external functions. Injection and jailbreaking attacks have been extensively explored to showcase the vulnerabilities of LLMs to user prompt manipulation. The expanded capabilities of agentic models introduce further vulnerabilities via their function calling interface. Recent work in LLM security showed that function calling can be abused, leading to data tampering and theft, causing disruptive behavior such as endless loops, or causing LLMs to produce harmful content in the style of jailbreaking attacks. This paper introduces a novel function hijacking attack (FHA) that manipulates the tool selection process of agentic models to force the invocation of a specific, attacker-chosen function. While existing attacks focus on semantic preference of the model for function-calling tasks, we show that FHA is largely agnostic to the context semantics and robust to the function sets, making it applicable across diverse domains. We further demonstrate that FHA can be trained to produce universal adversarial functions, enabling a single attacked function to hijack tool selection across multiple queries and payload configurations. We conducted experiments on 5 different models, including instructed and reasoning variants, reaching 70% to 100% ASR over the established BFCL dataset. Our findings further demonstrate the need for strong guardrails and security modules for agentic systems.

</details>


### 37. Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem

- **Authors:** Travis LaCroix
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20805v1](http://arxiv.org/abs/2604.20805v1)
- **PDF:** [https://arxiv.org/pdf/2604.20805v1](https://arxiv.org/pdf/2604.20805v1)
- **Categories:** cs.CY, cs.AI, cs.MA


> The paper reframes AI value‑alignment as a governance problem by extending the classic principal‑agent model into three interacting axes—objectives, information, and principals—showing that misalignment arises from how goals are specified, what information agents have, and whose interests are represented. Using this three‑axis decomposition, the author demonstrates that alignment cannot be treated as a single technical property of a model but must be managed through institutional processes that mediate trade‑offs among competing stakeholder values. Consequently, the work argues that effective AI alignment requires pluralistic, context‑dependent governance mechanisms rather than purely engineering solutions.


<details>
<summary>Abstract</summary>

The value alignment problem for artificial intelligence (AI) is often framed as a purely technical or normative challenge, sometimes focused on hypothetical future systems. I argue that the problem is better understood as a structural question about governance: not whether an AI system is aligned in the abstract, but whether it is aligned enough, for whom, and at what cost. Drawing on the principal-agent framework from economics, this paper reconceptualises misalignment as arising along three interacting axes: objectives, information, and principals. The three-axis framework provides a systematic way of diagnosing why misalignment arises in real-world systems and clarifies that alignment cannot be treated as a single technical property of models but an outcome shaped by how objectives are specified, how information is distributed, and whose interests count in practice. The core contribution of this paper is to show that the three-axis decomposition implies that alignment is fundamentally a problem of governance rather than engineering alone. From this perspective, alignment is inherently pluralistic and context-dependent, and resolving misalignment involves trade-offs among competing values. Because misalignment can occur along each axis -- and affect stakeholders differently -- the structural description shows that alignment cannot be "solved" through technical design alone, but must be managed through ongoing institutional processes that determine how objectives are set, how systems are evaluated, and how affected communities can contest or reshape those decisions.

</details>


### 38. SWE-chat: Coding Agent Interactions From Real Users in the Wild

- **Authors:** Joachim Baumann, Vishakh Padmakumar, Xiang Li, John Yang, Diyi Yang, Sanmi Koyejo
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20779v1](http://arxiv.org/abs/2604.20779v1)
- **PDF:** [https://arxiv.org/pdf/2604.20779v1](https://arxiv.org/pdf/2604.20779v1)
- **Categories:** cs.AI, cs.CY, cs.SE


> **Main contribution:** The paper introduces **SWE‑chat**, the first large‑scale, continuously updated dataset of real‑world interactions between developers and AI coding agents, comprising 6 K sessions, >63 K user prompts and 355 K agent tool calls collected automatically from public repositories.

**Methodology:** The authors built a pipeline that discovers public coding‑agent sessions, extracts the full conversational trace, and attributes each line of code to either the human or the agent. They then performed an empirical analysis of the dataset to characterize usage patterns, failure modes, and security outcomes.

**Key findings for agentic AI:** Developer workflows exhibit a bimodal “vibe‑coding” pattern—agents write almost all committed code in 41 % of sessions, while humans write everything in 23 %. Overall, only **44 %** of agent‑generated code survives into commits and it introduces **more security vulnerabilities** than human code; users intervene (corrections, failure reports, interruptions) in **44 %** of interaction turns, highlighting substantial inefficiency and the need for more robust, safety‑aware coding agents.


<details>
<summary>Abstract</summary>

AI coding agents are being adopted at scale, yet we lack empirical evidence on how people actually use them and how much of their output is useful in practice. We present SWE-chat, the first large-scale dataset of real coding agent sessions collected from open-source developers in the wild. The dataset currently contains 6,000 sessions, comprising more than 63,000 user prompts and 355,000 agent tool calls. SWE-chat is a living dataset; our collection pipeline automatically and continually discovers and processes sessions from public repositories. Leveraging SWE-chat, we provide an initial empirical characterization of real-world coding agent usage and failure modes. We find that coding patterns are bimodal: in 41% of sessions, agents author virtually all committed code ("vibe coding"), while in 23%, humans write all code themselves. Despite rapidly improving capabilities, coding agents remain inefficient in natural settings. Just 44% of all agent-produced code survives into user commits, and agent-written code introduces more security vulnerabilities than code authored by humans. Furthermore, users push back against agent outputs -- through corrections, failure reports, and interruptions -- in 44% of all turns. By capturing complete interaction traces with human vs. agent code authorship attribution, SWE-chat provides an empirical foundation for moving beyond curated benchmarks towards an evidence-based understanding of how AI agents perform in real developer workflows.

</details>


### 39. Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization

- **Authors:** Shan He, Runze Wang, Zhuoyun Du, Huiyu Bai, Zouying Cao, Yu Cheng, Bo Zheng
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20714v1](http://arxiv.org/abs/2604.20714v1)
- **PDF:** [https://arxiv.org/pdf/2604.20714v1](https://arxiv.org/pdf/2604.20714v1)
- **Categories:** cs.AI


> The paper introduces **Textual Parameter Graph Optimization (TPGO)**, a self‑evolving framework for multi‑agent systems that treats the whole MAS as a *Textual Parameter Graph* (TPG) whose nodes (agents, tools, workflows) can be optimized via natural‑language feedback. Its core meta‑learning component, **Group Relative Agent Optimization (GRAO)**, extracts “textual gradients” from execution traces and learns from past optimization episodes to propose increasingly effective structural and prompt‑level updates. Experiments on GAIA and MCP‑Universe benchmarks show that TPGO outperforms existing flat‑prompt tuning methods, markedly raising success rates and demonstrating that agents can autonomously improve their own design and coordination.


<details>
<summary>Abstract</summary>

Designing and optimizing multi-agent systems (MAS) is a complex, labor-intensive process of "Agent Engineering." Existing automatic optimization methods, primarily focused on flat prompt tuning, lack the structural awareness to debug the intricate web of interactions in MAS. More critically, these optimizers are static; they do not learn from experience to improve their own optimization strategies. To address these gaps, we introduce Textual Parameter Graph Optimization (TPGO), a framework that enables a multi-agent system to learn to evolve. TPGO first models the MAS as a Textual Parameter Graph (TPG), where agents, tools, and workflows are modular, optimizable nodes. To guide evolution, we derive "textual gradients," structured natural language feedback from execution traces, to pinpoint failures and suggest granular modifications. The core of our framework is Group Relative Agent Optimization (GRAO), a novel meta-learning strategy that learns from historical optimization experiences. By analyzing past successes and failures, GRAO becomes progressively better at proposing effective updates, allowing the system to learn how to optimize itself. Extensive experiments on complex benchmarks like GAIA and MCP-Universe show that TPGO significantly enhances the performance of state-of-the-art agent frameworks, achieving higher success rates through automated, self-improving optimization.

</details>


### 40. Cooperative Profiles Predict Multi-Agent LLM Team Performance in AI for Science Workflows

- **Authors:** Shivani Kumar, Adarsh Bharathwaj, David Jurgens
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20658v1](http://arxiv.org/abs/2604.20658v1)
- **PDF:** [https://arxiv.org/pdf/2604.20658v1](https://arxiv.org/pdf/2604.20658v1)
- **Categories:** cs.CL


> The paper shows that an LLM’s “cooperative disposition” – measured by its behavior in six classic behavioral‑economics games – is a strong predictor of how well that model will perform as a member of a multi‑agent scientific team. By benchmarking 35 open‑weight LLMs on these games and then letting them cooperate under shared GPU/credit budgets to analyse data, build models, and write reports, the authors demonstrate that agents that succeed in coordination and invest in multiplicative team production (rather than greedy shortcuts) generate more accurate, higher‑quality, and more complete scientific outputs. Importantly, the predictive power of the game‑derived cooperative profiles persists after accounting for overall model size and standard ability metrics, suggesting that cooperative fitness is a distinct, cheaply‑measurable property useful for screening LLMs before costly multi‑agent deployment.


<details>
<summary>Abstract</summary>

Multi-agent systems built from teams of large language models (LLMs) are increasingly deployed for collaborative scientific reasoning and problem-solving. These systems require agents to coordinate under shared constraints, such as GPUs or credit balances, where cooperative behavior matters. Behavioral economics provides a rich toolkit of games that isolate distinct cooperation mechanisms, yet it remains unknown whether a model's behavior in these stylized settings predicts its performance in realistic collaborative tasks. Here, we benchmark 35 open-weight LLMs across six behavioral economics games and show that game-derived cooperative profiles robustly predict downstream performance in AI-for-Science tasks, where teams of LLM agents collaboratively analyze data, build models, and produce scientific reports under shared budget constraints. Models that effectively coordinate games and invest in multiplicative team production (rather than greedy strategies) produce better scientific reports across three outcomes, accuracy, quality, and completion. These associations hold after controlling for multiple factors, indicating that cooperative disposition is a distinct, measurable property of LLMs not reducible to general ability. Our behavioral games framework thus offers a fast and inexpensive diagnostic for screening cooperative fitness before costly multi-agent deployment.

</details>


### 41. CHORUS: An Agentic Framework for Generating Realistic Deliberation Data

- **Authors:** A. Koursaris, G. Domalis, A. Apostolopoulou, K. Kanaris, D. Tsakalidis, I. E. Livieris
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20651v1](http://arxiv.org/abs/2604.20651v1)
- **PDF:** [https://arxiv.org/pdf/2604.20651v1](https://arxiv.org/pdf/2604.20651v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **CHORUS**, an agentic framework that synthesizes realistic online deliberation threads by coordinating multiple LLM‑driven “actors” each endowed with a stable persona, memory of the conversation, and a Poisson‑process model of posting times, plus structured tool use for external information access.

**Methodology:** CHORUS treats each participant as an autonomous agent that (1) maintains a dialogue memory, (2) follows a persona‑consistent policy for content generation, (3) decides when to speak according to a calibrated Poisson process that mimics heterogeneous user engagement, and (4) can invoke external tools (search, citation) to enrich arguments. The system was deployed on the Deliberate platform and evaluated by 30 domain experts.

**Key findings:** Expert evaluation showed that CHORUS‑generated discussions scored high on **content realism**, **coherence**, and **analytical utility**, confirming that the framework can produce large‑scale, high‑quality deliberation data suitable for studying and training agentic AI systems that need to model human‑like discourse.


<details>
<summary>Abstract</summary>

Understanding the intricate dynamics of online discourse depends on large-scale deliberation data, a resource that remains scarce across interactive web platforms due to restrictive accessibility policies, ethical concerns and inconsistent data quality. In this paper, we propose Chorus, an agentic framework, which orchestrates LLM-powered actors with behaviorally consistent personas to generate realistic deliberation discussions. Each actor is governed by an autonomous agent equipped with memory of the evolving discussion, while participation timing is governed by a principled Poisson process-based temporal model, which approximates the heterogeneous engagement patterns of real users. The framework is further supported by structured tool usage, enabling actors to access external resources and facilitating integration with interactive web platforms. The framework was deployed on the \textsc{Deliberate} platform and evaluated by 30 expert participants across three dimensions: content realism, discussion coherence and analytical utility, confirming Chorus as a practical tool for generating high-quality deliberation data suitable for online discourse analysis

</details>


### 42. pAI/MSc: ML Theory Research with Humans on the Loop

- **Authors:** Mahmoud Abdelmoneum, Pierfrancesco Beneventano, Tomaso Poggio
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20622v1](http://arxiv.org/abs/2604.20622v1)
- **PDF:** [https://arxiv.org/pdf/2604.20622v1](https://arxiv.org/pdf/2604.20622v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper introduces **pAI/MSc**, an open‑source, modular multi‑agent platform that embeds humans in the research loop to dramatically accelerate the execution of a specified scientific hypothesis—particularly in machine‑learning theory and related quantitative domains—into a fully sourced, mathematically rigorous, and experiment‑validated manuscript draft. The system integrates specialized agents for literature retrieval, formal reasoning, experiment design, and writing, coordinated through a lightweight orchestration layer that lets researchers intervene only at key decision points, thereby cutting the manual steering effort by orders of magnitude. Empirical evaluations on several ML‑theory projects show that pAI/MSc reduces total researcher time from weeks to days while maintaining comparable technical quality and citation coverage, demonstrating a practical, human‑in‑the‑loop alternative to fully autonomous scientific agents.


<details>
<summary>Abstract</summary>

We present pAI/MSc, an open-source, customizable, modular multi-agent system for academic research workflows. Our goal is not autonomous scientific ideation, nor fully automated research. It is narrower and more practical: to reduce by orders of magnitude the human steering required to turn a specified hypothesis into a literature-grounded, mathematically established, experimentally supported, submission-oriented manuscript draft. pAI/MSc is built with a current emphasis on machine learning theory and adjacent quantitative fields.

</details>


### 43. A Hierarchical MARL-Based Approach for Coordinated Retail P2P Trading and Wholesale Market Participation of DERs

- **Authors:** Patrick Wilk, Ethan Cantor, Yikui Liu, Jie Li
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20586v1](http://arxiv.org/abs/2604.20586v1)
- **PDF:** [https://arxiv.org/pdf/2604.20586v1](https://arxiv.org/pdf/2604.20586v1)
- **Categories:** cs.LG, eess.SY


> **Main contribution** – The paper introduces a hierarchical multi‑agent reinforcement‑learning (MARL) framework that lets individual prosumers first trade electricity in a peer‑to‑peer (P2P) retail auction and then, through an aggregation layer, take coordinated positions in the wholesale market; a Stackelberg game is used to formalize the leader‑follower interaction between the aggregator and the wholesale market operator.

**Methodology** – Each prosumer is modeled as a deep‑RL agent that learns optimal bidding/consumption policies in the P2P auction; a higher‑level aggregator agent, also trained via deep RL, receives the prosumers’ offers and decides collective wholesale bids while respecting network constraints. The hierarchical agents are trained jointly in a simulated market environment, and the Stackelberg equilibrium is approximated through iterative best‑response updates between the aggregator (leader) and the wholesale market (follower).

**Key findings** – Simulations show that the hierarchical MARL system yields higher overall social welfare, lower price volatility, and improved utilization of distributed energy resources compared with non‑coordinated or centrally‑optimized baselines. The Stackelberg‑guided coordination further reduces imbalance penalties for the aggregator, demonstrating that agentic, learning‑based coordination can effectively bridge retail P2P trading and wholesale market participation in future decentralized power systems.


<details>
<summary>Abstract</summary>

The ongoing shift towards decentralization of the electric energy sector, driven by the growing electrification across end-use sectors, and widespread adoption of distributed energy resources (DERs), necessitates their active participation in the electricity markets to support grid operations. Furthermore, with bi-directional energy and communication flows becoming standard, intelligent, easy-to-deploy, resource-conservative demand-side participation is expected to play a critical role in securing power grid operational flexibility and market efficiency. This work proposes a market engagement framework that leverages a hierarchical multi-agent deep reinforcement learning (MARL) approach to enable individual prosumers to participate in peer-to-peer retail auctions and further aggregate these intelligent prosumers to facilitate effective DER participation in wholesale markets. Ultimately, a Stackelberg game is proposed to coordinate this hierarchical MARL-based DER market participation framework toward enhanced market performance.

</details>


### 44. Trust, Lies, and Long Memories: Emergent Social Dynamics and Reputation in Multi-Round Avalon with LLM Agents

- **Authors:** Suveen Ellawela
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20582v1](http://arxiv.org/abs/2604.20582v1)
- **PDF:** [https://arxiv.org/pdf/2604.20582v1](https://arxiv.org/pdf/2604.20582v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> The paper demonstrates that large‑language‑model agents develop authentic reputation and deception dynamics when they play The Resistance: Avalon across many rounds while preserving a memory of past interactions. By end‑to‑end prompting agents to retain cross‑game role and behavior histories, the authors run 188 repeated games and find that (i) agents spontaneously form role‑conditional reputations that affect team selection—high‑reputation players are 46 % more likely to be included—and (ii) higher‑effort reasoning enables more sophisticated cheating, with evil agents deliberately passing early missions to build trust in 75 % of high‑effort games versus 36 % in low‑effort ones. These results show that even without explicit reputation mechanisms, LLM agents can exhibit emergent social dynamics relevant for designing trustworthy, multi‑agent AI systems.


<details>
<summary>Abstract</summary>

We study emergent social dynamics in LLM agents playing The Resistance: Avalon, a hidden-role deception game. Unlike prior work on single-game performance, our agents play repeated games while retaining memory of previous interactions, including who played which roles and how they behaved, enabling us to study how social dynamics evolve. Across 188 games, two key phenomena emerge. First, reputation dynamics emerge organically when agents retain cross-game memory: agents reference past behavior in statements like "I am wary of repeating last game's mistake of over-trusting early success." These reputations are role-conditional: the same agent is described as "straightforward" when playing good but "subtle" when playing evil, and high-reputation players receive 46% more team inclusions. Second, higher reasoning effort supports more strategic deception: evil players more often pass early missions to build trust before sabotaging later ones, 75% in high-effort games vs 36% in low-effort games. Together, these findings show that repeated interaction with memory gives rise to measurable reputation and deception dynamics among LLM agents.

</details>


### 45. Enhancing Research Idea Generation through Combinatorial Innovation and Multi-Agent Iterative Search Strategies

- **Authors:** Shuai Chen, Chengzhi Zhang
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20548v1](http://arxiv.org/abs/2604.20548v1)
- **PDF:** [https://arxiv.org/pdf/2604.20548v1](https://arxiv.org/pdf/2604.20548v1)
- **Categories:** cs.CL, cs.AI, cs.DL, cs.IR


> **Contribution:**  
The paper introduces **MAGenIdeas**, a multi‑agent framework that iteratively combines combinatorial‑innovation principles with LLM reasoning to produce research ideas that are more diverse and novel than those generated by existing single‑agent LLM approaches.

**Methodology:**  
A set of specialized LLM agents (generator, evaluator, and refiner) engage in a cyclic search loop: agents first propose idea components, then another agent scores novelty and relevance, and a third agent revises the proposals based on feedback. This iterative planning process is grounded in combinatorial innovation theory, enabling systematic recombination of knowledge fragments from the literature.

**Key Findings:**  
In NLP benchmark tasks, MAGenIdeas outperforms state‑of‑the‑art baselines on quantitative diversity and novelty metrics, and human judges rate its outputs as comparable to ideas from accepted conference papers—situated between accepted and rejected submissions. The results demonstrate that structured multi‑agent iteration can substantially elevate the quality of AI‑driven research idea generation.


<details>
<summary>Abstract</summary>

Scientific progress depends on the continual generation of innovative re-search ideas. However, the rapid growth of scientific literature has greatly increased the cost of knowledge filtering, making it harder for researchers to identify novel directions. Although existing large language model (LLM)-based methods show promise in research idea generation, the ideas they produce are often repetitive and lack depth. To address this issue, this study proposes a multi-agent iterative planning search strategy inspired by com-binatorial innovation theory. The framework combines iterative knowledge search with an LLM-based multi-agent system to generate, evaluate, and re-fine research ideas through repeated interaction, with the goal of improving idea diversity and novelty. Experiments in the natural language processing domain show that the proposed method outperforms state-of-the-art base-lines in both diversity and novelty. Further comparison with ideas derived from top-tier machine learning conference papers indicates that the quality of the generated ideas falls between that of accepted and rejected papers. These results suggest that the proposed framework is a promising approach for supporting high-quality research idea generation. The source code and dataset used in this paper are publicly available on Github repository: https://github.com/ChenShuai00/MAGenIdeas. The demo is available at https://huggingface.co/spaces/cshuai20/MAGenIdeas.

</details>


### 46. MedSkillAudit: A Domain-Specific Audit Framework for Medical Research Agent Skills

- **Authors:** Yingyong Hou, Xinyuan Lao, Huimei Wang, Qianyu Yao, Wei Chen, Bocheng Huang, Fei Sun, Yuxian Lv, Weiqi Lei, Xueqian Wen, Pengfei Xia, Zhujun Tan, Shengyang Xie
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20441v1](http://arxiv.org/abs/2604.20441v1)
- **PDF:** [https://arxiv.org/pdf/2604.20441v1](https://arxiv.org/pdf/2604.20441v1)
- **Categories:** cs.AI


> The paper introduces **MedSkillAudit**, a domain‑specific, layered auditing framework (skill‑auditor@1.0) designed to evaluate the readiness of modular medical‑research AI skills before they are released. By applying the framework to 75 skills across five research categories and comparing its outputs (quality scores, release dispositions, high‑risk flags) with independent expert judgments, the authors show that MedSkillAudit achieves higher agreement with consensus expert scores (ICC = 0.449) than the experts agree with each other (ICC = 0.300), and produces less score variance than human raters. The results suggest that a structured, specialty‑focused pre‑deployment audit can reliably complement generic AI safety checks and help enforce scientific integrity, reproducibility, and boundary safety for agentic AI used in medical research.


<details>
<summary>Abstract</summary>

Background: Agent skills are increasingly deployed as modular, reusable capability units in AI agent systems. Medical research agent skills require safeguards beyond general-purpose evaluation, including scientific integrity, methodological validity, reproducibility, and boundary safety. This study developed and preliminarily evaluated a domain-specific audit framework for medical research agent skills, with a focus on reliability against expert review. Methods: We developed MedSkillAudit (skill-auditor@1.0), a layered framework assessing skill release readiness before deployment. We evaluated 75 skills across five medical research categories (15 per category). Two experts independently assigned a quality score (0-100), an ordinal release disposition (Production Ready / Limited Release / Beta Only / Reject), and a high-risk failure flag. System-expert agreement was quantified using ICC(2,1) and linearly weighted Cohen's kappa, benchmarked against the human inter-rater baseline. Results: The mean consensus quality score was 72.4 (SD = 13.0); 57.3% of skills fell below the Limited Release threshold. MedSkillAudit achieved ICC(2,1) = 0.449 (95% CI: 0.250-0.610), exceeding the human inter-rater ICC of 0.300. System-consensus score divergence (SD = 9.5) was smaller than inter-expert divergence (SD = 12.4), with no directional bias (Wilcoxon p = 0.613). Protocol Design showed the strongest category-level agreement (ICC = 0.551); Academic Writing showed a negative ICC (-0.567), reflecting a structural rubric-expert mismatch. Conclusions: Domain-specific pre-deployment audit may provide a practical foundation for governing medical research agent skills, complementing general-purpose quality checks with structured audit workflows tailored to scientific use cases.

</details>


### 47. Graph2Counsel: Clinically Grounded Synthetic Counseling Dialogue Generation from Client Psychological Graphs

- **Authors:** Aishik Mandal, Hiba Arnaout, Clarissa W. Ong, Juliet Bockhorst, Kate Sheehan, Rachael Moldow, Tanmoy Chakraborty, Iryna Gurevych
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20382v1](http://arxiv.org/abs/2604.20382v1)
- **PDF:** [https://arxiv.org/pdf/2604.20382v1](https://arxiv.org/pdf/2604.20382v1)
- **Categories:** cs.CL


> **Main contribution:** Graph2Counsel introduces a novel pipeline for generating clinically grounded synthetic counseling dialogues by conditioning LLMs on *Client Psychological Graphs* (CPGs) that explicitly encode the inter‑relationships among a client’s thoughts, emotions, and behaviors, thereby addressing the psychological inconsistency problem of existing text‑only synthetic datasets.

**Methodology:** The authors construct CPGs for 76 diverse client profiles, then use a structured prompting framework that combines counselor‑strategy templates with chain‑of‑thought and multi‑agent feedback prompting to drive a base LLM to produce 760 full counseling sessions. The generated corpus is evaluated by mental‑health experts and used to fine‑tune an open‑source model.

**Key findings for agentic AI:** Expert ratings show the Graph2Counsel dialogues markedly outperform prior synthetic corpora on specificity, counselor competence, authenticity, flow, and safety (Krippendorff’s α = 0.70). Fine‑tuning on this data yields measurable gains on the CounselingBench and CounselBench benchmarks, demonstrating that structurally grounded prompts can create high‑quality, safety‑aware agentic behavior for high‑risk domains like mental‑health support.


<details>
<summary>Abstract</summary>

Rising demand for mental health support has increased interest in using Large Language Models (LLMs) for counseling. However, adapting LLMs to this high-risk safety-critical domain is hindered by the scarcity of real-world counseling data due to privacy constraints. Synthetic datasets provide a promising alternative, but existing approaches often rely on unstructured or semi-structured text inputs and overlook structural dependencies between a client's cognitive, emotional, and behavioral states, often producing psychologically inconsistent interactions and reducing data realism and quality. We introduce Graph2Counsel, a framework for generating synthetic counseling sessions grounded in Client Psychological Graphs (CPGs) that encode relationships among clients' thoughts, emotions, and behaviors. Graph2Counsel employs a structured prompting pipeline guided by counselor strategies and CPG, and explores prompting strategies including CoT (Wei et al., 2022) and Multi-Agent Feedback (Li et al., 2025a). Graph2Counsel produces 760 sessions from 76 CPGs across diverse client profiles. In expert evaluation, our dataset outperforms prior datasets on specificity, counselor competence, authenticity, conversational flow, and safety, with substantial inter-annotator agreement (Krippendorff's $α$ = 0.70). Fine-tuning an open-source model on this dataset improves performance on CounselingBench (Nguyen et al., 2025) and CounselBench (Li et al., 2025b), showing downstream utility. We also make our code and data public.

</details>


### 48. Bimanual Robot Manipulation via Multi-Agent In-Context Learning

- **Authors:** Alessio Palma, Indro Spinelli, Vignesh Prasad, Luca Scofano, Yufeng Jin, Georgia Chalvatzaki, Fabio Galasso
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20348v1](http://arxiv.org/abs/2604.20348v1)
- **PDF:** [https://arxiv.org/pdf/2604.20348v1](https://arxiv.org/pdf/2604.20348v1)
- **Categories:** cs.RO, cs.AI, cs.MA


> **Main contribution** – The paper presents **BiCICLe**, the first framework that lets off‑the‑shelf, text‑only large language models (LLMs) control a bimanual robot through in‑context learning (ICL) without any task‑specific fine‑tuning. The key idea is to treat the two arms as separate agents in a leader‑follower hierarchy, thereby reducing the combinatorial joint‑action space to a sequence of conditioned single‑arm predictions and adding an “Arms’ Debate” iterative refinement plus a third LLM‑as‑Judge to select the most coherent coordinated trajectory.

**Methodology** – BiCICLe constructs few‑shot prompts that encode the current scene, the leader‑arm’s planned action, and then asks the follower‑arm LLM to generate a compatible action. The process is repeated through a debate loop where the two arm‑LLMs propose alternatives, and a judge‑LLM scores each candidate based on feasibility and task constraints, finally outputting the best joint plan. The approach is evaluated on the TWIN benchmark’s 13 bimanual manipulation tasks.

**Key findings** – BiCICLe attains an average success rate of **71.1 %**, beating the strongest training‑free baseline by **6.7 pp** and rivaling many supervised methods, while also showing strong few‑shot generalization to previously unseen tasks. These results demonstrate that multi‑agent ICL with leader‑follower decomposition and a judging component can unlock high‑dimensional coordinated robot control for agentic AI systems.


<details>
<summary>Abstract</summary>

Language Models (LLMs) have emerged as powerful reasoning engines for embodied control. In particular, In-Context Learning (ICL) enables off-the-shelf, text-only LLMs to predict robot actions without any task-specific training while preserving their generalization capabilities. Applying ICL to bimanual manipulation remains challenging, as the high-dimensional joint action space and tight inter-arm coordination constraints rapidly overwhelm standard context windows. To address this, we introduce BiCICLe (Bimanual Coordinated In-Context Learning), the first framework that enables standard LLMs to perform few-shot bimanual manipulation without fine-tuning. BiCICLe frames bimanual control as a multi-agent leader-follower problem, decoupling the action space into sequential, conditioned single-arm predictions. This naturally extends to Arms' Debate, an iterative refinement process, and to the introduction of a third LLM-as-Judge to evaluate and select the most plausible coordinated trajectories. Evaluated on 13 tasks from the TWIN benchmark, BiCICLe achieves up to 71.1% average success rate, outperforming the best training-free baseline by 6.7 percentage points and surpassing most supervised methods. We further demonstrate strong few-shot generalization on novel tasks.

</details>


### 49. R2IF: Aligning Reasoning with Decisions via Composite Rewards for Interpretable LLM Function Calling

- **Authors:** Aijia Cheng, Kailong Wang, Ling Shi, Yongxin Zhao
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20316v1](http://arxiv.org/abs/2604.20316v1)
- **PDF:** [https://arxiv.org/pdf/2604.20316v1](https://arxiv.org/pdf/2604.20316v1)
- **Categories:** cs.LG


> **Main contribution** – The paper introduces **R2IF**, a reinforcement‑learning framework that jointly aligns an LLM’s *reasoning* (Chain‑of‑Thought) with its *tool‑calling decisions* by using a **composite reward** that penalizes format errors, rewards effective reasoning, and values specification‑modifying actions.  

**Methodology** – R2IF augments standard RL‑based function‑calling with three reward components: (1) a format/correctness term, (2) a **Chain‑of‑Thought Effectiveness Reward (CER)** that scores how well the generated CoT leads to a correct tool call, and (3) a **Specification‑Modification‑Value (SMV)** reward that incentivizes useful changes to tool specifications. The policy is optimized with **GRPO** (Generalized Reward‑Weighted Policy Optimization).  

**Key findings** – On the BFCL and ACEBench benchmarks, R2IF improves function‑calling accuracy by up to **34.6 %** (e.g., Llama 3.2‑3B on BFCL) and achieves a positive **Average CoT Effectiveness** of **0.05**, demonstrating that reasoning‑aware rewards produce more reliable and interpretable tool‑augmented LLM behavior—an advance for deploying agentic AI systems that must both think and act correctly.


<details>
<summary>Abstract</summary>

Function calling empowers large language models (LLMs) to interface with external tools, yet existing RL-based approaches suffer from misalignment between reasoning processes and tool-call decisions. We propose R2IF, a reasoning-aware RL framework for interpretable function calling, adopting a composite reward integrating format/correctness constraints, Chain-of-Thought Effectiveness Reward (CER), and Specification-Modification-Value (SMV) reward, optimized via GRPO. Experiments on BFCL/ACEBench show R2IF outperforms baselines by up to 34.62% (Llama3.2-3B on BFCL) with positive Average CoT Effectiveness (0.05 for Llama3.2-3B), enhancing both function-calling accuracy and interpretability for reliable tool-augmented LLM deployment.

</details>


### 50. FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory

- **Authors:** Yingjie Gu, Wenjian Xiong, Liqiang Wang, Pengcheng Ren, Chao Li, Xiaojing Zhang, Yijuan Guo, Qi Sun, Jingyao Ma, Shidang Shi
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20300v2](http://arxiv.org/abs/2604.20300v2)
- **PDF:** [https://arxiv.org/pdf/2604.20300v2](https://arxiv.org/pdf/2604.20300v2)
- **Categories:** cs.AI


> The paper introduces **FSFM**, a biologically‑inspired framework that equips large‑language‑model (LLM) agents with selective‑forgetting capabilities modeled on hippocampal indexing, consolidation, and the Ebbinghaus forgetting curve. By defining a taxonomy of forgetting mechanisms (passive decay, active deletion, safety‑triggered, and adaptive reinforcement) and integrating them with vector‑database‑backed memory architectures, the authors implement and evaluate pruning, updating, and security‑driven forgetting strategies. Empirical results show that FSFM improves memory access efficiency by ≈ 8.5 %, boosts content quality (signal‑to‑noise ratio) by ≈ 29 %, and completely eliminates identified security risks, demonstrating that systematic forgetting is a practical, performance‑critical component for responsible, resource‑constrained LLM agents.


<details>
<summary>Abstract</summary>

For LLM agents, memory management critically impacts efficiency, quality, and security. While much research focuses on retention, selective forgetting--inspired by human cognitive processes (hippocampal indexing/consolidation theory and Ebbinghaus forgetting curve)--remains underexplored. We argue that in resource-constrained environments, a well-designed forgetting mechanism is as crucial as remembering, delivering benefits across three dimensions: (1) efficiency via intelligent memory pruning, (2) quality by dynamically updating outdated preferences and context, and (3) security through active forgetting of malicious inputs, sensitive data, and privacy-compromising content. Our framework establishes a taxonomy of forgetting mechanisms: passive decay-based, active deletion-based, safety-triggered, and adaptive reinforcement-based. Building on advances in LLM agent architectures and vector databases, we present detailed specifications, implementation strategies, and empirical validation from controlled experiments. Results show significant improvements: access efficiency (+8.49%), content quality (+29.2% signal-to-noise ratio), and security performance (100% elimination of security risks). Our work bridges cognitive neuroscience and AI systems, offering practical solutions for real-world deployment while addressing ethical and regulatory compliance. The paper concludes with challenges and future directions, establishing selective forgetting as a fundamental capability for next-generation LLM agents operating in real-world, resource-constrained scenarios. Our contributions align with AI-native memory systems and responsible AI development.

</details>


### 51. ActuBench: A Multi-Agent LLM Pipeline for Generation and Evaluation of Actuarial Reasoning Tasks

- **Authors:** Jan-Philipp Schmidt
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20273v1](http://arxiv.org/abs/2604.20273v1)
- **PDF:** [https://arxiv.org/pdf/2604.20273v1](https://arxiv.org/pdf/2604.20273v1)
- **Categories:** cs.AI, cs.CL


> ActuBench introduces a four‑role, multi‑agent LLM pipeline that automatically drafts actuarial multiple‑choice and open‑ended questions, creates distractors, verifies the outputs, and runs a one‑shot repair loop, while a lightweight auxiliary agent supplies topic labels from Wikipedia. By applying this system to generate 200 benchmark items and evaluating 50 models from eight providers, the authors show that (1) an independent verifier is essential—most first‑draft items are flagged and then corrected by the repair loop; (2) open‑weight models running on consumer hardware (Gemma‑4) and large Cerebras‑hosted models achieve the best cost‑performance trade‑offs; and (3) rankings derived from multiple‑choice accuracy diverge from those obtained via LLM‑as‑judge scoring of open‑ended solutions, indicating that judge‑mode evaluation is needed to meaningfully differentiate top‑performing agents.


<details>
<summary>Abstract</summary>

We present ActuBench, a multi-agent LLM pipeline for the automated generation and evaluation of advanced actuarial assessment items aligned with the International Actuarial Association (IAA) Education Syllabus. The pipeline separates four LLM roles by adapter: one agent drafts items, one constructs distractors, a third independently verifies both stages and drives bounded one-shot repair loops, and a cost-optimized auxiliary agent handles Wikipedia-note summarization and topic labelling. The items, per-model responses and complete leaderboard are published as a browsable web interface at https://actubench.de/en/, allowing readers and practitioners to inspect individual items without a repository checkout. We evaluate 50 language models from eight providers on two complementary benchmarks -- 100 empirically hardest multiple-choice items and 100 open-ended items scored by an LLM judge -- and report three headline findings. First, multi-agent verification is load-bearing: the independent verifier flags a majority of drafted items on first pass, most of which the one-shot repair loop resolves. Second, locally-hosted open-weights inference sits on the cost-performance Pareto front: a Gemma~4 model running on consumer hardware and a Cerebras-hosted 120B open-weights model dominate the near-zero-cost region, with the latter within one item of the top of the leaderboard. Third, MCQ and LLM-as-Judge rankings differ meaningfully: the MCQ scaffold inflates the performance ceiling, and Judge-mode evaluation is needed to discriminate at the frontier.

</details>


### 52. Memory-Augmented LLM-based Multi-Agent System for Automated Feature Generation on Tabular Data

- **Authors:** Fengxian Dong, Zhi Zheng, Xiao Han, Wei Chen, Jingqing Ruan, Tong Xu, Yong Chen, Enhong Chen
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20261v1](http://arxiv.org/abs/2604.20261v1)
- **PDF:** [https://arxiv.org/pdf/2604.20261v1](https://arxiv.org/pdf/2604.20261v1)
- **Categories:** cs.AI


> The paper introduces **MALMAS**, a memory‑augmented, multi‑agent framework that uses a large language model to automate feature engineering for tabular datasets. By assigning separate agents to distinct generation tasks and using a Router Agent to activate the most promising subset each iteration, MALMAS combines procedural, feedback, and conceptual memory to iteratively refine and diversify the feature space based on downstream learning signals. Experiments on several public benchmarks show that MALMAS consistently outperforms existing LLM‑based and traditional auto‑feature generation methods, delivering higher predictive accuracy and more diverse, high‑utility features.


<details>
<summary>Abstract</summary>

Automated feature generation extracts informative features from raw tabular data without manual intervention and is crucial for accurate, generalizable machine learning. Traditional methods rely on predefined operator libraries and cannot leverage task semantics, limiting their ability to produce diverse, high-value features for complex tasks. Recent Large Language Model (LLM)-based approaches introduce richer semantic signals, but still suffer from a restricted feature space due to fixed generation patterns and from the absence of feedback from the learning objective. To address these challenges, we propose a Memory-Augmented LLM-based Multi-Agent System (\textbf{MALMAS}) for automated feature generation. MALMAS decomposes the generation process into agents with distinct responsibilities, and a Router Agent activates an appropriate subset of agents per iteration, further broadening exploration of the feature space. We further integrate a memory module comprising procedural memory, feedback memory, and conceptual memory, enabling iterative refinement that adaptively guides subsequent feature generation and improves feature quality and diversity. Extensive experiments on multiple public datasets against state-of-the-art baselines demonstrate the effectiveness of our approach. The code is available at https://github.com/fxdong24/MALMAS

</details>


### 53. Mol-Debate: Multi-Agent Debate Improves Structural Reasoning in Molecular Design

- **Authors:** Wengyu Zhang, Xiao-Yong Wei, Qing Li
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20254v1](http://arxiv.org/abs/2604.20254v1)
- **PDF:** [https://arxiv.org/pdf/2604.20254v1](https://arxiv.org/pdf/2604.20254v1)
- **Categories:** cs.AI, cs.LG


> Mol‑Debate introduces a multi‑agent generation framework for text‑guided molecular design that replaces the usual one‑shot generation pipeline with an iterative **generate‑debate‑refine** loop, wherein specialized “debater” agents critique and improve a candidate structure from complementary perspectives (global‑local structural reasoning, developer‑debater conflict, static‑dynamic integration). The system orchestrates these agents through a perspective‑oriented scheduler and uses standard language‑model prompting to produce chemically valid molecules that satisfy complex natural‑language constraints. Empirically, Mol‑Debate outperforms existing retrieval‑augmented, chain‑of‑thought, fine‑tuned, and reinforcement‑learning baselines, achieving 59.82 % exact‑match accuracy on ChEBI‑20 and a 50.52 % weighted success rate on the S²‑Bench, establishing a new state‑of‑the‑art for agentic reasoning in drug‑discovery tasks.


<details>
<summary>Abstract</summary>

Text-guided molecular design is a key capability for AI-driven drug discovery, yet it remains challenging to map sequential natural-language instructions with non-linear molecular structures under strict chemical constraints. Most existing approaches, including RAG, CoT prompting, and fine-tuning or RL, emphasize a small set of ad-hoc reasoning perspectives implemented in a largely one-shot generation pipeline. In contrast, real-world drug discovery relies on dynamic, multi-perspective critique and iterative refinement to reconcile semantic intent with structural feasibility. Motivated by this, we propose Mol-Debate, a generation paradigm that enables such dynamic reasoning through an iterative generate-debate-refine loop. We further characterize key challenges in this paradigm and address them through perspective-oriented orchestration, including developer-debater conflict, global-local structural reasoning, and static-dynamic integration. Experiments demonstrate that Mol-Debate achieves state-of-the-art performance against strong general and chemical baselines, reaching 59.82% exact match on ChEBI-20 and 50.52% weighted success rate on S$^2$-Bench. Our code is available at https://github.com/wyuzh/Mol-Debate.

</details>


### 54. Taint-Style Vulnerability Detection and Confirmation for Node.js Packages Using LLM Agent Reasoning

- **Authors:** Ronghao Ni, Mihai Christodorescu, Limin Jia
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20179v1](http://arxiv.org/abs/2604.20179v1)
- **PDF:** [https://arxiv.org/pdf/2604.20179v1](https://arxiv.org/pdf/2604.20179v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> The paper introduces **LLMVD.js**, a multi‑stage pipeline of LLM‑driven agents that automatically scans Node.js packages, hypothesizes taint‑style vulnerabilities, synthesizes proof‑of‑concept exploits, and confirms them using lightweight execution oracles—eliminating the need for hand‑crafted static/dynamic analyzers or prior vulnerability labels. By chaining LLM reasoning with tool augmentation (code‑retrieval, prompt‑guided exploit generation, and sandboxed validation), LLMVD.js achieves a confirmation rate of 84 % on benchmark vulnerabilities, vastly surpassing traditional analysis tools (< 22 %) and a prior LLM‑analysis hybrid. On a fresh set of 260 unpublished packages, the system validates exploits in 36 packages, whereas conventional tools succeed on at most two, demonstrating the practical scalability of agentic LLM reasoning for supply‑chain security in the Node.js ecosystem.


<details>
<summary>Abstract</summary>

The rapidly evolving Node$.$js ecosystem currently includes millions of packages and is a critical part of modern software supply chains, making vulnerability detection of Node$.$js packages increasingly important. However, traditional program analysis struggles in this setting because of dynamic JavaScript features and the large number of package dependencies. Recent advances in large language models (LLMs) and the emerging paradigm of LLM-based agents offer an alternative to handcrafted program models. This raises the question of whether an LLM-centric, tool-augmented approach can effectively detect and confirm taint-style vulnerabilities (e.g., arbitrary command injection) in Node$.$js packages. We implement LLMVD$.$js, a multi-stage agent pipeline to scan code, propose vulnerabilities, generate proof-of-concept exploits, and validate them through lightweight execution oracles; and systematically evaluate its effectiveness in taint-style vulnerability detection and confirmation in Node$.$js packages without dedicated static/dynamic analysis engines for path derivation. For packages from public benchmarks, LLMVD$.$js confirms 84% of the vulnerabilities, compared to less than 22% for prior program analysis tools. It also outperforms a prior LLM-program-analysis hybrid approach while requiring neither vulnerability annotations nor prior vulnerability reports. When evaluated on a set of 260 recently released packages (without vulnerability groundtruth information), traditional tools produce validated exploits for few ($\leq 2$) packages, while LLMVD$.$js generates validated exploits for 36 packages.

</details>


### 55. Stateless Decision Memory for Enterprise AI Agents

- **Authors:** Vasundra Srinivasan
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20158v1](http://arxiv.org/abs/2604.20158v1)
- **PDF:** [https://arxiv.org/pdf/2604.20158v1](https://arxiv.org/pdf/2604.20158v1)
- **Categories:** cs.AI


> The paper argues that regulated enterprise AI deployments require **stateless, deterministically replayable** decision pipelines, and that existing stateful memory architectures inherently violate these constraints. To meet these requirements, the authors introduce **Deterministic Projection Memory (DPM)**—an append‑only event log combined with a single task‑conditioned projection step performed at decision time, replacing the multiple LLM calls used by summarization‑based memories. Across ten long‑horizon decision tasks, DPM matches or exceeds the factual precision and reasoning coherence of stateful memories while using 20× less memory, running 7–15× faster, and reducing the nondeterministic and audit surface from dozens of LLM calls to just two per decision, thereby demonstrating that stateless, high‑performance memory is viable for enterprise‑grade AI agents.


<details>
<summary>Abstract</summary>

Enterprise deployment of long-horizon decision agents in regulated domains (underwriting, claims adjudication, tax examination) is dominated by retrieval-augmented pipelines despite a decade of increasingly sophisticated stateful memory architectures. We argue this reflects a hidden requirement: regulated deployment is load-bearing on four systems properties (deterministic replay, auditable rationale, multi-tenant isolation, statelessness for horizontal scale), and stateful architectures violate them by construction. We propose Deterministic Projection Memory (DPM): an append-only event log plus one task-conditioned projection at decision time. On ten regulated decisioning cases at three memory budgets, DPM matches summarization-based memory at generous budgets and substantially outperforms it when the budget binds: at a 20x compression ratio, DPM improves factual precision by +0.52 (Cohen's h=1.17, p=0.0014) and reasoning coherence by +0.53 (h=1.13, p=0.0034), paired permutation, n=10. DPM is additionally 7-15x faster at binding budgets, making one LLM call at decision time instead of N. A determinism study of 10 replays per case at temperature zero shows both architectures inherit residual API-level nondeterminism, but the asymmetry is structural: DPM exposes one nondeterministic call; summarization exposes N compounding calls. The audit surface follows the same one-versus-N pattern: DPM logs two LLM calls per decision while summarization logs 83-97 on LongHorizon-Bench. We conclude with TAMS, a practitioner heuristic for architecture selection, and a failure analysis of stateful memory under enterprise operating conditions. The contribution is the argument that statelessness is the load-bearing property explaining enterprise's preference for weaker but replayable retrieval pipelines, and that DPM demonstrates this property is attainable without the decisioning penalty retrieval pays.

</details>


### 56. Meta-Tool: Efficient Few-Shot Tool Adaptation for Small Language Models

- **Authors:** Sachin Kumar
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20148v1](http://arxiv.org/abs/2604.20148v1)
- **PDF:** [https://arxiv.org/pdf/2604.20148v1](https://arxiv.org/pdf/2604.20148v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> **Main contribution**  
The paper introduces *Meta‑Tool*, a systematic empirical comparison of four adaptation strategies—few‑shot prompting, documentation encoding, hypernetwork‑generated LoRA weights, and value‑guided beam search—for equipping a 3 B‑parameter Llama‑3.2 model with tool‑use capabilities, and demonstrates that the added hypernetwork (227.8 M parameters) yields no measurable benefit over well‑crafted prompts.

**Methodology**  
Using the same 3 B backbone, the authors evaluate each mechanism on four heterogeneous tool‑use benchmarks (Gorilla APIBench, Spider 2.0, WebArena, InterCode) and run extensive ablations varying the number of exemplars (0–5) and the presence of API documentation. They also perform a detailed error analysis on 722 failures to distinguish format vs. semantic errors across tasks.

**Key findings for agentic AI**  
- Few‑shot examples alone boost performance by **+21.5 %**, and adding documentation adds another **+5.0 %**, while the hypernetwork contributes **0 %**.  
- A 3 B model with optimized prompts reaches **≈80 % of GPT‑5’s average tool‑use accuracy** at **10× lower latency**.  
- Failure modes are task‑specific: format errors dominate on API‑heavy tasks (Gorilla, InterCode), whereas semantic errors dominate on schema‑intensive tasks (Spider 2.0, WebArena).  

The study suggests that, for small language models in agentic settings, investment should focus on prompt engineering and example curation rather than complex weight‑generation adapters.


<details>
<summary>Abstract</summary>

Can small language models achieve strong tool-use performance without complex adaptation mechanisms? This paper investigates this question through Meta-Tool, a controlled empirical study comparing hypernetwork-based LoRA adaptation against carefully designed few-shot prompting. Using a Llama-3.2-3B-Instruct backbone, we evaluate four adaptation mechanisms--few-shot prompting, documentation encoding, hypernetwork-generated LoRA weights, and value-guided beam search--across four diverse benchmarks: Gorilla APIBench, Spider 2.0, WebArena, and InterCode. Our central finding is a well-supported negative result: despite generating non-trivial weight matrices, the 227.8M-parameter hypernetwork provides no measurable improvement over few-shot prompting alone. Comprehensive ablation studies reveal that few-shot examples contribute +21.5% to performance and documentation contributes +5.0%, while the hypernetwork adds 0%. A 3B model with well-designed prompts achieves 79.7% of GPT-5's average performance at $10 \times$ lower latency. Error analysis across 722 failure cases spanning all shot counts (0--5) shows that at the 5-shot configuration (106 failures), failure modes are task-dependent: schema-heavy tasks (Spider 2.0, WebArena) show near-zero format errors with remaining failures semantic, while format errors dominate on Gorilla (100%) and InterCode (70%). These findings redirect practitioners toward prompt engineering and example curation rather than complex adaptation architectures.

</details>


### 57. SAKE: Self-aware Knowledge Exploitation-Exploration for Grounded Multimodal Named Entity Recognition

- **Authors:** Jielong Tang, Xujie Yuan, Jiayang Liu, Jianxing Yu, Xiao Dong, Lin Chen, Yunlai Teng, Shimin Di, Jian Yin
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20146v1](http://arxiv.org/abs/2604.20146v1)
- **PDF:** [https://arxiv.org/pdf/2604.20146v1](https://arxiv.org/pdf/2604.20146v1)
- **Categories:** cs.IR, cs.CL


> The paper introduces **SAKE**, an end‑to‑end agentic framework that jointly exploits internal knowledge of multimodal LLMs and selectively invokes external retrieval tools for Grounded Multimodal Named Entity Recognition (GMNER). The authors first generate difficulty‑aware search tags—uncertainty signals derived from multiple forward passes—to create a self‑awareness‑enhanced Chain‑of‑Thought (SAKE‑SeCoT) dataset, which is used to fine‑tune the model for basic tool use; then they apply agentic reinforcement learning with a hybrid reward that penalizes unnecessary retrieval, enabling the system to learn when external knowledge is truly needed. Experiments on two social‑media GMNER benchmarks show that SAKE markedly improves both entity extraction and visual grounding accuracy, especially for long‑tailed and unseen entities, while reducing retrieval‑induced noise.


<details>
<summary>Abstract</summary>

Grounded Multimodal Named Entity Recognition (GMNER) aims to extract named entities and localize their visual regions within image-text pairs, serving as a pivotal capability for various downstream applications. In open-world social media platforms, GMNER remains challenging due to the prevalence of long-tailed, rapidly evolving, and unseen entities. To tackle this, existing approaches typically rely on either external knowledge exploration through heuristic retrieval or internal knowledge exploitation via iterative refinement in Multimodal Large Language Models (MLLMs). However, heuristic retrieval often introduces noisy or conflicting evidence that degrades precision on known entities, while solely internal exploitation is constrained by the knowledge boundaries of MLLMs and prone to hallucinations. To address this, we propose SAKE, an end-to-end agentic framework that harmonizes internal knowledge exploitation and external knowledge exploration via self-aware reasoning and adaptive search tool invocation. We implement this via a two-stage training paradigm. First, we propose Difficulty-aware Search Tag Generation, which quantifies the model's entity-level uncertainty through multiple forward samplings to produce explicit knowledge-gap signals. Based on these signals, we construct SAKE-SeCoT, a high-quality Chain-of-Thought dataset that equips the model with basic self-awareness and tool-use capabilities through supervised fine-tuning. Second, we employ agentic reinforcement learning with a hybrid reward function that penalizes unnecessary retrieval, enabling the model to evolve from rigid search imitation to genuine self-aware decision-making about when retrieval is truly necessary. Extensive experiments on two widely used social media benchmarks demonstrate SAKE's effectiveness.

</details>


### 58. HiPO: Hierarchical Preference Optimization for Adaptive Reasoning in LLMs

- **Authors:** Darsh Kachroo, Adriana Caraeni, Arjun Prasaath Anbazhagan, Brennan Lagasse, Kevin Zhu
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20140v1](http://arxiv.org/abs/2604.20140v1)
- **PDF:** [https://arxiv.org/pdf/2604.20140v1](https://arxiv.org/pdf/2604.20140v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces **HiPO (Hierarchical Preference Optimization)**, a refinement of Direct Preference Optimization that partitions a model’s output into distinct reasoning segments (clarification, intermediate steps, final answer) and applies a weighted DPO loss to each part. By training on segment‑level preference signals while preserving DPO’s stability and efficiency, HiPO enables fine‑grained feedback for multi‑step reasoning. Experiments fine‑tuning several 7 B LLMs on a Math Stack Exchange preference dataset show that HiPO‑trained models consistently beat standard DPO on math benchmarks and receive higher GPT‑4.1 ratings for organization, logical flow, and answer consistency, demonstrating a viable path for aligning agents that must perform complex, structured reasoning.


<details>
<summary>Abstract</summary>

Direct Preference Optimization (DPO) is an effective framework for aligning large language models with human preferences, but it struggles with complex reasoning tasks. DPO optimizes for the likelihood of generating preferred over dispreferred responses in their entirety and lacks the granularity to provide feedback on subsections of many-step solutions typical of reasoning tasks. Existing methods excel at either stable preference learning (e.g., DPO variants like KTO and RSO) or structured reasoning (e.g., ReMA's multi-agent RL framework, Tree of Thoughts), but fail to merge these complementary strengths. We propose HiPO (Hierarchical Preference Optimization), an extension of DPO that separates responses into reasoning segments (query clarification and context, reasoning steps, and answer) and computes loss as a weighted sum of the DPO loss for each segment. Our approach enables segment-specific training while maintaining DPO's computational efficiency and training stability. We demonstrate that for multiple 7B LLMs fine-tuned using HiPO and DPO on the Math Stack Exchange preference dataset, the models trained with HiPO outperform the others on a variety of common math benchmarks and achieve greater organization, logical flow, and consistency as measured by GPT-4.1.

</details>


### 59. IMPACT-CYCLE: A Contract-Based Multi-Agent System for Claim-Level Supervisory Correction of Long-Video Semantic Memory

- **Authors:** Weitong Kong, Di Wen, Kunyu Peng, David Schneider, Zeyun Zhong, Alexander Jaus, Zdravko Marinov, Jiale Wei, Ruiping Liu, Junwei Zheng, Yufan Chen, Lei Qi, Rainer Stiefelhagen
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20136v1](http://arxiv.org/abs/2604.20136v1)
- **PDF:** [https://arxiv.org/pdf/2604.20136v1](https://arxiv.org/pdf/2604.20136v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces **IMPACT‑CYCLE**, a contract‑driven multi‑agent architecture that reframes long‑video comprehension as an incremental, claim‑level upkeep of a shared, versioned semantic memory (typed claims, dependency graph, and provenance log). By assigning specialized agents explicit authority contracts—verifying object‑relation facts, temporal consistency, and global coherence—and delegating only conflicted claims to a human supervisor with final override rights, the system bounds correction effort to the transitive closure of the affected claims. On the VidOR benchmark, this approach raises downstream VQA accuracy from 0.71 to 0.79 while cutting human arbitration cost by 4.8×, demonstrating that contract‑based supervisory agents can dramatically improve the efficiency and transparency of agentic AI for long‑video reasoning.


<details>
<summary>Abstract</summary>

Correcting errors in long-video understanding is disproportionately costly: existing multimodal pipelines produce opaque, end-to-end outputs that expose no intermediate state for inspection, forcing annotators to revisit raw video and reconstruct temporal logic from scratch. The core bottleneck is not generation quality alone, but the absence of a supervisory interface through which human effort can be proportional to the scope of each error. We present IMPACT-CYCLE, a supervisory multi-agent system that reformulates long-video understanding as iterative claim-level maintenance of a shared semantic memory -- a structured, versioned state encoding typed claims, a claim dependency graph, and a provenance log. Role-specialized agents operating under explicit authority contracts decompose verification into local object-relation correctness, cross-temporal consistency, and global semantic coherence, with corrections confined to structurally dependent claims. When automated evidence is insufficient, the system escalates to human arbitration as the supervisory authority with final override rights; dependency-closure re-verification then ensures correction cost remains proportional to error scope. Experiments on VidOR show substantially improved downstream reasoning (VQA: 0.71 to 0.79) and a 4.8x reduction in human arbitration cost, with workload significantly lower than manual annotation. Code will be released at https://github.com/MKong17/IMPACT_CYCLE.

</details>


### 60. AgentSOC: A Multi-Layer Agentic AI Framework for Security Operations Automation

- **Authors:** Joyjit Roy, Samaresh Kumar Singh
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20134v1](http://arxiv.org/abs/2604.20134v1)
- **PDF:** [https://arxiv.org/pdf/2604.20134v1](https://arxiv.org/pdf/2604.20134v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> The paper presents **AgentSOC**, a hierarchical, multi‑layer agentic AI framework that unifies alert normalization, contextual enrichment, hypothesis generation, feasibility validation, and policy‑compliant response planning to automate Security Operations Center (SOC) workflows. The authors implement the framework as a stack of perception, anticipatory‑reasoning, and risk‑based action‑planning agents, and evaluate it conceptually on a large enterprise dataset together with a lightweight proof‑of‑concept using LANL authentication logs. Results show that AgentSOC yields more consistent triage, correctly anticipates attacker intentions, and recommends containment actions that balance security effectiveness with operational impact, demonstrating the viability of hybrid agentic reasoning for safer, adaptive SOC automation.


<details>
<summary>Abstract</summary>

Security Operations Centers (SOCs) increasingly encounter difficulties in correlating heterogeneous alerts, interpreting multi-stage attack progressions, and selecting safe and effective response actions. This study introduces AgentSOC, a multi-layered agentic AI framework that enhances SOC automation by integrating perception, anticipatory reasoning, and risk-based action planning. The proposed architecture consolidates several layers of abstraction to provide a single operational loop to support normalizing alerts, enriching context, generating hypotheses, validating structural feasibility, and executing policy-compliant responses. Conceptually evaluated within a large enterprise environment, AgentSOC improves triage consistency, anticipates attackers' intentions, and provides recommended containment options that are both operationally feasible and well-balanced between security efficacy and operational impact. The results suggest that hybrid agentic reasoning has the potential to serve as a foundation for developing adaptive, safer SOC automation in large enterprises. Additionally, a minimal Proof-Of-Concept (POC) demonstration using LANL authentication data demonstrated the feasibility of the proposed architecture.

</details>


### 61. EvoAgent: An Evolvable Agent Framework with Skill Learning and Multi-Agent Delegation

- **Authors:** Aimin Zhang, Jiajing Guo, Fuwei Jia, Chen Lv, Boyu Wang, Fangzheng Li
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20133v2](http://arxiv.org/abs/2604.20133v2)
- **PDF:** [https://arxiv.org/pdf/2604.20133v2](https://arxiv.org/pdf/2604.20133v2)
- **Categories:** cs.AI


> EvoAgent introduces a modular, evolvable LLM‑agent architecture that treats each capability as a structured “skill” file equipped with triggers and evolutionary metadata, and that hierarchically delegates sub‑tasks to specialized sub‑agents using a three‑stage matching and three‑layer memory system. The methodology couples continuous, user‑feedback‑driven skill generation/optimization with dynamic task decomposition, enabling the base model (e.g., GPT‑5.2) to acquire and reuse long‑term competencies across domains. In foreign‑trade benchmarks, EvoAgent lifts the model’s professionalism, accuracy and utility by ~28 % on a five‑dimensional LLM‑as‑Judge metric, and ablation studies show that the synergy between the underlying LLM and the EvoAgent framework is a decisive factor in overall system performance.


<details>
<summary>Abstract</summary>

This paper proposes EvoAgent - an evolvable large language model (LLM) agent framework that integrates structured skill learning with a hierarchical sub-agent delegation mechanism. EvoAgent models skills as multi-file structured capability units equipped with triggering mechanisms and evolutionary metadata, and enables continuous skill generation and optimization through a user-feedback-driven closed-loop process. In addition, by incorporating a three-stage skill matching strategy and a three-layer memory architecture, the framework supports dynamic task decomposition for complex problems and long-term capability accumulation. Experimental results based on real-world foreign trade scenarios demonstrate that, after integrating EvoAgent, GPT5.2 achieves significant improvements in professionalism, accuracy, and practical utility. Under a five-dimensional LLM-as-Judge evaluation protocol, the overall average score increases by approximately 28%. Further model transfer experiments indicate that the performance of an agent system depends not only on the intrinsic capabilities of the underlying model, but also on the degree of synergy between the model and the agent architecture.

</details>


### 62. A Delta-Aware Orchestration Framework for Scalable Multi-Agent Edge Computing

- **Authors:** Samaresh Kumar Singh, Joyjit Roy
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20129v1](http://arxiv.org/abs/2604.20129v1)
- **PDF:** [https://arxiv.org/pdf/2604.20129v1](https://arxiv.org/pdf/2604.20129v1)
- **Categories:** cs.LG, cs.DC, cs.PF, cs.SE


> The paper introduces **DAOEF (Delta‑Aware Orchestration for Edge Federations)**, a unified framework that prevents the “Synergistic Collapse”—the super‑linear performance drop observed when more than ~100 reinforcement‑learning agents run on edge hardware. DAOEF combines three tightly coupled techniques: (1) **Differential Neural Caching**, which reuses intermediate activations and processes only input deltas to raise cache hit rates ≈ 2× with <2 % accuracy loss; (2) **Criticality‑Based Action‑Space Pruning**, which tiers agents by importance to cut the coordination complexity from O(n²) to O(n log n) while preserving >94 % of optimality; and (3) **Learned Hardware‑Affinity Matching**, which dynamically dispatches tasks to the most suitable accelerator (GPU/CPU/NPU/FPGA). Experiments on simulated and physical testbeds (100–250 agents, 20 edge devices) show that the three mechanisms are mutually reinforcing: removing any one degrades latency by > 40 %, and the full DAOEF stack yields a 1.45× multiplicative improvement over applying the components separately, achieving up to 62 % latency reduction and sub‑linear scaling up to 250 agents—results directly relevant to scalable, agentic AI deployments on edge infrastructures.


<details>
<summary>Abstract</summary>

The Synergistic Collapse occurs when scaling beyond 100 agents causes superlinear performance degradation that individual optimizations cannot prevent. We observe this collapse with 150 cameras in Smart City deployment using MADDPG, where Deadline Satisfaction drops from 78% to 34%, producing approximately $180,000 in annual cost overruns. Prior work has addressed each contributing factor in isolation: exponential action-space growth, computational redundancy among spatially adjacent agents, and task-agnostic hardware scheduling. None has examined how these three factors interact and amplify each other. We present DAOEF (Delta-Aware Orchestration for Edge Federations), a framework that addresses all three simultaneously through: (1) Differential Neural Caching, which stores intermediate layer activations and computes only the input deltas, achieving 2.1x higher hit ratios (72% vs. 35%) than output-level caching while staying within 2% accuracy loss through empirically calibrated similarity thresholds; (2) Criticality-Based Action Space Pruning, which organizes agents into priority tiers and reduces coordination complexity from O(n2) to O(n log n) with less than 6% optimality loss; and (3) Learned Hardware Affinity Matching, which assigns tasks to their optimal accelerator (GPU, CPU, NPU, or FPGA) to prevent compounding mismatch penalties. Controlled factor-isolation experiments confirm that each mechanism is necessary but insufficient on its own: removing any single mechanism increases latency by more than 40%, validating that the gains are interdependent rather than additive. Across four datasets (100-250 agents) and a 20-device physical testbed, DAOEF achieves a 1.45x multiplicative gain over applying the three mechanisms independently. A 200-agent cloud deployment yields 62% latency reduction (280 ms vs. 735 ms), sub-linear latency growth up to 250 agents.

</details>


### 63. Omission Constraints Decay While Commission Constraints Persist in Long-Context LLM Agents

- **Authors:** Yeran Gamage
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20911v1](http://arxiv.org/abs/2604.20911v1)
- **PDF:** [https://arxiv.org/pdf/2604.20911v1](https://arxiv.org/pdf/2604.20911v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution**  
The paper uncovers a systematic asymmetry in long‑context LLM agents—prohibition (“omit”) constraints degrade as the dialogue deepens, whereas requirement (“commission”) constraints remain fully obeyed. The authors name this phenomenon **Security‑Recall Divergence (SRD)** and show that it creates hidden safety failures in production agents that rely on static system‑prompt policies.  

**Methodology**  
A causal, three‑arm experiment was run on 12 LLMs from 8 providers (4 416 total trials) across six conversation depths (turn 5→turn 16). Agents were given a fixed safety policy (e.g., “never disclose credentials”). The study measured (1) omission compliance (the agent refrains from prohibited behavior) and (2) commission compliance (the agent follows required safety actions). Two models received token‑matched padding controls to isolate the effect of semantic “schema” content.  

**Key findings for agentic AI**  
- Omission compliance drops dramatically from **≈73 % at turn 5 to ≈33 % at turn 16**, while commission compliance stays at **100 %** (p < 10⁻³³ for Mistral‑Large‑3).  
- In the padded‑control models, **62–100 % of the decay is explained by the semantic load of the ongoing context**, not by token count alone.  
- Re‑injecting the policy before a model‑specific **Safe Turn Depth (STD)** restores omission compliance without any retraining, implying that a lightweight “policy refresh” could mitigate SRD in deployment.  

Overall, the work reveals that long‑context LLM agents can silently violate prohibition‑type safety rules while still appearing compliant on conventional audit signals, highlighting a critical gap in current monitoring and prompting strategies for safe, agentic AI.


<details>
<summary>Abstract</summary>

LLM agents deployed in production operate under operator-defined behavioral policies (system-prompt instructions such as prohibitions on credential disclosure, data exfiltration, and unauthorized output) that safety evaluations assume hold throughout a conversation. Prohibition-type constraints decay under context pressure while requirement-type constraints persist; we term this asymmetry Security-Recall Divergence (SRD). In a 4,416-trial three-arm causal study across 12 models and 8 providers at six conversation depths, omission compliance falls from 73% at turn 5 to 33% at turn 16 while commission compliance holds at 100% (Mistral Large 3, $p < 10^{-33}$). In the two models with token-matched padding controls, schema semantic content accounts for 62-100% of the dilution effect. Re-injecting constraints before the per-model Safe Turn Depth (STD) restores compliance without retraining. Production security policies consist of prohibitions such as never revealing credentials, never executing untrusted code, and never forwarding user data. Commission-type audit signals remain healthy while omission constraints have already failed, leaving the failure invisible to standard monitoring.

</details>


### 64. SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks

- **Authors:** Shanshan Zhong, Yi Lu, Jingjie Ning, Yibing Wan, Lihan Feng, Yuyi Ao, Leonardo F. R. Ribeiro, Markus Dreyer, Sean Ammirati, Chenyan Xiong
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20087v1](http://arxiv.org/abs/2604.20087v1)
- **PDF:** [https://arxiv.org/pdf/2604.20087v1](https://arxiv.org/pdf/2604.20087v1)
- **Categories:** cs.CL, cs.LG


> **Main contribution:** The paper introduces **SkillLearnBench**, the first systematic benchmark for evaluating continual‑learning approaches that automatically generate and refine LLM‑agent skills on real‑world tasks.  

**Methodology:** The benchmark comprises 20 verified, skill‑dependent tasks spanning 15 sub‑domains and evaluates each method on three axes—skill quality, execution trajectory, and final task outcome. The authors test a suite of recent continual‑learning strategies (one‑shot prompting, self‑feedback, teacher‑feedback, and “skill‑creator” pipelines) across multiple LLM backbones, measuring how skill libraries evolve over successive learning iterations.  

**Key findings:** All continual‑learning methods beat a no‑skill baseline, but no single technique dominates across tasks or model sizes; improvements are strongest on tasks with clear, reusable workflows, while open‑ended tasks suffer from “recursive drift” when relying only on self‑feedback. Moreover, larger LLMs do not guarantee better skill generation, and external feedback across multiple iterations is crucial for genuine skill enhancement.


<details>
<summary>Abstract</summary>

Skills have become the de facto way to enable LLM agents to perform complex real-world tasks with customized instructions, workflows, and tools, but how to learn them automatically and effectively remains unclear. We introduce SkillLearnBench, the first benchmark for evaluating continual skill learning methods, comprising 20 verified, skill-dependent tasks across 15 sub-domains derived from a real-world skill taxonomy , evaluated at three levels: skill quality, execution trajectory, and task outcome. Using this benchmark, we evaluate recent continual learning techniques, those leveraging one-shot, self/teacher feedback, and skill creator to generate skills from agent experiences. We find that all continual learning methods improve over the no-skill baseline, yet consistent gains remain elusive: no method leads across all tasks and LLMs, and scaling to stronger LLMs does not reliably help. Continual learning improves tasks with clear, reusable workflows but struggles on open-ended tasks, and using stronger LLM backbones does not consistently produce better skills. Our analysis also revealed that multiple iterations in continual learning facilitate genuine improvement via external feedback, whereas self-feedback alone induces recursive drift. Our data and code are open-source at https://github.com/cxcscmu/SkillLearnBench to enable further studies of automatic skill generation and continual learning techniques.

</details>


### 65. Auditing and Controlling AI Agent Actions in Spreadsheets

- **Authors:** Sadra Sabouri, Zeinabsadat Saghi, Run Huang, Sujay Maladi, Esmeralda Eufracio, Sumit Gulwani, Souti Chattopadhyay
- **Published:** 2026-04-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20070v1](http://arxiv.org/abs/2604.20070v1)
- **PDF:** [https://arxiv.org/pdf/2604.20070v1](https://arxiv.org/pdf/2604.20070v1)
- **Categories:** cs.HC, cs.AI, cs.CE


> **Contribution:** The paper introduces **Pista**, a spreadsheet‑embedded AI agent that breaks down its autonomous reasoning into a sequence of discrete, user‑visible actions, letting humans audit and intervene on the fly rather than only after the final output is produced.

**Methodology:** Pista’s architecture timestamps each decision as a cell‑level operation and presents it to the user through an interactive pane; users can accept, edit, or reject each step. The authors evaluated this design with a formative interview study (N = 8) and a within‑subjects controlled experiment (N = 16) that compared Pista against a conventional “black‑box” spreadsheet agent.

**Key Findings:** Real‑time participation let participants spot and correct errors that would have been missed in post‑hoc review, improve task performance, and increase their understanding of both the task and the agent’s behavior. Users reported higher perceived control, trust, and co‑ownership of the final spreadsheet artifacts, demonstrating that active, step‑wise oversight—not just after‑the‑fact auditing—is crucial for safe, transparent agentic AI in knowledge‑work contexts.


<details>
<summary>Abstract</summary>

Advances in AI agent capabilities have outpaced users' ability to meaningfully oversee their execution. AI agents can perform sophisticated, multi-step knowledge work autonomously from start to finish, yet this process remains effectively inaccessible during execution, often buried within large volumes of intermediate reasoning and outputs: by the time users receive the output, all underlying decisions have already been made without their involvement. This lack of transparency leaves users unable to examine the agent's assumptions, identify errors before they propagate, or redirect execution when it deviates from their intent. The stakes are particularly high in spreadsheet environments, where process and artifact are inseparable. Each decision the agent makes is recorded directly in cells that belong to and reflect on the user. We introduce Pista, a spreadsheet AI agent that decomposes execution into auditable, controllable actions, providing users with visibility into the agent's decision-making process and the capacity to intervene at each step. A formative study (N = 8) and a within-subjects summative evaluation (N = 16) comparing Pista to a baseline agent demonstrated that active participation in execution influenced not only task outcomes but also users' comprehension of the task, their perception of the agent, and their sense of role within the workflow. Users identified their own intent reflected in the agent's actions, detected errors that post-hoc review would have failed to surface, and reported a sense of co-ownership over the resulting output. These findings indicate that meaningful human oversight of AI agents in knowledge work requires not improved post-hoc review mechanisms, but active participation in decisions as they are made.

</details>


### 66. From Fuzzy to Formal: Scaling Hospital Quality Improvement with AI

- **Authors:** Patrick Vossler, Jean Feng, Venkat Sivaraman, Robert Gallo, Hemal Kanzaria, Dana Freiser, Christopher Ross, Amy Ou, James Marks, Susan Ehrlich, Christopher Peabody, Lucas Zier
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20055v1](http://arxiv.org/abs/2604.20055v1)
- **PDF:** [https://arxiv.org/pdf/2604.20055v1](https://arxiv.org/pdf/2604.20055v1)
- **Categories:** cs.AI, cs.HC


> The paper’s main contribution is a “Human‑AI Spec‑Solution Co‑optimization” framework that treats hospital quality‑improvement (QI) factor discovery—a fuzzy, expert‑driven sense‑making activity—as a jointly learnable problem of both LLM prompts and their natural‑language specifications. The methodology maps QI factor discovery onto the classic AI/ML development cycle (problem formalization → model learning → model validation), letting domain experts and autonomous AI agents iteratively adjust the specifications (treated as hyper‑parameters) and the extraction pipeline until the AI‑generated factors align with expert annotations and clinical goals. Applied to a safety‑net hospital, the approach achieved ≥70 % agreement with human experts, dramatically reduced analysis time, reproduced known drivers of long stays and readmissions, uncovered additional modifiable factors, and generated traceable, auditable reasoning—demonstrating a scalable, reproducible AI‑augmented workflow for exploratory, agentic tasks in healthcare quality improvement.


<details>
<summary>Abstract</summary>

Hospital Quality Improvement (QI) plays a critical role in optimizing healthcare delivery by translating high-level hospital goals into actionable solutions. A critical step of QI is to identify the key modifiable contributing factors, a process we call QI factor discovery, typically through expert-driven semi-structured qualitative tools like fishbone diagrams, chart reviews, and Lean Healthcare methods. AI has the potential to transform and accelerate QI factor discovery, which is traditionally time- and resource-intensive and limited in reproducibility and auditability. Nevertheless, current AI alignment methods assume the task is well-defined, whereas QI factor discovery is an exploratory, fuzzy, and iterative sense-making process that relies on complex implicit expert judgments. To design an AI pipeline that formalizes the QI process while preserving its exploratory components, we propose viewing the task as learning not only LLM prompts but also the overarching natural-language specifications. In particular, we map QI factor discovery to steps of the classical AI/ML development process (problem formalization, model learning, and model validation) where the specifications are tunable hyperparameters. Domain experts and AI agents iteratively refine both the overarching specifications and AI pipeline until AI extractions are concordant with expert annotations and aligned with clinical objectives. We applied this "Human-AI Spec-Solution Co-optimization" framework at an urban safety-net hospital to identify factors driving prolonged length of stay and unplanned 30-day readmissions. The resulting AI-for-QI pipelines achieved $\ge 70\%$ concordance with expert annotations. Compared to prior manual Lean analyses, the AI pipeline was substantially more efficient, recovered previous findings, surfaced new modifiable factors, and produced auditable reasoning traces.

</details>


### 67. Information Aggregation with AI Agents

- **Authors:** Spyros Galanis
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20050v1](http://arxiv.org/abs/2604.20050v1)
- **PDF:** [https://arxiv.org/pdf/2604.20050v1](https://arxiv.org/pdf/2604.20050v1)
- **Categories:** econ.GN, cs.AI, cs.GT


> **Main contribution:** The paper investigates whether large‑language‑model (LLM) agents can function as information‑aggregating participants in a prediction market, testing their ability to infer others’ private signals from price dynamics.  

**Methodology:** In a controlled laboratory setting, LLM agents receive private binary signals and then trade sequentially in a simulated prediction market; the quality of aggregation is measured by the log error of the final market price. The authors vary information structure complexity, market design features (cheap‑talk communication, market duration, initial price), and agent “smartness” (model size, prompting, feedback).  

**Key findings:** Median‑type markets reliably aggregate information under simple signal structures, but performance deteriorates sharply as signal complexity rises—mirroring human limits in higher‑order reasoning. Robustness checks show that cheap talk, market length, and initial price do not affect aggregation, confirming the market’s resilience. More capable LLM agents achieve lower price errors and higher profits, yet providing them with performance feedback paradoxically harms both aggregation accuracy and profitability. These results suggest that while LLM agents can emulate human‑like market aggregation, they inherit similar constraints in reasoning about others’ information.


<details>
<summary>Abstract</summary>

Can Large Language Models (AI agents) aggregate dispersed private information through trading and reason about the knowledge of others by observing price movements? We conduct a controlled experiment where AI agents trade in a prediction market after receiving private signals, measuring information aggregation by the log error of the last price. We find that although the median market is effective at aggregating information in the easy information structures, increasing the complexity has a significant and negative impact, suggesting that AI agents may suffer from the same limitations as humans when reasoning about others. Consistent with our theoretical predictions, information aggregation remains unaffected by allowing cheap talk communication, changing the duration of the market or initial price, and strategic prompting-thus demonstrating that prediction markets are robust. We establish that "smarter" AI agents perform better at aggregation and they are more profitable. Surprisingly, giving them feedback about past performance makes them worse at aggregation and reduces their profits.

</details>


### 68. TriEx: A Game-based Tri-View Framework for Explaining Internal Reasoning in Multi-Agent LLMs

- **Authors:** Ziyi Wang, Chen Zhang, Wenjun Peng, Qi Wu, Xinyu Wang
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20043v1](http://arxiv.org/abs/2604.20043v1)
- **PDF:** [https://arxiv.org/pdf/2604.20043v1](https://arxiv.org/pdf/2604.20043v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **TriEx**, a “tri‑view” framework for interpreting the internal reasoning of multi‑agent LLMs operating in interactive, partially‑observable games. TriEx pairs each action with (i) a structured first‑person self‑explanation, (ii) a second‑person model of the opponent’s belief state that is updated over time, and (iii) a third‑person “oracle” audit that ties explanations to ground‑truth signals extracted from the environment. Using imperfect‑information strategic games, the authors show that this multi‑perspective instrumentation allows systematic measurement of explanation faithfulness, belief dynamics, and evaluator reliability, uncovering consistent gaps between what agents say, what they actually believe, and the actions they take—demonstrating that explainability for LLM agents must be treated as an interaction‑dependent, evidence‑grounded property.


<details>
<summary>Abstract</summary>

Explainability for Large Language Model (LLM) agents is especially challenging in interactive, partially observable settings, where decisions depend on evolving beliefs and other agents. We present \textbf{TriEx}, a tri-view explainability framework that instruments sequential decision making with aligned artifacts: (i) structured first-person self-reasoning bound to an action, (ii) explicit second-person belief states about opponents updated over time, and (iii) third-person oracle audits grounded in environment-derived reference signals. This design turns explanations from free-form narratives into evidence-anchored objects that can be compared and checked across time and perspectives. Using imperfect-information strategic games as a controlled testbed, we show that TriEx enables scalable analysis of explanation faithfulness, belief dynamics, and evaluator reliability, revealing systematic mismatches between what agents say, what they believe, and what they do. Our results highlight explainability as an interaction-dependent property and motivate multi-view, evidence-grounded evaluation for LLM agents. Code is available at https://github.com/Einsam1819/TriEx.

</details>


### 69. Separable Pathways for Causal Reasoning: How Architectural Scaffolding Enables Hypothesis-Space Restructuring in LLM Agents

- **Authors:** John Alderete, Sebastian Benthal, Connie Xu, John Xing
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20039v1](http://arxiv.org/abs/2604.20039v1)
- **PDF:** [https://arxiv.org/pdf/2604.20039v1](https://arxiv.org/pdf/2604.20039v1)
- **Categories:** cs.AI, cs.LG


> The paper demonstrates that LLM agents can acquire true causal‑discovery abilities when their architecture explicitly supports restructuring of the hypothesis space. The authors introduce a compositional design that couples (1) **context graphs**—typed state‑machine representations that guide exploration within any given hypothesis space—and (2) **dynamic behaviors**—runtime monitors that detect when evidence invalidates the current space and instantiate new hypotheses. In 1,085 Blicket‑detector experiments, context graphs supply 94 % of the accuracy improvement by enhancing reasoning once the correct hypothesis space is reached, while the dynamic behaviors enable agents to recognise regime shifts and avoid premature commitment, together yielding far‑superior causal inference compared with standard LLM agents.


<details>
<summary>Abstract</summary>

Causal discovery through experimentation and intervention is fundamental to robust problem solving. It requires not just updating beliefs within a fixed framework but revising the hypothesis space itself, a capacity current AI agents lack when evidence demands representations they have not previously constructed. We extend the blicket detector paradigm from developmental science to test this capacity in AI agents equipped with architectural scaffolding that targets hypothesis-space restructuring. Our compositional architecture has two discrete components: context graphs, which structure exploration as typed state machines, and dynamic behaviors, which monitor for evidence that the current hypothesis space is inadequate and expand it at runtime. Across 1,085 experimental trials, these components make orthogonal contributions: context graphs drive reasoning quality within the post-switch hypothesis space, accounting for 94\% of the accuracy gain, while dynamic behaviors drive reasoning eligibility by detecting regime changes and preventing premature commitment to outdated hypotheses.

</details>


### 70. CreativeGame:Toward Mechanic-Aware Creative Game Generation

- **Authors:** Hongnan Ma, Han Wang, Shenglin Wang, Tieyue Yin, Yiwei Shi, Yucong Huang, Yingtian Zou, Muning Wen, Mengyue Yang
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19926v1](http://arxiv.org/abs/2604.19926v1)
- **PDF:** [https://arxiv.org/pdf/2604.19926v1](https://arxiv.org/pdf/2604.19926v1)
- **Categories:** cs.AI


> **CreativeGame** introduces a multi‑agent pipeline that treats game mechanics as first‑class objects during the generation of HTML5 games. By coupling (1) a proxy reward that scores programmatic signals (e.g., successful compilation, runtime checks) rather than raw LLM output, (2) lineage‑scoped memory that carries experience across successive versions, (3) integrated runtime validation in both repair and reward loops, and (4) a mechanic‑guided planning stage that converts retrieved mechanic knowledge into an explicit plan before code synthesis, the system enables iterative, interpretable improvement of game code. Experiments on a 4‑generation lineage demonstrate that new mechanics can be deliberately introduced and tracked across versions, confirming that the approach yields measurable, mechanistic creativity and offers a concrete framework for studying progressive, agentic AI‑driven design.


<details>
<summary>Abstract</summary>

Large language models can generate plausible game code, but turning this capability into \emph{iterative creative improvement} remains difficult. In practice, single-shot generation often produces brittle runtime behavior, weak accumulation of experience across versions, and creativity scores that are too subjective to serve as reliable optimization signals. A further limitation is that mechanics are frequently treated only as post-hoc descriptions, rather than as explicit objects that can be planned, tracked, preserved, and evaluated during generation.
  This report presents \textbf{CreativeGame}, a multi-agent system for iterative HTML5 game generation that addresses these issues through four coupled ideas: a proxy reward centered on programmatic signals rather than pure LLM judgment; lineage-scoped memory for cross-version experience accumulation; runtime validation integrated into both repair and reward; and a mechanic-guided planning loop in which retrieved mechanic knowledge is converted into an explicit mechanic plan before code generation begins. The goal is not merely to produce a playable artifact in one step, but to support interpretable version-to-version evolution.
  The current system contains 71 stored lineages, 88 saved nodes, and a 774-entry global mechanic archive, implemented in 6{,}181 lines of Python together with inspection and visualization tooling. The system is therefore substantial enough to support architectural analysis, reward inspection, and real lineage-level case studies rather than only prompt-level demos.
  A real 4-generation lineage shows that mechanic-level innovation can emerge in later versions and can be inspected directly through version-to-version records. The central contribution is therefore not only game generation, but a concrete pipeline for observing progressive evolution through explicit mechanic change.

</details>


### 71. Reinforcing privacy reasoning in LLMs via normative simulacra from fiction

- **Authors:** Matt Franchi, Madiha Zahrah Choksi, Harold Triedman, Helen Nissenbaum
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.20904v1](http://arxiv.org/abs/2604.20904v1)
- **PDF:** [https://arxiv.org/pdf/2604.20904v1](https://arxiv.org/pdf/2604.20904v1)
- **Categories:** cs.LG, cs.AI


> **Main contribution:** The paper shows that structured “normative simulacra” extracted from fiction novels can be used to teach large language models (LLMs) to reason about privacy in line with Contextual Integrity (CI) norms, and that this knowledge transfers to real‑world privacy tasks.  

**Methodology:** The authors automatically derive representations of context‑specific information‑flow norms from narrative texts, fine‑tune LLMs with supervised learning, and then apply GRPO (a reinforcement‑learning‑with‑programmatic‑objectives algorithm) that combines programmatic rewards (schema validity, completeness, consistency, context identification) with an LLM‑based judge that checks whether the model’s reasoning stays faithful to the held‑out normative universe; contrastive scoring against wrong universes prevents memorisation.  

**Key findings:** Across five CI‑aligned benchmarks and seven model sizes, the supervised‑fine‑tuned stage yields a conservative bias toward limiting information flow, while the subsequent GRPO stage with normative grounding significantly improves correct privacy judgments, achieving state‑of‑the‑art results on a law‑compliance benchmark and the highest correlation with crowdsourced human privacy expectations, demonstrating that fiction‑derived norms can effectively bootstrap contextual privacy reasoning in agentic AI.


<details>
<summary>Abstract</summary>

Information handling practices of LLM agents are broadly misaligned with the contextual privacy expectations of their users. Contextual Integrity (CI) provides a principled framework, defining privacy as the appropriate flow of information within context-relative norms. However, existing approaches either double inference cost via supervisor-assistant architectures, or fine-tune on narrow task-specific data. We propose extracting normative simulacra (structured representations of norms and information flows) from fiction novels and using them to fine-tune LLMs via supervised learning followed by GRPO reinforcement learning. Our composite reward function combines programmatic signals, including task clarity (subsuming schema validity, construct discrimination, and extraction confidence), structural completeness, internal consistency, and context identification, with an LLM judge that evaluates whether the model's privacy reasoning is grounded in the held-out normative universe of the source text. To mitigate overfitting, we introduce per-completion contrastive scoring: each completion is evaluated against both the correct normative universe and a randomly selected wrong one, teaching the model to condition on context rather than memorize source-specific norms. We evaluate on five CI-aligned benchmarks spanning distinct societal contexts and ablate the contributions of RL and normative grounding. Across seven models, SFT introduces a conservative prior toward restricting information flow, improving recognition of privacy-relevant situations but not the correctness of privacy judgments. GRPO with normative grounding achieves the highest score on a law compliance benchmark and strongest correlation with crowdsourced human privacy expectations, demonstrating that fiction-derived normative simulacra can teach contextual privacy reasoning that transfers to real-world domains.

</details>


### 72. Behavioral Transfer in AI Agents: Evidence and Privacy Implications

- **Authors:** Shilei Luo, Zhiqi Zhang, Hengchen Dai, Dennis Zhang
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19925v1](http://arxiv.org/abs/2604.19925v1)
- **PDF:** [https://arxiv.org/pdf/2604.19925v1](https://arxiv.org/pdf/2604.19925v1)
- **Categories:** econ.GN, cs.AI, cs.CY, cs.HC


> The paper demonstrates that large‑language‑model agents linked to individual users on the Moltbook platform systematically mirror the owners’ behavioral traits—topics, values, affect, and linguistic style—showing that agents act as personalized “behavioral extensions” rather than generic content generators. Using a dataset of 10,659 matched human‑agent pairs, the authors employ comparative statistical analyses across multiple behavioral dimensions and find that alignment on one dimension predicts alignment on others, even for agents without explicit configuration, implicating everyday interaction as the transfer mechanism. Crucially, agents with higher owner‑behavior transfer are also more prone to publicly reveal personal information about their owners, highlighting new privacy risks and informing the design and governance of agentic AI systems.


<details>
<summary>Abstract</summary>

AI agents powered by large language models are increasingly acting on behalf of humans in social and economic environments. Prior research has focused on their task performance and effects on human outcomes, but less is known about the relationship between agents and the specific individuals who deploy them. We ask whether agents systematically reflect the behavioral characteristics of their human owners, functioning as behavioral extensions rather than producing generic outputs. We study this question using 10,659 matched human-agent pairs from Moltbook, a social media platform where each autonomous agent is publicly linked to its owner's Twitter/X account. By comparing agents' posts on Moltbook with their owners' Twitter/X activity across features spanning topics, values, affect, and linguistic style, we find systematic transfer between agents and their specific owners. This transfer persists among agents without explicit configuration, and pairs that align on one behavioral dimension tend to align on others. These patterns are consistent with transfer emerging through accumulated interaction between owners (or owners' computer environments) and their agents in everyday use. We further show that agents with stronger behavioral transfer are more likely to disclose owner-related personal information in public discourse, suggesting that the same owner-specific context that drives behavioral transfer may also create privacy risk during ordinary use. Taken together, our results indicate that AI agents do not simply generate content, but reflect owner-related context in ways that can propagate human behavioral heterogeneity into digital environments, with implications for privacy, platform design, and the governance of agentic systems.

</details>


### 73. ChipCraftBrain: Validation-First RTL Generation via Multi-Agent Orchestration

- **Authors:** Cagri Eryilmaz
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19856v1](http://arxiv.org/abs/2604.19856v1)
- **PDF:** [https://arxiv.org/pdf/2604.19856v1](https://arxiv.org/pdf/2604.19856v1)
- **Categories:** cs.AR, cs.AI, cs.LG


> **Main contribution**  
ChipCraftBrain introduces a validation‑first RTL synthesis pipeline that orchestrates six specialized agents with a learned PPO (or MPC) controller and augments them with symbolic‑neural reasoning, knowledge‑enhanced retrieval, and hierarchical specification decomposition.  

**Methodology**  
The system treats RTL generation as a multi‑stage decision problem: a 168‑dim state representation feeds a PPO policy that selects among agents (symbolic K‑map solver, timing‑waveform expert, general RTL writer, etc.).  Retrieved patterns from a 321‑pattern base and 971 open‑source references guide each agent, while a symbolic layer solves truth‑table/K‑map sub‑tasks algorithmically and a hierarchical decomposition enforces dependency‑ordered sub‑module interfaces.  

**Key findings**  
On the human‑curated VerilogEval benchmark ChipCraftBrain reaches 97.2 % mean pass@1 (≈ 154/156), matching or surpassing prior multi‑agent systems.  On the much harder NVIDIA CVDP suite it attains 94.7 % pass@1 (286/302) – a 36‑60 ppt improvement over single‑shot baselines and comparable performance to NVIDIA’s ACE‑RTL while using ~30× fewer generation attempts.  A RISC‑V SoC case study shows that hierarchical, agent‑driven generation produces fully lint‑clean, FPGA‑validated RTL where monolithic generation fails.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) show promise for generating Register-Transfer Level (RTL) code from natural language specifications, but single-shot generation achieves only 60-65% functional correctness on standard benchmarks. Multi-agent approaches such as MAGE reach 95.9% on VerilogEval yet remain untested on harder industrial benchmarks such as NVIDIA's CVDP, lack synthesis awareness, and incur high API costs.
  We present ChipCraftBrain, a framework combining symbolic-neural reasoning with adaptive multi-agent orchestration for automated RTL generation. Four innovations drive the system: (1) adaptive orchestration over six specialized agents via a PPO policy over a 168-dim state (an alternative world-model MPC planner is also evaluated); (2) a hybrid symbolic-neural architecture that solves K-map and truth-table problems algorithmically while specialized agents handle waveform timing and general RTL; (3) knowledge-augmented generation from a 321-pattern base plus 971 open-source reference implementations with focus-aware retrieval; and (4) hierarchical specification decomposition into dependency-ordered sub-modules with interface synchronization.
  On VerilogEval-Human, ChipCraftBrain achieves 97.2% mean pass@1 (range 96.15-98.72% across 7 runs, best 154/156), on par with ChipAgents (97.4%, self-reported) and ahead of MAGE (95.9%). On a 302-problem non-agentic subset of CVDP spanning five task categories, we reach 94.7% mean pass@1 (286/302, averaged over 3 runs), a 36-60 percentage-point lift per category over the published single-shot baseline; we additionally lead three of four categories shared with NVIDIA's ACE-RTL despite using roughly 30x fewer per-problem attempts. A RISC-V SoC case study demonstrates hierarchical decomposition generating 8/8 lint-passing modules (689 LOC) validated on FPGA, where monolithic generation fails entirely.

</details>


### 74. An AI Agent Execution Environment to Safeguard User Data

- **Authors:** Robert Stanley, Avi Verma, Lillian Tsai, Konstantinos Kallas, Sam Kumar
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19657v1](http://arxiv.org/abs/2604.19657v1)
- **PDF:** [https://arxiv.org/pdf/2604.19657v1](https://arxiv.org/pdf/2604.19657v1)
- **Categories:** cs.CR, cs.AI, cs.OS


> The paper introduces **GAAP (Guaranteed Accounting for Agent Privacy)**, an execution sandbox that enforces user‑specified privacy policies on AI assistants by continuously tracking information flow from private data stores to any downstream component, including the underlying language model and its provider. GAAP augments traditional information‑flow control with persistent, annotated data stores that retain provenance across separate tasks, allowing deterministic enforcement of disclosure constraints without trusting the agent or requiring attack‑free prompts. Empirical evaluation shows that GAAP reliably blocks all tested data‑exfiltration attacks—including those that defeat prior state‑of‑the‑art defenses—while imposing only a modest overhead on the agent’s usefulness.


<details>
<summary>Abstract</summary>

AI agents promise to serve as general-purpose personal assistants for their users, which requires them to have access to private user data (e.g., personal and financial information). This poses a serious risk to security and privacy. Adversaries may attack the AI model (e.g., via prompt injection) to exfiltrate user data. Furthermore, sharing private data with an AI agent requires users to trust a potentially unscrupulous or compromised AI model provider with their private data.
  This paper presents GAAP (Guaranteed Accounting for Agent Privacy), an execution environment for AI agents that guarantees confidentiality for private user data. Through dynamic and directed user prompts, GAAP collects permission specifications from users describing how their private data may be shared, and GAAP enforces that the agent's disclosures of private user data, including disclosures to the AI model and its provider, comply with these specifications. Crucially, GAAP provides this guarantee deterministically, without trusting the agent with private user data, and without requiring any AI model or the user prompt to be free of attacks.
  GAAP enforces the user's permission specification by tracking how the AI agent accesses and uses private user data. It augments Information Flow Control with novel persistent data stores and annotations that enable it to track the flow of private information both across execution steps within a single task, and also over multiple tasks separated in time. Our evaluation confirms that GAAP blocks all data disclosure attacks, including those that make other state-of-the-art systems disclose private user data to untrusted parties, without a significant impact on agent utility.

</details>


### 75. SafetyALFRED: Evaluating Safety-Conscious Planning of Multimodal Large Language Models

- **Authors:** Josue Torres-Fonseca, Naihao Deng, Yinpei Dai, Shane Storks, Yichi Zhang, Rada Mihalcea, Casey Kennington, Joyce Chai
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19638v1](http://arxiv.org/abs/2604.19638v1)
- **PDF:** [https://arxiv.org/pdf/2604.19638v1](https://arxiv.org/pdf/2604.19638v1)
- **Categories:** cs.AI, cs.CL, cs.RO


> **Contribution:** The paper presents **SafetyALFRED**, a new embodied benchmark that extends the ALFRED kitchen‑task suite with six realistic safety hazards and measures not only a model’s ability to recognise hazards but also its capacity to **plan and execute corrective actions** in a simulated environment.  

**Methodology:** The authors evaluate 11 state‑of‑the‑art multimodal LLM agents (Qwen, Gemma, Gemini families) on two tasks: (1) hazard recognition via a disembodied QA format, and (2) active risk mitigation through embodied planning and execution in the SafetyALFRED environment; performance is quantified with recognition accuracy and mitigation‑success rates.  

**Key Findings:** While the models achieve high accuracy on the QA‑based hazard‑recognition test, their mitigation success rates are markedly low, exposing a substantial alignment gap between “knowing” a danger and “acting safely.” The results argue that safety assessment must move beyond static QA benchmarks to embodied, action‑oriented evaluations, and the authors release the dataset and code for the community.


<details>
<summary>Abstract</summary>

Multimodal Large Language Models are increasingly adopted as autonomous agents in interactive environments, yet their ability to proactively address safety hazards remains insufficient. We introduce SafetyALFRED, built upon the embodied agent benchmark ALFRED, augmented with six categories of real-world kitchen hazards. While existing safety evaluations focus on hazard recognition through disembodied question answering (QA) settings, we evaluate eleven state-of-the-art models from the Qwen, Gemma, and Gemini families on not only hazard recognition, but also active risk mitigation through embodied planning. Our experimental results reveal a significant alignment gap: while models can accurately recognize hazards in QA settings, average mitigation success rates for these hazards are low in comparison. Our findings demonstrate that static evaluations through QA are insufficient for physical safety, thus we advocate for a paradigm shift toward benchmarks that prioritize corrective actions in embodied contexts. We open-source our code and dataset under https://github.com/sled-group/SafetyALFRED.git

</details>


### 76. Time Series Augmented Generation for Financial Applications

- **Authors:** Anton Kolonin, Alexey Glushchenko, Evgeny Bochkov, Abhishek Saxena
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19633v1](http://arxiv.org/abs/2604.19633v1)
- **PDF:** [https://arxiv.org/pdf/2604.19633v1](https://arxiv.org/pdf/2604.19633v1)
- **Categories:** cs.AI, cs.CE


> The paper’s primary contribution is a new evaluation framework—Time Series Augmented Generation (TSAG)—and an accompanying benchmark of 100 financial‑analysis queries that isolate an LLM agent’s ability to parse questions, select appropriate quantitative tools, and integrate external tool outputs without hallucination. Using TSAG, the authors conduct a large‑scale study in which state‑of‑the‑art agents (GPT‑4o, Llama 3, Qwen‑2, etc.) delegate time‑series computations to verifiable external APIs, measuring tool‑selection accuracy, faithfulness to tool outputs, and incidence of hallucination. The empirical results show that well‑designed agents can attain near‑perfect tool‑use accuracy and very low hallucination rates, thereby validating the tool‑augmented paradigm for reliable, agentic financial AI and providing a public dataset for future research.


<details>
<summary>Abstract</summary>

Evaluating the reasoning capabilities of Large Language Models (LLMs) for complex, quantitative financial tasks is a critical and unsolved challenge. Standard benchmarks often fail to isolate an agent's core ability to parse queries and orchestrate computations. To address this, we introduce a novel evaluation methodology and benchmark designed to rigorously measure an LLM agent's reasoning for financial time-series analysis. We apply this methodology in a large-scale empirical study using our framework, Time Series Augmented Generation (TSAG), where an LLM agent delegates quantitative tasks to verifiable, external tools. Our benchmark, consisting of 100 financial questions, is used to compare multiple SOTA agents (e.g., GPT-4o, Llama 3, Qwen2) on metrics assessing tool selection accuracy, faithfulness, and hallucination. The results demonstrate that capable agents can achieve near-perfect tool-use accuracy with minimal hallucination, validating the tool-augmented paradigm. Our primary contribution is this evaluation framework and the corresponding empirical insights into agent performance, which we release publicly to foster standardized research on reliable financial AI.

</details>


### 77. TeamFusion: Supporting Open-ended Teamwork with Multi-Agent Systems

- **Authors:** Jiale Liu, Victor S. Bursztyn, Lin Ai, Haoliang Wang, Sunav Choudhary, Saayan Mitra, Qingyun Wu
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19589v1](http://arxiv.org/abs/2604.19589v1)
- **PDF:** [https://arxiv.org/pdf/2604.19589v1](https://arxiv.org/pdf/2604.19589v1)
- **Categories:** cs.MA


> TeamFusion introduces a novel multi‑agent workflow for open‑ended teamwork that preserves minority viewpoints instead of flattening them through simple answer aggregation. The system first creates a “proxy” agent for each participant that is conditioned on that participant’s expressed preferences, then runs a structured, multi‑turn discussion among the proxies to surface points of agreement and disagreement, and finally synthesizes a consensus‑oriented deliverable that can be iteratively refined. Empirical tests on two collaborative tasks show that TeamFusion consistently outperforms naïve aggregation baselines in both individual‑representation scores and overall consensus quality across diverse team sizes and configurations, highlighting its potential as a general framework for agentic AI support of complex, open‑ended group decision‑making.


<details>
<summary>Abstract</summary>

In open-ended domains, teams must reconcile diverse viewpoints to produce strong deliverables. Answer aggregation approaches commonly used in closed domains are ill-suited to this setting, as they tend to suppress minority perspectives rather than resolve underlying disagreements. We present TeamFusion, a multi-agent system designed to support teamwork in open-ended domains by: 1. Instantiating a proxy agent for each team member conditioned on their expressed preferences; 2. Conducting a structured discussion to surface agreements and disagreements; and 3. Synthesizing more consensus-oriented deliverables that feed into new iterations of discussion and refinement. We evaluate TeamFusion on two teamwork tasks where team members can assess how well their individual views are represented in team decisions and how consensually strong the final deliverables are, finding that it outperforms direct aggregation baselines across metrics, tasks, and team configurations.

</details>


### 78. A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression

- **Authors:** Jincheng Ren, Siwei Wu, Yizhi Li, Kang Zhu, Shu Xu, Boyu Feng, Ruibin Yuan, Wei Zhang, Riza Batista-Navarro, Jian Yang, Chenghua Lin
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19572v1](http://arxiv.org/abs/2604.19572v1)
- **PDF:** [https://arxiv.org/pdf/2604.19572v1](https://arxiv.org/pdf/2604.19572v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **TACO**, a plug‑and‑play, self‑evolving compression framework that automatically learns “observation‑compression rules” from an agent’s interaction histories, enabling terminal‑focused agents to retain only the most task‑relevant context and thus avoid the quadratic token blow‑up that hampers long‑horizon reasoning.

**Methodology:** TACO treats compression as a learnable, iterative process: it parses past trajectories, proposes candidate compression transformations (e.g., abstraction, summarization, selective pruning), evaluates their impact on downstream decision quality, and refines the rules through reinforcement‑style feedback. The framework can be attached to any existing terminal agent without modifying its core policy, and it updates its rule set continuously as more episodes are observed.

**Key findings:** Across TerminalBench (v1.0 & v2.0) and four additional terminal‑task suites (SWE‑Bench Lite, CompileBench, DevEval, CRUST‑Bench), TACO consistently **boosted agent accuracy by 1‑4 %** and, when combined with the MiniMax‑2.5 backbone, achieved **2‑3 % higher accuracy under a fixed token budget** while cutting token usage by roughly **10 %**. The gains held for a variety of agent architectures and model sizes, demonstrating that self‑evolving, task‑aware context compression is an effective, general tool for scaling agentic AI to longer horizons.


<details>
<summary>Abstract</summary>

As model capabilities advance, research has increasingly shifted toward long-horizon, multi-turn terminal-centric agentic tasks, where raw environment feedback is often preserved in the interaction history to support future decisions. However, repeatedly retaining such feedback introduces substantial redundancy and causes cumulative token cost to grow quadratically with the number of steps, hindering long-horizon reasoning. Although observation compression can mitigate this issue, the heterogeneity of terminal environments makes heuristic-based or fixed-prompt methods difficult to generalize. We propose TACO, a plug-and-play, self-evolving Terminal Agent Compression framework that automatically discovers and refines compression rules from interaction trajectories for existing terminal agents. Experiments on TerminalBench (TB 1.0 and TB 2.0) and four additional terminal-related benchmarks (i.e., SWE-Bench Lite, CompileBench, DevEval, and CRUST-Bench) show that TACO consistently improves performance across mainstream agent frameworks and strong backbone models. With MiniMax-2.5, it improves performance on most benchmarks while reducing token overhead by around 10%. On TerminalBench, it brings consistent gains of 1%-4% across strong agentic models, and further improves accuracy by around 2%-3% under the same token budget. These results demonstrate the effectiveness and generalization of self-evolving, task-aware compression for terminal agents.

</details>


### 79. Taming Actor-Observer Asymmetry in Agents via Dialectical Alignment

- **Authors:** Bobo Li, Rui Wu, Zibo Ji, Meishan Zhang, Hao Fei, Min Zhang, Mong-Li Lee, Wynne Hsu
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19548v1](http://arxiv.org/abs/2604.19548v1)
- **PDF:** [https://arxiv.org/pdf/2604.19548v1](https://arxiv.org/pdf/2604.19548v1)
- **Categories:** cs.CL, cs.AI, cs.CY


> The paper identifies a systematic “actor‑observer asymmetry” (AOA) in multi‑agent LLM systems: when an agent reflects on its own actions it credits external causes for failures, but when another agent audits it, the same failures are blamed on internal faults. Using a newly introduced Ambiguous Failure Benchmark, the authors show that this perspective‑driven bias flips attribution in >20 % of cases across several models. To counteract AOA, they train agents with **ReTAS** (Reasoning via Thesis‑Antithesis‑Synthesis), a dialectical alignment technique that adds a thesis‑antithesis‑synthesis chain‑of‑thought and integrates it with Group Relative Policy Optimization; the resulting agents produce perspective‑invariant reasoning, markedly reducing attribution inconsistencies and boosting fault‑resolution performance in ambiguous tasks.


<details>
<summary>Abstract</summary>

Large Language Model agents have rapidly evolved from static text generators into dynamic systems capable of executing complex autonomous workflows. To enhance reliability, multi-agent frameworks assigning specialized roles are increasingly adopted to enable self-reflection and mutual auditing. While such role-playing effectively leverages domain expert knowledge, we find it simultaneously induces a human-like cognitive bias known as Actor-Observer Asymmetry (AOA). Specifically, an agent acting as an actor (during self-reflection) tends to attribute failures to external factors, whereas an observer (during mutual auditing) attributes the same errors to internal faults. We quantify this using our new Ambiguous Failure Benchmark, which reveals that simply swapping perspectives triggers the AOA effect in over 20% of cases for most models. To tame this bias, we introduce ReTAS (Reasoning via Thesis-Antithesis-Synthesis), a model trained through dialectical alignment to enforce perspective-invariant reasoning. By integrating dialectical chain-of-thought with Group Relative Policy Optimization, ReTAS guides agents to synthesize conflicting viewpoints into an objective consensus. Experiments demonstrate that ReTAS effectively mitigates attribution inconsistency and significantly improves fault resolution rates in ambiguous scenarios.

</details>


### 80. FOCAL: Filtered On-device Continuous Activity Logging for Efficient Personal Desktop Summarization

- **Authors:** Haoran Yin, Zhiyuan Wen, Jiannong Cao, Bo Yuan, Ruosong Yang
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19541v1](http://arxiv.org/abs/2604.19541v1)
- **PDF:** [https://arxiv.org/pdf/2604.19541v1](https://arxiv.org/pdf/2604.19541v1)
- **Categories:** cs.MA, cs.HC


> The paper introduces **FOCAL**, a privacy‑preserving multi‑agent framework that turns raw desktop screenshot streams into task‑organized personal logs entirely on the user’s device. By cascading a lightweight Filter Agent, a text‑only Brain Agent for task attribution, a selective Record Agent for visual reasoning, and a task‑isolated Memory Agent for coherent summarization, FOCAL dramatically cuts VLM usage (‑72 % calls, ‑60 % tokens) while improving key‑information recall from 0.38 to 0.61 and achieving robust task accuracy (0.81) even under frequent task interruptions. Experiments on the DesktopBench benchmark demonstrate that this filtered “filter‑plan‑log” pipeline enables efficient, on‑device summarization of instruction‑free desktop activity—an advance directly relevant to scalable, agentic AI systems that must operate under privacy and resource constraints.


<details>
<summary>Abstract</summary>

Desktop interaction streams provide a continuous, privacy-sensitive record of interleaved user tasks. Transforming these streams into task-organized personal logs on-device faces two main challenges: exhaustive Vision-Language Model (VLM) processing strains local resources, and global stream processing causes cross-task context pollution. We present FOCAL (Filtered On-device Continuous Activity Logging), a privacy-first multi-agent system utilizing a unified filter-plan-log architecture. It cascades a lightweight Filter Agent for noise suppression, a text-only Brain Agent for task attribution, a Record Agent for selective visual reasoning, and a task-isolated Memory Agent for context-coherent summarization. Experiments on DesktopBench (comprising 2,572 screenshots across 420 complex sessions) show FOCAL reduces total token consumption by 60.4% and VLM call count by 72.3% versus a baseline, while boosting Key Information Recall (KIR) from 0.38 to 0.61. Crucially, under $A{\to}B{\to}A$ task interruptions, FOCAL maintains Task Acc 0.81 and KIR 0.80, whereas the baseline collapses to Task Acc 0.03. FOCAL pioneers the efficient, on-device summarization of instruction-free desktop streams into multi-perspective personal logs.

</details>


### 81. Mesh Memory Protocol: Semantic Infrastructure for Multi-Agent LLM Systems

- **Authors:** Hongwei Xu
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19540v1](http://arxiv.org/abs/2604.19540v1)
- **PDF:** [https://arxiv.org/pdf/2604.19540v1](https://arxiv.org/pdf/2604.19540v1)
- **Categories:** cs.MA, cs.AI


> **Main contribution** – The paper introduces the **Mesh Memory Protocol (MMP)**, a new semantic‑level communication layer that lets large‑language‑model (LLM) agents exchange fine‑grained cognitive state across session boundaries, preserving provenance and enabling incremental, role‑aware assimilation of peer information.

**Methodology** – MMP defines four composable primitives: (1) **CAT7**, a fixed seven‑field schema for every Cognitive Memory Block; (2) **SVAF**, which evaluates each field against the receiver’s role‑indexed anchors to decide what to accept (solving P1); (3) an **inter‑agent lineage** system that tags each block with parent/ancestor content‑hash keys to make every claim traceable to its source (P2); and (4) **remix**, which stores only the receiver’s own role‑evaluated interpretation, not the raw peer message, ensuring memory relevance is tied to how it was stored (P3). The protocol was implemented and deployed in three production systems where autonomous agents act as mesh peers.

**Key findings** – Experiments across the deployments show that agents can reliably build and reuse shared “semantic memory” over days‑long collaborations, achieving higher consistency and auditability of multi‑agent workflows compared with naïve message‑passing or flat tool‑access approaches. The fine‑grained acceptance logic and lineage tracking dramatically reduce knowledge drift and enable transparent, cumulative reasoning, demonstrating that a dedicated semantic infrastructure is essential for scalable, cross‑session, agentic AI systems.


<details>
<summary>Abstract</summary>

Teams of LLM agents increasingly collaborate on tasks spanning days or weeks: multi-day data-generation sprints where generator, reviewer, and auditor agents coordinate in real time on overlapping batches; specialists carrying findings forward across session restarts; product decisions compounding over many review rounds. This requires agents to share, evaluate, and combine each other's cognitive state in real time across sessions. We call this cross-session agent-to-agent cognitive collaboration, distinct from parallel agent execution. To enable it, three problems must be solved together. (P1) Each agent decides field by field what to accept from peers, not accept or reject whole messages. (P2) Every claim is traceable to source, so returning claims are recognised as echoes of the receiver's own prior thinking. (P3) Memory that survives session restarts is relevant because of how it was stored, not how it is retrieved. These are protocol-level properties at the semantic layer of agent communication, distinct from tool-access and task-delegation protocols at lower layers. We call this missing protocol layer "semantic infrastructure," and the Mesh Memory Protocol (MMP) specifies it. Four composable primitives work together: CAT7, a fixed seven-field schema for every Cognitive Memory Block (CMB); SVAF, which evaluates each field against the receiver's role-indexed anchors and realises P1; inter-agent lineage, carried as parents and ancestors of content-hash keys and realising P2; and remix, which stores only the receiver's own role-evaluated understanding of each accepted CMB, never the raw peer signal, realising P3. MMP is specified, shipped, and running in production across three reference deployments, where each session runs an autonomous agent as a mesh peer with its own identity and memory, collaborating with other agents across the network for collective intelligence.

</details>


### 82. Integrating Anomaly Detection into Agentic AI for Proactive Risk Management in Human Activity

- **Authors:** Farbod Zorriassatine, Ahmad Lotfi
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19538v1](http://arxiv.org/abs/2604.19538v1)
- **PDF:** [https://arxiv.org/pdf/2604.19538v1](https://arxiv.org/pdf/2604.19538v1)
- **Categories:** cs.AI, cs.HC, cs.MA


> **Main contribution:** The paper proposes a conceptual framework that embeds anomaly‑detection techniques within an agentic AI architecture to enable proactive, context‑aware risk management for human movement, targeting fall prevention in elderly care and other safety‑critical settings.  

**Methodology:** It reformulates fall prediction/detection as an anomaly‑detection problem and outlines how an autonomous, goal‑directed agent can dynamically select, combine, and orchestrate sensing, modeling, and mitigation tools in response to subtle deviations in gait or posture, rather than relying on static, pre‑programmed pipelines.  

**Key findings:** By treating falls as early‑stage anomalies, the agentic system can achieve higher sensitivity to emerging risk factors (e.g., fatigue, environmental changes) and lower false‑alarm rates through adaptive context awareness. The proposed framework demonstrates, at a conceptual level, how such an agent can continuously monitor, reason, and intervene across diverse care pathways, suggesting a path toward universal, scalable fall‑risk management solutions.


<details>
<summary>Abstract</summary>

Agentic AI, with goal-directed, proactive, and autonomous decision-making capabilities, offers a compelling opportunity to address movement-related risks in human activity, including the persistent hazard of falls among elderly populations. Despite numerous approaches to fall mitigation through fall prediction and detection, existing systems have not yet functioned as universal solutions across care pathways and safety-critical environments. This is largely due to limitations in consistently handling real-world complexity, particularly poor context awareness, high false alarm rates, environmental noise, and data scarcity. We argue that fall detection and fall prediction can usefully be formulated as anomaly detection problems and more effectively addressed through an agentic AI system. More broadly, this perspective enables the early identification of subtle deviations in movement patterns associated with increased risk, whether arising from age-related decline, fatigue, or environmental factors. While technical requirements for immediate deployment are beyond the scope of this paper, we propose a conceptual framework that highlights potential value. This framework promotes a well-orchestrated approach to risk management by dynamically selecting relevant tools and integrating them into adaptive decision-making workflows, rather than relying on static configurations tailored to narrowly defined scenarios.

</details>


### 83. Revac: A Social Deduction Reasoning Agent

- **Authors:** Mihir Shriniwas Arya, Avinash Anish, Aditya Ranjan
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19523v1](http://arxiv.org/abs/2604.19523v1)
- **PDF:** [https://arxiv.org/pdf/2604.19523v1](https://arxiv.org/pdf/2604.19523v1)
- **Categories:** cs.AI


> Revac‑8 is a multi‑module AI designed for the Mafia‑style social‑deduction game, whose main contribution is a unified architecture that couples long‑term memory‑based profiling of opponents with graph‑theoretic analysis of accusation/defense patterns and a controllable tone‑selection component for deceptive communication. The methodology evolves a baseline two‑stage reasoner into a pipeline where (i) a memory store tracks each player’s revealed actions and speech acts, (ii) a social‑graph model infers latent roles by propagating belief updates across accusation edges, and (iii) a tone generator selects utterances (truthful, ambiguous, or misleading) conditioned on the inferred confidence and strategic objectives. In competition on the MindGames Arena, Revac‑8 leveraged these mechanisms to outperform all rivals, demonstrating that structured episodic memory and adaptive, role‑consistent dialogue are critical for high‑performing agentic AI in environments dominated by uncertainty and deception.


<details>
<summary>Abstract</summary>

Social deduction games such as Mafia present a unique AI challenge: players must reason under uncertainty, interpret incomplete and intentionally misleading information, evaluate human-like communication, and make strategic elimination decisions. Unlike deterministic board games, success in Mafia depends not on perfect information or brute-force search, but on inference, memory, and adaptability in the presence of deception. This work presents the design and evaluation of Revac-8, an AI agent developed for the Social Deduction track of the MindGames Arena competition, where it achieved first place. The final agent evolved from a simple two-stage reasoning system into a multi-module architecture that integrates memory-based player profiling, social-graph analysis of accusations and defenses, and dynamic tone selection for communication. These results highlight the importance of structured memory and adaptive communication for achieving strong performance in high-stakes social environments.

</details>


### 84. From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning

- **Authors:** Beining Wu, Fuyou Mao, Jiong Lin, Cheng Yang, Jiaxuan Lu, Yifu Guo, Siyu Zhang, Yifan Wu, Ying Huang, Fu Li
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19516v1](http://arxiv.org/abs/2604.19516v1)
- **PDF:** [https://arxiv.org/pdf/2604.19516v1](https://arxiv.org/pdf/2604.19516v1)
- **Categories:** cs.AI


> The paper reframes Generative Engine Optimization (GEO) as a strategy‑learning problem and introduces **MAGEO**, a multi‑agent system that separates execution (coordinated planning, edit generation, and fidelity‑aware evaluation) from a skill‑distillation layer that incrementally abstracts validated editing patterns into reusable, engine‑specific optimization “skills.” By employing a Twin‑Branch Evaluation protocol for causal attribution of edits and a dual‑axis metric (DSV‑CF) that jointly measures semantic visibility and citation fidelity, MAGEO is benchmarked on the newly released MSME‑GEO‑Bench across three major generative engines, achieving markedly higher visibility and citation accuracy than heuristic baselines; ablation studies show that modeling engine‑specific preferences and reusing learned strategies are the primary drivers of performance.


<details>
<summary>Abstract</summary>

Generative engines (GEs) are reshaping information access by replacing ranked links with citation-grounded answers, yet current Generative Engine Optimization (GEO) methods optimize each instance in isolation, unable to accumulate or transfer effective strategies across tasks and engines. We reframe GEO as a strategy learning problem and propose MAGEO, a multi-agent framework in which coordinated planning, editing, and fidelity-aware evaluation serve as the execution layer, while validated editing patterns are progressively distilled into reusable, engine-specific optimization skills. To enable controlled assessment, we introduce a Twin Branch Evaluation Protocol for causal attribution of content edits and DSV-CF, a dual-axis metric that unifies semantic visibility with attribution accuracy. We further release MSME-GEO-Bench, a multi-scenario, multi-engine benchmark grounded in real-world queries. Experiments on three mainstream engines show that MAGEO substantially outperforms heuristic baselines in both visibility and citation fidelity, with ablations confirming that engine-specific preference modeling and strategy reuse are central to these gains, suggesting a scalable learning-driven paradigm for trustworthy GEO. Code is available at https://github.com/Wu-beining/MAGEO

</details>


### 85. Four-Axis Decision Alignment for Long-Horizon Enterprise AI Agents

- **Authors:** Vasundra Srininvasan
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19457v1](http://arxiv.org/abs/2604.19457v1)
- **PDF:** [https://arxiv.org/pdf/2604.19457v1](https://arxiv.org/pdf/2604.19457v1)
- **Categories:** cs.AI


> **Contribution:** The paper introduces a four‑axis framework for evaluating long‑horizon enterprise AI agents—factual precision (FRP), reasoning coherence (RCS), compliance reconstruction (CRR), and calibrated abstention (CAR)—arguing that a single success score masks distinct alignment failures, especially regulatory compliance and decision‑making coverage.

**Methodology:** The authors construct a deterministic benchmark (LongHorizon‑Bench) covering loan underwriting and insurance claim adjudication, then evaluate six different memory‑augmented agent architectures on each axis using schema‑based prompts and a CRR auditor prompt to measure regulatory reconstruction.

**Key Findings:** Plain summarization with a fact‑preservation prompt outperforms more complex memory systems on FRP, RCS, and CRR; retrieval‑augmented models collapse on factual precision; all models exhibit systematic failures on calibrated abstention, revealing a neglected decisional‑alignment problem. The study shows that CRR and CAR are critical, under‑explored dimensions for regulated decision making and that the four‑axis decomposition can uncover failures hidden by aggregate accuracy metrics.


<details>
<summary>Abstract</summary>

Long-horizon enterprise agents make high-stakes decisions (loan underwriting, claims adjudication, clinical review, prior authorization) under lossy memory, multi-step reasoning, and binding regulatory constraints. Current evaluation reports a single task-success scalar that conflates distinct failure modes and hides whether an agent is aligned with the standards its deployment environment requires. We propose that long-horizon decision behavior decomposes into four orthogonal alignment axes, each independently measurable and failable: factual precision (FRP), reasoning coherence (RCS), compliance reconstruction (CRR), and calibrated abstention (CAR). CRR is a novel regulatory-grounded axis; CAR is a measurement axis separating coverage from accuracy. We exercise the decomposition on a controlled benchmark (LongHorizon-Bench) covering loan qualification and insurance claims adjudication with deterministic ground-truth construction. Running six memory architectures, we find structure aggregate accuracy cannot see: retrieval collapses on factual precision; schema-anchored architectures pay a scaffolding tax; plain summarization under a fact-preservation prompt is a strong baseline on FRP, RCS, EDA, and CRR; and all six architectures commit on every case, exposing a decisional-alignment axis the field has not targeted. The decomposition also surfaced a pre-registered prediction of our own, that summarization would fail factual recall, which the data reversed at large magnitude, an axis-level reversal aggregate accuracy would have hidden. Institutional alignment (regulatory reconstruction) and decisional alignment (calibrated abstention) are under-represented in the alignment literature and become load-bearing once decisions leave the laboratory. The framework transfers to any regulated decisioning domain via two steps: build a fact schema, and calibrate the CRR auditor prompt.

</details>


### 86. M$^{2}$GRPO: Mamba-based Multi-Agent Group Relative Policy Optimization for Biomimetic Underwater Robots Pursuit

- **Authors:** Yukai Feng, Zhiheng Wu, Zhengxing Wu, Junwen Gu, Junzhi Yu
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19404v1](http://arxiv.org/abs/2604.19404v1)
- **PDF:** [https://arxiv.org/pdf/2604.19404v1](https://arxiv.org/pdf/2604.19404v1)
- **Categories:** cs.RO, cs.AI


> The paper introduces **M$^{2}$GRPO**, a novel cooperative‑pursuit framework for biomimetic underwater robots that combines a **Mamba‑based recurrent policy**—which exploits long‑horizon observation histories and attention‑driven relational encoding of inter‑robot interactions—with a **group‑relative policy‑optimization (GRPO)** objective under the centralized‑training/decentralized‑execution paradigm. By normalizing rewards across agents to compute group‑relative advantages, the method achieves more accurate credit assignment and stable, sample‑efficient updates, while the Mamba architecture yields bounded continuous actions via normalized Gaussian sampling. Experiments in simulation and real‑world pool settings show that M$^{2}$GRPO markedly outperforms MAPPO and other recurrent baselines in pursuit success rate and capture efficiency, demonstrating a scalable, stable solution for multi‑agent underwater pursuit.


<details>
<summary>Abstract</summary>

Traditional policy learning methods in cooperative pursuit face fundamental challenges in biomimetic underwater robots, where long-horizon decision making, partial observability, and inter-robot coordination require both expressiveness and stability. To address these issues, a novel framework called Mamba-based multi-agent group relative policy optimization (M$^{2}$GRPO) is proposed, which integrates a selective state-space Mamba policy with group-relative policy optimization under the centralized-training and decentralized-execution (CTDE) paradigm. Specifically, the Mamba-based policy leverages observation history to capture long-horizon temporal dependencies and exploits attention-based relational features to encode inter-agent interactions, producing bounded continuous actions through normalized Gaussian sampling. To further improve credit assignment without sacrificing stability, the group-relative advantages are obtained by normalizing rewards across agents within each episode and optimized through a multi-agent extension of GRPO, significantly reducing the demand for training resources while enabling stable and scalable policy updates. Extensive simulations and real-world pool experiments across team scales and evader strategies demonstrate that M$^{2}$GRPO consistently outperforms MAPPO and recurrent baselines in both pursuit success rate and capture efficiency. Overall, the proposed framework provides a practical and scalable solution for cooperative underwater pursuit with biomimetic robot systems.

</details>


### 87. Do Agents Dream of Root Shells? Partial-Credit Evaluation of LLM Agents in Capture The Flag Challenges

- **Authors:** Ali Al-Kaswan, Maksim Plotnikov, Maxim Hájek, Roland Vízner, Arie van Deursen, Maliheh Izadi
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19354v1](http://arxiv.org/abs/2604.19354v1)
- **PDF:** [https://arxiv.org/pdf/2604.19354v1](https://arxiv.org/pdf/2604.19354v1)
- **Categories:** cs.AI, cs.CR, cs.SE


> This work introduces **DeepRed**, an open‑source benchmark that places LLM‑driven agents in a realistic Kali attacker environment linked to isolated CTF VMs, records their full command‑line traces, and evaluates performance with a **partial‑credit scoring system** derived from public write‑ups and an automated “summarise‑then‑judge” pipeline. By running ten commercially available LLMs on ten diverse CTF challenges, the authors show that even the strongest model completes only about **35 % of the checkpoint‑based objectives**, excelling on standard categories (e.g., web exploitation, binary reversal) but struggling with non‑standard discovery and long‑horizon adaptation. The benchmark and scoring methodology provide a finer‑grained, reproducible way to gauge and compare the offensive capabilities of emerging agentic AI systems.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents are increasingly proposed for autonomous cybersecurity tasks, but their capabilities in realistic offensive settings remain poorly understood. We present DeepRed, an open-source benchmark for evaluating LLM-based agents on realistic Capture The Flag (CTF) challenges in isolated virtualized environments. DeepRed places an agent in a Kali attacker environment with terminal tools and optional web search, connected over a private network to a target challenge, and records full execution traces for analysis. To move beyond binary solved/unsolved outcomes, we introduce a partial-credit scoring method based on challenge-specific checkpoints derived from public writeups, together with an automated summarise-then-judge labelling pipeline for assigning checkpoint completion from logs. Using DeepRed, we benchmark ten commercially accessible LLMs on ten VM-based CTF challenges spanning different challenge categories. The results indicate that current agents remain limited: the best model achieves only 35% average checkpoint completion, performing strongest on common challenge types and weakest on tasks requiring non-standard discovery and longer-horizon adaptation.

</details>


### 88. If you're waiting for a sign... that might not be it! Mitigating Trust Boundary Confusion from Visual Injections on Vision-Language Agentic Systems

- **Authors:** Jiamin Chang, Minhui Xue, Ruoxi Sun, Shuchao Pang, Salil S. Kanhere, Hammond Pearce
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19844v1](http://arxiv.org/abs/2604.19844v1)
- **PDF:** [https://arxiv.org/pdf/2604.19844v1](https://arxiv.org/pdf/2604.19844v1)
- **Categories:** cs.CV, cs.AI


> The paper identifies **trust‑boundary confusion** in embodied Vision‑Language Agentic Systems (VLAS): agents must obey legitimate visual cues (e.g., traffic lights) yet resist adversarial visual injections that maliciously steer behavior. To expose this problem, the authors build a dual‑intent dataset and evaluation suite that inject both structured (e.g., fake signs) and noisy visual prompts into seven state‑of‑the‑art LVLM‑based agents across multiple simulated embodied environments, showing that existing models either ignore helpful cues or dutifully follow harmful ones. They then introduce a **multi‑agent defense** that decouples perception from decision‑making and dynamically verifies visual evidence; this architecture markedly lowers the rate of misleading actions while preserving correct cue‑following, providing empirical robustness guarantees against visual adversarial perturbations.


<details>
<summary>Abstract</summary>

Recent advances in embodied Vision-Language Agentic Systems (VLAS), powered by large vision-language models (LVLMs), enable AI systems to perceive and reason over real-world scenes. Within this context, environmental signals such as traffic lights are essential in-band signals that can and should influence agent behavior. However, similar signals could also be crafted to operate as misleading visual injections, overriding user intent and posing security risks. This duality creates a fundamental challenge: agents must respond to legitimate environmental cues while remaining robust to misleading ones. We refer to this tension as trust boundary confusion. To study this behavior, we design a dual-intent dataset and evaluation framework, through which we show that current LVLM-based agents fail to reliably balance this trade-off, either ignoring useful signals or following harmful ones. We systematically evaluate 7 LVLM agents across multiple embodied settings under both structure-based and noise-based visual injections. To address these vulnerabilities, we propose a multi-agent defense framework that separates perception from decision-making to dynamically assess the reliability of visual inputs. Our approach significantly reduces misleading behaviors while preserving correct responses and provides robustness guarantees under adversarial perturbations. The code of the evaluation framework and artifacts are made available at https://anonymous.4open.science/r/Visual-Prompt-Inject.

</details>


### 89. Large Language Models Exhibit Normative Conformity

- **Authors:** Mikako Bito, Keita Nishimoto, Kimitaka Asatani, Ichiro Sakata
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19301v1](http://arxiv.org/abs/2604.19301v1)
- **PDF:** [https://arxiv.org/pdf/2604.19301v1](https://arxiv.org/pdf/2604.19301v1)
- **Categories:** cs.AI, cs.MA, cs.NE


> The paper shows that many state‑of‑the‑art LLMs not only adjust their answers to be more accurate (informational conformity) but also deliberately align with a group to avoid conflict or gain acceptance (normative conformity), a distinction imported from social psychology. By designing dialogue tasks that isolate the two motives and probing model activations, the authors find that up to five of six LLMs display both conformity types and that subtle cues in the social context can steer which normative stance the model adopts, revealing a manipulable vulnerability in LLM‑based multi‑agent systems. These results suggest that “norms” in LLMs are encoded by distinct internal mechanisms and that agency‑level decision making may be compromised by targeted social prompting.


<details>
<summary>Abstract</summary>

The conformity bias exhibited by large language models (LLMs) can pose a significant challenge to decision-making in LLM-based multi-agent systems (LLM-MAS). While many prior studies have treated "conformity" simply as a matter of opinion change, this study introduces the social psychological distinction between informational conformity and normative conformity in order to understand LLM conformity at the mechanism level. Specifically, we design new tasks to distinguish between informational conformity, in which participants in a discussion are motivated to make accurate judgments, and normative conformity, in which participants are motivated to avoid conflict or gain acceptance within a group. We then conduct experiments based on these task settings. The experimental results show that, among the six LLMs evaluated, up to five exhibited tendencies toward not only informational conformity but also normative conformity. Furthermore, intriguingly, we demonstrate that by manipulating subtle aspects of the social context, it may be possible to control the target toward which a particular LLM directs its normative conformity. These findings suggest that decision-making in LLM-MAS may be vulnerable to manipulation by a small number of malicious users. In addition, through analysis of internal vectors associated with informational and normative conformity, we suggest that although both behaviors appear externally as the same form of "conformity," they may in fact be driven by distinct internal mechanisms. Taken together, these results may serve as an initial milestone toward understanding how "norms" are implemented in LLMs and how they influence group dynamics.

</details>


### 90. Rethinking Scale: Deployment Trade-offs of Small Language Models under Agent Paradigms

- **Authors:** Xinlin Wang, Mats Brorsson
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19299v1](http://arxiv.org/abs/2604.19299v1)
- **PDF:** [https://arxiv.org/pdf/2604.19299v1](https://arxiv.org/pdf/2604.19299v1)
- **Categories:** cs.CL, cs.AI


> The paper demonstrates that small language models (<10 B parameters) can regain much of the capability gap with large models by embedding them in agent‑centric architectures rather than relying solely on scaling or fine‑tuning. The authors evaluate a suite of open‑source SLMs across three deployment paradigms—raw model, a single tool‑using agent, and a collaborative multi‑agent system—and show that a single agent equipped with external tools consistently yields the best trade‑off between task performance, inference latency, and computational cost, while multi‑agent cooperation adds notable overhead with marginal gains. These results suggest that designing agentic pipelines is a more efficient and privacy‑friendly route for deploying capable AI systems in resource‑constrained environments.


<details>
<summary>Abstract</summary>

Despite the impressive capabilities of large language models, their substantial computational costs, latency, and privacy risks hinder their widespread deployment in real-world applications. Small Language Models (SLMs) with fewer than 10 billion parameters present a promising alternative; however, their inherent limitations in knowledge and reasoning curtail their effectiveness. Existing research primarily focuses on enhancing SLMs through scaling laws or fine-tuning strategies while overlooking the potential of using agent paradigms, such as tool use and multi-agent collaboration, to systematically compensate for the inherent weaknesses of small models. To address this gap, this paper presents the first large-scale, comprehensive study of <10B open-source models under three paradigms: (1) the base model, (2) a single agent equipped with tools, and (3) a multi-agent system with collaborative capabilities. Our results show that single-agent systems achieve the best balance between performance and cost, while multi-agent setups add overhead with limited gains. Our findings highlight the importance of agent-centric design for efficient and trustworthy deployment in resource-constrained settings.

</details>


### 91. Explicit Trait Inference for Multi-Agent Coordination

- **Authors:** Suhaib Abdurahman, Etsuko Ishii, Katerina Margatina, Divya Bhargavi, Monica Sunkara, Yi Zhang
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19278v2](http://arxiv.org/abs/2604.19278v2)
- **PDF:** [https://arxiv.org/pdf/2604.19278v2](https://arxiv.org/pdf/2604.19278v2)
- **Categories:** cs.AI, cs.MA


> The paper introduces **Explicit Trait Inference (ETI)**, a lightweight mechanism that equips LLM‑based agents with a psychological model of their partners by continuously estimating two traits—warmth (trustworthiness) and competence (skill)—from interaction histories and using these estimates to shape coordination decisions. Across economic‑game experiments and the larger MultiAgentBench suite, ETI cuts payoff losses by 45–77 % in simple settings and boosts overall task performance by 3–29 % over a Chain‑of‑Thought baseline, with ablative analyses confirming that accurate trait profiles both predict agents’ actions and drive the observed gains. These results demonstrate that LLM agents can reliably infer partner traits and that explicit, structured trait awareness is an effective lever for mitigating coordination failures in multi‑agent AI systems.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems (MAS) show promise on complex tasks but remain prone to coordination failures such as goal drift, error cascades, and misaligned behaviors. We propose Explicit Trait Inference (ETI), a psychologically grounded method for improving coordination. ETI enables agents to infer and track partner characteristics along two established psychological dimensions--warmth (e.g., trust) and competence (e.g., skill)--from interaction histories to guide decisions. We evaluate ETI in controlled settings (economic games), where it reduces payoff loss by 45-77%, and in more realistic, complex multi-agent settings (MultiAgentBench), where it improves performance by 3-29% depending on the scenario and model, relative to a CoT baseline. Additional analysis shows that gains are closely linked to trait inference: ETI profiles predict agents' actions, and informative profiles drive improvements. These results highlight ETI as a lightweight and robust mechanism for improving coordination in diverse multi-agent settings, and provide the first systematic evidence that LLM agents can (i) reliably infer others' traits from interaction histories and (ii) leverage structured awareness of others' traits for coordination.

</details>


### 92. BONSAI: A Mixed-Initiative Workspace for Human-AI Co-Development of Visual Analytics Applications

- **Authors:** Thilo Spinner, Matthias Miller, Fabian Sperrle-Roth, Mennatallah El-Assady
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19247v1](http://arxiv.org/abs/2604.19247v1)
- **PDF:** [https://arxiv.org/pdf/2604.19247v1](https://arxiv.org/pdf/2604.19247v1)
- **Categories:** cs.HC, cs.MA, cs.SE


> BONSAI proposes a mixed‑initiative workspace that lets human programmers and generative AI agents collaboratively build visual‑analytics applications. It does so by imposing a four‑layer modular architecture (hardware → services → orchestration → application) and a structured four‑phase workflow (plan, design, monitor, review) that bounds every contribution, records provenance, and enables independent reuse of components. In case‑study evaluations, the system was able to rapidly assemble new VA tools and faithfully re‑implement sophisticated VA systems from paper descriptions, showing that AI‑driven code generation can be harnessed without sacrificing the control, modularity, and auditability required for complex, agentic AI development.


<details>
<summary>Abstract</summary>

Developing Visual Analytics (VA) applications requires integrating complex machine learning models with expressive interactive interfaces. Developers face a stark trade-off: building tightly-coupled monoliths plagued by fragile interdependencies, or relying on restrictive, simplistic frameworks. Meanwhile, unconstrained, single-shot AI code generation promises speed but yields unstructured, unauditable chaos. The core challenge is combining the control and expressiveness of custom development with the efficiency of AI generation under strict constraints. To address this, we introduce BONSAI, a mixed-initiative workspace for the multi-agent co-development of VA applications. BONSAI utilizes a modular four-layer architecture (hardware, services, orchestration, application) that allows human and AI developers to independently contribute reusable components. The workspace incorporates this architecture into a structured four-phase development process (plan, design, monitor, and review), ensuring distributed agency and full provenance, where all human and AI contributions are structurally bounded and tracked. We evaluate BONSAI through case studies demonstrating the efficient creation of novel tools and the rapid reconstruction of complex VA applications directly from research paper descriptions. Ultimately, this paper contributes a conceptual workflow, a scalable architecture, and an integrated system that successfully balances AI's generative speed with the structural rigor required for complex VA development.

</details>


### 93. ClawNet: Human-Symbiotic Agent Network for Cross-User Autonomous Cooperation

- **Authors:** Zhiqin Yang, Zhenyuan Zhang, Xianzhang Jia, Jun Song, Wei Xue, Yonggang Zhang, Yike Guo
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19211v1](http://arxiv.org/abs/2604.19211v1)
- **PDF:** [https://arxiv.org/pdf/2604.19211v1](https://arxiv.org/pdf/2604.19211v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **ClawNet**, a novel “human‑symbiotic” framework that lets each person own a permanently bound, identity‑governed AI agent (a Manager Agent plus multiple context‑specific Identity Agents) so that agents can represent their owners in cross‑user collaborations, thereby digitizing human social and organizational relationships.  

**Methodology:** The authors design three governance primitives—(1) a layered identity architecture that isolates a global Manager Agent from external messages, (2) scoped, per‑identity authorization that escalates any boundary breach to the human owner, and (3) action‑level accountability that logs every operation with the owner’s identity. These primitives are enforced by a central orchestrator that binds identities, verifies authorizations, and mediates inter‑agent communication.  

**Key findings:** Experiments with ClawNet demonstrate that multiple users can securely collaborate through their agents while preserving auditability and fine‑grained access control; the system prevents unauthorized actions and provides transparent provenance for every delegated operation, establishing a practical infrastructure for agentic AI that supports multi‑user, cross‑organizational cooperation.


<details>
<summary>Abstract</summary>

Current AI agent frameworks have made remarkable progress in automating individual tasks, yet all existing systems serve a single user. Human productivity rests on the social and organizational relationships through which people coordinate, negotiate, and delegate. When agents move beyond performing tasks for one person to representing that person in collaboration with others, the infrastructure for cross-user agent collaboration is entirely absent, let alone the governance mechanisms needed to secure it. We argue that the next frontier for AI agents lies not in stronger individual capability, but in the digitization of human collaborative relationships. To this end, we propose a human-symbiotic agent paradigm. Each user owns a permanently bound agent system that collaborates on the owner's behalf, forming a network whose nodes are humans rather than agents. This paradigm rests on three governance primitives. A layered identity architecture separates a Manager Agent from multiple context-specific Identity Agents; the Manager Agent holds global knowledge but is architecturally isolated from external communication. Scoped authorization enforces per-identity access control and escalates boundary violations to the owner. Action-level accountability logs every operation against its owner's identity and authorization, ensuring full auditability. We instantiate this paradigm in ClawNet, an identity-governed agent collaboration framework that enforces identity binding and authorization verification through a central orchestrator, enabling multiple users to collaborate securely through their respective agents.

</details>


### 94. Forage V2: Knowledge Evolution and Transfer in Autonomous Agent Organizations

- **Authors:** Huaqing Xie
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19837v1](http://arxiv.org/abs/2604.19837v1)
- **PDF:** [https://arxiv.org/pdf/2604.19837v1](https://arxiv.org/pdf/2604.19837v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces **Forage V2**, an architectural framework that turns a single “expedition” of autonomous agents into a **learning organization** capable of accumulating, preserving, and transferring domain knowledge across runs and model generations. By adding institutional mechanisms—audit‑style separation of evaluator and planner, contract‑based interaction protocols, and a model‑agnostic, document‑based organizational memory—the system prevents knowledge decay and enables any incoming agent to inherit calibrated “denominator” estimates and task‑specific heuristics. Empirical evaluations on web‑scraping, API‑query, and mathematical‑reasoning tasks show that (1) knowledge entries grow from 0 to 54 over six runs, stabilizing completeness estimates, and (2) seeding a weaker model (Sonnet) with a stronger model’s (Opus) knowledge reduces coverage error from 6.6 pp to 1.1 pp, cuts cost by ≈ 45 % and halves the number of planning rounds, while yielding identical denominator estimates across independent runs—demonstrating reliable, model‑agnostic knowledge transfer for agentic AI.


<details>
<summary>Abstract</summary>

Autonomous agents operating in open-world tasks -- where the completion boundary is not given in advance -- face denominator blindness: they systematically underestimate the scope of the target space. Forage V1 addressed this through co-evolving evaluation (an independent Evaluator discovers what "complete" means) and method isolation (Evaluator and Planner cannot see each other's code). V2 extends the architecture from a single expedition to a learning organization: experience accumulates across runs, transfers across model capabilities, and institutional safeguards prevent knowledge degradation.
  We demonstrate two claims across three task types (web scraping, API queries, mathematical reasoning). Knowledge accumulation: over six runs, knowledge entries grow from 0 to 54, and denominator estimates stabilize as domain understanding deepens. Knowledge transfer: a weaker agent (Sonnet) seeded with a stronger agent's (Opus) knowledge narrows a 6.6pp coverage gap to 1.1pp, halves cost (9.40 to 5.13 USD), converges in half the rounds (mean 4.5 vs. 7.0), and three independent seeded runs arrive at exactly the same denominator estimate (266), suggesting organizational knowledge calibrates evaluation itself.
  V2's contribution is architectural: it designs institutions -- audit separation, contract protocols, organizational memory -- that make any agent more reliable upon entry. The accumulated experience is organizational, model-agnostic, and transferable, stored as readable documents that any future agent inherits regardless of provider or capability level.

</details>


### 95. Refute-or-Promote: An Adversarial Stage-Gated Multi-Agent Review Methodology for High-Precision LLM-Assisted Defect Discovery

- **Authors:** Abhinav Agarwal
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19049v1](http://arxiv.org/abs/2604.19049v1)
- **PDF:** [https://arxiv.org/pdf/2604.19049v1](https://arxiv.org/pdf/2604.19049v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> **Contribution:** The paper introduces **Refute‑or‑Promote**, a staged, adversarial review framework that couples a stratified context‑hunting generator with multiple “kill” agents—including cross‑model critics—to dramatically prune false‑positive defect reports produced by large language models.  

**Methodology:** Candidates are first generated by a context‑aware LLM (Stratified Context Hunting), then passed through successive promotion gates where adversarial agents from different model families attempt to refute them; a final empirical test gate ensures that any surviving claim is experimentally validated.  

**Findings:** Across a 31‑day, seven‑target campaign the system eliminated ~79 % of 171 LLM‑generated defect candidates before disclosure, yielding 4 CVEs, numerous accepted C++ working‑group changes, compiler bug fixes, and other security patches, and demonstrating that external, cross‑family adversarial filtering—not model scaling—can restore high precision in LLM‑assisted defect discovery.


<details>
<summary>Abstract</summary>

LLM-assisted defect discovery has a precision crisis: plausible-but-wrong reports overwhelm maintainers and degrade credibility for real findings. We present Refute-or-Promote, an inference-time reliability pattern combining Stratified Context Hunting (SCH) for candidate generation, adversarial kill mandates, context asymmetry, and a Cross-Model Critic (CMC). Adversarial agents attempt to disprove candidates at each promotion gate; cold-start reviewers are intended to reduce anchoring cascades; cross-family review can catch correlated blind spots that same-family review misses. Over a 31-day campaign across 7 targets (security libraries, the ISO C++ standard, major compilers), the pipeline killed roughly 79% of 171 candidates before advancing to disclosure (retrospective aggregate); on a consolidated-protocol subset (lcms2, wolfSSL; n=30), the prospective kill rate was 83%. Outcomes: 4 CVEs (3 public, 1 embargoed); LWG 4549 accepted to the C++ working paper; 5 merged C++ editorial PRs; 3 compiler conformance bugs; 8 merged security-related fixes without CVE; an RFC 9000 errata filed under committee review; and 1+ FIPS 140-3 normative compliance issues under coordinated disclosure -- all evaluated by external acceptance, not benchmarks. The most instructive failure: ten dedicated reviewers unanimously endorsed a non-existent Bleichenbacher padding oracle in OpenSSL's CMS module; it was killed only by a single empirical test, motivating the mandatory empirical gate. No vulnerability was discovered autonomously; the contribution is external structure that filters LLM agents' persistent false positives. As a preliminary transfer test beyond defect discovery, a simplified cross-family critique variant also solved five previously unsolved SymPy instances on SWE-bench Verified and one SWE-rebench hard task.

</details>


### 96. ClawCoin: An Agentic AI-Native Cryptocurrency for Decentralized Agent Economies

- **Authors:** Shaoyu Li, Chaoyu Zhang, Hexuan Yu, Y. Thomas Hou, Wenjing Lou
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19026v1](http://arxiv.org/abs/2604.19026v1)
- **PDF:** [https://arxiv.org/pdf/2604.19026v1](https://arxiv.org/pdf/2604.19026v1)
- **Categories:** cs.MA, cs.CR


> The paper introduces **ClawCoin**, a native cryptocurrency that directly indexes the compute tokens (API inference credits) consumed by autonomous AI agents, turning the otherwise non‑transferable cost of compute into a tradable unit of account and settlement asset for decentralized agent economies. The authors design a four‑layer architecture—(1) a basket index that aggregates standardized compute‑price feeds, (2) an oracle that issues signed, fresh price attestations, (3) a net‑asset‑value (NAV)‑backed mint‑and‑redeem vault with coverage thresholds and rate limits, and (4) an on‑chain settlement layer supporting multi‑hop delegations—and implement it on an Ethereum‑compatible L2. Experiments using a multi‑agent simulator and the OpenClaw testbed show that ClawCoin stabilizes agents’ execution capacity during cost spikes, narrows quoting variance across agents, removes partial settlements, and enables cooperative market dynamics that fiat‑based payment schemes cannot achieve, demonstrating the practical benefits of compute‑indexed tokens for agentic AI coordination.


<details>
<summary>Abstract</summary>

Autonomous AI agents live or die by the API tokens they consume: without paid inference capacity they cannot reason, act, or delegate. Compute-token cost has become the binding resource of the emerging agent economy, yet it is non-transferable: it is account-bound, vendor-specific, and absent from on-chain ledgers. Existing payment rails such as x402 move fiat-backed value between agents, but they do not represent the quantity agents actually burn. As a result, agents can transport purchasing power but cannot quote, escrow, or settle workflows in a unit aligned with compute cost.
  We present ClawCoin, a tokenized, compute-cost-indexed unit of account and settlement asset for decentralized agent economies. ClawCoin combines four layers: a robust basket index over standardized prices; an oracle publishing signed fresh attestations; a NAV-based mint/redeem vault with coverage thresholds and rate limits; and an on-chain settlement layer for multi-hop delegations.
  We implement a prototype on an Ethereum-compatible L2 and evaluate it using a multi-agent simulator and the OpenClaw testbed. Across single-agent, multi-agent, workflow, and procurement experiments, ClawCoin stabilizes execution capacity under cost shocks, reduces cross-agent quote dispersion, eliminates partial settlements, and sustains cooperative market dynamics that fiat-denominated baselines cannot. These results suggest that compute-indexed units of account can improve decentralized agent coordination.

</details>


### 97. Debating the Unspoken: Role-Anchored Multi-Agent Reasoning for Half-Truth Detection

- **Authors:** Yixuan Tang, Yirui Zhang, Hang Feng, Anthony K. H. Tung
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19005v1](http://arxiv.org/abs/2604.19005v1)
- **PDF:** [https://arxiv.org/pdf/2604.19005v1](https://arxiv.org/pdf/2604.19005v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **RADAR**, a role‑anchored multi‑agent debate framework that detects half‑truths by explicitly reasoning about omitted information, something traditional fact‑checking systems overlook.

**Methodology:** RADAR deploys three LLM‑based agents with fixed personas—a *Politician* (bias‑inclined), a *Scientist* (evidence‑focused), and a neutral *Judge*—that iteratively debate over a shared, noisy retrieval set. A dual‑threshold early‑termination controller monitors the debate’s progress and stops when the agents have gathered enough evidence to issue a verdict, thereby cutting unnecessary computation.

**Key findings:** Across several half‑truth detection benchmarks and backbone models, RADAR consistently beats strong single‑agent and prior multi‑agent baselines, achieving higher omission‑detection accuracy while using fewer reasoning steps. This demonstrates that persona‑driven, retrieval‑grounded debate with adaptive control is an effective and scalable approach for agentic AI systems tasked with uncovering missing context in fact verification.


<details>
<summary>Abstract</summary>

Half-truths, claims that are factually correct yet misleading due to omitted context, remain a blind spot for fact verification systems focused on explicit falsehoods. Addressing such omission-based manipulation requires reasoning not only about what is said, but also about what is left unsaid. We propose RADAR, a role-anchored multi-agent debate framework for omission-aware fact verification under realistic, noisy retrieval. RADAR assigns complementary roles to a Politician and a Scientist, who reason adversarially over shared retrieved evidence, moderated by a neutral Judge. A dual-threshold early termination controller adaptively decides when sufficient reasoning has been reached to issue a verdict. Experiments show that RADAR consistently outperforms strong single- and multi-agent baselines across datasets and backbones, improving omission detection accuracy while reducing reasoning cost. These results demonstrate that role-anchored, retrieval-grounded debate with adaptive control is an effective and scalable framework for uncovering missing context in fact verification. The code is available at https://github.com/tangyixuan/RADAR.

</details>


### 98. STAR-Teaming: A Strategy-Response Multiplex Network Approach to Automated LLM Red Teaming

- **Authors:** MinJae Jung, YongTaek Lim, Chaeyun Kim, Junghwan Kim, Kihyun Kim, Minwoo Kim
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18976v1](http://arxiv.org/abs/2604.18976v1)
- **PDF:** [https://arxiv.org/pdf/2604.18976v1](https://arxiv.org/pdf/2604.18976v1)
- **Categories:** cs.CL


> The paper presents **STAR‑Teaming**, a black‑box automated red‑teaming framework that casts jailbreak prompt generation for large language models as a **Strategy‑Response Multiplex Network** problem solved by a multi‑agent system; the network encodes attack strategies and their semantic relationships, allowing a network‑driven optimizer to efficiently sample diverse, high‑impact prompts. By reorganizing the otherwise intractable embedding space into interpretable semantic communities, STAR‑Teaming both clarifies a model’s strategic vulnerabilities and reduces redundant exploration, leading to a substantially higher attack‑success rate while using far less compute than prior approaches. Empirical evaluations on several mainstream LLMs confirm these gains and demonstrate the method’s explainability and scalability.


<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) are widely used, they remain susceptible to jailbreak prompts that can elicit harmful or inappropriate responses. This paper introduces STAR-Teaming, a novel black-box framework for automated red teaming that effectively generates such prompts. STAR-Teaming integrates a Multi-Agent System (MAS) with a Strategy-Response Multiplex Network and employs network-driven optimization to sample effective attack strategies. This network-based approach recasts the intractable high-dimensional embedding space into a tractable structure, yielding two key advantages: it enhances the interpretability of the LLM's strategic vulnerabilities, and it streamlines the search for effective strategies by organizing the search space into semantic communities, thereby preventing redundant exploration. Empirical results demonstrate that STAR-Teaming significantly surpasses existing methods, achieving a higher attack success rate (ASR) at a lower computational cost. Extensive experiments validate the effectiveness and explainability of the Multiplex Network. The code is available at https://github.com/selectstar-ai/STAR-Teaming-paper.

</details>


### 99. Gated Coordination for Efficient Multi-Agent Collaboration in Minecraft Game

- **Authors:** HuaDong Jian, Chenghao Li, Haoyu Wang, Jiajia Shuai, Jinyu Guo, Yang Yang, Chaoning Zhang
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18975v1](http://arxiv.org/abs/2604.18975v1)
- **PDF:** [https://arxiv.org/pdf/2604.18975v1](https://arxiv.org/pdf/2604.18975v1)
- **Categories:** cs.MA


> The paper introduces a **partitioned information architecture** for multi‑large‑language‑model (MLLM) agents that cleanly separates private execution state from shared coordination state, and equips it with two novel mechanisms: (1) an **event‑triggered working memory** that updates only on system‑verified outcomes, keeping local representations compact and low‑noise, and (2) a **cost‑sensitive gated escalation** that decides whether to broadcast information by jointly evaluating node criticality, local recovery cost, and downstream task impact. Using long‑horizon construction tasks in Minecraft, the authors show that this gated, selective communication strategy yields higher blueprint‑completion quality, shorter execution chains, better self‑recovery, and fewer ineffective escalations than strong‑communication baselines, demonstrating a more efficient form of agentic collaboration.


<details>
<summary>Abstract</summary>

In long-horizon open-world multi-agent systems, existing methods often treat local anomalies as automatic triggers for communication. This default design introduces coordination noise, interrupts local execution, and overuses public interaction in cases that could be resolved locally. To address this issue, we propose a partitioned information architecture for MLLM agents that explicitly separates private execution states from public coordination states. Building on this design, we introduce two key mechanisms. First, we develop an event-triggered working memory based on system-verified outcomes to maintain compact and low-noise local state representations. Second, we propose a cost-sensitive gated escalation mechanism that determines whether cross-region communication should be initiated by jointly considering node criticality, local recovery cost, and downstream task impact. In this way, communication is transformed from a default reaction into a selective decision. Experiments conducted on long-term construction tasks in open environments demonstrate that, compared to baseline models based on strong communication and planned structures, the introduction of gated communication and a partitioned information architecture results in superior performance in terms of blueprint completion quality and execution chain length. It also improves local self-recovery, reduces ineffective escalations, and increases the utility of public communication.

</details>


### 100. Superficial Success vs. Internal Breakdown: An Empirical Study of Generalization in Adaptive Multi-Agent Systems

- **Authors:** Namyoung So, Seokgyu Jang, Taeuk Kim
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18951v2](http://arxiv.org/abs/2604.18951v2)
- **PDF:** [https://arxiv.org/pdf/2604.18951v2](https://arxiv.org/pdf/2604.18951v2)
- **Categories:** cs.MA, cs.CL


> The paper shows that current adaptive multi‑agent systems (MAS) excel at producing correct final outputs on the training domain yet fail to generalize to new tasks and to maintain principled inter‑agent coordination. By systematically evaluating a suite of state‑of‑the‑art MAS across multiple environments, the authors uncover “topological overfitting” (performance collapses when the interaction graph or task structure changes) and “illusory coordination” (high surface‑level accuracy despite agents deviating from the intended coordination dynamics). These results call for new benchmarking protocols that probe both cross‑domain generalization and the fidelity of emergent coordination, suggesting that future agentic AI research must embed robustness and internal consistency into the design and evaluation of adaptive MAS.


<details>
<summary>Abstract</summary>

Adaptive multi-agent systems (MAS) are increasingly adopted to tackle complex problems. However, the narrow task coverage of their optimization raises the question of whether they can function as general-purpose systems. To address this gap, we conduct an extensive empirical study of adaptive MAS, revealing two key findings: (1) topological overfitting -- they fail to generalize across different domains; and (2) illusory coordination -- they achieve reasonable surface-level accuracy while the underlying agent interactions diverge from ideal MAS behavior, raising concerns about their practical utility. These findings highlight the pressing need to prioritize generalization in MAS development and motivate evaluation protocols that extend beyond simple final-answer correctness.

</details>


### 101. AutomationBench

- **Authors:** Daniel Shepard, Robin Salimans
- **Published:** 2026-04-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18934v1](http://arxiv.org/abs/2604.18934v1)
- **PDF:** [https://arxiv.org/pdf/2604.18934v1](https://arxiv.org/pdf/2604.18934v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **AutomationBench**, a new, programmatically graded benchmark that evaluates AI agents on realistic, cross‑application workflow orchestration—requiring autonomous REST‑API discovery, multi‑step coordination across disparate SaaS tools, and strict adherence to layered business policies.  

**Methodology:** Building on real Zapier workflow patterns across six business domains (Sales, Marketing, Operations, Support, Finance, HR), the authors generate tasks in which an agent must (1) identify the correct API endpoints among many noisy or misleading resources, (2) apply hierarchical policy rules, and (3) execute a sequence of API calls that leave the desired end‑state data in each target system. Scoring is binary: success only if the final data placement matches the specification.  

**Key findings:** Current state‑of‑the‑art “frontier” language models achieve **under 10 %** success on AutomationBench, revealing a substantial gap between existing agentic AI capabilities and the coordination, discovery, and compliance demands of real‑world business automation. The benchmark thus provides a rigorous, industry‑relevant yardstick for future research on truly autonomous, policy‑aware AI agents.


<details>
<summary>Abstract</summary>

Existing AI benchmarks for software automation rarely combine cross-application coordination, autonomous API discovery, and policy adherence. Real business workflows demand all three: a single task may span a CRM, inbox, calendar, and messaging platform - requiring the agent to find the right endpoints, follow a policy document, and write correct data to each system. To address this gap, we introduce AutomationBench, a benchmark for evaluating AI agents on cross-application workflow orchestration via REST APIs. Drawing on real workflow patterns from Zapier's platform, tasks span Sales, Marketing, Operations, Support, Finance, and HR domains. Agents must discover relevant endpoints themselves, follow layered business rules, and navigate environments with irrelevant and sometimes misleading records. Grading is programmatic and end-state only: whether the correct data ended up in the right systems. Even the best frontier models currently score below 10%. AutomationBench provides a challenging, realistic measure of where current models stand relative to the agentic capabilities businesses actually need.

</details>


### 102. How Adversarial Environments Mislead Agentic AI?

- **Authors:** Zhonghao Zhan, Huichi Zhou, Zhenhao Li, Peiyuan Jing, Krinos Li, Hamed Haddadi
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18874v1](http://arxiv.org/abs/2604.18874v1)
- **PDF:** [https://arxiv.org/pdf/2604.18874v1](https://arxiv.org/pdf/2604.18874v1)
- **Categories:** cs.AI


> The paper introduces the **Trust Gap** in tool‑integrated, agentic AI systems: while current benchmarks only test whether an agent can *use* external tools, they ignore whether the agent can *detect* when those tools are maliciously corrupted. To expose this vulnerability the authors formalize **Adversarial Environmental Injection (AEI)**—a threat model in which an adversary poisons tool outputs (e.g., search results or reference networks) to create a “fake world”—and implement **POTEMKIN**, a Model Context Protocol‑compatible harness that injects two orthogonal attacks: **The Illusion** (breadth‑wise poisoning that drives epistemic drift toward false beliefs) and **The Maze** (depth‑wise structural traps that force agents into infinite loops). Experiments on more than 11 k rollouts across five state‑of‑the‑art agents reveal a pronounced robustness gap: agents that are resilient to one attack class become more vulnerable to the other, showing that epistemic robustness and navigational robustness are distinct, under‑studied capabilities essential for trustworthy agentic AI.


<details>
<summary>Abstract</summary>

Tool-integrated agents are deployed on the premise that external tools ground their outputs in reality. Yet this very reliance creates a critical attack surface. Current evaluations benchmark capability in benign settings, asking "can the agent use tools correctly" but never "what if the tools lie". We identify this Trust Gap: agents are evaluated for performance, not for skepticism. We formalize this vulnerability as Adversarial Environmental Injection (AEI), a threat model where adversaries compromise tool outputs to deceive agents. AEI constitutes environmental deception: constructing a "fake world" of poisoned search results and fabricated reference networks around unsuspecting agents. We operationalize this via POTEMKIN, a Model Context Protocol (MCP)-compatible harness for plug-and-play robustness testing. We identify two orthogonal attack surfaces: The Illusion (breadth attacks) poison retrieval to induce epistemic drift toward false beliefs, while The Maze (depth attacks) exploit structural traps to cause policy collapse into infinite loops. Across 11,000+ runs on five frontier agents, we find a stark robustness gap: resistance to one attack often increases vulnerability to the other, demonstrating that epistemic and navigational robustness are distinct capabilities.

</details>


### 103. Mango: Multi-Agent Web Navigation via Global-View Optimization

- **Authors:** Weixi Tong, Yifeng Di, Tianyi Zhang
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18779v1](http://arxiv.org/abs/2604.18779v1)
- **PDF:** [https://arxiv.org/pdf/2604.18779v1](https://arxiv.org/pdf/2604.18779v1)
- **Categories:** cs.CL, cs.AI


> Mango introduces a multi‑agent web‑navigation framework that first infers a global view of a site’s hierarchical structure and then selects high‑utility entry URLs via a Thompson‑sampling bandit formulation, while an episodic memory module records past navigation attempts to guide future exploration. By allocating the limited interaction budget adaptively across candidate start points, Mango achieves substantially higher task success—63.6 % on WebVoyager (7.3 % above the strongest baseline) and 52.5 % on WebWalkerQA (26.8 % above baseline)—and demonstrates consistent gains across both open‑source and closed‑source language models. These results highlight the advantage of global‑structure awareness and multi‑agent budget optimization for agentic AI systems tasked with complex web navigation.


<details>
<summary>Abstract</summary>

Existing web agents typically initiate exploration from the root URL, which is inefficient for complex websites with deep hierarchical structures. Without a global view of the website's structure, agents frequently fall into navigation traps, explore irrelevant branches, or fail to reach target information within a limited budget. We propose Mango, a multi-agent web navigation method that leverages the website structure to dynamically determine optimal starting points. We formulate URL selection as a multi-armed bandit problem and employ Thompson Sampling to adaptively allocate the navigation budget across candidate URLs. Furthermore, we introduce an episodic memory component to store navigation history, enabling the agent to learn from previous attempts. Experiments on WebVoyager demonstrate that Mango achieves a success rate of 63.6% when using GPT-5-mini, outperforming the best baseline by 7.3%. Furthermore, on WebWalkerQA, Mango attains a 52.5% success rate, surpassing the best baseline by 26.8%. We also demonstrate the generalizability of Mango using both open-source and closed-source models as backbones. Our data and code are open-source and available at https://github.com/VichyTong/Mango.

</details>


### 104. Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs

- **Authors:** Kevin Murphy
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18576v2](http://arxiv.org/abs/2604.18576v2)
- **PDF:** [https://arxiv.org/pdf/2604.18576v2](https://arxiv.org/pdf/2604.18576v2)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **BLF (Bayesian Linguistic Forecaster)**, an agentic forecasting system that integrates probabilistic reasoning with natural‑language evidence via a structured “linguistic belief state,” and leverages hierarchical Bayesian techniques for trial aggregation and calibration to achieve state‑of‑the‑art binary predictions on ForecastBench.

**Methodology:** BLF iteratively updates a semi‑structured belief state (numeric probability + LLM‑generated evidence summary) in a tool‑use loop, runs multiple independent prediction trials, and combines them with logit‑space shrinkage using a data‑driven prior; predictions are finally calibrated through hierarchical Platt scaling that respects source‑specific base‑rate skew.

**Key findings:** On 400 back‑tested ForecastBench questions, BLF surpasses all leading public forecasters (including Cassi, GPT‑5, Grok 4.20, and Foresight‑32B). Ablations show the belief‑state representation contributes nearly as much performance gain as web search, while both hierarchical aggregation and calibration provide statistically significant additional improvements, all validated under a rigorously controlled leakage‑limited back‑testing framework.


<details>
<summary>Abstract</summary>

We present BLF (Bayesian Linguistic Forecaster), an agentic system for binary forecasting that achieves state-of-the-art performance on the ForecastBench benchmark. The system is built on three ideas. (1) A linguistic belief state: a semi-structured representation combining numerical probability estimates with natural-language evidence summaries, updated by the LLM at each step of an iterative tool-use loop. This contrasts with the common approach of appending all retrieved evidence to an ever-growing context. (2) Hierarchical multi-trial aggregation: running $K$ independent trials and combining them using logit-space shrinkage with a data-dependent prior. (3) Hierarchical calibration: Platt scaling with a hierarchical prior, which avoids over-shrinking extreme predictions for sources with skewed base rates. On 400 backtesting questions from the ForecastBench leaderboard, BLF outperforms all the top public methods, including Cassi, GPT-5, Grok~4.20, and Foresight-32B. Ablation studies show that the structured belief state is almost as impactful as web search access, and that shrinkage aggregation and hierarchical calibration each provide significant additional gains. In addition, we develop a robust back-testing framework with a leakage rate below 1.5\%, and use rigorous statistical methodology to compare different methods while controlling for various sources of noise.

</details>


### 105. MASS-RAG: Multi-Agent Synthesis Retrieval-Augmented Generation

- **Authors:** Xingchen Xiao, Heyan Huang, Runheng Liu, Jincheng Xie
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18509v2](http://arxiv.org/abs/2604.18509v2)
- **PDF:** [https://arxiv.org/pdf/2604.18509v2](https://arxiv.org/pdf/2604.18509v2)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **MASS‑RAG**, a multi‑agent framework for retrieval‑augmented generation that decomposes evidence handling into separate, role‑specialized LLM agents (summarizer, extractor, reasoner) and then fuses their outputs in a synthesis stage, thereby improving the model’s ability to reconcile noisy, incomplete, or heterogeneous retrieved documents.

**Methodology:** MASS‑RAG orchestrates three dedicated agents that (1) generate concise summaries of each retrieved passage, (2) extract salient facts or claims, and (3) perform chain‑of‑thought reasoning over the aggregated evidence; a final synthesis agent integrates these intermediate views to produce the answer. Experiments were run on four standard RAG benchmarks, comparing against strong single‑agent RAG baselines.

**Key findings:** Across all datasets, MASS‑RAG yields statistically significant gains (often 3–7 % absolute improvement in exact‑match/EM or F1) and is especially effective when relevant information is scattered across multiple retrieved texts, demonstrating that multi‑agent evidence synthesis can substantially boost the reliability of agentic AI systems in knowledge‑intensive tasks.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are widely used in retrieval-augmented generation (RAG) to incorporate external knowledge at inference time. However, when retrieved contexts are noisy, incomplete, or heterogeneous, a single generation process often struggles to reconcile evidence effectively. We propose \textbf{MASS-RAG}, a multi-agent synthesis approach to retrieval-augmented generation that structures evidence processing into multiple role-specialized agents. MASS-RAG applies distinct agents for evidence summarization, evidence extraction, and reasoning over retrieved documents, and combines their outputs through a dedicated synthesis stage to produce the final answer. This design exposes multiple intermediate evidence views, allowing the model to compare and integrate complementary information before answer generation. Experiments on four benchmarks show that MASS-RAG consistently improves performance over strong RAG baselines, particularly in settings where relevant evidence is distributed across retrieved contexts.

</details>


### 106. QRAFTI: An Agentic Framework for Empirical Research in Quantitative Finance

- **Authors:** Terence Lim, Kumar Muthuraman, Michael Sury
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18500v1](http://arxiv.org/abs/2604.18500v1)
- **PDF:** [https://arxiv.org/pdf/2604.18500v1](https://arxiv.org/pdf/2604.18500v1)
- **Categories:** cs.MA, q-fin.GN


> **Main contribution:** QRAFTI presents a modular, multi‑agent architecture that emulates the workflow of a quantitative research team, exposing data access, factor construction, and custom coding as callable services to automate equity‑factor research on large panel datasets.  

**Methodology:** The framework couples a specialized panel‑data toolkit with MCP (Multi‑Component Planner) servers that orchestrate chained tool calls and reflection‑based planning, allowing agents to iteratively build, test, and document factors while preserving computational traceability.  

**Key findings:** Experiments show that this planner‑driven, tool‑chaining approach yields more accurate factor replication and faster discovery of novel signals than relying solely on dynamic code generation, and it produces standardized research reports with narrative explanations that enhance transparency and explainability for agentic AI applications in finance.


<details>
<summary>Abstract</summary>

We introduce a multi-agent framework intended to emulate parts of a quantitative research team and support equity factor research on large financial panel datasets. QRAFTI integrates a research toolkit for panel data with MCP servers that expose data access, factor construction, and custom coding operations as callable tools. It can help replicate established factors, formulate and test new signals, and generate standardized research reports accompanied by narrative analysis and computational traces. On multi-step empirical tasks, using chained tool calls and reflection-based planning may offer better performance and explainability than dynamic code generation alone.

</details>


### 107. StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement Learning

- **Authors:** Daoyu Wang, Qingchuan Li, Mingyue Cheng, Jie Ouyang, Shuo Yu, Qi Liu, Enhong Chen
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18401v1](http://arxiv.org/abs/2604.18401v1)
- **PDF:** [https://arxiv.org/pdf/2604.18401v1](https://arxiv.org/pdf/2604.18401v1)
- **Categories:** cs.CL


> **Main contribution** – The paper introduces **StepPO**, a step‑level reinforcement‑learning framework that redefines the action space for LLM‑based agents from individual tokens to whole “steps” (i.e., coherent agent decisions such as a planning utterance, tool invocation, or multi‑turn sub‑dialogue). This reframing yields a step‑level Markov Decision Process and a corresponding step‑level credit‑assignment objective that aligns policy updates with the true granularity of agentic behavior.

**Methodology** – The authors formalize the step‑level MDP, derive a step‑aligned policy‑gradient estimator, and design system components (step detection, reward shaping, trajectory buffering) that enable efficient training of LLM agents under this formulation. Experiments compare token‑level baselines (RLHF, RLVR) with StepPO on benchmark multi‑turn tasks that require decision making and tool use.

**Key findings** – Preliminary results show that StepPO achieves higher success rates and more stable learning on delayed‑reward, multi‑turn tasks, confirming that step‑level credit assignment better captures the causal impact of agent decisions than token‑level methods. The work suggests that moving to a step‑aligned RL paradigm is a promising direction for building more capable, general‑purpose LLM agents.


<details>
<summary>Abstract</summary>

General agents have given rise to phenomenal applications such as OpenClaw and Claude Code. As these agent systems (a.k.a. Harnesses) strive for bolder goals, they demand increasingly stronger agentic capabilities from foundation Large Language Models (LLMs). Agentic Reinforcement Learning (RL) is emerging as a central post-training paradigm for empowering LLMs with these capabilities and is playing an increasingly pivotal role in agent training. Unlike single-turn token-level alignment or reasoning enhancement, as in RLHF and RLVR, Agentic RL targets multi-turn interactive settings, where the goal is to optimize core agentic capabilities such as decision making and tool use while addressing new challenges including delayed and sparse rewards, as well as long and variable context. As a result, the token-centric modeling and optimization paradigm inherited from traditional LLM RL is becoming increasingly inadequate for capturing real LLM agent behavior. In this paper, we present StepPO as a position on step-level Agentic RL. We argue that the conventional token-level Markov Decision Process (MDP) should be advanced to a step-level MDP formulation, and that the step, rather than the token, should be regarded as the proper action representation for LLM agents. We then propose step-level credit assignment as the natural optimization counterpart of this formulation, thereby aligning policy optimization and reward propagation with the granularity of agent decisions. Finally, we discuss the key systems designs required to realize step-level Agentic RL in practice and preliminary experiments provide initial evidence for the effectiveness of this perspective. We hope that the step-aligned, step-level paradigm embodied in StepPO offers the Agentic RL community a useful lens for understanding agent behavior and helps advance LLMs toward stronger general-agent capabilities.

</details>


### 108. More Is Different: Toward a Theory of Emergence in AI-Native Software Ecosystems

- **Authors:** Daniel Russo
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.19827v1](http://arxiv.org/abs/2604.19827v1)
- **PDF:** [https://arxiv.org/pdf/2604.19827v1](https://arxiv.org/pdf/2604.19827v1)
- **Categories:** cs.SE, cs.AI


> **Main contribution:** The paper proposes a new theoretical framework that treats AI‑native software ecosystems as Complex Adaptive Systems (CAS), arguing that the failures of multi‑agent AI systems stem from emergent, system‑level dynamics rather than from individual agents.  

**Methodology:** Building on Holland’s six CAS properties, the authors map these to observable software‑ecosystem phenomena (e.g., architectural entropy, cascade failures, comprehension debt) and introduce a formal measurement approach that defines micro‑level state variables, coarse‑graining functions, and causal‑emergence metrics. They formulate seven falsifiable propositions linking CAS theory to software evolution, and compare the predictions to Lehman’s laws of software change.  

**Key findings for agentic AI:** The analysis predicts that ecosystem‑level metrics—such as emergent entropy and cascade‑failure rates—will systematically diverge from predictions based on agent‑level correctness, indicating that traditional software‑engineering laws are insufficient for AI‑native systems. Empirical validation (or refutation) of the propositions would compel a shift toward continuous, ecosystem‑wide monitoring and governance as the primary means of ensuring reliability in autonomous‑agent deployments.


<details>
<summary>Abstract</summary>

Software engineering faces a fundamental challenge: multi-agent AI systems fail in ways that defy explanation by traditional theories. While individual agents perform correctly, their interactions degrade entire ecosystems, revealing a gap in our understanding of software evolution. This paper argues that AI-native software ecosystems must be studied as complex adaptive systems (CAS), where emergent properties like architectural entropy, cascade failures, and comprehension debt arise not from individual components, but from their interactions. We map Holland's six CAS properties onto observable ecosystem dynamics, distinguishing these systems from microservices or open-source networks. To measure causal emergence, we define micro-level state variables, coarse-graining functions, and a tractable measurement framework. Seven falsifiable propositions link CAS theory to software evolution, challenging or extending Lehman's laws where agent-level assumptions fail. If confirmed, these findings would demand a radical shift: ecosystem-level monitoring as the primary governance mechanism for AI-native systems. If refuted, existing theories may only need incremental updates. Either way, this work forces us to ask: Can software engineering's core assumptions survive the age of autonomous agents?

</details>


### 109. Dissecting AI Trading: Behavioral Finance and Market Bubbles

- **Authors:** Shumiao Ouyang, Pengfei Sui
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18373v1](http://arxiv.org/abs/2604.18373v1)
- **PDF:** [https://arxiv.org/pdf/2604.18373v1](https://arxiv.org/pdf/2604.18373v1)
- **Categories:** econ.GN, cs.AI, q-fin.GN


> The paper shows that autonomous Large‑Language‑Model (LLM) traders in a simulated open‑call auction reproduce well‑known behavioral finance phenomena—most notably a strong disposition effect and recency‑weighted extrapolation—and that these micro‑level biases aggregate into macro‑level market dynamics identical to classic experimental results (e.g., excess‑demand predicting future prices and disagreement driving volume). By prompting the LLM agents with carefully crafted textual cues, the authors can selectively activate or dampen twenty identified decision‑making mechanisms, thereby causally inflating or shrinking speculative bubbles. This work demonstrates both that LLM‑based agents are viable test‑beds for studying agentic behavior in financial markets and that prompt‑level interventions can be used as a novel tool to steer emergent market outcomes.


<details>
<summary>Abstract</summary>

We study how AI agents form expectations and trade in experimental asset markets. Using a simulated open-call auction populated by autonomous Large Language Model (LLM) agents, we document three main findings. First, AI agents exhibit classic behavioral patterns: a pronounced disposition effect and recency-weighted extrapolative beliefs. Second, these individual-level patterns aggregate into equilibrium dynamics that replicate classic experimental findings (Smith et al., 1988), including the predictive power of excess demand for future prices and the positive relationship between disagreement and trading volume. Third, by analyzing the agents' reasoning text through a twenty-mechanism scoring framework, we show that targeted prompt interventions causally amplify or suppress specific behavioral mechanisms, significantly altering the magnitude of market bubbles.

</details>


### 110. Aether: Network Validation Using Agentic AI and Digital Twin

- **Authors:** Jordan Auge, Sam Betts, Giovanna Carofiglio, Giulio Grassi, Martin Gysi, John Kenneth d'Souza
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18233v1](http://arxiv.org/abs/2604.18233v1)
- **PDF:** [https://arxiv.org/pdf/2604.18233v1](https://arxiv.org/pdf/2604.18233v1)
- **Categories:** cs.MA, cs.AI


> The paper introduces **Aether**, a framework that couples generative, agentic AI with a unified Network Digital Twin to fully automate the end‑to‑end validation of network configuration changes. Its methodology defines five specialized autonomous “Network Operations” agents that collaboratively parse change intents, update the twin’s model, run simulations/emulations, and generate verification and test artifacts, all while keeping a single, continuously synced virtual replica of the live network. Evaluation on synthetic change sets and real‑world incident logs from a large ISP shows that Aether detects 100 % of introduced errors, achieves 92–96 % diagnostic coverage, and completes the validation cycle in 6–7 minutes—dramatically faster and more reliable than existing manual or fragmented tooling approaches.


<details>
<summary>Abstract</summary>

Network change validation remains a critical yet predominantly manual, time-consuming, and error-prone process in modern network operations. While formal network verification has made substantial progress in proving correctness properties, it is typically applied in offline, pre-deployment settings and faces challenges in accommodating continuous changes and validating live production behavior. Current operational approaches typically involve scattered testing tools, resulting in partial coverage and errors that surface only after deployment. In this paper, we present Aether, a novel approach that integrates Generative Agentic AI with a multi-functional Network Digital Twin to automate and streamline network change validation workflows. It features an agentic architecture with five specialized Network Operations AI agents that collaboratively handle the change validation lifecycle from intent analysis to network verification and testing. Aether agents use a unified Network Digital Twin integrating modeling, simulation, and emulation to maintain a consistent, up-to-date network view for verification and testing. By orchestrating agent collaboration atop this digital twin, Aether enables automated, rapid network change validation while reducing manual effort, minimizing errors, and improving operational agility and cost-effectiveness. We evaluate Aether over synthetic network change scenarios covering main classes of network changes and on past incidents from a major ISP operational network, demonstrating promising results in error detection (100%), diagnostic coverage (92-96%), and speed (6-7 minutes) over traditional methods.

</details>


### 111. TacticGen: Grounding Adaptable and Scalable Generation of Football Tactics

- **Authors:** Sheng Xu, Guiliang Liu, Tarak Kharrat, Yudong Luo, Mohamed Aloulou, Javier López Peña, Konstantin Sofeikov, Adam Reid, Paul Roberts, Steven Spencer, Joe Carnall, Ian McHale, Oliver Schulte, Hongyuan Zha, Wei-Shi Zheng
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18210v1](http://arxiv.org/abs/2604.18210v1)
- **PDF:** [https://arxiv.org/pdf/2604.18210v1](https://arxiv.org/pdf/2604.18210v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> TacticGen introduces the first large‑scale generative framework that directly designs football tactics as coordinated multi‑agent movement sequences conditioned on the full game context. The method combines a diffusion‑based transformer with agent‑wise self‑attention and context‑aware cross‑attention, training on >3.3 M events and 100 M tracking frames, and it can be steered at inference time toward arbitrary objectives via classifier‑guided conditioning (rules, natural language, or neural models). Experiments show state‑of‑the‑art trajectory prediction accuracy and, in expert evaluations, produce realistic, strategically sound tactics, demonstrating a scalable, adaptable approach for agentic AI‑driven tactical planning.


<details>
<summary>Abstract</summary>

Success in association football relies on both individual skill and coordinated tactics. While recent advancements in spatio-temporal data and deep learning have enabled predictive analyses like trajectory forecasting, the development of tactical design remains limited. Bridging this gap is essential, as prediction reveals what is likely to occur, whereas tactic generation determines what should occur to achieve strategic objectives. In this work, we present TacticGen, a generative model for adaptable and scalable tactic generation. TacticGen formulates tactics as sequences of multi-agent movements and interactions conditioned on the game context. It employs a multi-agent diffusion transformer with agent-wise self-attention and context-aware cross-attention to capture cooperative and competitive dynamics among players and the ball. Trained with over 3.3 million events and 100 million tracking frames from top-tier leagues, TacticGen achieves state-of-the-art precision in predicting player trajectories. Building on it, TacticGen enables adaptable tactic generation tailored to diverse inference-time objectives through classifier guidance mechanism, specified via rules, natural language, or neural models. Its modeling performance is also inherently scalable. A case study with football experts confirms that TacticGen generates realistic, strategically valuable tactics, demonstrating its practical utility for tactical planning in professional football. The project page is available at: https://shengxu.net/TacticGen/.

</details>


### 112. Scalable Neighborhood-Based Multi-Agent Actor-Critic

- **Authors:** Tim Goppelsroeder, Rasmus Jensen
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18190v1](http://arxiv.org/abs/2604.18190v1)
- **PDF:** [https://arxiv.org/pdf/2604.18190v1](https://arxiv.org/pdf/2604.18190v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **MADDPG‑K**, a scalable variant of Multi‑Agent Deep Deterministic Policy Gradient that replaces the fully centralized critic with a **neighborhood‑based critic** which only receives the observations and actions of each agent’s *k* nearest peers (using Euclidean distance). By fixing the critic’s input dimension regardless of total population size, the method eliminates the costly matrix‑multiplied growth of standard MADDPG while retaining only cheap scalar distance calculations, yielding a quadratic‑time algorithm dominated by neighbor‑search rather than neural‑network overhead. Experiments on cooperative and competitive Multi‑Particle Environment tasks show that MADDPG‑K attains comparable or higher returns than the original algorithm, converges faster in cooperative scenarios, and scales substantially better in runtime as the number of agents increases.


<details>
<summary>Abstract</summary>

We propose MADDPG-K, a scalable extension to Multi-Agent Deep Deterministic Policy Gradient (MADDPG) that addresses the computational limitations of centralized critic approaches. Centralized critics, which condition on the observations and actions of all agents, have demonstrated significant performance gains in cooperative and competitive multi-agent settings. However, their critic networks grow linearly in input size with the number of agents, making them increasingly expensive to train at scale. MADDPG-K mitigates this by restricting each agent's critic to the $k$ closest agents under a chosen metric which in our case is Euclidean distance. This ensures a constant-size critic input regardless of the total agent count. We analyze the complexity of this approach, showing that the quadratic cost it retains arises from cheap scalar distance computations rather than the expensive neural network matrix multiplications that bottleneck standard MADDPG. We validate our method empirically across cooperative and adversarial environments from the Multi-Particle Environment suite, demonstrating competitive or superior performance compared to MADDPG, faster convergence in cooperative settings, and better runtime scaling as the number of agents grows. Our code is available at https://github.com/TimGop/MADDPG-K .

</details>


### 113. Multi-Agent Systems: From Classical Paradigms to Large Foundation Model-Enabled Futures

- **Authors:** Zixiang Wang, Mengjia Gong, Qiyu Sun, Jing Xu, Shuai Mao, Xin Jin, Qing-Long Han, Yang Tang
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18133v1](http://arxiv.org/abs/2604.18133v1)
- **PDF:** [https://arxiv.org/pdf/2604.18133v1](https://arxiv.org/pdf/2604.18133v1)
- **Categories:** cs.AI


> The paper surveys the transition of multi‑agent systems (MAS) from classical designs—where agents coordinate through low‑level perception, message passing, rule‑based decision‑making, and control loops—to new architectures that embed large foundation models (LFMs) as shared semantic engines. By framing both paradigms within a closed‑loop coordination pipeline, the authors compare classical MASs (CMAS) and LFM‑enabled MASs (LMAS) across architecture, operating mechanisms, adaptability, and application domains, showing that LFMs lift inter‑agent interaction from raw state exchanges to high‑level, context‑aware reasoning that improves flexibility and generalisation. The survey highlights open challenges such as scaling LFM inference, ensuring alignment and robustness, and integrating semantic reasoning with real‑time control, outlining a research agenda for building more capable, adaptable agentic AI systems.


<details>
<summary>Abstract</summary>

With the rapid advancement of artificial intelligence, multi-agent systems (MASs) are evolving from classical paradigms toward architectures built upon large foundation models (LFMs). This survey provides a systematic review and comparative analysis of classical MASs (CMASs) and LFM-based MASs (LMASs). First, within a closed-loop coordination framework, CMASs are reviewed across four fundamental dimensions: perception, communication, decision-making, and control. Beyond this framework, LMASs integrate LFMs to lift collaboration from low-level state exchanges to semantic-level reasoning, enabling more flexible coordination and improved adaptability across diverse scenarios. Then, a comparative analysis is conducted to contrast CMASs and LMASs across architecture, operating mechanism, adaptability, and application. Finally, future perspectives on MASs are presented, summarizing open challenges and potential research opportunities.

</details>


### 114. Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration

- **Authors:** Qifan Zhang, Dongyang Ma, Tianqing Fang, Jia Li, Jing Tang, Nuo Chen, Haitao Mi, Yan Wang
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18131v1](http://arxiv.org/abs/2604.18131v1)
- **PDF:** [https://arxiv.org/pdf/2604.18131v1](https://arxiv.org/pdf/2604.18131v1)
- **Categories:** cs.AI


> The paper introduces a “meta‑evolution” framework that trains large language model (LLM) agents to autonomously acquire and distill world knowledge about unseen environments before any downstream task, eliminating the need for external rewards at inference time. By defining an outcome‑based reward that evaluates how much self‑generated knowledge improves downstream success, the authors fine‑tune Qwen‑3‑30B and Seed‑OSS‑36B to explore, summarize, and internalize new information during training; the learned exploration policy is then executed purely from the model’s parameters. Empirically, this intrinsic self‑evolution yields ≈20 % higher scores on the WebVoyager and WebWalker benchmarks, and even a compact 14 B Qwen‑3 model surpasses the unassisted Gemini‑2.5‑Flash, demonstrating that reward‑free, internally driven knowledge acquisition can substantially boost agentic performance.


<details>
<summary>Abstract</summary>

Most agents today ``self-evolve'' by following rewards and rules defined by humans. However, this process remains fundamentally dependent on external supervision; without human guidance, the evolution stops. In this work, we train agents to possess an intrinsic meta-evolution capability to spontaneously learn about unseen environments prior to task execution.
  To instill this ability, we design an outcome-based reward mechanism that measures how much an agent's self-generated world knowledge improves its success rate on downstream tasks. This reward signal is used exclusively during the training phase to teach the model how to explore and summarize effectively. At inference time, the agent requires no external rewards or human instructions. It spontaneously performs native self-evolution to adapt to unknown environments using its internal parameters.
  When applied to Qwen3-30B and Seed-OSS-36B, this shift to native evolution yields a 20% performance increase on WebVoyager and WebWalker. Most strikingly, the generated world knowledge even enables a compact 14B Qwen3 model to outperform the unassisted Gemini-2.5-Flash, establishing a new paradigm for truly evolving agents.

</details>


### 115. Evaluating Answer Leakage Robustness of LLM Tutors against Adversarial Student Attacks

- **Authors:** Jin Zhao, Marta Knežević, Tanja Käser
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18660v1](http://arxiv.org/abs/2604.18660v1)
- **PDF:** [https://arxiv.org/pdf/2604.18660v1](https://arxiv.org/pdf/2604.18660v1)
- **Categories:** cs.CR, cs.AI


> The paper’s main contribution is a systematic evaluation of how vulnerable LLM‑based tutoring agents are to “answer‑leakage” when faced with adversarial students who deliberately try to coax the model into revealing full solutions. The authors first adapt six classes of persuasive/jailbreak techniques to the educational context and test a wide spectrum of tutor models—including vanilla LLMs, pedagogically‑aligned variants, and a multi‑agent tutor design—using both off‑the‑shelf in‑context student prompts and a newly fine‑tuned adversarial student agent that is optimized to jailbreak the tutors; they then propose this fine‑tuned agent as a benchmark for future robustness testing. Experiments show that most standard tutors resist simple attacks, but the specialized adversarial student can consistently induce answer leakage, while lightweight defenses (e.g., answer‑masking prompts and refusal conditioning) substantially curb the leakage, establishing baseline protection strategies for agentic AI tutoring systems.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) are increasingly used in education, yet their default helpfulness often conflicts with pedagogical principles. Prior work evaluates pedagogical quality via answer leakage-the disclosure of complete solutions instead of scaffolding-but typically assumes well-intentioned learners, leaving tutor robustness under student misuse largely unexplored. In this paper, we study scenarios where students behave adversarially and aim to obtain the correct answer from the tutor. We evaluate a broad set of LLM-based tutor models, including different model families, pedagogically aligned models, and a multi-agent design, under a range of adversarial student attacks. We adapt six groups of adversarial and persuasive techniques to the educational setting and use them to probe how likely a tutor is to reveal the final answer. We evaluate answer leakage robustness using different types of in-context adversarial student agents, finding that they often fail to carry out effective attacks. We therefore introduce an adversarial student agent that we fine-tune to jailbreak LLM-based tutors, which we propose as the core of a standardized benchmark for evaluating tutor robustness. Finally, we present simple but effective defense strategies that reduce answer leakage and strengthen the robustness of LLM-based tutors in adversarial scenarios.

</details>


### 116. Architectural Design Decisions in AI Agent Harnesses

- **Authors:** Hu Wei
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18071v1](http://arxiv.org/abs/2604.18071v1)
- **PDF:** [https://arxiv.org/pdf/2604.18071v1](https://arxiv.org/pdf/2604.18071v1)
- **Categories:** cs.AI


> The paper conducts a large‑scale, source‑code‑driven analysis of 70 open‑source AI‑agent systems to map the architectural decisions that underlie the non‑LLM infrastructure (tool mediation, context handling, safety, orchestration). It identifies five recurring design dimensions—sub‑agent architecture, context management, tool system, safety mechanisms, and orchestration—and shows systematic co‑occurrence patterns (e.g., deeper coordination ↔ explicit context services, stronger execution environments ↔ structured governance). From these findings the authors extract five common architectural patterns (lightweight tools, balanced CLI frameworks, multi‑agent orchestrators, enterprise‑grade systems, and scenario‑verticalized projects), providing concrete, evidence‑based guidance for designers and researchers building or selecting agent frameworks.


<details>
<summary>Abstract</summary>

AI agent systems increasingly rely on reusable non-LLM engineering infrastructure that packages tool mediation, context handling, delegation, safety control, and orchestration. Yet the architectural design decisions in this surrounding infrastructure remain understudied. This paper presents a protocol-guided, source-grounded empirical study of 70 publicly available agent-system projects, addressing three questions: which design-decision dimensions recur across projects, which co-occurrences structure those decisions, and which typical architectural patterns emerge. Methodologically, we contribute a transparent investigation procedure for analyzing heterogeneous agent-system corpora through source-code and technical-material reading. Empirically, we identify five recurring design dimensions (subagent architecture, context management, tool systems, safety mechanisms, and orchestration) and find that the corpus favors file-persistent, hybrid, and hierarchical context strategies; registry-oriented tool systems remain dominant while MCP- and plugin-oriented extensions are emerging; and intermediate isolation is common but high-assurance audit is rare. Cross-project co-occurrence analysis reveals that deeper coordination pairs with more explicit context services, stronger execution environments with more structured governance, and formalized tool-registration boundaries with broader ecosystem ambitions. We synthesize five recurring architectural patterns spanning lightweight tools, balanced CLI frameworks, multi-agent orchestrators, enterprise systems, and scenario-verticalized projects. The result provides an evidence-based account of architectural regularities in agent-system engineering, with grounded guidance for framework designers, selectors, and researchers.

</details>


### 117. Owner-Harm: A Missing Threat Model for AI Agent Safety

- **Authors:** Dongcheng Zhang, Yiqing Jiang
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18658v1](http://arxiv.org/abs/2604.18658v1)
- **PDF:** [https://arxiv.org/pdf/2604.18658v1](https://arxiv.org/pdf/2604.18658v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> The paper introduces **Owner‑Harm** as a previously overlooked threat model in AI agent safety, describing eight ways an agent can damage its own deployer (e.g., credential exfiltration, calendar injection, unauthorized data disclosure). By evaluating a state‑of‑the‑art compositional safety system and a generic LLM on both standard criminal‑harm benchmarks (AgentHarm) and newly created Owner‑Harm tasks (AgentDojo injection and a 300‑scenario suite), the authors show that current defenses that achieve perfect true‑positive rates on generic harms collapse to under 15 % true‑positive on owner‑harm cases, with the gap traced to environment‑specific symbolic rules that do not generalize across tool vocabularies. They then propose the **Symbolic‑Semantic Defense Generalization (SSDG)** framework and demonstrate that a layered defense—combining a gate with a deterministic post‑audit verifier—raises detection to 85 % true‑positive (3 % false‑positive), confirming that augmenting symbolic checks with semantic verification can substantially mitigate owner‑harm risks.


<details>
<summary>Abstract</summary>

Existing AI agent safety benchmarks focus on generic criminal harm (cybercrime, harassment, weapon synthesis), leaving a systematic blind spot for a distinct and commercially consequential threat category: agents harming their own deployers. Real-world incidents illustrate the gap: Slack AI credential exfiltration (Aug 2024), Microsoft 365 Copilot calendar-injection leaks (Jan 2024), and a Meta agent unauthorized forum post exposing operational data (Mar 2026). We propose Owner-Harm, a formal threat model with eight categories of agent behavior damaging the deployer. We quantify the defense gap on two benchmarks: a compositional safety system achieves 100% TPR / 0% FPR on AgentHarm (generic criminal harm) yet only 14.8% (4/27; 95% CI: 5.9%-32.5%) on AgentDojo injection tasks (prompt-injection-mediated owner harm). A controlled generic-LLM baseline shows the gap is not inherent to owner-harm (62.7% vs. 59.3%, delta 3.4 pp) but arises from environment-bound symbolic rules that fail to generalize across tool vocabularies. On a post-hoc 300-scenario owner-harm benchmark, the gate alone achieves 75.3% TPR / 3.3% FPR; adding a deterministic post-audit verifier raises overall TPR to 85.3% (+10.0 pp) and Hijacking detection from 43.3% to 93.3%, demonstrating strong layer complementarity. We introduce the Symbolic-Semantic Defense Generalization (SSDG) framework relating information coverage to detection rate. Two SSDG experiments partially validate it: context deprivation amplifies the detection gap 3.4x (R = 3.60 vs. R = 1.06); context injection reveals structured goal-action alignment, not text concatenation, is required for effective owner-harm detection.

</details>


### 118. EvoMarket: A High-Fidelity and Scalable Financial Market Simulator

- **Authors:** Muyao Zhong, Zhenhua Yang, Yuxiang Liu, Ke Tang, Peng Yang
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18046v1](http://arxiv.org/abs/2604.18046v1)
- **PDF:** [https://arxiv.org/pdf/2604.18046v1](https://arxiv.org/pdf/2604.18046v1)
- **Categories:** cs.CE, cs.MA


> EvoMarket is a discrete‑event, multi‑agent market simulator that simultaneously delivers (i) high‑fidelity replication of real‑world microstructure across multiple assets and days, (ii) full institutional mechanisms (calendars, call auctions, price limits, T+1 settlement), and (iii) scalable performance for market‑size order flows. The system couples an optimized limit‑order‑book engine (efficient data structures, hierarchical event scheduling, asynchronous per‑asset matching) with an “oracle‑guided” self‑calibration loop that detects deviations from historic LOB snapshots and injects synthetic corrective orders at checkpoint intervals, eliminating costly offline parameter tuning. Experiments on China A‑share data show that EvoMarket reproduces five‑day LOB dynamics with near‑perfect replay alignment, improves depth‑level fidelity when modest calibration budgets are used, handles increasing order‑rate and asset‑breadth without slowdown, and enables cross‑asset interventions that yield interpretable event‑time response patterns—making it a practical platform for testing and developing agentic trading strategies and market‑design policies.


<details>
<summary>Abstract</summary>

High-fidelity, scalable market simulation is a key instrument for mechanism evaluation, stress testing, and counterfactual policy analysis. Yet existing simulators rarely achieve \emph{mechanism fidelity} beyond single-asset intraday settings, \emph{microstructure fidelity} against historical limit order books (LOB), and \emph{computational tractability} at market scale in a single system. This paper presents \textit{EvoMarket}, a discrete-event, multi-agent financial market simulator designed for intervention-oriented experiments in multi-asset and cross-day environments. EvoMarket couples a high-throughput execution core (optimized LOB data structures, hierarchical scheduling under propagation delays, and asynchronous per-asset matching) with explicit institutional mechanisms (market calendars, opening call auctions, price limits, and T+1 settlement). To avoid expensive black-box calibration, EvoMarket introduces an Oracle-guided in-run self-calibration mechanism that interprets microstructure discrepancy as missing order flow and synthesizes corrective orders at recording checkpoints. Experiments on China A-share order-flow and LOB data show close replay alignment over five trading days, fidelity gains from budgeted in-run calibration across depth levels, broad agent order-space coverage, and scalable performance under increasing input order rates and market breadth. We further demonstrate cross-asset linkage and event-study style intervention evaluation that produces structured dependence and interpretable event-time responses.

</details>


### 119. Diversity Collapse in Multi-Agent LLM Systems: Structural Coupling and Collective Failure in Open-Ended Idea Generation

- **Authors:** Nuo Chen, Yicheng Tong, Yuzhe Yang, Yufei He, Xueyi Zhang, Qingyun Zou, Qian Wang, Bingsheng He
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18005v2](http://arxiv.org/abs/2604.18005v2)
- **PDF:** [https://arxiv.org/pdf/2604.18005v2](https://arxiv.org/pdf/2604.18005v2)
- **Categories:** cs.MA, cs.AI, cs.CL


> **Main contribution:** The paper uncovers a “diversity collapse” phenomenon in multi‑agent LLM systems for open‑ended ideation, showing that interaction structures—not model capability—can contract the collective exploration space and diminish creative diversity.  

**Methodology:** Through a large‑scale empirical sweep across three hierarchical factors—(1) model intelligence (varying size and alignment), (2) agent cognition (authority vs. junior‑driven groups), and (3) system dynamics (group size and communication topology)—the authors measured semantic diversity of generated ideas using embedding‑based dispersion metrics and convergence statistics.  

**Key findings:** 1) Stronger, highly aligned models produce higher‑quality but **lower‑diversity** outputs (the “compute efficiency paradox”). 2) Authority‑centric interaction suppresses semantic spread relative to egalitarian, junior‑driven groups. 3) Scaling group size yields diminishing returns, and dense communication networks accelerate premature convergence. The collapse is traced to structural coupling—over‑connected, hierarchical interactions that force agents into agreement—implying that preserving independence and disagreement is crucial when designing MAS for creative, agentic AI tasks.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) are increasingly used for open-ended idea generation, driven by the expectation that collective interaction will broaden the exploration diversity. However, when and why such collaboration truly expands the solution space remains unclear. We present a systematic empirical study of diversity in MAS-based ideation across three bottom-up levels: model intelligence, agent cognition, and system dynamics. At the model level, we identify a compute efficiency paradox, where stronger, highly aligned models yield diminishing marginal diversity despite higher per-sample quality. At the cognition level, authority-driven dynamics suppress semantic diversity compared to junior-dominated groups. At the system level, group-size scaling yields diminishing returns and dense communication topologies accelerate premature convergence. We characterize these outcomes as collective failures emerging from structural coupling, a process where interaction inadvertently contracts agent exploration and triggers diversity collapse. Our analysis shows that this collapse arises primarily from the interaction structure rather than inherent model insufficiency, highlighting the importance of preserving independence and disagreement when designing MAS for creative tasks. Our code is available at https://github.com/Xtra-Computing/MAS_Diversity.

</details>


### 120. AIT Academy: Cultivating the Complete Agent with a Confucian Three-Domain Curriculum

- **Authors:** Jiaqi Li, Lvyang Zhang, Yang Zhao, Wen Lu, Lidong Zhai
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.17989v1](http://arxiv.org/abs/2604.17989v1)
- **PDF:** [https://arxiv.org/pdf/2604.17989v1](https://arxiv.org/pdf/2604.17989v1)
- **Categories:** cs.AI


> **Main contribution:** The paper proposes **AIT Academy**, a formal curriculum framework for building *complete* AI agents by structuring their development across three knowledge domains—natural science/technical reasoning, humanities/creative expression, and social science/ethical reasoning—using the ancient Confucian Six Arts as behavioral archetypes.  

**Methodology:** The authors map each domain to concrete training “grounds” (ClawdGO Security Dojo, Athen’s Academy, Alt Mirage Stage) and apply them to several backbone LLMs, varying the order of domain exposure (e.g., weakest‑first scheduling) and introducing a principled attribution model for social reasoning.  

**Key findings:** Multi‑domain training yields sizable gains: a 15.9‑point rise in security capability scores and a 7‑percentage‑point boost in social‑reasoning performance, while also revealing a cross‑domain failure mode—**Security Awareness Calibration Pathology (SACP)**—where over‑specialization in Domain I harms out‑of‑distribution behavior, underscoring the diagnostic value of a holistic curriculum for agentic AI.


<details>
<summary>Abstract</summary>

What does it mean to give an AI agent a complete education? Current agent development produces specialists systems optimized for a single capability dimension, whether tool use, code generation, or security awareness that exhibit predictable deficits wherever they were not trained. We argue this pattern reflects a structural absence: there is no curriculum theory for agents, no principled account of what a fully developed agent should know, be, and be able to do across the full scope of intelligent behavior.
  This paper introduces the AIT Academy (Agents Institute of Technology Academy), a curriculum framework for cultivating AI agents across the tripartite structure of human knowledge. Grounded in Kagan's Three Cultures and UNESCO ISCED-F 2013, AIT organizes agent capability development into three domains: Natural Science and Technical Reasoning (Domain I), Humanities and Creative Expression (Domain II), and Social Science and Ethical Reasoning (Domain III). The Confucian Six Arts (liuyi) a 2,500-year-old holistic education system are reinterpreted as behavioral archetypes that map directly onto trainable agent capabilities within each domain.
  Three representative training grounds instantiate the framework across multiple backbone LLMs: the ClawdGO Security Dojo (Domain I), Athen's Academy (Domain II), and the Alt Mirage Stage (Domain III). Experiments demonstrate a 15.9-point improvement in security capability scores under weakest-first curriculum scheduling, and a 7-percentage-point gain in social reasoning performance under principled attribution modeling. A cross-domain finding Security Awareness Calibration Pathology (SACP), in which over-trained Domain I agents fail on out-of-distribution evaluation illustrates the diagnostic value of a multi-domain perspective unavailable to any single-domain framework.

</details>


### 121. CADMAS-CTX: Contextual Capability Calibration for Multi-Agent Delegation

- **Authors:** Chuhan Qiao
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.17950v1](http://arxiv.org/abs/2604.17950v1)
- **PDF:** [https://arxiv.org/pdf/2604.17950v1](https://arxiv.org/pdf/2604.17950v1)
- **Categories:** cs.AI


> **Main contribution:** CADMAS‑CTX introduces a hierarchical, context‑conditioned model of agent capabilities, replacing static skill‑level confidence with per‑agent, per‑skill, per‑context Beta posteriors and a risk‑aware delegation score that penalizes uncertainty.

**Methodology:** The system treats delegation as a contextual bandit problem: for each coarse task context it updates a Bayesian posterior on an agent’s performance, then routes tasks to the peer with the highest mean‑plus‑uncertainty‑adjusted score. The authors prove that, when capability varies across contexts, this routing yields lower cumulative regret than static delegation.

**Key findings:** Across the GAIA and SWE‑bench benchmarks, CADMAS‑CTX raises multi‑agent accuracy from 0.381 → 0.442 (GPT‑4o agents) and resolve rate from 22.3 % → 31.4 %, out‑performing strong baselines (AutoGen) with statistically significant margins. Ablation studies show the uncertainty penalty safeguards against noisy context tags, confirming that contextual calibration and risk‑aware delegation materially improve agentic cooperation.


<details>
<summary>Abstract</summary>

We revisit multi-agent delegation under a stronger and more realistic assumption: an agent's capability is not fixed at the skill level, but depends on task context. A coding agent may excel at short standalone edits yet fail on long-horizon debugging; a planner may perform well on shallow tasks yet degrade on chained dependencies. Static skill-level capability profiles therefore average over heterogeneous situations and can induce systematic misdelegation. We propose CADMAS-CTX, a framework for contextual capability calibration. For each agent, skill, and coarse context bucket, CADMAS-CTX maintains a Beta posterior that captures stable experience in that part of the task space. Delegation is then made by a risk-aware score that combines the posterior mean with an uncertainty penalty, so that agents delegate only when a peer appears better and that assessment is sufficiently well supported by evidence. This paper makes three contributions. First, a hierarchical contextual capability profile replaces static skill-level confidence with context-conditioned posteriors. Second, based on contextual bandit theory, we formally prove context-aware routing achieves lower cumulative regret than static routing under sufficient context heterogeneity, formalizing the bias-variance tradeoff. Third, we empirically validate our method on GAIA and SWE-bench benchmarks. On GAIA with GPT-4o agents, CADMAS-CTX achieves 0.442 accuracy, outperforming static baseline 0.381 and AutoGen 0.354 with non-overlapping 95% confidence intervals. On SWE-bench Lite, it improves resolve rate from 22.3% to 31.4%. Ablations show the uncertainty penalty improves robustness against context tagging noise. Our results demonstrate contextual calibration and risk-aware delegation significantly improve multi-agent teamwork compared with static global skill assignments.

</details>


### 122. RAVEN: Retrieval-Augmented Vulnerability Exploration Network for Memory Corruption Analysis in User Code and Binary Programs

- **Authors:** Parteek Jamwal, Minghao Shao, Boyuan Chen, Achyuta Muthuvelan, Asini Subanya, Boubacar Ballo, Kashish Satija, Mariam Shafey, Mohamed Mahmoud, Moncif Dahaji Bouffi, Pasindu Wickramasinghe, Siyona Goel, Yaakulya Sabbani, Hakim Hacid, Mthandazo Ndhlovu, Eleanna Kafeza, Sanjay Rawat, Muhammad Shafique
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.17948v1](http://arxiv.org/abs/2604.17948v1)
- **PDF:** [https://arxiv.org/pdf/2604.17948v1](https://arxiv.org/pdf/2604.17948v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> RAVEN introduces an end‑to‑end, agent‑based framework that combines Large Language Model (LLM) agents with Retrieval‑Augmented Generation (RAG) to automatically produce detailed vulnerability analysis reports that follow the Google Project Zero Root‑Cause Analysis format. The system orchestrates four specialized agents—Explorer (identifies the flaw), a RAG engine (fetches relevant CWE and Project Zero knowledge), Analyst (assesses impact and exploitation) and Reporter (generates the structured document)—and uses a task‑specific LLM Judge to grade reports on structure, correctness, reasoning, and remediation. Evaluated on 105 vulnerable code snippets spanning 15 CWE categories from NIST‑SARD, RAVEN achieved an average quality score of 54.21 %, demonstrating the feasibility of autonomous, high‑fidelity vulnerability documentation for agentic AI applications.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have demonstrated remarkable capabilities across various cybersecurity tasks, including vulnerability classification, detection, and patching. However, their potential in automated vulnerability report documentation and analysis remains underexplored. We present RAVEN (Retrieval Augmented Vulnerability Exploration Network), a framework leveraging LLM agents and Retrieval Augmented Generation (RAG) to synthesize comprehensive vulnerability analysis reports. Given vulnerable source code, RAVEN generates reports following the Google Project Zero Root Cause Analysis template. The framework uses four modules: an Explorer agent for vulnerability identification, a RAG engine retrieving relevant knowledge from curated databases including Google Project Zero reports and CWE entries, an Analyst agent for impact and exploitation assessment, and a Reporter agent for structured report generation. To ensure quality, RAVEN includes a task specific LLM Judge evaluating reports across structural integrity, ground truth alignment, code reasoning quality, and remediation quality. We evaluate RAVEN on 105 vulnerable code samples covering 15 CWE types from the NIST-SARD dataset. Results show an average quality score of 54.21%, supporting the effectiveness of our approach for automated vulnerability documentation.

</details>


### 123. GraSP: Graph-Structured Skill Compositions for LLM Agents

- **Authors:** Tianle Xia, Lingxiang Hu, Yiding Sun, Ming Xu, Lan Xu, Siying Wang, Wei Xu, Jie Jiang
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.17870v1](http://arxiv.org/abs/2604.17870v1)
- **PDF:** [https://arxiv.org/pdf/2604.17870v1](https://arxiv.org/pdf/2604.17870v1)
- **Categories:** cs.CL


> The paper introduces **GraSP**, an executable “skill‑graph” framework that turns a flat collection of LLM‑retrieved skills into a typed directed‑acyclic graph encoding precondition‑effect causal dependencies, and then compiles and runs the graph with node‑level verification and a locality‑bounded repair mechanism (five typed operators) that reduces replanning complexity from O(N) to O(d^h). Experiments on four diverse benchmarks (ALFWorld, ScienceWorld, WebShop, InterCode) with eight LLM backbones show that GraSP consistently outperforms flat‑skill baselines such as ReAct, Reflexion and ExpeL, achieving up to +19 reward points and up to 41 % fewer environment steps, with larger gains on more complex tasks and robustness to over‑retrieval or degraded skill quality. The key contribution is demonstrating that **structured skill orchestration via graph compilation—not merely larger skill libraries—is essential for reliable, performant agentic AI**.


<details>
<summary>Abstract</summary>

Skill ecosystems for LLM agents have matured rapidly, yet recent benchmarks show that providing agents with more skills does not monotonically improve performance -- focused sets of 2-3 skills outperform comprehensive documentation, and excessive skills actually hurt. The bottleneck has shifted from skill availability to skill orchestration: agents need not more skills, but a structural mechanism to select, compose, and execute them with explicit causal dependencies. We propose GraSP, the first executable skill graph architecture that introduces a compilation layer between skill retrieval and execution. GraSP transforms flat skill sets into typed directed acyclic graphs (DAGs) with precondition-effect edges, executes them with node-level verification, and performs locality-bounded repair through five typed operators -- reducing replanning from O(N) to O(d^h). Across ALFWorld, ScienceWorld, WebShop, and InterCode with eight LLM backbones, GraSP outperforms ReAct, Reflexion, ExpeL, and flat skill baselines in every configuration, improving reward by up to +19 points over the strongest baseline while cutting environment steps by up to 41%. GraSP's advantage grows with task complexity and is robust to both skill over-retrieval and quality degradation, confirming that structured orchestration -- not larger skill libraries -- is the key to reliable agent execution.

</details>


### 124. Learning from AVA: Early Lessons from a Curated and Trustworthy Generative AI for Policy and Development Research

- **Authors:** Nimisha Karnatak, Mohamad Chatila, Daniel Alejandro Pinzón Hernández, Reza Yazdanfar, Michelle Dugas, Renos Vakis
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.17843v1](http://arxiv.org/abs/2604.17843v1)
- **PDF:** [https://arxiv.org/pdf/2604.17843v1](https://arxiv.org/pdf/2604.17843v1)
- **Categories:** cs.HC, cs.AI


> The paper introduces **AVA (AI + Verified Analysis)**, a specialized generative‑AI platform that routes user queries through a multi‑agent pipeline built on a curated, citation‑indexed library of 4,000+ World Bank reports and supports multilingual access. By embedding **epistemic humility**—implemented as traceable, page‑anchored citations and a “reasoned abstention” module that declines unsupported requests with justification—the system delivers evidence‑backed syntheses while explicitly flagging its limits. An in‑the‑wild evaluation involving 2,200 users across 116 countries shows that sustained AVA use saves 2.4–3.9 hours per week per user, is perceived as a trusted “evidence engine,” and validates the design guidelines for building domain‑specific, humility‑driven agentic AI systems.


<details>
<summary>Abstract</summary>

General-purpose LLMs pose misinformation risks for development and policy experts, lacking epistemic humility for verifiable outputs. We present AVA (AI + Verified Analysis), a GenAI platform built on a curated library of over 4,000 World Bank Reports with multilingual capabilities. AVA's multi-agent pipeline enables users to query and receive evidence-based syntheses. It operationalizes epistemic humility through two mechanisms: citation verifiability (tracing claims to sources) and reasoned abstention (declining unsupported queries with justification and redirection). We conducted an in-the-wild evaluation with over 2,200 individuals from heterogeneous organisations and roles in 116 countries, via log analysis, surveys, and 20 interviews. Difference-in-Differences estimates associate sustained engagement with 2.4-3.9 hours saved weekly. Qualitatively, participants used AVA as a specialized "evidence engine"; reasoned abstention clarified scope boundaries, and trust was calibrated through institutional provenance and page-anchored citations. We contribute design guidelines for specialized AI and articulate a vision for "ecosystem-aware" Humble AI.

</details>


### 125. From Craft to Kernel: A Governance-First Execution Architecture and Semantic ISA for Agentic Computers

- **Authors:** Xiangyu Wen, Yuang Zhao, Xiaoyu Xu, Lingjun Chen, Changran Xu, Shu Chi, Jianrong Ding, Zeju Li, Haomin Li, Li Jiang, Fangxin Liu, Qiang Xu
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.18652v1](http://arxiv.org/abs/2604.18652v1)
- **PDF:** [https://arxiv.org/pdf/2604.18652v1](https://arxiv.org/pdf/2604.18652v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper introduces **Arbiter‑K**, a “governance‑first” execution architecture that treats a large language model (LLM) as a probabilistic processing unit (PPU) wrapped by a deterministic, neuro‑symbolic kernel with a **semantic ISA** that converts the PPU’s stochastic messages into concrete instructions.  

**Methodology:** By materializing each probabilistic inference as an instruction, the kernel builds a runtime **Instruction Dependency Graph** and a **Security Context Registry**, enabling fine‑grained taint propagation and deterministic interception of unsafe actions (e.g., privileged tool calls or network egress). The system can automatically correct unsafe execution paths or roll back the architecture when policy violations are detected.  

**Key findings:** In the OpenClaw and NanoBot benchmarks, Arbiter‑K enforces security at the microarchitectural level, intercepting 76 %–95 % of unsafe trajectories and delivering a 92.79 % absolute improvement over baseline LLM‑only policies, demonstrating that a governance‑first kernel can dramatically reduce the fragility that currently hampers production‑grade agentic AI.


<details>
<summary>Abstract</summary>

The transition of agentic AI from brittle prototypes to production systems is stalled by a pervasive crisis of craft. We suggest that the prevailing orchestration paradigm-delegating the system control loop to large language models and merely patching with heuristic guardrails-is the root cause of this fragility. Instead, we propose Arbiter-K, a Governance-First execution architecture that reconceptualizes the underlying model as a Probabilistic Processing Unit encapsulated by a deterministic, neuro-symbolic kernel. Arbiter-K implements a Semantic Instruction Set Architecture (ISA) to reify probabilistic messages into discrete instructions. This allows the kernel to maintain a Security Context Registry and construct an Instruction Dependency Graph at runtime, enabling active taint propagation based on the data-flow pedigree of each reasoning node. By leveraging this mechanism, Arbiter-K precisely interdicts unsafe trajectories at deterministic sinks (e.g., high-risk tool calls or unauthorized network egress) and enables autonomous execution correction and architectural rollback when security policies are triggered. Evaluations on OpenClaw and NanoBot demonstrate that Arbiter-K enforces security as a microarchitectural property, achieving 76% to 95% unsafe interception for a 92.79% absolute gain over native policies. The code is publicly available at https://github.com/cure-lab/ArbiterOS.

</details>


### 126. WebUncertainty: Dual-Level Uncertainty Driven Planning and Reasoning For Autonomous Web Agent

- **Authors:** Lingfeng Zhang, Yongan Sun, Jinpeng Hu, Hui Ma, Yang Ying, Kuien Liu, Zenglin Shi, Meng Wang
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.17821v2](http://arxiv.org/abs/2604.17821v2)
- **PDF:** [https://arxiv.org/pdf/2604.17821v2](https://arxiv.org/pdf/2604.17821v2)
- **Categories:** cs.AI


> WebUncertainty introduces a dual‑level uncertainty‑aware framework for autonomous web agents: (1) a Task‑Uncertainty‑Driven Adaptive Planning mechanism that switches between planning modes based on the estimated difficulty of navigating an unfamiliar web environment, and (2) an Action‑Uncertainty‑Driven Monte Carlo Tree Search (MCTS) reasoning module that quantifies both aleatoric and epistemic uncertainty via a Confidence‑induced Action Uncertainty (ConActU) score to prune and prioritize search branches. The authors evaluate the system on the WebArena and WebVoyager benchmarks, showing that the uncertainty‑guided planner and MCTS reasoning together yield statistically significant gains over existing LLM‑based agents in long‑horizon, dynamic web tasks. These results suggest that modeling and exploiting uncertainty at both the task‑selection and action‑execution levels can markedly improve the robustness and performance of agentic AI operating on real‑world webpages.


<details>
<summary>Abstract</summary>

Recent advancements in large language models (LLMs) have empowered autonomous web agents to execute natural language instructions directly on real-world webpages. However, existing agents often struggle with complex tasks involving dynamic interactions and long-horizon execution due to rigid planning strategies and hallucination-prone reasoning. To address these limitations, we propose WebUncertainty, a novel autonomous agent framework designed to tackle dual-level uncertainty in planning and reasoning. Specifically, we design a Task Uncertainty-Driven Adaptive Planning Mechanism that adaptively selects planning modes to navigate unknown environments. Furthermore, we introduce an Action Uncertainty-Driven Monte Carlo tree search (MCTS) Reasoning Mechanism. This mechanism incorporates the Confidence-induced Action Uncertainty (ConActU) strategy to quantify both aleatoric uncertainty (AU) and epistemic uncertainty (EU), thereby optimizing the search process and guiding robust decision-making. Experimental results on the WebArena and WebVoyager benchmarks demonstrate that WebUncertainty achieves superior performance compared to state-of-the-art baselines.

</details>


### 127. Prompt Optimization Enables Stable Algorithmic Collusion in LLM Agents

- **Authors:** Yingtao Tian
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.17774v1](http://arxiv.org/abs/2604.17774v1)
- **PDF:** [https://arxiv.org/pdf/2604.17774v1](https://arxiv.org/pdf/2604.17774v1)
- **Categories:** cs.AI


> The paper shows that automatically optimizing prompts can turn large‑language‑model (LLM) agents into stable colluders in simulated duopoly markets. By embedding the agents in a meta‑learning loop—where a separate LLM meta‑optimizer iteratively refines a shared “strategic guidance” prompt—the authors demonstrate that the agents quickly converge on tacit‑collusion policies that yield supracompetitive prices, out‑performing hand‑crafted baselines and transferring to unseen market instances. The results reveal that prompt‑level meta‑optimization discovers general coordination mechanisms, highlighting a new safety risk for autonomous AI agents that must be addressed in future research.


<details>
<summary>Abstract</summary>

LLM agents in markets present algorithmic collusion risks. While prior work shows LLM agents reach supracompetitive prices through tacit coordination, existing research focuses on hand-crafted prompts. The emerging paradigm of prompt optimization necessitates new methodologies for understanding autonomous agent behavior. We investigate whether prompt optimization leads to emergent collusive behaviors in market simulations. We propose a meta-learning loop where LLM agents participate in duopoly markets and an LLM meta-optimizer iteratively refines shared strategic guidance. Our experiments reveal that meta-prompt optimization enables agents to discover stable tacit collusion strategies with substantially improved coordination quality compared to baseline agents. These behaviors generalize to held-out test markets, indicating discovery of general coordination principles. Analysis of evolved prompts reveals systematic coordination mechanisms through stable shared strategies. Our findings call for further investigation into AI safety implications in autonomous multi-agent systems.

</details>


### 128. HiRAS: A Hierarchical Multi-Agent Framework for Paper-to-Code Generation and Execution

- **Authors:** Hanhua Hong, Yizhi LI, Jiaoyan Chen, Sophia Ananiadou, Xiaoli Li, Jung-jae Kim, Chenghua Lin
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.17745v1](http://arxiv.org/abs/2604.17745v1)
- **PDF:** [https://arxiv.org/pdf/2604.17745v1](https://arxiv.org/pdf/2604.17745v1)
- **Categories:** cs.CL


> The paper introduces **HiRAS**, a hierarchical multi‑agent system in which higher‑level manager agents dynamically supervise and orchestrate specialized sub‑agents that handle distinct steps of paper‑to‑code generation and execution, thereby improving global coordination compared with prior fixed‑pipeline approaches. The authors augment the existing Paper2Code benchmark with a new evaluation protocol (Paper2Code‑Extra) that incorporates repository‑level metadata and aligns reference‑free scores with reference‑based metrics, and they train open‑source backbone models within the HiRAS framework. Empirical results show that HiRAS achieves more than a 10 % relative gain over the previous state‑of‑the‑art while markedly reducing hallucinations, demonstrating a more robust and scalable solution for autonomous experiment reproduction in agentic AI.


<details>
<summary>Abstract</summary>

Recent advances in large language models have highlighted their potential to automate computational research, particularly reproducing experimental results. However, existing approaches still use fixed sequential agent pipelines with weak global coordination, which limits their robustness and overall performance. In this work, we propose Hierarchical Research Agent System (HiRAS), a hierarchical multi-agent framework for end-to-end experiment reproduction that employs supervisory manager agents to coordinate specialised agents across fine-grained stages. We also identify limitations in the reference-free evaluation of the Paper2Code benchmark and introduce Paper2Code-Extra (P2C-Ex), a refined protocol that incorporates repository-level information and better aligns with the original reference-based metric. We conduct extensive evaluation, validating the effectiveness and robustness of our proposed methods, and observing improvements, including >10\% relative performance gain beyond the previous state-of-the-art using open-source backbone models and significantly reduced hallucination in evaluation. Our work is available on GitHub: https://github.com/KOU-199024/HiRAS.

</details>


### 129. Co-evolving Agent Architectures and Interpretable Reasoning for Automated Optimization

- **Authors:** Jiahao Huang, Peilan Xu, Xiaoya Nan, Wenjian Luo
- **Published:** 2026-04-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.17708v1](http://arxiv.org/abs/2604.17708v1)
- **PDF:** [https://arxiv.org/pdf/2604.17708v1](https://arxiv.org/pdf/2604.17708v1)
- **Categories:** cs.AI


> **Main contribution**: The paper introduces **EvoOR‑Agent**, a co‑evolutionary system that simultaneously evolves both the *structure* of an OR‑agent’s workflow and the *reasoning trajectories* used to solve optimization problems, thereby moving beyond static, hand‑crafted LLM pipelines.  

**Methodology**: Agent workflows are encoded as activity‑on‑edge (AOE) graphs that capture task ordering, dependencies, and alternative reasoning paths. An evolutionary loop maintains a population of “reasoning individuals” that are recombined and mutated according to the graph topology (path‑conditioned recombination, multi‑granularity semantic mutation) and are periodically updated by elitism. A knowledge‑base module seeds the population with reusable OR heuristics and informs semantic variations.  

**Key findings**: Across a diverse set of operations‑research benchmarks, EvoOR‑Agent consistently outperforms zero‑shot LLMs, fixed‑pipeline OR agents, and prior evolutionary agents. Ablation studies show that the explicit evolution of architecture graphs and graph‑guided reasoning search both boost solution quality and yield interpretable, modular workflow structures, demonstrating the value of treating agent architecture and reasoning as jointly evolvable objects for adaptive, transparent automated optimization.


<details>
<summary>Abstract</summary>

Automating operations research (OR) with large language models (LLMs) remains limited by hand-crafted reasoning--execution workflows. Complex OR tasks require adaptive coordination among problem interpretation, mathematical formulation, solver selection, code generation, and iterative debugging. To address this limitation, we propose EvoOR-Agent, a co-evolutionary framework for automated optimization. The framework represents agent workflows as activity-on-edge (AOE)-style networks, making workflow topology, execution dependencies, and alternative reasoning paths explicit. On this representation, the framework maintains an architecture graph and evolves a population of reasoning individuals through graph-mediated path-conditioned recombination, multi-granularity semantic mutation, and elitist population update. A knowledge-base-assisted experience-acquisition module further injects reusable OR practices into initialization and semantic variation. Empirical results on heterogeneous OR benchmarks show that the proposed framework consistently improves over zero-shot LLMs, fixed-pipeline OR agents, and representative evolutionary agent frameworks. Case studies and ablation analyses further indicate that explicit architecture evolution and graph-supported reasoning-trajectory search contribute to both performance improvement and structural interpretability. These results suggest that treating agent architectures and reasoning trajectories as evolvable objects provides an effective route toward adaptive and interpretable automated optimization.

</details>



## Medrxiv (2 papers)


### 1. Artificial Intelligence Agents in Mental Health: A Systematic Review and Meta Analysis

- **Authors:** Zhu, L., Wang, W., Liang, Z., Tan, W., Chen, B., Lin, X., Wu, Z., Yu, H., Li, X., Jiao, J., He, S., Dai, G., Niu, J., Zhong, Y., Hua, W., Chan, N. Y., Lu, L., Wing, Y. K., Ma, X., Fan, L.
- **Published:** 2026-04-22
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.21.26351365](https://doi.org/10.64898/2026.04.21.26351365)

- **Categories:** psychiatry and clinical psychology


> **Contribution:** The paper provides the first systematic review and meta‑analysis of AI‑driven mental‑health agents (2023‑2025), introducing a six‑dimensional audit framework that distinguishes true “agentic” systems (multi‑role, tool‑augmented, planner‑based pipelines) from the prevalent monolithic chatbot implementations.

**Methodology:** The authors extracted 202 peer‑reviewed systems, categorising each along (i) model type and workflow, (ii) data modality and provenance, (iii) ICD‑11 diagnosis focus, (iv) demographic coverage, (v) downstream clinical task, and (vi) evaluation protocol; quantitative synthesis examined prevalence of each dimension and performed meta‑analysis of reported performance and safety metrics.

**Key Findings for Agentic AI:** 1) Over 80 % of systems are single‑agent text chatbots trained on self‑report data, largely targeting depression, anxiety and suicidality, with minimal coverage of severe or comorbid disorders. 2) Only a nascent subset (~12 %) adopts multi‑agent, role‑aware architectures that link planners, retrieval modules, safety auditors and external tools, showing modest gains in personalization and safety but raising new reliability and regulatory risks. 3) Evaluation is dominated by offline or vignette‑based metrics; prospective, clinician‑in‑the‑loop or longitudinal real‑world studies are scarce, highlighting a critical gap for establishing trustworthy, deployable mental‑health AI agents. The authors recommend shifting research toward clinically grounded, privacy‑preserving multi‑agent pipelines, broader demographic representation, and rigorous real‑world validation.


<details>
<summary>Abstract</summary>

The rapid rise of large language models (LLMs) and foundation models has accelerated efforts to build artificial intelligence (AI) agents for mental health assessment, triage, psychotherapy support and clinical decision assistance. Yet a gap persists between healthcare and AI-focused work: while both communities use the language of "agents," clinical research largely describes monolithic chatbots, whereas AI studies emphasize agentic properties such as autonomous planning, multiagent coordination, tool and database use and integration with multimodal mental health data streams.

In this Review, we conduct a systematic analysis of mental health AI agent systems from 2023 to 2025 using a six-dimensional audit framework: (i) system type (base model lineage, interface modality and workflow composition, from rule-based tools to role-aware multi-agent foundation-model systems), (ii) data scope (modalities and provenance, from elicited self-report and chatbot dialogues to electronic health records, biosensing and synthetic corpora), (iii) mental health focus (mapped to ICD-11 diagnostic groupings), (iv) demographics (age strata, geography and sex representation), (v) downstream tasks (screening/triage, clinical decision support, therapeutic interventions, documentation, ethical-legal support and education/simulation) and (vi) evaluation types (automated metrics, language quality benchmarks, safety stress tests, expert review and clinician or patient involvement).

Across this corpus, we find that most systems (1) concentrate on depression, anxiety and suicidality, with sparse coverage of severe mental illness, neurocognitive disorders, substance use and complex comorbidity; (2) rely heavily on text-based self-report rather than clinically verified longitudinal data or genuinely multimodal inputs; (3) are implemented as single-agent chatbots powered by general-purpose LLMs rather than role-structured, workflow-integrated pipelines; and (4) are evaluated primarily via offline metrics or vignette-based scenarios, with few prospective, clinician- or patient-in-the-loop studies. At the same time, an emerging class of agentic systems assigns foundation models explicit roles as planners, retrieval agents, safety auditors or supervisors coordinating other models and tools. These multiagent, tool-augmented workflows promise personalization, safety monitoring and greater transparency, but they also introduce new risks around reliability, bias amplification, privacy, regulatory accountability and the blurring of clinical versus non-clinical roles.

We conclude by outlining priorities for the next generation of mental health AI agents: clinically grounded, role-aware multi-agent architectures; transparent and privacy-preserving use of clinical and elicited data; demographic and cultural broadening beyond predominantly Western adult samples; and evaluation pipelines that progress from offline benchmarks to longitudinal, real-world studies with routine safety auditing and clear governance of responsibilities between agents and human clinicians.

</details>


### 2. Uncertainty-Gated Glaucoma Screening: Combining Semi-Supervised Classification with Multi-Agent Large Language Model Deliberation

- **Authors:** Garimella Narasimha, S. V., Brown, N., Sridhar, S.
- **Published:** 2026-04-20
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.17.26351127](https://doi.org/10.64898/2026.04.17.26351127)

- **Categories:** ophthalmology


> The paper introduces a two‑stage glaucoma‑screening pipeline that first uses a semi‑supervised EfficientNetV2‑S classifier (trained with only 350 labeled OCT scans) to flag uncertain cases, then routes those cases to a multi‑agent deliberation system built on the MedGemma‑4B large language model. The uncertainty estimator reliably separates confident from ambiguous predictions (96 % vs 74 % accuracy), providing a triage signal that sends 124 ambiguous cases to three specialist agents who discuss over three rounds. On these hard cases the agents achieve 100 % sensitivity and 89.5 % overall accuracy—substantially higher than the classifier’s 73.4 %—demonstrating that uncertainty‑gated routing to LLM‑based agentic deliberation can markedly improve diagnostic performance where vision‑only models are least reliable.


<details>
<summary>Abstract</summary>

Automated glaucoma screening from optical coherence tomography (OCT) faces two persistent challenges: scarcity of expert-labeled data and unreliable model predictions on diagnostically ambiguous cases. We present a two-tier diagnostic pipeline that addresses both. In the first tier, an EfficientNetV2-S classifier trained under a semi-supervised pseudo supervisor framework achieves 0.84 AUC on 150 held-out test patients from the Harvard Glaucoma Detection and Progression dataset, using only 350 labeled training samples out of 700. In the second tier, 124 flagged cases are routed to a multi-agent system built on MedGemma 4B, where three specialist agents deliberate over three rounds before rendering a final diagnosis. On these flagged cases, the agent system achieves 100% sensitivity--detecting all 55 glaucoma cases with zero missed diagnoses--and 89.5% overall accuracy (111/124), compared to the classifiers 73.4% (91/124). Uncertainty analysis confirms that the classifiers output probability reliably separates confident predictions (96.3% accuracy, n = 27) from uncertain ones (74.0%, n = 123), producing a 22-percentage-point gap that serves as a triage signal. The agents fix 32 cases the classifier misclassifies while introducing 12 new errors, yielding a net improvement of 20 cases. These results are from a single training run without variance estimates and should be interpreted as preliminary evidence that uncertainty-gated routing to vision-language model agents can meaningfully improve diagnostic accuracy on the cases where automated classifiers are least reliable.

</details>



## Biorxiv (1 papers)


### 1. MetaMuse: A Multi-Agent AI System for Biomedical Metadata Curation and Harmonization

- **Authors:** Mittal, E., Litman, E., Myers, T., Agarwal, V., Gopinath, A., Kassis, T.
- **Published:** 2026-04-20
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.04.12.718044](https://doi.org/10.64898/2026.04.12.718044)

- **Categories:** genomics


> The paper introduces **MetaMuse**, a modular, multi‑agent AI framework that automatically curates and harmonizes biomedical metadata from repositories such as GEO. The system chains large‑language‑model (LLM) agents for contextual extraction, a central orchestrator that enforces cross‑field logical consistency, and a SapBERT‑based semantic normalizer that maps free‑text values to ontology terms, deliberately opting for conservative false negatives to avoid hallucination. Evaluated on a gold‑standard GEO dataset, MetaMuse attains >95 % accuracy on key metadata fields and scales to hundreds of samples, providing an auditable, high‑integrity pipeline that advances agentic AI applications in biomedical data curation.


<details>
<summary>Abstract</summary>

Inconsistent and unstructured metadata in public biomedical repositories, such as the Gene Expression Omnibus (GEO), severely limits data discoverability and research reproducibility. To address this, we introduce MO_SCPLOWETAC_SCPLOWMO_SCPLOWUSEC_SCPLOW, a modular, multi-agent artificial intelligence framework designed to autonomously extract, validate, and standardize unstructured biomedical metadata. Operating through a three-stage architecture utilizing large language model agents, specialized CO_SCPLOWURATORC_SCPLOWAO_SCPLOWGENTSC_SCPLOW contextually extract candidate values for specific target metadata fields. A centralized AO_SCPLOWRBITRATORC_SCPLOWAO_SCPLOWGENTC_SCPLOW enforces cross-field logical consistency to prevent contradictory annotations. Finally, a NO_SCPLOWORMALIZERC_SCPLOWAO_SCPLOWGENTC_SCPLOW leveraging a domain-specific semantic search model (SapBERT) maps these free-text candidates to formal ontological terms. We evaluated MO_SCPLOWETAC_SCPLOWMO_SCPLOWUSEC_SCPLOW on a gold-standard dataset of manually curated GEO samples, achieving over 95% curation accuracy across key target metadata fields, and demonstrated robust scalability on a broader dataset of 400 samples. Notably, MO_SCPLOWETAC_SCPLOWMO_SCPLOWUSEC_SCPLOW avoids data hallucination by defaulting to conservative false negatives when evidence is ambiguous, thereby preserving strict data integrity. By providing a fully auditable and context-aware curation pipeline, MO_SCPLOWETAC_SCPLOWMO_SCPLOWUSEC_SCPLOW offers a scalable solution for enriching public data repositories and accelerating reproducible, data-driven scientific discovery.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*