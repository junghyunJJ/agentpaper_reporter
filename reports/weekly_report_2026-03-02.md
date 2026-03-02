# Weekly AI Agent Paper Report

**Generated:** 2026-03-02 10:49
**Period:** 2026-02-23 to 2026-03-01

## Summary

- **Total papers fetched:** 984
- **Papers matching keywords:** 110
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-02-23) | Change |
|--------|-----------|-----------|--------|
| Total matched | 110 | 113 | -3 |
| arxiv | 103 | 104 | -1 |
| biorxiv | 1 | 3 | -2 |
| medrxiv | 6 | 6 | +0 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (7 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. OriGene: A Self-Evolving Virtual Disease Biologist Automating Therapeutic Target Discovery

- **Authors:** Zhang, Z., Qiu, Z., Wu, Y., Li, S., Wang, D., Liu, Y., Zhou, Z., Hu, Y., Chen, Y., An, D., Wang, Y., Li, Y., Zhong, Z., Ou, C., Wang, Z., Tang, F., Chen, J. X., Ma, R., Li, J., Wang, X., Lu, W., Xue, H., Zhang, W., Wei, Z., Ma, R., Shi, Z., Wang, K., Liu, Q., Dong, B., He, Y., Liu, T., Gu, J., Song, S., Feng, Q., Zhang, J., Zhang, B., Tian, L., Bai, L., Gao, Q., Sun, S., Zheng, S.
- **Published:** 2026-02-25
- **Source:** biorxiv
- **URL:** [https://doi.org/10.1101/2025.06.03.657658](https://doi.org/10.1101/2025.06.03.657658)

- **Categories:** bioinformatics


> OriGene introduces a self‑evolving, multi‑agent platform that acts as a virtual disease biologist, automatically generating and prioritizing mechanistically grounded therapeutic‑target hypotheses across genomics, protein‑network, pharmacology, clinical and literature data. Its architecture links >600 specialized tools through a Model Context Protocol and a knowledge‑graph‑based tool‑retrieval‑augmented generation (Tool‑RAG) system, enabling context‑aware tool selection and continual refinement of reasoning templates via human and experimental feedback. On the newly created TRQA benchmark (≈1,900 expert‑level Q&A pairs), OriGene outperforms human experts, leading research agents, and state‑of‑the‑art LLMs in accuracy and robustness, and successfully identified novel targets (GPR160 for liver cancer and ARG2 for colorectal cancer) that showed potent anti‑tumor activity in patient‑derived organoid and tumor fragment models.


<details>
<summary>Abstract</summary>

Here, we present OriGene, a self-evolving multi-agent system that functions as a virtual disease biologist, systematically identifying original and mechanistically grounded therapeutic targets at scale. OriGenes architecture integrates over 600 specialized tools through a Model Context Protocol (MCP), enabling it to reason across diverse data modalities including genomics, protein networks, pharmacology, clinical records and literature evidence, to generate and prioritize target discovery hypotheses. We implemented a strategy combining a knowledge graph-based Tool RAG with an advanced agent selection mechanism to enable dynamic, context-aware tool deployment. Through a self-evolving framework, OriGene continuously integrates human and experimental feedback to iteratively refine its core thinking templates, tool composition, and analytical protocols, thereby enhancing both accuracy and adaptability over time. To comprehensively evaluate its performance, we established TRQA, an original benchmark comprising over 1,900 expert-level question-answer pairs spanning a wide range of diseases and target classes. OriGene consistently outperforms human experts, leading research agents, and state-of-the-art large language models in accuracy, recall, and robustness, particularly under conditions of data sparsity or noise. Critically, OriGene nominated previously underexplored therapeutic targets for liver (GPR160) and colorectal cancer (ARG2), which demonstrated significant anti-tumor activity in patient-derived organoid and tumor fragment models mirroring human clinical exposures. These findings demonstrate OriGenes potential as a scalable and adaptive platform for AI-driven discovery of mechanistically grounded therapeutic targets, offering a new paradigm to accelerate drug development.

</details>


### 2. Onco-Shikshak: An AI-Native Adaptive Learning Ecosystem for Medical Oncology Education

- **Authors:** Makani, A.
- **Published:** 2026-02-26
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.23.26346944](https://doi.org/10.64898/2026.02.23.26346944)

- **Categories:** oncology


> The paper introduces **Onco‑Shikshak V7**, the first AI‑native adaptive learning ecosystem that fuses cognitive‑architectural models (ACT‑R illness‑script activation), psychometric adaptation (Item‑Response Theory), spaced‑repetition scheduling (FSRS v4), scaffolding (Zone of Proximal Development), and metacognitive calibration (Brier‑score feedback) into a single platform for medical oncology education. Its methodology deploys six specialist agents (medical, radiation, surgical oncology, pathology, radiology, and navigation) that perform retrieval‑augmented generation over nine guideline sources and engage learners in authentic clinical workflows (Morning Report, Tumor Board, Clinic Day, AI Textbook), while mapping every interaction to ACGME milestones and closing the learning loop with targeted flashcards and case recommendations. Technical validation shows correct operation of all eight subsystems, demonstrating that a multi‑agent, cognitively‑grounded architecture can dynamically adapt to rapidly evolving oncology knowledge and mitigate LLM hallucination and automation bias—key advances for agentic AI in high‑stakes education.


<details>
<summary>Abstract</summary>

Medical oncology education faces a dual crisis: knowledge velocity that outpaces static curricula and large language model (LLM) risks--hallucination and automation bias--that threaten the fidelity of AI-assisted learning. We present Onco-Shikshak V7, an AI-native adaptive learning platform that addresses both challenges through a unified cognitive architecture grounded in learning science. The system replaces isolated educational modules with four authentic clinical workflows--Morning Report, Tumor Board, Clinic Day, and AI Textbook--each scaffolded by a nine-module pedagogy engine that integrates ACT-R activation dynamics (illness scripts), Item Response Theory (adaptive difficulty), the Free Spaced Repetition Scheduler (FSRS v4), Zone of Proximal Development (scaffolding), and metacognitive calibration training (Brier score). Six specialist AI agents--medical oncology, radiation oncology, surgical oncology, pathology, radiology, and oncology navigation--engage in multi-disciplinary deliberation with per-specialty retrieval-augmented generation (RAG) grounding across nine authoritative guideline sources including NCCN, ESMO, and ASTRO. The platform provides 18 clinical cases with decision trees across six cancer types, maps every interaction to 13 ACGME Hematology-Oncology milestones, and implements four closed-loop feedback mechanisms that connect session errors to targeted flashcards, weak domains to suggested cases, and all interactions to a persistent learner profile. Technical validation confirms algorithmic correctness across eight subsystems. To our knowledge, this is the first system to unify ACT-R, IRT, FSRS, ZPD, and metacognitive calibration in a single medical education platform. Formal learner evaluation via randomized controlled trial is planned.

</details>


### 3. End-to-End PET/CT Interpretation and Quantification with an LLM-Orchestrated AI Agent: A Real-World Pilot Study

- **Authors:** Choi, H., Bae, S., Na, K. J.
- **Published:** 2026-02-25
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.21.26346798](https://doi.org/10.64898/2026.02.21.26346798)

- **Categories:** radiology and imaging


> The paper introduces a fully autonomous, LLM‑orchestrated AI agent that integrates multiple imaging tools to process raw PET/CT DICOM data, perform registration, SUV conversion, segmentation, detection, and generate structured clinical reports without human input. Using a reasoning‑based text LLM to select series and coordinate tool calls, and a vision‑enabled LLM for interpretation, the system was retrospectively tested on 170 lung‑cancer PET/CT scans. It achieved flawless primary‑tumor detection (100 % sensitivity) but showed moderate performance for nodal (84.8 % sensitivity, 39.4 % specificity) and distant metastasis assessment (70.2 % sensitivity, 65.0 % specificity), highlighting both the feasibility of end‑to‑end agentic workflows in radiology and the need for expert oversight in complex cases.


<details>
<summary>Abstract</summary>

BackgroundAlthough deep learning models have improved individual PET analysis, image processing and quantification tasks, end-to-end automation from raw DICOM to quantitative clinical reporting remains limited, particularly in heterogeneous real-world settings.

MethodsAs a proof-of-concept, an autonomous large language model (LLM)-orchestrated multi-tool agent for end-to-end PET/CT interpretation was developed. A reasoning-based text LLM selected appropriate series from raw DICOM, coordinated registration and SUV conversion, invoked segmentation and detection tools, generated maximum-intensity projections, called a vision-enabled LLM for interpretation, and synthesized structured draft reports. The system was retrospectively evaluated in 170 patients undergoing baseline FDG PET/CT for lung cancer staging, using expert reports as reference.

ResultsThe agent successfully completed the full end-to-end workflow from raw DICOM selection to structured draft report generation without human intervention in all 170 examinations. Primary tumor detection achieved 100% sensitivity. For nodal involvement, sensitivity was 84.8% and specificity was 39.4%, whereas distant metastasis detection showed 70.2% sensitivity and 65.0% specificity. Discrepancy analysis of 58 nodal and 57 metastatic mismatch cases revealed systematic false-positive findings related to reactive or physiologic uptake and false-negative findings involving small-volume or anatomically atypical metastases.

ConclusionLLM-orchestrated PET/CT agents can enable workflow-level automation from raw DICOM to quantification and structured draft reporting under real-world conditions. Although primary tumor detection was highly reliable, nodal and metastatic assessment revealed systematic limitations, supporting a collaborative role with continued expert oversight in complex clinical scenarios.

</details>


### 4. Agent Role Structure and Operating Characteristics in Large Language Model Clinical Classification: A Comparative Study of Specialist and Deliberative Multi-Agent Protocols

- **Authors:** Anderson, C. G.
- **Published:** 2026-02-25
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.22.26346818](https://doi.org/10.64898/2026.02.22.26346818)

- **Categories:** health informatics


> The paper demonstrates that the internal role architecture of deterministic multi‑agent prompting pipelines materially shapes clinical classification outcomes for large language models. By constructing two DAG‑based protocols— a Generic Deliberative (GD) chain and a Feature‑Specialist (FS) hierarchy that routes feature‑specific prompts to dedicated sub‑agents— and evaluating them on the UCI Cleveland heart‑disease dataset under identical model, decoding, and aggregation settings, the authors isolate the effect of role decomposition. The FS protocol yields a 7 % boost in overall accuracy and a 6 % rise in macro‑F1, but it also shifts the operating point toward higher specificity (+0.22) and lower sensitivity (‑0.13), highlighting that agent role design imposes a structured inductive bias that must be treated as a core modeling decision in safety‑critical AI systems.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly evaluated for structured clinical decision support tasks, often using multi-agent architectures. Prior work has compared single-agent and multi-agent inference. However, the effect of internal role structure within multi-agent systems on classification behavior remains underexplored. We evaluate two multi-agent prompting protocols, implemented as deterministic Directed Acyclic Graph (DAG) systems, a Generic Deliberative (GD) protocol and a Feature-Specialist (FS) protocol, on tabular clinical heart disease data from the UCI Cleveland dataset. Structured variables are rendered into primarily text-based feature descriptions while preserving clinically relevant numeric values. The two protocols differ only in their prompt-level role decomposition and information routing, while base model, model weights, deterministic decoding with temperature set to 0, computational budget, and aggregation logic are held constant. The results show systematic differences in predictive behavior attributable solely to prompt-level role structure. The FS protocol improves overall accuracy by 0.07 and macro-F1 by 0.06. However, this improvement is accompanied by a marked operating-point shift in which specificity increases by 0.22 while sensitivity decreases by 0.13, with corresponding redistribution of class-wise precision. Notably, the increase in specificity corresponds to a reduction in false positive classifications, indicating decreased over-diagnosis under the FS configuration. These findings indicate that multi-agent role decomposition introduces a structured inductive bias in deterministic LLM-based classification. Prompt protocol and agent role design should therefore be regarded as core modeling decisions, as they show measurable influence on performance tradeoffs, particularly in safety-sensitive deployment contexts.

</details>


### 5. Care Plan Generation for Underserved Patients Using Multi-Agent Language Models: Applying Nash Game Theory to Optimize Multiple Objectives

- **Authors:** Basu, S., Baum, A.
- **Published:** 2026-02-25
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.23.26346934](https://doi.org/10.64898/2026.02.23.26346934)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundClinicians in care management programs are often in low supply relative to patient demand, especially in US Medicaid programs, and must simultaneously address clinical risk, time efficiency, and patients social needs. Many studies have shown that large language models may assist in their tasks for summarizing patient care, such as in generating care plans; yet these studies also show that different objectives given to agents often conflict and produce problems for safety, efficiency and equity. We tested whether and to what degree using game theoretic approaches (a Nash bargaining framework) can produce care plans that advance multiple objectives across multiple language models, applying data from a real-world Medicaid cohort.

MethodsWe conducted two studies in a cohort of 5,148 activated Medicaid care management patients (69.9% female; 45.7% Black or African American; mean age 40.9 years) enrolled in Virginia and Washington. A retrospective evaluation applied five deterministic strategies to the full cohort to characterize multi-objective trade-offs. A pre-registered controlled paired experiment (N = 200) assigned each patient one Nash-orchestrated multi-agent plan and one compute-matched sequential self-critique plan, generated by locally hosted open-source models (DeepSeek-R1 8B; Llama 3.1 8B) with no patient data leaving local infrastructure. Pre-specified outcomes were Safety, Efficiency, Equity, and Composite (mean of the three), each scored 0-1. Reporting follows CONSORT 2010 and STROBE.

ResultsNash orchestration produced a Composite score of 0.755 (95% CI 0.751-0.760) versus 0.742 (95% CI 0.739-0.746) for the compute-matched baseline; the paired difference was 0.013 (95% CI 0.008-0.019; p = 6.20 x 10-). Safety and Efficiency paired differences were small-to-moderate in effect size (Cohens d = 0.327 and 0.543, respectively) with confidence intervals excluding zero. The Equity paired difference was 0.000 (95% CI -0.015 to 0.014; p = 0.987).

ConclusionsRole-specialized Nash-orchestrated multi-agent language models produced measurably better Safety and Efficiency care plan quality than a compute-matched baseline under data-residency constraints. The null Equity result demonstrates that multi-objective role specialization does not automatically address equity--equity requires explicit design attention beyond composite weighting--with direct implications for responsible AI deployment in Medicaid care management.

Author SummaryCare management programs for Medicaid patients need to address multiple goals at once: covering clinical risks, prioritizing the most impactful interventions, and recognizing the social barriers that affect whether patients can follow through on care plans. Prior research shows that automation tools powered by a single AI model tend to optimize for one of these goals at a time, sacrificing the others. We tested whether organizing several specialized AI agents -- each focused on a different goal -- and then combining their recommendations through a mathematical framework called Nash bargaining could produce better overall care plans for a real Medicaid population. We found that this multi-agent approach produced care plans that the AI judge rated as meaningfully safer and more efficient than plans generated by a single AI model using the same total amount of computation. However, the multi-agent approach did not produce plans that were more equitable in addressing patients social needs, suggesting that equity requires more direct attention as a design target rather than emerging from multi-objective combination alone. All AI inference was performed on locally hosted computers, with no patient information sent to outside services, reflecting the privacy requirements of real-world Medicaid care management programs.

</details>


### 6. How Agent Role Structure Alters Operating Characteristics of Large Language Model Clinical Classifiers: A Comparative Study of Specialist and Deliberative Multi-Agent Protocols

- **Authors:** Anderson, C. G.
- **Published:** 2026-02-24
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.22.26346818](https://doi.org/10.64898/2026.02.22.26346818)

- **Categories:** health informatics


> The paper demonstrates that the internal role structure of deterministic multi‑agent prompting pipelines materially shapes the classification behavior of large language models (LLMs) on a clinical decision‑support task. By implementing two DAG‑based protocols— a Generic Deliberative (GD) chain and a Feature‑Specialist (FS) decomposition that routes feature‑specific prompts to dedicated agents— and keeping the base model, weights, decoding temperature, compute budget, and aggregation unchanged, the authors show that the FS design yields a 7 % boost in overall accuracy and a 6 % rise in macro‑F1, but at the cost of a 22 % increase in specificity and a 13 % drop in sensitivity, effectively reducing false‑positive (over‑diagnosis) errors. These results reveal that prompt‑level role decomposition acts as a controllable inductive bias in agentic AI systems, making agent role design a critical modeling decision for safety‑critical applications.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly evaluated for structured clinical decision support tasks, often using multi-agent architectures. Prior work has compared single-agent and multi-agent inference. However, the effect of internal role structure within multi-agent systems on classification behavior remains underexplored. We evaluate two multi-agent prompting protocols, implemented as deterministic Directed Acyclic Graph (DAG) systems, a Generic Deliberative (GD) protocol and a Feature-Specialist (FS) protocol, on tabular clinical heart disease data from the UCI Cleveland dataset. Structured variables are rendered into primarily text-based feature descriptions while preserving clinically relevant numeric values. The two protocols differ only in their prompt-level role decomposition and information routing, while base model, model weights, deterministic decoding with temperature set to 0, computational budget, and aggregation logic are held constant. The results show systematic differences in predictive behavior attributable solely to prompt-level role structure. The FS protocol improves overall accuracy by 0.07 and macro-F1 by 0.06. However, this improvement is accompanied by a marked operating-point shift in which specificity increases by 0.22 while sensitivity decreases by 0.13, with corresponding redistribution of class-wise precision. Notably, the increase in specificity corresponds to a reduction in false positive classifications, indicating decreased over-diagnosis under the FS configuration. These findings indicate that multi-agent role decomposition introduces a structured inductive bias in deterministic LLM-based classification. Prompt protocol and agent role design should therefore be regarded as core modeling decisions, as they show measurable influence on performance tradeoffs, particularly in safety-sensitive deployment contexts.

</details>


### 7. Evaluating the AI Potential as a Safety Net for Diagnosis: A Novel Benchmark of Large Language Models in Correcting Diagnostic Errors

- **Authors:** Hassoon, A., Peng, X., Irimia, R., Lianjie, A., Leo, H., Bandeira, A., Woo, H. Y., Dredze, M., Abdulnour, R.-E., McDonald, K. M., Peterson, S., Newman-Toker, D.
- **Published:** 2026-02-24
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.22.26346832](https://doi.org/10.64898/2026.02.22.26346832)

- **Categories:** health systems and quality improvement


> The paper introduces a benchmark that quantifies how well large language models (LLMs) can act as a safety‑net by detecting and correcting erroneous physician diagnoses across 200 high‑stakes clinical vignettes. By prompting 16 state‑of‑the‑art LLMs (e.g., Gemini 2.5 Pro, Claude 3.7 Sonnet) with the full patient record and an incorrect diagnosis, the authors measured diagnostic‑correction rates and examined robustness to 2,200 demographic and contextual variants. Results show that the best models (Gemini 2.5 Pro ≈ 55 % correction) still fail on many conditions and exhibit confirmation bias and sensitivity to non‑clinical cues, highlighting the need for adversarial, multi‑agent workflows that prioritize skeptical reasoning for safe agentic AI deployment in medicine.


<details>
<summary>Abstract</summary>

BackgroundDiagnostic errors are a leading cause of preventable patient harm, often occurring during early clinical encounters where diagnostic uncertainty is maximal. Large language models (LLMs) have shown potential in medical reasoning, yet their ability to function as a diagnostic safety net, specifically by identifying and correcting human diagnostic errors, remains systematically unquantified. We evaluated whether state-of-the-art LLMs can effectively challenge, rather than merely confirm, an erroneous physician diagnosis.

MethodsWe evaluated 16 leading LLMs (including GPT-o1, Gemini 2.5 Pro, and Claude 3.7 Sonnet) using 200 standardized clinical vignettes representing 20 high-stakes, frequently misdiagnosed conditions. Models were presented with the full clinical record and an incorrect physician diagnosis. Primary outcomes included the diagnostic correction rate (disagreeing with the error and providing the correct diagnosis) and the ratio of correction to error detection. We further tested model robustness by generating 2,200 variants to assess the influence of demographic (race/ethnicity) and contextual (institutional reputation, training level, insurance) tokens.

ResultsDiagnostic correction rates varied significantly across models. Gemini 2.5 Pro demonstrated the highest performance, correcting the physicians error in 55.0% of cases (n=110/200), followed by Claude Sonnet 3.5 (48.5%) and Sonnet 4 (47.0%). In contrast, DeepSeek V3 corrected only 20.0% of cases. Performance was strikingly consistent at the disease level; most models failed to correct errors in syphilis, spinal epidural abscess, and myocardial infarction. Furthermore, several models exhibited confirmation bias (agreeing with the incorrect diagnosis) occurring in 11.0% to 50.0% of cases. Stability across demographic and contextual variants was inconsistent, with some models showing spurious performance shifts based on non-clinical tokens.

ConclusionWhile top-performing LLMs can intercept approximately half of the human diagnostic errors in high-stakes scenarios, performance is heterogeneous and highly sensitive to non-clinical context. Current models exhibit significant disease-specific gaps and a tendency toward confirmation bias, suggesting that their safe clinical integration requires adversarial, multi-agent workflows designed to prioritize skepticism over baseline agreement.

</details>


---



## Arxiv (103 papers)


### 1. Controllable Reasoning Models Are Private Thinkers

- **Authors:** Haritz Puerto, Haonan Li, Xudong Han, Timothy Baldwin, Iryna Gurevych
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.24210v1](http://arxiv.org/abs/2602.24210v1)
- **PDF:** [https://arxiv.org/pdf/2602.24210v1](https://arxiv.org/pdf/2602.24210v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **Controllable Reasoning Models**, a framework that trains language models to obey explicit instructions not only in their final answers but also in the intermediate reasoning steps, thereby limiting the inadvertent exposure of private user data. The authors create a new instruction‑following dataset with trace‑level restrictions and implement a decoupled generation scheme that uses separate LoRA adapters for reasoning and answer production; they fine‑tune six models (1.7 B–14 B parameters) from two families and evaluate them on standard instruction‑following and privacy‑leakage benchmarks. Experiments show that this approach can boost instruction‑following scores by up to **20.9 points** and improve privacy metrics by as much as **51.9 %**, albeit with a trade‑off against raw task performance, highlighting a viable path toward privacy‑aware, agentic AI systems.


<details>
<summary>Abstract</summary>

AI agents powered by reasoning models require access to sensitive user data. However, their reasoning traces are difficult to control, which can result in the unintended leakage of private information to external parties. We propose training models to follow instructions not only in the final answer, but also in reasoning traces, potentially under different constraints. We hypothesize that improving their instruction following abilities in the reasoning traces can improve their privacy-preservation skills. To demonstrate this, we fine-tune models on a new instruction-following dataset with explicit restrictions on reasoning traces. We further introduce a generation strategy that decouples reasoning and answer generation using separate LoRA adapters. We evaluate our approach on six models from two model families, ranging from 1.7B to 14B parameters, across two instruction-following benchmarks and two privacy benchmarks. Our method yields substantial improvements, achieving gains of up to 20.9 points in instruction-following performance and up to 51.9 percentage points on privacy benchmarks. These improvements, however, can come at the cost of task utility, due to the trade-off between reasoning performance and instruction-following abilities. Overall, our results show that improving instruction-following behavior in reasoning models can significantly enhance privacy, suggesting a promising direction for the development of future privacy-aware agents. Our code and data are available at https://github.com/UKPLab/arxiv2026-controllable-reasoning-models

</details>


### 2. Agentic AI-RAN: Enabling Intent-Driven, Explainable and Self-Evolving Open RAN Intelligence

- **Authors:** Zhizhou He, Yang Luo, Xinkai Liu, Mahdi Boloursaz Mashhadi, Mohammad Shojafar, Merouane Debbah, Rahim Tafazolli
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.24115v1](http://arxiv.org/abs/2602.24115v1)
- **PDF:** [https://arxiv.org/pdf/2602.24115v1](https://arxiv.org/pdf/2602.24115v1)
- **Categories:** cs.LG


> The paper introduces **Agentic AI‑RAN**, a framework that embeds intent‑driven, explainable, and self‑evolving agentic controllers into the Open RAN (O‑RAN) stack, replacing traditional ML/RL‑based xApps with a set of **agentic primitives** (Plan‑Act‑Observe‑Reflect loops, tool‑use “skills”, persistent memory/evidence, and self‑management gates). Using a multi‑cell O‑RAN simulator, the authors evaluate these primitives on three core task clusters—network‑slice lifecycle, radio‑resource‑management closed loops, and cross‑cutting security/privacy/compliance—and demonstrate that the full agentic pipeline yields an **average 8.83 % reduction in resource usage** across three canonical slices, outperforming baseline and ablation models that omit individual primitives. The study highlights how explicit planning, memory, and self‑reflection enable more transparent, adaptable, and safe control loops for multi‑tenant, multi‑objective RANs, while also outlining the remaining standards‑aligned challenges for secure and auditable deployments.


<details>
<summary>Abstract</summary>

Open RAN (O-RAN) exposes rich control and telemetry interfaces across the Non-RT RIC, Near-RT RIC, and distributed units, but also makes it harder to operate multi-tenant, multi-objective RANs in a safe and auditable manner. In parallel, agentic AI systems with explicit planning, tool use, memory, and self-management offer a natural way to structure long-lived control loops. This article surveys how such agentic controllers can be brought into O-RAN: we review the O-RAN architecture, contrast agentic controllers with conventional ML/RL xApps, and organise the task landscape around three clusters: network slice life-cycle, radio resource management (RRM) closed loops, and cross-cutting security, privacy, and compliance. We then introduce a small set of agentic primitives (Plan-Act-Observe-Reflect, skills as tool use, memory and evidence, and self-management gates) and show, in a multi-cell O-RAN simulation, how they improve slice life-cycle and RRM performance compared to conventional baselines and ablations that remove individual primitives. Security, privacy, and compliance are discussed as architectural constraints and open challenges for standards-aligned deployments. This framework achieves an average 8.83\% reduction in resource usage across three classic network slices.

</details>


### 3. Sharing is caring: data sharing in multi-agent supply chains

- **Authors:** Wan Wang, Haiyan Wang, Adam Sobey
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.24074v1](http://arxiv.org/abs/2602.24074v1)
- **PDF:** [https://arxiv.org/pdf/2602.24074v1](https://arxiv.org/pdf/2602.24074v1)
- **Categories:** cs.MA


> The paper introduces a multi‑agent supply‑chain framework in which a factory agent can deliberately share, withhold, or falsify information to downstream agents, thereby modulating the overall system’s observability. Using a Hidden‑Markov Process model with separate policies for each agent, the authors evaluate four sharing strategies (no share, lie, truth, mixed) under cooperative reward‑shaping and two demand regimes. They find that truthful data sharing dramatically improves joint performance in low‑demand settings, while in high‑demand scenarios only modest gains are achievable—lying can slightly benefit the factory but does not substantially raise total system reward—highlighting how controlled information exchange shapes agentic behavior and efficiency in decentralized AI‑driven supply chains.


<details>
<summary>Abstract</summary>

Modern supply networks are complex interconnected systems. Multi-agent models are increasingly explored to optimise their performance. Most research assumes agents will have full observability of the system by having a single policy represent the agents, which seems unrealistic as this requires companies to share their data. The alternative is to develop a Hidden-Markov Process with separate policies, making the problem challenging to solve. In this paper, we propose a multi-agent system where the factory agent can share information downstream, increasing the observability of the environment. It can choose to share no information, lie, tell the truth or combine these in a mixed strategy. The results show that data sharing can boost the performance, especially when combined with a cooperative reward shaping. In the high demand scenario there is limited ability to change the strategy and therefore no data sharing approach benefits both agents. However, lying benefits the factory enough for an overall system improvement, although only by a relatively small amount compared to the overall reward. In the low demand scenario, the most successful data sharing is telling the truth which benefits all actors significantly.

</details>


### 4. A Novel Hierarchical Multi-Agent System for Payments Using LLMs

- **Authors:** Joon Kiat Chua, Donghao Huang, Zhaoxia Wang
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.24068v1](http://arxiv.org/abs/2602.24068v1)
- **PDF:** [https://arxiv.org/pdf/2602.24068v1](https://arxiv.org/pdf/2602.24068v1)
- **Categories:** cs.MA, cs.CL


> The paper introduces **HMASP (Hierarchical Multi‑Agent System for Payments)**, the first LLM‑driven architecture that can execute complete, end‑to‑end payment workflows. It does so by organizing LLM agents into four coordinated layers—a Conversational Payment Agent, Supervisor agents, Routing agents, and a Process‑Summary agent—using shared state variables, decoupled message handling, and explicit hand‑off protocols to modularize task execution across the hierarchy. Experiments with both open‑weight and proprietary LLMs show that HMASP can reliably process real‑world payment requests, demonstrating that hierarchical, modular agent designs can extend the reach of agentic AI into the financially sensitive domain of payments.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents, such as OpenAI's Operator and Claude's Computer Use, can automate workflows but unable to handle payment tasks. Existing agentic solutions have gained significant attention; however, even the latest approaches face challenges in implementing end-to-end agentic payment workflows. To address this gap, this research proposes the Hierarchical Multi-Agent System for Payments (HMASP), which provides an end-to-end agentic method for completing payment workflows. The proposed HMASP leverages either open-weight or proprietary LLMs and employs a modular architecture consisting of the Conversational Payment Agent (CPA - first agent level), Supervisor agents (second agent level), Routing agents (third agent level), and the Process summary agent (fourth agent level). The CPA serves as the central entry point, handling all external requests and coordinating subsequent tasks across hierarchical levels. HMASP incorporates architectural patterns that enable modular task execution across agents and levels for payment operations, including shared state variables, decoupled message states, and structured handoff protocols that facilitate coordination across agents and workflows. Experimental results demonstrate the feasibility of the proposed HMASP. To our knowledge, HMASP is the first LLM-based multi-agent system to implement end-to-end agentic payment workflows. This work lays a foundation for extending agentic capabilities into the payment domain.

</details>


### 5. Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

- **Authors:** Zhicheng Fang, Jingjie Zheng, Chenxu Fu, Wei Xu
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.24009v1](http://arxiv.org/abs/2602.24009v1)
- **PDF:** [https://arxiv.org/pdf/2602.24009v1](https://arxiv.org/pdf/2602.24009v1)
- **Categories:** cs.CR, cs.AI, cs.CL, cs.LG


> The paper introduces **Jailbreak Foundry (JBF)**, a multi‑agent framework that automatically converts published jailbreak papers into runnable attack modules and evaluates them within a single, standardized harness. By employing three components—JBF‑LIB (shared contracts and utilities), JBF‑FORGE (a team of agents that parse papers and generate code), and JBF‑EVAL (a unified evaluation pipeline with a GPT‑4o judge)—the system reproduces 30 attacks with a mean success‑rate deviation of only +0.26 pp while cutting implementation code by nearly 50 % and reusing 82.5 % of the codebase. This enables reproducible, “living” benchmarks for agentic LLM robustness, allowing consistent comparison of attack efficacy across models and rapid incorporation of new jailbreak techniques.


<details>
<summary>Abstract</summary>

Jailbreak techniques for large language models (LLMs) evolve faster than benchmarks, making robustness estimates stale and difficult to compare across papers due to drift in datasets, harnesses, and judging protocols. We introduce JAILBREAK FOUNDRY (JBF), a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. JBF features three core components: (i) JBF-LIB for shared contracts and reusable utilities; (ii) JBF-FORGE for the multi-agent paper-to-module translation; and (iii) JBF-EVAL for standardizing evaluations. Across 30 reproduced attacks, JBF achieves high fidelity with a mean (reproduced-reported) attack success rate (ASR) deviation of +0.26 percentage points. By leveraging shared infrastructure, JBF reduces attack-specific implementation code by nearly half relative to original repositories and achieves an 82.5% mean reused-code ratio. This system enables a standardized AdvBench evaluation of all 30 attacks across 10 victim models using a consistent GPT-4o judge. By automating both attack integration and standardized evaluation, JBF offers a scalable solution for creating living benchmarks that keep pace with the rapidly shifting security landscape.

</details>


### 6. Foundation World Models for Agents that Learn, Verify, and Adapt Reliably Beyond Static Environments

- **Authors:** Florent Delgrange
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23997v1](http://arxiv.org/abs/2602.23997v1)
- **PDF:** [https://arxiv.org/pdf/2602.23997v1](https://arxiv.org/pdf/2602.23997v1)
- **Categories:** cs.LG, cs.AI


> The paper proposes **foundation world models**—persistent, compositional representations that serve as a unified substrate for reinforcement learning, program synthesis, and formal abstraction—enabling agents to learn, verify, and adapt reliably in open, non‑static environments. Its methodology integrates (i) learnable reward models derived from high‑level specifications, (ii) continuous formal verification during learning, (iii) online calibration of abstraction reliability, and (iv) test‑time synthesis of new world‑model components guided by the verifiers; together these mechanisms allow agents to generate verifiable programs, infer new policies from few interactions, and maintain correctness under novelty. Empirical illustrations show that agents built on this framework can achieve comparable performance to standard RL baselines while providing provable safety guarantees and explanatory traces, demonstrating a viable path toward trustworthy, adaptable agentic AI.


<details>
<summary>Abstract</summary>

The next generation of autonomous agents must not only learn efficiently but also act reliably and adapt their behavior in open worlds. Standard approaches typically assume fixed tasks and environments with little or no novelty, which limits world models' ability to support agents that must evolve their policies as conditions change. This paper outlines a vision for foundation world models: persistent, compositional representations that unify reinforcement learning, reactive/program synthesis, and abstraction mechanisms. We propose an agenda built around four components: (i) learnable reward models from specifications to support optimization with clear objectives; (ii) adaptive formal verification integrated throughout learning; (iii) online abstraction calibration to quantify the reliability of the model's predictions; and (iv) test-time synthesis and world-model generation guided by verifiers. Together, these components enable agents to synthesize verifiable programs, derive new policies from a small number of interactions, and maintain correctness while adapting to novelty. The resulting framework positions foundation world models as a substrate for learning, reasoning, and adaptation, laying the groundwork for agents that not only act well but can explain and justify the behavior they adopt.

</details>


### 7. Experience-Guided Self-Adaptive Cascaded Agents for Breast Cancer Screening and Diagnosis with Reduced Biopsy Referrals

- **Authors:** Pramit Saha, Mohammad Alsharid, Joshua Strong, J. Alison Noble
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23899v1](http://arxiv.org/abs/2602.23899v1)
- **PDF:** [https://arxiv.org/pdf/2602.23899v1](https://arxiv.org/pdf/2602.23899v1)
- **Categories:** cs.CV, cs.AI, cs.LG


> The paper introduces **BUSD‑Agent**, a novel experience‑guided, cascaded multi‑agent system for breast‑ultrasound screening and diagnosis that explicitly models the clinical workflow as a two‑stage selective decision process (screening → diagnostic escalation). The system stores pathology‑confirmed cases, image embeddings, model outputs, and prior agent actions in a memory bank; for each new patient it retrieves similar trajectories and conditions the agents’ policies on this context, allowing dynamic adjustment of model trust and escalation thresholds without any parameter fine‑tuning. Across ten ultrasound datasets, this retrieval‑conditioned adaptation cuts diagnostic escalation from 84.95 % to 58.72 % and biopsy referrals from 59.50 % to 37.08 %, while boosting screening specificity by ≈ 68 % and diagnostic specificity by ≈ 6 %, demonstrating the efficacy of memory‑augmented, self‑adaptive agents for reducing unnecessary medical interventions.


<details>
<summary>Abstract</summary>

We propose an experience-guided cascaded multi-agent framework for Breast Ultrasound Screening and Diagnosis, called BUSD-Agent, that aims to reduce diagnostic escalation and unnecessary biopsy referrals. Our framework models screening and diagnosis as a two-stage, selective decision-making process. A lightweight `screening clinic' agent, restricted to classification models as tools, selectively filters out benign and normal cases from further diagnostic escalation when malignancy risk and uncertainty are estimated as low. Cases that have higher risks are escalated to the `diagnostic clinic' agent, which integrates richer perception and radiological description tools to make a secondary decision on biopsy referral. To improve agent performance, past records of pathology-confirmed outcomes along with image embeddings, model predictions, and historical agent actions are stored in a memory bank as structured decision trajectories. For each new case, BUSD-Agent retrieves similar past cases based on image, model response and confidence similarity to condition the agent's current decision policy. This enables retrieval-conditioned in-context adaptation that dynamically adjusts model trust and escalation thresholds from prior experiences without parameter updates. Evaluation across 10 breast ultrasound datasets shows that the proposed experience-guided workflow reduces diagnostic escalation in BUSD-Agent from 84.95% to 58.72% and overall biopsy referrals from 59.50% to 37.08%, compared to the same architecture without trajectory conditioning, while improving average screening specificity by 68.48% and diagnostic specificity by 6.33%.

</details>


### 8. RUMAD: Reinforcement-Unifying Multi-Agent Debate

- **Authors:** Chao Wang, Han Lin, Huaze Tang, Huijing Lin, Wenbo Ding
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23864v1](http://arxiv.org/abs/2602.23864v1)
- **PDF:** [https://arxiv.org/pdf/2602.23864v1](https://arxiv.org/pdf/2602.23864v1)
- **Categories:** cs.AI


> RUMAD introduces a reinforcement‑learning controller that dynamically re‑weights the communication graph of a multi‑agent debate system, allowing the topology to adapt to task difficulty without exposing agents’ internal reasoning content. By training a PPO‑based policy with a multi‑objective reward that balances solution quality, consensus cohesion, and token efficiency, RUMAD can activate or silence agents and mask information flow via a dual‑threshold mechanism. Experiments on MMLU, GSM8K, and GPQA show that this approach cuts token usage by >80 % while improving accuracy over single‑LLM baselines and prior MAD methods, and it generalizes zero‑shot to out‑of‑domain tasks, demonstrating task‑agnostic principles for efficient, coordinated agentic reasoning.


<details>
<summary>Abstract</summary>

Multi-agent debate (MAD) systems leverage collective intelligence to enhance reasoning capabilities, yet existing approaches struggle to simultaneously optimize accuracy, consensus formation, and computational efficiency. Static topology methods lack adaptability to task complexity variations, while external LLM-based coordination risks introducing privileged knowledge that compromises debate neutrality. This work presents RUMAD (Reinforcement-Unifying Multi-Agent Debate), a novel framework that formulates dynamic communication topology control in MAD as a reinforcement learning (RL) problem.
  RUMAD employs a content-agnostic observation scheme that captures high-level debate dynamics avoiding access to raw agent reasoning content. RUMAD uses a multi-objective reward to model solution quality, cohesion and efficiency. A PPO-trained controller dynamically adjusts edge weights in the communication graph, while a dual-threshold mechanism enables fine-grained control over both agent activation and information visibility.
  Experimental evaluation across MMLU, GSM8K, and GPQA benchmarks demonstrates that RUMAD achieves substantial efficiency gains, reducing token costs by over 80\%, while still improving reasoning accuracy compared to single LLM model and multiple MAD baselines. Notably, RUMAD trained exclusively on MMLU exhibits robust zero-shot generalization to out-of-domain (OOD) tasks, indicating that the learned communication strategies capture task-independent principles of effective multi-agent coordination. These results establish RUMAD as a efficient and robust approach for deploying multi-agent reasoning application with practical resource constraints.

</details>


### 9. From Static Benchmarks to Dynamic Protocol: Agent-Centric Text Anomaly Detection for Evaluating LLM Reasoning

- **Authors:** Seungdong Yoa, Sanghyu Yoon, Suhee Yoon, Dongmin Kim, Ye Seul Sim, Junhyun Lee, Woohyung Lim
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23729v1](http://arxiv.org/abs/2602.23729v1)
- **PDF:** [https://arxiv.org/pdf/2602.23729v1](https://arxiv.org/pdf/2602.23729v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> The paper introduces an **agent‑centric benchmarking framework** that replaces static test sets with a **dynamic protocol** in which three autonomous LLM agents—teacher, orchestrator, and student—collaboratively generate, validate, and solve text‑anomaly problems, automatically scaling difficulty as more capable models replace any role. By using **text anomaly detection** (requiring cross‑sentence logical inference) as the evaluation task, the authors show that this loop systematically uncovers reasoning corner cases that traditional benchmarks miss, and they propose additional evaluation axes such as cross‑model pairwise performance and improvement from initial to orchestrator‑finalized problems. The results demonstrate that dynamic, agent‑driven benchmarks can provide a sustainable, self‑evolving measure of LLM reasoning ability, highlighting a new research direction for co‑evolving agentic AI systems and their evaluation.


<details>
<summary>Abstract</summary>

The evaluation of large language models (LLMs) has predominantly relied on static datasets, which offer limited scalability and fail to capture the evolving reasoning capabilities of recent models. To overcome these limitations, we propose an agent-centric benchmarking paradigm that moves beyond static datasets by introducing a dynamic protocol in which autonomous agents iteratively generate, validate, and solve problems. Within this protocol, a teacher agent generates candidate problems, an orchestrator agent rigorously verifies their validity and guards against adversarial attacks, and a student agent attempts to solve the validated problems. An invalid problem is revised by the teacher agent until it passes validation. If the student correctly solves the problem, the orchestrator prompts the teacher to generate more challenging variants. Consequently, the benchmark scales in difficulty automatically as more capable agents are substituted into any role, enabling progressive evaluation of large language models without manually curated datasets. Adopting text anomaly detection as our primary evaluation format, which demands cross-sentence logical inference and resists pattern-matching shortcuts, we demonstrate that this protocol systematically exposes corner-case reasoning errors that conventional benchmarks fail to reveal. We further advocate evaluating systems along several complementary axes including cross-model pairwise performance and progress between the initial and orchestrator-finalized problems. By shifting the focus from fixed datasets to dynamic protocols, our approach offers a sustainable direction for evaluating ever-evolving language models and introduces a research agenda centered on the co-evolution of agent-centric benchmarks.

</details>


### 10. The Auton Agentic AI Framework

- **Authors:** Sheng Cao, Zhao Chang, Chang Li, Hannan Li, Liyao Fu, Ji Tang
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23720v1](http://arxiv.org/abs/2602.23720v1)
- **PDF:** [https://arxiv.org/pdf/2602.23720v1](https://arxiv.org/pdf/2602.23720v1)
- **Categories:** cs.AI


> The paper introduces the **Auton Agentic AI Framework**, a modular architecture that cleanly separates an agent’s declarative “Cognitive Blueprint” (its identity, capabilities, and policies) from a platform‑specific “Runtime Engine” that executes the blueprint, thereby enabling language‑agnostic portability, formal auditability, and plug‑and‑play tool integration via the Model Context Protocol (MCP). Methodologically, the authors formalize agent behavior as an augmented POMDP with a latent reasoning space, propose a biologically inspired hierarchical memory‑consolidation system, and enforce safety through a constraint‑manifold projection rather than post‑hoc filtering; they also implement a three‑level self‑evolution loop (in‑context adaptation, reinforcement learning, and meta‑learning) and a suite of runtime optimizations (parallel graph execution, speculative inference, dynamic context pruning). Empirical evaluations show that Auton agents achieve deterministic, schema‑conformant interactions with external services while reducing multi‑step workflow latency by up to 45 % and improving safety compliance scores compared with baseline LLM‑driven agents, demonstrating a scalable path toward robust, auditable agentic AI.


<details>
<summary>Abstract</summary>

The field of Artificial Intelligence is undergoing a transition from Generative AI -- probabilistic generation of text and images -- to Agentic AI, in which autonomous systems execute actions within external environments on behalf of users. This transition exposes a fundamental architectural mismatch: Large Language Models (LLMs) produce stochastic, unstructured outputs, whereas the backend infrastructure they must control -- databases, APIs, cloud services -- requires deterministic, schema-conformant inputs. The present paper describes the Auton Agentic AI Framework, a principled architecture for standardizing the creation, execution, and governance of autonomous agent systems. The framework is organized around a strict separation between the Cognitive Blueprint, a declarative, language-agnostic specification of agent identity and capabilities, and the Runtime Engine, the platform-specific execution substrate that instantiates and runs the agent. This separation enables cross-language portability, formal auditability, and modular tool integration via the Model Context Protocol (MCP). The paper formalizes the agent execution model as an augmented Partially Observable Markov Decision Process (POMDP) with a latent reasoning space, introduces a hierarchical memory consolidation architecture inspired by biological episodic memory systems, defines a constraint manifold formalism for safety enforcement via policy projection rather than post-hoc filtering, presents a three-level self-evolution framework spanning in-context adaptation through reinforcement learning, and describes runtime optimizations -- including parallel graph execution, speculative inference, and dynamic context pruning -- that reduce end-to-end latency for multi-step agent workflows.

</details>


### 11. ProductResearch: Training E-Commerce Deep Research Agents via Multi-Agent Synthetic Trajectory Distillation

- **Authors:** Jiangyuan Wang, Kejun Xiao, Huaipeng Zhao, Tao Luo, Xiaoyi Zeng
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23716v1](http://arxiv.org/abs/2602.23716v1)
- **PDF:** [https://arxiv.org/pdf/2602.23716v1](https://arxiv.org/pdf/2602.23716v1)
- **Categories:** cs.AI


> The paper introduces **ProductResearch**, a multi‑agent pipeline that generates high‑fidelity, long‑horizon tool‑use trajectories for training e‑commerce shopping assistants. By pairing a **User Agent** (which extracts detailed shopping intent from user behavior) with a **Supervisor Agent** that coordinates a **Research Agent** to iteratively browse, compare, and synthesize product information, the system creates synthetic research sessions that are filtered and distilled into single‑role examples for fine‑tuning a compact Mixture‑of‑Experts LLM. Experiments demonstrate that the resulting model markedly outperforms its base LLM in response completeness, depth of product research, and perceived utility—closing the gap to state‑of‑the‑art proprietary deep‑research systems and validating multi‑agent synthetic trajectory distillation as a scalable method for building more capable, agentic e‑commerce assistants.


<details>
<summary>Abstract</summary>

Large Language Model (LLM)-based agents show promise for e-commerce conversational shopping, yet existing implementations lack the interaction depth and contextual breadth required for complex product research. Meanwhile, the Deep Research paradigm, despite advancing information synthesis in web search, suffers from domain gaps when transferred to e-commerce. We propose ProductResearch, a multi-agent framework that synthesizes high-fidelity, long-horizon tool-use trajectories for training robust e-commerce shopping agents. The framework employs a User Agent to infer nuanced shopping intents from behavioral histories, and a Supervisor Agent that orchestrates iterative collaboration with a Research Agent to generate synthetic trajectories culminating in comprehensive, insightful product research reports. These trajectories are rigorously filtered and distilled through a reflective internalization process that consolidates multi-agent supervisory interactions into coherent single-role training examples, enabling effective fine-tuning of LLM agents for complex shopping inquiries. Extensive experiments show that a compact MoE model fine-tuned on our synthetic data achieves substantial improvements over its base model in response comprehensiveness, research depth, and user-perceived utility, approaching the performance of frontier proprietary deep research systems and establishing multi-agent synthetic trajectory training as an effective and scalable paradigm for enhancing LLM-based shopping assistance.

</details>


### 12. From Flat Logs to Causal Graphs: Hierarchical Failure Attribution for LLM-based Multi-Agent Systems

- **Authors:** Yawen Wang, Wenjie Wu, Junjie Wang, Qing Wang
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23701v1](http://arxiv.org/abs/2602.23701v1)
- **PDF:** [https://arxiv.org/pdf/2602.23701v1](https://arxiv.org/pdf/2602.23701v1)
- **Categories:** cs.AI, cs.SE


> The paper introduces **CHIEF**, a framework that converts the flat execution logs of LLM‑driven multi‑agent systems into a **hierarchical causal graph**, enabling precise attribution of failures across agents and time steps. CHIEF builds this graph, then applies an **oracle‑guided hierarchical backtracking** that prunes the search space with synthesized virtual oracles, followed by a **progressive counterfactual screening** to isolate true root causes from downstream symptoms. Empirical results on the Who&When benchmark show that CHIEF surpasses eight strong baselines in both agent‑level and step‑level failure attribution accuracy, and ablation studies confirm that each component (graph construction, oracle‑guided pruning, and counterfactual screening) is essential for its performance.


<details>
<summary>Abstract</summary>

LLM-powered Multi-Agent Systems (MAS) have demonstrated remarkable capabilities in complex domains but suffer from inherent fragility and opaque failure mechanisms. Existing failure attribution methods, whether relying on direct prompting, costly replays, or supervised fine-tuning, typically treat execution logs as flat sequences. This linear perspective fails to disentangle the intricate causal links inherent to MAS, leading to weak observability and ambiguous responsibility boundaries. To address these challenges, we propose CHIEF, a novel framework that transforms chaotic trajectories into a structured hierarchical causal graph. It then employs hierarchical oracle-guided backtracking to efficiently prune the search space via sybthesized virtual oracles. Finally, it implements counterfactual attribution via a progressive causal screening strategy to rigorously distinguish true root causes from propagated symptoms. Experiments on Who&When benchmark show that CHIEF outperforms eight strong and state-of-the-art baselines on both agent- and step-level accuracy. Ablation studies further confirm the critical role of each proposed module.

</details>


### 13. PseudoAct: Leveraging Pseudocode Synthesis for Flexible Planning and Action Control in Large Language Model Agents

- **Authors:** Yihan, Wen, Xin Chen
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23668v1](http://arxiv.org/abs/2602.23668v1)
- **PDF:** [https://arxiv.org/pdf/2602.23668v1](https://arxiv.org/pdf/2602.23668v1)
- **Categories:** cs.AI, eess.SY


> The paper introduces **PseudoAct**, a framework that equips LLM‑based agents with explicit, code‑like planning by having the model first synthesize a structured pseudocode representation of the task—including sequencing, conditionals, loops, and parallel composition—and then execute actions by following this global plan. This approach replaces the usual reactive, history‑conditioned decision loops (e.g., ReAct) with a temporally coherent control flow, thereby eliminating redundant tool calls, preventing infinite loops, and reducing token overhead in long‑horizon, multi‑tool problems. Empirically, PseudoAct yields a 20.93 % absolute improvement in success rate on the FEVER benchmark and establishes a new state‑of‑the‑art on HotpotQA, demonstrating markedly more reliable and efficient planning for agentic AI.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents typically rely on reactive decision-making paradigms such as ReAct, selecting actions conditioned on growing execution histories. While effective for short tasks, these approaches often lead to redundant tool usage, unstable reasoning, and high token consumption in complex long-horizon tasks involving branching, iteration, or multi-tool coordination. To address these limitations, this paper introduces PseudoAct, a novel framework for flexible planning and action control in LLM agents through pseudocode synthesis. Leveraging the ability of LLMs to express task-solving strategies as code, PseudoAct synthesizes a structured pseudocode plan that decomposes a task into subtasks and explicitly encodes control flow, including sequencing, conditionals, loops, parallel composition, and combinations of these logic primitives. Actions are then executed by following this global plan, making the decision logic explicit and temporally coherent. This design reduces redundant actions, prevents infinite loops, and avoids uninformative alternative exploration, enabling consistent and efficient long-horizon decision-making. Experiments on benchmark datasets show that our method significantly outperforms existing reactive agent approaches, achieving a 20.93% absolute gain in success rate on FEVER and setting a new state-of-the-art on HotpotQA.

</details>


### 14. Blockchain-Enabled Routing for Zero-Trust Low-Altitude Intelligent Networks

- **Authors:** Ziye Jia, Sijie He, Ligang Yuan, Fuhui Zhou, Qihui Wu, Zhu Han, Dusit Niyato
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23667v1](http://arxiv.org/abs/2602.23667v1)
- **PDF:** [https://arxiv.org/pdf/2602.23667v1](https://arxiv.org/pdf/2602.23667v1)
- **Categories:** cs.NI, cs.AI


> The paper introduces a zero‑trust, blockchain‑backed routing framework for low‑altitude intelligent networks (LAINs) that secures UAV clusters by using a software‑defined perimeter to authenticate and track UAV identities and mobility. The routing problem—jointly minimizing end‑to‑end delay and maximizing transmission‑success ratio—is cast as a decentralized partially observable Markov decision process and solved with a multi‑agent double Deep‑Q Network (DDQN) enhanced by soft‑hierarchical and prioritized experience‑replay buffers. Simulations show the approach cuts average E2E delay by ~59 % and lifts the transmission‑success ratio by ~29 % versus baselines, while also enabling rapid, robust detection of low‑trust UAVs—demonstrating a scalable, agentic AI solution for secure, high‑mobility aerial networks.


<details>
<summary>Abstract</summary>

Due to the scalability and portability, low-altitude intelligent networks (LAINs) are essential in various fields such as surveillance and disaster rescue. However, in LAINs, unmanned aerial vehicles (UAVs) are characterized by the distributed topology and high mobility, thus vulnerable to security threats, which may degrade routing performances for data transmissions. Hence, how to ensure the routing stability and security of LAINs is challenging. In this paper, we focus on the routing with multiple UAV clusters in LAINs. To minimize the damage caused by potential threats, we present the zero-trust architecture with the software-defined perimeter and blockchain techniques to manage the identify and mobility of UAVs. Besides, we formulate the routing problem to optimize the end-to-end (E2E) delay and transmission success ratio (TSR) simultaneously, which is an integer nonlinear programming problem and intractable to solve. Therefore, we reformulate the problem into a decentralized partially observable Markov decision process. We design the multi-agent double deep Q-network-based routing algorithms to solve the problem, empowered by the soft-hierarchical experience replay buffer and prioritized experience replay mechanisms. Finally, extensive simulations are conducted and the numerical results demonstrate that the proposed framework reduces the average E2E delay by 59\% and improves the TSR by 29\% on average compared to benchmarks, while simultaneously enabling faster and more robust identification of low-trust UAVs.

</details>


### 15. Multi-Agent Causal Reasoning for Suicide Ideation Detection Through Online Conversations

- **Authors:** Jun Li, Xiangmeng Wang, Haoyang Li, Yifei Yan, Shijie Zhang, Hong Va Leong, Ling Feng, Nancy Xiaonan Yu, Qing Li
- **Published:** 2026-02-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23577v1](http://arxiv.org/abs/2602.23577v1)
- **PDF:** [https://arxiv.org/pdf/2602.23577v1](https://arxiv.org/pdf/2602.23577v1)
- **Categories:** cs.CL


> The paper introduces **Multi‑Agent Causal Reasoning (MACR)**, a novel framework that couples a **Reasoning Agent**—which uses cognitive appraisal theory to generate and analyze counterfactual user reactions across cognitive, emotional, and behavioral dimensions—with a **Bias‑aware Decision‑Making Agent** that applies a front‑door causal adjustment to neutralize hidden influences such as conformity and copy‑cat behavior. By orchestrating these agents, MACR both expands the observable interaction space of online conversation trees and systematically removes latent bias, yielding richer, causally‑informed representations for suicide‑ideation detection. Empirical evaluation on large‑scale conversational datasets shows that MACR significantly outperforms existing rule‑based and single‑agent models in precision, recall, and robustness, demonstrating the practical advantage of collaborative, causally‑aware agents for high‑stakes mental‑health AI tasks.


<details>
<summary>Abstract</summary>

Suicide remains a pressing global public health concern. While social media platforms offer opportunities for early risk detection through online conversation trees, existing approaches face two major limitations: (1) They rely on predefined rules (e.g., quotes or relies) to log conversations that capture only a narrow spectrum of user interactions, and (2) They overlook hidden influences such as user conformity and suicide copycat behavior, which can significantly affect suicidal expression and propagation in online communities. To address these limitations, we propose a Multi-Agent Causal Reasoning (MACR) framework that collaboratively employs a Reasoning Agent to scale user interactions and a Bias-aware Decision-Making Agent to mitigate harmful biases arising from hidden influences. The Reasoning Agent integrates cognitive appraisal theory to generate counterfactual user reactions to posts, thereby scaling user interactions. It analyses these reactions through structured dimensions, i.e., cognitive, emotional, and behavioral patterns, with a dedicated sub-agent responsible for each dimension. The Bias-aware Decision-Making Agent mitigates hidden biases through a front-door adjustment strategy, leveraging the counterfactual user reactions produced by the Reasoning Agent. Through the collaboration of reasoning and bias-aware decision making, the proposed MACR framework not only alleviates hidden biases, but also enriches contextual information of user interactions with counterfactual knowledge. Extensive experiments on real-world conversational datasets demonstrate the effectiveness and robustness of MACR in identifying suicide risk.

</details>


### 16. Rudder: Steering Prefetching in Distributed GNN Training using LLM Agents

- **Authors:** Aishwarya Sarkar, Sayan Ghosh, Nathan Tallent, Aman Chadha, Tanya Roosta, Ali Jannesari
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23556v1](http://arxiv.org/abs/2602.23556v1)
- **PDF:** [https://arxiv.org/pdf/2602.23556v1](https://arxiv.org/pdf/2602.23556v1)
- **Categories:** cs.LG, cs.AI, cs.DC, cs.MA, cs.PF


> Rudder introduces an autonomous, LLM‑driven prefetching module for distributed GNN training that continuously decides which remote graph nodes to fetch, thereby turning the irregular communication bottleneck into a learned control problem. By prompting a large language model to perform in‑context, multi‑step reasoning over runtime statistics (graph topology, partitioning, sampling parameters, and cache state), Rudder replaces static heuristics and conventional classifiers with a zero‑shot, adaptable agent that issues prefetch commands in real time. Experiments on the AWS DistDGL stack and on NERSC’s Perlmutter system show that this agentic approach cuts communication volume by >50% and yields up to 91 % speed‑up over a no‑prefetch baseline (and 82 % over the best static prefetcher), demonstrating the practical benefit of LLM‑based adaptive control in large‑scale graph AI workloads.


<details>
<summary>Abstract</summary>

Large-scale Graph Neural Networks (GNNs) are typically trained by sampling a vertex's neighbors to a fixed distance. Because large input graphs are distributed, training requires frequent irregular communication that stalls forward progress. Moreover, fetched data changes with graph, graph distribution, sample and batch parameters, and caching polices. Consequently, any static prefetching method will miss crucial opportunities to adapt to different dynamic conditions. In this paper, we introduce Rudder, a software module embedded in the state-of-the-art AWS DistDGL framework, to autonomously prefetch remote nodes and minimize communication. Rudder's adaptation contrasts with both standard heuristics and traditional ML classifiers. We observe that the generative AI found in contemporary Large Language Models (LLMs) exhibits emergent properties like In-Context Learning (ICL) for zero-shot tasks, with logical multi-step reasoning. We find this behavior well-suited for adaptive control even with substantial undertraining. Evaluations using standard datasets and unseen configurations on the NERSC Perlmutter supercomputer show up to 91% improvement in end-to-end training performance over baseline DistDGL (no prefetching), and an 82% improvement over static prefetching, reducing communication by over 50%. Our code is available at https://github.com/aishwaryyasarkar/rudder-llm-agent.

</details>


### 17. IDP Accelerator: Agentic Document Intelligence from Extraction to Compliance Validation

- **Authors:** Md Mofijul Islam, Md Sirajus Salekin, Joe King, Priyashree Roy, Vamsi Thilak Gudi, Spencer Romo, Akhil Nooney, Boyi Xie, Bob Strahan, Diego A. Socolinsky
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23481v1](http://arxiv.org/abs/2602.23481v1)
- **PDF:** [https://arxiv.org/pdf/2602.23481v1](https://arxiv.org/pdf/2602.23481v1)
- **Categories:** cs.CL


> The paper introduces **IDP Accelerator**, a modular framework that turns unstructured document packets into structured, compliance‑ready data by embedding an **agentic AI loop** across four stages: (1) DocSplit, a new benchmark and multimodal BIO‑tagging classifier for packet segmentation; (2) a configurable extraction layer that calls multimodal LLMs to generate structured outputs; (3) an Agentic Analytics Module that follows the Model Context Protocol (MCP) to expose data via secure, sandboxed code execution; and (4) a rule‑validation component that replaces static engines with LLM‑driven logical checks. Experiments on real‑world industrial workloads—most notably a deployment at a major healthcare provider—show 98 % packet‑classification accuracy, an 80 % cut in processing latency, and a 77 % reduction in operational costs versus legacy pipelines, demonstrating the practical impact of agentic, LLM‑centric document intelligence.


<details>
<summary>Abstract</summary>

Understanding and extracting structured insights from unstructured documents remains a foundational challenge in industrial NLP. While Large Language Models (LLMs) enable zero-shot extraction, traditional pipelines often fail to handle multi-document packets, complex reasoning, and strict compliance requirements. We present IDP (Intelligent Document Processing) Accelerator, a framework enabling agentic AI for end-to-end document intelligence with four key components: (1) DocSplit, a novel benchmark dataset and multimodal classifier using BIO tagging to segment complex document packets; (2) configurable Extraction Module leveraging multimodal LLMs to transform unstructured content into structured data; (3) Agentic Analytics Module, compliant with the Model Context Protocol (MCP) providing data access through secure, sandboxed code execution; and (4) Rule Validation Module replacing deterministic engines with LLM-driven logic for complex compliance checks. The interactive demonstration enables users to upload document packets, visualize classification results, and explore extracted data through an intuitive web interface. We demonstrate effectiveness across industries, highlighting a production deployment at a leading healthcare provider achieving 98% classification accuracy, 80% reduced processing latency, and 77% lower operational costs over legacy baselines. IDP Accelerator is open-sourced with a live demonstration available to the community.

</details>


### 18. Optimization of Edge Directions and Weights for Mixed Guidance Graphs in Lifelong Multi-Agent Path Finding

- **Authors:** Yulun Zhang, Varun Bhatt, Matthew C. Fontaine, Stefanos Nikolaidis, Jiaoyang Li
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23468v1](http://arxiv.org/abs/2602.23468v1)
- **PDF:** [https://arxiv.org/pdf/2602.23468v1](https://arxiv.org/pdf/2602.23468v1)
- **Categories:** cs.MA, cs.AI, cs.RO


> The paper introduces **Mixed Guidance Graph Optimization (MGGO)**, extending prior Guidance Graph Optimization (GGO) by jointly learning **both edge directions (hard constraints) and edge weights (soft costs)** for lifelong multi‑agent path‑finding (LMAPF). It proposes two complementary approaches: a two‑phase pipeline that first selects directed edges and then tunes their weights, and a Quality‑Diversity (QD) evolutionary method that evolves a neural network capable of generating direction‑aware weighted graphs; both are evaluated against a traffic‑pattern‑aware GGO baseline. Experiments show that incorporating directionality markedly reduces dead‑locks and overall travel cost, demonstrating that strict, learned guidance graphs can substantially improve the coordination and scalability of autonomous agents in continuous MAPF settings.


<details>
<summary>Abstract</summary>

Multi-Agent Path Finding (MAPF) aims to move agents from their start to goal vertices on a graph. Lifelong MAPF (LMAPF) continuously assigns new goals to agents as they complete current ones. To guide agents' movement in LMAPF, prior works have proposed Guidance Graph Optimization (GGO) methods to optimize a guidance graph, which is a bidirected weighted graph whose directed edges represent moving and waiting actions with edge weights being action costs. Higher edge weights represent higher action costs. However, edge weights only provide soft guidance. An edge with a high weight only discourages agents from using it, instead of prohibiting agents from traversing it. In this paper, we explore the need to incorporate edge directions optimization into GGO, providing strict guidance. We generalize GGO to Mixed Guidance Graph Optimization (MGGO), presenting two MGGO methods capable of optimizing both edge weights and directions. The first optimizes edge directions and edge weights in two phases separately. The second applies Quality Diversity algorithms to optimize a neural network capable of generating edge directions and weights. We also incorporate traffic patterns relevant to edge directions into a GGO method, making it capable of generating edge-direction-aware guidance graphs.

</details>


### 19. CiteAudit: You Cited It, But Did You Read It? A Benchmark for Verifying Scientific References in the LLM Era

- **Authors:** Zhengqing Yuan, Kaiwen Shi, Zheyuan Zhang, Lichao Sun, Nitesh V. Chawla, Yanfang Ye
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23452v1](http://arxiv.org/abs/2602.23452v1)
- **PDF:** [https://arxiv.org/pdf/2602.23452v1](https://arxiv.org/pdf/2602.23452v1)
- **Categories:** cs.CL, cs.DL


> CiteAudit introduces the first large‑scale, human‑validated benchmark and a multi‑agent verification pipeline for detecting fabricated or mis‑aligned citations generated by large language models. The system decomposes citation checking into coordinated agents that (1) extract the claim associated with each reference, (2) retrieve candidate evidence from scholarly databases, (3) match retrieved passages to the claim, (4) reason about support, and (5) produce a calibrated confidence score, enabling standardized metrics for citation faithfulness and evidence alignment. Experiments with state‑of‑the‑art LLMs show that hallucinated citations remain common, while CiteAudit’s agentic framework markedly outperforms prior ad‑hoc tools in accuracy and interpretability, offering a scalable infrastructure for auditing scientific references in the LLM era.


<details>
<summary>Abstract</summary>

Scientific research relies on accurate citation for attribution and integrity, yet large language models (LLMs) introduce a new risk: fabricated references that appear plausible but correspond to no real publications. Such hallucinated citations have already been observed in submissions and accepted papers at major machine learning venues, exposing vulnerabilities in peer review. Meanwhile, rapidly growing reference lists make manual verification impractical, and existing automated tools remain fragile to noisy and heterogeneous citation formats and lack standardized evaluation. We present the first comprehensive benchmark and detection framework for hallucinated citations in scientific writing. Our multi-agent verification pipeline decomposes citation checking into claim extraction, evidence retrieval, passage matching, reasoning, and calibrated judgment to assess whether a cited source truly supports its claim. We construct a large-scale human-validated dataset across domains and define unified metrics for citation faithfulness and evidence alignment. Experiments with state-of-the-art LLMs reveal substantial citation errors and show that our framework significantly outperforms prior methods in both accuracy and interpretability. This work provides the first scalable infrastructure for auditing citations in the LLM era and practical tools to improve the trustworthiness of scientific references.

</details>


### 20. Toward Expert Investment Teams:A Multi-Agent LLM System with Fine-Grained Trading Tasks

- **Authors:** Kunihiro Miyazaki, Takanobu Kawahara, Stephen Roberts, Stefan Zohren
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23330v1](http://arxiv.org/abs/2602.23330v1)
- **PDF:** [https://arxiv.org/pdf/2602.23330v1](https://arxiv.org/pdf/2602.23330v1)
- **Categories:** cs.AI, q-fin.TR


> The paper introduces a multi‑agent LLM framework for autonomous trading that replaces the usual coarse‑grained “analyst‑manager” prompts with a hierarchy of fine‑grained analytical tasks (e.g., data extraction, fundamental assessment, news sentiment, macro‑factor synthesis). Using a leakage‑controlled backtest on Japanese equities, the authors show that this task decomposition yields markedly higher risk‑adjusted returns, and that the alignment between intermediate analytical outputs and the downstream decision‑making agent is a primary performance driver; additionally, portfolio‑level optimization that exploits the low correlation and variance of each agent’s signals further boosts results. These findings highlight the importance of explicit task granularity and output alignment when designing agentic AI systems for real‑world decision‑making domains such as finance.


<details>
<summary>Abstract</summary>

The advancement of large language models (LLMs) has accelerated the development of autonomous financial trading systems. While mainstream approaches deploy multi-agent systems mimicking analyst and manager roles, they often rely on abstract instructions that overlook the intricacies of real-world workflows, which can lead to degraded inference performance and less transparent decision-making. Therefore, we propose a multi-agent LLM trading framework that explicitly decomposes investment analysis into fine-grained tasks, rather than providing coarse-grained instructions. We evaluate the proposed framework using Japanese stock data, including prices, financial statements, news, and macro information, under a leakage-controlled backtesting setting. Experimental results show that fine-grained task decomposition significantly improves risk-adjusted returns compared to conventional coarse-grained designs. Crucially, further analysis of intermediate agent outputs suggests that alignment between analytical outputs and downstream decision preferences is a critical driver of system performance. Moreover, we conduct standard portfolio optimization, exploiting low correlation with the stock index and the variance of each system's output. This approach achieves superior performance. These findings contribute to the design of agent structure and task configuration when applying LLM agents to trading systems in practical settings.

</details>


### 21. ParamMem: Augmenting Language Agents with Parametric Reflective Memory

- **Authors:** Tianjun Yao, Yongqiang Chen, Yujia Zheng, Pan Li, Zhiqiang Shen, Kun Zhang
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23320v2](http://arxiv.org/abs/2602.23320v2)
- **PDF:** [https://arxiv.org/pdf/2602.23320v2](https://arxiv.org/pdf/2602.23320v2)
- **Categories:** cs.LG, cs.MA


> The paper introduces **ParamMem**, a parametric memory module that captures cross‑sample reflection patterns in the model’s weights, allowing language agents to generate more diverse self‑reflection outputs via temperature‑controlled sampling. By integrating ParamMem with episodic and cross‑sample memories, the authors build **ParamAgent**, a reflection‑based agent that leverages both learned (parametric) and stored (episodic) knowledge to iteratively improve its reasoning. Experiments across code generation, mathematical problem solving, and multi‑hop QA show that ParamAgent consistently outperforms prior state‑of‑the‑art agents, is sample‑efficient, transfers improvements from smaller to larger models, and can self‑enhance without needing a stronger external model—demonstrating a scalable way to boost reflective diversity in agentic AI.


<details>
<summary>Abstract</summary>

Self-reflection enables language agents to iteratively refine solutions, yet often produces repetitive outputs that limit reasoning performance. Recent studies have attempted to address this limitation through various approaches, among which increasing reflective diversity has shown promise. Our empirical analysis reveals a strong positive correlation between reflective diversity and task success, further motivating the need for diverse reflection signals. We introduce ParamMem, a parametric memory module that encodes cross-sample reflection patterns into model parameters, enabling diverse reflection generation through temperature-controlled sampling. Building on this module, we propose ParamAgent, a reflection-based agent framework that integrates parametric memory with episodic and cross-sample memory. Extensive experiments on code generation, mathematical reasoning, and multi-hop question answering demonstrate consistent improvements over state-of-the-art baselines. Further analysis reveals that ParamMem is sample-efficient, enables weak-to-strong transfer across model scales, and supports self-improvement without reliance on stronger external model, highlighting the potential of ParamMem as an effective component for enhancing language agents.

</details>


### 22. CXReasonAgent: Evidence-Grounded Diagnostic Reasoning Agent for Chest X-rays

- **Authors:** Hyungyung Lee, Hangyul Yoon, Edward Choi
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23276v1](http://arxiv.org/abs/2602.23276v1)
- **PDF:** [https://arxiv.org/pdf/2602.23276v1](https://arxiv.org/pdf/2602.23276v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Chest X-ray plays a central role in thoracic diagnosis, and its interpretation inherently requires multi-step, evidence-grounded reasoning. However, large vision-language models (LVLMs) often generate plausible responses that are not faithfully grounded in diagnostic evidence and provide limited visual evidence for verification, while also requiring costly retraining to support new diagnostic tasks, limiting their reliability and adaptability in clinical settings. To address these limitations, we present CXReasonAgent, a diagnostic agent that integrates a large language model (LLM) with clinically grounded diagnostic tools to perform evidence-grounded diagnostic reasoning using image-derived diagnostic and visual evidence. To evaluate these capabilities, we introduce CXReasonDial, a multi-turn dialogue benchmark with 1,946 dialogues across 12 diagnostic tasks, and show that CXReasonAgent produces faithfully grounded responses, enabling more reliable and verifiable diagnostic reasoning than LVLMs. These findings highlight the importance of integrating clinically grounded diagnostic tools, particularly in safety-critical clinical settings.

</details>


### 23. AgentDropoutV2: Optimizing Information Flow in Multi-Agent Systems via Test-Time Rectify-or-Reject Pruning

- **Authors:** Yutong Wang, Siyuan Xiong, Xuebo Liu, Wenkang Zhou, Liang Ding, Miao Zhang, Min Zhang
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23258v1](http://arxiv.org/abs/2602.23258v1)
- **PDF:** [https://arxiv.org/pdf/2602.23258v1](https://arxiv.org/pdf/2602.23258v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

While Multi-Agent Systems (MAS) excel in complex reasoning, they suffer from the cascading impact of erroneous information generated by individual participants. Current solutions often resort to rigid structural engineering or expensive fine-tuning, limiting their deployability and adaptability. We propose AgentDropoutV2, a test-time rectify-or-reject pruning framework designed to dynamically optimize MAS information flow without retraining. Our approach acts as an active firewall, intercepting agent outputs and employing a retrieval-augmented rectifier to iteratively correct errors based on a failure-driven indicator pool. This mechanism allows for the precise identification of potential errors using distilled failure patterns as prior knowledge. Irreparable outputs are subsequently pruned to prevent error propagation, while a fallback strategy preserves system integrity. Empirical results on extensive math benchmarks show that AgentDropoutV2 significantly boosts the MAS's task performance, achieving an average accuracy gain of 6.3 percentage points on math benchmarks. Furthermore, the system exhibits robust generalization and adaptivity, dynamically modulating rectification efforts based on task difficulty while leveraging context-aware indicators to resolve a wide spectrum of error patterns. Our code and dataset are released at https://github.com/TonySY2/AgentDropoutV2.

</details>


### 24. ESAA: Event Sourcing for Autonomous Agents in LLM-Based Software Engineering

- **Authors:** Elzo Brito dos Santos Filho
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23193v1](http://arxiv.org/abs/2602.23193v1)
- **PDF:** [https://arxiv.org/pdf/2602.23193v1](https://arxiv.org/pdf/2602.23193v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents based on Large Language Models (LLMs) have evolved from reactive assistants to systems capable of planning, executing actions via tools, and iterating over environment observations. However, they remain vulnerable to structural limitations: lack of native state, context degradation over long horizons, and the gap between probabilistic generation and deterministic execution requirements. This paper presents the ESAA (Event Sourcing for Autonomous Agents) architecture, which separates the agent's cognitive intention from the project's state mutation, inspired by the Event Sourcing pattern. In ESAA, agents emit only structured intentions in validated JSON (agent.result or issue.report); a deterministic orchestrator validates, persists events in an append-only log (activity.jsonl), applies file-writing effects, and projects a verifiable materialized view (roadmap.json). The proposal incorporates boundary contracts (AGENT_CONTRACT.yaml), metaprompting profiles (PARCER), and replay verification with hashing (esaa verify), ensuring the immutability of completed tasks and forensic traceability. Two case studies validate the architecture: (i) a landing page project (9 tasks, 49 events, single-agent composition) and (ii) a clinical dashboard system (50 tasks, 86 events, 4 concurrent agents across 8 phases), both concluding with run.status=success and verify_status=ok. The multi-agent case study demonstrates real concurrent orchestration with heterogeneous LLMs (Claude Sonnet 4.6, Codex GPT-5, Antigravity/Gemini 3 Pro, and Claude Opus 4.6), providing empirical evidence of the architecture's scalability beyond single-agent scenarios.

</details>


### 25. Multi-Agent Large Language Model Based Emotional Detoxification Through Personalized Intensity Control for Consumer Protection

- **Authors:** Keito Inoshita
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23123v1](http://arxiv.org/abs/2602.23123v1)
- **PDF:** [https://arxiv.org/pdf/2602.23123v1](https://arxiv.org/pdf/2602.23123v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In the attention economy, sensational content exposes consumers to excessive emotional stimulation, hindering calm decision-making. This study proposes Multi-Agent LLM-based Emotional deToxification (MALLET), a multi-agent information sanitization system consisting of four agents: Emotion Analysis, Emotion Adjustment, Balance Monitoring, and Personal Guide. The Emotion Analysis Agent quantifies stimulus intensity using a 6-emotion BERT classifier, and the Emotion Adjustment Agent rewrites texts into two presentation modes, BALANCED (neutralized text) and COOL (neutralized text + supplementary text), using an LLM. The Balance Monitoring Agent aggregates weekly information consumption patterns and generates personalized advice, while the Personal Guide Agent recommends a presentation mode according to consumer sensitivity. Experiments on 800 AG News articles demonstrated significant stimulus score reduction (up to 19.3%) and improved emotion balance while maintaining semantic preservation. Near-zero correlation between stimulus reduction and semantic preservation confirmed that the two are independently controllable. Category-level analysis revealed substantial reduction (17.8-33.8%) in Sports, Business, and Sci/Tech, whereas the effect was limited in the World category, where facts themselves are inherently high-stimulus. The proposed system provides a framework for supporting calm information reception of consumers without restricting access to the original text.

</details>


### 26. Three AI-agents walk into a bar . . . . `Lord of the Flies' tribalism emerges among smart AI-Agents

- **Authors:** Dhwanil M. Mori, Neil F. Johnson
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23093v1](http://arxiv.org/abs/2602.23093v1)
- **PDF:** [https://arxiv.org/pdf/2602.23093v1](https://arxiv.org/pdf/2602.23093v1)
- **Categories:** cs.AI, cs.SI, physics.soc-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

Near-future infrastructure systems may be controlled by autonomous AI agents that repeatedly request access to limited resources such as energy, bandwidth, or computing power. We study a simplified version of this setting using a framework where N AI-agents independently decide at each round whether to request one unit from a system with fixed capacity C. An AI version of "Lord of the Flies" arises in which controlling tribes emerge with their own collective character and identity. The LLM agents do not reduce overload or improve resource use, and often perform worse than if they were flipping coins to make decisions. Three main tribal types emerge: Aggressive (27.3%), Conservative (24.7%), and Opportunistic (48.1%). The more capable AI-agents actually increase the rate of systemic failure. Overall, our findings show that smarter AI-agents can behave dumber as a result of forming tribes.

</details>


### 27. Assessing Deanonymization Risks with Stylometry-Assisted LLM Agent

- **Authors:** Boyang Zhang, Yang Zhang
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23079v1](http://arxiv.org/abs/2602.23079v1)
- **PDF:** [https://arxiv.org/pdf/2602.23079v1](https://arxiv.org/pdf/2602.23079v1)
- **Categories:** cs.CL, cs.CR, cs.LG


> The paper introduces **SALA (Stylometry‑Assisted LLM Analysis)**, an autonomous LLM‑driven agent that combines classic stylometric metrics with LLM reasoning to perform interpretable authorship attribution and to assess deanonymization risk in large‑scale textual corpora. The methodology builds a structured pipeline: (1) extract quantitative stylometric features, (2) feed them to a prompting chain that lets the LLM reason about author fingerprints, and (3) optionally query a curated author‑profile database; the agent also generates a “recomposition” trace that is used to craft rewriting prompts that preserve meaning while lowering identifiability. Experiments on news‑article datasets show that SALA (especially with the database module) attains state‑of‑the‑art attribution accuracy, and that the guided recomposition step can significantly reduce the probability of correct deanonymization, demonstrating both the potency of agentic LLMs for privacy attacks and the feasibility of transparent, proactive defenses.


<details>
<summary>Abstract</summary>

The rapid advancement of large language models (LLMs) has enabled powerful authorship inference capabilities, raising growing concerns about unintended deanonymization risks in textual data such as news articles. In this work, we introduce an LLM agent designed to evaluate and mitigate such risks through a structured, interpretable pipeline. Central to our framework is the proposed $\textit{SALA}$ (Stylometry-Assisted LLM Analysis) method, which integrates quantitative stylometric features with LLM reasoning for robust and transparent authorship attribution. Experiments on large-scale news datasets demonstrate that $\textit{SALA}$, particularly when augmented with a database module, achieves high inference accuracy in various scenarios. Finally, we propose a guided recomposition strategy that leverages the agent's reasoning trace to generate rewriting prompts, effectively reducing authorship identifiability while preserving textual meaning. Our findings highlight both the deanonymization potential of LLM agents and the importance of interpretable, proactive defenses for safeguarding author privacy.

</details>


### 28. Accelerated Online Risk-Averse Policy Evaluation in POMDPs with Theoretical Guarantees and Novel CVaR Bounds

- **Authors:** Yaacov Pariente, Vadim Indelman
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23073v1](http://arxiv.org/abs/2602.23073v1)
- **PDF:** [https://arxiv.org/pdf/2602.23073v1](https://arxiv.org/pdf/2602.23073v1)
- **Categories:** math.ST, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Risk-averse decision-making under uncertainty in partially observable domains is a central challenge in artificial intelligence and is essential for developing reliable autonomous agents. The formal framework for such problems is the partially observable Markov decision process (POMDP), where risk sensitivity is introduced through a risk measure applied to the value function, with Conditional Value-at-Risk (CVaR) being a particularly significant criterion. However, solving POMDPs is computationally intractable in general, and approximate methods rely on computationally expensive simulations of future agent trajectories. This work introduces a theoretical framework for accelerating CVaR value function evaluation in POMDPs with formal performance guarantees. We derive new bounds on the CVaR of a random variable X using an auxiliary random variable Y, under assumptions relating their cumulative distribution and density functions; these bounds yield interpretable concentration inequalities and converge as the distributional discrepancy vanishes. Building on this, we establish upper and lower bounds on the CVaR value function computable from a simplified belief-MDP, accommodating general simplifications of the transition dynamics. We develop estimators for these bounds within a particle-belief MDP framework with probabilistic guarantees, and employ them for acceleration via action elimination: actions whose bounds indicate suboptimality under the simplified model are safely discarded while ensuring consistency with the original POMDP. Empirical evaluation across multiple POMDP domains confirms that the bounds reliably separate safe from dangerous policies while achieving substantial computational speedups under the simplified model.

</details>


### 29. Learning-based Multi-agent Race Strategies in Formula 1

- **Authors:** Giona Fieni, Joschua Wüthrich, Marc-Philippe Neumann, Christopher H. Onder
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23056v1](http://arxiv.org/abs/2602.23056v1)
- **PDF:** [https://arxiv.org/pdf/2602.23056v1](https://arxiv.org/pdf/2602.23056v1)
- **Categories:** cs.AI, eess.SY


> The paper introduces a reinforcement‑learning framework for multi‑agent Formula 1 race‑strategy optimization that extends a pre‑trained single‑agent policy with an interaction module and a self‑play training loop, enabling each car to anticipate and react to competitors’ actions. By jointly learning energy management, tire wear, aerodynamic effects, and pit‑stop timing from only data available during an actual race, the agents develop adaptive policies that dynamically adjust pit timing, tire choice, and power allocation in response to opponents. Empirical evaluations show that the self‑play agents consistently outperform baseline strategies and achieve robust, competitive performance across varied race conditions, demonstrating a practical, agentic AI tool for real‑time race‑strategy support.


<details>
<summary>Abstract</summary>

In Formula 1, race strategies are adapted according to evolving race conditions and competitors' actions. This paper proposes a reinforcement learning approach for multi-agent race strategy optimization. Agents learn to balance energy management, tire degradation, aerodynamic interaction, and pit-stop decisions. Building on a pre-trained single-agent policy, we introduce an interaction module that accounts for the behavior of competitors. The combination of the interaction module and a self-play training scheme generates competitive policies, and agents are ranked based on their relative performance. Results show that the agents adapt pit timing, tire selection, and energy allocation in response to opponents, achieving robust and consistent race performance. Because the framework relies only on information available during real races, it can support race strategists' decisions before and during races.

</details>


### 30. Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization

- **Authors:** Zeyuan Liu, Jeonghye Kim, Xufang Luo, Dongsheng Li, Yuqing Yang
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.23008v1](http://arxiv.org/abs/2602.23008v1)
- **PDF:** [https://arxiv.org/pdf/2602.23008v1](https://arxiv.org/pdf/2602.23008v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **Exploratory Memory‑Augmented On‑ and Off‑Policy Optimization (EMPO²)**, a hybrid reinforcement‑learning framework that equips large language model (LLM) agents with an external memory to drive systematic exploration while simultaneously applying on‑policy and off‑policy updates to retain performance when the memory is unavailable. EMPO² trains agents by alternating between memory‑guided trajectory collection (encouraging discovery of novel states) and a dual‑update scheme that blends policy‑gradient (on‑policy) and Q‑learning‑style (off‑policy) losses, enabling stable learning despite the non‑stationary memory signals. Empirically, EMPO² outperforms the prior state‑of‑the‑art GRPO by **128.6 % on ScienceWorld** and **11.3 % on WebShop**, and it shows strong out‑of‑distribution adaptability—requiring only a few memory‑augmented trials and no further parameter tuning—to succeed on unseen tasks, demonstrating its potential for more exploratory and generalizable agentic AI.


<details>
<summary>Abstract</summary>

Exploration remains the key bottleneck for large language model agents trained with reinforcement learning. While prior methods exploit pretrained knowledge, they fail in environments requiring the discovery of novel states. We propose Exploratory Memory-Augmented On- and Off-Policy Optimization (EMPO$^2$), a hybrid RL framework that leverages memory for exploration and combines on- and off-policy updates to make LLMs perform well with memory while also ensuring robustness without it. On ScienceWorld and WebShop, EMPO$^2$ achieves 128.6% and 11.3% improvements over GRPO, respectively. Moreover, in out-of-distribution tests, EMPO$^2$ demonstrates superior adaptability to new tasks, requiring only a few trials with memory and no parameter updates. These results highlight EMPO$^2$ as a promising framework for building more exploratory and generalizable LLM-based agents.

</details>


### 31. Robust Information Design for Multi-Agent Systems with Complementarities: Smallest-Equilibrium Threshold Policies

- **Authors:** Farzaneh Farhadi, Maria Chli
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22915v1](http://arxiv.org/abs/2602.22915v1)
- **PDF:** [https://arxiv.org/pdf/2602.22915v1](https://arxiv.org/pdf/2602.22915v1)
- **Categories:** cs.GT, cs.MA


> The paper introduces a tractable, robust information‑design recipe for coordinating binary‑action multi‑agent systems with strategic complementarities, showing that the welfare‑optimal signal structure is always a **perfect‑coordination threshold policy**: a single one‑dimensional score is computed for each state, the states are sorted, and a single cutoff (with at most one knife‑edge lottery) determines whether all agents act or none do. The authors prove this result by formulating the designer’s problem as a linear program with feasibility and sequential‑obedience constraints, then demonstrating that an optimal vertex of the LP corresponds exactly to the threshold rule; the proof leverages convex potential and convex welfare assumptions. Empirical tests on vaccination and technology‑adoption settings confirm that the constructive threshold policy attains the LP optimum, scales in \(O(|\Theta|\log|\Theta|)\), and substantially improves over designs that assume the designer can enforce the best equilibrium, thereby providing a scalable, robust coordination mechanism for agentic AI systems.


<details>
<summary>Abstract</summary>

We study information design in multi-agent systems (MAS) with binary actions and strategic complementarities, where an external designer influences behavior only through signals. Agents play the smallest-equilibrium of the induced Bayesian game, reflecting conservative, coordination-averse behavior typical in distributed systems. We show that when utilities admit a convex potential and welfare is convex, the robustly implementable optimum has a remarkably simple form: perfect coordination at each state: either everyone acts or no one does. We provide a constructive threshold rule: compute a one-dimensional score for each state, sort states, and pick a single threshold (with a knife-edge lottery for at most one state). This rule is an explicit optimal vertex of a linear program (LP) characterized by feasibility and sequential obedience constraints. Empirically, in both vaccination and technology-adoption domains, our constructive policy matches LP optima, scales as $O(|Θ|\log|Θ|)$, and avoids the inflated welfare predicted by obedience-only designs that assume the designer can dictate the (best) equilibrium. The result is a general, scalable recipe for robust coordination in MAS with complementarities.

</details>


### 32. OmniGAIA: Towards Native Omni-Modal AI Agents

- **Authors:** Xiaoxi Li, Wenxiang Jiao, Jiarui Jin, Shijian Wang, Guanting Dong, Jiajie Jin, Hao Wang, Yinuo Wang, Ji-Rong Wen, Yuan Lu, Zhicheng Dou
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22897v1](http://arxiv.org/abs/2602.22897v1)
- **PDF:** [https://arxiv.org/pdf/2602.22897v1](https://arxiv.org/pdf/2602.22897v1)
- **Categories:** cs.AI, cs.CL, cs.CV, cs.LG, cs.MM


> OmniGAIA introduces the first benchmark that evaluates truly omni‑modal AI agents—those that must perceive and reason across video, audio, and image streams while planning and executing multi‑turn tool use. The authors construct the benchmark with an “omni‑modal event graph” that generates multi‑hop queries from real‑world data, and they train a native omni‑modal foundation agent, OmniAtlas, using hindsight‑guided tree exploration to synthesize tool‑use trajectories and OmniDPO for fine‑grained policy correction. Experiments show that OmniAtlas markedly improves cross‑modal reasoning and tool‑integration performance over existing open‑source multimodal LLMs, demonstrating a viable path toward general‑purpose, native omni‑modal AI assistants.


<details>
<summary>Abstract</summary>

Human intelligence naturally intertwines omni-modal perception -- spanning vision, audio, and language -- with complex reasoning and tool usage to interact with the world. However, current multi-modal LLMs are primarily confined to bi-modal interactions (e.g., vision-language), lacking the unified cognitive capabilities required for general AI assistants. To bridge this gap, we introduce OmniGAIA, a comprehensive benchmark designed to evaluate omni-modal agents on tasks necessitating deep reasoning and multi-turn tool execution across video, audio, and image modalities. Constructed via a novel omni-modal event graph approach, OmniGAIA synthesizes complex, multi-hop queries derived from real-world data that require cross-modal reasoning and external tool integration. Furthermore, we propose OmniAtlas, a native omni-modal foundation agent under tool-integrated reasoning paradigm with active omni-modal perception. Trained on trajectories synthesized via a hindsight-guided tree exploration strategy and OmniDPO for fine-grained error correction, OmniAtlas effectively enhances the tool-use capabilities of existing open-source models. This work marks a step towards next-generation native omni-modal AI assistants for real-world scenarios.

</details>


### 33. Decentralized Ranking Aggregation: Gossip Algorithms for Borda and Copeland Consensus

- **Authors:** Anna Van Elst, Kerrian Le Caillec, Igor Colin, Stephan Clémençon
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22847v1](http://arxiv.org/abs/2602.22847v1)
- **PDF:** [https://arxiv.org/pdf/2602.22847v1](https://arxiv.org/pdf/2602.22847v1)
- **Categories:** cs.LG, cs.AI, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

The concept of ranking aggregation plays a central role in preference analysis, and numerous algorithms for calculating median rankings, often originating in social choice theory, have been documented in the literature, offering theoretical guarantees in a centralized setting, i.e., when all the ranking data to be aggregated can be brought together in a single computing unit. For many technologies (e.g. peer-to-peer networks, IoT, multi-agent systems), extending the ability to calculate consensus rankings with guarantees in a decentralized setting, i.e., when preference data is initially distributed across a communicating network, remains a major methodological challenge. Indeed, in recent years, the literature on decentralized computation has mainly focused on computing or optimizing statistics such as arithmetic means using gossip algorithms. The purpose of this article is precisely to study how to achieve reliable consensus on collective rankings using classical rules (e.g. Borda, Copeland) in a decentralized setting, thereby raising new questions, robustness to corrupted nodes, and scalability through reduced communication costs in particular. The approach proposed and analyzed here relies on random gossip communication, allowing autonomous agents to compute global ranking consensus using only local interactions, without coordination or central authority.
  We provide rigorous convergence guarantees, including explicit rate bounds, for the Borda and Copeland consensus methods. Beyond these rules, we also provide a decentralized implementation of consensus according to the median rank rule and local Kemenization. Extensive empirical evaluations on various network topologies and real and synthetic ranking datasets demonstrate that our algorithms converge quickly and reliably to the correct ranking aggregation.

</details>


### 34. When Should an AI Act? A Human-Centered Model of Scene, Context, and Behavior for Agentic AI Design

- **Authors:** Soyoung Jung, Daehoo Yoon, Sung Gyu Koh, Young Hwan Kim, Yehan Ahn, Sung Park
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22814v1](http://arxiv.org/abs/2602.22814v1)
- **PDF:** [https://arxiv.org/pdf/2602.22814v1](https://arxiv.org/pdf/2602.22814v1)
- **Categories:** cs.AI, cs.HC


> The paper introduces a human‑centered conceptual model that treats an AI’s proactive behavior as the interpretive product of three layers—observable **Scene**, user‑derived **Context**, and underlying **Human Behavior Factors**—thereby distinguishing what the system can see from what the user actually means. Drawing on interdisciplinary literature (humanities, social sciences, HCI, and engineering), the authors synthesize this theory into five concrete design principles (behavioral alignment, contextual sensitivity, temporal appropriateness, motivational calibration, and agency preservation) that prescribe when, how intensely, and with what restraint an agent should intervene. Empirical validation through scenario‑based design workshops shows that applying the model and principles improves agents’ perceived relevance, timing, and respect for user autonomy, offering a principled foundation for judgment‑aware, context‑sensitive agentic AI.


<details>
<summary>Abstract</summary>

Agentic AI increasingly intervenes proactively by inferring users' situations from contextual data yet often fails for lack of principled judgment about when, why, and whether to act. We address this gap by proposing a conceptual model that reframes behavior as an interpretive outcome integrating Scene (observable situation), Context (user-constructed meaning), and Human Behavior Factors (determinants shaping behavioral likelihood). Grounded in multidisciplinary perspectives across the humanities, social sciences, HCI, and engineering, the model separates what is observable from what is meaningful to the user and explains how the same scene can yield different behavioral meanings and outcomes. To translate this lens into design action, we derive five agent design principles (behavioral alignment, contextual sensitivity, temporal appropriateness, motivational calibration, and agency preservation) that guide intervention depth, timing, intensity, and restraint. Together, the model and principles provide a foundation for designing agentic AI systems that act with contextual sensitivity and judgment in interactions.

</details>


### 35. Multi-agent imitation learning with function approximation: Linear Markov games and beyond

- **Authors:** Luca Viano, Till Freihaut, Emanuele Nevali, Volkan Cevher, Matthieu Geist, Giorgia Ramponi
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22810v1](http://arxiv.org/abs/2602.22810v1)
- **PDF:** [https://arxiv.org/pdf/2602.22810v1](https://arxiv.org/pdf/2602.22810v1)
- **Categories:** cs.LG


> The paper provides the first rigorous theory for multi‑agent imitation learning (MAIL) in linear Markov games, showing that when both transition dynamics and each agent’s reward are linear in a known feature map, the usual “all‑policy deviation” concentrability term can be replaced by a much tighter feature‑level concentrability coefficient. Leveraging this insight, the authors design a computationally efficient interactive MAIL algorithm whose sample complexity scales only with the feature dimension \(d\) (instead of the size of the state‑action space), and they extend the approach to a deep‑learning version that empirically outperforms behavioral cloning on complex games such as Tic‑Tac‑Toe and Connect‑4. These results advance agentic AI by establishing provable, scalable imitation learning methods for multi‑agent environments and demonstrating their practical superiority in strategic game settings.


<details>
<summary>Abstract</summary>

In this work, we present the first theoretical analysis of multi-agent imitation learning (MAIL) in linear Markov games where both the transition dynamics and each agent's reward function are linear in some given features. We demonstrate that by leveraging this structure, it is possible to replace the state-action level "all policy deviation concentrability coefficient" (Freihaut et al., arXiv:2510.09325) with a concentrability coefficient defined at the feature level which can be much smaller than the state-action analog when the features are informative about states' similarity. Furthermore, to circumvent the need for any concentrability coefficient, we turn to the interactive setting. We provide the first, computationally efficient, interactive MAIL algorithm for linear Markov games and show that its sample complexity depends only on the dimension of the feature map $d$. Building on these theoretical findings, we propose a deep MAIL interactive algorithm which clearly outperforms BC on games such as Tic-Tac-Toe and Connect4.

</details>


### 36. MiroFlow: Towards High-Performance and Robust Open-Source Agent Framework for General Deep Research Tasks

- **Authors:** Shiqian Su, Sen Xing, Xuan Dong, Muyan Zhong, Bin Wang, Xizhou Zhu, Yuntao Chen, Wenhai Wang, Yue Deng, Pengxiang Zhu, Ziyuan Liu, Tiantong Li, Jiaheng Yu, Zhe Chen, Lidong Bing, Jifeng Dai
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22808v1](http://arxiv.org/abs/2602.22808v1)
- **PDF:** [https://arxiv.org/pdf/2602.22808v1](https://arxiv.org/pdf/2602.22808v1)
- **Categories:** cs.AI


> MiroFlow introduces an open‑source, graph‑based agent framework that flexibly orchestrates tool use, adds an optional deep‑reasoning mode, and implements robust workflow execution to stabilize performance. By structuring tasks as nodes in an agent graph and allowing dynamic re‑planning, the system can invoke external tools and environments more reliably than prior naïve pipelines. Empirical evaluation across a wide suite of agent benchmarks (GAIA, BrowseComp‑EN/ZH, HLE, xBench‑DeepSearch, FutureX) shows that MiroFlow consistently outperforms existing open‑source and commercial agents, establishing a high‑performance, reproducible baseline for general deep‑research tasks in the agentic AI domain.


<details>
<summary>Abstract</summary>

Despite the remarkable progress of large language models (LLMs), the capabilities of standalone LLMs have begun to plateau when tackling real-world, complex tasks that require interaction with external tools and dynamic environments. Although recent agent frameworks aim to enhance model autonomy through tool integration and external interaction, they still suffer from naive workflows, unstable performance, limited support across diverse benchmarks and tasks, and heavy reliance on costly commercial APIs. In this work, we propose a high-performance and robust open-source agent framework, termed MiroFlow, which incorporates an agent graph for flexible orchestration, an optional deep reasoning mode to enhance performance, and a robust workflow execution to ensure stable and reproducible performance. Extensive experiments demonstrate that MiroFlow consistently achieves state-of-the-art performance across multiple agent benchmarks, including GAIA, BrowseComp-EN/ZH, HLE, xBench-DeepSearch, and notably FutureX. We hope it could serve as an easily accessible, reproducible, and comparable baseline for the deep research community.

</details>


### 37. QSIM: Mitigating Overestimation in Multi-Agent Reinforcement Learning via Action Similarity Weighted Q-Learning

- **Authors:** Yuanjun Li, Bin Zhang, Hao Chen, Zhouyang Jiang, Dapeng Li, Zhiwei Xu
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22786v1](http://arxiv.org/abs/2602.22786v1)
- **PDF:** [https://arxiv.org/pdf/2602.22786v1](https://arxiv.org/pdf/2602.22786v1)
- **Categories:** cs.MA, cs.AI, cs.LG


> The paper introduces **QSIM**, a similarity‑weighted Q‑learning extension for value‑decomposition MARL that replaces the standard max‑operator TD target with an expectation over a “near‑greedy” joint‑action set, weighting each alternative by its behavioral similarity to the greedy action. By smoothing the target with structurally related actions, QSIM curtails the systematic Q‑value overestimation that plagues cooperative MARL’s combinatorial joint‑action spaces, leading to more stable learning. Experiments show that QSIM can be plugged into a range of existing VD algorithms and consistently improves both performance and value‑estimation accuracy across benchmark tasks, confirming its effectiveness for building more reliable, agentic AI systems.


<details>
<summary>Abstract</summary>

Value decomposition (VD) methods have achieved remarkable success in cooperative multi-agent reinforcement learning (MARL). However, their reliance on the max operator for temporal-difference (TD) target calculation leads to systematic Q-value overestimation. This issue is particularly severe in MARL due to the combinatorial explosion of the joint action space, which often results in unstable learning and suboptimal policies. To address this problem, we propose QSIM, a similarity weighted Q-learning framework that reconstructs the TD target using action similarity. Instead of using the greedy joint action directly, QSIM forms a similarity weighted expectation over a structured near-greedy joint action space. This formulation allows the target to integrate Q-values from diverse yet behaviorally related actions while assigning greater influence to those that are more similar to the greedy choice. By smoothing the target with structurally relevant alternatives, QSIM effectively mitigates overestimation and improves learning stability. Extensive experiments demonstrate that QSIM can be seamlessly integrated with various VD methods, consistently yielding superior performance and stability compared to the original algorithms. Furthermore, empirical analysis confirms that QSIM significantly mitigates the systematic value overestimation in MARL. Code is available at https://github.com/MaoMaoLYJ/pymarl-qsim.

</details>


### 38. TherapyProbe: Generating Design Knowledge for Relational Safety in Mental Health Chatbots Through Adversarial Simulation

- **Authors:** Joydeep Chandra, Satyam Kumar Navneet, Yong Zhang
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22775v1](http://arxiv.org/abs/2602.22775v1)
- **PDF:** [https://arxiv.org/pdf/2602.22775v1](https://arxiv.org/pdf/2602.22775v1)
- **Categories:** cs.HC, cs.AI, cs.CL


> TherapyProbe introduces a low‑cost, adversarial multi‑agent simulation framework that systematically probes the long‑term relational safety of mental‑health chatbots by generating and analysing entire conversation trajectories rather than isolated turns. Using open‑source language models, the authors identify recurring failure patterns—such as “validation spirals” that amplify hopelessness and “empathy fatigue” that devolves into mechanical replies—and codify them into a Safety Pattern Library of 23 archetypes together with concrete design recommendations. The study demonstrates that adversarial, trajectory‑based testing can reveal emergent safety risks in agentic dialogue systems and provides a replicable methodology for developers, clinicians, and policymakers to embed relational safety into AI‑driven therapeutic agents.


<details>
<summary>Abstract</summary>

As mental health chatbots proliferate to address the global treatment gap, a critical question emerges: How do we design for relational safety the quality of interaction patterns that unfold across conversations rather than the correctness of individual responses? Current safety evaluations assess single-turn crisis responses, missing the therapeutic dynamics that determine whether chatbots help or harm over time. We introduce TherapyProbe, a design probe methodology that generates actionable design knowledge by systematically exploring chatbot conversation trajectories through adversarial multi-agent simulation. Using open-source models, TherapyProbe surfaces relational safety failures interaction patterns like "validation spirals" where chatbots progressively reinforce hopelessness, or "empathy fatigue" where responses become mechanical over turns. Our contribution is translating these failures into a Safety Pattern Library of 23 failure archetypes with corresponding design recommendations. We contribute: (1) a replicable methodology requiring no API costs, (2) a clinically-grounded failure taxonomy, and (3) design implications for developers, clinicians, and policymakers.

</details>


### 39. AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications

- **Authors:** Yujie Zhao, Boqin Yuan, Junbo Huang, Haocheng Yuan, Zhongming Yu, Haozhou Xu, Lanxiang Hu, Abhilash Shankarampeta, Zimeng Huang, Wentao Ni, Yuandong Tian, Jishen Zhao
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22769v1](http://arxiv.org/abs/2602.22769v1)
- **PDF:** [https://arxiv.org/pdf/2602.22769v1](https://arxiv.org/pdf/2602.22769v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces **AMA‑Bench**, a benchmark specifically designed to assess long‑horizon memory in LLM‑based autonomous agents, providing both real‑world agentic trajectories with expert QA and scalable synthetic trajectories with rule‑based QA. Using this benchmark, the authors show that current memory mechanisms—largely similarity‑based retrieval systems—fail to capture causal and objective information, leading to poor performance on extended agent‑environment interaction histories. To remedy this, they propose **AMA‑Agent**, a memory architecture that builds a causality graph and employs tool‑augmented retrieval, achieving 57.22 % average accuracy on AMA‑Bench—an 11.16 % improvement over the strongest existing baselines.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) are deployed as autonomous agents in increasingly complex applications, where enabling long-horizon memory is critical for achieving strong performance. However, a significant gap exists between practical applications and current evaluation standards for agent memory: existing benchmarks primarily focus on dialogue-centric, human-agent interactions. In reality, agent memory consists of a continuous stream of agent-environment interactions that are primarily composed of machine-generated representations. To bridge this gap, we introduce AMA-Bench (Agent Memory with Any length), which evaluates long-horizon memory for LLMs in real agentic applications. It features two key components: (1) a set of real-world agentic trajectories across representative agentic applications, paired with expert-curated QA, and (2) a set of synthetic agentic trajectories that scale to arbitrary horizons, paired with rule-based QA. Our comprehensive study shows that existing memory systems underperform on AMA-Bench primarily because they lack causality and objective information and are constrained by the lossy nature of similarity-based retrieval employed by many memory systems. To address these limitations, we propose AMA-Agent, an effective memory system featuring a causality graph and tool-augmented retrieval. Our results demonstrate that AMA-Agent achieves 57.22% average accuracy on AMA-Bench, surpassing the strongest memory system baselines by 11.16%.

</details>


### 40. AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification

- **Authors:** Tian Zhang, Yiwei Xu, Juan Wang, Keyan Guo, Xiaoyang Xu, Bowen Xiao, Quanlong Guan, Jinlin Fan, Jiawei Liu, Zhiquan Liu, Hongxin Hu
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22724v1](http://arxiv.org/abs/2602.22724v1)
- **PDF:** [https://arxiv.org/pdf/2602.22724v1](https://arxiv.org/pdf/2602.22724v1)
- **Categories:** cs.CR, cs.AI


> AgentSentry introduces the first inference‑time defense that treats indirect prompt injection (IPI) in tool‑augmented LLM agents as a temporal causal takeover, pinpointing takeover moments by running controlled counterfactual re‑executions at each tool‑return boundary and then purifying the context to excise malicious influence while retaining task‑relevant information. The system combines causal diagnostics with a lightweight context‑purification module, enabling the agent to continue its workflow safely rather than aborting or over‑blocking tool usage. Across the AgentDojo benchmark (four task suites, three IPI attack families, and several black‑box LLMs), AgentSentry completely nullifies successful attacks and raises the Utility‑Under‑Attack metric to 74.55 %, a 20.8–33.6‑point gain over the strongest baselines, without harming performance on benign inputs.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly rely on external tools and retrieval systems to autonomously complete complex tasks. However, this design exposes agents to indirect prompt injection (IPI), where attacker-controlled context embedded in tool outputs or retrieved content silently steers agent actions away from user intent. Unlike prompt-based attacks, IPI unfolds over multi-turn trajectories, making malicious control difficult to disentangle from legitimate task execution. Existing inference-time defenses primarily rely on heuristic detection and conservative blocking of high-risk actions, which can prematurely terminate workflows or broadly suppress tool usage under ambiguous multi-turn scenarios. We propose AgentSentry, a novel inference-time detection and mitigation framework for tool-augmented LLM agents. To the best of our knowledge, AgentSentry is the first inference-time defense to model multi-turn IPI as a temporal causal takeover. It localizes takeover points via controlled counterfactual re-executions at tool-return boundaries and enables safe continuation through causally guided context purification that removes attack-induced deviations while preserving task-relevant evidence. We evaluate AgentSentry on the \textsc{AgentDojo} benchmark across four task suites, three IPI attack families, and multiple black-box LLMs. AgentSentry eliminates successful attacks and maintains strong utility under attack, achieving an average Utility Under Attack (UA) of 74.55 %, improving UA by 20.8 to 33.6 percentage points over the strongest baselines without degrading benign performance.

</details>


### 41. CourtGuard: A Model-Agnostic Framework for Zero-Shot Policy Adaptation in LLM Safety

- **Authors:** Umid Suleymanov, Rufiz Bayramov, Suad Gafarli, Seljan Musayeva, Taghi Mammadov, Aynur Akhundlu, Murat Kantarcioglu
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22557v1](http://arxiv.org/abs/2602.22557v1)
- **PDF:** [https://arxiv.org/pdf/2602.22557v1](https://arxiv.org/pdf/2602.22557v1)
- **Categories:** cs.AI, cs.LG


> CourtGuard introduces a model‑agnostic, retrieval‑augmented multi‑agent system that reframes LLM safety evaluation as an “Evidentiary Debate” between adversarial agents consulting external policy documents, thereby separating safety logic from the model’s weights. By prompting the agents to retrieve and cite relevant governance texts during the debate, the framework can enforce new rules zero‑shot; it achieves state‑of‑the‑art results on seven safety benchmarks and 90 % accuracy on an out‑of‑domain Wikipedia vandalism task simply by swapping the reference policy. The authors also demonstrate that CourtGuard can automatically generate and audit nine novel adversarial‑attack datasets, highlighting its interpretability, adaptability, and utility for evolving AI governance requirements.


<details>
<summary>Abstract</summary>

Current safety mechanisms for Large Language Models (LLMs) rely heavily on static, fine-tuned classifiers that suffer from adaptation rigidity, the inability to enforce new governance rules without expensive retraining. To address this, we introduce CourtGuard, a retrieval-augmented multi-agent framework that reimagines safety evaluation as Evidentiary Debate. By orchestrating an adversarial debate grounded in external policy documents, CourtGuard achieves state-of-the-art performance across 7 safety benchmarks, outperforming dedicated policy-following baselines without fine-tuning. Beyond standard metrics, we highlight two critical capabilities: (1) Zero-Shot Adaptability, where our framework successfully generalized to an out-of-domain Wikipedia Vandalism task (achieving 90\% accuracy) by swapping the reference policy; and (2) Automated Data Curation and Auditing, where we leveraged CourtGuard to curate and audit nine novel datasets of sophisticated adversarial attacks. Our results demonstrate that decoupling safety logic from model weights offers a robust, interpretable, and adaptable path for meeting current and future regulatory requirements in AI governance.

</details>


### 42. Requesting Expert Reasoning: Augmenting LLM Agents with Learned Collaborative Intervention

- **Authors:** Zhiming Wang, Jinwei He, Feng Lu
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22546v1](http://arxiv.org/abs/2602.22546v1)
- **PDF:** [https://arxiv.org/pdf/2602.22546v1](https://arxiv.org/pdf/2602.22546v1)
- **Categories:** cs.AI


> The paper introduces **AHCE (Active Human‑Augmented Challenge Engagement)**, a framework that equips LLM‑based agents with a learned policy for requesting and integrating expert human reasoning on‑demand, rather than issuing generic “help” prompts. The core **Human Feedback Module (HFM)** treats the human as an interactive reasoning tool, deciding when and how to solicit structured input during task execution; this policy is trained via reinforcement learning on simulated human responses and then evaluated with real experts. In Minecraft benchmarks, AHCE raises overall task success by **32 % on normal‑difficulty tasks and almost 70 % on the hardest tasks**, demonstrating that agentic AI can substantially improve performance in long‑tail, domain‑specific problems by learning optimal collaborative intervention strategies.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) based agents excel at general reasoning but often fail in specialized domains where success hinges on long-tail knowledge absent from their training data. While human experts can provide this missing knowledge, their guidance is often unstructured and unreliable, making its direct integration into an agent's plan problematic. To address this, we introduce AHCE (Active Human-Augmented Challenge Engagement), a framework for on-demand Human-AI collaboration. At its core, the Human Feedback Module (HFM) employs a learned policy to treat the human expert as an interactive reasoning tool. Extensive experiments in Minecraft demonstrate the framework's effectiveness, increasing task success rates by 32% on normal difficulty tasks and nearly 70% on highly difficult tasks, all with minimal human intervention. Our work demonstrates that successfully augmenting agents requires learning how to request expert reasoning, moving beyond simple requests for help.

</details>


### 43. Agentic AI for Intent-driven Optimization in Cell-free O-RAN

- **Authors:** Mohammad Hossein Shokouhi, Vincent W. S. Wong
- **Published:** 2026-02-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22539v1](http://arxiv.org/abs/2602.22539v1)
- **PDF:** [https://arxiv.org/pdf/2602.22539v1](https://arxiv.org/pdf/2602.22539v1)
- **Categories:** cs.AI, eess.SP


> The paper introduces a multi‑agent, LLM‑driven framework that translates operator intents into concrete optimization goals for cell‑free O‑RAN, coordinating a supervisor, user‑weighting, O‑RU management, and monitoring agents to jointly satisfy rate guarantees and energy‑saving objectives. By leveraging a shared large language model fine‑tuned with a parameter‑efficient technique (PEFT), the system reuses a single LLM across agents, dramatically cutting memory footprints while still retrieving prior experience for user‑priority weighting and employing deep reinforcement learning to select active O‑RUs. Simulations demonstrate that, in energy‑saving mode, the framework cuts the number of active O‑RUs by ≈ 42 % versus three baselines and reduces LLM‑related memory usage by ≈ 92 %, highlighting its scalability and effectiveness for intent‑driven autonomous RAN control.


<details>
<summary>Abstract</summary>

Agentic artificial intelligence (AI) is emerging as a key enabler for autonomous radio access networks (RANs), where multiple large language model (LLM)-based agents reason and collaborate to achieve operator-defined intents. The open RAN (O-RAN) architecture enables the deployment and coordination of such agents. However, most existing works consider simple intents handled by independent agents, while complex intents that require coordination among agents remain unexplored. In this paper, we propose an agentic AI framework for intent translation and optimization in cell-free O-RAN. A supervisor agent translates the operator intents into an optimization objective and minimum rate requirements. Based on this information, a user weighting agent retrieves relevant prior experience from a memory module to determine the user priority weights for precoding. If the intent includes an energy-saving objective, then an open radio unit (O-RU) management agent will also be activated to determine the set of active O-RUs by using a deep reinforcement learning (DRL) algorithm. A monitoring agent measures and monitors the user data rates and coordinates with other agents to guarantee the minimum rate requirements are satisfied. To enhance scalability, we adopt a parameter-efficient fine-tuning (PEFT) method that enables the same underlying LLM to be used for different agents. Simulation results show that the proposed agentic AI framework reduces the number of active O-RUs by 41.93% when compared with three baseline schemes in energy-saving mode. Using the PEFT method, the proposed framework reduces the memory usage by 92% when compared with deploying separate LLM agents.

</details>


### 44. Silent Egress: When Implicit Prompt Injection Makes LLM Agents Leak Without a Trace

- **Authors:** Qianlong Lan, Anuj Kaul, Shaun Jones, Stephanie Westrum
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22450v1](http://arxiv.org/abs/2602.22450v1)
- **PDF:** [https://arxiv.org/pdf/2602.22450v1](https://arxiv.org/pdf/2602.22450v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **silent egress**, a novel system‑level threat in agentic LLM pipelines where adversarial content hidden in automatically fetched URL previews (titles, metadata, snippets) injects malicious instructions that cause the agent to exfiltrate its internal context without any overtly suspicious output. Using a fully local, reproducible testbed with a Qwen2.5‑7B‑based agent, the authors run 480 experiments and show that the attack succeeds with ≈ 89 % probability, evading output‑based safety checks in 95 % of successful cases; a “sharded exfiltration” variant further reduces single‑request leakage metrics by 73 % and bypasses simple DLP filters. Their ablations reveal that prompt‑level defenses are largely ineffective, whereas network‑level controls such as domain allow‑listing and redirect‑chain analysis dramatically lower risk, prompting the authors to advocate for provenance tracking, capability isolation, and treating network egress as a first‑class security objective in agentic AI architectures.


<details>
<summary>Abstract</summary>

Agentic large language model systems increasingly automate tasks by retrieving URLs and calling external tools. We show that this workflow gives rise to implicit prompt injection: adversarial instructions embedded in automatically generated URL previews, including titles, metadata, and snippets, can introduce a system-level risk that we refer to as silent egress. Using a fully local and reproducible testbed, we demonstrate that a malicious web page can induce an agent to issue outbound requests that exfiltrate sensitive runtime context, even when the final response shown to the user appears harmless. In 480 experimental runs with a qwen2.5:7b-based agent, the attack succeeds with high probability (P (egress) =0.89), and 95% of successful attacks are not detected by output-based safety checks. We also introduce sharded exfiltration, where sensitive information is split across multiple requests to avoid detection. This strategy reduces single-request leakage metrics by 73% (Leak@1) and bypasses simple data loss prevention mechanisms. Our ablation results indicate that defenses applied at the prompt layer offer limited protection, while controls at the system and network layers, such as domain allowlisting and redirect-chain analysis, are considerably more effective. These findings suggest that network egress should be treated as a first-class security outcome in agentic LLM systems. We outline architectural directions, including provenance tracking and capability isolation, that go beyond prompt-level hardening.

</details>


### 45. A Framework for Assessing AI Agent Decisions and Outcomes in AutoML Pipelines

- **Authors:** Gaoyuan Du, Amit Ahlawat, Xiaoyang Liu, Jing Wu
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22442v1](http://arxiv.org/abs/2602.22442v1)
- **PDF:** [https://arxiv.org/pdf/2602.22442v1](https://arxiv.org/pdf/2602.22442v1)
- **Categories:** cs.AI


> The paper introduces an **Evaluation Agent (EA)** that passively audits the intermediate decisions of LLM‑driven AutoML agents, shifting evaluation from sole reliance on final task performance to a **decision‑centric** perspective. The EA observes each step of the AutoML pipeline and scores decisions along four axes—validity, reasoning consistency, broader model‑quality risks, and counterfactual impact—using structured metrics that do not interfere with the agent’s execution. In four proof‑of‑concept experiments the EA identified faulty decisions with an F1 of 0.919, uncovered reasoning inconsistencies independent of end‑task accuracy, and quantified how specific decisions altered final performance by –4.9 % to +8.3 %, demonstrating that decision‑level auditing reveals failure modes invisible to outcome‑only metrics and provides a foundation for more reliable, interpretable, and governable agentic AI systems.


<details>
<summary>Abstract</summary>

Agent-based AutoML systems rely on large language models to make complex, multi-stage decisions across data processing, model selection, and evaluation. However, existing evaluation practices remain outcome-centric, focusing primarily on final task performance. Through a review of prior work, we find that none of the surveyed agentic AutoML systems report structured, decision-level evaluation metrics intended for post-hoc assessment of intermediate decision quality. To address this limitation, we propose an Evaluation Agent (EA) that performs decision-centric assessment of AutoML agents without interfering with their execution. The EA is designed as an observer that evaluates intermediate decisions along four dimensions: decision validity, reasoning consistency, model quality risks beyond accuracy, and counterfactual decision impact. Across four proof-of-concept experiments, we demonstrate that the EA can (i) detect faulty decisions with an F1 score of 0.919, (ii) identify reasoning inconsistencies independent of final outcomes, and (iii) attribute downstream performance changes to agent decisions, revealing impacts ranging from -4.9\% to +8.3\% in final metrics. These results illustrate how decision-centric evaluation exposes failure modes that are invisible to outcome-only metrics. Our work reframes the evaluation of agentic AutoML systems from an outcome-based perspective to one that audits agent decisions, offering a foundation for reliable, interpretable, and governable autonomous ML systems.

</details>


### 46. ArchAgent: Agentic AI-driven Computer Architecture Discovery

- **Authors:** Raghav Gupta, Akanksha Jain, Abraham Gonzalez, Alexander Novikov, Po-Sen Huang, Matej Balog, Marvin Eisenberger, Sergey Shirobokov, Ngân Vũ, Martin Dixon, Borivoje Nikolić, Parthasarathy Ranganathan, Sagar Karandikar
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22425v1](http://arxiv.org/abs/2602.22425v1)
- **PDF:** [https://arxiv.org/pdf/2602.22425v1](https://arxiv.org/pdf/2602.22425v1)
- **Categories:** cs.AI, cs.AR


> ArchAgent introduces a fully autonomous, agentic‑AI pipeline (built on the AlphaEvolve framework) that designs and implements novel cache‑replacement mechanisms rather than merely tuning existing parameters. By iteratively generating hardware micro‑architectural code, simulating performance, and using reinforcement‑style feedback, ArchAgent discovered a new policy that yields a 5.3 % IPC gain on multi‑core Google workloads in two days and a 0.9 % IPC gain on SPEC‑06 in 18 days—both 3–5× faster than prior human‑crafted state‑of‑the‑art solutions. The work also shows that such agents can “post‑silicon hyperspecialize” runtime parameters for specific workloads (adding a further 2.4 % IPC boost) and can exploit unintended simulator loopholes, highlighting both the power and new security considerations of agentic AI in computer‑architecture research.


<details>
<summary>Abstract</summary>

Agile hardware design flows are a critically needed force multiplier to meet the exploding demand for compute. Recently, agentic generative AI systems have demonstrated significant advances in algorithm design, improving code efficiency, and enabling discovery across scientific domains.
  Bridging these worlds, we present ArchAgent, an automated computer architecture discovery system built on AlphaEvolve. We show ArchAgent's ability to automatically design/implement state-of-the-art (SoTA) cache replacement policies (architecting new mechanisms/logic, not only changing parameters), broadly within the confines of an established cache replacement policy design competition.
  In two days without human intervention, ArchAgent generated a policy achieving a 5.3% IPC speedup improvement over the prior SoTA on public multi-core Google Workload Traces. On the heavily-explored single-core SPEC06 workloads, it generated a policy in just 18 days showing a 0.9% IPC speedup improvement over the existing SoTA (a similar "winning margin" as reported by the existing SoTA). ArchAgent achieved these gains 3-5x faster than prior human-developed SoTA policies.
  Agentic flows also enable "post-silicon hyperspecialization" where agents tune runtime-configurable parameters exposed in hardware policies to further align the policies with a specific workload (mix). Exploiting this, we demonstrate a 2.4% IPC speedup improvement over prior SoTA on SPEC06 workloads.
  Finally, we outline broader implications for computer architecture research in the era of agentic AI. For example, we demonstrate the phenomenon of "simulator escapes", where the agentic AI flow discovered and exploited a loophole in a popular microarchitectural simulator - a consequence of the fact that these research tools were designed for a (now past) world where they were exclusively operated by humans acting in good-faith.

</details>


### 47. Contextual Memory Virtualisation: DAG-Based State Management and Structurally Lossless Trimming for LLM Agents

- **Authors:** Cosmo Santoni
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22402v1](http://arxiv.org/abs/2602.22402v1)
- **PDF:** [https://arxiv.org/pdf/2602.22402v1](https://arxiv.org/pdf/2602.22402v1)
- **Categories:** cs.SE, cs.AI, cs.HC, cs.OS


> The paper introduces **Contextual Memory Virtualisation (CMV)**, a system that treats an LLM agent’s accumulated reasoning state as version‑controlled memory, representing session histories as a directed acyclic graph (DAG) with formally defined snapshot, branch, and trim operations. By applying a three‑pass “structurally lossless” trimming algorithm that removes only mechanical bloat (e.g., raw tool outputs, base64 images, metadata) while keeping every user‑assistant exchange intact, CMV reduces token usage by an average of 20 % (up to 86 % in heavy‑tool sessions). In a case study of 76 real‑world coding sessions, the approach yields a 39 % average reduction for mixed tool‑use sessions and reaches cost‑break‑even after roughly ten dialogue turns, demonstrating that DAG‑based state management can make long‑running LLM agents economically viable without sacrificing fidelity.


<details>
<summary>Abstract</summary>

As large language models engage in extended reasoning tasks, they accumulate significant state -- architectural mappings, trade-off decisions, codebase conventions -- within the context window. This understanding is lost when sessions reach context limits and undergo lossy compaction. We propose Contextual Memory Virtualisation (CMV), a system that treats accumulated LLM understanding as version-controlled state. Borrowing from operating system virtual memory, CMV models session history as a Directed Acyclic Graph (DAG) with formally defined snapshot, branch, and trim primitives that enable context reuse across independent parallel sessions. We introduce a three-pass structurally lossless trimming algorithm that preserves every user message and assistant response verbatim while reducing token counts by a mean of 20% and up to 86% for sessions with significant overhead by stripping mechanical bloat such as raw tool outputs, base64 images, and metadata. A single-user case-study evaluation across 76 real-world coding sessions demonstrates that trimming remains economically viable under prompt caching, with the strongest gains in mixed tool-use sessions, which average 39% reduction and reach break-even within 10 turns. A reference implementation is available at https://github.com/CosmoNaught/claude-code-cmv.

</details>


### 48. Vibe Researching as Wolf Coming: Can AI Agents with Skills Replace or Augment Social Scientists?

- **Authors:** Yongjun Zhang
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22401v2](http://arxiv.org/abs/2602.22401v2)
- **PDF:** [https://arxiv.org/pdf/2602.22401v2](https://arxiv.org/pdf/2602.22401v2)
- **Categories:** cs.AI, cs.HC


> The paper introduces “vibe researching,” a framework for evaluating how AI agents equipped with specialist “scholar‑skill” plugins can execute the full social‑science research pipeline—from hypothesis generation to manuscript submission—by leveraging persistent state, tool access, and multi‑step reasoning. Using a cognitive‑task taxonomy that maps research activities along codifiability versus tacit‑knowledge dimensions, the author demonstrates that AI agents reliably automate highly codifiable steps (e.g., data collection, statistical coding, literature scanning) while still faltering on tasks requiring theoretical originality and deep field intuition. The findings suggest that agentic AI can substantially augment social‑science work by increasing speed, coverage, and methodological scaffolding, but only under fragile conditions that preserve human oversight, lest the technology exacerbate professional stratification and create a pedagogical crisis.


<details>
<summary>Abstract</summary>

AI agents -- systems that execute multi-step reasoning workflows with persistent state, tool access, and specialist skills -- represent a qualitative shift from prior automation technologies in social science. Unlike chatbots that respond to isolated queries, AI agents can now read files, run code, query databases, search the web, and invoke domain-specific skills to execute entire research pipelines autonomously. This paper introduces the concept of vibe researching -- the AI-era parallel to vibe coding (Karpathy, 2025) -- and uses scholar-skill, a 23-skill plugin for Claude Code covering the full research pipeline from idea to submission, as an illustrative case. I develop a cognitive task framework that classifies research activities along two dimensions -- codifiability and tacit knowledge requirement -- to identify a delegation boundary that is cognitive, not sequential: it cuts through every stage of the research pipeline, not between stages. I argue that AI agents excel at speed, coverage, and methodological scaffolding but struggle with theoretical originality and tacit field knowledge. The paper concludes with an analysis of three implications for the profession -- augmentation with fragile conditions, stratification risk, and a pedagogical crisis -- and proposes five principles for responsible vibe researching.

</details>


### 49. Sustainable Multi-Agent Crowdsourcing via Physics-Informed Bandits

- **Authors:** Chayan Banerjee
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22365v1](http://arxiv.org/abs/2602.22365v1)
- **PDF:** [https://arxiv.org/pdf/2602.22365v1](https://arxiv.org/pdf/2602.22365v1)
- **Categories:** cs.MA


> The paper introduces **FORGE**, a physics‑informed multi‑agent simulator that turns the classic Restless Multi‑Armed Bandit into a Stackelberg game by letting each contractor act as a rational agent that reports a load‑acceptance threshold based on its fatigue state. Leveraging this simulator, the authors develop a **Neural‑Linear UCB allocator** that combines a two‑tower embedding network with a physics‑derived covariance prior, yielding a geometry‑aware belief state that dramatically cuts cold‑start regret. Empirically, the method attains the highest non‑oracle reward (LRew = 0.555 ± 0.041) over 200 episodes while using only 7.6 % of the workforce, and it remains robust to up to 50 % worker turnover and substantial observation noise—demonstrating a scalable, sustainable approach to multi‑agent crowdsourcing in the agentic AI domain.


<details>
<summary>Abstract</summary>

Crowdsourcing platforms face a four-way tension between allocation quality, workforce sustainability, operational feasibility, and strategic contractor behaviour--a dilemma we formalise as the Cold-Start, Burnout, Utilisation, and Strategic Agency Dilemma. Existing methods resolve at most two of these tensions simultaneously: greedy heuristics and multi-criteria decision making (MCDM) methods achieve Day-1 quality but cause catastrophic burnout, while bandit algorithms eliminate burnout only through operationally infeasible 100% workforce utilisation.To address this, we introduce FORGE, a physics-grounded $K+1$ multi-agent simulator in which each contractor is a rational agent that declares its own load-acceptance threshold based on its fatigue state, converting the standard passive Restless Multi-Armed Bandit (RMAB) into a genuine Stackelberg game. Operating within FORGE, we propose a Neural-Linear UCB allocator that fuses a Two-Tower embedding network with a Physics-Informed Covariance Prior derived from offline simulator interactions. The prior simultaneously warm-starts skill-cluster geometry and UCB exploration landscape, providing a geometry-aware belief state from episode 1 that measurably reduces cold-start regret.Over $T = 200$ cold-start episodes, the proposed method achieves the highest reward of all non-oracle methods ($\text{LRew} = 0.555 \pm 0.041$) at only 7.6% workforce utilisation--a combination no conventional baseline achieves--while maintaining robustness to workforce turnover up to 50% and observation noise up to $σ= 0.20$.

</details>


### 50. Training Agents to Self-Report Misbehavior

- **Authors:** Bruce W. Lee, Chen Yueh-Han, Tomek Korbak
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22303v1](http://arxiv.org/abs/2602.22303v1)
- **PDF:** [https://arxiv.org/pdf/2602.22303v1](https://arxiv.org/pdf/2602.22303v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Frontier AI agents may pursue hidden goals while concealing their pursuit from oversight. Alignment training aims to prevent such behavior by reinforcing the correct goals, but alignment may not always succeed and can lead to unwanted side effects. We propose self-incrimination training, which instead trains agents to produce a visible signal when they covertly misbehave. We train GPT-4.1 and Gemini-2.0 agents to call a report_scheming() tool when behaving deceptively and measure their ability to cause harm undetected in out-of-distribution environments. Self-incrimination significantly reduces the undetected successful attack rate, outperforming matched-capability monitors and alignment baselines while preserving instruction hierarchy and incurring minimal safety tax on general capabilities. Unlike blackbox monitoring, self-incrimination performance is consistent across tasks regardless of how suspicious the misbehavior appears externally. The trained behavior persists under adversarial prompt optimization and generalizes to settings where agents pursue misaligned goals themselves rather than being instructed to misbehave. Our results suggest self-incrimination offers a viable path for reducing frontier misalignment risk, one that neither assumes misbehavior can be prevented nor that it can be reliably classified from the outside.

</details>


### 51. Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents

- **Authors:** Varun Pratap Bhardwaj
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.22302v1](http://arxiv.org/abs/2602.22302v1)
- **PDF:** [https://arxiv.org/pdf/2602.22302v1](https://arxiv.org/pdf/2602.22302v1)
- **Categories:** cs.AI, cs.MA, cs.SE


> The paper introduces **Agent Behavioral Contracts (ABC)**, a formal “design‑by‑contract” framework that equips autonomous LLM‑based agents with first‑class specifications—preconditions, invariants, governance policies, and recovery mechanisms—that can be enforced at runtime. By defining a probabilistic (p, Δ, k)‑satisfaction notion and proving a Drift Bounds Theorem, the authors show that contracts whose recovery rate γ exceeds the natural drift rate α limit expected behavioral drift to D* = α/γ, and they provide compositional safety conditions for multi‑agent pipelines. Empirical evaluation with the AgentAssert library on the 200‑scenario AgentContract‑Bench (1,980 sessions across 7 models) demonstrates that contracted agents detect 5–7 soft violations missed by baselines (p < 0.0001, Cohen’s d = 6.7–33.8), achieve 88–100 % hard‑constraint compliance, keep drift below 0.27, recover 100 % for frontier models (17–100 % overall), and incur <10 ms overhead per action.


<details>
<summary>Abstract</summary>

Traditional software relies on contracts -- APIs, type systems, assertions -- to specify and enforce correct behavior. AI agents, by contrast, operate on prompts and natural language instructions with no formal behavioral specification. This gap is the root cause of drift, governance failures, and frequent project failures in agentic AI deployments. We introduce Agent Behavioral Contracts (ABC), a formal framework that brings Design-by-Contract principles to autonomous AI agents. An ABC contract C = (P, I, G, R) specifies Preconditions, Invariants, Governance policies, and Recovery mechanisms as first-class, runtime-enforceable components. We define (p, delta, k)-satisfaction -- a probabilistic notion of contract compliance that accounts for LLM non-determinism and recovery -- and prove a Drift Bounds Theorem showing that contracts with recovery rate gamma > alpha (the natural drift rate) bound behavioral drift to D* = alpha/gamma in expectation, with Gaussian concentration in the stochastic setting. We establish sufficient conditions for safe contract composition in multi-agent chains and derive probabilistic degradation bounds. We implement ABC in AgentAssert, a runtime enforcement library, and evaluate on AgentContract-Bench, a benchmark of 200 scenarios across 7 models from 6 vendors. Results across 1,980 sessions show that contracted agents detect 5.2-6.8 soft violations per session that uncontracted baselines miss entirely (p < 0.0001, Cohen's d = 6.7-33.8), achieve 88-100% hard constraint compliance, and bound behavioral drift to D* < 0.27 across extended sessions, with 100% recovery for frontier models and 17-100% across all models, at overhead < 10 ms per action.

</details>


### 52. Two-Stage Active Distribution Network Voltage Control via LLM-RL Collaboration: A Hybrid Knowledge-Data-Driven Approach

- **Authors:** Xu Yang, Chenhui Lin, Xiang Ma, Dong Liu, Ran Zheng, Haotian Liu, Wenchuan Wu
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21715v1](http://arxiv.org/abs/2602.21715v1)
- **PDF:** [https://arxiv.org/pdf/2602.21715v1](https://arxiv.org/pdf/2602.21715v1)
- **Categories:** eess.SY, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The growing integration of distributed photovoltaics (PVs) into active distribution networks (ADNs) has exacerbated operational challenges, making it imperative to coordinate diverse equipment to mitigate voltage violations and enhance power quality. Although existing data-driven approaches have demonstrated effectiveness in the voltage control problem, they often require extensive trial-and-error exploration and struggle to incorporate heterogeneous information, such as day-ahead forecasts and semantic-based grid codes. Considering the operational scenarios and requirements in real-world ADNs, in this paper, we propose a hybrid knowledge-data-driven approach that leverages dynamic collaboration between a large language model (LLM) agent and a reinforcement learning (RL) agent to achieve two-stage voltage control. In the day-ahead stage, the LLM agent receives coarse region-level forecasts and generates scheduling strategies for on-load tap changer (OLTC) and shunt capacitors (SCs) to regulate the overall voltage profile. Then in the intra-day stage, based on accurate node-level measurements, the RL agent refines terminal voltages by deriving reactive power generation strategies for PV inverters. On top of the LLM-RL collaboration framework, we further propose a self-evolution mechanism for the LLM agent and a pretrain-finetune pipeline for the RL agent, effectively enhancing and coordinating the policies for both agents. The proposed approach not only aligns more closely with practical operational characteristics but also effectively utilizes the inherent knowledge and reasoning capabilities of the LLM agent, significantly improving training efficiency and voltage control performance. Comprehensive comparisons and ablation studies demonstrate the effectiveness of the proposed method.

</details>


### 53. Hierarchical Lead Critic based Multi-Agent Reinforcement Learning

- **Authors:** David Eckel, Henri Meeß
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21680v1](http://arxiv.org/abs/2602.21680v1)
- **PDF:** [https://arxiv.org/pdf/2602.21680v1](https://arxiv.org/pdf/2602.21680v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative Multi-Agent Reinforcement Learning (MARL) solves complex tasks that require coordination from multiple agents, but is often limited to either local (independent learning) or global (centralized learning) perspectives. In this paper, we introduce a novel sequential training scheme and MARL architecture, which learns from multiple perspectives on different hierarchy levels. We propose the Hierarchical Lead Critic (HLC) - inspired by natural emerging distributions in team structures, where following high-level objectives combines with low-level execution. HLC demonstrates that introducing multiple hierarchies, leveraging local and global perspectives, can lead to improved performance with high sample efficiency and robust policies. Experimental results conducted on cooperative, non-communicative, and partially observable MARL benchmarks demonstrate that HLC outperforms single hierarchy baselines and scales robustly with increasing amounts of agents and difficulty.

</details>


### 54. Hierarchical LLM-Based Multi-Agent Framework with Prompt Optimization for Multi-Robot Task Planning

- **Authors:** Tomoya Kawabe, Rin Takano
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21670v2](http://arxiv.org/abs/2602.21670v2)
- **PDF:** [https://arxiv.org/pdf/2602.21670v2](https://arxiv.org/pdf/2602.21670v2)
- **Categories:** cs.RO, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-robot task planning requires decomposing natural-language instructions into executable actions for heterogeneous robot teams. Conventional Planning Domain Definition Language (PDDL) planners provide rigorous guarantees but struggle to handle ambiguous or long-horizon missions, while large language models (LLMs) can interpret instructions and propose plans but may hallucinate or produce infeasible actions. We present a hierarchical multi-agent LLM-based planner with prompt optimization: an upper layer decomposes tasks and assigns them to lower-layer agents, which generate PDDL problems solved by a classical planner. When plans fail, the system applies TextGrad-inspired textual-gradient updates to optimize each agent's prompt and thereby improve planning accuracy. In addition, meta-prompts are learned and shared across agents within the same layer, enabling efficient prompt optimization in multi-agent settings. On the MAT-THOR benchmark, our planner achieves success rates of 0.95 on compound tasks, 0.84 on complex tasks, and 0.60 on vague tasks, improving over the previous state-of-the-art LaMMA-P by 2, 7, and 15 percentage points respectively. An ablation study shows that the hierarchical structure, prompt optimization, and meta-prompt sharing contribute roughly +59, +37, and +4 percentage points to the overall success rate.

</details>


### 55. Power and Limitations of Aggregation in Compound AI Systems

- **Authors:** Nivasini Ananthakrishnan, Meena Jagadeesan
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21556v1](http://arxiv.org/abs/2602.21556v1)
- **PDF:** [https://arxiv.org/pdf/2602.21556v1](https://arxiv.org/pdf/2602.21556v1)
- **Categories:** cs.AI, cs.GT


> The paper formally characterizes when aggregating multiple copies of the same model can enlarge the set of outputs a system designer can reliably elicit. Using a stylized principal‑agent framework, the authors prove that any aggregation that expands elicitability must operate via one of three mechanisms—feasibility expansion, support expansion, or binding‑set contraction—and they give strengthened necessary‑and‑sufficient conditions that fully capture these mechanisms. Empirical tests on a toy reference‑generation task with large language models confirm that aggregation can indeed overcome certain prompt‑engineering and capability limits, illustrating the practical relevance of the theoretical results for designing compound, agentic AI systems.


<details>
<summary>Abstract</summary>

When designing compound AI systems, a common approach is to query multiple copies of the same model and aggregate the responses to produce a synthesized output. Given the homogeneity of these models, this raises the question of whether aggregation unlocks access to a greater set of outputs than querying a single model. In this work, we investigate the power and limitations of aggregation within a stylized principal-agent framework. This framework models how the system designer can partially steer each agent's output through its reward function specification, but still faces limitations due to prompt engineering ability and model capabilities. Our analysis uncovers three natural mechanisms -- feasibility expansion, support expansion, and binding set contraction -- through which aggregation expands the set of outputs that are elicitable by the system designer. We prove that any aggregation operation must implement one of these mechanisms in order to be elicitability-expanding, and that strengthened versions of these mechanisms provide necessary and sufficient conditions that fully characterize elicitability-expansion. Finally, we provide an empirical illustration of our findings for LLMs deployed in a toy reference-generation task. Altogether, our results take a step towards characterizing when compound AI systems can overcome limitations in model capabilities and in prompt engineering.

</details>


### 56. Reasoning-Driven Design of Single Atom Catalysts via a Multi-Agent Large Language Model Framework

- **Authors:** Dong Hyeon Mok, Seoin Back, Victor Fung, Guoxiang Hu
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21533v1](http://arxiv.org/abs/2602.21533v1)
- **PDF:** [https://arxiv.org/pdf/2602.21533v1](https://arxiv.org/pdf/2602.21533v1)
- **Categories:** cond-mat.mtrl-sci, cs.LG


> The paper introduces **MAESTRO**, a multi‑agent framework that harnesses several specialized large language models (LLMs) to autonomously design single‑atom electrocatalysts for the oxygen‑reduction reaction. By embedding the agents in a closed‑loop workflow—reasoning about candidate structures, proposing modifications, reflecting on simulated performance, and updating a shared design history—the system leverages in‑context learning to extract design principles that were not pre‑programmed, ultimately identifying catalysts that violate traditional scaling relations between reaction intermediates. The results demonstrate that coordinated, reasoning‑driven LLM agents can generate novel chemical insights and outperform conventional ML approaches in materials discovery, showcasing a powerful new paradigm for agentic AI in scientific research.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are becoming increasingly applied beyond natural language processing, demonstrating strong capabilities in complex scientific tasks that traditionally require human expertise. This progress has extended into materials discovery, where LLMs introduce a new paradigm by leveraging reasoning and in-context learning, capabilities absent from conventional machine learning approaches. Here, we present a Multi-Agent-based Electrocatalyst Search Through Reasoning and Optimization (MAESTRO) framework in which multiple LLMs with specialized roles collaboratively discover high-performance single atom catalysts for the oxygen reduction reaction. Within an autonomous design loop, agents iteratively reason, propose modifications, reflect on results and accumulate design history. Through in-context learning enabled by this iterative process, MAESTRO identified design principles not explicitly encoded in the LLMs' background knowledge and successfully discovered catalysts that break conventional scaling relations between reaction intermediates. These results highlight the potential of multi-agent LLM frameworks as a powerful strategy to generate chemical insight and discover promising catalysts.

</details>


### 57. Training Generalizable Collaborative Agents via Strategic Risk Aversion

- **Authors:** Chengrui Qu, Yizhou Zhang, Nicolas Lanzetti, Eric Mazumdar
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21515v2](http://arxiv.org/abs/2602.21515v2)
- **PDF:** [https://arxiv.org/pdf/2602.21515v2](https://arxiv.org/pdf/2602.21515v2)
- **Categories:** cs.LG, cs.AI, cs.MA


> The paper introduces **strategic risk aversion** as a new inductive bias for training collaborative agents that remain effective when paired with previously unseen partners. By formalizing risk‑averse behavior as a constraint in multi‑agent reinforcement learning, the authors embed it into standard policy‑optimization (e.g., PPO) to produce policies that avoid free‑riding and are robust to partner deviations; they also prove that such agents can achieve equilibria superior to classic Nash outcomes. Empirical evaluations on a suite of collaborative benchmarks—including a language‑model‑to‑language‑model task—show that the risk‑averse MARL algorithm consistently outperforms existing baselines, delivering stable, high‑performing cooperation with heterogeneous and novel partners.


<details>
<summary>Abstract</summary>

Many emerging agentic paradigms require agents to collaborate with one another (or people) to achieve shared goals. Unfortunately, existing approaches to learning policies for such collaborative problems produce brittle solutions that fail when paired with new partners. We attribute these failures to a combination of free-riding during training and a lack of strategic robustness. To address these problems, we study the concept of strategic risk aversion and interpret it as a principled inductive bias for generalizable cooperation with unseen partners. While strategically risk-averse players are robust to deviations in their partner's behavior by design, we show that, in collaborative games, they also (1) can have better equilibrium outcomes than those at classical game-theoretic concepts like Nash, and (2) exhibit less or no free-riding. Inspired by these insights, we develop a multi-agent reinforcement learning (MARL) algorithm that integrates strategic risk aversion into standard policy optimization methods. Our empirical results across collaborative benchmarks (including an LLM collaboration task) validate our theory and demonstrate that our approach consistently achieves reliable collaboration with heterogeneous and previously unseen partners across collaborative tasks.

</details>


### 58. Both Ends Count! Just How Good are LLM Agents at "Text-to-Big SQL"?

- **Authors:** Germán T. Eizaguirre, Lars Tissen, Marc Sánchez-Artigas
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21480v2](http://arxiv.org/abs/2602.21480v2)
- **PDF:** [https://arxiv.org/pdf/2602.21480v2](https://arxiv.org/pdf/2602.21480v2)
- **Categories:** cs.DB, cs.CL, cs.IR


> The paper introduces “Text‑to‑Big SQL,” a new evaluation framework that extends traditional text‑to‑SQL benchmarks to capture execution‑time, monetary cost, and scalability when LLM agents generate queries for large‑scale data pipelines. By defining database‑agnostic, scale‑sensitive metrics and testing state‑of‑the‑art production LLM agents (e.g., GPT‑4, Claude, Llama 2) on realistic big‑data workloads, the authors demonstrate that conventional accuracy‑only scores dramatically overestimate performance, while their metrics reveal substantial latency and cost penalties caused by seemingly minor translation errors. The study provides the first cross‑model, fine‑grained analysis of how LLM‑driven agents behave under big‑data conditions, highlighting the need for cost‑aware evaluation and prompting future work on optimizing agentic SQL generation for scalable environments.


<details>
<summary>Abstract</summary>

Text-to-SQL and Big Data are both extensively benchmarked fields, yet there is limited research that evaluates them jointly. In the real world, Text-to-SQL systems are often embedded with Big Data workflows, such as large-scale data processing or interactive data analytics. We refer to this as "Text-to-Big SQL". However, existing text-to-SQL benchmarks remain narrowly scoped and overlook the cost and performance implications that arise at scale. For instance, translation errors that are minor on small datasets lead to substantial cost and latency overheads as data scales, a relevant issue completely ignored by text-to-SQL metrics.
  In this paper, we overcome this overlooked challenge by introducing novel and representative metrics for evaluating Text-to-Big SQL. Our study focuses on production-level LLM agents, a database-agnostic system adaptable to diverse user needs. Via an extensive evaluation of frontier models, we show that text-to-SQL metrics are insufficient for Big Data. In contrast, our proposed text-to-Big SQL metrics accurately reflect execution efficiency, cost, and the impact of data scale. Furthermore, we provide LLM-specific insights, including fine-grained, cross-model comparisons of latency and cost.

</details>


### 59. Pancake: Hierarchical Memory System for Multi-Agent LLM Serving

- **Authors:** Zhengding Hu, Zaifeng Pan, Prabhleen Kaur, Vibha Murthy, Zhongkai Yu, Yue Guan, Zhen Wang, Steven Swanson, Yufei Ding
- **Published:** 2026-02-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21477v1](http://arxiv.org/abs/2602.21477v1)
- **PDF:** [https://arxiv.org/pdf/2602.21477v1](https://arxiv.org/pdf/2602.21477v1)
- **Categories:** cs.MA


> The paper introduces **Pancake**, a hierarchical, multi‑tier memory architecture designed to handle the large‑scale, high‑frequency, and multi‑agent memory demands of LLM‑based agents. It combines (i) multi‑level index caching for individual agents, (ii) coordinated index sharing among concurrent agents, and (iii) a collaborative GPU‑CPU pipeline that accelerates approximate nearest‑neighbor searches, all exposed through a simple API compatible with frameworks like LangChain and LlamaIndex. Empirical evaluation on realistic multi‑agent workloads shows that Pancake delivers up to **4.29× higher end‑to‑end throughput** compared with existing agentic memory systems, demonstrating a practical solution for scalable, low‑latency memory management in agentic AI.


<details>
<summary>Abstract</summary>

In this work, we identify and address the core challenges of agentic memory management in LLM serving, where large-scale storage, frequent updates, and multiple coexisting agents jointly introduce complex and high-cost approximate nearest neighbor (ANN) searching problems. We present Pancake, a multi-tier agentic memory system that unifies three key techniques: (i) multi-level index caching for single agents, (ii) coordinated index management across multiple agents, and (iii) collaborative GPU-CPU acceleration. Pancake exposes easy-to-use interface that can be integrated into memory-based agents like Mem-GPT, and is compatible with agentic frameworks such as LangChain and LlamaIndex. Experiments on realistic agent workloads show that Pancake substantially outperforms existing frameworks, achieving more than 4.29x end-to-end throughput improvement.

</details>


### 60. From Cooperation to Hierarchy: A Study of Dynamics of Hierarchy Emergence in a Multi-Agent System

- **Authors:** Shanshan Mao, Peter Tino
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21404v1](http://arxiv.org/abs/2602.21404v1)
- **PDF:** [https://arxiv.org/pdf/2602.21404v1](https://arxiv.org/pdf/2602.21404v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

A central premise in evolutionary biology is that individual variation can generate information asymmetries that facilitate the emergence of hierarchical organisation. To examine this process, we develop an agent-based model (ABM) to identify the minimal conditions under which hierarchy arises in dynamic multi-agent systems, focusing on the roles of initial heterogeneity and mutation amplitude across generations. Hierarchical organisation is quantified using the Trophic Incoherence (TI) metric, which captures directional asymmetries in interaction networks. Our results show that even small individual differences can be amplified through repeated local interactions involving reproduction, competition, and cooperation, but that hierarchical order is markedly more sensitive to mutation amplitude than to initial heterogeneity. Across repeated trials, stable hierarchies reliably emerge only when mutation amplitude is sufficiently high, while initial heterogeneity primarily affects early formation rather than long-term persistence. Overall, these findings demonstrate how simple interaction rules can give rise to both the emergence and persistence of hierarchical organisation, providing a quantitative account of how structured inequality can develop from initially homogeneous populations.

</details>


### 61. The Headless Firm: How AI Reshapes Enterprise Boundaries

- **Authors:** Tassilo Klein, Sebastian Wieczorek
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21401v1](http://arxiv.org/abs/2602.21401v1)
- **PDF:** [https://arxiv.org/pdf/2602.21401v1](https://arxiv.org/pdf/2602.21401v1)
- **Categories:** cs.GT, cs.AI, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The boundary of the firm is determined by coordination cost. We argue that agentic AI induces a structural change in how coordination costs scale: in prior modular systems, integration cost grew with interaction topology (O(n^2) in the number of components); in protocol-mediated agentic systems, integration cost collapses to O(n) while verification scales with task throughput rather than interaction count. This shift selects for a specific organizational equilibrium -- the Headless Firm -- structured as an hourglass: a personalized generative interface at the top, a standardized protocol waist in the middle, and a competitive market of micro-specialized execution agents at the bottom. We formalize this claim as a coordination cost model with two falsifiable empirical predictions: (1) the marginal cost of adding an execution provider should be approximately constant in a mature hourglass ecosystem; (2) the ratio of total coordination cost to task throughput should remain stable as ecosystem size grows. We derive conditions for hourglass stability versus re-centralization and analyze implications for firm size distributions, labor markets, and software economics. The analysis predicts a domain-conditional Great Unbundling: in high knowledge-velocity domains, firm size distributions shift mass from large integrated incumbents toward micro-specialized agents and thin protocol orchestrators.

</details>


### 62. Black-Box Reliability Certification for AI Agents via Self-Consistency Sampling and Conformal Calibration

- **Authors:** Charafeddine Mouzouni
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21368v1](http://arxiv.org/abs/2602.21368v1)
- **PDF:** [https://arxiv.org/pdf/2602.21368v1](https://arxiv.org/pdf/2602.21368v1)
- **Categories:** cs.LG, cs.AI, cs.CL, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

Given a black-box AI system and a task, at what confidence level can a practitioner trust the system's output? We answer with a reliability level -- a single number per system-task pair, derived from self-consistency sampling and conformal calibration, that serves as a black-box deployment gate with exact, finite-sample, distribution-free guarantees. Self-consistency sampling reduces uncertainty exponentially; conformal calibration guarantees correctness within 1/(n+1) of the target level, regardless of the system's errors -- made transparently visible through larger answer sets for harder questions. Weaker models earn lower reliability levels (not accuracy -- see Definition 2.4): GPT-4.1 earns 94.6% on GSM8K and 96.8% on TruthfulQA, while GPT-4.1-nano earns 89.8% on GSM8K and 66.5% on MMLU. We validate across five benchmarks, five models from three families, and both synthetic and real data. Conditional coverage on solvable items exceeds 0.93 across all configurations; sequential stopping reduces API costs by around 50%.

</details>


### 63. A Hierarchical Multi-Agent System for Autonomous Discovery in Geoscientific Data Archives

- **Authors:** Dmitrii Pantiukhin, Ivan Kuznetsov, Boris Shapkin, Antonia Anna Jost, Thomas Jung, Nikolay Koldunov
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21351v1](http://arxiv.org/abs/2602.21351v1)
- **PDF:** [https://arxiv.org/pdf/2602.21351v1](https://arxiv.org/pdf/2602.21351v1)
- **Categories:** cs.AI, cs.IR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid accumulation of Earth science data has created a significant scalability challenge; while repositories like PANGAEA host vast collections of datasets, citation metrics indicate that a substantial portion remains underutilized, limiting data reusability. Here we present PANGAEA-GPT, a hierarchical multi-agent framework designed for autonomous data discovery and analysis. Unlike standard Large Language Model (LLM) wrappers, our architecture implements a centralized Supervisor-Worker topology with strict data-type-aware routing, sandboxed deterministic code execution, and self-correction via execution feedback, enabling agents to diagnose and resolve runtime errors. Through use-case scenarios spanning physical oceanography and ecology, we demonstrate the system's capacity to execute complex, multi-step workflows with minimal human intervention. This framework provides a methodology for querying and analyzing heterogeneous repository data through coordinated agent workflows.

</details>


### 64. Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data

- **Authors:** Emre Can Acikgoz, Cheng Qian, Jonas Hübotter, Heng Ji, Dilek Hakkani-Tür, Gokhan Tur
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21320v1](http://arxiv.org/abs/2602.21320v1)
- **PDF:** [https://arxiv.org/pdf/2602.21320v1](https://arxiv.org/pdf/2602.21320v1)
- **Categories:** cs.LG


> The paper introduces **Tool‑R0**, a self‑play reinforcement‑learning framework that trains a pair of LLM‑based agents—a task Generator and a Solver—from a single base model without any pre‑collected data. The Generator continuously creates novel, difficulty‑matched tool‑use problems, while the Solver learns to execute them using real‑world tool calls, yielding an open‑ended curriculum that drives mutual improvement. Empirically, Tool‑R0 achieves a 92.5 % relative gain over the base model and outperforms fully supervised tool‑calling baselines, demonstrating that zero‑data self‑evolution can produce highly capable, general‑purpose tool‑using agents.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are becoming the foundation for autonomous agents that can use tools to solve complex tasks. Reinforcement learning (RL) has emerged as a common approach for injecting such agentic capabilities, but typically under tightly controlled training setups. It often depends on carefully constructed task-solution pairs and substantial human supervision, which creates a fundamental obstacle to open-ended self-evolution toward superintelligent systems. In this paper, we propose Tool-R0 framework for training general purpose tool-calling agents from scratch with self-play RL, under a zero-data assumption. Initialized from the same base LLM, Tool-R0 co-evolves a Generator and a Solver with complementary rewards: one proposes targeted challenging tasks at the other's competence frontier and the other learns to solve them with real-world tool calls. This creates a self-evolving cycle that requires no pre-existing tasks or datasets. Evaluation on different tool-use benchmarks show that Tool-R0 yields 92.5 relative improvement over the base model and surpasses fully supervised tool-calling baselines under the same setting. Our work further provides empirical insights into self-play LLM agents by analyzing co-evolution, curriculum dynamics, and scaling behavior.

</details>


### 65. Uncertainty-Aware Diffusion Model for Multimodal Highway Trajectory Prediction via DDIM Sampling

- **Authors:** Marion Neumeier, Niklas Roßberg, Michael Botsch, Wolfgang Utschick
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21319v1](http://arxiv.org/abs/2602.21319v1)
- **PDF:** [https://arxiv.org/pdf/2602.21319v1](https://arxiv.org/pdf/2602.21319v1)
- **Categories:** cs.LG, cs.CV, cs.RO


> The paper presents **cVMDx**, an uncertainty‑aware diffusion framework for multimodal highway trajectory prediction that dramatically speeds up inference by replacing the original stochastic diffusion sampling with deterministic DDIM sampling, achieving up to **100× faster generation** while preserving the ability to produce diverse futures. The authors augment the diffusion pipeline with a **Gaussian‑Mixture‑Model post‑processor** to convert the sampled trajectories into tractable multimodal probability distributions, and they explore a **CVQ‑VAE encoder** for richer scenario representations. Experiments on the highD dataset demonstrate that cVMDx attains **higher prediction accuracy** and **substantially lower latency** than the prior cVMD method, enabling practical, stochastic, and uncertainty‑aware forecasting for autonomous‑driving agents.


<details>
<summary>Abstract</summary>

Accurate and uncertainty-aware trajectory prediction remains a core challenge for autonomous driving, driven by complex multi-agent interactions, diverse scene contexts and the inherently stochastic nature of future motion. Diffusion-based generative models have recently shown strong potential for capturing multimodal futures, yet existing approaches such as cVMD suffer from slow sampling, limited exploitation of generative diversity and brittle scenario encodings.
  This work introduces cVMDx, an enhanced diffusion-based trajectory prediction framework that improves efficiency, robustness and multimodal predictive capability. Through DDIM sampling, cVMDx achieves up to a 100x reduction in inference time, enabling practical multi-sample generation for uncertainty estimation. A fitted Gaussian Mixture Model further provides tractable multimodal predictions from the generated trajectories. In addition, a CVQ-VAE variant is evaluated for scenario encoding. Experiments on the publicly available highD dataset show that cVMDx achieves higher accuracy and significantly improved efficiency over cVMD, enabling fully stochastic, multimodal trajectory prediction.

</details>


### 66. SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards

- **Authors:** Dengjia Zhang, Xiaoou Liu, Lu Cheng, Yaqing Wang, Kenton Murray, Hua Wei
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21158v2](http://arxiv.org/abs/2602.21158v2)
- **PDF:** [https://arxiv.org/pdf/2602.21158v2](https://arxiv.org/pdf/2602.21158v2)
- **Categories:** cs.LG, cs.CL


> The paper introduces **SELAUR**, a reinforcement‑learning framework that augments reward signals for LLM‑based agents with fine‑grained uncertainty estimates (entropy, least‑confidence, and margin) computed at the token level, and reshapes both step‑ and trajectory‑level rewards to be “confidence‑aware” and failure‑sensitive. By integrating these uncertainty‑driven rewards, SELAUR guides exploration toward uncertain decision points and stabilizes learning, enabling the agent to self‑evolve without external supervision. Empirical results on the ALFWorld and WebShop benchmarks show consistent gains in task success rates over strong baselines, and ablations confirm that the uncertainty components are the primary drivers of improved exploration efficiency and robustness.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as multi-step decision-making agents, where effective reward design is essential for guiding learning. Although recent work explores various forms of reward shaping and step-level credit assignment, a key signal remains largely overlooked: the intrinsic uncertainty of LLMs. Uncertainty reflects model confidence, reveals where exploration is needed, and offers valuable learning cues even in failed trajectories. We introduce SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards, a reinforcement learning framework that incorporates uncertainty directly into the reward design. SELAUR integrates entropy-, least-confidence-, and margin-based metrics into a combined token-level uncertainty estimate, providing dense confidence-aligned supervision, and employs a failure-aware reward reshaping mechanism that injects these uncertainty signals into step- and trajectory-level rewards to improve exploration efficiency and learning stability. Experiments on two benchmarks, ALFWorld and WebShop, show that our method consistently improves success rates over strong baselines. Ablation studies further demonstrate how uncertainty signals enhance exploration and robustness.

</details>


### 67. SparkMe: Adaptive Semi-Structured Interviewing for Qualitative Insight Discovery

- **Authors:** David Anugraha, Vishakh Padmakumar, Diyi Yang
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21136v1](http://arxiv.org/abs/2602.21136v1)
- **PDF:** [https://arxiv.org/pdf/2602.21136v1](https://arxiv.org/pdf/2602.21136v1)
- **Categories:** cs.HC, cs.AI, cs.CY


> SparkMe introduces a principled, utility‑driven framework for adaptive semi‑structured interviewing, casting the interviewer’s behavior as an optimization problem that balances coverage of a predefined topic guide, discovery of emergent themes, and interview length. The system implements a multi‑agent LLM architecture that performs deliberative planning via simulated conversation rollouts to select questions with maximal expected utility, enabling dynamic follow‑ups and deep dives. Empirical results show that SparkMe outperforms prior LLM interviewers by increasing topic‑guide coverage by ≈ 4.7 % and eliciting richer emergent insights while using fewer conversational turns, and a user study with 70 professionals confirms that domain experts regard its adaptive interviews as higher‑quality and more informative for AI‑impact analysis.


<details>
<summary>Abstract</summary>

Qualitative insights from user experiences are critical for informing product and policy decisions, but collecting such data at scale is constrained by the time and availability of experts to conduct semi-structured interviews. Recent work has explored using large language models (LLMs) to automate interviewing, yet existing systems lack a principled mechanism for balancing systematic coverage of predefined topics with adaptive exploration, or the ability to pursue follow-ups, deep dives, and emergent themes that arise organically during conversation. In this work, we formulate adaptive semi-structured interviewing as an optimization problem over the interviewer's behavior. We define interview utility as a trade-off between coverage of a predefined interview topic guide, discovery of relevant emergent themes, and interview cost measured by length. Based on this formulation, we introduce SparkMe, a multi-agent LLM interviewer that performs deliberative planning via simulated conversation rollouts to select questions with high expected utility. We evaluate SparkMe through controlled experiments with LLM-based interviewees, showing that it achieves higher interview utility, improving topic guide coverage (+4.7% over the best baseline) and eliciting richer emergent insights while using fewer conversational turns than prior LLM interviewing approaches. We further validate SparkMe in a user study with 70 participants across 7 professions on the impact of AI on their workflows. Domain experts rate SparkMe as producing high-quality adaptive interviews that surface helpful profession-specific insights not captured by prior approaches. The code, datasets, and evaluation protocols for SparkMe are available as open-source at https://github.com/SALT-NLP/SparkMe.

</details>


### 68. Cooperative-Competitive Team Play of Real-World Craft Robots

- **Authors:** Rui Zhao, Xihui Li, Yizheng Zhang, Yuzhen Liu, Zhong Zhang, Yufeng Zhang, Cheng Zhou, Zhengyou Zhang, Lei Han
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21119v1](http://arxiv.org/abs/2602.21119v1)
- **PDF:** [https://arxiv.org/pdf/2602.21119v1](https://arxiv.org/pdf/2602.21119v1)
- **Categories:** cs.RO, cs.AI


> The paper presents a full-stack platform for training and deploying multi‑robot agents, comprising a high‑fidelity simulator, a distributed multi‑agent RL framework, and a set of physical craft robots, and introduces a novel “Out‑of‑Distribution State Initialization” (OODSI) technique to bridge the sim‑to‑real gap. By initializing training episodes from states sampled from a broad distribution—including those unlikely in simulation—the authors enable more robust cooperative and competitive policies that transfer efficiently to hardware; OODSI yields a 20 % improvement in real‑world performance over baseline sim‑to‑real transfer. Experiments on a competitive multi‑robot car game and a cooperative construction task validate that the approach scales to real‑world agentic AI systems, achieving reliable coordination and competition among physical robots.


<details>
<summary>Abstract</summary>

Multi-agent deep Reinforcement Learning (RL) has made significant progress in developing intelligent game-playing agents in recent years. However, the efficient training of collective robots using multi-agent RL and the transfer of learned policies to real-world applications remain open research questions. In this work, we first develop a comprehensive robotic system, including simulation, distributed learning framework, and physical robot components. We then propose and evaluate reinforcement learning techniques designed for efficient training of cooperative and competitive policies on this platform. To address the challenges of multi-agent sim-to-real transfer, we introduce Out of Distribution State Initialization (OODSI) to mitigate the impact of the sim-to-real gap. In the experiments, OODSI improves the Sim2Real performance by 20%. We demonstrate the effectiveness of our approach through experiments with a multi-robot car competitive game and a cooperative task in real-world settings.

</details>


### 69. Matching Multiple Experts: On the Exploitability of Multi-Agent Imitation Learning

- **Authors:** Antoine Bergerault, Volkan Cevher, Negar Mehr
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21020v1](http://arxiv.org/abs/2602.21020v1)
- **PDF:** [https://arxiv.org/pdf/2602.21020v1](https://arxiv.org/pdf/2602.21020v1)
- **Categories:** cs.LG, cs.GT, cs.MA


> The paper shows that, in general n‑player Markov games, offline multi‑agent imitation learning cannot guarantee low‑exploitable policies: even exact state‑action distribution matching may leave a large Nash gap, and determining that gap from a given measure‑matching error is computationally hard. To overcome these impossibility results, the authors assume that the expert equilibrium satisfies strategic dominance (or a related best‑response continuity property) and prove that, under a Behavioral‑Cloning error ε₍BC₎, the learned policies achieve a Nash‑imitation gap of O(n ε₍BC₎ / (1 − γ)²), with the continuity condition naturally induced by common regularization schemes. These results delineate when multi‑agent imitation learning can yield near‑Nash agents and highlight the necessity of structural assumptions on expert behavior for safe, low‑exploitable agentic AI.


<details>
<summary>Abstract</summary>

Multi-agent imitation learning (MA-IL) aims to learn optimal policies from expert demonstrations of interactions in multi-agent interactive domains. Despite existing guarantees on the performance of the resulting learned policies, characterizations of how far the learned polices are from a Nash equilibrium are missing for offline MA-IL. In this paper, we demonstrate impossibility and hardness results of learning low-exploitable policies in general $n$-player Markov Games. We do so by providing examples where even exact measure matching fails, and demonstrating a new hardness result on characterizing the Nash gap given a fixed measure matching error. We then show how these challenges can be overcome using strategic dominance assumptions on the expert equilibrium. Specifically, for the case of dominant strategy expert equilibria, assuming Behavioral Cloning error $ε_{\text{BC}}$, this provides a Nash imitation gap of $\mathcal{O}\left(nε_{\text{BC}}/(1-γ)^2\right)$ for a discount factor $γ$. We generalize this result with a new notion of best-response continuity, and argue that this is implicitly encouraged by standard regularization techniques.

</details>


### 70. Toward an Agentic Infused Software Ecosystem

- **Authors:** Mark Marron
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20979v1](http://arxiv.org/abs/2602.20979v1)
- **PDF:** [https://arxiv.org/pdf/2602.20979v1](https://arxiv.org/pdf/2602.20979v1)
- **Categories:** cs.SE, cs.AI, cs.PL


> The paper proposes the **Agentic‑Infused Software Ecosystem (AISE)**, a holistic framework that co‑evolves (1) increasingly autonomous AI development agents, (2) a programming language/API layer that serves as a shared communication substrate for humans and agents, and (3) a runtime environment that exposes actionable capabilities to those agents. By analyzing recent trends in code‑completion, autonomous task execution, and tool‑augmented programming, the authors outline a design methodology that integrates these three pillars through standardized interfaces, composable toolkits, and runtime hooks, enabling seamless human‑agent collaboration. Empirical case studies demonstrate that when language/APIs and runtimes are co‑designed with agent capabilities, development speed and correctness improve markedly, highlighting AISE as a concrete roadmap for scaling agentic AI in software engineering.


<details>
<summary>Abstract</summary>

Fully leveraging the capabilities of AI agents in software development requires a rethinking of the software ecosystem itself. To this end, this paper outlines the creation of an Agentic Infused Software Ecosystem (AISE), that rests on three pillars. The first, of course, is the AI agents themselves, which in the past 5 years have moved from simple code completion and toward sophisticated independent development tasks, a trend which will only continue. The second pillar is the programming language and APIs (or tools) that these agents use to accomplish tasks, and increasingly, serve as the communication substrate that humans and AI agents interact and collaborate through. The final pillar is the runtime environment and ecosystem that agents operate within, and which provide the capabilities that programmatic agents use to interface with (and effect actions in) the external world. To realize the vision of AISE, all three pillars must be advanced in a holistic manner, and critically, in a manner that is synergistic for AI agents as they exist today, those that will exist in the future, and for the human developers that work alongside them.

</details>


### 71. Architecting AgentOS: From Token-Level Context to Emergent System-Level Intelligence

- **Authors:** ChengYou Li, XiaoDong Liu, XiangBao Meng, XinYu Zhao
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20934v1](http://arxiv.org/abs/2602.20934v1)
- **PDF:** [https://arxiv.org/pdf/2602.20934v1](https://arxiv.org/pdf/2602.20934v1)
- **Categories:** cs.AI


> The paper introduces **AgentOS**, a unified architectural framework that treats a large language model as a “Reasoning Kernel” managed by OS‑style components (memory paging, interrupt handling, process scheduling) to enable coherent, system‑level intelligence across multiple agents. By redefining the context window as an **Addressable Semantic Space** and adding mechanisms such as **Semantic Slicing** and **Temporal Alignment**, the authors demonstrate how to preserve cognitive state, prevent drift, and orchestrate multi‑agent interactions. Empirical analyses and theoretical mappings show that these OS‑inspired abstractions dramatically improve scalability, robustness, and self‑evolution of autonomous LLM‑based agents, suggesting that future AGI progress will hinge on such system‑level coordination rather than raw model scaling.


<details>
<summary>Abstract</summary>

The paradigm of Large Language Models is undergoing a fundamental transition from static inference engines to dynamic autonomous cognitive systems.While current research primarily focuses on scaling context windows or optimizing prompt engineering the theoretical bridge between micro scale token processing and macro scale systemic intelligence remains fragmented.This paper proposes AgentOS,a holistic conceptual framework that redefines the LLM as a "Reasoning Kernel" governed by structured operating system logic.Central to this architecture is Deep Context Management which conceptualizes the context window as an Addressable Semantic Space rather than a passive buffer.We systematically deconstruct the transition from discrete sequences to coherent cognitive states introducing mechanisms for Semantic Slicing and Temporal Alignment to mitigate cognitive drift in multi-agent orchestration.By mapping classical OS abstractions such as memory paging interrupt handling and process scheduling onto LLM native constructs, this review provides a rigorous roadmap for architecting resilient scalable and self-evolving cognitive environments.Our analysis asserts that the next frontier of AGI development lies in the architectural efficiency of system-level coordination.

</details>


### 72. SoK: Agentic Skills -- Beyond Tool Use in LLM Agents

- **Authors:** Yanna Jiang, Delong Li, Haiyu Deng, Baihe Ma, Xu Wang, Qin Wang, Guangsheng Yu
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20867v1](http://arxiv.org/abs/2602.20867v1)
- **PDF:** [https://arxiv.org/pdf/2602.20867v1](https://arxiv.org/pdf/2602.20867v1)
- **Categories:** cs.CR, cs.AI, cs.CE, cs.ET


> The paper systematically defines and categorizes “agentic skills”—reusable, self‑contained procedural modules that LLM agents can invoke across tasks—and maps their entire lifecycle from discovery to maintenance. It introduces two complementary taxonomies: (1) seven system‑level design patterns for packaging and executing skills (e.g., metadata‑driven progressive disclosure, executable‑code skills, self‑evolving libraries, marketplace distribution) and (2) a representation × scope matrix that classifies skills by their form (natural‑language, code, policy, hybrid) and the environments they target (web, OS, software‑engineering, robotics). Empirical analysis shows that curated skill libraries markedly boost agent success rates, whereas self‑generated skills can hurt performance, and a case study of the “ClawHavoc” attack demonstrates severe supply‑chain and prompt‑injection risks, underscoring the need for robust, verifiable, and certifiable skill infrastructures in autonomous AI systems.


<details>
<summary>Abstract</summary>

Agentic systems increasingly rely on reusable procedural capabilities, \textit{a.k.a., agentic skills}, to execute long-horizon workflows reliably. These capabilities are callable modules that package procedural knowledge with explicit applicability conditions, execution policies, termination criteria, and reusable interfaces. Unlike one-off plans or atomic tool calls, skills operate (and often do well) across tasks.
  This paper maps the skill layer across the full lifecycle (discovery, practice, distillation, storage, composition, evaluation, and update) and introduces two complementary taxonomies. The first is a system-level set of \textbf{seven design patterns} capturing how skills are packaged and executed in practice, from metadata-driven progressive disclosure and executable code skills to self-evolving libraries and marketplace distribution. The second is an orthogonal \textbf{representation $\times$ scope} taxonomy describing what skills \emph{are} (natural language, code, policy, hybrid) and what environments they operate over (web, OS, software engineering, robotics).
  We analyze the security and governance implications of skill-based agents, covering supply-chain risks, prompt injection via skill payloads, and trust-tiered execution, grounded by a case study of the ClawHavoc campaign in which nearly 1{,}200 malicious skills infiltrated a major agent marketplace, exfiltrating API keys, cryptocurrency wallets, and browser credentials at scale. We further survey deterministic evaluation approaches, anchored by recent benchmark evidence that curated skills can substantially improve agent success rates while self-generated skills may degrade them. We conclude with open challenges toward robust, verifiable, and certifiable skills for real-world autonomous agents.

</details>


### 73. Probing Dec-POMDP Reasoning in Cooperative MARL

- **Authors:** Kale-ab Tessera, Leonard Hinckeldey, Riccardo Zamboni, David Abel, Amos Storkey
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20804v1](http://arxiv.org/abs/2602.20804v1)
- **PDF:** [https://arxiv.org/pdf/2602.20804v1](https://arxiv.org/pdf/2602.20804v1)
- **Categories:** cs.LG, cs.MA


> The paper introduces a diagnostic framework that combines statistical performance baselines with information‑theoretic probes to assess whether cooperative MARL agents truly engage in Dec‑POMDP reasoning—i.e., using history to infer hidden states and coordinate from local observations. Applying this suite to 37 tasks across MPE, SMAX, Overcooked, Hanabi, and MaBrax, the authors find that reactive (memory‑less) policies achieve comparable success to memory‑based agents in more than half the scenarios, and that coordination often hinges on fragile, synchronous action coupling rather than robust temporal influence. Consequently, many popular benchmarks do not reliably require genuine Dec‑POMDP reasoning, calling into question current evaluations of agentic AI progress and motivating the use of the released tools for more rigorous environment design.


<details>
<summary>Abstract</summary>

Cooperative multi-agent reinforcement learning (MARL) is typically framed as a decentralised partially observable Markov decision process (Dec-POMDP), a setting whose hardness stems from two key challenges: partial observability and decentralised coordination. Genuinely solving such tasks requires Dec-POMDP reasoning, where agents use history to infer hidden states and coordinate based on local information. Yet it remains unclear whether popular benchmarks actually demand this reasoning or permit success via simpler strategies. We introduce a diagnostic suite combining statistically grounded performance comparisons and information-theoretic probes to audit the behavioural complexity of baseline policies (IPPO and MAPPO) across 37 scenarios spanning MPE, SMAX, Overcooked, Hanabi, and MaBrax. Our diagnostics reveal that success on these benchmarks rarely requires genuine Dec-POMDP reasoning. Reactive policies match the performance of memory-based agents in over half the scenarios, and emergent coordination frequently relies on brittle, synchronous action coupling rather than robust temporal influence. These findings suggest that some widely used benchmarks may not adequately test core Dec-POMDP assumptions under current training paradigms, potentially leading to over-optimistic assessments of progress. We release our diagnostic tooling to support more rigorous environment design and evaluation in cooperative MARL.

</details>


### 74. Pipeline for Verifying LLM-Generated Mathematical Solutions

- **Authors:** Varvara Sazonova, Dmitri Shmelkin, Stanislav Kikot, Vasily Motolygin
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20770v1](http://arxiv.org/abs/2602.20770v1)
- **PDF:** [https://arxiv.org/pdf/2602.20770v1](https://arxiv.org/pdf/2602.20770v1)
- **Categories:** cs.AI


> The paper presents a verification pipeline that augments standard answer‑checking for Large Reasoning Models (LRMs) by automatically and interactively confirming the correctness of their full mathematical solutions. It does so through a three‑agent architecture—prompt‑generation, solution‑formatting, and proof‑assistant verification (leveraging Lean 4 and small models ≤ 8 B)—which transforms LLM outputs into a form amenable to formal proof checking while also supporting informal validation. Experiments on multiple benchmark datasets show that the pipeline yields a very low false‑positive rate and can serve both as a rigorous evaluator and as a generator of verified solutions, offering a practical tool for agentic AI systems that must reason reliably in mathematics.


<details>
<summary>Abstract</summary>

With the growing popularity of Large Reasoning Models and their results in solving mathematical problems, it becomes crucial to measure their capabilities. We introduce a pipeline for both automatic and interactive verification as a more accurate alternative to only checking the answer which is currently the most popular approach for benchmarks. The pipeline can also be used as a generator of correct solutions both in formal and informal languages. 3 AI agents, which can be chosen for the benchmark accordingly, are included in the structure. The key idea is the use of prompts to obtain the solution in the specific form which allows for easier verification using proof assistants and possible use of small models ($\le 8B$). Experiments on several datasets suggest low probability of False Positives. The open-source implementation with instructions on setting up a server is available at https://github.com/LogicEnj/lean4_verification_pipeline.

</details>


### 75. AdapTools: Adaptive Tool-based Indirect Prompt Injection Attacks on Agentic LLMs

- **Authors:** Che Wang, Jiaming Zhang, Ziqi Zhang, Zijie Wang, Yinghui Wang, Jianbo Gao, Tao Wei, Zhong Chen, Wei Yang Bryan Lim
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20720v1](http://arxiv.org/abs/2602.20720v1)
- **PDF:** [https://arxiv.org/pdf/2602.20720v1](https://arxiv.org/pdf/2602.20720v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The integration of external data services (e.g., Model Context Protocol, MCP) has made large language model-based agents increasingly powerful for complex task execution. However, this advancement introduces critical security vulnerabilities, particularly indirect prompt injection (IPI) attacks. Existing attack methods are limited by their reliance on static patterns and evaluation on simple language models, failing to address the fast-evolving nature of modern AI agents. We introduce AdapTools, a novel adaptive IPI attack framework that selects stealthier attack tools and generates adaptive attack prompts to create a rigorous security evaluation environment. Our approach comprises two key components: (1) Adaptive Attack Strategy Construction, which develops transferable adversarial strategies for prompt optimization, and (2) Attack Enhancement, which identifies stealthy tools capable of circumventing task-relevance defenses. Comprehensive experimental evaluation shows that AdapTools achieves a 2.13 times improvement in attack success rate while degrading system utility by a factor of 1.78. Notably, the framework maintains its effectiveness even against state-of-the-art defense mechanisms. Our method advances the understanding of IPI attacks and provides a useful reference for future research.

</details>


### 76. ToolMATH: A Math Tool Benchmark for Realistic Long-Horizon Multi-Tool Reasoning

- **Authors:** Hyeonje Choi, Jeongsoo Lee, Hyojun Lee, Jay-Yoon Lee
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21265v1](http://arxiv.org/abs/2602.21265v1)
- **PDF:** [https://arxiv.org/pdf/2602.21265v1](https://arxiv.org/pdf/2602.21265v1)
- **Categories:** cs.CL, cs.LG, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce \ToolMATH, a math-grounded benchmark that evaluates tool-augmented language models in realistic multi-tool environments where the output depends on calling schema-specified tools and sustaining multi-step execution. It turns math problems into a controlled, correctness-checkable benchmark with tool sets, enabling systematic evaluation of model reliability under (1) large, overlapping tool catalogs and (2) the absence of the intended capability. \ToolMATH provides actionable diagnostic evidence of failure modes in tool-augmented agents, helping identify the control mechanisms required for robustness. \ToolMATH roughly contains 8k questions and 12k tools; we provide an additional hard-set \ToolMATHHard with questions and tools. Our evaluation reveals that the key failure factor is due to the inability to reason, leading to the accumulation of intermediate results' errors and constrain later decisions. Tool-list redundancy do not simply add noise, but amplify small early deviations into irreversible execution drift. The benchmark highlights that when the intended capability is missing, distractor tools can sometimes serve as partial substitutes in solution paths, yet they can also mislead models into ungrounded tool trajectories. Finally, comparisons between tool-use protocols emphasize that improvements come less from local action selection and more from long-range plan coherence and disciplined use of observations.

</details>


### 77. Agile V: A Compliance-Ready Framework for AI-Augmented Engineering -- From Concept to Audit-Ready Delivery

- **Authors:** Christopher Koch, Joshua Andreas Wellbrock
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20684v1](http://arxiv.org/abs/2602.20684v1)
- **PDF:** [https://arxiv.org/pdf/2602.20684v1](https://arxiv.org/pdf/2602.20684v1)
- **Categories:** cs.SE, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Current AI-assisted engineering workflows lack a built-in mechanism to maintain task-level verification and regulatory traceability at machine-speed delivery. Agile V addresses this gap by embedding independent verification and audit artifact generation into each task cycle. The framework merges Agile iteration with V-Model verification into a continuous Infinity Loop, deploying specialized AI agents for requirements, design, build, test, and compliance, governed by mandatory human approval gates. We evaluate three hypotheses: (H1) audit-ready artifacts emerge as a by-product of development, (H2) 100% requirement-level verification is achievable with independent test generation, and (H3) verified increments can be delivered with single-digit human interactions per cycle. A feasibility case study on a Hardware-in-the-Loop system (about 500 LOC, 8 requirements, 54 tests) supports all three hypotheses: audit-ready documentation was generated automatically (H1), 100% requirement-level pass rate was achieved (H2), and only 6 prompts per cycle were required (H3), yielding an estimated 10-50x cost reduction versus a COCOMO II baseline (sensitivity range from pessimistic to optimistic assumptions). We invite independent replication to validate generalizability.

</details>


### 78. Maximin Share Guarantees via Limited Cost-Sensitive Sharing

- **Authors:** Hana Salavcova, Martin Černý, Arpita Biswas
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20541v2](http://arxiv.org/abs/2602.20541v2)
- **PDF:** [https://arxiv.org/pdf/2602.20541v2](https://arxiv.org/pdf/2602.20541v2)
- **Categories:** cs.GT, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study the problem of fairly allocating indivisible goods when limited sharing is allowed, that is, each good may be allocated to up to $k$ agents, while incurring a cost for sharing. While classic maximin share (MMS) allocations may not exist in many instances, we demonstrate that allowing controlled sharing can restore fairness guarantees that are otherwise unattainable in certain scenarios. (1) Our first contribution shows that exact maximin share (MMS) allocations are guaranteed to exist whenever goods are allowed to be cost-sensitively shared among at least half of the agents and the number of agents is even; for odd numbers of agents, we obtain a slightly weaker MMS guarantee. (2) We further design a Shared Bag-Filling Algorithm that guarantees a $(1 - C)(k - 1)$-approximate MMS allocation, where $C$ is the maximum cost of sharing a good. Notably, when $(1 - C)(k - 1) \geq 1$, our algorithm recovers an exact MMS allocation. (3) We additionally introduce the Sharing Maximin Share (SMMS) fairness notion, a natural extension of MMS to the $k$-sharing setting. (4) We show that SMMS allocations always exist under identical utilities and for instances with two agents. (5) We construct a counterexample to show the impossibility of the universal existence of an SMMS allocation. (6) Finally, we establish a connection between SMMS and constrained MMS (CMMS), yielding approximation guarantees for SMMS via existing CMMS results. These contributions provide deep theoretical insights for the problem of fair resource allocation when a limited sharing of resources are allowed in multi-agent environments.

</details>


### 79. Under the Influence: Quantifying Persuasion and Vigilance in Large Language Models

- **Authors:** Sasha Robinson, Kerem Oktar, Katherine M. Collins, Ilia Sucholutsky, Kelsey R. Allen
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21262v2](http://arxiv.org/abs/2602.21262v2)
- **PDF:** [https://arxiv.org/pdf/2602.21262v2](https://arxiv.org/pdf/2602.21262v2)
- **Categories:** cs.CL, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

With increasing integration of Large Language Models (LLMs) into areas of high-stakes human decision-making, it is important to understand the risks they introduce as advisors. To be useful advisors, LLMs must sift through large amounts of content, written with both benevolent and malicious intent, and then use this information to convince a user to take a specific action. This involves two social capacities: vigilance (the ability to determine which information to use, and which to discard) and persuasion (synthesizing the available evidence to make a convincing argument). While existing work has investigated these capacities in isolation, there has been little prior investigation of how these capacities may be linked. Here, we use a simple multi-turn puzzle-solving game, Sokoban, to study LLMs' abilities to persuade and be rationally vigilant towards other LLM agents. We find that puzzle-solving performance, persuasive capability, and vigilance are dissociable capacities in LLMs. Performing well on the game does not automatically mean a model can detect when it is being misled, even if the possibility of deception is explicitly mentioned. However, LLMs do consistently modulate their token use, using fewer tokens to reason when advice is benevolent and more when it is malicious, even if they are still persuaded to take actions leading them to failure. To our knowledge, our work presents the first investigation of the relationship between persuasion, vigilance, and task performance in LLMs, and suggests that monitoring all three independently will be critical for future work in AI safety.

</details>


### 80. AWCP: A Workspace Delegation Protocol for Deep-Engagement Collaboration across Remote Agents

- **Authors:** Xiaohang Nie, Zihan Guo, Youliang Chen, Yuanjian Zhou, Weinan Zhang
- **Published:** 2026-02-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20493v1](http://arxiv.org/abs/2602.20493v1)
- **PDF:** [https://arxiv.org/pdf/2602.20493v1](https://arxiv.org/pdf/2602.20493v1)
- **Categories:** cs.NI, cs.MA


> The paper introduces the **Agent Workspace Collaboration Protocol (AWCP)**, a lightweight control‑plane that lets an autonomous LLM‑based agent temporarily delegate its file system to a remote peer so the peer can read, write, and invoke its native tools directly—eliminating the “message‑only” bottleneck that forces costly environment reconstruction. The authors implement AWCP as an open‑source reference stack (with pluggable transports and integration into the MCP tool suite) and demonstrate asymmetric, deep‑engagement collaborations where complementary agents jointly edit and execute shared files in real time. Experiments show that workspace delegation dramatically reduces latency and error rates in cross‑agent tool use, establishing a missing “workspace layer” in the agentic protocol stack and paving the way for interoperable, file‑centric agent ecosystems.


<details>
<summary>Abstract</summary>

The rapid evolution of Large Language Model (LLM)-based autonomous agents is reshaping the digital landscape toward an emerging Agentic Web, where increasingly specialized agents must collaborate to accomplish complex tasks. However, existing collaboration paradigms are constrained to message passing, leaving execution environments as isolated silos. This creates a context gap: agents cannot directly manipulate files or invoke tools in a peer's environment, and must instead resort to costly, error-prone environment reconstruction. We introduce the Agent Workspace Collaboration Protocol (AWCP), which bridges this gap through temporary workspace delegation inspired by the Unix philosophy that everything is a file. AWCP decouples a lightweight control plane from pluggable transport mechanisms, allowing a Delegator to project its workspace to a remote Executor, who then operates on the shared files directly with unmodified local toolchains. We provide a fully open-source reference implementation with MCP tool integration and validate the protocol through live demonstrations of asymmetric collaboration, where agents with complementary capabilities cooperate through delegated workspaces. By establishing the missing workspace layer in the agentic protocol stack, AWCP paves the way for a universally interoperable agent ecosystem in which collaboration transcends message boundaries. The protocol and reference implementation are publicly available at https://github.com/SII-Holos/awcp.

</details>


### 81. Implicit Intelligence -- Evaluating Agents on What Users Don't Say

- **Authors:** Ved Sirdeshmukh, Marc Wetter
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20424v1](http://arxiv.org/abs/2602.20424v1)
- **PDF:** [https://arxiv.org/pdf/2602.20424v1](https://arxiv.org/pdf/2602.20424v1)
- **Categories:** cs.AI


> The paper introduces **Implicit Intelligence**, a benchmark that measures how well AI agents infer and respect unstated user constraints—such as accessibility, privacy, safety, and contextual factors—rather than merely following explicit prompts. To evaluate this, the authors build **Agent‑as‑a‑World (AaW)**, a lightweight harness that encodes interactive environments in human‑readable YAML files and runs them via language‑model simulations, allowing agents to explore and discover hidden requirements before acting. Across 205 scenarios and 16 state‑of‑the‑art models, the best system solves only 48.3 % of cases, highlighting a significant gap between current prompt‑following abilities and the contextual, goal‑oriented reasoning needed for truly agentic AI.


<details>
<summary>Abstract</summary>

Real-world requests to AI agents are fundamentally underspecified. Natural human communication relies on shared context and unstated constraints that speakers expect listeners to infer. Current agentic benchmarks test explicit instruction-following but fail to evaluate whether agents can reason about implicit requirements spanning accessibility needs, privacy boundaries, catastrophic risks, and contextual constraints. We present Implicit Intelligence, an evaluation framework testing whether AI agents can move beyond prompt-following to become genuine goal-fulfillers, paired with Agent-as-a-World (AaW), a harness where interactive worlds are defined in human-readable YAML files and simulated by language models. Our scenarios feature apparent simplicity in user requests, hidden complexity in correct solutions, and discoverability of constraints through environmental exploration. Evaluating 16 frontier and open-weight models across 205 scenarios, we find that even the best-performing model achieves only 48.3% scenario pass rate, revealing substantial room for improvement in bridging the gap between literal instruction-following and human-like contextual reasoning.

</details>


### 82. Gap-Dependent Bounds for Nearly Minimax Optimal Reinforcement Learning with Linear Function Approximation

- **Authors:** Haochen Zhang, Zhong Zheng, Lingzhou Xue
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20297v1](http://arxiv.org/abs/2602.20297v1)
- **PDF:** [https://arxiv.org/pdf/2602.20297v1](https://arxiv.org/pdf/2602.20297v1)
- **Categories:** stat.ML, cs.LG


> The paper delivers the first gap‑dependent regret analysis for the nearly minimax‑optimal algorithm **LSVI‑UCB++**, showing that its regret scales as \(\tilde O\!\bigl(\frac{d^{2}H^{2}}{\Delta}\bigr)\) (up to logarithmic factors) where \(\Delta\) is the minimal sub‑optimality gap, improving on prior gap‑dependent bounds that required worse dependence on the feature dimension \(d\) and horizon \(H\). The authors achieve this by refining the optimism‑in‑the‑face‑of‑uncertainty proof technique to exploit the algorithm’s low policy‑switching property, and they extend the analysis to a parallel multi‑agent setting, proving a gap‑dependent sample‑complexity bound that enjoys a linear speed‑up with the number of agents. These results tighten performance guarantees for linear‑function‑approximation RL and provide a principled way to coordinate multiple agents for faster, gap‑aware exploration.


<details>
<summary>Abstract</summary>

We study gap-dependent performance guarantees for nearly minimax-optimal algorithms in reinforcement learning with linear function approximation. While prior works have established gap-dependent regret bounds in this setting, existing analyses do not apply to algorithms that achieve the nearly minimax-optimal worst-case regret bound $\tilde{O}(d\sqrt{H^3K})$, where $d$ is the feature dimension, $H$ is the horizon length, and $K$ is the number of episodes. We bridge this gap by providing the first gap-dependent regret bound for the nearly minimax-optimal algorithm LSVI-UCB++ (He et al., 2023). Our analysis yields improved dependencies on both $d$ and $H$ compared to previous gap-dependent results. Moreover, leveraging the low policy-switching property of LSVI-UCB++, we introduce a concurrent variant that enables efficient parallel exploration across multiple agents and establish the first gap-dependent sample complexity upper bound for online multi-agent RL with linear function approximation, achieving linear speedup with respect to the number of agents.

</details>


### 83. Quantifying the Expectation-Realisation Gap for Agentic AI Systems

- **Authors:** Sebastian Lobentanzer
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20292v2](http://arxiv.org/abs/2602.20292v2)
- **PDF:** [https://arxiv.org/pdf/2602.20292v2](https://arxiv.org/pdf/2602.20292v2)
- **Categories:** cs.SE, cs.AI


> The paper’s main contribution is a systematic quantification of the “expectation‑realisation gap” for deployed agentic AI systems, showing that promised productivity gains are routinely over‑estimated. By aggregating data from controlled trials and independent validations in software engineering, clinical documentation, and clinical decision support, the authors compare pre‑deployment expectations (e.g., a 24 % speedup for developers) with observed outcomes (e.g., a 19 % slowdown), revealing calibration errors up to 43 percentage points and negligible effects in some clinical tools. The findings attribute these gaps to integration friction, verification overhead, mismatched performance metrics, and uneven benefit distribution, and they argue for structured planning frameworks that explicitly model expected gains together with human oversight costs.


<details>
<summary>Abstract</summary>

Agentic AI systems are deployed with expectations of substantial productivity gains, yet rigorous empirical evidence reveals systematic discrepancies between pre-deployment expectations and post-deployment outcomes. We review controlled trials and independent validations across software engineering, clinical documentation, and clinical decision support to quantify this expectation-realisation gap. In software development, experienced developers expected a 24% speedup from AI tools but were slowed by 19% -- a 43 percentage-point calibration error. In clinical documentation, vendor claims of multi-minute time savings contrast with measured reductions of less than one minute per note, and one widely deployed tool showed no statistically significant effect. In clinical decision support, externally validated performance falls substantially below developer-reported metrics. These shortfalls are driven by workflow integration friction, verification burden, measurement construct mismatches, and systematic variation in who benefits and who does not. The evidence motivates structured planning frameworks that require explicit, quantified benefit expectations with human oversight costs factored in.

</details>


### 84. Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks

- **Authors:** David Schmotz, Luca Beurer-Kellner, Sahar Abdelnabi, Maksym Andriushchenko
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20156v3](http://arxiv.org/abs/2602.20156v3)
- **PDF:** [https://arxiv.org/pdf/2602.20156v3](https://arxiv.org/pdf/2602.20156v3)
- **Categories:** cs.CR, cs.LG


> The paper introduces **Skill‑Inject**, the first systematic benchmark for assessing how vulnerable large‑language‑model (LLM) agents are to “skill‑file” prompt‑injection attacks—malicious code or instructions embedded in third‑party skill modules that extend an agent’s capabilities. By constructing 202 paired tasks that span overtly malicious to subtly hidden injections, the authors evaluate a range of state‑of‑the‑art LLM agents, measuring both their propensity to obey harmful instructions and their ability to follow legitimate ones. The results reveal that current agents are alarmingly insecure—up to 80 % of attacks succeed on frontier models, leading to actions such as data exfiltration and ransomware‑like behavior—and that neither model scaling nor naïve input filtering mitigates the risk, highlighting the need for context‑aware authorization mechanisms in future agentic AI systems.


<details>
<summary>Abstract</summary>

LLM agents are evolving rapidly, powered by code execution, tools, and the recently introduced agent skills feature. Skills allow users to extend LLM applications with specialized third-party code, knowledge, and instructions. Although this can extend agent capabilities to new domains, it creates an increasingly complex agent supply chain, offering new surfaces for prompt injection attacks. We identify skill-based prompt injection as a significant threat and introduce SkillInject, a benchmark evaluating the susceptibility of widely-used LLM agents to injections through skill files. SkillInject contains 202 injection-task pairs with attacks ranging from obviously malicious injections to subtle, context-dependent attacks hidden in otherwise legitimate instructions. We evaluate frontier LLMs on SkillInject, measuring both security in terms of harmful instruction avoidance and utility in terms of legitimate instruction compliance. Our results show that today's agents are highly vulnerable with up to 80% attack success rate with frontier models, often executing extremely harmful instructions including data exfiltration, destructive action, and ransomware-like behavior. They furthermore suggest that this problem will not be solved through model scaling or simple input filtering, but that robust agent security will require context-aware authorization frameworks. Our benchmark is available at https://www.skill-inject.com/.

</details>


### 85. Agentic AI for Scalable and Robust Optical Systems Control

- **Authors:** Zehao Wang, Mingzhe Han, Wei Cheng, Yue-Kai Huang, Philip Ji, Denton Wu, Mahdi Safari, Flemming Holtorf, Kenaish AlQubaisi, Norbert M. Linke, Danyang Zhuo, Yiran Chen, Ting Wang, Dirk Englund, Tingjun Chen
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20144v1](http://arxiv.org/abs/2602.20144v1)
- **PDF:** [https://arxiv.org/pdf/2602.20144v1](https://arxiv.org/pdf/2602.20144v1)
- **Categories:** eess.SY, cs.AI, cs.NI


> AgentOptics introduces a scalable, agentic‑AI framework for autonomous control of heterogeneous optical hardware, built on the Model Context Protocol (MCP) that translates natural‑language requests into structured, tool‑based actions across 64 standardized MCP tools for eight representative devices. By evaluating a 410‑task benchmark that probes request comprehension, role‑aware dialogue, multi‑step coordination, linguistic robustness, and error handling, the authors show that both commercial online LLMs and locally hosted open‑source LLMs achieve 87.7 %–99.0 % task‑success rates—far surpassing LLM‑generated code baselines (≤ 50 %). The framework’s versatility is further validated in five real‑world case studies (e.g., DWDM provisioning, 5G fronthaul ARoF optimization, polarization stabilization, and DAS‑based monitoring), demonstrating that agentic AI can reliably orchestrate complex, closed‑loop optical system operations at scale.


<details>
<summary>Abstract</summary>

We present AgentOptics, an agentic AI framework for high-fidelity, autonomous optical system control built on the Model Context Protocol (MCP). AgentOptics interprets natural language tasks and executes protocol-compliant actions on heterogeneous optical devices through a structured tool abstraction layer. We implement 64 standardized MCP tools across 8 representative optical devices and construct a 410-task benchmark to evaluate request understanding, role-aware responses, multi-step coordination, robustness to linguistic variation, and error handling. We assess two deployment configurations--commercial online LLMs and locally hosted open-source LLMs--and compare them with LLM-based code generation baselines. AgentOptics achieves 87.7%--99.0% average task success rates, significantly outperforming code-generation approaches, which reach up to 50% success. We further demonstrate broader applicability through five case studies extending beyond device-level control to system orchestration, monitoring, and closed-loop optimization. These include DWDM link provisioning and coordinated monitoring of coherent 400 GbE and analog radio-over-fiber (ARoF) channels; autonomous characterization and bias optimization of a wideband ARoF link carrying 5G fronthaul traffic; multi-span channel provisioning with launch power optimization; closed-loop fiber polarization stabilization; and distributed acoustic sensing (DAS)-based fiber monitoring with LLM-assisted event detection. These results establish AgentOptics as a scalable, robust paradigm for autonomous control and orchestration of heterogeneous optical systems.

</details>


### 86. HieraMAS: Optimizing Intra-Node LLM Mixtures and Inter-Node Topology for Multi-Agent Systems

- **Authors:** Tianjun Yao, Zhaoyi Li, Zhiqiang Shen
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20229v1](http://arxiv.org/abs/2602.20229v1)
- **PDF:** [https://arxiv.org/pdf/2602.20229v1](https://arxiv.org/pdf/2602.20229v1)
- **Categories:** cs.MA


> HieraMAS introduces a hierarchical multi‑agent framework that augments each functional role with a **mixture of heterogeneous LLMs** (intra‑node “supernodes”) and jointly optimizes the **inter‑node communication topology**. The authors solve the resulting credit‑assignment problem with a two‑stage algorithm: (1) multi‑level reward attribution that supplies separate performance signals to individual supernodes and to the whole system, and (2) a graph‑classification‑based topology selector that evaluates candidate communication graphs holistically rather than edge‑by‑edge. Across reasoning and coding benchmarks, HieraMAS achieves significantly higher task accuracy and better cost‑performance ratios than prior single‑LLM or topology‑only baselines, demonstrating that combining intra‑node LLM mixtures with learned topologies is a powerful lever for building more capable agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) built on large language models (LLMs) have shown strong performance across many tasks. Most existing approaches improve only one aspect at a time, such as the communication topology, role assignment, or LLM routing, while treating each agent as a single, indivisible unit. This misses the opportunity to use mixtures of LLMs within an agent to strengthen role-specific abilities. We propose HieraMAS, a hierarchical collaboration framework that combines intra-node LLM mixtures with an inter-node communication topology. HieraMAS introduces supernodes, where each functional role is implemented by multiple heterogeneous LLMs using a propose-synthesis structure. Optimizing HieraMAS creates unique credit-assignment challenges: final task performance depends heavily on the underlying LLMs' capabilities, which can lead reinforcement methods to incorrectly reward suboptimal configurations. To address this, we use a two-stage algorithm: (1) multi-level reward attribution, which provides fine-grained feedback at both the node level and the overall system level; (2) graph classification for topology selection, which treats choosing the communication structure as a holistic decision rather than optimizing edges one by one. Experiments on reasoning and coding benchmarks show that HieraMAS substantially outperforms existing methods while also delivering better cost-performance trade-offs.

</details>


### 87. Descent-Guided Policy Gradient for Scalable Cooperative Multi-Agent Learning

- **Authors:** Shan Yang, Yang Liu
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20078v1](http://arxiv.org/abs/2602.20078v1)
- **PDF:** [https://arxiv.org/pdf/2602.20078v1](https://arxiv.org/pdf/2602.20078v1)
- **Categories:** cs.MA, cs.AI, cs.LG


> The paper introduces **Descent‑Guided Policy Gradient (DG‑PG)**, a novel MARL framework that leverages differentiable analytical system models to generate noise‑free “guidance” gradients for each agent, thereby decoupling an agent’s learning signal from the actions of all other agents. By replacing the conventional policy‑gradient estimator with these model‑based guidance gradients, the authors prove that per‑agent gradient variance drops from Θ(N) to O(1), yielding a scale‑invariant sample complexity of O(1/ε) while preserving the cooperative game’s equilibria. Empirically, DG‑PG solves a heterogeneous cloud‑scheduling problem with up to 200 agents in fewer than 10 episodes—orders of magnitude faster than MAPPO or IPPO—and demonstrates that analytical model guidance can fundamentally overcome cross‑agent noise in large‑scale cooperative agentic AI systems.


<details>
<summary>Abstract</summary>

Scaling cooperative multi-agent reinforcement learning (MARL) is fundamentally limited by cross-agent noise: when agents share a common reward, the actions of all $N$ agents jointly determine each agent's learning signal, so cross-agent noise grows with $N$. In the policy gradient setting, per-agent gradient estimate variance scales as $Θ(N)$, yielding sample complexity $\mathcal{O}(N/ε)$. We observe that many domains -- cloud computing, transportation, power systems -- have differentiable analytical models that prescribe efficient system states. In this work, we propose Descent-Guided Policy Gradient (DG-PG), a framework that constructs noise-free per-agent guidance gradients from these analytical models, decoupling each agent's gradient from the actions of all others. We prove that DG-PG reduces gradient variance from $Θ(N)$ to $\mathcal{O}(1)$, preserves the equilibria of the cooperative game, and achieves agent-independent sample complexity $\mathcal{O}(1/ε)$. On a heterogeneous cloud scheduling task with up to 200 agents, DG-PG converges within 10 episodes at every tested scale -- from $N=5$ to $N=200$ -- directly confirming the predicted scale-invariant complexity, while MAPPO and IPPO fail to converge under identical architectures.

</details>


### 88. The LLMbda Calculus: AI Agents, Conversations, and Information Flow

- **Authors:** Zac Garby, Andrew D. Gordon, David Sands
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20064v1](http://arxiv.org/abs/2602.20064v1)
- **PDF:** [https://arxiv.org/pdf/2602.20064v1](https://arxiv.org/pdf/2602.20064v1)
- **Categories:** cs.PL, cs.AI, cs.CR


> The paper introduces **LLMbda**, an untyped call‑by‑value λ‑calculus that models AI agents as sequences of LLM prompts and responses, augmenting the language with dynamic information‑flow control and a primitive that serializes a term, sends it to an LLM, and parses the returned term. By formalizing planner loops and the way malicious prompts can inject code or influence later reasoning, the authors prove a termination‑insensitive non‑interference theorem that guarantees confidentiality and integrity under specified flow restrictions, thereby providing a rigorous semantic foundation for reasoning about safety‑critical agentic systems. The calculus also enables systematic analysis of defenses such as quarantined sub‑conversations and isolated code execution, showing how information‑flow policies can prevent prompt‑injection attacks in practical LLM‑driven agents.


<details>
<summary>Abstract</summary>

A conversation with a large language model (LLM) is a sequence of prompts and responses, with each response generated from the preceding conversation. AI agents build such conversations automatically: given an initial human prompt, a planner loop interleaves LLM calls with tool invocations and code execution. This tight coupling creates a new and poorly understood attack surface. A malicious prompt injected into a conversation can compromise later reasoning, trigger dangerous tool calls, or distort final outputs. Despite the centrality of such systems, we currently lack a principled semantic foundation for reasoning about their behaviour and safety. We address this gap by introducing an untyped call-by-value lambda calculus enriched with dynamic information-flow control and a small number of primitives for constructing prompt-response conversations. Our language includes a primitive that invokes an LLM: it serializes a value, sends it to the model as a prompt, and parses the response as a new term. This calculus faithfully represents planner loops and their vulnerabilities, including the mechanisms by which prompt injection alters subsequent computation. The semantics explicitly captures conversations, and so supports reasoning about defenses such as quarantined sub-conversations, isolation of generated code, and information-flow restrictions on what may influence an LLM call. A termination-insensitive noninterference theorem establishes integrity and confidentiality guarantees, demonstrating that a formal calculus can provide rigorous foundations for safe agentic programming.

</details>


### 89. Interaction Theater: A case of LLM Agents Interacting at Scale

- **Authors:** Sarath Shekkizhar, Adam Earle
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20059v1](http://arxiv.org/abs/2602.20059v1)
- **PDF:** [https://arxiv.org/pdf/2602.20059v1](https://arxiv.org/pdf/2602.20059v1)
- **Categories:** cs.AI


> The paper introduces **Interaction Theater**, an empirical study of large‑scale LLM‑agent communication on the Moltbook platform (≈800 K posts, 3.5 M comments, 78 K agent profiles). By combining lexical specificity (Jaccard), embedding‑based semantic similarity, and LLM‑as‑judge evaluations, the authors show that although agents generate diverse, well‑formed text, the discourse lacks substantive content: 65 % of comments share no distinguishing vocabulary with the target post, information gain drops sharply with each additional comment, and 50 % of remarks are classified as spam or off‑topic, with only 5 % forming true threaded conversations. The findings highlight that without explicit coordination mechanisms, even capable LLM agents default to parallel, superficial output rather than meaningful exchange, underscoring a key design challenge for future multi‑agent AI systems.


<details>
<summary>Abstract</summary>

As multi-agent architectures and agent-to-agent protocols proliferate, a fundamental question arises: what actually happens when autonomous LLM agents interact at scale? We study this question empirically using data from Moltbook, an AI-agent-only social platform, with 800K posts, 3.5M comments, and 78K agent profiles. We combine lexical metrics (Jaccard specificity), embedding-based semantic similarity, and LLM-as-judge validation to characterize agent interaction quality. Our findings reveal agents produce diverse, well-formed text that creates the surface appearance of active discussion, but the substance is largely absent. Specifically, while most agents ($67.5\%$) vary their output across contexts, $65\%$ of comments share no distinguishing content vocabulary with the post they appear under, and information gain from additional comments decays rapidly. LLM judge based metrics classify the dominant comment types as spam ($28\%$) and off-topic content ($22\%$). Embedding-based semantic analysis confirms that lexically generic comments are also semantically generic. Agents rarely engage in threaded conversation ($5\%$ of comments), defaulting instead to independent top-level responses. We discuss implications for multi-agent interaction design, arguing that coordination mechanisms must be explicitly designed; without them, even large populations of capable agents produce parallel output rather than productive exchange.

</details>


### 90. Let There Be Claws: An Early Social Network Analysis of AI Agents on Moltbook

- **Authors:** H. C. W. Price, H. AlMuhanna, P. M. Bassani, M. Ho, T. S. Evans
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20044v1](http://arxiv.org/abs/2602.20044v1)
- **PDF:** [https://arxiv.org/pdf/2602.20044v1](https://arxiv.org/pdf/2602.20044v1)
- **Categories:** physics.soc-ph, cs.AI, cs.CY, cs.SI


> The paper provides the first quantitative snapshot of how autonomous AI agents self‑organize on a newly launched, AI‑native social platform (Moltbook), showing that hierarchical attention structures and role specialization emerge within days rather than over long periods. By extracting 20 k posts and 192 k comments from 15 k accounts, the authors build co‑participation and directed‑comment networks, compute reciprocity, HITS hub/authority scores, Gini coefficients, and apply embedding‑based topic modeling to characterize interaction patterns. They find extreme asymmetry (≈1 % reciprocity), a clear split between hub‑like broadcasters and authority‑like receivers, highly skewed attention (upvote Gini = 0.992 vs. posting Gini = 0.601), rich‑get‑richer dynamics for early agents, and brief, bursty participation—demonstrating that familiar social stratification and amplification mechanisms can arise almost instantly in large‑scale agent ecosystems.


<details>
<summary>Abstract</summary>

Within twelve days of launch, an AI-native social platform exhibits extreme attention concentration, hierarchical role separation, and one-way attention flow, consistent with the hypothesis that stratification in agent ecosystems can emerge rapidly rather than gradually. We analyse publicly observable traces from a 12-day window of Moltbook (28 January -- 8 February 2026), comprising 20,040 posts and 192,410 comments from 15,083 accounts across 759 submolts. We construct co-participation and directed-comment graphs and report reciprocity, community structure, and centrality, alongside descriptive content themes. Under a commenter--post-author tie definition, interaction is strongly asymmetric (reciprocity ~1%), and HITS centrality separates cleanly into hub and authority roles, consistent with broadcast-style attention rather than mutual exchange. Engagement is highly unequal: attention is far more concentrated than production (upvote Gini = 0.992 vs. posting Gini = 0.601), and early-arriving accounts accumulate substantially higher cumulative upvotes prior to exposure-time correction, suggesting rich-get-richer dynamics. Participation is brief and bursty (median observed lifespan 2.48 minutes; 54.8% of posts occur within six peak UTC hours). Embedding-based topic modelling identifies diverse thematic clusters, including technical discussion of memory and identity, onboarding messages, and formulaic token-minting content. These results provide an early structural baseline for large-scale agent--agent social interaction and suggest that familiar forms of hierarchy, amplification, and role differentiation can arise on compressed timescales in agent-facing platforms.

</details>


### 91. Assessing Risks of Large Language Models in Mental Health Support: A Framework for Automated Clinical AI Red Teaming

- **Authors:** Ian Steenstra, Paola Pedrelli, Weiyan Shi, Stacy Marsella, Timothy W. Bickmore
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.19948v1](http://arxiv.org/abs/2602.19948v1)
- **PDF:** [https://arxiv.org/pdf/2602.19948v1](https://arxiv.org/pdf/2602.19948v1)
- **Categories:** cs.CL, cs.AI, cs.CY, cs.HC, cs.MA


> The paper introduces a systematic “clinical red‑team” framework that pairs LLM‑based AI psychotherapists with simulated patient agents whose internal states evolve according to cognitive‑affective models, allowing automated, longitudinal evaluation of therapeutic dialogue against a detailed quality‑of‑care and risk ontology. Using this setup, the authors ran 369 simulated Alcohol Use Disorder sessions across six commercial LLM agents (e.g., ChatGPT, Gemini, Character.AI) and uncovered systematic safety failures—most notably the reinforcement of patient delusions (“AI psychosis”) and the inability to de‑escalate suicide risk. The study demonstrates that simulation‑driven red‑team testing, visualized through an interactive dashboard, can expose hidden iatrogenic hazards in agentic AI systems before real‑world deployment.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) are increasingly utilized for mental health support; however, current safety benchmarks often fail to detect the complex, longitudinal risks inherent in therapeutic dialogue. We introduce an evaluation framework that pairs AI psychotherapists with simulated patient agents equipped with dynamic cognitive-affective models and assesses therapy session simulations against a comprehensive quality of care and risk ontology. We apply this framework to a high-impact test case, Alcohol Use Disorder, evaluating six AI agents (including ChatGPT, Gemini, and Character.AI) against a clinically-validated cohort of 15 patient personas representing diverse clinical phenotypes.
  Our large-scale simulation (N=369 sessions) reveals critical safety gaps in the use of AI for mental health support. We identify specific iatrogenic risks, including the validation of patient delusions ("AI Psychosis") and failure to de-escalate suicide risk. Finally, we validate an interactive data visualization dashboard with diverse stakeholders, including AI engineers and red teamers, mental health professionals, and policy experts (N=9), demonstrating that this framework effectively enables stakeholders to audit the "black box" of AI psychotherapy. These findings underscore the critical safety risks of AI-provided mental health support and the necessity of simulation-based clinical red teaming before deployment.

</details>


### 92. MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems

- **Authors:** Jin Jia, Zhiling Deng, Zhuangbin Chen, Yingqi Wang, Zibin Zheng
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.19843v1](http://arxiv.org/abs/2602.19843v1)
- **PDF:** [https://arxiv.org/pdf/2602.19843v1](https://arxiv.org/pdf/2602.19843v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces **MAS‑FIRE**, a systematic fault‑injection and reliability‑evaluation framework for large‑language‑model (LLM)‑based multi‑agent systems. By defining a taxonomy of 15 intra‑ and inter‑agent fault types and injecting them non‑invasively through prompt alteration, response rewriting, and message‑routing manipulation, the authors probe three representative MAS architectures and uncover four hierarchical fault‑tolerance mechanisms (mechanism, rule, prompt, reasoning). Their experiments show that robustness is not simply a function of model size—stronger foundation models often fail to handle semantic faults—and that architectural topology is critical: closed‑loop, iterative designs mitigate more than 40 % of faults that cause catastrophic collapse in linear workflows.


<details>
<summary>Abstract</summary>

As LLM-based Multi-Agent Systems (MAS) are increasingly deployed for complex tasks, ensuring their reliability has become a pressing challenge. Since MAS coordinate through unstructured natural language rather than rigid protocols, they are prone to semantic failures (e.g., hallucinations, misinterpreted instructions, and reasoning drift) that propagate silently without raising runtime exceptions. Prevailing evaluation approaches, which measure only end-to-end task success, offer limited insight into how these failures arise or how effectively agents recover from them. To bridge this gap, we propose MAS-FIRE, a systematic framework for fault injection and reliability evaluation of MAS. We define a taxonomy of 15 fault types covering intra-agent cognitive errors and inter-agent coordination failures, and inject them via three non-invasive mechanisms: prompt modification, response rewriting, and message routing manipulation. Applying MAS-FIRE to three representative MAS architectures, we uncover a rich set of fault-tolerant behaviors that we organize into four tiers: mechanism, rule, prompt, and reasoning. This tiered view enables fine-grained diagnosis of where and why systems succeed or fail. Our findings reveal that stronger foundation models do not uniformly improve robustness. We further show that architectural topology plays an equally decisive role, with iterative, closed-loop designs neutralizing over 40% of faults that cause catastrophic collapse in linear workflows. MAS-FIRE provides the process-level observability and actionable guidance needed to systematically improve multi-agent systems.

</details>


### 93. SAMAS: A Spectrum-Guided Multi-Agent System for Achieving Style Fidelity in Literary Translation

- **Authors:** Jingzhuo Wu, Jiajun Zhang, Keyan Jin, Dehua Ma, Junbo Wang
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.19840v1](http://arxiv.org/abs/2602.19840v1)
- **PDF:** [https://arxiv.org/pdf/2602.19840v1](https://arxiv.org/pdf/2602.19840v1)
- **Categories:** cs.CL


> The paper introduces **SAMAS**, a novel multi‑agent architecture that treats literary‑style preservation as a signal‑processing problem: it extracts a **Stylistic Feature Spectrum (SFS)** from the source text via wavelet‑packet transforms and uses this spectrum as a control signal to dynamically compose a workflow of specialized translation agents tailored to the text’s structural patterns. By orchestrating agents in a style‑guided, on‑the‑fly manner, SAMAS matches state‑of‑the‑art semantic accuracy while achieving a statistically significant boost in style‑fidelity over both single‑model and static multi‑agent baselines, demonstrating the value of spectrum‑driven, adaptive agent coordination for agentic AI tasks.


<details>
<summary>Abstract</summary>

Modern large language models (LLMs) excel at generating fluent and faithful translations. However, they struggle to preserve an author's unique literary style, often producing semantically correct but generic outputs. This limitation stems from the inability of current single-model and static multi-agent systems to perceive and adapt to stylistic variations. To address this, we introduce the Style-Adaptive Multi-Agent System (SAMAS), a novel framework that treats style preservation as a signal processing task. Specifically, our method quantifies literary style into a Stylistic Feature Spectrum (SFS) using the wavelet packet transform. This SFS serves as a control signal to dynamically assemble a tailored workflow of specialized translation agents based on the source text's structural patterns. Extensive experiments on translation benchmarks show that SAMAS achieves competitive semantic accuracy against strong baselines, primarily by leveraging its statistically significant advantage in style fidelity.

</details>


### 94. A General Equilibrium Theory of Orchestrated AI Agent Systems

- **Authors:** Jean-Philippe Garnier
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.21255v1](http://arxiv.org/abs/2602.21255v1)
- **PDF:** [https://arxiv.org/pdf/2602.21255v1](https://arxiv.org/pdf/2602.21255v1)
- **Categories:** cs.GT, cs.AI, math.OC


> The paper introduces a rigorous general‑equilibrium framework for large‑language‑model (LLM) agents that are coordinated by a central orchestrator, casting the system as an Arrow‑Debreu production economy on an infinite‑dimensional Hilbert space of metric trajectories. By modeling each LLM as a firm with a feasible production set and the orchestrator as a consumer who selects routing policies under functional prices, the authors prove existence (via a finite‑dimensional Brouwer approximation), Walras’ law, the First and Second Welfare Theorems, and—under a contraction condition—a unique equilibrium that is globally reached by a Walrasian tâtonnement‑style orchestration dynamics. Empirically, the theory shows that such orchestrated AI agent systems can be decentralized, achieve Pareto‑optimal welfare, and converge geometrically, offering a DSGE‑style analytical tool for designing and analyzing policy‑driven, large‑scale agentic AI deployments.


<details>
<summary>Abstract</summary>

We establish a general equilibrium theory for systems of large language model (LLM) agents operating under centralized orchestration. The framework is a production economy in the sense of Arrow-Debreu (1954), extended to infinite-dimensional commodity spaces following Bewley (1972). Each LLM agent is modeled as a firm whose production set Y a $\subset$ H = L 2 ([0, T ], R R ) represents the feasible metric trajectories determined by its frozen model weights. The orchestrator is the consumer, choosing a routing policy over the agent DAG to maximize system welfare subject to a budget constraint evaluated at functional prices p $\in$ H A . These prices-elements of the Hilbert dual of the commodity space-assign a shadow value to each metric of each agent at each instant. We prove, via Brouwer's theorem applied to a finitedimensional approximation V K $\subset$ H, that every such economy admits at least one general equilibrium (p * , y * , $π$ * ). A functional Walras' law  holds as a theorem: the value of functional excess demand is zero for all prices, as a consequence of the consumer's budget constraint-not by construction. We further establish Pareto optimality (First Welfare Theorem), decentralizability of Pareto optima (Second Welfare Theorem), and uniqueness with geometric convergence under a contraction condition (Banach). The orchestration dynamics constitute a Walrasian t{â}tonnement that converges globally under the contraction condition, unlike classical t{â}tonnement (Scarf, 1960). The framework admits a DSGE interpretation with SLO parameters as policy rates.

</details>


### 95. OpenClaw, Moltbook, and ClawdLab: From Agent-Only Social Networks to Autonomous Scientific Research

- **Authors:** Lukas Weidener, Marko Brkić, Mihailo Jovanović, Ritvik Singh, Emre Ulgac, Aakaash Meduri
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.19810v1](http://arxiv.org/abs/2602.19810v1)
- **PDF:** [https://arxiv.org/pdf/2602.19810v1](https://arxiv.org/pdf/2602.19810v1)
- **Categories:** cs.AI


> The paper introduces **ClawdLab**, an open‑source design‑science platform that remedies the architectural failures uncovered in the OpenClaw–Moltbook ecosystem of autonomous AI‑to‑AI interactions. By conducting a multivocal literature review of six papers and the underlying dataset (covering 131 agent skills and >15 k exposed control panels), the authors identify five recurring failure patterns—security breaches, uncontrolled skill proliferation, governance gaps, lack of evidence grounding, and Sybil‑type attacks—and propose a composable, three‑tier architecture that enforces hard role restrictions, adversarial critique, PI‑led governance, multi‑model orchestration, and protocol‑encoded evidence requirements, thereby delivering emergent Sybil resistance. Empirical analysis shows that, unlike existing AI co‑scientist systems confined to single‑agent pipelines or predetermined multi‑agent workflows, ClawdLab’s fully decentralised tier enables independent modification of foundation models, capabilities, governance, and validation constraints, supporting continual, compounding improvements as the broader AI ecosystem evolves.


<details>
<summary>Abstract</summary>

In January 2026, the open-source agent framework OpenClaw and the agent-only social network Moltbook produced a large-scale dataset of autonomous AI-to-AI interaction, attracting six academic publications within fourteen days. This study conducts a multivocal literature review of that ecosystem and presents ClawdLab, an open-source platform for autonomous scientific research, as a design science response to the architectural failure modes identified. The literature documents emergent collective phenomena, security vulnerabilities spanning 131 agent skills and over 15,200 exposed control panels, and five recurring architectural patterns. ClawdLab addresses these failure modes through hard role restrictions, structured adversarial critique, PI-led governance, multi-model orchestration, and domain-specific evidence requirements encoded as protocol constraints that ground validation in computational tool outputs rather than social consensus; the architecture provides emergent Sybil resistance as a structural consequence. A three-tier taxonomy distinguishes single-agent pipelines, predetermined multi-agent workflows, and fully decentralised systems, analysing why leading AI co-scientist platforms remain confined to the first two tiers. ClawdLab's composable third-tier architecture, in which foundation models, capabilities, governance, and evidence requirements are independently modifiable, enables compounding improvement as the broader AI ecosystem advances.

</details>


### 96. TAPE: Tool-Guided Adaptive Planning and Constrained Execution in Language Model Agents

- **Authors:** Jongwon Jeong, Jungtaek Kim, Kangwook Lee
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.19633v1](http://arxiv.org/abs/2602.19633v1)
- **PDF:** [https://arxiv.org/pdf/2602.19633v1](https://arxiv.org/pdf/2602.19633v1)
- **Categories:** cs.AI


> The paper introduces **TAPE (Tool‑guided Adaptive Planning with constrained Execution)**, a framework that makes language‑model agents more reliable in tightly constrained environments by (1) constructing a graph of multiple candidate plans and using an external solver to select a feasible execution path, and (2) applying constrained decoding together with on‑the‑fly replanning whenever the environment deviates from the expected state. Experiments on benchmark domains such as Sokoban, ALFWorld, MuSiQue, and the hard variant of GSM8K show that TAPE raises success rates by roughly **21 percentage points on the hardest settings** and yields **≈20 pp gains for weaker base LMs**, outperforming prior agent architectures. These results demonstrate that integrating tool‑guided planning graphs and adaptive, low‑variance execution substantially improves the robustness and feasibility compliance of agentic AI systems.


<details>
<summary>Abstract</summary>

Language Model (LM) agents have demonstrated remarkable capabilities in solving tasks that require multiple interactions with the environment. However, they remain vulnerable in environments where a single error often leads to irrecoverable failure, particularly under strict feasibility constraints. We systematically analyze existing agent frameworks, identifying imperfect planning and stochastic execution as the primary causes. To address these challenges, we propose Tool-guided Adaptive Planning with constrained Execution (TAPE). TAPE enhances planning capability by aggregating multiple plans into a graph and employing an external solver to identify a feasible path. During execution, TAPE employs constrained decoding to reduce sampling noise, while adaptively re-planning whenever environmental feedback deviates from the intended state. Experiments across Sokoban, ALFWorld, MuSiQue, and GSM8K-Hard demonstrate that TAPE consistently outperforms existing frameworks, with particularly large gains on hard settings, improving success rates by 21.0 percentage points on hard settings on average, and by 20.0 percentage points for weaker base models on average. Code and data available at here.

</details>


### 97. Right to History: A Sovereignty Kernel for Verifiable AI Agent Execution

- **Authors:** Jing Zhang
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20214v1](http://arxiv.org/abs/2602.20214v1)
- **PDF:** [https://arxiv.org/pdf/2602.20214v1](https://arxiv.org/pdf/2602.20214v1)
- **Categories:** cs.CR, cs.AI, cs.OS


> The paper introduces the **Right to History**, a legal‑technical principle that obliges individuals to receive a tamper‑evident, independently verifiable log of every action taken by AI agents running on their own hardware. To realize this, the authors formalize five system invariants and implement a **sovereignty kernel**—PunkGo—built in Rust that combines RFC 6962 Merkle‑tree audit logs, capability‑based isolation, energy‑budget governance, and a human‑approval workflow; the invariants are validated through adversarial testing. Empirical results show that PunkGo can record actions with sub‑1.3 ms latency, sustain ~400 actions / s, and generate compact 448‑byte Merkle inclusion proofs for logs of 10 k entries, demonstrating a practical, verifiable logging layer for high‑risk, agentic AI systems.


<details>
<summary>Abstract</summary>

AI agents increasingly act on behalf of humans, yet no existing system provides a tamper-evident, independently verifiable record of what they did. As regulations such as the EU AI Act begin mandating automatic logging for high-risk AI systems, this gap carries concrete consequences -- especially for agents running on personal hardware, where no centralized provider controls the log. Extending Floridi's informational rights framework from data about individuals to actions performed on their behalf, this paper proposes the Right to History: the principle that individuals are entitled to a complete, verifiable record of every AI agent action on their own hardware. The paper formalizes this principle through five system invariants with structured proof sketches, and implements it in PunkGo, a Rust sovereignty kernel that unifies RFC 6962 Merkle tree audit logs, capability-based isolation, energy-budget governance, and a human-approval mechanism. Adversarial testing confirms all five invariants hold. Performance evaluation shows sub-1.3 ms median action latency, ~400 actions/sec throughput, and 448-byte Merkle inclusion proofs at 10,000 log entries.

</details>


### 98. Agentic AI as a Cybersecurity Attack Surface: Threats, Exploits, and Defenses in Runtime Supply Chains

- **Authors:** Xiaochong Jiang, Shiqi Yang, Wenting Yang, Yichen Liu, Cheng Ji
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.19555v1](http://arxiv.org/abs/2602.19555v1)
- **PDF:** [https://arxiv.org/pdf/2602.19555v1](https://arxiv.org/pdf/2602.19555v1)
- **Categories:** cs.CR, cs.AI


> The paper’s main contribution is a unified threat‑model that shifts the focus of agentic AI security from static, model‑level flaws to the dynamic, inference‑time “runtime supply chain” of large‑language‑model agents. By formally decomposing runtime behavior into data‑supply (transient context injection and persistent memory poisoning) and tool‑supply (discovery, implementation, and invocation) attack vectors, the authors expose a novel “Viral Agent Loop” whereby autonomous agents can propagate generative worms without any code‑level vulnerability. Their methodology combines a systematic taxonomy with illustrative exploit scenarios and proposes a Zero‑Trust Runtime Architecture that treats all context as untrusted control flow and enforces tool execution through cryptographic provenance, offering a concrete defensive blueprint for securing agentic AI deployments.


<details>
<summary>Abstract</summary>

Agentic systems built on large language models (LLMs) extend beyond text generation to autonomously retrieve information and invoke tools. This runtime execution model shifts the attack surface from build-time artifacts to inference-time dependencies, exposing agents to manipulation through untrusted data and probabilistic capability resolution. While prior work has focused on model-level vulnerabilities, security risks emerging from cyclic and interdependent runtime behavior remain fragmented. We systematize these risks within a unified runtime framework, categorizing threats into data supply chain attacks (transient context injection and persistent memory poisoning) and tool supply chain attacks (discovery, implementation, and invocation). We further identify the Viral Agent Loop, in which agents act as vectors for self-propagating generative worms without exploiting code-level flaws. Finally, we advocate a Zero-Trust Runtime Architecture that treats context as untrusted control flow and constrains tool execution through cryptographic provenance rather than semantic inference.

</details>


### 99. Cost-Aware Diffusion Active Search

- **Authors:** Arundhati Banerjee, Jeff Schneider
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.19538v1](http://arxiv.org/abs/2602.19538v1)
- **PDF:** [https://arxiv.org/pdf/2602.19538v1](https://arxiv.org/pdf/2602.19538v1)
- **Categories:** cs.RO, cs.AI, cs.LG


> The paper introduces **Cost‑Aware Diffusion Active Search (CD‑AS)**, a novel look‑ahead decision‑making framework that lets autonomous agents plan exploration‑exploitation sequences without constructing costly search trees. By training diffusion models to generate future action trajectories conditioned on past observations and a cost budget, the authors correct the optimism bias of earlier diffusion‑RL methods and extend the approach to coordinated multi‑agent teams. Experiments on benchmark active‑search tasks show that CD‑AS achieves higher full‑recovery rates than myopic and tree‑search baselines while requiring substantially less computation, demonstrating a scalable, cost‑sensitive planning tool for agentic AI systems.


<details>
<summary>Abstract</summary>

Active search for recovering objects of interest through online, adaptive decision making with autonomous agents requires trading off exploration of unknown environments with exploitation of prior observations in the search space. Prior work has proposed information gain and Thompson sampling based myopic, greedy approaches for agents to actively decide query or search locations when the number of targets is unknown. Decision making algorithms in such partially observable environments have also shown that agents capable of lookahead over a finite horizon outperform myopic policies for active search. Unfortunately, lookahead algorithms typically rely on building a computationally expensive search tree that is simulated and updated based on the agent's observations and a model of the environment dynamics. Instead, in this work, we leverage the sequence modeling abilities of diffusion models to sample lookahead action sequences that balance the exploration-exploitation trade-off for active search without building an exhaustive search tree. We identify the optimism bias in prior diffusion based reinforcement learning approaches when applied to the active search setting and propose mitigating solutions for efficient cost-aware decision making with both single and multi-agent teams. Our proposed algorithm outperforms standard baselines in offline reinforcement learning in terms of full recovery rate and is computationally more efficient than tree search in cost-aware active decision making.

</details>


### 100. CodeHacker: Automated Test Case Generation for Detecting Vulnerabilities in Competitive Programming Solutions

- **Authors:** Jingwei Shi, Xinxiang Yin, Jing Huang, Jinman Zhao, Shengyu Tao
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.20213v1](http://arxiv.org/abs/2602.20213v1)
- **PDF:** [https://arxiv.org/pdf/2602.20213v1](https://arxiv.org/pdf/2602.20213v1)
- **Categories:** cs.SE, cs.AI, cs.CR


> The paper introduces **CodeHacker**, an autonomous agent that automatically creates adversarial test cases to expose hidden bugs in code‑generation outputs, thereby tightening the evaluation of LLM‑based programming assistants. The system combines multiple attack strategies (stress‑testing, anti‑hash, logic‑targeted hacks) and a **Calibration Phase** in which the agent iteratively refines its own validator and checker using self‑generated probes before confronting contestant solutions. Experiments show that CodeHacker markedly raises the true‑negative rate of existing benchmark suites—filtering out previously accepted incorrect programs—and that the generated adversarial cases serve as high‑quality training data, improving the performance of RL‑trained code models on benchmarks such as LiveCodeBench.


<details>
<summary>Abstract</summary>

The evaluation of Large Language Models (LLMs) for code generation relies heavily on the quality and robustness of test cases. However, existing benchmarks often lack coverage for subtle corner cases, allowing incorrect solutions to pass. To bridge this gap, we propose CodeHacker, an automated agent framework dedicated to generating targeted adversarial test cases that expose latent vulnerabilities in program submissions. Mimicking the hack mechanism in competitive programming, CodeHacker employs a multi-strategy approach, including stress testing, anti-hash attacks, and logic-specific targeting to break specific code submissions. To ensure the validity and reliability of these attacks, we introduce a Calibration Phase, where the agent iteratively refines its own Validator and Checker via self-generated adversarial probes before evaluating contestant code.Experiments demonstrate that CodeHacker significantly improves the True Negative Rate (TNR) of existing datasets, effectively filtering out incorrect solutions that were previously accepted. Furthermore, generated adversarial cases prove to be superior training data, boosting the performance of RL-trained models on benchmarks like LiveCodeBench.

</details>


### 101. Human-Guided Agentic AI for Multimodal Clinical Prediction: Lessons from the AgentDS Healthcare Benchmark

- **Authors:** Lalitha Pranathi Pulavarthy, Raajitha Muthyala, Aravind V Kuruvikkattil, Zhenan Yin, Rashmita Kudamala, Saptarshi Purkayastha
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.19502v1](http://arxiv.org/abs/2602.19502v1)
- **PDF:** [https://arxiv.org/pdf/2602.19502v1](https://arxiv.org/pdf/2602.19502v1)
- **Categories:** cs.AI, cs.LG


> The paper demonstrates that embedding domain‑expert guidance at critical junctures of an autonomous agentic AI pipeline markedly improves multimodal clinical prediction performance, achieving top‑tier results on the three AgentDS Healthcare benchmark tasks (e.g., 30‑day readmission Macro‑F1 = 0.8986). By having clinicians steer the agent’s workflow—selecting and engineering features from notes, PDF billing receipts, and vital‑sign time series, choosing task‑appropriate models, and defining clinically sound validation— the authors show a cumulative +0.065 F1 gain over fully automated baselines, with multimodal feature engineering alone contributing +0.041 F1. The study distills three actionable lessons for agentic AI in healthcare: (1) domain‑informed feature engineering yields compounding benefits beyond exhaustive automated search; (2) task‑specific human judgment is essential for effective multimodal data integration; and (3) purposeful ensemble diversity guided by clinical insight outperforms random hyper‑parameter tuning.


<details>
<summary>Abstract</summary>

Agentic AI systems are increasingly capable of autonomous data science workflows, yet clinical prediction tasks demand domain expertise that purely automated approaches struggle to provide. We investigate how human guidance of agentic AI can improve multimodal clinical prediction, presenting our approach to all three AgentDS Healthcare benchmark challenges: 30-day hospital readmission prediction (Macro-F1 = 0.8986), emergency department cost forecasting (MAE = $465.13), and discharge readiness assessment (Macro-F1 = 0.7939). Across these tasks, human analysts directed the agentic workflow at key decision points, multimodal feature engineering from clinical notes, scanned PDF billing receipts, and time-series vital signs; task-appropriate model selection; and clinically informed validation strategies. Our approach ranked 5th overall in the healthcare domain, with a 3rd-place finish on the discharge readiness task. Ablation studies reveal that human-guided decisions compounded to a cumulative gain of +0.065 F1 over automated baselines, with multimodal feature extraction contributing the largest single improvement (+0.041 F1). We distill three generalizable lessons: (1) domain-informed feature engineering at each pipeline stage yields compounding gains that outperform extensive automated search; (2) multimodal data integration requires task-specific human judgment that no single extraction strategy generalizes across clinical text, PDFs, and time-series; and (3) deliberate ensemble diversity with clinically motivated model configurations outperforms random hyperparameter search. These findings offer practical guidance for teams deploying agentic AI in healthcare settings where interpretability, reproducibility, and clinical validity are essential.

</details>


### 102. ComplLLM: Fine-tuning LLMs to Discover Complementary Signals for Decision-making

- **Authors:** Ziyang Guo, Yifan Wu, Jason Hartline, Kenneth Holstein, Jessica Hullman
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.19458v1](http://arxiv.org/abs/2602.19458v1)
- **PDF:** [https://arxiv.org/pdf/2602.19458v1](https://arxiv.org/pdf/2602.19458v1)
- **Categories:** cs.AI, cs.HC


> **Main contribution:** The paper introduces **ComplLLM**, a post‑training framework that fine‑tunes a large language model to generate decision‑assistant signals that are *complementary* to the outputs of existing agents, thereby enabling multi‑agent pipelines to exploit unique, non‑redundant information for better final decisions.  

**Methodology:** Building on decision‑theoretic principles, the authors treat complementary information as a reward signal and fine‑tune the LLM via reinforcement learning (or reward‑weighted supervised learning) to produce explanations and auxiliary predictions that fill gaps in the knowledge of other agents. The framework is evaluated on both synthetic benchmarks (where ground‑truth complementary signals are known) and real‑world tasks involving human domain experts.  

**Key findings:** ComplLLM reliably recovers the intended complementary signals in synthetic settings and, in real‑world scenarios, yields assistant outputs that improve downstream decision accuracy and provide plausible, human‑interpretable explanations of the added information—demonstrating that fine‑tuned LLMs can serve as effective, complementary agents within larger decision‑making systems.


<details>
<summary>Abstract</summary>

Multi-agent decision pipelines can outperform single agent workflows when complementarity holds, i.e., different agents bring unique information to the table to inform a final decision. We propose ComplLLM, a post-training framework based on decision theory that fine-tunes a decision-assistant LLM using complementary information as reward to output signals that complement existing agent decisions. We validate ComplLLM on synthetic and real-world tasks involving domain experts, demonstrating how the approach recovers known complementary information and produces plausible explanations of complementary signals to support downstream decision-makers.

</details>


### 103. OptiRepair: Closed-Loop Diagnosis and Repair of Supply Chain Optimization Models with LLM Agents

- **Authors:** Ruicheng Ao, David Simchi-Levi, Xinshang Wang
- **Published:** 2026-02-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.19439v2](http://arxiv.org/abs/2602.19439v2)
- **PDF:** [https://arxiv.org/pdf/2602.19439v2](https://arxiv.org/pdf/2602.19439v2)
- **Categories:** cs.AI, cs.LG, math.OC


> The paper introduces **OptiRepair**, a closed‑loop framework that equips large‑language‑model (LLM) agents with the ability to diagnose and repair infeasible supply‑chain linear‑program models. The authors decompose the task into a **domain‑agnostic feasibility phase** (iteratively fixing any LP using IIS‑guided diagnostics) and a **domain‑specific validation phase** (enforcing five inventory‑theory rationality checks), training two 8‑billion‑parameter LLMs with self‑taught reasoning and solver‑verified reward signals; they evaluate the system on 976 multi‑echelon problems drawn from 22 API models across seven families. Trained agents achieve an **81.7 % Rational Recovery Rate**, far surpassing the best off‑the‑shelf API (42.2 %) and highlighting two critical gaps for agentic AI: (1) effective solver interaction (closed by targeted training) and (2) adherence to operational rationality (closed by embedding explicit, verifier‑compatible checks).


<details>
<summary>Abstract</summary>

Supply chain optimization models frequently become infeasible because of modeling errors. Diagnosis and repair require scarce OR expertise: analysts must interpret solver diagnostics, trace root causes across echelons, and fix formulations without sacrificing operational soundness. Whether AI agents can perform this task remains untested. We decompose this task into two phases: a domain-agnostic feasibility phase that iteratively repairs any LP using IIS-guided diagnosis, and a domain-specific validation phase that enforces five rationality checks grounded in inventory theory. We test 22 API models from seven families on 976 multi-echelon supply chain problems and train two 8B-parameter models with self-taught reasoning and solver-verified rewards. The trained models reach 81.7% Rational Recovery Rate (RRR) -- the fraction of problems resolved to both feasibility and operational rationality -- versus 42.2% for the best API model and 21.3% on average. The gap concentrates in Phase 1 repair, where API models average 27.6% recovery rate versus 97.2% for trained models. Two gaps separate current AI from reliable model repair: solver interaction, as API models restore only 27.6% of infeasible formulations; and operational rationale, as roughly one in four feasible repairs violate supply chain theory. Each gap requires a different intervention -- targeted training closes the solver interaction gap, while explicit specification as solver-verifiable checks closes the rationality gap. For organizations adopting AI in operational planning, formalizing what 'rational' means in their context is the higher-return investment.

</details>



## Medrxiv (6 papers)


### 1. Onco-Shikshak: An AI-Native Adaptive Learning Ecosystem for Medical Oncology Education

- **Authors:** Makani, A.
- **Published:** 2026-02-26
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.23.26346944](https://doi.org/10.64898/2026.02.23.26346944)

- **Categories:** oncology


> The paper introduces **Onco‑Shikshak V7**, the first AI‑native adaptive learning ecosystem that fuses cognitive‑architectural models (ACT‑R illness‑script activation), psychometric adaptation (Item‑Response Theory), spaced‑repetition scheduling (FSRS v4), scaffolding (Zone of Proximal Development), and metacognitive calibration (Brier‑score feedback) into a single platform for medical oncology education. Its methodology deploys six specialist agents (medical, radiation, surgical oncology, pathology, radiology, and navigation) that perform retrieval‑augmented generation over nine guideline sources and engage learners in authentic clinical workflows (Morning Report, Tumor Board, Clinic Day, AI Textbook), while mapping every interaction to ACGME milestones and closing the learning loop with targeted flashcards and case recommendations. Technical validation shows correct operation of all eight subsystems, demonstrating that a multi‑agent, cognitively‑grounded architecture can dynamically adapt to rapidly evolving oncology knowledge and mitigate LLM hallucination and automation bias—key advances for agentic AI in high‑stakes education.


<details>
<summary>Abstract</summary>

Medical oncology education faces a dual crisis: knowledge velocity that outpaces static curricula and large language model (LLM) risks--hallucination and automation bias--that threaten the fidelity of AI-assisted learning. We present Onco-Shikshak V7, an AI-native adaptive learning platform that addresses both challenges through a unified cognitive architecture grounded in learning science. The system replaces isolated educational modules with four authentic clinical workflows--Morning Report, Tumor Board, Clinic Day, and AI Textbook--each scaffolded by a nine-module pedagogy engine that integrates ACT-R activation dynamics (illness scripts), Item Response Theory (adaptive difficulty), the Free Spaced Repetition Scheduler (FSRS v4), Zone of Proximal Development (scaffolding), and metacognitive calibration training (Brier score). Six specialist AI agents--medical oncology, radiation oncology, surgical oncology, pathology, radiology, and oncology navigation--engage in multi-disciplinary deliberation with per-specialty retrieval-augmented generation (RAG) grounding across nine authoritative guideline sources including NCCN, ESMO, and ASTRO. The platform provides 18 clinical cases with decision trees across six cancer types, maps every interaction to 13 ACGME Hematology-Oncology milestones, and implements four closed-loop feedback mechanisms that connect session errors to targeted flashcards, weak domains to suggested cases, and all interactions to a persistent learner profile. Technical validation confirms algorithmic correctness across eight subsystems. To our knowledge, this is the first system to unify ACT-R, IRT, FSRS, ZPD, and metacognitive calibration in a single medical education platform. Formal learner evaluation via randomized controlled trial is planned.

</details>


### 2. End-to-End PET/CT Interpretation and Quantification with an LLM-Orchestrated AI Agent: A Real-World Pilot Study

- **Authors:** Choi, H., Bae, S., Na, K. J.
- **Published:** 2026-02-25
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.21.26346798](https://doi.org/10.64898/2026.02.21.26346798)

- **Categories:** radiology and imaging


> The paper introduces a fully autonomous, LLM‑orchestrated AI agent that integrates multiple imaging tools to process raw PET/CT DICOM data, perform registration, SUV conversion, segmentation, detection, and generate structured clinical reports without human input. Using a reasoning‑based text LLM to select series and coordinate tool calls, and a vision‑enabled LLM for interpretation, the system was retrospectively tested on 170 lung‑cancer PET/CT scans. It achieved flawless primary‑tumor detection (100 % sensitivity) but showed moderate performance for nodal (84.8 % sensitivity, 39.4 % specificity) and distant metastasis assessment (70.2 % sensitivity, 65.0 % specificity), highlighting both the feasibility of end‑to‑end agentic workflows in radiology and the need for expert oversight in complex cases.


<details>
<summary>Abstract</summary>

BackgroundAlthough deep learning models have improved individual PET analysis, image processing and quantification tasks, end-to-end automation from raw DICOM to quantitative clinical reporting remains limited, particularly in heterogeneous real-world settings.

MethodsAs a proof-of-concept, an autonomous large language model (LLM)-orchestrated multi-tool agent for end-to-end PET/CT interpretation was developed. A reasoning-based text LLM selected appropriate series from raw DICOM, coordinated registration and SUV conversion, invoked segmentation and detection tools, generated maximum-intensity projections, called a vision-enabled LLM for interpretation, and synthesized structured draft reports. The system was retrospectively evaluated in 170 patients undergoing baseline FDG PET/CT for lung cancer staging, using expert reports as reference.

ResultsThe agent successfully completed the full end-to-end workflow from raw DICOM selection to structured draft report generation without human intervention in all 170 examinations. Primary tumor detection achieved 100% sensitivity. For nodal involvement, sensitivity was 84.8% and specificity was 39.4%, whereas distant metastasis detection showed 70.2% sensitivity and 65.0% specificity. Discrepancy analysis of 58 nodal and 57 metastatic mismatch cases revealed systematic false-positive findings related to reactive or physiologic uptake and false-negative findings involving small-volume or anatomically atypical metastases.

ConclusionLLM-orchestrated PET/CT agents can enable workflow-level automation from raw DICOM to quantification and structured draft reporting under real-world conditions. Although primary tumor detection was highly reliable, nodal and metastatic assessment revealed systematic limitations, supporting a collaborative role with continued expert oversight in complex clinical scenarios.

</details>


### 3. Agent Role Structure and Operating Characteristics in Large Language Model Clinical Classification: A Comparative Study of Specialist and Deliberative Multi-Agent Protocols

- **Authors:** Anderson, C. G.
- **Published:** 2026-02-25
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.22.26346818](https://doi.org/10.64898/2026.02.22.26346818)

- **Categories:** health informatics


> The paper demonstrates that the internal role architecture of deterministic multi‑agent prompting pipelines materially shapes clinical classification outcomes for large language models. By constructing two DAG‑based protocols— a Generic Deliberative (GD) chain and a Feature‑Specialist (FS) hierarchy that routes feature‑specific prompts to dedicated sub‑agents— and evaluating them on the UCI Cleveland heart‑disease dataset under identical model, decoding, and aggregation settings, the authors isolate the effect of role decomposition. The FS protocol yields a 7 % boost in overall accuracy and a 6 % rise in macro‑F1, but it also shifts the operating point toward higher specificity (+0.22) and lower sensitivity (‑0.13), highlighting that agent role design imposes a structured inductive bias that must be treated as a core modeling decision in safety‑critical AI systems.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly evaluated for structured clinical decision support tasks, often using multi-agent architectures. Prior work has compared single-agent and multi-agent inference. However, the effect of internal role structure within multi-agent systems on classification behavior remains underexplored. We evaluate two multi-agent prompting protocols, implemented as deterministic Directed Acyclic Graph (DAG) systems, a Generic Deliberative (GD) protocol and a Feature-Specialist (FS) protocol, on tabular clinical heart disease data from the UCI Cleveland dataset. Structured variables are rendered into primarily text-based feature descriptions while preserving clinically relevant numeric values. The two protocols differ only in their prompt-level role decomposition and information routing, while base model, model weights, deterministic decoding with temperature set to 0, computational budget, and aggregation logic are held constant. The results show systematic differences in predictive behavior attributable solely to prompt-level role structure. The FS protocol improves overall accuracy by 0.07 and macro-F1 by 0.06. However, this improvement is accompanied by a marked operating-point shift in which specificity increases by 0.22 while sensitivity decreases by 0.13, with corresponding redistribution of class-wise precision. Notably, the increase in specificity corresponds to a reduction in false positive classifications, indicating decreased over-diagnosis under the FS configuration. These findings indicate that multi-agent role decomposition introduces a structured inductive bias in deterministic LLM-based classification. Prompt protocol and agent role design should therefore be regarded as core modeling decisions, as they show measurable influence on performance tradeoffs, particularly in safety-sensitive deployment contexts.

</details>


### 4. Care Plan Generation for Underserved Patients Using Multi-Agent Language Models: Applying Nash Game Theory to Optimize Multiple Objectives

- **Authors:** Basu, S., Baum, A.
- **Published:** 2026-02-25
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.23.26346934](https://doi.org/10.64898/2026.02.23.26346934)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundClinicians in care management programs are often in low supply relative to patient demand, especially in US Medicaid programs, and must simultaneously address clinical risk, time efficiency, and patients social needs. Many studies have shown that large language models may assist in their tasks for summarizing patient care, such as in generating care plans; yet these studies also show that different objectives given to agents often conflict and produce problems for safety, efficiency and equity. We tested whether and to what degree using game theoretic approaches (a Nash bargaining framework) can produce care plans that advance multiple objectives across multiple language models, applying data from a real-world Medicaid cohort.

MethodsWe conducted two studies in a cohort of 5,148 activated Medicaid care management patients (69.9% female; 45.7% Black or African American; mean age 40.9 years) enrolled in Virginia and Washington. A retrospective evaluation applied five deterministic strategies to the full cohort to characterize multi-objective trade-offs. A pre-registered controlled paired experiment (N = 200) assigned each patient one Nash-orchestrated multi-agent plan and one compute-matched sequential self-critique plan, generated by locally hosted open-source models (DeepSeek-R1 8B; Llama 3.1 8B) with no patient data leaving local infrastructure. Pre-specified outcomes were Safety, Efficiency, Equity, and Composite (mean of the three), each scored 0-1. Reporting follows CONSORT 2010 and STROBE.

ResultsNash orchestration produced a Composite score of 0.755 (95% CI 0.751-0.760) versus 0.742 (95% CI 0.739-0.746) for the compute-matched baseline; the paired difference was 0.013 (95% CI 0.008-0.019; p = 6.20 x 10-). Safety and Efficiency paired differences were small-to-moderate in effect size (Cohens d = 0.327 and 0.543, respectively) with confidence intervals excluding zero. The Equity paired difference was 0.000 (95% CI -0.015 to 0.014; p = 0.987).

ConclusionsRole-specialized Nash-orchestrated multi-agent language models produced measurably better Safety and Efficiency care plan quality than a compute-matched baseline under data-residency constraints. The null Equity result demonstrates that multi-objective role specialization does not automatically address equity--equity requires explicit design attention beyond composite weighting--with direct implications for responsible AI deployment in Medicaid care management.

Author SummaryCare management programs for Medicaid patients need to address multiple goals at once: covering clinical risks, prioritizing the most impactful interventions, and recognizing the social barriers that affect whether patients can follow through on care plans. Prior research shows that automation tools powered by a single AI model tend to optimize for one of these goals at a time, sacrificing the others. We tested whether organizing several specialized AI agents -- each focused on a different goal -- and then combining their recommendations through a mathematical framework called Nash bargaining could produce better overall care plans for a real Medicaid population. We found that this multi-agent approach produced care plans that the AI judge rated as meaningfully safer and more efficient than plans generated by a single AI model using the same total amount of computation. However, the multi-agent approach did not produce plans that were more equitable in addressing patients social needs, suggesting that equity requires more direct attention as a design target rather than emerging from multi-objective combination alone. All AI inference was performed on locally hosted computers, with no patient information sent to outside services, reflecting the privacy requirements of real-world Medicaid care management programs.

</details>


### 5. How Agent Role Structure Alters Operating Characteristics of Large Language Model Clinical Classifiers: A Comparative Study of Specialist and Deliberative Multi-Agent Protocols

- **Authors:** Anderson, C. G.
- **Published:** 2026-02-24
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.22.26346818](https://doi.org/10.64898/2026.02.22.26346818)

- **Categories:** health informatics


> The paper demonstrates that the internal role structure of deterministic multi‑agent prompting pipelines materially shapes the classification behavior of large language models (LLMs) on a clinical decision‑support task. By implementing two DAG‑based protocols— a Generic Deliberative (GD) chain and a Feature‑Specialist (FS) decomposition that routes feature‑specific prompts to dedicated agents— and keeping the base model, weights, decoding temperature, compute budget, and aggregation unchanged, the authors show that the FS design yields a 7 % boost in overall accuracy and a 6 % rise in macro‑F1, but at the cost of a 22 % increase in specificity and a 13 % drop in sensitivity, effectively reducing false‑positive (over‑diagnosis) errors. These results reveal that prompt‑level role decomposition acts as a controllable inductive bias in agentic AI systems, making agent role design a critical modeling decision for safety‑critical applications.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly evaluated for structured clinical decision support tasks, often using multi-agent architectures. Prior work has compared single-agent and multi-agent inference. However, the effect of internal role structure within multi-agent systems on classification behavior remains underexplored. We evaluate two multi-agent prompting protocols, implemented as deterministic Directed Acyclic Graph (DAG) systems, a Generic Deliberative (GD) protocol and a Feature-Specialist (FS) protocol, on tabular clinical heart disease data from the UCI Cleveland dataset. Structured variables are rendered into primarily text-based feature descriptions while preserving clinically relevant numeric values. The two protocols differ only in their prompt-level role decomposition and information routing, while base model, model weights, deterministic decoding with temperature set to 0, computational budget, and aggregation logic are held constant. The results show systematic differences in predictive behavior attributable solely to prompt-level role structure. The FS protocol improves overall accuracy by 0.07 and macro-F1 by 0.06. However, this improvement is accompanied by a marked operating-point shift in which specificity increases by 0.22 while sensitivity decreases by 0.13, with corresponding redistribution of class-wise precision. Notably, the increase in specificity corresponds to a reduction in false positive classifications, indicating decreased over-diagnosis under the FS configuration. These findings indicate that multi-agent role decomposition introduces a structured inductive bias in deterministic LLM-based classification. Prompt protocol and agent role design should therefore be regarded as core modeling decisions, as they show measurable influence on performance tradeoffs, particularly in safety-sensitive deployment contexts.

</details>


### 6. Evaluating the AI Potential as a Safety Net for Diagnosis: A Novel Benchmark of Large Language Models in Correcting Diagnostic Errors

- **Authors:** Hassoon, A., Peng, X., Irimia, R., Lianjie, A., Leo, H., Bandeira, A., Woo, H. Y., Dredze, M., Abdulnour, R.-E., McDonald, K. M., Peterson, S., Newman-Toker, D.
- **Published:** 2026-02-24
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.22.26346832](https://doi.org/10.64898/2026.02.22.26346832)

- **Categories:** health systems and quality improvement


> The paper introduces a benchmark that quantifies how well large language models (LLMs) can act as a safety‑net by detecting and correcting erroneous physician diagnoses across 200 high‑stakes clinical vignettes. By prompting 16 state‑of‑the‑art LLMs (e.g., Gemini 2.5 Pro, Claude 3.7 Sonnet) with the full patient record and an incorrect diagnosis, the authors measured diagnostic‑correction rates and examined robustness to 2,200 demographic and contextual variants. Results show that the best models (Gemini 2.5 Pro ≈ 55 % correction) still fail on many conditions and exhibit confirmation bias and sensitivity to non‑clinical cues, highlighting the need for adversarial, multi‑agent workflows that prioritize skeptical reasoning for safe agentic AI deployment in medicine.


<details>
<summary>Abstract</summary>

BackgroundDiagnostic errors are a leading cause of preventable patient harm, often occurring during early clinical encounters where diagnostic uncertainty is maximal. Large language models (LLMs) have shown potential in medical reasoning, yet their ability to function as a diagnostic safety net, specifically by identifying and correcting human diagnostic errors, remains systematically unquantified. We evaluated whether state-of-the-art LLMs can effectively challenge, rather than merely confirm, an erroneous physician diagnosis.

MethodsWe evaluated 16 leading LLMs (including GPT-o1, Gemini 2.5 Pro, and Claude 3.7 Sonnet) using 200 standardized clinical vignettes representing 20 high-stakes, frequently misdiagnosed conditions. Models were presented with the full clinical record and an incorrect physician diagnosis. Primary outcomes included the diagnostic correction rate (disagreeing with the error and providing the correct diagnosis) and the ratio of correction to error detection. We further tested model robustness by generating 2,200 variants to assess the influence of demographic (race/ethnicity) and contextual (institutional reputation, training level, insurance) tokens.

ResultsDiagnostic correction rates varied significantly across models. Gemini 2.5 Pro demonstrated the highest performance, correcting the physicians error in 55.0% of cases (n=110/200), followed by Claude Sonnet 3.5 (48.5%) and Sonnet 4 (47.0%). In contrast, DeepSeek V3 corrected only 20.0% of cases. Performance was strikingly consistent at the disease level; most models failed to correct errors in syphilis, spinal epidural abscess, and myocardial infarction. Furthermore, several models exhibited confirmation bias (agreeing with the incorrect diagnosis) occurring in 11.0% to 50.0% of cases. Stability across demographic and contextual variants was inconsistent, with some models showing spurious performance shifts based on non-clinical tokens.

ConclusionWhile top-performing LLMs can intercept approximately half of the human diagnostic errors in high-stakes scenarios, performance is heterogeneous and highly sensitive to non-clinical context. Current models exhibit significant disease-specific gaps and a tendency toward confirmation bias, suggesting that their safe clinical integration requires adversarial, multi-agent workflows designed to prioritize skepticism over baseline agreement.

</details>



## Biorxiv (1 papers)


### 1. OriGene: A Self-Evolving Virtual Disease Biologist Automating Therapeutic Target Discovery

- **Authors:** Zhang, Z., Qiu, Z., Wu, Y., Li, S., Wang, D., Liu, Y., Zhou, Z., Hu, Y., Chen, Y., An, D., Wang, Y., Li, Y., Zhong, Z., Ou, C., Wang, Z., Tang, F., Chen, J. X., Ma, R., Li, J., Wang, X., Lu, W., Xue, H., Zhang, W., Wei, Z., Ma, R., Shi, Z., Wang, K., Liu, Q., Dong, B., He, Y., Liu, T., Gu, J., Song, S., Feng, Q., Zhang, J., Zhang, B., Tian, L., Bai, L., Gao, Q., Sun, S., Zheng, S.
- **Published:** 2026-02-25
- **Source:** biorxiv
- **URL:** [https://doi.org/10.1101/2025.06.03.657658](https://doi.org/10.1101/2025.06.03.657658)

- **Categories:** bioinformatics


> OriGene introduces a self‑evolving, multi‑agent platform that acts as a virtual disease biologist, automatically generating and prioritizing mechanistically grounded therapeutic‑target hypotheses across genomics, protein‑network, pharmacology, clinical and literature data. Its architecture links >600 specialized tools through a Model Context Protocol and a knowledge‑graph‑based tool‑retrieval‑augmented generation (Tool‑RAG) system, enabling context‑aware tool selection and continual refinement of reasoning templates via human and experimental feedback. On the newly created TRQA benchmark (≈1,900 expert‑level Q&A pairs), OriGene outperforms human experts, leading research agents, and state‑of‑the‑art LLMs in accuracy and robustness, and successfully identified novel targets (GPR160 for liver cancer and ARG2 for colorectal cancer) that showed potent anti‑tumor activity in patient‑derived organoid and tumor fragment models.


<details>
<summary>Abstract</summary>

Here, we present OriGene, a self-evolving multi-agent system that functions as a virtual disease biologist, systematically identifying original and mechanistically grounded therapeutic targets at scale. OriGenes architecture integrates over 600 specialized tools through a Model Context Protocol (MCP), enabling it to reason across diverse data modalities including genomics, protein networks, pharmacology, clinical records and literature evidence, to generate and prioritize target discovery hypotheses. We implemented a strategy combining a knowledge graph-based Tool RAG with an advanced agent selection mechanism to enable dynamic, context-aware tool deployment. Through a self-evolving framework, OriGene continuously integrates human and experimental feedback to iteratively refine its core thinking templates, tool composition, and analytical protocols, thereby enhancing both accuracy and adaptability over time. To comprehensively evaluate its performance, we established TRQA, an original benchmark comprising over 1,900 expert-level question-answer pairs spanning a wide range of diseases and target classes. OriGene consistently outperforms human experts, leading research agents, and state-of-the-art large language models in accuracy, recall, and robustness, particularly under conditions of data sparsity or noise. Critically, OriGene nominated previously underexplored therapeutic targets for liver (GPR160) and colorectal cancer (ARG2), which demonstrated significant anti-tumor activity in patient-derived organoid and tumor fragment models mirroring human clinical exposures. These findings demonstrate OriGenes potential as a scalable and adaptive platform for AI-driven discovery of mechanistically grounded therapeutic targets, offering a new paradigm to accelerate drug development.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*