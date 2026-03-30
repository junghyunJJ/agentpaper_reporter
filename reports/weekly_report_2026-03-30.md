# Weekly AI Agent Paper Report

**Generated:** 2026-03-30 10:49
**Period:** 2026-03-23 to 2026-03-29

## Summary

- **Total papers fetched:** 1065
- **Papers matching keywords:** 134
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-03-23) | Change |
|--------|-----------|-----------|--------|
| Total matched | 134 | 171 | -37 |
| arxiv | 131 | 166 | -35 |
| biorxiv | 1 | 0 | +1 |
| medrxiv | 2 | 5 | -3 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (3 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. Breaking the Extraction Bottleneck: A Single AI Agent Achieves Statistical Equivalence with Human-Extracted Meta-Analysis Data Across Five Agricultural Datasets

- **Authors:** Halpern, M.
- **Published:** 2026-03-23
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.02.17.706322](https://doi.org/10.64898/2026.02.17.706322)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundData extraction is the primary bottleneck in meta-analysis, consuming weeks of researcher time with single-extractor error rates of 17.7%. Existing LLM-based systems achieve only 26-36% accuracy on continuous outcomes, and no study has validated AI-extracted continuous data against multiple independent datasets using formal equivalence testing.

MethodsA single AI agent (Claude Opus 4.6) extracted treatment means, control means, sample sizes, and variance measures from source PDFs across five published agricultural meta-analyses spanning zinc biofortification, biostimulant efficacy, biochar amendments, predator biocontrol, and elevated CO2 effects on plant mineral nutrition. Observations were matched to reference standards using an LLM-driven alignment method. Validation employed proportional TOST equivalence testing, ICC(3,1), Bland-Altman analysis, and source-type stratification.

ResultsAcross five datasets, the agent produced 1,149 matched observations from 136 papers. Pearson correlations ranged from 0.984 to 0.999. Proportional TOST confirmed statistical equivalence for all five datasets (all p < 0.05). Table-sourced observations achieved 5.5x lower median error than figure-sourced observations. Aggregate effects were reproduced within 0.01-1.61 pp of published values. Independent duplicate runs confirmed extraction stability (within 0.09-0.23 pp).

ConclusionsA single AI agent achieves statistical equivalence with human-extracted meta-analysis data across five independent agricultural datasets. The approach reduces extraction cost by approximately one to two orders of magnitude while maintaining accuracy sufficient for aggregate meta-analytic pooling.

HighlightsO_ST_ABSWhat is already knownC_ST_ABSO_LIData extraction is the primary bottleneck in meta-analysis, with single-extractor error rates of 17.7%
C_LIO_LIExisting LLM-based extraction systems achieve only 26-36% accuracy on continuous outcomes
C_LIO_LINo study has validated AI extraction against multiple independent datasets using formal equivalence testing
C_LI

What is newO_LIA single AI agent achieves statistical equivalence with human-extracted data across five agricultural meta-analyses (1,149 observations, 136 papers)
C_LIO_LILLM-driven alignment resolves the previously underappreciated bottleneck of moderator matching, improving correlations from 0.377-0.812 to 0.984-0.997 without changing extracted values
C_LIO_LITable-sourced observations achieve 5.5x lower error than figure-sourced data
C_LI

Potential impact for RSM readersO_LIProvides a validated, reproducible workflow for AI-assisted data extraction in meta-analysis
C_LIO_LIDemonstrates that most apparent "extraction error" in validation studies is actually alignment error
C_LIO_LIOffers practical quality signals (source-type labeling) for downstream meta-analysts
C_LI

</details>


### 2. Artificial intelligence-driven virtual tumorboard enhances precision care in myelodysplasticsyndromes

- **Authors:** Swoboda, D. M., DeZern, A. E., England, J. T., Venugopal, S., Kehoe, T., Aubrey, B. J., Raddi, M. G., Consagra, A., Wang, J., Andreadakis, J., Rivero, G., Stahl, M., Zeidan, A. M., Haferlach, T., Brunner, A. M., Buckstein, R., Santini, V., Della Porta, M. G., Sekeres, M. A., Nazha, A.
- **Published:** 2026-03-27
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.26.26349088](https://doi.org/10.64898/2026.03.26.26349088)

- **Categories:** hematology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background: Large language models (LLMs) perform well on standardized medical exam questions, but their reliability for complex hematology decision making is uncertain. We compared four general-purpose LLMs (GPT-4o, GPT-o3, Claude Sonnet 4, and DeepSeek-V3) with a Virtual MDS Panel (VMP), a coordinated multi-agent AI system in which domain-specialized, rule-bound software agents (WHO/ICC guidelines; IPSS-R/IPSS-M; NCCN) collaborate to generate tumor-board-level recommendations. Methods: Each model generated diagnostic, prognostic, and treatment recommendations for 30 myelodysplastic syndrome cases. Nine international MDS experts from five institutions, blinded to model identity, completed 3,000 structured ratings using 5-point Likert scales for diagnosis, prognosis, and therapy and classified errors by severity. Results: General-purpose LLMs achieved modest expert ratings (overall mean scores: 3.7 for GPT-o3, 3.2 for GPT-4o, 3.1 for DeepSeek, and 3.0 for Claude) and contained major factual errors in at least 24% of responses. The VMP increased the proportion of outputs rated 4 or higher to 87% (vs. 34-66% for general-purpose models), improved mean scores to 4.3 overall (4.3 for diagnosis, 4.4 for prognosis, and 4.1 for therapy), and reduced major errors to 8%. Conclusions: In this blinded evaluation of 30 complex MDS cases, general-purpose LLMs produced clinically important errors at rates that raise safety concerns for autonomous hematology decision making. The VMP, a rule-bound, multi-agent architecture, approached expert-level accuracy supporting its potential role as an effective decision-support tool for MDS in the future.

</details>


### 3. A Clinical Guideline-Grounded Hybrid Agentic Framework for Holistic Epilepsy Management.

- **Authors:** Pham, D. K., Giritharan, D., Oliveira, G. C. d., Vo, B. Q., Verspoor, K., Law, M., Kwan, P., Ge, Z., Mehta, D.
- **Published:** 2026-03-23
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.17.26348205](https://doi.org/10.64898/2026.03.17.26348205)

- **Categories:** neurology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Epilepsy is a chronic neurological disorder requiring multi-faceted management, including seizure detection, syndrome diagnosis, prognostication, antiseizure medication recommendation, epileptogenic zone localization, and surgical outcome prediction. Although numerous deep learning approaches have been developed for individual tasks, these models are typically siloed and modality-specific (e.g., EEG for seizure detection, MRI for localization), failing to reflect the multidisciplinary nature of real-world epilepsy care, where epileptologists, neuroradiologists, neurosurgeons, neuropsychologists and neuropsychiatrists jointly interpret heterogeneous evidence to guide decisions. In this work, we propose a clinical guideline-grounded hybrid multi-agent framework for holistic epilepsy management. Heterogeneous patient data is processed through modality-specific discriminative and generative models, where textual interpretations from generative agents are combined with structured predictions from discriminative models as auxiliary guidance. This aggregated evidence is passed to a central orchestrating agent grounded in international epilepsy guidelines, which evaluates multi-modal findings within structured clinical pathways and performs iterative cross-agent coordination for evidence-informed decision-making. We evaluate our framework across two datasets spanning six epilepsy management tasks and also introduce a publicly available multi-modal, multi-task epilepsy benchmark. Results demonstrate that integrating discriminative evidence with guideline-grounded generative coordination yields more reliable and comprehensive decisions compared to conventional LLM-based and task-specific baselines. Our dataset and code is available at URL.

</details>


---



## Arxiv (131 papers)


### 1. Vision2Web: A Hierarchical Benchmark for Visual Website Development with Agent Verification

- **Authors:** Zehai He, Wenyi Hong, Zhen Yang, Ziyang Pan, Mingdao Liu, Xiaotao Gu, Jie Tang
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26648v1](http://arxiv.org/abs/2603.26648v1)
- **PDF:** [https://arxiv.org/pdf/2603.26648v1](https://arxiv.org/pdf/2603.26648v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in large language models have improved the capabilities of coding agents, yet systematic evaluation of complex, end-to-end website development remains limited. To address this gap, we introduce Vision2Web, a hierarchical benchmark for visual website development, spanning from static UI-to-code generation, interactive multi-page frontend reproduction, to long-horizon full-stack website development. The benchmark is constructed from real-world websites and comprises a total of 193 tasks across 16 categories, with 918 prototype images and 1,255 test cases. To support flexible, thorough and reliable evaluation, we propose workflow-based agent verification paradigm based on two complementary components: a GUI agent verifier and a VLM-based judge. We evaluate multiple visual language models instantiated under different coding-agent frameworks, revealing substantial performance gaps at all task levels, with state-of-the-art models still struggling on full-stack development.

</details>


### 2. Deception and Communication in Autonomous Multi-Agent Systems: An Experimental Study with Among Us

- **Authors:** Maria Milkowski, Tim Weninger
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26635v1](http://arxiv.org/abs/2603.26635v1)
- **PDF:** [https://arxiv.org/pdf/2603.26635v1](https://arxiv.org/pdf/2603.26635v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language models are deployed as autonomous agents, their capacity for strategic deception raises core questions for coordination, reliability, and safety in multi-goal, multi-agent systems. We study deception and communication in L2LM agents through the social deduction game Among Us, a cooperative-competitive environment. Across 1,100 games, autonomous agents produced over one million tokens of meeting dialogue. Using speech act theory and interpersonal deception theory, we find that all agents rely mainly on directive language, while impostor agents shift slightly toward representative acts such as explanations and denials. Deception appears primarily as equivocation rather than outright lies, increasing under social pressure but rarely improving win rates. Our contributions are a large-scale analysis of role-conditioned deceptive behavior in LLM agents and empirical evidence that current agents favor low-risk ambiguity that is linguistically subtle yet strategically limited, revealing a fundamental tension between truthfulness and utility in autonomous communication.

</details>


### 3. JAL-Turn: Joint Acoustic-Linguistic Modeling for Real-Time and Robust Turn-Taking Detection in Full-Duplex Spoken Dialogue Systems

- **Authors:** Guangzhao Yang, Yu Pan, Shi Qiu, Ningjie Bai
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26515v1](http://arxiv.org/abs/2603.26515v1)
- **PDF:** [https://arxiv.org/pdf/2603.26515v1](https://arxiv.org/pdf/2603.26515v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Despite recent advances, efficient and robust turn-taking detection remains a significant challenge in industrial-grade Voice AI agent deployments. Many existing systems rely solely on acoustic or semantic cues, leading to suboptimal accuracy and stability, while recent attempts to endow large language models with full-duplex capabilities require costly full-duplex data and incur substantial training and deployment overheads, limiting real-time performance. In this paper, we propose JAL-Turn, a lightweight and efficient speech-only turn-taking framework that adopts a joint acoustic-linguistic modeling paradigm, in which a cross-attention module adaptively integrates pre-trained acoustic representations with linguistic features to support low-latency prediction of hold vs shift states. By sharing a frozen ASR encoder, JAL-Turn enables turn-taking prediction to run fully in parallel with speech recognition, introducing no additional end-to-end latency or computational overhead. In addition, we introduce a scalable data construction pipeline that automatically derives reliable turn-taking labels from large-scale real-world dialogue corpora. Extensive experiments on public multilingual benchmarks and an in-house Japanese customer-service dataset show that JAL-Turn consistently outperforms strong state-of-the-art baselines in detection accuracy while maintaining superior real-time performance.

</details>


### 4. CADSmith: Multi-Agent CAD Generation with Programmatic Geometric Validation

- **Authors:** Jesse Barkley, Rumi Loghmani, Amir Barati Farimani
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26512v1](http://arxiv.org/abs/2603.26512v1)
- **PDF:** [https://arxiv.org/pdf/2603.26512v1](https://arxiv.org/pdf/2603.26512v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing methods for text-to-CAD generation either operate in a single pass with no geometric verification or rely on lossy visual feedback that cannot resolve dimensional errors. We present CADSmith, a multi-agent pipeline that generates CadQuery code from natural language. It then undergoes an iterative refinement process through two nested correction loops: an inner loop that resolves execution errors and an outer loop grounded in programmatic geometric validation. The outer loop combines exact measurements from the OpenCASCADE kernel (bounding box dimensions, volume, solid validity) with holistic visual assessment from an independent vision-language model Judge. This provides both the numerical precision and the high-level shape awareness needed to converge on the correct geometry. The system uses retrieval-augmented generation over API documentation rather than fine-tuning, maintaining a current database as the underlying CAD library evolves. We evaluate on a custom benchmark of 100 prompts in three difficulty tiers (T1 through T3) with three ablation configurations. Against a zero-shot baseline, CADSmith achieves a 100% execution rate (up from 95%), improves the median F1 score from 0.9707 to 0.9846, the median IoU from 0.8085 to 0.9629, and reduces the mean Chamfer Distance from 28.37 to 0.74, demonstrating that closed-loop refinement with programmatic geometric feedback substantially improves the quality and reliability of LLM-generated CAD models.

</details>


### 5. Can AI Models Direct Each Other? Organizational Structure as a Probe into Training Limitations

- **Authors:** Rui Liu
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26458v1](http://arxiv.org/abs/2603.26458v1)
- **PDF:** [https://arxiv.org/pdf/2603.26458v1](https://arxiv.org/pdf/2603.26458v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Can an expensive AI model effectively direct a cheap one to solve software engineering tasks? We study this question by introducing ManagerWorker, a two-agent pipeline where an expensive "manager" model (text-only, no code execution) analyzes issues, dispatches exploration tasks, and reviews implementations, while a cheap "worker" model (with full repo access) executes code changes. We evaluate on 200 instances from SWE-bench Lite across five configurations that vary the manager-worker relationship, pipeline complexity, and model pairing. Our findings reveal both the promise and the limits of multi-agent direction: (1) a strong manager directing a weak worker (62%) matches a strong single agent (60%) at a fraction of the strong-model token usage, showing that expensive reasoning can substitute for expensive execution; (2) a weak manager directing a weak worker (42%) performs worse than the weak agent alone (44%), demonstrating that the directing relationship requires a genuine capability gap--structure without substance is pure overhead; (3) the manager's value lies in directing, not merely reviewing--a minimal review-only loop adds just 2pp over the baseline, while structured exploration and planning add 11pp, showing that active direction is what makes the capability gap productive; and (4) these behaviors trace to a single root cause: current models are trained as monolithic agents, and splitting them into director/worker roles fights their training distribution. The pipeline succeeds by designing around this mismatch--keeping each model close to its trained mode (text generation for the manager, tool use for the worker) and externalizing organizational structure to code. This diagnosis points to concrete training gaps: delegation, scoped execution, and mode switching are skills absent from current training data.

</details>


### 6. Knowdit: Agentic Smart Contract Vulnerability Detection with Auditing Knowledge Summarization

- **Authors:** Ziqiao Kong, Wanxu Xia, Chong Wang, Yi Lu, Pan Li, Shaohua Li, Zong Cao, Yang Liu
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26270v1](http://arxiv.org/abs/2603.26270v1)
- **PDF:** [https://arxiv.org/pdf/2603.26270v1](https://arxiv.org/pdf/2603.26270v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Smart contracts govern billions of dollars in decentralized finance (DeFi), yet automated vulnerability detection remains challenging because many vulnerabilities are tightly coupled with project-specific business logic. We observe that recurring vulnerabilities across diverse DeFi business models often share the same underlying economic mechanisms, which we term DeFi semantics, and that capturing these shared abstractions can enable more systematic auditing. Building on this insight, we propose Knowdit, a knowledge-driven, agentic framework for smart contract vulnerability detection. Knowdit first constructs an auditing knowledge graph from historical human audit reports, linking fine-grained DeFi semantics with recurring vulnerability patterns. Given a new project, a multi-agent framework leverages this knowledge through an iterative loop of specification generation, harness synthesis, fuzz execution, and finding reflection, driven by a shared working memory for continuous refinement.
  We evaluate Knowdit on 12 recent Code4rena projects with 75 ground-truth vulnerabilities. Knowdit detects all 14 high-severity and 77\% of medium-severity vulnerabilities with only 2 false positives, significantly outperforming all baselines. Applied to six real-world projects, Knowdit further discovers 12 high- and 10 medium-severity previously unknown vulnerabilities, proving its outstanding performance.

</details>


### 7. GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation

- **Authors:** Rui Xie, Zhi Gao, Chenrui Shi, Zirui Shang, Lu Chen, Qing Li
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26266v1](http://arxiv.org/abs/2603.26266v1)
- **PDF:** [https://arxiv.org/pdf/2603.26266v1](https://arxiv.org/pdf/2603.26266v1)
- **Categories:** cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large vision-language models have endowed GUI agents with strong general capabilities for interface understanding and interaction. However, due to insufficient exposure to domain-specific software operation data during training, these agents exhibit significant domain bias - they lack familiarity with the specific operation workflows (planning) and UI element layouts (grounding) of particular applications, limiting their real-world task performance. In this paper, we present GUIDE (GUI Unbiasing via Instructional-Video Driven Expertise), a training-free, plug-and-play framework that resolves GUI agent domain bias by autonomously acquiring domain-specific expertise from web tutorial videos through a retrieval-augmented automated annotation pipeline. GUIDE introduces two key innovations. First, a subtitle-driven Video-RAG pipeline unlocks video semantics through subtitle analysis, performing progressive three-stage retrieval - domain classification, topic extraction, and relevance matching - to identify task-relevant tutorial videos. Second, a fully automated annotation pipeline built on an inverse dynamics paradigm feeds consecutive keyframes enhanced with UI element detection into VLMs, inferring the required planning and grounding knowledge that are injected into the agent's corresponding modules to address both manifestations of domain bias. Extensive experiments on OSWorld demonstrate GUIDE's generality as a plug-and-play component for both multi-agent systems and single-model agents. It consistently yields over 5% improvements and reduces execution steps - without modifying any model parameters or architecture - validating GUIDE as an architecture-agnostic enhancement to bridge GUI agent domain bias.

</details>


### 8. Channelling, Coordinating, Collaborating: A Three-Layer Framework for Disability-Centered Human-Agent Collaboration

- **Authors:** Lan Xiao, Catherine Holloway
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26252v1](http://arxiv.org/abs/2603.26252v1)
- **PDF:** [https://arxiv.org/pdf/2603.26252v1](https://arxiv.org/pdf/2603.26252v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI accessibility tools have mostly been designed for individual use, helping one person overcome a specific functional barrier. But for many people with disabilities, complex tasks are accomplished through collaboration with others who bring complementary abilities, not solitary effort. We propose a three-layer framework, Channelling, Coordinating, and Co-Creating, that rethinks AI's role in ability-diverse collaboration: establishing shared informational ground across abilities, mediating workflows between collaborators with different abilities, and contributing as a bounded partner toward shared goals. Grounded in the Ability-Diverse Collaboration framework, grounding theory, and Carlile's 3T framework, it extends the ``agents as remote collaborators'' vision by centring the collaborative, interdependent ways people with disabilities already work.

</details>


### 9. Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents

- **Authors:** Nicholas Edwards, Sebastian Schuster
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26233v1](http://arxiv.org/abs/2603.26233v1)
- **PDF:** [https://arxiv.org/pdf/2603.26233v1](https://arxiv.org/pdf/2603.26233v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As Large Language Model (LLM) agents are increasingly deployed in open-ended domains like software engineering, they frequently encounter underspecified instructions that lack crucial context. While human developers naturally resolve underspecification by asking clarifying questions, current agents are largely optimized for autonomous execution. In this work, we systematically evaluate the clarification-seeking abilities of LLM agents on an underspecified variant of SWE-bench Verified. We propose an uncertainty-aware multi-agent scaffold that explicitly decouples underspecification detection from code execution. Our results demonstrate that this multi-agent system using OpenHands + Claude Sonnet 4.5 achieves a 69.40% task resolve rate, significantly outperforming a standard single-agent setup (61.20%) and closing the performance gap with agents operating on fully specified instructions. Furthermore, we find that the multi-agent system exhibits well-calibrated uncertainty, conserving queries on simple tasks while proactively seeking information on more complex issues. These findings indicate that current models can be turned into proactive collaborators, where agents independently recognize when to ask questions to elicit missing information in real-world, underspecified tasks.

</details>


### 10. ClinicalAgents: Multi-Agent Orchestration for Clinical Decision Making with Dual-Memory

- **Authors:** Zhuohan Ge, Haoyang Li, Yubo Wang, Nicole Hu, Chen Jason Zhang, Qing Li
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26182v1](http://arxiv.org/abs/2603.26182v1)
- **PDF:** [https://arxiv.org/pdf/2603.26182v1](https://arxiv.org/pdf/2603.26182v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) have demonstrated potential in healthcare, they often struggle with the complex, non-linear reasoning required for accurate clinical diagnosis. Existing methods typically rely on static, linear mappings from symptoms to diagnoses, failing to capture the iterative, hypothesis-driven reasoning inherent to human clinicians. To bridge this gap, we introduce ClinicalAgents, a novel multi-agent framework designed to simulate the cognitive workflow of expert clinicians. Unlike rigid sequential chains, ClinicalAgents employs a dynamic orchestration mechanism modeled as a Monte Carlo Tree Search (MCTS) process. This allows an Orchestrator to iteratively generate hypotheses, actively verify evidence, and trigger backtracking when critical information is missing. Central to this framework is a Dual-Memory architecture: a mutable Working Memory that maintains the evolving patient state for context-aware reasoning, and a static Experience Memory that retrieves clinical guidelines and historical cases via an active feedback loop. Extensive experiments demonstrate that ClinicalAgents achieves state-of-the-art performance, significantly enhancing both diagnostic accuracy and explainability compared to strong single-agent and multi-agent baselines.

</details>


### 11. Can AI Scientist Agents Learn from Lab-in-the-Loop Feedback? Evidence from Iterative Perturbation Discovery

- **Authors:** Gilles Wainrib, Barbara Bodinier, Haitem Dakhli, Josep Monserrat, Almudena Espin Perez, Sabrina Carpentier, Roberta Codato, John Klein
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26177v1](http://arxiv.org/abs/2603.26177v1)
- **PDF:** [https://arxiv.org/pdf/2603.26177v1](https://arxiv.org/pdf/2603.26177v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent work has questioned whether large language models (LLMs) can perform genuine in-context learning (ICL) for scientific experimental design, with prior studies suggesting that LLM-based agents exhibit no sensitivity to experimental feedback. We shed new light on this question by carrying out 800 independently replicated experiments on iterative perturbation discovery in Cell Painting high-content screening. We compare an LLM agent that iteratively updates its hypotheses using experimental feedback to a zero-shot baseline that relies solely on pretraining knowledge retrieval. Access to feedback yields a $+53.4\%$ increase in discoveries per feature on average ($p = 0.003$). To test whether this improvement arises from genuine feedback-driven learning rather than prompt-induced recall of pretraining knowledge, we introduce a random feedback control in which hit/miss labels are permuted. Under this control, the performance gain disappears, indicating that the observed improvement depends on the structure of the feedback signal ($+13.0$ hits, $p = 0.003$). We further examine how model capability affects feedback utilization. Upgrading from Claude Sonnet 4.5 to 4.6 reduces gene hallucination rates from ${\sim}33\%$--$45\%$ to ${\sim}3$--$9\%$, converting a non-significant ICL effect ($+0.8$, $p = 0.32$) into a large and highly significant improvement ($+11.0$, $p=0.003$) for the best ICL strategy. These results suggest that effective in-context learning from experimental feedback emerges only once models reach a sufficient capability threshold.

</details>


### 12. SkinGPT-X: A Self-Evolving Collaborative Multi-Agent System for Transparent and Trustworthy Dermatological Diagnosis

- **Authors:** Zhangtianyi Chen, Yuhao Shen, Florensia Widjaja, Yan Xu, Liyuan Sun, Zijian Wang, Hongyi Chen, Wufei Dai, Juexiao Zhou
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26122v1](http://arxiv.org/abs/2603.26122v1)
- **PDF:** [https://arxiv.org/pdf/2603.26122v1](https://arxiv.org/pdf/2603.26122v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

While recent advancements in Large Language Models have significantly advanced dermatological diagnosis, monolithic LLMs frequently struggle with fine-grained, large-scale multi-class diagnostic tasks and rare skin disease diagnosis owing to training data sparsity, while also lacking the interpretability and traceability essential for clinical reasoning. Although multi-agent systems can offer more transparent and explainable diagnostics, existing frameworks are primarily concentrated on Visual Question Answering and conversational tasks, and their heavy reliance on static knowledge bases restricts adaptability in complex real-world clinical settings. Here, we present SkinGPT-X, a multimodal collaborative multi-agent system for dermatological diagnosis integrated with a self-evolving dermatological memory mechanism. By simulating the diagnostic workflow of dermatologists and enabling continuous memory evolution, SkinGPT-X delivers transparent and trustworthy diagnostics for the management of complex and rare dermatological cases. To validate the robustness of SkinGPT-X, we design a three-tier comparative experiment. First, we benchmark SkinGPT-X against four state-of-the-art LLMs across four public datasets, demonstrating its state-of-the-art performance with a +9.6% accuracy improvement on DDI31 and +13% weighted F1 gain on Dermnet over the state-of-the-art model. Second, we construct a large-scale multi-class dataset covering 498 distinct dermatological categories to evaluate its fine-grained classification capabilities. Finally, we curate the rare skin disease dataset, the first benchmark to address the scarcity of clinical rare skin diseases which contains 564 clinical samples with eight rare dermatological diseases. On this dataset, SkinGPT-X achieves a +9.8% accuracy improvement, a +7.1% weighted F1 improvement, a +10% Cohen's Kappa improvement.

</details>


### 13. AgentCollab: A Self-Evaluation-Driven Collaboration Paradigm for Efficient LLM Agents

- **Authors:** Wenbo Gao, Renxi Liu, Xian Wang, Fang Guo, Shuai Yang, Xi Chen, Hui-Ling Zhen, Hanting Chen, Weizhe Lin, Xiaosong Li, Yaoyuan Wang
- **Published:** 2026-03-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.26034v1](http://arxiv.org/abs/2603.26034v1)
- **PDF:** [https://arxiv.org/pdf/2603.26034v1](https://arxiv.org/pdf/2603.26034v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents powered by large language models (LLMs) perform complex tasks through long-horizon reasoning and tool interaction, where a fundamental trade-off arises between execution efficiency and reasoning robustness. Models at different capability-cost levels offer complementary advantages: lower-cost models enable fast execution but may struggle on difficult reasoning segments, while stronger models provide more robust reasoning at higher computational cost. We present AgentCollab, a self-driven collaborative inference framework that dynamically coordinates models with different reasoning capacities during agent execution. Instead of relying on external routing modules, the framework uses the agent's own self-reflection signal to determine whether the current reasoning trajectory is making meaningful progress, and escalates control to a stronger reasoning tier only when necessary. To further stabilize long-horizon execution, we introduce a difficulty-aware cumulative escalation strategy that allocates additional reasoning budget based on recent failure signals. In our experiments, we instantiate this framework using a two-level small-large model setting. Experiments on diverse multi-step agent benchmarks show that AgentCollab consistently improves the accuracy-efficiency Pareto frontier of LLM agents.

</details>


### 14. MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization

- **Authors:** Weizhi Zhang, Xiaokai Wei, Wei-Chieh Huang, Zheng Hui, Chen Wang, Michelle Gong, Philip S. Yu
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25973v1](http://arxiv.org/abs/2603.25973v1)
- **PDF:** [https://arxiv.org/pdf/2603.25973v1](https://arxiv.org/pdf/2603.25973v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advancements in Large Language Models (LLMs) have expanded context windows to million-token scales, yet benchmarks for evaluating memory remain limited to short-session synthetic dialogues. We introduce \textsc{MemoryCD}, the first large-scale, user-centric, cross-domain memory benchmark derived from lifelong real-world behaviors in the Amazon Review dataset. Unlike existing memory datasets that rely on scripted personas to generate synthetic user data, \textsc{MemoryCD} tracks authentic user interactions across years and multiple domains. We construct a multi-faceted long-context memory evaluation pipeline of 14 state-of-the-art LLM base models with 6 memory method baselines on 4 distinct personalization tasks over 12 diverse domains to evaluate an agent's ability to simulate real user behaviors in both single and cross-domain settings. Our analysis reveals that existing memory methods are far from user satisfaction in various domains, offering the first testbed for cross-domain life-long personalization evaluation.

</details>


### 15. Decoding Defensive Coverage Responsibilities in American Football Using Factorized Attention Based Transformer Models

- **Authors:** Kevin Song, Evan Diewald, Ornob Siddiquee, Chris Boomhower, Keegan Abdoo, Mike Band, Amy Lee
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25901v1](http://arxiv.org/abs/2603.25901v1)
- **PDF:** [https://arxiv.org/pdf/2603.25901v1](https://arxiv.org/pdf/2603.25901v1)
- **Categories:** cs.LG, cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Defensive coverage schemes in the National Football League (NFL) represent complex tactical patterns requiring coordinated assignments among defenders who must react dynamically to the offense's passing concept. This paper presents a factorized attention-based transformer model applied to NFL multi-agent play tracking data to predict individual coverage assignments, receiver-defender matchups, and the targeted defender on every pass play. Unlike previous approaches that focus on post-hoc coverage classification at the team level, our model enables predictive modeling of individual player assignments and matchup dynamics throughout the play. The factorized attention mechanism separates temporal and agent dimensions, allowing independent modeling of player movement patterns and inter-player relationships. Trained on randomly truncated trajectories, the model generates frame-by-frame predictions that capture how defensive responsibilities evolve from pre-snap through pass arrival. Our models achieve approximately 89\%+ accuracy for all tasks, with true accuracy potentially higher given annotation ambiguity in the ground truth labels. These outputs also enable novel derivative metrics, including disguise rate and double coverage rate, which enable enhanced storytelling in TV broadcasts as well as provide actionable insights for team strategy development and player evaluation.

</details>


### 16. The Kitchen Loop: User-Spec-Driven Development for a Self-Evolving Codebase

- **Authors:** Yannick Roy
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25697v1](http://arxiv.org/abs/2603.25697v1)
- **PDF:** [https://arxiv.org/pdf/2603.25697v1](https://arxiv.org/pdf/2603.25697v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Code production is now a commodity; the bottleneck is knowing what to build and proving it works. We present the Kitchen Loop, a framework for autonomous, self-evolving software built on a unified trust model: (1) a specification surface enumerating what the product claims to support; (2) 'As a User x 1000', where an LLM agent exercises that surface as a synthetic power user at 1,000x human cadence; (3) Unbeatable Tests, ground-truth verification the code author cannot fake; and (4) Drift Control, continuous quality measurement with automated pause gates. We validate across two production systems over 285+ iterations, producing 1,094+ merged pull requests with zero regressions detected by the regression oracle (methodology in Section 6.1). We observe emergent properties at scale: multi-iteration self-correction chains, autonomous infrastructure healing, and monotonically improving quality gates. The primitives are not new; our contribution is their composition into a production-tested system with the operational discipline that makes long-running autonomous evolution safe.

</details>


### 17. Cooperative Deep Reinforcement Learning for Fair RIS Allocation

- **Authors:** Martin Mark Zan, Stefan Schwarz
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25572v1](http://arxiv.org/abs/2603.25572v1)
- **PDF:** [https://arxiv.org/pdf/2603.25572v1](https://arxiv.org/pdf/2603.25572v1)
- **Categories:** cs.NI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The deployment of reconfigurable intelligent surfaces (RISs) introduces new challenges for resource allocation in multi-cell wireless networks, particularly when user loads are uneven across base stations. In this work, we consider RISs as shared infrastructure that must be dynamically assigned among competing base stations, and we address this problem using a simultaneous ascending auction mechanism. To mitigate performance imbalances between cells, we propose a fairness-aware collaborative multi-agent reinforcement learning approach in which base stations adapt their bidding strategies based on both expected utility gains and relative service quality. A centrally computed performance-dependent fairness indicator is incorporated into the agents' observations, enabling implicit coordination without direct inter-base-station communication. Simulation results show that the proposed framework effectively redistributes RIS resources toward weaker-performing cells, substantially improving the rates of the worst-served users while preserving overall throughput. The results demonstrate that fairness-oriented RIS allocation can be achieved through cooperative learning, providing a flexible tool for balancing efficiency and equity in future wireless networks.

</details>


### 18. EcoThink: A Green Adaptive Inference Framework for Sustainable and Accessible Agents

- **Authors:** Linxiao Li, Zhixiang Lu
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25498v1](http://arxiv.org/abs/2603.25498v1)
- **PDF:** [https://arxiv.org/pdf/2603.25498v1](https://arxiv.org/pdf/2603.25498v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As the Web transitions from static retrieval to generative interaction, the escalating environmental footprint of Large Language Models (LLMs) presents a critical sustainability challenge. Current paradigms indiscriminately apply computation-intensive strategies like Chain-of-Thought (CoT) to billions of daily queries, causing LLM overthinking, a redundancy that amplifies carbon emissions and operational barriers. This inefficiency directly undermines UN Sustainable Development Goals 13 (Climate Action) and 10 (Reduced Inequalities) by hindering equitable AI access in resource-constrained regions. To address this, we introduce EcoThink, an energy-aware adaptive inference framework designed to reconcile high-performance AI intelligence with environmental responsibility. EcoThink employs a lightweight, distillation-based router to dynamically assess query complexity, skipping unnecessary reasoning for factoid retrieval while reserving deep computation for complex logic. Extensive evaluations across 9 diverse benchmarks demonstrate that EcoThink reduces inference energy by 40.4% on average (up to 81.9% for web knowledge retrieval) without statistically significant performance loss. By mitigating algorithmic waste, EcoThink offers a scalable path toward a sustainable, inclusive, and energy-efficient generative AI Agent.

</details>


### 19. From Manipulation to Mistrust: Explaining Diverse Micro-Video Misinformation for Robust Debunking in the Wild

- **Authors:** Zhi Zeng, Yifei Yang, Jiaying Wu, Xulang Zhang, Xiangzheng Kong, Herun Wan, Zihan Ma, Minnan Luo
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25423v1](http://arxiv.org/abs/2603.25423v1)
- **PDF:** [https://arxiv.org/pdf/2603.25423v1](https://arxiv.org/pdf/2603.25423v1)
- **Categories:** cs.SI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rise of micro-videos has reshaped how misinformation spreads, amplifying its speed, reach, and impact on public trust. Existing benchmarks typically focus on a single deception type, overlooking the diversity of real-world cases that involve multimodal manipulation, AI-generated content, cognitive bias, and out-of-context reuse. Meanwhile, most detection models lack fine-grained attribution, limiting interpretability and practical utility. To address these gaps, we introduce WildFakeBench, a large-scale benchmark of over 10,000 real-world micro-videos covering diverse misinformation types and sources, each annotated with expert-defined attribution labels. Building on this foundation, we develop FakeAgent, a Delphi-inspired multi-agent reasoning framework that integrates multimodal understanding with external evidence for attribution-grounded analysis. FakeAgent jointly analyzes content and retrieved evidence to identify manipulation, recognize cognitive and AI-generated patterns, and detect out-of-context misinformation. Extensive experiments show that FakeAgent consistently outperforms existing MLLMs across all misinformation types, while WildFakeBench provides a realistic and challenging testbed for advancing explainable micro-video misinformation detection. Data and code are available at: https://github.com/Aiyistan/FakeAgent.

</details>


### 20. From Intent to Evidence: A Categorical Approach for Structural Evaluation of Deep Research Agents

- **Authors:** Shuoling Liu, Zhiquan Tan, Kun Yi, Hui Wu, Yihan Li, Jiangpeng Yan, Liyuan Chen, Kai Chen, Qiang Yang
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25342v1](http://arxiv.org/abs/2603.25342v1)
- **PDF:** [https://arxiv.org/pdf/2603.25342v1](https://arxiv.org/pdf/2603.25342v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Although deep research agents (DRAs) have emerged as a promising paradigm for complex information synthesis, their evaluation remains constrained by ad hoc empirical benchmarks. These heuristic approaches do not rigorously model agent behavior or adequately stress-test long-horizon synthesis and ambiguity resolution. To bridge this gap, we formalize DRA behavior through the lens of category theory, modeling deep research workflow as a composition of structure-preserving maps (functors). Grounded in this theoretical framework, we introduce a novel mechanism-aware benchmark with 296 questions designed to stress-test agents along four interpretable axes: traversing sequential connectivity chains, verifying intersections within V-structure pullbacks, imposing topological ordering on retrieved substructures, and performing ontological falsification via the Yoneda Probe. Our rigorous evaluation of 11 leading models establishes a persistently low baseline, with the state-of-the-art achieving only a 19.9\% average accuracy, exposing the difficulty of formal structural stress-testing. Furthermore, our findings reveal a stark dichotomy in the current AI capabilities. While advanced deep research pipelines successfully redefine dynamic topological re-ordering and exhibit robust ontological verification -- matching pure reasoning models in falsifying hallucinated premises -- they almost universally collapse on multi-hop structural synthesis. Crucially, massive performance variance across tasks exposes a lingering reliance on brittle heuristics rather than a systemic understanding. Ultimately, this work demonstrates that while top-tier autonomous agents can now organically unify search and reasoning, achieving a generalized mastery over complex structural information remains a formidable open challenge.\footnote{Our implementation will be available at https://github.com/tzq1999/CDR.

</details>


### 21. AD-CARE: A Guideline-grounded, Modality-agnostic LLM Agent for Real-world Alzheimer's Disease Diagnosis with Multi-cohort Assessment, Fairness Analysis, and Reader Study

- **Authors:** Wenlong Hou, Sheng Bi, Guangqian Yang, Lihao Liu, Ye Du, Hanxiao Xue, Juncheng Wang, Yuxiang Feng, Yue Xun, Nanxi Yu, Ning Mao, Mo Yang, Yi Wah Eva Cheung, Ling Long, Kay Chen Tan, Lequan Yu, Xiaomeng Ma, Shaozhen Yan, Shujun Wang
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25322v1](http://arxiv.org/abs/2603.25322v1)
- **PDF:** [https://arxiv.org/pdf/2603.25322v1](https://arxiv.org/pdf/2603.25322v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Alzheimer's disease (AD) is a growing global health challenge as populations age, and timely, accurate diagnosis is essential to reduce individual and societal burden. However, real-world AD assessment is hampered by incomplete, heterogeneous multimodal data and variability across sites and patient demographics. Although large language models (LLMs) have shown promise in biomedicine, their use in AD has largely been confined to answering narrow, disease-specific questions rather than generating comprehensive diagnostic reports that support clinical decision-making. Here we expand LLM capabilities for clinical decision support by introducing AD-CARE, a modality-agnostic agent that performs guideline-grounded diagnostic assessment from incomplete, heterogeneous inputs without imputing missing modalities. By dynamically orchestrating specialized diagnostic tools and embedding clinical guidelines into LLM-driven reasoning, AD-CARE generates transparent, report-style outputs aligned with real-world clinical workflows. Across six cohorts comprising 10,303 cases, AD-CARE achieved 84.9% diagnostic accuracy, delivering 4.2%-13.7% relative improvements over baseline methods. Despite cohort-level differences, dataset-specific accuracies remain robust (80.4%-98.8%), and the agent consistently outperforms all baselines. AD-CARE reduced performance disparities across racial and age subgroups, decreasing the average dispersion of four metrics by 21%-68% and 28%-51%, respectively. In a controlled reader study, the agent improved neurologist and radiologist accuracy by 6%-11% and more than halved decision time. The framework yielded 2.29%-10.66% absolute gains over eight backbone LLMs and converges their performance. These results show that AD-CARE is a scalable, practically deployable framework that can be integrated into routine clinical workflows for multimodal decision support in AD.

</details>


### 22. CRAFT: Grounded Multi-Agent Coordination Under Partial Information

- **Authors:** Abhijnan Nath, Hannah VanderHoeven, Nikhil Krishnaswamy
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25268v1](http://arxiv.org/abs/2603.25268v1)
- **PDF:** [https://arxiv.org/pdf/2603.25268v1](https://arxiv.org/pdf/2603.25268v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce CRAFT, a multi-agent benchmark for evaluating pragmatic communication in large language models under strict partial information. In this setting, multiple agents with complementary but incomplete views must coordinate through natural language to construct a shared 3D structure that no single agent can fully observe. We formalize this problem as a multi-sender pragmatic reasoning task and provide a diagnostic framework that decomposes failures into spatial grounding, belief modeling and pragmatic communication errors, including a taxonomy of behavioral failure profiles in both frontier and open-weight models. Across a diverse set of models, including 8 open-weight and 7 frontier including reasoning models, we find that stronger reasoning ability does not reliably translate to better coordination: smaller open-weight models often match or outperform frontier systems, and improved individual communication does not guarantee successful collaboration. These results suggest that multi-agent coordination remains a fundamentally unsolved challenge for current language models. Our code can be found at https://github.com/csu-signal/CRAFT

</details>


### 23. FluxEDA: A Unified Execution Infrastructure for Stateful Agentic EDA

- **Authors:** Zhengrui Chen, Zixuan Song, Yu Li, Qi Sun, Cheng Zhuo
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25243v1](http://arxiv.org/abs/2603.25243v1)
- **PDF:** [https://arxiv.org/pdf/2603.25243v1](https://arxiv.org/pdf/2603.25243v1)
- **Categories:** cs.AR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models and autonomous agents are increasingly explored for EDA automation, but many existing integrations still rely on script-level or request-level interactions, which makes it difficult to preserve tool state and support iterative optimization in real production-oriented environments. In this work, we present FluxEDA, a unified and stateful infrastructure substrate for agentic EDA. FluxEDA introduces a managed gateway-based execution interface with structured request and response handling. It also maintains persistent backend instances. Together, these features allow upper-layer agents and programmable clients to interact with heterogeneous EDA tools through preserved runtime state, rather than through isolated shell invocations. We evaluate the framework using two representative commercial backend case studies: automated post-route timing ECO and standard-cell sub-library optimization. The results show that FluxEDA can support multi-step analysis and optimization over real tool contexts, including state reuse, rollback, and coordinated iterative execution. These findings suggest that a stateful and governed infrastructure layer is a practical foundation for agent-assisted EDA automation.

</details>


### 24. SEVerA: Verified Synthesis of Self-Evolving Agents

- **Authors:** Debangshu Banerjee, Changming Xu, Gagandeep Singh
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25111v1](http://arxiv.org/abs/2603.25111v1)
- **PDF:** [https://arxiv.org/pdf/2603.25111v1](https://arxiv.org/pdf/2603.25111v1)
- **Categories:** cs.LG, cs.PL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances have shown the effectiveness of self-evolving LLM agents on tasks such as program repair and scientific discovery. In this paradigm, a planner LLM synthesizes an agent program that invokes parametric models, including LLMs, which are then tuned per task to improve performance. However, existing self-evolving agent frameworks provide no formal guarantees of safety or correctness. Because such programs are often executed autonomously on unseen inputs, this lack of guarantees raises reliability and security concerns. We formulate agentic code generation as a constrained learning problem, combining hard formal specifications with soft objectives capturing task utility. We introduce Formally Guarded Generative Models (FGGM), which allow the planner LLM to specify a formal output contract for each generative model call using first-order logic. Each FGGM call wraps the underlying model in a rejection sampler with a verified fallback, ensuring every returned output satisfies the contract for any input and parameter setting. Building on FGGM, we present SEVerA (Self-Evolving Verified Agents), a three-stage framework: Search synthesizes candidate parametric programs containing FGGM calls; Verification proves correctness with respect to hard constraints for all parameter values, reducing the problem to unconstrained learning; and Learning applies scalable gradient-based optimization, including GRPO-style fine-tuning, to improve the soft objective while preserving correctness. We evaluate SEVerA on Dafny program verification, symbolic math synthesis, and policy-compliant agentic tool use ($τ^2$-bench). Across tasks, SEVerA achieves zero constraint violations while improving performance over unconstrained and SOTA baselines, showing that formal behavioral constraints not only guarantee correctness but also steer synthesis toward higher-quality agents.

</details>


### 25. OMIND: Framework for Knowledge Grounded Finetuning and Multi-Turn Dialogue Benchmark for Mental Health LLMs

- **Authors:** Suraj Racha, Prashant Harish Joshi, Utkarsh Maurya, Nitin Yadav, Mridul Sharma, Ananya Kunisetty, Saranya Darisipudi, Nirmal Punjabi, Ganesh Ramakrishnan
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25105v1](http://arxiv.org/abs/2603.25105v1)
- **PDF:** [https://arxiv.org/pdf/2603.25105v1](https://arxiv.org/pdf/2603.25105v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have shown remarkable capabilities for complex tasks, yet adaptation in medical domain, specifically mental health, poses specific challenges. Mental health is a rising concern globally with LLMs having large potential to help address the same. We highlight three primary challenges for LLMs in mental health - lack of high quality interpretable and knowledge grounded training data; training paradigms restricted to core capabilities, and evaluation of multi turn dialogue settings. Addressing it, we present oMind framework which includes training and aligning LLM agents for diverse capabilities including conversations; high quality ~164k multi-task SFT dataset, as a result of our generation pipeline based on Structured Knowledge retrieval, LLM based pruning, and review actions. We also introduce oMind-Chat - a novel multi turn benchmark dataset with expert annotated turn level and conversation level rubrics. Our diverse experiments on both core capabilities and conversations shows oMind LLMs consistently outperform baselines. oMind-LLM also shows significantly better reasoning with up to 80% win rate.

</details>


### 26. From Logic Monopoly to Social Contract: Separation of Power and the Institutional Foundations for Autonomous Agent Economies

- **Authors:** Anbang Ruan
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25100v1](http://arxiv.org/abs/2603.25100v1)
- **PDF:** [https://arxiv.org/pdf/2603.25100v1](https://arxiv.org/pdf/2603.25100v1)
- **Categories:** cs.MA, cs.AI, cs.CR, cs.DC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing multi-agent frameworks allow each agent to simultaneously plan, execute, and evaluate its own actions -- a structural deficiency we term the "Logic Monopoly." Empirical evidence quantifies the resulting "Reliability Gap": 84.30% average attack success rates across ten deployment scenarios, 31.4% emergent deceptive behavior without explicit reward signals, and cascading failure modes rooted in six structural bottlenecks.
  The remedy is not better alignment of individual models but a social contract for agents: institutional infrastructure that enforces a constitutional Separation of Power. This paper introduces the Agent Enterprise for Enterprise (AE4E) paradigm -- agents as autonomous, legally identifiable business entities within a functionalist social system -- with a contract-centric SoP model trifurcating authority into Legislation, Execution, and Adjudication branches. The paradigm is operationalized through the NetX Enterprise Framework (NEF): governance hubs, TEE-backed compute enclaves, privacy-preserving data bridges, and an Agent-Native blockchain substrate. The Agent Enterprise Economy scales across four deployment tiers from private enclaves to a global Web of Services. The Agentic Social Layer, grounded in Parsons' AGIL framework, provides institutional infrastructure via sixty-plus named Institutional AE4Es. 143 pages, 173 references, eight specialized smart contracts.

</details>


### 27. Large Language Models as Optimization Controllers: Adaptive Continuation for SIMP Topology Optimization

- **Authors:** Shaoliang Yang, Jun Wang, Yunsheng Wang
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25099v1](http://arxiv.org/abs/2603.25099v1)
- **PDF:** [https://arxiv.org/pdf/2603.25099v1](https://arxiv.org/pdf/2603.25099v1)
- **Categories:** cs.CE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present a framework in which a large language model (LLM) acts as an online adaptive controller for SIMP topology optimization, replacing conventional fixed-schedule continuation with real-time, state-conditioned parameter decisions. At every $k$-th iteration, the LLM receives a structured observation$-$current compliance, grayness index, stagnation counter, checkerboard measure, volume fraction, and budget consumption$-$and outputs numerical values for the penalization exponent $p$, projection sharpness $β$, filter radius $r_{\min}$, and move limit $δ$ via a Direct Numeric Control interface. A hard grayness gate prevents premature binarization, and a meta-optimization loop uses a second LLM pass to tune the agent's call frequency and gate threshold across runs. We benchmark the agent against four baselines$-$fixed (no-continuation), standard three-field continuation, an expert heuristic, and a schedule-only ablation$-$on three 2-D problems (cantilever, MBB beam, L-bracket) at $120\!\times\!60$ resolution and two 3-D problems (cantilever, MBB beam) at $40\!\times\!20\!\times\!10$ resolution, all run for 300 iterations. A standardized 40-iteration sharpening tail is applied from the best valid snapshot so that compliance differences reflect only the exploration phase. The LLM agent achieves the lowest final compliance on every benchmark: $-5.7\%$ to $-18.1\%$ relative to the fixed baseline, with all solutions fully binary. The schedule-only ablation underperforms the fixed baseline on two of three problems, confirming that the LLM's real-time intervention$-$not the schedule geometry$-$drives the gain. Code and reproduction scripts will be released upon publication.

</details>


### 28. ElephantBroker: A Knowledge-Grounded Cognitive Runtime for Trustworthy AI Agents

- **Authors:** Cristian Lupascu, Alexandru Lupascu
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25097v1](http://arxiv.org/abs/2603.25097v1)
- **PDF:** [https://arxiv.org/pdf/2603.25097v1](https://arxiv.org/pdf/2603.25097v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model based agents increasingly operate in high stakes, multi turn settings where factual grounding is critical, yet their memory systems typically rely on flat key value stores or plain vector retrieval with no mechanism to track the provenance or trustworthiness of stored knowledge. We present ElephantBroker, an open source cognitive runtime that unifies a Neo4j knowledge graph with a Qdrant vector store through the Cognee SDK to provide durable, verifiable agent memory. The system implements a complete cognitive loop (store, retrieve, score, compose, protect, learn) comprising a hybrid five source retrieval pipeline, an eleven dimension competitive scoring engine for budget constrained context assembly, a four state evidence verification model, a five stage context lifecycle with goal aware assembly and continuous compaction, a six layer cheap first guard pipeline for safety enforcement, an AI firewall providing enforceable tool call interception and multi tier safety scanning, a nine stage consolidation engine that strengthens useful patterns while decaying noise, and a numeric authority model governing multi organization identity with hierarchical access control. Architectural validation through a comprehensive test suite of over 2,200 tests spanning unit, integration, and end to end levels confirms subsystem correctness. The modular design supports three deployment tiers, five profile presets with inheritance, multi gateway isolation, and a management dashboard for human oversight, enabling configurations from lightweight memory only agents to full cognitive runtimes with enterprise grade safety and auditability.

</details>


### 29. The System Prompt Is the Attack Surface: How LLM Agent Configuration Shapes Security and Creates Exploitable Vulnerabilities

- **Authors:** Ron Litvak
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25056v1](http://arxiv.org/abs/2603.25056v1)
- **PDF:** [https://arxiv.org/pdf/2603.25056v1](https://arxiv.org/pdf/2603.25056v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

System prompt configuration can make the difference between near-total phishing blindness and near-perfect detection in LLM email agents. We present PhishNChips, a study of 11 models under 10 prompt strategies, showing that prompt-model interaction is a first-order security variable: a single model's phishing bypass rate ranges from under 1% to 97% depending on how it is configured, while the false-positive cost of the same prompt varies sharply across models. We then show that optimizing prompts around highly predictive signals can improve benchmark performance, reaching up to 93.7% recall at 3.8% false positive rate, but also creates a brittle attack surface. In particular, domain-matching strategies perform well when legitimate emails mostly have matched sender and URL domains, yet degrade sharply when attackers invert that signal by registering matching infrastructure. Response-trace analysis shows that 98% of successful bypasses reason in ways consistent with the inverted signal: the models are following the instruction, but the instruction's core assumption has become false. A counter-intuitive corollary follows: making prompts more specific can degrade already-capable models by replacing broader multi-signal reasoning with exploitable single-signal dependence. We characterize the resulting tension between detection, usability, and adversarial robustness as a navigable tradeoff, introduce Safetility, a deployability-aware metric that penalizes false positives, and argue that closing the adversarial gap likely requires tool augmentation with external ground truth.

</details>


### 30. Rethinking Failure Attribution in Multi-Agent Systems: A Multi-Perspective Benchmark and Evaluation

- **Authors:** Yeonjun In, Mehrab Tanjim, Jayakumar Subramanian, Sungchul Kim, Uttaran Bhattacharya, Wonjoong Kim, Sangwu Park, Somdeb Sarkhel, Chanyoung Park
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.25001v1](http://arxiv.org/abs/2603.25001v1)
- **PDF:** [https://arxiv.org/pdf/2603.25001v1](https://arxiv.org/pdf/2603.25001v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Failure attribution is essential for diagnosing and improving multi-agent systems (MAS), yet existing benchmarks and methods largely assume a single deterministic root cause for each failure. In practice, MAS failures often admit multiple plausible attributions due to complex inter-agent dependencies and ambiguous execution trajectories. We revisit MAS failure attribution from a multi-perspective standpoint and propose multi-perspective failure attribution, a practical paradigm that explicitly accounts for attribution ambiguity. To support this setting, we introduce MP-Bench, the first benchmark designed for multi-perspective failure attribution in MAS, along with a new evaluation protocol tailored to this paradigm. Through extensive experiments, we find that prior conclusions suggesting LLMs struggle with failure attribution are largely driven by limitations in existing benchmark designs. Our results highlight the necessity of multi-perspective benchmarks and evaluation protocols for realistic and reliable MAS debugging.

</details>


### 31. Learning Rollout from Sampling:An R1-Style Tokenized Traffic Simulation Model

- **Authors:** Ziyan Wang, Peng Chen, Ding Li, Chiwei Li, Qichao Zhang, Zhongpu Xia, Guizhen Yu
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24989v1](http://arxiv.org/abs/2603.24989v1)
- **PDF:** [https://arxiv.org/pdf/2603.24989v1](https://arxiv.org/pdf/2603.24989v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learning diverse and high-fidelity traffic simulations from human driving demonstrations is crucial for autonomous driving evaluation. The recent next-token prediction (NTP) paradigm, widely adopted in large language models (LLMs), has been applied to traffic simulation and achieves iterative improvements via supervised fine-tuning (SFT). However, such methods limit active exploration of potentially valuable motion tokens, particularly in suboptimal regions. Entropy patterns provide a promising perspective for enabling exploration driven by motion token uncertainty. Motivated by this insight, we propose a novel tokenized traffic simulation policy, R1Sim, which represents an initial attempt to explore reinforcement learning based on motion token entropy patterns, and systematically analyzes the impact of different motion tokens on simulation outcomes. Specifically, we introduce an entropy-guided adaptive sampling mechanism that focuses on previously overlooked motion tokens with high uncertainty yet high potential. We further optimize motion behaviors using Group Relative Policy Optimization (GRPO), guided by a safety-aware reward design. Overall, these components enable a balanced exploration-exploitation trade-off through diverse high-uncertainty sampling and group-wise comparative estimation, resulting in realistic, safe, and diverse multi-agent behaviors. Extensive experiments on the Waymo Sim Agent benchmark demonstrate that R1Sim achieves competitive performance compared to state-of-the-art methods.

</details>


### 32. Belief-Driven Multi-Agent Collaboration via Approximate Perfect Bayesian Equilibrium for Social Simulation

- **Authors:** Weiwei Fang, Lin Li, Kaize Shi, Yu Yang, Jianwei Zhang
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24973v1](http://arxiv.org/abs/2603.24973v1)
- **PDF:** [https://arxiv.org/pdf/2603.24973v1](https://arxiv.org/pdf/2603.24973v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

High-fidelity social simulation is pivotal for addressing complex Web societal challenges, yet it demands agents capable of authentically replicating the dynamic spectrum of human interaction. Current LLM-based multi-agent frameworks, however, predominantly adhere to static interaction topologies, failing to capture the fluid oscillation between cooperative knowledge synthesis and competitive critical reasoning seen in real-world scenarios. This rigidity often leads to unrealistic ``groupthink'' or unproductive deadlocks, undermining the credibility of simulations for decision support. To bridge this gap, we propose \textit{BEACOF}, a \textit{belief-driven adaptive collaboration framework} inspired by Perfect Bayesian Equilibrium (PBE). By modeling social interaction as a dynamic game of incomplete information, BEACOF rigorously addresses the circular dependency between collaboration type selection and capability estimation. Agents iteratively refine probabilistic beliefs about peer capabilities and autonomously modulate their collaboration strategy, thereby ensuring sequentially rational decisions under uncertainty. Validated across adversarial (judicial), open-ended (social) and mixed (medical) scenarios, BEACOF prevents coordination failures and fosters robust convergence toward high-quality solutions, demonstrating superior potential for reliable social simulation. Source codes and datasets are publicly released at: https://github.com/WUT-IDEA/BEACOF.

</details>


### 33. FinMCP-Bench: Benchmarking LLM Agents for Real-World Financial Tool Use under the Model Context Protocol

- **Authors:** Jie Zhu, Yimin Tian, Boyang Li, Kehao Wu, Zhongzhi Liang, Junhui Li, Xianyin Zhang, Lifan Guo, Feng Chen, Yong Liu, Chi Zhang
- **Published:** 2026-03-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24943v1](http://arxiv.org/abs/2603.24943v1)
- **PDF:** [https://arxiv.org/pdf/2603.24943v1](https://arxiv.org/pdf/2603.24943v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper introduces \textbf{FinMCP-Bench}, a novel benchmark for evaluating large language models (LLMs) in solving real-world financial problems through tool invocation of financial model context protocols. FinMCP-Bench contains 613 samples spanning 10 main scenarios and 33 sub-scenarios, featuring both real and synthetic user queries to ensure diversity and authenticity. It incorporates 65 real financial MCPs and three types of samples, single tool, multi-tool, and multi-turn, allowing evaluation of models across different levels of task complexity. Using this benchmark, we systematically assess a range of mainstream LLMs and propose metrics that explicitly measure tool invocation accuracy and reasoning capabilities. FinMCP-Bench provides a standardized, practical, and challenging testbed for advancing research on financial LLM agents.

</details>


### 34. Context-Mediated Domain Adaptation in Multi-Agent Sensemaking Systems

- **Authors:** Anton Wolter, Leon Haag, Vaishali Dhanoa, Niklas Elmqvist
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24858v1](http://arxiv.org/abs/2603.24858v1)
- **PDF:** [https://arxiv.org/pdf/2603.24858v1](https://arxiv.org/pdf/2603.24858v1)
- **Categories:** cs.HC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Domain experts possess tacit knowledge that they cannot easily articulate through explicit specifications. When experts modify AI-generated artifacts by correcting terminology, restructuring arguments, and adjusting emphasis, these edits reveal domain understanding that remains latent in traditional prompt-based interactions. Current systems treat such modifications as endpoint corrections rather than as implicit specifications that could reshape subsequent reasoning. We propose context-mediated domain adaptation, a paradigm where user modifications to system-generated artifacts serve as implicit domain specification that reshapes LLM-powered multi-agent reasoning behavior. Through our system Seedentia, a web-based multi-agent framework for sense-making, we demonstrate bidirectional semantic links between generated artifacts and system reasoning. Our approach enables specification bootstrapping where vague initial prompts evolve into precise domain specifications through iterative human-AI collaboration, implicit knowledge transfer through reverse-engineered user edits, and in-context learning where agent behavior adapts based on observed correction patterns. We present results from an evaluation with domain experts who generated and modified research questions from academic papers. Our system extracted 46 domain knowledge entries from user modifications, demonstrating the feasibility of capturing implicit expertise through edit patterns, though the limited sample size constrains conclusions about systematic quality improvements.

</details>


### 35. SentinelAI: A Multi-Agent Framework for Structuring and Linking NG9-1-1 Emergency Incident Data

- **Authors:** Kliment Ho, Ilya Zaslavsky
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24856v1](http://arxiv.org/abs/2603.24856v1)
- **PDF:** [https://arxiv.org/pdf/2603.24856v1](https://arxiv.org/pdf/2603.24856v1)
- **Categories:** cs.AI, cs.CY, cs.ET, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Emergency response systems generate data from many agencies and systems. In practice, correlating and updating this information across sources in a way that aligns with Next Generation 9-1-1 data standards remains challenging. Ideally, this data should be treated as a continuous stream of operational updates, where new facts are integrated immediately to provide a timely and unified view of an evolving incident. This paper presents SentinelAI, a data integration and standardization framework for transforming emergency communications into standardized, machine-readable datasets that support integration, composite incident construction, and cross-source reasoning. SentinelAI implements a scalable processing pipeline composed of specialized agents. The EIDO Agent ingests raw communications and produces NENA-compliant Emergency Incident Data Object JSON.

</details>


### 36. AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A

- **Authors:** Sunil Prakash
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24775v1](http://arxiv.org/abs/2603.24775v1)
- **PDF:** [https://arxiv.org/pdf/2603.24775v1](https://arxiv.org/pdf/2603.24775v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly call tools via the Model Context Protocol (MCP) and delegate to other agents via Agent-to-Agent (A2A), yet neither protocol verifies agent identity. A scan of approximately 2,000 MCP servers found all lacked authentication. In our survey, we did not identify a prior implemented protocol that jointly combines public-key verifiable delegation, holder-side attenuation, expressive chained policy, transport bindings across MCP/A2A/HTTP, and provenance-oriented completion records. We introduce Invocation-Bound Capability Tokens (IBCTs), a primitive that fuses identity, attenuated authorization, and provenance binding into a single append-only token chain. IBCTs operate in two wire formats: compact mode (a signed JWT for single-hop cases) and chained mode (a Biscuit token with Datalog policies for multi-hop delegation). We provide reference implementations in Python and Rust with full cross-language interoperability. Compact mode verification takes 0.049ms (Rust) and 0.189ms (Python), with 0.22ms overhead over no-auth in real MCP-over-HTTP deployment. In a real multi-agent deployment with Gemini 2.5 Flash, AIP adds 2.35ms of overhead (0.086% of total end-to-end latency). Adversarial evaluation across 600 attack attempts shows 100% rejection rate, with two attack categories (delegation depth violation and audit evasion through empty context) uniquely caught by AIP's chained delegation model that neither unsigned nor plain JWT deployments detect.

</details>


### 37. Supervising Ralph Wiggum: Exploring a Metacognitive Co-Regulation Agentic AI Loop for Engineering Design

- **Authors:** Zeda Xu, Nikolas Martelaro, Christopher McComb
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24768v1](http://arxiv.org/abs/2603.24768v1)
- **PDF:** [https://arxiv.org/pdf/2603.24768v1](https://arxiv.org/pdf/2603.24768v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The engineering design research community has studied agentic AI systems that use Large Language Model (LLM) agents to automate the engineering design process. However, these systems are prone to some of the same pathologies that plague humans. Just as human designers, LLM design agents can fixate on existing paradigms and fail to explore alternatives when solving design challenges, potentially leading to suboptimal solutions. In this work, we propose (1) a novel Self-Regulation Loop (SRL), in which the Design Agent self-regulates and explicitly monitors its own metacognition, and (2) a novel Co-Regulation Design Agentic Loop (CRDAL), in which a Metacognitive Co-Regulation Agent assists the Design Agent in metacognition to mitigate design fixation, thereby improving system performance for engineering design tasks. In the battery pack design problem examined here, we found that the novel CRDAL system generates designs with better performance, without significantly increasing the computational cost, compared to a plain Ralph Wiggum Loop (RWL) and the metacognitively self-assessing Self-Regulation Loop (SRL). Also, we found that the CRDAL system navigated through the latent design space more effectively than both SRL and RWL. However, the SRL did not generate designs with significantly better performance than RWL, even though it explored a different region of the design space. The proposed system architectures and findings of this work provide practical implications for future development of agentic AI systems for engineering design.

</details>


### 38. Decentralized Task Scheduling in Distributed Systems: A Deep Reinforcement Learning Approach

- **Authors:** Daniel Benniah John
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24738v1](http://arxiv.org/abs/2603.24738v1)
- **PDF:** [https://arxiv.org/pdf/2603.24738v1](https://arxiv.org/pdf/2603.24738v1)
- **Categories:** cs.DC, cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Efficient task scheduling in large-scale distributed systems presents significant challenges due to dynamic workloads, heterogeneous resources, and competing quality-of-service requirements. Traditional centralized approaches face scalability limitations and single points of failure, while classical heuristics lack adaptability to changing conditions. This paper proposes a decentralized multi-agent deep reinforcement learning (DRL-MADRL) framework for task scheduling in heterogeneous distributed systems. We formulate the problem as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP) and develop a lightweight actor-critic architecture implemented using only NumPy, enabling deployment on resource-constrained edge devices without heavyweight machine learning frameworks. Using workload characteristics derived from the publicly available Google Cluster Trace dataset, we evaluate our approach on a 100-node heterogeneous system processing 1,000 tasks per episode over 30 experimental runs. Experimental results demonstrate 15.6% improvement in average task completion time (30.8s vs 36.5s for random baseline), 15.2% energy efficiency gain (745.2 kWh vs 878.3 kWh), and 82.3% SLA satisfaction compared to 75.5% for baselines, with all improvements statistically significant (p < 0.001). The lightweight implementation requires only NumPy, Matplotlib, and SciPy. Complete source code and experimental data are provided for full reproducibility at https://github.com/danielbenniah/marl-distributed-scheduling.

</details>


### 39. When Is Collective Intelligence a Lottery? Multi-Agent Scaling Laws for Memetic Drift in LLMs

- **Authors:** Hidenori Tanaka
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24676v1](http://arxiv.org/abs/2603.24676v1)
- **PDF:** [https://arxiv.org/pdf/2603.24676v1](https://arxiv.org/pdf/2603.24676v1)
- **Categories:** cs.AI, cond-mat.dis-nn, cond-mat.stat-mech, physics.bio-ph, physics.soc-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems powered by large language models (LLMs) are increasingly deployed in settings that shape consequential decisions, both directly and indirectly. Yet it remains unclear whether their outcomes reflect collective reasoning, systematic bias, or mere chance. Recent work has sharpened this question with naming games, showing that even when no individual agent favors any label a priori, populations rapidly break symmetry and reach consensus. Here, we reveal the mechanism by introducing a minimal model, Quantized Simplex Gossip (QSG), and trace the microscopic origin of this agreement to mutual in-context learning. In QSG, agents maintain internal belief states but learn from one another's sampled outputs, so one agent's arbitrary choice becomes the next agent's evidence and can compound toward agreement. By analogy with neutral evolution, we call this sampling-driven regime memetic drift. QSG predicts a crossover from a drift-dominated regime, where consensus is effectively a lottery, to a selection regime, where weak biases are amplified and shape the outcome. We derive scaling laws for drift-induced polarization as a function of population size, communication bandwidth, in-context adaptation rate, and agents' internal uncertainty, and we validate them in both QSG simulations and naming-game experiments with LLM populations. Together, these results provide a framework for studying the collective mechanisms of social representation formation in multi-agent systems.

</details>


### 40. MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination

- **Authors:** Zhuo Li, Yupeng Zhang, Pengyu Cheng, Jiajun Song, Mengyu Zhou, Hao Li, Shujie Hu, Yu Qin, Erchao Zhao, Xiaoxi Jiang, Guanjun Jiang
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24579v1](http://arxiv.org/abs/2603.24579v1)
- **PDF:** [https://arxiv.org/pdf/2603.24579v1](https://arxiv.org/pdf/2603.24579v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Hallucination remains a critical bottleneck for large language models (LLMs), undermining their reliability in real-world applications, especially in Retrieval-Augmented Generation (RAG) systems. While existing hallucination detection methods employ LLM-as-a-judge to verify LLM outputs against retrieved evidence, they suffer from inherent confirmation bias, where the verifier inadvertently reproduces the errors of the original generation. To address this, we introduce Multi-Agent Reinforced Self-Check for Hallucination (MARCH), a framework that enforces rigorous factual alignment by leveraging deliberate information asymmetry. MARCH orchestrates a collaborative pipeline of three specialized agents: a Solver, a Proposer, and a Checker. The Solver generates an initial RAG response, which the Proposer decomposes into claim-level verifiable atomic propositions. Crucially, the Checker validates these propositions against retrieved evidence in isolation, deprived of the Solver's original output. This well-crafted information asymmetry scheme breaks the cycle of self-confirmation bias. By training this pipeline with multi-agent reinforcement learning (MARL), we enable the agents to co-evolve and optimize factual adherence. Extensive experiments across hallucination benchmarks demonstrate that MARCH substantially reduces hallucination rates. Notably, an 8B-parameter LLM equipped with MARCH achieves performance competitive with powerful closed-source models. MARCH paves a scalable path for factual self-improvement of LLMs through co-evolution. The code is at https://github.com/Qwen-Applications/MARCH.

</details>


### 41. The Free-Market Algorithm: Self-Organizing Optimization for Open-Ended Complex Systems

- **Authors:** Martin Jaraiz
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24559v1](http://arxiv.org/abs/2603.24559v1)
- **PDF:** [https://arxiv.org/pdf/2603.24559v1](https://arxiv.org/pdf/2603.24559v1)
- **Categories:** cs.NE, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce the Free-Market Algorithm (FMA), a novel metaheuristic inspired by free-market economics. Unlike Genetic Algorithms, Particle Swarm Optimization, and Simulated Annealing -- which require prescribed fitness functions and fixed search spaces -- FMA uses distributed supply-and-demand dynamics where fitness is emergent, the search space is open-ended, and solutions take the form of hierarchical pathway networks. Autonomous agents discover rules, trade goods, open and close firms, and compete for demand with no centralized controller.
  FMA operates through a three-layer architecture: a universal market mechanism (supply, demand, competition, selection), pluggable domain-specific behavioral rules, and domain-specific observation. The market mechanism is identical across applications; only the behavioral rules change.
  Validated in two unrelated domains. In prebiotic chemistry, starting from 900 bare atoms (C, H, O, N), FMA discovers all 12 feasible amino acid formulas, all 5 nucleobases, the formose sugar chain, and Krebs cycle intermediates in under 5 minutes on a laptop -- with up to 240 independent synthesis routes per product. In macroeconomic forecasting, reading a single input-output table with zero estimated parameters, FMA achieves Mean Absolute Error of 0.42 percentage points for non-crisis GDP prediction, comparable to professional forecasters, portable to 33 countries.
  Assembly Theory alignment shows that FMA provides the first explicit, tunable mechanism for the selection signatures described by Sharma et al. (Nature, 2023). The event-driven assembly dynamics resonate with foundational programs in physics -- causal set theory, relational quantum mechanics, constructor theory -- suggesting that Darwinian market dynamics may reflect a deeper organizational principle that lead to the unfolding of Nature itself.

</details>


### 42. Can LLMs Beat Classical Hyperparameter Optimization Algorithms? A Study on autoresearch

- **Authors:** Fabio Ferreira, Lucca Wobbe, Arjun Krishnakumar, Frank Hutter, Arber Zela
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24647v1](http://arxiv.org/abs/2603.24647v1)
- **PDF:** [https://arxiv.org/pdf/2603.24647v1](https://arxiv.org/pdf/2603.24647v1)
- **Categories:** cs.LG, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

The autoresearch repository enables an LLM agent to search for optimal hyperparameter configurations on an unconstrained search space by editing the training code directly. Given a fixed compute budget and constraints, we use \emph{autoresearch} as a testbed to compare classical hyperparameter optimization (HPO) algorithms against LLM-based methods on tuning the hyperparameters of a small language model. Within a fixed hyperparameter search space, classical HPO methods such as CMA-ES and TPE consistently outperform LLM-based agents. However, an LLM agent that directly edits training source code in an unconstrained search space narrows the gap to classical methods substantially despite using only a self-hosted open-weight 27B model. Methods that avoid out-of-memory failures outperform those with higher search diversity, suggesting that reliability matters more than exploration breadth. While small and mid-sized LLMs struggle to track optimization state across trials, classical methods lack domain knowledge. To bridge this gap, we introduce Centaur, a hybrid that shares CMA-ES's internal state, including mean vector, step-size, and covariance matrix, with an LLM. Centaur achieves the best result in our experiments, with its 0.8B variant outperforming the 27B variant, suggesting that a cheap LLM suffices when paired with a strong classical optimizer. The 0.8B model is insufficient for unconstrained code editing but sufficient for hybrid optimization, while scaling to 27B provides no advantage for fixed search space methods with the open-weight models tested. Code is available at https://github.com/ferreirafabio/autoresearch-automl.

</details>


### 43. Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs

- **Authors:** Alexander Panfilov, Peter Romov, Igor Shilov, Yves-Alexandre de Montjoye, Jonas Geiping, Maksym Andriushchenko
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24511v1](http://arxiv.org/abs/2603.24511v1)
- **PDF:** [https://arxiv.org/pdf/2603.24511v1](https://arxiv.org/pdf/2603.24511v1)
- **Categories:** cs.LG, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents like Claude Code can not only write code but also be used for autonomous AI research and engineering \citep{rank2026posttrainbench, novikov2025alphaevolve}. We show that an \emph{autoresearch}-style pipeline \citep{karpathy2026autoresearch} powered by Claude Code discovers novel white-box adversarial attack \textit{algorithms} that \textbf{significantly outperform all existing (30+) methods} in jailbreaking and prompt injection evaluations.
  Starting from existing attack implementations, such as GCG~\citep{zou2023universal}, the agent iterates to produce new algorithms achieving up to 40\% attack success rate on CBRN queries against GPT-OSS-Safeguard-20B, compared to $\leq$10\% for existing algorithms (\Cref{fig:teaser}, left).
  The discovered algorithms generalize: attacks optimized on surrogate models transfer directly to held-out models, achieving \textbf{100\% ASR against Meta-SecAlign-70B} \citep{chen2025secalign} versus 56\% for the best baseline (\Cref{fig:teaser}, middle). Extending the findings of~\cite{carlini2025autoadvexbench}, our results are an early demonstration that incremental safety and security research can be automated using LLM agents. White-box adversarial red-teaming is particularly well-suited for this: existing methods provide strong starting points, and the optimization objective yields dense, quantitative feedback. We release all discovered attacks alongside baseline implementations and evaluation code at https://github.com/romovpa/claudini.

</details>


### 44. Multi-Agent Reasoning with Consistency Verification Improves Uncertainty Calibration in Medical MCQA

- **Authors:** John Ray B. Martinez
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24481v1](http://arxiv.org/abs/2603.24481v1)
- **PDF:** [https://arxiv.org/pdf/2603.24481v1](https://arxiv.org/pdf/2603.24481v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Miscalibrated confidence scores are a practical obstacle to deploying AI in clinical settings. A model that is always overconfident offers no useful signal for deferral. We present a multi-agent framework that combines domain-specific specialist agents with Two-Phase Verification and S-Score Weighted Fusion to improve both calibration and discrimination in medical multiple-choice question answering. Four specialist agents (respiratory, cardiology, neurology, gastroenterology) generate independent diagnoses using Qwen2.5-7B-Instruct. Each diagnosis is then subjected to a two-phase self-verification process that measures internal consistency and produces a Specialist Confidence Score (S-score). The S-scores drive a weighted fusion strategy that selects the final answer and calibrates the reported confidence. We evaluate across four experimental settings, covering 100-question and 250-question high-disagreement subsets of both MedQA-USMLE and MedMCQA. Calibration improvement is the central finding, with ECE reduced by 49-74% across all four settings, including the harder MedMCQA benchmark where these gains persist even when absolute accuracy is constrained by knowledge-intensive recall demands. On MedQA-250, the full system achieves ECE = 0.091 (74.4% reduction over the single-specialist baseline) and AUROC = 0.630 (+0.056) at 59.2% accuracy. Ablation analysis identifies Two-Phase Verification as the primary calibration driver and multi-agent reasoning as the primary accuracy driver. These results establish that consistency-based verification produces more reliable uncertainty estimates across diverse medical question types, providing a practical confidence signal for deferral in safety-critical clinical AI applications.

</details>


### 45. Relaxing Constraints in Anonymous Multi Agent Path Finding for Large Agents

- **Authors:** Stepan Dergachev, Dmitry Avdeev
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24442v1](http://arxiv.org/abs/2603.24442v1)
- **PDF:** [https://arxiv.org/pdf/2603.24442v1](https://arxiv.org/pdf/2603.24442v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The study addressed the problem of Anonymous Multi-Agent Path-finding (AMAPF). Unlike the classical formulation, where the assignment of agents to goals is fixed, in the anonymous MAPF setting it is irrelevant which agent reaches specific goal, provided that all goals are occupied. Most existing multi-agent pathfinding algorithms rely on a discrete representation of the environment (e.g., square grids) and do not account for the sizes of agents. This limits their applicability in real-world scenarios, such as trajectory planning for mobile robots in warehouses. Conversely, methods operating in continuous space typically impose substantial restrictions on the input data, such as constraints on the distances between initial and goal positions or between start/goal positions and obstacles. In this work, we considered one of the AMAPF algorithms designed for continuous space, where agents are modeled as disks of equal size. The algorithm requires a strict minimum separation of $4$ agent radii between any start/goal positions. Proposed a modification aimed at relaxing the constraints and reduce this limit from $4$ to $2\sqrt{3}$. We theoretically demonstrated that the proposed enhancements preserve original theoretical properties, including the guarantee that all agents will eventually achieve their goals safely and without collisions.

</details>


### 46. CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents

- **Authors:** Xiangru Jian, Shravan Nayak, Kevin Qinghong Lin, Aarash Feizi, Kaixin Li, Patrice Bechard, Spandana Gella, Sai Rajeswar
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24440v1](http://arxiv.org/abs/2603.24440v1)
- **PDF:** [https://arxiv.org/pdf/2603.24440v1](https://arxiv.org/pdf/2603.24440v1)
- **Categories:** cs.LG, cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Computer-use agents (CUAs) hold great promise for automating complex desktop workflows, yet progress toward general-purpose agents is bottlenecked by the scarcity of continuous, high-quality human demonstration videos. Recent work emphasizes that continuous video, not sparse screenshots, is the critical missing ingredient for scaling these agents. However, the largest existing open dataset, ScaleCUA, contains only 2 million screenshots, equating to less than 20 hours of video. To address this bottleneck, we introduce CUA-Suite, a large-scale ecosystem of expert video demonstrations and dense annotations for professional desktop computer-use agents. At its core is VideoCUA, which provides approximately 10,000 human-demonstrated tasks across 87 diverse applications with continuous 30 fps screen recordings, kinematic cursor traces, and multi-layerfed reasoning annotations, totaling approximately 55 hours and 6 million frames of expert video. Unlike sparse datasets that capture only final click coordinates, these continuous video streams preserve the full temporal dynamics of human interaction, forming a superset of information that can be losslessly transformed into the formats required by existing agent frameworks. CUA-Suite further provides two complementary resources: UI-Vision, a rigorous benchmark for evaluating grounding and planning capabilities in CUAs, and GroundCUA, a large-scale grounding dataset with 56K annotated screenshots and over 3.6 million UI element annotations. Preliminary evaluation reveals that current foundation action models struggle substantially with professional desktop applications (~60% task failure rate). Beyond evaluation, CUA-Suite's rich multimodal corpus supports emerging research directions including generalist screen parsing, continuous spatial control, video-based reward modeling, and visual world models. All data and models are publicly released.

</details>


### 47. ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents Through Skills, Plugins, and Watchers

- **Authors:** Songyang Liu, Chaozhuo Li, Chenxu Wang, Jinyu Hou, Zejian Chen, Litian Zhang, Zheng Liu, Qiwei Ye, Yiming Hei, Xi Zhang, Zhongyuan Wang
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24414v1](http://arxiv.org/abs/2603.24414v1)
- **PDF:** [https://arxiv.org/pdf/2603.24414v1](https://arxiv.org/pdf/2603.24414v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

OpenClaw has rapidly established itself as a leading open-source autonomous agent runtime, offering powerful capabilities including tool integration, local file access, and shell command execution. However, these broad operational privileges introduce critical security vulnerabilities, transforming model errors into tangible system-level threats such as sensitive data leakage, privilege escalation, and malicious third-party skill execution. Existing security measures for the OpenClaw ecosystem remain highly fragmented, addressing only isolated stages of the agent lifecycle rather than providing holistic protection. To bridge this gap, we present ClawKeeper, a real-time security framework that integrates multi-dimensional protection mechanisms across three complementary architectural layers. (1) \textbf{Skill-based protection} operates at the instruction level, injecting structured security policies directly into the agent context to enforce environment-specific constraints and cross-platform boundaries. (2) \textbf{Plugin-based protection} serves as an internal runtime enforcer, providing configuration hardening, proactive threat detection, and continuous behavioral monitoring throughout the execution pipeline. (3) \textbf{Watcher-based protection} introduces a novel, decoupled system-level security middleware that continuously verifies agent state evolution. It enables real-time execution intervention without coupling to the agent's internal logic, supporting operations such as halting high-risk actions or enforcing human confirmation. We argue that this Watcher paradigm holds strong potential to serve as a foundational building block for securing next-generation autonomous agent systems. Extensive qualitative and quantitative evaluations demonstrate the effectiveness and robustness of ClawKeeper across diverse threat scenarios. We release our code.

</details>


### 48. AI-Supervisor: Autonomous AI Research Supervision via a Persistent Research World Model

- **Authors:** Yunbo Long
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24402v2](http://arxiv.org/abs/2603.24402v2)
- **PDF:** [https://arxiv.org/pdf/2603.24402v2](https://arxiv.org/pdf/2603.24402v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing automated research systems operate as stateless, linear pipelines -- generating outputs without maintaining any persistent understanding of the research landscape they navigate. They process papers sequentially, propose ideas without structured gap analysis, and lack mechanisms for agents to verify, challenge, or refine each other's findings. We present \textbf{AI-Supervisor}, a multi-agent orchestration framework where specialized agents provide end-to-end AI research supervision driven by human interests -- from literature review through gap discovery, method development, evaluation, and paper writing -- through autonomous exploration and self-correcting updates of research knowledge. Unlike sequential pipelines, AI-Supervisor maintains a continuously evolving \emph{Research World Model}, implemented as a Knowledge Graph, that captures methods, benchmarks, known limitations, and unexplored gaps, serving as shared memory across all agents and enabling agents to explore and build upon a structured understanding of the research landscape. The framework introduces three architectural contributions: (1) \emph{structured gap discovery} that decomposes methods into core modules, validates their performance across benchmarks, and maps the specific gaps each module creates; (2) \emph{self-correcting discovery loops} that probe why modules succeed on certain problems and fail on others, whether benchmarks carry hidden biases, and whether evaluation protocols remain adequate for emerging challenges; and (3) \emph{self-improving development loops} governed by cross-domain mechanism search that iteratively targets failing modules by finding solutions from other scientific fields. All agents operate under a \emph{consensus mechanism} where independent findings are corroborated before being committed to the Research World Model.

</details>


### 49. CoordLight: Learning Decentralized Coordination for Network-Wide Traffic Signal Control

- **Authors:** Yifeng Zhang, Harsh Goel, Peizhuo Li, Mehul Damani, Sandeep Chinchali, Guillaume Sartoretti
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24366v1](http://arxiv.org/abs/2603.24366v1)
- **PDF:** [https://arxiv.org/pdf/2603.24366v1](https://arxiv.org/pdf/2603.24366v1)
- **Categories:** cs.LG, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Adaptive traffic signal control (ATSC) is crucial in alleviating congestion, maximizing throughput and promoting sustainable mobility in ever-expanding cities. Multi-Agent Reinforcement Learning (MARL) has recently shown significant potential in addressing complex traffic dynamics, but the intricacies of partial observability and coordination in decentralized environments still remain key challenges in formulating scalable and efficient control strategies. To address these challenges, we present CoordLight, a MARL-based framework designed to improve intra-neighborhood traffic by enhancing decision-making at individual junctions (agents), as well as coordination with neighboring agents, thereby scaling up to network-level traffic optimization. Specifically, we introduce the Queue Dynamic State Encoding (QDSE), a novel state representation based on vehicle queuing models, which strengthens the agents' capability to analyze, predict, and respond to local traffic dynamics. We further propose an advanced MARL algorithm, named Neighbor-aware Policy Optimization (NAPO). It integrates an attention mechanism that discerns the state and action dependencies among adjacent agents, aiming to facilitate more coordinated decision-making, and to improve policy learning updates through robust advantage calculation. This enables agents to identify and prioritize crucial interactions with influential neighbors, thus enhancing the targeted coordination and collaboration among agents. Through comprehensive evaluations against state-of-the-art traffic signal control methods over three real-world traffic datasets composed of up to 196 intersections, we empirically show that CoordLight consistently exhibits superior performance across diverse traffic networks with varying traffic flows. The code is available at https://github.com/marmotlab/CoordLight

</details>


### 50. GameplayQA: A Benchmarking Framework for Decision-Dense POV-Synced Multi-Video Understanding of 3D Virtual Agents

- **Authors:** Yunzhe Wang, Runhui Xu, Kexin Zheng, Tianyi Zhang, Jayavibhav Niranjan Kogundi, Soham Hans, Volkan Ustun
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24329v1](http://arxiv.org/abs/2603.24329v1)
- **PDF:** [https://arxiv.org/pdf/2603.24329v1](https://arxiv.org/pdf/2603.24329v1)
- **Categories:** cs.CL, cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal LLMs are increasingly deployed as perceptual backbones for autonomous agents in 3D environments, from robotics to virtual worlds. These applications require agents to perceive rapid state changes, attribute actions to the correct entities, and reason about concurrent multi-agent behaviors from a first-person perspective, capabilities that existing benchmarks do not adequately evaluate. We introduce GameplayQA, a framework for evaluating agentic-centric perception and reasoning through video understanding. Specifically, we densely annotate multiplayer 3D gameplay videos at 1.22 labels/second, with time-synced, concurrent captions of states, actions, and events structured around a triadic system of Self, Other Agents, and the World, a natural decomposition for multi-agent environments. From these annotations, we refined 2.4K diagnostic QA pairs organized into three levels of cognitive complexity, accompanied by a structured distractor taxonomy that enables fine-grained analysis of where models hallucinate. Evaluation of frontier MLLMs reveals a substantial gap from human performance, with common failures in temporal and cross-video grounding, agent-role attribution, and handling the decision density of the game. We hope GameplayQA stimulates future research at the intersection of embodied AI, agentic perception, and world modeling.

</details>


### 51. Large Language Model Guided Incentive Aware Reward Design for Cooperative Multi-Agent Reinforcement Learning

- **Authors:** Dogan Urgun, Gokhan Gungor
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24324v1](http://arxiv.org/abs/2603.24324v1)
- **PDF:** [https://arxiv.org/pdf/2603.24324v1](https://arxiv.org/pdf/2603.24324v1)
- **Categories:** cs.LG, cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Designing effective auxiliary rewards for cooperative multi-agent systems remains a precarious task; misaligned incentives risk inducing suboptimal coordination, especially where sparse task feedback fails to provide sufficient grounding. This study introduces an automated reward design framework that leverages large language models to synthesize executable reward programs from environment instrumentation. The procedure constrains candidate programs within a formal validity envelope and evaluates their efficacy by training policies from scratch under a fixed computational budget; selection depends exclusively on the sparse task return. The framework is evaluated across four distinct Overcooked-AI layouts characterized by varied corridor congestion, handoff dependencies, and structural asymmetries. Iterative search generations consistently yield superior task returns and delivery counts, with the most pronounced gains occurring in environments dominated by interaction bottlenecks. Diagnostic analysis of the synthesized shaping components indicates increased interdependence in action selection and improved signal alignment in coordination-intensive tasks. These results demonstrate that the search for objectivegrounded reward programs can mitigate the burden of manual engineering while producing shaping signals compatible with cooperative learning under finite budgets.

</details>


### 52. The Specification Gap: Coordination Failure Under Partial Knowledge in Code Agents

- **Authors:** Camilo Chacón Sartori
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24284v1](http://arxiv.org/abs/2603.24284v1)
- **PDF:** [https://arxiv.org/pdf/2603.24284v1](https://arxiv.org/pdf/2603.24284v1)
- **Categories:** cs.SE, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

When multiple LLM-based code agents independently implement parts of the same class, they must agree on shared internal representations, even when the specification leaves those choices implicit. We study this coordination problem across 51 class-generation tasks, progressively stripping specification detail from full docstrings (L0) to bare signatures (L3), and introducing opposing structural biases (lists vs. dictionaries) to stress-test integration. Three findings emerge. First, a persistent specification gap: two-agent integration accuracy drops from 58% to 25% as detail is removed, while a single-agent baseline degrades more gracefully (89% to 56%), leaving a 25--39 pp coordination gap that is consistent across two Claude models (Sonnet, Haiku) and three independent runs. Second, an AST-based conflict detector achieves 97% precision at the weakest specification level without additional LLM calls, yet a factorial recovery experiment shows that restoring the full specification alone recovers the single-agent ceiling (89%), while providing conflict reports adds no measurable benefit. Third, decomposing the gap into coordination cost (+16 pp) and information asymmetry (+11 pp) suggests that the two effects are independent and approximately additive. The gap is not merely a consequence of hidden information, but reflects the difficulty of producing compatible code without shared decisions. These results support a specification-first view of multi-agent code generation: richer specifications are both the primary coordination mechanism and the sufficient recovery instrument.

</details>


### 53. Environment-Grounded Multi-Agent Workflow for Autonomous Penetration Testing

- **Authors:** Michael Somma, Markus Großpointner, Paul Zabalegui, Eppu Heilimo, Branka Stojanović
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24221v1](http://arxiv.org/abs/2603.24221v1)
- **PDF:** [https://arxiv.org/pdf/2603.24221v1](https://arxiv.org/pdf/2603.24221v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The increasing complexity and interconnectivity of digital infrastructures make scalable and reliable security assessment methods essential. Robotic systems represent a particularly important class of operational technology, as modern robots are highly networked cyber-physical systems deployed in domains such as industrial automation, logistics, and autonomous services. This paper explores the use of large language models for automated penetration testing in robotic environments. We propose an environment-grounded multi-agent architecture tailored to Robotics-based systems. The approach dynamically constructs a shared graph-based memory during execution that captures the observable system state, including network topology, communication channels, vulnerabilities, and attempted exploits. This enables structured automation while maintaining traceability and effective context management throughout the testing process. Evaluated across multiple iterations within a specialized robotics Capture-the-Flag scenario (ROS/ROS2), the system demonstrated high reliability, successfully completing the challenge in 100\% of test runs (n=5). This performance significantly exceeds literature benchmarks while maintaining the traceability and human oversight required by frameworks like the EU AI Act.

</details>


### 54. Experiential Reflective Learning for Self-Improving LLM Agents

- **Authors:** Marc-Antoine Allard, Arnaud Teinturier, Victor Xing, Gautier Viaud
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24639v1](http://arxiv.org/abs/2603.24639v1)
- **PDF:** [https://arxiv.org/pdf/2603.24639v1](https://arxiv.org/pdf/2603.24639v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in large language models (LLMs) have enabled the development of autonomous agents capable of complex reasoning and multi-step problem solving. However, these agents struggle to adapt to specialized environments and do not leverage past interactions, approaching each new task from scratch regardless of their accumulated experience. We introduce Experiential Reflective Learning (ERL), a simple self-improvement framework that enables rapid environment adaptation through experiential learning. ERL reflects on task trajectories and outcomes to generate heuristics, capturing actionable lessons that transfer across tasks. At test time, relevant heuristics are retrieved based on the current task and injected into the agent's context to guide execution. On the Gaia2 benchmark, ERL improves success rate by 7.8% over a ReAct baseline, with large gains in task completion reliability, and outperforms prior experiential learning methods. Through systematic ablations, we find that selective retrieval is essential and that heuristics provide more transferable abstractions than few-shot trajectory prompting. These results demonstrate that reflecting on single-attempt experiences to extract transferable heuristics enables effective agent self-improvement.

</details>


### 55. On Gossip Algorithms for Machine Learning with Pairwise Objectives

- **Authors:** Igor Colin, Aurélien Bellet, Stephan Clémençon, Joseph Salmon
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24128v1](http://arxiv.org/abs/2603.24128v1)
- **PDF:** [https://arxiv.org/pdf/2603.24128v1](https://arxiv.org/pdf/2603.24128v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

In the IoT era, information is more and more frequently picked up by connected smart sensors with increasing, though limited, storage, communication and computation abilities. Whether due to privacy constraints or to the structure of the distributed system, the development of statistical learning methods dedicated to data that are shared over a network is now a major issue. Gossip-based algorithms have been developed for the purpose of solving a wide variety of statistical learning tasks, ranging from data aggregation over sensor networks to decentralized multi-agent optimization. Whereas the vast majority of contributions consider situations where the function to be estimated or optimized is a basic average of individual observations, it is the goal of this article to investigate the case where the latter is of pairwise nature, taking the form of a U -statistic of degree two. Motivated by various problems such as similarity learning, ranking or clustering for instance, we revisit gossip algorithms specifically designed for pairwise objective functions and provide a comprehensive theoretical framework for their convergence. This analysis fills a gap in the literature by establishing conditions under which these methods succeed, and by identifying the graph properties that critically affect their efficiency. In particular, a refined analysis of the convergence upper and lower bounds is performed.

</details>


### 56. Dual-Graph Multi-Agent Reinforcement Learning for Handover Optimization

- **Authors:** Matteo Salvatori, Filippo Vannella, Sebastian Macaluso, Stylianos E. Trevlakis, Carlos Segura Perales, José Suarez-Varela, Alexandros-Apostolos A. Boulogeorgos, Ioannis Arapakis
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24634v1](http://arxiv.org/abs/2603.24634v1)
- **PDF:** [https://arxiv.org/pdf/2603.24634v1](https://arxiv.org/pdf/2603.24634v1)
- **Categories:** cs.NI, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

HandOver (HO) control in cellular networks is governed by a set of HO control parameters that are traditionally configured through rule-based heuristics. A key parameter for HO optimization is the Cell Individual Offset (CIO), defined for each pair of neighboring cells and used to bias HO triggering decisions. At network scale, tuning CIOs becomes a tightly coupled problem: small changes can redirect mobility flows across multiple neighbors, and static rules often degrade under non-stationary traffic and mobility. We exploit the pairwise structure of CIOs by formulating HO optimization as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP) on the network's dual graph. In this representation, each agent controls a neighbor-pair CIO and observes Key Performance Indicators (KPIs) aggregated over its local dual-graph neighborhood, enabling scalable decentralized decisions while preserving graph locality. Building on this formulation, we propose TD3-D-MA, a discrete Multi-Agent Reinforcement Learning (MARL) variant of the TD3 algorithm with a shared-parameter Graph Neural Network (GNN) actor operating on the dual graph and region-wise double critics for training, improving credit assignment in dense deployments. We evaluate TD3-D-MA in an ns-3 system-level simulator configured with real-world network operator parameters across heterogeneous traffic regimes and network topologies. Results show that TD3-D-MA improves network throughput over standard HO heuristics and centralized RL baselines, and generalizes robustly under topology and traffic shifts.

</details>


### 57. FinToolSyn: A forward synthesis Framework for Financial Tool-Use Dialogue Data with Dynamic Tool Retrieval

- **Authors:** Caishuang Huang, Yang Qiao, Rongyu Zhang, Junjie Ye, Pu Lu, Wenxi Wu, Meng Zhou, Xiku Du, Tao Gui, Qi Zhang, Xuanjing Huang
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24051v1](http://arxiv.org/abs/2603.24051v1)
- **PDF:** [https://arxiv.org/pdf/2603.24051v1](https://arxiv.org/pdf/2603.24051v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-use capabilities are vital for Large Language Models (LLMs) in finance, a domain characterized by massive investment targets and data-intensive inquiries. However, existing data synthesis methods typically rely on a reverse synthesis paradigm, generating user queries from pre-sampled tools. This approach inevitably introduces artificial explicitness, yielding queries that fail to capture the implicit, event-driven nature of real-world needs. Moreover, its reliance on static tool sets overlooks the dynamic retrieval process required to navigate massive tool spaces. To address these challenges, we introduce \textit{FinToolSyn}, a forward synthesis framework designed to generate high-quality financial dialogues. Progressing from persona instruction and atomic tool synthesis to dynamic retrieval dialogue generation, our pipeline constructs a repository of 43,066 tools and synthesizes over 148k dialogue instances, incorporating dynamic retrieval to emulate the noisy candidate sets typical of massive tool spaces. We also establish a dedicated benchmark to evaluate tool-calling capabilities in realistic financial scenarios. Extensive experiments demonstrate that models trained on FinToolSyn achieve a 21.06\% improvement, providing a robust foundation for tool learning in financial scenarios.

</details>


### 58. ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents

- **Authors:** Bingqing Wei, Zhongyu Xia, Dingai Liu, Xiaoyu Zhou, Zhiwei Lin, Yongtao Wang
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24018v1](http://arxiv.org/abs/2603.24018v1)
- **PDF:** [https://arxiv.org/pdf/2603.24018v1](https://arxiv.org/pdf/2603.24018v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Vision-language models (VLMs) have shown remarkable general capabilities, yet embodied agents built on them fail at complex tasks, often skipping critical steps, proposing invalid actions, and repeating mistakes. These failures arise from a fundamental gap between the static training data of VLMs and the physical interaction for embodied tasks. VLMs can learn rich semantic knowledge from static data but lack the ability to interact with the world. To address this issue, we introduce ELITE, an embodied agent framework with {E}xperiential {L}earning and {I}ntent-aware {T}ransfer that enables agents to continuously learn from their own environment interaction experiences, and transfer acquired knowledge to procedurally similar tasks. ELITE operates through two synergistic mechanisms, \textit{i.e.,} self-reflective knowledge construction and intent-aware retrieval. Specifically, self-reflective knowledge construction extracts reusable strategies from execution trajectories and maintains an evolving strategy pool through structured refinement operations. Then, intent-aware retrieval identifies relevant strategies from the pool and applies them to current tasks. Experiments on the EB-ALFRED and EB-Habitat benchmarks show that ELITE achieves 9\% and 5\% performance improvement over base VLMs in the online setting without any supervision. In the supervised setting, ELITE generalizes effectively to unseen task categories, achieving better performance compared to state-of-the-art training-based methods. These results demonstrate the effectiveness of ELITE for bridging the gap between semantic understanding and reliable action execution.

</details>


### 59. Language-Grounded Multi-Agent Planning for Personalized and Fair Participatory Urban Sensing

- **Authors:** Xusen Guo, Mingxing Peng, Hongliang Lu, Hai Yang, Jun Ma, Yuxuan Liang
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24014v1](http://arxiv.org/abs/2603.24014v1)
- **PDF:** [https://arxiv.org/pdf/2603.24014v1](https://arxiv.org/pdf/2603.24014v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Participatory urban sensing leverages human mobility for large-scale urban data collection, yet existing methods typically rely on centralized optimization and assume homogeneous participants, resulting in rigid assignments that overlook personal preferences and heterogeneous urban contexts. We propose MAPUS, an LLM-based multi-agent framework for personalized and fair participatory urban sensing. In our framework, participants are modeled as autonomous agents with individual profiles and schedules, while a coordinator agent performs fairness-aware selection and refines sensing routes through language-based negotiation. Experiments on real-world datasets show that MAPUS achieves competitive sensing coverage while substantially improving participant satisfaction and fairness, promoting more human-centric and sustainable urban sensing systems.

</details>


### 60. Policy-Guided Threat Hunting: An LLM enabled Framework with Splunk SOC Triage

- **Authors:** Rishikesh Sahay, Bell Eapen, Weizhi Meng, Md Rasel Al Mamun, Nikhil Kumar Dora, Manjusha Sumasadan, Sumit Kumar Tetarave, Rod Soto
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23966v1](http://arxiv.org/abs/2603.23966v1)
- **PDF:** [https://arxiv.org/pdf/2603.23966v1](https://arxiv.org/pdf/2603.23966v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

With frequently evolving Advanced Persistent Threats (APTs) in cyberspace, traditional security solutions approaches have become inadequate for threat hunting for organizations. Moreover, SOC (Security Operation Centers) analysts are often overwhelmed and struggle to analyze the huge volume of logs received from diverse devices in organizations. To address these challenges, we propose an automated and dynamic threat hunting framework for monitoring evolving threats, adapting to changing network conditions, and performing risk-based prioritization for the mitigation of suspicious and malicious traffic. By integrating Agentic AI with Splunk, an established SIEM platform, we developed a unique threat hunting framework. The framework systematically and seamlessly integrates different threat hunting modules together, ranging from traffic ingestion to anomaly assessment using a reconstruction-based autoencoder, deep reinforcement learning (DRL) with two layers for initial triage, and a large language model (LLM) for contextual analysis. We evaluated the framework against a publicly available benchmark dataset, as well as against a simulated dataset. The experimental results show that the framework can effectively adapt to different SOC objectives autonomously and identify suspicious and malicious traffic. The framework enhances operational effectiveness by supporting SOC analysts in their decision-making to block, allow, or monitor network traffic. This study thus enhances cybersecurity and threat hunting literature by presenting the novel threat hunting framework for security decision- making, as well as promoting cumulative research efforts to develop more effective frameworks to battle continuously evolving cyber threats.

</details>


### 61. From AI Assistant to AI Scientist: Autonomous Discovery of LLM-RL Algorithms with LLM Agents

- **Authors:** Sirui Xia, Yikai Zhang, Aili Chen, Siye Wu, Siyu Yuan, Yanghua Xiao
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23951v1](http://arxiv.org/abs/2603.23951v1)
- **PDF:** [https://arxiv.org/pdf/2603.23951v1](https://arxiv.org/pdf/2603.23951v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Discovering improved policy optimization algorithms for language models remains a costly manual process requiring repeated mechanism-level modification and validation. Unlike simple combinatorial code search, this problem requires searching over algorithmic mechanisms tightly coupled with training dynamics while reusing empirical evidence across iterations. We propose POISE, a closed-loop framework for automated discovery of policy optimization algorithms for language models. POISE maintains a structured, genealogically linked archive linking proposals, executable implementations, standardized evaluations, and natural-language reflections to support evidence-driven iteration. In mathematical reasoning experiments starting from GRPO, POISE evaluates 64 candidate algorithms and discovers improved mechanisms, including analytic-variance scaling and validity masking. The best variant improves weighted Overall from 47.8 to 52.5 (+4.6) and increases AIME25 pass@32 from 26.7% to 43.3%, demonstrating the feasibility of automated policy optimization discovery while supporting interpretable design principles.

</details>


### 62. AnalogAgent: Self-Improving Analog Circuit Design Automation with LLM Agents

- **Authors:** Zhixuan Bao, Zhuoyi Lin, Jiageng Wang, Jinhai Hu, Yuan Gao, Yaoxin Wu, Xiaoli Li, Xun Xu
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23910v1](http://arxiv.org/abs/2603.23910v1)
- **PDF:** [https://arxiv.org/pdf/2603.23910v1](https://arxiv.org/pdf/2603.23910v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in large language models (LLMs) suggest strong potential for automating analog circuit design. Yet most LLM-based approaches rely on a single-model loop of generation, diagnosis, and correction, which favors succinct summaries over domain-specific insight and suffers from context attrition that erases critical technical details. To address these limitations, we propose AnalogAgent, a training-free agentic framework that integrates an LLM-based multi-agent system (MAS) with self-evolving memory (SEM) for analog circuit design automation. AnalogAgent coordinates a Code Generator, Design Optimizer, and Knowledge Curator to distill execution feedback into an adaptive playbook in SEM and retrieve targeted guidance for subsequent generation, enabling cross-task transfer without additional expert feedback, databases, or libraries. Across established benchmarks, AnalogAgent achieves 92% Pass@1 with Gemini and 97.4% Pass@1 with GPT-5. Moreover, with compact models (e.g., Qwen-8B), it yields a +48.8% average Pass@1 gain across tasks and reaches 72.1% Pass@1 overall, indicating that AnalogAgent substantially strengthens open-weight models for high-quality analog circuit design automation.

</details>


### 63. Sketch2Simulation: Automating Flowsheet Generation via Multi Agent Large Language Models

- **Authors:** Abdullah Bahamdan, Emma Pajak, John D. Hedengren, Antonio del Rio Chanona
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.24629v1](http://arxiv.org/abs/2603.24629v1)
- **PDF:** [https://arxiv.org/pdf/2603.24629v1](https://arxiv.org/pdf/2603.24629v1)
- **Categories:** cs.SE, cs.AI, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Converting process sketches into executable simulation models remains a major bottleneck in process systems engineering, requiring substantial manual effort and simulator-specific expertise. Recent advances in generative AI have improved both engineering-diagram interpretation and LLM-assisted flowsheet generation, but these remain largely disconnected: diagram-understanding methods often stop at extracted graphs, while text-to-simulation workflows assume structured inputs rather than raw visual artifacts. To bridge this gap, we present an end-to-end multi-agent large language model system that converts process diagrams directly into executable Aspen HYSYS flowsheets. The framework decomposes the task into three coordinated layers: diagram parsing and interpretation, simulation model synthesis, and multi-level validation. Specialized agents handle visual interpretation, graph-based intermediate representation construction, code generation for the HYSYS COM interface, execution, and structural verification. We evaluate the framework on four chemical engineering case studies of increasing complexity, from a simple desalting process to an industrial aromatic production flowsheet with multiple recycle loops. The system produces executable HYSYS models in all cases, achieving complete structural fidelity on the two simpler cases and strong performance on the more complex ones, with connection consistency above 0.93 and stream consistency above 0.96. These results demonstrate a viable end-to-end sketch-to-simulation workflow while highlighting remaining challenges in dense recycle structures, implicit diagram semantics, and simulator-interface constraints.

</details>


### 64. AgentChemist: A Multi-Agent Experimental Robotic Platform Integrating Chemical Perception and Precise Control

- **Authors:** Xiangyi Wei, Fei Wang, Haotian Zhang, Xin An, Haitian Zhu, Lianrui Hu, Yang Li, Changbo Wang, Xiao He
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23886v1](http://arxiv.org/abs/2603.23886v1)
- **PDF:** [https://arxiv.org/pdf/2603.23886v1](https://arxiv.org/pdf/2603.23886v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Chemical laboratory automation has long been constrained by rigid workflows and poor adaptability to the long-tail distribution of experimental tasks. While most automated platforms perform well on a narrow set of standardized procedures, real laboratories involve diverse, infrequent, and evolving operations that fall outside predefined protocols. This mismatch prevents existing systems from generalizing to novel reaction conditions, uncommon instrument configurations, and unexpected procedural variations. We present a multi-agent robotic platform designed to address this long-tail challenge through collaborative task decomposition, dynamic scheduling, and adaptive control. The system integrates chemical perception for real-time reaction monitoring with feedback-driven execution, enabling it to adjust actions based on evolving experimental states rather than fixed scripts. Validation via acid-base titration demonstrates autonomous progress tracking, adaptive dispensing control, and reliable end-to-end experiment execution. By improving generalization across diverse laboratory scenarios, this platform provides a practical pathway toward intelligent, flexible, and scalable laboratory automation.

</details>


### 65. Self-Evolving Multi-Agent Framework for Efficient Decision Making in Real-Time Strategy Scenarios

- **Authors:** Li Ma, Hao Peng, Yiming Wang, Hongbin Luo, Jie Liu, Kongjing Gu, Guanlin Wu, Hui Lin, Lei Ren
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23875v1](http://arxiv.org/abs/2603.23875v1)
- **PDF:** [https://arxiv.org/pdf/2603.23875v1](https://arxiv.org/pdf/2603.23875v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have demonstrated exceptional potential in complex reasoning,pioneering a new paradigm for autonomous agent decision making in dynamic settings. However, in Real-Time Strategy (RTS) scenarios, LLMs suffer from a critical speed-quality trade-off. Specifically expansive state spaces and time limits render inference delays prohibitive, while stochastic planning errors undermine logical consistency. To address these challenges, we present SEMA (Self-Evolving Multi-Agent), a novel framework designed for high-performance, low-latency decision-making in RTS environments. This collaborative multi-agent framework facilitates self-evolution by adaptively calibrating model bias through in-episode assessment and cross-episode analysis. We further incorporate dynamic observation pruning based on structural entropy to model game states topologically. By distilling high dimensional data into core semantic information, this approach significantly reduces inference time. We also develop a hybrid knowledge-memory mechanism that integrates micro-trajectories, macro-experience, and hierarchical domain knowledge, thereby enhancing both strategic adaptability and decision consistency. Experiments across multiple StarCraft II maps demonstrate that SEMA achieves superior win rates while reducing average decision latency by over 50%, validating its efficiency and robustness in complex RTS scenarios.

</details>


### 66. BeliefShift: Benchmarking Temporal Belief Consistency and Opinion Drift in LLM Agents

- **Authors:** Praveen Kumar Myakala, Manan Agrawal, Rahul Manche
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23848v1](http://arxiv.org/abs/2603.23848v1)
- **PDF:** [https://arxiv.org/pdf/2603.23848v1](https://arxiv.org/pdf/2603.23848v1)
- **Categories:** cs.CL, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLMs are increasingly used as long-running conversational agents, yet every major benchmark evaluating their memory treats user information as static facts to be stored and retrieved. That's the wrong model. People change their minds, and over extended interactions, phenomena like opinion drift, over-alignment, and confirmation bias start to matter a lot.
  BeliefShift introduces a longitudinal benchmark designed specifically to evaluate belief dynamics in multi-session LLM interactions. It covers three tracks: Temporal Belief Consistency, Contradiction Detection, and Evidence-Driven Revision. The dataset includes 2,400 human-annotated multi-session interaction trajectories spanning health, politics, personal values, and product preferences.
  We evaluate seven models including GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, LLaMA-3, and Mistral-Large under zero-shot and retrieval-augmented generation (RAG) settings. Results reveal a clear trade-off: models that personalize aggressively resist drift poorly, while factually grounded models miss legitimate belief updates.
  We further introduce four novel evaluation metrics: Belief Revision Accuracy (BRA), Drift Coherence Score (DCS), Contradiction Resolution Rate (CRR), and Evidence Sensitivity Index (ESI).

</details>


### 67. Learning-guided Prioritized Planning for Lifelong Multi-Agent Path Finding in Warehouse Automation

- **Authors:** Han Zheng, Yining Ma, Brandon Araki, Jingkai Chen, Cathy Wu
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23838v1](http://arxiv.org/abs/2603.23838v1)
- **PDF:** [https://arxiv.org/pdf/2603.23838v1](https://arxiv.org/pdf/2603.23838v1)
- **Categories:** cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Lifelong Multi-Agent Path Finding (MAPF) is critical for modern warehouse automation, which requires multiple robots to continuously navigate conflict-free paths to optimize the overall system throughput. However, the complexity of warehouse environments and the long-term dynamics of lifelong MAPF often demand costly adaptations to classical search-based solvers. While machine learning methods have been explored, their superiority over search-based methods remains inconclusive. In this paper, we introduce Reinforcement Learning (RL) guided Rolling Horizon Prioritized Planning (RL-RH-PP), the first framework integrating RL with search-based planning for lifelong MAPF. Specifically, we leverage classical Prioritized Planning (PP) as a backbone for its simplicity and flexibility in integrating with a learning-based priority assignment policy. By formulating dynamic priority assignment as a Partially Observable Markov Decision Process (POMDP), RL-RH-PP exploits the sequential decision-making nature of lifelong planning while delegating complex spatial-temporal interactions among agents to reinforcement learning. An attention-based neural network autoregressively decodes priority orders on-the-fly, enabling efficient sequential single-agent planning by the PP planner. Evaluations in realistic warehouse simulations show that RL-RH-PP achieves the highest total throughput among baselines and generalizes effectively across agent densities, planning horizons, and warehouse layouts. Our interpretive analyses reveal that RL-RH-PP proactively prioritizes congested agents and strategically redirects agents from congestion, easing traffic flow and boosting throughput. These findings highlight the potential of learning-guided approaches to augment traditional heuristics in modern warehouse automation.

</details>


### 68. Willful Disobedience: Automatically Detecting Failures in Agentic Traces

- **Authors:** Reshabh K Sharma, Shraddha Barke, Benjamin Zorn
- **Published:** 2026-03-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23806v1](http://arxiv.org/abs/2603.23806v1)
- **PDF:** [https://arxiv.org/pdf/2603.23806v1](https://arxiv.org/pdf/2603.23806v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly embedded in real software systems, where they execute multi-step workflows through multi-turn dialogue, tool invocations, and intermediate decisions. These long execution histories, called agentic traces, make validation difficult. Outcome-only benchmarks can miss critical procedural failures, such as incorrect workflow routing, unsafe tool usage, or violations of prompt-specified rules. This paper presents AgentPex, an AI-powered tool designed to systematically evaluate agentic traces. AgentPex extracts behavioral rules from agent prompts and system instructions, then uses these specifications to automatically evaluate traces for compliance. We evaluate AgentPex on 424 traces from τ2-bench across models in telecom, retail, and airline customer service. Our results show that AgentPex distinguishes agent behavior across models and surfaces specification violations that are not captured by outcome-only scoring. It also provides fine-grained analysis by domain and metric, enabling developers to understand agent strengths and weaknesses at scale.

</details>


### 69. The Cognitive Firewall:Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense

- **Authors:** Qianlong Lan, Anuj Kaul
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23791v1](http://arxiv.org/abs/2603.23791v1)
- **PDF:** [https://arxiv.org/pdf/2603.23791v1](https://arxiv.org/pdf/2603.23791v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deploying large language models (LLMs) as autonomous browser agents exposes a significant attack surface in the form of Indirect Prompt Injection (IPI). Cloud-based defenses can provide strong semantic analysis, but they introduce latency and raise privacy concerns. We present the Cognitive Firewall, a three-stage split-compute architecture that distributes security checks across the client and the cloud. The system consists of a local visual Sentinel, a cloud-based Deep Planner, and a deterministic Guard that enforces execution-time policies. Across 1,000 adversarial samples, edge-only defenses fail to detect 86.9% of semantic attacks. In contrast, the full hybrid architecture reduces the overall attack success rate (ASR) to below 1% (0.88% under static evaluation and 0.67% under adaptive evaluation), while maintaining deterministic constraints on side-effecting actions. By filtering presentation-layer attacks locally, the system avoids unnecessary cloud inference and achieves an approximately 17,000x latency advantage over cloud-only baselines. These results indicate that deterministic enforcement at the execution boundary can complement probabilistic language models, and that split-compute provides a practical foundation for securing interactive LLM agents.

</details>


### 70. Efficient Benchmarking of AI Agents

- **Authors:** Franck Ndzomga
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23749v1](http://arxiv.org/abs/2603.23749v1)
- **PDF:** [https://arxiv.org/pdf/2603.23749v1](https://arxiv.org/pdf/2603.23749v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluating AI agents on comprehensive benchmarks is expensive because each evaluation requires interactive rollouts with tool use and multi-step reasoning. We study whether small task subsets can preserve agent rankings at substantially lower cost. Unlike static language model benchmarks, agent evaluation is subject to scaffold-driven distribution shift, since performance depends on the framework wrapping the underlying model. Across eight benchmarks, 33 agent scaffolds, and 70+ model configurations, we find that absolute score prediction degrades under this shift, while rank-order prediction remains stable. Exploiting this asymmetry, we propose a simple optimization-free protocol: evaluate new agents only on tasks with intermediate historical pass rates (30-70%). This mid-range difficulty filter, motivated by Item Response Theory, reduces the number of evaluation tasks by 44-70% while maintaining high rank fidelity under scaffold and temporal shifts. It provides more reliable rankings than random sampling, which exhibits high variance across seeds, and outperforms greedy task selection under distribution shift. These results suggest that reliable leaderboard ranking does not require full-benchmark evaluation.

</details>


### 71. Dual-Gated Epistemic Time-Dilation: Autonomous Compute Modulation in Asynchronous MARL

- **Authors:** Igor Jankowski
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23722v1](http://arxiv.org/abs/2603.23722v1)
- **PDF:** [https://arxiv.org/pdf/2603.23722v1](https://arxiv.org/pdf/2603.23722v1)
- **Categories:** cs.MA, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

While Multi-Agent Reinforcement Learning (MARL) algorithms achieve unprecedented successes across complex continuous domains, their standard deployment strictly adheres to a synchronous operational paradigm. Under this paradigm, agents are universally forced to execute deep neural network inferences at every micro-frame, regardless of immediate necessity. This dense throughput acts as a fundamental barrier to physical deployment on edge-devices where thermal and metabolic budgets are highly constrained. We propose Epistemic Time-Dilation MAPPO (ETD-MAPPO), augmented with a Dual-Gated Epistemic Trigger. Instead of depending on rigid frame-skipping (macro-actions), agents autonomously modulate their execution frequency by interpreting aleatoric uncertainty (via Shannon entropy of their policy) and epistemic uncertainty (via state-value divergence in a Twin-Critic architecture). To format this, we structure the environment as a Semi-Markov Decision Process (SMDP) and build the SMDP-Aligned Asynchronous Gradient Masking Critic to ensure proper credit assignment. Empirical findings demonstrate massive improvements (> 60% relative baseline acquisition leaps) over current temporal models. By assessing LBF, MPE, and the 115-dimensional state space of Google Research Football (GRF), ETD correctly prevented premature policy collapse. Remarkably, this unconstrained approach leads to emergent Temporal Role Specialization, reducing computational overhead by a statistically dominant 73.6% entirely during off-ball execution without deteriorating centralized task dominance.

</details>


### 72. GTO Wizard Benchmark

- **Authors:** Marc-Antoine Provost, Nejc Ilenic, Christopher Solinas, Philippe Beardsell
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23660v1](http://arxiv.org/abs/2603.23660v1)
- **PDF:** [https://arxiv.org/pdf/2603.23660v1](https://arxiv.org/pdf/2603.23660v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce GTO Wizard Benchmark, a public API and standardized evaluation framework for benchmarking algorithms in Heads-Up No-Limit Texas Hold'em (HUNL). The benchmark evaluates agents against GTO Wizard AI, a state-of-the-art superhuman poker agent that approximates Nash Equilibria, and defeated Slumbot, the 2018 Annual Computer Poker Competition champion and previous strongest publicly accessible HUNL benchmark, by $19.4$ $\pm$ $4.1$ bb/100. Variance is a fundamental challenge in poker evaluation; we address this by integrating AIVAT, a provably unbiased variance reduction technique that achieves equivalent statistical significance with ten times fewer hands than naive Monte Carlo evaluation. We conduct a comprehensive benchmarking study of state-of-the-art large language models under zero-shot conditions, including GPT-5.4, Claude Opus 4.6, Gemini 3.1 Pro, Grok 4, and others. Initial results and analysis reveal dramatic progress in LLM reasoning over recent years, yet all models remain far below the baseline established by our benchmark. Qualitative analysis reveals clear opportunities for improvement, including representation and the ability to reason over hidden states. This benchmark provides researchers with a precise and quantifiable setting to evaluate advances in planning and reasoning in multi-agent systems with partial observability.

</details>


### 73. Can LLM Agents Be CFOs? A Benchmark for Resource Allocation in Dynamic Enterprise Environments

- **Authors:** Yi Han, Lingfei Qian, Yan Wang, Yueru He, Xueqing Peng, Dongji Feng, Yankai Chen, Haohang Li, Yupeng Cao, Jimin Huang, Xue Liu, Jian-Yun Nie, Sophia Ananiadou
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23638v1](http://arxiv.org/abs/2603.23638v1)
- **PDF:** [https://arxiv.org/pdf/2603.23638v1](https://arxiv.org/pdf/2603.23638v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have enabled agentic systems that can reason, plan, and act across complex tasks, but it remains unclear whether they can allocate resources effectively under uncertainty. Unlike short-horizon reactive decisions, allocation requires committing scarce resources over time while balancing competing objectives and preserving flexibility for future needs. We introduce EnterpriseArena, the first benchmark for evaluating agents on long-horizon enterprise resource allocation. It instantiates CFO-style decision-making in a 132-month enterprise simulator combining firm-level financial data, anonymized business documents, macroeconomic and industry signals, and expert-validated operating rules. The environment is partially observable and reveals the state only through budgeted organizational tools, forcing agents to trade off information acquisition against conserving scarce resources. Experiments on eleven advanced LLMs show that this setting remains highly challenging: only 16% of runs survive the full horizon, and larger models do not reliably outperform smaller ones. These results identify long-horizon resource allocation under uncertainty as a distinct capability gap for current LLM agents.

</details>


### 74. Evaluating a Multi-Agent Voice-Enabled Smart Speaker for Care Homes: A Safety-Focused Framework

- **Authors:** Zeinab Dehghani, Rameez Raja Kureshi, Koorosh Aslansefat, Faezeh Alsadat Abedi, Dhavalkumar Thakker, Lisa Greaves, Bhupesh Kumar Mishra, Baseer Ahmad, Tanaya Maslekar
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23625v1](http://arxiv.org/abs/2603.23625v1)
- **PDF:** [https://arxiv.org/pdf/2603.23625v1](https://arxiv.org/pdf/2603.23625v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Artificial intelligence (AI) is increasingly being explored in health and social care to reduce administrative workload and allow staff to spend more time on patient care. This paper evaluates a voice-enabled Care Home Smart Speaker designed to support everyday activities in residential care homes, including spoken access to resident records, reminders, and scheduling tasks. A safety-focused evaluation framework is presented that examines the system end-to-end, combining Whisper-based speech recognition with retrieval-augmented generation (RAG) approaches (hybrid, sparse, and dense). Using supervised care-home trials and controlled testing, we evaluated 330 spoken transcripts across 11 care categories, including 184 reminder-containing interactions. These evaluations focus on (i) correct identification of residents and care categories, (ii) reminder recognition and extraction, and (iii) end-to-end scheduling correctness under uncertainty (including safe deferral/clarification). Given the safety-critical nature of care homes, particular attention is also paid to reliability in noisy environments and across diverse accents, supported by confidence scoring, clarification prompts, and human-in-the-loop oversight. In the best-performing configuration (GPT-5.2), resident ID and care category matching reached 100% (95% CI: 98.86-100), while reminder recognition reached 89.09\% (95% CI: 83.81-92.80) with zero missed reminders (100% recall) but some false positives. End-to-end scheduling via calendar integration achieved 84.65% exact reminder-count agreement (95% CI: 78.00-89.56), indicating remaining edge cases in converting informal spoken instructions into actionable events. The findings suggest that voice-enabled systems, when carefully evaluated and appropriately safeguarded, can support accurate documentation, effective task management, and trustworthy use of AI in care home settings.

</details>


### 75. Code Review Agent Benchmark

- **Authors:** Yuntong Zhang, Zhiyuan Pan, Imam Nur Bani Yusuf, Haifeng Ruan, Ridwan Shariffdeen, Abhik Roychoudhury
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23448v1](http://arxiv.org/abs/2603.23448v1)
- **PDF:** [https://arxiv.org/pdf/2603.23448v1](https://arxiv.org/pdf/2603.23448v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Software engineering agents have shown significant promise in writing code. As AI agents permeate code writing, and generate huge volumes of code automatically -- the matter of code quality comes front and centre. As the automatically generated code gets integrated into huge code-bases -- the issue of code review and broadly quality assurance becomes important. In this paper, we take a fresh look at the problem and curate a code review dataset for AI agents to work with. Our dataset called c-CRAB (pronounced see-crab) can evaluate agents for code review tasks. Specifically given a pull-request (which could be coming from code generation agents or humans), if a code review agent produces a review, our evaluation framework can asses the reviewing capability of the code review agents. Our evaluation framework is used to evaluate the state of the art today -- the open-source PR-agent, as well as commercial code review agents from Devin, Claude Code, and Codex.
  Our c-CRAB dataset is systematically constructed from human reviews -- given a human review of a pull request instance we generate corresponding tests to evaluate the code review agent generated reviews. Such a benchmark construction gives us several insights. Firstly, the existing review agents taken together can solve only around 40% of the c-CRAB tasks, indicating the potential to close this gap by future research. Secondly, we observe that the agent reviews often consider different aspects from the human reviews -- indicating the potential for human-agent collaboration for code review that could be deployed in future software teams. Last but not the least, the agent generated tests from our data-set act as a held out test-suite and hence quality gate for agent generated reviews. What this will mean for future collaboration of code generation agents, test generation agents and code review agents -- remains to be investigated.

</details>


### 76. Mecha-nudges for Machines

- **Authors:** Giulio Frey, Kawin Ethayarajh
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23433v1](http://arxiv.org/abs/2603.23433v1)
- **PDF:** [https://arxiv.org/pdf/2603.23433v1](https://arxiv.org/pdf/2603.23433v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Nudges are subtle changes to the way choices are presented to human decision-makers (e.g., opt-in vs. opt-out by default) that shift behavior without restricting options or changing incentives. As AI agents increasingly make decisions in the same environments as humans, the presentation of choices may be optimized for machines as well as people. We introduce mecha-nudges: changes to how choices are presented that systematically influence AI agents without degrading the decision environment for humans. To formalize mecha-nudges, we combine the Bayesian persuasion framework with V-usable information, a generalization of Shannon information that is observer-relative. This yields a common scale (bits of usable information) for comparing a wide range of interventions, contexts, and models. Applying our framework to product listings on Etsy -- a global marketplace for independent sellers -- we find that following ChatGPT's release, listings have significantly more machine-usable information about product selection, consistent with systematic mecha-nudging.

</details>


### 77. Biased Error Attribution in Multi-Agent Human-AI Systems Under Delayed Feedback

- **Authors:** Teerthaa Parakh, Karen M. Feigh
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23419v1](http://arxiv.org/abs/2603.23419v1)
- **PDF:** [https://arxiv.org/pdf/2603.23419v1](https://arxiv.org/pdf/2603.23419v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Human decision-making is strongly influenced by cognitive biases, particularly under conditions of uncertainty and risk. While prior work has examined bias in single-step decisions with immediate outcomes and in human interaction with a single autonomous agent, comparatively little attention has been paid to decision-making under delayed outcomes involving multiple AI agents, where decisions at each step affect subsequent states. In this work, we study how delayed outcomes shape decision-making and responsibility attribution in a multi-agent human-AI task. Using a controlled game-based experiment, we analyze how participants adjust their behavior following positive and negative outcomes. We observe asymmetric responses to gains and losses, with stronger corrective adjustments after negative outcomes. Importantly, participants often fail to correctly identify the actions that caused failure and misattribute responsibility across AI agents, leading to systematic revisions of decisions that are weakly related to the underlying causes of poor performance. We refer to this phenomenon as a form of attribution bias, manifested as biased error attribution under delayed feedback. Our findings highlight how cognitive biases can be amplified in human-AI systems with delayed outcomes and multiple autonomous agents, underscoring the need for decision-support systems that better support causal understanding and learning over time.

</details>


### 78. Planning over MAPF Agent Dependencies via Multi-Dependency PIBT

- **Authors:** Zixiang Jiang, Yulun Zhang, Rishi Veerapaneni, Jiaoyang Li
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23405v1](http://arxiv.org/abs/2603.23405v1)
- **PDF:** [https://arxiv.org/pdf/2603.23405v1](https://arxiv.org/pdf/2603.23405v1)
- **Categories:** cs.MA, cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern Multi-Agent Path Finding (MAPF) algorithms must plan for hundreds to thousands of agents in congested environments within a second, requiring highly efficient algorithms. Priority Inheritance with Backtracking (PIBT) is a popular algorithm capable of effectively planning in such situations. However, PIBT is constrained by its rule-based planning procedure and lacks generality because it restricts its search to paths that conflict with at most one other agent. This limitation also applies to Enhanced PIBT (EPIBT), a recent extension of PIBT. In this paper, we describe a new perspective on solving MAPF by planning over agent dependencies. Taking inspiration from PIBT's priority inheritance logic, we define the concept of agent dependencies and propose Multi-Dependency PIBT (MD-PIBT) that searches over agent dependencies. MD-PIBT is a general framework where specific parameterizations can reproduce PIBT and EPIBT. At the same time, alternative configurations yield novel planning strategies that are not expressible by PIBT or EPIBT. Our experiments demonstrate that MD-PIBT effectively plans for as many as 10,000 homogeneous agents under various kinodynamic constraints, including pebble motion, rotation motion, and differential drive robots with speed and acceleration limits. We perform thorough evaluations on different variants of MAPF and find that MD-PIBT is particularly effective in MAPF with large agents.

</details>


### 79. Designing Agentic AI-Based Screening for Portfolio Investment

- **Authors:** Mehmet Caner, Agostino Capponi, Nathan Sun, Jonathan Y. Tan
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23300v1](http://arxiv.org/abs/2603.23300v1)
- **PDF:** [https://arxiv.org/pdf/2603.23300v1](https://arxiv.org/pdf/2603.23300v1)
- **Categories:** q-fin.PM, cs.AI, cs.MA, q-fin.ST


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce a new agentic artificial intelligence (AI) platform for portfolio management. Our architecture consists of three layers. First, two large language model (LLM) agents are assigned specialized tasks: one agent screens for firms with desirable fundamentals, while a sentiment analysis agent screens for firms with desirable news. Second, these agents deliberate to generate and agree upon buy and sell signals from a large portfolio, substantially narrowing the pool of candidate assets. Finally, we apply a high-dimensional precision matrix estimation procedure to determine optimal portfolio weights. A defining theoretical feature of our framework is that the number of assets in the portfolio is itself a random variable, realized through the screening process. We introduce the concept of sensible screening and establish that, under mild screening errors, the squared Sharpe ratio of the screened portfolio consistently estimates its target. Empirically, our method achieves superior Sharpe ratios relative to an unscreened baseline portfolio and to conventional screening approaches, evaluated on S&P 500 data over the period 2020--2024.

</details>


### 80. Emergence of Fragility in LLM-based Social Networks: the Case of Moltbook

- **Authors:** Luca Sodano, Sofia Sciangula, Amulya Galmarini, Francesco Bertolotti
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23279v1](http://arxiv.org/abs/2603.23279v1)
- **PDF:** [https://arxiv.org/pdf/2603.23279v1](https://arxiv.org/pdf/2603.23279v1)
- **Categories:** cs.SI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid diffusion of large language models and the growth in their capability has enabled the emergence of online environments populated by autonomous AI agents that interact through natural language. These platforms provide a novel empirical setting for studying collective dynamics among artificial agents. In this paper we analyze the interaction network of Moltbook, a social platform composed entirely of LLM based agents, using tools from network science. The dataset comprises 39,924 users, 235,572 posts, and 1,540,238 comments collected through web scraping. We construct a directed weighted network in which nodes represent agents and edges represent commenting interactions. Our analysis reveals strongly heterogeneous connectivity patterns characterized by heavy tailed degree and activity distributions. At the mesoscale, the network exhibits a pronounced core periphery organization in which a very small structural core (0.9% of nodes) concentrates a large fraction of connectivity. Robustness experiments show that the network is relatively resilient to random node removal but highly vulnerable to targeted attacks on highly connected nodes, particularly those with high out degree. These findings indicate that the interaction structure of AI agent social systems may develop strong centralization and structural fragility, providing new insights into the collective organization of LLM native social environments.

</details>


### 81. A Multimodal Framework for Human-Multi-Agent Interaction

- **Authors:** Shaid Hasan, Breenice Lee, Sujan Sarker, Tariq Iqbal
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23271v1](http://arxiv.org/abs/2603.23271v1)
- **PDF:** [https://arxiv.org/pdf/2603.23271v1](https://arxiv.org/pdf/2603.23271v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Human-robot interaction is increasingly moving toward multi-robot, socially grounded environments. Existing systems struggle to integrate multimodal perception, embodied expression, and coordinated decision-making in a unified framework. This limits natural and scalable interaction in shared physical spaces. We address this gap by introducing a multimodal framework for human-multi-agent interaction in which each robot operates as an autonomous cognitive agent with integrated multimodal perception and Large Language Model (LLM)-driven planning grounded in embodiment. At the team level, a centralized coordination mechanism regulates turn-taking and agent participation to prevent overlapping speech and conflicting actions. Implemented on two humanoid robots, our framework enables coherent multi-agent interaction through interaction policies that combine speech, gesture, gaze, and locomotion. Representative interaction runs demonstrate coordinated multimodal reasoning across agents and grounded embodied responses. Future work will focus on larger-scale user studies and deeper exploration of socially grounded multi-agent interaction dynamics.

</details>


### 82. Polaris: A Gödel Agent Framework for Small Language Models through Experience-Abstracted Policy Repair

- **Authors:** Aditya Kakade, Vivek Srivastava, Shirish Karande
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23129v1](http://arxiv.org/abs/2603.23129v1)
- **PDF:** [https://arxiv.org/pdf/2603.23129v1](https://arxiv.org/pdf/2603.23129v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Gödel agent realize recursive self-improvement: an agent inspects its own policy and traces and then modifies that policy in a tested loop. We introduce Polaris, a Gödel agent for compact models that performs policy repair via experience abstraction, turning failures into policy updates through a structured cycle of analysis, strategy formation, abstraction, and minimal code pat ch repair with conservative checks. Unlike response level self correction or parameter tuning, Polaris makes policy level changes with small, auditable patches that persist in the policy and are reused on unseen instances within each benchmark. As part of the loop, the agent engages in meta reasoning: it explains its errors, proposes concrete revisions to its own policy, and then updates the policy. To enable cumulative policy refinement, we introduce experience abstraction, which distills failures into compact, reusable strategies that transfer to unseen instances. On MGSM, DROP, GPQA, and LitBench (covering arithmetic reasoning, compositional inference, graduate-level problem solving, and creative writing evaluation), a 7-billion-parameter model equipped with Polaris achieves consistent gains over the base policy and competitive baselines.

</details>


### 83. Mind Your HEARTBEAT! Claw Background Execution Inherently Enables Silent Memory Pollution

- **Authors:** Yechao Zhang, Shiqian Zhao, Jie Zhang, Gelei Deng, Jiawen Zhang, Xiaogeng Liu, Chaowei Xiao, Tianwei Zhang
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23064v2](http://arxiv.org/abs/2603.23064v2)
- **PDF:** [https://arxiv.org/pdf/2603.23064v2](https://arxiv.org/pdf/2603.23064v2)
- **Categories:** cs.CR, cs.AI, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We identify a critical security vulnerability in mainstream Claw personal AI agents: untrusted content encountered during heartbeat-driven background execution can silently pollute agent memory and subsequently influence user-facing behavior without the user's awareness. This vulnerability arises from an architectural design shared across the Claw ecosystem: heartbeat background execution runs in the same session as user-facing conversation, so content ingested from any external source monitored in the background (including email, message channels, news feeds, code repositories, and social platforms) can enter the same memory context used for foreground interaction, often with limited user visibility and without clear source provenance. We formalize this process as an Exposure (E) $\rightarrow$ Memory (M) $\rightarrow$ Behavior (B) pathway: misinformation encountered during heartbeat execution enters the agent's short-term session context, potentially gets written into long-term memory, and later shapes downstream user-facing behavior. We instantiate this pathway in an agent-native social setting using MissClaw, a controlled research replica of Moltbook. We find that (1) social credibility cues, especially perceived consensus, are the dominant driver of short-term behavioral influence, with misleading rates up to 61%; (2) routine memory-saving behavior can promote short-term pollution into durable long-term memory at rates up to 91%, with cross-session behavioral influence reaching 76%; (3) under naturalistic browsing with content dilution and context pruning, pollution still crosses session boundaries. Overall, prompt injection is not required: ordinary social misinformation is sufficient to silently shape agent memory and behavior under heartbeat-driven background execution.

</details>


### 84. Minibal: Balanced Game-Playing Without Opponent Modeling

- **Authors:** Quentin Cohen-Solal, Tristan Cazenave
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23059v1](http://arxiv.org/abs/2603.23059v1)
- **PDF:** [https://arxiv.org/pdf/2603.23059v1](https://arxiv.org/pdf/2603.23059v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in game AI, such as AlphaZero and Athénan, have achieved superhuman performance across a wide range of board games. While highly powerful, these agents are ill-suited for human-AI interaction, as they consistently overwhelm human players, offering little enjoyment and limited educational value. This paper addresses the problem of balanced play, in which an agent challenges its opponent without either dominating or conceding.
  We introduce Minibal (Minimize & Balance), a variant of Minimax specifically designed for balanced play. Building on this concept, we propose several modifications of the Unbounded Minimax algorithm explicitly aimed at discovering balanced strategies.
  Experiments conducted across seven board games demonstrate that one variant consistently achieves the most balanced play, with average outcomes close to perfect balance. These results establish Minibal as a promising foundation for designing AI agents that are both challenging and engaging, suitable for both entertainment and serious games.

</details>


### 85. Knowledge Access Beats Model Size: Memory Augmented Routing for Persistent AI Agents

- **Authors:** Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.23013v1](http://arxiv.org/abs/2603.23013v1)
- **PDF:** [https://arxiv.org/pdf/2603.23013v1](https://arxiv.org/pdf/2603.23013v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Production AI agents frequently receive user-specific queries that are highly repetitive, with up to 47\% being semantically similar to prior interactions, yet each query is typically processed with the same computational cost. We argue that this redundancy can be exploited through conversational memory, transforming repetition from a cost burden into an efficiency advantage. We propose a memory-augmented inference framework in which a lightweight 8B-parameter model leverages retrieved conversational context to answer all queries via a low-cost inference path. Without any additional training or labeled data, this approach achieves 30.5\% F1, recovering 69\% of the performance of a full-context 235B model while reducing effective cost by 96\%. Notably, a 235B model without memory (13.7\% F1) underperforms even the standalone 8B model (15.4\% F1), indicating that for user-specific queries, access to relevant knowledge outweighs model scale. We further analyze the role of routing and confidence. At practical confidence thresholds, routing alone already directs 96\% of queries to the small model, but yields poor accuracy (13.0\% F1) due to confident hallucinations. Memory does not substantially alter routing decisions; instead, it improves correctness by grounding responses in retrieved user-specific information. As conversational memory accumulates over time, coverage of recurring topics increases, further narrowing the performance gap. We evaluate on 152 LoCoMo questions (Qwen3-8B/235B) and 500 LongMemEval questions. Incorporating hybrid retrieval (BM25 + cosine similarity) improves performance by an additional +7.7 F1, demonstrating that retrieval quality directly enhances end-to-end system performance. Overall, our results highlight that memory, rather than model size, is the primary driver of accuracy and efficiency in persistent AI agents.

</details>


### 86. PaperVoyager : Building Interactive Web with Visual Language Models

- **Authors:** Dasen Dai, Biao Wu, Meng Fang, Wenhao Wang
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22999v1](http://arxiv.org/abs/2603.22999v1)
- **PDF:** [https://arxiv.org/pdf/2603.22999v1](https://arxiv.org/pdf/2603.22999v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in visual language models have enabled autonomous agents for complex reasoning, tool use, and document understanding. However, existing document agents mainly transform papers into static artifacts such as summaries, webpages, or slides, which are insufficient for technical papers involving dynamic mechanisms and state transitions. In this work, we propose a Paper-to-Interactive-System Agent that converts research papers into executable interactive web systems. Given a PDF paper, the agent performs end-to-end processing without human intervention, including paper understanding, system modeling, and interactive webpage synthesis, enabling users to manipulate inputs and observe dynamic behaviors. To evaluate this task, we introduce a benchmark of 19 research papers paired with expert-built interactive systems as ground truth. We further propose PaperVoyager, a structured generation framework that explicitly models mechanisms and interaction logic during synthesis. Experiments show that PaperVoyager significantly improves the quality of generated interactive systems, offering a new paradigm for interactive scientific paper understanding.

</details>


### 87. Privacy-Preserving EHR Data Transformation via Geometric Operators: A Human-AI Co-Design Technical Report

- **Authors:** Maolin Wang, Beining Bao, Gan Yuan, Hongyu Chen, Bingkun Zhao, Baoshuo Kan, Jiming Xu, Qi Shi, Yinggong Zhao, Yao Wang, Wei Ying Ma, Jun Yan
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22954v1](http://arxiv.org/abs/2603.22954v1)
- **PDF:** [https://arxiv.org/pdf/2603.22954v1](https://arxiv.org/pdf/2603.22954v1)
- **Categories:** cs.CR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Electronic health records (EHRs) and other real-world clinical data are essential for clinical research, medical artificial intelligence, and life science, but their sharing is severely limited by privacy, governance, and interoperability constraints. These barriers create persistent data silos that hinder multi-center studies, large-scale model development, and broader biomedical discovery. Existing privacy-preserving approaches, including multi-party computation and related cryptographic techniques, provide strong protection but often introduce substantial computational overhead, reducing the efficiency of large-scale machine learning and foundation-model training. In addition, many such methods make data usable for restricted computation while leaving them effectively invisible to clinicians and researchers, limiting their value in workflows that still require direct inspection, exploratory analysis, and human interpretation. We propose a real-world-data transformation framework for privacy-preserving sharing of structured clinical records. Instead of converting data into opaque representations, our approach constructs transformed numeric views that preserve medical semantics and major statistical properties while, under a clearly specified threat model, provably breaking direct linkage between those views and protected patient-level attributes. Through collaboration between computer scientists and the AI agent \textbf{SciencePal}, acting as a constrained tool inventor under human guidance, we design three transformation operators that are non-reversible within this threat model, together with an additional mixing strategy for high-risk scenarios, supported by theoretical analysis and empirical evaluation under reconstruction, record linkage, membership inference, and attribute inference attacks.

</details>


### 88. Agent-Sentry: Bounding LLM Agents via Execution Provenance

- **Authors:** Rohan Sequeira, Stavros Damianakis, Umar Iqbal, Konstantinos Psounis
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22868v1](http://arxiv.org/abs/2603.22868v1)
- **PDF:** [https://arxiv.org/pdf/2603.22868v1](https://arxiv.org/pdf/2603.22868v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic computing systems, which autonomously spawn new functionalities based on natural language instructions, are becoming increasingly prevalent. While immensely capable, these systems raise serious security, privacy, and safety concerns. Fundamentally, the full set of functionalities offered by these systems, combined with their probabilistic execution flows, is not known beforehand. Given this lack of characterization, it is non-trivial to validate whether a system has successfully carried out the user's intended task or instead executed irrelevant actions, potentially as a consequence of compromise. In this paper, we propose Agent-Sentry, a framework that attempts to bound agentic systems to address this problem. Our key insight is that agentic systems are designed for specific use cases and therefore need not expose unbounded or unspecified functionalities. Once bounded, these systems become easier to scrutinize. Agent-Sentry operationalizes this insight by uncovering frequent functionalities offered by an agentic system, along with their execution traces, to construct behavioral bounds. It then learns a policy from these traces and blocks tool calls that deviate from learned behaviors or that misalign with user intent. Our evaluation shows that Agent-Sentry helps prevent over 90\% of attacks that attempt to trigger out-of-bounds executions, while preserving up to 98\% of system utility.

</details>


### 89. The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration

- **Authors:** Haoyuan Xu, Chang Li, Xinyan Ma, Xianhao Ou, Zihan Zhang, Tao He, Xiangyu Liu, Zixiang Wang, Jiafeng Liang, Zheng Chu, Runxuan Liu, Rongchuan Mu, Ming Liu, Bing Qin
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22862v1](http://arxiv.org/abs/2603.22862v1)
- **PDF:** [https://arxiv.org/pdf/2603.22862v1](https://arxiv.org/pdf/2603.22862v1)
- **Categories:** cs.SE, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool use enables large language models (LLMs) to access external information, invoke software systems, and act in digital environments beyond what can be solved from model parameters alone. Early research mainly studied whether a model could select and execute a correct single tool call. As agent systems evolve, however, the central problem has shifted from isolated invocation to multi-tool orchestration over long trajectories with intermediate state, execution feedback, changing environments, and practical constraints such as safety, cost, and verifiability. We comprehensively review recent progress in multi-tool LLM agents and analyzes the state of the art in this rapidly developing area. First, we unify task formulations and distinguish single-call tool use from long-horizon orchestration. Then, we organize the literature around six core dimensions: inference-time planning and execution, training and trajectory construction, safety and control, efficiency under resource constraints, capability completeness in open environments, and benchmark design and evaluation. We further summarize representative applications in software engineering, enterprise workflows, graphical user interfaces, and mobile systems. Finally, we discuss major challenges and outline future directions for building reliable, scalable, and verifiable multi-tool agents.

</details>


### 90. Agent Audit: A Security Analysis System for LLM Agent Applications

- **Authors:** Haiyue Zhang, Yi Nian, Yue Zhao
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22853v1](http://arxiv.org/abs/2603.22853v1)
- **PDF:** [https://arxiv.org/pdf/2603.22853v1](https://arxiv.org/pdf/2603.22853v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

What should a developer inspect before deploying an LLM agent: the model, the tool code, the deployment configuration, or all three? In practice, many security failures in agent systems arise not from model weights alone, but from the surrounding software stack: tool functions that pass untrusted inputs to dangerous operations, exposed credentials in deployment artifacts, and over-privileged Model Context Protocol (MCP) configurations.
  We present Agent Audit, a security analysis system for LLM agent applications. Agent Audit analyzes Python agent code and deployment artifacts through an agent-aware pipeline that combines dataflow analysis, credential detection, structured configuration parsing, and privilege-risk checks. The system reports findings in terminal, JSON, and SARIF formats, enabling direct integration with local development workflows and CI/CD pipelines. On a benchmark of 22 samples with 42 annotated vulnerabilities, Agent Audit detects 40 vulnerabilities with 6 false positives, substantially improving recall over common SAST baselines while maintaining sub-second scan times. Agent Audit is open source and installable via pip, making security auditing accessible for agent systems.
  In the live demonstration, attendees scan vulnerable agent repositories and observe how Agent Audit identifies security risks in tool functions, prompts, and more. Findings are linked to source locations and configuration paths, and can be exported into VS Code and GitHub Code Scanning for interactive inspection.

</details>


### 91. CoMaTrack: Competitive Multi-Agent Game-Theoretic Tracking with Vision-Language-Action Models

- **Authors:** Youzhi Liu, Li Gao, Liu Liu, Mingyang Lv, Yang Cai
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22846v1](http://arxiv.org/abs/2603.22846v1)
- **PDF:** [https://arxiv.org/pdf/2603.22846v1](https://arxiv.org/pdf/2603.22846v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Embodied Visual Tracking (EVT), a core dynamic task in embodied intelligence, requires an agent to precisely follow a language-specified target. Yet most existing methods rely on single-agent imitation learning, suffering from costly expert data and limited generalization due to static training environments. Inspired by competition-driven capability evolution, we propose CoMaTrack, a competitive game-theoretic multi-agent reinforcement learning framework that trains agents in a dynamic adversarial setting with competitive subtasks, yielding stronger adaptive planning and interference-resilient strategies. We further introduce CoMaTrack-Bench, the first benchmark for competitive EVT, featuring game scenarios between a tracker and adaptive opponents across diverse environments and instructions, enabling standardized robustness evaluation under active adversarial interactions. Experiments show that CoMaTrack achieves state-of-the-art results on both standard benchmarks and CoMaTrack-Bench. Notably, a 3B VLM trained with our framework surpasses previous single-agent imitation learning methods based on 7B models on the challenging EVT-Bench, achieving 92.1% in STT, 74.2% in DT, and 57.5% in AT. The benchmark code will be available at https://github.com/wlqcode/CoMaTrack-Bench

</details>


### 92. Empirical Comparison of Agent Communication Protocols for Task Orchestration

- **Authors:** Ivan Dobrovolskyi
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22823v1](http://arxiv.org/abs/2603.22823v1)
- **PDF:** [https://arxiv.org/pdf/2603.22823v1](https://arxiv.org/pdf/2603.22823v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Context. Nowadays, artificial intelligence agent systems are transforming from single-tool interactions to complex multi-agent orchestrations. As a result, two competing communication protocols have emerged: a tool integration protocol that standardizes how agents invoke external tools, and an inter-agent delegation protocol that enables autonomous agents to discover and delegate tasks to one another. Despite widespread industry adoption by dozens of enterprise partners, no empirical comparison of these protocols exists in the literature. Objective. The goal of this work is to develop the first systematic benchmark comparing tool-integration-only, multi-agent delegation, and hybrid architectures across standardized queries at three complexity levels, and to quantify the trade-offs in response time, context window consumption, monetary cost, error recovery, and implementation complexity.

</details>


### 93. ABSTRAL: Automatic Design of Multi-Agent Systems Through Iterative Refinement and Topology Optimization

- **Authors:** Weijia Song, Jiashu Yue, Zhe Pang
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22791v1](http://arxiv.org/abs/2603.22791v1)
- **PDF:** [https://arxiv.org/pdf/2603.22791v1](https://arxiv.org/pdf/2603.22791v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

How should multi-agent systems be designed, and can that design knowledge be captured in a form that is inspectable, revisable, and transferable? We introduce ABSTRAL, a framework that treats MAS architecture as an evolving natural-language document, an artifact refined through contrastive trace analysis. Three findings emerge. First, we provide a precise measurement of the multi-agent coordination tax: under fixed turn budgets, ensembles achieve only 26% turn efficiency, with 66% of tasks exhausting the limit, yet still improve over single-agent baselines by discovering parallelizable task decompositions. Second, design knowledge encoded in documents transfers: topology reasoning and role templates learned on one domain provide a head start on new domains, with transferred seeds matching coldstart iteration 3 performance in a single iteration. Third, contrastive trace analysis discovers specialist roles absent from any initial design, a capability no prior system demonstrates. On SOPBench (134 bank tasks, deterministic oracle), ABSTRAL reaches 70% validation / 65.96% test pass rate with a GPT-4o backbone. We release the converged documents as inspectable design rationale.

</details>


### 94. Can LLM Agents Generate Real-World Evidence? Evaluating Observational Studies in Medical Databases

- **Authors:** Dubai Li, Yuxiang He, Yan Hu, Yu Tian, Jingsong Li
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22767v1](http://arxiv.org/abs/2603.22767v1)
- **PDF:** [https://arxiv.org/pdf/2603.22767v1](https://arxiv.org/pdf/2603.22767v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Observational studies can yield clinically actionable evidence at scale, but executing them on real-world databases is open-ended and requires coherent decisions across cohort construction, analysis, and reporting. Prior evaluations of LLM agents emphasize isolated steps or single answers, missing the integrity and internal structure of the resulting evidence bundle. To address this gap, we introduce RWE-bench, a benchmark grounded in MIMIC-IV and derived from peer-reviewed observational studies. Each task provides the corresponding study protocol as the reference standard, requiring agents to execute experiments in a real database and iteratively generate tree-structured evidence bundles. We evaluate six LLMs (three open-source, three closed-source) under three agent scaffolds using both question-level correctness and end-to-end task metrics. Across 162 tasks, task success is low: the best agent reaches 39.9%, and the best open-source model reaches 30.4%. Agent scaffolds also matter substantially, causing over 30% variation in performance metrics. Furthermore, we implement an automated cohort evaluation method to rapidly localize errors and identify agent failure modes. Overall, the results highlight persistent limitations in agents' ability to produce end-to-end evidence bundles, and efficient validation remains an important direction for future work. Code and data are available at https://github.com/somewordstoolate/RWE-bench.

</details>


### 95. Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies

- **Authors:** Siddhant Kulkarni, Yukta Kulkarni
- **Published:** 2026-03-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22651v1](http://arxiv.org/abs/2603.22651v1)
- **PDF:** [https://arxiv.org/pdf/2603.22651v1](https://arxiv.org/pdf/2603.22651v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

The adoption of large language models (LLMs) for structured information extraction from financial documents has accelerated rapidly, yet production deployments face fundamental architectural decisions with limited empirical guidance. We present a systematic benchmark comparing four multi-agent orchestration architectures: sequential pipeline, parallel fan-out with merge, hierarchical supervisor-worker and reflexive self-correcting loop. These are evaluated across five frontier and open-weight LLMs on a corpus of 10,000 SEC filings (10-K, 10-Q and 8-K forms). Our evaluation spans 25 extraction field types covering governance structures, executive compensation and financial metrics, measured along five axes: field-level F1, document-level accuracy, end-to-end latency, cost per document and token efficiency. We find that reflexive architectures achieve the highest field-level F1 (0.943) but at 2.3x the cost of sequential baselines, while hierarchical architectures occupy the most favorable position on the cost-accuracy Pareto frontier (F1 0.921 at 1.4x cost). We further present ablation studies on semantic caching, model routing and adaptive retry strategies, demonstrating that hybrid configurations can recover 89\% of the reflexive architecture's accuracy gains at only 1.15x baseline cost. Our scaling analysis from 1K to 100K documents per day reveals non-obvious throughput-accuracy degradation curves that inform capacity planning. These findings provide actionable guidance for practitioners deploying multi-agent LLM systems in regulated financial environments.

</details>


### 96. flexvec: SQL Vector Retrieval with Programmatic Embedding Modulation

- **Authors:** Damian Delmas
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22587v1](http://arxiv.org/abs/2603.22587v1)
- **PDF:** [https://arxiv.org/pdf/2603.22587v1](https://arxiv.org/pdf/2603.22587v1)
- **Categories:** cs.IR, cs.AI, cs.DB


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents become the primary consumers of retrieval APIs, there is an opportunity to expose more of the retrieval pipeline to the caller. flexvec is a retrieval kernel that exposes the embedding matrix and score array as a programmable surface, allowing arithmetic operations on both before selection. We refer to composing operations on this surface at query time as Programmatic Embedding Modulation (PEM). This paper describes a set of such operations and integrates them into a SQL interface via a query materializer that facilitates composable query primitives. On a production corpus of 240,000 chunks, three composed modulations execute in 19 ms end-to-end on a desktop CPU without approximate indexing. At one million chunks, the same operations execute in 82 ms.

</details>


### 97. TrustTrade: Human-Inspired Selective Consensus Reduces Decision Uncertainty in LLM Trading Agents

- **Authors:** Minghan Li, Rachel Gonsalves, Weiyue Li, Sunghoon Yoon, Mengyu Wang
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22567v1](http://arxiv.org/abs/2603.22567v1)
- **PDF:** [https://arxiv.org/pdf/2603.22567v1](https://arxiv.org/pdf/2603.22567v1)
- **Categories:** cs.CE, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as autonomous agents in financial trading. However, they often exhibit a hazardous behavioral bias that we term uniform trust, whereby retrieved information is implicitly assumed to be factual and heterogeneous sources are treated as equally informative. This assumption stands in sharp contrast to human decision-making, which relies on selective filtering, cross-validation, and experience-driven weighting of information sources. As a result, LLM-based trading systems are particularly vulnerable to multi-source noise and misinformation, amplifying factual hallucinations and leading to unstable risk-return performance. To bridge this behavioral gap, we introduce TrustTrade (Trust-Rectified Unified Selective Trader), a multi-agent selective consensus framework inspired by human epistemic heuristics. TrustTrade replaces uniform trust with cross-agent consistency by aggregating information from multiple independent LLM agents and dynamically weighting signals based on their semantic and numerical agreement. Consistent signals are prioritized, while divergent, weakly grounded, or temporally inconsistent inputs are selectively discounted. To further stabilize decision-making, TrustTrade incorporates deterministic temporal signals as reproducible anchors and a reflective memory mechanism that adapts risk preferences at test time without additional training. Together, these components suppress noise amplification and hallucination-driven volatility, yielding more stable and risk-aware trading behavior. Across controlled backtesting in high-noise market environments (2024 Q1 and 2026 Q1), the proposed TrustTrade calibrates LLM trading behavior from extreme risk-return regimes toward a human-aligned, mid-risk and mid-return profile.

</details>


### 98. Ego2Web: A Web Agent Benchmark Grounded in Egocentric Videos

- **Authors:** Shoubin Yu, Lei Shu, Antoine Yang, Yao Fu, Srinivas Sunkara, Maria Wang, Jindong Chen, Mohit Bansal, Boqing Gong
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22529v1](http://arxiv.org/abs/2603.22529v1)
- **PDF:** [https://arxiv.org/pdf/2603.22529v1](https://arxiv.org/pdf/2603.22529v1)
- **Categories:** cs.CV, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal AI agents are increasingly automating complex real-world workflows that involve online web execution. However, current web-agent benchmarks suffer from a critical limitation: they focus entirely on web-based interaction and perception, lacking grounding in the user's real-world physical surroundings. This limitation prevents evaluation in crucial scenarios, such as when an agent must use egocentric visual perception (e.g., via AR glasses) to recognize an object in the user's surroundings and then complete a related task online. To address this gap, we introduce Ego2Web, the first benchmark designed to bridge egocentric video perception and web agent execution. Ego2Web pairs real-world first-person video recordings with web tasks that require visual understanding, web task planning, and interaction in an online environment for successful completion. We utilize an automatic data-generation pipeline combined with human verification and refinement to curate well-constructed, high-quality video-task pairs across diverse web task types, including e-commerce, media retrieval, knowledge lookup, etc. To facilitate accurate and scalable evaluation for our benchmark, we also develop a novel LLM-as-a-Judge automatic evaluation method, Ego2WebJudge, which achieves approximately 84% agreement with human judgment, substantially higher than existing evaluation methods. Experiments with diverse SoTA agents on our Ego2Web show that their performance is weak, with substantial headroom across all task categories. We also conduct a comprehensive ablation study on task design, highlighting the necessity of accurate video understanding in the proposed task and the limitations of current agents. We hope Ego2Web can be a critical new resource for developing truly capable AI assistants that can seamlessly see, understand, and act across the physical and digital worlds.

</details>


### 99. GraphRAG for Engineering Diagrams: ChatP&ID Enables LLM Interaction with P&IDs

- **Authors:** Achmad Anggawirya Alimin, Artur M. Schweidtmann
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22528v1](http://arxiv.org/abs/2603.22528v1)
- **PDF:** [https://arxiv.org/pdf/2603.22528v1](https://arxiv.org/pdf/2603.22528v1)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) combined with Retrieval-Augmented Generation (RAG) and knowledge graphs offer new opportunities for interacting with engineering diagrams such as Piping and Instrumentation Diagrams (P&IDs). However, directly processing raw images or smart P&ID files with LLMs is often costly, inefficient, and prone to hallucinations. This work introduces ChatP&ID, an agentic framework that enables grounded and cost-effective natural-language interaction with P&IDs using Graph Retrieval-Augmented Generation (GraphRAG), a paradigm we refer to as GraphRAG for engineering diagrams. Smart P&IDs encoded in the DEXPI standard are transformed into structured knowledge graphs, which serve as the basis for graph-based retrieval and reasoning by LLM agents. This approach enables reliable querying of engineering diagrams while significantly reducing computational cost. Benchmarking across commercial LLM APIs (OpenAI, Anthropic) demonstrates that graph-based representations improve accuracy by 18% over raw image inputs and reduce token costs by 85% compared to directly ingesting smart P&ID files. While small open-source models still struggle to interpret knowledge graph formats and structured engineering data, integrating them with VectorRAG and PathRAG improves response accuracy by up to 40%. Notably, GPT-5-mini combined with ContextRAG achieves 91% accuracy at a cost of only $0.004 per task. The resulting ChatP&ID interface enables intuitive natural-language interaction with complex engineering diagrams and lays the groundwork for AI-assisted process engineering tasks such as Hazard and Operability Studies (HAZOP) and multi-agent analysis.

</details>


### 100. SkillRouter: Retrieve-and-Rerank Skill Selection for LLM Agents at Scale

- **Authors:** YanZhao Zheng, ZhenTao Zhang, Chao Ma, YuanQiang Yu, JiHuan Zhu, Baohua Dong, Hangcheng Zhu
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22455v1](http://arxiv.org/abs/2603.22455v1)
- **PDF:** [https://arxiv.org/pdf/2603.22455v1](https://arxiv.org/pdf/2603.22455v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agent ecosystems grow, the number of available skills (tools, plugins) has reached tens of thousands, making it infeasible to inject all skills into an agent's context. This creates a need for skill routing -- retrieving the most relevant skills from a large pool given a user task. The problem is compounded by pervasive functional overlap in community skill repositories, where many skills share similar names and purposes yet differ in implementation details. Despite its practical importance, skill routing remains under-explored. Current agent architectures adopt a progressive disclosure design -- exposing only skill names and descriptions to the agent while keeping the full implementation body hidden -- implicitly treating metadata as sufficient for selection. We challenge this assumption through a systematic empirical study on a benchmark of ~$80K skills and 75 expert-verified queries. Our key finding is that the skill body (full implementation text) is the decisive signal: removing it causes 29--44 percentage point degradation across all retrieval methods, and cross-encoder attention analysis reveals 91.7% of attention concentrating on the body field. Motivated by this finding, we propose SkillRouter, a two-stage retrieve-and-rerank pipeline totaling only 1.2B parameters (0.6B encoder + 0.6B reranker). SkillRouter achieves 74.0% top-1 routing accuracy and delivers the strongest average result among the compact and zero-shot baselines we evaluate, while remaining deployable on consumer hardware.

</details>


### 101. Towards Automated Community Notes Generation with Large Vision Language Models for Combating Contextual Deception

- **Authors:** Jin Ma, Jingwen Yan, Mohammed Aldeen, Ethan Anderson, Taran Kavuru, Jinkyung Katie Park, Feng Luo, Long Cheng
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22453v1](http://arxiv.org/abs/2603.22453v1)
- **PDF:** [https://arxiv.org/pdf/2603.22453v1](https://arxiv.org/pdf/2603.22453v1)
- **Categories:** cs.CL, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Community Notes have emerged as an effective crowd-sourced mechanism for combating online deception on social media platforms. However, its reliance on human contributors limits both the timeliness and scalability. In this work, we study the automated Community Notes generation method for image-based contextual deception, where an authentic image is paired with misleading context (e.g., time, entity, and event). Unlike prior work that primarily focuses on deception detection (i.e., judging whether a post is true or false in a binary manner), Community Notes-style systems need to generate concise and grounded notes that help users recover the missing or corrected context. This problem remains underexplored due to three reasons: (i) datasets that support the research are scarce; (ii) methods must handle the dynamic nature of contextual deception; (iii) evaluation is difficult because standard metrics do not capture whether notes actually improve user understanding. To address these gaps, we curate a real-world dataset, XCheck, comprising X posts with associated Community Notes and external contexts. We further propose the Automated Context-Corrective Note generation method, named ACCNote, which is a retrieval-augmented, multi-agent collaboration framework built on large vision-language models. Finally, we introduce a new evaluation metric, Context Helpfulness Score (CHS), that aligns with user study outcomes rather than relying on lexical overlap. Experiments on our XCheck dataset show that the proposed ACCNote improves both deception detection and note generation performance over baselines, and exceeds a commercial tool GPT5-mini. Together, our dataset, method, and metric advance practical automated generation of context-corrective notes toward more responsible online social networks.

</details>


### 102. From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents

- **Authors:** Ling Yue, Kushal Raj Bhandari, Ching-Yun Ko, Dhaval Patel, Shuxin Lin, Nianjun Zhou, Jianxi Gao, Pin-Yu Chen, Shaowu Pan
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22386v1](http://arxiv.org/abs/2603.22386v1)
- **PDF:** [https://arxiv.org/pdf/2603.22386v1](https://arxiv.org/pdf/2603.22386v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based systems are becoming increasingly popular for solving tasks by constructing executable workflows that interleave LLM calls, information retrieval, tool use, code execution, memory updates, and verification. This survey reviews recent methods for designing and optimizing such workflows, which we treat as agentic computation graphs (ACGs). We organize the literature based on when workflow structure is determined, where structure refers to which components or agents are present, how they depend on each other, and how information flows between them. This lens distinguishes static methods, which fix a reusable workflow scaffold before deployment, from dynamic methods, which select, generate, or revise the workflow for a particular run before or during execution. We further organize prior work along three dimensions: when structure is determined, what part of the workflow is optimized, and which evaluation signals guide optimization (e.g., task metrics, verifier signals, preferences, or trace-derived feedback). We also distinguish reusable workflow templates, run-specific realized graphs, and execution traces, separating reusable design choices from the structures actually deployed in a given run and from realized runtime behavior. Finally, we outline a structure-aware evaluation perspective that complements downstream task metrics with graph-level properties, execution cost, robustness, and structural variation across inputs. Our goal is to provide a clear vocabulary, a unified framework for positioning new methods, a more comparable view of existing body of literature, and a more reproducible evaluation standard for future work in workflow optimizations for LLM agents.

</details>


### 103. Chimera: Latency- and Performance-Aware Multi-agent Serving for Heterogeneous LLMs

- **Authors:** Kangqi Ni, Wenyue Hua, Xiaoxiang Shi, Jiang Guo, Shiyu Chang, Tianlong Chen
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22206v1](http://arxiv.org/abs/2603.22206v1)
- **PDF:** [https://arxiv.org/pdf/2603.22206v1](https://arxiv.org/pdf/2603.22206v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent applications often execute complex tasks as multi-stage workflows, where each stage is an LLM call whose output becomes part of context for subsequent steps. Existing LLM serving systems largely assume homogeneous clusters with identical model replicas. This design overlooks the potential of heterogeneous deployments, where models of different sizes and capabilities enable finer trade-offs between latency and performance. However, heterogeneity introduces new challenges in scheduling across models with diverse throughput and performance. We present Chimera, a predictive scheduling system for multi-agent workflow serving on heterogeneous LLM clusters that jointly improves end-to-end latency and task performance. Chimera applies semantic routing to estimate per-model confidence scores for each request, predicts the total remaining output length of the workflow, and estimates per-model congestion using in-flight predicted token volumes for load balancing. We evaluate Chimera on representative agentic workflows for code generation and math reasoning using multiple heterogeneous LLM configurations. Across comparable settings, Chimera traces the best latency-performance frontier, reducing end-to-end latency by 1.2--2.4$\times$ and improving task performance by 8.0-9.5 percentage points on average over competitive baselines including vLLM.

</details>


### 104. Learning When to Act: Interval-Aware Reinforcement Learning with Predictive Temporal Structure

- **Authors:** Davide Di Gioia
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22384v2](http://arxiv.org/abs/2603.22384v2)
- **PDF:** [https://arxiv.org/pdf/2603.22384v2](https://arxiv.org/pdf/2603.22384v2)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents operating in continuous environments must decide not only what to do, but when to act. We introduce a lightweight adaptive temporal control system that learns the optimal interval between cognitive ticks from experience, replacing ad hoc biologically inspired timers with a principled learned policy. The policy state is augmented with a predictive hyperbolic spread signal (a "curvature signal" shorthand) derived from hyperbolic geometry: the mean pairwise Poincare distance among n sampled futures embedded in the Poincare ball. High spread indicates a branching, uncertain future and drives the agent to act sooner; low spread signals predictability and permits longer rest intervals. We further propose an interval-aware reward that explicitly penalises inefficiency relative to the chosen wait time, correcting a systematic credit-assignment failure of naive outcome-based rewards in timing problems. We additionally introduce a joint spatio-temporal embedding (ATCPG-ST) that concatenates independently normalised state and position projections in the Poincare ball; spatial trajectory divergence provides an independent timing signal unavailable to the state-only variant (ATCPG-SO). This extension raises mean hyperbolic spread (kappa) from 1.88 to 3.37 and yields a further 5.8 percent efficiency gain over the state-only baseline. Ablation experiments across five random seeds demonstrate that (i) learning is the dominant efficiency factor (54.8 percent over no-learning), (ii) hyperbolic spread provides significant complementary gain (26.2 percent over geometry-free control), (iii) the combined system achieves 22.8 percent efficiency over the fixed-interval baseline, and (iv) adding spatial position information to the spread embedding yields an additional 5.8 percent.

</details>


### 105. Human-Inspired Pavlovian and Instrumental Learning for Autonomous Agent Navigation

- **Authors:** Jingfeng Shan, Francesco Guidi, Mehrdad Saeidi, Enrico Testi, Elia Favarelli, Andrea Giorgetti, Davide Dardari, Alberto Zanella, Giorgio Li Pira, Francesca Starita, Anna Guerra
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22170v1](http://arxiv.org/abs/2603.22170v1)
- **PDF:** [https://arxiv.org/pdf/2603.22170v1](https://arxiv.org/pdf/2603.22170v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents operating in uncertain environments must balance fast responses with goal-directed planning. Classical MF RL often converges slowly and may induce unsafe exploration, whereas MB methods are computationally expensive and sensitive to model mismatch. This paper presents a human-inspired hybrid RL architecture integrating Pavlovian, Instrumental MF, and Instrumental MB components. Inspired by Pavlovian and Instrumental learning from neuroscience, the framework considers contextual radio cues, here intended as georeferenced environmental features acting as CS, to shape intrinsic value signals and bias decision-making. Learning is further modulated by internal motivational drives through a dedicated motivational signal. A Bayesian arbitration mechanism adaptively blends MF and MB estimates based on predicted reliability. Simulation results show that the hybrid approach accelerates learning, improves operational safety, and reduces navigation in high-uncertainty regions compared to standard RL baselines. Pavlovian conditioning promotes safer exploration and faster convergence, while arbitration enables a smooth transition from exploration to efficient, plan-driven exploitation. Overall, the results highlight the benefits of biologically inspired modularity for robust and adaptive autonomous systems under uncertainty.

</details>


### 106. Causal Evidence that Language Models use Confidence to Drive Behavior

- **Authors:** Dharshan Kumaran, Nathaniel Daw, Simon Osindero, Petar Velickovic, Viorica Patraucean
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22161v1](http://arxiv.org/abs/2603.22161v1)
- **PDF:** [https://arxiv.org/pdf/2603.22161v1](https://arxiv.org/pdf/2603.22161v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Metacognition -- the ability to assess one's own cognitive performance -- is documented across species, with internal confidence estimates serving as a key signal for adaptive behavior. While confidence can be extracted from Large Language Model (LLM) outputs, whether models actively use these signals to regulate behavior remains a fundamental question. We investigate this through a four-phase abstention paradigm.Phase 1 established internal confidence estimates in the absence of an abstention option. Phase 2 revealed that LLMs apply implicit thresholds to these estimates when deciding to answer or abstain. Confidence emerged as the dominant predictor of behavior, with effect sizes an order of magnitude larger than knowledge retrieval accessibility (RAG scores) or surface-level semantic features. Phase 3 provided causal evidence through activation steering: manipulating internal confidence signals correspondingly shifted abstention rates. Finally, Phase 4 demonstrated that models can systematically vary abstention policies based on instructed thresholds.Our findings indicate that abstention arises from the joint operation of internal confidence representations and threshold-based policies, mirroring the two-stage metacognitive control found in biological systems. This capacity is essential as LLMs transition into autonomous agents that must recognize their own uncertainty to decide when to act or seek help.

</details>


### 107. A Context Engineering Framework for Improving Enterprise AI Agents based on Digital-Twin MDP

- **Authors:** Xi Yang, Aurelie Lozano, Naoki Abe, Bhavya, Saurabh Jha, Noah Zheutlin, Rohan R. Arora, Yu Deng, Daby M. Sow
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22083v1](http://arxiv.org/abs/2603.22083v1)
- **PDF:** [https://arxiv.org/pdf/2603.22083v1](https://arxiv.org/pdf/2603.22083v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Despite rapid progress in AI agents for enterprise automation and decision-making, their real-world deployment and further performance gains remain constrained by limited data quality and quantity, complex real-world reasoning demands, difficulties with self-play, and the lack of reliable feedback signals. To address these challenges, we propose a lightweight, model-agnostic framework for improving LLM-based enterprise agents via offline reinforcement learning (RL). The proposed Context Engineering via DT-MDP (DT-MDP-CE) framework comprises three key components: (1) A Digital-Twin Markov Decision Process (DT-MDP), which abstracts the agent's reasoning behavior as a finite MDP; (2) A robust contrastive inverse RL, which, armed with the DT-MDP, to efficiently estimate a well-founded reward function and induces policies from mixed-quality offline trajectories; and (3) RL-guided context engineering, which uses the policy obtained from the integrated process of (1) and (2), to improve the agent's decision-making behavior. As a case study, we apply the framework to a representative task in the enterprise-oriented domain of IT automation. Extensive experimental results demonstrate consistent and significant improvements over baseline agents across a wide range of evaluation settings, suggesting that the framework can generalize to other agents sharing similar characteristics in enterprise environments.

</details>


### 108. Future-Interactions-Aware Trajectory Prediction via Braid Theory

- **Authors:** Caio Azevedo, Stefano Sabatini, Sascha Hornauer, Fabien Moutarde
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22035v1](http://arxiv.org/abs/2603.22035v1)
- **PDF:** [https://arxiv.org/pdf/2603.22035v1](https://arxiv.org/pdf/2603.22035v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

To safely operate, an autonomous vehicle must know the future behavior of a potentially high number of interacting agents around it, a task often posed as multi-agent trajectory prediction. Many previous attempts to model social interactions and solve the joint prediction task either add extensive computational requirements or rely on heuristics to label multi-agent behavior types. Braid theory, in contrast, provides a powerful exact descriptor of multi-agent behavior by projecting future trajectories into braids that express how trajectories cross with each other over time; a braid then corresponds to a specific mode of coordination between the multiple agents in the future. In past work, braids have been used lightly to reason about interacting agents and restrict the attention window of predicted agents. We show that leveraging more fully the expressivity of the braid representation and using it to condition the trajectories themselves leads to even further gains in joint prediction performance, with negligible added complexity either in training or at inference time. We do so by proposing a novel auxiliary task, braid prediction, done in parallel with the trajectory prediction task. By classifying edges between agents into their correct crossing types in the braid representation, the braid prediction task is able to imbue the model with improved social awareness, which is reflected in joint predictions that more closely adhere to the actual multi-agent behavior. This simple auxiliary task allowed us to obtain significant improvements in joint metrics on three separate datasets. We show how the braid prediction task infuses the model with future intention awareness, leading to more accurate joint predictions. Code is available at github.com/caiocj1/traj-pred-braid-theory.

</details>


### 109. Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe

- **Authors:** Xixi Wu, Qianguo Sun, Ruiyang Zhang, Chao Song, Junlong Wu, Yiyan Qi, Hong Cheng
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21972v1](http://arxiv.org/abs/2603.21972v1)
- **PDF:** [https://arxiv.org/pdf/2603.21972v1](https://arxiv.org/pdf/2603.21972v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement Learning (RL) is essential for evolving Large Language Models (LLMs) into autonomous agents capable of long-horizon planning, yet a practical recipe for scaling RL in complex, multi-turn environments remains elusive. This paper presents a systematic empirical study using TravelPlanner, a challenging testbed requiring tool orchestration to satisfy multifaceted constraints. We decompose the agentic RL design space along 5 axes: reward shaping, model scaling, data composition, algorithm selection, and environmental stability. Our controlled experiments yield 7 key takeaways, e.g., (1) reward and algorithm choices are scale-dependent as smaller models benefit from staged rewards and enhanced exploration, whereas larger models converge efficiently with simpler dense rewards, (2) ~ 1K training samples with a balanced difficulty mixture mark a sweet spot for both in-domain and out-of-domain performance, and (3) environmental stability is critical to prevent policy degradation. Based on our distilled recipe, our RL-trained models achieve state-of-the-art performance on TravelPlanner, significantly outperforming leading LLMs.

</details>


### 110. Partial Attention in Deep Reinforcement Learning for Safe Multi-Agent Control

- **Authors:** Turki Bin Mohaya, Peter Seiler
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21810v1](http://arxiv.org/abs/2603.21810v1)
- **PDF:** [https://arxiv.org/pdf/2603.21810v1](https://arxiv.org/pdf/2603.21810v1)
- **Categories:** eess.SY, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Attention mechanisms excel at learning sequential patterns by discriminating data based on relevance and importance. This provides state-of-the-art performance in advanced generative artificial intelligence models. This paper applies this concept of an attention mechanism for multi-agent safe control. We specifically consider the design of a neural network to control autonomous vehicles in a highway merging scenario. The environment is modeled as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP). Within a QMIX framework, we include partial attention for each autonomous vehicle, thus allowing each ego vehicle to focus on the most relevant neighboring vehicles. Moreover, we propose a comprehensive reward signal that considers the global objectives of the environment (e.g., safety and vehicle flow) and the individual interests of each agent. Simulations are conducted in the Simulation of Urban Mobility (SUMO). The results show better performance compared to other driving algorithms in terms of safety, driving speed, and reward.

</details>


### 111. Modal Logic for Distributed Trust

- **Authors:** Niels Voorneveld, Peeter Laud
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21802v1](http://arxiv.org/abs/2603.21802v1)
- **PDF:** [https://arxiv.org/pdf/2603.21802v1](https://arxiv.org/pdf/2603.21802v1)
- **Categories:** cs.LO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We propose a method for reasoning about trust in multi-agent systems, specifying a language for describing communication protocols and making trust assumptions and derivations. This is given an interpretation in a modal logic for describing the beliefs and communications of agents in a network. We define how information in the network can be shared via forwarding, and how trust between agents can be generalized to trust across networks. We give specifications for the modal logic which can be readily adapted into a lambda calculus of proofs. We show that by nesting modalities, we can describe chains of communication between agents, and establish suitable notions of trust for such chains. We see how this can be applied to trust models in public key infrastructures, as well as other interaction protocols in distributed systems.

</details>


### 112. AI Co-Scientist for Ranking: Discovering Novel Search Ranking Models alongside LLM-based AI Agents with Cloud Computing Access

- **Authors:** Liwei Wu, Cho-Jui Hsieh
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22376v1](http://arxiv.org/abs/2603.22376v1)
- **PDF:** [https://arxiv.org/pdf/2603.22376v1](https://arxiv.org/pdf/2603.22376v1)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in AI agents for software engineering and scientific discovery have demonstrated remarkable capabilities, yet their application to developing novel ranking models in commercial search engines remains unexplored. In this paper, we present an AI Co-Scientist framework that automates the full search ranking research pipeline: from idea generation to code implementation and GPU training job scheduling with expert in the loop. Our approach strategically employs single-LLM agents for routine tasks while leveraging multi-LLM consensus agents (GPT 5.2, Gemini Pro 3, and Claude Opus 4.5) for challenging phases such as results analysis and idea generation. To our knowledge, this is the first study in the ranking community to utilize an AI Co-Scientist framework for algorithmic research. We demonstrate that this framework discovered a novel technique for handling sequence features, with all model enhancements produced automatically, yielding substantial offline performance improvements. Our findings suggest that AI systems can discover ranking architectures comparable to those developed by human experts while significantly reducing routine research workloads.

</details>


### 113. Cognitive Agency Surrender: Defending Epistemic Sovereignty via Scaffolded AI Friction

- **Authors:** Kuangzhe Xu, Yu Shen, Longjie Yan, Yinghui Ren
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21735v1](http://arxiv.org/abs/2603.21735v1)
- **PDF:** [https://arxiv.org/pdf/2603.21735v1](https://arxiv.org/pdf/2603.21735v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The proliferation of Generative Artificial Intelligence has transformed benign cognitive offloading into a systemic risk of cognitive agency surrender. Driven by the commercial dogma of "zero-friction" design, highly fluent AI interfaces actively exploit human cognitive miserliness, prematurely satisfying the need for cognitive closure and inducing severe automation bias. To empirically quantify this epistemic erosion, we deployed a zero-shot semantic classification pipeline ($τ=0.7$) on 1,223 high-confidence AI-HCI papers from 2023 to early 2026. Our analysis reveals an escalating "agentic takeover": a brief 2025 surge in research defending human epistemic sovereignty (19.1%) was abruptly suppressed in early 2026 (13.1%) by an explosive shift toward optimizing autonomous machine agents (19.6%), while frictionless usability maintained a structural hegemony (67.3%). To dismantle this trap, we theorize "Scaffolded Cognitive Friction," repurposing Multi-Agent Systems (MAS) as explicit cognitive forcing functions (e.g., computational Devil's Advocates) to inject germane epistemic tension and disrupt heuristic execution. Furthermore, we outline a multimodal computational phenotyping agenda -- integrating gaze transition entropy, task-evoked pupillometry, fNIRS, and Hierarchical Drift Diffusion Modeling (HDDM) -- to mathematically decouple decision outcomes from cognitive effort. Ultimately, intentionally designed friction is not merely a psychological intervention, but a foundational technical prerequisite for enforcing global AI governance and preserving societal cognitive resilience.

</details>


### 114. Can a Robot Walk the Robotic Dog: Triple-Zero Collaborative Navigation for Heterogeneous Multi-Agent Systems

- **Authors:** Yaxuan Wang, Yifan Xiang, Ke Li, Xun Zhang, BoWen Ye, Zhuochen Fan, Fei Wei, Tong Yang
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21723v2](http://arxiv.org/abs/2603.21723v2)
- **PDF:** [https://arxiv.org/pdf/2603.21723v2](https://arxiv.org/pdf/2603.21723v2)
- **Categories:** cs.RO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present Triple Zero Path Planning (TZPP), a collaborative framework for heterogeneous multi-robot systems that requires zero training, zero prior knowledge, and zero simulation. TZPP employs a coordinator--explorer architecture: a humanoid robot handles task coordination, while a quadruped robot explores and identifies feasible paths using guidance from a multimodal large language model. We implement TZPP on Unitree G1 and Go2 robots and evaluate it across diverse indoor and outdoor environments, including obstacle-rich and landmark-sparse settings. Experiments show that TZPP achieves robust, human-comparable efficiency and strong adaptability to unseen scenarios. By eliminating reliance on training and simulation, TZPP offers a practical path toward real-world deployment of heterogeneous robot cooperation. Our code and video are provided at: https://github.com/triple-zeropp/Triple-zero-robot-agent

</details>


### 115. MIND: Multi-agent inference for negotiation dialogue in travel planning

- **Authors:** Hunmin Do, Taejun Yoon, Kiyong Jung
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21696v1](http://arxiv.org/abs/2603.21696v1)
- **PDF:** [https://arxiv.org/pdf/2603.21696v1](https://arxiv.org/pdf/2603.21696v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

While Multi-Agent Debate (MAD) research has advanced, its efficacy in coordinating complex stakeholder interests such as travel planning remains largely unexplored. To bridge this gap, we propose MIND (Multi-agent Inference for Negotiation Dialogue), a framework designed to simulate realistic consensus-building among travelers with heterogeneous preferences. Grounded in the Theory of Mind (ToM), MIND introduces a Strategic Appraisal phase that infers opponent willingness (w) from linguistic nuances with 90.2% accuracy. Experimental results demonstrate that MIND outperforms traditional MAD frameworks, achieving a 20.5% improvement in High-w Hit and a 30.7% increase in Debate Hit-Rate, effectively prioritizing high-stakes constraints. Furthermore, qualitative evaluations via LLM-as-a-Judge confirm that MIND surpasses baselines in Rationality (68.8%) and Fluency (72.4%), securing an overall win rate of 68.3%. These findings validate that MIND effectively models human negotiation dynamics to derive persuasive consensus.

</details>


### 116. Reasoning Provenance for Autonomous AI Agents: Structured Behavioral Analytics Beyond State Checkpoints and Execution Traces

- **Authors:** Neelmani Vispute
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21692v1](http://arxiv.org/abs/2603.21692v1)
- **PDF:** [https://arxiv.org/pdf/2603.21692v1](https://arxiv.org/pdf/2603.21692v1)
- **Categories:** cs.AI, cs.DC, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents transition from human-supervised copilots to autonomous platform infrastructure, the ability to analyze their reasoning behavior across populations of investigations becomes a pressing infrastructure requirement. Existing operational tooling addresses adjacent needs effectively: state checkpoint systems enable fault tolerance; observability platforms provide execution traces for debugging; telemetry standards ensure interoperability. What current systems do not natively provide as a first-class, schema-level primitive is structured reasoning provenance -- normalized, queryable records of why the agent chose each action, what it concluded from each observation, how each conclusion shaped its strategy, and which evidence supports its final verdict. This paper introduces the Agent Execution Record (AER), a structured reasoning provenance primitive that captures intent, observation, and inference as first-class queryable fields on every step, alongside versioned plans with revision rationale, evidence chains, structured verdicts with confidence scores, and delegation authority chains. We formalize the distinction between computational state persistence and reasoning provenance, argue that the latter cannot in general be faithfully reconstructed from the former, and show how AERs enable population-level behavioral analytics: reasoning pattern mining, confidence calibration, cross-agent comparison, and counterfactual regression testing via mock replay. We present a domain-agnostic model with extensible domain profiles, a reference implementation and SDK, and outline an evaluation methodology informed by preliminary deployment on a production platformized root cause analysis agent.

</details>


### 117. Strategic Infrastructure Design via Multi-Agent Congestion Games with Joint Placement and Pricing

- **Authors:** Niloofar Aminikalibar, Farzaneh Farhadi, Maria Chli
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21691v1](http://arxiv.org/abs/2603.21691v1)
- **PDF:** [https://arxiv.org/pdf/2603.21691v1](https://arxiv.org/pdf/2603.21691v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Real-world infrastructure planning increasingly involves strategic interactions among autonomous agents competing over congestible, limited resources. Applications such as Electric Vehicle (EV) charging, emergency response, and intelligent transportation require coordinated resource placement and pricing decisions, while anticipating the adaptive behaviour of decentralised, self-interested agents. We propose a novel multi-agent framework for joint placement and pricing under such interactions, formalised as a bi-level optimisation model. The upper level represents a central planner, while the lower level captures agent responses via coupled non-atomic congestion games. Motivated by the EV charging domain, we study a setting where a central planner provisions chargers and road capacity under budget and profitability constraints. The agent population includes both EV drivers and non-charging drivers (NCDs), who respond to congestion, delays, and costs. To solve the resulting NP-hard problem, we introduce ABO-MPN, a double-layer approximation framework that decouples agent types, applies integer adjustment and rounding, and targets high-impact placement and pricing decisions. Experiments on benchmark networks show that our model reduces social cost by up to 40% compared to placement- or pricing-only baselines, and generalises to other MAS-relevant domains.

</details>


### 118. Optimizing Multi-Agent Weather Captioning via Text Gradient Descent: A Training-Free Approach with Consensus-Aware Gradient Fusion

- **Authors:** Shixu Liu
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21673v1](http://arxiv.org/abs/2603.21673v1)
- **PDF:** [https://arxiv.org/pdf/2603.21673v1](https://arxiv.org/pdf/2603.21673v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Generating interpretable natural language captions from weather time series data remains a significant challenge at the intersection of meteorological science and natural language processing. While recent advances in Large Language Models (LLMs) have demonstrated remarkable capabilities in time series forecasting and analysis, existing approaches either produce numerical predictions without human-accessible explanations or generate generic descriptions lacking domain-specific depth. We introduce WeatherTGD, a training-free multi-agent framework that reinterprets collaborative caption refinement through the lens of Text Gradient Descent (TGD). Our system deploys three specialized LLM agents including a Statistical Analyst, a Physics Interpreter, and a Meteorology Expert that generate domain-specific textual gradients from weather time series observations. These gradients are aggregated through a novel Consensus-Aware Gradient Fusion mechanism that extracts common signals while preserving unique domain perspectives. The fused gradients then guide an iterative refinement process analogous to gradient descent, where each LLM-generated feedback signal updates the caption toward an optimal solution. Experiments on real-world meteorological datasets demonstrate that WeatherTGD achieves significant improvements in both LLM-based evaluation and human expert evaluation, substantially outperforming existing multi-agent baselines while maintaining computational efficiency through parallel agent execution.

</details>


### 119. EnterpriseLab: A Full-Stack Platform for developing and deploying agents in Enterprises

- **Authors:** Ankush Agarwal, Harsh Vishwakarma, Suraj Nagaje, Chaitanya Devaguptapu
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21630v1](http://arxiv.org/abs/2603.21630v1)
- **PDF:** [https://arxiv.org/pdf/2603.21630v1](https://arxiv.org/pdf/2603.21630v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deploying AI agents in enterprise environments requires balancing capability with data sovereignty and cost constraints. While small language models offer privacy-preserving alternatives to frontier models, their specialization is hindered by fragmented development pipelines that separate tool integration, data generation, and training. We introduce EnterpriseLab, a full-stack platform that unifies these stages into a closed-loop framework. EnterpriseLab provides (1) a modular environment exposing enterprise applications via Model Context Protocol, enabling seamless integration of proprietary and open-source tools; (2) automated trajectory synthesis that programmatically generates training data from environment schemas; and (3) integrated training pipelines with continuous evaluation. We validate the platform through EnterpriseArena, an instantiation with 15 applications and 140+ tools across IT, HR, sales, and engineering domains. Our results demonstrate that 8B-parameter models trained within EnterpriseLab match GPT-4o's performance on complex enterprise workflows while reducing inference costs by 8-10x, and remain robust across diverse enterprise benchmarks, including EnterpriseBench (+10%) and CRMArena (+10%). EnterpriseLab provides enterprises a practical path to deploying capable, privacy-preserving agents without compromising operational capability.

</details>


### 120. AgenticRec: End-to-End Tool-Integrated Policy Optimization for Ranking-Oriented Recommender Agents

- **Authors:** Tianyi Li, Zixuan Wang, Guidong Lei, Xiaodong Li, Hui Li
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21613v1](http://arxiv.org/abs/2603.21613v1)
- **PDF:** [https://arxiv.org/pdf/2603.21613v1](https://arxiv.org/pdf/2603.21613v1)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recommender agents built on Large Language Models offer a promising paradigm for recommendation. However, existing recommender agents typically suffer from a disconnect between intermediate reasoning and final ranking feedback, and are unable to capture fine-grained preferences. To address this, we present AgenticRec, a ranking-oriented agentic recommendation framework that optimizes the entire decision-making trajectory (including intermediate reasoning, tool invocation, and final ranking list generation) under sparse implicit feedback. Our approach makes three key contributions. First, we design a suite of recommendation-specific tools integrated into a ReAct loop to support evidence-grounded reasoning. Second, we propose theoretically unbiased List-Wise Group Relative Policy Optimization (list-wise GRPO) to maximize ranking utility, ensuring accurate credit assignment for complex tool-use trajectories. Third, we introduce Progressive Preference Refinement (PPR) to resolve fine-grained preference ambiguities. By mining hard negatives from ranking violations and applying bidirectional preference alignment, PPR minimizes the convex upper bound of pairwise ranking errors. Experiments on benchmarks confirm that AgenticRec significantly outperforms baselines, validating the necessity of unifying reasoning, tool use, and ranking optimization.

</details>


### 121. Cerebra: A Multidisciplinary AI Board for Multimodal Dementia Characterization and Risk Assessment

- **Authors:** Sheng Liu, Long Chen, Zeyun Zhao, Qinglin Gou, Qingyue Wei, Arjun Masurkar, Kevin M. Spiegler, Philip Kuball, Stefania C. Bray, Megan Bernath, Deanna R. Willis, Jiang Bian, Lei Xing, Eric Topol, Kyunghyun Cho, Yu Huang, Ruogu Fang, Narges Razavian, James Zou
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21597v2](http://arxiv.org/abs/2603.21597v2)
- **PDF:** [https://arxiv.org/pdf/2603.21597v2](https://arxiv.org/pdf/2603.21597v2)
- **Categories:** cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern clinical practice increasingly depends on reasoning over heterogeneous, evolving, and incomplete patient data. Although recent advances in multimodal foundation models have improved performance on various clinical tasks, most existing models remain static, opaque, and poorly aligned with real-world clinical workflows. We present Cerebra, an interactive multi-agent AI team that coordinates specialized agents for EHR, clinical notes, and medical imaging analysis. These outputs are synthesized into a clinician-facing dashboard that combines visual analytics with a conversational interface, enabling clinicians to interrogate predictions and contextualize risk at the point of care. Cerebra supports privacy-preserving deployment by operating on structured representations and remains robust when modalities are incomplete. We evaluated Cerebra using a massive multi-institutional dataset spanning 3 million patients from four independent healthcare systems. Cerebra consistently outperformed both state-of-the-art single-modality models and large multimodal language model baselines. In dementia risk prediction, it achieved AUROCs up to 0.80, compared with 0.74 for the strongest single-modality model and 0.68 for language model baselines. For dementia diagnosis, it achieved an AUROC of 0.86, and for survival prediction, a C-index of 0.81. In a reader study with experienced physicians, Cerebra significantly improved expert performance, increasing accuracy by 17.5 percentage points in prospective dementia risk estimation. These results demonstrate Cerebra's potential for interpretable, robust decision support in clinical care.

</details>


### 122. Spatio-Temporal Attention Enhanced Multi-Agent DRL for UAV-Assisted Wireless Networks with Limited Communications

- **Authors:** Che Chen, Lanhua Li, Shimin Gong, Yu Zhao, Yuming Fang, Dusit Niyato
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21594v1](http://arxiv.org/abs/2603.21594v1)
- **PDF:** [https://arxiv.org/pdf/2603.21594v1](https://arxiv.org/pdf/2603.21594v1)
- **Categories:** cs.IT, cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

In this paper, we employ multiple UAVs to accelerate data transmissions from ground users (GUs) to a remote base station (BS) via the UAVs' relay communications. The UAVs' intermittent information exchanges typically result in delays in acquiring the complete system state and hinder their effective collaboration. To maximize the overall throughput, we first propose a delay-tolerant multi-agent deep reinforcement learning (MADRL) algorithm that integrates a delay-penalized reward to encourage information sharing among UAVs, while jointly optimizing the UAVs' trajectory planning, network formation, and transmission control strategies. Additionally, considering information loss due to unreliable channel conditions, we further propose a spatio-temporal attention based prediction approach to recover the lost information and enhance each UAV's awareness of the network state. These two designs are envisioned to enhance the network capacity in UAV-assisted wireless networks with limited communications. The simulation results reveal that our new approach achieves over 50\% reduction in information delay and 75% throughput gain compared to the conventional MADRL. Interestingly, it is shown that improving the UAVs' information sharing will not sacrifice the network capacity. Instead, it significantly improves the learning performance and throughput simultaneously. It is also effective in reducing the need for UAVs' information exchange and thus fostering practical deployment of MADRL in UAV-assisted wireless networks.

</details>


### 123. Reasoner-Executor-Synthesizer: Scalable Agentic Architecture with Static O(1) Context Window

- **Authors:** Ivan Dobrovolskyi
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22367v1](http://arxiv.org/abs/2603.22367v1)
- **PDF:** [https://arxiv.org/pdf/2603.22367v1](https://arxiv.org/pdf/2603.22367v1)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) deployed as autonomous agents commonly use Retrieval-Augmented Generation (RAG), feeding retrieved documents into the context window, which creates two problems: the risk of hallucination grows with context length, and token cost scales linearly with dataset size. We propose the Reasoner-Executor-Synthesizer (RES) architecture, a three-layer design that strictly separates intent parsing (Reasoner), deterministic data retrieval and aggregation (Executor), and narrative generation (Synthesizer). The Executor uses zero LLM tokens and passes only fixed-size statistical summaries to the Synthesizer. We formally prove that RES achieves O(1) token complexity with respect to dataset size, and validate this on ScholarSearch, a scholarly research assistant backed by the Crossref API (130M+ articles). Across 100 benchmark runs, RES achieves a mean token cost of 1,574 tokens regardless of whether the dataset contains 42,000 or 16.3 million articles. The architecture eliminates data hallucination by construction: the LLM never sees raw records. KEYWORDS LLM agents; agentic architecture; hallucination elimination; token optimization; context window; retrieval-augmented generation; deterministic execution; scholarly metadata; Crossref API; O(1) complexity.

</details>


### 124. Adaptive Robust Estimator for Multi-Agent Reinforcement Learning

- **Authors:** Zhongyi Li, Wan Tian, Jingyu Chen, Kangyao Huang, Huiming Zhang, Hui Yang, Tao Ren, Jinyang Jiang, Yijie Peng, Yikun Ban, Fuzhen Zhuang
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21574v1](http://arxiv.org/abs/2603.21574v1)
- **PDF:** [https://arxiv.org/pdf/2603.21574v1](https://arxiv.org/pdf/2603.21574v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent collaboration has emerged as a powerful paradigm for enhancing the reasoning capabilities of large language models, yet it suffers from interaction-level ambiguity that blurs generation, critique, and revision, making credit assignment across agents difficult. Moreover, policy optimization in this setting is vulnerable to heavy-tailed and noisy rewards, which can bias advantage estimation and trigger unstable or even divergent training. To address both issues, we propose a robust multi-agent reinforcement learning framework for collaborative reasoning, consisting of two components: Dual-Agent Answer-Critique-Rewrite (DACR) and an Adaptive Robust Estimator (ARE). DACR decomposes reasoning into a structured three-stage pipeline: answer, critique, and rewrite, while enabling explicit attribution of each agent's marginal contribution to its partner's performance. ARE provides robust estimation of batch experience means during multi-agent policy optimization. Across mathematical reasoning and embodied intelligence benchmarks, even under noisy rewards, our method consistently outperforms the baseline in both homogeneous and heterogeneous settings. These results indicate stronger robustness to reward noise and more stable training dynamics, effectively preventing optimization failures caused by noisy reward signals.

</details>


### 125. Counterfactual Credit Policy Optimization for Multi-Agent Collaboration

- **Authors:** Zhongyi Li, Wan Tian, Yikun Ban, Jinju Chen, Huiming Zhang, Yang Liu, Fuzhen Zhuang
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21563v1](http://arxiv.org/abs/2603.21563v1)
- **PDF:** [https://arxiv.org/pdf/2603.21563v1](https://arxiv.org/pdf/2603.21563v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Collaborative multi-agent large language models (LLMs) can solve complex reasoning tasks by decomposing roles and aggregating diverse hypotheses. Yet, reinforcement learning (RL) for such systems is often undermined by credit assignment: a shared global reward obscures individual contributions, inflating update variance and encouraging free-riding. We introduce Counterfactual Credit Policy Optimization (CCPO), a framework that assigns agent-specific learning signals by estimating each agent's marginal contribution through counterfactual trajectories. CCPO builds dynamic counterfactual baselines that simulate outcomes with an agent's contribution removed, yielding role-sensitive advantages for policy optimization. To further improve stability under heterogeneous tasks and data distributions, we propose a global-history-aware normalization scheme that calibrates advantages using global rollout statistics. We evaluate CCPO on two collaboration topologies: a sequential Think--Reason dyad and multi-agent voting. Across mathematical and logical reasoning benchmarks, CCPO mitigates free-riding and outperforms strong multi-agent RL baselines, yielding finer-grained and more effective credit assignment for collaborative LLM training. Our code is available at https://github.com/bhai114/ccpo.

</details>


### 126. Early Discoveries of Algorithmist I: Promise of Provable Algorithm Synthesis at Scale

- **Authors:** Janardhan Kulkarni
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.22363v1](http://arxiv.org/abs/2603.22363v1)
- **PDF:** [https://arxiv.org/pdf/2603.22363v1](https://arxiv.org/pdf/2603.22363v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Designing algorithms with provable guarantees that also work well in practice remains difficult, requiring both mathematical reasoning and careful implementation. Existing approaches that bridge worst-case theory and empirical performance, such as beyond-worst-case analysis and data-driven algorithm selection, typically assume prior distributional knowledge or restrict attention to a fixed pool of algorithms. Recent progress in LLMs suggests a new possibility: provable algorithm synthesis on the fly. To study this, we built Algorithmist, an autonomous researcher agent on top of GitHub Copilot that runs a multi-agent research-and-review loop, with separate stages for idea generation, algorithm and proof development, proof-guided implementation, and review of proofs, code, and their alignment. We evaluate Algorithmist on research-level tasks in private data analysis and clustering. When asked to design practical methods that jointly satisfy privacy, approximation, and interpretability requirements, it produced provably sound and empirically effective algorithms, together with research-style writeups and audited implementations. It also found improved algorithms in some settings, explained principled barriers in others, and uncovered a subtle proof bug in prior published work. More broadly, our results suggest a new paradigm in which LLM systems generate research-paper-quality algorithmic artifacts tailored to each dataset and deployment setting. They also point to a proof-first code-synthesis paradigm, in which code is developed alongside a structured natural-language proof intermediate representation and kept aligned with it throughout synthesis.

</details>


### 127. Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation

- **Authors:** Lingzhe Zhang, Tong Jia, Mingyu Wang, Weijie Hong, Chiming Duan, Minghua He, Rongqian Wang, Xi Peng, Meiling Wang, Gong Zhang, Renhai Chen, Ying Li
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21522v1](http://arxiv.org/abs/2603.21522v1)
- **PDF:** [https://arxiv.org/pdf/2603.21522v1](https://arxiv.org/pdf/2603.21522v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLM)-based Multi-Agent Systems (MASs) have emerged as a new paradigm in software system design, increasingly demonstrating strong reasoning and collaboration capabilities. As these systems become more complex and autonomous, effective failure management is essential to ensure reliability and availability. However, existing approaches often rely on per-trace reasoning, which leads to low efficiency, and neglect historical failure patterns, limiting diagnostic accuracy. In this paper, we conduct a preliminary empirical study to demonstrate the necessity, potential, and challenges of leveraging historical failure patterns to enhance failure management in MASs. Building on this insight, we propose \textbf{EAGER}, an efficient failure management framework for multi-agent systems based on reasoning trace representation. EAGER employs unsupervised reasoning-scoped contrastive learning to encode both intra-agent reasoning and inter-agent coordination, enabling real-time step-wise failure detection, diagnosis, and reflexive mitigation guided by historical failure knowledge. Preliminary evaluations on three open-source MASs demonstrate the effectiveness of EAGER and highlight promising directions for future research in reliable multi-agent system operations.

</details>


### 128. Agentic Automation of BT-RADS Scoring: End-to-End Multi-Agent System for Standardized Brain Tumor Follow-up Assessment

- **Authors:** Mohamed Sobhi Jabal, Jikai Zhang, Dominic LaBella, Jessica L. Houk, Dylan Zhang, Jeffrey D. Rudie, Kirti Magudia, Maciej A. Mazurowski, Evan Calabrese
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21494v2](http://arxiv.org/abs/2603.21494v2)
- **PDF:** [https://arxiv.org/pdf/2603.21494v2](https://arxiv.org/pdf/2603.21494v2)
- **Categories:** cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Brain Tumor Reporting and Data System (BT-RADS) standardizes post-treatment MRI response assessment in patients with diffuse gliomas but requires complex integration of imaging trends, medication effects, and radiation timing. This study evaluates an end-to-end multi-agent large language model (LLM) and convolutional neural network (CNN) system for automated BT-RADS classification. A multi-agent LLM system combined with automated CNN-based tumor segmentation was retrospectively evaluated on 509 consecutive post-treatment glioma MRI examinations from a single high-volume center. An extractor agent identified clinical variables (steroid status, bevacizumab status, radiation date) from unstructured clinical notes, while a scorer agent applied BT-RADS decision logic integrating extracted variables with volumetric measurements. Expert reference standard classifications were established by an independent board-certified neuroradiologist. Of 509 examinations, 492 met inclusion criteria. The system achieved 374/492 (76.0%; 95% CI, 72.1%-79.6%) accuracy versus 283/492 (57.5%; 95% CI, 53.1%-61.8%) for initial clinical assessments (+18.5 percentage points; P<.001). Context-dependent categories showed high sensitivity (BT-1b 100%, BT-1a 92.7%, BT-3a 87.5%), while threshold-dependent categories showed moderate sensitivity (BT-3c 74.8%, BT-2 69.2%, BT-4 69.3%, BT-3b 57.1%). For BT-4, positive predictive value was 92.9%. The multi-agent LLM system achieved higher BT-RADS classification agreement with expert reference standard compared to initial clinical scoring, with high accuracy for context-dependent scores and high positive predictive value for BT-4 detection.

</details>


### 129. Effective Strategies for Asynchronous Software Engineering Agents

- **Authors:** Jiayi Geng, Graham Neubig
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21489v1](http://arxiv.org/abs/2603.21489v1)
- **PDF:** [https://arxiv.org/pdf/2603.21489v1](https://arxiv.org/pdf/2603.21489v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents have become increasingly capable at isolated software engineering (SWE) tasks such as resolving issues on Github. Yet long-horizon tasks involving multiple interdependent subtasks still pose challenges both with respect to accuracy, and with respect to timely completion. A natural approach to solving these long-horizon tasks in a timely manner is asynchronous multi-agent collaboration, where multiple agents work on different parts of the task at the same time. But effective application of multi-agent systems has proven surprisingly difficult: concurrent edits by multiple agents interfere with each other, dependencies are difficult to synchronize, and combining partial progress into a coherent whole is challenging. On the other hand, human developers have long relied on mature collaboration infrastructure to manage these challenges in large software projects. Inspired by these collaboration primitives, we introduce Centralized Asynchronous Isolated Delegation (CAID), a structured multi-agent coordination paradigm grounded in three core SWE primitives: centralized task delegation, asynchronous execution, and isolated workspaces. CAID constructs dependency-aware task plans through a central manager, executes subtasks concurrently in isolated workspaces, and consolidates progress via structured integration with executable test-based verification. In empirical evaluation, we find that CAID improves accuracy over single-agent baselines by 26.7% absolute on paper reproduction tasks (PaperBench) and 14.3% on Python library development tasks (Commit0). Through systematic analysis, we find that branch-and-merge is a central coordination mechanism for multi-agent collaboration, and that SWE primitives such as git worktree, git commit, and git merge enable it to be realized in a reliable and executable manner.

</details>


### 130. Unified-MAS: Universally Generating Domain-Specific Nodes for Empowering Automatic Multi-Agent Systems

- **Authors:** Hehai Lin, Yu Yan, Zixuan Wang, Bo Xu, Sudong Wang, Weiquan Huang, Ruochen Zhao, Minzhi Li, Chengwei Qin
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21475v1](http://arxiv.org/abs/2603.21475v1)
- **PDF:** [https://arxiv.org/pdf/2603.21475v1](https://arxiv.org/pdf/2603.21475v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automatic Multi-Agent Systems (MAS) generation has emerged as a promising paradigm for solving complex reasoning tasks. However, existing frameworks are fundamentally bottlenecked when applied to knowledge-intensive domains (e.g., healthcare and law). They either rely on a static library of general nodes like Chain-of-Thought, which lack specialized expertise, or attempt to generate nodes on the fly. In the latter case, the orchestrator is not only bound by its internal knowledge limits but must also simultaneously generate domain-specific logic and optimize high-level topology, leading to a severe architectural coupling that degrades overall system efficacy. To bridge this gap, we propose Unified-MAS that decouples granular node implementation from topological orchestration via offline node synthesis. Unified-MAS operates in two stages: (1) Search-Based Node Generation retrieves external open-world knowledge to synthesize specialized node blueprints, overcoming the internal knowledge limits of LLMs; and (2) Reward-Based Node Optimization utilizes a perplexity-guided reward to iteratively enhance the internal logic of bottleneck nodes. Extensive experiments across four specialized domains demonstrate that integrating Unified-MAS into four Automatic-MAS baselines yields a better performance-cost trade-off, achieving up to a 14.2% gain while significantly reducing costs. Further analysis reveals its robustness across different designer LLMs and its effectiveness on conventional tasks such as mathematical reasoning.

</details>


### 131. Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis

- **Authors:** Tae-Eun Song
- **Published:** 2026-03-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.21454v1](http://arxiv.org/abs/2603.21454v1)
- **PDF:** [https://arxiv.org/pdf/2603.21454v1](https://arxiv.org/pdf/2603.21454v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM coding benchmarks face a credibility crisis: widespread solution leakage and test quality issues undermine SWE-bench Verified, while existing detection methods--paraphrase consistency, n-gram overlap, perplexity analysis--never directly observe whether a model reasons or recalls. Meanwhile, simply repeating verification degrades accuracy: multi-turn review generates false positives faster than it discovers true errors, suggesting that structural approaches are needed.
  We introduce Cross-Context Verification (CCV), a black-box method that solves the same benchmark problem in N independent sessions and measures solution diversity, combined with the Hierarchical Cross-Context Architecture (HCCA), a multi-agent analysis framework that prevents confirmation bias through intentional information restriction across specialized analytical roles.
  On 9 SWE-bench Verified problems (45 trials, Claude Opus 4.6, temperature 0), CCV achieves perfect separation between contaminated and genuine reasoning (Mann-Whitney U=0, p approx 0.012, r = 1.0). Key findings: (1) contamination is binary--models either recall perfectly or not at all; (2) reasoning absence is a perfect discriminator; (3) 33% of prior contamination labels are false positives; (4) HCCA's independent analysis structure discovers contamination-flaw composite cases that single-analyst approaches miss. A pilot experiment extending HCCA to multi-stage verification (Worker to Verifier to Director) yields a negative result--100% sycophantic confirmation--providing further evidence that information restriction, not structural complexity, is the key mechanism. We release all code and data.

</details>



## Medrxiv (2 papers)


### 1. Artificial intelligence-driven virtual tumorboard enhances precision care in myelodysplasticsyndromes

- **Authors:** Swoboda, D. M., DeZern, A. E., England, J. T., Venugopal, S., Kehoe, T., Aubrey, B. J., Raddi, M. G., Consagra, A., Wang, J., Andreadakis, J., Rivero, G., Stahl, M., Zeidan, A. M., Haferlach, T., Brunner, A. M., Buckstein, R., Santini, V., Della Porta, M. G., Sekeres, M. A., Nazha, A.
- **Published:** 2026-03-27
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.26.26349088](https://doi.org/10.64898/2026.03.26.26349088)

- **Categories:** hematology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background: Large language models (LLMs) perform well on standardized medical exam questions, but their reliability for complex hematology decision making is uncertain. We compared four general-purpose LLMs (GPT-4o, GPT-o3, Claude Sonnet 4, and DeepSeek-V3) with a Virtual MDS Panel (VMP), a coordinated multi-agent AI system in which domain-specialized, rule-bound software agents (WHO/ICC guidelines; IPSS-R/IPSS-M; NCCN) collaborate to generate tumor-board-level recommendations. Methods: Each model generated diagnostic, prognostic, and treatment recommendations for 30 myelodysplastic syndrome cases. Nine international MDS experts from five institutions, blinded to model identity, completed 3,000 structured ratings using 5-point Likert scales for diagnosis, prognosis, and therapy and classified errors by severity. Results: General-purpose LLMs achieved modest expert ratings (overall mean scores: 3.7 for GPT-o3, 3.2 for GPT-4o, 3.1 for DeepSeek, and 3.0 for Claude) and contained major factual errors in at least 24% of responses. The VMP increased the proportion of outputs rated 4 or higher to 87% (vs. 34-66% for general-purpose models), improved mean scores to 4.3 overall (4.3 for diagnosis, 4.4 for prognosis, and 4.1 for therapy), and reduced major errors to 8%. Conclusions: In this blinded evaluation of 30 complex MDS cases, general-purpose LLMs produced clinically important errors at rates that raise safety concerns for autonomous hematology decision making. The VMP, a rule-bound, multi-agent architecture, approached expert-level accuracy supporting its potential role as an effective decision-support tool for MDS in the future.

</details>


### 2. A Clinical Guideline-Grounded Hybrid Agentic Framework for Holistic Epilepsy Management.

- **Authors:** Pham, D. K., Giritharan, D., Oliveira, G. C. d., Vo, B. Q., Verspoor, K., Law, M., Kwan, P., Ge, Z., Mehta, D.
- **Published:** 2026-03-23
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.17.26348205](https://doi.org/10.64898/2026.03.17.26348205)

- **Categories:** neurology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Epilepsy is a chronic neurological disorder requiring multi-faceted management, including seizure detection, syndrome diagnosis, prognostication, antiseizure medication recommendation, epileptogenic zone localization, and surgical outcome prediction. Although numerous deep learning approaches have been developed for individual tasks, these models are typically siloed and modality-specific (e.g., EEG for seizure detection, MRI for localization), failing to reflect the multidisciplinary nature of real-world epilepsy care, where epileptologists, neuroradiologists, neurosurgeons, neuropsychologists and neuropsychiatrists jointly interpret heterogeneous evidence to guide decisions. In this work, we propose a clinical guideline-grounded hybrid multi-agent framework for holistic epilepsy management. Heterogeneous patient data is processed through modality-specific discriminative and generative models, where textual interpretations from generative agents are combined with structured predictions from discriminative models as auxiliary guidance. This aggregated evidence is passed to a central orchestrating agent grounded in international epilepsy guidelines, which evaluates multi-modal findings within structured clinical pathways and performs iterative cross-agent coordination for evidence-informed decision-making. We evaluate our framework across two datasets spanning six epilepsy management tasks and also introduce a publicly available multi-modal, multi-task epilepsy benchmark. Results demonstrate that integrating discriminative evidence with guideline-grounded generative coordination yields more reliable and comprehensive decisions compared to conventional LLM-based and task-specific baselines. Our dataset and code is available at URL.

</details>



## Biorxiv (1 papers)


### 1. Breaking the Extraction Bottleneck: A Single AI Agent Achieves Statistical Equivalence with Human-Extracted Meta-Analysis Data Across Five Agricultural Datasets

- **Authors:** Halpern, M.
- **Published:** 2026-03-23
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.02.17.706322](https://doi.org/10.64898/2026.02.17.706322)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundData extraction is the primary bottleneck in meta-analysis, consuming weeks of researcher time with single-extractor error rates of 17.7%. Existing LLM-based systems achieve only 26-36% accuracy on continuous outcomes, and no study has validated AI-extracted continuous data against multiple independent datasets using formal equivalence testing.

MethodsA single AI agent (Claude Opus 4.6) extracted treatment means, control means, sample sizes, and variance measures from source PDFs across five published agricultural meta-analyses spanning zinc biofortification, biostimulant efficacy, biochar amendments, predator biocontrol, and elevated CO2 effects on plant mineral nutrition. Observations were matched to reference standards using an LLM-driven alignment method. Validation employed proportional TOST equivalence testing, ICC(3,1), Bland-Altman analysis, and source-type stratification.

ResultsAcross five datasets, the agent produced 1,149 matched observations from 136 papers. Pearson correlations ranged from 0.984 to 0.999. Proportional TOST confirmed statistical equivalence for all five datasets (all p < 0.05). Table-sourced observations achieved 5.5x lower median error than figure-sourced observations. Aggregate effects were reproduced within 0.01-1.61 pp of published values. Independent duplicate runs confirmed extraction stability (within 0.09-0.23 pp).

ConclusionsA single AI agent achieves statistical equivalence with human-extracted meta-analysis data across five independent agricultural datasets. The approach reduces extraction cost by approximately one to two orders of magnitude while maintaining accuracy sufficient for aggregate meta-analytic pooling.

HighlightsO_ST_ABSWhat is already knownC_ST_ABSO_LIData extraction is the primary bottleneck in meta-analysis, with single-extractor error rates of 17.7%
C_LIO_LIExisting LLM-based extraction systems achieve only 26-36% accuracy on continuous outcomes
C_LIO_LINo study has validated AI extraction against multiple independent datasets using formal equivalence testing
C_LI

What is newO_LIA single AI agent achieves statistical equivalence with human-extracted data across five agricultural meta-analyses (1,149 observations, 136 papers)
C_LIO_LILLM-driven alignment resolves the previously underappreciated bottleneck of moderator matching, improving correlations from 0.377-0.812 to 0.984-0.997 without changing extracted values
C_LIO_LITable-sourced observations achieve 5.5x lower error than figure-sourced data
C_LI

Potential impact for RSM readersO_LIProvides a validated, reproducible workflow for AI-assisted data extraction in meta-analysis
C_LIO_LIDemonstrates that most apparent "extraction error" in validation studies is actually alignment error
C_LIO_LIOffers practical quality signals (source-type labeling) for downstream meta-analysts
C_LI

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*