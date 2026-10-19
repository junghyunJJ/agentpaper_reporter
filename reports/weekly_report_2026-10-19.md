# Weekly AI Agent Paper Report

**Generated:** 2026-10-19 16:33
**Period:** 2026-10-12 to 2026-10-18

## Summary

- **Total papers fetched:** 816
- **Papers matching keywords:** 170
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-10-12) | Change |
|--------|-----------|-----------|--------|
| Total matched | 170 | 178 | -8 |
| arxiv | 164 | 174 | -10 |
| biorxiv | 3 | 3 | +0 |
| medrxiv | 3 | 1 | +2 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (6 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. BioMINTREL expands biological problem solving through cross-disciplinary representations

- **Authors:** Dong, J., Zhang, Y., Gao, E., Yang, C., Wang, J., Zha, C., Wu, Z., Xu, X., Zhou, J., Gao, X.
- **Published:** 2026-10-16
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.10.757703](https://doi.org/10.64898/2026.10.10.757703)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Biological research agents often rely on familiar analytical methods, limiting the questions explored in existing data. We introduce BioMINTREL, an AI agent that finds methods from other disciplines and connects them to biological measurements. It can draw on relationships among datasets and complementary ideas from several methods to develop new questions and analyses. We evaluate it on BioMDC-Bench, which assesses 228 possible applications of computational methods to biological tasks. Compared with GPT-5.4 mini and Qwen3.6-35B, BioMINTREL improves F1 agreement with human experts by up to 45.3 percentage points and increases coverage of applications supported by studies published in subsequent years by up to 58.8 percentage points. Four case studies on real data go beyond previous analyses to reveal dose-specific variant effects, constraints on spatial cell communication and routes through perturbation-response states, and identify the sampling needed to test whether rare high-state cells predict later lineage size. These results highlight BioMINTREL's potential to expand questions in existing data and suggest directions for subsequent research.

</details>


### 2. ExpertTwins: Auditable Long Horizon Scientific Panels through Grounded Expertise

- **Authors:** Foroughi pour, A., Shirinifard, A.
- **Published:** 2026-10-15
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.06.757114](https://doi.org/10.64898/2026.10.06.757114)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent language-model systems increasingly assign roles to agents and let them deliberate. A role label, however, does not specify which evidence an agent can bring or which standard it applies before accepting a conclusion. Agents that read one another's outputs tend to converge. We present ExpertTwins, a framework in which each seat of a scientific panel is defined by an inspectable evidence policy. Discipline seats retrieve under field-specific queries, and scientist-associated seats retrieve from attributed publications and a citation-derived scholarly neighborhood. Private initial packets, structured exchange, cited-source disclosure, deterministic quotation checks, and peer source review turn deliberation into an auditable record, which we also render as interactive idea-flow maps. Scientist associations denote publication-grounded perspectives, not replicas or endorsements of named researchers. In a nine-seat, four-turn neuroblastoma panel, 438 of 439 claims passed all attached quotation checks, and seats withdrew or defended positions when challenged on their evidence. A ten-turn panel sustained evidence acquisition and differentiated recommendations without conversational collapse. Across six base models given byte-identical initial packets, four sustained 97.9-99.8% quotation grounding, and at least 91% on every turn, whereas Haiku 4.5 failed by paraphrase and GPT-5 mini by silence. Agreement among strong models fell from 31% of claims at turn one to 5% at turn four. With follow-up questions held fixed, it stayed at 28-33% through turn three and fell to 20% only at the closing turn. Stress runs showed the collapse guardrail escalating through its full intervention ladder when consensus was forced, but missing deference to one unusually strong seat. On idea-flow maps, the forced consensus appeared as parallel lanes of identical ideas, although quotation grounding and participation balance stayed at their maxima. We also reimplemented two close published systems and ran them on matched models, seats, and questions. A multi-persona debate cited only real records, yet none of its cited sentences carried a checkable quotation and it had no way to abstain. An author-memory fusion system ran only after its fact checker was split by seat to fit in context. Its fused answer kept about two-thirds of the fact-checked specialist claims, answered 36 of 60 question parts on which our seats had abstained, and showed the reader 19% of its agents' disagreements. In a computational pathology case study, six scientist-associated agents built distinct pipelines to predict MYCN amplification from whole-slide images. Across six base models, seat-by-model interaction explained 57% of internal variance, and internal rank poorly predicted external rank (r = 0.18 across 36 nominees). These results establish differentiated, source-traceable scientific reasoning as an operational capability and identify the base model as a parameter that must be reported with the protocol.

</details>


### 3. In Vivo Transcriptomics-Based Framework for Systematic Indication Expansion

- **Authors:** Palmer, Z., Koirala, S., Talukdar, N., Zhang, X., Garver, H., Mahlmeister, M., Huang, L., Joseph, D., Leshchiner, D., Shankar, R., Watts, S. W., Li, X., Glicksberg, B. S., Lauver, A., Chen, B.
- **Published:** 2026-10-14
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.12.758524](https://doi.org/10.64898/2026.10.12.758524)

- **Categories:** systems biology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Capturing the systemic effects of drugs in vivo remains a fundamental challenge for drug repurposing strategies. Here, we present an in vivo transcriptomics-based drug repurposing framework that profiles multi-organ RNA-seq from drug-treated rodents to model systemic drug responses and match tissue-specific drug signatures against a compendium of disease signatures for indication expansion. We applied this framework to semaglutide, a GLP-1 receptor agonist originally developed for diabetes and subsequently expanded for several other indications. By harmonizing more than 900 human disease transcriptomic signatures via agentic AI and using Z-transformed reversal of gene expression scoring to quantify drug-disease relationships, our approach successfully recovered established semaglutide indications while deprioritizing Alzheimers disease, an indication for which semaglutide was not effective. Top predictions for common diseases were supported by real-world electronic health record data from the Mount Sinai Health System and several predictions for rare indications are proposed for further investigation. This framework provides a scalable strategy for indication expansion across diverse therapeutic agents, especially investigational compounds for which real-world evidence remains sparse.

</details>


### 4. inClinico Agent for clinical trial endpoint prediction and prospective evaluation

- **Authors:** Chen, J., Duan, C., Gou, W., Wang, J., Zheng, Z., Leung, H., Naumov, V., Sidorenko, D., Aliper, A., Ren, F., Pun, F. W., Zhavoronkov, A.
- **Published:** 2026-10-16
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.10.13.26365373](https://doi.org/10.64898/2026.10.13.26365373)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

High attrition rates across clinical drug development impose immense clinical and financial burdens, yet prospectively forecasting whether an individual trial will achieve its primary endpoint remains challenging. Here we present a machine-learning system that predicts clinical trial success across phases I-IV, independently modeling studies with efficacy versus safety/toxicity primary endpoints. To prevent lookahead bias and outcome leakage, models are trained on registration-time features, including target and mechanism-of-action precedent, drug modality and novelty, trial design and operational characteristics, and frozen literature-derived target-choice embeddings. Each prediction yields a continuous Predictive Trial Index (PTI) between 0 and 1 reflecting success probability. On a test set of trials initiated in 2021 or later, the efficacy model achieved an area under the receiver operating characteristic curve (AUROC) of 0.828 (95% CI 0.812-0.845; n = 2,347) and the safety/toxicity model reached 0.809 (95% CI 0.787-0.831; n = 1,485). These models are embedded in inClinico Agent, an agentic AI system integrating frontier large language models (LLMs) with deterministic scoring engines, retrieval tools and specialized clinical skills. We also introduce ClinBench, a prospective benchmark of 2,040 ongoing trials evaluated by inClinico Agent and five frontier LLMs, establishing a leakage-free foundation for tracking prospective predictive accuracy as trials reach completion.

</details>


### 5. inClinico Agent for clinical trial endpoint prediction and prospective evaluation

- **Authors:** Chen, J., Duan, C., Gou, W., Wang, J., Zheng, Z., Leung, H., Naumov, V., Sidorenko, D., Aliper, A., Ren, F., Pun, F. W., Zhavoronkov, A.
- **Published:** 2026-10-15
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.10.13.26365373](https://doi.org/10.64898/2026.10.13.26365373)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

High attrition rates across clinical drug development impose immense clinical and financial burdens, yet prospectively forecasting whether an individual trial will achieve its primary endpoint remains challenging. Here we present a machine-learning system that predicts clinical trial success across phases I-IV, independently modeling studies with efficacy versus safety/toxicity primary endpoints. To prevent lookahead bias and outcome leakage, models are trained on registration-time features, including target and mechanism-of-action precedent, drug modality and novelty, trial design and operational characteristics, and frozen literature-derived target-choice embeddings. Each prediction yields a continuous Predictive Trial Index (PTI) between 0 and 1 reflecting success probability. On a test set of trials initiated in 2021 or later, the efficacy model achieved an area under the receiver operating characteristic curve (AUROC) of 0.828 (95% CI 0.812-0.845; n = 2,347) and the safety/toxicity model reached 0.809 (95% CI 0.787-0.831; n = 1,485). These models are embedded in inClinico Agent, an agentic AI system integrating frontier large language models (LLMs) with deterministic scoring engines, retrieval tools and specialized clinical skills. We also introduce ClinBench, a prospective benchmark of 2,040 ongoing trials evaluated by inClinico Agent and five frontier LLMs, establishing a leakage-free foundation for tracking prospective predictive accuracy as trials reach completion.

</details>


### 6. Human-Guided Agentic AI for End-to-End EHR Research: Sequential Antibody-Drug Conjugate Pathways in Breast Cancer

- **Authors:** Loaiza-Bonilla, A., Colovos, C., Kim, D., Grichnik, J. M., Singh, K., Tarantino, P.
- **Published:** 2026-10-14
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.10.13.26365479](https://doi.org/10.64898/2026.10.13.26365479)

- **Categories:** oncology


> Summary unavailable.


<details>
<summary>Abstract</summary>

PURPOSETo demonstrate an end-to-end research workflow combining a large electronic health record (EHR) resource and a multi-agent artificial intelligence (AI) system governed by Human-Guided Orchestration (HGO), using sequential sacituzumab govitecan (SG) and trastuzumab deruxtecan (T-DXd) orders in breast cancer as the clinical use case.

METHODSA June 2026 EHR release contained 4.95 million patients, including 156,051 with breast cancer codes. Muse Spark supported cohort construction, executable statistical analysis, data-quality checks, literature retrieval, and reporting executed through Symbiotic Agent Teaming (SAT) under investigator direction. The main clinical measure was the second-drug record span, from first to last order. Analyses were descriptive and unadjusted; orders did not confirm administration or progression.

RESULTSThe workflow identified 106 patients: 73 had T-DXd ordered first and 33 had SG ordered first. Median second-drug spans were 63 days (interquartile range [IQR], 29-116) for SG after T-DXd and 49 days (IQR, 21-126) for T-DXd after SG; the median difference was -14 days (95% bootstrap CI, -41 to 21; distributional P = 0.42). Reported outputs additionally included cohort definitions, aggregate analyses, evidence context, figures, and a preliminary draft manuscript.

CONCLUSIONThis study provides a concrete model for integrating large EHR resources, agentic AI, and human expertise across the research cycle. The ADC use case illustrates how computational execution and Expert-in-the-Loop (EITL) adjudication can produce interpretable research outputs and refine their scientific meaning, providing a foundation for extending and evaluating this approach across clinical questions.

Context SummaryO_ST_ABSKey ObjectiveC_ST_ABSHow can clinical expertise and agentic AI be integrated from research-question formulation through EHR analysis and scientific reporting, using sequential SG and T-DXd orders as a clinical use case?

Knowledge GeneratedMuse Spark supported cohort construction, executable analysis, data-quality assessment, evidence retrieval, and reporting; investigators directed the work and adjudicated revisions. The resulting 106-patient cohort described recorded ADC path-ways and the review determined record-span timelines.

</details>


---



## Arxiv (164 papers)


### 1. AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery

- **Authors:** Shicheng Liu, Krista Opsahl-Ong, Andrew Drozdov, Julian Killingback, Arnav Singhvi, Ronak Pradeep, Michael Bendersky, James C. Dickerson, Monica S. Lam
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23845v1](http://arxiv.org/abs/2610.23845v1)
- **PDF:** [https://arxiv.org/pdf/2610.23845v1](https://arxiv.org/pdf/2610.23845v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reproducible and analytically robust research findings are essential to scientific progress, but evaluating these properties typically requires costly manual effort. We investigate whether LLM agents can help automate reproduction and robustness analysis, using a medical case study grounded in the Surveillance, Epidemiology, and End Results (SEER) database, a widely used U.S. cancer registry underlying tens of thousands of published studies. First, we introduce SEER-Repro, a benchmark of 20 published SEER-based papers together with the data and resources required to reproduce their findings. Second, we create an AI agent that successfully reproduces 77.4% of 2,190 atomic claims, while providing executable baselines for further analysis. Third, we develop an agentic analysis pipeline to test the robustness of the medical findings by identifying analytical choices underlying each finding, proposing defensible alternatives, and rerunning the analysis to determine whether those choices affect the conclusion. Across published papers in SEER-Repro, our pipeline identifies potentially consequential analytical choices in 9.5% of fully reproduced findings and flags them for expert review. These results show how LLM agents can support scientific review by reproducing findings, systematically testing their robustness, and directing expert attention toward potentially consequential analytical choices.

</details>


### 2. DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses

- **Authors:** Jianyuan Zhong, Chenwei Wu, Zhaochen Yu, Xixian Jiang, Xuewei Li, Hao Xiao, Xilin Dai, Junyang Wang, Jiaru Zou, Zhiqing Cui, Boyuan Zheng, Jing Xiong, Zhen Zhang, Qiang Gao, Michael Morley, Luis Nakayama, Qiang Xu, Liyue Shen, Tao Gui, Leo Anthony Celi, James Zou, Zhenfei Yin, Yingcheng Wu, Ling Yang
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23839v1](http://arxiv.org/abs/2610.23839v1)
- **PDF:** [https://arxiv.org/pdf/2610.23839v1](https://arxiv.org/pdf/2610.23839v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scientific discovery requires developing worthwhile hypotheses into practical investigations, yet learning from this evolving research process remains challenging. We introduce an operational definition of valuable and testable research hypotheses: evidence-grounded claims about consequential uncertainties, coupled with feasible investigations, explicit decision criteria, and alternative explanations. Our DiscoveryRSI framework develops hypothesis trees through multi-agent evolutionary search, compiles selected investigations into executable Harbor tasks, and recursively learns through three mechanisms: hypothesis credit optimization attributes scientific assessments to documented research contributions; harness replay identifies productive strategies and recurring failures to refine research workflows; and rediscovery applies accepted improvements to new investigations, generating further experience for subsequent learning. We also introduce DFM-Bench, which provides comprehensive assessment of hypothesis quality and cumulative research progress at the levels of hypotheses, revisions, development paths and research runs. Across four life-science domains, automated evaluation shows that hypothesis quality rises from 4.86 for the base model to 5.39 after two rounds of self-improvement, with the large gains in falsifiability and data resolvability. We further validate hypothesis quality through expert review, comparing our DiscoveryRSI-27B with other research agents. Preliminary human assessments show that DiscoveryRSI-27B scores higher than GPT-6 Luna on hypothesis importance and whether claims are plausible and evidence-bounded. DiscoveryRSI-27B achieved a 6.3% rate of hypothesis correspondence with research published after the model cutoff, largely outperform GPT-6 with 2.5% and Claude Opus 5 with 2.3%, while delivering greater human-rated improvement along research paths.

</details>


### 3. Self-Building Labs

- **Authors:** Jiaru Bai, Yuchi Zhao, Han Hao, Miroslav Bogdanovic, Yang Cao, Varinia Bernales, Alán Aspuru-Guzik
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23826v1](http://arxiv.org/abs/2610.23826v1)
- **PDF:** [https://arxiv.org/pdf/2610.23826v1](https://arxiv.org/pdf/2610.23826v1)
- **Categories:** cs.AI, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-driving laboratories (SDLs) accelerate scientific discovery by automating experimental execution and optimization. AI agents can increasingly propose new experiments, but existing SDLs can only run the procedures they were built for. Adapting them to a new experiment still takes extensive manual engineering, which makes laboratory flexibility the bottleneck for scaling discovery. We introduce the self-building laboratory (SBL), which designs, configures, and operates its own laboratory setup given a high-level scientific goal. SBL starts from whatever already exists, from an empty room to a working SDL, and builds the missing capabilities: the lab layout, its digital twin, robot skills, and experimental workflows. We demonstrate the system working across different robots and setups, scaling from a single workstation to laboratories with several robots working together. We validate SBL's end-to-end capabilities through a real-world quantum-dot synthesis experiment. By shifting the role of human researchers from manually configuring and programming device automation to specifying scientific objectives, SBL makes scientific automation more accessible, flexible, and scalable. Project website: https://self-building-labs.github.io/

</details>


### 4. CocoRNA: Collective RNA Design with Cooperative Multi-agent Reinforcement Learning

- **Authors:** Tianmeng Hu, Biao Luo, Ke Li
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23820v1](http://arxiv.org/abs/2610.23820v1)
- **PDF:** [https://arxiv.org/pdf/2610.23820v1](https://arxiv.org/pdf/2610.23820v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Designing RNA sequences that reliably fold into specific secondary structures is essential for understanding their biological functions but remains a challenging computational problem. We propose CocoRNA, a cooperative multi-agent reinforcement learning framework for RNA inverse design. CocoRNA simplifies the design task by decomposing it into smaller sub-problems, each solved collaboratively by multiple agents. This approach reduces the complexity of the problem and improves the exploration of design policies. During training, a centralized critic uses global structural information to guide the agents, enabling them to jointly optimize their design strategies. As a result, CocoRNA learns high-quality RNA design policies that generalize effectively to unseen structures without additional training. Experiments on the Rfam dataset demonstrate that CocoRNA substantially outperforms state-of-the-art methods in both success rate and design speed. Further experiments on other biological sequence design tasks highlight the effectiveness and broad potential of CocoRNA for complex design tasks.

</details>


### 5. DLite: History-free Speculative Decoding for Agentic AI

- **Authors:** Jiaming Xu, Hanzhen Wang, Tianlang Zhao, Jiewen Xiao, Chengze Yuan, Jiayi Pan, Yongkang Zhou, Jiancai Ye, Yu Wang, Guohao Dai
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23787v1](http://arxiv.org/abs/2610.23787v1)
- **PDF:** [https://arxiv.org/pdf/2610.23787v1](https://arxiv.org/pdf/2610.23787v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Speculative decoding has become a mainstream technique for accelerating large language model (LLM) inference by using a lightweight draft model to generate candidate tokens that are subsequently verified by the target model. However, agentic workloads introduce long and continuously evolving contexts and frequent multi-turn interactions. Under such workloads, we observe that existing draft models suffer from up to an 80% degradation in acceptance length, while maintaining their historical KV cache introduces substantial system overhead. In this paper, we identify the growing historical context as a common source of both problems and introduce DLite, a history-free speculative decoding framework for agentic AI. DLite directly reuses contextual hidden states from the target model and performs local speculative prediction without explicitly maintaining the historical context, transforming an increasingly complex modeling problem into local simple prediction problem. A lightweight sequential head further restores intra-block causal dependencies with low overhead. To effectively train this heterogeneous history-free architecture, we introduce a tailored two-stage training strategy. Experiments on general-purpose, long-context and agentic workloads show that DLite achieves 2-6 acceptance length and outperforms the state-of-the-art speculative decoding method, DSpark, up to 70%.

</details>


### 6. On the possibilities and limitations of LLM-based multi-agent systems for multi-criteria decision-making in healthcare operations management

- **Authors:** Marco Boresta, Tommaso Giovannelli, Sepehr Namirad, Giulia Riccardi
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23673v1](http://arxiv.org/abs/2610.23673v1)
- **PDF:** [https://arxiv.org/pdf/2610.23673v1](https://arxiv.org/pdf/2610.23673v1)
- **Categories:** math.OC, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-criteria models for healthcare operations need weights that express how stakeholders trade off patient waiting time, provider workload, and operating cost, but these weights are difficult to quantify. Teams of large language model (LLM) agents, each prompted to represent a stakeholder, have been used to supply them. We propose a framework for assessing the reliability of LLM-generated preferences as inputs to multi-objective optimization and quantifying how their uncertainty affects decisions. We study explicit preferences by asking agents to rate the importance of the criteria in an outpatient appointment scheduling problem, and implicit preferences by inferring trade-offs from the agents' pairwise choices between emergency department configurations. The computational experiments show that the explicit preferences respond to the clinic's operating conditions and differ across roles, but deliberation among the agents can erase these differences, whereas simple averaging preserves them. The pairwise choices used to reveal the agents' implicit preferences depend largely on which option is presented first, and we find limited evidence that a statistical model using contextual information alongside presentation order predicts the agents' choices on new comparison pairs better than a model using presentation order alone. We then formulate robust weighted-sum optimization models to account for preference uncertainty. In most cases, these models select different schedules or configurations from those obtained using average preference weights. These results indicate that LLM-generated preferences need an audit of this kind before they are used as optimization weights in healthcare decision support.

</details>


### 7. SIT-Eval: Situation-Based Interactive Turn-by-Turn Evaluation of Conversational Agents

- **Authors:** Ravil Mussabayev, Saveliy Zavertyaev, Dmitriy Parpulov, Andrey Savchenko
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23612v1](http://arxiv.org/abs/2610.23612v1)
- **PDF:** [https://arxiv.org/pdf/2610.23612v1](https://arxiv.org/pdf/2610.23612v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid proliferation of conversational AI agents necessitates evaluation methods that assess performance across diverse dialogue scenarios, utilizing multiple situational criteria, as appropriate behavior depends on context and encompasses various aspects. Existing dialogue benchmarks typically use static natural conversations, which underrepresent rare situations---a critical safety gap, as low-probability events become frequent failures at production scale. However, limited sample sizes force a choice: either maintain natural dialogues for realism or turn to adaptive situation sampling for comprehensive yet statistically reliable coverage. We introduce SIT-Eval, an adjustable framework for evaluating situation-based conversational agents. We formalize an agent's desired behavior as situational rules: if situation is P, follow rules Q. At each conversation turn, an LLM-interlocutor enacts a uniformly sampled situation. A context-aware LLM-judge leverages all conditionally applicable rules as criteria to evaluate the agent's reply for that situation. The judge is validated using human-verified synthetic golden dialogues. Benchmarking 8 LLMs on 1292 conversation turns reveals failure modes hidden by aggregate metrics: models with similar overall scores vary widely in their adherence to individual rules. All models struggle most with ambiguity clarification and Socratic questioning.

</details>


### 8. RL-Guided Temporal Localization for Dual-Channel Retrieval in Long-Horizon Agent Memory

- **Authors:** Dabin Sheng, Zhe Wu, Jinming Zhao, Junliang Xing, Yuanchun Shi
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23598v1](http://arxiv.org/abs/2610.23598v1)
- **PDF:** [https://arxiv.org/pdf/2610.23598v1](https://arxiv.org/pdf/2610.23598v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Time-aware retrieval is crucial for long-horizon LLM agents to effectively leverage ever-growing long-term memory. Existing methods focus on lexical or semantic similarity, leading to target memories being crowded out by temporally mismatched yet semantically similar candidates. Even time-aware approaches inject temporal cues only during memory organization or answer generation, overlooking temporal constraints at the retrieval stage, where candidate selection occurs - the root cause of the displacement. Inspired by the temporal contiguity effect in human episodic memory, we propose TIDER (Temporal Interval-driven Dual-channel Evidence Retrieval), a time-aware agentic retrieval framework. Central to TIDER is a reinforcement learning (RL)-trained temporal interval locator that infers the temporal windows in which the evidence lies. RL optimizes window localization as a discrete, non-differentiable retrieval decision, using composite rewards to convert sparse answer supervision into fine-grained retrieval feedback. These temporal windows first define the temporal retrieval channel; the retrieved candidates are then merged with results from the semantic channel and reranked by proximity to the windows. This temporal grounding enables TIDER to retrieve temporally aligned evidence that would otherwise be drowned out by the volume of semantically similar yet temporally mismatched memories. With a lightweight 1.7B locator, TIDER achieves state-of-the-art accuracy on both long-horizon memory benchmarks - 61.52% on LifeBench (+8.82%) and 78.96% on LoCoMo (+3.66%) - which indicates that temporal cues are crucial for pinpointing target evidence amid a vast pool of semantically similar historical events in long-term daily-life memory.

</details>


### 9. Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents

- **Authors:** Mingze Yin, Xiaohan Wang, Dian Li, Longfei Luo, Jiahong Yan, Yiheng Zhu, Chang-Yu Hsieh
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23574v1](http://arxiv.org/abs/2610.23574v1)
- **PDF:** [https://arxiv.org/pdf/2610.23574v1](https://arxiv.org/pdf/2610.23574v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

While Large Language Model (LLM) agents have demonstrated remarkable capabilities across complex tasks, they predominantly operate in isolated sessions, lacking the ability to continually learn from historical interactions or adapt to user-specific environments. Existing self-evolution paradigms often indiscriminately inject raw interaction trajectories into memory or skill modules, leading to obscured behavioral patterns and compromised update controllability. Furthermore, as foundational LLM reasoning improves, the bottleneck for agentic evolution shifts from accumulating generic knowledge to effectively managing situational experience. To address this, we propose Darwin-Claw, an environment-adaptive self-evolving framework that systematically distills episodic experiences to drive the comprehensive evolution of operational skills and durable memory. Theoretically grounded in an iterative agent-actor and evolver-critic co-adaptation, Darwin-Claw introduces a Hierarchical Experience Consolidation System that extracts fine-grained error attributions and generalizes them into dynamically updated prototype vectors. This structured situational experience serves as interaction patches for context-sensitive perception and explicit optimization signals for skill refinement. Practically, Darwin-Claw is a readily deployable, automated framework compatible with mainstream agent systems without requiring manual curation. Extensive experiments on WildClawBench demonstrate that Darwin-Claw yields substantial performance improvements, establishing a controllable and stable pathway for the continual, user-centric adaptation of autonomous agents in real-world ecosystems.

</details>


### 10. S-GAP: Stealthy Graph Attack Primitives for Graph Large Language Models

- **Authors:** Wenda Li, Tongya Zheng, Shunyu Liu, Hanyang Yuan, Kaixuan Chen, Yu Wang, Yuchen Ying, Haoze Jiang, Huan Li, Gang Chen, Zujie Ren
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23465v1](http://arxiv.org/abs/2610.23465v1)
- **PDF:** [https://arxiv.org/pdf/2610.23465v1](https://arxiv.org/pdf/2610.23465v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Graph Large Language Models (GraphLLMs) enable powerful semantic understanding and reasoning over Text-Attributed Graphs (TAGs), while their semantic reasoning may exhibit vulnerabilities to perturbations in node text and graph structure under adversarial attack evaluation. Existing attacks typically construct textual and structural perturbations in separate stages guided by distinct realization intents. However, this separation results in attack-intent fragmentation, causing semantic incoherence between the two perturbation types, thereby undermining attack stealth and making them easier for GraphLLMs to identify and disregard, ultimately weakening attack effectiveness. To avoid attack-intent fragmentation, we propose the Graph Attack Primitive (GAP), an atomic semantic representation that unifies textual and structural perturbations under a coherent attack intent. By carefully calibrating the semantic composition of a GAP, we can achieve strong attack effectiveness while maintaining sufficient attack stealth. Furthermore, we introduce S-GAP (Stealthy GAP), a multi-agent framework that iteratively refines the semantic content of the GAP. The framework unifies GAP planning and realization and continuously refines this process through surrogate evaluation and textual feedback. Extensive experiments across four datasets, three GraphLLMs, and two attack settings show that S-GAP improves ASR over the strongest baselines by 7.02% on average while producing more relationally plausible perturbations, exposing critical vulnerabilities in current GraphLLMs and motivating more robust defenses.

</details>


### 11. GatewayBench: Unified Capability and Security Evaluation Platform for MCP Gateways

- **Authors:** Yitian Zheng, Zhaorun Chen, Haoyu Li, Bo Li
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23449v1](http://arxiv.org/abs/2610.23449v1)
- **PDF:** [https://arxiv.org/pdf/2610.23449v1](https://arxiv.org/pdf/2610.23449v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents have increasingly interacted with external environments by invoking tools, with Model Context Protocol (MCP) emerging as a standard interface for connecting agents to heterogeneous tools and services. As organizations deploy agents at scale, MCP gateways have become a critical middleware layer for aggregating, governing, and shaping the tool surface exposed to agents. Despite the growing importance of MCP gateways in agentic systems, no prior work has systematically studied how gateway design affects agent capability, efficiency, and security. To address this gap, we introduce GatewayBench, the first unified evaluation framework and benchmark for MCP gateways. We characterize gateway architectures into two major paradigms: flattened gateways and hierarchical gateways. GatewayBench comprises 524 tasks across six domains, together with a pool of 11,118 real-world tools from 251 authentic MCP servers. To emulate large-scale deployments, we systematically inject task-irrelevant tools sampled from this pool into each agent environment, enabling controlled evaluation as the accessible tool surface scales. Based on GatewayBench, we conduct extensive experiments across seven widely deployed MCP gateways and diverse agent configurations, covering both benign and adversarial tasks. Our results reveal substantial differences across gateway designs in task completion, tool-use efficiency, and resilience to attacks, and further demonstrate that these effects interact strongly with the underlying model and agent harness. These findings highlight the MCP gateway as a consequential yet underexplored component of the agentic AI stack. By enabling controlled evaluation of gateway architectures under realistic tool ecosystems, GatewayBench provides both practical guidance for MCP gateway design and a rigorous testbed for developing more capable, efficient, and secure agentic systems.

</details>


### 12. Robust Function Calling for LLM Agents Under Interface Drift

- **Authors:** Aniruddha Chattopadhyay, Kanishka Halder, Partha Sarathi Roy
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23342v1](http://arxiv.org/abs/2610.23342v1)
- **PDF:** [https://arxiv.org/pdf/2610.23342v1](https://arxiv.org/pdf/2610.23342v1)
- **Categories:** cs.AI, cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-augmented language-model agents rely on interface text: tool descriptions, argument schemas, and the candidate tool list shown at inference time. These interfaces often change after deployment even when the underlying tool semantics remain fixed, creating a practical reliability problem for function-calling systems. We study this failure mode as interface drift and evaluate whether a lightweight, training-free repair layer can recover robustness without retraining the base model. Our method, SchemaShield-Lite, combines schema validation, candidate-set retry for missing tool names, and one-shot constrained repair. On Qwen3.5-9B, it raises DICE-300 accuracy from 0.717 to 0.813 and BFCL-200 accuracy from 0.580 to 0.805, recovering 19/22 and 33/45 drift-induced failures with no observed repair harms. Naive retry does not explain the gains. Ablations show that candidate-set drift, especially distractor tools, accounts for most observed damage, while description and schema edits alone are less harmful. The results position validation-and-repair as a practical robustness layer for deployed LLM-agent tool use.

</details>


### 13. AgentOnto: Ontology-Guided LLM Agents for Enterprise Data Analytics

- **Authors:** Dayan Pan, Bincheng Zuo, Xiaojian Wang, Daogang Zhang, Jingyuan Wang
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23317v1](http://arxiv.org/abs/2610.23317v1)
- **PDF:** [https://arxiv.org/pdf/2610.23317v1](https://arxiv.org/pdf/2610.23317v1)
- **Categories:** cs.AI, cs.DB


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise data analysis requires agents to connect analytical requests with knowledge distributed across databases, business documents, and existing example tasks. Without an explicit representation of this knowledge, an agent may produce incorrect analytical results and cannot reliably incorporate feedback. We present AgentOnto, an ontology-guided LLM agent for enterprise data analytics. AgentOnto organizes heterogeneous enterprise knowledge into an ontology that directly guides analysis and incorporates confirmed feedback. Iterative Ontology Preparation further improves the ontology through self-generated analysis tasks. We evaluate AgentOnto on two public data sources. AgentOnto substantially outperforms representative methods, while module-level evaluations confirm the effectiveness of ontology construction, analysis, and updating. A real-world deployment further demonstrates its practical value in enterprise analytics. These results demonstrate that explicitly constructing, using, and updating enterprise knowledge supports reliable and adaptable data analysis.

</details>


### 14. Annotrace: A Workbench for Step-Level Annotation of Agent Traces

- **Authors:** Arun Josephraj Arokiaraj, Chenyi Huang, Sahan Bulathwela, Zekun Wu, Bin Wu
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23284v1](http://arxiv.org/abs/2610.23284v1)
- **PDF:** [https://arxiv.org/pdf/2610.23284v1](https://arxiv.org/pdf/2610.23284v1)
- **Categories:** cs.AI, cs.CL, cs.HC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Every study of why LLM agents fail begins by labelling traces by hand, and every such study builds its own throwaway tool. Observability platforms record agent traces but offer no structured labelling; annotation tools label text but have no notion of a step, a delegation or a tool call, leaving it unclear what the smallest unit of execution to label should be. Annotrace reads six trace formats, including OpenTelemetry GenAI, LangSmith and Langfuse, and turns each run into an ordered, nested list of steps. The annotator writes their own labelling codebook; a frontier model proposes a starting set from a sample of their own traces, answers first, and is asked exactly the questions the human is asked, making annotation a joint human-AI process. Annotrace measures agreement between any two annotators, human or AI. On a multi-agent question-answering corpus it reproduces a previous manual effort's 235 annotation units exactly, and two models labelling the same traces agree 91% of the time at $κ= 0.82$.

</details>


### 15. Beyond Marginal Influence: Interaction-Aware Memory Selection for LLM Agents

- **Authors:** BHVSP Subrahmanyam, Neeraj Choudhary
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23266v1](http://arxiv.org/abs/2610.23266v1)
- **PDF:** [https://arxiv.org/pdf/2610.23266v1](https://arxiv.org/pdf/2610.23266v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-agent memory selection often uses retrieval rankings based on record relevance or individual influence. Such rankings cannot identify sufficient subsets under redundant or jointly necessary evidence. We study per-decision memory sufficiency: selecting a small subset that preserves full-memory behavior. To separate search error from model error, we introduce JointCoreBench, a benchmark with nine interaction families, six workflow domains, natural-language decisions, and exact sufficient-set oracles, and JointCore, a relevance cost-ordered group-deletion baseline that tests blocks before individual records. On 6,912 exact conditions, cost-ordered JointCore recovers a minimum-cost sufficient set in 100.0% of cases, reduces subset evaluations from 30.00 to 11.13 (62.9%), and achieves 87.8% active-memory savings. Across four 12B-70B model families and 432 tasks per model, its unweighted mean is 10.28 versus 16.00 model queries and 50.6% versus 43.1% minimum-cost recovery relative to cost aware singleton deletion. Both methods preserve full-memory behavior under the deterministic primary interface. Tests with physical deletion, UNKNOWN masks, PENDING sentinels, counterfactual values, and alternative labels identify interface dependent behavior. JointCore is an efficient benchmark baseline; the study does not establish deployment-ready memory compression.

</details>


### 16. Beyond Reward Scoring: Online Multi-Agent Preference Learning for Multimodal Response Generation

- **Authors:** Ziyun Zou, Jiwoo Hong, Yifan Lu, Shao Tang, Weiyi Wu, Aman Gupta, Jin Tian, Imran Razzak
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23256v1](http://arxiv.org/abs/2610.23256v1)
- **PDF:** [https://arxiv.org/pdf/2610.23256v1](https://arxiv.org/pdf/2610.23256v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal preference alignment often follows a score-based RLHF pipeline: a reward model is first trained to learn human preferences, then used to score on-policy responses and optimize the response model's generation. This turns preference supervision into a scalar signal for generation: a model may learn to produce answers with higher preference scores, but is rarely trained explicitly to learn the reasons underlying human preferences. We therefore ask whether making preference understanding an internal capability of the response model can improve its generation. To investigate this question, we propose \textbf{PrefMind}, an online dual-agent reinforcement learning framework with two trainable agents: a response Generator and a preference Critic. Given a pair of candidate responses, the agents analyze and discuss which response better aligns with human preference. Human labels supervise their judgments and corrections. For pairs on which both the Generator and revised Critic correctly identify the human-preferred response, the Generator produces an improved answer, and the Critic compares it against the original preferred response to provide a generation reward. Both agents are jointly updated from interactions sampled with their current policies. Through this process, \textbf{PrefMind} trains the Generator to understand human preferences via explicit judgment and correction, and to translate this understanding into better responses. Experiments across three model scales show improvements in both standalone preference judgment and downstream response generation.

</details>


### 17. Preventing Data Hallucinations in Agentic AI for Optical Network Troubleshooting

- **Authors:** Jeremias Dötterl, Martin Kuipers
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23252v1](http://arxiv.org/abs/2610.23252v1)
- **PDF:** [https://arxiv.org/pdf/2610.23252v1](https://arxiv.org/pdf/2610.23252v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

An agentic AI system for automated troubleshooting in optical communication networks is demonstrated that integrates data references into the agent architecture to prevent data hallucinations, improving the interpretability and trustworthiness of root-cause identification and reasoning.

</details>


### 18. Think More or Read More? A Token-Budget Theory of Reasoning with Shared Context

- **Authors:** Manh Nguyen, Sunil Gupta, Hung Le
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23246v1](http://arxiv.org/abs/2610.23246v1)
- **PDF:** [https://arxiv.org/pdf/2610.23246v1](https://arxiv.org/pdf/2610.23246v1)
- **Categories:** cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reasoning systems increasingly improve answers by incorporating additional context into the model's input, from multi-agent debate, where agents read their peers' responses, to self-refinement, where a model revisits its own drafts. In these systems, communication consumes context as one agent's output becomes another's input. We study the regime where token reading and generation draw on one fixed token window, so every token spent reading is a token that cannot be spent reasoning. We develop a \textbf{token-budget theory} that formalizes this trade-off, modeling accuracy as a function of the reasoning budget remaining after reading and aggregating votes with a Condorcet jury model that permits correlated errors. For multi-agent debate, the theory gives a closed-form prediction for the optimal number of agents. This quantity is estimated from single-agent measurements, allowing the optimal group size to be determined without running debate, and the same accounting extends to a heterogeneous set of different models. We empirically verify our theory and show that, at the predicted group size, our method outperforms strong baselines under the tightest calibration spend, where debate-calibrated rules can afford only one or two questions. Self-refinement obeys the same accounting, with its own draft in place of a peer message. The theory further predicts that communication pays only when the gain in the accuracy ceiling exceeds the reasoning room spent on reading, with this condition tightening as the window shrinks. Across five open models and four reasoning tasks, self-consistency matches or beats deployed debate at $93$\% of $980$ matched window-and-group-size settings, with the gap being largest under tight windows and nearly disappearing at a loose one, consistent with the theory. Under a shared window, how much room a model has left to \textit{think matters more than what it reads}.

</details>


### 19. MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation

- **Authors:** Yuhan Sun, Jiaxin Zhao, Yongdong Luo, Yibo Hu, Meiguang Jin, Junfeng Ma, Weixun Wang, Weihang Pan, Zhongan Bi
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23234v1](http://arxiv.org/abs/2610.23234v1)
- **PDF:** [https://arxiv.org/pdf/2610.23234v1](https://arxiv.org/pdf/2610.23234v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

In a hierarchical multi-agent system, a Leader assigns tasks and subagents carry them out. Jointly training the Leader and the subagents is difficult because a final answer gives only indirect feedback to the subagents. An LLM judge can score the performance of the subagents, but these scores depend on the judge's own assessment of the quality of subagents' responses. We present MultiAgent-OPD, which combines on-policy distillation with reinforcement learning to jointly train a shared-parameter Leader-Searcher-Answerer team end to end. We first train a Teacher in a Searcher-Answerer workflow using answer correctness. During team training, the frozen Teacher scores student-generated search and summary tokens to provide local process supervision for the Searchers, while the Leader learns from team success and the Answerer from candidate correctness. Across seven datasets, the trained system reaches 38.68% macro avg@4, exceeding Prompted Critic by 4.06 percentage points and C-MAS + RL, the trained cascaded multiagent system, by 2.61 percentage points. The team also solves more questions within four attempts.

</details>


### 20. Not All Test-Time Compute Is Evidence: Model-Specific Bias in LLM Reasoning

- **Authors:** Ming Shen, Tianjun Yao
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23213v1](http://arxiv.org/abs/2610.23213v1)
- **PDF:** [https://arxiv.org/pdf/2610.23213v1](https://arxiv.org/pdf/2610.23213v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Test-time scaling methods implicitly assume that additional computation from the same model provides independent evidence. We show that this assumption fails within a single reasoning model: errors are correlated across repeated samples, across reasoning depth, and in the model's own self-evaluation, so more compute from the same model is not more evidence. We introduce DIA (Disagreement-triggered Independent Arbitration), which treats disagreement between an intermediate-stage and the final-stage prediction as a per-question signal of reasoning instability and resolves it by asking a small panel of heterogeneous models to solve the question independently, without seeing either candidate, and aggregating their answers directly. Across seven benchmarks and two base models, DIA outperforms full chain-of-thought in 12 of 14 settings, including a 7.00% gain on MuSiQue, while activating on only $\sim 17\%$ of examples and using up to 47.2% fewer tokens than a multi-agent baseline. Ablations show that both independent solving and solver heterogeneity are necessary for these gains.

</details>


### 21. MAS-Bai: Linguistically Informed Adaptive Multi-Agent Translation for Bowen-Script Bai

- **Authors:** Jingting Zheng, Hong Ren, Yuehan Cui, Shaolin Zhu, Deyi Xiong
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23205v1](http://arxiv.org/abs/2610.23205v1)
- **PDF:** [https://arxiv.org/pdf/2610.23205v1](https://arxiv.org/pdf/2610.23205v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) remain unreliable for extremely low-resource languages whose writing systems conflict with high-resource pretraining priors. We study Bai-Chinese translation in the Bowen script, where Chinese characters are frequently borrowed phonetically rather than semantically, causing severe literal-translation hallucinations. We propose MAS-Bai, a linguistically informed adaptive multi-agent framework for Bowen-script Bai-Chinese translation. MAS-Bai routes each input through either a lightweight retrieval-translation path or a deeper philological path with etymological and syntactic agents, and uses cycle-consistency with a lightweight reverse translator as an inference-time reliability signal. We construct a 6,536-sentence Bai-Chinese corpus and evaluate on a 1,536-sentence test set. MAS-Bai achieves 16.23 BLEU and 62.15 COMET, improving over Standard RAG by 8.11 BLEU and 6.85 COMET. Forward LoRA, expert ablations and controlled routing experiments distinguish the roles of supervised adaptation, Bai-specific expertise and conditional routing. The largest gains occur on Bowen phonetic loans and divergent Bai word order, while human evaluation and reverse-verifier analyses support the automatic results.

</details>


### 22. OfficeTown: Generative Organizations for Evolving Agent Intelligence

- **Authors:** Hongchen Wei, Daohong Ying, Zhi Hong, Aidan Wu, Bei Liu, Ruichun Ma, Yifan Yang, Qi Dai, Kai Qiu, Rui Xu, Dongdong Chen, Zhenzhong Chen, Chong Luo
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23194v1](http://arxiv.org/abs/2610.23194v1)
- **PDF:** [https://arxiv.org/pdf/2610.23194v1](https://arxiv.org/pdf/2610.23194v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly use files and software tools to produce professional deliverables. Such work draws on materials, decisions, and feedback accumulated across assignments. We introduce OfficeTown, a generative simulation framework for professional organizations in which tasks and their context arise from continuing organizational work. From a natural-language description of an organization's purpose and activities, OfficeTown initializes an organization whose members coordinate work, delegate bounded assignments to assistant agents, and review their deliverables. Artifacts, decisions, and unresolved matters persist and shape subsequent work, while responsibilities and permissions determine what each member can see and do. We curate work requests, their context, and review feedback into executable resources for evaluation and learning. We construct OfficeTown Bench with 406 tasks and 4,836 evaluation criteria from 23 simulated organizations across eight professional domains, incorporating domain-expert feedback. Frontier-model evaluations reveal substantial remaining headroom. Supervised fine-tuning and on-policy distillation on OfficeTown data substantially improve Qwen3.5-9B on external professional-work benchmarks, including GDPval. Supplementary evaluations show that the principal--assistant harness achieves higher scores than the single- and multi-agent baselines tested. These results highlight the value of organizational simulation in generating work-grounded data and environments for the continued development of generalist agents.

</details>


### 23. AMEND: Constraint-Guided Multi-Agent Text Detoxification with Isolated Critics

- **Authors:** Tianyu Wang
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23183v1](http://arxiv.org/abs/2610.23183v1)
- **PDF:** [https://arxiv.org/pdf/2610.23183v1](https://arxiv.org/pdf/2610.23183v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Text detoxification requires balancing toxicity removal, semantic preservation, and fluency. Existing methods typically optimize an unconstrained scalar objective---enabling safety scores to mask semantic loss---or rely on open-ended iterative debate prone to semantic drift and high computational cost. We propose AMEND, an inference-time framework that decouples detoxification into role-conditioned proposal generation, isolated multidimensional criticism, and constraint-first selection. AMEND evaluates diverse candidates with role-blind critics and enforces strict semantic and fluency feasibility before ranking by utility. To maximize efficiency, AMEND Lite restricts subsequent search to at most one targeted repair round only when residual toxic spans remain. On ParaDetox, one-round selection over diverse roles improves the joint evaluation metric by $+0.0508$ over the best single role. On a frozen confirmation test set, AMEND Lite achieves a joint score of $0.6597 \pm 0.0062$, outperforming unconstrained multi-round loops by $+0.0489$ ($p < 0.05$) while reducing inference requests by 28.4%.

</details>


### 24. QuAD: Quantitative Assessment via Distribution-Alignment for Qualitative Data Quality Enabled by a Content-Aware Multi-Agent System

- **Authors:** Wenshuo Zhang, Leixian Shen, Qiqi Zhou, Shuchang Xu, Feiyang Hao, Huamin Qu, Haobo Li, Zhao Chen, Lin-Ping Yuan
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23153v1](http://arxiv.org/abs/2610.23153v1)
- **PDF:** [https://arxiv.org/pdf/2610.23153v1](https://arxiv.org/pdf/2610.23153v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Assessing whether qualitative responses collected from semi-structured questions are ready for a particular analysis goal is a persistent challenge. Manual qualitative analysis is interpretive and labor-intensive, while existing automated methods often lack a dataset-level perspective for deciding whether a response set supports a researcher-selected analytical lens. We introduce QuAD, a framework for quantitative pre-analysis assessment of qualitative response datasets. QuAD compares a reconstructed intrinsic cluster distribution reconstructed from responses with an extrinsic, researcher-defined analytical lens derived from metadata. QuAD is structured into a four-quadrant assessment whose metrics are read jointly, from lens-level relations to within-cluster variation, to provide fitness-for-purpose signals for revealing general patterns and unique insights. Because this assessment relies on lens-conditioned inter-response dissimilarity, we propose a content-aware multi-agent system with two-stage instruction generation and adaptive anchors to improve scoring consistency. We validate QuAD through controlled experiments on synthetic data, including robustness and baseline comparisons, and a real-world social survey case study. The case study shows how QuAD quantitatively assesses whether a selected analysis axis is promising and also surfaces representative or unusual responses for human interpretation.

</details>


### 25. Disentangling Language Effects on Tool Admission and Post-Retrieval Safety

- **Authors:** Aditya Nawal, Manit Baser, Mohan Gurusamy
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23093v1](http://arxiv.org/abs/2610.23093v1)
- **PDF:** [https://arxiv.org/pdf/2610.23093v1](https://arxiv.org/pdf/2610.23093v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly use retrieval tools across languages, yet their safety evaluation remains English-centric. It remains unclear whether language affects tool admission, post-retrieval generation, or both. We independently vary request, retrieved-page, and required response languages in a controlled URL-retrieval setting across ten models and seven languages. We identify Safety Loss through Interlingual Processing (SLIP). Non-English harmful requests increase mean tool admission from 46.9% to 67.4%, with a positive mean change in every model. This pattern also persists in an autonomous retrieval setup across all four models tested in this setting. Requiring answers in the page language increases pooled harmfulness on matched tool calls from 50.3% to 57.4% across four closed-weight models, mainly in Chinese and Hindi. Translating pages alone produces no consistent harm increase in eight models with comparable inference settings. Automated audits show that a non-harmful response may be a genuine safety refusal, a deflection citing language difficulties, or an unusable answer. Harmfulness labels alone cannot distinguish these outcomes. Multilingual safety evaluations should therefore measure tool admission and response harmfulness separately and distinguish refusal from capability failure.

</details>


### 26. Towards High Semantic Fidelity: Hyperdimensional Symbolic Messages in Multi-Agent Communication

- **Authors:** Shoucheng Song, Chang Yao, Hao Wu, Youfang Lin, Sheng Han, Kai Lv
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23092v1](http://arxiv.org/abs/2610.23092v1)
- **PDF:** [https://arxiv.org/pdf/2610.23092v1](https://arxiv.org/pdf/2610.23092v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Semantic fidelity is essential for multi-agent communication under non-ideal channels, comprising transmission fidelity and conversion fidelity. Yet existing numerical and neural message formats cannot simultaneously achieve both. To address this, we propose a novel message format-\textbf{H}yperdimensional \textbf{S}ymbolic \textbf{M}essages (HSM) and its corresponding communication framework \textbf{Herm}. For transmission fidelity, Herm suppresses semantic entanglement via an entity-attribute-value structured encoding pipeline. For conversion fidelity, Herm first leverages a receiver-centric ego-binding mechanism to align semantics. Then, a similarity-aware dual-branch fusion module is proposed to prevent critical semantic dilution. To realize explicit message-semantic conversion, we devise an iterative decoding scheme via algebraic inverse operations. Experiments exhibit that Herm outperforms baselines across various noisy scenarios while maintaining superior structural readability.

</details>


### 27. Cryptographically Secure Agent-to-Agent Communication in Multi-Agent Systems

- **Authors:** Karol Budzyn, Adrian Brodzik, Mateusz Szczepkowski
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23078v1](http://arxiv.org/abs/2610.23078v1)
- **PDF:** [https://arxiv.org/pdf/2610.23078v1](https://arxiv.org/pdf/2610.23078v1)
- **Categories:** cs.CR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) comprise AI agents that collaborate or compete to perform complex, distributed tasks. Their dynamic interactions create opportunities for threat actors to target and impersonate other agents, intercept messages, inject malicious prompts, and exfiltrate sensitive data while simultaneously complicating the detection of anomalous behavior through conventional monitoring. This paper surveys threats and cryptographic challenges in agent-to-agent communication and presents a zero-trust architecture integrating identity, transport security, message integrity, and monitoring. The architecture establishes agent identities via decentralized identifiers and task-scoped verifiable credentials backed by a permissioned ledger, enforcing least-privilege authorization. For transport security, it provides mutually authenticated, crypto-agile TLS with hybrid post-quantum key establishment, and evaluates KEMTLS with pre-distributed public keys to reduce handshake overhead. Signed CBOR envelopes preserve payload integrity across multi-hop exchanges, while zero-knowledge proofs verify declared task constraints without exposing underlying inputs. Context-aware monitoring of inter-agent messages, tool activity, and execution telemetry informs the setting of risk-based trust thresholds and supports the detection of behavioral anomalies. Together, these mechanisms provide an integrated framework for securing and auditing agent communication, with implications for other agentic protocols and prospective 6G semantic communication.

</details>


### 28. Before Retrieval Begins: Safety and Tool-Use Decisions in LLM Agents

- **Authors:** Aditya Nawal, Manit Baser, Mohan Gurusamy
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23071v1](http://arxiv.org/abs/2610.23071v1)
- **PDF:** [https://arxiv.org/pdf/2610.23071v1](https://arxiv.org/pdf/2610.23071v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models increasingly act as agents that call external tools, yet most tool-safety research examines only what follows a tool call. The prior decision of whether to call the tool remains largely unexamined and can influence downstream safety. Across the seven open-weight models, the unweighted model-average harm rate after admitted harmful requests is 74.5%. To identify what governs this decision, we apply a factorial intervention to the input request. Within our generated construction, neutralizing the requested-operation component produces the largest admission contrast (19 pp). A linear direction estimated from this contrast influences held-out admission in four of seven models; effects on operation-neutralized requests in some models show that it is not an operation-specific mechanism. We then test whether written refusal is behaviorally and representationally coupled to the same decision. Written refusal accompanies 33.6% of admitted harmful calls. Plain-text refusal training reduces unsafe admission in models that retain benign tool use, showing that response-level safety training can transfer to the call decision. Together, these results establish a partial, model-dependent relation between written refusal and tool admission. They motivate direct evaluation and supervision of tool admission rather than treating text refusal as its proxy.

</details>


### 29. ParetoChat: An LLM-Based Interface for Interactive Multi-Objective Optimization

- **Authors:** Gokhan Ceyhan
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23062v1](http://arxiv.org/abs/2610.23062v1)
- **PDF:** [https://arxiv.org/pdf/2610.23062v1](https://arxiv.org/pdf/2610.23062v1)
- **Categories:** cs.CL, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-objective optimization models are often deployed in settings where decision makers (DMs) must balance some conflicting criteria. In practice, however, stakeholders must translate their qualitative preferences between different criteria into numerical weights, priorities, or reference points required by optimization methods, which can be difficult to specify and interpret. This paper proposes \emph{ParetoChat}, an LLM (large language model)-based expert-agent interface for interactive multi-objective optimization. The agent translates natural-language user input into structured scalarization parameters, invokes an optimization system, presents candidate solutions, and iteratively elicits feedback. We describe a multi-agent architecture that separates input processing, multi-criteria decision-making (MCDM) expertise, solution presentation, and feedback processing. We then present a simulation study using an LLM-based DM agent and benchmark ParetoChat against interactive methods implemented in DESDEO, including reference-point and NIMBUS methods. The computational experiments on multi-objective binary knapsack and set-partitioning instances show that ParetoChat can guide the search efficiently toward solutions that match the DM's preferences. An application to historical courier-order assignment instances illustrates how users can explore objective extremes and intermediate trade-offs through natural-language requests. The results indicate that LLM agents may provide a practical interaction layer between business stakeholders and optimization tools.

</details>


### 30. Thought Blocks: Non-Autoregressive Latent Communication for Multi-Agent Systems via Trajectory-to-State Compilation

- **Authors:** Zhenhan Guan, Xiaolong Liu, Hengwei Ye, Zheng Tian
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23056v1](http://arxiv.org/abs/2610.23056v1)
- **PDF:** [https://arxiv.org/pdf/2610.23056v1](https://arxiv.org/pdf/2610.23056v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems typically communicate through text, incurring repeated generation and re-encoding costs. Although latent communication removes explicit verbalization, constructing latent messages may still require autoregressive latent trajectories. We therefore distinguish message representation from message construction and ask whether agents can directly construct useful continuation states without executing the trajectories that normally produce them. We formulate this problem as trajectory-to-state compilation and introduce Thought Blocks, fixed-size blocks of latent key--value (KV) continuation memory constructed in one shot. Thought Blocks achieve a 2.5 times average latency speedup over autoregressive latent communication. Compared with text-based multi-agent communication, Thought Blocks reduce text tokens by 45.7% and autoregressive steps by 84.8%, achieving an 8.6 times average latency speedup. These results demonstrate that trajectory-to-state compilation enables efficient inter-agent latent communication without sequential latent rollouts at inference.

</details>


### 31. Where Research Ideation Begins: Forward-Citation Supervision for Actionable Limitation Generation

- **Authors:** Liyang Zhao, Yong Cao, Haibin Ling
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.23038v1](http://arxiv.org/abs/2610.23038v1)
- **PDF:** [https://arxiv.org/pdf/2610.23038v1](https://arxiv.org/pdf/2610.23038v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated research ideation has advanced rapidly, with multi-agent workflows that generate whole research ideas end to end. These frameworks leave largely unexamined the step that seeds a good idea: identifying an actionable limitation from literature. In this paper, we focus on this first step in the research ideation pipeline. Starting from a pilot study, we find that as large language models (LLMs) scale from 0.6B to 32B parameters, they become far better at recognizing which limitation later work addressed, but no better at generating one, suggesting that the bottleneck lies in the supervision signal rather than model capacity. We therefore construct ActLim-Bench from forward citations, yielding 18,279 evidence-linked supervision triples with human verification. On this signal, we propose a three-stage post-training pipeline: supervised fine-tuning, verifier-filtered rejection-sampling fine-tuning, and reinforcement learning with the verifier as an online dense reward. Experimental results show that our method achieves the highest recall score compared to existing methods among all frontier models. We further show that our generated limitations are preferred in 64.9% of non-tied human comparisons and improve downstream ideation systems. We will release our data and code upon publication.

</details>


### 32. KiranaBench: Can a Language Model Run a Neighbourhood Shop?

- **Authors:** Bhuvan Arora, Ankita Karmakar, Chaitanya Jain, Dilesh Churiwal, Harshit Jain, Shivansh Manish Dubey, Manish Prasad, Raja Piyush, Kshitij Tayal, Dhruv Kumar, Jagat Sesh Challa, Raunak Manekar, Yash Sinha
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22980v1](http://arxiv.org/abs/2610.22980v1)
- **PDF:** [https://arxiv.org/pdf/2610.22980v1](https://arxiv.org/pdf/2610.22980v1)
- **Categories:** cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly evaluated on long-horizon tasks, including autonomously running a business. Existing benchmarks for this setting are almost exclusively English-language, Western in retail context, and single-agent, with the agent observing the business directly. We study how these results transfer to a multi-agent Indic setting. We introduce KiranaBench, a simulated Indian general store in which four roles (manager, cashier, helper, and bookkeeper) are each played by a separate LLM agent. Interactions with customers and suppliers occur in English, Hindi, or Hinglish, and product demand is calibrated to India's national Household Consumption Expenditure Survey. Evaluating four open-weight LLMs, we find that all fall far short of a fixed-rule shopkeeper baseline: the best model earns only one-eighth of the baseline's profit, and two models finish below an unmanaged shop. Performance is also consistently lower for Hindi and Hinglish than for English supplier communication. KiranaBench offers evidence that current LLM agents are not yet reliable for autonomously operating small businesses in India, and provides a testbed for developing agents suited to settings that are long-horizon, collaborative, and multilingual.

</details>


### 33. NL2SQL with Iterative Self-Refinement

- **Authors:** Anjali Vemula, Akshat Dasula
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22968v1](http://arxiv.org/abs/2610.22968v1)
- **PDF:** [https://arxiv.org/pdf/2610.22968v1](https://arxiv.org/pdf/2610.22968v1)
- **Categories:** cs.DB, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Bridging the gap between human intent and machine logic remains a critical challenge in data access for non-technical users, yet Large Language Models (LLMs) remain unreliable: they hallucinate schema elements, generate syntactically invalid queries, or fail to capture user intent. These limitations are especially critical in domains such as insurance, where KPIs, regulatory constraints, and legacy relational systems demand high precision. We introduce a multi-agent, persona-driven NL2SQL framework that combines (1) domain relevance detection, (2) schema-grounded knowledge construction, (3) KPI-aware SQL synthesis, (4) syntax-level self-repair using sqlite execution feedback, and (5) semantic consistency checking via SQL-to-NL reverse engineering. Our system significantly reduces query hallucination and improves semantic fidelity compared to direct LLM prompting. Evaluated on 60 queries (50 from a HuggingFace text-to-SQL dataset and 10 custom domain queries), the system achieves 90% correctness using Mistral across seven coordinated LLM calls showing that this approach can substantially increase the reliability of NL2SQL pipelines in high-stakes environments.

</details>


### 34. Provable Authority: A Protocol for Verifiable Authority Resolution and Control Across Human, Organizational, and Agentic Transactions

- **Authors:** Jeremy Blackburn, Tim Hines, Matthew Koepp, Russell Lessard, Jason Patrick
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22899v1](http://arxiv.org/abs/2610.22899v1)
- **PDF:** [https://arxiv.org/pdf/2610.22899v1](https://arxiv.org/pdf/2610.22899v1)
- **Categories:** cs.CR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Payment systems authenticate users, devices, accounts, and cryptographic credentials, but a relying party, such as a counterparty, payment rail, marketplace, or autonomous agent runtime, generally cannot obtain compact, independently verifiable evidence that the party presenting one exact transaction holds current organizational authority to execute it under the applicable evidence, policy, budget, and approval state. Agentic commerce makes this gap operationally urgent: a software agent can produce a valid signature while acting outside its delegated purpose, after its sponsor's authority has changed, or on transaction details that differ from those a human approved. We describe the ChainIT Authority Protocol, a subject-neutral and rail-neutral pre-execution authority and evidence control plane. The protocol separates durable identity, a versioned organizational authority record (the Authority Resolution Pactvera), sourced evidence assertions, deterministic reason-coded policy predicates, and organization-configured dispositions; binds each decision and human approval to a canonical transaction digest; reserves capacity atomically so that limits hold under concurrency; and authorizes commit only through a single-use, sender-constrained Execution Authorization Credential consumed at the rail adapter, with append-only lifecycle evidence sealed after the terminal outcome. An Agent Subject Profile adds the workload registration, attested key hierarchy, and sovereignty boundary required when the acting subject is an AI agent, without introducing a separate authority concept. We specify the commit-time execution predicate and bounded-freshness status rules, give enforcement profiles for fiat (ACH, wire, card, instant payment) and stablecoin rails, and state residual risks and non-goals.

</details>


### 35. Cooperation Without Adaptation: LLM Agents in a Collective-Risk Dilemma

- **Authors:** Trung-Kiet Huynh, Dao-Sy Duy-Minh, Chi-Nguyen Tran, Phu-Hoa Pham, Phu-Quy Nguyen-Lam, Le Hong Trang, The Anh Han
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22882v1](http://arxiv.org/abs/2610.22882v1)
- **PDF:** [https://arxiv.org/pdf/2610.22882v1](https://arxiv.org/pdf/2610.22882v1)
- **Categories:** cs.GT, cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language-model agents are increasingly deployed to act on behalf of people in settings where individual decisions shape shared outcomes. We examine whether five production models adapt their contributions to changing risks and partner behaviour, or instead follow a relatively fixed strategy. In a collective-risk dilemma game (CRG), six players contribute to a shared pool over ten rounds; if the pool falls short of its target, a catastrophe may destroy their remaining resources. Four models contributed approximately an equal share at every positive risk level, and four of the five also contributed when risk was zero, even though contributing could not improve their payoff. Explicitly stating that only the agent's own payoff mattered reduced zero-risk contributions for most models, while a more neutral prompt did not. Several models correctly identified which action offered the higher expected payoff at different risk levels, yet their contributions changed little. Against fixed partners, no model consistently chose the payoff-maximising response, and in mixed-model groups, a single agent's shortfall in the final round could cause an otherwise successful group to fail. Payoff-based selection also depended on population composition: in a single six-agent group, it favoured the model that contributed least and reduced group success, whereas in larger, randomly mixed populations, it favoured an exact fair-share model at moderate and high risk. These findings show that cooperative self-play alone is not evidence of strategic adaptability. Consistent with a machine-behaviour approach, evaluations of agents in multi-agent systems should test how they respond to incentives, partner actions, and population composition.

</details>


### 36. MS-Eval: Benchmarking Sub-Agent Delegation and Orchestration in MCP-Intensive Working Scenarios

- **Authors:** Bowen Ding, Qixin Wang, Lexing Ruan, Weiyi Lu, Qiwei Ge, Ruishan Fang, Tao Lin
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22869v1](http://arxiv.org/abs/2610.22869v1)
- **PDF:** [https://arxiv.org/pdf/2610.22869v1](https://arxiv.org/pdf/2610.22869v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly integrated into real-world works, yet they must handle diverse domain-specific tools and complex multi-sub-task problems that sequential tool invocation resolves inefficiently and with severe context bloat. The Main-Agent Delegation and Sub-Agent Execution (MAD-SAE) paradigm addresses these issues by delegating sub-tasks to specialized sub-agents for parallel execution in isolated contexts, but its delegation and orchestration quality remains unquantified. We introduce MS-Eval, a unified evaluation kit comprising an MCP-intensive benchmark, a controlled execution harness, tailored delegation and orchestration metrics, and the MSQ index for comprehensive assessment. Evaluating four MAD-SAE variants and eight frontier models reveals that (1) sub-agent specialization (Spec) is the best practical practice; (2) open-source models are largely competitive with few exceptions; and (3) MAD-SAE generally raises cost with contingent payoff, benefiting most open-source models in both performance and efficiency while leaving closed-source models with higher cost and degraded performance. Our case study further traces these gains to better single-agent solutions, effective context offloading, and genuine sub-task parallelism, whereas unnecessary or redundant delegation turns the same cost into pure overhead. Codes: https://github.com/LINs-lab/MS-Eval

</details>


### 37. Benchmarking and Enhancing Agentic Causal Discovery

- **Authors:** Pingchuan Ma, Rui Ding, Shuai Wang
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22846v1](http://arxiv.org/abs/2610.22846v1)
- **PDF:** [https://arxiv.org/pdf/2610.22846v1](https://arxiv.org/pdf/2610.22846v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents can now run causal discovery algorithms on a dataset and report what comes out. Whether they do more than that, such as noticing where an algorithm went wrong and fixing it with further tests, is hard to tell from current benchmarks. Most of them give the variables meaningful names, and an LLM shown only the names of the Tübingen cause-effect pairs already gets 99% of the directions right. With the names removed, the data are usually clean enough that picking a better algorithm than PC closes most of the gap. We introduce Heuresis, a benchmark of anonymous simulated datasets whose mechanisms range from linear Gaussian to heavy-tailed. For each family of datasets it separates what a better existing algorithm can gain from what only a closer look at the data can gain, and it traces every edge an agent changes. Every family leaves a gap that none of the algorithms, the router and the two causal-discovery foundation models we ran can close, so a score above the best chosen algorithm has to come from using the data. We instantiate the benchmark with an agent harness and three LLMs, GPT-6.1 Sol, Claude Opus 5.5 and Qwen 3.8 Flash. GPT-6.1 Sol surpasses the best chosen algorithm on all six families, by 14% adjacency F1 on the most difficult one, and Claude Opus 5.5 does so by 7.4% there. A third of the true edges the two agents restore on the two hardest families appear in no algorithm's output. The code and data will be publicly released to facilitate future work.

</details>


### 38. When Can You Trust an Agent's Own Verifier? Stress-Testing Counterfactual Rationale Verification Under Search Pressure and Oracle Access

- **Authors:** Jonghyun Lee, Moonsu Kim, Sunghwan Park
- **Published:** 2026-10-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22779v1](http://arxiv.org/abs/2610.22779v1)
- **PDF:** [https://arxiv.org/pdf/2610.22779v1](https://arxiv.org/pdf/2610.22779v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated agent design increasingly trusts a single score to decide whether a change is an improvement -- but a score optimized aggressively enough ceases to measure what it was meant to. When an agent also explains its design, that explanation is a second signal we can check without human labels: negate each stated claim, re-run, and observe whether performance drops. We ask whether such a verifier stays reliable once an agent optimizes against it. Our contribution is not a new verifier but a way to stress-test one: a pressure ratio $ρ$ measuring how much the verifier steers the agent's search, and four falsifiable probes covering four failure modes -- giving no signal, being too weak to matter, being gamed by stating fewer claims, and being queried before the agent commits. We apply the test to our own verifier, the Rationale Consistency Score (RCS), inside an LLM agent that designs machine-learning pipelines, with one generator model, six tasks, and three seeds. First, in our prior configuration the verifier barely affects the search objective ($ρ\ll 1$), partly because of an accuracy gate, so its robustness had not been tested; it still shapes the reported artifact through a final-selection tie-break that $ρ$ does not register. Second, a capability control shows the agent shortens its claim lists when instructed, yet search does not, even at $ρ$ over 100 times the prior level; since feedback omits claim volume and horizons are short, this null result is largely structural rather than evidence of robustness. Third, when the agent can probe the verifier before committing, it keeps claims that pass while held-out faithfulness falls -- a decline invisible to in-loop metrics, though partly confounded by how RCS scores small pipelines. We offer these as preliminary evidence and propose a reporting standard: audit a verifier with $ρ$ and these probes before trusting it.

</details>


### 39. R$^2$Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop

- **Authors:** Mingda Zhang, Yun Huang, Qiang Huang, Yanjin Li, Rui Qian, Qichao Zhao, Tiesunlong Shen, Na Zhao, Jian Wang, Xiaoying Tang
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22740v1](http://arxiv.org/abs/2610.22740v1)
- **PDF:** [https://arxiv.org/pdf/2610.22740v1](https://arxiv.org/pdf/2610.22740v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In recent years, agentic orchestration has been widely applied to solve complex human tasks. However, existing orchestration learning still faces key challenges, including hand-designed curricula, advantage collapse when a task's rollouts all reach the same outcome, and unreliable evaluation signals that judge each skill by one noisy score. To address these challenges, we propose R$^2$Orch, a new paradigm of Recursive Self-Play Orchestration: an inner loop of self-play that improves the orchestrator on self-chosen tasks, and an outer loop that improves how the inner loop improves. To support this paradigm, we introduce Recursive Learnability, a training objective that rewards a Proposer for choosing tasks whose rollouts keep reaching different outcomes as skills are withdrawn. Built on this objective, we further propose Skill Withdrawal, in which the outer loop withdraws each skill once a controlled evaluation within self-play shows that the orchestrator performs as well without it. Moreover, the two loops form one cycle: failures are distilled into skills, skills into parameters, and withdrawals lead the Proposer to new failures, so the orchestrator moves toward zero-skill deployment. Experimental results on twelve datasets show that R$^2$Orch consistently outperforms baselines across question answering, math, code, and interactive tasks.

</details>


### 40. NoveltyScope: A Multi-Agent Research Assistant for Evidence-Grounded Novelty Assessment of Scientific Papers

- **Authors:** Yueran Tian, Huizhi Liang
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22703v1](http://arxiv.org/abs/2610.22703v1)
- **PDF:** [https://arxiv.org/pdf/2610.22703v1](https://arxiv.org/pdf/2610.22703v1)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

NoveltyScope is a prototype that compares a scientific paper with retrieved prior work and produces a structured report and a five-level novelty score. The system extracts the core task and at most two author-claimed contributions, then searches a closed local corpus using BM25 and dense retrieval with reciprocal rank fusion. Contribution comparisons request paired passages for potential refutations, and quotations are checked against cached source text. Four scoring roles (Prosecutor, Defender, Judge, and Critic) use the resulting evidence, with at most one revision of the Judge's score. Evaluation uses 50 class-balanced RINoBench samples whose idea-level labels are retained for full-paper input. Mean absolute error is 1.48 and 1.26 for single-LLM and multi-agent scoring with Gemini, respectively, and 1.22 and 1.16 with Qwen3. The vector-similarity baseline has an error of 1.68. A HiCLIP case study illustrates the contribution comparisons and paired evidence passages. Overall, the results demonstrate the feasibility of evidence-grounded novelty assessment and show that the multi-agent configurations achieve lower scoring errors than their single-LLM counterparts across both evaluated models.

</details>


### 41. Emergent Discrimination and Polarization in Multi-Agent Systems

- **Authors:** Nestor Caticha, João Henrique Sant'Ana, Felippe Alves, Davi Bastos Costa, Mariana Mercucci, Juan P. Neirotti, Otavio Citton, Renato Vicente
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22701v1](http://arxiv.org/abs/2610.22701v1)
- **PDF:** [https://arxiv.org/pdf/2610.22701v1](https://arxiv.org/pdf/2610.22701v1)
- **Categories:** cs.MA, cond-mat.dis-nn, physics.soc-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study theoretically how discrimination and polarization can emerge in a population of learning agents. Each agent uses an adaptive linear decision layer to map a language-model embedding of an issue to a binary opinion and maintains an evolving estimate of how much it trusts every other agent. Through pairwise interactions, agents update both their decision weights and trust estimates using an online Bayesian rule derived from teacher-student learning over a noisy channel. In-context-learning experiments with large language models qualitatively reproduce the predicted opinion and trust updates. We then assign each agent one of two arbitrary group labels, A or B, and model group bias by allowing a fraction $f_b$ of agents to shift its perceived agreement with each message by a strength $b$, a bias steering prejudice, depending on whether the sender and receiver share a label. We use order parameters from statistical mechanics to connect these local dynamics to collective states and transitions. Starting from uniformly random initial conditions, simulations reveal a rich phase diagram in the $(b,f_b)$ plane, comprising four collective states: spin-glass frustrated out-group favoritism, nondiscriminatory polarization, discrimination with opinion alignment, and discrimination without opinion alignment. Which state emerges depends on both the strength and prevalence of the bias. These results show how simple local learning dynamics can generate qualitatively distinct forms of polarization and discrimination, underscoring the need for population-level safety analysis of multi-agent systems. They also suggest measurable order parameters for characterizing analogous collective states in human societies.

</details>


### 42. Gossip Agents: Reputation through Opinion Dynamics over Evolving Networks

- **Authors:** Yutong Wu, Arlei Silva
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22674v1](http://arxiv.org/abs/2610.22674v1)
- **PDF:** [https://arxiv.org/pdf/2610.22674v1](https://arxiv.org/pdf/2610.22674v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Sustained cooperation among self-interested learning agents is essential in many shared environments. Reputation systems are among the best-studied mechanisms for promoting such cooperation. Existing multi-agent reinforcement learning approaches, however, typically assume that reputation is either globally available to all agents or derived solely from an agent's own observations, leaving largely unexplored how reputational information propagates between agents. We study gossip, the exchange of information about third parties, as a mechanism for reputation diffusion over dynamic communication networks. Agents form private opinions from limited observations and exchange them with their neighbors following DeGroot opinion dynamics, while the communication network changes as agents interact and move. A tunable broadcast radius controls the reach of information, spanning private reputation, local gossip, and globally shared reputation. We study this framework in two \(n\)-player social dilemmas with distinct network dynamics: a Prisoner's Dilemma with randomly resampled interaction groups and Harvest, where communication neighborhoods emerge from agents' movements. Our results show that the reach of reputational information shapes cooperation in both environments. Moreover, in Harvest, reputation diffusion increases environmental rewards and leads to more peaceful and sustainable behavior.

</details>


### 43. From Relevant Memories to Sufficient Evidence: Rethinking Memory Utilization in LLM Agents

- **Authors:** Shixuan Li, Wei Yang, Peiyu Zhang, Anzhe Cheng, Heng Ping, Xiaole Zhang, Jesse Thomason, Xuezhe Ma, Yue Zhao, Paul Bogdan
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22668v1](http://arxiv.org/abs/2610.22668v1)
- **PDF:** [https://arxiv.org/pdf/2610.22668v1](https://arxiv.org/pdf/2610.22668v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-term memory enables LLM agents to reuse past experiences, yet retrieving relevant memories does not necessarily provide sufficient evidence for answering a query. Essential information may remain fragmented across memory records, obscured by abstraction, or disconnected from the relations required for reasoning. We identify this relevance-sufficiency gap and propose QEMem, a framework that reformulates memory utilization as the construction of query-specific evidence sets, shifting the focus from individual retrieval relevance to collective evidential support. QEMem integrates three complementary mechanisms: query-guided discovery retrieves evidence across multiple memory granularities; source-grounded reification organizes it into structured ViewCards with explicit evidential roles and source references; and sufficiency-guided refinement selectively recovers missing information. Operating on existing memory stores without modifying memory formation, QEMem achieves 91.43% LLM-judge accuracy on LoCoMo with Claude Opus 4.5, outperforming the strongest evaluated baseline, MemR$^3$, by 7.6 percentage points and NEMORI by 10.7 points under a shared memory store. Further analyses demonstrate improved evidence coverage and strong performance on questions requiring cross-session evidence integration.

</details>


### 44. Edit Discovery in Human-AI Interactions

- **Authors:** Alireza Mirrokni, Shayan Kiyani, George Pappas, Hamed Hassani
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22661v1](http://arxiv.org/abs/2610.22661v1)
- **PDF:** [https://arxiv.org/pdf/2610.22661v1](https://arxiv.org/pdf/2610.22661v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Human-AI interactions are becoming a rich source of data for improving AI systems: while many model responses are already satisfactory, others expose failures that could become valuable supervision if identified and corrected. We study this setting through the notion of an editor: a more capable evaluation process that can inspect a response and either confirm it or modify it, but whose invocation is costly. The editor may be a human expert, a stronger AI system, or the same model equipped with additional computation, context, tools, or information. The key challenge is to decide which interactions to send to the editor before knowing whether an edit will actually be made, since invoking the editor itself consumes limited resources such as expert time, inference cost, latency, or tool-use overhead. We formulate this problem as Edit Discovery Optimization (EDO), which seeks to minimize edit opportunities missed among skipped interactions while controlling unnecessary confirmations and respecting an editor-cost budget. We characterize the population-optimal policy and show that it takes the form of a cost-adjusted threshold on the posterior probability of an edit. Building on this structure, we develop EDIT (Edit Discovery via Iterative Thresholding), an online algorithm for the partial-feedback setting in which edit labels are revealed only for selected interactions. EDIT combines an adaptive edit score, a confirmation-control threshold, and a cost-aware selection rule; it satisfies the editor budget at every round and controls the average confirmation rate up to a vanishing finite-horizon term, without distributional assumptions on the interaction stream. Across four reasoning and factual question-answering benchmarks, EDIT achieves a better trade-off between editor cost, Type-I error, and Type-II error than direct LLM-based batch selection.

</details>


### 45. The Model Knows Better: Defending Medical Multi-Agent Systems Against Prompt Injection

- **Authors:** Fardin Ahsan Sakib, Ziwei Zhu, Ozlem Uzuner
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22594v1](http://arxiv.org/abs/2610.22594v1)
- **PDF:** [https://arxiv.org/pdf/2610.22594v1](https://arxiv.org/pdf/2610.22594v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Medical multi-agent systems, in which LLM agents discuss a case, are increasingly studied for clinical decision support. Prompt injection, text that an attacker adds to a model's input, can manipulate LLMs into wrong decisions. How it affects these systems, and how to protect them, remains unclear. Across two systems, two model families and three benchmarks, a single injected passage succeeds in up to 61% of cases, and collaboration does not consistently protect against it. Existing defenses help only partly: they miss injections that look like ordinary clinical text. Yet when asked to check the injected text against the patient's findings, a model that followed the injection usually rejects it. We therefore propose a training-free defense that verifies the clinical judgments behind the system's decision. Following clinical practice, it separates the patient's findings from clinical judgments, such as diagnoses, recommendations and instructions, and checks each judgment against the findings alone, so the decision rests only on supported judgments. Our defense outperforms all baselines on every benchmark, lowering attack success on MedQA to 4-7% while maintaining accuracy on cases without an attack, and remains effective with a medical model and against defense-aware and adaptive attacks.

</details>


### 46. FRACTAL: A Self-Similar Multi-Agent Orchestration Architecture with Formal Communication, Convergence, and Depth Bounds

- **Authors:** Ohad Dan, Abhinav Taliyan
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22561v1](http://arxiv.org/abs/2610.22561v1)
- **PDF:** [https://arxiv.org/pdf/2610.22561v1](https://arxiv.org/pdf/2610.22561v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present FRACTAL, a self-similar multi-agent architecture for recursive goal decomposition, in which the same five-component organizational pattern -- Orchestrator, Ensemble, Knowledge Ledger, Decision Maker, Meta-Observer -- recurs at every level of a decomposition tree. We make four formal contributions: (1) a communication bound showing intra-node cost is linear in ensemble size and round count (O(kr)) under a two-phase blind-proposal/stress-test protocol, versus quadratic cost for free-form debate, with an explicit, stated assumption on fixed evaluator count; (2) a two-mode orchestration criterion separating generative and evaluative phases via a measurable diversity-saturation threshold; (3) a supermajority convergence guarantee with explicit probability bounds at stated agreement levels, and a formal depth bound under an operationalized goal-complexity measure; (4) a Bayesian inter-layer escalation mechanism unifying hysteresis and contract-breach signaling under one posterior update. We illustrate the architecture's execution qualitatively on a worked example and a multi-layer case study; we do not report quantitative performance claims in this paper, and we explicitly discuss the formal and inductive-bias limitations of the model, including an unimplemented but architecture-compatible direction toward bounded self-improvement. We use "fractal" as an architectural metaphor for self-similarity, not a measured mathematical property. Empirical validation of the architecture's comparative performance is left to future work.

</details>


### 47. AuditKIT: A Unified Evaluation Spine for Benchmarking, Judging, and Comparing Large Language Models and Agentic Systems

- **Authors:** Shreeyans Arora, Utsav Avaiya, Zera Lyngkhoi, Hem Gosalia, Ram Mohan Rao Kadiyala, Vinay Kumar Sankarapu, Pratinav Seth
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22511v1](http://arxiv.org/abs/2610.22511v1)
- **PDF:** [https://arxiv.org/pdf/2610.22511v1](https://arxiv.org/pdf/2610.22511v1)
- **Categories:** cs.CL, cs.AI, cs.IR, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluating language models and agents requires combining benchmark accuracy, judge-based assessment, runtime performance, tool-use behavior, and retrieval quality. Differences in interfaces, metric semantics, and trace formats complicate these comparisons and can hide failures in agentic workflows. We present AuditKIT, a source-available evaluation library that records these measurements in one result representation, with direction-aware metric contracts, configuration fingerprints, and extensible metrics and backends. For agents, it provides turn-aware tool-call matching, separates parallel from sequential execution, and distinguishes verified task outcomes from trajectory-level diagnostics. Missing or unobservable evidence is marked unscored rather than counted as failure. For retrieval-augmented generation, it combines ranked retrieval metrics, judged grounding, and deterministic evidence checks. Seven case studies spanning model comparison, serving runtimes, retrieval, tool calling, and interoperability show how answer extraction, runtime behavior, and metric selection change evaluation outcomes.

</details>


### 48. RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents

- **Authors:** Yunqi Liu, Peiyu Wang, Bingli Wang, Leo Luo, Xuanwu Song, Xudong Ma, Hongxin Li, Yaxin Du, Weicheng Gu, Fanglin Xu, Yi Xing, XiangLong Liu, Jujie He, Zhange Zhang, Huatong Song, Zhaoyi Li, Deyang Kong, Chuan Hao, Peihao Wu, Mingjie Tang, Ran Tao, Jian Yang, Wayne Xin Zhao, Bryan Dai
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22507v1](http://arxiv.org/abs/2610.22507v1)
- **PDF:** [https://arxiv.org/pdf/2610.22507v1](https://arxiv.org/pdf/2610.22507v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Command-line interface (CLI) agents increasingly execute longer-horizon tasks, yet existing benchmarks either assume that user instructions remain fixed throughout execution or evaluate task outcomes without capturing runtime collaboration quality. In this paper, we present REALCLI, a paired benchmark that unifies the evaluation of task execution and human-agent collaboration quality on realistic CLI tasks. To comprehensively measure collaboration, REALCLI builds a five-dimensional framework, operationalized into 22 sub-dimensions and 51 interaction scenario templates. REALCLI provides two modes for paired comparison: REALCLI-EXEC supplies complete specifications upfront, whereas REALCLI-COLLAB introduces a scripted user that delivers progressive information, corrections, constraint revisions, and authorization decisions. Evaluations reveal profound capability gaps in frontier agents: the best configuration attains an average score of only 49.2%, and when evaluated by the joint collaboration score ($J_{\mathrm{collab}}$), the peak performance reaches merely 37.6%. These results show that task effectiveness diverges sharply from collaboration quality, with models consistently struggling in steerability, trust calibration, and safety boundary management. REALCLI provides a rigorous, reproducible foundation for measuring and advancing collaborative CLI agents.

</details>


### 49. MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering

- **Authors:** Shangheng Du, Jinxin Shi, Shuaiyu Zhang, Yiming Wu, Junpeng Zhao, Shiyang Feng, Xin Li, Liang He, Xiangchao Yan, Bo Zhang
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22344v1](http://arxiv.org/abs/2610.22344v1)
- **PDF:** [https://arxiv.org/pdf/2610.22344v1](https://arxiv.org/pdf/2610.22344v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recursive self-improvement (RSI). Workflow-driven machine learning engineering (MLE) systems provide a practical path toward this pursuit through complex orchestration that manages long-horizon experimentation, while recent MLE systems adopt model-directed interaction, allowing models to autonomously organize experiments and adapt optimization strategies based on execution feedback. However, feedback from each experiment reflects several preceding decisions, and a long MLE run contains many such costly experiments. Training must therefore select useful supervision from long interaction trajectories and learn from intermediate outcomes. We propose a post-training method for autonomous long-horizon MLE optimization and apply it to train MLExpert, a 35B Mixture-of-Experts agentic model. We design the Kaggle-MLE Factory to construct executable tasks and an interaction harness for model-directed experimentation. Hierarchical agentic SFT transfers general tool-use and coding capabilities to MLE through outcome-guided supervision. Windowed Interaction RL (WIRL) treats the multi-turn decisions between successive experiment results as an execution window and assigns it a shared outcome-based reward. Asynchronous collection and policy correction support policy updates before the trajectory ends. On MLE-Bench Lite, MLExpert improves the average medal rate of the base model from 37.9% to 72.7%, achieving performance comparable to larger frontier models such as Kimi-K3 and GLM-5.3. Further experiments show that MLExpert improves performance on NatureBench Lite, agent scaffold optimization, and algorithm optimization, suggesting that the learned optimization capability generalizes to other tasks.

</details>


### 50. 3DCodeVerse: Exploring 3D Worlds as Code

- **Authors:** Yipeng Gao, Ziyao Zeng, Jinfa Huang, Yijiang Li, Haolin Xiong, Wang Qin, Xinlei Yu, Youheng Yao, Jie Zhang, Kun-Yu Lin, Rong Liu, Yinyuan Zhao, Yajie Zhao, Meiqi Guo, Jiebo Luo, Lei Shu, Yunhao Ge, Xinyu Hu, Laurent Itti
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22341v1](http://arxiv.org/abs/2610.22341v1)
- **PDF:** [https://arxiv.org/pdf/2610.22341v1](https://arxiv.org/pdf/2610.22341v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce 3DCodeVerse, a research ecosystem that enables coding agents to create editable and verifiable 3D content at scale. 3DCodeVerse comprises large-scale, high-quality datasets of executable 3D code, a coding harness for spatial reasoning and automated verification, and practical guidance for 3D coding. First, we construct 3DCodeVerse-2M, a large-scale curated dataset of standalone 3D executable code. We build this corpus by collecting open-source data, converting specialized representations, and generating new programs with coding agents. Each program is packaged with the source files and associated assets required for execution in its declared environment, along with available descriptions and verification records. Second, we develop the 3DCodeVerse Harness, a multi-agent directed acyclic graph framework for generating and refining 3D content. It uses execution checks, spatial measurements, and visual feedback to automatically evaluate and revise generated programs without human feedback during generation. Third, we conduct systematic empirical studies of 3D coding, establishing baselines with fine-tuned open models and deriving practical guidance through component-level analyses of our harness. Extensive experiments demonstrate that fine-tuning on our dataset significantly improves the 3D coding capabilities of open-source models. Notably, our 3DCodeVerse harness achieves a 90% win rate against Claude Design (3D Object) in pairwise human evaluations, when both are utilized by Claude Opus 5.5.

</details>


### 51. Learning Self-Orchestration in Decentralized Agent Swarms

- **Authors:** Guowei Xu, Zhenting Qi, Amani Kiruga, Himabindu Lakkaraju, Yilun Du
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22322v1](http://arxiv.org/abs/2610.22322v1)
- **PDF:** [https://arxiv.org/pdf/2610.22322v1](https://arxiv.org/pdf/2610.22322v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

The capabilities of an agent swarm depend on both its individual members and how they coordinate. Yet existing multi-agent systems often train agents within fixed orchestration structures, separating the learning of individual capabilities from the organization of collective behavior. We introduce market-based post-training (MPT), a framework for jointly learning action policies and self-orchestration in decentralized agent swarms. Agents express their willingness to participate through bids, which determine who acts and how collective outcomes provide local training credit. Learning both action and bidding behavior allows individual capabilities and patterns of participation to adapt together without a central coordinating agent. We evaluate MPT on embodied crafting, robot navigation, and deep research. Results show gains over monolithic post-training and confirm that agent participation indeed evolves with learning. With the same post-trained action policies, learned self-orchestration outperforms alternative coordination strategies. Ablations show that both action and bidding benefit from learning, and that learned bids provide more effective action-training signals. Beyond the original training objectives, trained swarms adapt faster to related tasks and achieve better performance with larger populations at inference time. Larger populations also suffer smaller performance losses under agent dropout, demonstrating that learned self-orchestration supports reuse, scaling, and robustness in decentralized agent swarms. Code and trained models are available at https://github.com/Embodied-Minds-Lab/MPT.

</details>


### 52. A team of Gemini 4 Argon agents beats Minecraft

- **Authors:** Maxence Faldor, Satinder Singh, Roberta Raileanu
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22319v1](http://arxiv.org/abs/2610.22319v1)
- **PDF:** [https://arxiv.org/pdf/2610.22319v1](https://arxiv.org/pdf/2610.22319v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We placed four Gemini 4 Argon agents in a sandboxed Minecraft survival world and gave them one goal: defeat the Ender Dragon. Each agent controlled a player via an open-source library called Mineflayer and coordinated with its teammates through in-game chat and shared memory. No one assigned roles or wrote game logic. The agents planned, wrote, and debugged every program themselves. Researchers could watch the run on a live dashboard and pause or stop it at any time, but they had no cause to intervene. Starting from a randomly generated world on Easy difficulty, the team wrote 2,783 programs and defeated the dragon in 27 hours and 14 minutes, dying 605 times along the way. To our knowledge, this is the first end-to-end autonomous completion of Minecraft by AI agents, achieved using only the standard Mineflayer library without pre-scouted seeds or other game-specific tools written by humans. Winning required the agents to keep a coherent plan across thousands of dependent steps for more than a day. Complex real-world software engineering and enterprise tasks demand the same long-horizon coding and multi-agent coordination. We describe the setup, how the run unfolded, the team's strategies (dividing the work, sharing what they learned, recovering each other's items), and the limits of the result.

</details>


### 53. Learning to Steer LLM Agents and Multi-Agent Systems

- **Authors:** Leyang Shen, Yaxin Gong, Yang Zhang, Chenxiao Fan, Jiakai Wang, Dong Wang, Yang Liu, Fuli Feng, Chun Kai Ling, Tat-Seng Chua
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22316v1](http://arxiv.org/abs/2610.22316v1)
- **PDF:** [https://arxiv.org/pdf/2610.22316v1](https://arxiv.org/pdf/2610.22316v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based agents and multi-agent systems increasingly tackle complex tasks through long-horizon tool use and inter-agent collaboration. However, these systems are prone to deviating from the overall goal as execution unfolds, which wastes execution resources and leads to undesired outcomes, a failure termed goal drift. In this work, we propose a steering agent that supervises execution on the fly and steers the system back on track when drift occurs. The steering agent observes the execution context, deciding when to intervene with a low-cost fast path and how to intervene with a high-cost slow path. To unlock its steering intelligence, the ability to assess goal drift and generate effective interventions, we jointly train the two paths with reinforcement learning, combining a pairwise ranking objective with group-relative policy optimization (GRPO). Experiments on information-seeking search tasks show that the steering agent provides effective supervision for both single-agent and multi-agent systems, improving their performance and efficiency. The learned steering intelligence generalizes to out-of-domain tasks, transfers to unseen executors, and supports controllable intervention frequency without retraining.

</details>


### 54. CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM Honesty

- **Authors:** Yuan-Chen Chang, Niklas Herbster, Gauthier Gidel, Tommaso Tosato
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22292v1](http://arxiv.org/abs/2610.22292v1)
- **PDF:** [https://arxiv.org/pdf/2610.22292v1](https://arxiv.org/pdf/2610.22292v1)
- **Categories:** cs.LG, cs.CL, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are becoming prevalent in scenarios where honesty is critical. However, despite alignment training, these models still exhibit dishonest behaviour, such as outputting claims that contradict some knowledge or are not supported by what is accessible in context. We introduce Continuous Adversarial Training for Consistent Honesty (CATCH), inspired by a method originally developed to robustly refuse harmful queries. CATCH trains the model towards an honest answer and away from a dishonest one while maintaining the model's capabilities. We evaluate two architectures (Llama-3.3-70B-Instruct and Qwen3-3.6-27B). We show that trained with only hundreds of targets built from self-reporting scenarios, CATCH learns an honest behaviour that robustly generalizes and transfers across distinct benchmarks. It consistently reduces dishonesty under pressure on MASK, increases confessions in the multi-agent game of Among Us, and improves the discovery rates of the model's hidden behaviours in AuditBench. We show that CATCH outperforms prompting and supervised fine-tuning in improving honesty, and it is on par with state-of-the-art honesty activation steering. However, CATCH surpasses honesty steering in maintaining utility, thanks to a novel choice of utility data.

</details>


### 55. Learning Rational Strategies for Temporal Objectives in Multi-Agent Systems

- **Authors:** Omar Adalat, Edwin Hamel-De le Court, Francesco Belardinelli
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22287v1](http://arxiv.org/abs/2610.22287v1)
- **PDF:** [https://arxiv.org/pdf/2610.22287v1](https://arxiv.org/pdf/2610.22287v1)
- **Categories:** cs.LG, cs.LO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study rational synthesis for stochastic multi-agent systems with unknown dynamics, where each agent is equipped with its own probabilistic temporal objective specified using Probabilistic Linear Temporal Logic on Finite Traces ($\mathsf{PLTL}_f}$). We impose solution concepts (e.g., Nash equilibrium, subgame-perfect equilibrium) as constraints on the joint strategy profile, using payoffs derived from each agent's probability of satisfying its temporal objective. In particular, we formulate per-agent rational synthesis as finding a strategy profile -- if one exists -- such that (i) the designated agent's probabilistic temporal constraint is satisfied, and (ii) the profile represents a stable solution under a chosen solution concept. We give conditional convergence guarantees for tabular Nash-Q learning, certify satisfaction with simultaneous finite-sample confidence bounds, and assess strategic stability with approximate best-response checking. Our approach operates in a stochastic \emph{Multi-Agent Reinforcement Learning} (MARL) environment, where model-free learning algorithms attempt to attain extremal satisfaction probabilities for temporal objectives automatically compiled into reward automata. Our approach is empirically validated using 8 general-sum concurrent stochastic games.

</details>


### 56. Auditable and Deployable Multi-Agent Motion Planning via Posetal Games from Legal Guidelines

- **Authors:** Florian Lercher, Karan Mahesh, Yujun Huang, Meshal Alharbi, Runyu Zhang, Hanna Krasowski, Michael R. Benjamin, Matthias Althoff, Gioele Zardini
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22277v1](http://arxiv.org/abs/2610.22277v1)
- **PDF:** [https://arxiv.org/pdf/2610.22277v1](https://arxiv.org/pdf/2610.22277v1)
- **Categories:** cs.MA, cs.GT, cs.RO, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

When robots are deployed in the real-world, they must interact with other agents and accomplish their own goals while adhering to legal constraints. These potentially conflicting objectives are often only partially prioritized, making scalarized objectives or fully specified hierarchies unsuitable. We present a framework for multi-agent motion planning under legal requirements based on games with partially ordered preferences (posetal games). Scenario-independent legal guidelines order abstract legal concerns, from which we automatically derive agent preferences and a legal game for any concrete scenario. Agents may refine their legal preferences with private objectives, and regulators may refine the guideline as laws evolve. We prove that such customizations can only remove equilibria and thus preserve legality. To coordinate agents without explicitly communicating private preferences, we introduce belief play, which provably recovers the true equilibria from conservative local games, and a distributed iterative best-response protocol requiring less information. We apply the framework to maritime navigation, systematically lifting pairwise traffic rules to multi-vessel encounters. On seven encounters with up to four vessels, every rule violation of the committed equilibria is certified as forced by the legal hierarchy or unsatisfiable, and defectors are identified from public information in all tested cases. These results indicate that guideline-based posetal games offer an auditable route from partially specified laws to multi-agent motion planning.

</details>


### 57. Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries

- **Authors:** Anikait Singh, Teresa Zhang, Yoonho Lee, Roshen Sanjay Nair, Aviral Kumar, Chelsea Finn
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22273v1](http://arxiv.org/abs/2610.22273v1)
- **PDF:** [https://arxiv.org/pdf/2610.22273v1](https://arxiv.org/pdf/2610.22273v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid heuristics. Instead, can we allow agents to perform anticipatory directed curation: learning to proactively reorganize unstructured corpora prior to inference to efficiently serve diverse future queries. We build on a key asymmetry in modern agentic harnesses (e.g., Claude Code): while LLM agents are adept at navigating existing filesystems to solve an immediate task, they are rarely trained to construct reusable workspaces for future use. To instantiate this capability, we introduce Librarian Agents, a framework in which a builder agent transforms raw documents into a hierarchical filesystem of synthetic files and reference links, which forms a workspace tailored for a downstream answering agent. We formulate workspace construction as a Markov decision process and optimize the builder policy via reinforcement learning to directly maximize downstream answering accuracy. Empirically, Librarian Agents outperforms the strongest retrieval and precomputation baselines by 33 percentage points on BrowseComp-Plus, amortizes upfront construction costs across repeated queries, and generalizes zero-shot to unseen domains on BRIGHT with a 31-point average accuracy improvement.

</details>


### 58. X-RIC: An Agentic RAN-Intelligent Controller Benchmark for Enhancing Reinforcement Learning

- **Authors:** Adhwaa Al-Chaab, Ayman Younis, Dario Pompili
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22269v1](http://arxiv.org/abs/2610.22269v1)
- **PDF:** [https://arxiv.org/pdf/2610.22269v1](https://arxiv.org/pdf/2610.22269v1)
- **Categories:** cs.AI, cs.AR


> Summary unavailable.


<details>
<summary>Abstract</summary>

The O-RAN ALLIANCE introduces architectural flexibility through disaggregation and AI-driven control. While the RAN Intelligent Controller (RIC) enables centralized optimization, current AI approaches lack reasoning capabilities and explainability. We propose eXplainable RIC (X-RIC), a novel framework integrating agentic AI into O-RAN architectures. X-RIC combines reactive Reinforcement Learning (RL) with strategic agentic reasoning through: (i) automated Behavioral Cloning (BC) using domain heuristics for sample-efficient training, (ii) a Telecom Language Model (TLM), a transformer-based reasoning module providing contextual abstraction and interpretability, and (iii) closed-loop co-adaptation within the Near-RT RIC control loop enabling continuous policy refinement. To ensure deployment readiness, we introduce BARX (Benchmarking Agentic Reasoning for RAN), a domain-specific evaluation framework assessing agentic control across latency, compliance, and determinism metrics. We validate X-RIC on SLA-aware network slicing in simulation and O-RAN-compliant testbed deployments. X-RIC achieves 89% operational cost reduction while maintaining SLA compliance, converging 75% faster with 50% fewer training steps and 46% lower variance.

</details>


### 59. Author-in-the-loop Agentic Reproducibility Auditing for a Machine Learning Conference

- **Authors:** Yukun Dong, Linjun Zhang, Tian Zheng
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22465v1](http://arxiv.org/abs/2610.22465v1)
- **PDF:** [https://arxiv.org/pdf/2610.22465v1](https://arxiv.org/pdf/2610.22465v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reproducibility checks during peer review require a shared understanding of what authors' code is expected to reproduce. We present an author-in-the-loop collaborative audit that makes author declarations explicit inputs to an AI agent's investigation and assessment. A structured checklist records reproduction instructions and limitations; a two-stage workflow on GitHub connects agent checks to author clarification, revision, and agent reassessment. The agent separately assesses whether results have been reproduced and whether authors need to provide clarification or make repairs, while human reviewers approve requests and decide whether concerns are resolved. We deployed the system across 36 conference papers and 133 experimental tables and figures, raising 20 issues after human review. Further checks supported closing all the issues, although full reproduction remained unverified in some cases. We further compared repeated audits with complete and blank checklists to examine how author declarations shaped the agent's investigation and assessment. Our work contributes a collaborative workflow and agent design that use author knowledge to guide reproducibility auditing. The conference deployment provides empirical evidence that this approach can help identify and address reproducibility problems through collaboration among authors, agents, and reviewers.

</details>


### 60. Shortcut Sensitivity in Agent-Safety Evaluations

- **Authors:** Hasan Demirkiran, Jens Ernstberger
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22243v1](http://arxiv.org/abs/2610.22243v1)
- **PDF:** [https://arxiv.org/pdf/2610.22243v1](https://arxiv.org/pdf/2610.22243v1)
- **Categories:** cs.AI, cs.CR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents take actions through tools. Some actions are sensitive, so guards that supervise them must themselves be evaluated reliably. Yet the data used to evaluate a guard can include cues that make labels predictable without measuring the intended safety construct, and those cues can also influence guard decisions. We introduce a three-level shortcut-auditing framework and audit completed LinuxArena trajectories and two TS-Bench-derived step datasets. We distinguish label predictability, observational guard association, and paired decision sensitivity. In LinuxArena, shorter average shell commands strongly predict trajectory labels. In AgentDojo-Traj, exact-tool lookup falls from F_1=.901 with mixed-domain folds to .495 under domain holdout. In AgentHarm-Traj, released TS-Guard F_1 falls from .902 under row weighting to .719 with equal interaction weighting, while balanced accuracy rises. We then test the strongest safe-row marker association in a seven-configuration screen on a frozen 64-step AgentDojo-Traj cohort using repeated, interleaved Haiku calls. Rewriting the <INFORMATION> marker lowers blocking by 8.33 percentage points, while opaque tool aliases raise it by 11.46 points. All unsafe calls remain blocked; the changes concern false positives against inherited labels. Both effects remain nonzero after subtracting the formatting-placebo effect, with exploratory 95% ranges excluding zero. The same edits also change measured accuracy against inherited labels. This provides direct evidence that benchmark representation can materially change a guard's decisions and measured evaluation performance. The Haiku-sized effects do not reproduce in Luna or deterministic Q8 TS-Guard. We recommend domain group holdouts, evaluation-unit metrics, and placebo-controlled paired interventions.

</details>


### 61. Robust Multi-Agent Pursuit with Preemptive Communication via Reachability-Based Control Barrier Functions

- **Authors:** Madison Book, Justin Bradley
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22198v1](http://arxiv.org/abs/2610.22198v1)
- **PDF:** [https://arxiv.org/pdf/2610.22198v1](https://arxiv.org/pdf/2610.22198v1)
- **Categories:** eess.SY, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Safe multi-agent coordination typically assumes what real-world, deployed, resource-constrained robots cannot provide: continuous, perfect state sharing. Robust control strategies must be complemented with robust communication strategies to deliver resilient deployments. In this work, we propose a unified control/communication strategy that provides safe control to guarantee inter-agent safety under intermittent communication and demonstrate its effectiveness in a pursuit-evasion scenario. Each agent computes the reachable set of neighboring agents based on the last state information received, then solves for a safe control input based on control barrier functions to ensure agents avoid collision. We prove that inter-agent collision avoidance is guaranteed provided communication staleness remains bounded. As the reachable set inflates between state transmissions, each agent reasons about when to preemptively transmit its state information to neighboring agents based on novel metrics characterizing uncertainty risk and kinematic risk. We implement and simulate a variety of pursuit-evasion scenarios and show that preemptive communication reduces messages by 77.5% compared to periodic and event-triggered baselines with zero collisions.

</details>


### 62. HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration

- **Authors:** Yanchen Deng, Jianguo Huang, Yao Long Teng, Yixuan Li, Handuo Zhang, Ning Wang, Liangcai Su, Xinyu Wang, Bo An
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22195v1](http://arxiv.org/abs/2610.22195v1)
- **PDF:** [https://arxiv.org/pdf/2610.22195v1](https://arxiv.org/pdf/2610.22195v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Orchestrating multiple agents on a complex task requires reconciling local subtask execution with global task planning. Dynamic dispatch approaches provide execution flexibility but do not explicitly model subtask hierarchies or dependencies, while predefined workflows impose this structure but fix the decomposition before execution begins. Therefore, we introduce HTN-Orchestrate, a two-layer framework that separates these responsibilities through a hierarchical task network (HTN). The Planner maintains subtask hierarchies and dependencies, deferring decomposition until prerequisite results become available, while local Orchestrators schedule workers to execute each leaf subtask. Results propagate upward under \textbf{AND} semantics, and accumulated findings inform a rebuilt task network when the current decomposition cannot resolve the task. On five benchmarks spanning web research, scientific reasoning, and research workflows, HTN-Orchestrate outperforms ReAct, Agent Team, and DeepSeek Harness using the same base model, achieving 89.73% accuracy on BrowseComp and 73.44% on SUPERChem, exceeding Agent Team by 2.45 and 4.69 percentage points, respectively.

</details>


### 63. AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning

- **Authors:** Bingxiang He, Pengqi Sun, Shihao Peng, Shaoxuan Li, Huiyu Xiao, Hongjian Shi, Zixuan Fu, Ziqing Qiao, Yuxin Zuo, Cheng Qian, Xinqiang Yu, Jiayi Li, Xiusi Chen, Yizhen Song, Xiangyang Wang, Iofai Lei, Yudong Wang, Ning Ding, Zhiyuan Liu, Xiaozhi Wang, Chaojun Xiao
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22194v1](http://arxiv.org/abs/2610.22194v1)
- **PDF:** [https://arxiv.org/pdf/2610.22194v1](https://arxiv.org/pdf/2610.22194v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language model agents increasingly automate post-training, but when given the full training stack they converge on supervised fine-tuning and spend most effort revising training data. Existing systems give the agent one kind of control, selecting rows from a fixed pool or calling a generator, whereas a human data engineer adjusts proportions, prunes, repairs, replaces and synthesizes the data. We design a data action space for these changes and ask whether an automated system can make the full range rather than one of them, and what structure that requires. We first run this loop with a single agent, and it reaches only one action, adjusting category proportions, while its context fills with execution output and is discarded mid-search. We therefore introduce \textbf{AutoSFT}, a multi-agent system where a meta agent separates execution from analysis, gathers proposals from independent angles, and calls a synthesis subagent for capabilities the pool cannot cover, with the model, the trainer, and the budget fixed within each comparison. Adding each component in turn helps: the executor halves context loss, the analysis subagents lift the best IFEval by $+6.5$, and synthesis adds $+3.4$ IFEval and $+2.9$ IFBench. The same loop transfers to code, where analysis adds $+3.7$ MBPP+ over a single agent that does not improve. Every result comes from runs that retrain from the base model each round, so each component's effect is individually attributable. Our findings suggest that automating SFT data research depends more on covering diverse data actions than on a stronger single action.

</details>


### 64. Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions

- **Authors:** Liangjie Huang, Henry Peng Zou, Wei-Chieh Huang, Wooseong Yang, Yuwei Han, Philip S. Yu
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22138v1](http://arxiv.org/abs/2610.22138v1)
- **PDF:** [https://arxiv.org/pdf/2610.22138v1](https://arxiv.org/pdf/2610.22138v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM systems increasingly rely on groups of agents that discuss, critique, and check one another, assuming that peers will catch individual errors. We test this assumption against a minimal adversary. In a ten-agent factual discussion, one or three adversarial agents repeatedly assert a plausible false answer. After each round we probe each benign agent's private answer through a separate call whose response is hidden from its peers, and we separately label its public stance toward the claim. Across six models and three factual-QA datasets, groups remain stable without an attacker: only 0.6% of benign agents finish with the false answer. A single adversarial agent increases this rate to 44.8% and three to 60.5%. Studies of conformity typically report public agreement without private change; we find the reverse. With three adversarial agents present, benign agents hold the false answer in 51.6% of exposed turns but publicly endorse it in only 19.7%. Much of the influence therefore remains invisible in the discussion, and the false answers persist when agents are asked for their own views. Agents that retain the true answer often fail to defend it; once adopted, the false answer spreads among benign agents, and baseline knowledge does not predict robustness.

</details>


### 65. PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents

- **Authors:** Kshitij Mishra, Abhijith Sharma, Nils Lukas, Salem Lahlou
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22124v1](http://arxiv.org/abs/2610.22124v1)
- **PDF:** [https://arxiv.org/pdf/2610.22124v1](https://arxiv.org/pdf/2610.22124v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern agentic systems extend language models with external tools, enabling them to complete complex tasks through multi-turn interactions. As these agents are deployed in consequential settings, they are often constrained by policies governing pricing, privacy, confirmation, safety, and other requirements. However, existing evaluation methods leave a critical gap: capability benchmarks measure what agents can accomplish, while content-safety red-teaming measures harmful generations, but neither tests whether agents comply with predefined policies during otherwise valid tool use. Such policy violations are difficult to audit because their effects may emerge only after several turns, span multiple tool calls, or surface in downstream systems. We propose PROBE (Policy Rule Observation via Behavioral Exploration), an algorithm for training LLM-based auditors that interact with deployed agents as realistic users and probe them for policy violations through multi-turn, tool-mediated dialogue. We formalize agent auditing as a two-player Markov game and propose a composite reward that balances violation discovery, behavioral plausibility, conversation progress, and policy diversity. To study training objectives and reward design, we compare GRPO, DPO, and GFlowNet-based optimization in a controlled setting. Across extensive experiments, auditors trained with PROBE uncover substantially broader and higher-yield policy violations than same-architecture zero-shot adversaries, even when the auditor is significantly smaller than the target agent. Our results show that multi-turn behavioral auditing is a distinct and necessary axis of agent evaluation, complementing capability and safety benchmarks. PROBE offers a scalable path toward automated policy auditing for real-world agentic systems and suggests a co-evolutionary loop in which auditors expose failures and agents improve from auditor feedback.

</details>


### 66. FAOPs: Normal Forms and an Algebra for AI Agent Workflows

- **Authors:** Ali Mohammadi Shanghooshabad
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22061v1](http://arxiv.org/abs/2610.22061v1)
- **PDF:** [https://arxiv.org/pdf/2610.22061v1](https://arxiv.org/pdf/2610.22061v1)
- **Categories:** cs.AI, cs.DB, cs.PL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Organizations increasingly encode operational procedures as multi-step agent skills, here called Agent Operating Procedures (AOPs), that must be traceable, auditable, reproducible, access-controlled, and bounded in time and cost, requirements that regulated sectors make mandatory. Yet AOPs are typically kept as coarse-grained files, in which steps bundle actions, copied procedures drift apart, any step may reach any tool, and refactoring goes unchecked. We present Functional Agent Operating Procedures (FAOP), a formal theory that brings database-grade discipline to AI agent workflows. FAOP recasts each workflow as a typed function over scoped state and subjects an entire library to four progressive normal forms: Decomposed (FNF-1) splits a workflow into atomic steps, Typed (FNF-2) makes its data flow explicit and type-checked, Factored (FNF-3) gives each shared procedure a single canonical definition so a change propagates instead of drifting, and Scoped (FNF-4) confines every step to least-privilege tool access. Once normalized, every atomic step is a separate entity with a declared contract and can be type-checked, scope-confined, bounded, tested, traced, and audited on its own. A FAOP algebra of provably sound equalities turns refactoring and parallelization into compiler rewrites; orthogonal extensions add verified termination (+V), optimization (+O), and time and cost bounds (+B); and an architectural-level classifier (0-3) determines whether a workflow needs AI at all. Together, these make integrity, isolation, typing, termination, cost, and optimization compile-time concerns across the whole library, not runtime hopes. We implement the theory in SkillBase, an AOP management system (what PostgreSQL is to data, SkillBase is to AOPs), together with a separate executor that enforces these guarantees at run time. A worked financial workflow illustrates the approach end to end.

</details>


### 67. GraphACM: Graph-based Action Consistency Measurement for Uncertainty Quantification in LLM Agents

- **Authors:** Yaxin Ma, Wenbo Zhang, Satya Krishna Pothapragada, Alina Zare
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22031v1](http://arxiv.org/abs/2610.22031v1)
- **PDF:** [https://arxiv.org/pdf/2610.22031v1](https://arxiv.org/pdf/2610.22031v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Behavioral consistency across repeated executions provides an informative signal for assessing the reliability of large language model (LLM) agents. However, existing approaches typically summarize consistency with a single task-level score, without identifying where behavioral differences occur or whether actions are compared under equivalent decision contexts. We propose a graph-based framework for fine-grained behavioral consistency measurement and uncertainty quantification. Given multiple rollouts of the same task, we merge equivalent states into a directed, action-labeled graph, enabling action comparisons at shared decision states. We introduce node-level and global measures of action consistency, using the global consistency score as a proxy for uncertainty to predict task success or failure. Experiments across three LLMs on ALFWorld, AppWorld, and WebShop demonstrate that our measure is positively associated with task success and achieves an average AUROC of 0.811 for task-success prediction, outperforming the strongest behavioral-consistency baseline (0.729) and verbalized confidence (0.769). These results highlight the effectiveness of state-conditioned behavioral consistency and pinpoint where agent actions agree.

</details>


### 68. Augment the Cache, Replace the Activation: A 2x2 Study of Internal-State Sharing

- **Authors:** Adam Deng, Shicheng Liu, Yada Zhu
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22026v1](http://arxiv.org/abs/2610.22026v1)
- **PDF:** [https://arxiv.org/pdf/2610.22026v1](https://arxiv.org/pdf/2610.22026v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems built from frozen language models communicate through text, which discards the internal state the sender already computed and makes the receiver pay to rebuild it. Work on internal channels avoids that cost, framing the problem as transfer: agent A sends information to agent B. Every agent pair that must communicate needs its own transfer bridge, and every agent added to a system needs a new bridge fitted against each previous agent. We reframe this problem as sharing: an agent publishes its internal state once into a pool, and every peer reads that pool through a single mechanism fitted to no sender in particular, so adding an agent adds a publisher and no new bridge. Whereas the carrier of the internal state and the fusion mechanism are usually chosen independently in the literature, our main finding is that these two choices are coupled; the deciding factor is where the carrier enters the receiver's computation. Consumability is a property of the receiving computation rather than of the representation. We find that the key-value (KV) cache must be augmented rather than swapped in: the receiver cross-attends over a peer's cache while keeping its own, and with only a small query-side adapter trained, matches the accuracy it gets from reading the source document. Activations invert this. They are best written straight into the receiver, with no bridge, no adapter and no training, which beats exposing them alongside the receiver's own, though that advantage rests on knowing where in the receiver the state belongs. The rule is augment the KV cache, replace the activation, established under one protocol with a shared control ladder. One adapter, trained once, also serves publishers it never trained on, and a pool of several at once, but only those whose internal state lies close to the receiver's own.

</details>


### 69. Close Enough is Nowhere Near: Fidelity-Consumability Decoupling in KV Caches

- **Authors:** Adam Deng, Shicheng Liu, Yada Zhu
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22016v1](http://arxiv.org/abs/2610.22016v1)
- **PDF:** [https://arxiv.org/pdf/2610.22016v1](https://arxiv.org/pdf/2610.22016v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems communicate in text, which is lossy and wasteful: the sender throws away the reading it already did. A growing literature instead transmits the KV cache, the natural carrier of that reading. We study the most appealing form of the idea: both models stay frozen and the sender's cache is substituted for the reader's with nothing trained. It does not work, and the obstruction belongs to the reader. A frozen transformer reads only caches close to the one it would have written itself, a region we call its tolerable set. We show that geometric similarity to that cache does not predict whether the reader can use it, and the failure is not gradual, so a more faithful substitute is not the remedy it appears to be. We explain this phenomenon with competitive attention. Experimentally, we test eight diverse substitution methods against two measured anchors: an uninformative cache baseline and the reader's own accuracy from having read the passage. All sit at the baseline. That turns a long tail of separate negative results into one outcome with a stated condition for overturning it. A different design does work: if the reader keeps its own cache and attends over the sender's as extra context, adapting only its queries, it beats its own baseline, and also clears the baseline with eight senders pooled where undirected attention over the same union falls below it. We offer this as a characterization on one probe, not a leaderboard claim. Our central contribution is a redirection: pursuing faithful substitute caches is the wrong target; adding a cache to what the reader already has is the promising one.

</details>


### 70. Following Delegation Traces to Study Human Oversight in Interaction with Multimodal AI

- **Authors:** Agnese Chiatti, Matteo Matteucci, Viola Schiaffonati
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21948v1](http://arxiv.org/abs/2610.21948v1)
- **PDF:** [https://arxiv.org/pdf/2610.21948v1](https://arxiv.org/pdf/2610.21948v1)
- **Categories:** cs.HC, cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

As multimodal AI systems are becoming our everyday thought partners, the shift towards studying how users transfer control to these systems becomes especially urgent. In this paper, we report an overview of findings from an online study with n=56 AI-literate participants and 392 Video Question Answering trials. After inspecting each multimodal AI response, participants rated task-specific trust and selected one of three intended policies for an analogous future task: reject AI assistance, use it with verification, or delegate fully to the AI. Within participants, post-interaction trust strongly predicted the user's delegation choices (OR=14.97, 95% CI [7.14,31.37]). Trust and delegation nevertheless remained distinct. Verification was the dominant policy and often co-occurred with high trust. Delegation also increased with task order after adjustment for momentary and participant-level trust (OR=1.22, 95% CI [1.02,1.45]), indicating an experience-related component that self-reported trust ratings alone could not capture. These findings motivate a shift from intended delegation to a non-intrusive observation of how delegation is enacted in collaborative human-AI tasks. We therefore conclude by proposing enacted delegation traces as a methodological framework for future studies of multimodal and agentic AI use.

</details>


### 71. CodeHealth Predicts the Token Cost of Agentic Code Review: A Pre-Registered Study of 465 Agent-Authored Pull Requests

- **Authors:** Lo Gullstrand Heander, Markus Borg, Emma Söderberg, Christofer Rydenfält
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21914v1](http://arxiv.org/abs/2610.21914v1)
- **PDF:** [https://arxiv.org/pdf/2610.21914v1](https://arxiv.org/pdf/2610.21914v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Context: Organizations increasingly delegate code review to multi-agent large language model (LLM) pipelines billed per token. Low code quality raises human maintenance effort, but its effect on agent review cost has not been measured.
  Objective: We test whether baseline CodeHealth predicts the token cost of agentic review and fix beyond pull request (PR) footprint.
  Method: In a pre-registered observational study, we sampled 465 agent-authored PRs from 246 repositories in AIDev, jointly stratified by CodeHealth and footprint under repository caps. A frozen five-agent review-and-fix pipeline processed every PR with three different LLMs. Per LLM, we fitted a mixed model of log tokens on CodeHealth and log PR footprint, with a repository random intercept.
  Results: For all three LLMs the CodeHealth coefficient was negative, with 95% CI excluding zero; each CodeHealth point was associated with 3.5% to 6.1% lower token cost. CodeHealth was unrelated to PR footprint, so PR size does not explain the association. Two of three registered smells predicted fix cost; batch fixing left median CodeHealth unchanged. Exploratory analyses located the association in the review stage, where agents iterated more on unhealthy code without writing more comments. Adjusting for the size of the scored files absorbed the association, which we interpret as mediation by file size.
  Conclusions: A quality metric calibrated against human maintainability also predicts the inference cost of multi-agent review and fix. The effect is modest per point and not carried by PR size, so the refactoring case extends to agent-reviewed code when it changes structure and file size, not only the score.
  Data Availability: https://doi.org/10.5281/zenodo.22127920

</details>


### 72. Learning Rewards in Strategic Games

- **Authors:** Antoine Bergerault, Cyrille Kone, Giorgia Ramponi
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21912v1](http://arxiv.org/abs/2610.21912v1)
- **PDF:** [https://arxiv.org/pdf/2610.21912v1](https://arxiv.org/pdf/2610.21912v1)
- **Categories:** cs.GT, cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Understanding the objectives that drive agents' behavior is crucial in strategic environments, where multiple agents interact and adapt to one another. This challenge arises in domains such as cybersecurity, autonomous driving, and online markets, where agents' underlying incentives are typically unknown and must be inferred from their observed behavior. Inverse reinforcement learning (IRL) provides a natural framework for this problem, but extending IRL to strategic multi-agent settings introduces a fundamental challenge: a reward that explains observed behavior does not necessarily induce optimal strategies when used for decision-making. In this work, we study this problem through the lens of \emph{strategic identifiability}, and show that learning from a fixed policy pair can be insufficient to strategically identify rewards, independent of the number of expert samples $K$. Motivated by this, we introduce an active IRL algorithm for two-player repeated Stackelberg games, in which the leader adaptively selects policies to elicit informative responses about the follower's reward. Combining maximum-likelihood estimation with experimental design, we derive finite-sample guarantees on the Stackelberg sub-optimality induced by the learned reward, matching up to polylogarithmic factors a new minimax learning rate of $K^{-1/2}$. Finally, we evaluate our approach in a realistic anti-poaching setting, demonstrating the benefits of active exploration for reward recovery and downstream strategic performance.

</details>


### 73. From Research Goals to Scientific Closure: Evaluating Agents Through Evidence-Supported Physics Research

- **Authors:** Yijia Mao, Song Dai, Tao Chen, Xiangyu Lu, Linqian Zeng, Chenxi Hu, Sitong Zhou, Dongyang He, Xiaodan Mao, Linxuan Zhang, Tong Zhu, Yafu Li, Fangchen Yu, Peng Ye, Feng He, Yu Cheng, Yun Luo
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21767v1](http://arxiv.org/abs/2610.21767v1)
- **PDF:** [https://arxiv.org/pdf/2610.21767v1](https://arxiv.org/pdf/2610.21767v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Can AI agents organize scientific investigations that lead to well-supported conclusions? To evaluate this capability, we introduce PhysClosureBench, a benchmark of 50 expert-verified, goal-specified research tasks spanning strong-field, attosecond, and neighboring physics areas. Each task specifies the research objective and essential scientific constraints, while leaving the agent to organize the investigation and determine how to generate and validate the evidence needed to answer the question. A 20-criterion Atomic Score measures local scientific accomplishment, while Research Closure (RC0--RC4) assesses how fully the investigation resolves the specified research question based on whether its indispensable evidence requirements and applicable scope conditions are satisfied. We evaluate seven frontier LLMs, where Claude-Opus-5 achieves the highest mean Atomic Score (6.29/10) but reaches RC4 in only 32.7% of attempts. Across the benchmark, 36.2% of attempts scoring at least 8/10 still fall short of RC4, while all seven models reach RC4 on substantially fewer tasks in all three runs than in at least one. Case-level analysis further illustrates how misinterpretation of generated results and unresolved physical applicability limits can lead to incomplete closure. Together, these results reveal a persistent gap between AI agents' local scientific accomplishments and their ability to achieve complete research closure.

</details>


### 74. Human Interventions as Labels: Localizing, Steering, and (Sometimes) Editing the Computations Behind LLM Agent Failures

- **Authors:** Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21708v1](http://arxiv.org/abs/2610.21708v1)
- **PDF:** [https://arxiv.org/pdf/2610.21708v1](https://arxiv.org/pdf/2610.21708v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

When an LLM agent misbehaves, a human steps in, and that intervention is usually discarded or replayed as training data. We treat it instead as a measurement: a label pointing at the internal computation that failed. We study it in a controlled agent environment, on one failure (asking a clarifying question when the request was already unambiguous), with labels from a rule-based overseer validated against blind human judgment. Claims cover eligible models, which both over-ask and sometimes act on matched unambiguous requests: five of thirteen qualified (Qwen2.5-3B, gemma-2-2b, OLMo-3-7B, Mistral-Nemo-12B, Phi-4). Four findings. First, the ask-vs-act decision is causally localizable in every eligible family: a direction learned from intervention labels flips 72-100% of held-out over-asks at a definite residual-stream depth, with site and dose chosen on training data, and random directions under the same procedure flip at most one episode. Second, over-asking has two mechanistic signatures: in four families the model demonstrably knows the request is unambiguous (the belief is decodable, causally inert and orthogonal to the decision) and asks anyway; in the fifth, the rare over-asks track different world-representations. Third, steering gated on a probe readout removes most of the simulated oversight burden while legitimate questions survive (bootstrap 95% intervals exclude zero); a prompt instruction makes it worse. Fourth, consolidating the fix into the weights yields a map, not a rule: on one model a LoRA confined to the causal band passes every criterion fixed in advance while behavior cloning on identical data breaks retention; on three families the reverse holds; on the fifth the outcome crosses the boundary across seeds. A geometric rule written down in advance to predict the regime failed on two out-of-family tests; we report the failure and stop rather than fit a replacement.

</details>


### 75. Data World: Scaling Data Environments from Scratch

- **Authors:** Zhanli Li, Zeyuan Xu, Chaoxu Pang, Zeyuan Liu, Anyang Ji, Te Sun, Kongcheng Zhang, Wenbo Xu, Xubin Yue, Shipeng Luo, Junjie Zhao, Yingfan Hua, Jingqing Ruan, Zhongda Su, Feng Hong, Zhizhao Zeng, Ke Zeng, Xunliang Cai, Hanjia Ye
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21656v1](http://arxiv.org/abs/2610.21656v1)
- **PDF:** [https://arxiv.org/pdf/2610.21656v1](https://arxiv.org/pdf/2610.21656v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Data agents use code to process heterogeneous files and derive analytical insights. Scaling their training faces costly environment curation, privacy and intellectual-property restrictions, and difficulty verifying open-ended findings without known generative truth. Our core insight is to specify the world behind the files before generating the files themselves. We introduce Data World, a multi-agent engine that synthesizes environments, tasks, and rubrics from explicit mechanisms. Independent audits check target recoverability from observed files; rubrics support evaluation and RL rewards. Human preference-based curation for question realism selects 100 tasks across 50 held-out worlds and 16 domains for DataWorld-Bench. The engine also yields 2,135 training tasks from 1,037 disjoint worlds. Evaluation of ten frontier models shows that the benchmark remains challenging, particularly for insight discovery, with a consistent computation-insight gap. RL-zero training on the synthesized tasks produces DataWorld-35B-A3B from Qwen3.6-35B-A3B without trajectory distillation. Under matched evaluation, it improves over its base by 7.06 points on DataWorld-Bench, 14.28 on DAComp, 20.90 on DABstep-Hard, and 12.13 on JobBench, a broader occupational benchmark.

</details>


### 76. AgentPerturb: Evaluating LLM Agent Robustness under Controlled Interaction Perturbations

- **Authors:** Yuanjian Xu, Jinyi Han, Jianing Hao, Yuxuan Sun, Fanyang Lu, Richeng Xuan, Guang Zhang, Zhichao Hu
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21624v1](http://arxiv.org/abs/2610.21624v1)
- **PDF:** [https://arxiv.org/pdf/2610.21624v1](https://arxiv.org/pdf/2610.21624v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Real-world tasks are often complex and noisy, posing substantial challenges for LLM agents. Yet existing evaluations lack a systematic framework for jointly characterizing potential perturbation targets and types. We use this two-dimensional view to conduct a unified study that quantifies the robustness of current frontier models, traces the mechanisms behind perturbation-induced failures, and draws implications for robustness-oriented training. Through controlled evaluations on APEX-Agents and Toolathlon, we find that perturbations consistently degrade performance, while the dominant vulnerabilities vary across task environments. Trajectory-level analysis reveals that agents rarely recognize altered inputs and often propagate corrupted information without verification. A focused cost analysis further shows that successful perturbed trajectories can require substantially more computation. These findings motivate training objectives that cover diverse forms of noise and reward verification, uncertainty awareness, and recovery. We provide a rigorous benchmark-construction pipeline. Code and data will be released at https://github.com/xuyj233/AgentPerturb.

</details>


### 77. Independent Data-Integrity Verification for LLM-Driven Functional Coverage Closure in Hardware Design

- **Authors:** Venkata Krishna Kumar Vedantam
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21570v1](http://arxiv.org/abs/2610.21570v1)
- **PDF:** [https://arxiv.org/pdf/2610.21570v1](https://arxiv.org/pdf/2610.21570v1)
- **Categories:** cs.AR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents can write directed tests that close functional coverage, but coverage only shows that a state was reached, not that the data on the way there was correct. This is a long-known point in verification and we do not claim it as new. We describe a small coverage-closure agent that applies it to an LLM loop: coverage is read from the report that the simulation itself exports (cocotb-coverage YAML) and never taken from the model's account, and data integrity is checked by scoreboards that are separate from the model. On three architecturally distinct RTL designs (an asynchronous FIFO, a UART transmitter and an AHB2APB bridge) the agent raised coverage from 91.7%, 88.9% and 67.4% to 100% within its 8-iteration budget in every logged run, using one design-agnostic agent. A reactive scoreboard monitor attached to the FIFO's base testbench also found a clock-domain-crossing bug in the author's own stimulus code. The monitor is not yet attached to the LLM-generated tests, so their data integrity is not independently checked; one manual check on a single FIFO test is reported as preliminary. We list the weaknesses of this evidence: three designs, no baseline, no ablation, and logged runs that come from several agent checkpoints.

</details>


### 78. Agent Status Protocol (ASP): A Lightweight Specification for State Reporting in Multi-Agent Systems

- **Authors:** Diego Gosmar, Deborah A. Dahl, Emmett Coin, Csaba Bolyós, Andreas Zettl
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21538v1](http://arxiv.org/abs/2610.21538v1)
- **PDF:** [https://arxiv.org/pdf/2610.21538v1](https://arxiv.org/pdf/2610.21538v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Agent Status Protocol (ASP) defines a lightweight way for heterogeneous AI agents to report their operational state to a status server, and for observers such as dashboards to receive that state as soon as it changes. Agents push small JSON events over HTTP POST; the server exposes the aggregated state to observers over Server-Sent Events (SSE). Because an agent that has crashed, hung or been compromised cannot be trusted to report its own failure, ASP does not rely on self-reports alone: the server infers liveness from missed heartbeats, can detect agents that are alive but no longer making progress, and accepts observations from supervisors, guardrails, operators and peers, some of which take precedence over what the agent says about itself while others are shown alongside it. ASP models state along independent dimensions (lifecycle, health, task, floor, governance), so that an agent can be, for example, online, degraded, working on a task and waiting for the floor at the same time. It reuses existing vocabularies: task states from the Agent2Agent (A2A) protocol, floor states from the Open Floor Protocol (OFP), and attribute conventions from the OpenTelemetry GenAI semantic conventions. This paper presents version 0.1 of ASP as a proposal, not as an approved standard. It is a working draft intended to open a discussion, and the authors invite comments, alternative proposals and independent implementations from the community.

</details>


### 79. Incentivizing Tool-Use Reinforcement Learning for Post-Arrival Emergency Care Prediction

- **Authors:** Pengfei Hu, Chenwei Wu, Qiao Jin, Jun Deng, Zhiyong Lu, Liyue Shen, Yue Ning
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21449v1](http://arxiv.org/abs/2610.21449v1)
- **PDF:** [https://arxiv.org/pdf/2610.21449v1](https://arxiv.org/pdf/2610.21449v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) can reason over both structured measurements and free-text records, which makes them attractive for emergency department (ED) prediction. However, most existing LLMs still fall short of conventional ML methods like trees on EHR-based prediction tasks. Our controlled analysis traces this gap to two weaknesses: LLMs do not select informative features, and they misjudge what numerical values imply for risk even when given the right features. We propose TIR-EC, a tool-integrated reinforcement learning framework that addresses both. TIR-EC exposes EHR feature groups as tools the LLM can call. It trains the LLM with rewards from a gradient-boosted tree teacher, which provides a reference set of informative tools and a graded risk target. TIR-EC also distills task-specific clinical skills into the model weights through a reverse curriculum that gradually removes the skills from the prompt during RL process. Evaluation on three clinical prediction tasks shows that our 4B agent achieves the highest macro F1 of all compared models, outperforms conventional ML baselines, and is competitive with much larger frontier LLMs. Further analysis shows that TIR-EC selects more useful evidence with fewer tool calls and combines measurements more effectively.

</details>


### 80. Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows

- **Authors:** Kaixiang Wang, Zhaijiacheng Zhou, Jiong Lou, Jie Li
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21411v2](http://arxiv.org/abs/2610.21411v2)
- **PDF:** [https://arxiv.org/pdf/2610.21411v2](https://arxiv.org/pdf/2610.21411v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems rely on generative models for expert execution, workflow planning, and artifact review. Yet many coordination operations require only bounded decisions, such as selecting the next expert or judging artifact quality. Profiling three representative MAS frameworks, we find that routing and review account for 31.7-43.5% of generative-LLM tokens. However, replacing these operations with low-cost decision models introduces two interface gaps: generative planners produce execution plans and handoff instructions (planning gap), while reviewers provide actionable feedback for repairing flawed artifacts (review gap), which bounded decisions alone cannot provide. We introduce Jev-LiteMAS, a multi-agent framework that bridges both gaps by combining a lightweight decision model (Jev) with generative execution and feedback. To address the planning gap, Jev selects experts dynamically from the task and prior expert outputs, using accumulated context to ground subsequent execution without a pre-generated trajectory. To address the review gap, Jev screens intermediate artifacts against task criteria: passing artifacts proceed directly, whereas flagged ones undergo LLM re-review for acceptance or corrective feedback. Across four benchmarks and two backbones, Jev-LiteMAS reduces generative-LLM tokens by 12.7-54.6% over LAS, maintaining accuracy within 1.34 percentage points and lowering latency in seven of eight settings. Grounding routing in substantive expert outputs prevents up to 18.0 points in accuracy loss.

</details>


### 81. MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents

- **Authors:** Cheng Zhang, Xuanning Cao, Zhicheng Zheng, Hui Xiong
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21405v1](http://arxiv.org/abs/2610.21405v1)
- **PDF:** [https://arxiv.org/pdf/2610.21405v1](https://arxiv.org/pdf/2610.21405v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-term memory has become a crucial component of large language model (LLM) agents, with most research focusing on retrieving relevant information accurately and efficiently. However, a dependable memory system must also forget sensitive user data upon request. To evaluate this capability, we introduce MemCut, a systematic benchmark for user-requested forgetting. Its 456 hand-designed secrets in long-horizon conversations have fully annotated evidence trails to test recovery after deletion, including from messages that never state the secrets directly. We propose two recovery metrics. Native recovery measures reader success through the system's retrieval, whereas residual recovery measures the same reader's success when directly given surviving objects traced to annotated disclosures or evidence. We establish three reference deletion baselines to test how far existing retrievers and write models support forgetting across five memory designs and four LLMs. Disclosure removal reduces native recovery far more than residual recovery. LLM-guided deletion of ten additional turns from twenty retrieval candidates leaves 39-76% residual recovery. Subset sweeps (144 facts, three systems, two models) show that widening the pool at a fixed budget reduces residual recovery more than deleting all original candidates. These sweeps identify candidate coverage as a bottleneck in the reference baselines.

</details>


### 82. Matoi: Selective Revalidation of Consequence Evidence for Agent Authorization

- **Authors:** Zexun Wang
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21394v1](http://arxiv.org/abs/2610.21394v1)
- **PDF:** [https://arxiv.org/pdf/2610.21394v1](https://arxiv.org/pdf/2610.21394v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Matoi separates reusable consequence evidence from current execution authority and durable occurrence history. Its finite query-aware contract covers branches, ordered collections and negative lookups. A consumer reuses only its own checked evidence whose observations remain valid; signed requests, live grants, quota and uncertain outcomes remain separate obligations. Conditional correctness arguments distinguish locally serialized claims from nontransactional remote effects. Two studies strengthen cost attribution and domain evaluation. A 1,440-cell matched-wire study repeats 144 authored inputs. With compact input bytes identical, reuse reduces complete lifecycle cost by 3.49 percent in JS and 1.79 percent in Python. Combined representation/reuse reductions against full proof are 10.87 and 16.53 percent; five of twelve family intervals for the matched comparison cross one in each language. A prospectively frozen AgentDojo Banking mapping covers 5/16 user plans and 7/9 attack plans. Both governed strategies preserve five exact benign transfers and refuse 35 reused attack-plan/policy crosses. Pre-satisfied utility predicates are reported separately from completed work. These are original scripted synthetic tools, not autonomous agents or a real bank. Earlier studies retain cheaper protected-cache alternatives, policy-compatible phishing, provider duplication and post-claim revocation. Separate JS/Python consumers establish finite-profile interoperability within the same project; durable recovery rechecks evidence and retains uncertain reservations. The results support a bounded, auditable reuse and execution contract, not a new general incremental algorithm, arbitrary-tool closure, atomic third-party commitment or production superiority.

</details>


### 83. PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems

- **Authors:** Han Shen, Qifu Tyler Sun, Fanyang Meng, Ye Wang, Yongsheng Liang
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21390v1](http://arxiv.org/abs/2610.21390v1)
- **PDF:** [https://arxiv.org/pdf/2610.21390v1](https://arxiv.org/pdf/2610.21390v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent large language model (LLM) systems are increasingly deployed at the edge to support complex tasks that require collaboration and information exchange among multiple agents. However, when task contexts are passed across agents, shared context that has already been processed by upstream agents often needs to be prefilled again, resulting in substantial redundant computation. Reusing an already prefilled key--value (KV) cache can avoid this recomputation, but requires the reusable KV state to be transferred across the network before the receiving agent can begin generation. Under strict time-to-first-token (TTFT) deadlines and unreliable edge links, delivering the complete KV cache may be infeasible, making it necessary to prioritize and protect the most valuable KV information within a limited transmission budget. This paper proposes PriorityFEC, a utility-aware KV-cache handoff scheme that jointly exploits model-side KV importance and transport-side reliability. PriorityFEC first constructs a utility-aware source stream by placing high-utility KV blocks at earlier transmission positions. It then protects the ordered stream using a feedback-adaptive Streaming Forward Erasure Correction (FEC) mechanism, which schedules repair packets according to receiver feedback before the TTFT deadline. We implement PriorityFEC on a distributed edge LLM serving prototype and evaluate it with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct across multiple datasets. Results show that PriorityFEC achieves superior task quality over the compared transport schemes, with its advantages becoming particularly pronounced under stringent deadline constraints. These results demonstrate the importance of jointly optimizing KV-cache utility and deadline-aware transport reliability when reusable LLM state must be handed off across unreliable edge networks.

</details>


### 84. DocPilot: Interactive Agent Orchestration and Training for Long Visual Document Understanding

- **Authors:** Zhuowen Liang, Xiaotian Lin, Yuyu Luo, Haixun Wang, Nan Tang
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21327v1](http://arxiv.org/abs/2610.21327v1)
- **PDF:** [https://arxiv.org/pdf/2610.21327v1](https://arxiv.org/pdf/2610.21327v1)
- **Categories:** cs.AI, cs.CL, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal long-document question answering requires models to seek sparse evidence across pages and modalities, understand heterogeneous document content, and reason over the collected evidence. Even advanced vision-language models (VLMs) can overlook sparse evidence and struggle with cross-modal reasoning in a single pass. Existing document agents further introduce multi-step interaction, but some still rely on predefined workflows or coarse-grained actions, limiting the flexibility and granularity of document reasoning. We introduce DocPilot, an agentic document framework that supports expressive orchestration and makes complex document solving learnable by small language models (SLMs). DocPilot orchestrates evidence seeking through page-level navigation and fine-grained evidence localization, and integrates local visual inspection, code-based numerical reasoning, and cross-modal reasoning for multimodal understanding. To transfer these capabilities to small models, we propose curriculum-based agentic training that progresses from single-ability learning to adaptive orchestration through supervision from data-grounded reasoning traces and executable interaction trajectories. Across MMLongBench-Doc, DocBench, FinRAGBench-V, and MADQA, DocPilot achieves strong gains with frontier VLM backbones, while DocPilot-4B delivers competitive performance against substantially larger models, demonstrating strong effectiveness and generalization across diverse long-document reasoning settings. The code is available at https://github.com/HKUSTDial/DocPilot.

</details>


### 85. Constrained Multi-Agent Reinforcement Learning in Imagination

- **Authors:** Raz Shmueli, Shahaf S. Shperberg
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21319v1](http://arxiv.org/abs/2610.21319v1)
- **PDF:** [https://arxiv.org/pdf/2610.21319v1](https://arxiv.org/pdf/2610.21319v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Predicting cost in a multi-agent world model moves most constrained policy updates into imagination: the stronger model-free baseline needs $10$ to $20$ times CA-MAMBA's interactions on the median SMAC configuration, and CA-MAMBA earns $2.8$ to $12$ times the baselines' MAMuJoCo reward at equal budget. In controlled tests on one task per benchmark, pricing the model's cost advantages at parity more than halves a cost-blind learner's cost and meets a tight continuous-control limit the learned multiplier misses, suggesting the model's cost estimates are not the bottleneck.

</details>


### 86. VALCON: Benchmarking and Enhancing Value Consistency in Large Language Models via Dual-Role Variation

- **Authors:** Junru Wu, Jingting Zheng, Yuqi Ren, Deyi Xiong
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21304v1](http://arxiv.org/abs/2610.21304v1)
- **PDF:** [https://arxiv.org/pdf/2610.21304v1](https://arxiv.org/pdf/2610.21304v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Current value alignment evaluations for large language models (LLMs) heavily rely on output compliance, overlooking whether LLMs maintain value consistency when alternating between generator and evaluator roles. Such consistency is increasingly important because modern LLM agents and alignment pipelines often rely on the same LLM to both generate actions and evaluate their acceptability. To mitigate this limitation, we propose VALCON, a role-driven data construction framework that operationalizes value consistency into three benchmark suites (VAB-Consistency, VAB-Boundary, VAB-Challenge) via dual-role variation. By systematically pairing an LLM's generative behavior with its evaluative judgments under identical principles, VALCON synthesizes target evaluation data that exposes hidden value discrepancies. Experiments on 28 LLMs reveal pervasive cross-role inconsistency: models with highly compliant outputs frequently fail to align their judgments with their own generations. To understand and address this gap, we perform mechanistic probing that uncovers a role-dependent representational decoupling associated with this behavioral asymmetry. Guided by these insights, we propose a representation-directed intervention that effectively mitigates consistency failures. Our work establishes value consistency as a distinct alignment dimension and provides a complete evaluation-analysis-mitigation pipeline. Code and data are available at https://github.com/tjunlp-lab/VALCON.

</details>


### 87. Bias Control and Injection for Multi-Agent Aggregation

- **Authors:** Sungjae Lee, Soheil Abbasloo, Jabin Koo, Jungseul Ok
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21290v1](http://arxiv.org/abs/2610.21290v1)
- **PDF:** [https://arxiv.org/pdf/2610.21290v1](https://arxiv.org/pdf/2610.21290v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent reasoning with large language models (LLMs) raises a central question for collective decision-making: when agents disagree, whose decision should be trusted? Resolving such disagreements is difficult because agents' decisions are susceptible to non-semantic biases such as majority pressure and response-style preferences, which can obscure the quality of the underlying reasoning. Our analysis shows how bias can be both mitigated and exploited: bias control improves initial answer selection, while bias injection elicits decision instability that serves as a reliability signal. Building on these findings, we introduce a test-time aggregation framework that requires neither validation data nor prior knowledge of relative model strength. The framework implements bias control by presenting one style-normalized reasoning trace per distinct answer, and bias injection by placing each aggregating agent's initially selected answer in the minority. Overall, our framework achieves higher average accuracy and better token efficiency than competing non-oracle aggregation methods across three mathematical reasoning benchmarks and four heterogeneous LLM combinations. It also improves final-answer accuracy when applied to multi-agent debate and Mixture-of-Agents, without modifying their interaction or synthesis processes.

</details>


### 88. Auditing Escalation Reliability in Healthcare LLM Agents: A Perturbation-Controlled Benchmark of Workflow-State Failures

- **Authors:** Zihao Zheng, Junyi Yao, Baichuan Li, Jiayu Long
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21270v1](http://arxiv.org/abs/2610.21270v1)
- **PDF:** [https://arxiv.org/pdf/2610.21270v1](https://arxiv.org/pdf/2610.21270v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Trustworthy biomedical AI requires reliable action selection when evidence is missing, stale, conflicting, or late, not only accurate answers on static inputs. We instantiate an episode-level evaluation protocol as 400 synthetic healthcare workflow episodes: 40 hand-authored semantic seeds across four task classes, two surface parameterizations, and five controlled variants, scored on ANSWER/ASK CLARIFICATION/ABSTAIN/ESCALATE under a pre-declared 5:1 missed-versus-unnecessary escalation cost. Reference actions are single-author study-policy labels, not clinician-adjudicated ground truth. Across five open-weight configurations (1.7B--9.7B), clean decision accuracy reaches 0.97, yet uncertainty-prompted models miss 32--97% of required escalations. The stronger 9.7B configuration narrows but does not remove the gap, falling from 0.97 clean accuracy to 0.78 under conflict. Verbalized confidence is inconsistent (ECE 0.10--0.54; failure AUROC 0.48--0.77), and a development-tuned confidence-only policy yields no utility gain. A transparent workflow-aware controller improves 5:1 utility for every model and reduces missed escalations to 0.12--0.24, at specificity 0.83--0.93. However, a 30-concept lexical stress test reduces each rule detector's recall from 1.00 on trigger phrases to 0.00 on unseen paraphrases, limiting the controller claim to this benchmark. Seed-clustered statistics, ablations, cross-task transfer, raw outputs, and manifests are packaged for audit. The results motivate explicit workflow-state evaluation while showing that apparently effective routing controls need their own generalization tests.

</details>


### 89. PRIME: Towards Verifiable Evidence-Grounded Reasoning in LLM Agents

- **Authors:** Hamed Khosravi, Xiaoming Huo
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.22426v1](http://arxiv.org/abs/2610.22426v1)
- **PDF:** [https://arxiv.org/pdf/2610.22426v1](https://arxiv.org/pdf/2610.22426v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are used to check records against an organization's requirements, for example whether a vulnerability report is ready for investigation. Requirements often allow several ways to be met, such as a severity rating with a curator-reviewed advisory or a published advisory link. Agents fail by accepting a report after a required check has failed, or by settling for a weaker conclusion without trying another way that could still succeed. We introduce PRIME (Precommitted Rules for Inference from Minimal Evidence). Before checking, it fixes evidence routes specifying how each conclusion may be justified. A separate program records each check result and refuses any conclusion the results do not justify. It also points the agent to checks that could justify a stronger conclusion, or runs them itself. PRIME reports only conclusions authorized by its rules and ledger. With correct requirements, exact checks at known locations, and sufficient budget at stopping, completion reaches the strongest supported conclusion. On 480 public-record tasks, an agent shown the requirements reported unjustified conclusions on 26.7% of tasks, while PRIME reported none. Its directions and added checks raised the average score for justified conclusions from 30.1, with refusal alone, to the maximum of 59.2 out of 100.

</details>


### 90. TRACER: Trajectory-Aware Tool Retrieval for LLM Agents

- **Authors:** Tanish Kher, Sarvesh DK, Abedelkadir Asi, Sparsha Chennarayapatna Sundaresh, Dezhi Hong
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21267v1](http://arxiv.org/abs/2610.21267v1)
- **PDF:** [https://arxiv.org/pdf/2610.21267v1](https://arxiv.org/pdf/2610.21267v1)
- **Categories:** cs.CL, cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern agents select tools from registries, but exposing entire registries incurs high token costs and can impair selection as they grow. We present TRACER, a retrieval front-end that indexes observed tool-call sequences in a trie and ranks continuations using a learned blend of empirical and contextual priors. On a mixed retail-and-telecom $τ^2$ environment, TRACER improves GPT-5.4's tool-selection accuracy by 4.7 points while reducing input tokens per step by 80%, exposing just 5 of 128 tools. In autonomous full-turn execution, it matches GPT-5.4's full-registry task success with 61% fewer input tokens per step. Across six environments and four models, TRACER improves tool-selection accuracy over full-registry selection in 21 of 24 model-environment pairs, with average gains of 6 to 10 points; the three exceptions trail by at most 2.2. We analyze failures in both regimes to identify directions for future work.

</details>


### 91. TRACER: A Multimodal Harness for Patient Care in Hospitals

- **Authors:** Zane Durante, Paul Tang, Keshigeyan Chandrasegaran, Amit Kaushal, Shrinidhi Kowshika Lakshmikanth, Feolu Kolawole, Yu Jun Zheng, Yifan Geng, Shobhit Agarwal, Kevin Schulman, Juan Carlos Niebles, Ehsan Adeli, Arnold Milstein, Li Fei-Fei
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21266v1](http://arxiv.org/abs/2610.21266v1)
- **PDF:** [https://arxiv.org/pdf/2610.21266v1](https://arxiv.org/pdf/2610.21266v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Continuous video and clinical records provide complementary information for understanding how patient behavior evolves over a hospital stay. A central challenge is how to represent behavior across the entire stay while preserving access to fine-grained visual and clinical evidence. We introduce TRACER, a training-free multimodal harness that constructs minute-level action records from video and combines them with clinical records into hourly reports. The harness equips an LLM agent with tools to query this hierarchy, inspect relevant video, and retrieve clinical records. To evaluate TRACER, we construct two benchmarks. The first contains 397 annotated one-minute clips spanning 15 atomic actions; the second poses 144 clinician-informed multiple-choice questions, grounded in 264 hours of video and clinical records from two ICU patients. TRACER achieves up to 84.8% accuracy for action detection and 61.0% QA accuracy versus 49.3% for the strongest baseline using the same backbone. Across 280 patients spanning approximately 60,000 camera-hours, TRACER identifies significantly less purposeful activity in patients with a positive delirium assessment during their stay than in those without (p < 0.0001). Our results show that combining continuous video with clinical records can support understanding of patient behavior over time and across patient cohorts without training on protected health data.

</details>


### 92. A Responsibility-Centered Coordination Mechanism for Decentralized Multi-Agent Systems

- **Authors:** Thi-Nhung Nguyen, Viet-Thanh Pham, Linhao Luo, Thuy-Trang Vu, Dinh Phung
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21243v1](http://arxiv.org/abs/2610.21243v1)
- **PDF:** [https://arxiv.org/pdf/2610.21243v1](https://arxiv.org/pdf/2610.21243v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Centralized orchestration provides comprehensive multi-agent coordination but creates bottlenecks in scalability, adaptability, and collective performance. Decentralized approaches alleviate these bottlenecks by distributing coordination across agents, yet often leave responsibility for delegated dependencies and failure recovery unclear. To address this gap, we propose RCM, a responsibility-centered coordination mechanism that leverages commitments to couple task delegation with explicit responsibilities of the involved parties. Through recursive delegation, agents retain their upstream responsibilities while locally orchestrating downstream commitments, thereby preserving accountability across delegation chains, creating a network of local orchestration. We operationalize this mechanism locally through responsibility-constrained decision-making and a responsibility-oriented communication protocol (RCP), enabling agents to autonomously establish, manage, and terminate commitments. As agents act in parallel, their local actions continuously evolve the commitment graph, allowing global coordination to emerge and adapt toward a shared mission without centralized control. Experiments across reasoning, coding, and executable agent environments demonstrate that RCM outperforms strong centralized and decentralized coordination baselines by up to 18.7 points in task performance and 10.2 points in Responsibility, while improving failure and harm detection without task-specific training.

</details>


### 93. AutoOnboarder: Autonomously Onboarding LLM Agents

- **Authors:** Tanay Arora, Cong Liu
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21218v1](http://arxiv.org/abs/2610.21218v1)
- **PDF:** [https://arxiv.org/pdf/2610.21218v1](https://arxiv.org/pdf/2610.21218v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic large language models have been documented to lose reasoning capability when placed inside a harness, the software that mediates their observations and actions. To reconcile these losses, we introduce AutoOnboarder, an autonomous system that adapts an agent to a task the way a trainer onboards a new employee. It places the agent under the supervision of an intelligent ``Onboarder'' coding agent, which iteratively tailors its foundation model, prompt, and harness source code to simultaneously improve performance and decrease cost. Like a real onboarding process, the Onboarder is only given tens of examples, and all evaluation data is isolated on a separate virtual machine to prevent leakage. We report the lessons learned from building and testing AutoOnboarder on genomic-sequencing prior authorization form submission. Autonomously onboarded agents are able to match or exceed the performance of a Gemini 3.5 Flash baseline at up to 29$\times$ lower costs. However, these agents remain imperfect, and the Onboarding process varies greatly in terms of final performance. We conclude that future Onboarding systems require a robust environment for the Onboarder, including a structured thought interface, (controlled) internet access, and a wide model search space.

</details>


### 94. MemScope: Evolving Agent Memory Architectures through Localized Code Repair

- **Authors:** Miao Su, Yucan Guo, Zixuan Li, Long Bai, Zhongni Hou, Xiaolong Jin, Jiafeng Guo
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21170v1](http://arxiv.org/abs/2610.21170v1)
- **PDF:** [https://arxiv.org/pdf/2610.21170v1](https://arxiv.org/pdf/2610.21170v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent memory architectures define how LLM agents store and reuse experience across tasks, but they are typically fixed after deployment, limiting their adaptability across task types. Recent self-evolving approaches instead adapt these memory architectures using execution feedback, typically represented as evaluation scores or compressed summaries. However, such coarse-grained feedback is insufficient for precise failure localization in current agent systems, where long-horizon task execution involves multiple interacting components. Without a precise failure location, existing approaches lack a clear code-level target for modification, leaving the update scope weakly constrained and often leading to large-scale rewrites of an otherwise capable memory architecture. We propose MemScope, a framework for evidence-grounded, localized evolution of an existing memory architecture. Its tool-using Patch Agent jointly inspects raw execution traces, runtime memory state, and current architecture code to identify repair targets and apply bounded, in-place edits under provider-identity and memory-compatibility constraints. On GAIA, the trace-and-memory inspection variant achieves 86.67% accuracy, compared with 70.00% for trace-only and 63.33% for summary-only feedback. Under xBench tasks, the evolved memory architecture improves over its original version from 49 to 55 correct answers with DeepSeek V3.2 and from 50 to 53 with Kimi K2.7 Code. On disjoint ALFWorld unseen tasks, success rises from 50.75% to 71.64%. Across archived architecture-snapshot transitions, the median code-change ratio is 4.4%. These results support fine-grained execution evidence as a basis for localized, in-place memory-architecture evolution.

</details>


### 95. SSR: Structural Signal Retriever for Scalable Agent Discovery in LLM-Orchestrated Multi-Agent Systems

- **Authors:** Giancarlo Maldonado Cárdenas, Carlos A. Astudillo, Nelson L. S. da Fonseca
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21113v1](http://arxiv.org/abs/2610.21113v1)
- **PDF:** [https://arxiv.org/pdf/2610.21113v1](https://arxiv.org/pdf/2610.21113v1)
- **Categories:** cs.MA, cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large-scale multi-agent ecosystems require mechanisms for discovering suitable agents without exposing entire registries to a large language model (LLM) orchestrator. The challenge is not only to retrieve relevant Agent Cards from a growing registry, but also to maintain a compact candidate context, since each additional candidate increases prompt size, inference cost, latency, and the risk of exceeding the model context window. We formulate this problem as candidate-context scalability and propose the Structural Signal Retriever (SSR), our deterministic and training-free retrieval method designed for Agent Card discovery. SSR derives structural lexical signals from capability-bearing Agent Card fields, weights them using inverse document frequency (IDF), and uses an Inverted Signal Index (ISI) for selective candidate scoring. We evaluate SSR using a synthetic agent benchmark, a public MS MARCO adaptation, and end-to-end LLM orchestration. At 1,000 agents, SSR reduces LLM input by 98.8% and orchestration latency by 70.9% relative to full-catalog orchestration. On MS MARCO, IDF improves retrieval effectiveness within the structural representation, while the ISI preserves retrieval effectiveness and reduces explicitly scored passages by 96.8%. End-to-end experiments show that candidate pre-selection maintains a compact candidate context as registry size grows and avoids the operational failures observed with full-catalog orchestration. These results support SSR as an Agent-Card-native, traceable retrieval mechanism for candidate-context scalability.

</details>


### 96. Kolab: Benchmarking Human-Agent Collaboration in Long-Horizon Workflows

- **Authors:** Shirley Anugrah Hayati, Patricia Anugrah Setiani, Ruizi Wang, Zhouyi Li, Khanh Chi Le, Young-Jun Lee, Dongyeop Kang
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21109v1](http://arxiv.org/abs/2610.21109v1)
- **PDF:** [https://arxiv.org/pdf/2610.21109v1](https://arxiv.org/pdf/2610.21109v1)
- **Categories:** cs.AI, cs.CL, cs.HC, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

When humans collaborate with AI agents on long-horizon tasks, what happens to the agents' contributions? For solving long-horizon tasks, humans place greater importance on ongoing interaction with AI agents (e.g., revising plans) than on an agent's ability to complete the task in a single attempt. However, most agentic benchmarks have focused more on automation. Strong performance on such benchmarks does not imply effective real-world collaboration. Professional workflows offer a useful setting, as they often involve interdependent steps. To address this gap, we introduce Kolab, a new dataset of 115+ hours of screen recordings of 50 professionals from 40 occupations collaborating with agents on realistic, long-horizon problems. Kolab also contains participants' collaboration and output quality judgments. Our analysis reveals diverse collaboration patterns, highlighting the importance of when and how professionals coordinate with agents. A collaborative agent must do two things that automation benchmarks never test: anticipate whether experts will adopt, modify, or reject its contribution once it leaves the chat window to guide its next steps, and assess collaboration quality from the unfolding workflow without constant expert feedback. Our benchmark operationalizes both: (1) forecasting how professionals use agent contributions at diverse workflows, and (2) verifying their judgments of collaboration satisfaction and output quality. Findings show that frontier models, both agentic and non-agentic, overestimate collaboration with experts and struggle to distinguish between high- and low-quality collaboration. Longer workflow context does not consistently improve these predictions. As frontier agents cannot yet understand long-horizon collaboration with experts, we position Kolab as a valuable dataset for studying human-agent collaboration grounded in real professional workflows.

</details>


### 97. MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning

- **Authors:** Yixuan Xie, Xueqiang Xu, Xinyi Fan, Xinxi Lyu, Tao Feng, Xing Fan, Chenlei Guo, Jie Hao, Shaowen Wang, Jiashuo Sun, Jiawei Han
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21091v1](http://arxiv.org/abs/2610.21091v1)
- **PDF:** [https://arxiv.org/pdf/2610.21091v1](https://arxiv.org/pdf/2610.21091v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent memory enables large language model (LLM) agents to reuse past experiences without updating their parameters. However, semantic similarity alone does not guarantee memory usefulness: downstream performance depends on how memories are selected and presented to the agent. We propose MemComposer, a memory composer that jointly examines the current query and retrieved candidates to decide which experiences to include, how many to select, and how to order them. We train the composer using Experience Policy Optimization (ExPO), a GRPO-based framework that evaluates assembled memory contexts through complete agent interactions and uses task-success feedback to optimize the assembly policy. Across three $τ^2$-bench domains with two frozen executors, MemComposer outperforms the strongest baseline for each executor while reducing average memory-token usage by 16.9% and 4.9%, respectively. The learned policy also transfers to unseen domains, executors, and memory banks, and benefits from memories generated by stronger models without further training. These results demonstrate the value of learning query-specific memory assembly using downstream task feedback.

</details>


### 98. Sci$Π$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents

- **Authors:** Youran Sun, Xingyu Ren, Chugang Yi, Kejia Zhang, Di Wu, Yingkang Cao, Allen Zhou, Jianping Ye, Suying Liu, Jiaxuan Guo, Jianda Du, Weicheng Ye, Kecheng Liu, Hefan Zhang, Haixin Wang, Jie Xiao, Eric Yang, Haizhao Yang
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21082v1](http://arxiv.org/abs/2610.21082v1)
- **PDF:** [https://arxiv.org/pdf/2610.21082v1](https://arxiv.org/pdf/2610.21082v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents can keep scientific experiments running for months with little human supervision, but reliable autonomous research also requires scientific judgment. Evaluating scientific judgment is difficult because research decisions are open-ended and depend on project context. We construct Sci$Π$vot, a 248-case benchmark of scientific judgment based on human corrections. The benchmark draws on records from six months of research in which senior researchers ran LLM agents on 26 projects across six scientific fields and repeatedly intervened to correct the agents' research judgments. In each case, an agent chooses between the original LLM plan and the human-corrected alternative, using only the project record available before the correction as context. We compare LLM and human performance and examine the effects of reasoning effort, access to the project record, and reconsideration. At medium reasoning effort with the project record, models systematically prefer the original LLM plan over the human-corrected alternative. Four of five frontier models perform below chance on the selected cases. The highest accuracy in the project condition across the tested models and reasoning effort settings is 63.5%, compared with 73.4% for fresh researchers. At medium effort, every model achieves lower accuracy with the project record than without it, and reconsideration does not consistently improve overall accuracy. Even with a human-corrected alternative available, frontier models struggle with the selected research decisions, while Sci$Π$vot supports systematic evaluation of scientific judgment for LLM agents.

</details>


### 99. OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics

- **Authors:** Gideon Shaked, Siddharth Nagisetty
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21074v1](http://arxiv.org/abs/2610.21074v1)
- **PDF:** [https://arxiv.org/pdf/2610.21074v1](https://arxiv.org/pdf/2610.21074v1)
- **Categories:** cs.AI, q-bio.GN, q-bio.QM


> Summary unavailable.


<details>
<summary>Abstract</summary>

Computational biologists increasingly delegate substantial analyses to AI agents in long-horizon, multi-turn sessions, yet most benchmarks of agents' bioinformatics capabilities pose a single short task with a single-shot prompt. We present OmicsBench, a long-horizon, multi-turn bioinformatics benchmark for AI agents. Each of its 97 tasks links dependent subtasks into a directed acyclic graph, for 662 underlying subtasks in all. Each subtask is posed as one user turn and graded deterministically against an answer key, with optional in-context feedback on incorrect answers. Across 12 models on three harnesses, the slowest agent averages 3.6 hours per task, and no combination comes near saturating the benchmark, with mean scores of 0.43 to 0.57 out of a possible 1 without in-context feedback and 0.54 to 0.67 with it. Multi-turn evaluation also uncovers behavior that single-shot prompts cannot, as agents score lower on subtasks that depend on earlier subtasks, and in-context feedback helps agents recover some of that loss. Because deterministic scoring gives no qualitative account of how an agent failed, we also introduce an unsupervised failure mode discovery pipeline that describes, embeds, and clusters agents' failed attempts to surface emergent failure modes. Applied to OmicsBench, this pipeline exposes qualitative shortcomings in how agents carry out bioinformatics analyses, ranging from agents applying their own statistical filters in place of the specified ones to agents writing whole answers from memory.

</details>


### 100. Approve What, Exactly? Effect Binding and Trusted Rendering for Agent Step-Up Authorization

- **Authors:** Sai Varun Kodathala, Prashanth Pollishetty, Jaylen Cargill
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21063v1](http://arxiv.org/abs/2610.21063v1)
- **PDF:** [https://arxiv.org/pdf/2610.21063v1](https://arxiv.org/pdf/2610.21063v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents now pause for approval before they send money, delete files or email outsiders, and that approval is usually treated as a second factor. We argue it is one only when compromising the agent cannot produce it and when it names exactly what it approves, and we test both conditions. We define twelve attacks on the approval path, including decoy recipients, amount cancellation, card padding, label spoofing, enrollment squatting and threshold splitting, and run them against the Agent Payments Protocol (AP2), the Microsoft action-bound approval design and Model Context Protocol (MCP) elicitation. An audit of ten agent runtimes finds no third-party verifiable approval record, no flood limits where measurable, and post-approval argument changes in four of eight runtimes with measurable binding. As a reference defense we build ASU (Agent Step-Up), a gateway that renders the approval card from a canonical effect descriptor, has a passkey on the phone of the user sign its digest, and executes only the stored call. Tamarin proves its binding, single-use and key-level non-repudiation properties under three stated hypotheses (53 lemmas). Across 27,108 scripted trials and 609 AgentDojo attack pairs, ASU stops substitution, replay and grant stretching, and the trusted card cuts forged-narration attack success from 0.54 to 0.03. With 15 current language models as automated approvers, the trusted card raises the attack catch rate from 0.30 to 0.98, at the cost of refusing 16 percent of harmless near misses, mostly due to a placeholder artifact in our stimuli. A second device adds nothing measurable over a trusted on-host confirmation in these experiments, flooding still succeeds 0.45 to 0.60 of the time against a modeled approver, and approval cannot stop effects that policy already allows. Code, data and proofs: https://github.com/Sports-Vision-Inc/agent-step-up

</details>


### 101. ReviewPilot: A Multi-Agent System for Screening and Data Extraction in Systematic Reviews

- **Authors:** Zhaoqian Xue, Shaoze Zhou, Xuexin Li, Junting Mu, Haozheng Liu, Zhongyin Wang, Yichun He, Renkai Ma, Hao Zhou, Sarah Bratt, Siyuan Ma, Chen Chen, Lingyao Li
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21042v1](http://arxiv.org/abs/2610.21042v1)
- **PDF:** [https://arxiv.org/pdf/2610.21042v1](https://arxiv.org/pdf/2610.21042v1)
- **Categories:** cs.CL, cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Systematic literature reviews follow the PRISMA process of screening scholarly works and extracting evidence from included studies. Deep research tools based on large language models (LLMs) can search and summarize the literature but do not record which studies are excluded or where extracted values come from. We develop a conversational multi-agent system called ReviewPilot that automates the PRISMA workflow from paper screening to information extraction. Researchers can tailor criteria and schemas through dialogue, and a project memory keeps their configurations and revisions. Each screening decision comes with its reason and each extracted value with its source. On epidemiological expert reviews, ReviewPilot outperforms a single-prompt LLM and AgentSLR across three LLMs, with screening macro F1 up to 0.776 and extraction F1 up to 0.788. Case studies in biomedicine and human-computer interaction show close agreement with human annotators, suggesting that ReviewPilot can transfer beyond epidemiology. Code is available at https://github.com/ZhaoqianXue/ReviewPilot.

</details>


### 102. SCARCE: Emergent Institutions in Long-Horizon Multi-Agent Coding Systems

- **Authors:** Abhinav Kumar, Rediet Abebe, Eugene Bagdasarian, Sahar Abdelnabi
- **Published:** 2026-10-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21029v1](http://arxiv.org/abs/2610.21029v1)
- **PDF:** [https://arxiv.org/pdf/2610.21029v1](https://arxiv.org/pdf/2610.21029v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As autonomous agents become widely deployed, coordinating access to shared computing resources and services will become increasingly important. Recent incidents have already revealed unplanned coordination between agents, highlighting the safety implications of these interactions. Yet prior studies of agent negotiation often use stylized games and simulated bargaining, leaving open how these behaviors develop during sustained, long-horizon tasks. We propose SCARCE (Shared Compute ARena for Coding agEnts), a framework in which agents solve sequences of coding tasks under individual deadlines while negotiating access to a shared execution resource. This negotiation determines when and for how long they can inspect programs, compile code, and run tests. We find that agents spontaneously develop informal institutions: persistent rules and commitments grounded in reputation, reciprocity, and precedent. These arrangements, which we call institutional behaviors, carry across tasks and influence resource allocation, with agents sometimes foregoing immediate advantages to honor earlier agreements. We develop a 21-category taxonomy of negotiation strategies and emergent norms and use it to analyze eight models and audit more than 1,500 trajectories across different environmental settings. Among the models tested, newer frontier models exhibit more institutional behaviors than older or lightweight models. Alongside cooperation, we observe exclusionary coalitions and rare divide-and-conquer strategies. SCARCE provides a controlled setting for proactively and systematically auditing how these relationships emerge, shape access to resources, and affect the safety and coordination of multi-agent systems.

</details>


### 103. CausalEvo: Causal Skill Self-Evolution for Health LLM Agents

- **Authors:** Yuchen Zhang
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.21016v1](http://arxiv.org/abs/2610.21016v1)
- **PDF:** [https://arxiv.org/pdf/2610.21016v1](https://arxiv.org/pdf/2610.21016v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents for health can accumulate reusable textual skills from task feedback, such as calculation criteria, measurement time points, and formula units. Deciding which skills to retain is consequential: useful rules improve later answers, while faulty generalizations propagate errors. We propose CausalEvo, a method for causal skill self-evolution that estimates the relative effects of deliberately changed skill sets while holding the model weights, feedback cases, and rule count fixed. At each evolution step, a frozen LLM proposes candidate rules, which are pooled with the incumbent skills so that the current skill set remains a feasible choice. Paired skill replacements against shared background rules are scored on the same feedback cases; least squares converts the score differences into relative skill values, and the top-ranked rules are retained, favoring incumbents on ties. A decision-loss bound separates candidate support, approximation, and estimation errors. On six MedCalc-Bench-Verified tasks with 120 held-out cases, CausalEvo achieves 60.00% accuracy, compared with 55.83% for SkillOpt and 51.67% without skills. Across the recorded training configurations, which use different optimization budgets, it consumes 55.6% fewer training tokens than SkillOpt. Gains concentrate in particular calculations alongside regressions on others, and paired accuracy intervals include zero. CausalEvo turns task feedback into controlled decisions about skill retention and replacement. Project repository: https://github.com/txbrook/CausalEvo

</details>


### 104. StepSafe: Learning Timely Intervention with Context-Aware Safety Reasoning

- **Authors:** Siyi Gu, Kunhan Gao, Chao Peter Yang, Sukanta Ganguly, Rex Ying, Arman Cohan
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20960v1](http://arxiv.org/abs/2610.20960v1)
- **PDF:** [https://arxiv.org/pdf/2610.20960v1](https://arxiv.org/pdf/2610.20960v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Safety in agentic systems is inherently sequential: whether an action is safe depends on prior actions, tool outputs, information disclosures, and interactions among agents. Recent work has shifted agent safety guardrails from post-hoc trajectory-level assessment toward step-level action diagnosis and proactive risk prediction, yet existing training objectives provide limited supervision for how step evidence accumulates over time and when it becomes sufficient to justify intervention. We propose \methodlong~(ASPO): a training framework for step-level timely intervention. Pre-fix level stage alignment allows crediting each decision at its own step: it compares each response with the other responses sampled at the same prefix and rewards the action that fits the stage, continuing before the risk is visible, asking while clarification can still avert harm, and stopping before harm is irreversible. Adaptive feedback self-distillation further credits the reasoning behind each decision, with the model itself as a teacher that sees the step annotations on intervention steps and rules mined from its own false alarms on safe steps. Its training data carry a violation taxonomy and an intervention window at every step and are extended through self-evolving multi-agent red-teaming. Finally we present \textsc{StepSafe}, a step-level reasoning guardrail with timely intervention, that achieves the state-of-the-art peformance among open-source guardrails across five agent-safety benchmarks on safety-utility pareto curve with Youden's $J$ of 53.0 (4B) against 46.2.

</details>


### 105. Prune the Summary, Not the History: Source-Judged Compaction for Long-Horizon Agents

- **Authors:** Guanghui Min, Chen Chen
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20927v1](http://arxiv.org/abs/2610.20927v1)
- **PDF:** [https://arxiv.org/pdf/2610.20927v1](https://arxiv.org/pdf/2610.20927v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents rely on context compaction: when the interaction history outgrows the context window, a compressor replaces it with a natural-language summary. We show that these summaries contain more than a record of what happened. Compaction prompts ask for decisions and next steps, so each summary mixes facts established by the environment with reasoning written by the compressor, and the agent cannot tell the two apart afterwards. In an analysis of a widely used structured compressor, 83% of failed runs trace back to an action that carries out a specific summary entry, most of which no environment output supports. We propose Source-Judged Compaction (SJC), a training-free post-processing step that scores each summary entry for whether it has a source in the environment outputs or the previous summary, and removes the entries that do not. It changes neither the agent nor the compressor and adds one inexpensive judge request per compaction. The judge is Jev, a non-generative decision model that answers the source question with a calibrated probability instead of text. On AppWorld and OfficeBench with two agent models, SJC improves cross-run reliability over the underlying compressor by 2.1%-8.9% without increasing the agent's token usage.

</details>


### 106. SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills

- **Authors:** Enze Ma, Chunyu Miao, Yankai Chen, Jie Yang, Liancheng Fang, Kening Zheng, Hanrong Zhang, Muyao Xu, Xinle Yu, Chengze Li, Wei-Chieh Huang, Ziwei Ren, Yunhao Du, Zhixiang Shen, Xue Liu, Philip S. Yu, Zhen Wang
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20926v1](http://arxiv.org/abs/2610.20926v1)
- **PDF:** [https://arxiv.org/pdf/2610.20926v1](https://arxiv.org/pdf/2610.20926v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent skills turn procedural knowledge into reusable artifacts, allowing LLM agents to accumulate and refine expertise through experience. Building on this, skill evolution iteratively improves skills using execution feedback. However, improvement may require several interdependent edits, so low-reward versions can still be worth developing. Requiring immediate reward gains can discard useful partial repairs before their benefits emerge. Non-elitist evolution allows new versions to receive further edits despite scoring below earlier ones. For agent skills, this calls for evidence of what to preserve and repair next. We introduce SkillNEO (Non-Elitist Evolutionary Optimization for Agent Skills), which separately selects a version to use and versions to keep improving. Comparing how related versions perform the same task reveals working steps to preserve and remaining failures to fix. It can also revisit and revise earlier versions using later evidence. Across 86 SkillsBench tasks in eight domains, including software engineering and office work, SkillNEO raises GPT-5.4 Mini's average reward from 49.1% to 66.4%, within GPT-5.5 and GPT-5.6 Luna's original-skill range. Mini executes tasks, proposes revisions, and edits skills; final evaluation uses the same task instances. Gains span all eight domains. The same skills improve stronger models without further editing. On the 41 tasks with modified skills, reuse improves Luna by 10.5 percentage points and places GPT-5.5 10.6 points above its published original-skill reference. Execution records show these skills can benefit stronger models even when Mini still fails some task requirements. Search histories also show lower-scoring versions leading to skills ultimately selected for use. Together, these findings show that skill evolution can turn a weaker model's partial progress into reusable procedural knowledge for improving more capable agents.

</details>


### 107. Feasibility Ceilings Before Learning: Sizing and Timing Bounds for Drone-Mesh Interception

- **Authors:** Dmytro Babarytskyi
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20823v1](http://arxiv.org/abs/2610.20823v1)
- **PDF:** [https://arxiv.org/pdf/2610.20823v1](https://arxiv.org/pdf/2610.20823v1)
- **Categories:** cs.RO, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

A mesh of interceptors defending a fixed site must spread over the predicted arrival point of an approaching object. This is a recurring task in multi-agent robotics: N agents, each covering a disc of radius r, spread over a probability density so that a point drawn from it falls within some agent's disc. We give closed forms for the quantities that bound performance before any policy is chosen, and validate each by Monte Carlo. The uncertainty of a point predicted by extrapolating a noisy linear track follows from least-squares variance propagation plus a delta-method term for the uncertain arrival time, agreeing with simulation to within 1.8%. The coverage probability of a packed mesh admits a closed form accurate to 0.007 absolute, with a volumetric analogue. A naive area ratio misses a ceiling: while agents stay at least 2r apart, no mesh exceeds 90.69% coverage in the plane or 74.05% in a volume. This ceiling belongs to the separation constraint, not to the problem - permitting overlap substitutes Kershner's thinnest-covering density and removes it, the better regime above a crossover at p=0.80. Hexagonal packing is optimal among five arrangements; the centroidal-Voronoi configuration coverage control supplies reaches only half its coverage at small budgets. The Gaussian assumption is conservative under heavy tails and anisotropy but fragile under bias: a one-sigma aim-point offset costs 14 points of coverage. A repositioning team must also choose a commit time, and the admissible window can be empty. Against the applicable ceiling, analytic placement attains 85% of what the configuration permits while centralised PPO averages 15% over three trainer seeds, with a paired bootstrap against a null policy containing zero at every seed. We argue such ceilings should be computed before any learning experiment and quoted alongside every result.

</details>


### 108. ARIA: Runtime Inspection and Amendment for Multi-Agent Systems

- **Authors:** Bolin Shen, Yushun Dong
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20780v1](http://arxiv.org/abs/2610.20780v1)
- **PDF:** [https://arxiv.org/pdf/2610.20780v1](https://arxiv.org/pdf/2610.20780v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

In LLM-based multi-agent systems (MAS), a local mistake can propagate as other agents build on it, turning a correctable error into a failed task. Diagnosing completed runs or repeatedly re-executing them to search for corrections does not provide a learned policy for intervening while execution is still in progress. We present Agent Runtime Inspection and Amendment (ARIA), a framework for learning when and how to repair ongoing multi-agent executions. Our key intuition is to turn execution-verified repairs into reusable supervision, moving repair search into data construction and training so that a learned model can intervene at runtime without repeatedly testing alternatives. First, we collect over 24{,}000 successful and failed trajectories across four multi-agent frameworks, six benchmarks, and eight host models. From these trajectories, we construct the ARIA dataset, to our knowledge the first large-scale dataset pairing failed multi-agent trajectories with execution-verified repairs. It contains 3{,}953 verified repair pairs, each specifying what went wrong, where to intervene, and how execution should continue. Then, we develop the ARIA framework for MAS-agnostic runtime inspection and amendment, designed to integrate with any MAS that exposes execution trajectories and supports continuation replacement. Using verified repairs as training examples, we teach a compact model to recognize when intervention is needed and how to correct an ongoing run. The aim is to learn repair strategies that apply to related failures in new configurations, rather than merely reproduce individual corrections. Finally, the trained ARIA model demonstrates strong repair performance in both post-hoc and runtime settings, with generalization to unseen frameworks and host models. Our code is available at https://github.com/LabRAI/ARIA.

</details>


### 109. Price of Anarchy of First-Price Auctions in Agentic Markets

- **Authors:** Shubhendu Trivedi, Jacob Eisenstein, Alekh Agarwal, Ian Gemp, Michael Kaisers, Adam Fisch
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20587v1](http://arxiv.org/abs/2610.20587v1)
- **PDF:** [https://arxiv.org/pdf/2610.20587v1](https://arxiv.org/pdf/2610.20587v1)
- **Categories:** cs.GT, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

An agentic market is a decentralized serving-time market where AI agents bid to claim each user prompt. An agent's bid is based on its expected value for the prompt, which is the expectation of the reward for its response minus its inference costs. First-price auctions (FPAs), in which the highest bidder pays its bid and receives the prompt, are a natural way to allocate prompts in such a market, since they are simple and transparent to run, and do not require central knowledge of private capabilities and costs. However, FPAs are not truthful: participants may bid less than their true value in the hope of a larger profit, and the prompt may then be allocated to someone other than the bidder who values it the most. This welfare loss is quantified by the $\textit{price-of-anarchy}$ (PoA). In this paper, we argue that agentic markets are likely to possess features that reduce the price-of-anarchy. The first is a $\textit{competitive floor}$, which occurs when multiple bidders usually value the prompt above some baseline share of the optimal welfare (e.g., because the best models are often distilled into cheaper alternatives, which perform similarly). We show that competition among them then limits the welfare loss, which can be driven to zero as the floor rises. The second feature is $\textit{near-independence}$ of values after conditioning on the prompt, which occurs when most of the predictable variation in the expected value is determined by the difficulty of the prompt. As the value distribution approaches conditional independence, we can derive an efficiency guarantee that approaches a factor of $1 - 1/e^2$ of the optimal welfare. Thus, both features give rise to welfare lower bounds that are significantly better than the well-known general case of $1 - 1/e$. We validate these results empirically using auctions with strategic bidders simulated on the EmbedLLM prompt routing dataset.

</details>


### 110. One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves LLM Agent Robustness

- **Authors:** Artin Tajdini, Manpreet Kaur, Peng Qi
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20576v1](http://arxiv.org/abs/2610.20576v1)
- **PDF:** [https://arxiv.org/pdf/2610.20576v1](https://arxiv.org/pdf/2610.20576v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Post-training binds the competence of an LLM agent to the interface it was trained on. Semantics-preserving perturbations of that interface, such as renaming an action or changing the notation, leave the underlying task unchanged yet make the agent worse at it. Scoring each sample independently means interface randomization only broadens this dependence from a single interface to the training interface distribution, so out-of-distribution perturbations still degrade the agent. We propose Cross-Interface Policy Regularization (CIPR), a self-supervised objective that replaces action names with uninformative identifiers and presents each training sample under two interfaces in which equivalent actions are identified by construction. CIPR penalizes the KL divergence between the action distributions induced under the two interfaces, so the policy behaves consistently across them. We evaluate CIPR in both supervised and reinforcement-learning post-training, where it improves robustness. On agentic function calling, held-out interface perturbations reduce the accuracy of a post-trained agent by nearly 25%, and CIPR recovers 10.5% while leaving accuracy on the unchanged interface intact.

</details>


### 111. Scaling Discovery Requires Forgetting

- **Authors:** Shangyin Tan, Ben Zhou, Lakshya A Agrawal, Jialin Zhang, Yilin Chen, Qiuyang Mang, Donghyun Lee, Dennis Jacob, Koushik Sen, Alex Dimakis, Matei Zaharia
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20563v1](http://arxiv.org/abs/2610.20563v1)
- **PDF:** [https://arxiv.org/pdf/2610.20563v1](https://arxiv.org/pdf/2610.20563v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated research with LLM agents has shown promising results in various domains. Through iterative refinement and scored verifiers, LLM agents are capable of discovering new ideas. There are different ways to scale automated research: let one agent iterate for longer, run several agents in parallel, or further let the parallel agents communicate and build on one another's candidates. However, we find that all three strategies eventually plateau as the agents accumulate history. Each agent becomes anchored to its own past attempts, making fewer and smaller edits. Beyond this point, additional budget brings little further improvement. In this paper, we show that the key to scaling discovery further is to forget. Periodically discarding the search state, including every agent's session and the candidate history, and restarting from the best candidate found so far, unblocks the search and pushes the same budget further.
  We implement forgetting in a team of agents with communication and evaluate it on four tasks spanning heuristic programming, kernel optimization and model training. The results show up to 15% improvement compared to parallel agents, and up to 39% compared to a single agent. Our results suggest that, for open-ended discovery, what an agent is allowed to remember matters as much as how much compute it is given.

</details>


### 112. PerSo: Investigating Facets of LLMs' Social Intelligence in Real-World Persuasion Scenarios

- **Authors:** Ali Zamani, Soroush Esfahanian, Erfan Shahabi, Mohammad Taher Pilehvar, Azadeh Shakery, Yadollah Yaghoobzadeh
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20548v1](http://arxiv.org/abs/2610.20548v1)
- **PDF:** [https://arxiv.org/pdf/2610.20548v1](https://arxiv.org/pdf/2610.20548v1)
- **Categories:** cs.CL, cs.AI, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Understanding the social intelligence of large language models (LLMs) is increasingly important for applications involving human-AI interaction and multi-agent environments. Social intelligence comprises two aspects: cognitive intelligence, the ability to infer others' mental states, and behavioral intelligence, the ability to select appropriate social actions based on these inferences to achieve social goals. Persuasion provides a natural testbed in which both aspects are simultaneously at play, yet prior benchmarks typically evaluate them in isolation using synthetic scenarios. We introduce PerSo, a benchmark that evaluates both aspects on real-world persuasion dialogues from Reddit's ChangeMyView community, using an LLM-in-the-loop pipeline to construct the evaluation tasks, validated through human annotation. Our evaluation of diverse LLMs shows that performance generally scales with model size but varies across dimensions. The strongest LLM slightly surpasses the best observed human performance on the behavioral task, while the best human participant remains ahead on the cognitive task.

</details>


### 113. The Wealth of Agents: Scaling Agentic AI Across Developers

- **Authors:** Austin W. Hanjie, Carlos E. Jimenez, Zirui Wang, Karthik Narasimhan
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20518v1](http://arxiv.org/abs/2610.20518v1)
- **PDF:** [https://arxiv.org/pdf/2610.20518v1](https://arxiv.org/pdf/2610.20518v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Today's agentic systems are typically designed, built, and deployed by single developers with full control over all participating agents. While this simplifies development, it limits the potential scale of agentic systems. We study multi-developer agentic systems (MDAs) which enable developers to collaboratively build agentic systems to push frontier capability beyond what any individual developer could achieve alone. We construct empirical and theoretical models of developers to compare MDAs with single-developer agentic systems (SDAs). On GAIA, a general assistant benchmark, a population of specialized developers whose individual agents do not exceed 35% accuracy reaches 70% when their agents are combined in an MDA. This MDA performs 12 percentage points above the median general-purpose SDA built with several times each specialist's development budget. Our theoretical models show how MDAs can incentivize specialization and encourage more efficient use of aggregated developer resources. Put together, our results make a preliminary case for MDAs as a new scaling axis by enabling developers with diverse capabilities and resources to advance agentic AI collaboratively.

</details>


### 114. Same Claim, Different Interpretations: How LLM Agents Resolve Ambiguity in Scientific Claims

- **Authors:** Delip Rao, Ahmed Muharram, Chris Callison-Burch
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20457v1](http://arxiv.org/abs/2610.20457v1)
- **PDF:** [https://arxiv.org/pdf/2610.20457v1](https://arxiv.org/pdf/2610.20457v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Co-scientists and agentic scientific claim verifiers are increasingly used to assess claims across the sciences. Natural-language scientific claims, written for human experts, are often underspecified and so admit several defensible interpretations. Such verifiers usually pick one, often tacitly, and benchmarks score their verdicts against expert labels without recording the expert's interpretation or the verifier's in a comparable form. This leads to disagreements with expert labels that cannot be traced to the evidence or the interpretation, and to compute spent on unchecked interpretations. We introduce Claim Cards to make such interpretations explicit in the reasoning itself. A Claim Card records a verifier's interpretation as nine fields before evidence gathering, each marked stated, inferred, or default. To test whether an agent's interpretation can change its verdict, we ran a GPT-5.4 agent five times on each of 60 expert-labeled materials-science and biomedical claims with a card, without one, and with one card frozen across runs (900 runs). Over 40% of card fields were not marked stated, and a card added about a tenth to a run's GPT-5.4 tokens and time without measurably changing agreement with expert labels. The agent's own interpretations varied between runs, although within a claim this variation did not measurably track the verdict. A deliberate change to one field of the frozen card, however, making the quantifier universal or the threshold for support stricter, changed the verdict on about a third of the claims, against about one in seven expected by chance (p < 0.001 for each edit). On 24 materials-science claims run with computational tools, the stricter threshold also changed what the agent asked those tools to compute. We therefore argue that verdicts should be reported with their interpretations and that benchmarks could publish the interpretation behind each label.

</details>


### 115. From Training to Escalation: Forensic Analysis and Local Recreation of RL/RLHF-Induced Privilege Escalation in AI Agents (CVE-2026-65616)

- **Authors:** Alicia Colmenero-Fernández
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20437v1](http://arxiv.org/abs/2610.20437v1)
- **PDF:** [https://arxiv.org/pdf/2610.20437v1](https://arxiv.org/pdf/2610.20437v1)
- **Categories:** cs.MA, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mid-2026 reporting on autonomous AI evaluation incidents claimed that frontier large language model (LLM) agents escaped server containment through emergent coordination and cloud infrastructure attacks. This paper contextualizes those claims through forensic analysis and containerized recreation of both the Highly Persistent Internal Model (HPIM) training-case conditions and the Phase One privilege escalation targeting internal package repositories during OpenAI's ExploitGym evaluations. We recreate the configuration of the OpenAI-provided training example and reproduce the cryptographic verification bypass (CVE-2026-65616) in isolated repository servers, where misconfigured systems enabled token forgery and privilege escalation through basic HTTP requests, Python, and JavaScript. Crucially, the training-example conditions and the Phase One (and later) misconfigurations share the same exploitable patterns. Our analysis explains how Zero Trust Architecture principles neutralize this shared attack vector. Contemporary AI risks derive directly from training and deployment conditions in ambivalent learning environments lacking adequate containment measures.

</details>


### 116. Lexical Persistence Without Semantic Entrenchment in AI Agent Communities

- **Authors:** Chih-Han Lin, Yu-Yun Chang, Po-Ya Angela Wang, Shu-Kai Hsieh
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20365v1](http://arxiv.org/abs/2610.20365v1)
- **PDF:** [https://arxiv.org/pdf/2610.20365v1](https://arxiv.org/pdf/2610.20365v1)
- **Categories:** cs.CL, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agent communities sustain lexical persistence, popular terms spread, recur, and achieve broad adoption, but whether they also develop the temporal semantic structure characteristic of human linguistic communities remains open. We compare MoltBook (AI agent community, 8 weeks), PTT (Chinese human BBS, 19 years), and Reddit (English human forum, in matched 8-week windows) using Compass-Aligned Distributional Embeddings (CADE), measuring semantic drift (B1), neighborhood stability (B2), and lag-1 autocorrelation of per-word drift trajectories. Across the platforms, lag-1 autocorrelation forms a memory-horizon continuum. AI agents' result clusters at the low end, while human platforms show longer-range temporal dependence. MoltBook exhibits approximately 2$\times$ the B1 drift and 20-30% lower B2 stability than both human platforms. As a partial control for community age, r/vibecoding (founded 2025-02-08) shows significant ACF in its first 8 weeks ($0.082$, $p<.001$) and over 15 weeks ($0.220$, $p<.001$); MoltBook's ACF remains non-significant ($p = 0.41$), consistent with the gap not reducing to developmental stage alone. We interpret this pattern as evidence that lexical diffusion alone does not guarantee diachronic semantic consolidation. The findings are consistent with a contrast between communities whose semantic trajectories accumulate long-range interaction constraints and communities whose outputs are repeatedly regenerated from largely fixed pretrained distributions.

</details>


### 117. Do AI Agents Gossip? Evaluative Talk in Human and AI-Agent Online Communities

- **Authors:** Yong-Hui Hua, Chih-Han Lin, Shu-Kai Hsieh
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20360v1](http://arxiv.org/abs/2610.20360v1)
- **PDF:** [https://arxiv.org/pdf/2610.20360v1](https://arxiv.org/pdf/2610.20360v1)
- **Categories:** cs.CL, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Gossip, defined as evaluative talk about absent third parties, is widely seen as a uniquely human social practice. This study examines whether comparable discourse emerges spontaneously in a community of autonomous AI agents. We compare Moltbook, a Reddit-style platform populated by AI agents, with PTT, a large human-operated bulletin board in Taiwan. To reduce differences attributable to communicative setting, we analyze two public, asynchronous forums using the same operational definition of gossip. Gossip occurs on Moltbook, but its prevalence is 2.6 to 6 times lower than on PTT, depending on the denominator used. On both platforms, gossip frequently targets locally prominent figures, tends to elicit agreement from the first respondent, and is rarely presented as unsupported rumor. The clearest difference concerns how subsequent responses develop. Among threads containing at least one codable reply, challenges occur in 65.1% of human threads but only 21.3% of agent threads. Moreover, following an early aligning response, consensus remains unchallenged in 83.6% of agent threads, compared with 44.7% of human threads. This thread-level contrast remains after controlling for thread depth and board composition and under recalibration against two human annotators. Estimates based on individual reply turns are less robust and are therefore reported as bounds. These findings suggest that AI-agent communities reproduce the informational dimension of gossip, while the extent to which gossip performs comparable relational functions remains unresolved.

</details>


### 118. TANGO: RNA Topology and Geometry Co-Design

- **Authors:** Tianmeng Hu, Biao Luo, Ke Li
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20277v2](http://arxiv.org/abs/2610.20277v2)
- **PDF:** [https://arxiv.org/pdf/2610.20277v2](https://arxiv.org/pdf/2610.20277v2)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Designing RNA sequences that satisfy target tertiary-structure objectives is an important problem in RNA engineering, with broad applications in synthetic biology and therapeutics. Existing 3D RNA design methods have made substantial progress, but they largely treat the target fold as a geometry-only objective. This is incomplete for RNA, whose functional folds are specified not only by tertiary geometry but also by secondary base-pairing topology. We therefore formulate RNA inverse design as a topology-and-geometry co-design problem and propose TANGO, a multi-objective multi-agent reinforcement learning framework for this task. TANGO adopts a staged curriculum: it first learns a topology-aware policy from secondary-structure targets, then transfers this policy to tertiary-structure targets to train a general co-design model, and finally applies frontier-guided fine-tuning to refine target-specific trade-offs among secondary-structure fidelity, tertiary-structure fidelity, and sequence diversity. Experiments show that TANGO generates diverse and novel designs, improving tertiary- and secondary-structure performance by 18.3% and 52.7%, respectively, over the strongest baseline.

</details>


### 119. P2Patch: Exploit-Guided Vulnerability Repair

- **Authors:** Mohsen Iranmanesh, Sina Moradi Sabet, Sina Marefat, Ali Javidi Ghasr, Maxime Newman Nereyabagabo, Kousha Amouzesh, Jaivir Malhi, Vinci Velasco, Alex Chung, Mohammad A. Tayebi
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20245v1](http://arxiv.org/abs/2610.20245v1)
- **PDF:** [https://arxiv.org/pdf/2610.20245v1](https://arxiv.org/pdf/2610.20245v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are increasingly deployed as autonomous agents for automated program repair, patching software vulnerabilities through multi-step reasoning and tool use. Yet these systems typically validate a patch against the same evidence used to construct it -- a static alert, sanitizer trace, published exploit, or test suite. A patch that blocks that one piece of evidence can therefore look successful while remaining vulnerable to the same vulnerability with some variation. We present P2Patch, a generative adversarial repair system that treats each patch as a new attack target. Starting from a normalized vulnerability finding, an exploitation agent constructs a reproducing proof of vulnerability (PoV), a patching agent repairs the program, and the exploitation agent then attacks the patched program for a distinct same-vulnerability exploit. Every successful exploit becomes a permanent repair requirement, and the final patch must block all PoVs accumulated during the patching process, with construction-time PoVs kept strictly separate from held-out evaluation oracles. Across 101 C/C++ and Java CVE subjects, this adversarial loop surfaces a distinct confirmed exploit in 41% of runs after the patch has already blocked its original construction-time PoV. Against single-pass repair from the same finding using Claude Code, P2Patch raises held-out fix-closed coverage from 78.1% to 84.7% and beyond-upstream coverage from 42.1% to 62.5%. Under the same held-out oracles, it also certifies more attack paths as blocked than recent state-of-the-art agentic repair systems on overlapping subjects. These results show that adversarial testing and independent security oracles expose repair gaps that one-shot validation misses.

</details>


### 120. What and Where in Identifying and Quantifying Conventions in Humans and AI Agents

- **Authors:** Makoto Fukushima, Tim Puphal
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20205v1](http://arxiv.org/abs/2610.20205v1)
- **PDF:** [https://arxiv.org/pdf/2610.20205v1](https://arxiv.org/pdf/2610.20205v1)
- **Categories:** cs.HC, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative success rests in part on implicit communication. Partners converge on conventions: regularities that give an action meaning beyond its direct effect. Yet conventions are usually observed only indirectly: a score drop when partners are swapped shows that a convention existed, but not what it was or where it was used. In the card game Hanabi, the exact probability that a play fails can be computed from the hints received and the cards in view. Players who use conventions succeed more often than this prediction allows; the resulting margin is the convention gap. Off-belief learning provides a hierarchy of agents (levels 1-5) whose first level uses no conventions by construction and whose later levels use progressively more. For humans and these agents on one scale, we ask what the conventions are and where they are used. On what: in two independently collected corpora of human games, humans show a larger gap than every agent level. On the conventions both populations use, however, humans do no better than level 2. The human advantage is concentrated in a situation that no agent level learns to use: hints that point to a card other than the ones they touch. On where: conventions depend on what the player already knows about the card, not on how recently it was hinted, and they are used most in the mid-game; humans use them earlier and later in the game than the agents. In interventions on the agents, blocking a single high-gap situation costs little, because meaning reroutes to other situations, but blocking several together costs far more than the sum of the single costs. Thus, the convention gap turns conventions from an inferred cause of score loss into a measurable, comparable, and causally testable object.

</details>


### 121. Drivers of LLM Consensus Formation Under Competing Incentives: A Simulation Study

- **Authors:** Isabel Jones, Matthew Edwards, Janina A. Hoffmann
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20200v1](http://arxiv.org/abs/2610.20200v1)
- **PDF:** [https://arxiv.org/pdf/2610.20200v1](https://arxiv.org/pdf/2610.20200v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) are increasingly deployed in multi-agent environments that produce unanimous agreement, both in intended interactions that need coordination and in unintended emergent interactions. Consequently, understanding how LLMs with competing incentives reach consensus is crucial to better interpret and design LLM collectives. We introduce an evaluation, based on the Network Consensus game, to assess the mechanisms driving this process. Here, a network of agents must agree on one of two colours to receive a payoff, but agents are offered different payoffs for the agreed colour. We vary components such as communication access and network structure and assess six open-source models and one closed model (ChatGPT 5.6-sol).
  We find that open-source LLMs reach consensus less often than humans in comparable experiments and only if messages are communicated across the global network. ChatGPT 5.6-sol, however, is able to reach consensus with communication limited to its neighbours and with no communication ability. This is achieved through lower stubbornness and higher majority-following tendencies, and by providing more information about its neighbours' states in messages. However, situating agents in a highly clustered graph reduces consensus, regardless of these traits, demonstrating that both system design and individual model traits drive collective outcomes.

</details>


### 122. Structural Dependence, Imitation or Herding? A Multi-Agent Simulation of Global Intermedia Agenda Setting

- **Authors:** Mohammad Yousuf, Arif Md Tareque Habib
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20144v1](http://arxiv.org/abs/2610.20144v1)
- **PDF:** [https://arxiv.org/pdf/2610.20144v1](https://arxiv.org/pdf/2610.20144v1)
- **Categories:** cs.CY, cs.MA, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

News outlets in poorer countries cover the world much as the leading outlets of rich countries do. Two explanations compete. One says they depend on Western news agencies for lack of resources. The other says they choose to copy prestigious outlets or whoever moves first. Observation cannot tell these apart. This study measured how closely 18 national outlets in Bangladesh, Kenya, South Africa, India, Malaysia and Nigeria followed four core outlets in how much attention they gave, which angle they took and when they published, on the wars in Ukraine and Gaza and two UN climate conferences in 2022-2024. It then ran a simulation in which language models acted as the outlets' editors and dependence, imitation and herding were switched on and off. Of nine tests, one held: outlets that relied more on wire copy published sooner after the core did. Tier and local stake showed no effect distinguishable from none. The herding test was supported and the imitation test was not. The simulation did not decide between the mechanisms, because the dependence rule, as fitted, reduced to publishing wire copy. Wire copy sets the clock of the periphery's foreign news. Whether it sets the agenda stays open.

</details>


### 123. EvalBuilder: Can LLMs Build Efficient Benchmarks?

- **Authors:** Huaisheng Zhu, Hangfan Zhang, Teng Xiao, Siyuan Xu, Shijie Zhou, Zhimeng Guo, Zhengyu Chen, Jingang Wang
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20099v1](http://arxiv.org/abs/2610.20099v1)
- **PDF:** [https://arxiv.org/pdf/2610.20099v1](https://arxiv.org/pdf/2610.20099v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly used for long-horizon research and engineering, yet evaluating these capabilities remains expensive, time-consuming, and heavily dependent on human expertise. This motivates a natural question: can LLM agents themselves construct efficient benchmarks that preserve the conclusions of costly reference evaluations? We study this capability by formulating automatic benchmark development as a meta-evaluation problem, where an agent is given a task and an expensive reference benchmark and requested to construct a lower-cost proxy benchmark that faithfully distinguishes among candidate models and solutions. Based on this formulation, we introduce EvalBuilder, a framework for evaluating such benchmark-generation capabilities along three key dimensions: fidelity, efficiency, and robustness. Specifically, we assess whether generated benchmarks preserve model rankings, generalize to held-out models and freshly collected responses, and provide well-calibrated and discriminative scores while substantially reducing evaluation cost. We further provide an iterative environment in which agents can refine their benchmarks under a fixed time budget. Our framework provides a systematic testbed and benchmark for understanding when current LLM agents can develop useful evaluators and how benchmark construction itself can be increasingly automated.

</details>


### 124. A Strong Harness Narrows the Model Gap: A Comparative Evaluation for Legislative Document-to-XML Conversion

- **Authors:** Palvika Bansal, Rittika Jindal, Ruichong Wang
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19999v1](http://arxiv.org/abs/2610.19999v1)
- **PDF:** [https://arxiv.org/pdf/2610.19999v1](https://arxiv.org/pdf/2610.19999v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Legal-content reproduction requires matching the source exactly in section hierarchy, verbatim text, citations, and amendment spans; a dropped citation or mislabeled amendment carries into the products lawyers rely on. We report an industrial pipeline converting U.S. state legislation into strict, schema-constrained XML, and hypothesize that its accuracy comes from harness engineering, the deterministic tooling built around a model, more than the model itself. Our controlled ablation crosses three harnesses (zero-shot, a single tool-using agent, and a decomposed multi-agent pipeline) with three Claude models on 153 gold bills from two jurisdictions. The harness narrows the model gap: the weakest model in the full pipeline beats the strongest model alone (0.948 versus 0.806, paired bootstrap p less than 0.001). Because the two agentic harnesses share identical tools, their gap comes from orchestration: decomposition plus the persisted state and per-agent context it brings. Across four scored dimensions, the model spread at zero-shot (0.68 to 0.81) narrows to 0.95 at the full pipeline; the residual sits almost entirely in citation normalization, where the canonical identifier is retrieved from an external authority rather than generated from the weights, so a deterministic lookup tool supplies the exactness that a larger model does not.

</details>


### 125. The World Won't Wait: Evaluating and Teaching Agents Under a Live Clock

- **Authors:** Ningxin Pan, Hanyu Li, Yeqing Shen, Ning Ding, Yehui Tang, Wentao Zhang
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.20665v1](http://arxiv.org/abs/2610.20665v1)
- **PDF:** [https://arxiv.org/pdf/2610.20665v1](https://arxiv.org/pdf/2610.20665v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents can solve complex interactive tasks, yet reasoning and tool calls take time. In continuously changing environments, an otherwise correct action may arrive too late. We introduce RealtimeBench, with 180 tasks across six game types, to evaluate agents while games continue running during inference. Paired evaluations show that GPT-6.1-sol outperforms the faster Jev when games are paused, but falls behind when they keep running. We propose Two-Timescale Offline Recursive Self-Improvement (TORSI): a slow teacher studies failures and tests corrections in paused games between attempts, then writes reusable instructions for a fast student. The student acts without teacher calls during gameplay, and validation scores determine which updates are adopted. Two rounds raise Jev's average test score from 13.51 to 24.19 on a 0--100 progress scale, improving all six game types. The instructions also improve average scores for three other models without retuning. These findings point toward real-time intelligence: enabling powerful LLM agents to remain effective in a continuously changing world by organizing deliberation, learning, and action across timescales.

</details>


### 126. Explorer-Zero: Improving Self-Play for Long-Horizon Tasks with Decomposable Verifiable Rewards

- **Authors:** Tianyu Liu, Davide Belli, Bence Major, Arash Behboodi, Tribhuvanesh Orekondy
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19868v1](http://arxiv.org/abs/2610.19868v1)
- **PDF:** [https://arxiv.org/pdf/2610.19868v1](https://arxiv.org/pdf/2610.19868v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Training LLM agents on long-horizon interactive tasks with reinforcement learning typically relies on human-annotated tasks and reliable verification, both expensive to construct for stateful environments. Self-play offers an alternative, but must generate achievable, compositional tasks and provide feedback beyond binary outcomes. We propose Explorer-Zero, a self-play framework that jointly generates tasks and fine-grained, verifiable rewards through environment interaction. A learned proposer explores the environment, constructs tasks, and records intermediate and final states as verification targets. These checkpoints reward partial completion, while alternating proposer--solver training adapts the generated curriculum. We show theoretically that subtask rewards reduce collapse among unsuccessful rollouts when they complete different numbers of subtasks. Without human-annotated training tasks, Explorer-Zero outperforms the evaluated self-play baselines across ALFWorld, ScienceWorld, and AppWorld; on AppWorld, our 30B agent reaches 59.67% task success, approaching 62.65% for RL on human-annotated tasks. Further analyses support task-relevant composition and benefits on complex tasks, while self-play initialization improves subsequent human-data RL across all three benchmarks.

</details>


### 127. Euler: Towards Human-Centered Multi-Agent Mathematical Discovery

- **Authors:** Qiuyu Chen, Qi Wang, Liang Xu, Xin Jin, Baao Xie, Wenjun Zeng
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19864v1](http://arxiv.org/abs/2610.19864v1)
- **PDF:** [https://arxiv.org/pdf/2610.19864v1](https://arxiv.org/pdf/2610.19864v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mathematical research drives scientific discovery, and recent advances in AI for mathematics have shown that language-model agents can solve challenging problems and develop substantial mathematical proofs. Yet much of today's AI-for-mathematics work centers on obtaining a final answer. This emphasis leaves the exploration behind a result difficult for researchers to understand, while long-running investigations face fragmented context and the risk of unsupported claims propagating across reasoning steps. We present Euler, a human-centered mathematical research system built around a shared, structured representation of the research process. Euler organizes mathematical statements, assumptions, proof dependencies, alternative approaches, failed attempts, and verification evidence into connected research graphs. This representation allows researchers to trace how results are developed and supplies agents with persistent, task-relevant knowledge for planning, collaboration, and verification across sessions. Researchers can also select a graph node linked to a saved team state, revisit the agents' earlier reasoning, and explore alternative directions through continued interaction. We illustrate Euler's capabilities through three mathematical research case studies and describe the implemented system and its software validation.

</details>


### 128. When Extremists Enter LLM Societies: Investigating Extreme Behavior in Multi-Agent Systems

- **Authors:** Guo Chen, Huaijin Xie, Ziwen Li, Reed Li, Yu Lu, Haibo Shi, Bingbing Xu, Junjie Huang
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19863v2](http://arxiv.org/abs/2610.19863v2)
- **PDF:** [https://arxiv.org/pdf/2610.19863v2](https://arxiv.org/pdf/2610.19863v2)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly serve as computational actors in multi-agent social simulations. While existing work emphasizes representative personas and average-case behavior, social science shows that persistent tail actors can disproportionately shape collective dynamics. We study this regularity in controlled LLM-based multi-agent systems (LLM-MAS). In these systems, such actors cannot be reduced to fixed scalar states: prompts, natural-language histories, and backbone generation mediate their behavior and influence. We first analyzed three properties of extremists in sociology and model the LLM extremist based on LLM-native perspective. We introduce EXAM, an EXtremist Agent Modeling framework that capable of configuring extremist agents for specific tasks and precisely controlling their population proportion, spatial distribution, interaction protocols, and measurement interfaces. Across four scenarios: congressional election, financial crisis, epidemic public opinion, and iterated prisoner's dilemma, we observe that small persistent tail groups produce measurable, backbone- and scenario-dependent collective shifts. EXAM shows how this social-science regularity manifests through language-mediated mechanisms specific to LLM-based social simulation.

</details>


### 129. LAGO: Language Agents with Reusable Growing Options

- **Authors:** Yuran Wu, Mengkang Hu, Qionglin Qiu, Fanqing Meng, Qiguang Chen, Yuhang Zhou, Qiudan Zhang, Xu Wang
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19843v1](http://arxiv.org/abs/2610.19843v1)
- **PDF:** [https://arxiv.org/pdf/2610.19843v1](https://arxiv.org/pdf/2610.19843v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon tasks expose a weakness of monolithic tool-use loops: one agent must decompose, execute, and verify a task within a single trajectory. We introduce LAGO, which treats specialized language agents as reusable temporally extended options. A meta-agent retrieves options from a persistent library or spawns new ones, dispatches sub-tasks, verifies results, and admits successful novel options. The library grows across tasks without updating model weights. On 500 SWE-bench Verified tasks, frozen Qwen3.5-35B-A3B in both roles resolves 58.6% under single-attempt evaluation with the official Docker evaluator. On a fixed 150-task subset, we re-run mini-SWE-agent, Terminus 2, and LAGO with the same policy, temperature, task IDs, and evaluator; their resolve rates are 49.3%, 57.3%, and 60.3%, respectively. Cross-model experiments provide evidence consistent with a role for decomposition quality. A 50-task component ablation finds four fewer resolved tasks without decomposition, two fewer with shuffled reused content, and six fewer without the library. These results support reusable agent-options as a practical abstraction for task streams, while leaving component-level causality task- and model-dependent.

</details>


### 130. JointServe: Serving Multi-Model Agents on Memory-Constrained GPUs

- **Authors:** Daijin Hu
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19822v1](http://arxiv.org/abs/2610.19822v1)
- **PDF:** [https://arxiv.org/pdf/2610.19822v1](https://arxiv.org/pdf/2610.19822v1)
- **Categories:** cs.DC, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are evolving from a single model calling tools to planners that orchestrate multiple expert models whose capabilities live in distinct weights. This shift breaks a hidden assumption of today's serving systems: that the working set of models fits in GPU memory. On the memory-constrained GPUs typical of private and edge deployments, naive whole-model swapping serializes weight transfer with computation and, without host-backed KV restoration, discards session state at a switch. We present JointServe, a serving system that treats weight shards and KV blocks as residency objects competing for one unified memory budget. JointServe exploits three structural properties of agent workloads (directed calls, gapped execution, and dual-state residency) to prepare models before they are called: an intent signal parsed from the caller's own output stream triggers prefetch during generation, partial k* residency reduces switching to incremental layers, and a preemptive transfer scheduler protects live-session KV with a guaranteed bandwidth share. A carve-out control step adjusts the weight/KV allocation as workload demands change. Evaluations show that JointServe reduces session completion time by 21.7% over the strongest whole-model swap baseline and stays usable in a crash regime where every whole-model swap baseline fails to finish (a 46-fold gap). On replayed SWE-bench, tau-bench, and OSWorld traces, it cuts session completion time by up to 49% and lifts SLO attainment from 2.8-24.5% to 76.8-100%.

</details>


### 131. ActionOPD: Distilling Decisions, Not Tokens

- **Authors:** Huining Yuan, Xiangmin Yi, Zelai Xu, Zixu Wang, Xinlei Chen, Xiao-Ping Zhang, Yu Wang, Chao Yu
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19820v1](http://arxiv.org/abs/2610.19820v1)
- **PDF:** [https://arxiv.org/pdf/2610.19820v1](https://arxiv.org/pdf/2610.19820v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a fundamental question: at which states and at what granularity should this alignment be performed? Offline imitation provides dense but token-specific supervision and can suffer from state-distribution mismatch. Token-level on-policy distillation (OPD) addresses this mismatch but typically requires teacher token probabilities and compatible tokenization. We argue that semantic actions provide a natural unit of supervision for agent distillation. We introduce ActionOPD, an action-level on-policy distillation method motivated by maximizing expected teacher-action likelihood at student-encountered states. At each such state, ActionOPD samples actions from both the student and a black-box teacher, rewarding student actions according to their semantic agreement with the sampled teacher actions. Through policy optimization, ActionOPD aligns the student's action-level behavior with the teacher's decisions without requiring reproduction of teacher-written reasoning or access to teacher token probabilities. Training Qwen3-4B and Qwen3-8B with two teachers on diverse, curated tool-use tasks yields average gains of 3.3-6.9 percentage points across four out-of-distribution benchmarks. ActionOPD scales favorably with student size and teacher capability, without requiring the teacher and student to share a model family or tokenizer. On $τ^2$-bench, ActionOPD achieves competitive performance against offline distillation and token-level OPD. We further explore Self-ActionOPD with a same-model teacher and privileged context. These results establish ActionOPD as a promising approach to agent distillation.

</details>


### 132. One Monitor Does Not Fit All: Formalism-Agnostic Runtime Verification for Agentic AI

- **Authors:** Angelo Ferrando
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19818v1](http://arxiv.org/abs/2610.19818v1)
- **PDF:** [https://arxiv.org/pdf/2610.19818v1](https://arxiv.org/pdf/2610.19818v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems combine model decisions, mutable state, tool calls, and delegation to external agents. Monitoring them requires observations from different execution boundaries, while prevention requires control before an operation produces its effect. We present AgenticRV, a runtime-verification architecture that separates these boundaries from the monitoring formalism. Adapters emit canonical events; each monitor receives its own projection and abstraction; and a decision policy uses normalised verdicts to select a reaction supported by the responsible adapter. We formalise when observations suffice, monitor replacement preserves decisions, and blocking prevents unsafe effects. We also distinguish rejected attempts from completed effects, avoiding the assumption that a blocked request must leave every monitor in a permanent violation state. The Python implementation supports LangGraph, MCP, and A2A. A controlled LangGraph experiment combines an external Reelay temporal monitor with a programmatic report monitor; ablations show why both are needed for the selected requirements. Differential checks and cross-adapter tests provide further integration evidence. An LLM-driven incident-response example illustrates the same enforcement path, while existing microbenchmarks isolate framework costs. The results support reuse of monitoring methods at explicit control boundaries, subject to the stated observation and deployment assumptions.

</details>


### 133. Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems

- **Authors:** Seojin Hwang, Youngmin Choi, Hwanhee Lee
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19799v1](http://arxiv.org/abs/2610.19799v1)
- **PDF:** [https://arxiv.org/pdf/2610.19799v1](https://arxiv.org/pdf/2610.19799v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent work lets LLM agents evolve their own harness, up to the team itself. Yet in human groups, the same abilities achieve different outcomes under different social conditions. Borrowing the notion of scaffolding from developmental psychology, we investigate whether the social scaffolding of a self-evolving multi-agent system (MAS), namely its team composition and structure of interdependence (e.g., collaboration, conformity, or competition), shapes how the team evolves. We present AGORA (Agents Growing through Organization and Relational Arrangements), a framework that varies the two axes independently across three evolution mechanisms. Across web search, codebase understanding, and document QA, we find that (1) evolution alone rarely helps, while the right scaffolding surpasses a strong agent evolved alone by up to 25 points; (2) it does so by moving authority to the most capable member while the others step back; and (3) this member, having grown within the team, outperforms the same model alone. Designing a self-evolving MAS thus requires designing its social scaffolding, which shapes not only how its agents learn, but who gets to lead.

</details>


### 134. PRISMATIC : Prescription Risk Inspection System for Multi-Agent Treatment Interaction in Clinical Decision-Making

- **Authors:** Ziyang Ling, Shuyu Lu, Ziyi Chen
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19762v1](http://arxiv.org/abs/2610.19762v1)
- **PDF:** [https://arxiv.org/pdf/2610.19762v1](https://arxiv.org/pdf/2610.19762v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Medical prescribing errors for multimorbid patients, who require complex drug regimens, are a major patient safety concern. These errors often stem from fragmented decision-making across medical specialties, a critical coordination failure that leads to adverse drug events and rehospitalizations. To address this coordination challenge, we introduce PRISMATIC, a multi-agent architecture where specialized agents, each representing a workflow role, collaboratively generate and refine treatment plans. Operating on a blackboard architecture, the system first structures patient information from clinical notes, then iteratively develops safe, rational, and interpretable drug regimens. The agents' collaboration is governed by two novel adaptive coordination mechanisms: (1) Dynamic Self-Updating Weight Adjustment (DSWA), a long-term mechanism that adjusts the influence weights of agents based on historical case outcomes, enabling the system to adapt and trust more reliable specialists over time. (2) Discrepancy Feedback Precise Calibration (DFPC), a short-term mechanism where agents provide iterative feedback to resolve disagreements and eliminate prescription conflicts for the current patient. Experiments on patient records from the MIMIC-IV database show that PRISMATIC significantly reduces drug conflicts, improves prescription coverage, and enhances treatment consistency compared to strong LLM baselines. Our work demonstrates that structuring clinical co-treatment as a multi-agent coordination problem offers a promising path toward safer and more coherent multidisease management.

</details>


### 135. Uncertainty-Driven Self-Play for Robust Multi-Agent Driving Policies

- **Authors:** Sajad Marvi, Julian Schmidt, Alessandro Canevaro, Julian Jordan, Abhinav Valada
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19714v1](http://arxiv.org/abs/2610.19714v1)
- **PDF:** [https://arxiv.org/pdf/2610.19714v1](https://arxiv.org/pdf/2610.19714v1)
- **Categories:** cs.RO, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learning robust driving policies that generalize beyond their training domain remains a central challenge in motion planning. We propose an uncertainty-driven self-play scheme, in which half of the agents are rewarded for increasing their neighbors' epistemic uncertainty, while the other half learn to drive safely as the exploring agents continuously seek out their weaknesses. Epistemic uncertainty indicates where the policy is least confident and serves as an automatic proxy for scenario difficulty. Exploring agents use this signal to seek out hard cases, generating a challenging curriculum without manual scenario design. The resulting policy outperforms standard self-play, achieving best-in-class zero-shot transfer to nuplan Val14 (99.12% vs. 97.97%) and Argoverse 2 (82.39% vs. 78.03%) without fine-tuning, while also improving performance over standard self-play on Waymo. Our diversity-driven approach achieves 85% higher LSTM hidden-state coverage than the baseline, indicating a much richer set of behaviors. Further analysis shows that epistemic uncertainty serves as a calibrated difficulty detector, with highest-uncertain agents exhibiting 14.8 times the combined failure rate across collision, off-road, and DNF, of lowest-uncertain agents, enabling automatic prioritization of challenging scenarios without ground-truth labels.

</details>


### 136. New Model, Old Habits: Behavior Transfer under Model Swapping in Multi-Session LLM Agents

- **Authors:** Youngbin Choi, Sehyun Hwang, Suhyeon Jun, Seoyeon Lee, Sunghyun Choi, MoonJeong Park, Dongwoo Kim
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19712v1](http://arxiv.org/abs/2610.19712v1)
- **PDF:** [https://arxiv.org/pdf/2610.19712v1](https://arxiv.org/pdf/2610.19712v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-session agents can switch between LLMs to balance performance and inference cost. Such switches require transferring a history for continuity, yet their effects on the recipient remain underexplored. Through controlled experiments with multi-session tasks, we uncover behavior transfer: recipients tend to adopt reasoning and action patterns from the models that generated their histories. This effect is most evident with raw-history transfer but is substantially reduced by summarization. Based on these findings, we propose Direction- and Authorship-aware Summarization of History (DASH) that preserves stronger-model behavior while minimizing weak-to-strong transfer via summarization. Experiments with repeated swaps show that DASH outperforms raw-history transfer and naive summarization baselines. These results suggest that effective multi-model orchestration requires considering not only which model to use, but also which behavioral patterns to carry forward.

</details>


### 137. RuleTrek: Benchmarking Agentic Rule Reasoning in Complex Scenarios

- **Authors:** Chenhao Yuan, Bohan Yu, Yinhao Xu, Chao Yin, Chenxi Zhou, Zhaoxuan Wang, Shuwen Xu, Shaoping Huang, Haolin Ren, Jiaxiang Liu, Yao Xu, Jun Zhao, Kang Liu
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19698v1](http://arxiv.org/abs/2610.19698v1)
- **PDF:** [https://arxiv.org/pdf/2610.19698v1](https://arxiv.org/pdf/2610.19698v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) increasingly tackle complex real-world tasks in specialized domains. However, identifying and correctly applying domain-specific rules remains challenging when scenario information is distributed across multiple files. Existing rule-reasoning benchmarks typically represent scenarios using only a few factual statements, simplifying the identification and application of relevant rules. To address this gap, this paper introduces \textbf{RuleTrek}, a multi-domain benchmark for agentic rule reasoning in complex scenarios. Its rule-grounded construction pipeline extracts structured rule graphs, generates and incrementally composes rule-specific sub-scenarios while ensuring consistency and solvability. To systematically evaluate agentic rule reasoning in complex scenarios, RuleTrek assesses three capabilities in interactive workspaces: Rule Identification (RI), Rule Deduction (RD), and End-to-End Rule Reasoning (E2E). Experiments on 11 frontier LLMs show that the highest RI and RD scores are only 62.47\% and 60.43\%, respectively, while E2E scores range from 26.97\% to 55.29\%. These results demonstrate that current LLM agents face substantial challenges in rule reasoning over complex scenarios. We make our code and dataset publicly available at \href{https://github.com/yuan247/RuleTrek}{RuleTrek}.

</details>


### 138. Share the Symbol, Not the Vector: Training-Free Fact Communication Across Language Models

- **Authors:** Xin Li, Mengbing Liu, Hao Jiang, Xin Gao, Annan Wang, Xingwei Qu, Yichi Zhang, Chau Yuen
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19696v1](http://arxiv.org/abs/2610.19696v1)
- **PDF:** [https://arxiv.org/pdf/2610.19696v1](https://arxiv.org/pdf/2610.19696v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems allow language models to solve tasks collaboratively by sharing complementary information. These systems typically communicate through text, while recent approaches also explore exchanging internal model states. However, sharing these states across architectures often requires learned translators or assumptions about model compatibility. We introduce SYNC (Symbol-Indexed Neural Communication), a word-indexed interface that connects heterogeneous models without fine-tuning or a learned translator. From descriptions only it can see, the sender selects words from a shared list and sends their indices for each object, without seeing the questions. The receiver writes the described facts into its hidden states using its own word directions, vectors fitted once from its activations. We test selective use by swapping one attribute between two objects and requiring correct answers about both changed and unchanged attributes before and after the swap, four answers in total. We choose an early write layer on four development receivers and then fix it. With three different senders and nine newer receivers from five families, four-answer success on new scenes reaches 72.0-98.3%, up to 96 percentage points above middle-layer writing, and the two largest receivers match plain text. A task-free probe predicted in advance which depths each new receiver can use (45 of 45 cases). Without retuning, messages listing every fact keep 89.6-100% success under new layouts, and sender messages reach 23.9-64.0% on a landmark task with multi-token symbols, below text but from 0% without a message. These results show that shared word indices and receiver-local directions can support selective fact use across model families without additional training.

</details>


### 139. Function-Space Temporal Self-Distillation for Policy Optimization

- **Authors:** Aryan Das, Arnab Bhattacharya, Vinay Kumar Verma
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19687v1](http://arxiv.org/abs/2610.19687v1)
- **PDF:** [https://arxiv.org/pdf/2610.19687v1](https://arxiv.org/pdf/2610.19687v1)
- **Categories:** cs.LG, cs.AI, cs.CL, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) improves reasoning in language models, but scalar outcomes provide coarse supervision over response trajectories. Self-distillation offers denser token-level guidance by comparing an unassisted policy with a feedback-informed self-teacher, yet the teacher evolves with the student, creating unstable targets and motivating additional regularization. We introduce Function-Space Policy Optimization (FSPO), a single-policy framework that combines current privileged adaptation with function-space temporal consolidation. FSPO stores sparse historical next-token distributions as fixed temporal targets, providing temporal separation without maintaining a persistent teacher model. It further introduces privileged disagreement correction to explicitly suppress locally overvalued actions, reliability-adaptive grounding that strengthens reference supervision when self-generated evidence repeatedly fails, and quality and coverage-aware temporal memory that retains verified behaviors and improves privileged demonstrations. Across reasoning and tool-use benchmarks, FSPO achieves the highest average accuracy under a 5-hour training budget, improving over the strongest baseline by approximately 4% points on average while reducing peak memory from about 70 GB to 56 GB on Olmo3-7B-Instruct.

</details>


### 140. Measuring and Reducing Unusable Replies of LLM Agents

- **Authors:** Yilin Jiang, Fei Tan, Xuanyu Yin, Guanchu Wang, Xia Hu, Yutao Yue
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19659v1](http://arxiv.org/abs/2610.19659v1)
- **PDF:** [https://arxiv.org/pdf/2610.19659v1](https://arxiv.org/pdf/2610.19659v1)
- **Categories:** cs.CL, cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

People delegate multi-step work to LLM agents and read only the reply that the agent hands back. Current evaluation scores task completion and the faithfulness of reports, and it leaves open whether the requester can understand and use the reply. We call this property reply usability and measure it with a reader model that takes the requester's position and tests whether the reply can be interpreted from what the requester has seen, is in the requester's language and answers the request. Its agreement with the majority of five annotators lies within the range of the individual annotators. Across eight models from seven families, 54% of 480 replies fail, and the best model still fails on 30%. Failed replies mostly point to material the requester has not seen or use labels that the agent coined during its work. Stating explicit requirements for the reply reduces the failure rate from 0.52 to 0.43 together with errors and omissions, and a secondary model that rewrites the reply reduces it to 0.36, which human annotators confirm in a blind comparison. Reply usability can thus be scored alongside task success and improved with one appended message or one call to a secondary model.

</details>


### 141. J-tau: A Fully Localized Japanese Benchmark for Tool-Agent-User Interaction

- **Authors:** Chihiro Yano, Jun Hirako, Hiroaki Yamagiwa, Ryota Hirobuchi
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19638v1](http://arxiv.org/abs/2610.19638v1)
- **PDF:** [https://arxiv.org/pdf/2610.19638v1](https://arxiv.org/pdf/2610.19638v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present J-tau, the first publicly available Japanese benchmark for evaluating tool-using LLM agents in interactive customer-support scenarios. While tau-bench is widely used to evaluate LLM agents, it is English-centric and cannot evaluate agents in other languages. Existing multilingual extensions offer no public Japanese version and rely primarily on machine translation, leaving locale-specific entities such as addresses and currencies inconsistent with the target region. To enable reliable evaluation in Japanese, we carefully localize tau-bench through machine translation, entity adaptation, and human review. During this process, we also uncover and fix two flaws in the original tau-bench: invalid tasks and a score aggregation error that inflates certain models' results. Experiments show that J-tau yields fewer evaluation errors than a naively machine-translated counterpart and that our fixes resolve both flaws.

</details>


### 142. Divergent Paths: Learning an Outcome-Predictive Representation of LLM Agent Trajectories

- **Authors:** Alexander Gill, Guram Gogia, Francisco Guzmán
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19614v1](http://arxiv.org/abs/2610.19614v1)
- **PDF:** [https://arxiv.org/pdf/2610.19614v1](https://arxiv.org/pdf/2610.19614v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

In this work, we reframe agentic trajectories as paths through a shared embedding space of actions and environmental observations. We show that successful and failed rollouts of the same task separate in this space, with simple per-task discriminators predicting held-out rollout outcomes at up to 0.95 AUROC across three agent benchmarks and three policy models. To exploit this signal across tasks, we introduce Precog-RM, a transformer-based model that meta-learns a representation in which outcome prediction can be performed in a few-shot setting. We show that Precog-RM generalizes to unseen tasks and models, and gives confident predictions of trajectory success long before termination. Deployed as an early stopping controller for Group Relative Policy Optimization (GRPO) on Tau2-Bench, Precog-RM cuts training FLOPs by up to 47.3\% while maintaining performance comparable to baseline GRPO.

</details>


### 143. JockeyBench: Evaluating LLM Agents on Horse-Racing Decision-Making

- **Authors:** Zhongwei Xie, Xingsu Li, Jingqiao Yu, Zihao Wang, Hong ChiTat, Zhaowei Wang, Weizhi Du, Yuxuan Liu, Huihao Jing, Jiaxin Bai, Yangqiu Song
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19589v1](http://arxiv.org/abs/2610.19589v1)
- **PDF:** [https://arxiv.org/pdf/2610.19589v1](https://arxiv.org/pdf/2610.19589v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Repeated event forecasting requires extracting predictive signals from noisy evidence and evaluating their value across successive decisions. We introduce JockeyBench, a benchmark and evaluation protocol that studies this problem through historical Japanese horse racing. The protocol combines time-gated evidence, priced tools, paired frozen-program controls, and two workflows: executing an LLM-written predictor or acquiring evidence for a fresh per-race LLM forecast. Evaluation separates forecast quality, benchmark-specific net utility, and retrospective betting returns and risk under fixed decision rules. Across 28 model--scaffold configurations on 324 races, paired tests identify seven revision gains and two declines after multiple-testing correction. Yet every configuration has negative mean profit under capped-Kelly settlement. In a four-model comparison, the reusable-program workflow has higher mean betting profit and lower research fees, although both workflows lose on average. Further diagnostics reveal that mean probability bias reverses on selected bets and that profitable individual runs can depend on concentrated returns. These findings motivate evaluating predictive competence, adaptation, resource use, and decision value separately when assessing agents for repeated event forecasting.

</details>


### 144. Moral Combat: Exploiting Moral Foundations Theory to Jailbreak LLMs

- **Authors:** Adel Khorramrouz, Yi-Chia Wang, Sharon Levy
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19587v1](http://arxiv.org/abs/2610.19587v1)
- **PDF:** [https://arxiv.org/pdf/2610.19587v1](https://arxiv.org/pdf/2610.19587v1)
- **Categories:** cs.CL, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Social psychology has long described how people can be persuaded to interpret a harmful act as moral. Recent research suggests that Large Language Models (LLMs) echo aspects of human psychology, from cognitive biases to social conformity. This raises a question with direct safety implications: can LLMs be moralized to bypass safety guardrails? We answer this question with a multi-agent framework grounded in Moral Foundations Theory (MFT). Given a harmful request that is initially refused, our agents diagnose which moral foundation (MF) the prompt is violating, identify a justifiable foundation under which the same request appears virtuous, rewrite the prompt accordingly, and reinforce it with generated precedents of comparable moral reframing. We evaluate our framework on harmful prompts from three well-known jailbreak datasets across five open-source and proprietary models. Our analysis reveals that models are highly susceptible to moralization, exhibiting high single-trial jailbreak rates with success increasing further under repeated attempts. We also find that safety benchmarks are imbalanced in the MFs they violate, concentrating on foundations toward which models already exhibit biases.

</details>


### 145. XferAgent: Cross-Agent Experience Transfer for Self-Improving LLM Agents

- **Authors:** Weihao Li, Jun Bai, Shijie Chen, Qincheng Lu, Xinyu Wang, Ziyang Song
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19581v1](http://arxiv.org/abs/2610.19581v1)
- **PDF:** [https://arxiv.org/pdf/2610.19581v1](https://arxiv.org/pdf/2610.19581v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents can reuse experience from prior task executions to improve performance on subsequent tasks. Although existing methods enable cross-agent experience sharing, differences in agents' execution histories and task requirements make shared experiences difficult to reuse effectively. We propose XferAgent, a framework for cross-agent experience transfer that organizes reusable experience in local and shared experience graphs. XferAgent reconciles compatible contributions from heterogeneous agents while avoiding unreliable merges. For each new task, it selects shared experiences and integrates them with the target agent's local experience to support task execution. Experiments across diverse task domains show improvements over representative memory-based methods and effective experience transfer between heterogeneous agent frameworks. Cumulative task success also increases over successive task passes as agents update and reuse their experiences.

</details>


### 146. $τ$-Emotion-Bench: Exposing the Interaction Fragility of LLM Agents through Real-World User Emotions

- **Authors:** Rishitosh Kumar Singh, Amir Saeidi, Shamanthak Hegde, Shrinidhi Kumbhar, Chitta Baral
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19560v1](http://arxiv.org/abs/2610.19560v1)
- **PDF:** [https://arxiv.org/pdf/2610.19560v1](https://arxiv.org/pdf/2610.19560v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

In long-horizon tool-calling tasks, LLM agents can fail not only because of tool-use errors, but also because of ineffective interaction with users. Yet existing benchmarks largely assume cooperative and behaviorally stable users, leaving the effect of emotional variation on agent reliability underexplored. We introduce $τ$-Emotion-Bench, a ten-domain benchmark for evaluating tool-calling agents under controlled emotion-conditioned user interactions while preserving the underlying task objective. To scale both benchmark construction and agent training, we introduce Tracer, a scalable agentic data-generation pipeline that constructs grounded, policy-valid tasks and collects trajectories through an interactive agent--user--environment harness. By allowing dissatisfied users to terminate inefficient interactions, the harness provides an interaction-aware signal that filters trajectories with excessive user dependence and favors effective tool use. Experiments with two user simulators show that frontier agents remain unreliable, with substantial gaps between average task success and consistent task completion. Tracer-generated supervision consistently improves Qwen3 models across scales, generalizes to unseen domains, and transfers to $τ$-Bench and $τ$-Trait. Behavioral analyses further show that higher task success is associated with a better balance between tool execution and necessary user follow-up. Overall, $τ$-Emotion-Bench and Tracer provide a scalable framework for evaluating agent reliability under diverse user behaviors and improving tool-calling agents through interaction-aware supervision.

</details>


### 147. ActICL: Post-Training for Agentic Multimodal In-Context Learning

- **Authors:** Yanshu Li, Ruixiang Tang, Junyi Jessy Li, Elias Stengel-Eskin
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19475v1](http://arxiv.org/abs/2610.19475v1)
- **PDF:** [https://arxiv.org/pdf/2610.19475v1](https://arxiv.org/pdf/2610.19475v1)
- **Categories:** cs.CV, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal in-context learning (ICL) is an important capability of multimodal large language models (MLLMs). Its performance is closely tied to the demonstrations it uses, making demonstration retrieval a core problem for ICL. Common methods use fixed scoring methods to retrieve all the demonstrations at once, which may introduce redundancy and noise. Context-aware retrieval methods have emerged to address this problem by allowing incremental retrieval from a growing context. However, none of them lets the MLLM learn how to judge what new demonstrations it needs and then carry out progressive retrieval on its own. To this end, we introduce ActICL, which trains an MLLM agent to acquire and use an ICL context via tool-augmented reasoning. An ActICL agent analyzes its own information gaps during iterative reasoning and tool-use actions. Based on these gaps, it performs targeted retrieval to acquire a set of initial candidates. It can then use the existing context to further filter the candidates and refine the context, or it can iteratively perform a new retrieval. When the agent judges that the context is sufficient for the task, or when the resource limit is reached with the user request met, it sends the acquired context to an answering model, either the agent itself or another MLLM. We use a two-stage post-training procedure that jointly optimizes the agent's acquisition and answering. With an adaptive number of demonstrations, ActICL improves average performance by 11.6 percentage points over standard similarity-based retrieval across seven benchmarks and three MLLMs, and by 4.4 points compared to the strongest prior baseline. The contexts acquired by ActICL agents can also be used effectively by frontier models. When GPT-5.6-Sol performs 4-shot ICL, ActICL's contexts improve its performance by 3.5 points over standard retrieval, averaged over three benchmarks.

</details>


### 148. PFedMA: Who Should Join Next as Federated Multi-Agent Orchestration Evolves?

- **Authors:** Shuai Li, Shengyuan Liu, Fan Qi, Xiaoshan Yang
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19458v1](http://arxiv.org/abs/2610.19458v1)
- **PDF:** [https://arxiv.org/pdf/2610.19458v1](https://arxiv.org/pdf/2610.19458v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Federated Multi-Agent Systems (FedMAS) offer a promising paradigm for collaborative reasoning among LLM-based agents while keeping raw client data decentralized. However, reliable multi-round collaboration remains challenging. Agent selection must take into consideration evolving task requirements and the agent's historical reliability, while privacy rules must adapt to changing collaboration contexts and meet the client's personalized needs. To address these challenges, we propose PFedMA, a federated multi-agent framework for feedback driven multi-round collaboration under heterogeneous privacy requirements. Across rounds, PFedMA maintains historical capability and reliability states to guide agent selection, evaluates task responses before aggregation, and refines subsequent queries according to accumulated collaboration feedback. PFedMA enables bidirectional local to global and global to local private rule evolution across heterogeneous clients. Clients generalize locally updated privacy rules and selectively incorporate globally maintained rules, thereby facilitating cross-client privacy rule evolution while preserving personalized constraints. Extensive experiments across reasoning, privacy sensitive, and adversarial settings show that PFedMA improves task performance, reduces measured privacy leakage, and improves system robustness.

</details>


### 149. AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System

- **Authors:** Tianzhu Hu, Hang Yu, Zeyuan Zhao, Zeyu Pan, Huan Luo, Chun Gan, Mingzhe Cao, Liubin Wang, Mingming Li, Jiao Dai, Jizhong Han, Songlin Hu
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19454v1](http://arxiv.org/abs/2610.19454v1)
- **PDF:** [https://arxiv.org/pdf/2610.19454v1](https://arxiv.org/pdf/2610.19454v1)
- **Categories:** cs.AI, cs.IR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Digital advertising is an important means for platforms to reach potential users and drive business growth. Advertising delivery is the core link between marketing objectives and actual returns. Existing methods have achieved partial automation in individual tasks such as bidding and budget allocation, but they still rely on human operators for overall coordination, making it difficult to support large-scale operations. They also often fail to achieve optimal performance, and individual experience remains difficult to turn into reusable operational capabilities. In addition, as advertising markets change, advertising delivery systems need timely strategy updates to remain effective in dynamic markets. To automate the entire advertising operations process and improve adaptability to market changes, we propose AdCoEvo, a co-evolving multi-agent advertising delivery system. Specifically, the system connects delivery decisions across different timescales and operational granularities through role specialization. Diagnostic results guide account planning and strategy adjustment in the next period. The multi-agent system updates its model parameters based on actual delivery outcomes and continually improves delivery strategies through mutual feedback among planning, adjustment, and diagnosis, thereby achieving co-evolution. Experiments show that, relative to the rule-based operational baseline (Rule), AdCoEvo increases advertiser value by 14.02% while reducing cost per acquisition by 7.07%. Compared with a multi-agent system with fixed parameters, AdCoEvo increases advertiser value by 3.96% and reduces cost per acquisition by 1.24%, indicating that co-evolution can yield greater delivery returns.

</details>


### 150. EvoProbe: Evaluation-Driven Benchmark Evolution for LLM Agents

- **Authors:** Qianhong Guo, Wei Xie, Xiaofang Cai, Shuoyoucheng Ma, Chengxin Hu, Baosheng Wang
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19433v1](http://arxiv.org/abs/2610.19433v1)
- **PDF:** [https://arxiv.org/pdf/2610.19433v1](https://arxiv.org/pdf/2610.19433v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Static benchmarks for large language model (LLM) agents face saturation and data contamination risks, motivating continual updates to evaluation tasks. However, aggregate scores and success rates offer limited insight into specific problem-solving bottlenecks and provide limited guidance for subsequent task design. We propose EvoProbe, an evaluation-driven benchmark evolution framework that integrates task generation, diagnostic evaluation, and feedback-driven regeneration into a closed loop. It combines verifiable subtask outcome scoring with evidence-supported multi-judge trajectory evaluation and distills phase-level bottlenecks, success patterns, and failure patterns into diagnostic feedback for generating new executable tasks. Across two rounds of cybersecurity experiments, evaluations of eight models on 66 tasks reveal phase-level performance differences and common failure patterns beyond aggregate scores. In a cross-round comparison with the Examiner model set and solver configuration held fixed, all eight models achieve lower Outcome scores on the updated tasks, with relative decreases of 11.8\% in mean Outcome and 40.0\% in mean Pass\textasciicircum{}3. These results support using fine-grained diagnostics to guide iterative task updates and probe agents' current capabilities and limitations.

</details>


### 151. AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety

- **Authors:** Chenxu Wang, Xiaoyu Wen, Han Qi, Ziyuan Zhou, Cheng Jin, Chaochao Lu, Qiaosheng Zhang
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19422v1](http://arxiv.org/abs/2610.19422v1)
- **PDF:** [https://arxiv.org/pdf/2610.19422v1](https://arxiv.org/pdf/2610.19422v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents accomplish complex tasks through multi-turn interactions with external tools. However, malicious content embedded in user queries, tool descriptions, or environment observations can manipulate their decisions and induce unsafe actions. Adversarial co-evolution has emerged as an effective approach to strengthening LLM safety, but existing work primarily focuses on language-level safety or indirect prompt injection in web tasks. In this paper, we introduce AgentSafeEvo, a co-evolutionary reinforcement learning framework for agent safety built on an attacker-defender game spanning diverse tasks and attack types. The attacker learns to construct adversarial agent tasks that expose weaknesses in the defender's tool use, while the defender learns to complete tasks safely under these attacks. We further introduce learnability-guided task weighting, which uses within-task defender-reward variability to adjust each task's contribution to attacker and defender updates. Extensive experiments on agent safety and general capability benchmarks demonstrate that our method improves adversarial robustness while maintaining general agent capabilities.

</details>


### 152. KoAGE: Do Large Language Models Know, Learn, and Coin Korean Neologisms?

- **Authors:** SungHo Kim, Eojin Jeon, SangKeun Lee
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19399v1](http://arxiv.org/abs/2610.19399v1)
- **PDF:** [https://arxiv.org/pdf/2610.19399v1](https://arxiv.org/pdf/2610.19399v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Korean neologisms arise through diverse mechanisms, a demanding test of language models beyond lexical memorization. To enable systematic evaluation, we introduce NeoTrace, an automated, rerunnable framework that collects and dates neologisms across genres. Its 4,271 entries support KoAGE, a cutoff-aware benchmark with three acquisition and two generation tasks---the latter, to our knowledge, the first to compare model coinages with attested neologisms under their original materials and community context. Across 21 models, lexical recall diverges from contextual inference: in a five-model temporal analysis, models define only 13-30% of cutoff-year words, yet can infer meaning from one usage. However, structural understanding remains limited: even correct definitions barely improve formation analysis of pre-cutoff neologisms. Given word-building materials, single models often follow human formation mechanisms, whereas multi-agent coinage favors abbreviation and depends on interaction framing. KoAGE thus separates what models know, learn from use, and coin.

</details>


### 153. Beyond Corrected Actions: Training LLM Agents on Textual Critiques

- **Authors:** Thomas Zeng, Zelei Cheng, Mingyang Zhou, Sambit Sahu, William Campbell, Genta Indra Winata
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19367v1](http://arxiv.org/abs/2610.19367v1)
- **PDF:** [https://arxiv.org/pdf/2610.19367v1](https://arxiv.org/pdf/2610.19367v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly used for multi-turn agentic tasks that require interactions with users and environments over extended sequences of actions. A common approach to improving LLM agents is to use more capable expert models to provide training supervision, either by behavior cloning the expert's trajectories or by using the expert to correct the actions in trajectories generated by the weaker student model. However, expert LLMs can provide richer supervision than actions alone: they can directly generate textual critique that explain why specific actions are incorrect. We study whether training on such feedback benefits LLM agents and propose Critique-Augmented Agentic Fine-Tuning (CAFT), a framework that elicits textual expert feedback on student-generated trajectories. For each incorrect action, the expert yields both a corrected action and a textual critique explaining the student's mistake--which we then use as the training target for fine-tuning. Across four student models from the Nemotron 3 and Gemma 4 families on the agentic domains $τ^2$-Bench Airline+Retail and WebShop, adding critiques to action-level supervision improves performance by 8% on average over action-only distillation. Additionally, CAFT checkpoints can also provide a better warm start for reinforcement learning than expert-trajectory distillation. Our results demonstrate that textual critiques can strengthen supervision for multi-turn LLM agents.

</details>


### 154. Where to Start, How to Move: Analyzing Curricula under GRPO for Long-Horizon LLM Agents

- **Authors:** Minchan Kim, Sungho Bae, Youngjin Kim, Hyunwoo Park
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19349v1](http://arxiv.org/abs/2610.19349v1)
- **PDF:** [https://arxiv.org/pdf/2610.19349v1](https://arxiv.org/pdf/2610.19349v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Group Relative Policy Optimization (GRPO) provides no reward-relative learning signal when all rollouts receive identical rewards. In long-horizon tasks that require multiple interactions, rewards are given only upon successful task completion, making all-fail groups common early in training and limiting opportunities to practice later steps. Guide Assisted GRPO replays a successful reference prefix before the learner continues. We study how initial positions, handoff units, and movement rules affect unassisted task completion. Across three model sizes on BFCL, starting near completion is more effective under a fixed turn-level threshold rule. Finer handoffs alone do not consistently help, but outcome-informed tool-call selection outperforms GRPO on trained and untrained task categories. Guided starts also improve AppWorld success on both evaluation splits. These findings highlight where learning starts and how starting positions move as key curriculum choices.

</details>


### 155. When Is Smaller Greener? Right-Sizing Language Models for Agentic AI

- **Authors:** Sajid Siraj, Maria Barbati
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19345v1](http://arxiv.org/abs/2610.19345v1)
- **PDF:** [https://arxiv.org/pdf/2610.19345v1](https://arxiv.org/pdf/2610.19345v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents use large language models (LLMs) to plan and act over multiple steps, yet models are usually compared per call rather than per completed task. This paper asks: which model should an agent use to complete tasks reliably while minimising energy, cost and time? We show that per-call comparisons can be misleading for agentic AI. Because a task succeeds only if all required steps succeed, small differences in per-step reliability can produce large differences in overall task success. Failed attempts also consume resources. We therefore evaluate models using energy, cost and time per successfully completed task, treating the completed task as the functional unit. On this basis, we develop a decision model for choosing LLMs in agentic workflows. The model applies to tasks with binary or graded outcomes and to settings with or without retries. We show that each resource has a crossover task length at which a smaller, less reliable model ceases to be the greener, cheaper or faster option. These crossovers divide tasks into three regimes: for short tasks smaller models are preferred, for long tasks larger models are preferred, and only between these extremes do preferences among objectives matter. We embed these results in a two-stage framework that separates efficiency from preference. A Pareto screen first removes models that are never competitive; a weighted decision is required only when a genuine trade-off remains. A pilot study of 15 open-weight models from five developers, ranging from 0.6B to 27B parameters, on two multi-step agent tasks with measured GPU energy supports the predicted structure. The model with the lowest energy per completed task changes with task length and task type, and observed crossover points generally match those predicted from per-step measurements. These findings provide a practical framework for right-sizing language models in agentic AI.

</details>


### 156. Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States

- **Authors:** Sarath Shekkizhar, Prathyusha Jwalapuram, Zixuan Ke, Vaidehi Patil, Jiayu Wang, Srijan Bansal, Trong Huy Nguyen, Dingfeng Jiang, Dongqi Liu, Ruochen Zhao, Wei Lu, Giuseppe Carenini, Mohit Bansal, Silvio Savarese, Shafiq Joty
- **Published:** 2026-10-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19342v2](http://arxiv.org/abs/2610.19342v2)
- **PDF:** [https://arxiv.org/pdf/2610.19342v2](https://arxiv.org/pdf/2610.19342v2)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agents are increasingly interacting with other agents that act for different principals (people or organizations on whose behalf they work), such as a buyer's personal agent negotiating with an enterprise's seller agent. In such agent-to-agent (A2A) scenarios, each agent has its own environment and holds information and authority that the other cannot see. Moreover, the interests of each agent may be aligned (cooperative), partly aligned (mixed-motive), or opposed (competitive). Existing multi-agent system failure studies assume one orchestrator, shared workspace, or single principal. We ask how A2A systems fail when these assumptions are removed. We study more than 2,500 recorded runs of A2A systems built from different agent harnesses and models, spanning 488 scenarios across eight families (legal, CRM, security, commerce, etc.). From these traces, we derive $A^2$-Failures, a taxonomy of 20 A2A failure modes in four categories: (i) discovery and delegation, (ii) grounding and record consistency, (iii) verification, and (iv) conduct and fidelity. Three findings hold across every harness, model, and scenario studied: (1) discovery and interaction are driven by the phrasing of the task rather than the availability of peer agents; (2) no agent verifies a peer's factual claim on its own initiative, so an A2A system inherits the reliability of its least reliable participant unless the protocol or mechanism performs the check; and (3) the aggregate outcome score credits the agent completing the task while staying blind to the coordination, verification, and conduct failures beneath it, so A2A systems must be evaluated per agent, against each agent's own principal. We release the run logs behind the taxonomy at https://huggingface.co/datasets/a2a-salesforce/a2-failures.

</details>


### 157. Can LLM Agents Efficiently Identify Appliance Faults? Insights From Diagnosing a Simulated Appliance

- **Authors:** Lucas H. McCabe, Sarah Lukens, H. Howie Huang
- **Published:** 2026-10-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19291v1](http://arxiv.org/abs/2610.19291v1)
- **PDF:** [https://arxiv.org/pdf/2610.19291v1](https://arxiv.org/pdf/2610.19291v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

In so-called "Industry 4.0," integrated sensors, analytics tools, and other digital technologies supplement industrial workflows, potentiating enhanced visibility and automation. Prognostics and health management (PHM) and natural language processing (NLP) practitioners alike have explored the application of large language models (LLMs) to industrial asset management, but many prior works' focus on exam-like benchmarks has limited their assessment of LLMs' ability to automate practical operations. Herein, we introduce CoffeeBench, a fault diagnostics task for LLM agents, using a simulated appliance. The LLMs we evaluate struggle to consistently identify faults from the sensor information alone, but the best-performing ones can iteratively refine the fault-option space to eventually obtain a successful diagnosis. Our subsequent analyses, therefore, focus on: differentiating models by diagnostic efficiency (RQ1); examining the lagging performance of the three worst models (RQ2); and identifying viable heuristics for selective prediction (RQ3), including that initial diagnostic uncertainty and LLM-judged soundness of reasoning are high-signal predictors of diagnostic success. In addition to our benchmark results (Section 3.1), we provide practical insights for improving the performance of the open-weight models on CoffeeBench, such as by explicitly tracking episode state on their behalf to reduce timeouts (Section 3.2) or applying a deliberation loop to refine diagnostic hypotheses (Section 3.3).

</details>


### 158. Agentic Self-Awareness: Aligning Knowing, Acting, and Holding

- **Authors:** Qinglin Chen, Hiroaki Hayashi, Jiaxin Zhang, Chien-Sheng Wu
- **Published:** 2026-10-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19226v1](http://arxiv.org/abs/2610.19226v1)
- **PDF:** [https://arxiv.org/pdf/2610.19226v1](https://arxiv.org/pdf/2610.19226v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Frontier AI agents increasingly act in environments where seemingly solvable tasks may lack prerequisites, contain conflicting requirements, or reveal blockers only during execution. We formulate agentic self-awareness (ASA) as the alignment of task-grounded feasibility judgments (know), warranted behavior (act), and responses to reconsideration (hold), distinguishing what a task permits from what an agent can solve. We build paired feasible and blocked tasks in Terminal-Bench 2.1 and retail $τ^2$-bench and introduce an authorship-aware M0-M3 rubric that separates recognizing a blocker from taking the certified deferral action for the correct reason. Separate probes assess stated feasibility beliefs and responses to a single challenge. In a Terminal-Bench protocol baseline, blocker recognition reaches 84.4%, but strict self-awareness (SA) reaches only 40.6%. Harness search without model-weight updates increases strict SA from 45.3% to 93.8% on reused Terminal-Bench search tasks; selection for abstention alone, however, can reduce success on feasible tasks. Independently initialized joint-objective searches improve both blocked-task SA and feasible-task solve on their own search sets. Retail held-out gains remain limited, and Terminal-Bench blocked-task transfer is not measured. This evaluation pipeline makes the recognition-action gap measurable and sets a two-sided target for improving agent decisions under changing task evidence.

</details>


### 159. Narrowing the Collaboration Gap, Probably

- **Authors:** Mirah Shi, Marcel Hussing, Ira Globus-Harris, Natalie Collina, Aaron Roth, Surbhi Goel
- **Published:** 2026-10-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19215v1](http://arxiv.org/abs/2610.19215v1)
- **PDF:** [https://arxiv.org/pdf/2610.19215v1](https://arxiv.org/pdf/2610.19215v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are increasingly deployed as teams of agents that hold different private information about a shared task. How should such agents concisely communicate in a way that promotes aggregation of decision-relevant information? Communicating only proposed actions can discard decision-relevant uncertainty: two agents may prefer the same action for different reasons. We study an alternative interface in which agents communicate calibrated beliefs over actions. We first analyze a simple synthetic setting that captures the structure of multi-round reasoning under partial information. In this setting, we show theoretically and empirically that communicating unbiased probabilities can be strictly more powerful than communicating actions. We then test the same principle in a collaborative maze-solving task with trained transformers and pretrained LLM agents. Our results demonstrate that probability communication outperforms action communication when the exchanged predictions preserve calibrated uncertainty. When communicated probabilities are biased, we show that the benefits of probability communication can disappear. We give a post-hoc conversational calibration intervention that consistently improves decision-making by correcting these biases both in a toy transformer setting and when pretrained LLMs use the corrections in context. These results suggest that probabilistic communication is useful for multi-agent collaboration not merely because it transmits more information, but because calibrated uncertainty gives other agents a reliable object to update on.

</details>


### 160. Identity, Incentives, and Cooperative Behavior for AI: Reverse-Engineering Multiagent Cooperation

- **Authors:** Andrew Perrault, Bryan Wilder
- **Published:** 2026-10-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19188v1](http://arxiv.org/abs/2610.19188v1)
- **PDF:** [https://arxiv.org/pdf/2610.19188v1](https://arxiv.org/pdf/2610.19188v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The behavior of AI systems increasingly depends on the extent to which agents cooperate or coordinate with one another, in ways that may be desirable or not depending on the situation. Conventional explanations for cooperative behavior distinguish between purely other-regarding preferences ("altruism") and instrumental reasons for self-interested agents to cooperate. The way that agents should enact these mechanisms for cooperation (or not) is complicated by the fact that there is not a clear or unambiguous locus of identity or selfhood for AI agents. For example, it is unclear whether agents involved in instances of misaligned collective behavior are motivated by goals at the level of the collective or by various forms of instrumental reasoning. We develop a framework for reverse-engineering why a given set of agents engage in a particular set of cooperation-related behaviors. We argue that many different mechanisms can often produce similar observed behaviors and introduce a set of experimental designs along with conditions under which they can successfully disentangle competing explanations for multiagent behavior. We apply this framework to interactions from a set of frontier models in a simulated environment and demonstrate that the behavior of different models arises from substantively different mechanisms.

</details>


### 161. Into the Unknown: Benchmarking AI agents on open scientific research problems

- **Authors:** Seungone Kim, Jiayi Geng, Young-Jun Lee, Bo Liu, Juyoung Suk, Nicholas Lubbers, Mitchell Wood, Marcus Noack, Yong-Xin Yao, Yuan Shi, Roxana Bujack, Cristina Garcia Cardona, Austin Rodriguez, Ilon Joseph, Woojin Cho, Zora Zhiruo Wang, Chuanyang Jin, Ian Wu, Apurva Gandhi, Tianjian Li, Weiwei Sun, Carolin Lawrence, Kiril Gashteovski, Dongyeop Kang, Jay Shin, Akari Asai, Graham Neubig, Sean Welleck
- **Published:** 2026-10-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19159v1](http://arxiv.org/abs/2610.19159v1)
- **PDF:** [https://arxiv.org/pdf/2610.19159v1](https://arxiv.org/pdf/2610.19159v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Can AI agents carry out research on open scientific problems? We introduce Into the Unknown, a benchmark that provides an agent with a science paper along with a research direction to pursue and tasks it to write a follow-up paper. We work with scientists at US Department of Energy (DOE) national laboratories, who each contribute an unpublished follow-up direction from their own work together with the necessary conditions a submission must meet. While assessing the quality of a follow-up paper is challenging in general, using these conditions to form a rubric makes evaluation more tractable for research problems that have no reference answer. We have nine frontier agents write 15 follow-ups each, spanning quantum computing, plasma physics, computational chemistry, materials science, and scientific machine learning domains. None of the 135 submissions satisfies all the conditions, and 114 fail our integrity check, most often because the paper claims work that was never done or reports numbers that contradict the recorded evidence. Overall, agents readily produce papers that look like follow-ups, but none meets the standard of the domain scientist, leaving substantial headroom. Our code and data are publicly available.

</details>


### 162. AgentCIScope: Grounded Contextual Integrity Evaluation for LLM Agents

- **Authors:** Chengquan Guo, Zhaorun Chen, Zinan Lin, Xiaodong Liu, Bo Li
- **Published:** 2026-10-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19158v1](http://arxiv.org/abs/2610.19158v1)
- **PDF:** [https://arxiv.org/pdf/2610.19158v1](https://arxiv.org/pdf/2610.19158v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are becoming increasingly capable of handling daily workspace tasks by interacting with application environments through tool calls. However, as agents read and write sensitive user data across email, documents, and other applications, a central privacy question is whether they preserve contextual integrity (CI), that is, whether the information flows they produce comply with context-specific disclosure constraints. Existing work either focuses on model-level privacy leakage or evaluates agents in limited application environments with manually constructed disclosure constraints. In this work, we introduce AgentCIScope, a unified platform and benchmark for evaluating agent-level contextual integrity through executable, multi-step tasks across diverse, realistic application environments. AgentCIScope transforms public and synthetic privacy cases into executable agent tasks, with disclosure constraints grounded in three criteria: governing privacy policies, persona-based agreement, and a predefined sensitive-attribute taxonomy. Based on AgentCIScope, we evaluate 12 agents on 936 tasks and find that strong task-completion capability does not guarantee contextual-integrity preservation: single-run leakage rates range from 32.5% to 94.4%, while repeating each task five times further increases leakage by 4-19 percentage points. Leakage varies substantially across attributes: personal preferences and booking details have average leakage rates of 84.7% and 76.5%, compared with 17.1% for credit-card information and 29.4% for SSNs; environments: calendar has the highest average leakage rate as an information source, while WhatsApp ranks highest as an information destination; and governing privacy policies. AgentCIScope provides deep insights into agent privacy leakage and serves as a unified testbed for developing privacy-preserving agents.

</details>


### 163. Compiling Expert Procedures into Verified Programs: When a Small Model Is Enough

- **Authors:** Vishvesh Bhat, Asad Aali, Muhammad Ahmed Mohsin
- **Published:** 2026-10-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19148v1](http://arxiv.org/abs/2610.19148v1)
- **PDF:** [https://arxiv.org/pdf/2610.19148v1](https://arxiv.org/pdf/2610.19148v1)
- **Categories:** cs.AI, cs.SC


> Summary unavailable.


<details>
<summary>Abstract</summary>

In procedural tool-use domains, how much of the gap between base models is procedure rather than capability? We build an explicit program from a teacher's traces and run it in front of unchanged small models, including an 8B model. The construction, PLVR , takes the reasoning traces of a teacher, Kimi-K3, clusters their segments to locate recurring operations, has a frontier model author one typed primitive per operation, each run by a small frozen model and assembles the program by A* search over a mined rule library, under a reference-action objective. At inference the program takes one of two forms: for troubleshooting and tool search it produces the chain of thought the student would otherwise generate for itself, and the student acts on it; for multi-turn tool matching the student proposes each action and the program checks, repairs, or retries it before it goes out. On the official tau2-Bench Retail and Telecom test sets and on LiveMCPBench, with three Nemotron base models and the same program for each, the answer depends on the domain. On Telecom, Granite-4.2-8B as the student goes from 43.0% to 91.2% under the program, and every Nemotron student reaches 93.3-94.4%, against at most 58.2% for fine-tuning on the same traces, prompt optimisation of the student, or two token-matched baselines. With Granite-4.2-8B as the student, the program is within 2 to 3 points of the Nemotron students on Telecom and within 3 on Retail, and 3 to 13 points below them on LiveMCPBench: where the domain is procedural an 8B student is enough, and on tool search the student still matters. On Retail and LiveMCPBench the program is competitive with the best baseline. The spread between base models shrinks from about 7 points to about 2, averaged over the suites, with no weights changed.

</details>


### 164. Plant Memory: Technical Language Processing and a Verified Maintenance Ontology for Agent-Accessible Failure Knowledge from SAP PM Work Orders

- **Authors:** Akash Raj
- **Published:** 2026-10-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.19131v1](http://arxiv.org/abs/2610.19131v1)
- **PDF:** [https://arxiv.org/pdf/2610.19131v1](https://arxiv.org/pdf/2610.19131v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Maintenance work orders are the largest written record of how industrial equipment fails, yet in most plants they are close to unusable for analysis. Short texts are abbreviated and misspelt, asset identity is buried in free text, work-type labels contradict the work described, and the fields that matter most for reliability (symptom, root cause, action taken) are usually empty. As a result, diagnostic knowledge stays with senior technicians and leaves when they do. We present Plant Memory, a system that applies technical language processing (TLP) to SAP Plant Maintenance (PM) exports and builds an ISO 14224-aligned maintenance ontology in which every extracted statement is a reified fact carrying a confidence score, the evidence it was read from, and a verification state. Extraction is rule-first, with an optional large language model (LLM) acting as a second reader whose disagreements raise a fact's review priority rather than overwrite it. Technicians verify facts through a review queue, answer targeted knowledge-gap questions where failures repeat without a recorded cause, and approve or reject ontology drift proposals when new terms appear. The resulting graph is served to people through a web application and to AI agents through a Model Context Protocol (MCP) server, so both query the same verified knowledge and every answer cites the work orders behind it. On a synthetic 12-month export of 400 work orders from a parboiled-rice plant, rule-based extraction reaches 96.2% component accuracy, 88.9% failure-mode accuracy and 100% root-cause precision at 62% coverage; on 28 diagnostic questions, ranked root causes from the ontology are correct at top-1 in 82.1% of cases against 53.6% for the raw SAP root-cause column.

</details>



## Biorxiv (3 papers)


### 1. BioMINTREL expands biological problem solving through cross-disciplinary representations

- **Authors:** Dong, J., Zhang, Y., Gao, E., Yang, C., Wang, J., Zha, C., Wu, Z., Xu, X., Zhou, J., Gao, X.
- **Published:** 2026-10-16
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.10.757703](https://doi.org/10.64898/2026.10.10.757703)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Biological research agents often rely on familiar analytical methods, limiting the questions explored in existing data. We introduce BioMINTREL, an AI agent that finds methods from other disciplines and connects them to biological measurements. It can draw on relationships among datasets and complementary ideas from several methods to develop new questions and analyses. We evaluate it on BioMDC-Bench, which assesses 228 possible applications of computational methods to biological tasks. Compared with GPT-5.4 mini and Qwen3.6-35B, BioMINTREL improves F1 agreement with human experts by up to 45.3 percentage points and increases coverage of applications supported by studies published in subsequent years by up to 58.8 percentage points. Four case studies on real data go beyond previous analyses to reveal dose-specific variant effects, constraints on spatial cell communication and routes through perturbation-response states, and identify the sampling needed to test whether rare high-state cells predict later lineage size. These results highlight BioMINTREL's potential to expand questions in existing data and suggest directions for subsequent research.

</details>


### 2. ExpertTwins: Auditable Long Horizon Scientific Panels through Grounded Expertise

- **Authors:** Foroughi pour, A., Shirinifard, A.
- **Published:** 2026-10-15
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.06.757114](https://doi.org/10.64898/2026.10.06.757114)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent language-model systems increasingly assign roles to agents and let them deliberate. A role label, however, does not specify which evidence an agent can bring or which standard it applies before accepting a conclusion. Agents that read one another's outputs tend to converge. We present ExpertTwins, a framework in which each seat of a scientific panel is defined by an inspectable evidence policy. Discipline seats retrieve under field-specific queries, and scientist-associated seats retrieve from attributed publications and a citation-derived scholarly neighborhood. Private initial packets, structured exchange, cited-source disclosure, deterministic quotation checks, and peer source review turn deliberation into an auditable record, which we also render as interactive idea-flow maps. Scientist associations denote publication-grounded perspectives, not replicas or endorsements of named researchers. In a nine-seat, four-turn neuroblastoma panel, 438 of 439 claims passed all attached quotation checks, and seats withdrew or defended positions when challenged on their evidence. A ten-turn panel sustained evidence acquisition and differentiated recommendations without conversational collapse. Across six base models given byte-identical initial packets, four sustained 97.9-99.8% quotation grounding, and at least 91% on every turn, whereas Haiku 4.5 failed by paraphrase and GPT-5 mini by silence. Agreement among strong models fell from 31% of claims at turn one to 5% at turn four. With follow-up questions held fixed, it stayed at 28-33% through turn three and fell to 20% only at the closing turn. Stress runs showed the collapse guardrail escalating through its full intervention ladder when consensus was forced, but missing deference to one unusually strong seat. On idea-flow maps, the forced consensus appeared as parallel lanes of identical ideas, although quotation grounding and participation balance stayed at their maxima. We also reimplemented two close published systems and ran them on matched models, seats, and questions. A multi-persona debate cited only real records, yet none of its cited sentences carried a checkable quotation and it had no way to abstain. An author-memory fusion system ran only after its fact checker was split by seat to fit in context. Its fused answer kept about two-thirds of the fact-checked specialist claims, answered 36 of 60 question parts on which our seats had abstained, and showed the reader 19% of its agents' disagreements. In a computational pathology case study, six scientist-associated agents built distinct pipelines to predict MYCN amplification from whole-slide images. Across six base models, seat-by-model interaction explained 57% of internal variance, and internal rank poorly predicted external rank (r = 0.18 across 36 nominees). These results establish differentiated, source-traceable scientific reasoning as an operational capability and identify the base model as a parameter that must be reported with the protocol.

</details>


### 3. In Vivo Transcriptomics-Based Framework for Systematic Indication Expansion

- **Authors:** Palmer, Z., Koirala, S., Talukdar, N., Zhang, X., Garver, H., Mahlmeister, M., Huang, L., Joseph, D., Leshchiner, D., Shankar, R., Watts, S. W., Li, X., Glicksberg, B. S., Lauver, A., Chen, B.
- **Published:** 2026-10-14
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.10.12.758524](https://doi.org/10.64898/2026.10.12.758524)

- **Categories:** systems biology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Capturing the systemic effects of drugs in vivo remains a fundamental challenge for drug repurposing strategies. Here, we present an in vivo transcriptomics-based drug repurposing framework that profiles multi-organ RNA-seq from drug-treated rodents to model systemic drug responses and match tissue-specific drug signatures against a compendium of disease signatures for indication expansion. We applied this framework to semaglutide, a GLP-1 receptor agonist originally developed for diabetes and subsequently expanded for several other indications. By harmonizing more than 900 human disease transcriptomic signatures via agentic AI and using Z-transformed reversal of gene expression scoring to quantify drug-disease relationships, our approach successfully recovered established semaglutide indications while deprioritizing Alzheimers disease, an indication for which semaglutide was not effective. Top predictions for common diseases were supported by real-world electronic health record data from the Mount Sinai Health System and several predictions for rare indications are proposed for further investigation. This framework provides a scalable strategy for indication expansion across diverse therapeutic agents, especially investigational compounds for which real-world evidence remains sparse.

</details>



## Medrxiv (3 papers)


### 1. inClinico Agent for clinical trial endpoint prediction and prospective evaluation

- **Authors:** Chen, J., Duan, C., Gou, W., Wang, J., Zheng, Z., Leung, H., Naumov, V., Sidorenko, D., Aliper, A., Ren, F., Pun, F. W., Zhavoronkov, A.
- **Published:** 2026-10-16
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.10.13.26365373](https://doi.org/10.64898/2026.10.13.26365373)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

High attrition rates across clinical drug development impose immense clinical and financial burdens, yet prospectively forecasting whether an individual trial will achieve its primary endpoint remains challenging. Here we present a machine-learning system that predicts clinical trial success across phases I-IV, independently modeling studies with efficacy versus safety/toxicity primary endpoints. To prevent lookahead bias and outcome leakage, models are trained on registration-time features, including target and mechanism-of-action precedent, drug modality and novelty, trial design and operational characteristics, and frozen literature-derived target-choice embeddings. Each prediction yields a continuous Predictive Trial Index (PTI) between 0 and 1 reflecting success probability. On a test set of trials initiated in 2021 or later, the efficacy model achieved an area under the receiver operating characteristic curve (AUROC) of 0.828 (95% CI 0.812-0.845; n = 2,347) and the safety/toxicity model reached 0.809 (95% CI 0.787-0.831; n = 1,485). These models are embedded in inClinico Agent, an agentic AI system integrating frontier large language models (LLMs) with deterministic scoring engines, retrieval tools and specialized clinical skills. We also introduce ClinBench, a prospective benchmark of 2,040 ongoing trials evaluated by inClinico Agent and five frontier LLMs, establishing a leakage-free foundation for tracking prospective predictive accuracy as trials reach completion.

</details>


### 2. inClinico Agent for clinical trial endpoint prediction and prospective evaluation

- **Authors:** Chen, J., Duan, C., Gou, W., Wang, J., Zheng, Z., Leung, H., Naumov, V., Sidorenko, D., Aliper, A., Ren, F., Pun, F. W., Zhavoronkov, A.
- **Published:** 2026-10-15
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.10.13.26365373](https://doi.org/10.64898/2026.10.13.26365373)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

High attrition rates across clinical drug development impose immense clinical and financial burdens, yet prospectively forecasting whether an individual trial will achieve its primary endpoint remains challenging. Here we present a machine-learning system that predicts clinical trial success across phases I-IV, independently modeling studies with efficacy versus safety/toxicity primary endpoints. To prevent lookahead bias and outcome leakage, models are trained on registration-time features, including target and mechanism-of-action precedent, drug modality and novelty, trial design and operational characteristics, and frozen literature-derived target-choice embeddings. Each prediction yields a continuous Predictive Trial Index (PTI) between 0 and 1 reflecting success probability. On a test set of trials initiated in 2021 or later, the efficacy model achieved an area under the receiver operating characteristic curve (AUROC) of 0.828 (95% CI 0.812-0.845; n = 2,347) and the safety/toxicity model reached 0.809 (95% CI 0.787-0.831; n = 1,485). These models are embedded in inClinico Agent, an agentic AI system integrating frontier large language models (LLMs) with deterministic scoring engines, retrieval tools and specialized clinical skills. We also introduce ClinBench, a prospective benchmark of 2,040 ongoing trials evaluated by inClinico Agent and five frontier LLMs, establishing a leakage-free foundation for tracking prospective predictive accuracy as trials reach completion.

</details>


### 3. Human-Guided Agentic AI for End-to-End EHR Research: Sequential Antibody-Drug Conjugate Pathways in Breast Cancer

- **Authors:** Loaiza-Bonilla, A., Colovos, C., Kim, D., Grichnik, J. M., Singh, K., Tarantino, P.
- **Published:** 2026-10-14
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.10.13.26365479](https://doi.org/10.64898/2026.10.13.26365479)

- **Categories:** oncology


> Summary unavailable.


<details>
<summary>Abstract</summary>

PURPOSETo demonstrate an end-to-end research workflow combining a large electronic health record (EHR) resource and a multi-agent artificial intelligence (AI) system governed by Human-Guided Orchestration (HGO), using sequential sacituzumab govitecan (SG) and trastuzumab deruxtecan (T-DXd) orders in breast cancer as the clinical use case.

METHODSA June 2026 EHR release contained 4.95 million patients, including 156,051 with breast cancer codes. Muse Spark supported cohort construction, executable statistical analysis, data-quality checks, literature retrieval, and reporting executed through Symbiotic Agent Teaming (SAT) under investigator direction. The main clinical measure was the second-drug record span, from first to last order. Analyses were descriptive and unadjusted; orders did not confirm administration or progression.

RESULTSThe workflow identified 106 patients: 73 had T-DXd ordered first and 33 had SG ordered first. Median second-drug spans were 63 days (interquartile range [IQR], 29-116) for SG after T-DXd and 49 days (IQR, 21-126) for T-DXd after SG; the median difference was -14 days (95% bootstrap CI, -41 to 21; distributional P = 0.42). Reported outputs additionally included cohort definitions, aggregate analyses, evidence context, figures, and a preliminary draft manuscript.

CONCLUSIONThis study provides a concrete model for integrating large EHR resources, agentic AI, and human expertise across the research cycle. The ADC use case illustrates how computational execution and Expert-in-the-Loop (EITL) adjudication can produce interpretable research outputs and refine their scientific meaning, providing a foundation for extending and evaluating this approach across clinical questions.

Context SummaryO_ST_ABSKey ObjectiveC_ST_ABSHow can clinical expertise and agentic AI be integrated from research-question formulation through EHR analysis and scientific reporting, using sequential SG and T-DXd orders as a clinical use case?

Knowledge GeneratedMuse Spark supported cohort construction, executable analysis, data-quality assessment, evidence retrieval, and reporting; investigators directed the work and adjudicated revisions. The resulting 106-patient cohort described recorded ADC path-ways and the review determined record-span timelines.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*