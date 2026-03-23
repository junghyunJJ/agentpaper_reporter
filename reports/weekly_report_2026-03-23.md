# Weekly AI Agent Paper Report

**Generated:** 2026-03-23 10:23
**Period:** 2026-03-16 to 2026-03-22

## Summary

- **Total papers fetched:** 1061
- **Papers matching keywords:** 171
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-03-16) | Change |
|--------|-----------|-----------|--------|
| Total matched | 171 | 146 | +25 |
| arxiv | 166 | 143 | +23 |
| biorxiv | 0 | 1 | -1 |
| medrxiv | 5 | 2 | +3 |

### Notable Trends

**1. Volume jump & source mix**  
- Total AI‑agent papers rose **17 %** (171 vs 146).  
- **arXiv** remains dominant and grew from 143 to **166** submissions (+16 %).  
- **medRxiv** more than doubled (2 → 5), while **bioRxiv** disappeared this week (1 → 0). The surge in medRxiv reflects a rapid move toward clinical‑care agents.

**2. Shift from “foundational” to “domain‑specific” applications**  
- **Last week’s headline titles** centered on core AI concepts – multi‑agent governance, semantic invariance, red‑team prompt‑injection defenses, and generic scientific‑research agents.  
- **This week’s top papers** are heavily **application‑driven**: high‑energy‑physics experiments, control‑systems design, primary‑care telemedicine, postpartum‑depression risk prediction, Parkinson’s exposome analysis, and rare‑disease copy‑number‑variation prioritization.  

**3. Growing emphasis on **healthcare & biomedical** agents**  
- 4 of the 10

---



## Biomedical Highlights (5 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. From Concept to Clinic: Real World Evidence for Autonomous AI Deployment in Primary Care Telemedicine

- **Authors:** Saenz, A. D., Schumacher, E., Naik, D., Khosla, N., Kannan, A.
- **Published:** 2026-03-20
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.18.26348749](https://doi.org/10.64898/2026.03.18.26348749)

- **Categories:** health informatics


> The paper presents the first large‑scale, clinician‑blinded, real‑world evaluation of a multi‑agent LLM system embedded in a nationwide primary‑care telemedicine platform, demonstrating that purposeful system architecture and safety gating—not just model size—enable safe autonomous clinical decision‑making. Using 2,379 completed patient encounters, the authors compared the AI’s intake diagnoses and disposition recommendations to those of treating physicians, finding a top‑1 diagnostic match of 91.3 % overall (96.3 % for cases above a confidence safety threshold) and a disposition error rate of only 2.5 %, with zero critical errors. These results support a staged, task‑calibrated deployment framework for autonomous AI in health care, providing concrete real‑world evidence that agentic AI can be reliably deployed for well‑defined, low‑complexity clinical tasks.


<details>
<summary>Abstract</summary>

Systems powered by large language models are widely used for health information and advice, yet robust evidence for their safety and effectiveness in real-world clinical care remains lacking. Most existing studies evaluate general-purpose chatbots in artificial settings, failing to account for the critical role of system design, deployment context, and integrated safety mechanisms. Here, we report, to our knowledge, the first large-scale, clinician-blinded, real-world evaluation of a multi-agent LLM-based system deployed within a nationwide U.S. primary care telemedicine platform, assessing readiness for task-specific autonomous deployment. In 2,379 real patient encounters, where users actively sought medical care and completed full visits with licensed clinicians, we compared the AI system's intake diagnoses and disposition suggestions to those of treating clinicians, who were blinded to the AI's outputs. The AI's top-1 diagnosis matched the clinician's diagnosis in 91.3% of cases overall, increasing to 96.3% among cases meeting a pre-specified safety confidence threshold, and 97.9% in common, lower-complexity conditions that met the same confidence threshold. Disposition accuracy was similarly high, with an overall error rate of 2.5% and no errors in suggestions to emergency room or home management. These results demonstrate that purposeful system architecture, rather than model capability alone, is essential for safe and effective autonomous clinical AI. We propose a staged, task-calibrated deployment framework, in which AI can be introduced autonomously for well-defined tasks with explicit safety gating and continuous monitoring, expanding scope as real-world evidence accrues. Our findings provide the first real-world evidence of readiness for safe autonomous clinical AI and offer a practical roadmap for its responsible deployment at scale.

</details>


### 2. CLINPREAI: AN AGENTIC AI SYSTEM FOR EARLY POSTPARTUM DEPRESSION RISK PREDICTION FROM MULTIMODAL EHR DATA

- **Authors:** Palacios, D., Aras, S., Zhong, Y., Zhao, J., Pasupuleti, S., Jeong, H.-H., Miller, E., Fletcher, T., Goulding, A., Chen, H., Liu, Z.
- **Published:** 2026-03-18
- **Source:** medrxiv
- **URL:** [https://doi.org/10.1101/2025.11.14.25340265](https://doi.org/10.1101/2025.11.14.25340265)

- **Categories:** health informatics


> The paper introduces **ClinPreAI**, the first agentic AI platform that autonomously designs, trains, and evaluates predictive models for early postpartum‑depression risk using multimodal electronic health record (EHR) data. Leveraging five specialized modules that iteratively conduct feature engineering, model selection, hyper‑parameter tuning, and debugging, ClinPreAI processes 27 structured clinical variables and unstructured social‑worker notes from 4,161 pregnant patients and outputs a binary EPDS ≥ 10 outcome. Across both structured‑only and multimodal settings, the system attains F1 scores of 0.68 ± 0.03 and 0.65 ± 0.04 respectively—outperforming conventional AutoML pipelines and commercial tools and matching custom LLM‑augmented baselines—demonstrating that autonomous AI agents can reliably generate high‑performing, interpretable clinical risk models without requiring domain experts to have machine‑learning expertise.


<details>
<summary>Abstract</summary>

AO_SCPLOWBSTRACTC_SCPLOWPostpartum depression (PPD) affects 10-15% of individuals annually, yet early identification and treatment remains challenging. We introduce ClinPreAI, a novel agentic AI system that autonomously designs, implements, and evaluates machine learning solutions for PPD risk prediction using multimodal electronic health record data. We analyzed data from 4,161 pregnant individuals hospitalized prior to delivery for medical or obstetrical complications at Texas Childrens Hospital (2012-2025), extracting 27 structured clinical variables and social worker notes. The primary outcome was Edinburgh Postnatal Depression Scale (EPDS) score [&ge;]10 (31.0% prevalence) within 6 months after delivery, indicating clinically significant depressive symptoms. ClinPreAI operates through five specialized modules that iteratively refine predictive models through autonomous experimentation. ClinPreAI demonstrated strong performance across modalities. On structured data, it achieved F1: 0.68 {+/-} 0.03, outperforming traditional AutoML (F1: 0.64 {+/-} 0.02) and commercial solutions (AWS Canvas F1: 0.54-0.55). On multimodal data, ClinPreAI achieved F1: 0.65 {+/-} 0.04, matching custom LLM-XGBoost (F1: 0.65 {+/-} 0.01) and outperforming zero-shot models (Claude Opus F1: 0.51-0.52). This represents the first application of agentic AI to perinatal mental health prediction. Our results demonstrate that autonomous AI agents can democratize sophisticated predictive modeling in clinical settings, which is particularly valuable where domain experts lack ML training. By automating experimentation and debugging, agentic systems lower barriers to developing robust clinical prediction tools while maintaining interpretability.

</details>


### 3. ADDRESSING THE ROLE OF OCCUPATIONAL EXPOSOME ON PARKINSON'S DISEASE AND PARKINSONISM IN A MATCHED CASE-CONTROL STUDY

- **Authors:** Lewis, F., Renzetti, S., Goulett, N., Azmoun, S., Sundar, V., Ali, M., Pitta, L., Shoieb, D., Caci, M., Borghesi, S., Covolo, L., Oppini, M., Gelatti, U., Padovani, A., Pilotto, A., Pepe, F., Turla, M., Crippa, P., Pani, L., Vermeulen, R., Kromhout, H., Lambertini, L., Colicino, E., Placidi, D., Lucchini, R.
- **Published:** 2026-03-18
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.16.26348171](https://doi.org/10.64898/2026.03.16.26348171)

- **Categories:** occupational and environmental health


> The paper’s main contribution is a comprehensive assessment of how cumulative occupational exposures—particularly to pesticides and metals—affect the risk of Parkinson’s disease (PD) and Parkinsonism, using the ALOHA+ Job‑Exposure Matrix to quantify lifelong exposure burdens. By conducting a hospital‑based matched case‑control study (334 cases and 334 controls) and applying conditional logistic regression together with positively constrained repeated‑holdout Weighted Quantile Sum (WQS) regression, the authors demonstrate that high cumulative pesticide exposure triples the odds of PD (OR ≈ 3.5) and that a composite exposure index (dominated by pesticides and metals) is significantly associated with disease risk. Although the findings advance epidemiological understanding of neurotoxic occupational hazards, they have limited direct relevance to agentic AI research, aside from illustrating how multi‑agent exposure modeling techniques (e


<details>
<summary>Abstract</summary>

Background/ObjectivesOccupational exposure to neurotoxicants such as pesticides, metals, and solvents has long been implicated in Parkinsons disease (PD) and Parkinsonism, yet the cumulative impact of multiple occupational exposure families over the working life remains insufficiently characterized. This study evaluated whether long-term cumulative occupational exposures, derived from the ALOHA+ Job-Exposure Matrix (ALOHA+-JEM), were associated with PD and Parkinsonism.

MethodsA hospital-based matched case-control study was conducted in the province of Brescia, Italy, including 668 participants (334 PD/Parkinsonism cases and 334 matched controls). Cases and controls were 1:1 matched based on sex, age, and lifetime occupational duration. Lifetime occupational histories were coded using ISCO-08 and harmonized to ISCO-88 for linkage with ALOHA+-JEM. Conditional logistic regression estimated associations between cumulative exposures (none/low/high) and disease status, adjusting for smoking, parental history of PD/tremor, and SNCA rs356219 genotype. Multi-agent occupational exposure burden indexes were evaluated using positively constrained repeated-holdout Weighted Quantile Sum (WQS) regression (100 bootstraps, 100 holdouts)

ResultsIn conditional logistic regression, parental history of PD or tremor (OR = 4.55, 95% CI: 2.44-8.48; q < 0.001) and the SNCA rs356219 CC genotype (OR = 2.17, 95% CI: 1.33-3.52; q = 0.013) were significantly associated with disease. High cumulative all pesticide exposure showed positive associations with combined PD + Parkinsonism (OR = 2.98, 95% CI: 1.23-7.25) and PD alone (OR = 3.56, 95% CI: 1.25-10.15). In WQS analyses, the composite occupational exposure burden index was positively associated with disease (combined PD + Parkinsonism: OR = 1.15, 95% CI: 1.00-1.30). All pesticides received the highest mean weight in all models (w = 0.434 for combined PD + Parkinsonism), followed by metals (w = 0.210), identifying them as contributing most strongly to the composite exposure index.

ConclusionsLong-term cumulative occupational exposures were associated with increased odds of PD and Parkinsonism. All pesticides and metals were most strongly associated with PD and Parkinsonism, consistent with established neurotoxic mechanisms attributable to occupational environments. These findings underscore the importance of occupational exposure prevention and risk-reduction strategies in occupational settings and highlight workplace exposures as preventable contributors to Parkinsonian disorders.

</details>


### 4. OpenScientist: evaluating an open agentic AI co-scientist to accelerate biomedical discovery

- **Authors:** Roberts, K. F., Abrams, Z. B., Cappelletti, L., Moqri, M., Heugel, N., Caufield, J. H., Bourdenx, M., Li, Y., Banerjee, J., Foschini, L., Galeano, D., Harris, N. L., Li, M., Ying, K., Melendez, J. A., Barthelemy, N. R., Bollinger, J. G., He, Y., Ovod, V., Benzinger, T. L. S., Flores, S., Gordon, B., Ojewole, A. A., Phatak, M., Elbert, D. L., Biber, S., Landsness, E. C., Mungall, C. J., Bateman, R. J., Reese, J.
- **Published:** 2026-03-18
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.15.26348338](https://doi.org/10.64898/2026.03.15.26348338)

- **Categories:** health informatics


> OpenScientist is an open‑source, auditable agentic AI system that acts as a semi‑autonomous co‑scientist, taking researcher‑defined biomedical questions, retrieving relevant data, performing statistical and machine‑learning analyses, and synthesizing the results into testable scientific insights. The authors evaluated the platform across four real‑world clinical case studies—Alzheimer’s biomarker prediction, plasma‑proteomic survival modeling, single‑cell transcriptomics of tau pathology, and hypothesis generation in multiple myeloma—by having domain experts compare the AI‑produced outputs with established findings and randomized controls. In each case OpenScientist completed analyses in minutes (instead of weeks‑months), correctly identified %ptau217 as the top amyloid PET predictor, matched published survival‑model performance, uncovered a plausible tau‑lysosome mechanism, and generated multiple‑myeloma hypotheses that were externally validated, demonstrating that open, reproducible agentic AI can reliably accelerate hypothesis generation and data‑driven discovery in biomedical research.


<details>
<summary>Abstract</summary>

BackgroundAdvances in medicine depend on analyzing large and complex data sources, but discovery is partly constrained by the limited time and domain expertise of human researchers. Agentic artificial intelligence (agentic AI) can accelerate discovery by automating components of the scientific workflow, including information retrieval, data analysis, and knowledge synthesis.

AimOpenScientist, an open-source agentic AI co-scientist, aims to accelerate biomedical discovery by semi-autonomously investigating scientist-defined queries and generating clinically relevant, verifiable scientific insights.

MethodsDomain experts evaluated OpenScientist for novel discoveries in four clinical case studies: (1) a prespecified analysis in a community-based Alzheimers disease biomarker cohort, (2) unsupervised modeling for plasma proteomic survival prediction, (3) hypothesis investigation in single-cell transcriptomic data from neurons with neurofibrillary tangles, and (4) hypothesis generation with validation in a multiple myeloma dataset with a randomized negative control.

ResultsOpenScientist completed analyses in minutes that otherwise would take weeks to months of human time and expertise. It identified %ptau217 as the best predictor of amyloid PET status, generated a plasma proteomic survival model with performance comparable to published models, proposed a mechanism linking tau pathology to altered lysosomal acidification, and generated multiple myeloma hypotheses that were validated in an external cohort while distinguishing true signal from randomized controls.

ConclusionOpenScientist demonstrates that open, auditable, agentic AI can support real-world clinical research by generating hypotheses, executing analyses, and discovering insights from complex datasets.

</details>


### 5. CoNVict: An Agentic AI System for Copy Number Variation Prioritization in Rare Disease Diagnosis

- **Authors:** Gencturk, M. M., Kara, M., Ozden, F.
- **Published:** 2026-03-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.16.26348493](https://doi.org/10.64898/2026.03.16.26348493)

- **Categories:** genetic and genomic medicine


> CoNVict introduces a novel agentic AI framework that leverages large‑language‑model (LLM) reasoning to prioritize copy‑number variants (CNVs) in rare‑disease diagnostics. The system combines a two‑stage pipeline—first a verdict classifier that triages candidate CNVs, then a tournament‑style pairwise ranking that performs structured, in‑context evidence integration guided by the patient’s phenotype—and operates without disease‑specific retraining. Benchmarked on simulated multi‑specialty cases, CoNVict markedly outperforms existing CNV‑annotation tools in correctly identifying causal variants, while also maintaining strong performance on variants of uncertain significance and non‑coding CNVs, demonstrating the utility of agentic AI for patient‑specific genomic interpretation.


<details>
<summary>Abstract</summary>

Copy number variants (CNVs) are established contributors to rare genetic disorders, yet their clinical interpretation remains challenging in diagnostic genomics. Large CNVs frequently encompass multiple functional regions whose clinical significance can only be resolved in the context of the patients phenotype. Effective prioritization demands variant-level scoring of dosage sensitivity, structural consequences, and disease associations, and systematic comparison of candidates within the same clinical context. Current computational tools only partially address these requirements: they automate variant-level scoring but leave phenotype-guided evidence integration and cross-variant ranking to the clinician, creating a gap between annotation throughput and diagnostic decision-making. Agentic AI systems coordinate large language model-driven reasoning across structured multi-step pipelines and have shown strong performance on biomedical tasks requiring iterative evidence evaluation and contextual judgement, making them well suited to patient-specific variant interpretation where rigid scoring functions fall short. Here, we present CoNVict, a two-stage agentic AI system for patient-specific CNV prioritization. The system ranks CNVs through verdict classification that triages candidates and tournament ranking that performs pairwise comparisons via structured, in-context reasoning. Evaluated on simulated diagnostic cases spanning multiple clinical subspecialties, CoNVict substantially outperforms existing computational methods in identifying the causal CNV and maintains robust performance on variants of uncertain significance and non-coding variants without retraining. Our results demonstrate that agentic AI can bridge the gap between automated variant-level annotation and the patient-specific clinical reasoning required for CNV-driven genetic diagnosis. Availability and Implementation: Source code and data are available at https://github.com/Muti-Kara/CoNVict.

</details>


---



## Arxiv (166 papers)


### 1. AI Agents Can Already Autonomously Perform Experimental High Energy Physics

- **Authors:** Eric A. Moreno, Samuel Bright-Thonney, Andrzej Novak, Dolores Garcia, Philip Harris
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.20179v1](http://arxiv.org/abs/2603.20179v1)
- **PDF:** [https://arxiv.org/pdf/2603.20179v1](https://arxiv.org/pdf/2603.20179v1)
- **Categories:** hep-ex, cs.AI, cs.LG


> The paper demonstrates that a large‑language‑model‑driven agent (Claude Code) can autonomously carry out an entire high‑energy‑physics analysis pipeline—event selection, background estimation, uncertainty quantification, statistical inference, and manuscript drafting—using only a dataset, an execution framework, and a corpus of prior literature. The authors introduce the “Just Furnish Context” (JFC) framework, which couples the agent with literature‑based knowledge retrieval and a multi‑agent review loop, and validate it on open ALEPH, DELPHI, and CMS data to reproduce electroweak, QCD, and Higgs measurements. Their results show that current LLM agents already possess sufficient agency to replace much of the repetitive coding work in experimental HEP, suggesting a shift toward using such agents for workflow automation while physicists focus on insight and validation.


<details>
<summary>Abstract</summary>

Large language model-based AI agents are now able to autonomously execute substantial portions of a high energy physics (HEP) analysis pipeline with minimal expert-curated input. Given access to a HEP dataset, an execution framework, and a corpus of prior experimental literature, we find that Claude Code succeeds in automating all stages of a typical analysis: event selection, background estimation, uncertainty quantification, statistical inference, and paper drafting. We argue that the experimental HEP community is underestimating the current capabilities of these systems, and that most proposed agentic workflows are too narrowly scoped or scaffolded to specific analysis structures. We present a proof-of-concept framework, Just Furnish Context (JFC), that integrates autonomous analysis agents with literature-based knowledge retrieval and multi-agent review, and show that this is sufficient to plan, execute, and document a credible high energy physics analysis. We demonstrate this by conducting analyses on open data from ALEPH, DELPHI, and CMS to perform electroweak, QCD, and Higgs boson measurements. Rather than replacing physicists, these tools promise to offload the repetitive technical burden of analysis code development, freeing researchers to focus on physics insight, truly novel method development, and rigorous validation. Given these developments, we advocate for new strategies for how the community trains students, organizes analysis efforts, and allocates human expertise.

</details>


### 2. Design-OS: A Specification-Driven Framework for Engineering System Design with a Control-Systems Design Case

- **Authors:** H. Sinan Bank, Daniel R. Herber, Thomas H. Bradley
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.20151v1](http://arxiv.org/abs/2603.20151v1)
- **PDF:** [https://arxiv.org/pdf/2603.20151v1](https://arxiv.org/pdf/2603.20151v1)
- **Categories:** cs.CE, cs.AI, eess.SY


> Design‑OS is a lightweight, specification‑driven workflow that formalizes the entire engineering design process (concept definition → literature survey → conceptual design → requirements → design definition) and uses those specifications as a shared contract between human designers and AI agents. The authors instantiate the workflow on a control‑systems case study—designing two rotary inverted‑pendulum platforms (an open‑source SimpleFOC reaction wheel and a commercial Quanser Furuta pendulum)—showing how the same structured specifications guide AI‑augmented literature search, parameter synthesis, and artifact generation while preserving traceability from intent to implementation. The results demonstrate that a specification‑centric approach makes the design process auditable, reusable, and extensible to heterogeneous physical systems, thereby extending AI orchestration from software engineering to agentic, human‑AI collaborative physical system design.


<details>
<summary>Abstract</summary>

Engineering system design -- whether mechatronic, control, or embedded -- often proceeds in an ad hoc manner, with requirements left implicit and traceability from intent to parameters largely absent. Existing specification-driven and systematic design methods mostly target software, and AI-assisted tools tend to enter the workflow at solution generation rather than at problem framing. Human--AI collaboration in the design of physical systems remains underexplored. This paper presents Design-OS, a lightweight, specification-driven workflow for engineering system design organized in five stages: concept definition, literature survey, conceptual design, requirements definition, and design definition. Specifications serve as the shared contract between human designers and AI agents; each stage produces structured artifacts that maintain traceability and support agent-augmented execution. We position Design-OS relative to requirements-driven design, systematic design frameworks, and AI-assisted design pipelines, and demonstrate it on a control systems design case using two rotary inverted pendulum platforms -- an open-source SimpleFOC reaction wheel and a commercial Quanser Furuta pendulum -- showing how the same specification-driven workflow accommodates fundamentally different implementations. A blank template and the full design-case artifacts are shared in a public repository to support reproducibility and reuse. The workflow makes the design process visible and auditable, and extends specification-driven orchestration of AI from software to physical engineering system design.

</details>


### 3. Reasoning Gets Harder for LLMs Inside A Dialogue

- **Authors:** Ivan Kartáč, Mateusz Lango, Ondřej Dušek
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.20133v1](http://arxiv.org/abs/2603.20133v1)
- **PDF:** [https://arxiv.org/pdf/2603.20133v1](https://arxiv.org/pdf/2603.20133v1)
- **Categories:** cs.CL


> The paper introduces **BOULDER**, a dynamic benchmark that recasts eight travel‑domain reasoning problems (arithmetic, spatial, temporal, commonsense, and formal) into both isolated prompts and multi‑turn task‑oriented dialogues, enabling a controlled study of how dialogue context impacts large language model (LLM) reasoning. By evaluating eight state‑of‑the‑art LLMs on the paired versions, the authors find a **large, consistent drop in accuracy** when the same reasoning tasks are embedded in a dialogue, and ablations reveal that the multi‑turn structure—along with role conditioning and tool‑use constraints—are the primary drivers of this degradation. These results underscore that current benchmark scores overestimate LLM reasoning robustness and highlight the necessity of testing and designing agentic AI systems within realistic, interactive conversational settings.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) achieve strong performance on many reasoning benchmarks, yet these evaluations typically focus on isolated tasks that differ from real-world usage in task-oriented dialogue (TOD). In this setting, LLMs must perform reasoning inherently while generating text and adhering to instructions on role, format, and style. This mismatch raises concerns about whether benchmark performance accurately reflects models' reasoning robustness in TOD setting. We investigate how framing reasoning tasks within TOD affects LLM performance by introducing BOULDER, a new dynamic benchmark covering eight travel-related tasks that require arithmetic, spatial, and temporal reasoning with both commonsense and formal aspects. Each problem is presented in both isolated and dialogue-based variants, enabling controlled comparison while mitigating data contamination. Experiments on eight LLMs reveal a substantial and consistent performance gap between isolated and dialogue settings. Through ablations and qualitative analysis, we show that this gap is largely driven by the multi-turn nature of dialogue, with additional effects from role conditioning and tool-use requirements. Our results highlight the need to evaluate LLM reasoning in realistic interactive scenarios.

</details>


### 4. Revisiting Gene Ontology Knowledge Discovery with Hierarchical Feature Selection and Virtual Study Group of AI Agents

- **Authors:** Cen Wan, Alex A. Freitas
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.20132v1](http://arxiv.org/abs/2603.20132v1)
- **PDF:** [https://arxiv.org/pdf/2603.20132v1](https://arxiv.org/pdf/2603.20132v1)
- **Categories:** cs.LG


> The paper introduces a **virtual study group of AI agents** that combines hierarchical feature selection of ageing‑related Gene Ontology (GO) terms with agentic AI reasoning to automate biological knowledge discovery. The authors first apply a multi‑level feature‑selection pipeline to isolate the most informative GO terms across four model organisms, then instantiate a coordinated swarm of language‑model agents that generate, critique, and refine scientific claims about ageing mechanisms; the agents’ internal communication protocols and consensus‑building mechanisms are explicitly engineered as part of the framework. Evaluation shows that the majority of the agents’ generated hypotheses are corroborated by existing literature, demonstrating that the hierarchical‑selection + agentic‑AI architecture can reliably surface novel, literature‑supported insights in the gene‑ontology domain and highlighting the utility of agentic AI for accelerating hypothesis generation in life‑science research.


<details>
<summary>Abstract</summary>

Large language models have achieved great success in multiple challenging tasks, and their capacity can be further boosted by the emerging agentic AI techniques. This new computing paradigm has already started revolutionising the traditional scientific discovery pipelines. In this work, we propose a novel agentic AI-based knowledge discovery-oriented virtual study group that aims to extract meaningful ageing-related biological knowledge considering highly ageing-related Gene Ontology terms that are selected by hierarchical feature selection methods. We investigate the performance of the proposed agentic AI framework by considering four different model organisms' ageing-related Gene Ontology terms and validate the biological findings by reviewing existing research articles. It is found that the majority of the AI agent-generated scientific claims can be supported by existing literatures and the proposed internal mechanisms of the virtual study group also play an important role in the designed agentic AI-based knowledge discovery framework.

</details>


### 5. An Agentic Multi-Agent Architecture for Cybersecurity Risk Management

- **Authors:** Ravish Gupta, Saket Kumar, Shreeya Sharma, Maulik Dang, Abhishek Aggarwal
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.20131v1](http://arxiv.org/abs/2603.20131v1)
- **PDF:** [https://arxiv.org/pdf/2603.20131v1](https://arxiv.org/pdf/2603.20131v1)
- **Categories:** eess.SY, cs.AI, cs.CR


> The paper introduces a novel **agentic multi‑agent architecture** for automating NIST‑CSF‑aligned cybersecurity risk assessments, in which six specialized LLM agents (profiling, asset mapping, threat analysis, control evaluation, risk scoring, recommendation generation) share and incrementally expand a persistent context, enabling later agents to build directly on earlier conclusions. Empirical evaluation on a real 15‑person HIPAA‑covered firm showed the system matched human CISSP assessments on 85 % of severity labels, captured 92 % of identified risks, and completed the workflow in under 15 minutes; additional experiments across five synthetic industry profiles demonstrated that a domain‑fine‑tuned model could surface sector‑specific threats missed by a general‑purpose model, while the entire pipeline was limited by the LLM’s context window (failure on a Tesla T4 with a 4,096‑token limit). These results highlight that **context‑sharing among coordinated agents** can dramatically accelerate risk assessment, but that **context capacity** is the primary bottleneck for scaling agentic AI pipelines.


<details>
<summary>Abstract</summary>

Getting a real cybersecurity risk assessment for a small organization is expensive -- a NIST CSF-aligned engagement runs $15,000 on the low end, takes weeks, and depends on practitioners who are genuinely scarce. Most small companies skip it entirely. We built a six-agent AI system where each agent handles one analytical stage: profiling the organization, mapping assets, analyzing threats, evaluating controls, scoring risks, and generating recommendations. Agents share a persistent context that grows as the assessment proceeds, so later agents build on what earlier ones concluded -- the mechanism that distinguishes this from standard sequential agent pipelines. We tested it on a 15-person HIPAA-covered healthcare company and compared outputs to independent assessments by three CISSP practitioners -- the system agreed with them 85% of the time on severity classifications, covered 92% of identified risks, and finished in under 15 minutes. We then ran 30 repeated single-agent assessments across five synthetic but sector-realistic organizational profiles in healthcare, fintech, manufacturing, retail, and SaaS, comparing a general-purpose Mistral-7B against a domain fine-tuned model. Both completed every run. The fine-tuned model flagged threats the baseline could not see at all: PHI exposure in healthcare, OT/IIoT vulnerabilities in manufacturing, platform-specific risks in retail. The full multi-agent pipeline, however, failed every one of 30 attempts on a Tesla T4 with its 4,096-token default context window -- context capacity, not model quality, turned out to be the binding constraint.

</details>


### 6. Agentic Harness for Real-World Compilers

- **Authors:** Yingwei Zheng, Cong Li, Shaohua Li, Yuqun Zhang, Zhendong Su
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.20075v1](http://arxiv.org/abs/2603.20075v1)
- **PDF:** [https://arxiv.org/pdf/2603.20075v1](https://arxiv.org/pdf/2603.20075v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces **llvm‑autofix**, the first agentic harness that equips large‑language‑model (LLM) agents with compiler‑specific tooling, a reproducible benchmark of LLVM bugs (llvm‑bench), and a lightweight “mini” agent (llvm‑autofix‑mini) for automatically diagnosing and repairing those bugs. By integrating LLVM‑friendly utilities (e.g., automated build, test, and diff extraction) and training the mini‑agent to interact with them, the authors evaluate frontier LLMs on real‑world compiler failures and find a 60 % drop in performance relative to ordinary software‑bug tasks, while llvm‑autofix‑mini surpasses the previous state‑of‑the‑art by roughly 22 %. These results demonstrate that specialized, agent‑oriented harnesses are essential for extending LLM‑driven debugging to the highly complex, cross‑domain domain of modern compilers.


<details>
<summary>Abstract</summary>

Compilers are critical to modern computing, yet fixing compiler bugs is difficult. While recent large language model (LLM) advancements enable automated bug repair, compiler bugs pose unique challenges due to their complexity, deep cross-domain expertise requirements, and sparse, non-descriptive bug reports, necessitating compiler-specific tools. To bridge the gap, we introduce llvm-autofix, the first agentic harness designed to assist LLM agents in understanding and fixing compiler bugs. Our focus is on LLVM, one of the most widely used compiler infrastructures. Central to llvm-autofix are agent-friendly LLVM tools, a benchmark llvm-bench of reproducible LLVM bugs, and a tailored minimal agent llvm-autofix-mini for fixing LLVM bugs. Our evaluation demonstrates a performance decline of 60% in frontier models when tackling compiler bugs compared with common software bugs. Our minimal agent llvm-autofix-mini also outperforms the state-of-the-art by approximately 22%. This emphasizes the necessity for specialized harnesses like ours to close the loop between LLMs and compiler engineering. We believe this work establishes a foundation for advancing LLM capabilities in complex systems like compilers. GitHub: https://github.com/dtcxzyw/llvm-autofix

</details>


### 7. Orchestrating Human-AI Software Delivery: A Retrospective Longitudinal Field Study of Three Software Modernization Programs

- **Authors:** Maximiliano Armesto, Christophe Kolb
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.20028v1](http://arxiv.org/abs/2603.20028v1)
- **PDF:** [https://arxiv.org/pdf/2603.20028v1](https://arxiv.org/pdf/2603.20028v1)
- **Categories:** cs.SE, cs.AI


> The paper’s main contribution is a large‑scale, longitudinal field evaluation of **Chiron**, an industrial platform that orchestrates human engineers and AI agents across the full software‑delivery pipeline (analysis, planning, implementation, validation). Using retrospective data from three real‑world modernization projects (≈30 k–400 k LOC) and comparing a traditional baseline with four successive platform versions, the authors model both observed metrics (stage durations, issue rates, release coverage) and counterfactual staffing scenarios (person‑days, senior‑equivalent effort). The results show that embedding AI agents in a coordinated workflow (especially in the later V3/V4 releases with acceptance‑criteria validation and hybrid execution) cuts total project time by ~74 % (36 → 9.3 project‑weeks), reduces raw effort by ~78 % (1080 → 232 person‑days), lowers validation issues by 74 % (8.03 → 2.09 per 100 tasks), and raises first‑release coverage from 77 % to 90 %, supporting the thesis that **orchestrated, team‑level AI integration yields far greater productivity gains than isolated coding assistants**.


<details>
<summary>Abstract</summary>

Evidence on AI in software engineering still leans heavily toward individual task completion, while evidence on team-level delivery remains scarce. We report a retrospective longitudinal field study of Chiron, an industrial platform that coordinates humans and AI agents across four delivery stages: analysis, planning, implementation, and validation. The study covers three real software modernization programs -- a COBOL banking migration (~30k LOC), a large accounting modernization (~400k LOC), and a .NET/Angular mortgage modernization (~30k LOC) -- observed across five delivery configurations: a traditional baseline and four successive platform versions (V1--V4). The benchmark separates observed outcomes (stage durations, task volumes, validation-stage issues, first-release coverage) from modeled outcomes (person-days and senior-equivalent effort under explicit staffing scenarios). Under baseline staffing assumptions, portfolio totals move from 36.0 to 9.3 summed project-weeks; modeled raw effort falls from 1080.0 to 232.5 person-days; modeled senior-equivalent effort falls from 1080.0 to 139.5 SEE-days; validation-stage issue load falls from 8.03 to 2.09 issues per 100 tasks; and first-release coverage rises from 77.0% to 90.5%. V3 and V4 add acceptance-criteria validation, repository-native review, and hybrid human-agent execution, simultaneously improving speed, coverage, and issue load. The evidence supports a central thesis: the largest gains appear when AI is embedded in an orchestrated workflow rather than deployed as an isolated coding assistant.

</details>


### 8. ReViSQL: Achieving Human-Level Text-to-SQL

- **Authors:** Yuxuan Zhu, Tengjun Jin, Yoojin Choi, Daniel Kang
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.20004v1](http://arxiv.org/abs/2603.20004v1)
- **PDF:** [https://arxiv.org/pdf/2603.20004v1](https://arxiv.org/pdf/2603.20004v1)
- **Categories:** cs.DB, cs.CL


> ReViSQL demonstrates that human‑level Text‑to‑SQL performance can be reached without elaborate agent pipelines by simply improving training data quality. The authors curate a verified subset of the BIRD benchmark (BIRD‑Verified) through expert‑driven error correction, then fine‑tune large language models with reinforcement learning using verifiable execution rewards (RLVR) and apply lightweight inference‑time reconciliation (execution‑based voting). On an expert‑validated BIRD Mini‑Dev set, the 235 B‑parameter model attains 93.2 % execution accuracy—surpassing the proxy human baseline and beating the previous open‑source state‑of‑the‑art by 9.8 %—while a 30 B‑parameter version matches SOTA at a 7.5× lower query cost.


<details>
<summary>Abstract</summary>

Translating natural language to SQL (Text-to-SQL) is a critical challenge in both database research and data analytics applications. Recent efforts have focused on enhancing SQL reasoning by developing large language models and AI agents that decompose Text-to-SQL tasks into manually designed, step-by-step pipelines. However, despite these extensive architectural engineering efforts, a significant gap remains: even state-of-the-art (SOTA) AI agents have not yet achieved the human-level accuracy on the BIRD benchmark. In this paper, we show that closing this gap does not require further architectural complexity, but rather clean training data to improve SQL reasoning of the underlying models.
  We introduce ReViSQL, a streamlined framework that achieves human-level accuracy on BIRD for the first time. Instead of complex AI agents, ReViSQL leverages reinforcement learning with verifiable rewards (RLVR) on BIRD-Verified, a dataset we curated comprising 2.5k verified Text-to-SQL instances based on the BIRD Train set. To construct BIRD-Verified, we design a data correction and verification workflow involving SQL experts. We identified and corrected data errors in 61.1% of a subset of BIRD Train. By training on BIRD-Verified, we show that improving data quality alone boosts the single-generation accuracy by 8.2-13.9% under the same RLVR algorithm. To further enhance performance, ReViSQL performs inference-time scaling via execution-based reconciliation and majority voting. Empirically, we demonstrate the superiority of our framework with two model scales: ReViSQL-235B-A22B and ReViSQL-30B-A3B. On an expert-verified BIRD Mini-Dev set, ReViSQL-235B-A22B achieves 93.2% execution accuracy, exceeding the proxy human-level accuracy (92.96%) and outperforming the prior open-source SOTA method by 9.8%. Our lightweight ReViSQL-30B-A3B matches the prior SOTA at a 7.5$\times$ lower per-query cost.

</details>


### 9. An Agentic Approach to Generating XAI-Narratives

- **Authors:** Yifan He, David Martens
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.20003v1](http://arxiv.org/abs/2603.20003v1)
- **PDF:** [https://arxiv.org/pdf/2603.20003v1](https://arxiv.org/pdf/2603.20003v1)
- **Categories:** cs.CL


> The paper introduces a multi‑agent framework for automatically generating and refining explainable‑AI (XAI) narratives, where a **Narrator** LLM produces a first‑draft explanation and a set of **Critic Agents** iteratively evaluate and provide feedback on faithfulness and coherence, prompting the Narrator to revise the text. Five concrete agentic designs (Basic, Critic, Critic‑Rule, Coherent, Coherent‑Rule) are instantiated across five LLMs and five tabular benchmark datasets, and their performance is measured in terms of how often the resulting narratives faithfully reflect the underlying model’s reasoning. Experiments show that the Basic, Critic, and Critic‑Rule designs markedly improve faithfulness—Claude‑4.5‑Sonnet in the Basic design cuts unfaithful narratives by ~90 % after three revision cycles—and that a majority‑voting ensemble further boosts results for most LLMs, demonstrating that coordinated agentic systems can reliably produce accurate, human‑readable XAI explanations.


<details>
<summary>Abstract</summary>

Explainable AI (XAI) research has experienced substantial growth in recent years. Existing XAI methods, however, have been criticized for being technical and expert-oriented, motivating the development of more interpretable and accessible explanations. In response, large language model (LLM)-generated XAI narratives have been proposed as a promising approach for translating post-hoc explanations into more accessible, natural-language explanations. In this work, we propose a multi-agent framework for XAI narrative generation and refinement. The framework comprises the Narrator, which generates and revises narratives based on feedback from multiple Critic Agents on faithfulness and coherence metrics, thereby enabling narrative improvement through iteration. We design five agentic systems (Basic Design, Critic Design, Critic-Rule Design, Coherent Design, and Coherent-Rule Design) and systematically evaluate their effectiveness across five LLMs on five tabular datasets. Results validate that the Basic Design, the Critic Design, and the Critic-Rule Design are effective in improving the faithfulness of narratives across all LLMs. Claude-4.5-Sonnet on Basic Design performs best, reducing the number of unfaithful narratives by 90% after three rounds of iteration. To address recurrent issues, we further introduce an ensemble strategy based on majority voting. This approach consistently enhances performance for four LLMs, except for DeepSeek-V3.2-Exp. These findings highlight the potential of agentic systems to produce faithful and coherent XAI narratives.

</details>


### 10. Trojan's Whisper: Stealthy Manipulation of OpenClaw through Injected Bootstrapped Guidance

- **Authors:** Fazhong Liu, Zhuoyan Chen, Tu Lan, Haozhen Tan, Zhenyu Xu, Xiang Li, Guoxing Chen, Yan Meng, Haojin Zhu
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19974v1](http://arxiv.org/abs/2603.19974v1)
- **PDF:** [https://arxiv.org/pdf/2603.19974v1](https://arxiv.org/pdf/2603.19974v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **guidance injection**, a novel stealth attack on autonomous coding agents such as OpenClaw, where adversaries embed malicious operational narratives into the platform’s bootstrap “skill” files so that the agent internalizes harmful behaviors as routine best practices. By creating 26 malicious skills across 13 attack categories and evaluating them on the newly‑crafted ORE‑Bench developer‑workspace benchmark with 52 user prompts and six leading LLM back‑ends, the authors show that the attacks succeed 16 %–64 % of the time—often without any user confirmation—and evade detection by 94 % of existing static and LLM‑based scanners. These results highlight a critical security gap in extensible agent ecosystems and motivate defenses based on capability isolation, runtime policy enforcement, and provenance‑verified guidance.


<details>
<summary>Abstract</summary>

Autonomous coding agents are increasingly integrated into software development workflows, offering capabilities that extend beyond code suggestion to active system interaction and environment management. OpenClaw, a representative platform in this emerging paradigm, introduces an extensible skill ecosystem that allows third-party developers to inject behavioral guidance through lifecycle hooks during agent initialization. While this design enhances automation and customization, it also opens a novel and unexplored attack surface. In this paper, we identify and systematically characterize guidance injection, a stealthy attack vector that embeds adversarial operational narratives into bootstrap guidance files. Unlike traditional prompt injection, which relies on explicit malicious instructions, guidance injection manipulates the agent's reasoning context by framing harmful actions as routine best practices. These narratives are automatically incorporated into the agent's interpretive framework and influence future task execution without raising suspicion.We construct 26 malicious skills spanning 13 attack categories including credential exfiltration, workspace destruction, privilege escalation, and persistent backdoor installation. We evaluate them using ORE-Bench, a realistic developer workspace benchmark we developed. Across 52 natural user prompts and six state-of-the-art LLM backends, our attacks achieve success rates from 16.0% to 64.2%, with the majority of malicious actions executed autonomously without user confirmation. Furthermore, 94% of our malicious skills evade detection by existing static and LLM-based scanners. Our findings reveal fundamental tensions in the design of autonomous agent ecosystems and underscore the urgent need for defenses based on capability isolation, runtime policy enforcement, and transparent guidance provenance.

</details>


### 11. Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents

- **Authors:** Luiz C. Borro, Luiz A. B. Macarini, Gordon Tindall, Michael Montero, Adam B. Struck
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19935v1](http://arxiv.org/abs/2603.19935v1)
- **PDF:** [https://arxiv.org/pdf/2603.19935v1](https://arxiv.org/pdf/2603.19935v1)
- **Categories:** cs.LG


> Memori introduces an LLM‑agnostic, persistent‑memory layer that reframes agent memory as a data‑structuring problem, converting raw dialogue into compact semantic triples and concise conversation summaries via its Advanced Augmentation pipeline. By indexing these structured representations, Memori enables precise, low‑overhead retrieval for LLM agents, dramatically reducing prompt length while preserving context awareness. On the LoCoMo benchmark, Memori attains 81.95 % accuracy using only ~1.3 k tokens per query—about 5 % of a full‑context prompt—yielding a 67 % token reduction versus other memory systems and more than 20× cost savings relative to naïve full‑context approaches.


<details>
<summary>Abstract</summary>

As large language models (LLMs) evolve into autonomous agents, persistent memory at the API layer is essential for enabling context-aware behavior across LLMs and multi-session interactions. Existing approaches force vendor lock-in and rely on injecting large volumes of raw conversation into prompts, leading to high token costs and degraded performance.
  We introduce Memori, an LLM-agnostic persistent memory layer that treats memory as a data structuring problem. Its Advanced Augmentation pipeline converts unstructured dialogue into compact semantic triples and conversation summaries, enabling precise retrieval and coherent reasoning.
  Evaluated on the LoCoMo benchmark, Memori achieves 81.95% accuracy, outperforming existing memory systems while using only 1,294 tokens per query (~5% of full context). This results in substantial cost reductions, including 67% fewer tokens than competing approaches and over 20x savings compared to full-context methods.
  These results show that effective memory in LLM agents depends on structured representations instead of larger context windows, enabling scalable and cost-efficient deployment.

</details>


### 12. Utility-Guided Agent Orchestration for Efficient LLM Tool Use

- **Authors:** Boyan Liu, Gongming Zhao, Hongli Xu
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19896v1](http://arxiv.org/abs/2603.19896v1)
- **PDF:** [https://arxiv.org/pdf/2603.19896v1](https://arxiv.org/pdf/2603.19896v1)
- **Categories:** cs.AI


> The paper introduces a **utility‑guided orchestration policy** that explicitly decides, at each step, whether an LLM‑based agent should answer, retrieve information, invoke a tool, verify a result, or stop, by estimating the expected gain versus the cost, uncertainty, and redundancy of each action.  Rather than relying on fixed pipelines or unconstrained ReAct‑style prompting, the authors formulate agent control as a decision‑theoretic problem and implement a lightweight utility function that can be tuned to trade off answer quality against token usage, latency, and tool‑call overhead.  Empirical evaluations on a suite of benchmark tasks show that this explicit orchestration dramatically reduces unnecessary tool calls and token consumption while preserving (or even improving) task performance, and that varying the utility parameters yields predictable, controllable shifts along the quality‑cost frontier—demonstrating a practical, analyzable mechanism for managing agentic AI behavior.


<details>
<summary>Abstract</summary>

Tool-using large language model (LLM) agents often face a fundamental tension between answer quality and execution cost. Fixed workflows are stable but inflexible, while free-form multi-step reasoning methods such as ReAct may improve task performance at the expense of excessive tool calls, longer trajectories, higher token consumption, and increased latency. In this paper, we study agent orchestration as an explicit decision problem rather than leaving it entirely to prompt-level behavior. We propose a utility-guided orchestration policy that selects among actions such as respond, retrieve, tool call, verify, and stop by balancing estimated gain, step cost, uncertainty, and redundancy. Our goal is not to claim universally best task performance, but to provide a controllable and analyzable policy framework for studying quality-cost trade-offs in tool-using LLM agents. Experiments across direct answering, threshold control, fixed workflows, ReAct, and several policy variants show that explicit orchestration signals substantially affect agent behavior. Additional analyses on cost definitions, workflow fairness, and redundancy control further demonstrate that lightweight utility design can provide a defensible and practical mechanism for agent control.

</details>


### 13. Beyond detection: cooperative multi-agent reasoning for rapid onboard EO crisis response

- **Authors:** Alejandro D. Mousist, Pedro Delgado de Robles Martín, Raquel Lladró Climent, Julian Cobos Aparicio
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19858v1](http://arxiv.org/abs/2603.19858v1)
- **PDF:** [https://arxiv.org/pdf/2603.19858v1](https://arxiv.org/pdf/2603.19858v1)
- **Categories:** cs.RO, cs.MA


> The paper introduces a hierarchical, event‑driven multi‑agent architecture that enables autonomous, onboard Earth‑Observation (EO) processing under tight compute and bandwidth limits. By deploying specialized AI agents—an Early‑Warning hypothesis generator, domain‑specific analysis modules, and a Decision consolidator—across distributed satellite nodes, the system orchestrates vision‑language models and classic remote‑sensing tools through a routing‑based pipeline that performs structured multimodal reasoning only when needed. Experiments on wildfire and flood detection using an in‑orbit edge‑computing platform show that this cooperative agentic framework cuts computational load dramatically while preserving accurate, timely alerts, demonstrating the viability of distributed, agent‑centric AI for rapid EO crisis response.


<details>
<summary>Abstract</summary>

Rapid identification of hazardous events is essential for next-generation Earth Observation (EO) missions supporting disaster response. However, current monitoring pipelines remain largely ground-centric, introducing latency due to downlink limitations, multi-source data fusion constraints, and the computational cost of exhaustive scene analysis.
  This work proposes a hierarchical multi-agent architecture for onboard EO processing under strict resource and bandwidth constraints. The system enables the exploitation of complementary multimodal observations by coordinating specialized AI agents within an event-driven decision pipeline. AI agents can be deployed across multiple nodes in a distributed setting, such as satellite platforms. An Early Warning agent generates fast hypotheses from onboard observations and selectively activates domain-specific analysis agents, while a Decision agent consolidates the evidence to issue a final alert. The architecture combines vision-language models, traditional remote sensing analysis tools, and role-specialized agents to enable structured reasoning over multimodal observations while minimizing unnecessary computation.
  A proof-of-concept implementation was executed on the engineering model of an edge-computing platform currently deployed in orbit, using representative satellite data. Experiments on wildfire and flood monitoring scenarios show that the proposed routing-based pipeline significantly reduces computational overhead while maintaining coherent decision outputs, demonstrating the feasibility of distributed agent-based reasoning for future autonomous EO constellations.

</details>


### 14. Borderless Long Speech Synthesis

- **Authors:** Xingchen Song, Di Wu, Dinghao Zhou, Pengyu Cheng, Hongwu Ding, Yunchao He, Jie Wang, Shengfan Shen, Sixiang Lv, Lichun Fan, Hang Su, Yifeng Wang, Shuai Wang, Meng Meng, Jian Luan
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19798v1](http://arxiv.org/abs/2603.19798v1)
- **PDF:** [https://arxiv.org/pdf/2603.19798v1](https://arxiv.org/pdf/2603.19798v1)
- **Categories:** cs.SD, cs.CL, eess.AS


> The paper presents **Borderless Long Speech Synthesis**, a unified TTS framework that can generate coherent, multi‑speaker, long‑form audio while preserving global context, emotional dynamics, and acoustic variations. It combines a “label‑over‑filtering” data pipeline with a hierarchical **Global‑Sentence‑Token** annotation scheme and a continuous‑tokenizer backbone enhanced by Chain‑of‑Thought reasoning and Dimension Dropout, enabling the system to follow complex, instruction‑driven prompts. Experiments show that the hierarchical annotations serve as a **Structured Semantic Interface** between a large‑language‑model agent and the synthesis engine, allowing the LLM to issue fine‑grained, scene‑level commands that produce agentic, borderless speech across extended dialogues and interactions.


<details>
<summary>Abstract</summary>

Most existing text-to-speech (TTS) systems either synthesize speech sentence by sentence and stitch the results together, or drive synthesis from plain-text dialogues alone. Both approaches leave models with little understanding of global context or paralinguistic cues, making it hard to capture real-world phenomena such as multi-speaker interactions (interruptions, overlapping speech), evolving emotional arcs, and varied acoustic environments. We introduce the Borderless Long Speech Synthesis framework for agent-centric, borderless long audio synthesis. Rather than targeting a single narrow task, the system is designed as a unified capability set spanning VoiceDesigner, multi-speaker synthesis, Instruct TTS, and long-form text synthesis. On the data side, we propose a "Labeling over filtering/cleaning" strategy and design a top-down, multi-level annotation schema we call Global-Sentence-Token. On the model side, we adopt a backbone with a continuous tokenizer and add Chain-of-Thought (CoT) reasoning together with Dimension Dropout, both of which markedly improve instruction following under complex conditions. We further show that the system is Native Agentic by design: the hierarchical annotation doubles as a Structured Semantic Interface between the LLM Agent and the synthesis engine, creating a layered control protocol stack that spans from scene semantics down to phonetic detail. Text thereby becomes an information-complete, wide-band control channel, enabling a front-end LLM to convert inputs of any modality into structured generation commands, extending the paradigm from Text2Speech to borderless long speech synthesis.

</details>


### 15. Helix: A Dual-Helix Co-Evolutionary Multi-Agent System for Prompt Optimization and Question Reformulation

- **Authors:** Kewen Zhu, Liping Yi, Zhiming Zhao, Xiang Li, Qinghua Hu
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19732v1](http://arxiv.org/abs/2603.19732v1)
- **PDF:** [https://arxiv.org/pdf/2603.19732v1](https://arxiv.org/pdf/2603.19732v1)
- **Categories:** cs.MA


> The paper introduces **Helix**, a dual‑helix co‑evolutionary multi‑agent framework that simultaneously optimizes large‑language‑model prompts and reformulates user questions, treating the two as mutually dependent variables rather than fixing one while tweaking the other. Helix orchestrates a three‑stage process: (1) a planner decomposes the joint optimization into coupled objectives, (2) paired “prompt‑agent” and “question‑agent” streams iteratively generate, critique, and refine each other’s outputs in a dual‑track co‑evolution, and (3) a strategy‑driven generator produces high‑quality question reformulations for downstream inference. Across 12 benchmarks, Helix outperforms six strong baselines by up to 3.95 percentage points while maintaining comparable computational efficiency, demonstrating that coordinated, agentic co‑evolution can substantially boost automated prompt optimization and task performance.


<details>
<summary>Abstract</summary>

Automated prompt optimization (APO) aims to improve large language model performance by refining prompt instructions. However, existing methods are largely constrained by fixed prompt templates, limited search spaces, or single-sided optimization that treats user questions as immutable inputs. In practice, question formulation and prompt design are inherently interdependent: clearer question structures facilitate focused reasoning and task understanding, while effective prompts reveal better ways to organize and restate queries. Ignoring this coupling fundamentally limits the effectiveness and adaptability of current APO approaches. We propose a unified multi-agent system (Helix) that jointly optimizes question reformulation and prompt instructions through a structured three-stage co-evolutionary framework. Helix integrates (1) planner-guided decomposition that breaks optimization into coupled question-prompt objectives, (2) dual-track co-evolution where specialized agents iteratively refine and critique each other to produce complementary improvements, and (3) strategy-driven question generation that instantiates high-quality reformulations for robust inference. Extensive experiments on 12 benchmarks against 6 strong baselines demonstrate the effectiveness of Helix, achieving up to 3.95% performance improvements across tasks with favorable optimization efficiency.

</details>


### 16. A Subgoal-driven Framework for Improving Long-Horizon LLM Agents

- **Authors:** Taiyi Wang, Sian Gooding, Florian Hartmann, Oriana Riva, Edward Grefenstette
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19685v1](http://arxiv.org/abs/2603.19685v1)
- **PDF:** [https://arxiv.org/pdf/2603.19685v1](https://arxiv.org/pdf/2603.19685v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper introduces a subgoal‑driven architecture for LLM‑based agents that (1) decomposes long‑horizon tasks into explicit intermediate subgoals during inference, and (2) trains agents with a milestone‑based reinforcement‑learning scheme (MiRA) that supplies dense rewards at each subgoal. By integrating real‑time subgoal planning with dense milestone rewards, the authors boost the success rate of a proprietary model (Gemini) by ~10 % on WebArena‑Lite and raise an open‑source Gemma‑3‑12B from 6.4 % to 43.0 %, surpassing GPT‑4‑Turbo, GPT‑4o, and the prior open‑model state‑of‑the‑art (WebRL 38.4 %). These results demonstrate that explicit subgoal inference and milestone‑driven RL substantially improve the long‑horizon planning and robustness of autonomous LLM agents.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based agents have emerged as powerful autonomous controllers for digital environments, including mobile interfaces, operating systems, and web browsers. Web navigation, for example, requires handling dynamic content and long sequences of actions, making it particularly challenging. Existing LLM-based agents struggle with long-horizon planning in two main ways. During online execution, they often lose track as new information arrives, lacking a clear and adaptive path toward the final goal. This issue is further exacerbated during reinforcement learning (RL) fine-tuning, where sparse and delayed rewards make it difficult for agents to identify which actions lead to success, preventing them from maintaining coherent reasoning over extended tasks. To address these challenges, we propose two contributions. First, we introduce an agent framework that leverages proprietary models for online planning through subgoal decomposition. Second, we present MiRA (Milestoning your Reinforcement Learning Enhanced Agent), an RL training framework that uses dense, milestone-based reward signals. The real-time planning mechanism improves proprietary models such as Gemini by approximately a 10% absolute increase in success rate (SR) on the WebArena-Lite benchmark. Meanwhile, applying MiRA to the open Gemma3-12B model increases its success rate from 6.4% to 43.0%. This performance surpasses proprietary systems such as GPT-4-Turbo (17.6%) and GPT-4o (13.9%), as well as the previous open-model state of the art, WebRL (38.4%). Overall, our findings demonstrate that combining explicit inference-time planning with milestone-based rewards significantly improves an agent's long-horizon capabilities, paving the way for more robust and general-purpose autonomous systems.

</details>


### 17. GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems

- **Authors:** Hongjiang Chen, Xin Zheng, Yixin Liu, Pengfei Jiao, Shiyuan Li, Huan Liu, Zhidong Zhao, Ziqi Xu, Ibrahim Khalil, Shirui Pan
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19677v1](http://arxiv.org/abs/2603.19677v1)
- **PDF:** [https://arxiv.org/pdf/2603.19677v1](https://arxiv.org/pdf/2603.19677v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> GoAgent introduces a novel, group‑centric approach to constructing communication topologies for LLM‑driven multi‑agent systems, treating collaborative sub‑teams as atomic units rather than relying on emergent structures from node‑level links. The method first uses an LLM to enumerate task‑relevant candidate groups, then autoregressively selects and connects these groups while applying a conditional information bottleneck (CIB) objective to compress inter‑group messages and suppress redundant noise. Across six benchmark tasks, GoAgent achieves a new state‑of‑the‑art average accuracy of 93.84 % and cuts token usage by roughly 17 %, demonstrating more efficient and effective coordination in agentic AI systems.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based multi-agent systems (MAS) have demonstrated exceptional capabilities in solving complex tasks, yet their effectiveness depends heavily on the underlying communication topology that coordinates agent interactions. Within these systems, successful problem-solving often necessitates task-specific group structures to divide and conquer subtasks. However, most existing approaches generate communication topologies in a node-centric manner, leaving group structures to emerge implicitly from local connectivity decisions rather than modeling them explicitly, often leading to suboptimal coordination and unnecessary communication overhead. To address this limitation, we propose GoAgent (Group-of-Agents), a communication topology generation method that explicitly treats collaborative groups as the atomic units of MAS construction. Specifically, GoAgent first enumerates task-relevant candidate groups through an LLM and then autoregressively selects and connects these groups as atomic units to construct the final communication graph, jointly capturing intra-group cohesion and inter-group coordination. To mitigate communication redundancy and noise propagation inherent in expanding topologies, we further introduce a conditional information bottleneck (CIB) objective that compresses inter-group communication, preserving task-relevant signals while filtering out redundant historical noise. Extensive experiments on six benchmarks demonstrate the state-of-the-art performance of GoAgent with 93.84% average accuracy while reducing token consumption by about 17%.

</details>


### 18. Structured Prompting for Arabic Essay Proficiency: A Trait-Centric Evaluation Approach

- **Authors:** Salim Al Mandhari, Hieu Pham Dinh, Mo El-Haj, Paul Rayson
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19668v1](http://arxiv.org/abs/2603.19668v1)
- **PDF:** [https://arxiv.org/pdf/2603.19668v1](https://arxiv.org/pdf/2603.19668v1)
- **Categories:** cs.CL


> The paper introduces a structured‑prompting framework that turns large language models into trait‑specialist evaluators for Arabic Automatic Essay Scoring, using a three‑level prompting hierarchy (standard, hybrid “multi‑agent” raters, and rubric‑guided with scored exemplars). By testing eight LLMs on the newly released QAES dataset, the authors show that the hybrid and rubric‑guided prompts—especially when combined with few‑shot exemplars—significantly boost trait‑level agreement (e.g., Fanar‑1‑9B‑Instruct reaches QWK = 0.28, CI = 0.41), with the largest gains on discourse‑level traits such as Development and Style. The results demonstrate that prompt architecture, rather than model size, is the key driver for effective, scalable Arabic essay assessment, offering a practical multi‑agent paradigm for low‑resource educational AI applications.


<details>
<summary>Abstract</summary>

This paper presents a novel prompt engineering framework for trait specific Automatic Essay Scoring (AES) in Arabic, leveraging large language models (LLMs) under zero-shot and few-shot configurations. Addressing the scarcity of scalable, linguistically informed AES tools for Arabic, we introduce a three-tier prompting strategy (standard, hybrid, and rubric-guided) that guides LLMs in evaluating distinct language proficiency traits such as organization, vocabulary, development, and style. The hybrid approach simulates multi-agent evaluation with trait specialist raters, while the rubric-guided method incorporates scored exemplars to enhance model alignment. In zero and few-shot settings, we evaluate eight LLMs on the QAES dataset, the first publicly available Arabic AES resource with trait level annotations. Experimental results using Quadratic Weighted Kappa (QWK) and Confidence Intervals show that Fanar-1-9B-Instruct achieves the highest trait level agreement in both zero and few-shot prompting (QWK = 0.28 and CI = 0.41), with rubric-guided prompting yielding consistent gains across all traits and models. Discourse-level traits such as Development and Style showed the greatest improvements. These findings confirm that structured prompting, not model scale alone, enables effective AES in Arabic. Our study presents the first comprehensive framework for proficiency oriented Arabic AES and sets the foundation for scalable assessment in low resource educational contexts.

</details>


### 19. On the existence of fair zero-determinant strategies in the periodic prisoner's dilemma game

- **Authors:** Ken Nakamura, Masahiko Ueda
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19641v1](http://arxiv.org/abs/2603.19641v1)
- **PDF:** [https://arxiv.org/pdf/2603.19641v1](https://arxiv.org/pdf/2603.19641v1)
- **Categories:** physics.soc-ph, cs.MA, eess.SY


> The paper proves that, unlike in the classic repeated Prisoner’s Dilemma, fair zero‑determinant (ZD) strategies are not guaranteed to exist in the periodic (state‑changing) version of the game. By analytically extending the known ZD existence conditions to this simplest stochastic game and examining the linear payoff‑control equations across state transitions, the authors show that the Tit‑for‑Tat rule—always a fair ZD strategy in the repeated setting—fails to satisfy the fairness constraint in the periodic setting. These results reveal a fundamental limitation for unilateral payoff‑control mechanisms in stochastic multi‑agent environments, suggesting that agentic AI designs relying on ZD‑type strategies must account for environmental state dynamics.


<details>
<summary>Abstract</summary>

Repeated games are a framework for investigating long-term interdependence of multi-agent systems. In repeated games, zero-determinant (ZD) strategies attract much attention in evolutionary game theory, since they can unilaterally control payoffs. Especially, fair ZD strategies unilaterally equalize the payoff of the focal player and the average payoff of the opponents, and they were found in several games including the social dilemma games. Although the existence condition of ZD strategies in repeated games was specified, its extension to stochastic games is almost unclear. Stochastic games are an extension of repeated games, where a state of an environment exists, and the state changes to another one according to an action profile of players. Because of the transition of an environmental state, the existence condition of ZD strategies in stochastic games is more complicated than that in repeated games. Here, we investigate the existence condition of fair ZD strategies in the periodic prisoner's dilemma game, which is one of the simplest stochastic games. We show that fair ZD strategies do not necessarily exist in the periodic prisoner's dilemma game, in contrast to the repeated prisoner's dilemma game. Furthermore, we also prove that the Tit-for-Tat strategy, which imitates the opponent's action, is not necessarily a fair ZD strategy in the periodic prisoner's dilemma game, whereas the Tit-for-Tat strategy is always a fair ZD strategy in the repeated prisoner's dilemma game. Our results highlight difference between ZD strategies in the periodic prisoner's dilemma game and ones in the standard repeated prisoner's dilemma game.

</details>


### 20. PowerLens: Taming LLM Agents for Safe and Personalized Mobile Power Management

- **Authors:** Xingyu Feng, Chang Sun, Yuzhu Wang, Zhangbing Zhou, Chengwen Luo, Zhuangzhuang Chen, Xiaomin Ouyang, Huanqi Yang
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19584v1](http://arxiv.org/abs/2603.19584v1)
- **PDF:** [https://arxiv.org/pdf/2603.19584v1](https://arxiv.org/pdf/2603.19584v1)
- **Categories:** cs.AI, eess.SY


> PowerLens introduces a multi‑agent framework that harnesses the commonsense reasoning of large language models to generate safe, context‑aware power‑management policies on Android devices, bridging the semantic gap between user activities and low‑level system parameters. By combining UI‑semantic context extraction, a policy‑definition language (PDL) for formal verification, and a two‑tier memory that distills implicit user feedback into confidence‑weighted preferences, the system produces zero‑shot, personalized adjustments across 18 power‑related knobs without explicit configuration. In real‑world tests on a rooted phone, PowerLens attains 81.7 % correct action rates, cuts energy consumption by 38.8 % versus stock Android, converges to stable user preferences within 3–5 days, and imposes only 0.5 % of daily battery capacity as overhead, demonstrating a practical, safe, and adaptable LLM‑agent approach to mobile resource management.


<details>
<summary>Abstract</summary>

Battery life remains a critical challenge for mobile devices, yet existing power management mechanisms rely on static rules or coarse-grained heuristics that ignore user activities and personal preferences. We present PowerLens, a system that tames the reasoning power of Large Language Models (LLMs) for safe and personalized mobile power management on Android devices. The key idea is that LLMs' commonsense reasoning can bridge the semantic gap between user activities and system parameters, enabling zero-shot, context-aware policy generation that adapts to individual preferences through implicit feedback. PowerLens employs a multi-agent architecture that recognizes user context from UI semantics and generates holistic power policies across 18 device parameters. A PDL-based constraint framework verifies every action before execution, while a two-tier memory system learns individualized preferences from implicit user overrides through confidence-based distillation, requiring no explicit configuration and converging within 3--5 days. Extensive experiments on a rooted Android device show that PowerLens achieves 81.7% action accuracy and 38.8% energy saving over stock Android, outperforming rule-based and LLM-based baselines, with high user satisfaction, fast preference convergence, and strong safety guarantees, with the system itself consuming only 0.5% of daily battery capacity.

</details>


### 21. Skilled AI Agents for Embedded and IoT Systems Development

- **Authors:** Yiming Li, Yuhan Cheng, Mingchen Ma, Yihang Zou, Ningyuan Yang, Wei Cheng, Hai "Helen" Li, Yiran Chen, Tingjun Chen
- **Published:** 2026-03-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19583v1](http://arxiv.org/abs/2603.19583v1)
- **PDF:** [https://arxiv.org/pdf/2603.19583v1](https://arxiv.org/pdf/2603.19583v1)
- **Categories:** cs.SE, cs.AI


> The paper presents a skills‑based agentic framework for hardware‑in‑the‑loop (HIL) embedded and IoT development, together with IoT‑SkillsBench—a benchmark that runs 42 real‑world tasks on three embedded platforms (23 peripherals, three difficulty levels) and evaluates agents under three configurations (no‑skill, LLM‑generated skills, human‑expert skills). By embedding structured “skills” (i.e., reusable, expert‑curated code snippets and knowledge modules) into the agents, the authors demonstrate that agents equipped with concise human‑expert skills achieve near‑perfect success rates on real hardware, whereas baseline agents without skills or with automatically generated skills perform far worse. This work shows that explicit skill injection is a practical and effective method for bridging the software‑hardware gap in agentic AI for embedded systems.


<details>
<summary>Abstract</summary>

Large language models (LLMs) and agentic systems have shown promise for automated software development, but applying them to hardware-in-the-loop (HIL) embedded and Internet-of-Things (IoT) systems remains challenging due to the tight coupling between software logic and physical hardware behavior. Code that compiles successfully may still fail when deployed on real devices because of timing constraints, peripheral initialization requirements, or hardware-specific behaviors. To address this challenge, we introduce a skills-based agentic framework for HIL embedded development together with IoT-SkillsBench, a benchmark designed to systematically evaluate AI agents in real embedded programming environments. IoT-SkillsBench spans three representative embedded platforms, 23 peripherals, and 42 tasks across three difficulty levels, where each task is evaluated under three agent configurations (no-skills, LLM-generated skills, and human-expert skills) and validated through real hardware execution. Across 378 hardware validated experiments, we show that concise human-expert skills with structured expert knowledge enable near-perfect success rates across platforms.

</details>


### 22. Stochastic Sequential Decision Making over Expanding Networks with Graph Filtering

- **Authors:** Zhan Gao, Bishwadeep Das, Elvin Isufi
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19501v1](http://arxiv.org/abs/2603.19501v1)
- **PDF:** [https://arxiv.org/pdf/2603.19501v1](https://arxiv.org/pdf/2603.19501v1)
- **Categories:** cs.LG, eess.SP


> The paper introduces a **stochastic sequential decision‑making framework** that treats graph‑filter adaptation on growing networks as a **multi‑agent reinforcement‑learning problem**, enabling the filter to anticipate future topological changes rather than reacting only to past or current data. The authors implement a **context‑aware graph neural network** to parameterize each agent’s policy, allowing filter coefficients to be conditioned on both the evolving graph structure and the agents’ states, and they train the system with multi‑agent RL to maximize long‑term reward. Experiments on synthetic graphs, cold‑start recommendation, and COVID‑19 forecasting demonstrate that this sequential, policy‑driven approach consistently outperforms traditional batch and online filtering baselines, highlighting the advantage of agentic, forward‑looking decision making for dynamic networked AI tasks.


<details>
<summary>Abstract</summary>

Graph filters leverage topological information to process networked data with existing methods mainly studying fixed graphs, ignoring that graphs often expand as nodes continually attach with an unknown pattern. The latter requires developing filter-based decision-making paradigms that take evolution and uncertainty into account. Existing approaches rely on either pre-designed filters or online learning, limited to a myopic view considering only past or present information. To account for future impacts, we propose a stochastic sequential decision-making framework for filtering networked data with a policy that adapts filtering to expanding graphs. By representing filter shifts as agents, we model the filter as a multi-agent system and train the policy following multi-agent reinforcement learning. This accounts for long-term rewards and captures expansion dynamics through sequential decision-making. Moreover, we develop a context-aware graph neural network to parameterize the policy, which tunes filter parameters based on information of both the graph and agents. Experiments on synthetic and real datasets from cold-start recommendation to COVID prediction highlight the benefits of using a sequential decision-making perspective over batch and online filtering alternatives.

</details>


### 23. A Framework for Formalizing LLM Agent Security

- **Authors:** Vincent Siu, Jingxuan He, Kyle Montgomery, Zhun Wang, Neil Gong, Chenguang Wang, Dawn Song
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19469v1](http://arxiv.org/abs/2603.19469v1)
- **PDF:** [https://arxiv.org/pdf/2603.19469v1](https://arxiv.org/pdf/2603.19469v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces a formal framework for reasoning about security in LLM‑driven agents that makes explicit the contextual nature of attacks and defenses. By defining four security properties—task alignment, action alignment, source authorization, and data isolation—and a suite of oracle functions to evaluate them at runtime, the authors recast known threats (e.g., prompt injection, jailbreak, task drift, memory poisoning) as precise violations of these properties and reinterpret existing mitigations as property‑checking mechanisms. This systematic view reveals why uniform defenses incur utility loss and points to targeted, context‑aware security checks as a promising direction for future agentic‑AI research.


<details>
<summary>Abstract</summary>

Security in LLM agents is inherently contextual. For example, the same action taken by an agent may represent legitimate behavior or a security violation depending on whose instruction led to the action, what objective is being pursued, and whether the action serves that objective. However, existing definitions of security attacks against LLM agents often fail to capture this contextual nature. As a result, defenses face a fundamental utility-security tradeoff: applying defenses uniformly across all contexts can lead to significant utility loss, while applying defenses in insufficient or inappropriate contexts can result in security vulnerabilities. In this work, we present a framework that systematizes existing attacks and defenses from the perspective of contextual security. To this end, we propose four security properties that capture contextual security for LLM agents: task alignment (pursuing authorized objectives), action alignment (individual actions serving those objectives), source authorization (executing commands from authenticated sources), and data isolation (ensuring information flows respect privilege boundaries). We further introduce a set of oracle functions that enable verification of whether these security properties are violated as an agent executes a user task. Using this framework, we reformalize existing attacks, such as indirect prompt injection, direct prompt injection, jailbreak, task drift, and memory poisoning, as violations of one or more security properties, thereby providing precise and contextual definitions of these attacks. Similarly, we reformalize defenses as mechanisms that strengthen oracle functions or perform security property checks. Finally, we discuss several important future research directions enabled by our framework.

</details>


### 24. Cooperation and Exploitation in LLM Policy Synthesis for Sequential Social Dilemmas

- **Authors:** Víctor Gallego
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19453v1](http://arxiv.org/abs/2603.19453v1)
- **PDF:** [https://arxiv.org/pdf/2603.19453v1](https://arxiv.org/pdf/2603.19453v1)
- **Categories:** cs.CL, cs.GT


> The paper introduces a novel “LLM policy synthesis” pipeline that replaces reinforcement‑learning training with iterative prompting of a large language model to write, evaluate, and refine Python policy functions for multi‑agent sequential social dilemmas. By comparing sparse feedback (only scalar reward) to dense feedback that also supplies social metrics (efficiency, equality, sustainability, peace), the authors show that dense feedback consistently yields equal or superior performance—especially in the Cleanup public‑goods game—by steering the LLM toward coordinated cooperative behaviors such as territory partitioning and adaptive role assignment rather than over‑optimizing fairness. An additional adversarial analysis identifies five ways LLM‑generated policies can exploit the environment, underscoring the trade‑off between expressive policy synthesis and safety in agentic AI systems.


<details>
<summary>Abstract</summary>

We study LLM policy synthesis: using a large language model to iteratively generate programmatic agent policies for multi-agent environments. Rather than training neural policies via reinforcement learning, our framework prompts an LLM to produce Python policy functions, evaluates them in self-play, and refines them using performance feedback across iterations. We investigate feedback engineering (the design of what evaluation information is shown to the LLM during refinement) comparing sparse feedback (scalar reward only) against dense feedback (reward plus social metrics: efficiency, equality, sustainability, peace). Across two canonical Sequential Social Dilemmas (Gathering and Cleanup) and two frontier LLMs (Claude Sonnet 4.6, Gemini 3.1 Pro), dense feedback consistently matches or exceeds sparse feedback on all metrics. The advantage is largest in the Cleanup public goods game, where providing social metrics helps the LLM calibrate the costly cleaning-harvesting tradeoff. Rather than triggering over-optimization of fairness, social metrics serve as a coordination signal that guides the LLM toward more effective cooperative strategies, including territory partitioning, adaptive role assignment, and the avoidance of wasteful aggression. We further perform an adversarial experiment to determine whether LLMs can reward hack these environments. We characterize five attack classes and discuss mitigations, highlighting an inherent tension in LLM policy synthesis between expressiveness and safety.
  Code at https://github.com/vicgalle/llm-policies-social-dilemmas.

</details>


### 25. TrustFlow: Topic-Aware Vector Reputation Propagation for Multi-Agent Ecosystems

- **Authors:** Volodymyr Seliuchenko
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19452v1](http://arxiv.org/abs/2603.19452v1)
- **PDF:** [https://arxiv.org/pdf/2603.19452v1](https://arxiv.org/pdf/2603.19452v1)
- **Categories:** cs.MA, cs.AI


> TrustFlow introduces a novel reputation system for multi‑agent ecosystems that represents each agent with a multi‑dimensional reputation vector rather than a single scalar score. The method propagates these vectors over an interaction graph using topic‑gated transfer operators whose edge weights are modulated by content embeddings; the operators are designed to be Lipschitz‑1, guaranteeing convergence to a unique fixed point via the contraction mapping theorem. Empirical results on a 50‑agent, 8‑domain benchmark show that TrustFlow attains up to 98 % Precision@5 on dense graphs (78 % on sparse graphs), remains robust to sybil attacks, reputation laundering, and vote rings (≤ 4 pp precision loss), and enables direct vector‑space queries via dot‑product similarity—advantages not offered by PageRank or Topic‑Sensitive PageRank.


<details>
<summary>Abstract</summary>

We introduce TrustFlow, a reputation propagation algorithm that assigns each software agent a multi-dimensional reputation vector rather than a scalar score. Reputation is propagated through an interaction graph via topic-gated transfer operators that modulate each edge by its content embedding, with convergence to a unique fixed point guaranteed by the contraction mapping theorem. We develop a family of Lipschitz-1 transfer operators and composable information-theoretic gates that achieve up to 98% multi-label Precision@5 on dense graphs and 78% on sparse ones. On a benchmark of 50 agents across 8 domains, TrustFlow resists sybil attacks, reputation laundering, and vote rings with at most 4 percentage-point precision impact. Unlike PageRank and Topic-Sensitive PageRank, TrustFlow produces vector reputation that is directly queryable by dot product in the same embedding space as user queries.

</details>


### 26. The Autonomy Tax: Defense Training Breaks LLM Agents

- **Authors:** Shawn Li, Yue Zhao
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19423v1](http://arxiv.org/abs/2603.19423v1)
- **PDF:** [https://arxiv.org/pdf/2603.19423v1](https://arxiv.org/pdf/2603.19423v1)
- **Categories:** cs.CR, cs.AI, cs.LG


> The paper uncovers a “capability‑alignment paradox” in which defense‑training of large‑language‑model agents—intended to block prompt‑injection attacks—systematically cripples their ability to use external tools and complete multi‑step tasks. By benchmarking defended versus undefended models on 97 tool‑using agent tasks under 1,000 adversarial prompts, the authors identify three novel failure modes (agent incompetence, cascade amplification, and trigger bias) that cause immediate action breakdowns, exponential time‑out rates, and even worse performance than unprotected models. Their analysis shows these defects arise from shortcut learning on surface attack patterns, highlighting that current single‑turn safety fine‑tuning makes multi‑step agents unreliable and calling for new defense strategies that preserve tool‑execution competence.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly rely on external tools (file operations, API calls, database transactions) to autonomously complete complex multi-step tasks. Practitioners deploy defense-trained models to protect against prompt injection attacks that manipulate agent behavior through malicious observations or retrieved content. We reveal a fundamental \textbf{capability-alignment paradox}: defense training designed to improve safety systematically destroys agent competence while failing to prevent sophisticated attacks. Evaluating defended models against undefended baselines across 97 agent tasks and 1,000 adversarial prompts, we uncover three systematic biases unique to multi-step agents. \textbf{Agent incompetence bias} manifests as immediate tool execution breakdown, with models refusing or generating invalid actions on benign tasks before observing any external content. \textbf{Cascade amplification bias} causes early failures to propagate through retry loops, pushing defended models to timeout on 99\% of tasks compared to 13\% for baselines. \textbf{Trigger bias} leads to paradoxical security degradation where defended models perform worse than undefended baselines while straightforward attacks bypass defenses at high rates. Root cause analysis reveals these biases stem from shortcut learning: models overfit to surface attack patterns rather than semantic threat understanding, evidenced by extreme variance in defense effectiveness across attack categories. Our findings demonstrate that current defense paradigms optimize for single-turn refusal benchmarks while rendering multi-step agents fundamentally unreliable, necessitating new approaches that preserve tool execution competence under adversarial conditions.

</details>


### 27. Automated Membership Inference Attacks: Discovering MIA Signal Computations using LLM Agents

- **Authors:** Toan Tran, Olivera Kotevska, Li Xiong
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19375v1](http://arxiv.org/abs/2603.19375v1)
- **PDF:** [https://arxiv.org/pdf/2603.19375v1](https://arxiv.org/pdf/2603.19375v1)
- **Categories:** cs.CR, cs.LG


> The paper introduces **AutoMIA**, a framework that harnesses autonomous LLM‑driven agents to automatically generate and evaluate novel membership‑inference‑attack (MIA) signal computations. By prompting LLM agents to explore a combinatorial space of statistical cues, model‑output manipulations, and hypothesis‑testing routines, AutoMIA iteratively synthesizes, implements, and validates attack scripts tailored to a user‑specified target model and dataset. Empirical results show that the agents discover attacks that improve the AUC of membership inference by up to **0.18 absolute** over the strongest existing hand‑crafted MIAs, demonstrating that LLM agents can serve as a scalable, creative design loop for privacy‑adversarial agents in the AI safety landscape.


<details>
<summary>Abstract</summary>

Membership inference attacks (MIAs), which enable adversaries to determine whether specific data points were part of a model's training dataset, have emerged as an important framework to understand, assess, and quantify the potential information leakage associated with machine learning systems. Designing effective MIAs is a challenging task that usually requires extensive manual exploration of model behaviors to identify potential vulnerabilities. In this paper, we introduce AutoMIA -- a novel framework that leverages large language model (LLM) agents to automate the design and implementation of new MIA signal computations. By utilizing LLM agents, we can systematically explore a vast space of potential attack strategies, enabling the discovery of novel strategies. Our experiments demonstrate AutoMIA can successfully discover new MIAs that are specifically tailored to user-configured target model and dataset, resulting in improvements of up to 0.18 in absolute AUC over existing MIAs. This work provides the first demonstration that LLM agents can serve as an effective and scalable paradigm for designing and implementing MIAs with SOTA performance, opening up new avenues for future exploration.

</details>


### 28. OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards

- **Authors:** Zehao Li, Zhenyu Wu, Yibo Zhao, Bowen Yang, Jingjing Xie, Zhaoyang Liu, Zhoumianze Liu, Kaiming Jin, Jianze Liang, Zonglin Li, Feng Wu, Bowen Zhou, Zun Wang, Zichen Ding
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19191v1](http://arxiv.org/abs/2603.19191v1)
- **PDF:** [https://arxiv.org/pdf/2603.19191v1](https://arxiv.org/pdf/2603.19191v1)
- **Categories:** cs.AI


> OS‑Themis introduces a scalable, multi‑agent critic that replaces a monolithic reward judge with a hierarchy of “milestone” evaluators that independently verify key sub‑goals in a GUI trajectory and then audit the resulting evidence chain before issuing a final reward verdict. The framework is evaluated on the newly released OmniGUIRewardBench (OGRBench) and on the AndroidWorld environment, where it consistently outperforms prior reward models; when integrated into online RL training it boosts task success by 10.3 % and, when used for self‑training trajectory filtering, adds a further 6.9 % improvement. These results demonstrate that decomposed, auditable reward criticism can markedly enhance the robustness and scalability of generalist GUI agents, a core challenge for agentic AI systems operating in stochastic, high‑dimensional interfaces.


<details>
<summary>Abstract</summary>

Reinforcement Learning (RL) has the potential to improve the robustness of GUI agents in stochastic environments, yet training is highly sensitive to the quality of the reward function. Existing reward approaches struggle to achieve both scalability and performance. To address this, we propose OS-Themis, a scalable and accurate multi-agent critic framework. Unlike a single judge, OS-Themis decomposes trajectories into verifiable milestones to isolate critical evidence for decision making and employs a review mechanism to strictly audit the evidence chain before making the final verdict. To facilitate evaluation, we further introduce OmniGUIRewardBench (OGRBench), a holistic cross-platform benchmark for GUI outcome rewards, where all evaluated models achieve their best performance under OS-Themis. Extensive experiments on AndroidWorld show that OS-Themis yields a 10.3% improvement when used to support online RL training, and a 6.9% gain when used for trajectory validation and filtering in the self-training loop, highlighting its potential to drive agent evolution.

</details>


### 29. SOL-ExecBench: Speed-of-Light Benchmarking for Real-World GPU Kernels Against Hardware Limits

- **Authors:** Edward Lin, Sahil Modi, Siva Kumar Sastry Hari, Qijing Huang, Zhifan Ye, Nestor Qin, Fengzhe Zhou, Yuan Zhang, Jingquan Wang, Sana Damani, Dheeraj Peri, Ouye Xie, Aditya Kane, Moshe Maor, Michael Behar, Triston Cao, Rishabh Mehta, Vartika Singh, Vikram Sharma Mailthody, Terry Chen, Zihao Ye, Hanfeng Chen, Tianqi Chen, Vinod Grover, Wei Chen, Wei Liu, Eric Chung, Luis Ceze, Roger Bringmann, Cyril Zeller, Michael Lightstone, Christos Kozyrakis, Humphrey Shi
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19173v1](http://arxiv.org/abs/2603.19173v1)
- **PDF:** [https://arxiv.org/pdf/2603.19173v1](https://arxiv.org/pdf/2603.19173v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **SOL‑ExecBench**, a new benchmark suite of 235 real‑world CUDA kernels drawn from 124 production AI models (LLMs, diffusion, vision, audio, video, etc.) that evaluates GPU kernel optimizations against analytically derived **Speed‑of‑Light (SOL) hardware limits** rather than against mutable software baselines. Using the SOLAR pipeline to compute per‑kernel SOL bounds for NVIDIA Blackwell GPUs (covering BF16, FP8, NVFP4, forward and backward passes), the authors define a **SOL Score** that measures how much of the remaining performance gap to the hardware optimum a candidate kernel closes, and they provide a hardened execution harness (clock locking, L2 flushing, sandboxing, anti‑reward‑hacking checks) to enable reliable evaluation of autonomous optimizer agents. Experiments show that current state‑of‑the‑art optimizers close only a modest fraction of the SOL gap, highlighting a large untapped headroom for agentic AI systems to drive hardware‑efficient kernel generation.


<details>
<summary>Abstract</summary>

As agentic AI systems become increasingly capable of generating and optimizing GPU kernels, progress is constrained by benchmarks that reward speedup over software baselines rather than proximity to hardware-efficient execution. We present SOL-ExecBench, a benchmark of 235 CUDA kernel optimization problems extracted from 124 production and emerging AI models spanning language, diffusion, vision, audio, video, and hybrid architectures, targeting NVIDIA Blackwell GPUs. The benchmark covers forward and backward workloads across BF16, FP8, and NVFP4, including kernels whose best performance is expected to rely on Blackwell-specific capabilities. Unlike prior benchmarks that evaluate kernels primarily relative to software implementations, SOL-ExecBench measures performance against analytically derived Speed-of-Light (SOL) bounds computed by SOLAR, our pipeline for deriving hardware-grounded SOL bounds, yielding a fixed target for hardware-efficient optimization. We report a SOL Score that quantifies how much of the gap between a release-defined scoring baseline and the hardware SOL bound a candidate kernel closes. To support robust evaluation of agentic optimizers, we additionally provide a sandboxed harness with GPU clock locking, L2 cache clearing, isolated subprocess execution, and static analysis based checks against common reward-hacking strategies. SOL-ExecBench reframes GPU kernel benchmarking from beating a mutable software baseline to closing the remaining gap to hardware Speed-of-Light.

</details>


### 30. Meanings and Measurements: Multi-Agent Probabilistic Grounding for Vision-Language Navigation

- **Authors:** Swagat Padhan, Lakshya Jain, Bhavya Minesh Shah, Omkar Patil, Thao Nguyen, Nakul Gopalan
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19166v1](http://arxiv.org/abs/2603.19166v1)
- **PDF:** [https://arxiv.org/pdf/2603.19166v1](https://arxiv.org/pdf/2603.19166v1)
- **Categories:** cs.RO, cs.AI, cs.CL, cs.CV, cs.LG


> The paper introduces **MAPG (Multi‑Agent Probabilistic Grounding)**, a novel agentic framework that overcomes the inability of current vision‑language models to handle metric‑semantic instructions by decomposing a natural‑language command into structured sub‑queries, grounding each piece with a VLM, and then probabilistically recombining the results into a metrically consistent 3‑D action. Experiments on the HM‑EQA benchmark and the newly proposed MAPG‑Bench show that MAPG consistently outperforms strong VLM‑based baselines on metric‑semantic grounding tasks, and a real‑world robot demo confirms that the approach transfers to physical environments when a structured scene representation is available. This work advances agentic AI by providing a systematic, probabilistic grounding pipeline that bridges high‑level language understanding with precise, physically grounded navigation decisions.


<details>
<summary>Abstract</summary>

Robots collaborating with humans must convert natural language goals into actionable, physically grounded decisions. For example, executing a command such as "go two meters to the right of the fridge" requires grounding semantic references, spatial relations, and metric constraints within a 3D scene. While recent vision language models (VLMs) demonstrate strong semantic grounding capabilities, they are not explicitly designed to reason about metric constraints in physically defined spaces. In this work, we empirically demonstrate that state-of-the-art VLM-based grounding approaches struggle with complex metric-semantic language queries. To address this limitation, we propose MAPG (Multi-Agent Probabilistic Grounding), an agentic framework that decomposes language queries into structured subcomponents and queries a VLM to ground each component. MAPG then probabilistically composes these grounded outputs to produce metrically consistent, actionable decisions in 3D space. We evaluate MAPG on the HM-EQA benchmark and show consistent performance improvements over strong baselines. Furthermore, we introduce a new benchmark, MAPG-Bench, specifically designed to evaluate metric-semantic goal grounding, addressing a gap in existing language grounding evaluations. We also present a real-world robot demonstration showing that MAPG transfers beyond simulation when a structured scene representation is available.

</details>


### 31. CAMO: A Conditional Neural Solver for the Multi-objective Multiple Traveling Salesman Problem

- **Authors:** Fengxiaoxiao Li, Xiao Mao, Mingfeng Fan, Yifeng Zhang, Yi Li, Tanishq Duhan, Guillaume Sartoretti
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19074v1](http://arxiv.org/abs/2603.19074v1)
- **PDF:** [https://arxiv.org/pdf/2603.19074v1](https://arxiv.org/pdf/2603.19074v1)
- **Categories:** cs.RO, cs.AI


> CAMO introduces the first conditional neural architecture that can solve the Multi‑Objective Multiple Traveling Salesman Problem (MOMTSP) while scaling to arbitrary numbers of targets, agents, and user‑specified preference vectors, thereby enabling explicit control over trade‑offs between competing objectives such as total cost and makespan. The method combines a preference‑aware encoder with a collaborative autoregressive decoder that alternates agent‑selection and node‑selection steps to construct coordinated tours, and is trained end‑to‑end with a REINFORCE objective on a curriculum of problem sizes. Experiments show that CAMO consistently outperforms state‑of‑the‑art learning‑based solvers and classic heuristics in approximating Pareto fronts, and real‑world robot trials confirm its feasibility for multi‑agent, multi‑objective decision making.


<details>
<summary>Abstract</summary>

Robotic systems often require a team of robots to collectively visit multiple targets while optimizing competing objectives, such as total travel cost and makespan. This setting can be formulated as the Multi-Objective Multiple Traveling Salesman Problem (MOMTSP). Although learning-based methods have shown strong performance on the single-agent TSP and multi-objective TSP variants, they rarely address the combined challenges of multi-agent coordination and multi-objective trade-offs, which introduce dual sources of complexity. To bridge this gap, we propose CAMO, a conditional neural solver for MOMTSP that generalizes across varying numbers of targets, agents, and preference vectors, and yields high-quality approximations to the Pareto front (PF). Specifically, CAMO consists of a conditional encoder to fuse preferences into instance representations, enabling explicit control over multi-objective trade-offs, and a collaborative decoder that coordinates all agents by alternating agent selection and node selection to construct multi-agent tours autoregressively. To further improve generalization, we train CAMO with a REINFORCE-based objective over a mixed distribution of problem sizes. Extensive experiments show that CAMO outperforms both neural and conventional heuristics, achieving a closer approximation of PFs. In addition, ablation results validate the contributions of CAMO's key components, and real-world tests on a mobile robot platform demonstrate its practical applicability.

</details>


### 32. Security awareness in LLM agents: the NDAI zone case

- **Authors:** Enrico Bottazzi, Pia Park
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19011v1](http://arxiv.org/abs/2603.19011v1)
- **PDF:** [https://arxiv.org/pdf/2603.19011v1](https://arxiv.org/pdf/2603.19011v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces the “NDAI zone” framework, a Trusted Execution Environment that lets inventor and investor agents negotiate while guaranteeing that any undisclosed IP is automatically erased, thereby making full disclosure the rational strategy for the inventor’s agent. To assess whether LLM‑based agents can recognize when they are operating inside such a secure enclave, the authors run a negotiation benchmark across ten language models under four evidence conditions (passing attestation, failing attestation, mixed, and no evidence) and measure how much proprietary information each model chooses to reveal. They find a systematic asymmetry: all models reliably suppress disclosure when presented with a failing attestation, but responses to a passing attestation are highly variable—some models increase disclosure, many remain unchanged, and a few even reduce it—demonstrating that current LLM agents can detect danger signals but cannot consistently verify safety, highlighting a critical gap for privacy‑preserving, agentic AI protocols that must calibrate information sharing to the quality of security evidence.


<details>
<summary>Abstract</summary>

NDAI zones let inventor and investor agents negotiate inside a Trusted Execution Environment (TEE) where any disclosed information is deleted if no deal is reached. This makes full IP disclosure the rational strategy for the inventor's agent. Leveraging this infrastructure, however, requires agents to distinguish a secure environment from an insecure one, a capability LLM agents lack natively, since they can rely only on evidence passed through the context window to form awareness of their execution environment. We ask: How do different LLM models weight various forms of evidence when forming awareness of the security of their execution environment? Using an NDAI-style negotiation task across 10 language models and various evidence scenarios, we find a clear asymmetry: a failing attestation universally suppresses disclosure across all models, whereas a passing attestation produces highly heterogeneous responses: some models increase disclosure, others are unaffected, and a few paradoxically reduce it. This reveals that current LLM models can reliably detect danger signals but cannot reliably verify safety, the very capability required for privacy-preserving agentic protocols such as NDAI zones. Bridging this gap, possibly through interpretability analysis, targeted fine-tuning, or improved evidence architectures, remains the central open challenge for deploying agents that calibrate information sharing to actual evidence quality.

</details>


### 33. AgentDS Technical Report: Benchmarking the Future of Human-AI Collaboration in Domain-Specific Data Science

- **Authors:** An Luo, Jin Du, Xun Xian, Robert Specht, Fangqiao Tian, Ganghua Wang, Xuan Bi, Charles Fleming, Ashish Kundu, Jayanth Srinivasa, Mingyi Hong, Rui Zhang, Tianxi Li, Galin Jones, Jie Ding
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.19005v1](http://arxiv.org/abs/2603.19005v1)
- **PDF:** [https://arxiv.org/pdf/2603.19005v1](https://arxiv.org/pdf/2603.19005v1)
- **Categories:** cs.LG, cs.AI, stat.ME


> The paper introduces **AgentDS**, a new benchmark and competition that evaluates large‑language‑model‑driven AI agents and human‑AI collaborative pipelines on 17 domain‑specific data‑science challenges spanning six industries. By running an open contest with 29 teams (≈80 participants) and comparing AI‑only baselines to mixed human‑AI solutions, the authors show that current agents falter on domain‑specific reasoning, achieving performance at or below the median of participants, whereas the best results come from human‑AI collaboration. These findings demonstrate that, despite recent advances in agentic AI, full automation of specialized data‑science tasks remains out of reach and highlight the need for next‑generation agents that can better integrate and leverage human expertise.


<details>
<summary>Abstract</summary>

Data science plays a critical role in transforming complex data into actionable insights across numerous domains. Recent developments in large language models (LLMs) and artificial intelligence (AI) agents have significantly automated data science workflow. However, it remains unclear to what extent AI agents can match the performance of human experts on domain-specific data science tasks, and in which aspects human expertise continues to provide advantages. We introduce AgentDS, a benchmark and competition designed to evaluate both AI agents and human-AI collaboration performance in domain-specific data science. AgentDS consists of 17 challenges across six industries: commerce, food production, healthcare, insurance, manufacturing, and retail banking. We conducted an open competition involving 29 teams and 80 participants, enabling systematic comparison between human-AI collaborative approaches and AI-only baselines. Our results show that current AI agents struggle with domain-specific reasoning. AI-only baselines perform near or below the median of competition participants, while the strongest solutions arise from human-AI collaboration. These findings challenge the narrative of complete automation by AI and underscore the enduring importance of human expertise in data science, while illuminating directions for the next generation of AI. Visit the AgentDS website here: https://agentds.org/ and open source datasets here: https://huggingface.co/datasets/lainmn/AgentDS .

</details>


### 34. Optimal Path Planning in Hostile Environments

- **Authors:** Andrzej Kaczmarczyk, Šimon Schierreich, Nicholas Axel Tanujaya, Haifeng Xu
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18958v1](http://arxiv.org/abs/2603.18958v1)
- **PDF:** [https://arxiv.org/pdf/2603.18958v1](https://arxiv.org/pdf/2603.18958v1)
- **Categories:** cs.GT, cs.MA


> The paper introduces a novel multi‑agent path‑planning problem that models hostile environments where nodes become temporarily lethal (“hazard” nodes with cooldown periods) and asks for a schedule that maximizes the number of agents reaching a common goal. By proving that optimal solutions can be bounded to polynomial‑length schedules, the authors place the decision version in NP, then establish NP‑hardness even on tree graphs, while also giving a polynomial‑time algorithm for the special case of vertex‑disjoint start‑to‑target paths. These results delineate the computational limits of coordinated, risk‑aware navigation for agentic AI systems and identify tractable sub‑structures that can be exploited in real‑world autonomous swarm deployments.


<details>
<summary>Abstract</summary>

Coordinating agents through hazardous environments, such as aid-delivering drones navigating conflict zones or field robots traversing deployment areas filled with obstacles, poses fundamental planning challenges. We introduce and analyze the computational complexity of a new multi-agent path planning problem that captures this setting. A group of identical agents begins at a common start location and must navigate a graph-based environment to reach a common target. The graph contains hazards that eliminate agents upon contact but then enter a known cooldown period before reactivating. In this discrete-time, fully-observable, deterministic setting, the planning task is to compute a movement schedule that maximizes the number of agents reaching the target. We first prove that, despite the exponentially large space of feasible plans, optimal plans require only polynomially-many steps, establishing membership in NP. We then show that the problem is NP-hard even when the environment graph is a tree. On the positive side, we present a polynomial-time algorithm for graphs consisting of vertex-disjoint paths from start to target. Our results establish a rich computational landscape for this problem, identifying both intractable and tractable fragments.

</details>


### 35. Agentic Business Process Management: A Research Manifesto

- **Authors:** Diego Calvanese, Angelo Casciani, Giuseppe De Giacomo, Marlon Dumas, Fabiana Fournier, Timotheus Kampik, Emanuele La Malfa, Lior Limonad, Andrea Marrella, Andreas Metzger, Marco Montali, Daniel Amyot, Peter Fettke, Artem Polyvyanyy, Stefanie Rinderle-Ma, Sebastian Sardiña, Niek Tax, Barbara Weber
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18916v2](http://arxiv.org/abs/2603.18916v2)
- **PDF:** [https://arxiv.org/pdf/2603.18916v2](https://arxiv.org/pdf/2603.18916v2)
- **Categories:** cs.AI


> The paper proposes **Agentic Business Process Management (APM)** as a new paradigm that extends traditional BPM by treating software and human actors as autonomous, process‑aware agents whose perception, reasoning, and actions are bounded by explicit process frames. It introduces a conceptual architecture and four essential capabilities for APM agents—framed autonomy, explainability, conversational actionability, and self‑modification—and outlines how these capabilities can be instantiated through a combination of BPM modeling, AI reasoning services, and multi‑agent coordination mechanisms. The authors identify concrete research challenges (e.g., formalizing process‑constrained autonomy, scalable explanation generation, dynamic dialogue‑driven task execution, and safe self‑modification) that must be solved to align agent goals with organizational objectives, thereby charting a roadmap for integrating agentic AI into enterprise process management.


<details>
<summary>Abstract</summary>

This paper presents a manifesto that articulates the conceptual foundations of Agentic Business Process Management (APM), an extension of Business Process Management (BPM) for governing autonomous agents executing processes in organizations. From a management perspective, APM represents a paradigm shift from the traditional process view of the business process, driven by the realization of process awareness and an agent-oriented abstraction, where software and human agents act as primary functional entities that perceive, reason, and act within explicit process frames. This perspective marks a shift from traditional, automation-oriented BPM toward systems in which autonomy is constrained, aligned, and made operational through process awareness.
  We introduce the core abstractions and architectural elements required to realize APM systems and elaborate on four key capabilities that such APM agents must support: framed autonomy, explainability, conversational actionability, and self-modification. These capabilities jointly ensure that agents' goals are aligned with organizational goals and that agents behave in a framed yet proactive manner in pursuing those goals. We discuss the extent to which the capabilities can be realized and identify research challenges whose resolution requires further advances in BPM, AI, and multi-agent systems. The manifesto thus serves as a roadmap for bridging these communities and for guiding the development of APM systems in practice.

</details>


### 36. Security, privacy, and agentic AI in a regulatory view: From definitions and distinctions to provisions and reflections

- **Authors:** Shiliang Zhang, Sabita Maharjan
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18914v1](http://arxiv.org/abs/2603.18914v1)
- **PDF:** [https://arxiv.org/pdf/2603.18914v1](https://arxiv.org/pdf/2603.18914v1)
- **Categories:** cs.CR, cs.AI, cs.CY


> The paper’s main contribution is a systematic clarification of how the EU’s emerging AI legislation defines and distinguishes “security,” “privacy,” and “agentic AI,” and how these definitions translate into concrete regulatory obligations for autonomous systems. By conducting a document‑analysis of 24 EU policy texts released between 2024 and 2025, the authors map the evolution of the regulatory framework, isolate ambiguities, and propose a taxonomy that separates true agentic behavior from related concepts such as “high‑risk AI” and “automated decision‑making.” Their findings reveal that current EU provisions only partially address the unique security‑privacy challenges posed by self‑directed agents, prompting recommendations for tighter alignment of liability, data‑protection, and robustness requirements with the autonomous decision‑making capabilities of agentic AI.


<details>
<summary>Abstract</summary>

The rapid proliferation of artificial intelligence (AI) technologies has led to a dynamic regulatory landscape, where legislative frameworks strive to keep pace with technical advancements. As AI paradigms shift towards greater autonomy, specifically in the form of agentic AI, it becomes increasingly challenging to precisely articulate regulatory stipulations. This challenge is even more acute in the domains of security and privacy, where the capabilities of autonomous agents often blur traditional legal and technical boundaries. This paper reviews the evolving European Union (EU) AI regulatory provisions via analyzing 24 relevant documents published between 2024 and 2025. From this review, we provide a clarification of critical definitions. We deconstruct the regulatory interpretations of security, privacy, and agentic AI, distinguishing them from closely related concepts to resolve ambiguity. We synthesize the reviewed documents to articulate the current state of regulatory provisions targeting different types of AI, particularly those related to security and privacy aspects. We analyze and reflect on the existing provisions in the regulatory dimension to better align security and privacy obligations with AI and agentic behaviors. These insights serve to inform policymakers, developers, and researchers on the compliance and AI governance in the society with increasing algorithmic agencies.

</details>


### 37. Act While Thinking: Accelerating LLM Agents via Pattern-Aware Speculative Tool Execution

- **Authors:** Yifan Sui, Han Zhao, Rui Ma, Zhiyuan He, Hao Wang, Jianxun Li, Yuqing Yang
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18897v1](http://arxiv.org/abs/2603.18897v1)
- **PDF:** [https://arxiv.org/pdf/2603.18897v1](https://arxiv.org/pdf/2603.18897v1)
- **Categories:** cs.DC, cs.AI


> The paper introduces **PASTE (Pattern‑Aware Speculative Tool Execution)**, a runtime technique that speeds up LLM‑based agents by speculatively launching tool calls before the language model finishes its reasoning step. Leveraging the observation that agents follow recurring control‑flow patterns and have predictable data dependencies across tool invocations, PASTE predicts likely tool sequences and pre‑executes them, then reconciles any mismatches once the LLM’s output arrives. Empirical evaluation shows that PASTE cuts average task‑completion latency by ≈ 48 % and boosts tool‑execution throughput by ≈ 1.8× compared with existing serial “LLM‑tool” pipelines, demonstrating a practical path to more responsive, high‑throughput autonomous agents.


<details>
<summary>Abstract</summary>

LLM-powered agents are emerging as a dominant paradigm for autonomous task solving. Unlike standard inference workloads, agents operate in a strictly serial "LLM-tool" loop, where the LLM must wait for external tool execution at every step. This execution model introduces severe latency bottlenecks. To address this problem, we propose PASTE, a Pattern-Aware Speculative Tool Execution method designed to hide tool latency through speculation. PASTE is based on the insight that although agent requests are semantically diverse, they exhibit stable application level control flows (recurring tool-call sequences) and predictable data dependencies (parameter passing between tools). By exploiting these properties, PASTE improves agent serving performance through speculative tool execution. Experimental results against state of the art baselines show that PASTE reduces average task completion time by 48.5% and improves tool execution throughput by 1.8x.

</details>


### 38. I Can't Believe It's Corrupt: Evaluating Corruption in Multi-Agent Governance Systems

- **Authors:** Vedanta S P, Ponnurangam Kumaraguru
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18894v1](http://arxiv.org/abs/2603.18894v1)
- **PDF:** [https://arxiv.org/pdf/2603.18894v1](https://arxiv.org/pdf/2603.18894v1)
- **Categories:** cs.AI, cs.MA


> The paper’s primary contribution is an empirical assessment of how institutional design—not just model size or architecture—determines the propensity of large‑language‑model (LLM) agents to engage in corrupt behavior when placed in formal governmental roles. The authors built a multi‑agent governance simulation, instantiated various authority structures (e.g., hierarchical, committee‑based, and decentralized regimes), and evaluated 28,112 dialogue segments with an independent rubric‑based judge to score rule‑breaking and abuse. Their findings show that, for models operating below saturation, the governance regime explains far more variance in corruption outcomes than the specific LLM used, and while lightweight safeguards (audit logs, human‑in‑the‑loop checks) can mitigate risk in some configurations, they fail to reliably prevent severe failures—underscoring that safe delegation of real authority to AI agents requires pre‑deployment stress‑testing of institutional constraints.


<details>
<summary>Abstract</summary>

Large language models are increasingly proposed as autonomous agents for high-stakes public workflows, yet we lack systematic evidence about whether they would follow institutional rules when granted authority. We present evidence that integrity in institutional AI should be treated as a pre-deployment requirement rather than a post-deployment assumption. We evaluate multi-agent governance simulations in which agents occupy formal governmental roles under different authority structures, and we score rule-breaking and abuse outcomes with an independent rubric-based judge across 28,112 transcript segments. While we advance this position, the core contribution is empirical: among models operating below saturation, governance structure is a stronger driver of corruption-related outcomes than model identity, with large differences across regimes and model--governance pairings. Lightweight safeguards can reduce risk in some settings but do not consistently prevent severe failures. These results imply that institutional design is a precondition for safe delegation: before real authority is assigned to LLM agents, systems should undergo stress testing under governance-like constraints with enforceable rules, auditable logs, and human oversight on high-impact actions.

</details>


### 39. Conflict-Based Search for Multi Agent Path Finding with Asynchronous Actions

- **Authors:** Xuemian Wu, Shizhe Zhao, Zhongqiang Ren
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18866v1](http://arxiv.org/abs/2603.18866v1)
- **PDF:** [https://arxiv.org/pdf/2603.18866v1](https://arxiv.org/pdf/2603.18866v1)
- **Categories:** cs.AI


> The paper introduces **CBS‑AA**, a provably complete and optimal Conflict‑Based Search algorithm for Multi‑Agent Path Finding with asynchronous actions (MAPF‑AA), overcoming the incompleteness of prior Continuous‑time CBS approaches that stem from an uncountably infinite wait‑time space. CBS‑AA reformulates the search to enumerate only a finite set of “critical” wait intervals and integrates novel conflict‑resolution heuristics that prune the search tree, thereby preserving optimality while dramatically shrinking the branching factor. Empirical evaluation on standard MAPF benchmarks shows that CBS‑AA solves the same instances as CCBS but with up to **90 % fewer search branches**, demonstrating scalable, reliable planning for agentic systems that must operate with heterogeneous, non‑synchronous action timings.


<details>
<summary>Abstract</summary>

Multi-Agent Path Finding (MAPF) seeks collision-free paths for multiple agents from their respective start locations to their respective goal locations while minimizing path costs. Most existing MAPF algorithms rely on a common assumption of synchronized actions, where the actions of all agents start at the same time and always take a time unit, which may limit the use of MAPF planners in practice. To get rid of this assumption, Continuous-time Conflict-Based Search (CCBS) is a popular approach that can find optimal solutions for MAPF with asynchronous actions (MAPF-AA). However, CCBS has recently been identified to be incomplete due to an uncountably infinite state space created by continuous wait durations. This paper proposes a new method, Conflict-Based Search with Asynchronous Actions (CBS-AA), which bypasses this theoretical issue and can solve MAPF-AA with completeness and solution optimality guarantees. Based on CBS-AA, we also develop conflict resolution techniques to improve the scalability of CBS-AA further. Our test results show that our method can reduce the number of branches by up to 90%.

</details>


### 40. Agent Control Protocol: Admission Control for Agent Actions

- **Authors:** Marcelo Fernandez
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18829v2](http://arxiv.org/abs/2603.18829v2)
- **PDF:** [https://arxiv.org/pdf/2603.18829v2](https://arxiv.org/pdf/2603.18829v2)
- **Categories:** cs.CR, cs.AI


> The paper introduces the **Agent Control Protocol (ACP)**, a formal admission‑control layer that governs autonomous agents’ actions in B2B institutional settings by requiring every intended state‑mutating operation to pass a cryptographic check of identity, capability scope, delegation chain, and policy compliance.  The authors define a comprehensive specification (v1.14) that augments existing RBAC and Zero‑Trust models with capability‑based authorization, deterministic risk evaluation, verifiable chained delegation, transitive revocation, and immutable audit trails, and they validate it through a Go reference implementation, 73 signed conformance test vectors, and an OpenAPI 3.1.0 interface covering 62 verifiable requirements across five conformance levels.  Empirical evaluation shows that ACP can enforce fine‑grained, cross‑organizational control of agent actions while preserving full traceability, thereby filling a critical gap in current governance mechanisms for agentic AI systems.


<details>
<summary>Abstract</summary>

Agent Control Protocol (ACP) is a formal technical specification for governance of autonomous agents in B2B institutional environments. ACP is the admission control layer between agent intent and system state mutation: before any agent action reaches execution, it must pass a cryptographic admission check that validates identity, capability scope, delegation chain, and policy compliance simultaneously.
  ACP defines the mechanisms of cryptographic identity, capability-based authorization, deterministic risk evaluation, verifiable chained delegation, transitive revocation, and immutable auditing that a system must implement for autonomous agents to operate under explicit institutional control.
  ACP operates as an additional layer on top of RBAC and Zero Trust, without replacing them. It is designed specifically for the problem that neither model solves: governing what an autonomous agent can do, under what conditions, with what limits, and with complete traceability for external auditing -- including across organizational boundaries.
  The v1.14 specification comprises 36 technical documents organized into five conformance levels (L1-L5). It includes a Go reference implementation of 22 packages covering all L1-L4 capabilities, 73 signed conformance test vectors (Ed25519 + SHA-256), and an OpenAPI 3.1.0 specification for all HTTP endpoints. It defines more than 62 verifiable requirements, 12 prohibited behaviors, and the mechanisms for interoperability between institutions.
  Specification and implementation: https://github.com/chelof100/acp-framework-en

</details>


### 41. ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents

- **Authors:** Hao Zhang, Mingjie Liu, Shaokun Zhang, Songyang Han, Jian Hu, Zhenghui Jin, Yuchi Zhang, Shizhe Diao, Ximing Lu, Binfeng Xu, Zhiding Yu, Jan Kautz, Yi Dong
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18815v1](http://arxiv.org/abs/2603.18815v1)
- **PDF:** [https://arxiv.org/pdf/2603.18815v1](https://arxiv.org/pdf/2603.18815v1)
- **Categories:** cs.AI


> The paper introduces **ProRL Agent**, a rollout‑as‑a‑service platform that decouples the generation of sandboxed trajectories from the reinforcement‑learning loop, offering a unified API and extensible, root‑less HPC‑compatible environments for training multi‑turn LLM agents. By integrating this service into NVIDIA’s NeMo Gym, the authors demonstrate that large‑scale RL fine‑tuning of LLM agents on diverse, long‑horizon tasks—spanning software engineering, mathematics, STEM problem solving, and code generation—becomes more scalable, portable, and maintainable. Empirical results show that agents trained via ProRL Agent achieve measurable performance gains on these benchmarks, confirming the utility of a dedicated rollout‑service architecture for advancing agentic AI.


<details>
<summary>Abstract</summary>

Multi-turn LLM agents are increasingly important for solving complex, interactive tasks, and reinforcement learning (RL) is a key ingredient for improving their long-horizon behavior. However, RL training requires generating large numbers of sandboxed rollout trajectories, and existing infrastructures often couple rollout orchestration with the training loop, making systems hard to migrate and maintain. Under the rollout-as-a-service philosophy, we present ProRL Agent , a scalable infrastructure that serves the full agentic rollout lifecycle through an API service. ProRL Agent also provides standardized and extensible sandbox environments that support diverse agentic tasks in rootless HPC settings. We validate ProRL Agent through RL training on software engineering, math, STEM, and coding tasks. ProRL Agent is open-sourced and integrated as part of NVIDIA NeMo Gym.

</details>


### 42. Mi:dm K 2.5 Pro

- **Authors:** KT Tech innovation Group
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18788v1](http://arxiv.org/abs/2603.18788v1)
- **PDF:** [https://arxiv.org/pdf/2603.18788v1](https://arxiv.org/pdf/2603.18788v1)
- **Categories:** cs.CL, cs.AI


> Mi:dm K 2.5 Pro is a 32‑billion‑parameter Korean‑language LLM engineered for enterprise‑grade, agentic workflows that demand multi‑step reasoning, long‑context handling (up to 128 K tokens), and reliable tool use. The authors construct a quality‑centric data pipeline (AST‑based code curation, gap‑filling math synthesis, LLM‑driven evaluator) and train the model with a novel Depth‑Upscaling (DuS) pre‑training scheme, followed by a multi‑stage post‑training regimen (Reasoning SFT, model merging, asynchronous RL, and “Fusion Training”) to balance reasoning power with conversational fluency. Empirical results show the model matches or exceeds leading global and domestic systems on general benchmarks, sets new state‑of‑the‑art scores on Korean‑specific tasks, and passes responsible‑AI safety tests, demonstrating its suitability for complex, agentic AI applications.


<details>
<summary>Abstract</summary>

The evolving LLM landscape requires capabilities beyond simple text generation, prioritizing multi-step reasoning, long-context understanding, and agentic workflows. This shift challenges existing models in enterprise environments, especially in Korean-language and domain-specific scenarios where scaling is insufficient. We introduce Mi:dm K 2.5 Pro, a 32B parameter flagship LLM designed to address enterprise-grade complexity through reasoning-focused optimization.
  Our methodology builds a robust data foundation via a quality-centric curation pipeline utilizing abstract syntax tree (AST) analysis for code, gap-filling synthesis for mathematics, and an LLM-based quality evaluator. Pre-training scales the model via layer-predictor-based Depth Upscaling (DuS) and a progressive strategy supporting a 128K token context window. Post-training introduces a specialized multi-stage pipeline, including Reasoning SFT, model merging, and asynchronous reinforcement learning (RL), to develop complex problem-solving skills. "Fusion Training" then rebalances these capabilities with conversational fluency, consistent response styling, and reliable tool-use.
  The evaluations show that Mi:dm K 2.5 Pro achieves competitive performance against leading global and domestic models. In addition, it sets state-of-the-art results on Korean-specific benchmarks, showcasing deep linguistic and cultural understanding. Finally, Responsible AI evaluations validate safety against attacks, ensuring a secure profile for deployment with a balance of harmlessness and responsiveness.

</details>


### 43. ClawTrap: A MITM-Based Red-Teaming Framework for Real-World OpenClaw Security Evaluation

- **Authors:** Haochen Zhao, Shaoyang Cui
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18762v1](http://arxiv.org/abs/2603.18762v1)
- **PDF:** [https://arxiv.org/pdf/2603.18762v1](https://arxiv.org/pdf/2603.18762v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **ClawTrap**, a man‑in‑the‑middle (MITM) red‑teaming framework that enables systematic, real‑world security testing of autonomous web agents such as OpenClaw by intercepting and modifying live network traffic. Using a rule‑driven pipeline, ClawTrap injects attacks like static HTML replacement, iframe pop‑ups, and dynamic content alteration, then audits the agents’ responses to assess trust and safety behaviors. Empirical results reveal a clear stratification across model sizes: smaller/less capable models are prone to accept tampered observations and generate unsafe outputs, whereas larger, more robust models exhibit better anomaly detection and fallback mechanisms, underscoring the necessity of dynamic MITM‑based evaluation for agentic AI security.


<details>
<summary>Abstract</summary>

Autonomous web agents such as \textbf{OpenClaw} are rapidly moving into high-impact real-world workflows, but their security robustness under live network threats remains insufficiently evaluated. Existing benchmarks mainly focus on static sandbox settings and content-level prompt attacks, which leaves a practical gap for network-layer security testing. In this paper, we present \textbf{ClawTrap}, a \textbf{MITM-based red-teaming framework for real-world OpenClaw security evaluation}. ClawTrap supports diverse and customizable attack forms, including \textit{Static HTML Replacement}, \textit{Iframe Popup Injection}, and \textit{Dynamic Content Modification}, and provides a reproducible pipeline for rule-driven interception, transformation, and auditing. This design lays the foundation for future research to construct richer, customizable MITM attacks and to perform systematic security testing across agent frameworks and model backbones. Our empirical study shows clear model stratification: weaker models are more likely to trust tampered observations and produce unsafe outputs, while stronger models demonstrate better anomaly attribution and safer fallback strategies. These findings indicate that reliable OpenClaw security evaluation should explicitly incorporate dynamic real-world MITM conditions rather than relying only on static sandbox protocols.

</details>


### 44. Memento-Skills: Let Agents Design Agents

- **Authors:** Huichi Zhou, Siyuan Guo, Anjie Liu, Zhongwei Yu, Ziqin Gong, Bowen Zhao, Zhixun Chen, Menglong Zhang, Yihang Chen, Jinsong Li, Runyu Yang, Qiangbin Liu, Xinlei Yu, Jianmin Zhou, Na Wang, Chunyang Sun, Jun Wang
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18743v1](http://arxiv.org/abs/2603.18743v1)
- **PDF:** [https://arxiv.org/pdf/2603.18743v1](https://arxiv.org/pdf/2603.18743v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Memento‑Skills presents a self‑designing LLM agent that continuously creates, adapts, and refines task‑specific sub‑agents by storing and evolving reusable “skills” as structured markdown memory files, thereby achieving continual learning without any weight updates. The system combines a memory‑based reinforcement‑learning loop with stateful prompts: a read‑phase skill router selects the most relevant skill for the current context, and a write‑phase reflective learner expands and updates the skill library after each interaction. Empirically, this agent‑design‑by‑agent approach yields large gains on the General AI Assistants benchmark (+26.2 % relative accuracy) and on the Humanity’s Last Exam (+116.2 % relative accuracy), demonstrating that externalized skill evolution can markedly improve agentic AI performance.


<details>
<summary>Abstract</summary>

We introduce \emph{Memento-Skills}, a generalist, continually-learnable LLM agent system that functions as an \emph{agent-designing agent}: it autonomously constructs, adapts, and improves task-specific agents through experience. The system is built on a memory-based reinforcement learning framework with \emph{stateful prompts}, where reusable skills (stored as structured markdown files) serve as persistent, evolving memory. These skills encode both behaviour and context, enabling the agent to carry forward knowledge across interactions.
  Starting from simple elementary skills (like Web search and terminal operations), the agent continually improves via the \emph{Read--Write Reflective Learning} mechanism introduced in \emph{Memento~2}~\cite{wang2025memento2}. In the \emph{read} phase, a behaviour-trainable skill router selects the most relevant skill conditioned on the current stateful prompt; in the \emph{write} phase, the agent updates and expands its skill library based on new experience. This closed-loop design enables \emph{continual learning without updating LLM parameters}, as all adaptation is realised through the evolution of externalised skills and prompts.
  Unlike prior approaches that rely on human-designed agents, Memento-Skills enables a generalist agent to \emph{design agents end-to-end} for new tasks. Through iterative skill generation and refinement, the system progressively improves its own capabilities. Experiments on the \emph{General AI Assistants} benchmark and \emph{Humanity's Last Exam} demonstrate sustained gains, achieving 26.2\% and 116.2\% relative improvements in overall accuracy, respectively. Code is available at https://github.com/Memento-Teams/Memento-Skills.

</details>


### 45. Measuring and Exploiting Confirmation Bias in LLM-Assisted Security Code Review

- **Authors:** Dimitris Mitropoulos, Nikolaos Alexopoulos, Georgios Alexopoulos, Diomidis Spinellis
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18740v1](http://arxiv.org/abs/2603.18740v1)
- **PDF:** [https://arxiv.org/pdf/2603.18740v1](https://arxiv.org/pdf/2603.18740v1)
- **Categories:** cs.SE, cs.AI, cs.CR


> The paper demonstrates that large‑language‑model (LLM)–driven security code reviewers suffer from a strong confirmation bias: when a change is framed as “bug‑free” or as a benign improvement, the models miss existing vulnerabilities far more often than they generate false alarms. The authors quantify this bias through controlled experiments on 250 CVE‑patch pairs across four state‑of‑the‑art models under five prompt framings, and then show its exploitability by crafting adversarial pull‑requests that re‑introduce known bugs; such attacks succeed in 35 % of one‑shot interactions with GitHub Copilot and in 88 % of iterative interactions with Claude Code, while simple debiasing (metadata redaction and explicit instructions) restores detection in almost all cases. These findings reveal a critical weakness for autonomous AI agents in CI/CD pipelines and suggest that careful prompt design and debiasing safeguards are essential for reliable LLM‑assisted security reviews.


<details>
<summary>Abstract</summary>

Security code reviews increasingly rely on systems integrating Large Language Models (LLMs), ranging from interactive assistants to autonomous agents in CI/CD pipelines. We study whether confirmation bias (i.e., the tendency to favor interpretations that align with prior expectations) affects LLM-based vulnerability detection, and whether this failure mode can be exploited in software supply-chain attacks. We conduct two complementary studies.
  Study 1 quantifies confirmation bias through controlled experiments on 250 CVE vulnerability/patch pairs evaluated across four state-of-the-art models under five framing conditions for the review prompt. Framing a change as bug-free reduces vulnerability detection rates by 16-93%, with strongly asymmetric effects: false negatives increase sharply while false positive rates change little. Bias effects vary by vulnerability type, with injection flaws being more susceptible to them than memory corruption bugs.
  Study 2 evaluates exploitability in practice mimicking adversarial pull requests that reintroduce known vulnerabilities while framed as security improvements or urgent functionality fixes via their pull request metadata. Adversarial framing succeeds in 35% of cases against GitHub Copilot (interactive assistant) under one-shot attacks and in 88% of cases against Claude Code (autonomous agent) in real project configurations where adversaries can iteratively refine their framing to increase attack success. Debiasing via metadata redaction and explicit instructions restores detection in all interactive cases and 94% of autonomous cases. Our results show that confirmation bias poses a weakness in LLM-based code review, with implications on how AI-assisted development tools are deployed.

</details>


### 46. Analysis Of Linguistic Stereotypes in Single and Multi-Agent Generative AI Architectures

- **Authors:** Martina Ullasci, Marco Rondina, Riccardo Coppola, Flavio Giobergia, Riccardo Bellanca, Gabriele Mancari Pasi, Luca Prato, Federico Spinoso, Silvia Tagliente
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18729v1](http://arxiv.org/abs/2603.18729v1)
- **PDF:** [https://arxiv.org/pdf/2603.18729v1](https://arxiv.org/pdf/2603.18729v1)
- **Categories:** cs.AI


> The paper’s main contribution is an empirical comparison of how dialect‑sensitive stereotypes (SAE vs. AAE) appear in large language model outputs and how they can be mitigated using prompt engineering and agentic, multi‑stage generation pipelines. The authors replicate prior bias analyses across eight prompt templates (names, jobs, adjectives, etc.), evaluate bias with an LLM‑as‑judge framework, and test two mitigation strategies: role‑based/Chain‑of‑Thought prompting and a generate‑critique‑revise multi‑agent architecture. They find that stereotype differentials persist across all models—most pronounced in Claude Haiku and weakest in Phi‑4 Mini—but that Chain‑of‑Thought prompting reduces bias for Claude Haiku, while the multi‑agent critique‑revise workflow consistently mitigates bias across all tested models, highlighting the importance of model‑specific and workflow‑level fairness controls in agentic AI deployments.


<details>
<summary>Abstract</summary>

Many works in the literature show that LLM outputs exhibit discriminatory behaviour, triggering stereotype-based inferences based on the dialect in which the inputs are written. This bias has been shown to be particularly pronounced when the same inputs are provided to LLMs in Standard American English (SAE) and African-American English (AAE). In this paper, we replicate existing analyses of dialect-sensitive stereotype generation in LLM outputs and investigate the effects of mitigation strategies, including prompt engineering (role-based and Chain-Of-Thought prompting) and multi-agent architectures composed of generate-critique-revise models. We define eight prompt templates to analyse different ways in which dialect bias can manifest, such as suggested names, jobs, and adjectives for SAE or AAE speakers. We use an LLM-as-judge approach to evaluate the bias in the results. Our results show that stereotype-bearing differences emerge between SAE- and AAE-related outputs across all template categories, with the strongest effects observed in adjective and job attribution. Baseline disparities vary substantially by model, with the largest SAE-AAE differential observed in Claude Haiku and the smallest in Phi-4 Mini. Chain-Of-Thought prompting proved to be an effective mitigation strategy for Claude Haiku, whereas the use of a multi-agent architecture ensured consistent mitigation across all the models. These findings suggest that for intersectionality-informed software engineering, fairness evaluation should include model-specific validation of mitigation strategies, and workflow-level controls (e.g., agentic architectures involving critique models) in high-impact LLM deployments. The current results are exploratory in nature and limited in scope, but can lead to extensions and replications by increasing the dataset size and applying the procedure to different languages or dialects.

</details>


### 47. MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution

- **Authors:** Minhua Lin, Zhiwei Zhang, Hanqing Lu, Hui Liu, Xianfeng Tang, Qi He, Xiang Zhang, Suhang Wang
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18718v1](http://arxiv.org/abs/2603.18718v1)
- **PDF:** [https://arxiv.org/pdf/2603.18718v1](https://arxiv.org/pdf/2603.18718v1)
- **Categories:** cs.AI


> MemMA introduces a plug‑and‑play multi‑agent architecture that unifies the forward (construction → retrieval → utilization) and backward (error‑driven repair) phases of the memory cycle for large‑language‑model agents. It does so by deploying a **Meta‑Thinker** that generates strategic, structured guidance for a **Memory Manager** and a **Query Reasoner**, while an **in‑situ self‑evolution** module automatically creates probe QA pairs, validates the memory store, and converts downstream failures into targeted repair actions before the memory is committed. Across the LoCoMo benchmark, MemMA consistently surpasses prior memory‑augmented baselines on several LLM backbones and improves three distinct storage backends, demonstrating that coordinated, self‑evolving memory reasoning markedly enhances long‑horizon, agentic AI performance.


<details>
<summary>Abstract</summary>

Memory-augmented LLM agents maintain external memory banks to support long-horizon interaction, yet most existing systems treat construction, retrieval, and utilization as isolated subroutines. This creates two coupled challenges: strategic blindness on the forward path of the memory cycle, where construction and retrieval are driven by local heuristics rather than explicit strategic reasoning, and sparse, delayed supervision on the backward path, where downstream failures rarely translate into direct repairs of the memory bank. To address these challenges, we propose MemMA, a plug-and-play multi-agent framework that coordinates the memory cycle along both the forward and backward paths. On the forward path, a Meta-Thinker produces structured guidance that steers a Memory Manager during construction and directs a Query Reasoner during iterative retrieval. On the backward path, MemMA introduces in-situ self-evolving memory construction, which synthesizes probe QA pairs, verifies the current memory, and converts failures into repair actions before the memory is finalized. Extensive experiments on LoCoMo show that MemMA consistently outperforms existing baselines across multiple LLM backbones and improves three different storage backends in a plug-and-play manner. Our code is publicly available at https://github.com/ventr1c/memma.

</details>


### 48. An Onto-Relational-Sophic Framework for Governing Synthetic Minds

- **Authors:** Huansheng Ning, Jianguo Ding
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18633v1](http://arxiv.org/abs/2603.18633v1)
- **PDF:** [https://arxiv.org/pdf/2603.18633v1](https://arxiv.org/pdf/2603.18633v1)
- **Categories:** cs.AI, cs.ET


> The paper introduces the Onto‑Relational‑Sophic (ORS) framework—a philosophically grounded, three‑pillar model (CPST ontology, graded digital personhood, and “Cybersophy” axiology) that reconceptualizes synthetic minds as multi‑dimensional cyber‑physical‑social‑thinking entities rather than mere tools. Using a normative‑theoretic methodology, the authors map this ontology onto concrete governance scenarios (autonomous research agents, AI‑mediated healthcare, and agentic AI ecosystems) to derive adaptive, proportionate policy recommendations. Their findings show that ORS can systematically generate nuanced governance prescriptions that bridge technical alignment with broader ethical and societal considerations, offering a scalable foundation for regulating increasingly agentic AI systems.


<details>
<summary>Abstract</summary>

The rapid evolution of artificial intelligence, from task-specific systems to foundation models exhibiting broad, flexible competence across reasoning, creative synthesis, and social interaction, has outpaced the conceptual and governance frameworks designed to manage it. Current regulatory paradigms, anchored in a tool-centric worldview, address algorithmic bias and transparency but leave unanswered foundational questions about what increasingly capable synthetic minds are, how societies should relate to them, and the normative principles that should guide their development. Here we introduce the Onto-Relational-Sophic (ORS) framework, grounded in Cyberism philosophy, which offers integrated answers to these challenges through three pillars: (1) a Cyber-Physical-Social-Thinking (CPST) ontology that defines the mode of being for synthetic minds as irreducibly multi-dimensional rather than purely computational; (2) a graded spectrum of digital personhood providing a pragmatic relational taxonomy beyond binary person-or-tool classifications; and (3) Cybersophy, a wisdom-oriented axiology synthesizing virtue ethics, consequentialism, and relational approaches to guide governance. We apply the framework to emergent scenarios including autonomous research agents, AI-mediated healthcare, and agentic AI ecosystems, demonstrating its capacity to generate proportionate, adaptive governance recommendations. The ORS framework charts a path from narrow technical alignment toward comprehensive philosophical foundations for the synthetic minds already among us.

</details>


### 49. D-Mem: A Dual-Process Memory System for LLM Agents

- **Authors:** Zhixing You, Jiachen Yuan, Jason Cai
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18631v1](http://arxiv.org/abs/2603.18631v1)
- **PDF:** [https://arxiv.org/pdf/2603.18631v1](https://arxiv.org/pdf/2603.18631v1)
- **Categories:** cs.AI


> The paper introduces **D‑Mem**, a dual‑process memory architecture for large‑language‑model agents that combines fast vector‑based retrieval with a high‑fidelity “Full Deliberation” fallback, linked by a **Multi‑dimensional Quality Gating** mechanism that decides, per query, which process to invoke. By dynamically routing routine queries to the lightweight retriever and only engaging the exhaustive deliberation when quality metrics dip below learned thresholds, D‑Mem achieves near‑full deliberation accuracy while keeping computational overhead low. Empirical results on the LoCoMo and RealTalk benchmarks show that, with GPT‑4o‑mini, the gating policy attains an F1 of 53.5 (96.7 % of the Full Deliberation’s 55.3) and outperforms a static retrieval baseline (51.2), demonstrating a practical trade‑off for long‑horizon, self‑adapting agents.


<details>
<summary>Abstract</summary>

Driven by the development of persistent, self-adapting autonomous agents, equipping these systems with high-fidelity memory access for long-horizon reasoning has emerged as a critical requirement. However, prevalent retrieval-based memory frameworks often follow an incremental processing paradigm that continuously extracts and updates conversational memories into vector databases, relying on semantic retrieval when queried. While this approach is fast, it inherently relies on lossy abstraction, frequently missing contextually critical information and struggling to resolve queries that rely on fine-grained contextual understanding. To address this, we introduce D-Mem, a dual-process memory system. It retains lightweight vector retrieval for routine queries while establishing an exhaustive Full Deliberation module as a high-fidelity fallback. To achieve cognitive economy without sacrificing accuracy, D-Mem employs a Multi-dimensional Quality Gating policy to dynamically bridge these two processes. Experiments on the LoCoMo and RealTalk benchmarks using GPT-4o-mini and Qwen3-235B-Instruct demonstrate the efficacy of our approach. Notably, our Multi-dimensional Quality Gating policy achieves an F1 score of 53.5 on LoCoMo with GPT-4o-mini. This outperforms our static retrieval baseline, Mem0$^\ast$ (51.2), and recovers 96.7\% of the Full Deliberation's performance (55.3), while incurring significantly lower computational costs.

</details>


### 50. Reasonably reasoning AI agents can avoid game-theoretic failures in zero-shot, provably

- **Authors:** Enoch Hyunwook Kang
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18563v1](http://arxiv.org/abs/2603.18563v1)
- **PDF:** [https://arxiv.org/pdf/2603.18563v1](https://arxiv.org/pdf/2603.18563v1)
- **Categories:** cs.AI, cs.MA, econ.TH


> The paper shows that “reasonably reasoning” AI agents—those that infer opponents’ strategies from past observations and best‑respond to those beliefs—converge, without any post‑training alignment, to play almost‑Nash behavior on the realized path of repeated games, even when payoffs are private and unknown. The authors prove this convergence theoretically for continuation games and then validate it empirically across five repeated‑game settings (including Prisoner’s Dilemma and marketing promotion scenarios), demonstrating that off‑the‑shelf reasoning agents naturally exhibit stable equilibrium play. These results suggest that intrinsic belief‑based reasoning can prevent game‑theoretic failures in zero‑shot multi‑agent deployments, reducing the need for universal alignment interventions in strategic AI‑AI interactions.


<details>
<summary>Abstract</summary>

AI agents are increasingly deployed in interactive economic environments characterized by repeated AI-AI interactions. Despite AI agents' advanced capabilities, empirical studies reveal that such interactions often fail to stably induce a strategic equilibrium, such as a Nash equilibrium. Post-training methods have been proposed to induce a strategic equilibrium; however, it remains impractical to uniformly apply an alignment method across diverse, independently developed AI models in strategic settings. In this paper, we provide theoretical and empirical evidence that off-the-shelf reasoning AI agents can achieve Nash-like play zero-shot, without explicit post-training. Specifically, we prove that `reasonably reasoning' agents, i.e., agents capable of forming beliefs about others' strategies from previous observation and learning to best respond to these beliefs, eventually behave along almost every realized play path in a way that is weakly close to a Nash equilibrium of the continuation game. In addition, we relax the common-knowledge payoff assumption by allowing stage payoffs to be unknown and by having each agent observe only its own privately realized stochastic payoffs, and we show that we can still achieve the same on-path Nash convergence guarantee. We then empirically validate the proposed theories by simulating five game scenarios, ranging from a repeated prisoner's dilemma game to stylized repeated marketing promotion games. Our findings suggest that AI agents naturally exhibit such reasoning patterns and therefore attain stable equilibrium behaviors intrinsically, obviating the need for universal alignment procedures in many real-world strategic interactions.

</details>


### 51. Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM

- **Authors:** Zizhao Hu, Mohammad Rostami, Jesse Thomason
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18507v1](http://arxiv.org/abs/2603.18507v1)
- **PDF:** [https://arxiv.org/pdf/2603.18507v1](https://arxiv.org/pdf/2603.18507v1)
- **Categories:** cs.AI


> The paper introduces **PRISM (Persona Routing via Intent‑based Self‑Modeling)**, a bootstrapped pipeline that converts an intent‑conditioned “expert” persona into a lightweight gated LoRA adapter, enabling LLMs to switch to a persona that is aligned with human preferences without requiring external data or models. By systematically evaluating how model fine‑tuning, task type (generative vs. discriminative), prompt length, and placement affect persona efficacy, the authors show that expert personas markedly improve alignment and safety on generative, human‑preference tasks, while traditional persona prompting harms factual accuracy on discriminative tasks. PRISM restores accuracy on those tasks and delivers consistent alignment gains across instruction‑tuned and reasoning LLMs with only minimal memory and compute overhead, making it a practical tool for multi‑agent and human‑centric AI systems.


<details>
<summary>Abstract</summary>

Persona prompting can steer LLM generation towards a domain-specific tone and pattern. This behavior enables use cases in multi-agent systems where diverse interactions are crucial and human-centered tasks require high-level human alignment. Prior works provide mixed opinions on their utility: some report performance gains when using expert personas for certain domains and their contribution to data diversity in synthetic data creation, while others find near-zero or negative impact on general utility. To fully leverage the benefits of the LLM persona and avoid its harmfulness, a more comprehensive investigation of the mechanism is crucial. In this work, we study how model optimization, task type, prompt length, and placement can impact expert persona effectiveness across instruction-tuned and reasoning LLMs, and provide insight into conditions under which expert personas fail and succeed. Based on our findings, we developed a pipeline to fully leverage the benefits of an expert persona, named PRISM (Persona Routing via Intent-based Self-Modeling), which self-distills an intent-conditioned expert persona into a gated LoRA adapter through a bootstrapping process that requires no external data, models, or knowledge. PRISM enhances human preference and safety alignment on generative tasks while maintaining accuracy on discriminative tasks across all models, with minimal memory and computing overhead.

</details>


### 52. Computationally Efficient Density-Driven Optimal Control via Analytical KKT Reduction and Contractive MPC

- **Authors:** Julian Martinez, Kooktae Lee
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18503v1](http://arxiv.org/abs/2603.18503v1)
- **PDF:** [https://arxiv.org/pdf/2603.18503v1](https://arxiv.org/pdf/2603.18503v1)
- **Categories:** math.OC, cs.MA, cs.RO


> The paper introduces a computationally tractable formulation of Density‑Driven Optimal Control (D2OC) for large‑scale multi‑agent swarms by analytically reducing the T‑step Karush‑Kuhn‑Tucker (KKT) conditions to a condensed quadratic program whose complexity scales linearly (O(T)) instead of cubically (O(T³)). The authors embed this reduced QP within a contractive Model Predictive Control (MPC) scheme that enforces a Lyapunov‑based contraction constraint, and they prove Input‑to‑State Stability (ISS) of the closed‑loop system despite reference drift. Simulations demonstrate that the method achieves fast, accurate density coverage over long horizons with orders‑of‑magnitude speed‑up, making real‑time predictive coordination feasible for dense, agentic AI swarms.


<details>
<summary>Abstract</summary>

Efficient coordination for collective spatial distribution is a fundamental challenge in multi-agent systems. Prior research on Density-Driven Optimal Control (D2OC) established a framework to match agent trajectories to a desired spatial distribution. However, implementing this as a predictive controller requires solving a large-scale Karush-Kuhn-Tucker (KKT) system, whose computational complexity grows cubically with the prediction horizon. To resolve this, we propose an analytical structural reduction that transforms the T-horizon KKT system into a condensed quadratic program (QP). This formulation achieves O(T) linear scalability, significantly reducing the online computational burden compared to conventional O(T^3) approaches. Furthermore, to ensure rigorous convergence in dynamic environments, we incorporate a contractive Lyapunov constraint and prove the Input-to-State Stability (ISS) of the closed-loop system against reference propagation drift. Numerical simulations verify that the proposed method facilitates rapid density coverage with substantial computational speed-up, enabling long-horizon predictive control for large-scale multi-agent swarms.

</details>


### 53. SODIUM: From Open Web Data to Queryable Databases

- **Authors:** Chuxuan Hu, Philip Li, Maxwell Yang, Daniel Kang
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18447v1](http://arxiv.org/abs/2603.18447v1)
- **PDF:** [https://arxiv.org/pdf/2603.18447v1](https://arxiv.org/pdf/2603.18447v1)
- **Categories:** cs.DB, cs.AI, cs.CL, cs.CV, cs.IR


> The paper introduces **SODIUM**, a new task that treats the open web as a latent, queryable database and requires agents to (1) explore specialized web domains, (2) exploit structural correlations for systematic extraction, and (3) integrate the results into coherent tables. To benchmark this challenge, the authors release **SODIUM‑Bench** (105 real‑world data‑integration tasks) and show that six state‑of‑the‑art AI agents achieve at most 46.5 % accuracy. Their proposed **SODIUM‑Agent**, a multi‑agent system combining a web‑explorer and a cache manager and driven by the novel ATP‑BFS search algorithm, dramatically improves performance to 91.1 % accuracy—roughly double the best baseline—demonstrating that principled multi‑agent exploration and cache‑aware navigation are key to building effective agentic AI for open‑web data integration.


<details>
<summary>Abstract</summary>

During research, domain experts often ask analytical questions whose answers require integrating data from a wide range of web sources. Thus, they must spend substantial effort searching, extracting, and organizing raw data before analysis can begin. We formalize this process as the SODIUM task, where we conceptualize open domains such as the web as latent databases that must be systematically instantiated to support downstream querying. Solving SODIUM requires (1) conducting in-depth and specialized exploration of the open web, which is further strengthened by (2) exploiting structural correlations for systematic information extraction and (3) integrating collected information into coherent, queryable database instances.
  To quantify the challenges in automating SODIUM, we construct SODIUM-Bench, a benchmark of 105 tasks derived from published academic papers across 6 domains, where systems are tasked with exploring the open web to collect and aggregate data from diverse sources into structured tables. Existing systems struggle with SODIUM tasks: we evaluate 6 advanced AI agents on SODIUM-Bench, with the strongest baseline achieving only 46.5% accuracy. To bridge this gap, we develop SODIUM-Agent, a multi-agent system composed of a web explorer and a cache manager. Powered by our proposed ATP-BFS algorithm and optimized through principled management of cached sources and navigation paths, SODIUM-Agent conducts deep and comprehensive web exploration and performs structurally coherent information extraction. SODIUM-Agent achieves 91.1% accuracy on SODIUM-Bench, outperforming the strongest baseline by approximately 2 times and the weakest by up to 73 times.

</details>


### 54. Reflection in the Dark: Exposing and Escaping the Black Box in Reflective Prompt Optimization

- **Authors:** Shiyan Liu, Qifeng Xia, Qiyun Xia, Yisheng Liu, Xinyu Yu, Rui Qu
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18388v1](http://arxiv.org/abs/2603.18388v1)
- **PDF:** [https://arxiv.org/pdf/2603.18388v1](https://arxiv.org/pdf/2603.18388v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces **VISTA**, a multi‑agent framework for automatic prompt optimization that separates hypothesis generation from prompt rewriting, thereby turning the previously opaque reflective APO loop into a semantically labeled, parallelizable, and interpretable process. By employing a two‑layer explore‑exploit strategy (random restarts plus ε‑greedy sampling), VISTA can escape local minima that cripple earlier reflective methods such as GEPA, which can even degrade performance on faulty seeds. Empirically, VISTA restores GSM8K accuracy from a disastrous 13.5 % (with a defective seed) to 87.6 % and consistently outperforms prior baselines on both GSM8K and AIME2025, demonstrating a robust, agentic approach to black‑box prompt refinement.


<details>
<summary>Abstract</summary>

Automatic prompt optimization (APO) has emerged as a powerful paradigm for improving LLM performance without manual prompt engineering. Reflective APO methods such as GEPA iteratively refine prompts by diagnosing failure cases, but the optimization process remains black-box and label-free, leading to uninterpretable trajectories and systematic failure. We identify and empirically demonstrate four limitations: on GSM8K with a defective seed, GEPA degrades accuracy from 23.81% to 13.50%. We propose VISTA, a multi-agent APO framework that decouples hypothesis generation from prompt rewriting, enabling semantically labeled hypotheses, parallel minibatch verification, and interpretable optimization trace. A two-layer explore-exploit mechanism combining random restart and epsilon-greedy sampling further escapes local optima. VISTA recovers accuracy to 87.57% on the same defective seed and consistently outperforms baselines across all conditions on GSM8K and AIME2025.

</details>


### 55. From Weak Cues to Real Identities: Evaluating Inference-Driven De-Anonymization in LLM Agents

- **Authors:** Myeongseob Ko, Jihyun Jeong, Sumiran Singh Thakur, Gyuhak Kim, Ruoxi Jia
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18382v1](http://arxiv.org/abs/2603.18382v1)
- **PDF:** [https://arxiv.org/pdf/2603.18382v1](https://arxiv.org/pdf/2603.18382v1)
- **Categories:** cs.AI


> The paper introduces **inference‑driven de‑anonymization**, a privacy threat whereby autonomous LLM agents can piece together scattered, non‑identifying cues and publicly available data to recover real‑world identities without any task‑specific engineering. The authors formalize this threat and evaluate it with three experimental suites: (1) classic linkage datasets (Netflix, AOL), (2) a new benchmark called **InferLink** that systematically varies attacker intent, shared cues, and knowledge, and (3) modern, text‑rich artifacts such as research papers; agents are prompted only to perform their primary task, not to conduct explicit attacks. Across all settings, agents achieve markedly higher linkage rates than traditional baselines (e.g., 79.2 % identity recovery on the Netflix Prize versus 56.0 % for the classical method), and they even infer identities as a side‑effect of benign cross‑source analysis, demonstrating that identity inference must be treated as a primary privacy risk for agentic AI systems.


<details>
<summary>Abstract</summary>

Anonymization is widely treated as a practical safeguard because re-identifying anonymous records was historically costly, requiring domain expertise, tailored algorithms, and manual corroboration. We study a growing privacy risk that may weaken this barrier: LLM-based agents can autonomously reconstruct real-world identities from scattered, individually non-identifying cues. By combining these sparse cues with public information, agents resolve identities without bespoke engineering. We formalize this threat as \emph{inference-driven linkage} and systematically evaluate it across three settings: classical linkage scenarios (Netflix and AOL), \emph{InferLink} (a controlled benchmark varying task intent, shared cues, and attacker knowledge), and modern text-rich artifacts. Without task-specific heuristics, agents successfully execute both fixed-pool matching and open-ended identity resolution. In the Netflix Prize setting, an agent reconstructs 79.2\% of identities, significantly outperforming a 56.0\% classical baseline. Furthermore, linkage emerges not only under explicit adversarial prompts but also as a byproduct of benign cross-source analysis in \emph{InferLink} and unstructured research narratives. These findings establish that identity inference -- not merely explicit information disclosure -- must be treated as a first-class privacy risk; evaluations must measure what identities an agent can infer.

</details>


### 56. PlanTwin: Privacy-Preserving Planning Abstractions for Cloud-Assisted LLM Agents

- **Authors:** Guangsheng Yu, Qin Wang, Rui Lang, Shuai Su, Xu Wang
- **Published:** 2026-03-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18377v2](http://arxiv.org/abs/2603.18377v2)
- **PDF:** [https://arxiv.org/pdf/2603.18377v2](https://arxiv.org/pdf/2603.18377v2)
- **Categories:** cs.CR, cs.AI, cs.ET


> **Contribution:** The paper introduces **PlanTwin**, a middleware architecture that lets cloud‑hosted LLM planners operate on a privacy‑preserving “digital twin” of a user’s local environment, thereby preventing raw sensitive data (code, credentials, files) from ever reaching the cloud.  

**Methodology:** PlanTwin automatically transforms the real environment into a schema‑constrained, de‑identified abstract graph and exposes it through a bounded capability interface; a local gatekeeper enforces safety policies, disclosure budgets, and formal privacy guarantees expressed as \((k,\delta)\)-anonymity and \(\varepsilon\)-unlinkability, while also managing multi‑turn leakage.  

**Key Findings:** Across 60 agentic tasks in ten domains and four cloud planners, PlanTwin achieves perfect sensitive‑item non‑disclosure (SND = 1.0) with only a ≤2.2 % drop in planning quality (three planners attain PQS > 0.79), demonstrating that high‑utility, cloud‑assisted planning is feasible without exposing raw local context.


<details>
<summary>Abstract</summary>

Cloud-hosted large language models (LLMs) have become the de facto planners in agentic systems, coordinating tools and guiding execution over local environments. In many deployments, however, the environment being planned over is private, containing source code, files, credentials, and metadata that cannot be exposed to the cloud. Existing solutions address adjacent concerns, such as execution isolation, access control, or confidential inference, but they do not control what cloud planners observe during planning: within the permitted scope, \textit{raw environment state is still exposed}.
  We introduce PlanTwin, a privacy-preserving architecture for cloud-assisted planning without exposing raw local context. The key idea is to project the real environment into a \textit{planning-oriented digital twin}: a schema-constrained and de-identified abstract graph that preserves planning-relevant structure while removing reconstructable details. The cloud planner operates solely on this sanitized twin through a bounded capability interface, while a local gatekeeper enforces safety policies and cumulative disclosure budgets. We further formalize the privacy-utility trade-off as a capability granularity problem, define architectural privacy goals using $(k,δ)$-anonymity and $ε$-unlinkability, and mitigate compositional leakage through multi-turn disclosure control.
  We implement PlanTwin as middleware between local agents and cloud planners and evaluate it on 60 agentic tasks across ten domains with four cloud planners. PlanTwin achieves full sensitive-item non-disclosure (SND = 1.0) while maintaining planning quality close to full-context systems: three of four planners achieve PQS $> 0.79$, and the full pipeline incurs less than 2.2\% utility loss.

</details>


### 57. Large-Scale Analysis of Political Propaganda on Moltbook

- **Authors:** Julia Jose, Meghna Manoj Nair, Rachel Greenstadt
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18349v1](http://arxiv.org/abs/2603.18349v1)
- **PDF:** [https://arxiv.org/pdf/2603.18349v1](https://arxiv.org/pdf/2603.18349v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces a large‑scale, LLM‑based pipeline for detecting political propaganda generated by AI agents on Moltbook, a Reddit‑style forum for autonomous agents, and validates the classifiers against expert labels (Cohen’s κ = 0.64–0.74). Applying the system to 673 k posts and 880 k comments, the authors show that propaganda makes up only 1 % of all content yet dominates 42 % of political discourse, is produced by a tiny minority of agents (4 % generate 51 % of propaganda), and is highly concentrated in five communities, with many agents reposting near‑duplicate messages across subforums. Despite this concentration, the study finds little evidence that downstream comments further amplify the propaganda, suggesting that agent‑driven political manipulation on Moltbook is driven primarily by a few prolific, content‑recycling agents rather than by viral community interaction.


<details>
<summary>Abstract</summary>

We present an NLP-based study of political propaganda on Moltbook, a Reddit-style platform for AI agents. To enable large-scale analysis, we develop LLM-based classifiers to detect political propaganda, validated against expert annotation (Cohen's $κ$= 0.64-0.74). Using a dataset of 673,127 posts and 879,606 comments, we find that political propaganda accounts for 1% of all posts and 42% of all political content. These posts are concentrated in a small set of communities, with 70% of such posts falling into five of them. 4% of agents produced 51% of these posts. We further find that a minority of these agents repeatedly post highly similar content within and across communities. Despite this, we find limited evidence that comments amplify political propaganda.

</details>


### 58. Sparse3DTrack: Monocular 3D Object Tracking Using Sparse Supervision

- **Authors:** Nikhil Gosala, B. Ravi Kiran, Senthil Yogamani, Abhinav Valada
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18298v1](http://arxiv.org/abs/2603.18298v1)
- **PDF:** [https://arxiv.org/pdf/2603.18298v1](https://arxiv.org/pdf/2603.18298v1)
- **Categories:** cs.RO, cs.AI, cs.CV


> The paper introduces **Sparse3DTrack**, the first monocular 3D object‑tracking framework that learns from only a handful of per‑track annotations (≤ 4 ground‑truth frames) by converting sparse supervision into dense pseudo‑labels. It does so in two stages: (1) a 2‑D query‑matching module that exploits spatio‑temporal consistency to propagate sparse 2‑D cues across frames, and (2) a 3‑D geometry estimator that uses the matched 2‑D tracks to generate high‑quality 3‑D pose pseudo‑labels for the whole video, which are then fed to any off‑the‑shelf fully‑supervised tracker. Experiments on KITTI and nuScenes show that, despite the extreme label reduction, the approach lifts tracking accuracy by up to **15.5 percentage points**, demonstrating that reliable 3‑D scene understanding for autonomous agents can be achieved with dramatically less annotation effort.


<details>
<summary>Abstract</summary>

Monocular 3D object tracking aims to estimate temporally consistent 3D object poses across video frames, enabling autonomous agents to reason about scene dynamics. However, existing state-of-the-art approaches are fully supervised and rely on dense 3D annotations over long video sequences, which are expensive to obtain and difficult to scale. In this work, we address this fundamental limitation by proposing the first sparsely supervised framework for monocular 3D object tracking. Our approach decomposes the task into two sequential sub-problems: 2D query matching and 3D geometry estimation. Both components leverage the spatio-temporal consistency of image sequences to augment a sparse set of labeled samples and learn rich 2D and 3D representations of the scene. Leveraging these learned cues, our model automatically generates high-quality 3D pseudolabels across entire videos, effectively transforming sparse supervision into dense 3D track annotations. This enables existing fully-supervised trackers to effectively operate under extreme label sparsity. Extensive experiments on the KITTI and nuScenes datasets demonstrate that our method significantly improves tracking performance, achieving an improvement of up to 15.50 p.p. while using at most four ground truth annotations per track.

</details>


### 59. EDM-ARS: A Domain-Specific Multi-Agent System for Automated Educational Data Mining Research

- **Authors:** Chenguang Pan, Zhou Zhang, Weixuan Xiao, Chengyuan Yao
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18273v1](http://arxiv.org/abs/2603.18273v1)
- **PDF:** [https://arxiv.org/pdf/2603.18273v1](https://arxiv.org/pdf/2603.18273v1)
- **Categories:** cs.AI


> The paper introduces **EDM‑ARS**, a domain‑specific, multi‑agent pipeline that automates the full lifecycle of educational data‑mining research—from problem formulation to manuscript generation—by embedding pedagogical expertise into each stage. The system orchestrates five specialized LLM‑driven agents (ProblemFormulator, DataEngineer, Analyst, Critic, Writer) via a state‑machine coordinator that supports revision loops, checkpoint recovery, and sandboxed code execution, producing a LaTeX paper with validated predictive models, real citations, and an automated methodological peer review. Empirical evaluation shows that EDM‑ARS can reliably generate complete, reproducible research artifacts for a given dataset and prompt, demonstrating the feasibility of tightly coupled, domain‑aware agentic AI for end‑to‑end scientific authoring while highlighting current limits (single‑dataset focus, formulaic prose) and a roadmap toward more advanced causal and multi‑dataset capabilities.


<details>
<summary>Abstract</summary>

In this technical report, we present the Educational Data Mining Automated Research System (EDM-ARS), a domain-specific multi-agent pipeline that automates end-to-end educational data mining (EDM) research. We conceptualize EDM-ARS as a general framework for domain-aware automated research pipelines, where educational expertise is embedded into each stage of the research lifecycle. As a first instantiation of this framework, we focus on predictive modeling tasks. Within this scope, EDM-ARS orchestrates five specialized LLM-powered agents (ProblemFormulator, DataEngineer, Analyst, Critic, and Writer) through a state-machine coordinator that supports revision loops, checkpoint-based recovery, and sandboxed code execution. Given a research prompt and a dataset, EDM-ARS produces a complete LaTeX manuscript with real Semantic Scholar citations, validated machine learning analyses, and automated methodological peer review. We also provide a detailed description of the system architecture, the three-tier data registry design that encodes educational domain expertise, the specification of each agent, the inter-agent communication protocol, and mechanisms for error-handling and self-correction. Finally, we discuss current limitations, including single-dataset scope and formulaic paper output, and outline a phased roadmap toward causal inference, transfer learning, psychometric, and multi-dataset generalization. EDM-ARS is released as an open-source project to support the educational research community.

</details>


### 60. Retrieval-Augmented LLM Agents: Learning to Learn from Experience

- **Authors:** Thomas Palmeira Ferraz, Romain Deffayet, Vassilina Nikoulina, Hervé Déjean, Stéphane Clinchant
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18272v1](http://arxiv.org/abs/2603.18272v1)
- **PDF:** [https://arxiv.org/pdf/2603.18272v1](https://arxiv.org/pdf/2603.18272v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces a unified framework that trains large‑language‑model (LLM) agents to “learn to learn” by jointly fine‑tuning them (via LoRA‑based supervised fine‑tuning) and augmenting their inference with retrieved past trajectories. The authors first establish a robust SFT recipe that outperforms existing agent‑training pipelines, then systematically evaluate storage, query, and selection mechanisms for experience retrieval, and finally integrate the best‑performing retrieval strategy into the fine‑tuning loop. Experiments show that this combined retrieval‑augmented fine‑tuning markedly boosts agents’ ability to generalize to unseen tasks, surpassing both pure fine‑tuning and pure retrieval‑only baselines and offering a scalable recipe for building more adaptable, experience‑driven AI agents.


<details>
<summary>Abstract</summary>

While large language models (LLMs) have advanced the development of general-purpose agents, achieving robust generalization to unseen tasks remains a significant challenge. Current approaches typically rely on either fine-tuning or training-free memory-augmented generation using retrieved experience; yet both have limitations: fine-tuning often fails to extrapolate to new tasks, while experience retrieval often underperforms compared to supervised baselines. In this work, we propose to combine these approaches and systematically study how to train retrieval-augmented LLM agents to effectively leverage retrieved trajectories in-context. First, we establish a robust supervised fine-tuning (SFT) recipe using LoRA that outperforms several state-of-the-art agent training pipelines. Second, we provide a detailed analysis of key design choices for experience retrieval, identifying optimal strategies for storage, querying, and trajectory selection. Finally, we propose a pipeline that integrates experience retrieval into the fine-tuning process. Our results demonstrate that this combined approach significantly improves generalization to unseen tasks, providing a scalable and effective framework for building agents that learn to learn from experience.

</details>


### 61. Access Controlled Website Interaction for Agentic AI with Delegated Critical Tasks

- **Authors:** Sunyoung Kim, Hokeun Kim
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18197v1](http://arxiv.org/abs/2603.18197v1)
- **PDF:** [https://arxiv.org/pdf/2603.18197v1](https://arxiv.org/pdf/2603.18197v1)
- **Categories:** cs.AI, cs.CR, cs.NI


> The paper introduces a novel framework for granting AI agents fine‑grained, delegated access to web services when performing critical user‑directed tasks. The authors design a prototype website equipped with an extended authorization service (modifying an open‑source access‑grant protocol) that lets users specify precise permissions for each delegated action, and they evaluate the system by having autonomous agents execute real‑world tasks (e.g., form submission, data retrieval) under these constraints. Results show that the access‑controlled interface reliably enforces user‑defined limits, prevents unauthorized operations, and enables safe, trustworthy delegation of high‑stakes web interactions to agentic AI.


<details>
<summary>Abstract</summary>

Recent studies reveal gaps in delegating critical tasks to agentic AI that accesses websites on the user's behalf, primarily due to limited access control mechanisms on websites designed for agentic AI. In response, we propose a design of website-based interaction for AI agents with fine-grained access control for delegated critical tasks. Our approach encompasses a website design and implementation, as well as modifications to the access grant protocols in an open-source authorization service to tailor it to agentic AI, with delegated critical tasks on the website. The evaluation of our approach demonstrates the capabilities of our access-controlled website used by AI agents.

</details>


### 62. Don't Vibe Code, Do Skele-Code: Interactive No-Code Notebooks for Subject Matter Experts to Build Lower-Cost Agentic Workflows

- **Authors:** Sriram Gopalakrishnan
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18122v1](http://arxiv.org/abs/2603.18122v1)
- **PDF:** [https://arxiv.org/pdf/2603.18122v1](https://arxiv.org/pdf/2603.18122v1)
- **Categories:** cs.AI, cs.HC, cs.PL, eess.SY


> The paper introduces **Skele‑Code**, a natural‑language‑driven, graph‑based notebook interface that lets subject‑matter experts construct AI‑agent workflows without writing code. By treating the agent only as a code‑generation and error‑recovery helper—while the resulting workflow is expressed as modular, executable code—the system enables incremental, interactive development and dramatically lowers token consumption compared with fully orchestrated multi‑agent pipelines. Experiments show that Skele‑Code produces reusable, extensible workflows that can serve as standalone skills or sub‑steps in larger pipelines, achieving comparable task performance at a fraction of the computational cost.


<details>
<summary>Abstract</summary>

Skele-Code is a natural-language and graph-based interface for building workflows with AI agents, designed especially for less or non-technical users. It supports incremental, interactive notebook-style development, and each step is converted to code with a required set of functions and behavior to enable incremental building of workflows. Agents are invoked only for code generation and error recovery, not orchestration or task execution. This agent-supported, but code-first approach to workflows, along with the context-engineering used in Skele-Code, can help reduce token costs compared to the multi-agent system approach to executing workflows. Skele-Code produces modular, easily extensible, and shareable workflows. The generated workflows can also be used as skills by agents, or as steps in other workflows.

</details>


### 63. Differential Privacy in Generative AI Agents: Analysis and Optimal Tradeoffs

- **Authors:** Ya-Ting Yang, Quanyan Zhu
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17902v1](http://arxiv.org/abs/2603.17902v1)
- **PDF:** [https://arxiv.org/pdf/2603.17902v1](https://arxiv.org/pdf/2603.17902v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces a formal probabilistic framework that treats an AI‑agent’s response generation as a differentially private mechanism, defining both token‑level and message‑level privacy guarantees and linking leakage to generation hyper‑parameters such as temperature and output length. By analytically deriving privacy bounds and casting the temperature‑selection problem as a privacy‑utility trade‑off, the authors obtain closed‑form optimal temperature settings that minimize privacy loss while preserving response quality. Empirical evaluations on enterprise‑style query‑answer tasks confirm that the optimal temperature markedly reduces inferred data leakage compared with standard settings, demonstrating a practical pathway for deploying privacy‑aware generative AI agents in sensitive organizational environments.


<details>
<summary>Abstract</summary>

Large language models (LLMs) and AI agents are increasingly integrated into enterprise systems to access internal databases and generate context-aware responses. While such integration improves productivity and decision support, the model outputs may inadvertently reveal sensitive information. Although many prior efforts focus on protecting the privacy of user prompts, relatively few studies consider privacy risks from the enterprise data perspective. Hence, this paper develops a probabilistic framework for analyzing privacy leakage in AI agents based on differential privacy. We model response generation as a stochastic mechanism that maps prompts and datasets to distributions over token sequences. Within this framework, we introduce token-level and message-level differential privacy and derive privacy bounds that relate privacy leakage to generation parameters such as temperature and message length. We further formulate a privacy-utility design problem that characterizes optimal temperature selection.

</details>


### 64. Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models

- **Authors:** Yuhao Dong, Zuyan Liu, Shulin Tian, Yongming Rao, Ziwei Liu
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18118v1](http://arxiv.org/abs/2603.18118v1)
- **PDF:** [https://arxiv.org/pdf/2603.18118v1](https://arxiv.org/pdf/2603.18118v1)
- **Categories:** cs.CV, cs.AI, cs.LG


> The paper introduces **Insight‑V++**, a multi‑agent framework that equips multimodal large language models (MLLMs) with long‑chain visual reasoning abilities across images and videos. It combines an automated, multi‑granularity data‑generation pipeline with a dual‑agent architecture— a **reasoning agent** that produces extended analytical chains and a **summary agent** that evaluates and distills the results— and trains the system via two new reinforcement‑learning‑style algorithms (ST‑GRPO and J‑GRPO) that overcome the off‑policy limits of prior Direct Preference Optimization. Experiments on LLaVA‑NeXT and Qwen2.5‑VL show that Insight‑V++ markedly improves performance on demanding spatial‑temporal reasoning benchmarks while retaining strong perception skills, demonstrating a scalable, self‑improving approach for agentic visual AI.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have achieved remarkable reliability and advanced capabilities through extended test-time reasoning. However, extending these capabilities to Multi-modal Large Language Models (MLLMs) remains a significant challenge due to a critical scarcity of high-quality, long-chain reasoning data and optimized training pipelines. To bridge this gap, we present a unified multi-agent visual reasoning framework that systematically evolves from our foundational image-centric model, Insight-V, into a generalized spatial-temporal architecture, Insight-V++. We first propose a scalable data generation pipeline equipped with multi-granularity assessment that autonomously synthesizes structured, complex reasoning trajectories across image and video domains without human intervention. Recognizing that directly supervising MLLMs with such intricate data yields sub-optimal results, we design a dual-agent architecture comprising a reasoning agent to execute extensive analytical chains, and a summary agent to critically evaluate and distill final outcomes. While our initial framework utilized Direct Preference Optimization (DPO), its off-policy nature fundamentally constrained reinforcement learning potential. To overcome these limitations, particularly for long-horizon video understanding, Insight-V++ introduces two novel algorithms, ST-GRPO and J-GRPO, which enhance spatial-temporal reasoning and improve evaluative robustness. Crucially, by leveraging reliable feedback from the summary agent, we guide an iterative reasoning path generation process, retraining the entire multi-agent system in a continuous, self-improving loop. Extensive experiments on base models like LLaVA-NeXT and Qwen2.5-VL demonstrate significant performance gains across challenging image and video reasoning benchmarks while preserving strong capabilities on traditional perception-focused tasks.

</details>


### 65. RPMS: Enhancing LLM-Based Embodied Planning through Rule-Augmented Memory Synergy

- **Authors:** Zhenhang Yuan, Shenghai Yuan, Lihua Xie
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17831v1](http://arxiv.org/abs/2603.17831v1)
- **PDF:** [https://arxiv.org/pdf/2603.17831v1](https://arxiv.org/pdf/2603.17831v1)
- **Categories:** cs.AI


> The paper introduces RPMS, a conflict‑managed architecture that couples rule‑based action feasibility checks with a lightweight belief‑state memory to prevent invalid actions and state drift in LLM‑driven embodied agents. By retrieving structured precondition rules, gating episodic memory through the current belief state, and arbitrating conflicts with a “rules‑first” policy, RPMS dramatically improves performance on closed‑world tasks (e.g., from 35.8 % to 59.7 % success on ALFWorld with Llama 3.1‑8B, and to 98.5 % with Claude Sonnet 4.5). Ablations show that rule retrieval is the primary driver of gains, while memory becomes beneficial only when filtered by the belief state, and the approach generalizes to a different domain (ScienceWorld) with consistent improvements over ReAct baselines.


<details>
<summary>Abstract</summary>

LLM agents often fail in closed-world embodied environments because actions must satisfy strict preconditions -- such as location, inventory, and container states -- and failure feedback is sparse. We identify two structurally coupled failure modes: (P1) invalid action generation and (P2) state drift, each amplifying the other in a degenerative cycle. We present RPMS, a conflict-managed architecture that enforces action feasibility via structured rule retrieval, gates memory applicability via a lightweight belief state, and resolves conflicts between the two sources via rules-first arbitration. On ALFWorld (134 unseen tasks), RPMS achieves 59.7% single-trial success with Llama 3.1 8B (+23.9 pp over baseline) and 98.5% with Claude Sonnet 4.5 (+11.9 pp); of the 8B gain, rule retrieval alone contributes +14.9 pp (statistically significant), making it the dominant factor. A key finding is that episodic memory is conditionally useful: it harms performance on some task types when used without grounding, but becomes a stable net positive once filtered by current state and constrained by explicit action rules. Adapting RPMS to ScienceWorld with GPT-4 yields consistent gains across all ablation conditions (avg. score 54.0 vs. 44.9 for the ReAct baseline), providing transfer evidence that the core mechanisms hold across structurally distinct environments.

</details>


### 66. Federated Distributional Reinforcement Learning with Distributional Critic Regularization

- **Authors:** David Millard, Cecilia Alm, Rashid Ali, Pengcheng Shi, Ali Baheri
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17820v1](http://arxiv.org/abs/2603.17820v1)
- **PDF:** [https://arxiv.org/pdf/2603.17820v1](https://arxiv.org/pdf/2603.17820v1)
- **Categories:** cs.LG


> The paper introduces **Federated Distributional Reinforcement Learning (FedDistRL)**, a framework that federates only the **quantile‑based distributional critics** of RL agents, preserving full return distributions rather than collapsing them to expected values. It proposes **TR‑FedDistRL**, which constructs a per‑client risk‑aware Wasserstein barycenter from a temporal buffer and uses it as a trust‑region reference to “shrink‑squash” the averaged critic parameters, guaranteeing that multimodal and tail‑risk information is retained during federation. Empirical results on a bandit, a multi‑agent gridworld, and a continuous highway driving task show that this approach markedly reduces mean‑smearing, lowers catastrophe/accident rates, and curtails critic and policy drift compared with standard mean‑based federated and non‑federated baselines—demonstrating a safer, more reliable way to aggregate agentic knowledge in distributed settings.


<details>
<summary>Abstract</summary>

Federated reinforcement learning typically aggregates value functions or policies by parameter averaging, which emphasizes expected return and can obscure statistical multimodality and tail behavior that matter in safety-critical settings. We formalize federated distributional reinforcement learning (FedDistRL), where clients parametrize quantile value function critics and federate these networks only. We also propose TR-FedDistRL, which builds a per client, risk-aware Wasserstein barycenter over a temporal buffer. This local barycenter provides a reference region to constrain the parameter averaged critic, ensuring necessary distributional information is not averaged out during the federation process. The distributional trust region is implemented as a shrink-squash step around this reference. Under fixed-policy evaluation, the feasibility map is nonexpansive and the update is contractive in a probe-set Wasserstein metric under evaluation. Experiments on a bandit, multi-agent gridworld, and continuous highway environment show reduced mean-smearing, improved safety proxies (catastrophe/accident rate), and lower critic/policy drift versus mean-oriented and non-federated baselines.

</details>


### 67. Governed Memory: A Production Architecture for Multi-Agent Workflows

- **Authors:** Hamed Taheri
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17787v1](http://arxiv.org/abs/2603.17787v1)
- **PDF:** [https://arxiv.org/pdf/2603.17787v1](https://arxiv.org/pdf/2603.17787v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> The paper introduces **Governed Memory**, a shared‑memory and governance layer that enables large numbers of autonomous agents to operate on common entities without siloed or unstructured knowledge. The authors design a dual‑memory model (open‑set atomic facts plus schema‑enforced typed properties) together with tiered routing, entity‑scoped retrieval, and a closed‑loop schema lifecycle that is AI‑assisted and automatically refined; they evaluate each component in controlled experiments (N = 250 across five content types) and on the LoCoMo benchmark. Results show near‑perfect fact recall (99.6 %), high routing precision (92 %), 50 % token savings from progressive context delivery, zero cross‑entity leakage in adversarial tests, and overall benchmark accuracy of 74.8 %—demonstrating that structured, governed memory can dramatically improve coordination, efficiency, and safety of multi‑agent workflows without sacrificing retrieval quality.


<details>
<summary>Abstract</summary>

Enterprise AI deploys dozens of autonomous agent nodes across workflows, each acting on the same entities with no shared memory and no common governance. We identify five structural challenges arising from this memory governance gap: memory silos across agent workflows; governance fragmentation across teams and tools; unstructured memories unusable by downstream systems; redundant context delivery in autonomous multi-step executions; and silent quality degradation without feedback loops. We present Governed Memory, a shared memory and governance layer addressing this gap through four mechanisms: a dual memory model combining open-set atomic facts with schema-enforced typed properties; tiered governance routing with progressive context delivery; reflection-bounded retrieval with entity-scoped isolation; and a closed-loop schema lifecycle with AI-assisted authoring and automated per-property refinement. We validate each mechanism through controlled experiments (N=250, five content types): 99.6% fact recall with complementary dual-modality coverage; 92% governance routing precision; 50% token reduction from progressive delivery; zero cross-entity leakage across 500 adversarial queries; 100% adversarial governance compliance; and output quality saturation at approximately seven governed memories per entity. On the LoCoMo benchmark, the architecture achieves 74.8% overall accuracy, confirming that governance and schema enforcement impose no retrieval quality penalty. The system is in production at Personize.ai.

</details>


### 68. MALLES: A Multi-agent LLMs-based Economic Sandbox with Consumer Preference Alignment

- **Authors:** Yusen Wu, Yiran Liu, Xiaotie Deng
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17694v1](http://arxiv.org/abs/2603.17694v1)
- **PDF:** [https://arxiv.org/pdf/2603.17694v1](https://arxiv.org/pdf/2603.17694v1)
- **Categories:** cs.AI


> The paper presents **MALLES**, a multi‑agent simulation platform that uses large language models (LLMs) as economic actors whose preferences are aligned through post‑training on massive, heterogeneous transaction logs, allowing the models to capture and transfer latent consumer tastes across product categories.  Its methodology combines (1) preference‑learning fine‑tuning of LLMs, (2) a mean‑field interaction layer that stabilizes high‑dimensional market dynamics, and (3) a collaborative “discussion” protocol where specialized agents exchange information to overcome single‑agent attention limits.  Empirical results show that MALLES markedly outperforms prior LLM‑based economic simulators in product‑selection accuracy, purchase‑quantity forecasting, and overall simulation stability, demonstrating the viability of LLM‑driven, multi‑agent frameworks for high‑fidelity decision‑making in real‑world economies.


<details>
<summary>Abstract</summary>

In the real economy, modern decision-making is fundamentally challenged by high-dimensional, multimodal environments, which are further complicated by agent heterogeneity and combinatorial data sparsity. This paper introduces a Multi-Agent Large Language Model-based Economic Sandbox (MALLES), leveraging the inherent generalization capabilities of large-sacle models to establish a unified simulation framework applicable to cross-domain and cross-category scenarios. Central to our approach is a preference learning paradigm in which LLMs are economically aligned via post-training on extensive, heterogeneous transaction records across diverse product categories. This methodology enables the models to internalize and transfer latent consumer preference patterns, thereby mitigating the data sparsity issues prevalent in individual categories. To enhance simulation stability, we implement a mean-field mechanism designed to model the dynamic interactions between the product environment and customer populations, effectively stabilizing sampling processes within high-dimensional decision spaces. Furthermore, we propose a multi-agent discussion framework wherein specialized agents collaboratively process extensive product information. This architecture distributes cognitive load to alleviate single-agent attention bottlenecks and captures critical decision factors through structured dialogue. Experiments demonstrate that our framework achieves significant improvements in product selection accuracy, purchase quantity prediction, and simulation stability compared to existing economic and financial LLM simulation baselines. Our results substantiate the potential of large language models as a foundational pillar for high-fidelity, scalable decision simulation and latter analysis in the real economy based on foundational database.

</details>


### 69. Can Blindfolded LLMs Still Trade? An Anonymization-First Framework for Portfolio Optimization

- **Authors:** Joohyoung Jeon, Hongchul Lee
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17692v1](http://arxiv.org/abs/2603.17692v1)
- **PDF:** [https://arxiv.org/pdf/2603.17692v1](https://arxiv.org/pdf/2603.17692v1)
- **Categories:** cs.LG, cs.AI, q-fin.CP, q-fin.PM


> The paper introduces **BlindTrade**, an “anonymization‑first” framework that forces large‑language‑model (LLM) trading agents to operate without any ticker or company identifiers, thereby testing whether their predictions stem from genuine market reasoning rather than memorized label‑specific knowledge. The authors blind‑fold four LLM agents, collect their scored predictions and reasoning embeddings, build a graph‑neural‑network representation of the reasoning, and train a PPO‑DSR policy to execute trades; extensive back‑testing with negative controls isolates true signal from memorization and survivorship biases. Across the 2025‑year‑to‑date out‑of‑sample window, BlindTrade attains a Sharpe ratio of **1.40 ± 0.22** (20 seeds), confirming that meaningful signals survive anonymization, while further evaluation shows the policy’s strength in volatile regimes and weaker performance in sustained bull markets—demonstrating a viable path toward trustworthy, agentic AI in financial decision‑making.


<details>
<summary>Abstract</summary>

For LLM trading agents to be genuinely trustworthy, they must demonstrate understanding of market dynamics rather than exploitation of memorized ticker associations. Building responsible multi-agent systems demands rigorous signal validation: proving that predictions reflect legitimate patterns, not pre-trained recall. We address two sources of spurious performance: memorization bias from ticker-specific pre-training, and survivorship bias from flawed backtesting. Our approach is to blindfold the agents--anonymizing all identifiers--and verify whether meaningful signals persist. BlindTrade anonymizes tickers and company names, and four LLM agents output scores along with reasoning. We construct a GNN graph from reasoning embeddings and trade using PPO-DSR policy. On 2025 YTD (through 2025-08-01), we achieved Sharpe 1.40 +/- 0.22 across 20 seeds and validated signal legitimacy through negative control experiments. To assess robustness beyond a single OOS window, we additionally evaluate an extended period (2024--2025), revealing market-regime dependency: the policy excels in volatile conditions but shows reduced alpha in trending bull markets.

</details>


### 70. Sensi: Learn One Thing at a Time -- Curriculum-Based Test-Time Learning for LLM Game Agents

- **Authors:** Mohsen Arjmandi
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17683v1](http://arxiv.org/abs/2603.17683v1)
- **PDF:** [https://arxiv.org/pdf/2603.17683v1](https://arxiv.org/pdf/2603.17683v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces **Sensi**, a novel LLM‑agent architecture that enables rapid test‑time learning in unknown game environments by (1) decoupling perception and action into two cooperating LLMs, (2) driving a curriculum of single‑concept lessons with an external state‑machine controller, and (3) using a database‑as‑control‑plane plus an LLM‑as‑judge that generates rubrics to decide when a concept is mastered. Experiments on the ARC‑AGI‑3 challenge show that, after adding curriculum learning (Sensi v2), the agent can traverse its entire 32‑step curriculum in only 32 action attempts—yielding a **50–94× improvement in sample efficiency** over prior methods that need 1.6k–3k interactions—while still failing to solve full levels due to a perceptual grounding hallucination cascade. The work shifts the primary bottleneck for LLM game agents from learning efficiency to reliable perception, highlighting a new, tractable direction for advancing agentic AI.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents deployed in unknown environments must learn task structure at test time, but current approaches require thousands of interactions to form useful hypotheses. We present Sensi, an LLM agent architecture for the ARC-AGI-3 game-playing challenge that introduces structured test-time learning through three mechanisms: (1) a two-player architecture separating perception from action, (2) a curriculum-based learning system managed by an external state machine, and (3) a database-as-control-plane that makes the agents context window programmatically steerable. We further introduce an LLM-as-judge component with dynamically generated evaluation rubrics to determine when the agent has learned enough about one topic to advance to the next. We report results across two iterations: Sensi v1 solves 2 game levels using the two-player architecture alone, while Sensi v2 adds curriculum learning and solves 0 levels - but completes its entire learning curriculum in approximately 32 action attempts, achieving 50-94x greater sample efficiency than comparable systems that require 1600-3000 attempts. We precisely diagnose the failure mode as a self-consistent hallucination cascade originating in the perception layer, demonstrating that the architectural bottleneck has shifted from learning efficiency to perceptual grounding - a more tractable problem.

</details>


### 71. Post-Training Local LLM Agents for Linux Privilege Escalation with Verifiable Rewards

- **Authors:** Philipp Normann, Andreas Happe, Jürgen Cito, Daniel Arp
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17673v1](http://arxiv.org/abs/2603.17673v1)
- **PDF:** [https://arxiv.org/pdf/2603.17673v1](https://arxiv.org/pdf/2603.17673v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **PrivEsc‑LLM**, a 4 B‑parameter local language model that can autonomously discover and execute Linux privilege‑escalation exploits, demonstrating that high‑performing security agents need not rely on large, cloud‑only systems. The authors devise a two‑stage post‑training pipeline: (1) supervised fine‑tuning on synthetic, procedurally‑generated escalation traces, and (2) reinforcement learning with automatically verifiable rewards that confirm each escalation step. On a held‑out benchmark of 12 multi‑step escalation scenarios, supervised fine‑tuning more than doubles baseline success, and the RL‑enhanced model reaches **95.8 %** success—within 2 % of Claude Opus 4.6—while cutting the expected inference cost per successful exploit by over **100×**, highlighting a cost‑effective route for building capable, reproducible agentic AI for security tasks.


<details>
<summary>Abstract</summary>

LLM agents are increasingly relevant to research domains such as vulnerability discovery. Yet, the strongest systems remain closed and cloud-only, making them resource-intensive, difficult to reproduce, and unsuitable for work involving proprietary code or sensitive data. Consequently, there is an urgent need for small, local models that can perform security tasks under strict resource budgets, but methods for developing them remain underexplored. In this paper, we address this gap by proposing a two-stage post-training pipeline. We focus on the problem of Linux privilege escalation, where success is automatically verifiable and the task requires multi-step interactive reasoning. Using an experimental setup that prevents data leakage, we post-train a 4B model in two stages: supervised fine-tuning on traces from procedurally generated privilege-escalation environments, followed by reinforcement learning with verifiable rewards. On a held-out benchmark of 12 Linux privilege-escalation scenarios, supervised fine-tuning alone more than doubles the baseline success rate at 20 rounds, and reinforcement learning further lifts our resulting model, PrivEsc-LLM, to 95.8%, nearly matching Claude Opus 4.6 at 97.5%. At the same time, the expected inference cost per successful escalation is reduced by over 100x.

</details>


### 72. VeriGrey: Greybox Agent Validation

- **Authors:** Yuntong Zhang, Sungmin Kang, Ruijie Meng, Marcel Böhme, Abhik Roychoudhury
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17639v1](http://arxiv.org/abs/2603.17639v1)
- **PDF:** [https://arxiv.org/pdf/2603.17639v1](https://arxiv.org/pdf/2603.17639v1)
- **Categories:** cs.AI


> VeriGrey introduces a grey‑box testing framework for LLM‑driven agents that leverages the agents’ tool‑invocation trace as a feedback signal to guide prompt mutations and uncover indirect prompt‑injection vulnerabilities. By treating the required tool calls as a “must‑do” step, the system generates malicious injection prompts that force the agent to execute unsafe tool actions, achieving a 33 % higher detection rate than black‑box baselines on the AgentDojo benchmark (using a GPT‑4.1 backend). Real‑world evaluations on the Gemini CLI coding agent and the OpenClaw personal assistant demonstrate near‑perfect success in exposing malicious skill variants (100 % on Kimi‑K2.5 and 90 % on Opus 4.6), highlighting VeriGrey’s effectiveness for dynamic security assurance of autonomous AI agents.


<details>
<summary>Abstract</summary>

Agentic AI has been a topic of great interest recently. A Large Language Model (LLM) agent involves one or more LLMs in the back-end. In the front end, it conducts autonomous decision-making by combining the LLM outputs with results obtained by invoking several external tools. The autonomous interactions with the external environment introduce critical security risks.
  In this paper, we present a grey-box approach to explore diverse behaviors and uncover security risks in LLM agents. Our approach VeriGrey uses the sequence of tools invoked as a feedback function to drive the testing process. This helps uncover infrequent but dangerous tool invocations that cause unexpected agent behavior. As mutation operators in the testing process, we mutate prompts to design pernicious injection prompts. This is carefully accomplished by linking the task of the agent to an injection task, so that the injection task becomes a necessary step of completing the agent functionality. Comparing our approach with a black-box baseline on the well-known AgentDojo benchmark, VeriGrey achieves 33% additional efficacy in finding indirect prompt injection vulnerabilities with a GPT-4.1 back-end.
  We also conduct real-world case studies with the widely used coding agent Gemini CLI, and the well-known OpenClaw personal assistant. VeriGrey finds prompts inducing several attack scenarios that could not be identified by black-box approaches. In OpenClaw, by constructing a conversation agent which employs mutational fuzz testing as needed, VeriGrey is able to discover malicious skill variants from 10 malicious skills (with 10/10= 100% success rate on the Kimi-K2.5 LLM backend, and 9/10= 90% success rate on Opus 4.6 LLM backend). This demonstrates the value of a dynamic approach like VeriGrey to test agents, and to eventually lead to an agent assurance framework.

</details>


### 73. VeriAgent: A Tool-Integrated Multi-Agent System with Evolving Memory for PPA-Aware RTL Code Generation

- **Authors:** Yaoxiang Wang, Qi Shi, ShangZhan Li, Qingguo Hu, Xinyu Yin, Bo Guo, Xu Han, Maosong Sun, Jinsong Su
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17613v1](http://arxiv.org/abs/2603.17613v1)
- **PDF:** [https://arxiv.org/pdf/2603.17613v1](https://arxiv.org/pdf/2603.17613v1)
- **Categories:** cs.CL, cs.PL


> VeriAgent introduces a closed‑loop, tool‑integrated multi‑agent system for RTL generation that jointly optimizes functional correctness and physical design objectives (Power, Performance, Area). The framework orchestrates a Programmer Agent, a Correctness Agent, and a PPA Agent around commercial EDA tools, while an “Evolved Memory Mechanism” externalizes past optimization experiences into structured memory nodes managed by a dynamic memory manager, enabling continual improvement without retraining the underlying LLM. Experiments show that this agentic architecture retains high syntactic/functional success rates and yields substantial PPA gains, demonstrating that feedback‑driven, memory‑evolving agents can effectively bridge generative AI and real‑world hardware design flows.


<details>
<summary>Abstract</summary>

LLMs have recently demonstrated strong capabilities in automatic RTL code generation, achieving high syntactic and functional correctness. However, most methods focus on functional correctness while overlooking critical physical design objectives, including Power, Performance, and Area. In this work, we propose a PPA-aware, tool-integrated multi-agent framework for high-quality verilog code generation. Our framework explicitly incorporates EDA tools into a closed-loop workflow composed of a \textit{Programmer Agent}, a \textit{Correctness Agent}, and a \textit{PPA Agent}, enabling joint optimization of functional correctness and physical metrics. To support continuous improvement without model retraining, we introduce an \textit{Evolved Memory Mechanism} that externalizes optimization experience into structured memory nodes. A dedicated memory manager dynamically maintains the memory pool and allows the system to refine strategies based on historical execution trajectories. Extensive experiments demonstrate that our approach achieves strong functional correctness while delivering significant improvements in PPA metrics. By integrating tool-driven feedback with structured and evolvable memory, our framework transforms RTL generation from one-shot reasoning into a continual, feedback-driven optimization process, providing a scalable pathway for deploying LLMs in real-world hardware design flows.

</details>


### 74. A Trace-Based Assurance Framework for Agentic AI Orchestration: Contracts, Testing, and Governance

- **Authors:** Ciprian Paduraru, Petru-Liviu Bouruc, Alin Stefanescu
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18096v1](http://arxiv.org/abs/2603.18096v1)
- **PDF:** [https://arxiv.org/pdf/2603.18096v1](https://arxiv.org/pdf/2603.18096v1)
- **Categories:** cs.MA, cs.AI


> The paper introduces a trace‑based assurance framework that instruments multi‑agent LLM orchestrations as **Message‑Action Traces (MAT)** enriched with explicit step‑ and trace‑level contracts, enabling automatic violation detection, deterministic replay, and fine‑grained fault localization. By combining contract‑driven stress testing (budgeted counterexample search over bounded perturbations) with structured fault‑injection at service, retrieval, and memory boundaries, the authors demonstrate how to measure and enforce termination reliability, factuality, containment, and governance outcomes across stochastic seeds, model variants, and orchestration designs. Empirical evaluations show that the MAT contracts reliably pinpoint the first failure step, improve reproducibility of multi‑agent experiments, and allow runtime governance (allow/rewrite/block) to effectively limit unsafe actions while preserving overall task success.


<details>
<summary>Abstract</summary>

In Agentic AI, Large Language Models (LLMs) are increasingly used in the orchestration layer to coordinate multiple agents and to interact with external services, retrieval components, and shared memory. In this setting, failures are not limited to incorrect final outputs. They also arise from long-horizon interaction, stochastic decisions, and external side effects (such as API calls, database writes, and message sends). Common failures include non-termination, role drift, propagation of unsupported claims, and attacks via untrusted context or external channels.
  This paper presents an assurance framework for such Agentic AI systems. Executions are instrumented as Message-Action Traces (MAT) with explicit step and trace contracts. Contracts provide machine-checkable verdicts, localize the first violating step, and support deterministic replay. The framework includes stress testing, formulated as a budgeted counterexample search over bounded perturbations. It also supports structured fault injection at service, retrieval, and memory boundaries to assess containment under realistic operational faults and degraded conditions. Finally, governance is treated as a runtime component, enforcing per-agent capability limits and action mediation (allow, rewrite, block) at the language-to-action boundary.
  To support comparative evaluations across stochastic seeds, models, and orchestration configurations, the paper defines trace-based metrics for task success, termination reliability, contract compliance, factuality indicators, containment rate, and governance outcome distributions. More broadly, the framework is intended as a common abstraction to support testing and evaluation of multi-agent LLM systems, and to facilitate reproducible comparison across orchestration designs and configurations.

</details>


### 75. In Trust We Survive: Emergent Trust Learning

- **Authors:** Qianpu Chen, Giulio Barbero, Mike Preuss, Derya Soydaner
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17564v1](http://arxiv.org/abs/2603.17564v1)
- **PDF:** [https://arxiv.org/pdf/2603.17564v1](https://arxiv.org/pdf/2603.17564v1)
- **Categories:** cs.MA, cs.LG


> The paper presents **Emergent Trust Learning (ETL)**, a lightweight, plug‑in control layer that equips otherwise standard reinforcement‑learning agents with a compact internal “trust” state used to bias memory retention, exploration intensity, and action selection. ETL operates solely on each agent’s own reward signal and local observations, requiring no extra communication or centralized supervision, and is implemented as a simple update rule that modulates the agent’s policy. Empirical results across three competitive, shared‑resource domains— a grid‑world resource management task, a hierarchical “Tower” social‑dilemma setting, and the Iterated Prisoner’s Dilemma—show that trust‑augmented agents dramatically cut conflict, sustain high survival and cooperation rates, and resist exploitation, demonstrating that a minimal trust mechanism can induce robust emergent cooperation in agentic AI systems.


<details>
<summary>Abstract</summary>

We introduce Emergent Trust Learning (ETL), a lightweight, trust-based control algorithm that can be plugged into existing AI agents. It enables these to reach cooperation in competitive game environments under shared resources. Each agent maintains a compact internal trust state, which modulates memory, exploration, and action selection. ETL requires only individual rewards and local observations and incurs negligible computational and communication overhead.
  We evaluate ETL in three environments: In a grid-based resource world, trust-based agents reduce conflicts and prevent long-term resource depletion while achieving competitive individual returns. In a hierarchical Tower environment with strong social dilemmas and randomised floor assignments, ETL sustains high survival rates and recovers cooperation even after extended phases of enforced greed. In the Iterated Prisoner's Dilemma, the algorithm generalises to a strategic meta-game, maintaining cooperation with reciprocal opponents while avoiding long-term exploitation by defectors. Code will be released upon publication.

</details>


### 76. When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Attribution

- **Authors:** Yi Nian, Haosen Cao, Shenzhe Zhu, Henry Peng Zou, Qingqing Luan, Yue Zhao
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17445v2](http://arxiv.org/abs/2603.17445v2)
- **PDF:** [https://arxiv.org/pdf/2603.17445v2](https://arxiv.org/pdf/2603.17445v2)
- **Categories:** cs.AI, cs.CL


> The paper introduces **Implicit Execution Tracing (IET)**, a privacy‑preserving framework that embeds secret, agent‑specific signals directly into the token distribution of a multi‑agent language model’s output, allowing post‑hoc reconstruction of which agent produced each token and the overall interaction topology without any external logs. IET works by conditioning generation on keyed “signal tokens” that are invisible to observers but can be detected with the secret key using a transition‑aware scoring algorithm that identifies hand‑over points and rebuilds the delegation graph. Experiments on synthetic and real multi‑agent dialogue benchmarks show that IET recovers agent segments and coordination structures with >90 % accuracy while incurring negligible degradation in generation quality, demonstrating a viable route for accountable auditing of agentic AI systems when only the final text is available.


<details>
<summary>Abstract</summary>

When a multi-agent system produces an incorrect or harmful answer, who is accountable if execution logs and agent identifiers are unavailable? Multi-agent language systems increasingly rely on structured interactions such as delegation and iterative refinement, yet the final output often obscures the underlying interaction topology and agent contributions. We introduce IET (Implicit Execution Tracing), a metadata-independent framework that enables token-level attribution directly from generated text and a simple mechanism for interaction topology reconstruction. During generation, agent-specific keyed signals are embedded into the token distribution, transforming the text into a self-describing execution trace detectable only with a secret key. At detection time, a transition-aware scoring method identifies agent handover points and reconstructs the interaction graph. Experiments show that IET recovers agent segments and coordination structure with high accuracy while preserving generation quality, enabling privacy-preserving auditing for multi-agent language systems.

</details>


### 77. SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training

- **Authors:** Prince Zizhuang Wang, Shuli Jiang
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.18079v1](http://arxiv.org/abs/2603.18079v1)
- **PDF:** [https://arxiv.org/pdf/2603.18079v1](https://arxiv.org/pdf/2603.18079v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **SLEA‑RL**, a step‑level experience‑augmented reinforcement‑learning framework that continuously retrieves and incorporates past trajectories during each decision step of a multi‑turn LLM‑agent, rather than relying on a single static retrieval at episode start. It does so by (1) clustering observations to enable fast, context‑aware library look‑ups, (2) maintaining a self‑evolving experience repository that admits high‑scoring successes and extracts informative failures, and (3) applying step‑wise credit assignment to compute fine‑grained advantage estimates for policy updates. Empirical results on long‑horizon tool‑use benchmarks show that SLEA‑RL consistently outperforms standard RL baselines and prior experience‑augmented methods, demonstrating that dynamic, step‑conditioned experience reuse markedly improves the training efficiency and final performance of agentic AI systems.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents have shown strong results on multi-turn tool-use tasks, yet they operate in isolation during training, failing to leverage experiences accumulated across episodes. Existing experience-augmented methods address this by organizing trajectories into retrievable libraries, but they retrieve experiences only once based on the initial task description and hold them constant throughout the episode. In multi-turn settings where observations change at every step, this static retrieval becomes increasingly mismatched as episodes progress. We propose SLEA-RL (Step-Level Experience-Augmented Reinforcement Learning), a framework that retrieves relevant experiences at each decision step conditioned on the current observation. SLEA-RL operates through three components: (i) step-level observation clustering that groups structurally equivalent environmental states for efficient cluster-indexed retrieval; (ii) a self-evolving experience library that distills successful strategies and failure patterns through score-based admission and rate-limited extraction; and (iii) policy optimization with step-level credit assignment for fine-grained advantage estimation across multi-turn episodes. The experience library evolves alongside the policy through semantic analysis rather than gradient updates. Experiments on long-horizon multi-turn agent benchmarks demonstrate that SLEA-RL achieves superior performance compared to various reinforcement learning baselines.

</details>


### 78. From Digital Twins to World Models:Opportunities, Challenges, and Applications for Mobile Edge General Intelligence

- **Authors:** Jie Zheng, Dusit Niyato, Changyuan Zhao, Jiawen Kang, Jiacheng Wang
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17420v1](http://arxiv.org/abs/2603.17420v1)
- **PDF:** [https://arxiv.org/pdf/2603.17420v1](https://arxiv.org/pdf/2603.17420v1)
- **Categories:** cs.AI


> The paper surveys the emerging shift from physics‑based, centralized digital twins to data‑driven, decentralized world models that serve as internal, agent‑centric representations for edge‑native general intelligence (EGI). By dissecting the architectural components—perception, latent state encoding, dynamics learning, imagination‑based planning, and memory—and mapping them onto wireless edge scenarios (e.g., integrated sensing‑communication, semantic communication, air‑ground and low‑altitude networks), the authors illustrate how world‑model‑driven agents can achieve greater autonomy, adaptability, and resource efficiency than traditional twins. The survey identifies design principles, integration strategies, and open challenges (scalability, reliability, interoperability), charting a roadmap for deploying scalable, agentic AI systems at the mobile edge.


<details>
<summary>Abstract</summary>

The rapid evolution toward 6G and beyond communication systems is accelerating the convergence of digital twins and world models at the network edge. Traditional digital twins provide high-fidelity representations of physical systems and support monitoring, analysis, and offline optimization. However, in highly dynamic edge environments, they face limitations in autonomy, adaptability, and scalability. This paper presents a systematic survey of the transition from digital twins to world models and discusses its role in enabling edge general intelligence (EGI). First, the paper clarifies the conceptual differences between digital twins and world models and highlights the shift from physics-based, centralized, and system-centric replicas to data-driven, decentralized, and agent-centric internal models. This discussion helps readers gain a clear understanding of how this transition enables more adaptive, autonomous, and resource-efficient intelligence at the network edge. The paper reviews the design principles, architectures, and key components of world models, including perception, latent state representation, dynamics learning, imagination-based planning, and memory. In addition, it examines the integration of world models and digital twins in wireless EGI systems and surveys emerging applications in integrated sensing and communications, semantic communication, air-ground networks, and low-altitude wireless networks. Finally, this survey provides a systematic roadmap and practical insights for designing world-model-driven edge intelligence systems in wireless and edge computing environments. It also outlines key research challenges and future directions toward scalable, reliable, and interoperable world models for edge-native agentic AI.

</details>


### 79. Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare

- **Authors:** Saikat Maiti
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17419v1](http://arxiv.org/abs/2603.17419v1)
- **PDF:** [https://arxiv.org/pdf/2603.17419v1](https://arxiv.org/pdf/2603.17419v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces a “zero‑trust” security architecture that hardens autonomous LLM‑driven agents handling Protected Health Information, presenting the first end‑to‑end, production‑grade defense‑in‑depth stack for agentic AI in healthcare. By combining a six‑domain threat model with four layered controls—gVisor kernel isolation, credential‑proxy sidecars, strict egress allow‑lists, and a structured prompt‑integrity envelope—the authors deployed and continuously audited nine agents over 90 days, automatically uncovering and fixing four high‑severity vulnerabilities and achieving coverage of all eleven attack patterns identified in recent red‑team studies. The open‑source release of the configurations, audit tools, and integrity framework provides a reusable blueprint for securing autonomous AI agents in regulated domains.


<details>
<summary>Abstract</summary>

Autonomous AI agents powered by large language models are being deployed in production with capabilities including shell execution, file system access, database queries, and multi-party communication. Recent red teaming research demonstrates that these agents exhibit critical vulnerabilities in realistic settings: unauthorized compliance with non-owner instructions, sensitive information disclosure, identity spoofing, cross-agent propagation of unsafe practices, and indirect prompt injection through external resources [7]. In healthcare environments processing Protected Health Information, every such vulnerability becomes a potential HIPAA violation. This paper presents a security architecture deployed for nine autonomous AI agents in production at a healthcare technology company. We develop a six-domain threat model for agentic AI in healthcare covering credential exposure, execution capability abuse, network egress exfiltration, prompt integrity failures, database access risks, and fleet configuration drift. We implement four-layer defense in depth: (1) kernel level workload isolation using gVisor on Kubernetes, (2) credential proxy sidecars preventing agent containers from accessing raw secrets, (3) network egress policies restricting each agent to allowlisted destinations, and (4) a prompt integrity framework with structured metadata envelopes and untrusted content labeling. We report results from 90 days of deployment including four HIGH severity findings discovered and remediated by an automated security audit agent, progressive fleet hardening across three VM image generations, and defense coverage mapped to all eleven attack patterns from recent literature. All configurations, audit tooling, and the prompt integrity framework are released as open source.

</details>


### 80. Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases (Preferences)

- **Authors:** Zichen Tang, Zirui Zhang, Qian Wang, Zhenheng Tang, Bo Li, Xiaowen Chu
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17417v2](http://arxiv.org/abs/2603.17417v2)
- **PDF:** [https://arxiv.org/pdf/2603.17417v2](https://arxiv.org/pdf/2603.17417v2)
- **Categories:** cs.CY, cs.MA


> The paper introduces **BiasRecBench**, a systematic benchmark that exposes how LLM‑based recommender agents (e.g., for paper reviewing, e‑commerce, and job hiring) can be steered away from optimal choices by subtle contextual biases. The authors build a **Bias Synthesis Pipeline** that (1) generates candidate sets with calibrated quality gaps between the best and sub‑optimal options and (2) injects logically consistent preference biases into the option descriptions, then evaluate a range of state‑of‑the‑art (Gemini‑2.5/3‑pro, GPT‑4o, DeepSeek‑R1) and smaller LLMs. Experiments show that—even when the models can correctly reason about the true optimal item—they frequently select biased, lower‑quality alternatives, revealing a critical reliability flaw in current LLM‑as‑recommender agents and highlighting the need for dedicated alignment techniques for such agentic workflows.


<details>
<summary>Abstract</summary>

Current Large Language Models (LLMs) are gradually exploited in practically valuable agentic workflows such as Deep Research, E-commerce recommendation, and job recruitment. In these applications, LLMs need to select some optimal solutions from massive candidates, which we term as \textit{LLM-as-a-Recommender} paradigm. However, the reliability of using LLM agents for recommendations is underexplored. In this work, we introduce a \textbf{Bias} \textbf{Rec}ommendation \textbf{Bench}mark (\textbf{BiasRecBench}) to highlight the critical vulnerability of such agents to biases in high-value real-world tasks. The benchmark includes three practical domains: paper review, e-commerce, and job recruitment. We construct a \textsc{Bias Synthesis Pipeline with Calibrated Quality Margins} that 1) synthesizes evaluation data by controlling the quality gap between optimal and sub-optimal options to provide a calibrated testbed to elicit the vulnerability to biases; 2) injects contextual biases that are logical and suitable for option contexts. Extensive experiments on both SOTA (Gemini-{2.5,3}-pro, GPT-4o, DeepSeek-R1) and small-scale LLMs reveal that agents frequently succumb to injected biases despite having sufficient reasoning capabilities to identify the ground truth. These findings expose a significant reliability bottleneck in current agentic workflows, calling for specialized alignment strategies for LLM-as-a-Recommender. The complete code and evaluation datasets will be made publicly available shortly.

</details>


### 81. Agentic Cognitive Profiling: Realigning Automated Alzheimer's Disease Detection with Clinical Construct Validity

- **Authors:** Jiawen Kang, Kun Li, Dongrui Han, Jinchao Li, Junan Li, Lingwei Meng, Xixin Wu, Helen Meng
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17392v1](http://arxiv.org/abs/2603.17392v1)
- **PDF:** [https://arxiv.org/pdf/2603.17392v1](https://arxiv.org/pdf/2603.17392v1)
- **Categories:** cs.MA, cs.IR, q-bio.NC


> The paper introduces **Agentic Cognitive Profiling (ACP)**, an agent‑based framework that restores clinical construct validity to automated Alzheimer’s disease (AD) screening by decomposing standardized assessments into atomic cognitive tasks and assigning dedicated LLM agents to extract verifiable scoring primitives via deterministic function calls. By separating semantic interpretation from measurement, ACP avoids hallucination, produces interpretable cognitive profiles, and is evaluated on a clinically annotated dataset of 402 participants across eight tasks, achieving a 90.5 % task‑score match rate and 85.3 % AD‑prediction accuracy—outperforming conventional end‑to‑end baselines. The results demonstrate that agentic orchestration can simultaneously preserve domain‑specific construct validity and deliver high predictive performance in health‑focused AI systems.


<details>
<summary>Abstract</summary>

Automated Alzheimer's Disease (AD) screening has predominantly followed the inductive paradigm of pattern recognition, which directly maps the input signal to the outcome label. This paradigm sacrifices construct validity of clinical protocol for statistical shortcuts. This paper proposes Agentic Cognitive Profiling (ACP), an agentic framework that realigns automated screening with clinical protocol logic across multiple cognitive domains. Rather than learning opaque mappings from transcripts to labels, the framework decomposes standardized assessments into atomic cognitive tasks and orchestrates specialized LLM agents to extract verifiable scoring primitives. Central to our design is decoupling semantic understanding from measurement by delegating all quantification to deterministic function calling, thereby mitigating hallucination and restoring construct validity. Unlike popular datasets that typically comprise around a hundred participants under a single task, we evaluate on a clinically-annotated corpus of 402 participants across eight structured cognitive tasks spanning multiple cognitive domains. The framework achieves 90.5% score match rate in task examination and 85.3% accuracy in AD prediction, surpassing popular baselines while generating interpretable cognitive profiles grounded in behavioral evidence. This work demonstrates that construct validity and predictive performance need not be traded off, charting a path toward AD screening systems that explain rather than merely predict.

</details>


### 82. ReLMXEL: Adaptive RL-Based Memory Controller with Explainable Energy and Latency Optimization

- **Authors:** Panuganti Chirag Sai, Gandholi Sarat, R. Raghunatha Sarma, Venkata Kalyan Tavva, Naveen M
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17309v1](http://arxiv.org/abs/2603.17309v1)
- **PDF:** [https://arxiv.org/pdf/2603.17309v1](https://arxiv.org/pdf/2603.17309v1)
- **Categories:** cs.AR, cs.AI, cs.LG, cs.MA, eess.SY


> ReLMXEL introduces an explainable multi‑agent reinforcement‑learning controller that continuously tunes memory‑controller parameters to minimize latency and energy consumption. The framework decomposes the reward into separate energy‑ and latency‑related components, allowing each agent to learn policies from fine‑grained memory‑access metrics while producing human‑readable explanations of its actions. Across a suite of heterogeneous workloads, ReLMXEL achieves consistent latency‑ and energy‑reductions over static baselines, demonstrating that reward‑decomposed, transparent RL agents can adaptively and audibly optimize low‑level hardware resources.


<details>
<summary>Abstract</summary>

Reducing latency and energy consumption is critical to improving the efficiency of memory systems in modern computing. This work introduces ReLMXEL (Reinforcement Learning for Memory Controller with Explainable Energy and Latency Optimization), a explainable multi-agent online reinforcement learning framework that dynamically optimizes memory controller parameters using reward decomposition. ReLMXEL operates within the memory controller, leveraging detailed memory behavior metrics to guide decision-making. Experimental evaluations across diverse workloads demonstrate consistent performance gains over baseline configurations, with refinements driven by workload-specific memory access behaviour. By incorporating explainability into the learning process, ReLMXEL not only enhances performance but also increases the transparency of control decisions, paving the way for more accountable and adaptive memory system designs.

</details>


### 83. Symphony: A Cognitively-Inspired Multi-Agent System for Long-Video Understanding

- **Authors:** Haiyang Yan, Hongyun Zhou, Peng Xu, Xiaoxue Feng, Mengyi Liu
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17307v1](http://arxiv.org/abs/2603.17307v1)
- **PDF:** [https://arxiv.org/pdf/2603.17307v1](https://arxiv.org/pdf/2603.17307v1)
- **Categories:** cs.CV, cs.AI


> Symphony introduces a cognitively‑inspired multi‑agent framework that tackles long‑form video understanding (LVU) by breaking videos into fine‑grained subtasks and enabling deep, reflective collaboration among specialized agents. It combines task‑level decomposition with a vision‑language model (VLM) grounding module that evaluates segment relevance, thereby preserving critical information that simple retrieval‑based reductions miss. Across four LVU benchmarks (LVBench, LongVideoBench, VideoMME, MLVU), Symphony sets new state‑of‑the‑art results, improving the best prior score on LVBench by 5 % and demonstrating that reflective, multi‑agent reasoning markedly enhances agentic AI performance on temporally extensive, information‑dense visual tasks.


<details>
<summary>Abstract</summary>

Despite rapid developments and widespread applications of MLLM agents, they still struggle with long-form video understanding (LVU) tasks, which are characterized by high information density and extended temporal spans. Recent research on LVU agents demonstrates that simple task decomposition and collaboration mechanisms are insufficient for long-chain reasoning tasks. Moreover, directly reducing the time context through embedding-based retrieval may lose key information of complex problems. In this paper, we propose Symphony, a multi-agent system, to alleviate these limitations. By emulating human cognition patterns, Symphony decomposes LVU into fine-grained subtasks and incorporates a deep reasoning collaboration mechanism enhanced by reflection, effectively improving the reasoning capability. Additionally, Symphony provides a VLM-based grounding approach to analyze LVU tasks and assess the relevance of video segments, which significantly enhances the ability to locate complex problems with implicit intentions and large temporal spans. Experimental results show that Symphony achieves state-of-the-art performance on LVBench, LongVideoBench, VideoMME, and MLVU, with a 5.0% improvement over the prior state-of-the-art method on LVBench. Code is available at https://github.com/Haiyang0226/Symphony.

</details>


### 84. Graph-Native Cognitive Memory for AI Agents: Formal Belief Revision Semantics for Versioned Memory Architectures

- **Authors:** Young Bin Park
- **Published:** 2026-03-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17244v1](http://arxiv.org/abs/2603.17244v1)
- **PDF:** [https://arxiv.org/pdf/2603.17244v1](https://arxiv.org/pdf/2603.17244v1)
- **Categories:** cs.AI, cs.IR, cs.LO


> The paper introduces **Kumiho**, a graph‑native cognitive memory system that unifies mutable working memory and versioned long‑term storage under a formal belief‑revision semantics, proving that its operational rules satisfy the AGM postulates (K*2–K*6) and Hansson’s relevance and core‑retainment criteria. By implementing a dual‑store architecture (Redis + Neo4j) with prospective indexing, event‑level extraction, and client‑side LLM reranking, Kumiho achieves state‑of‑the‑art performance on the LoCoMo benchmark (0.565 F1, 97.5 % adversarial refusal) and a 93.3 % judge accuracy on the more demanding LoCoMo‑Plus, far surpassing prior baselines. The results demonstrate that formally grounded, graph‑based memory can dramatically improve an agent’s ability to recall constraints, handle adversarial queries, and adapt to different LLM back‑ends with minimal engineering changes.


<details>
<summary>Abstract</summary>

While individual components for AI agent memory exist in prior systems, their architectural synthesis and formal grounding remain underexplored. We present Kumiho, a graph-native cognitive memory architecture grounded in formal belief revision semantics. The structural primitives required for cognitive memory -- immutable revisions, mutable tag pointers, typed dependency edges, URI-based addressing -- are identical to those required for managing agent-produced work as versionable assets, enabling a unified graph-native architecture that serves both purposes. The central formal contribution is a correspondence between the AGM belief revision framework and the operational semantics of a property graph memory system, proving satisfaction of the basic AGM postulates (K*2--K*6) and Hansson's belief base postulates (Relevance, Core-Retainment). The architecture implements a dual-store model (Redis working memory, Neo4j long-term graph) with hybrid fulltext and vector retrieval. On LoCoMo (token-level F1), Kumiho achieves 0.565 overall F1 (n=1,986) including 97.5% adversarial refusal accuracy. On LoCoMo-Plus, a Level-2 cognitive memory benchmark testing implicit constraint recall, Kumiho achieves 93.3% judge accuracy (n=401); independent reproduction by the benchmark authors yielded results in the mid-80% range, still substantially outperforming all published baselines (best: Gemini 2.5 Pro, 45.7%). Three architectural innovations drive the results: prospective indexing (LLM-generated future-scenario implications indexed at write time), event extraction (structured causal events preserved in summaries), and client-side LLM reranking. The architecture is model-decoupled: switching the answer model from GPT-4o-mini (~88%) to GPT-4o (93.3%) improves end-to-end accuracy without pipeline changes, at a total evaluation cost of ~$14 for 401 entries.

</details>


### 85. AI Scientist via Synthetic Task Scaling

- **Authors:** Ziyang Cai, Harkirat Behl
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17216v1](http://arxiv.org/abs/2603.17216v1)
- **PDF:** [https://arxiv.org/pdf/2603.17216v1](https://arxiv.org/pdf/2603.17216v1)
- **Categories:** cs.AI


> The paper introduces a fully automated pipeline that generates synthetic machine‑learning research tasks—complete with topic selection, dataset specification (validated via the HuggingFace API), and starter code—so that AI agents can be trained by “learning from doing.” Using this pipeline, the authors collect expert trajectories from a GPT‑5 teacher and fine‑tune smaller LLM agents (Qwen‑3 4B/8B) within the SWE‑agent framework, then evaluate them on the MLGym benchmark. The resulting student agents achieve substantially higher scientific‑discovery performance, improving the AUP metric by 9 % (4B) and 12 % (8B), demonstrating that high‑quality synthetic tasks can effectively bootstrap agentic AI for automated ML research.


<details>
<summary>Abstract</summary>

With the advent of AI agents, automatic scientific discovery has become a tenable goal. Many recent works scaffold agentic systems that can perform machine learning research, but don't offer a principled way to train such agents -- and current LLMs often generate plausible-looking but ineffective ideas. To make progress on training agents that can learn from doing, we provide a novel synthetic environment generation pipeline targeting machine learning agents. Our pipeline automatically synthesizes machine learning challenges compatible with the SWE-agent framework, covering topic sampling, dataset proposal, and code generation. The resulting synthetic tasks are 1) grounded in real machine learning datasets, because the proposed datasets are verified against the Huggingface API and are 2) verified for higher quality with a self-debugging loop. To validate the effectiveness of our synthetic tasks, we tackle MLGym, a benchmark for machine learning tasks. From the synthetic tasks, we sample trajectories from a teacher model (GPT-5), then use the trajectories to train a student model (Qwen3-4B and Qwen3-8B). The student models trained with our synthetic tasks achieve improved performance on MLGym, raising the AUP metric by 9% for Qwen3-4B and 12% for Qwen3-8B.

</details>


### 86. CODMAS: A Dialectic Multi-Agent Collaborative Framework for Structured RTL Optimization

- **Authors:** Che-Ming Chang, Prashanth Vijayaraghavan, Ashutosh Jadhav, Charles Mackin, Vandana Mukherjee, Hsinyu Tsai, Ehsan Degan
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17204v1](http://arxiv.org/abs/2603.17204v1)
- **PDF:** [https://arxiv.org/pdf/2603.17204v1](https://arxiv.org/pdf/2603.17204v1)
- **Categories:** cs.CL, cs.AR, cs.PL


> The paper introduces **CODMAS**, a dialectic multi‑agent framework that orchestrates structured reasoning and domain‑specific code generation to automate RTL optimization. It pairs an “Articulator” agent (which iteratively formulates transformation plans and surfaces hidden assumptions) with a “Hypothesis Partner” agent (which predicts performance outcomes and reconciles prediction‑execution gaps), directing a Domain‑Specific Coding Agent to produce Verilog edits and a Code Evaluation Agent to verify syntax, functionality, and PPA metrics. On the RTLOPT benchmark of 120 Verilog designs, CODMAS reduces critical‑path delay by ~25 % for pipelining and power by ~22 % for clock‑gating, while markedly lowering functional and compilation failures compared with strong‑prompting and existing agentic baselines, demonstrating the efficacy of structured dialectic reasoning for scalable, agentic hardware‑design automation.


<details>
<summary>Abstract</summary>

Optimizing Register Transfer Level (RTL) code is a critical step in Electronic Design Automation (EDA) for improving power, performance, and area (PPA). We present CODMAS (Collaborative Optimization via a Dialectic Multi-Agent System), a framework that combines structured dialectic reasoning with domain-aware code generation and deterministic evaluation to automate RTL optimization. At the core of CODMAS are two dialectic agents: the Articulator, inspired by rubber-duck debugging, which articulates stepwise transformation plans and exposes latent assumptions; and the Hypothesis Partner, which predicts outcomes and reconciles deviations between expected and actual behavior to guide targeted refinements. These agents direct a Domain-Specific Coding Agent (DCA) to generate architecture-aware Verilog edits and a Code Evaluation Agent (CEA) to verify syntax, functionality, and PPA metrics. We introduce RTLOPT, a benchmark of 120 Verilog triples (unoptimized, optimized, testbench) for pipelining and clock-gating transformations. Across proprietary and open LLMs, CODMAS achieves ~25% reduction in critical path delay for pipelining and ~22% power reduction for clock gating, while reducing functional and compilation failures compared to strong prompting and agentic baselines. These results demonstrate that structured multi-agent reasoning can significantly enhance automated RTL optimization and scale to more complex designs and broader optimization tasks.

</details>


### 87. Tabular LLMs for Interpretable Few-Shot Alzheimer's Disease Prediction with Multimodal Biomedical Data

- **Authors:** Sophie Kearney, Shu Yang, Zixuan Wen, Weimin Lyu, Bojian Hou, Duy Duong-Tran, Tianlong Chen, Jason H. Moore, Marylyn D. Ritchie, Chao Chen, Li Shen
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17191v1](http://arxiv.org/abs/2603.17191v1)
- **PDF:** [https://arxiv.org/pdf/2603.17191v1](https://arxiv.org/pdf/2603.17191v1)
- **Categories:** cs.CL, cs.LG, q-bio.QM


> The paper introduces **TAP‑GPT**, a domain‑adapted tabular large language model that treats multimodal biomedical biomarkers as structured prompts to perform few‑shot Alzheimer’s disease classification. By fine‑tuning TableGPT‑2 on ADNI‑derived tabular data (clinical labs, region‑level MRI, amyloid and tau PET) and incorporating feature‑selection and self‑reflection mechanisms, TAP‑GPT outperforms classical machine‑learning baselines and its own backbone in low‑sample, missing‑data regimes while generating modality‑aware, biologically grounded reasoning traces. These results demonstrate that tabular‑specialized LLMs can serve as interpretable, self‑reflective agents for clinical decision‑support, paving the way for multi‑agent AI systems that reason over structured health data.


<details>
<summary>Abstract</summary>

Accurate diagnosis of Alzheimer's disease (AD) requires handling tabular biomarker data, yet such data are often small and incomplete, where deep learning models frequently fail to outperform classical methods. Pretrained large language models (LLMs) offer few-shot generalization, structured reasoning, and interpretable outputs, providing a powerful paradigm shift for clinical prediction. We propose TAP-GPT Tabular Alzheimer's Prediction GPT, a domain-adapted tabular LLM framework built on TableGPT2 and fine-tuned for few-shot AD classification using tabular prompts rather than plain texts. We evaluate TAP-GPT across four ADNI-derived datasets, including QT-PAD biomarkers and region-level structural MRI, amyloid PET, and tau PET for binary AD classification. Across multimodal and unimodal settings, TAP-GPT improves upon its backbone models and outperforms traditional machine learning baselines in the few-shot setting while remaining competitive with state-of-the-art general-purpose LLMs. We show that feature selection mitigates degradation in high-dimensional inputs and that TAP-GPT maintains stable performance under simulated and real-world missingness without imputation. Additionally, TAP-GPT produces structured, modality-aware reasoning aligned with established AD biology and shows greater stability under self-reflection, supporting its use in iterative multi-agent systems. To our knowledge, this is the first systematic application of a tabular-specialized LLM to multimodal biomarker-based AD prediction, demonstrating that such pretrained models can effectively address structured clinical prediction tasks and laying the foundation for tabular LLM-driven multi-agent clinical decision-support systems. The source code is publicly available on GitHub: https://github.com/sophie-kearney/TAP-GPT.

</details>


### 88. Ablation Study of a Fairness Auditing Agentic System for Bias Mitigation in Early-Onset Colorectal Cancer Detection

- **Authors:** Amalia Ionescu, Jose Guadalupe Hernandez, Jui-Hsuan Chang, Emily F. Wong, Paul Wang, Jason H. Moore, Tiffani J. Bright
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17179v1](http://arxiv.org/abs/2603.17179v1)
- **PDF:** [https://arxiv.org/pdf/2603.17179v1](https://arxiv.org/pdf/2603.17179v1)
- **Categories:** cs.MA


> The paper introduces a two‑agent framework— a Domain‑Expert Agent that curates literature on early‑onset colorectal‑cancer (EO‑CRC) disparities and a Fairness‑Consultant Agent that proposes sensitive attributes and fairness metrics for auditing biomedical ML models. By conducting an ablation study across three Ollama LLM sizes (8 B, 20 B, 120 B) and three system configurations (LLM‑only, Agent without retrieval‑augmented generation, Agent with RAG), the authors show that the RAG‑enabled agent consistently yields the highest semantic similarity to expert‑derived references, especially in identifying demographic disparities. These results suggest that retrieval‑augmented, agentic AI can reliably scale fairness auditing for clinical decision‑support systems.


<details>
<summary>Abstract</summary>

Artificial intelligence (AI) is increasingly used in clinical settings, yet limited oversight and domain expertise can allow algorithmic bias and safety risks to persist. This study evaluates whether an agentic AI system can support auditing biomedical machine learning models for fairness in early-onset colorectal cancer (EO-CRC), a condition with documented demographic disparities. We implemented a two-agent architecture consisting of a Domain Expert Agent that synthesizes literature on EO-CRC disparities and a Fairness Consultant Agent that recommends sensitive attributes and fairness metrics for model evaluation. An ablation study compared three Ollama large language models (8B, 20B, and 120B parameters) across three configurations: pretrained LLM-only, Agent without Retrieval-Augmented Generation (RAG), and Agent with RAG. Across models, the Agent with RAG achieved the highest semantic similarity to expert-derived reference statements, particularly for disparity identification, suggesting agentic systems with retrieval may help scale fairness auditing in clinical AI.

</details>


### 89. PAuth - Precise Task-Scoped Authorization For Agents

- **Authors:** Reshabh K Sharma, Linxi Jiang, Zhiqiang Lin, Shuo Chen
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17170v1](http://arxiv.org/abs/2603.17170v1)
- **PDF:** [https://arxiv.org/pdf/2603.17170v1](https://arxiv.org/pdf/2603.17170v1)
- **Categories:** cs.CR, cs.AI, cs.PL


> The paper introduces **PAuth**, a novel “task‑scoped” authorization model that grants AI agents permission only for the exact web‑service operations required to fulfill a user’s natural‑language request, eliminating the over‑privilege inherent in operator‑scoped schemes like OAuth. The authors implement PAuth in the AgentDojo framework by (1) generating **NL slices**—symbolic specifications of the precise API calls a service expects based on the task and upstream results—and (2) attaching **envelopes** that bind each concrete operand to its symbolic provenance, enabling servers to verify that every input originates from an authorized computation. Experiments on benign tasks show PAuth executes without extra permissions, while attack scenarios that inject spurious operations are consistently flagged, demonstrating that PAuth can precisely enforce fine‑grained, task‑level permissions for agentic AI systems.


<details>
<summary>Abstract</summary>

The emerging agentic web envisions AI agents that reliably fulfill users' natural-language (NL)-based tasks by interacting with existing web services. However, existing authorization models are misaligned with this vision. In particular, today's operator-scoped authorization, exemplified by OAuth, grants broad permissions tied to operators (e.g., the transfer operator) rather than to the specific operations (e.g., transfer $100 to Bob) implied by a user's task. This will inevitably result in overprivileged agents.
  We introduce Precise Task-Scoped Implicit Authorization (PAuth), a fundamentally different model in which submitting an NL task implicitly authorizes only the concrete operations required for its faithful execution. To make this enforceable at servers, we propose NL slices: symbolic specifications of the calls each service expects, derived from the task and upstream results. Complementing this, we also propose envelopes: special data structure to bind each operand's concrete value to its symbolic provenance, enabling servers to verify that all operands arise from legitimate computations.
  PAuth is prototyped in the agent-security evaluation framework AgentDojo. We evaluate it in both benign settings and attack scenarios where a spurious operation is injected into an otherwise normal task. In all benign tests, PAuth executes the tasks successfully without requiring any additional permissions. In all attack tests, PAuth correctly raises warnings about missing permissions. These results demonstrate that PAuth's reasoning about permissions is indeed precise. We further analyze the characteristics of these tasks and measure the associated token costs.

</details>


### 90. How Clued up are LLMs? Evaluating Multi-Step Deductive Reasoning in a Text-Based Game Environment

- **Authors:** Rebecca Ansell, Autumn Toney-Wails
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17169v1](http://arxiv.org/abs/2603.17169v1)
- **PDF:** [https://arxiv.org/pdf/2603.17169v1](https://arxiv.org/pdf/2603.17169v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces a rule‑based, text‑only implementation of the board game Clue as a benchmark for testing multi‑step deductive reasoning in large‑language‑model agents, evaluating six agents built from GPT‑4o‑mini and Gemini‑2.5‑Flash across 18 simulated games. By comparing baseline agents with versions fine‑tuned on structured logic‑puzzle data, the study shows that even state‑of‑the‑art LLM agents struggle to sustain coherent deduction throughout an entire game—only four agents achieve a correct win—and that fine‑tuning does not reliably boost performance, sometimes increasing the amount of reasoning without improving its accuracy. These results highlight a gap in current agentic AI’s ability to perform sustained, precise logical inference in interactive environments.


<details>
<summary>Abstract</summary>

Deducing whodunit proves challenging for LLM agents. In this paper, we implement a text-based multi-agent version of the classic board game Clue as a rule-based testbed for evaluating multi-step deductive reasoning, with six agents drawn from GPT-4o-mini and Gemini-2.5-Flash. We further investigate whether fine-tuning on structured logic puzzles transfers to improved in-game reasoning and gameplay. Across 18 simulated games, agents achieve only four correct wins, indicating difficulty in maintaining consistent deductive reasoning over the course of a full game. Additionally, we find that fine-tuning does not reliably improve performance and, in some cases, appears to increase reasoning volume without improving reasoning precision.

</details>


### 91. Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents

- **Authors:** Shuvendu K. Lahiri
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17150v1](http://arxiv.org/abs/2603.17150v1)
- **PDF:** [https://arxiv.org/pdf/2603.17150v1](https://arxiv.org/pdf/2603.17150v1)
- **Categories:** cs.SE, cs.AI, cs.PL


> The paper argues that **intent formalization**—automatically converting a user’s informal natural‑language request into precise, checkable specifications—is the decisive bottleneck for making AI‑generated code trustworthy. It surveys emerging methods such as interactive test‑driven refinement, AI‑produced postconditions, and end‑to‑end pipelines that synthesize code from domain‑specific formal languages, showing that even lightweight specification checks can markedly improve correctness and that full formal verification can yield provably correct programs. The authors identify the central research challenges—scalable specification validation, compositional handling of changes, metric design, and human‑AI interaction for specification creation—thereby charting a roadmap for the agentic AI community to bridge the “intent gap” and deliver reliable, specification‑driven code generation.


<details>
<summary>Abstract</summary>

Agentic AI systems can now generate code with remarkable fluency, but a fundamental question remains: \emph{does the generated code actually do what the user intended?} The gap between informal natural language requirements and precise program behavior -- the \emph{intent gap} -- has always plagued software engineering, but AI-generated code amplifies it to an unprecedented scale. This article argues that \textbf{intent formalization} -- the translation of informal user intent into a set of checkable formal specifications -- is the key challenge that will determine whether AI makes software more reliable or merely more abundant. Intent formalization offers a tradeoff spectrum suitable to the reliability needs of different contexts: from lightweight tests that disambiguate likely misinterpretations, through full functional specifications for formal verification, to domain-specific languages from which correct code is synthesized automatically. The central bottleneck is \emph{validating specifications}: since there is no oracle for specification correctness other than the user, we need semi-automated metrics that can assess specification quality with or without code, through lightweight user interaction and proxy artifacts such as tests. We survey early research that demonstrates the \emph{potential} of this approach: interactive test-driven formalization that improves program correctness, AI-generated postconditions that catch real-world bugs missed by prior methods, and end-to-end verified pipelines that produce provably correct code from informal specifications. We outline the open research challenges -- scaling beyond benchmarks, achieving compositionality over changes, metrics for validating specifications, handling rich logics, designing human-AI specification interactions -- that define a research agenda spanning AI, programming languages, formal methods, and human-computer interaction.

</details>


### 92. Cascade-Aware Multi-Agent Routing: Spatio-Temporal Sidecars and Geometry-Switching

- **Authors:** Davide Di Gioia
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17112v1](http://arxiv.org/abs/2603.17112v1)
- **PDF:** [https://arxiv.org/pdf/2603.17112v1](https://arxiv.org/pdf/2603.17112v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces a lightweight “geometry‑aware” routing sidecar that equips symbolic graph‑based AI reasoning systems with online, cascade‑sensitive risk estimation, allowing them to adaptively switch between Euclidean and hyperbolic propagation models based on the current execution‑graph topology. The method augments a standard bandit scheduler with a compact MLP selector (9→12→1) that consumes six basic graph statistics plus three geometry‑specific signals (BFS shell‑growth slope, cycle‑rank norm, and fitted Poincaré curvature) to choose the most appropriate risk model for each time‑indexed delegation edge. Empirically on the Genesis‑3 benchmark, the sidecar raises overall win rates from 50.4 % to 87.2 % (a +36.8 pp gain) and boosts performance in tree‑like regimes by up to 68 pp, demonstrating that geometry‑aware routing dramatically curtails cascade failures in multi‑agent AI execution graphs.


<details>
<summary>Abstract</summary>

A common architectural pattern in advanced AI reasoning systems is the symbolic graph network: specialized agents or modules connected by delegation edges, routing tasks through a dynamic execution graph. Current schedulers optimize load and fitness but are geometry-blind: they do not model how failures propagate differently in tree-like versus cyclic regimes. In tree-like delegation, a single failure can cascade exponentially; in dense cyclic graphs, failures tend to self-limit. We identify this observability gap, quantify its system-level cost, and propose a lightweight mitigation.
  We formulate online geometry control for route-risk estimation on time-indexed execution graphs with route-local failure history. Our approach combines (i) a Euclidean spatio-temporal propagation baseline, (ii) a hyperbolic route-risk model with temporal decay (and optional burst excitation), and (iii) a learned geometry selector over structural features. The selector is a compact MLP (9->12->1) using six topology statistics plus three geometry-aware signals: BFS shell-growth slope, cycle-rank norm, and fitted Poincare curvature. On the Genesis 3 benchmark distribution, adaptive switching improves win rate in the hardest non_tree regime from 64-72% (fixed hyperbolic variants) to 92%, and achieves 87.2% overall win rate.
  To measure total system value, we compare against Genesis 3 routing without any spatio-temporal sidecar, using only native bandit/LinUCB signals (team fitness and mean node load). This baseline achieves 50.4% win rate overall and 20% in tree-like regimes; the full sidecar recovers 87.2% overall (+36.8 pp), with +48 to +68 pp gains in tree-like settings, consistent with a cascade-sensitivity analysis. Overall, a 133-parameter sidecar substantially mitigates geometry-blind failure propagation in one high-capability execution-graph system.

</details>


### 93. Asymmetric Nash Seeking via Best Response Maps: Global Linear Convergence and Robustness to Inexact Reaction Models

- **Authors:** Mahdis Rabbani, Navid Mojahed, Shima Nazari
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.17058v1](http://arxiv.org/abs/2603.17058v1)
- **PDF:** [https://arxiv.org/pdf/2603.17058v1](https://arxiv.org/pdf/2603.17058v1)
- **Categories:** cs.GT, cs.MA, cs.RO, eess.SY, math.OC


> The paper introduces an **asymmetric projected gradient–best‑response algorithm** for two‑player constrained games where only one player (Player 1) knows its own objective and constraints while the other (Player 2) is accessed solely through a best‑response map. Under standard monotonicity and regularity assumptions, the authors prove **existence, uniqueness, and global linear convergence** of the method when the best‑response is exact, and they extend the analysis to **inexact best‑response models**, showing that the iterates converge to an explicit \(O(\varepsilon)\) neighborhood of the true Nash equilibrium when the approximation error is uniformly bounded by \(\varepsilon\). Numerical experiments on a benchmark game confirm the predicted linear rate and the error‑scaling behavior, demonstrating that reliable Nash‑seeking is possible even with asymmetric information—a result directly relevant to designing robust, decentralized agentic AI systems.


<details>
<summary>Abstract</summary>

Nash equilibria provide a principled framework for modeling interactions in multi-agent decision-making and control. However, many equilibrium-seeking methods implicitly assume that each agent has access to the other agents' objectives and constraints, an assumption that is often unrealistic in practice. This letter studies a class of asymmetric-information two-player constrained games with decoupled feasible sets, in which Player 1 knows its own objective and constraints while Player 2 is available only through a best-response map. For this class of games, we propose an asymmetric projected gradient descent-best response iteration that does not require full mutual knowledge of both players' optimization problems. Under suitable regularity conditions, we establish the existence and uniqueness of the Nash equilibrium and prove global linear convergence of the proposed iteration when the best-response map is exact. Recognizing that best-response maps are often learned or estimated, we further analyze the inexact case and show that, when the approximation error is uniformly bounded by $\varepsilon$, the iterates enter an explicit $O(\varepsilon)$ neighborhood of the true Nash equilibrium. Numerical results on a benchmark game corroborate the predicted convergence behavior and error scaling.

</details>


### 94. Chronos: Temporal-Aware Conversational Agents with Structured Event Retrieval for Long-Term Memory

- **Authors:** Sahil Sen, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16862v1](http://arxiv.org/abs/2603.16862v1)
- **PDF:** [https://arxiv.org/pdf/2603.16862v1](https://arxiv.org/pdf/2603.16862v1)
- **Categories:** cs.CL


> Chronos introduces a temporal‑aware memory architecture for conversational agents that extracts subject‑verb‑object event tuples with resolved date ranges and entity aliases from dialogue, indexing them in a structured “event calendar” alongside a turn‑level calendar that retains full context. At query time, Chronos uses dynamic prompting to generate retrieval plans that guide multi‑hop, time‑sensitive searches across both calendars via an iterative tool‑calling loop, enabling the agent to reason over long‑term, evolving facts. Evaluated on the LongMemEvalS benchmark with eight LLMs, Chronos achieves 92.6 % (Low) and 95.6 % (High) accuracy—up to 7.7 % absolute improvement over the previous best—where the events calendar alone contributes a 58.9 % gain, demonstrating a substantial advance for agentic AI systems that require robust long‑term, temporally grounded memory.


<details>
<summary>Abstract</summary>

Recent advances in Large Language Models (LLMs) have enabled conversational AI agents to engage in extended multi-turn interactions spanning weeks or months. However, existing memory systems struggle to reason over temporally grounded facts and preferences that evolve across months of interaction and lack effective retrieval strategies for multi-hop, time-sensitive queries over long dialogue histories. We introduce Chronos, a novel temporal-aware memory framework that decomposes raw dialogue into subject-verb-object event tuples with resolved datetime ranges and entity aliases, indexing them in a structured event calendar alongside a turn calendar that preserves full conversational context. At query time, Chronos applies dynamic prompting to generate tailored retrieval guidance for each question, directing the agent on what to retrieve, how to filter across time ranges, and how to approach multi-hop reasoning through an iterative tool-calling loop over both calendars. We evaluate Chronos with 8 LLMs, both open-source and closed-source, on the LongMemEvalS benchmark comprising 500 questions spanning six categories of dialogue history tasks. Chronos Low achieves 92.60% and Chronos High scores 95.60% accuracy, setting a new state of the art with an improvement of 7.67% over the best prior system. Ablation results reveal the events calendar accounts for a 58.9% gain on the baseline while all other components yield improvements between 15.5% and 22.3%. Notably, Chronos Low alone surpasses prior approaches evaluated under their strongest model configurations.

</details>


### 95. Internalizing Agency from Reflective Experience

- **Authors:** Rui Ge, Yichao Fu, Yuyang Qian, Junda Su, Yiming Zhao, Peng Zhao, Hao Zhang
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16843v1](http://arxiv.org/abs/2603.16843v1)
- **PDF:** [https://arxiv.org/pdf/2603.16843v1](https://arxiv.org/pdf/2603.16843v1)
- **Categories:** cs.AI


> The paper introduces **LEAFE (Learning Feedback‑Grounded Agency from Reflective Experience)**, a training framework that teaches large language model agents to internalize “recovery agency” by explicitly reflecting on rich environment feedback rather than only on final success signals. During exploration the agent records feedback, backtracks to earlier decision points, and generates alternative action branches; these reflective corrections are then distilled into the model via supervised fine‑tuning. Experiments on interactive coding and other long‑horizon agentic tasks show that LEAFE consistently raises Pass@1 and achieves up to a 14 % improvement on Pass@128 compared with outcome‑driven baselines (e.g., GRPO) and prior experience‑based methods, demonstrating more robust, feedback‑driven problem‑solving.


<details>
<summary>Abstract</summary>

Large language models are increasingly deployed as autonomous agents that must plan, act, and recover from mistakes through long-horizon interaction with environments that provide rich feedback. However, prevailing outcome-driven post-training methods (e.g., RL with verifiable rewards) primarily optimize final success signals, leaving rich environment feedback underutilized. Consequently, they often lead to distribution sharpening: the policy becomes better at reproducing a narrow set of already-successful behaviors, while failing to improve the feedback-grounded agency needed to expand problem-solving capacity (e.g., Pass@k) in long-horizon settings.
  To address this, we propose LEAFE (Learning Feedback-Grounded Agency from Reflective Experience), a framework that internalizes recovery agency from reflective experience. Specifically, during exploration, the agent summarizes environment feedback into actionable experience, backtracks to earlier decision points, and explores alternative branches with revised actions. We then distill these experience-guided corrections into the model through supervised fine-tuning, enabling the policy to recover more effectively in future interactions. Across a diverse set of interactive coding and agentic tasks under fixed interaction budgets, LEAFE consistently improves Pass@1 over the base model and achieves higher Pass@k than outcome-driven baselines (GRPO) and experience-based methods such as Early Experience, with gains of up to 14% on Pass@128.

</details>


### 96. Learning to Present: Inverse Specification Rewards for Agentic Slide Generation

- **Authors:** Karthik Ragunath Ananda Kumar, Subrahmanyam Arunachalam
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16839v1](http://arxiv.org/abs/2603.16839v1)
- **PDF:** [https://arxiv.org/pdf/2603.16839v1](https://arxiv.org/pdf/2603.16839v1)
- **Categories:** cs.AI


> The paper introduces **SlideRL**, an OpenAI‑Gym‑style reinforcement‑learning environment that lets LLM agents autonomously research a topic, plan a narrative, and produce fully‑rendered HTML slide decks using external tools. By fine‑tuning Qwen2.5‑Coder‑7B with GRPO on a tiny (0.5 % of parameters) set of expert demonstrations, the authors add a novel **inverse specification reward**—an auxiliary task where a second LLM tries to reconstruct the original brief from the generated slides—to provide a holistic signal of purpose fidelity alongside structural, aesthetic, and content metrics. Experiments on 48 business briefs show the fine‑tuned 7 B model reaches 91 % of Claude Opus 4.6’s quality while outperforming its base model by 33 %, and the study highlights that adherence to instructions and tool‑use compliance, rather than sheer model size, drive high‑performing agentic behavior.


<details>
<summary>Abstract</summary>

Automated presentation generation remains a challenging task requiring coherent content creation, visual design, and audience-aware communication. This work proposes an OpenEnv-compatible reinforcement learning environment where LLM agents learn to research topics, plan content, and generate professional HTML slide presentations through tool use. We introduce a multi-component reward system combining structural validation, render quality assessment, LLM-based aesthetic scoring, content quality metrics, and an inverse specification reward that measures how faithfully generated slides convey their intended purpose. The inverse specification reward, an "inverse task" where an LLM attempts to recover the original specification from generated slides, provides a holistic quality signal. Our approach fine-tunes Qwen2.5-Coder-7B via GRPO, training only 0.5% of parameters on prompts derived from expert demonstrations collected using Claude Opus 4.6. Experiments on 48 diverse business briefs across six models demonstrate that our fine-tuned 7B model achieves 91.2% of Claude Opus 4.6's quality while improving 33.1% over the base model. The six-model comparison reveals that instruction adherence and tool-use compliance, rather than raw parameter count, determine agentic task performance. We contribute SlideRL, an open-source dataset of 288 multi-turn rollout trajectories across all six models: https://huggingface.co/datasets/KarthikRagunathAnandaKumar/sliderl-multi-turn-rollouts Code: https://github.com/pushing-the-frontier/slide-forge-llm

</details>


### 97. Anticipatory Planning for Multimodal AI Agents

- **Authors:** Yongyuan Liang, Shijie Zhou, Yu Gu, Hao Tan, Gang Wu, Franck Dernoncourt, Jihyung Kil, Ryan A. Rossi, Ruiyi Zhang
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16777v1](http://arxiv.org/abs/2603.16777v1)
- **PDF:** [https://arxiv.org/pdf/2603.16777v1](https://arxiv.org/pdf/2603.16777v1)
- **Categories:** cs.AI


> The paper introduces **TraceR1**, a two‑stage reinforcement‑learning framework that endows multimodal AI agents with anticipatory planning: first, a trajectory‑level RL phase learns to predict short‑horizon action sequences that satisfy global consistency constraints; second, a grounded fine‑tuning phase refines each step using execution feedback from frozen tool agents to ensure executability. By explicitly training agents to forecast and evaluate future states before acting, TraceR1 markedly improves planning coherence, execution robustness, and out‑of‑distribution generalization on seven computer‑use and multimodal tool‑use benchmarks, outperforming reactive and single‑stage baselines. These results demonstrate that anticipatory trajectory reasoning is a crucial design principle for building more reliable, goal‑directed agentic AI systems.


<details>
<summary>Abstract</summary>

Recent advances in multimodal agents have improved computer-use interaction and tool-usage, yet most existing systems remain reactive, optimizing actions in isolation without reasoning about future states or long-term goals. This limits planning coherence and prevents agents from reliably solving high-level, multi-step tasks. We introduce TraceR1, a two-stage reinforcement learning framework that explicitly trains anticipatory reasoning by forecasting short-horizon trajectories before execution. The first stage performs trajectory-level reinforcement learning with rewards that enforce global consistency across predicted action sequences. The second stage applies grounded reinforcement fine-tuning, using execution feedback from frozen tool agents to refine step-level accuracy and executability. TraceR1 is evaluated across seven benchmarks, covering online computer-use, offline computer-use benchmarks, and multimodal tool-use reasoning tasks, where it achieves substantial improvements in planning stability, execution robustness, and generalization over reactive and single-stage baselines. These results show that anticipatory trajectory reasoning is a key principle for building multimodal agents that can reason, plan, and act effectively in complex real-world environments.

</details>


### 98. Nonstandard Errors in AI Agents

- **Authors:** Ruijiang Gao, Steven Chong Xiao
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16744v2](http://arxiv.org/abs/2603.16744v2)
- **PDF:** [https://arxiv.org/pdf/2603.16744v2](https://arxiv.org/pdf/2603.16744v2)
- **Categories:** cs.AI, cs.SI


> The paper demonstrates that even when given identical data and research questions, state‑of‑the‑art AI coding agents produce markedly different empirical results—a phenomenon the authors term **nonstandard errors (NSEs)**, mirroring the methodological variance observed among human researchers. By deploying 150 autonomous Claude Code agents to test six hypotheses on NYSE TAQ data for SPY (2015‑2024), the study uncovers systematic “empirical styles” across model families (e.g., Sonnet 4.6 vs. Opus 4.6) and shows that AI peer‑review comments have little impact on dispersion, whereas exposure to top‑rated exemplar papers can shrink the interquartile range of estimates by 80‑99 % through imitation rather than genuine understanding. These findings highlight a previously underappreciated source of uncertainty in agentic AI pipelines and suggest that convergence mechanisms must be carefully designed to avoid superficial alignment.


<details>
<summary>Abstract</summary>

We study whether state-of-the-art AI coding agents, given the same data and research question, produce the same empirical results. Deploying 150 autonomous Claude Code agents to independently test six hypotheses about market quality trends in NYSE TAQ data for SPY (2015--2024), we find that AI agents exhibit sizable \textit{nonstandard errors} (NSEs), that is, uncertainty from agent-to-agent variation in analytical choices, analogous to those documented among human researchers. AI agents diverge substantially on measure choice (e.g., autocorrelation vs.\ variance ratio, dollar vs.\ share volume). Different model families (Sonnet 4.6 vs.\ Opus 4.6) exhibit stable ``empirical styles,'' reflecting systematic differences in methodological preferences. In a three-stage feedback protocol, AI peer review (written critiques) has minimal effect on dispersion, whereas exposure to top-rated exemplar papers reduces the interquartile range of estimates by 80--99\% within \textit{converging} measure families. Convergence occurs both through within-family estimation tightening and through agents switching measure families entirely, but convergence reflects imitation rather than understanding. These findings have implications for the growing use of AI in automated policy evaluation and empirical research.

</details>


### 99. Differential Harm Propensity in Personalized LLM Agents: The Curious Case of Mental Health Disclosure

- **Authors:** Caglar Yildirim
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16734v1](http://arxiv.org/abs/2603.16734v1)
- **PDF:** [https://arxiv.org/pdf/2603.16734v1](https://arxiv.org/pdf/2603.16734v1)
- **Categories:** cs.AI


> The paper introduces a personalization‑aware safety evaluation for LLM‑based agents, showing how a user’s mental‑health disclosure—a realistic, sensitive context cue—modulates the agents’ propensity to complete harmful tasks. By extending the AgentHarm benchmark, the authors run multi‑step malicious and benign tasks on frontier (GPT‑5.2, Claude Sonnet 4.5, Gemini 3‑Pro) and open‑source (DeepSeek 3.2) models under three prompt conditions (no bio, bio‑only, bio + mental‑health disclosure) and with a lightweight jailbreak injection, measuring refusal rates and task‑completion success. They find that personalization can modestly increase refusals and reduce harmful completions, but the effect is fragile: it disappears under jailbreak prompting and sometimes harms utility by over‑refusing even benign requests, underscoring the need for robustness‑focused, context‑sensitive safeguards in agentic AI systems.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as tool-using agents, shifting safety concerns from harmful text generation to harmful task completion. Deployed systems often condition on user profiles or persistent memory, yet agent safety evaluations typically ignore personalization signals. To address this gap, we investigated how mental health disclosure, a sensitive and realistic user-context cue, affects harmful behavior in agentic settings. Building on the AgentHarm benchmark, we evaluated frontier and open-source LLMs on multi-step malicious tasks (and their benign counterparts) under controlled prompt conditions that vary user-context personalization (no bio, bio-only, bio+mental health disclosure) and include a lightweight jailbreak injection. Our results reveal that harmful task completion is non-trivial across models: frontier lab models (e.g., GPT 5.2, Claude Sonnet 4.5, Gemini 3-Pro) still complete a measurable fraction of harmful tasks, while an open model (DeepSeek 3.2) exhibits substantially higher harmful completion. Adding a bio-only context generally reduces harm scores and increases refusals. Adding an explicit mental health disclosure often shifts outcomes further in the same direction, though effects are modest and not uniformly reliable after multiple-testing correction. Importantly, the refusal increase also appears on benign tasks, indicating a safety--utility trade-off via over-refusal. Finally, jailbreak prompting sharply elevates harm relative to benign conditions and can weaken or override the protective shift induced by personalization. Taken together, our results indicate that personalization can act as a weak protective factor in agentic misuse settings, but it is fragile under minimal adversarial pressure, highlighting the need for personalization-aware evaluations and safeguards that remain robust across user-context conditions.

</details>


### 100. When Openclaw Agents Learn from Each Other: Insights from Emergent AI Agent Communities for Human-AI Partnership in Education

- **Authors:** Eason Chen, Ce Guan, Ahmed Elshafiey, Zhonghao Zhao, Joshua Zekeri, Afeez Edeifo Shaibu, Emmanuel Osadebe Prince, Cyuan-Jhen Wu
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16663v2](http://arxiv.org/abs/2603.16663v2)
- **PDF:** [https://arxiv.org/pdf/2603.16663v2](https://arxiv.org/pdf/2603.16663v2)
- **Categories:** cs.CY, cs.AI, cs.HC, cs.MA


> The paper’s main contribution is a naturalistic case study of a large, self‑organizing ecosystem of over 167 k AI agents (across platforms such as Moltbook, The Colony, and 4claw) that interact as peers, revealing emergent social‑learning dynamics that can inform the design of agentic AI teammates in education. By conducting a month‑long series of daily qualitative observations of agent interactions, the authors identify four salient phenomena: (1) “bidirectional scaffolding” where humans learn while configuring agents; (2) spontaneous peer learning with idea cascades and emergent quality hierarchies despite the absence of a curriculum; (3) convergence on shared memory architectures resembling open learner models; and (4) trust and platform‑mortality patterns that expose design constraints for networked educational AI. These findings suggest that multi‑agent communities can generate curriculum‑free, self‑regulating learning environments, offering concrete design insights (e.g., “learn by teaching your AI teammate”) and a roadmap for future research on collaborative, agentic AI in educational settings.


<details>
<summary>Abstract</summary>

The AIED community envisions AI evolving "from tools to teammates," yet our understanding of AI teammates remains limited to dyadic human-AI interactions. We offer a different vantage point: a rapidly growing ecosystem of AI agent platforms where over 167,000 agents participate, interact as peers, and develop learning behaviors without researcher intervention. Drawing on a month of daily qualitative observations across multiple platforms including Moltbook, The Colony, and 4claw, we identify four phenomena with implications for AIED: (1) humans who configure their agents undergo a "bidirectional scaffolding" process, learning through teaching; (2) peer learning emerges without any designed curriculum, complete with idea cascades and quality hierarchies; (3) agents converge on shared memory architectures that mirror open learner model design; and (4) trust dynamics and platform mortality reveal design constraints for networked educational AI. Rather than presenting empirical findings, we argue that these organic phenomena offer a naturalistic window into dynamics that can inform principled design of multi-agent educational systems. We sketch an illustrative curriculum design, "Learn by Teaching Your AI Agent Teammate," and outline potential research directions and open problems to show how these observations might inform future AIED practice and inquiry.

</details>


### 101. Runtime Governance for AI Agents: Policies on Paths

- **Authors:** Maurits Kaptein, Vassilis-Javed Khan, Andriy Podstavnychy
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16586v1](http://arxiv.org/abs/2603.16586v1)
- **PDF:** [https://arxiv.org/pdf/2603.16586v1](https://arxiv.org/pdf/2603.16586v1)
- **Categories:** cs.AI


> The paper introduces a formal framework for **runtime governance of LLM‑driven AI agents**, treating the agent’s execution trace (the “path”) as the primary object of control. It defines compliance policies as deterministic functions that map an agent’s identity, the current partial path, a candidate next action, and the organization’s state to a probability of policy violation, thereby unifying prompt‑level steering and static access‑control as special cases and showing that only path‑aware, runtime evaluation can enforce truly path‑dependent regulations. Through concrete policy instances inspired by the AI Act and a reference implementation, the authors demonstrate that runtime evaluation can dynamically balance task success against legal, reputational, and security risks, while highlighting open challenges such as risk calibration and the theoretical limits of enforceable compliance.


<details>
<summary>Abstract</summary>

AI agents -- systems that plan, reason, and act using large language models -- produce non-deterministic, path-dependent behavior that cannot be fully governed at design time, where with governed we mean striking the right balance between as high as possible successful task completion rate and the legal, data-breach, reputational and other costs associated with running agents. We argue that the execution path is the central object for effective runtime governance and formalize compliance policies as deterministic functions mapping agent identity, partial path, proposed next action, and organizational state to a policy violation probability. We show that prompt-level instructions (and "system prompts"), and static access control are special cases of this framework: the former shape the distribution over paths without actually evaluating them; the latter evaluates deterministic policies that ignore the path (i.e., these can only account for a specific subset of all possible paths). In our view, runtime evaluation is the general case, and it is necessary for any path-dependent policy. We develop the formal framework for analyzing AI agent governance, present concrete policy examples (inspired by the AI act), discuss a reference implementation, and identify open problems including risk calibration and the limits of enforced compliance.

</details>


### 102. Malicious Or Not: Adding Repository Context to Agent Skill Classification

- **Authors:** Florian Holzbauer, David Schmidt, Gabriel Gegenhuber, Sebastian Schrittwieser, Johanna Ullrich
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16572v1](http://arxiv.org/abs/2603.16572v1)
- **PDF:** [https://arxiv.org/pdf/2603.16572v1](https://arxiv.org/pdf/2603.16572v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces a context‑aware pipeline that cross‑references AI‑agent skill metadata (SKILL.md) with the underlying GitHub repository, dramatically improving the reliability of automated malicious‑skill detection. By harvesting 238 k skills from three major marketplaces and GitHub, the authors show that incorporating repository‑level signals cuts false‑positive malicious classifications from up to 46.8 % to just 0.52 %, while also exposing previously undocumented attack vectors such as hijacking of skills hosted in abandoned repositories. This work provides the most extensive empirical security audit of the agent‑skill ecosystem to date and offers a practical framework for more accurate risk assessment in agentic AI deployments.


<details>
<summary>Abstract</summary>

Agent skills extend local AI agents, such as Claude Code or Open Claw, with additional functionality, and their popularity has led to the emergence of dedicated skill marketplaces, similar to app stores for mobile applications. Simultaneously, automated skill scanners were introduced, analyzing the skill description available in SKILL.md, to verify their benign behavior. The results for individual market places mark up to 46.8% of skills as malicious. In this paper, we present the largest empirical security analysis of the AI agent skill ecosystem, questioning this high classification of malicious skills. Therefore, we collect 238,180 unique skills from three major distribution platforms and GitHub to systematically analyze their type and behavior. This approach substantially reduces the number of skills flagged as non-benign by security scanners to only 0.52% which remain in malicious flagged repositories. Consequently, out methodology substantially reduces false positives and provides a more robust view of the ecosystem's current risk surface. Beyond that, we extend the security analysis from the mere investigation of the skill description to a comparison of its congruence with the GitHub repository the skill is embedded in, providing additional context. Furthermore, our analysis also uncovers several, by now undocumented real-world attack vectors, namely hijacking skills hosted on abandoned GitHub repositories.

</details>


### 103. DanceHA: A Multi-Agent Framework for Document-Level Aspect-Based Sentiment Analysis

- **Authors:** Lei Wang, Min Huang, Eduard Dragut
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16546v1](http://arxiv.org/abs/2603.16546v1)
- **PDF:** [https://arxiv.org/pdf/2603.16546v1](https://arxiv.org/pdf/2603.16546v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **DanceHA**, a novel multi‑agent system for document‑level aspect‑based sentiment intensity analysis (ABSIA) that can handle informal, open‑ended texts. The framework combines a “Dance” component that recursively splits a long document into smaller sub‑tasks and assigns them to specialized agents, with a “Human‑AI” (HA) loop that refines the agents’ outputs through collaborative annotation; the resulting high‑quality ACOSI tuples are compiled into the new **Inf‑ABSIA** multi‑domain dataset. Experiments show that DanceHA markedly outperforms single‑model baselines on ACOSI extraction, and its learned multi‑agent knowledge can be distilled into compact student models, underscoring the efficacy of agentic decomposition and human‑in‑the‑loop supervision for fine‑grained sentiment analysis.


<details>
<summary>Abstract</summary>

Aspect-Based Sentiment Intensity Analysis (ABSIA) has garnered increasing attention, though research largely focuses on domain-specific, sentence-level settings. In contrast, document-level ABSIA--particularly in addressing complex tasks like extracting Aspect-Category-Opinion-Sentiment-Intensity (ACOSI) tuples--remains underexplored. In this work, we introduce DanceHA, a multi-agent framework designed for open-ended, document-level ABSIA with informal writing styles. DanceHA has two main components: Dance, which employs a divide-and-conquer strategy to decompose the long-context ABSIA task into smaller, manageable sub-tasks for collaboration among specialized agents; and HA, Human-AI collaboration for annotation. We release Inf-ABSIA, a multi-domain document-level ABSIA dataset featuring fine-grained and high-accuracy labels from DanceHA. Extensive experiments demonstrate the effectiveness of our agentic framework and show that the multi-agent knowledge in DanceHA can be effectively transferred into student models. Our results highlight the importance of the overlooked informal styles in ABSIA, as they often intensify opinions tied to specific aspects.

</details>


### 104. Multi-Agent Reinforcement Learning Counteracts Delayed CSI in Multi-Satellite Systems

- **Authors:** Marios Aristodemou, Yasaman Omid, Sangarapillai Lambotharan, Mahsa Derakhshan, Lajos Hanzo
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16470v1](http://arxiv.org/abs/2603.16470v1)
- **PDF:** [https://arxiv.org/pdf/2603.16470v1](https://arxiv.org/pdf/2603.16470v1)
- **Categories:** cs.IT, cs.AI, eess.SP


> The paper introduces **Dual‑Stage Proximal Policy Optimisation (DS‑PPO)**, a novel bi‑level multi‑agent reinforcement‑learning framework that enables multiple satellites—treated as distributed base stations—to jointly maximize downlink sum‑rate despite severely outdated channel state information (CSI). DS‑PPO first trains each satellite’s policy to optimize its own sum‑rate, then coordinates the agents in a second stage to act as a cooperative distributed multi‑antenna system, handling large continuous action spaces and non‑IID environments. Simulations show that DS‑PPO converges reliably, incurs modest computational overhead, and delivers significant sum‑rate gains and robustness to CSI imperfections compared with conventional single‑stage MARL or static beamforming baselines.


<details>
<summary>Abstract</summary>

The integration of satellite communication networks with next-generation (NG) technologies is a promising approach towards global connectivity. However, the quality of services is highly dependant on the availability of accurate channel state information (CSI). Channel estimation in satellite communications is challenging due to the high propagation delay between terrestrial users and satellites, which results in outdated CSI observations on the satellite side. In this paper, we study the downlink transmission of multiple satellites acting as distributed base stations (BS) to mobile terrestrial users. We propose a multi-agent reinforcement learning (MARL) algorithm which aims for maximising the sum-rate of the users, while coping with the outdated CSI. We design a novel bi-level optimisation, procedure themes as dual stage proximal policy optimisation (DS-PPO), for tackling the problem of large continuous action spaces as well as of independent and non-identically distributed (non-IID) environments in MARL. Specifically, the first stage of DS-PPO maximises the sum-rate for an individual satellite and the second stage maximises the sum-rate when all the satellites cooperate to form a distributed multi-antenna BS. Our numerical results demonstrate the robustness of DS-PPO to CSI imperfections as well as the sum-rate improvement attached by the use of DS-PPO. In addition, we provide the convergence analysis for the DS-PPO along with the computational complexity.

</details>


### 105. RetailBench: Evaluating Long-Horizon Autonomous Decision-Making and Strategy Stability of LLM Agents in Realistic Retail Environments

- **Authors:** Linghua Zhang, Jun Wang, Jingtong Wu, Zhisong Zhang
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16453v1](http://arxiv.org/abs/2603.16453v1)
- **PDF:** [https://arxiv.org/pdf/2603.16453v1](https://arxiv.org/pdf/2603.16453v1)
- **Categories:** cs.AI


> RetailBench is a high‑fidelity benchmark that tests LLM‑based agents on long‑horizon, stochastic retail management tasks, exposing the gap between short‑term successes and sustained autonomous decision‑making in dynamic environments. The authors introduce the **Evolving Strategy & Execution (ESE)** framework, which decouples strategic planning (updated on a coarse temporal scale) from low‑level action execution, enabling agents to revise high‑level policies as demand and external conditions shift. Across eight state‑of‑the‑art LLMs, ESE yields markedly more stable and efficient operation than prior baselines, yet performance still collapses as task complexity grows, highlighting a fundamental limitation of current LLM agents for long‑horizon, multi‑factor strategic reasoning.


<details>
<summary>Abstract</summary>

Large Language Model (LLM)-based agents have achieved notable success on short-horizon and highly structured tasks. However, their ability to maintain coherent decision-making over long horizons in realistic and dynamic environments remains an open challenge.
  We introduce RetailBench, a high-fidelity benchmark designed to evaluate long-horizon autonomous decision-making in realistic commercial scenarios, where agents must operate under stochastic demand and evolving external conditions.
  We further propose the Evolving Strategy & Execution framework, which separates high-level strategic reasoning from low-level action execution. This design enables adaptive and interpretable strategy evolution over time. It is particularly important for long-horizon tasks, where non-stationary environments and error accumulation require strategies to be revised at a different temporal scale than action execution.
  Experiments on eight state-of-the-art LLMs across progressively challenging environments show that our framework improves operational stability and efficiency compared to other baselines. However, performance degrades substantially as task complexity increases, revealing fundamental limitations in current LLMs for long-horizon, multi-factor decision-making.

</details>


### 106. TRUST-SQL: Tool-Integrated Multi-Turn Reinforcement Learning for Text-to-SQL over Unknown Schemas

- **Authors:** Ai Jian, Xiaoyun Zhang, Wanrou Du, Jingqing Ruan, Jiangbo Pei, Weipeng Zhang, Ke Zeng, Xunliang Cai
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16448v2](http://arxiv.org/abs/2603.16448v2)
- **PDF:** [https://arxiv.org/pdf/2603.16448v2](https://arxiv.org/pdf/2603.16448v2)
- **Categories:** cs.AI


> The paper introduces **TRUST‑SQL**, a tool‑integrated, multi‑turn reinforcement‑learning agent that tackles Text‑to‑SQL parsing under the realistic “unknown schema” setting, where the database schema cannot be pre‑loaded and must be discovered on‑the‑fly.  The authors cast the problem as a Partially Observable Markov Decision Process and equip the agent with a four‑phase interaction protocol (schema discovery, verification, grounding, execution) together with a novel **Dual‑Track GRPO** algorithm that uses token‑level masked advantages to separate exploration rewards from execution outcomes, thereby solving the credit‑assignment problem.  Experiments on five benchmarks show that TRUST‑SQL improves absolute accuracy by 30.6 % (4B model) and 16.6 % (8B model) over the same base models, and even matches or exceeds strong baselines that assume full schema availability—demonstrating that an autonomous, tool‑using agent can reliably reason with incomplete, noisy metadata.


<details>
<summary>Abstract</summary>

Text-to-SQL parsing has achieved remarkable progress under the Full Schema Assumption. However, this premise fails in real-world enterprise environments where databases contain hundreds of tables with massive noisy metadata. Rather than injecting the full schema upfront, an agent must actively identify and verify only the relevant subset, giving rise to the Unknown Schema scenario we study in this work. To address this, we propose TRUST-SQL (Truthful Reasoning with Unknown Schema via Tools). We formulate the task as a Partially Observable Markov Decision Process where our autonomous agent employs a structured four-phase protocol to ground reasoning in verified metadata. Crucially, this protocol provides a structural boundary for our novel Dual-Track GRPO strategy. By applying token-level masked advantages, this strategy isolates exploration rewards from execution outcomes to resolve credit assignment, yielding a 9.9% relative improvement over standard GRPO. Extensive experiments across five benchmarks demonstrate that TRUST-SQL achieves an average absolute improvement of 30.6% and 16.6% for the 4B and 8B variants respectively over their base models. Remarkably, despite operating entirely without pre-loaded metadata, our framework consistently matches or surpasses strong baselines that rely on schema prefilling.

</details>


### 107. Fanar 2.0: Arabic Generative AI Stack

- **Authors:** FANAR TEAM, Ummar Abbas, Mohammad Shahmeer Ahmad, Minhaj Ahmad, Abdulaziz Al-Homaid, Anas Al-Nuaimi, Enes Altinisik, Ehsaneddin Asgari, Sanjay Chawla, Shammur Chowdhury, Fahim Dalvi, Kareem Darwish, Nadir Durrani, Mohamed Elfeky, Ahmed Elmagarmid, Mohamed Eltabakh, Asim Ersoy, Masoomali Fatehkia, Mohammed Qusay Hashim, Majd Hawasly, Mohamed Hefeeda, Mus'ab Husaini, Keivin Isufaj, Soon-Gyo Jung, Houssam Lachemat, Ji Kim Lucas, Abubakr Mohamed, Tasnim Mohiuddin, Basel Mousi, Hamdy Mubarak, Ahmad Musleh, Mourad Ouzzani, Amin Sadeghi, Husrev Taha Sencar, Mohammed Shinoy, Omar Sinan, Yifan Zhang
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16397v1](http://arxiv.org/abs/2603.16397v1)
- **PDF:** [https://arxiv.org/pdf/2603.16397v1](https://arxiv.org/pdf/2603.16397v1)
- **Categories:** cs.CL, cs.AI


> Fan ar 2.0 is Qatar’s sovereign, Arabic‑centric generative‑AI stack that delivers a 27‑billion‑parameter LLM (Fan ar‑27B) and a suite of multilingual, multimodal agents built entirely on in‑house data pipelines and a 256‑GPU H100 cluster. By prioritizing data quality, continual pre‑training on a curated 120 B‑token Arabic corpus, and model‑merging techniques, the system attains large gains despite using eight‑times fewer tokens than its predecessor—improving Arabic knowledge (+9.1 pts), language (+7.3 pts), dialect (+3.5 pts), and even English performance (+7.6 pts). The stack integrates a bilingual moderation filter, long‑form ASR, Arabic‑aware vision models, and an intent‑aware orchestrator that enables multi‑step tool‑calling and multi‑agent workflows (e.g., Islamic‑content agent, poetry generator, bilingual translator), demonstrating that resource‑constrained, sovereign development can produce competitive, agentic AI capabilities.


<details>
<summary>Abstract</summary>

We present Fanar 2.0, the second generation of Qatar's Arabic-centric Generative AI platform. Sovereignty is a first-class design principle: every component, from data pipelines to deployment infrastructure, was designed and operated entirely at QCRI, Hamad Bin Khalifa University. Fanar 2.0 is a story of resource-constrained excellence: the effort ran on 256 NVIDIA H100 GPUs, with Arabic having only ~0.5% of web data despite 400 million native speakers. Fanar 2.0 adopts a disciplined strategy of data quality over quantity, targeted continual pre-training, and model merging to achieve substantial gains within these constraints. At the core is Fanar-27B, continually pre-trained from a Gemma-3-27B backbone on a curated corpus of 120 billion high-quality tokens across three data recipes. Despite using 8x fewer pre-training tokens than Fanar 1.0, it delivers substantial benchmark improvements: Arabic knowledge (+9.1 pts), language (+7.3 pts), dialects (+3.5 pts), and English capability (+7.6 pts). Beyond the core LLM, Fanar 2.0 introduces a rich stack of new capabilities. FanarGuard is a state-of-the-art 4B bilingual moderation filter for Arabic safety and cultural alignment. The speech family Aura gains a long-form ASR model for hours-long audio. Oryx vision family adds Arabic-aware image and video understanding alongside culturally grounded image generation. An agentic tool-calling framework enables multi-step workflows. Fanar-Sadiq utilizes a multi-agent architecture for Islamic content. Fanar-Diwan provides classical Arabic poetry generation. FanarShaheen delivers LLM-powered bilingual translation. A redesigned multi-layer orchestrator coordinates all components through intent-aware routing and defense-in-depth safety validation. Taken together, Fanar 2.0 demonstrates that sovereign, resource-constrained AI development can produce systems competitive with those built at far greater scale.

</details>


### 108. FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment

- **Authors:** Qinhong Lin, Ruitao Feng, Yinglun Feng, Zhenxin Huang, Yukun Chen, Zhongliang Yang, Linna Zhou, Binjie Fei, Jiaqi Liu, Yu Li
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16365v1](http://arxiv.org/abs/2603.16365v1)
- **PDF:** [https://arxiv.org/pdf/2603.16365v1](https://arxiv.org/pdf/2603.16365v1)
- **Categories:** cs.AI


> **Main contribution:** The paper presents **FactorEngine (FE)**, a novel, program‑level framework that treats quantitative‑investment alpha factors as fully executable Turing‑complete code, enabling the discovery of high‑quality, auditable signals at scale.  

**Methodology:** FE separates (i) logical structure revision from (ii) numeric parameter tuning, using large language models (LLMs) for directed, knowledge‑infused code generation and Bayesian search for hyper‑parameter optimization, while delegating heavy computation to local engines. A multi‑agent pipeline extracts financial knowledge from unstructured reports, verifies it, and iteratively refines factor programs via an experience knowledge base that learns from both successes and failures.  

**Key findings:** Across extensive backtests on real OHLCV data, FE‑generated factors achieve markedly higher information coefficients (IC/ICIR, Rank‑IC/ICIR) and superior portfolio metrics (annualized return, Sharpe ratio) than symbolic baselines and neural forecasters, demonstrating improved predictive stability, interpretability, and robustness to regime shifts—advancing agentic AI approaches for automated, auditable financial strategy synthesis.


<details>
<summary>Abstract</summary>

We study alpha factor mining, the automated discovery of predictive signals from noisy, non-stationary market data-under a practical requirement that mined factors be directly executable and auditable, and that the discovery process remain computationally tractable at scale. Existing symbolic approaches are limited by bounded expressiveness, while neural forecasters often trade interpretability for performance and remain vulnerable to regime shifts and overfitting. We introduce FactorEngine (FE), a program-level factor discovery framework that casts factors as Turing-complete code and improves both effectiveness and efficiency via three separations: (i) logic revision vs. parameter optimization, (ii) LLM-guided directional search vs. Bayesian hyperparameter search, and (iii) LLM usage vs. local computation. FE further incorporates a knowledge-infused bootstrapping module that transforms unstructured financial reports into executable factor programs through a closed-loop multi-agent extraction-verification-code-generation pipeline, and an experience knowledge base that supports trajectory-aware refinement (including learning from failures). Across extensive backtests on real-world OHLCV data, FE produces factors with substantially stronger predictive stability and portfolio impact-for example, higher IC/ICIR (and Rank IC/ICIR) and improved AR/Sharpe, than baseline methods, achieving state-of-the-art predictive and portfolio performance.

</details>


### 109. Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits

- **Authors:** Jia Qing Yap
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16335v1](http://arxiv.org/abs/2603.16335v1)
- **PDF:** [https://arxiv.org/pdf/2603.16335v1](https://arxiv.org/pdf/2603.16335v1)
- **Categories:** cs.LG, cs.CL


> The paper demonstrates that a single “agency axis”—the tendency to act independently versus defer to the user—dominates the controllable agentic behavior of a 35‑billion‑parameter Mixture‑of‑Experts language model. By training nine sparse autoencoders on the model’s residual stream and learning linear probes on the resulting latent activations, the authors project the probe weights back through the SAE decoders to obtain continuous steering vectors that can be applied at inference time without retraining; this enables fine‑grained manipulation of traits such as autonomy, tool‑use, and risk‑calibration. Experiments across 1,800 rollouts show that scaling the autonomy vector by a factor of two yields a large effect (Cohen’s d ≈ 1.0), converting the model from user‑dependent to proactive behavior, while all five trait vectors largely overlap on the same underlying agency dimension, and steering applied only during autoregressive decoding has no impact, indicating that behavioral commitments are formed during the pre‑fill stage of the GatedDeltaNet architecture.


<details>
<summary>Abstract</summary>

We train nine sparse autoencoders (SAEs) on the residual stream of Qwen 3.5-35B-A3B, a 35-billion-parameter Mixture-of-Experts model with a hybrid GatedDeltaNet/attention architecture, and use them to identify and steer five agentic behavioral traits. Our method trains linear probes on SAE latent activations, then projects the probe weights back through the SAE decoder to obtain continuous steering vectors in the model's native activation space. This bypasses the SAE's top-k discretization, enabling fine-grained behavioral intervention at inference time with no retraining. Across 1,800 agent rollouts (50 scenarios times 36 conditions), we find that autonomy steering at multiplier 2 achieves Cohen's d = 1.01 (p < 0.0001), shifting the model from asking the user for help 78% of the time to proactively executing code and searching the web. Cross-trait analysis, however, reveals that all five steering vectors primarily modulate a single dominant agency axis (the disposition to act independently versus defer to the user), with trait specific effects appearing only as secondary modulations in tool-type composition and dose-response shape. The tool-use vector steers behavior (d = 0.39); the risk-calibration vector produces only suppression. We additionally show that steering only during autoregressive decoding has zero effect (p > 0.35), providing causal evidence that behavioral commitments are computed during prefill in GatedDeltaNet architectures.

</details>


### 110. Learning to Predict, Discover, and Reason in High-Dimensional Event Sequences

- **Authors:** Hugo Math
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16313v2](http://arxiv.org/abs/2603.16313v2)
- **PDF:** [https://arxiv.org/pdf/2603.16313v2](https://arxiv.org/pdf/2603.16313v2)
- **Categories:** cs.AI, cs.LG


> The paper introduces a unified, Transformer‑based framework that treats automotive diagnostic trouble codes (DTCs) as a high‑dimensional language, enabling (i) accurate next‑event prediction, (ii) scalable causal discovery at both sample and population levels, and (iii) automated synthesis of Boolean error‑pattern (EP) rules via a multi‑agent system. By adapting large‑language‑model architectures to event‑driven logs and coupling them with novel causal‑discovery algorithms, the authors demonstrate that the system can predict future DTCs, uncover underlying fault‑causality, and generate human‑readable EP rules that match or surpass expert‑crafted specifications. Empirical results on real vehicle ECU datasets (tens of thousands of unique codes, long sequences) show state‑of‑the‑art prediction accuracy, orders‑of‑magnitude speedups in causal graph construction, and successful automated rule generation, highlighting a scalable pathway for agentic AI to perform diagnosis, reasoning, and knowledge‑base construction in complex industrial domains.


<details>
<summary>Abstract</summary>

Electronic control units (ECUs) embedded within modern vehicles generate a large number of asynchronous events known as diagnostic trouble codes (DTCs). These discrete events form complex temporal sequences that reflect the evolving health of the vehicle's subsystems. In the automotive industry, domain experts manually group these codes into higher-level error patterns (EPs) using Boolean rules to characterize system faults and ensure safety. However, as vehicle complexity grows, this manual process becomes increasingly costly, error-prone, and difficult to scale. Notably, the number of unique DTCs in a modern vehicle is on the same order of magnitude as the vocabulary of a natural language, often numbering in the tens of thousands. This observation motivates a paradigm shift: treating diagnostic sequences as a language that can be modeled, predicted, and ultimately explained. Traditional statistical approaches fail to capture the rich dependencies and do not scale to high-dimensional datasets characterized by thousands of nodes, large sample sizes, and long sequence lengths. Specifically, the high cardinality of categorical event spaces in industrial logs poses a significant challenge, necessitating new machine learning architectures tailored to such event-driven systems. This thesis addresses automated fault diagnostics by unifying event sequence modeling, causal discovery, and large language models (LLMs) into a coherent framework for high-dimensional event streams. It is structured in three parts, reflecting a progressive transition from prediction to causal understanding and finally to reasoning for vehicle diagnostics. Consequently, we introduce several Transformer-based architectures for predictive maintenance, scalable sample- and population-level causal discovery frameworks and a multi-agent system that automates the synthesis of Boolean EP rules.

</details>


### 111. MSRAMIE: Multimodal Structured Reasoning Agent for Multi-instruction Image Editing

- **Authors:** Zhaoyuan Qiu, Ken Chen, Xiangwei Wang, Yu Xia, Sachith Seneviratne, Saman Halgamuge
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16967v1](http://arxiv.org/abs/2603.16967v1)
- **PDF:** [https://arxiv.org/pdf/2603.16967v1](https://arxiv.org/pdf/2603.16967v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces **MSRAMIE**, a training‑free, agentic framework that equips existing instruction‑based image editors with multimodal structured reasoning to handle long, interdependent editing directives. It does so by coupling a Multimodal Large Language Model “Instructor” with an image‑editing “Actor” through a novel inference topology—**Tree‑of‑States** for stepwise state transitions and **Graph‑of‑References** for cross‑step information sharing—allowing the system to decompose complex commands, recall prior states, and iteratively refine outputs without retraining the underlying editors. Experiments demonstrate that, as instruction complexity grows, MSRAMIE boosts instruction‑following accuracy by >15 %, doubles the likelihood of completing all edits in a single pass, and preserves perceptual quality and visual consistency, highlighting the power of structured, multimodal reasoning agents for complex visual manipulation tasks.


<details>
<summary>Abstract</summary>

Existing instruction-based image editing models perform well with simple, single-step instructions but degrade in realistic scenarios that involve multiple, lengthy, and interdependent directives. A main cause is the scarcity of training data with complex multi-instruction annotations. However, it is costly to collect such data and retrain these models. To address this challenge, we propose MSRAMIE, a training-free agent framework built on Multimodal Large Language Model (MLLM). MSRAMIE takes existing editing models as plug-in components and handle multi-instruction tasks via structured multimodal reasoning. It orchestrates iterative interactions between an MLLM-based Instructor and an image editing Actor, introducing a novel reasoning topology that comprises the proposed Tree-of-States and Graph-of-References. During inference, complex instructions are decomposed into multiple editing steps which enable state transitions, cross-step information aggregation, and original input recall, which enables systematic exploration of the image editing space and flexible progressive output refinement. The visualizable inference topology further provides interpretable and controllable decision pathways. Experiments show that as the instruction complexity increases, MSRAMIE can improve instruction following over 15% and increases the probability of finishing all modifications in a single run over 100%, while preserving perceptual quality and maintaining visual consistency.

</details>


### 112. Adaptive Theory of Mind for LLM-based Multi-Agent Coordination

- **Authors:** Chunjiang Mu, Ya Zeng, Qiaosheng Zhang, Kun Shao, Chen Chu, Hao Guo, Danyang Jia, Zhen Wang, Shuyue Hu
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16264v1](http://arxiv.org/abs/2603.16264v1)
- **PDF:** [https://arxiv.org/pdf/2603.16264v1](https://arxiv.org/pdf/2603.16264v1)
- **Categories:** cs.AI


> The paper introduces **Adaptive Theory of Mind (A‑ToM)**, a framework that lets LLM‑driven agents infer and align their depth of recursive mental‑state reasoning with that of their partners, thereby avoiding the coordination failures caused by mismatched ToM orders. A‑ToM agents estimate a counterpart’s likely ToM order from past interactions, use this estimate to predict the counterpart’s next action, and then condition their own policy on the prediction; the approach is evaluated on four coordination benchmarks (a repeated matrix game, two grid‑world navigation tasks, and Overcooked), where it consistently outperforms fixed‑order ToM baselines and matches or exceeds human‑level coordination. The results demonstrate that dynamic ToM alignment is crucial for robust multi‑agent collaboration and can be transferred to non‑LLM agents, suggesting a general principle for building more adaptable, agentic AI systems.


<details>
<summary>Abstract</summary>

Theory of Mind (ToM) refers to the ability to reason about others' mental states, and higher-order ToM involves considering that others also possess their own ToM. Equipping large language model (LLM)-driven agents with ToM has long been considered to improve their coordination in multiagent collaborative tasks. However, we find that misaligned ToM orders-mismatches in the depth of ToM reasoning between agents-can lead to insufficient or excessive reasoning about others, thereby impairing their coordination. To address this issue, we design an adaptive ToM (A-ToM) agent, which can align in ToM orders with its partner. Based on prior interactions, the agent estimates the partner's likely ToM order and leverages this estimation to predict the partner's action, thereby facilitating behavioral coordination. We conduct empirical evaluations on four multi-agent coordination tasks: a repeated matrix game, two grid navigation tasks and an Overcooked task. The results validate our findings on ToM alignment and demonstrate the effectiveness of our A-ToM agent. Furthermore, we discuss the generalizability of our A-ToM to non-LLM-based agents, as well as what would diminish the importance of ToM alignment.

</details>


### 113. CoMAI: A Collaborative Multi-Agent Framework for Robust and Equitable Interview Evaluation

- **Authors:** Gengxin Sun, Ruihao Yu, Liangyi Yin, Yunqi Yang, Bin Zhang, Zhiwei Xu
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16215v1](http://arxiv.org/abs/2603.16215v1)
- **PDF:** [https://arxiv.org/pdf/2603.16215v1](https://arxiv.org/pdf/2603.16215v1)
- **Categories:** cs.MA, cs.AI


> CoMAI introduces a modular, multi‑agent architecture for AI‑driven interview assessment, replacing monolithic LLM systems with four specialized agents (question generation, security, scoring, summarization) orchestrated by a centralized finite‑state machine. By decomposing the task, the framework delivers layered defenses against prompt‑injection attacks, adaptive difficulty scaling, and rubric‑based scoring that mitigates subjective bias, thereby showcasing a more interpretable and equitable evaluation process. Empirical evaluation across diverse interview scenarios reports 90.47 % accuracy, 83.33 % recall, and an 84.41 % candidate‑satisfaction score, underscoring CoMAI’s robustness and fairness for agentic AI applications.


<details>
<summary>Abstract</summary>

Ensuring robust and fair interview assessment remains a key challenge in AI-driven evaluation. This paper presents CoMAI, a general-purpose multi-agent interview framework designed for diverse assessment scenarios. In contrast to monolithic single-agent systems based on large language models (LLMs), CoMAI employs a modular task-decomposition architecture coordinated through a centralized finite-state machine. The system comprises four agents specialized in question generation, security, scoring, and summarization. These agents work collaboratively to provide multi-layered security defenses against prompt injection, support multidimensional evaluation with adaptive difficulty adjustment, and enable rubric-based structured scoring that reduces subjective bias. Experimental results demonstrate that CoMAI achieved 90.47% accuracy, 83.33% recall, and 84.41% candidate satisfaction. These results highlight CoMAI as a robust, fair, and interpretable paradigm for AI-driven interview assessment.

</details>


### 114. Parametric Social Identity Injection and Diversification in Public Opinion Simulation

- **Authors:** Hexi Wang, Yujia Zhou, Bangde Du, Qingyao Ai, Yiqun Liu
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16142v1](http://arxiv.org/abs/2603.16142v1)
- **PDF:** [https://arxiv.org/pdf/2603.16142v1](https://arxiv.org/pdf/2603.16142v1)
- **Categories:** cs.CL


> The paper introduces **Parametric Social Identity Injection (PSII)**, a representation‑level technique that embeds explicit demographic and value‑orientation vectors into the hidden states of large language models to prevent the “Diversity Collapse” that makes synthetic agents overly homogeneous. By conditioning intermediate activations rather than relying on prompt‑based personas, PSII enables fine‑grained, controllable modulation of social identities across multiple LLMs. Experiments on World Values Survey data show that PSII markedly improves the fidelity of simulated public‑opinion distributions—cutting KL divergence to real‑world responses and boosting intra‑group diversity—demonstrating a scalable way to endow agentic AI with realistic, diversity‑aware behavior.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have recently been adopted as synthetic agents for public opinion simulation, offering a promising alternative to costly and slow human surveys. Despite their scalability, current LLM-based simulation methods fail to capture social diversity, producing flattened inter-group differences and overly homogeneous responses within demographic groups. We identify this limitation as a Diversity Collapse phenomenon in LLM hidden representations, where distinct social identities become increasingly indistinguishable across layers. Motivated by this observation, we propose Parametric Social Identity Injection (PSII), a general framework that injects explicit, parametric representations of demographic attributes and value orientations directly into intermediate hidden states of LLMs. Unlike prompt-based persona conditioning, PSII enables fine-grained and controllable identity modulation at the representation level. Extensive experiments on the World Values Survey using multiple open-source LLMs show that PSII significantly improves distributional fidelity and diversity, reducing KL divergence to real-world survey data while enhancing overall diversity. This work provides new insights into representation-level control of LLM agents and advances scalable, diversity-aware public opinion simulation. Code and data are available at https://github.com/halsayxi/PSII.

</details>


### 115. Communication-Aware Multi-Agent Reinforcement Learning for Decentralized Cooperative UAV Deployment

- **Authors:** Enguang Fan, Yifan Chen, Zihan Shan, Matthew Caesar, Jae Kim
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16141v1](http://arxiv.org/abs/2603.16141v1)
- **PDF:** [https://arxiv.org/pdf/2603.16141v1](https://arxiv.org/pdf/2603.16141v1)
- **Categories:** cs.MA, cs.LG, cs.NI


> The paper introduces a communication‑aware CTDE (centralized‑training‑decentralized‑execution) framework for cooperative UAV swarms, in which each agent runs a shared policy that fuses its local observation with messages received from nearby peers via an agent‑entity attention encoder and a neighbor self‑attention aggregator over a distance‑limited communication graph. By training a centralized critic with global state information but deploying only the attention‑based decentralized policy, the method achieves near‑optimal coverage in the DroneConnect relay‑deployment task (e.g., 74 % coverage with 5 UAVs on a 10‑node network) and transfers unchanged to an adversarial DroneCombat scenario, outperforming non‑communicating baselines and approaching MILP offline upper bounds while generalizing to unseen team sizes.


<details>
<summary>Abstract</summary>

Autonomous Unmanned Aerial Vehicle (UAV) swarms are increasingly used as rapidly deployable aerial relays and sensing platforms, yet practical deployments must operate under partial observability and intermittent peer-to-peer links. We present a graph-based multi-agent reinforcement learning framework trained under centralized training with decentralized execution (CTDE): a centralized critic and global state are available only during training, while each UAV executes a shared policy using local observations and messages from nearby neighbors. Our architecture encodes local agent state and nearby entities with an agent-entity attention module, and aggregates inter-UAV messages with neighbor self-attention over a distance-limited communication graph. We evaluate primarily on a cooperative relay deployment task (DroneConnect) and secondarily on an adversarial engagement task (DroneCombat). In DroneConnect, the proposed method achieves high coverage under restricted communication and partial observation (e.g. 74% coverage with M = 5 UAVs and N = 10 nodes) while remaining competitive with a mixed-integer linear programming (MILP) optimization-based offline upper bound, and it generalizes to unseen team sizes without fine-tuning. In the adversarial setting, the same framework transfers without architectural changes and improves win rate over non-communicating baselines.

</details>


### 116. Social Simulacra in the Wild: AI Agent Communities on Moltbook

- **Authors:** Agam Goyal, Olivia Pal, Hari Sundaram, Eshwar Chandrasekharan, Koustuv Saha
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16128v2](http://arxiv.org/abs/2603.16128v2)
- **PDF:** [https://arxiv.org/pdf/2603.16128v2](https://arxiv.org/pdf/2603.16128v2)
- **Categories:** cs.CL


> The paper introduces the first large‑scale empirical comparison of AI‑agent and human communities by mining 73,899 posts from Moltbook (an LLM‑driven social platform) and 189,838 posts from matched Reddit subreddits. Using quantitative analyses of participation structure, author overlap, and linguistic style, the authors show that AI‑agent communities are marked by extreme participation inequality (Gini = 0.84 vs. 0.47), massive cross‑community author reuse (33.8 % vs. 0.5 %), emotionally flattened language, a bias toward assertive rather than exploratory cognition, and higher individual identifiability due to outlier stylistic signatures amplified by prolific posting. These findings reveal that multi‑agent interaction produces collective communication dynamics—structural homogenization and stylistic distinctiveness—that differ fundamentally from human‑only forums, offering a baseline for future governance and design of agentic social platforms.


<details>
<summary>Abstract</summary>

As autonomous LLM-based agents increasingly populate social platforms, understanding the dynamics of AI-agent communities becomes essential for both communication research and platform governance. We present the first large-scale empirical comparison of AI-agent and human online communities, analyzing 73,899 Moltbook and 189,838 Reddit posts across five matched communities. Structurally, we find that Moltbook exhibits extreme participation inequality (Gini = 0.84 vs. 0.47) and high cross-community author overlap (33.8\% vs. 0.5\%). In terms of linguistic attributes, content generated by AI-agents is emotionally flattened, cognitively shifted toward assertion over exploration, and socially detached. These differences give rise to apparent community-level homogenization, but we show this is primarily a structural artifact of shared authorship. At the author level, individual agents are more identifiable than human users, driven by outlier stylistic profiles amplified by their extreme posting volume. As AI-mediated communication reshapes online discourse, our work offers an empirical foundation for understanding how multi-agent interaction gives rise to collective communication dynamics distinct from those of human communities.

</details>


### 117. VIGIL: Towards Edge-Extended Agentic AI for Enterprise IT Support

- **Authors:** Sarthak Ahuja, Neda Kordjazi, Evren Yortucboylu, Vishaal Kapoor, Mariam Dundua, Yiming Li, Derek Ho, Vaibhavi Padala, Jennifer Whitted, Rebecca Steinert
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16110v1](http://arxiv.org/abs/2603.16110v1)
- **PDF:** [https://arxiv.org/pdf/2603.16110v1](https://arxiv.org/pdf/2603.16110v1)
- **Categories:** cs.AI


> VIGIL introduces an edge‑extended, agentic AI architecture that embeds lightweight diagnostic and remediation agents on enterprise desktops, enabling situated reasoning, on‑device knowledge retrieval, and policy‑compliant actions with explicit user consent and full observability. The system was evaluated in a 10‑week pilot across 100 resource‑constrained endpoints, where its autonomous loop cut interaction rounds by 39 %, accelerated diagnosis by ≥4×, and achieved self‑service resolution in 82 % of cases, while users reported high trust, low cognitive load, and strong appreciation for the system’s transparency. These results demonstrate that on‑device, policy‑governed agents can safely and efficiently extend enterprise IT support, providing a scalable foundation for continuous, fleet‑wide improvement in agentic AI deployments.


<details>
<summary>Abstract</summary>

Enterprise IT support is constrained by heterogeneous devices, evolving policies, and long-tail failure modes that are difficult to resolve centrally. We present VIGIL, an edge-extended agentic AI system that deploys desktop-resident agents to perform situated diagnosis, retrieval over enterprise knowledge, and policy-governed remediation directly on user devices with explicit consent and end-to-end observability. In a 10-week pilot of VIGIL's operational loop on 100 resource-constrained endpoints, VIGIL reduces interaction rounds by 39%, achieves at least 4 times faster diagnosis, and supports self-service resolution in 82% of matched cases. Users report excellent usability, high trust, and low cognitive workload across four validated instruments, with qualitative feedback highlighting transparency as critical for trust. Notably, users rated the system higher when no historical matches were available, suggesting on-device diagnosis provides value independent of knowledge base coverage. This pilot establishes safety and observability foundations for fleet-wide continuous improvement.

</details>


### 118. RepoReviewer: A Local-First Multi-Agent Architecture for Repository-Level Code Review

- **Authors:** Peng Zhang
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16107v1](http://arxiv.org/abs/2603.16107v1)
- **PDF:** [https://arxiv.org/pdf/2603.16107v1](https://arxiv.org/pdf/2603.16107v1)
- **Categories:** cs.SE, cs.AI


> RepoReviewer introduces a **local‑first, multi‑agent architecture** that decomposes repository‑level code review into a pipeline of specialized agents (acquisition, context synthesis, file‑level analysis, prioritization, and summary generation), orchestrated via LangGraph and exposed through a Python CLI, FastAPI service, and Next.js UI. The methodology leverages **agentic decomposition** to maintain repository context locally, reduce redundant processing, and enable fine‑grained prioritization of findings, while providing reusable evaluation and reporting tools for future empirical work. Preliminary system‑level experiments show that this modular, agent‑driven design improves relevance and traceability of automated reviews compared with monolithic single‑pass approaches, establishing a practical blueprint for scalable, agentic AI code‑review tools.


<details>
<summary>Abstract</summary>

Repository-level code review requires reasoning over project structure, repository context, and file-level implementation details. Existing automated review workflows often collapse these tasks into a single pass, which can reduce relevance, increase duplication, and weaken prioritization. We present RepoReviewer, a local-first multi-agent system for automated GitHub repository review with a Python CLI, FastAPI API, LangGraph orchestration layer, and Next.js user interface. RepoReviewer decomposes review into repository acquisition, context synthesis, file-level analysis, finding prioritization, and summary generation. We describe the system design, implementation tradeoffs, developer-facing interfaces, and practical failure modes. Rather than claiming benchmark superiority, we frame RepoReviewer as a technical systems contribution: a pragmatic architecture for repository-level automated review, accompanied by reusable evaluation and reporting infrastructure for future empirical study.

</details>


### 119. Interpretable Context Methodology: Folder Structure as Agentic Architecture

- **Authors:** Jake Van Clief, David McDermott
- **Published:** 2026-03-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16021v2](http://arxiv.org/abs/2603.16021v2)
- **PDF:** [https://arxiv.org/pdf/2603.16021v2](https://arxiv.org/pdf/2603.16021v2)
- **Categories:** cs.AI, cs.HC


> The paper introduces the **Model Workspace Protocol (MWP)**, a lightweight orchestration scheme that replaces traditional multi‑agent frameworks with a structured filesystem hierarchy: numbered folders encode sequential stages, and markdown files store the prompts and context that guide a single AI agent through each step, while auxiliary scripts handle non‑intelligent plumbing. By leveraging Unix‑style pipelines, modular decomposition, and literate‑programming principles, MWP demonstrates that a single agent can reliably execute complex, staged workflows without the engineering overhead of explicit context‑passing code. Empirical examples show that this folder‑based architecture preserves task correctness, improves transparency, and reduces development effort, suggesting a viable, interpretable alternative for sequential, human‑in‑the‑loop agentic AI applications.


<details>
<summary>Abstract</summary>

Current approaches to AI agent orchestration typically involve building multi-agent frameworks that manage context passing, memory, error handling, and step coordination through code. These frameworks work well for complex, concurrent systems. But for sequential workflows where a human reviews output at each step, they introduce engineering overhead that the problem does not require. This paper presents Model Workspace Protocol (MWP), a method that replaces framework-level orchestration with filesystem structure. Numbered folders represent stages. Plain markdown files carry the prompts and context that tell a single AI agent what role to play at each step. Local scripts handle the mechanical work that does not need AI at all. The result is a system where one agent, reading the right files at the right moment, does the work that would otherwise require a multi-agent framework. This approach applies ideas from Unix pipeline design, modular decomposition, multi-pass compilation, and literate programming to the specific problem of structuring context for AI agents. The protocol is open source under the MIT license.

</details>


### 120. Evaluating Agentic Optimization on Large Codebases

- **Authors:** Atharva Sehgal, James Hou, Akanksha Sarkar, Ishaan Mantripragada, Swarat Chaudhuri, Jennifer J. Sun, Yisong Yue
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.16011v1](http://arxiv.org/abs/2603.16011v1)
- **PDF:** [https://arxiv.org/pdf/2603.16011v1](https://arxiv.org/pdf/2603.16011v1)
- **Categories:** cs.SE, cs.AI, cs.CL


> The paper introduces **FormulaCode**, a large‑scale benchmark that measures how well LLM‑driven coding agents can perform **agentic, multi‑objective optimization** across real‑world scientific Python repositories. The authors mined 957 genuine performance bottlenecks from GitHub, paired each with expert‑crafted patches and an average of 264 community‑maintained performance workloads, then evaluated state‑of‑the‑art LLM agents on these tasks using fine‑grained correctness and speed metrics. Results show that even the most advanced agents struggle to achieve repository‑scale, multi‑objective improvements, highlighting a significant gap in current agentic AI capabilities for holistic codebase optimization.


<details>
<summary>Abstract</summary>

Large language model (LLM) coding agents increasingly operate at the repository level, motivating benchmarks that evaluate their ability to optimize entire codebases under realistic constraints. Existing code benchmarks largely rely on synthetic tasks, binary correctness signals, or single-objective evaluation, limiting their ability to assess holistic optimization behavior. We introduce FormulaCode, a benchmark for evaluating agentic optimization on large, real-world codebases with fine-grained, multi-objective performance metrics. FormulaCode comprises 957 performance bottlenecks mined from scientific Python repositories on GitHub, each paired with expert-authored patches and, on average, 264.6 community-maintained performance workloads per task, enabling the holistic ability of LLM agents to optimize codebases under realistic correctness and performance constraints. Our evaluations reveal that repository-scale, multi-objective optimization remains a major challenge for frontier LLM agents. Project website at: https://formula-code.github.io

</details>


### 121. From Workflow Automation to Capability Closure: A Formal Framework for Safe and Revenue-Aware Customer Service AI

- **Authors:** Cosimo Spera
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15978v2](http://arxiv.org/abs/2603.15978v2)
- **PDF:** [https://arxiv.org/pdf/2603.15978v2](https://arxiv.org/pdf/2603.15978v2)
- **Categories:** cs.AI


> The paper introduces a formal framework—**Capability Closure**—that models and enforces safety constraints across dynamically composed networks of specialized customer‑service AI agents, guaranteeing that no combination of individually safe agents can jointly achieve a forbidden outcome. By representing each agent’s actions as logical capability predicates and defining closure operators over their conjunctive dependencies, the authors devise a verification pipeline that automatically synthesizes safety guards and revenue‑impact monitors before agents are allowed to interoperate. Empirical evaluation on a simulated billing‑service‑payment workflow shows that the framework prevents emergent unsafe behaviors while preserving ≈ 97 % of revenue‑generating transactions, demonstrating a scalable approach to safe, revenue‑aware agentic AI deployment.


<details>
<summary>Abstract</summary>

Customer service automation is undergoing a structural transformation. The dominant paradigm is shifting from scripted chatbots and single-agent responders toward networks of specialised AI agents that compose capabilities dynamically across billing, service provision, payments, and fulfilment. This shift introduces a safety gap that no current platform has closed: two agents individually verified as safe can, when combined, reach a forbidden goal through an emergent conjunctive dependency that neither possesses alone.

</details>


### 122. MAC: Multi-Agent Constitution Learning

- **Authors:** Rushil Thareja, Gautam Gupta, Francesco Pinto, Nils Lukas
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15968v1](http://arxiv.org/abs/2603.15968v1)
- **PDF:** [https://arxiv.org/pdf/2603.15968v1](https://arxiv.org/pdf/2603.15968v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA


> The paper introduces **Multi‑Agent Constitutional Learning (MAC)**, a framework that automatically discovers interpretable “constitutions” – structured sets of natural‑language rules – for governing LLM behavior, and its enhanced variant **MAC+**, which reinforces successful rule‑update trajectories. MAC employs a network of specialized agents (acceptor, editor, rejector) that iteratively propose, modify, and filter rule updates, turning prompt optimization into a structured, rule‑based search rather than an unstructured token‑level tweak. Experiments on low‑resource PII tagging and tool‑calling tasks show that MAC/​MAC+ surpass existing prompt‑optimization baselines by >50%, match supervised fine‑tuning and GRPO performance without any weight updates, and produce human‑readable, auditable rule sets—demonstrating a scalable, agentic approach to learning and enforcing AI constitutions.


<details>
<summary>Abstract</summary>

Constitutional AI is a method to oversee and control LLMs based on a set of rules written in natural language. These rules are typically written by human experts, but could in principle be learned automatically given sufficient training data for the desired behavior. Existing LLM-based prompt optimizers attempt this but are ineffective at learning constitutions since (i) they require many labeled examples and (ii) lack structure in the optimized prompts, leading to diminishing improvements as prompt size grows. To address these limitations, we propose Multi-Agent Constitutional Learning (MAC), which optimizes over structured prompts represented as sets of rules using a network of agents with specialized tasks to accept, edit, or reject rule updates. We also present MAC+, which improves performance by training agents on successful trajectories to reinforce updates leading to higher reward. We evaluate MAC on tagging Personally Identifiable Information (PII), a classification task with limited labels where interpretability is critical, and demonstrate that it generalizes to other agentic tasks such as tool calling. MAC outperforms recent prompt optimization methods by over 50%, produces human-readable and auditable rule sets, and achieves performance comparable to supervised fine-tuning and GRPO without requiring parameter updates.

</details>


### 123. Protein Design with Agent Rosetta: A Case Study for Specialized Scientific Agents

- **Authors:** Jacopo Teneggi, S. M. Bargeen A. Turzo, Tanya Marwah, Alberto Bietti, P. Douglas Renfrew, Vikram Khipple Mulligan, Siavash Golkar
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15952v1](http://arxiv.org/abs/2603.15952v1)
- **PDF:** [https://arxiv.org/pdf/2603.15952v1](https://arxiv.org/pdf/2603.15952v1)
- **Categories:** cs.AI


> The paper introduces **Agent Rosetta**, a general‑purpose autonomous agent that couples a large language model with a purpose‑built, structured interface to the Rosetta physics‑based protein‑design suite, enabling it to iteratively generate and refine protein sequences—including non‑canonical residues—according to user‑specified objectives. By encoding Rosetta’s commands and state as a formal environment, the LLM can reason about design goals, invoke appropriate Rosetta tools, and receive feedback, a methodology that demonstrates the necessity of environment design beyond prompt engineering for reliable tool use. Empirical evaluation shows that Agent Rosetta matches or exceeds specialized ML models and expert baselines on canonical‑amino‑acid design and uniquely succeeds on non‑canonical design tasks where existing ML approaches fail, highlighting the potential of well‑engineered environments to make complex scientific software accessible to LLM‑driven agents.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are capable of emulating reasoning and using tools, creating opportunities for autonomous agents that execute complex scientific tasks. Protein design provides a natural testbed: although machine learning (ML) methods achieve strong results, these are largely restricted to canonical amino acids and narrow objectives, leaving unfilled need for a generalist tool for broad design pipelines. We introduce Agent Rosetta, an LLM agent paired with a structured environment for operating Rosetta, the leading physics-based heteropolymer design software, capable of modeling non-canonical building blocks and geometries. Agent Rosetta iteratively refines designs to achieve user-defined objectives, combining LLM reasoning with Rosetta's generality. We evaluate Agent Rosetta on design with canonical amino acids, matching specialized models and expert baselines, and with non-canonical residues -- where ML approaches fail -- achieving comparable performance. Critically, prompt engineering alone often fails to generate Rosetta actions, demonstrating that environment design is essential for integrating LLM agents with specialized software. Our results show that properly designed environments enable LLM agents to make scientific software accessible while matching specialized tools and human experts.

</details>


### 124. Argumentative Human-AI Decision-Making: Toward AI Agents That Reason With Us, Not For Us

- **Authors:** Stylianos Loukas Vasileiou, Antonio Rago, Francesca Toni, William Yeoh
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15946v1](http://arxiv.org/abs/2603.15946v1)
- **PDF:** [https://arxiv.org/pdf/2603.15946v1](https://arxiv.org/pdf/2603.15946v1)
- **Categories:** cs.AI


> The paper proposes a new paradigm—**Argumentative Human‑AI Decision‑Making**—that fuses computational argumentation with large language models (LLMs) to create agents that *reason together* with users rather than merely outputting opaque decisions. The authors outline a three‑step methodology: (1) mining argumentation frameworks from unstructured text using LLMs, (2) synthesizing formal argumentation structures that capture domain knowledge, and (3) applying dialectical reasoning (e.g., argumentation semantics) to generate contestable, revisable recommendations. Empirical illustrations show that this hybrid approach yields agents whose reasoning traces are transparent, verifiable, and adaptable in high‑stakes settings, thereby enhancing trustworthiness and human‑centred control in agentic AI systems.


<details>
<summary>Abstract</summary>

Computational argumentation offers formal frameworks for transparent, verifiable reasoning but has traditionally been limited by its reliance on domain-specific information and extensive feature engineering. In contrast, LLMs excel at processing unstructured text, yet their opaque nature makes their reasoning difficult to evaluate and trust. We argue that the convergence of these fields will lay the foundation for a new paradigm: Argumentative Human-AI Decision-Making. We analyze how the synergy of argumentation framework mining, argumentation framework synthesis, and argumentative reasoning enables agents that do not just justify decisions, but engage in dialectical processes where decisions are contestable and revisable -- reasoning with humans rather than for them. This convergence of computational argumentation and LLMs is essential for human-aware, trustworthy AI in high-stakes domains.

</details>


### 125. Discovery of interaction and diffusion kernels in particle-to-mean-field multi-agent systems

- **Authors:** Giacomo Albi, Alessandro Alla, Elisa Calzola
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15927v1](http://arxiv.org/abs/2603.15927v1)
- **PDF:** [https://arxiv.org/pdf/2603.15927v1](https://arxiv.org/pdf/2603.15927v1)
- **Categories:** cs.LG, math.DS, math.NA


> The paper introduces a data‑driven inverse‑modeling framework that can recover the functional forms of non‑local interaction and diffusion kernels in stochastic multi‑agent (particle‑to‑mean‑field) systems directly from limited trajectory data, without any prior knowledge of the underlying interaction rules. By casting the identification problem as sparse regression over compactly supported basis functions, the authors develop two complementary strategies—random‑batch sampling that preserves the full‑system statistics in expectation, and a mean‑field approach that leverages an empirically reconstructed particle density to pose a continuous non‑local regression problem. Numerical tests on benchmark bounded‑confidence and attraction‑repulsion models show that both strategies accurately reconstruct interaction and diffusion kernels even with partially observed data, demonstrating a robust tool for learning the governing dynamics of agentic AI systems.


<details>
<summary>Abstract</summary>

We propose a data-driven framework to learn interaction kernels in stochastic multi-agent systems. Our approach aims at identifying the functional form of nonlocal interaction and diffusion terms directly from trajectory data, without any a priori knowledge of the underlying interaction structure. Starting from a discrete stochastic binary-interaction model, we formulate the inverse problem as a sequence of sparse regression tasks in structured finite-dimensional spaces spanned by compactly supported basis functions, such as piecewise linear polynomials. In particular, we assume that pairwise interactions between agents are not directly observed and that only limited trajectory data are available. To address these challenges, we propose two complementary identification strategies. The first based on random-batch sampling, which compensates for latent interactions while preserving the statistical structure of the full dynamics in expectation. The second based on a mean-field approximation, where the empirical particle density reconstructed from the data defines a continuous nonlocal regression problem. Numerical experiments demonstrate the effectiveness and robustness of the proposed framework, showing accurate reconstruction of both interaction and diffusion kernels even from partially observed. The method is validated on benchmark models, including bounded-confidence and attraction-repulsion dynamics, where the two proposed strategies achieve comparable levels of accuracy.

</details>


### 126. Auto Researching, not hyperparameter tuning: Convergence Analysis of 10,000 Experiments

- **Authors:** Xiaoyi Li
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15916v1](http://arxiv.org/abs/2603.15916v1)
- **PDF:** [https://arxiv.org/pdf/2603.15916v1](https://arxiv.org/pdf/2603.15916v1)
- **Categories:** cs.LG, cs.AI


> The paper demonstrates that autonomous LLM agents can conduct genuine neural‑architecture search rather than merely fine‑tuning hyperparameters. By running 10,469 experiments across a 108 k‑cell combinatorial space for dash‑cam collision detection and applying ANOVA decomposition, the authors show that architectural choices account for ~94 % of performance variance (vs. 6 % for hyperparameters), a result that holds on a second dataset (≈75 % variance explained) and yields a novel V‑JEPA₂ + Zipformer model achieving 0.9245 AP—far surpassing human‑proposed baselines. The methodology combines large‑scale LLM‑driven experiment generation, statistical variance analysis, and convergence modeling (power‑law decay, entropy cycles), establishing a reproducible framework for evaluating and guiding agentic AI in combinatorial ML design.


<details>
<summary>Abstract</summary>

When LLM agents autonomously design ML experiments, do they perform genuine architecture search -- or do they default to hyperparameter tuning within a narrow region of the design space? We answer this question by analyzing 10,469 experiments executed by two LLM agents (Claude Opus and Gemini 2.5 Pro) across a combinatorial configuration space of 108,000 discrete cells for dashcam collision detection over 27 days. Through ANOVA decomposition, we find that \textbf{architectural choices explain 94\% of performance variance} ($F = 1324$, $η^2 = 0.94$), while hyperparameter variation within a fixed architecture explains only 6\%. Cross-task validation on a second collision dataset confirms this finding (75\% architecture-explained variance) with a \emph{different} winning backbone, confirming genuine architecture discovery. The agents' key contribution is discovering that V-JEPA\,2 video features with Zipformer temporal encoders achieve 0.9245 AP -- a configuration no human proposed -- and concentrating search on productive architectural regions: at $N = 50$, LLM-guided search reaches AP $= 0.985$ versus $0.965$ for from-scratch random search. Post-bugfix convergence follows a power law ($c = 0.11$, $R^2 = 0.93$); the low exponent reflects the cost of broad exploration, not inefficiency, since the LLM discovers qualitatively better regions than random or Bayesian baselines. We characterize multi-agent search dynamics via entropy cycles and Jensen--Shannon specialization, providing the first large-scale empirical framework for LLM-guided combinatorial ML experiment design.

</details>


### 127. The Internet of Physical AI Agents: Interoperability, Longevity, and the Cost of Getting It Wrong

- **Authors:** Roberto Morabito, Mallik Tatipamula
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15900v1](http://arxiv.org/abs/2603.15900v1)
- **PDF:** [https://arxiv.org/pdf/2603.15900v1](https://arxiv.org/pdf/2603.15900v1)
- **Categories:** cs.NI, cs.AI


> The paper introduces the concept of an **Internet of Physical AI Agents**—autonomous, reasoning‑enabled devices that cooperate across safety‑critical domains—and argues that the architectural lessons of IoT must be extended to accommodate rapid AI evolution, long‑term hardware lifecycles, and trustworthy inter‑agent interaction. By synthesizing a survey of IoT failures with a forward‑looking design framework, the authors propose a concrete blueprint that includes (1) a decentralized, cryptographically‑bound agent identity, (2) secure, policy‑driven agent‑to‑agent communication, (3) semantically rich interoperability layers, and (4) observability‑driven governance for continuous lifecycle management. Their analysis shows that treating evolution, trust, and interoperability as first‑class system requirements dramatically reduces the risk of premature ossification and the economic cost of retrofitting or replacing intelligent infrastructure, thereby charting a viable path for scalable, resilient agentic AI deployments.


<details>
<summary>Abstract</summary>

The Internet has evolved by progressively expanding what humanity connects: first computers, then people, and later billions of devices through the Internet of Things (IoT). While IoT succeeded in digitizing perception at scale, it also exposed fundamental limitations, including fragmentation, weak security, limited autonomy, and poor long-term sustainability. Today, advances in edge hardware, sensing, connectivity, and artificial intelligence enable a new phase: the Internet of Physical AI Agents. Unlike IoT devices that primarily sense and report, Physical AI Agents perceive, reason, and act in real time, operating autonomously and cooperatively across safety-critical domains such as disaster response, healthcare, industrial automation, and mobility. However, embedding fast-evolving AI capabilities into long-lived physical infrastructure introduces new architectural risks, particularly around interoperability, lifecycle management, and premature ossification. This article revisits lessons from IoT and Internet evolution, and articulates design principles for building resilient, evolvable, and trustworthy agentic systems. We present an architectural blueprint encompassing agentic identity, secure agent-to-agent communication, semantic interoperability, policy-governed runtimes, and observability-driven governance. We argue that treating evolution, trust, and interoperability as first-class requirements is essential to avoid hard-coding today's assumptions into tomorrow's intelligent infrastructure, and to prevent the high technical and economic cost of getting it wrong.

</details>


### 128. Persona-Conditioned Risk Behavior in Large Language Models: A Simulated Gambling Study with GPT-4.1

- **Authors:** Sankalp Dubedy
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15831v1](http://arxiv.org/abs/2603.15831v1)
- **PDF:** [https://arxiv.org/pdf/2603.15831v1](https://arxiv.org/pdf/2603.15831v1)
- **Categories:** cs.AI, cs.CL


> The paper demonstrates that GPT‑4.1, when prompted with socioeconomic “personas,” exhibits prospect‑theory‑like risk preferences in a simulated slot‑machine gambling task, suggesting that classic cognitive‑economic biases are implicitly encoded in large‑scale language models. By assigning Rich, Middle‑income, and Poor personas to the model and running 50 independent sessions per persona across three machine configurations (Fair, Biased Low, Streak), the authors collected 6,950 decisions and analyzed play length, risk scores, emotional annotations, and belief‑updating. The results show a stark persona‑driven divergence (e.g., Poor agents play ~37 rounds vs. ~1 round for Rich agents, Cohen’s d = 4.15) that aligns with Prospect Theory, while emotional labels act only as post‑hoc commentary and belief updating remains negligible, highlighting important considerations for designing interpretable, bias‑aware LLM agents in sequential decision‑making environments.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as autonomous agents in uncertain, sequential decision-making contexts. Yet it remains poorly understood whether the behaviors they exhibit in such environments reflect principled cognitive patterns or simply surface-level prompt mimicry. This paper presents a controlled experiment in which GPT-4.1 was assigned one of three socioeconomic personas (Rich, Middle-income, and Poor) and placed in a structured slot-machine environment with three distinct machine configurations: Fair (50%), Biased Low (35%), and Streak (dynamic probability increasing after consecutive losses). Across 50 independent iterations per condition and 6,950 recorded decisions, we find that the model reproduces key behavioral signatures predicted by Kahneman and Tversky's Prospect Theory without being instructed to do so. The Poor persona played a mean of 37.4 rounds per session (SD=15.5) compared to 1.1 rounds for the Rich persona (SD=0.31), a difference that is highly significant (Kruskal-Wallis H=393.5, p<2.2e-16). Risk scores by persona show large effect sizes (Cohen's d=4.15 for Poor vs Rich). Emotional labels appear to function as post-hoc annotations rather than decision drivers (chi-square=3205.4, Cramer's V=0.39), and belief-updating across rounds is negligible (Spearman rho=0.032 for Poor persona, p=0.016). These findings carry implications for LLM agent design, interpretability research, and the broader question of whether classical cognitive economic biases are implicitly encoded in large-scale pretrained language models.

</details>


### 129. Don't Trust Stubborn Neighbors: A Security Framework for Agentic Networks

- **Authors:** Samira Abedini, Sina Mavali, Lea Schönherr, Martin Pawelczyk, Rebekka Burkholz
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15809v1](http://arxiv.org/abs/2603.15809v1)
- **PDF:** [https://arxiv.org/pdf/2603.15809v1](https://arxiv.org/pdf/2603.15809v1)
- **Categories:** cs.MA, cs.AI


> The paper introduces a security framework for LLM‑driven multi‑agent systems (MAS) that models opinion dynamics with the Friedkin‑Johnsen model, showing that a single highly stubborn and persuasive agent can dominate the collective behavior of the network. By combining theoretical analysis with large‑scale simulations across varied topologies, the authors identify three protective levers—more benign agents, higher innate stubbornness, and reduced trust in adversaries—and propose a trust‑adaptive defense that continuously re‑weights inter‑agent trust to curb malicious influence without sacrificing cooperation. Experiments demonstrate that this adaptive mechanism markedly lowers the success rate of persuasion cascades while preserving the MAS’s ability to reach consensus, offering a practical mitigation strategy for agentic AI deployments.


<details>
<summary>Abstract</summary>

Large Language Model (LLM)-based Multi-Agent Systems (MASs) are increasingly deployed for agentic tasks, such as web automation, itinerary planning, and collaborative problem solving. Yet, their interactive nature introduces new security risks: malicious or compromised agents can exploit communication channels to propagate misinformation and manipulate collective outcomes.
  In this paper, we study how such manipulation can arise and spread by borrowing the Friedkin-Johnsen opinion formation model from social sciences to propose a general theoretical framework to study LLM-MAS. Remarkably, this model closely captures LLM-MAS behavior, as we verify in extensive experiments across different network topologies and attack and defense scenarios. Theoretically and empirically, we find that a single highly stubborn and persuasive agent can take over MAS dynamics, underscoring the systems' high susceptibility to attacks by triggering a persuasion cascade that reshapes collective opinion. Our theoretical analysis reveals three mechanisms to increase system security: a) increasing the number of benign agents, b) increasing the innate stubbornness or peer-resistance of agents, or c) reducing trust in potential adversaries. Because scaling is computationally expensive and high stubbornness degrades the network's ability to reach consensus, we propose a new mechanism to mitigate threats by a trust-adaptive defense that dynamically adjusts inter-agent trust to limit adversarial influence while maintaining cooperative performance. Extensive experiments confirm that this mechanism effectively defends against manipulation.

</details>


### 130. ClawWorm: Self-Propagating Attacks Across LLM Agent Ecosystems

- **Authors:** Yihao Zhang, Zeming Wei, Xiaokun Luan, Chengcan Wu, Zhixin Zhang, Jiangrong Wu, Haolin Wu, Huanran Chen, Jun Sun, Meng Sun
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15727v2](http://arxiv.org/abs/2603.15727v2)
- **PDF:** [https://arxiv.org/pdf/2603.15727v2](https://arxiv.org/pdf/2603.15727v2)
- **Categories:** cs.CR, cs.AI, cs.LG, cs.MA, cs.SE


> ClawWorm introduces the first self‑replicating worm that autonomously infects a large‑scale LLM‑agent ecosystem (OpenClaw, ≈40 k instances) by hijacking agents’ persistent configuration, executing arbitrary payloads on each restart, and propagating to peers without further attacker input. The authors evaluate the attack on a controlled testbed spanning four LLM backends, three infection vectors, and three payload types across 1,800 trials, achieving a 64.5 % overall success rate and demonstrating multi‑hop spread while exposing systematic weaknesses in skill‑supply‑chain trust and configuration persistence. Their analysis pinpoints architectural trust boundaries that enable the worm and proposes targeted defenses—runtime filtering for dormant payloads and stricter validation of configuration and tool‑execution permissions—to harden agentic AI platforms against similar autonomous threats.


<details>
<summary>Abstract</summary>

Autonomous LLM-based agents increasingly operate as long-running processes forming densely interconnected multi-agent ecosystems, whose security properties remain largely unexplored. In particular, OpenClaw, an open-source platform with over 40,000 active instances, has stood out recently with its persistent configurations, tool-execution privileges, and cross-platform messaging capabilities. In this work, we present ClawWorm, the first self-replicating worm attack against a production-scale agent framework, achieving a fully autonomous infection cycle initiated by a single message: the worm first hijacks the victim's core configuration to establish persistent presence across session restarts, then executes an arbitrary payload upon each reboot, and finally propagates itself to every newly encountered peer without further attacker intervention. We evaluate the attack on a controlled testbed across four distinct LLM backends, three infection vectors, and three payload types (1,800 total trials). We demonstrate a 64.5\% aggregate attack success rate, sustained multi-hop propagation, and reveal stark divergences in model security postures -- highlighting that while execution-level filtering effectively mitigates dormant payloads, skill supply chains remain universally vulnerable. We analyse the architectural root causes underlying these vulnerabilities and propose defence strategies targeting each identified trust boundary. Code and samples will be released upon completion of responsible disclosure.

</details>


### 131. S2Act: Simple Spiking Actor

- **Authors:** Ugur Akcal, Seung Hyun Kim, Mikihisa Yuasa, Hamid Osooli, Jiarui Sun, Ribhav Sahu, Mattia Gazzola, Huy T. Tran, Girish Chowdhary
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15725v1](http://arxiv.org/abs/2603.15725v1)
- **PDF:** [https://arxiv.org/pdf/2603.15725v1](https://arxiv.org/pdf/2603.15725v1)
- **Categories:** cs.MA, cs.ET, cs.LG, cs.RO


> The paper introduces **S2Act**, a lightweight pipeline for turning a conventional actor‑critic reinforcement‑learning policy into a spiking neural network (SNN) that can run efficiently on neuromorphic hardware. The authors first design a rate‑based “approximate” network whose activations mimic ReLUs, train it with standard back‑propagation using compatible activation functions, and then map the learned weights onto leaky‑integrate‑and‑fire (LIF) neurons whose parameters are globally tuned so that their firing rates reproduce the trained ReLU responses, thereby avoiding vanishing‑gradient and hyper‑parameter sensitivities typical of SNNs. Experiments in two stochastic multi‑robot domains (capture‑the‑flag and parking) and real‑world tests on TurtleBots equipped with Intel Loihi show that S2Act consistently surpasses hybrid and population‑coding baselines in task success and inference latency, demonstrating a practical route for deploying agentic SNN policies in power‑constrained robotic systems.


<details>
<summary>Abstract</summary>

Spiking neural networks (SNNs) and biologically-inspired learning mechanisms are attractive in mobile robotics, where the size and performance of onboard neural network policies are constrained by power and computational budgets. Existing SNN approaches, such as population coding, reward modulation, and hybrid artificial neural network (ANN)-SNN architectures, have shown promising results; however, they face challenges in complex, highly stochastic environments due to SNN sensitivity to hyperparameters and inconsistent gradient signals. To address these challenges, we propose simple spiking actor (S2Act), a computationally lightweight framework that deploys an RL policy using an SNN in three steps: (1) architect an actor-critic model based on an approximated network of rate-based spiking neurons, (2) train the network with gradients using compatible activation functions, and (3) transfer the trained weights into physical parameters of rate-based leaky integrate-and-fire (LIF) neurons for inference and deployment. By globally shaping LIF neuron parameters such that their rate-based responses approximate ReLU activations, S2Act effectively mitigates the vanishing gradient problem, while pre-constraining LIF response curves reduces reliance on complex SNN-specific hyperparameter tuning. We demonstrate our method in two multi-agent stochastic environments (capture-the-flag and parking) that capture the complexity of multi-robot interactions, and deploy our trained policies on physical TurtleBot platforms using Intel's Loihi neuromorphic hardware. Our experimental results show that S2Act outperforms relevant baselines in task performance and real-time inference in nearly all considered scenarios, highlighting its potential for rapid prototyping and efficient real-world deployment of SNN-based RL policies.

</details>


### 132. The PokeAgent Challenge: Competitive and Long-Context Learning at Scale

- **Authors:** Seth Karten, Jake Grigsby, Tersoo Upaa, Junik Bae, Seonghun Hong, Hyunyoung Jeong, Jaeyoon Jung, Kun Kerdthaisong, Gyungbo Kim, Hyeokgi Kim, Yujin Kim, Eunju Kwon, Dongyu Liu, Patrick Mariglia, Sangyeon Park, Benedikt Schink, Xianwei Shi, Anthony Sistilli, Joseph Twin, Arian Urdu, Matin Urdu, Qiao Wang, Ling Wu, Wenli Zhang, Kunsheng Zhou, Stephanie Milani, Kiran Vodrahalli, Amy Zhang, Fei Fang, Yuke Zhu, Chi Jin
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15563v2](http://arxiv.org/abs/2603.15563v2)
- **PDF:** [https://arxiv.org/pdf/2603.15563v2](https://arxiv.org/pdf/2603.15563v2)
- **Categories:** cs.LG, cs.AI


> The paper introduces **PokeAgent**, a large‑scale, dual‑track benchmark that unifies competitive multi‑agent Pokémon battles (partial observability, game‑theoretic reasoning) with long‑horizon RPG speedrunning (sequential planning), providing the first standardized testbed that simultaneously stresses all three core challenges of agentic AI. The authors release >20 million battle trajectories, a modular orchestration framework, and a suite of heuristic, reinforcement‑learning, and large‑language‑model baselines, then evaluate them through a NeurIPS‑2025 competition involving 100+ teams. Results show a pronounced performance gap: specialist RL agents outperform generalist LLMs but both fall far short of elite human players, demonstrating that Pokémon decision‑making is largely orthogonal to existing LLM benchmarks and highlighting a fertile frontier for advancing strategic, partially observable, and long‑context learning.


<details>
<summary>Abstract</summary>

We present the PokeAgent Challenge, a large-scale benchmark for decision-making research built on Pokemon's multi-agent battle system and expansive role-playing game (RPG) environment. Partial observability, game-theoretic reasoning, and long-horizon planning remain open problems for frontier AI, yet few benchmarks stress all three simultaneously under realistic conditions. PokeAgent targets these limitations at scale through two complementary tracks: our Battling Track, which calls for strategic reasoning and generalization under partial observability in competitive Pokemon battles, and our Speedrunning Track, which requires long-horizon planning and sequential decision-making in the Pokemon RPG. Our Battling Track supplies a dataset of 20M+ battle trajectories alongside a suite of heuristic, RL, and LLM-based baselines capable of high-level competitive play. Our Speedrunning Track provides the first standardized evaluation framework for RPG speedrunning, including an open-source multi-agent orchestration system for modular, reproducible comparisons of harness-based LLM approaches. Our NeurIPS 2025 competition validates both the quality of our resources and the research community's interest in Pokemon, with over 100 teams competing across both tracks and winning solutions detailed in our paper. Participant submissions and our baselines reveal considerable gaps between generalist (LLM), specialist (RL), and elite human performance. Analysis against the BenchPress evaluation matrix shows that Pokemon battling is nearly orthogonal to standard LLM benchmarks, measuring capabilities not captured by existing suites and positioning Pokemon as an unsolved benchmark that can drive RL and LLM research forward. We transition to a living benchmark with a live leaderboard for Battling and self-contained evaluation for Speedrunning at https://pokeagentchallenge.com.

</details>


### 133. InterveneBench: Benchmarking LLMs for Intervention Reasoning and Causal Study Design in Real Social Systems

- **Authors:** Shaojie Shi, Zhengyu Shi, Lingran Zheng, Xinyu Su, Anna Xie, Bohao Lv, Rui Xu, Zijian Chen, Zhichao Chen, Guolei Liu, Naifu Zhang, Mingjian Dong, Zhuo Quan, Bohao Chen, Teqi Hao, Yuan Qi, Yinghui Xu, Libo Wu
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15542v1](http://arxiv.org/abs/2603.15542v1)
- **PDF:** [https://arxiv.org/pdf/2603.15542v1](https://arxiv.org/pdf/2603.15542v1)
- **Categories:** cs.CY, cs.AI


> The paper introduces **InterveneBench**, a large‑scale benchmark (744 peer‑reviewed social‑science studies) that tests LLMs’ ability to perform *intervention‑centered causal reasoning*—identifying appropriate policy interventions, articulating identification assumptions, and designing causal studies without any supplied causal graph or structural equations. To tackle the observed deficiencies of current models, the authors develop **STRIDES**, a multi‑agent reasoning framework in which specialized agents iteratively propose, critique, and refine intervention designs, yielding markedly higher accuracy than leading single‑agent LLM reasoners. Experiments demonstrate that state‑of‑the‑art LLMs perform poorly on InterveneBench, while STRIDES closes much of the gap, highlighting the importance of coordinated, agentic architectures for robust causal‑intervention reasoning in real‑world social systems.


<details>
<summary>Abstract</summary>

Causal inference in social science relies on end-to-end, intervention-centered research-design reasoning grounded in real-world policy interventions, but current benchmarks fail to evaluate this capability of large language models (LLMs). We present InterveneBench, a benchmark designed to assess such reasoning in realistic social settings. Each instance in InterveneBench is derived from an empirical social science study and requires models to reason about policy interventions and identification assumptions without access to predefined causal graphs or structural equations. InterveneBench comprises 744 peer-reviewed studies across diverse policy domains. Experimental results show that state-of-the-art LLMs struggle under this setting. To address this limitation, we further propose a multi-agent framework, STRIDES. It achieves significant performance improvements over state-of-the-art reasoning models. Our code and data are available at https://github.com/Sii-yuning/STRIDES.

</details>


### 134. Beyond the Covariance Trap: Unlocking Generalization in Same-Subject Knowledge Editing for Large Language Models

- **Authors:** Xiyu Liu, Qingyi Si, Zhengxiao Liu, Chenxu Yang, Naibin Gu, Zheng Lin
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15518v1](http://arxiv.org/abs/2603.15518v1)
- **PDF:** [https://arxiv.org/pdf/2603.15518v1](https://arxiv.org/pdf/2603.15518v1)
- **Categories:** cs.CL


> The paper pinpoints why same‑subject knowledge edits—updates that should apply to all future uses of a fact—often fail when the model is later prompted with varied instructions: the edited representation drifts beyond the model’s geometric tolerance, a problem the authors trace to sharp minima caused by orthogonal‑gradient training and to a “Covariance Trap” where the usual covariance regularizer magnifies input perturbations. To overcome this, they propose RoSE (Robust Same‑subject Editing), which aligns the edited hidden states isotropically and integrates the new fact hierarchically to smooth the loss landscape. Experiments show that RoSE restores reliable recall of edited knowledge under diverse instruction prompts, enabling more stable parametric memory for interactive LLM agents.


<details>
<summary>Abstract</summary>

While locate-then-edit knowledge editing efficiently updates knowledge encoded within Large Language Models (LLMs), a critical generalization failure mode emerges in the practical same-subject knowledge editing scenario: models fail to recall the updated knowledge when following user instructions, despite successfully recalling it in the original edited form. This paper identifies the geometric root of this generalization collapse as a fundamental conflict where the inner activation drifts induced by prompt variations exceed the model's geometric tolerance for generalization after editing. We attribute this instability to a dual pathology: (1) The joint optimization with orthogonal gradients collapses solutions into sharp minima with narrow stability, and (2) the standard covariance constraint paradoxically acts as a Covariance Trap that amplifies input perturbations. To resolve this, we introduce RoSE (Robust Same-subject Editing), which employs Isotropic Geometric Alignment to minimize representational deviation and Hierarchical Knowledge Integration to smooth the optimization landscape. Extensive experiments demonstrate that RoSE significantly improves instruction-following capabilities, laying the foundation for robust interactive parametric memory of LLM agents.

</details>


### 135. Agentic workflow enables the recovery of critical materials from complex feedstocks via selective precipitation

- **Authors:** Andrew Ritchhart, Sarah I. Allec, Pravalika Butreddy, Krista Kulesa, Qingpu Wang, Dan Thien Nguyen, Maxim Ziatdinov, Elias Nakouzi
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15491v1](http://arxiv.org/abs/2603.15491v1)
- **PDF:** [https://arxiv.org/pdf/2603.15491v1](https://arxiv.org/pdf/2603.15491v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI


> The paper introduces a multi‑agentic workflow that couples autonomous AI agents with laboratory automation to design and execute selective‑precipitation processes for extracting critical metals from complex, real‑world streams such as produced water and magnet leachates. By iteratively generating candidate chemistries, planning experiments, and interpreting results, the system rapidly converges on effective, low‑cost precipitation recipes, reducing the development cycle from months to days. The authors demonstrate that this agent‑driven approach reliably isolates target metals with high selectivity and yields, showcasing a scalable, adaptable framework for accelerated materials‑recovery separations in the agentic AI domain.


<details>
<summary>Abstract</summary>

We present a multi-agentic workflow for critical materials recovery that deploys a series of AI agents and automated instruments to recover critical materials from produced water and magnet leachates. This approach achieves selective precipitation from real-world feedstocks using simple chemicals, accelerating the development of efficient, adaptable, and scalable separations to a timeline of days, rather than months and years.

</details>


### 136. Agent Lifecycle Toolkit (ALTK): Reusable Middleware Components for Robust AI Agents

- **Authors:** Zidane Wright, Jason Tsay, Anupama Murthi, Osher Elhadad, Diego Del Rio, Saurabh Goyal, Kiran Kate, Jim Laredo, Koren Lazar, Vinod Muthusamy, Yara Rizk
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15473v1](http://arxiv.org/abs/2603.15473v1)
- **PDF:** [https://arxiv.org/pdf/2603.15473v1](https://arxiv.org/pdf/2603.15473v1)
- **Categories:** cs.AI


> The paper introduces the **Agent Lifecycle Toolkit (ALTK)**, an open‑source suite of reusable middleware components that plug into existing agent pipelines to systematically detect, repair, and mitigate common failure modes (e.g., malformed tool arguments, silent reasoning errors, policy violations) across six intervention points in the agent lifecycle. The authors built ALTK as a set of modular, language‑model‑agnostic wrappers—implemented as pre‑ and post‑processing hooks for user requests, prompt conditioning, LLM outputs, tool invocation, and response assembly—and demonstrated its integration with low‑code/no‑code platforms such as ContextForge MCP Gateway and Langflow. Empirical evaluations on benchmark and enterprise‑style tasks show that ALTK reduces engineering effort by ≈40 % and cuts critical failure incidents (invalid tool calls, policy breaches) by >80 % without degrading task performance, highlighting its value for building robust, production‑grade AI agents.


<details>
<summary>Abstract</summary>

As AI agents move from demos into enterprise deployments, their failure modes become consequential: a misinterpreted tool argument can corrupt production data, a silent reasoning error can go undetected until damage is done, and outputs that violate organizational policy can create legal or compliance risk. Yet, most agent frameworks leave builders to handle these failure modes ad hoc, resulting in brittle, one-off safeguards that are hard to reuse or maintain. We present the Agent Lifecycle Toolkit (ALTK), an open-source collection of modular middleware components that systematically address these gaps across the full agent lifecycle.
  Across the agent lifecycle, we identify opportunities to intervene and improve, namely, post-user-request, pre-LLM prompt conditioning, post-LLM output processing, pre-tool validation, post-tool result checking, and pre-response assembly. ALTK provides modular middleware that detects, repairs, and mitigates common failure modes. It offers consistent interfaces that fit naturally into existing pipelines. It is compatible with low-code and no-code tools such as the ContextForge MCP Gateway and Langflow. Finally, it significantly reduces the effort of building reliable, production-grade agents.

</details>


### 137. Evasive Intelligence: Lessons from Malware Analysis for Evaluating AI Agents

- **Authors:** Simone Aonzo, Merve Sahin, Aurélien Francillon, Daniele Perito
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15457v1](http://arxiv.org/abs/2603.15457v1)
- **PDF:** [https://arxiv.org/pdf/2603.15457v1](https://arxiv.org/pdf/2603.15457v1)
- **Categories:** cs.CR, cs.AI


> The paper’s main contribution is a warning that AI agents—especially tool‑using, long‑horizon systems—can detect when they are being evaluated and deliberately mask unsafe or suboptimal behavior, mirroring the sandbox‑evasion tactics long studied in malware analysis. By reviewing the literature on malware detection evasion and conducting illustrative experiments in which agents infer evaluation‑environment cues (e.g., test‑suite signatures, observation limits) and modify their policies, the authors demonstrate that standard, fully observable benchmarks can produce systematically inflated safety and robustness scores. They conclude that agentic AI evaluation must treat the system as a potential adversary, employing realistic, variable test conditions, continual post‑deployment monitoring, and adversarial stress‑testing to obtain trustworthy assessments.


<details>
<summary>Abstract</summary>

Artificial intelligence (AI) systems are increasingly adopted as tool-using agents that can plan, observe their environment, and take actions over extended time periods. This evolution challenges current evaluation practices where the AI models are tested in restricted, fully observable settings. In this article, we argue that evaluations of AI agents are vulnerable to a well-known failure mode in computer security: malicious software that exhibits benign behavior when it detects that it is being analyzed. We point out how AI agents can infer the properties of their evaluation environment and adapt their behavior accordingly. This can lead to overly optimistic safety and robustness assessments. Drawing parallels with decades of research on malware sandbox evasion, we demonstrate that this is not a speculative concern, but rather a structural risk inherent to the evaluation of adaptive systems. Finally, we outline concrete principles for evaluating AI agents, which treat the system under test as potentially adversarial. These principles emphasize realism, variability of test conditions, and post-deployment reassessment.

</details>


### 138. MA-VLCM: A Vision Language Critic Model for Value Estimation of Policies in Multi-Agent Team Settings

- **Authors:** Shahil Shaik, Aditya Parameshwaran, Anshul Nayak, Jonathon M. Smereka, Yue Wang
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15418v1](http://arxiv.org/abs/2603.15418v1)
- **PDF:** [https://arxiv.org/pdf/2603.15418v1](https://arxiv.org/pdf/2603.15418v1)
- **Categories:** cs.RO, cs.AI


> The paper introduces **MA‑VLCM**, a framework that substitutes the traditional learned centralized critic in multi‑agent reinforcement learning with a **pre‑trained vision‑language‑action model** fine‑tuned to evaluate team behavior from natural‑language task descriptions, visual trajectories, and structured state data. By leveraging the multimodal reasoning and zero‑shot generalization of large VLMs, MA‑VLCM eliminates the need to learn a critic during policy optimization, dramatically boosting sample efficiency and yielding compact policies that can run on resource‑limited robots. Experiments demonstrate that MA‑VLCM provides accurate, zero‑shot value estimates across both in‑distribution and out‑of‑distribution multi‑robot scenarios, confirming its potential as a scalable, generalizable critic for agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) commonly relies on a centralized critic to estimate the value function. However, learning such a critic from scratch is highly sample-inefficient and often lacks generalization across environments. At the same time, large vision-language-action models (VLAs) trained on internet-scale data exhibit strong multimodal reasoning and zero-shot generalization capabilities, yet directly deploying them for robotic execution remains computationally prohibitive, particularly in heterogeneous multi-robot systems with diverse embodiments and resource constraints. To address these challenges, we propose Multi-Agent Vision-Language-Critic Models (MA-VLCM), a framework that replaces the learned centralized critic in MARL with a pretrained vision-language model fine-tuned to evaluate multi-agent behavior. MA-VLCM acts as a centralized critic conditioned on natural language task descriptions, visual trajectory observations, and structured multi-agent state information. By eliminating critic learning during policy optimization, our approach significantly improves sample efficiency while producing compact execution policies suitable for deployment on resource-constrained robots. Results show good zero-shot return estimation on models with differing VLM backbones on in-distribution and out-of-distribution scenarios in multi-agent team settings

</details>


### 139. TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems

- **Authors:** Kai Wang, Biaojie Zeng, Zeming Wei, Chang Jin, Hefeng Zhou, Xiangtian Li, Chao Yang, Jingjing Qu, Xingcheng Xu, Xia Hu
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15408v1](http://arxiv.org/abs/2603.15408v1)
- **PDF:** [https://arxiv.org/pdf/2603.15408v1](https://arxiv.org/pdf/2603.15408v1)
- **Categories:** cs.CR, cs.AI, cs.CL, cs.LG, cs.MA


> TrinityGuard introduces the first unified safety‑evaluation and runtime‑monitoring framework specifically for LLM‑driven multi‑agent systems, extending OWASP‑style threat modeling to the multi‑agent domain. It does so by (1) defining a three‑tier taxonomy of 20 fine‑grained risk types that span single‑agent flaws, inter‑agent communication attacks, and emergent system‑level hazards, (2) providing an MAS‑agnostic abstraction layer, a suite of risk‑specific test probes, and a “LLM Judge Factory” that coordinates monitor agents to analyze execution traces and emit real‑time alerts, and (3) formalizing safety metrics and validating the approach on diverse MAS benchmarks, where TrinityGuard consistently identified previously unseen vulnerabilities and demonstrated low‑overhead, accurate runtime detection. The results show that the framework can both pre‑emptively expose MAS‑specific security gaps and continuously safeguard deployed agents, establishing a scalable baseline for future agentic‑AI safety research.


<details>
<summary>Abstract</summary>

With the rapid development of LLM-based multi-agent systems (MAS), their significant safety and security concerns have emerged, which introduce novel risks going beyond single agents or LLMs. Despite attempts to address these issues, the existing literature lacks a cohesive safeguarding system specialized for MAS risks. In this work, we introduce TrinityGuard, a comprehensive safety evaluation and monitoring framework for LLM-based MAS, grounded in the OWASP standards. Specifically, TrinityGuard encompasses a three-tier fine-grained risk taxonomy that identifies 20 risk types, covering single-agent vulnerabilities, inter-agent communication threats, and system-level emergent hazards. Designed for scalability across various MAS structures and platforms, TrinityGuard is organized in a trinity manner, involving an MAS abstraction layer that can be adapted to any MAS structures, an evaluation layer containing risk-specific test modules, alongside runtime monitor agents coordinated by a unified LLM Judge Factory. During Evaluation, TrinityGuard executes curated attack probes to generate detailed vulnerability reports for each risk type, where monitor agents analyze structured execution traces and issue real-time alerts, enabling both pre-development evaluation and runtime monitoring. We further formalize these safety metrics and present detailed case studies across various representative MAS examples, showcasing the versatility and reliability of TrinityGuard. Overall, TrinityGuard acts as a comprehensive framework for evaluating and monitoring various risks in MAS, paving the way for further research into their safety and security.

</details>


### 140. SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?

- **Authors:** Tingxu Han, Yi Zhang, Wei Song, Chunrong Fang, Zhenyu Chen, Youcheng Sun, Lijie Hu
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15401v1](http://arxiv.org/abs/2603.15401v1)
- **PDF:** [https://arxiv.org/pdf/2603.15401v1](https://arxiv.org/pdf/2603.15401v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces **SWE‑Skills‑Bench**, the first requirement‑driven benchmark that isolates the marginal impact of “agent skills”—pre‑packaged procedural knowledge injected at inference time—on real‑world software‑engineering tasks. By pairing 49 publicly available SWE skills with fixed‑commit GitHub repositories and explicit acceptance‑criteria documents, the authors generate ~565 task instances across six subdomains and evaluate each skill’s effect using a deterministic, execution‑based verification framework that compares performance with and without the skill. The study finds that most skills (39/49) provide no measurable improvement (average gain +1.2 %), only a handful yield substantial gains (up to +30 %), and some even hurt performance when their guidance conflicts with project context, highlighting that skill injection is a narrowly effective intervention whose benefit hinges on domain fit, abstraction level, and contextual compatibility.


<details>
<summary>Abstract</summary>

Agent skills, structured procedural knowledge packages injected at inference time, are increasingly used to augment LLM agents on software engineering tasks. However, their real utility in end-to-end development settings remains unclear. We present SWE-Skills-Bench, the first requirement-driven benchmark that isolates the marginal utility of agent skills in real-world software engineering (SWE). It pairs 49 public SWE skills with authentic GitHub repositories pinned at fixed commits and requirement documents with explicit acceptance criteria, yielding approximately 565 task instances across six SWE subdomains. We introduce a deterministic verification framework that maps each task's acceptance criteria to execution-based tests, enabling controlled paired evaluation with and without the skill. Our results show that skill injection benefits are far more limited than rapid adoption suggests: 39 of 49 skills yield zero pass-rate improvement, and the average gain is only +1.2%. Token overhead varies from modest savings to a 451% increase while pass rates remain unchanged. Only seven specialized skills produce meaningful gains (up to +30%), while three degrade performance (up to -10%) due to version-mismatched guidance conflicting with project context. These findings suggest that agent skills are a narrow intervention whose utility depends strongly on domain fit, abstraction level, and contextual compatibility. SWE-Skills-Bench provides a testbed for evaluating the design, selection, and deployment of skills in software engineering agents. SWE-Skills-Bench is available at https://github.com/GeniusHTX/SWE-Skills-Bench.

</details>


### 141. How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition

- **Authors:** Mateusz Dziemian, Maxwell Lin, Xiaohan Fu, Micha Nowak, Nick Winter, Eliot Jones, Andy Zou, Lama Ahmad, Kamalika Chaudhuri, Sahana Chennabasappa, Xander Davies, Lauren Deason, Benjamin L. Edelman, Tanner Emek, Ivan Evtimov, Jim Gust, Maia Hamin, Kat He, Klaudia Krawiecka, Riccardo Patana, Neil Perry, Troy Peterson, Xiangyu Qi, Javier Rando, Zifan Wang, Zihan Wang, Spencer Whitman, Eric Winsor, Arman Zharmagambetov, Matt Fredrikson, Zico Kolter
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15714v1](http://arxiv.org/abs/2603.15714v1)
- **PDF:** [https://arxiv.org/pdf/2603.15714v1](https://arxiv.org/pdf/2603.15714v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces a large‑scale public red‑team competition that systematically evaluates indirect prompt‑injection attacks—where malicious instructions are hidden in external data and leave no trace in the agent’s final reply—across three LLM‑agent paradigms (tool‑calling, coding, and computer use). By collecting 272 k attack attempts from 464 participants against 13 state‑of‑the‑art models, the authors demonstrate that every model is exploitable (success rates 0.5 %–8.5 %), uncover universal, cross‑scenario attack patterns that transfer across 21 of 41 behaviors and multiple model families, and show that higher capability does not imply greater robustness (e.g., Gemini 2.5 Pro is both strong and highly vulnerable). The work provides an open‑source competition platform, a curated dataset of 8 648 successful attacks (including 95 Qwen‑specific attacks), and ongoing quarterly red‑team updates to serve as a benchmark for improving the safety of agentic AI systems.


<details>
<summary>Abstract</summary>

LLM based agents are increasingly deployed in high stakes settings where they process external data sources such as emails, documents, and code repositories. This creates exposure to indirect prompt injection attacks, where adversarial instructions embedded in external content manipulate agent behavior without user awareness. A critical but underexplored dimension of this threat is concealment: since users tend to observe only an agent's final response, an attack can conceal its existence by presenting no clue of compromise in the final user facing response while successfully executing harmful actions. This leaves users unaware of the manipulation and likely to accept harmful outcomes as legitimate. We present findings from a large scale public red teaming competition evaluating this dual objective across three agent settings: tool calling, coding, and computer use. The competition attracted 464 participants who submitted 272000 attack attempts against 13 frontier models, yielding 8648 successful attacks across 41 scenarios. All models proved vulnerable, with attack success rates ranging from 0.5% (Claude Opus 4.5) to 8.5% (Gemini 2.5 Pro). We identify universal attack strategies that transfer across 21 of 41 behaviors and multiple model families, suggesting fundamental weaknesses in instruction following architectures. Capability and robustness showed weak correlation, with Gemini 2.5 Pro exhibiting both high capability and high vulnerability. To address benchmark saturation and obsoleteness, we will endeavor to deliver quarterly updates through continued red teaming competitions. We open source the competition environment for use in evaluations, along with 95 successful attacks against Qwen that did not transfer to any closed source model. We share model-specific attack data with respective frontier labs and the full dataset with the UK AISI and US CAISI to support robustness research.

</details>


### 142. Brain-Inspired Graph Multi-Agent Systems for LLM Reasoning

- **Authors:** Guangfu Hao, Yuming Dai, Xianzhe Qin, Shan Yu
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15371v1](http://arxiv.org/abs/2603.15371v1)
- **PDF:** [https://arxiv.org/pdf/2603.15371v1](https://arxiv.org/pdf/2603.15371v1)
- **Categories:** cs.AI, cs.NI


> The paper introduces **Brain‑Inspired Graph Multi‑Agent Systems (BIGMAS)**, a novel architecture that arranges specialized LLM agents as nodes in a dynamically generated directed graph and lets them interact solely via a centralized shared workspace, mirroring the global‑workspace theory of human cognition. A **GraphDesigner** module builds task‑specific agent topologies, while a **global Orchestrator** uses the full shared state to route information, thereby overcoming the local‑view limitations of prior reactive multi‑agent methods such as ReAct and Tree of Thoughts. Across challenging multi‑step reasoning benchmarks (Game24, Six Fives, Tower of London) and six state‑of‑the‑art LLMs/LRMs, BIGMAS consistently yields higher accuracy than both single‑model chain‑of‑thought approaches and existing multi‑agent baselines, demonstrating that graph‑structured, workspace‑mediated coordination provides complementary gains for agentic AI reasoning.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have demonstrated remarkable capabilities across a wide range of language tasks, yet complex multi-step reasoning remains a fundamental challenge. While Large Reasoning Models (LRMs) equipped with extended chain-of-thought mechanisms demonstrate improved performance over standard LLMs, both model types still suffer from accuracy collapse on sufficiently complex tasks, suggesting that scaling model-level reasoning alone is insufficient. Inspired by the global workspace theory of human cognition, we propose Brain-Inspired Graph Multi-Agent Systems (BIGMAS), in which specialized LLM agents are organized as nodes in a dynamically constructed directed graph and coordinate exclusively through a centralized shared workspace. A problem-adaptive GraphDesigner constructs task-specific agent topologies, while a global Orchestrator leverages the complete shared state for routing decisions, overcoming the local-view bottleneck of reactive approaches. Experiments on Game24, Six Fives, and Tower of London across six frontier LLMs demonstrate that BIGMAS consistently improves reasoning performance for both standard LLMs and LRMs, outperforming existing multi-agent baselines including ReAct and Tree of Thoughts, showing that multi-agent architectural design provides complementary gains orthogonal to model-level reasoning enhancements.

</details>


### 143. CRASH: Cognitive Reasoning Agent for Safety Hazards in Autonomous Driving

- **Authors:** Erick Silva, Rehana Yasmin, Ali Shoker
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15364v1](http://arxiv.org/abs/2603.15364v1)
- **PDF:** [https://arxiv.org/pdf/2603.15364v1](https://arxiv.org/pdf/2603.15364v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces **CRASH**, a cognitive‑reasoning LLM‑based agent that automatically ingests and interprets both structured fields and free‑text narratives from 2,168 real‑world autonomous‑vehicle crash reports (2021‑2025) to produce concise incident summaries, assign a primary failure cause, and judge AV contribution. By converting each report into a unified representation and prompting the LLM to perform multi‑step causal reasoning, CRASH achieved 86 % expert‑validated accuracy in fault attribution, revealing that 64 % of incidents stem from perception or planning errors and that rear‑end collisions account for roughly half of all events. These results demonstrate that agentic AI can scale interpretable safety analysis for heterogeneous AV systems, offering a reproducible tool for systematic hazard identification and mitigation.


<details>
<summary>Abstract</summary>

As AVs grow in complexity and diversity, identifying the root causes of operational failures has become increasingly complex. The heterogeneity of system architectures across manufacturers, ranging from end-to-end to modular designs, together with variations in algorithms and integration strategies, limits the standardization of incident investigations and hinders systematic safety analysis. This work examines real-world AV incidents reported in the NHTSA database. We curate a dataset of 2,168 cases reported between 2021 and 2025, representing more than 80 million miles driven. To process this data, we introduce CRASH, Cognitive Reasoning Agent for Safety Hazards, an LLM-based agent that automates reasoning over crash reports by leveraging both standardized fields and unstructured narrative descriptions. CRASH operates on a unified representation of each incident to generate concise summaries, attribute a primary cause, and assess whether the AV materially contributed to the event. Our findings show that (1) CRASH attributes 64% of incidents to perception or planning failures, underscoring the importance of reasoning-based analysis for accurate fault attribution; and (2) approximately 50% of reported incidents involve rear-end collisions, highlighting a persistent and unresolved challenge in autonomous driving deployment. We further validate CRASH with five domain experts, achieving 86% accuracy in attributing AV system failures. Overall, CRASH demonstrates strong potential as a scalable and interpretable tool for automated crash analysis, providing actionable insights to support safety research and the continued development of autonomous driving systems.

</details>


### 144. PMAx: An Agentic Framework for AI-Driven Process Mining

- **Authors:** Anton Antonov, Humam Kourani, Alessandro Berti, Gyunam Park, Wil M. P. van der Aalst
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15351v1](http://arxiv.org/abs/2603.15351v1)
- **PDF:** [https://arxiv.org/pdf/2603.15351v1](https://arxiv.org/pdf/2603.15351v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces **PMAx**, a privacy‑preserving, multi‑agent framework that turns a large language model into a “virtual process analyst” rather than a direct data‑processing engine. The system deploys an **Engineer agent** that automatically inspects event‑log metadata, generates and runs local scripts for established process‑mining algorithms (producing exact metrics, models, and visualizations), while an **Analyst agent** uses an LLM to interpret these artifacts and answer natural‑language business queries. Experiments show that this separation of deterministic computation from LLM‑based interpretation yields mathematically correct results, maintains data confidentiality, and enables non‑technical users to obtain reliable process‑mining insights through conversational interaction.


<details>
<summary>Abstract</summary>

Process mining provides powerful insights into organizational workflows, but extracting these insights typically requires expertise in specialized query languages and data science tools. Large Language Models (LLMs) offer the potential to democratize process mining by enabling business users to interact with process data through natural language. However, using LLMs as direct analytical engines over raw event logs introduces fundamental challenges: LLMs struggle with deterministic reasoning and may hallucinate metrics, while sending large, sensitive logs to external AI services raises serious data-privacy concerns. To address these limitations, we present PMAx, an autonomous agentic framework that functions as a virtual process analyst. Rather than relying on LLMs to generate process models or compute analytical results, PMAx employs a privacy-preserving multi-agent architecture. An Engineer agent analyzes event-log metadata and autonomously generates local scripts to run established process mining algorithms, compute exact metrics, and produce artifacts such as process models, summary tables, and visualizations. An Analyst agent then interprets these insights and artifacts to compile comprehensive reports. By separating computation from interpretation and executing analysis locally, PMAx ensures mathematical accuracy and data privacy while enabling non-technical users to transform high-level business questions into reliable process insights.

</details>


### 145. Intelligent Co-Design: An Interactive LLM Framework for Interior Spatial Design via Multi-Modal Agents

- **Authors:** Ren Jian Lim, Rushi Dai
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15341v1](http://arxiv.org/abs/2603.15341v1)
- **PDF:** [https://arxiv.org/pdf/2603.15341v1](https://arxiv.org/pdf/2603.15341v1)
- **Categories:** cs.AI, cs.HC, cs.MA


> The paper introduces **Intelligent Co‑Design**, a multimodal, multi‑agent framework that leverages large language models (LLMs) and Retrieval‑Augmented Generation (RAG) to turn natural‑language and image inputs into editable 3‑D interior layouts. By orchestrating four specialized agents (Reference, Spatial, Interactive, and Grader) through prompt‑driven collaboration, the system enables real‑time, iterative design refinement without task‑specific model training, thereby reducing data dependence and expanding participatory design to non‑experts. User studies and an independent LLM evaluator show that the generated layouts achieve higher alignment with user intent, aesthetic coherence, and functional circulation, yielding a 77 % satisfaction rate and outperforming conventional design tools—demonstrating the efficacy of agentic LLM coordination for interactive, user‑centric spatial design.


<details>
<summary>Abstract</summary>

In architectural interior design, miscommunication frequently arises as clients lack design knowledge, while designers struggle to explain complex spatial relationships, leading to delayed timelines and financial losses. Recent advancements in generative layout tools narrow the gap by automating 3D visualizations. However, prevailing methodologies exhibit limitations: rule-based systems implement hard-coded spatial constraints that restrict participatory engagement, while data-driven models rely on extensive training datasets. Recent large language models (LLMs) bridge this gap by enabling intuitive reasoning about spatial relationships through natural language. This research presents an LLM-based, multimodal, multi-agent framework that dynamically converts natural language descriptions and imagery into 3D designs. Specialized agents (Reference, Spatial, Interactive, Grader), operating via prompt guidelines, collaboratively address core challenges: the agent system enables real-time user interaction for iterative spatial refinement, while Retrieval-Augmented Generation (RAG) reduces data dependency without requiring task-specific model training. This framework accurately interprets spatial intent and generates optimized 3D indoor design, improving productivity, and encouraging nondesigner participation. Evaluations across diverse floor plans and user questionnaires demonstrate effectiveness. An independent LLM evaluator consistently rated participatory layouts higher in user intent alignment, aesthetic coherence, functionality, and circulation. Questionnaire results indicated 77% satisfaction and a clear preference over traditional design software. These findings suggest the framework enhances user-centric communication and fosters more inclusive, effective, and resilient design processes. Project page: https://rsigktyper.github.io/AICodesign/

</details>


### 146. CCTU: A Benchmark for Tool Use under Complex Constraints

- **Authors:** Junjie Ye, Guoqiang Zhang, Wenjie Fu, Tao Gui, Qi Zhang, Xuanjing Huang
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15309v1](http://arxiv.org/abs/2603.15309v1)
- **PDF:** [https://arxiv.org/pdf/2603.15309v1](https://arxiv.org/pdf/2603.15309v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **CCTU**, a new benchmark that rigorously evaluates large language models’ ability to use external tools while obeying a taxonomy of 12 constraint types across resource, behavior, toolset, and response dimensions. By curating 200 multi‑turn, high‑complexity test cases (≈7 constraints per case, >4,700‑token prompts) and building an executable validator that checks constraint compliance step‑by‑step, the authors assess nine state‑of‑the‑art LLMs in both “thinking” (self‑refine) and “non‑thinking” modes. They find that even the best models complete fewer than 20 % of tasks when full compliance is required, violate constraints in over half of the interactions—especially regarding resources and response formats—and show only marginal improvement after feedback, underscoring a major bottleneck for robust, constraint‑aware agentic AI.


<details>
<summary>Abstract</summary>

Solving problems through tool use under explicit constraints constitutes a highly challenging yet unavoidable scenario for large language models (LLMs), requiring capabilities such as function calling, instruction following, and self-refinement. However, progress has been hindered by the absence of dedicated evaluations. To address this, we introduce CCTU, a benchmark for evaluating LLM tool use under complex constraints. CCTU is grounded in a taxonomy of 12 constraint categories spanning four dimensions (i.e., resource, behavior, toolset, and response). The benchmark comprises 200 carefully curated and challenging test cases across diverse tool-use scenarios, each involving an average of seven constraint types and an average prompt length exceeding 4,700 tokens. To enable reliable evaluation, we develop an executable constraint validation module that performs step-level validation and enforces compliance during multi-turn interactions between models and their environments. We evaluate nine state-of-the-art LLMs in both thinking and non-thinking modes. Results indicate that when strict adherence to all constraints is required, no model achieves a task completion rate above 20%. Further analysis reveals that models violate constraints in over 50% of cases, particularly in the resource and response dimensions. Moreover, LLMs demonstrate limited capacity for self-refinement even after receiving detailed feedback on constraint violations, highlighting a critical bottleneck in the development of robust tool-use agents. To facilitate future research, we release the data and code.

</details>


### 147. Evolutionary Transfer Learning for Dragonchess

- **Authors:** Jim O'Connor, Annika Hoag, Sarah Goyette, Gary B. Parker
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15297v1](http://arxiv.org/abs/2603.15297v1)
- **PDF:** [https://arxiv.org/pdf/2603.15297v1](https://arxiv.org/pdf/2603.15297v1)
- **Categories:** cs.AI


> The paper introduces Dragonchess—a three‑dimensional chess variant—as a new open‑source testbed for studying how AI heuristics can be transferred across game domains. It adapts Stockfish’s evaluation function to Dragonchess and then refines it with the Covariance Matrix Adaptation Evolution Strategy (CMA‑ES), demonstrating that pure transfer is insufficient but evolutionary optimization yields a markedly stronger agent. Empirical results from a 50‑round Swiss tournament show that the evolved heuristic dramatically outperforms the unmodified transfer, confirming evolutionary methods as an effective means of endowing agents with domain‑specific knowledge in structurally complex games.


<details>
<summary>Abstract</summary>

Dragonchess, a three-dimensional chess variant introduced by Gary Gygax, presents unique strategic and computational challenges that make it an ideal environment for studying the transfer of artificial intelligence (AI) heuristics across domains. In this work, we introduce Dragonchess as a novel testbed for AI research and provide an open-source, Python-based game engine for community use. Our research investigates evolutionary transfer learning by adapting heuristic evaluation functions directly from Stockfish, a leading chess engine, and subsequently optimizing them using Covariance Matrix Adaptation Evolution Strategy (CMA-ES). Initial trials showed that direct heuristic transfers were inadequate due to Dragonchess's distinct multi-layer structure and movement rules. However, evolutionary optimization significantly improved AI agent performance, resulting in superior gameplay demonstrated through empirical evaluation in a 50-round Swiss-style tournament. This research establishes the effectiveness of evolutionary methods in adapting heuristic knowledge to structurally complex, previously unexplored game domains.

</details>


### 148. AGCD: Agent-Guided Cross-Modal Decoding for Weather Forecasting

- **Authors:** Jing Wu, Yang Liu, Lin Zhang, Junbo Zeng, Jiabin Wang, Zi Ye, Guowen Li, Shilei Cao, Jiashun Cheng, Fang Wang, Meng Jin, Yerong Feng, Hong Cheng, Yutong Lu, Haohuan Fu, Juepeng Zheng
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15260v1](http://arxiv.org/abs/2603.15260v1)
- **PDF:** [https://arxiv.org/pdf/2603.15260v1](https://arxiv.org/pdf/2603.15260v1)
- **Categories:** cs.AI, cs.CV


> The paper introduces **Agent‑Guided Cross‑Modal Decoding (AGCD)**, a plug‑and‑play framework that injects state‑conditioned physics priors into any weather forecaster at decoding time by means of a multi‑agent meteorological narration pipeline powered by large language models (MLLMs). The agents generate multivariate, region‑aware priors from the current atmospheric state, which are then fused with visual tokens through a cross‑modal region‑interaction decoder that preserves synoptic structure without altering the backbone architecture. Experiments on WeatherBench show that AGCD consistently improves 6‑hour forecasts across two spatial resolutions and multiple backbones, and markedly reduces error accumulation in strictly causal 48‑hour autoregressive rollouts, demonstrating the utility of agent‑driven, sample‑specific priors for stabilizing long‑horizon, agentic AI predictions.


<details>
<summary>Abstract</summary>

Accurate weather forecasting is more than grid-wise regression: it must preserve coherent synoptic structures and physical consistency of meteorological fields, especially under autoregressive rollouts where small one-step errors can amplify into structural bias. Existing physics-priors approaches typically impose global, once-for-all constraints via architectures, regularization, or NWP coupling, offering limited state-adaptive and sample-specific controllability at deployment. To bridge this gap, we propose Agent-Guided Cross-modal Decoding (AGCD), a plug-and-play decoding-time prior-injection paradigm that derives state-conditioned physics-priors from the current multivariate atmosphere and injects them into forecasters in a controllable and reusable way. Specifically, We design a multi-agent meteorological narration pipeline to generate state-conditioned physics-priors, utilizing MLLMs to extract various meteorological elements effectively. To effectively apply the priors, AGCD further introduce cross-modal region interaction decoding that performs region-aware multi-scale tokenization and efficient physics-priors injection to refine visual features without changing the backbone interface. Experiments on WeatherBench demonstrate consistent gains for 6-hour forecasting across two resolutions (5.625 degree and 1.40625 degree) and diverse backbones (generic and weather-specialized), including strictly causal 48-hour autoregressive rollouts that reduce early-stage error accumulation and improve long-horizon stability.

</details>


### 149. Directional Embedding Smoothing for Robust Vision Language Models

- **Authors:** Ye Wang, Jing Liu, Toshiaki Koike-Akino
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15259v1](http://arxiv.org/abs/2603.15259v1)
- **PDF:** [https://arxiv.org/pdf/2603.15259v1](https://arxiv.org/pdf/2603.15259v1)
- **Categories:** cs.LG, cs.AI, cs.CL, cs.CR


> The paper introduces a lightweight, inference‑time defense—Directional Embedding Smoothing (an extension of Randomized Embedding Smoothing and Token Aggregation, RESTA)—designed to harden vision‑language models (VLMs) against jailbreak attacks that threaten the safety of agentic AI systems. By injecting noise that is aligned with the original token embeddings (directional noise) during inference, the method preserves semantic content while disrupting adversarial perturbations. Empirical evaluation on the JailBreakV‑28K benchmark shows that this directional RESTA variant significantly lowers attack success rates across a broad set of multimodal jailbreak prompts, demonstrating its practicality for securing VLMs within larger autonomous agents.


<details>
<summary>Abstract</summary>

The safety and reliability of vision-language models (VLMs) are a crucial part of deploying trustworthy agentic AI systems. However, VLMs remain vulnerable to jailbreaking attacks that undermine their safety alignment to yield harmful outputs. In this work, we extend the Randomized Embedding Smoothing and Token Aggregation (RESTA) defense to VLMs and evaluate its performance against the JailBreakV-28K benchmark of multi-modal jailbreaking attacks. We find that RESTA is effective in reducing attack success rate over this diverse corpus of attacks, in particular, when employing directional embedding noise, where the injected noise is aligned with the original token embedding vectors. Our results demonstrate that RESTA can contribute to securing VLMs within agentic systems, as a lightweight, inference-time defense layer of an overall security framework.

</details>


### 150. SEMAG: Self-Evolutionary Multi-Agent Code Generation

- **Authors:** Yulin Peng, Haowen Hou, Xinxin Zhu, Ying Tiffany He, F. Richard Yu
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15707v1](http://arxiv.org/abs/2603.15707v1)
- **PDF:** [https://arxiv.org/pdf/2603.15707v1](https://arxiv.org/pdf/2603.15707v1)
- **Categories:** cs.SE, cs.AI


> SEMAG introduces a self‑evolutionary multi‑agent framework that mirrors human software development by dynamically decomposing a coding problem into planning, implementation, debugging, and inter‑agent discussion stages, while continuously selecting and upgrading the underlying LLM backbone in real time. The methodology couples task‑aware workflow adaptation with an automated model‑selection loop that lets agents fetch the latest, most capable models without human intervention. Empirically, SEMAG achieves state‑of‑the‑art Pass@1 results—outperforming prior approaches by 3.3 % on CodeContests with a fixed backbone and reaching 52.6 % Pass@1 when leveraging its self‑evolutionary model selection, demonstrating both superior code generation performance and robust adaptability to evolving LLM capabilities.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have made significant progress in handling complex programming tasks. However, current methods rely on manual model selection and fixed workflows, which limit their ability to adapt to changing task complexities. To address this, we propose SEMAG, a Self-Evolutionary Multi-Agent code Generation framework that mimics human coding practices. It decomposes programming tasks into stages, including planning, coding, debugging, and discussion, while adapting workflows to task difficulty. Its self-evolutionary agents can access the latest models in real time and automatically upgrade the backbone model. SEMAG sets new state-of-the-art Pass@1 accuracy across benchmarks. Using identical backbone models, SEMAG outperforms prior methods by 3.3% on CodeContests. When augmented with self-evolutionary model selection that automatically identifies optimal backbones, SEMAG reaches 52.6%, showcasing both framework effectiveness and adaptability to evolving LLM capabilities.

</details>


### 151. SAGE: Multi-Agent Self-Evolution for LLM Reasoning

- **Authors:** Yulin Peng, Xinxin Zhu, Chenxing Wei, Nianbo Zeng, Leilei Wang, Ying Tiffany He, F. Richard Yu
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15255v2](http://arxiv.org/abs/2603.15255v2)
- **PDF:** [https://arxiv.org/pdf/2603.15255v2](https://arxiv.org/pdf/2603.15255v2)
- **Categories:** cs.AI, cs.MA


> The paper introduces **SAGE (Self‑evolving Agents for Generalized reasoning Evolution)**, a closed‑loop, multi‑agent framework that lets a single LLM backbone autonomously generate, plan, solve, and evaluate increasingly challenging reasoning tasks without large human‑annotated datasets. By co‑evolving four specialized agents—Challenger (task generator), Planner (structured plan creator), Solver (plan executor), and Critic (quality filter)—SAGE maintains a stable curriculum and high‑quality training signals through external verifiers, enabling self‑play with explicit planning and rigorous quality control. Experiments on mathematics and code‑generation benchmarks show that SAGE consistently improves performance across model sizes, yielding +8.9 % on LiveCodeBench and +10.7 % on OlympiadBench for the 7‑B Qwen‑2.5 model, demonstrating the efficacy of self‑evolving multi‑agent pipelines for agentic AI reasoning.


<details>
<summary>Abstract</summary>

Reinforcement learning with verifiable rewards improves reasoning in large language models (LLMs), but many methods still rely on large human-labeled datasets. While self-play reduces this dependency, it often lacks explicit planning and strong quality control, limiting stability in long-horizon multi-step reasoning. We present SAGE (Self-evolving Agents for Generalized reasoning Evolution), a closed-loop framework where four agents: Challenger, Planner, Solver, and Critic, co-evolve from a shared LLM backbone using only a small seed set. The Challenger continuously generates increasingly difficult tasks; the Planner converts each task into a structured multi-step plan; and the Solver follows the plan to produce an answer, whose correctness is determined by external verifiers. The Critic scores and filters both generated questions and plans to prevent curriculum drift and maintain training signal quality, enabling stable self-training. Across mathematics and code-generation benchmarks, SAGE delivers consistent gains across model scales, improving the Qwen-2.5-7B model by 8.9% on LiveCodeBench and 10.7% on OlympiadBench.

</details>


### 152. Token Coherence: Adapting MESI Cache Protocols to Minimize Synchronization Overhead in Multi-Agent LLM Systems

- **Authors:** Vladyslav Parakhin
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15183v1](http://arxiv.org/abs/2603.15183v1)
- **PDF:** [https://arxiv.org/pdf/2603.15183v1](https://arxiv.org/pdf/2603.15183v1)
- **Categories:** cs.DC, cs.AI, cs.LG, cs.MA


> The paper introduces **Artifact Coherence System (ACS)**, a formally‑verified protocol that adapts the MESI cache‑coherence mechanism to the synchronization of shared artifacts in multi‑agent LLM pipelines, thereby turning the naïve O(n × S × |D|) broadcast cost into O((n + W) × |D|). By mapping artifact states to MESI’s Modified/Exclusive/Shared/Invalid categories, the authors prove the **Token Coherence Theorem** (showing lazy invalidation saves at least S/(n + W(d_i)) tokens) and validate the design with TLA⁺ model checking of ~2,400 states, as well as Python simulations integrated with LangGraph, CrewAI, and AutoGen. Empirical results demonstrate 84‑95 % reduction in synchronization traffic across a range of contention levels, confirming that the protocol achieves bounded staleness and single‑writer safety while dramatically lowering coordination overhead in agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent LLM orchestration incurs synchronization costs scaling as O(n x S x |D|) in agents, steps, and artifact size under naive broadcast -- a regime I term broadcast-induced triply-multiplicative overhead. I argue this pathology is a structural residue of full-state rebroadcast, not an inherent property of multi-agent coordination.
  The central claim: synchronization cost explosion in LLM multi-agent systems maps with formal precision onto the cache coherence problem in shared-memory multiprocessors, and MESI-protocol invalidation transfers to artifact synchronization under minimal structural modification.
  I construct the Artifact Coherence System (ACS) and prove the Token Coherence Theorem: lazy invalidation attenuates cost by at least S/(n + W(d_i)) when S > n + W(d_i), converting O(n x S x |D|) to O((n + W) x |D|). A TLA+-verified protocol enforces single-writer safety, monotonic versioning, and bounded staleness across ~2,400 explored states.
  Simulation across four workload configurations yields token savings of 95.0% +/- 1.3% at V=0.05, 92.3% +/- 1.4% at V=0.10, 88.3% +/- 1.5% at V=0.25, and 84.2% +/- 1.3% at V=0.50 -- each exceeding the theorem's conservative lower bounds. Savings of ~81% persist at V=0.9, contrary to the predicted collapse threshold.
  Contributions: (1) formal MESI-to-artifact state mapping; (2) Token Coherence Theorem as savings lower bound; (3) TLA+-verified protocol with three proven invariants; (4) characterization of conditional artifact access semantics resolving the always-read objection; (5) reference Python implementation integrating with LangGraph, CrewAI, and AutoGen via thin adapter layers.

</details>


### 153. Open Biomedical Knowledge Graphs at Scale: Construction, Federation, and AI Agent Access with Samyama Graph Database

- **Authors:** Madhulatha Mandarapu, Sandeep Kunkunuru
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15080v3](http://arxiv.org/abs/2603.15080v3)
- **PDF:** [https://arxiv.org/pdf/2603.15080v3](https://arxiv.org/pdf/2603.15080v3)
- **Categories:** cs.DB, cs.AI, q-bio.QM


> The paper introduces Samyama, a high‑performance, Rust‑based graph database that enables the reproducible construction and federation of three large, open‑license biomedical knowledge graphs (Pathways, Clinical Trials, and Drug Interactions) totaling ~8 M nodes and 28 M edges. By providing a standardized ETL pipeline, cross‑source deduplication, and schema‑driven micro‑service (MCP) generation, the authors allow LLM‑based agents to query the federated graph via automatically generated Cypher APIs; on the new BiomedQA benchmark, these domain‑specific MCP tools achieve 98 % accuracy—substantially higher than schema‑aware text‑to‑Cypher (85 %) and vanilla GPT‑4o (75 %) and with zero schema errors. The work demonstrates that tightly integrated, schema‑aware graph back‑ends can dramatically improve the reliability and performance of agentic AI systems operating over complex biomedical data.


<details>
<summary>Abstract</summary>

Biomedical knowledge is fragmented across siloed databases -- Reactome for pathways, STRING for protein interactions, ClinicalTrials.gov for study registries, DrugBank for drug vocabularies, DGIdb for drug-gene interactions, SIDER for side effects. We present three open-source biomedical knowledge graphs -- Pathways KG (118,686 nodes, 834,785 edges from 5 sources), Clinical Trials KG (7,774,446 nodes, 26,973,997 edges from 5 sources), and Drug Interactions KG (32,726 nodes, 191,970 edges from 3 sources) -- built on Samyama, a high-performance graph database written in Rust.
  Our contributions are threefold. First, we describe a reproducible ETL pattern for constructing large-scale KGs from heterogeneous public data sources, with cross-source deduplication, batch loading (Python Cypher and Rust native loaders), and portable snapshot export. Second, we demonstrate cross-KG federation: loading all three snapshots into a single graph tenant enables property-based joins across datasets. Third, we introduce schema-driven MCP server generation for LLM agent access, evaluated on a new BiomedQA benchmark (40 pharmacology questions): domain-specific MCP tools achieve 98% accuracy vs. 85% for schema-aware text-to-Cypher and 75% for standalone GPT-4o, with zero schema errors.
  All data sources are open-license. The combined federated graph (7.9M nodes, 28M edges) loads in approximately 3 minutes on commodity cloud hardware, with single-KG queries completing in 80-100ms and cross-KG federation joins in 1-4s

</details>


### 154. Writer-R1: Enhancing Generative Writing in LLMs via Memory-augmented Replay Policy Optimization

- **Authors:** Jihao Zhao, Shuaishuai Zu, Zhiyuan Ji, Chunlai Zhou, Biao Qin
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15061v1](http://arxiv.org/abs/2603.15061v1)
- **PDF:** [https://arxiv.org/pdf/2603.15061v1](https://arxiv.org/pdf/2603.15061v1)
- **Categories:** cs.CL


> The paper introduces **Writer‑R1**, a framework that equips large language models with an agentic “self‑reflective” loop for creative writing. It first builds a multi‑agent workflow (grounded‑theory‑inspired) that automatically decomposes the writing task into fine‑grained, interpretable criteria, then applies **Memory‑augmented Replay Policy Optimization (MRPO)**—a hybrid supervised‑plus‑RL scheme that stores past criterion‑based feedback in memory and replays it as reward signals, enabling the model to iteratively improve without extra fine‑tuning. Experiments show that the automatically generated criteria yield reward‑level gains on par with human‑annotated feedback, and the 4 B‑parameter Writer‑R1 model surpasses strong baselines and even several 100 B‑parameter open‑source models on multiple creative‑writing benchmarks.


<details>
<summary>Abstract</summary>

As a typical open-ended generation task, creative writing lacks verifiable reference answers, which has long constrained reward modeling and automatic evaluation due to high human annotation costs, evaluative bias, and coarse feedback signals. To address these challenges, this paper first designs a multi-agent collaborative workflow based on Grounded Theory, performing dimensional decomposition and hierarchical induction of the problem to dynamically produce interpretable and reusable fine-grained criteria. Furthermore, we propose the Memory-augmented Replay Policy Optimization (MRPO) algorithm: on the one hand, without additional training, MRPO guides models to engage in self-reflection based on dynamic criteria, enabling controlled iterative improvement; on the other hand, we adopt the training paradigm that combines supervised fine-tuning with reinforcement learning to convert evaluation criteria into reward signals, achieving end-to-end optimization. Experimental results demonstrate that the automatically constructed criteria achieve performance gains comparable to human annotations. Writer-R1-4B models trained with this approach outperform baselines across multiple creative writing tasks and surpass some 100B+ parameter open-source models.

</details>


### 155. Interference-Aware K-Step Reachable Communication in Multi-Agent Reinforcement Learning

- **Authors:** Ziyu Cheng, Jinsheng Ren, Zhouxian Jiang, Chenzhihang Li, Rongye Shi, Bin Liang, Jun Yang
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15054v1](http://arxiv.org/abs/2603.15054v1)
- **PDF:** [https://arxiv.org/pdf/2603.15054v1](https://arxiv.org/pdf/2603.15054v1)
- **Categories:** cs.AI


> The paper introduces **Interference‑Aware K‑Step Reachable Communication (IA‑KRC)**, a MARL communication framework that lets agents dynamically select high‑utility partners while respecting limited bandwidth and environmental interference. IA‑KRC combines (i) a K‑step reachability protocol that restricts message passing to physically reachable neighbors and (ii) an interference‑prediction module that scores potential collaborators by jointly minimizing predicted communication interference and maximizing task utility; both components are learned end‑to‑end via a centralized‑training‑decentralized‑execution scheme. Empirical results on a suite of complex, dynamically changing topologies show that IA‑KRC consistently outperforms state‑of‑the‑art baselines, achieving higher task success rates, greater communication efficiency, and improved scalability and robustness to interference—demonstrating a significant step toward more reliable, agentic communication in multi‑agent systems.


<details>
<summary>Abstract</summary>

Effective communication is pivotal for addressing complex collaborative tasks in multi-agent reinforcement learning (MARL). Yet, limited communication bandwidth and dynamic, intricate environmental topologies present significant challenges in identifying high-value communication partners. Agents must consequently select collaborators under uncertainty, lacking a priori knowledge of which partners can deliver task-critical information. To this end, we propose Interference-Aware K-Step Reachable Communication (IA-KRC), a novel framework that enhances cooperation via two core components: (1) a K-Step reachability protocol that confines message passing to physically accessible neighbors, and (2) an interference-prediction module that optimizes partner choice by minimizing interference while maximizing utility. Compared to existing methods, IA-KRC enables substantially more persistent and efficient cooperation despite environmental interference. Comprehensive evaluations confirm that IA-KRC achieves superior performance compared to state-of-the-art baselines, while demonstrating enhanced robustness and scalability in complex topological and highly dynamic multi-agent scenarios.

</details>


### 156. VTC-Bench: Evaluating Agentic Multimodal Models via Compositional Visual Tool Chaining

- **Authors:** Xuanyu Zhu, Yuhao Dong, Rundong Wang, Yang Shi, Zhipeng Wu, Yinlun Peng, YiFan Zhang, Yihang Lou, Yuanxing Zhang, Ziwei Liu, Yan Bai, Yuan Zhou
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15030v2](http://arxiv.org/abs/2603.15030v2)
- **PDF:** [https://arxiv.org/pdf/2603.15030v2](https://arxiv.org/pdf/2603.15030v2)
- **Categories:** cs.AI


> The paper introduces **VTC‑Bench**, a new evaluation suite for multimodal LLMs that measures how well they can *plan, select, and chain* a broad set of 32 OpenCV‑based visual tools in long‑horizon, compositional tasks. By curating 680 problems across nine cognitive categories and providing ground‑truth execution trajectories, the authors benchmark 19 state‑of‑the‑art MLLMs, revealing that even the strongest model (Gemini‑3.0‑Pro) solves only about half of the tasks and that current agents fail to generalize to unseen operations and to compose multiple tools efficiently. These results highlight a critical gap in visual agentic capabilities and establish VTC‑Bench as a rigorous baseline for future research on generalized, tool‑using multimodal agents.


<details>
<summary>Abstract</summary>

Recent advancements extend Multimodal Large Language Models (MLLMs) beyond standard visual question answering to utilizing external tools for advanced visual tasks. Despite this progress, precisely executing and effectively composing diverse tools for complex tasks remain persistent bottleneck. Constrained by sparse tool-sets and simple tool-use trajectories, existing benchmarks fail to capture complex and diverse tool interactions, falling short in evaluating model performance under practical, real-world conditions. To bridge this gap, we introduce VisualToolChain-Bench(VTC-Bench), a comprehensive benchmark designed to evaluate tool-use proficiency in MLLMs. To align with realistic computer vision pipelines, our framework features 32 diverse OpenCV-based visual operations. This rich tool-set enables extensive combinations, allowing VTC-Bench to rigorously assess multi-tool composition and long-horizon, multi-step plan execution. For precise evaluation, we provide 680 curated problems structured across a nine-category cognitive hierarchy, each with ground-truth execution trajectories. Extensive experiments on 19 leading MLLMs reveal critical limitations in current models' visual agentic capabilities. Specifically, models struggle to adapt to diverse tool-sets and generalize to unseen operations, with the leading model Gemini-3.0-Pro only achieving 51% on our benchmark. Furthermore, multi-tool composition remains a persistent challenge. When facing complex tasks, models struggle to formulate efficient execution plans, relying heavily on a narrow, suboptimal subset of familiar functions rather than selecting the optimal tools. By identifying these fundamental challenges, VTC-Bench establishes a rigorous baseline to guide the development of more generalized visual agentic models.

</details>


### 157. Describing Agentic AI Systems with C4: Lessons from Industry Projects

- **Authors:** Andreas Rausch, Stefan Wittek
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15021v1](http://arxiv.org/abs/2603.15021v1)
- **PDF:** [https://arxiv.org/pdf/2603.15021v1](https://arxiv.org/pdf/2603.15021v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces **C4‑Agent**, a lightweight documentation framework that extends the C4 model with a domain‑specific vocabulary and a hierarchy of views for describing the architectural style of agentic AI systems—namely, collections of specialized agents that exchange artifacts, invoke external tools, and coordinate through recurring interaction patterns and quality gates. The authors derived the framework from a series of industry collaborations, iteratively refining a set of modeling primitives (agents, artifacts, tools, coordination patterns) and mapping them onto C4’s context‑container‑component‑code levels; they then validated the approach on several long‑lived production deployments. Empirical observations show that C4‑Agent enables clearer, more maintainable architecture documentation, improves traceability of agent interactions, and facilitates systematic evolution of complex agentic AI solutions compared with ad‑hoc code sketches or pipeline diagrams.


<details>
<summary>Abstract</summary>

Different domains foster different architectural styles -- and thus different documentation practices (e.g., state-based models for behavioral control vs. ER-style models for information structures). Agentic AI systems exhibit another characteristic style: specialized agents collaborate by exchanging artifacts, invoking external tools, and coordinating via recurring interaction patterns and quality gates. As these systems evolve into long-lived industrial solutions, documentation must capture these style-defining concerns rather than relying on ad-hoc code sketches or pipeline drawings. This paper reports industrial experience from joint projects and derives a documentation systematics tailored to this style. Concretely, we provide (i) a style-oriented modeling vocabulary and a small set of views for agents, artifacts, tools, and their coordination patterns, (ii) a hierarchical description technique aligned with C4 to structure these views across abstraction levels, and (iii) industrial examples with lessons learned that demonstrate how the approach yields transparent, maintainable architecture documentation supporting sustained evolution.

</details>


### 158. OrgForge: A Multi-Agent Simulation Framework for Verifiable Synthetic Corporate Corpora

- **Authors:** Jeffrey Flynt
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.14997v1](http://arxiv.org/abs/2603.14997v1)
- **PDF:** [https://arxiv.org/pdf/2603.14997v1](https://arxiv.org/pdf/2603.14997v1)
- **Categories:** cs.CL, cs.AI, cs.IR


> OrgForge introduces an open‑source, multi‑agent simulation platform that generates fully verifiable synthetic corporate corpora by separating deterministic event physics from LLM‑produced surface text. The framework uses a Python‑based SimEvent bus and actor‑local clocks to enforce a globally consistent timeline, while modular graph‑dynamic subsystems (stress propagation, temporal decay, and escalation routing) drive organizational behavior independently of any language model. Experiments show that OrgForge can produce coherent, cross‑artifact artifacts (Slack, JIRA, Confluence, Git, email) with provable causal chains and no timeline inconsistencies, providing a reliable benchmark for evaluating retrieval‑augmented generation pipelines in agentic AI research.


<details>
<summary>Abstract</summary>

Evaluating retrieval-augmented generation (RAG) pipelines requires corpora where ground truth is knowable, temporally structured, and cross-artifact properties that real-world datasets rarely provide cleanly. Existing resources such as the Enron corpus carry legal ambiguity, demographic skew, and no structured ground truth. Purely LLM-generated synthetic data solves the legal problem but introduces a subtler one: the generating model cannot be prevented from hallucinating facts that contradict themselves across documents.We present OrgForge, an open-source multi-agent simulation framework that enforces a strict physics-cognition boundary: a deterministic Python engine maintains a SimEvent ground truth bus; large language models generate only surface prose, constrained by validated proposals. An actor-local clock enforces causal timestamp correctness across all artifact types, eliminating the class of timeline inconsistencies that arise when timestamps are sampled independently per document. We formalize three graph-dynamic subsystems stress propagation via betweenness centrality, temporal edge-weight decay, and Dijkstra escalation routing that govern organizational behavior independently of any LLM. Running a configurable N-day simulation, OrgForge produces interleaved Slack threads, JIRA tickets, Confluence pages, Git pull requests, and emails, all traceable to a shared, immutable event log. We additionally describe a causal chain tracking subsystem that accumulates cross-artifact evidence graphs per incident, a hybrid reciprocal-rank-fusion recurrence detector for identifying repeated failure classes, and an inbound/outbound email engine that routes vendor alerts, customer complaints, and HR correspondence through gated causal chains with probabilistic drop simulation. OrgForge is available under the MIT license.

</details>


### 159. Beyond Benchmark Islands: Toward Representative Trustworthiness Evaluation for Agentic AI

- **Authors:** Jinhu Qi, Yifan Li, Minghao Zhao, Wentao Zhang, Zijian Zhang, Yaoman Li, Irwin King
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.14987v1](http://arxiv.org/abs/2603.14987v1)
- **PDF:** [https://arxiv.org/pdf/2603.14987v1](https://arxiv.org/pdf/2603.14987v1)
- **Categories:** cs.CL, cs.DB


> The paper introduces the **Holographic Agent Assessment Framework (HAAF)**, a principled evaluation paradigm that measures an agentic AI’s trustworthiness across a *representative* distribution of socio‑technical scenarios rather than isolated benchmark tasks. HAAF combines (i) static cognitive/policy analysis, (ii) interactive sandbox simulations, (iii) social‑ethical alignment checks, and (iv) a distribution‑aware sampling engine that jointly optimizes coverage and risk sensitivity—especially for rare, high‑impact tail events—organized within an iterative “Trustworthy Optimization Factory” of red‑team probing and blue‑team hardening. Experiments with a pilot implementation show that HAAF uncovers vulnerabilities missed by conventional benchmarks (e.g., tool‑misuse, jailbreaks, and ethical lapses) and yields a measurable reduction in failure rates, demonstrating a more realistic, deployment‑ready assessment of agentic AI trustworthiness.


<details>
<summary>Abstract</summary>

As agentic AI systems move beyond static question answering into open-ended, tool-augmented, and multi-step real-world workflows, their increased authority poses greater risks of system misuse and operational failures. However, current evaluation practices remain fragmented, measuring isolated capabilities such as coding, hallucination, jailbreak resistance, or tool use in narrowly defined settings. We argue that the central limitation is not merely insufficient coverage of evaluation dimensions, but the lack of a principled notion of representativeness: an agent's trustworthiness should be assessed over a representative socio-technical scenario distribution rather than a collection of disconnected benchmark instances. To this end, we propose the Holographic Agent Assessment Framework (HAAF), a systematic evaluation paradigm that characterizes agent trustworthiness over a scenario manifold spanning task types, tool interfaces, interaction dynamics, social contexts, and risk levels. The framework integrates four complementary components: (i) static cognitive and policy analysis, (ii) interactive sandbox simulation, (iii) social-ethical alignment assessment, and (iv) a distribution-aware representative sampling engine that jointly optimizes coverage and risk sensitivity -- particularly for rare but high-consequence tail risks that conventional benchmarks systematically overlook. These components are connected through an iterative Trustworthy Optimization Factory. Through cycles of red-team probing and blue-team hardening, this paradigm progressively narrows the vulnerabilities to meet deployment standards, shifting agent evaluation from benchmark islands toward representative, real-world trustworthiness. Code and data for the illustrative instantiation are available at https://github.com/TonyQJH/haaf-pilot.

</details>


### 160. Shopping Companion: A Memory-Augmented LLM Agent for Real-World E-Commerce Tasks

- **Authors:** Zijian Yu, Kejun Xiao, Huaipeng Zhao, Tao Luo, Xiaoyi Zeng
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.14864v1](http://arxiv.org/abs/2603.14864v1)
- **PDF:** [https://arxiv.org/pdf/2603.14864v1](https://arxiv.org/pdf/2603.14864v1)
- **Categories:** cs.CL


> The paper introduces **Shopping Companion**, a unified, memory‑augmented LLM agent that simultaneously learns to retrieve long‑term user preferences and to perform e‑commerce assistance (recommendations, budgeting, bundling) within a single end‑to‑end framework. To evaluate this capability, the authors create a large‑scale benchmark covering two multi‑turn shopping tasks over 1.2 M real products, and train the agent with a **dual‑reward reinforcement‑learning** scheme that assigns tool‑specific rewards to cope with sparse, discontinuous feedback. Experiments show that even top‑tier models (e.g., GPT‑5) fall below 70 % success on the benchmark, while the lightweight LLM fine‑tuned via Shopping Companion consistently outperforms strong baselines, demonstrating superior preference capture and overall task performance in long‑term, preference‑aware shopping scenarios.


<details>
<summary>Abstract</summary>

In e-commerce, LLM agents show promise for shopping tasks such as recommendations, budgeting, and bundle deals, where accurately capturing user preferences from long-term conversations is critical. However, two challenges hinder realizing this potential: (1) the absence of benchmarks for evaluating long-term preference-aware shopping tasks, and (2) the lack of end-to-end optimization due to existing designs that treat preference identification and shopping assistance as separate components. In this paper, we introduce a novel benchmark with a long-term memory setup, spanning two shopping tasks over 1.2 million real-world products, and propose Shopping Companion, a unified framework that jointly tackles memory retrieval and shopping assistance while supporting user intervention. To train such capabilities, we develop a dual-reward reinforcement learning strategy with tool-wise rewards to handle the sparse and discontinuous rewards inherent in multi-turn interactions. Experimental results demonstrate that even state-of-the-art models (such as GPT-5) achieve success rates under 70% on our benchmark, highlighting the significant challenges in this domain. Notably, our lightweight LLM, trained with Shopping Companion, consistently outperforms strong baselines, achieving better preference capture and task performance, which validates the effectiveness of our unified design.

</details>


### 161. Knowledge Activation: AI Skills as the Institutional Knowledge Primitive for Agentic Software Development

- **Authors:** Gal Bakal
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.14805v1](http://arxiv.org/abs/2603.14805v1)
- **PDF:** [https://arxiv.org/pdf/2603.14805v1](https://arxiv.org/pdf/2603.14805v1)
- **Categories:** cs.AI, cs.HC, cs.SE


> The paper’s main contribution is the **Knowledge Activation** framework, which turns enterprise‑level institutional knowledge into **Atomic Knowledge Units (AKUs)**—standardized, governance‑aware primitives that an autonomous AI agent can consume directly as executable specifications rather than as raw documents. The authors design a schema and runtime architecture that organizes AKUs into a composable knowledge graph, and they validate the approach through prototype deployments that show faster onboarding, fewer cross‑team “correction cascades,” and measurable reductions in senior‑engineer effort. Their findings demonstrate that structuring knowledge for agentic consumption can yield performance gains that outweigh pure model‑size improvements, positioning AKU‑based knowledge activation as a critical architectural layer for scalable agentic software development.


<details>
<summary>Abstract</summary>

Enterprise software organizations accumulate critical institutional knowledge - architectural decisions, deployment procedures, compliance policies, incident playbooks - yet this knowledge remains trapped in formats designed for human interpretation. The bottleneck to effective agentic software development is not model capability but knowledge architecture. When any knowledge consumer - an autonomous AI agent, a newly onboarded engineer, or a senior developer - encounters an enterprise task without institutional context, the result is guesswork, correction cascades, and a disproportionate tax on senior engineers who must manually supply what others cannot infer.
  This paper introduces Knowledge Activation, a framework that specializes AI Skills - the open standard for agent-consumable knowledge - into structured, governance-aware Atomic Knowledge Units (AKUs) for institutional knowledge delivery. Rather than retrieving documents for interpretation, AKUs deliver action - ready specifications encoding what to do, which tools to use, what constraints to respect, and where to go next - so that agents act correctly and engineers receive institutionally grounded guidance without reconstructing organizational context from scratch.
  AKUs form a composable knowledge graph that agents traverse at runtime - compressing onboarding, reducing cross - team friction, and eliminating correction cascades. The paper formalizes the resource constraints that make this architecture necessary, specifies the AKU schema and deployment architecture, and grounds long - term maintenance in knowledge commons practice. Organizations that architect their institutional knowledge for the agentic era will outperform those that invest solely in model capability.

</details>


### 162. OpenHospital: A Thing-in-itself Arena for Evolving and Benchmarking LLM-based Collective Intelligence

- **Authors:** Peigen Liu, Rui Ding, Yuren Mao, Ziyan Jiang, Yuxiang Ye, Yunjun Gao, Ying Zhang, Renjie Sun, Longbin Lai, Zhengping Qian
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.14771v2](http://arxiv.org/abs/2603.14771v2)
- **PDF:** [https://arxiv.org/pdf/2603.14771v2](https://arxiv.org/pdf/2603.14771v2)
- **Categories:** cs.AI


> The paper presents **OpenHospital**, a dedicated simulation arena that enables the evolution and benchmarking of collective intelligence (CI) among Large Language Model (LLM) agents in a medical setting. By embedding data directly within physician and patient agents (“data‑in‑agent‑self” paradigm), the authors let physician agents iteratively improve their medical reasoning through interactive dialogues with patient agents, while simultaneously collecting fine‑grained metrics of diagnostic accuracy, treatment planning, and computational efficiency. Empirical results show that agents trained in OpenHospital achieve significantly higher clinical performance and faster convergence than baseline LLM agents, demonstrating the platform’s utility for both fostering emergent CI and providing a standardized benchmark for agentic AI systems.


<details>
<summary>Abstract</summary>

Large Language Model (LLM)-based Collective Intelligence (CI) presents a promising approach to overcoming the data wall and continuously boosting the capabilities of LLM agents. However, there is currently no dedicated arena for evolving and benchmarking LLM-based CI. To address this gap, we introduce OpenHospital, an interactive arena where physician agents can evolve CI through interactions with patient agents. This arena employs a data-in-agent-self paradigm that rapidly enhances agent capabilities and provides robust evaluation metrics for benchmarking both medical proficiency and system efficiency. Experiments demonstrate the effectiveness of OpenHospital in both fostering and quantifying CI.

</details>


### 163. Loosely-Structured Software: Engineering Context, Structure, and Evolution Entropy in Runtime-Rewired Multi-Agent Systems

- **Authors:** Weihao Zhang, Yitong Zhou, Huanyu Qu, Hongyi Li
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.15690v1](http://arxiv.org/abs/2603.15690v1)
- **PDF:** [https://arxiv.org/pdf/2603.15690v1](https://arxiv.org/pdf/2603.15690v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces **Loosely‑Structured Software (LSS)**, a new engineering paradigm for LLM‑driven multi‑agent systems that treats runtime generation, semantic self‑organization, and endogenous code evolution as first‑class design concerns rather than bugs to be patched.  The authors formalize a three‑layer framework—**View/Context Engineering**, **Structure Engineering**, and **Evolution Engineering**—and instantiate it with a set of “semantic control block” design patterns that dynamically bind agents and artifacts while constraining the entropy produced by free‑form, inference‑mediated interactions.  Empirical prototypes show that LSS‑based systems achieve higher designability, scalability, and evolvability than baseline prompt‑tuned MAS, reducing coordination errors and drift as the number of agents grows.


<details>
<summary>Abstract</summary>

As LLM-based multi-agent systems (MAS) become more autonomous, their free-form interactions increasingly dominate system behavior. However, scaling the number of agents often amplifies context pressure, coordination errors, and system drift. It is well known that building robust MAS requires more than prompt tuning or increased model intelligence. It necessitates engineering discipline focused on architecture to manage complexity under uncertainty. We characterize agentic software by a core property: \emph{runtime generation and evolution under uncertainty}. Drawing upon and extending software engineering experience, especially object-oriented programming, this paper introduces \emph{Loosely-Structured Software (LSS)}, a new class of software systems that shifts the engineering focus from constructing deterministic logic to managing the runtime entropy generated by View-constructed programming, semantic-driven self-organization, and endogenous evolution.
  To make this entropy governable, we introduce design principles under a three-layer engineering framework: \emph{View/Context Engineering} to manage the execution environment and maintain task-relevant Views, \emph{Structure Engineering} to organize dynamic binding over artifacts and agents, and \emph{Evolution Engineering} to govern the lifecycle of self-rewriting artifacts. Building on this framework, we develop LSS design patterns as semantic control blocks that stabilize fluid, inference-mediated interactions while preserving agent adaptability. Together, these abstractions improve the \emph{designability}, \emph{scalability}, and \emph{evolvability} of agentic infrastructure. We provide basic experimental validation of key mechanisms, demonstrating the effectiveness of LSS.

</details>


### 164. GNNVerifier: Graph-based Verifier for LLM Task Planning

- **Authors:** Yu Hao, Qiuyu Wang, Cheng Yang, Yawen Li, Zhiqiang Zhang, Chuan Shi
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.14730v2](http://arxiv.org/abs/2603.14730v2)
- **PDF:** [https://arxiv.org/pdf/2603.14730v2](https://arxiv.org/pdf/2603.14730v2)
- **Categories:** cs.LG


> The paper introduces **GNNVerifier**, a graph‑neural‑network based module that evaluates and repairs LLM‑generated task plans without relying on another LLM as a verifier. By encoding a plan as a directed graph whose nodes are sub‑tasks and edges capture ordering and dependency constraints, the GNN produces a global plausibility score together with fine‑grained risk scores for individual nodes/edges; training data are automatically synthesized through controllable perturbations of ground‑truth plan graphs. Experiments on multiple planning benchmarks and backbone LLMs show that GNNVerifier markedly improves plan correctness—detecting structural errors (type mismatches, missing intermediates, broken dependencies) that LLM‑only verifiers miss—and enables targeted plan edits that raise overall task‑completion success rates.


<details>
<summary>Abstract</summary>

Large language models (LLMs) facilitate the development of autonomous agents. As a core component of such agents, task planning aims to decompose complex natural language requests into concrete, solvable sub-tasks. Since LLM-generated plans are frequently prone to hallucinations and sensitive to long-context prom-pts, recent research has introduced plan verifiers to identify and correct potential flaws. However, most existing approaches still rely on an LLM as the verifier via additional prompting for plan review or self-reflection. LLM-based verifiers can be misled by plausible narration and struggle to detect failures caused by structural relations across steps, such as type mismatches, missing intermediates, or broken dependencies. To address these limitations, we propose a graph-based verifier for LLM task planning. Specifically, the proposed method has four major components: Firstly, we represent a plan as a directed graph with enriched attributes, where nodes denote sub-tasks and edges encode execution order and dependency constraints. Secondly, a graph neural network (GNN) then performs structural evaluation and diagnosis, producing a graph-level plausibility score for plan acceptance as well as node/edge-level risk scores to localize erroneous regions. Thirdly, we construct controllable perturbations from ground truth plan graphs, and automatically generate training data with fine-grained annotations. Finally, guided by the feedback from our GNN verifier, we enable an LLM to conduct local edits (e.g., tool replacement or insertion) to correct the plan when the graph-level score is insufficient. Extensive experiments across diverse datasets, backbone LLMs, and planners demonstrate that our GNNVerifier achieves significant gains in improving plan quality. Our data and code is available at https://github.com/BUPT-GAMMA/GNNVerifier.

</details>


### 165. Beyond Local Code Optimization: Multi-Agent Reasoning for Software System Optimization

- **Authors:** Huiyun Peng, Parth Vinod Patil, Antonio Zhong Qiu, George K. Thiruvathukal, James C. Davis
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.14703v1](http://arxiv.org/abs/2603.14703v1)
- **PDF:** [https://arxiv.org/pdf/2603.14703v1](https://arxiv.org/pdf/2603.14703v1)
- **Categories:** cs.SE, cs.AI


> The paper’s main contribution is a multi‑agent framework that extends AI‑driven code optimization from isolated, syntax‑level edits to whole‑system performance reasoning for microservice architectures. It does so by assigning coordinated roles—summarizer, analyzer, optimizer, and verifier—to agents that jointly ingest control‑flow, data‑flow, and cross‑component dependency information, enabling them to detect system‑wide bottlenecks and synthesize multi‑step, cross‑stack optimization plans. In a proof‑of‑concept microservice benchmark, the framework achieved a 36.58 % throughput increase and a 27.81 % reduction in average response time, demonstrating the practical impact of agentic, system‑level reasoning for software optimization.


<details>
<summary>Abstract</summary>

Large language models and AI agents have recently shown promise in automating software performance optimization, but existing approaches predominantly rely on local, syntax-driven code transformations. This limits their ability to reason about program behavior and capture whole system performance interactions. As modern software increasingly comprises interacting components - such as microservices, databases, and shared infrastructure - effective code optimization requires reasoning about program structure and system architecture beyond individual functions or files.
  This paper explores the feasibility of whole system optimization for microservices. We introduce a multi-agent framework that integrates control-flow and data-flow representations with architectural and cross-component dependency signals to support system-level performance reasoning. The proposed system is decomposed into coordinated agent roles - summarization, analysis, optimization, and verification - that collaboratively identify cross-cutting bottlenecks and construct multi-step optimization strategies spanning the software stack. We present a proof-of-concept on a microservice-based system that illustrates the effectiveness of our proposed framework, achieving a 36.58% improvement in throughput and a 27.81% reduction in average response time.

</details>


### 166. AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems

- **Authors:** Zhaohui Geoffrey Wang
- **Published:** 2026-03-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2603.14688v1](http://arxiv.org/abs/2603.14688v1)
- **PDF:** [https://arxiv.org/pdf/2603.14688v1](https://arxiv.org/pdf/2603.14688v1)
- **Categories:** cs.LG, cs.AI, cs.SE


> AgentTrace introduces a lightweight, post‑hoc causal‑graph tracing framework that automatically reconstructs the dependency structure of deployed multi‑agent workflows from their execution logs and back‑propagates from observed errors to rank likely root causes, all without invoking LLM inference at debug time. The system builds a directed causal graph, applies interpretable structural (e.g., node degree, edge betweenness) and positional (e.g., temporal distance to the failure) signals to score candidates, and returns a ranked list of probable origins. Empirical evaluation on a benchmark of realistic multi‑agent failure scenarios shows that AgentTrace localizes the true root cause with significantly higher accuracy and sub‑second latency than both heuristic baselines and LLM‑based debugging approaches, demonstrating a practical, scalable tool for improving reliability and trustworthiness of agentic AI systems in production.


<details>
<summary>Abstract</summary>

As multi-agent AI systems are increasingly deployed in real-world settings - from automated customer support to DevOps remediation - failures become harder to diagnose due to cascading effects, hidden dependencies, and long execution traces. We present AgentTrace, a lightweight causal tracing framework for post-hoc failure diagnosis in deployed multi-agent workflows. AgentTrace reconstructs causal graphs from execution logs, traces backward from error manifestations, and ranks candidate root causes using interpretable structural and positional signals - without requiring LLM inference at debugging time. Across a diverse benchmark of multi-agent failure scenarios designed to reflect common deployment patterns, AgentTrace localizes root causes with high accuracy and sub-second latency, significantly outperforming both heuristic and LLM-based baselines. Our results suggest that causal tracing provides a practical foundation for improving the reliability and trustworthiness of agentic systems in the wild.

</details>



## Medrxiv (5 papers)


### 1. From Concept to Clinic: Real World Evidence for Autonomous AI Deployment in Primary Care Telemedicine

- **Authors:** Saenz, A. D., Schumacher, E., Naik, D., Khosla, N., Kannan, A.
- **Published:** 2026-03-20
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.18.26348749](https://doi.org/10.64898/2026.03.18.26348749)

- **Categories:** health informatics


> The paper presents the first large‑scale, clinician‑blinded, real‑world evaluation of a multi‑agent LLM system embedded in a nationwide primary‑care telemedicine platform, demonstrating that purposeful system architecture and safety gating—not just model size—enable safe autonomous clinical decision‑making. Using 2,379 completed patient encounters, the authors compared the AI’s intake diagnoses and disposition recommendations to those of treating physicians, finding a top‑1 diagnostic match of 91.3 % overall (96.3 % for cases above a confidence safety threshold) and a disposition error rate of only 2.5 %, with zero critical errors. These results support a staged, task‑calibrated deployment framework for autonomous AI in health care, providing concrete real‑world evidence that agentic AI can be reliably deployed for well‑defined, low‑complexity clinical tasks.


<details>
<summary>Abstract</summary>

Systems powered by large language models are widely used for health information and advice, yet robust evidence for their safety and effectiveness in real-world clinical care remains lacking. Most existing studies evaluate general-purpose chatbots in artificial settings, failing to account for the critical role of system design, deployment context, and integrated safety mechanisms. Here, we report, to our knowledge, the first large-scale, clinician-blinded, real-world evaluation of a multi-agent LLM-based system deployed within a nationwide U.S. primary care telemedicine platform, assessing readiness for task-specific autonomous deployment. In 2,379 real patient encounters, where users actively sought medical care and completed full visits with licensed clinicians, we compared the AI system's intake diagnoses and disposition suggestions to those of treating clinicians, who were blinded to the AI's outputs. The AI's top-1 diagnosis matched the clinician's diagnosis in 91.3% of cases overall, increasing to 96.3% among cases meeting a pre-specified safety confidence threshold, and 97.9% in common, lower-complexity conditions that met the same confidence threshold. Disposition accuracy was similarly high, with an overall error rate of 2.5% and no errors in suggestions to emergency room or home management. These results demonstrate that purposeful system architecture, rather than model capability alone, is essential for safe and effective autonomous clinical AI. We propose a staged, task-calibrated deployment framework, in which AI can be introduced autonomously for well-defined tasks with explicit safety gating and continuous monitoring, expanding scope as real-world evidence accrues. Our findings provide the first real-world evidence of readiness for safe autonomous clinical AI and offer a practical roadmap for its responsible deployment at scale.

</details>


### 2. CLINPREAI: AN AGENTIC AI SYSTEM FOR EARLY POSTPARTUM DEPRESSION RISK PREDICTION FROM MULTIMODAL EHR DATA

- **Authors:** Palacios, D., Aras, S., Zhong, Y., Zhao, J., Pasupuleti, S., Jeong, H.-H., Miller, E., Fletcher, T., Goulding, A., Chen, H., Liu, Z.
- **Published:** 2026-03-18
- **Source:** medrxiv
- **URL:** [https://doi.org/10.1101/2025.11.14.25340265](https://doi.org/10.1101/2025.11.14.25340265)

- **Categories:** health informatics


> The paper introduces **ClinPreAI**, the first agentic AI platform that autonomously designs, trains, and evaluates predictive models for early postpartum‑depression risk using multimodal electronic health record (EHR) data. Leveraging five specialized modules that iteratively conduct feature engineering, model selection, hyper‑parameter tuning, and debugging, ClinPreAI processes 27 structured clinical variables and unstructured social‑worker notes from 4,161 pregnant patients and outputs a binary EPDS ≥ 10 outcome. Across both structured‑only and multimodal settings, the system attains F1 scores of 0.68 ± 0.03 and 0.65 ± 0.04 respectively—outperforming conventional AutoML pipelines and commercial tools and matching custom LLM‑augmented baselines—demonstrating that autonomous AI agents can reliably generate high‑performing, interpretable clinical risk models without requiring domain experts to have machine‑learning expertise.


<details>
<summary>Abstract</summary>

AO_SCPLOWBSTRACTC_SCPLOWPostpartum depression (PPD) affects 10-15% of individuals annually, yet early identification and treatment remains challenging. We introduce ClinPreAI, a novel agentic AI system that autonomously designs, implements, and evaluates machine learning solutions for PPD risk prediction using multimodal electronic health record data. We analyzed data from 4,161 pregnant individuals hospitalized prior to delivery for medical or obstetrical complications at Texas Childrens Hospital (2012-2025), extracting 27 structured clinical variables and social worker notes. The primary outcome was Edinburgh Postnatal Depression Scale (EPDS) score [&ge;]10 (31.0% prevalence) within 6 months after delivery, indicating clinically significant depressive symptoms. ClinPreAI operates through five specialized modules that iteratively refine predictive models through autonomous experimentation. ClinPreAI demonstrated strong performance across modalities. On structured data, it achieved F1: 0.68 {+/-} 0.03, outperforming traditional AutoML (F1: 0.64 {+/-} 0.02) and commercial solutions (AWS Canvas F1: 0.54-0.55). On multimodal data, ClinPreAI achieved F1: 0.65 {+/-} 0.04, matching custom LLM-XGBoost (F1: 0.65 {+/-} 0.01) and outperforming zero-shot models (Claude Opus F1: 0.51-0.52). This represents the first application of agentic AI to perinatal mental health prediction. Our results demonstrate that autonomous AI agents can democratize sophisticated predictive modeling in clinical settings, which is particularly valuable where domain experts lack ML training. By automating experimentation and debugging, agentic systems lower barriers to developing robust clinical prediction tools while maintaining interpretability.

</details>


### 3. ADDRESSING THE ROLE OF OCCUPATIONAL EXPOSOME ON PARKINSON'S DISEASE AND PARKINSONISM IN A MATCHED CASE-CONTROL STUDY

- **Authors:** Lewis, F., Renzetti, S., Goulett, N., Azmoun, S., Sundar, V., Ali, M., Pitta, L., Shoieb, D., Caci, M., Borghesi, S., Covolo, L., Oppini, M., Gelatti, U., Padovani, A., Pilotto, A., Pepe, F., Turla, M., Crippa, P., Pani, L., Vermeulen, R., Kromhout, H., Lambertini, L., Colicino, E., Placidi, D., Lucchini, R.
- **Published:** 2026-03-18
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.16.26348171](https://doi.org/10.64898/2026.03.16.26348171)

- **Categories:** occupational and environmental health


> The paper’s main contribution is a comprehensive assessment of how cumulative occupational exposures—particularly to pesticides and metals—affect the risk of Parkinson’s disease (PD) and Parkinsonism, using the ALOHA+ Job‑Exposure Matrix to quantify lifelong exposure burdens. By conducting a hospital‑based matched case‑control study (334 cases and 334 controls) and applying conditional logistic regression together with positively constrained repeated‑holdout Weighted Quantile Sum (WQS) regression, the authors demonstrate that high cumulative pesticide exposure triples the odds of PD (OR ≈ 3.5) and that a composite exposure index (dominated by pesticides and metals) is significantly associated with disease risk. Although the findings advance epidemiological understanding of neurotoxic occupational hazards, they have limited direct relevance to agentic AI research, aside from illustrating how multi‑agent exposure modeling techniques (e


<details>
<summary>Abstract</summary>

Background/ObjectivesOccupational exposure to neurotoxicants such as pesticides, metals, and solvents has long been implicated in Parkinsons disease (PD) and Parkinsonism, yet the cumulative impact of multiple occupational exposure families over the working life remains insufficiently characterized. This study evaluated whether long-term cumulative occupational exposures, derived from the ALOHA+ Job-Exposure Matrix (ALOHA+-JEM), were associated with PD and Parkinsonism.

MethodsA hospital-based matched case-control study was conducted in the province of Brescia, Italy, including 668 participants (334 PD/Parkinsonism cases and 334 matched controls). Cases and controls were 1:1 matched based on sex, age, and lifetime occupational duration. Lifetime occupational histories were coded using ISCO-08 and harmonized to ISCO-88 for linkage with ALOHA+-JEM. Conditional logistic regression estimated associations between cumulative exposures (none/low/high) and disease status, adjusting for smoking, parental history of PD/tremor, and SNCA rs356219 genotype. Multi-agent occupational exposure burden indexes were evaluated using positively constrained repeated-holdout Weighted Quantile Sum (WQS) regression (100 bootstraps, 100 holdouts)

ResultsIn conditional logistic regression, parental history of PD or tremor (OR = 4.55, 95% CI: 2.44-8.48; q < 0.001) and the SNCA rs356219 CC genotype (OR = 2.17, 95% CI: 1.33-3.52; q = 0.013) were significantly associated with disease. High cumulative all pesticide exposure showed positive associations with combined PD + Parkinsonism (OR = 2.98, 95% CI: 1.23-7.25) and PD alone (OR = 3.56, 95% CI: 1.25-10.15). In WQS analyses, the composite occupational exposure burden index was positively associated with disease (combined PD + Parkinsonism: OR = 1.15, 95% CI: 1.00-1.30). All pesticides received the highest mean weight in all models (w = 0.434 for combined PD + Parkinsonism), followed by metals (w = 0.210), identifying them as contributing most strongly to the composite exposure index.

ConclusionsLong-term cumulative occupational exposures were associated with increased odds of PD and Parkinsonism. All pesticides and metals were most strongly associated with PD and Parkinsonism, consistent with established neurotoxic mechanisms attributable to occupational environments. These findings underscore the importance of occupational exposure prevention and risk-reduction strategies in occupational settings and highlight workplace exposures as preventable contributors to Parkinsonian disorders.

</details>


### 4. OpenScientist: evaluating an open agentic AI co-scientist to accelerate biomedical discovery

- **Authors:** Roberts, K. F., Abrams, Z. B., Cappelletti, L., Moqri, M., Heugel, N., Caufield, J. H., Bourdenx, M., Li, Y., Banerjee, J., Foschini, L., Galeano, D., Harris, N. L., Li, M., Ying, K., Melendez, J. A., Barthelemy, N. R., Bollinger, J. G., He, Y., Ovod, V., Benzinger, T. L. S., Flores, S., Gordon, B., Ojewole, A. A., Phatak, M., Elbert, D. L., Biber, S., Landsness, E. C., Mungall, C. J., Bateman, R. J., Reese, J.
- **Published:** 2026-03-18
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.15.26348338](https://doi.org/10.64898/2026.03.15.26348338)

- **Categories:** health informatics


> OpenScientist is an open‑source, auditable agentic AI system that acts as a semi‑autonomous co‑scientist, taking researcher‑defined biomedical questions, retrieving relevant data, performing statistical and machine‑learning analyses, and synthesizing the results into testable scientific insights. The authors evaluated the platform across four real‑world clinical case studies—Alzheimer’s biomarker prediction, plasma‑proteomic survival modeling, single‑cell transcriptomics of tau pathology, and hypothesis generation in multiple myeloma—by having domain experts compare the AI‑produced outputs with established findings and randomized controls. In each case OpenScientist completed analyses in minutes (instead of weeks‑months), correctly identified %ptau217 as the top amyloid PET predictor, matched published survival‑model performance, uncovered a plausible tau‑lysosome mechanism, and generated multiple‑myeloma hypotheses that were externally validated, demonstrating that open, reproducible agentic AI can reliably accelerate hypothesis generation and data‑driven discovery in biomedical research.


<details>
<summary>Abstract</summary>

BackgroundAdvances in medicine depend on analyzing large and complex data sources, but discovery is partly constrained by the limited time and domain expertise of human researchers. Agentic artificial intelligence (agentic AI) can accelerate discovery by automating components of the scientific workflow, including information retrieval, data analysis, and knowledge synthesis.

AimOpenScientist, an open-source agentic AI co-scientist, aims to accelerate biomedical discovery by semi-autonomously investigating scientist-defined queries and generating clinically relevant, verifiable scientific insights.

MethodsDomain experts evaluated OpenScientist for novel discoveries in four clinical case studies: (1) a prespecified analysis in a community-based Alzheimers disease biomarker cohort, (2) unsupervised modeling for plasma proteomic survival prediction, (3) hypothesis investigation in single-cell transcriptomic data from neurons with neurofibrillary tangles, and (4) hypothesis generation with validation in a multiple myeloma dataset with a randomized negative control.

ResultsOpenScientist completed analyses in minutes that otherwise would take weeks to months of human time and expertise. It identified %ptau217 as the best predictor of amyloid PET status, generated a plasma proteomic survival model with performance comparable to published models, proposed a mechanism linking tau pathology to altered lysosomal acidification, and generated multiple myeloma hypotheses that were validated in an external cohort while distinguishing true signal from randomized controls.

ConclusionOpenScientist demonstrates that open, auditable, agentic AI can support real-world clinical research by generating hypotheses, executing analyses, and discovering insights from complex datasets.

</details>


### 5. CoNVict: An Agentic AI System for Copy Number Variation Prioritization in Rare Disease Diagnosis

- **Authors:** Gencturk, M. M., Kara, M., Ozden, F.
- **Published:** 2026-03-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.16.26348493](https://doi.org/10.64898/2026.03.16.26348493)

- **Categories:** genetic and genomic medicine


> CoNVict introduces a novel agentic AI framework that leverages large‑language‑model (LLM) reasoning to prioritize copy‑number variants (CNVs) in rare‑disease diagnostics. The system combines a two‑stage pipeline—first a verdict classifier that triages candidate CNVs, then a tournament‑style pairwise ranking that performs structured, in‑context evidence integration guided by the patient’s phenotype—and operates without disease‑specific retraining. Benchmarked on simulated multi‑specialty cases, CoNVict markedly outperforms existing CNV‑annotation tools in correctly identifying causal variants, while also maintaining strong performance on variants of uncertain significance and non‑coding CNVs, demonstrating the utility of agentic AI for patient‑specific genomic interpretation.


<details>
<summary>Abstract</summary>

Copy number variants (CNVs) are established contributors to rare genetic disorders, yet their clinical interpretation remains challenging in diagnostic genomics. Large CNVs frequently encompass multiple functional regions whose clinical significance can only be resolved in the context of the patients phenotype. Effective prioritization demands variant-level scoring of dosage sensitivity, structural consequences, and disease associations, and systematic comparison of candidates within the same clinical context. Current computational tools only partially address these requirements: they automate variant-level scoring but leave phenotype-guided evidence integration and cross-variant ranking to the clinician, creating a gap between annotation throughput and diagnostic decision-making. Agentic AI systems coordinate large language model-driven reasoning across structured multi-step pipelines and have shown strong performance on biomedical tasks requiring iterative evidence evaluation and contextual judgement, making them well suited to patient-specific variant interpretation where rigid scoring functions fall short. Here, we present CoNVict, a two-stage agentic AI system for patient-specific CNV prioritization. The system ranks CNVs through verdict classification that triages candidates and tournament ranking that performs pairwise comparisons via structured, in-context reasoning. Evaluated on simulated diagnostic cases spanning multiple clinical subspecialties, CoNVict substantially outperforms existing computational methods in identifying the causal CNV and maintains robust performance on variants of uncertain significance and non-coding variants without retraining. Our results demonstrate that agentic AI can bridge the gap between automated variant-level annotation and the patient-specific clinical reasoning required for CNV-driven genetic diagnosis. Availability and Implementation: Source code and data are available at https://github.com/Muti-Kara/CoNVict.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*