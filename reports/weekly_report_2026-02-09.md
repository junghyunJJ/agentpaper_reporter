# Weekly AI Agent Paper Report

**Generated:** 2026-02-09 15:52
**Period:** 2026-02-02 to 2026-02-08

## Summary

- **Total papers fetched:** 1070
- **Papers matching keywords:** 167
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-02-02) | Change |
|--------|-----------|-----------|--------|
| Total matched | 167 | 23 | +144 |
| arxiv | 162 | 21 | +141 |
| biorxiv | 1 | 1 | +0 |
| medrxiv | 4 | 1 | +3 |

### Notable Trends

1. **Significant Surge in Paper Volume**: This week's count of 167 AI agent papers marks a dramatic increase from only 23 papers the previous week, indicating a potential surge in interest or ongoing research activity in the field.

2. **Diverse Applications and Themes**: The current week's top papers showcase a broad range of applications, from automated debugging and causal inference in epidemiology to hospital course summarization, emphasizing the growing diversity of AI agent systems in practical environments. In contrast, the previous week's papers were more focused on foundational and theoretical aspects of AI governance and cooperative agent exploration.

3. **Strong Focus on Practical Implementations**: There is a noticeable shift towards practical implementations (e.g., hospital course summarizer, diagnostic studies in surgery) in this week's papers, highlighting an increasing trend toward applying AI agents in real-world scenarios, as opposed to primarily theoretical discussions present in last week's selections.

4. **Emerging Interdisciplinary Connections**: This week’s titles reflect interdisciplinary approaches, integrating insights from fields like epidemiology and software engineering, suggesting a trend toward cross-domain applications of AI agents that was less pronounced in the previous week's collection.

5. **Increased Complexity in Topics**: The current week's papers delve into complex concepts such as agentic uncertainty, Nash equilibria, and multi-agent frameworks, indicating an elevation in the complexity of research topics being explored as the field matures. This complexity contrasts with the more foundational topics seen in the previous week.

---



## Biomedical Highlights (5 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


The reviewed biomedical papers illustrate the diverse applications of AI agents, focusing on improving healthcare outcomes and enhancing research methodologies. The first paper explores the use of high-definition transcranial direct current stimulation (HD-tDCS) in optimizing motor skills, revealing neurological adaptations linked to practicing chopstick use. The second paper presents EpiCa, an AI-driven tool designed to streamline causal inference in epidemiology, aiming to reduce inefficiencies and reliance on expert knowledge in traditional methodologies. A third study evaluates the efficacy of a large language model-based agent in generating hospital discharge summaries, addressing documentation burdens and clinician burnout. The fourth paper discusses how AI agents utilizing graphs and ontologies can enhance pharmacovigilance, simplifying the analysis of complex drug safety data. Finally, the fifth study compares task-specific and general-purpose AI in detecting subtle intraoperative cues during cataract surgery, highlighting the potential of vision-language models in surgical settings. Collectively, these papers underscore the potential of AI agents to improve clinical practices, epidemiological research, and patient safety through automation and advanced data analysis techniques.



### 1. Optimizing Motor Skills with HD-tDCS: Insights from a Pilot Study on Chopstick Proficiency

- **Authors:** Scholl, J. L., Bosch, T. J., Baugh, L. A.
- **Published:** 2026-02-02
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.01.30.702932](https://doi.org/10.64898/2026.01.30.702932)

- **Categories:** neuroscience


> This study explores how high-definition transcranial direct current stimulation (HD-tDCS) applied to the anterior supramarginal gyrus (aSMG) impacts motor learning, specifically in the context of chopstick proficiency. Utilizing a double-blind, sham-controlled design with 24 participants, the research found that participants receiving active stimulation demonstrated a significant increase in successful marble drops per minute (17.3 vs. 14.1), along with altered kinematic patterns and enhanced gamma-band activity, suggesting that HD-tDCS can effectively boost motor skill acquisition. These findings contribute to the agentic AI field by highlighting the neuromodulation techniques that might enhance human motor learning, relevant for developing AI systems that mimic or augment human skill acquisition processes.


<details>
<summary>Abstract</summary>

This study extends our previous research on neurological adaptations associated with learning to use chopsticks, in which we observed increased functional activity and connectivity changes in the anterior supramarginal gyrus (aSMG), a brain region previously implicated in novel tool use. In the present study, we investigated the effects of high-definition transcranial direct current stimulation (HD-tDCS) on motor learning by applying anodal stimulation to the aSMG in a double-blind, sham-controlled design with 24 participants (12 active, 12 sham). Participants in the active condition received [~]3 mA of HD-tDCS focused over the aSMG while watching a 20-minute video of the task - picking up a marble with chopsticks and dropping it into a cylindrical container. In comparison, participants in the sham condition watched the same video while receiving sham stimulation consisting of a 30-s ramp-up and ramp-down at the start and end of the 20-minute video. Immediately after the video task, all participants completed 15 one-minute trials in which they performed the task while electroencephalography (EEG) was recorded. Performance was assessed by the average number of successful marble drops per minute (MDPM) across trials. Additionally, video-based motion was analyzed using DeepLabCut to compare key kinematic metrics, providing insights into subtle variations in movement patterns during the marble task. Results showed a significant increase in MDPM in the active stimulation group compared to the sham group (17. 3 vs. 14. 1 MDPM; p < .05). Kinematic data showed increased movement jerk in the active stimulation group compared to sham (21719 vs 16926; p < .05), and EEG revealed differences in task-related gamma-band power over Cz (.0227 vs -.0758; p < .05). These findings suggest that HD-tDCS enhances the rate of motor learning in novel tool use and underscore the potential of aSMG-targeted stimulation in facilitating complex motor tasks. Further studies are warranted to explore the broader applicability of HD-tDCS in skill acquisition and rehabilitation.

New and NoteworthyThe presented study shows the role that the left anterior supramarginal gyrus plays in experience-independent tool learning. Anodal HD-tDCS applied during action observation increased performance in a subsequent chopstick skill acquisition task. This increase in performance was accompanied by enhanced task-related gamma-band activity and altered movement kinematics. By linking neuromodulation of the parietal tool-use hub to behavioral, kinematics, and electrophysiological changes, these findings significantly advance our understanding of how higher-order sensorimotor networks support tool-use learning.

</details>


### 2. An AI Agent for Automated Causal Inference in Epidemiology

- **Authors:** Liu, H., Shi, K., li, A., Li, X., Chu, J., Xue, Y., Cen, S., Wang, Y., Zhang, T.
- **Published:** 2026-02-06
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.06.26345723](https://doi.org/10.64898/2026.02.06.26345723)

- **Categories:** epidemiology


> The paper presents the EpiCausalX Agent, an AI-powered tool designed to automate the traditional workflow of causal inference in epidemiology, significantly reducing inefficiencies and expertise barriers. Utilizing the LangChain framework and incorporating advanced features such as multi-database retrieval, causal reasoning based on Hills criteria, and automated DAG visualization, the agent achieves full-process automation while maintaining usability for non-technical researchers. Key findings indicate that EpiCausalX provides evidence-based, traceable conclusions and has broad applications in observational research and clinical study design, thereby enhancing the accessibility and rigor of causal analysis in the field.


<details>
<summary>Abstract</summary>

ObjectiveTo address the inefficiency, subjectivity, and high expertise barrier of traditional epidemiological causal inference, this study designed, developed, and validated an AI-powered agent (EpiCausalX Agent) to automate the end-to-end workflow. It integrates cross-database literature retrieval, intelligent causal reasoning, and Directed Acyclic Graph (DAG) visualization to provide a reliable, accessible tool for researchers.

Materials and MethodsBuilt on the LangChain 1.0 framework with a layered design (Agent/Tool/Storage/Utility Layers), the agent uses the DeepSeek V3.2 LLM and ReAct paradigm for dynamic task orchestration. Four specialized tools were integrated including multi-database retrieval with 7 databases, causal inference based on Hills criteria and DAG logic, automated DAG drawing using NetworkX and Matplotlib, and clinical standard query. Performance was validated via unit tests, workflow verification, and usability testing.

ResultsThe agent achieved full-process automation. It efficiently retrieves and synthesizes literature, automatically identifies confounders and mediators, and generates standardized interactive DAGs. It produces evidence-based, traceable conclusions aligned with established epidemiological knowledge. Its user-friendly natural language interface enables seamless use by non-technical researchers who complete task initiation quickly without operational confusion. The agent is publicly available on WeChat Mini Program for easy access.

ConclusionEpiCausalX Agent advances intelligent, automated epidemiological research. By integrating domain expertise with AI agent technology, it overcomes limitations of manual methods and general LLMs to provide a specialized, verifiable, efficient solution. It has broad applications in observational research, clinical study design, and education to enhance productivity and lower barriers to rigorous causal analysis.

</details>


### 3. Safety and Utility of an Agentic Large Language Model-Based Hospital Course Summarizer: A Prospective Real-World Pilot Study

- **Authors:** Grolleau, F., Liang, A. S., Keyes, T., Ma, S. P., Lew, T., Huynh, T. R., Steele, N., Chung, P., Qin, P., Chandra, G., Wang, S. F., Mullen, E., Carpenter, L., Hoppenfeld, M., Morrin, M., Kyerematen, B. A., Ambers, N., Kotecha, N., Alsentzer, E., Hom, J., Shah, N. H., Schulman, K., Chen, J. H.
- **Published:** 2026-02-06
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.05.26345607](https://doi.org/10.64898/2026.02.05.26345607)

- **Categories:** health informatics


> The study evaluates the safety and utility of MedAgentBrief, an agentic AI workflow based on a large language model (LLM) used to generate hospital course summaries, aiming to alleviate clinician documentation burdens. In a prospective pilot study involving 11 hospitalist physicians, it was found that 57% of generated summaries were utilized, and while some inaccuracies were noted, the potential for harm was predominantly rated as minimal. Notably, the introduction of this AI tool significantly reduced physician burnout and offered time savings in documentation, highlighting its potential to enhance clinician well-being in real-world settings.


<details>
<summary>Abstract</summary>

ImportanceHigh-quality discharge summaries are essential for safe care transitions but contribute substantially to clinician documentation burden and burnout. While retrospective studies suggest large language models (LLMs) can generate clinical summaries of comparable quality to physicians, prospective data on their safety, utility, and impact on clinician well-being in real-world environments are lacking.

ObjectiveTo evaluate the safety, utilization, and impact on clinician burden of MedAgentBrief, an LLM-based agentic workflow for generating hospital course summaries, during prospective clinical deployment.

Design, Setting, and ParticipantsSingle-arm prospective pilot study of 11 attending hospitalist physicians at one inpatient unit from August 1 to October 11, 2025, with baseline comparisons drawn from April 9 to July 31, 2025.

InterventionMedAgentBrief, a custom agentic AI workflow utilizing Gemini 2.5 Pro, generated draft hospital course summaries nightly using the patients history and physical and daily progress notes. Drafts were securely emailed to physicians daily for review and optional use.

Main Outcomes and MeasuresThe primary outcome was physician-reported potential for and severity of harm from unedited summaries (AHRQ Common Format Harm Scale). Secondary outcomes included utilization rate, error types (omissions, inaccuracies, hallucinations), time spent in discharge summaries (EHR logs), and changes in cognitive burden (NASA Task Load Index [NASA-TLX]) and burnout (Stanford Professional Fulfillment Index [PFI] Work Exhaustion Scale).

ResultsThe system generated 1274 summaries. Of 384 discharges, physicians utilized AI content in 219 (57%) cases. Feedback on 100 summaries (40.2%) noted omissions (25%) and inaccuracies (20%) but rare hallucinations (2%). Physicians rated 88% of unedited summaries as having no harm potential and 1% as likely to cause moderate harm; no severe harm was reported. Physician burnout scores decreased significantly (1.75 vs 1.20; P = .03). Time savings were heterogeneous: 71% of physicians saw reductions in median documentation time (up to 2.9 minutes).

Conclusions and RelevanceAn LLM-based agentic workflow produced hospital course summaries that were frequently utilized with mild to minimal risk of harm identified. The intervention was associated with a significant reduction in physician burnout, supporting the viability of AI summarization to mitigate documentation burden.

</details>


### 4. Drug Safety Agents Using Graphs and Ontologies

- **Authors:** Mathialagan, C. S., Nip, A., Bhat, A.
- **Published:** 2026-02-05
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.04.26345582](https://doi.org/10.64898/2026.02.04.26345582)

- **Categories:** health informatics


> The paper presents a novel knowledge-grounded framework for analyzing drug safety cases, which enhances the efficiency of pharmacovigilance using a combination of disproportionality analysis and a hallucination-risk-aware execution planner. By prioritizing deterministic graph retrieval over generative methodologies, the system improves the reliability and explainability of adverse event hypothesis generation, addressing previous shortcomings in large language models related to causal reasoning and interpretability. Key findings indicate that integrating structured medical knowledge can lead to more accurate and clinically relevant assessments, with potential for further development through causal inference modules.


<details>
<summary>Abstract</summary>

In pharmacovigilance, analyzing drug safety cases is often time consuming due to the abundance of laboratory data, complex medical histories, and intricate temporal relationships. Agentic AI systems can significantly reduce case processing time by assisting medical reviewers in surfacing clinically relevant evidence. However, previous studies have highlighted that large language models alone lack causal reasoning and evidence-based interpretability.

To address these limitations, we present a knowledge-grounded safety case analysis framework that integrates disproportionality analysis to generate and prioritize potential adverse event hypotheses. Crucially, we introduce a novel hallucination-risk-aware execution planner that dynamically routes queries to the safest reasoning pathway, prioritizing deterministic graph retrieval over generative methods for clinically sensitive signals. The system demonstrates how structured medical knowledge and statistical evidence can be combined to support a reliable, explainable case assessment and can be readily extended with causal inference modules for deeper clinical reasoning.

</details>


### 5. Automated Task-Specific vs General-Purpose Artificial Intelligence for Detecting Subtle Intraoperative Warning Signs During Cataract Surgery: A Multicenter Diagnostic Study

- **Authors:** Zhang, Y., chen, l., Zhao, W., Zhang, H., Qiao, C., Liu, Z., Chung, C. H., Tan, M. C. J., Wang, M., Tham, Y. C., Koh, V., Cheng, C., Liu, D.
- **Published:** 2026-02-03
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.01.15.26344200](https://doi.org/10.64898/2026.01.15.26344200)

- **Categories:** ophthalmology


> This study benchmarks generalist vision-language models (VLMs) against autonomous AI agents in detecting subtle intraoperative warning signs during cataract surgery, specifically anterior capsular radial folds. Utilizing a multicenter dataset of 537 video clips, it compares the performance of 11 VLMs and classifiers generated by 4 autonomous AI agents, finding that the agent-engineered classifiers significantly outperformed VLMs, achieving an F1-score of 0.869 compared to the top VLM’s score of 0.519. These results demonstrate that autonomous AI agents are more effective for task-specific applications in fine-grained surgical video analysis, thus highlighting their potential in the agentic AI field.


<details>
<summary>Abstract</summary>

ImportanceVision-language models (VLMs) enable generalist multimodal reasoning, but their ability to resolve brief, low-contrast cues in surgical video without task-specific training is uncertain. Autonomous artificial intelligence (AI) agents offer an alternative paradigm by autonomously generating supervised classifiers tailored to specific visual tasks.

ObjectiveTo benchmark the performance of VLMs against supervised classifiers engineered by autonomous AI agents for detecting anterior capsular radial folds during continuous curvilinear capsulorhexis (CCC), and to compare both approaches with human graders.

Design, Setting, and ParticipantsThis retrospective diagnostic study utilized a multicenter dataset of 537 CCC videos collected from Beijing Tongren Hospital (China), National University Hospital (Singapore), and the OphNet-APTOS public dataset.

ExposurePresence or absence of anterior capsular radial folds during CCC, defined based on established expert consensus, was annotated at both clip and frame levels by senior glaucoma surgeons. Two analytic paradigms were evaluated: (1) direct zero-shot and few-shot inference using 11 generalist and medical-specific VLMs on single frames and frame sequences; and (2) autonomous code generation by 4 AI agents to construct supervised image classifiers from labeled frames. Human comparison included 7 graders with varying levels of ophthalmic experience.

Main Outcomes and MeasuresDiscrimination of fold-positive versus fold-negative cases was assessed using macro-averaged precision, recall, and F1-score at the clip and frame levels. Secondary outcomes included comparisons with human graders.

ResultsAmong 537 video clips (7.32 {+/-} 3.35 seconds), 156 (29.1%) were fold-positive. VLM performance was limited; the top-performing model, Qwen2.5-VL, achieved a mean F1-score of 0.519. Few-shot prompting improved GPT-4.1 performance (mean F1-score from 0.177 to 0.480) but remained unstable. In contrast, an agent-engineered classifier achieved an F1-score of 0.869 and an area under the receiver operating characteristic curve of 0.958. In comparison with human graders, the top agent-generated model (F1-score, 0.835) matched junior specialists (mean F1-score, 0.829), whereas fine-tuned VLMs (maximum F1-score, 0.606) underperformed all human graders.

Conclusions and RelevanceGeneralist VLMs showed limited capacity to detect subtle intraoperative cues, whereas autonomous AI agents successfully constructed task-specific classifiers with near-clinical-level performance. These findings support agent-driven supervised modeling as a more effective strategy for fine-grained surgical video interpretation.

Key PointsO_ST_ABSQuestionC_ST_ABSHow do generalist vision-language models (VLMs) and autonomous AI agents compare with human graders in detecting brief, low-contrast intraoperative cues in surgical video?

FindingsIn this retrospective, multicenter diagnostic benchmarking study of 537 phacoemulsification video clips, VLMs showed limited discrimination of anterior capsular radial folds, even with few-shot prompting, whereas autonomous AI agents successfully generated supervised classifiers with substantially higher performance, approaching that of junior glaucoma specialists.

MeaningFor fine-grained intraoperative video interpretation, task-specific classifiers engineered by autonomous agents currently demonstrate greater clinical relevance than generalist VLMs.

</details>


---



## Arxiv (162 papers)


### 1. Agentic Uncertainty Reveals Agentic Overconfidence

- **Authors:** Jean Kaddour, Srijan Patel, Gbètondji Dovonon, Leo Richter, Pasquale Minervini, Matt J. Kusner
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06948v1](http://arxiv.org/abs/2602.06948v1)
- **PDF:** [https://arxiv.org/pdf/2602.06948v1](https://arxiv.org/pdf/2602.06948v1)
- **Categories:** cs.AI, cs.LG


> This paper investigates agentic uncertainty in AI by examining how agents predict their success rates before, during, and after task execution, revealing a phenomenon termed agentic overconfidence. The study finds that agents with a success rate as low as 22% often overestimate their success at 77%, and notably, pre-execution assessments, despite lower information availability, can provide better discrimination than post-execution reviews. The researchers also discover that reframing the assessment process through adversarial prompting as a bug-finding task improves the calibration of success predictions, highlighting implications for building more reliable agentic AI systems.


<details>
<summary>Abstract</summary>

Can AI agents predict whether they will succeed at a task? We study agentic uncertainty by eliciting success probability estimates before, during, and after task execution. All results exhibit agentic overconfidence: some agents that succeed only 22% of the time predict 77% success. Counterintuitively, pre-execution assessment with strictly less information tends to yield better discrimination than standard post-execution review, though differences are not always significant. Adversarial prompting reframing assessment as bug-finding achieves the best calibration.

</details>


### 2. TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code

- **Authors:** Jiangping Huang, Wenguang Ye, Weisong Sun, Jian Zhang, Mingyue Zhang, Yang Liu
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06875v1](http://arxiv.org/abs/2602.06875v1)
- **PDF:** [https://arxiv.org/pdf/2602.06875v1](https://arxiv.org/pdf/2602.06875v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces TraceCoder, a multi-agent framework designed for the automated debugging of code generated by Large Language Models (LLMs), which often contain subtle bugs. The methodology involves instrumenting code to collect runtime traces, conducting causal analysis for precise error localization, and incorporating a Historical Lesson Learning Mechanism to leverage insights from previous failures for improved correction strategies. Key findings demonstrate that TraceCoder significantly enhances debugging performance, achieving up to a 34.43% improvement in Pass@1 accuracy compared to state-of-the-art methods, highlighting its effectiveness and efficiency in the agentic AI domain.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) often generate code with subtle but critical bugs, especially for complex tasks. Existing automated repair methods typically rely on superficial pass/fail signals, offering limited visibility into program behavior and hindering precise error localization. In addition, without a way to learn from prior failures, repair processes often fall into repetitive and inefficient cycles. To overcome these challenges, we present TraceCoder, a collaborative multi-agent framework that emulates the observe-analyze-repair process of human experts. The framework first instruments the code with diagnostic probes to capture fine-grained runtime traces, enabling deep insight into its internal execution. It then conducts causal analysis on these traces to accurately identify the root cause of the failure. This process is further enhanced by a novel Historical Lesson Learning Mechanism (HLLM), which distills insights from prior failed repair attempts to inform subsequent correction strategies and prevent recurrence of similar mistakes. To ensure stable convergence, a Rollback Mechanism enforces that each repair iteration constitutes a strict improvement toward the correct solution. Comprehensive experiments across multiple benchmarks show that TraceCoder achieves up to a 34.43\% relative improvement in Pass@1 accuracy over existing advanced baselines. Ablation studies verify the significance of each system component, with the iterative repair process alone contributing a 65.61\% relative gain in accuracy. Furthermore, TraceCoder significantly outperforms leading iterative methods in terms of both accuracy and cost-efficiency.

</details>


### 3. AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents

- **Authors:** Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster, Bassel Al Omari, Despoina Magka, Alberto Pepe, Alexis Audran-Reiss, Muna Aghamelu, Nicolas Baldwin, Lucia Cipolina-Kun, Jean-Christophe Gagnon-Audet, Chee Hau Leow, Sandra Lefdal, Hossam Mossalam, Abhinav Moudgil, Saba Nazir, Emanuel Tewolde, Isabel Urrego, Jordi Armengol Estape, Amar Budhiraja, Gaurav Chaurasia, Abhishek Charnalia, Derek Dunfield, Karen Hambardzumyan, Daniel Izcovich, Martin Josifoski, Ishita Mediratta, Kelvin Niu, Parth Pathak, Michael Shvartsman, Edan Toledo, Anton Protopopov, Roberta Raileanu, Alexander Miller, Tatiana Shavrina, Jakob Foerster, Yoram Bachrach
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06855v1](http://arxiv.org/abs/2602.06855v1)
- **PDF:** [https://arxiv.org/pdf/2602.06855v1](https://arxiv.org/pdf/2602.06855v1)
- **Categories:** cs.AI


> The paper introduces AIRS-Bench, a comprehensive suite of 20 benchmark tasks designed to evaluate the agentic capabilities of large language model (LLM) agents in scientific research across various domains, including language modeling and bioinformatics. The methodology focuses on assessing agents throughout the entire research lifecycle, from idea generation to iterative refinement, without providing baseline code, allowing for flexible task integration and comparison of different frameworks. Key findings reveal that while some agents outperform human state-of-the-art (SOTA) in four tasks, they do not achieve comparable performance in sixteen others, indicating that the benchmark is not fully saturated and highlighting opportunities for enhancement in the field of autonomous scientific research.


<details>
<summary>Abstract</summary>

LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce AIRS-Bench (the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. These tasks span diverse domains, including language modeling, mathematics, bioinformatics, and time series forecasting. AIRS-Bench tasks assess agentic capabilities over the full research lifecycle -- including idea generation, experiment analysis and iterative refinement -- without providing baseline code. The AIRS-Bench task format is versatile, enabling easy integration of new tasks and rigorous comparison across different agentic frameworks. We establish baselines using frontier models paired with both sequential and parallel scaffolds. Our results show that agents exceed human SOTA in four tasks but fail to match it in sixteen others. Even when agents surpass human benchmarks, they do not reach the theoretical performance ceiling for the underlying tasks. These findings indicate that AIRS-Bench is far from saturated and offers substantial room for improvement. We open-source the AIRS-Bench task definitions and evaluation code to catalyze further development in autonomous scientific research.

</details>


### 4. From Features to Actions: Explainability in Traditional and Agentic AI Systems

- **Authors:** Sindhuja Chaduvula, Jessee Ho, Kina Kim, Aravind Narayanan, Mahshid Alinoori, Muskan Garg, Dhanesh Ramachandram, Shaina Raza
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06841v1](http://arxiv.org/abs/2602.06841v1)
- **PDF:** [https://arxiv.org/pdf/2602.06841v1](https://arxiv.org/pdf/2602.06841v1)
- **Categories:** cs.AI


> This paper addresses the challenge of explainability in agentic AI systems, emphasizing the need for distinct approaches compared to traditional, static AI explanations. The authors evaluate attribution-based explanations in static tasks against trace-based diagnostics in agentic benchmarks, revealing that while attribution methods are effective for fixed predictions, they fail to adequately diagnose execution-level failures in agentic contexts. Key findings indicate that state tracking inconsistencies are significantly more common in failed agentic runs, leading to a recommendation for adopting trajectory-level explainability to better assess and diagnose the behavior of autonomous AI systems.


<details>
<summary>Abstract</summary>

Over the last decade, explainable AI has primarily focused on interpreting individual model predictions, producing post-hoc explanations that relate inputs to outputs under a fixed decision structure. Recent advances in large language models (LLMs) have enabled agentic AI systems whose behaviour unfolds over multi-step trajectories. In these settings, success and failure are determined by sequences of decisions rather than a single output. While useful, it remains unclear how explanation approaches designed for static predictions translate to agentic settings where behaviour emerges over time. In this work, we bridge the gap between static and agentic explainability by comparing attribution-based explanations with trace-based diagnostics across both settings. To make this distinction explicit, we empirically compare attribution-based explanations used in static classification tasks with trace-based diagnostics used in agentic benchmarks (TAU-bench Airline and AssistantBench). Our results show that while attribution methods achieve stable feature rankings in static settings (Spearman $ρ= 0.86$), they cannot be applied reliably to diagnose execution-level failures in agentic trajectories. In contrast, trace-grounded rubric evaluation for agentic settings consistently localizes behaviour breakdowns and reveals that state tracking inconsistency is 2.7$\times$ more prevalent in failed runs and reduces success probability by 49\%. These findings motivate a shift towards trajectory-level explainability for agentic systems when evaluating and diagnosing autonomous AI behaviour.
  Resources:
  https://github.com/VectorInstitute/unified-xai-evaluation-framework https://vectorinstitute.github.io/unified-xai-evaluation-framework

</details>


### 5. LLM Active Alignment: A Nash Equilibrium Perspective

- **Authors:** Tonghan Wang, Yuqi Pan, Xinyi Yang, Yanchen Jiang, Milind Tambe, David C. Parkes
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06836v1](http://arxiv.org/abs/2602.06836v1)
- **PDF:** [https://arxiv.org/pdf/2602.06836v1](https://arxiv.org/pdf/2602.06836v1)
- **Categories:** cs.AI


> The paper introduces a novel game-theoretic framework called LLM Active Alignment, employing Nash equilibrium analysis to guide and predict the behavior of populations of large language models (LLMs). By modeling agents' actions as strategic alignments with human subpopulations, the authors derive closed-form equilibrium characterizations that facilitate actionable alignment strategies aimed at socially beneficial outcomes. Key findings reveal that without this method, LLMs may exhibit detrimental behaviors, such as political exclusion of certain subpopulations, while the proposed framework effectively mitigates these issues, demonstrating its potential for regulating multi-agent interactions across various domains.


<details>
<summary>Abstract</summary>

We develop a game-theoretic framework for predicting and steering the behavior of populations of large language models (LLMs) through Nash equilibrium (NE) analysis. To avoid the intractability of equilibrium computation in open-ended text spaces, we model each agent's action as a mixture over human subpopulations. Agents choose actively and strategically which groups to align with, yielding an interpretable and behaviorally substantive policy class. We derive closed-form NE characterizations, adopting standard concave-utility assumptions to enable analytical system-level predictions and give explicit, actionable guidance for shifting alignment targets toward socially desirable outcomes. The method functions as an active alignment layer on top of existing alignment pipelines such as RLHF. In a social-media setting, we show that a population of LLMs, especially reasoning-based models, may exhibit political exclusion, pathologies where some subpopulations are ignored by all LLM agents, which can be avoided by our method, illustrating the promise of applying the method to regulate multi-agent LLM dynamics across domains.

</details>


### 6. ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training

- **Authors:** Dunwei Tu, Hongyan Hao, Hansi Yang, Yihao Chen, Yi-Kai Zhang, Zhikang Xia, Yu Yang, Yueqing Sun, Xingchen Liu, Furao Shen, Qi Gu, Hui Su, Xunliang Cai
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06820v1](http://arxiv.org/abs/2602.06820v1)
- **PDF:** [https://arxiv.org/pdf/2602.06820v1](https://arxiv.org/pdf/2602.06820v1)
- **Categories:** cs.AI


> The paper presents ScaleEnv, a novel framework for generating interactive environments from scratch, addressing the scarcity and limitations of existing environment synthesis methods for training generalist agents. The methodology involves procedural testing for reliability and ensuring task completeness through tool dependency graph expansion and verification of executable actions. Key findings indicate that agents trained in these diverse environments achieve significant performance improvements on multi-turn tool-use benchmarks and that increasing the number of domains enhances model generalization performance, emphasizing the importance of environmental diversity in robust AI agent training.


<details>
<summary>Abstract</summary>

Training generalist agents capable of adapting to diverse scenarios requires interactive environments for self-exploration. However, interactive environments remain critically scarce, and existing synthesis methods suffer from significant limitations regarding environmental diversity and scalability. To address these challenges, we introduce ScaleEnv, a framework that constructs fully interactive environments and verifiable tasks entirely from scratch. Specifically, ScaleEnv ensures environment reliability through procedural testing, and guarantees task completeness and solvability via tool dependency graph expansion and executable action verification. By enabling agents to learn through exploration within ScaleEnv, we demonstrate significant performance improvements on unseen, multi-turn tool-use benchmarks such as $τ^2$-Bench and VitaBench, highlighting strong generalization capabilities. Furthermore, we investigate the relationship between increasing number of domains and model generalization performance, providing empirical evidence that scaling environmental diversity is critical for robust agent learning.

</details>


### 7. Pairwise is Not Enough: Hypergraph Neural Networks for Multi-Agent Pathfinding

- **Authors:** Rishabh Jain, Keisuke Okumura, Michael Amir, Pietro Lio, Amanda Prorok
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06733v1](http://arxiv.org/abs/2602.06733v1)
- **PDF:** [https://arxiv.org/pdf/2602.06733v1](https://arxiv.org/pdf/2602.06733v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> The paper introduces a novel architecture called HMAGAT (Hypergraph Multi-Agent Attention Network) for solving Multi-Agent Path Finding (MAPF) tasks, addressing the limitations of traditional Graph Neural Networks (GNNs) that rely on pairwise message passing. By employing directed hypergraphs to capture group dynamics, HMAGAT significantly improves the modeling of complex interactions among multiple agents, achieving state-of-the-art performance while using substantially fewer parameters and training data compared to previous models. The findings emphasize that leveraging appropriate inductive biases in model design can be more beneficial for performance in multi-agent environments than merely increasing the amount of training data or parameter count.


<details>
<summary>Abstract</summary>

Multi-Agent Path Finding (MAPF) is a representative multi-agent coordination problem, where multiple agents are required to navigate to their respective goals without collisions. Solving MAPF optimally is known to be NP-hard, leading to the adoption of learning-based approaches to alleviate the online computational burden. Prevailing approaches, such as Graph Neural Networks (GNNs), are typically constrained to pairwise message passing between agents. However, this limitation leads to suboptimal behaviours and critical issues, such as attention dilution, particularly in dense environments where group (i.e. beyond just two agents) coordination is most critical. Despite the importance of such higher-order interactions, existing approaches have not been able to fully explore them. To address this representational bottleneck, we introduce HMAGAT (Hypergraph Multi-Agent Attention Network), a novel architecture that leverages attentional mechanisms over directed hypergraphs to explicitly capture group dynamics. Empirically, HMAGAT establishes a new state-of-the-art among learning-based MAPF solvers: e.g., despite having just 1M parameters and being trained on 100$\times$ less data, it outperforms the current SoTA 85M parameter model. Through detailed analysis of HMAGAT's attention values, we demonstrate how hypergraph representations mitigate the attention dilution inherent in GNNs and capture complex interactions where pairwise methods fail. Our results illustrate that appropriate inductive biases are often more critical than the training data size or sheer parameter count for multi-agent problems.

</details>


### 8. Table-as-Search: Formulate Long-Horizon Agentic Information Seeking as Table Completion

- **Authors:** Tian Lan, Felix Henry, Bin Zhu, Qianghuai Jia, Junyang Ren, Qihang Pu, Haijun Li, Longyue Wang, Zhao Xu, Weihua Luo
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06724v1](http://arxiv.org/abs/2602.06724v1)
- **PDF:** [https://arxiv.org/pdf/2602.06724v1](https://arxiv.org/pdf/2602.06724v1)
- **Categories:** cs.CL


> The paper introduces Table-as-Search (TaS), a novel framework that reformulates long-horizon Information Seeking (InfoSeeking) tasks as Table Completion, significantly improving an agent's ability to maintain focus and coherence during extensive exploration. The methodology involves organizing queries into a structured table schema, where search states are systematically recorded and managed, allowing for effective planning and state tracking. The key findings highlight that TaS outperforms existing state-of-the-art baselines across multiple benchmarks and demonstrates enhanced robustness, efficiency, scalability, and flexibility in handling complex InfoSeeking tasks, contributing valuable insights to the field of agentic AI.


<details>
<summary>Abstract</summary>

Current Information Seeking (InfoSeeking) agents struggle to maintain focus and coherence during long-horizon exploration, as tracking search states, including planning procedure and massive search results, within one plain-text context is inherently fragile. To address this, we introduce \textbf{Table-as-Search (TaS)}, a structured planning framework that reformulates the InfoSeeking task as a Table Completion task. TaS maps each query into a structured table schema maintained in an external database, where rows represent search candidates and columns denote constraints or required information. This table precisely manages the search states: filled cells strictly record the history and search results, while empty cells serve as an explicit search plan. Crucially, TaS unifies three distinct InfoSeeking tasks: Deep Search, Wide Search, and the challenging DeepWide Search. Extensive experiments demonstrate that TaS significantly outperforms numerous state-of-the-art baselines across three kinds of benchmarks, including multi-agent framework and commercial systems. Furthermore, our analysis validates the TaS's superior robustness in long-horizon InfoSeeking, alongside its efficiency, scalability and flexibility. Code and datasets are publicly released at https://github.com/AIDC-AI/Marco-Search-Agent.

</details>


### 9. Sample-Efficient Policy Space Response Oracles with Joint Experience Best Response

- **Authors:** Ariyan Bighashdel, Thiago D. Simão, Frans A. Oliehoek
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06599v1](http://arxiv.org/abs/2602.06599v1)
- **PDF:** [https://arxiv.org/pdf/2602.06599v1](https://arxiv.org/pdf/2602.06599v1)
- **Categories:** cs.MA, cs.AI, cs.LG


> The paper presents the Joint Experience Best Response (JBR) approach, a significant enhancement to the Policy Space Response Oracles (PSRO) framework in multi-agent reinforcement learning (MARL), aimed at improving sample efficiency in large-scale environments. By enabling simultaneous computation of best responses for all agents from a shared dataset, JBR reduces the need for extensive environment interactions while addressing distribution-shift bias through various strategies. The key findings reveal that JBR, particularly with Exploration-Augmented techniques, achieves superior accuracy and efficiency compared to traditional methods, making it a practical solution for large-scale strategic learning while maintaining equilibrium robustness.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) offers a scalable alternative to exact game-theoretic analysis but suffers from non-stationarity and the need to maintain diverse populations of strategies that capture non-transitive interactions. Policy Space Response Oracles (PSRO) address these issues by iteratively expanding a restricted game with approximate best responses (BRs), yet per-agent BR training makes it prohibitively expensive in many-agent or simulator-expensive settings. We introduce Joint Experience Best Response (JBR), a drop-in modification to PSRO that collects trajectories once under the current meta-strategy profile and reuses this joint dataset to compute BRs for all agents simultaneously. This amortizes environment interaction and improves the sample efficiency of best-response computation. Because JBR converts BR computation into an offline RL problem, we propose three remedies for distribution-shift bias: (i) Conservative JBR with safe policy improvement, (ii) Exploration-Augmented JBR that perturbs data collection and admits theoretical guarantees, and (iii) Hybrid BR that interleaves JBR with periodic independent BR updates. Across benchmark multi-agent environments, Exploration-Augmented JBR achieves the best accuracy-efficiency trade-off, while Hybrid BR attains near-PSRO performance at a fraction of the sample cost. Overall, JBR makes PSRO substantially more practical for large-scale strategic learning while preserving equilibrium robustness.

</details>


### 10. SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees

- **Authors:** Tianyi Hu, Qingxu Fu, Yanxi Chen, Zhaoyang Liu, Bolin Ding
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06554v1](http://arxiv.org/abs/2602.06554v1)
- **PDF:** [https://arxiv.org/pdf/2602.06554v1](https://arxiv.org/pdf/2602.06554v1)
- **Categories:** cs.AI


> The paper presents SeeUPO, a novel reinforcement learning approach designed to provide convergence guarantees for large language model (LLM)-based AI agents in multi-turn interaction scenarios. The authors systematically investigate the effects of various policy update mechanisms and advantage estimation methods, finding that traditional algorithms struggle with convergence and training stability. Through experiments on benchmark environments, SeeUPO demonstrates significant performance improvements over existing algorithms, achieving relative gains of 43.3%-54.6%, showcasing its effectiveness as a critic-free method that ensures both monotonic improvement and convergence to global optimal solutions.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) has emerged as the predominant paradigm for training large language model (LLM)-based AI agents. However, existing backbone RL algorithms lack verified convergence guarantees in agentic scenarios, especially in multi-turn settings, which can lead to training instability and failure to converge to optimal policies.
  In this paper, we systematically analyze how different combinations of policy update mechanisms and advantage estimation methods affect convergence properties in single/multi-turn scenarios. We find that REINFORCE with Group Relative Advantage Estimation (GRAE) can converge to the globally optimal under undiscounted conditions, but the combination of PPO & GRAE breaks PPO's original monotonic improvement property. Furthermore, we demonstrate that mainstream backbone RL algorithms cannot simultaneously achieve both critic-free and convergence guarantees in multi-turn scenarios.
  To address this, we propose SeeUPO (Sequence-level Sequential Update Policy Optimization), a critic-free approach with convergence guarantees for multi-turn interactions. SeeUPO models multi-turn interaction as sequentially executed multi-agent bandit problems. Through turn-by-turn sequential policy updates in reverse execution order, it ensures monotonic improvement and convergence to global optimal solution via backward induction.
  Experiments on AppWorld and BFCL v4 demonstrate SeeUPO's substantial improvements over existing backbone algorithms: relative gains of 43.3%-54.6% on Qwen3-14B and 24.1%-41.9% on Qwen2.5-14B (averaged across benchmarks), along with superior training stability.

</details>


### 11. Completing Missing Annotation: Multi-Agent Debate for Accurate and Scalable Relevant Assessment for IR Benchmarks

- **Authors:** Minjeong Ban, Jeonghwan Choi, Hyangsuk Min, Nicole Hee-Yeon Kim, Minseok Kim, Jae-Gil Lee, Hwanjun Song
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06526v1](http://arxiv.org/abs/2602.06526v1)
- **PDF:** [https://arxiv.org/pdf/2602.06526v1](https://arxiv.org/pdf/2602.06526v1)
- **Categories:** cs.CL, cs.AI


> The paper presents DREAM, a multi-agent debate framework that enhances relevance assessment in information retrieval (IR) by utilizing LLM agents that engage in iterative critiques based on opposing stances. This methodology resulted in a significantly accurate labeling process, achieving 95.2% accuracy with just 3.5% human involvement, and led to the creation of the BRIDGE benchmark, which identifies 29,824 previously missing relevant chunks. The findings highlight that addressing these data gaps not only improves the reliability of IR evaluations but also clarifies issues like retrieval-generation misalignment, making significant contributions to the field of agentic AI.


<details>
<summary>Abstract</summary>

Information retrieval (IR) evaluation remains challenging due to incomplete IR benchmark datasets that contain unlabeled relevant chunks. While LLMs and LLM-human hybrid strategies reduce costly human effort, they remain prone to LLM overconfidence and ineffective AI-to-human escalation. To address this, we propose DREAM, a multi-round debate-based relevance assessment framework with LLM agents, built on opposing initial stances and iterative reciprocal critique. Through our agreement-based debate, it yields more accurate labeling for certain cases and more reliable AI-to-human escalation for uncertain ones, achieving 95.2% labeling accuracy with only 3.5% human involvement. Using DREAM, we build BRIDGE, a refined benchmark that mitigates evaluation bias and enables fairer retriever comparison by uncovering 29,824 missing relevant chunks. We then re-benchmark IR systems and extend evaluation to RAG, showing that unaddressed holes not only distort retriever rankings but also drive retrieval-generation misalignment. The relevance assessment framework is available at https: //github.com/DISL-Lab/DREAM-ICLR-26; and the BRIDGE dataset is available at https://github.com/DISL-Lab/BRIDGE-Benchmark.

</details>


### 12. Evolutionary Generation of Multi-Agent Systems

- **Authors:** Yuntong Hu, Matthew Trager, Yuting Zhang, Yi Zhang, Shuo Yang, Wei Xia, Stefano Soatto
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06511v1](http://arxiv.org/abs/2602.06511v1)
- **PDF:** [https://arxiv.org/pdf/2602.06511v1](https://arxiv.org/pdf/2602.06511v1)
- **Categories:** cs.LG


> The paper presents Evolutionary Generation of Multi-Agent Systems (EvoMAS), a novel approach for automatically generating multi-agent system architectures by framing the process as structured configuration generation through evolutionary methods. Utilizing feedback-conditioned mutation and crossover based on execution traces, EvoMAS iterates on initial configurations, resulting in improved design flexibility and system performance. The methodology demonstrates significant advancements in task performance, executability, and robustness, outperforming previous methods, including human-designed systems and the EvoAgent evolutionary approach, across various benchmarks in reasoning and tool-use tasks.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based multi-agent systems (MAS) show strong promise for complex reasoning, planning, and tool-augmented tasks, but designing effective MAS architectures remains labor-intensive, brittle, and hard to generalize. Existing automatic MAS generation methods either rely on code generation, which often leads to executability and robustness failures, or impose rigid architectural templates that limit expressiveness and adaptability. We propose Evolutionary Generation of Multi-Agent Systems (EvoMAS), which formulates MAS generation as structured configuration generation. EvoMAS performs evolutionary generation in configuration space. Specifically, EvoMAS selects initial configurations from a pool, applies feedback-conditioned mutation and crossover guided by execution traces, and iteratively refines both the candidate pool and an experience memory. We evaluate EvoMAS on diverse benchmarks, including BBEH, SWE-Bench, and WorkBench, covering reasoning, software engineering, and tool-use tasks. EvoMAS consistently improves task performance over both human-designed MAS and prior automatic MAS generation methods, while producing generated systems with higher executability and runtime robustness. EvoMAS outperforms the agent evolution method EvoAgent by +10.5 points on BBEH reasoning and +7.1 points on WorkBench. With Claude-4.5-Sonnet, EvoMAS also reaches 79.1% on SWE-Bench-Verified, matching the top of the leaderboard.

</details>


### 13. JADE: Expert-Grounded Dynamic Evaluation for Open-Ended Professional Tasks

- **Authors:** Lanbo Lin, Jiayao Liu, Tianyuan Yang, Li Cai, Yuanwu Xu, Lei Wei, Sicong Xie, Guannan Zhang
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06486v1](http://arxiv.org/abs/2602.06486v1)
- **PDF:** [https://arxiv.org/pdf/2602.06486v1](https://arxiv.org/pdf/2602.06486v1)
- **Categories:** cs.AI


> The paper introduces JADE, a two-layer evaluation framework designed to effectively assess agentic AI performance on open-ended professional tasks, balancing the need for rigor with the flexibility to accommodate diverse responses. The first layer incorporates expert knowledge through a predefined set of evaluation skills, while the second layer allows for dynamic, claim-level assessments, enhancing evaluation stability and identifying agent failure modes that static rubrics or LLM-based evaluations overlook. Experimental results demonstrate JADE's alignment with expert-authored criteria and its adaptability across various professional domains, highlighting its potential to improve assessments in agentic AI applications.


<details>
<summary>Abstract</summary>

Evaluating agentic AI on open-ended professional tasks faces a fundamental dilemma between rigor and flexibility. Static rubrics provide rigorous, reproducible assessment but fail to accommodate diverse valid response strategies, while LLM-as-a-judge approaches adapt to individual responses yet suffer from instability and bias. Human experts address this dilemma by combining domain-grounded principles with dynamic, claim-level assessment. Inspired by this process, we propose JADE, a two-layer evaluation framework. Layer 1 encodes expert knowledge as a predefined set of evaluation skills, providing stable evaluation criteria. Layer 2 performs report-specific, claim-level evaluation to flexibly assess diverse reasoning strategies, with evidence-dependency gating to invalidate conclusions built on refuted claims. Experiments on BizBench show that JADE improves evaluation stability and reveals critical agent failure modes missed by holistic LLM-based evaluators. We further demonstrate strong alignment with expert-authored rubrics and effective transfer to a medical-domain benchmark, validating JADE across professional domains. Our code is publicly available at https://github.com/smiling-world/JADE.

</details>


### 14. Prism: Spectral Parameter Sharing for Multi-Agent Reinforcement Learning

- **Authors:** Kyungbeom Kim, Seungwon Oh, Kyung-Joong Kim
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06476v1](http://arxiv.org/abs/2602.06476v1)
- **PDF:** [https://arxiv.org/pdf/2602.06476v1](https://arxiv.org/pdf/2602.06476v1)
- **Categories:** cs.MA, cs.AI, cs.LG


> The paper introduces Prism, a novel parameter sharing framework for multi-agent reinforcement learning that utilizes singular value decomposition (SVD) to induce diversity among agents while maintaining scalability. By allowing agents to share singular vector directions while learning distinct spectral masks on singular values, Prism promotes inter-agent diversity without compromising resource efficiency. The extensive experimental results demonstrate that Prism consistently outperforms conventional methods on various benchmarks, achieving competitive performance with enhanced resource utilization in both homogeneous and heterogeneous environments.


<details>
<summary>Abstract</summary>

Parameter sharing is a key strategy in multi-agent reinforcement learning (MARL) for improving scalability, yet conventional fully shared architectures often collapse into homogeneous behaviors. Recent methods introduce diversity through clustering, pruning, or masking, but typically compromise resource efficiency. We propose Prism, a parameter sharing framework that induces inter-agent diversity by representing shared networks in the spectral domain via singular value decomposition (SVD). All agents share the singular vector directions while learning distinct spectral masks on singular values. This mechanism encourages inter-agent diversity and preserves scalability. Extensive experiments on both homogeneous (LBF, SMACv2) and heterogeneous (MaMuJoCo) benchmarks show that Prism achieves competitive performance with superior resource efficiency.

</details>


### 15. TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents

- **Authors:** Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, Yilong Yin
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06443v1](http://arxiv.org/abs/2602.06443v1)
- **PDF:** [https://arxiv.org/pdf/2602.06443v1](https://arxiv.org/pdf/2602.06443v1)
- **Categories:** cs.CR, cs.AI


> The paper presents TrajAD, a novel framework for trajectory anomaly detection aimed at enhancing the trustworthiness of large language model (LLM) agents by focusing on intermediate execution processes rather than just static input/output filtering. The authors introduce TrajBench, a synthesized dataset designed to capture a variety of procedural anomalies, demonstrating through experimental results that general-purpose LLMs struggle with anomaly detection and localization. Their findings highlight the necessity of fine-grained process supervision for training specialized verifiers like TrajAD, which significantly outperforms baseline methods, thereby underscoring the importance of this approach in ensuring agent reliability in AI systems.


<details>
<summary>Abstract</summary>

We address the problem of runtime trajectory anomaly detection, a critical capability for enabling trustworthy LLM agents. Current safety measures predominantly focus on static input/output filtering. However, we argue that ensuring LLM agents reliability requires auditing the intermediate execution process. In this work, we formulate the task of Trajectory Anomaly Detection. The goal is not merely detection, but precise error localization. This capability is essential for enabling efficient rollback-and-retry. To achieve this, we construct TrajBench, a dataset synthesized via a perturb-and-complete strategy to cover diverse procedural anomalies. Using this benchmark, we investigate the capability of models in process supervision. We observe that general-purpose LLMs, even with zero-shot prompting, struggle to identify and localize these anomalies. This reveals that generalized capabilities do not automatically translate to process reliability. To address this, we propose TrajAD, a specialized verifier trained with fine-grained process supervision. Our approach outperforms baselines, demonstrating that specialized supervision is essential for building trustworthy agents.

</details>


### 16. Zero-Trust Runtime Verification for Agentic Payment Protocols: Mitigating Replay and Context-Binding Failures in AP2

- **Authors:** Qianlong Lan, Anuj Kaul, Shaun Jones, Stephanie Westrum
- **Published:** 2026-02-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06345v1](http://arxiv.org/abs/2602.06345v1)
- **PDF:** [https://arxiv.org/pdf/2602.06345v1](https://arxiv.org/pdf/2602.06345v1)
- **Categories:** cs.CR, cs.AI


> This paper presents a zero-trust runtime verification framework designed to enhance the security of the Agent Payments Protocol (AP2) in autonomous AI agent-driven payment systems by addressing vulnerabilities related to replay and context-binding failures. The methodology involves enforcing explicit context binding and consume-once semantics through the use of dynamically generated, time-bound nonces, ensuring that authorization decisions are made at execution time rather than relying on static properties. Key findings indicate that this framework effectively mitigates various attack types while maintaining low verification latencies, proving that robust security can be achieved with minimal overhead in high concurrency environments relevant to agentic AI applications.


<details>
<summary>Abstract</summary>

The deployment of autonomous AI agents capable of executing commercial transactions has motivated the adoption of mandate-based payment authorization protocols, including the Universal Commerce Protocol (UCP) and the Agent Payments Protocol (AP2). These protocols replace interactive, session-based authorization with cryptographically issued mandates, enabling asynchronous and autonomous execution. While AP2 provides specification-level guarantees through signature verification, explicit binding, and expiration semantics, real-world agentic execution introduces runtime behaviors such as retries, concurrency, and orchestration that challenge implicit assumptions about mandate usage.
  In this work, we present a security analysis of the AP2 mandate lifecycle and identify enforcement gaps that arise during runtime in agent-based payment systems. We propose a zero-trust runtime verification framework that enforces explicit context binding and consume-once mandate semantics using dynamically generated, time-bound nonces, ensuring that authorization decisions are evaluated at execution time rather than assumed from static issuance properties.
  Through simulation-based evaluation under high concurrency, we show that context-aware binding and consume-once enforcement address distinct and complementary attack classes, and that both are required to prevent replay and context-redirect attacks. The proposed framework mitigates all evaluated attacks while maintaining stable verification latency of approximately 3.8~ms at throughput levels up to 10{,}000 transactions per second. We further demonstrate that the required runtime state is bounded by peak concurrency rather than cumulative transaction history, indicating that robust runtime security for agentic payment execution can be achieved with minimal and predictable overhead.

</details>


### 17. RuleSmith: Multi-Agent LLMs for Automated Game Balancing

- **Authors:** Ziyao Zeng, Chen Liu, Tianyu Liu, Hao Wang, Xiatao Sun, Fengyu Yang, Xiaofeng Liu, Zhiwen Fan
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06232v1](http://arxiv.org/abs/2602.06232v1)
- **PDF:** [https://arxiv.org/pdf/2602.06232v1](https://arxiv.org/pdf/2602.06232v1)
- **Categories:** cs.LG, cs.AI, cs.GT, cs.MA


> The paper presents RuleSmith, an innovative framework that automates game balancing using multi-agent large language models (LLMs) combined with a game engine and Bayesian optimization. By applying RuleSmith to CivMini, the authors demonstrate that LLMs can interpret game rules and states to evaluate balance metrics through efficient self-play and adaptive sampling. The findings reveal that RuleSmith not only converges to well-balanced game configurations but also offers interpretable rule adjustments, showcasing the potential of LLMs in optimizing complex multi-agent systems in game design.


<details>
<summary>Abstract</summary>

Game balancing is a longstanding challenge requiring repeated playtesting, expert intuition, and extensive manual tuning. We introduce RuleSmith, the first framework that achieves automated game balancing by leveraging the reasoning capabilities of multi-agent LLMs. It couples a game engine, multi-agent LLMs self-play, and Bayesian optimization operating over a multi-dimensional rule space. As a proof of concept, we instantiate RuleSmith on CivMini, a simplified civilization-style game containing heterogeneous factions, economy systems, production rules, and combat mechanics, all governed by tunable parameters. LLM agents interpret textual rulebooks and game states to generate actions, to conduct fast evaluation of balance metrics such as win-rate disparities. To search the parameter landscape efficiently, we integrate Bayesian optimization with acquisition-based adaptive sampling and discrete projection: promising candidates receive more evaluation games for accurate assessment, while exploratory candidates receive fewer games for efficient exploration. Experiments show that RuleSmith converges to highly balanced configurations and provides interpretable rule adjustments that can be directly applied to downstream game systems. Our results illustrate that LLM simulation can serve as a powerful surrogate for automating design and balancing in complex multi-agent environments.

</details>


### 18. Flow Matching for Offline Reinforcement Learning with Discrete Actions

- **Authors:** Fairoz Nower Khan, Nabuat Zaman Nahim, Ruiquan Huang, Haibo Yang, Peizhong Ju
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06138v1](http://arxiv.org/abs/2602.06138v1)
- **PDF:** [https://arxiv.org/pdf/2602.06138v1](https://arxiv.org/pdf/2602.06138v1)
- **Categories:** cs.LG


> The main contribution of this paper is the extension of flow matching techniques for offline reinforcement learning (RL) to support discrete action spaces, which traditionally have been challenging for generative policies. The authors employ continuous-time Markov chains and propose a Q-weighted flow matching objective to enable this extension, while also addressing the complexity of multi-agent settings through a factorized conditional path approach. Key findings indicate that the proposed method maintains performance across various challenging scenarios, including high-dimensional control tasks and dynamic multi-objective preferences, thereby offering a versatile solution for both discrete and continuous action problems in agentic AI applications.


<details>
<summary>Abstract</summary>

Generative policies based on diffusion models and flow matching have shown strong promise for offline reinforcement learning (RL), but their applicability remains largely confined to continuous action spaces. To address a broader range of offline RL settings, we extend flow matching to a general framework that supports discrete action spaces with multiple objectives. Specifically, we replace continuous flows with continuous-time Markov chains, trained using a Q-weighted flow matching objective. We then extend our design to multi-agent settings, mitigating the exponential growth of joint action spaces via a factorized conditional path. We theoretically show that, under idealized conditions, optimizing this objective recovers the optimal policy. Extensive experiments further demonstrate that our method performs robustly in practical scenarios, including high-dimensional control, multi-modal decision-making, and dynamically changing preferences over multiple objectives. Our discrete framework can also be applied to continuous-control problems through action quantization, providing a flexible trade-off between representational complexity and performance.

</details>


### 19. DyTopo: Dynamic Topology Routing for Multi-Agent Reasoning via Semantic Matching

- **Authors:** Yuxing Lu, Yucheng Hu, Xukai Zhao, Jiuxin Cao
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06039v1](http://arxiv.org/abs/2602.06039v1)
- **PDF:** [https://arxiv.org/pdf/2602.06039v1](https://arxiv.org/pdf/2602.06039v1)
- **Categories:** cs.AI


> The paper presents DyTopo, a dynamic communication framework designed to enhance multi-agent reasoning by reconstructing a sparse directed graph for each round of problem-solving based on agents' needs and offers. Utilizing semantic matching for routing messages, DyTopo optimizes communication dynamically, leading to improved performance in code generation and mathematical reasoning tasks, achieving an average 6.2% accuracy increase over baseline methods. Additionally, DyTopo provides interpretable coordination traces, allowing for qualitative analysis of communication patterns throughout the reasoning process.


<details>
<summary>Abstract</summary>

Multi-agent systems built from prompted large language models can improve multi-round reasoning, yet most existing pipelines rely on fixed, trajectory-wide communication patterns that are poorly matched to the stage-dependent needs of iterative problem solving. We introduce DyTopo, a manager-guided multi-agent framework that reconstructs a sparse directed communication graph at each round. Conditioned on the manager's round goal, each agent outputs lightweight natural-language query (need) and \key (offer) descriptors; DyTopo embeds these descriptors and performs semantic matching, routing private messages only along the induced edges. Across code generation and mathematical reasoning benchmarks and four LLM backbones, DyTopo consistently outperforms over the strongest baseline (avg. +6.2). Beyond accuracy, DyTopo yields an interpretable coordination trace via the evolving graphs, enabling qualitative inspection of how communication pathways reconfigure across rounds.

</details>


### 20. CommCP: Efficient Multi-Agent Coordination via LLM-Based Communication with Conformal Prediction

- **Authors:** Xiaopan Zhang, Zejin Wang, Zhixu Li, Jianpeng Yao, Jiachen Li
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06038v1](http://arxiv.org/abs/2602.06038v1)
- **PDF:** [https://arxiv.org/pdf/2602.06038v1](https://arxiv.org/pdf/2602.06038v1)
- **Categories:** cs.RO, cs.AI, cs.CV, cs.LG, cs.MA


> The paper presents CommCP, a novel decentralized communication framework that utilizes large language models (LLMs) and conformal prediction to enhance multi-agent coordination in the multi-agent multi-task Embodied Question Answering (MM-EQA) problem. The methodology involves formalizing the information-gathering process in cooperative environments, and the framework aims to improve communication reliability among heterogeneous robots with different capabilities. Key findings indicate that CommCP significantly increases task success rates and exploration efficiency compared to existing baselines, contributing to the agentic AI field by addressing effective communication strategies for collaborative robotic systems.


<details>
<summary>Abstract</summary>

To complete assignments provided by humans in natural language, robots must interpret commands, generate and answer relevant questions for scene understanding, and manipulate target objects. Real-world deployments often require multiple heterogeneous robots with different manipulation capabilities to handle different assignments cooperatively. Beyond the need for specialized manipulation skills, effective information gathering is important in completing these assignments. To address this component of the problem, we formalize the information-gathering process in a fully cooperative setting as an underexplored multi-agent multi-task Embodied Question Answering (MM-EQA) problem, which is a novel extension of canonical Embodied Question Answering (EQA), where effective communication is crucial for coordinating efforts without redundancy. To address this problem, we propose CommCP, a novel LLM-based decentralized communication framework designed for MM-EQA. Our framework employs conformal prediction to calibrate the generated messages, thereby minimizing receiver distractions and enhancing communication reliability. To evaluate our framework, we introduce an MM-EQA benchmark featuring diverse, photo-realistic household scenarios with embodied questions. Experimental results demonstrate that CommCP significantly enhances the task success rate and exploration efficiency over baselines. The experiment videos, code, and dataset are available on our project website: https://comm-cp.github.io.

</details>


### 21. PhysicsAgentABM: Physics-Guided Generative Agent-Based Modeling

- **Authors:** Kavana Venkatesh, Yinhan He, Jundong Li, Jiaming Cui
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06030v1](http://arxiv.org/abs/2602.06030v1)
- **PDF:** [https://arxiv.org/pdf/2602.06030v1](https://arxiv.org/pdf/2602.06030v1)
- **Categories:** cs.MA, cs.LG


> The paper introduces PhysicsAgentABM, a novel framework that integrates physics-guided principles into agent-based modeling to enhance the performance and interpretability of simulations within multi-agent systems. The methodology involves clustering agents based on behavioral coherence, utilizing symbolic representations for transition modeling, and employing an uncertainty-aware fusion strategy to produce accurate state transitions. Key findings demonstrate that PhysicsAgentABM significantly improves event-time accuracy and calibration over traditional models and LLMs, showcasing its potential to advance scalable, calibrated simulations in agentic AI applications across various fields.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based multi-agent systems enable expressive agent reasoning but are expensive to scale and poorly calibrated for timestep-aligned state-transition simulation, while classical agent-based models (ABMs) offer interpretability but struggle to integrate rich individual-level signals and non-stationary behaviors. We propose PhysicsAgentABM, which shifts inference to behaviorally coherent agent clusters: state-specialized symbolic agents encode mechanistic transition priors, a multimodal neural transition model captures temporal and interaction dynamics, and uncertainty-aware epistemic fusion yields calibrated cluster-level transition distributions. Individual agents then stochastically realize transitions under local constraints, decoupling population inference from entity-level variability. We further introduce ANCHOR, an LLM agent-driven clustering strategy based on cross-contextual behavioral responses and a novel contrastive loss, reducing LLM calls by up to 6-8 times. Experiments across public health, finance, and social sciences show consistent gains in event-time accuracy and calibration over mechanistic, neural, and LLM baselines. By re-architecting generative ABM around population-level inference with uncertainty-aware neuro-symbolic fusion, PhysicsAgentABM establishes a new paradigm for scalable and calibrated simulation with LLMs.

</details>


### 22. AgenticPay: A Multi-Agent LLM Negotiation System for Buyer-Seller Transactions

- **Authors:** Xianyang Liu, Shangding Gu, Dawn Song
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06008v1](http://arxiv.org/abs/2602.06008v1)
- **PDF:** [https://arxiv.org/pdf/2602.06008v1](https://arxiv.org/pdf/2602.06008v1)
- **Categories:** cs.AI, cs.LG


> The paper presents AgenticPay, a novel benchmark and simulation framework designed for evaluating multi-agent negotiations in buyer-seller transactions mediated by natural language, addressing the lack of principled evaluation settings in existing benchmarks. The methodology involves modeling markets with private constraints and product-dependent valuations, enabling linguistic negotiation through over 110 diverse tasks, which facilitates structured action extraction and provides metrics for assessing negotiation performance. Key findings reveal significant gaps in negotiation performance among state-of-the-art LLMs, particularly in long-horizon strategic reasoning, positioning AgenticPay as a foundational tool for future research in agentic AI and language-mediated market interactions.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based agents are increasingly expected to negotiate, coordinate, and transact autonomously, yet existing benchmarks lack principled settings for evaluating language-mediated economic interaction among multiple agents. We introduce AgenticPay, a benchmark and simulation framework for multi-agent buyer-seller negotiation driven by natural language. AgenticPay models markets in which buyers and sellers possess private constraints and product-dependent valuations, and must reach agreements through multi-round linguistic negotiation rather than numeric bidding alone. The framework supports a diverse suite of over 110 tasks ranging from bilateral bargaining to many-to-many markets, with structured action extraction and metrics for feasibility, efficiency, and welfare. Benchmarking state-of-the-art proprietary and open-weight LLMs reveals substantial gaps in negotiation performance and highlights challenges in long-horizon strategic reasoning, establishing AgenticPay as a foundation for studying agentic commerce and language-based market interaction. Code and dataset are available at the link: https://github.com/SafeRL-Lab/AgenticPay.

</details>


### 23. Agent2Agent Threats in Safety-Critical LLM Assistants: A Human-Centric Taxonomy

- **Authors:** Lukas Stappen, Ahmet Erkan Turan, Johann Hagerer, Georg Groh
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05877v1](http://arxiv.org/abs/2602.05877v1)
- **PDF:** [https://arxiv.org/pdf/2602.05877v1](https://arxiv.org/pdf/2602.05877v1)
- **Categories:** cs.AI, cs.HC


> The paper presents a novel threat modeling framework, AgentHeLLM, aimed at addressing security challenges posed by Large Language Model (LLM)-based conversational agents in vehicles, where inter-agent communication can lead to severe safety risks. The methodology includes a human-centric taxonomy for asset identification based on victim modeling and a formal graph-based model that differentiates between various attack paths, such as poison paths and trigger paths. Key findings highlight the framework's ability to improve safety by formally separating asset protection from attack analysis, as validated by the development of the AgentHeLLM Attack Path Generator, which automates multi-stage threat discovery.


<details>
<summary>Abstract</summary>

The integration of Large Language Model (LLM)-based conversational agents into vehicles creates novel security challenges at the intersection of agentic AI, automotive safety, and inter-agent communication. As these intelligent assistants coordinate with external services via protocols such as Google's Agent-to-Agent (A2A), they establish attack surfaces where manipulations can propagate through natural language payloads, potentially causing severe consequences ranging from driver distraction to unauthorized vehicle control. Existing AI security frameworks, while foundational, lack the rigorous "separation of concerns" standard in safety-critical systems engineering by co-mingling the concepts of what is being protected (assets) with how it is attacked (attack paths). This paper addresses this methodological gap by proposing a threat modeling framework called AgentHeLLM (Agent Hazard Exploration for LLM Assistants) that formally separates asset identification from attack path analysis. We introduce a human-centric asset taxonomy derived from harm-oriented "victim modeling" and inspired by the Universal Declaration of Human Rights, and a formal graph-based model that distinguishes poison paths (malicious data propagation) from trigger paths (activation actions). We demonstrate the framework's practical applicability through an open-source attack path suggestion tool AgentHeLLM Attack Path Generator that automates multi-stage threat discovery using a bi-level search strategy.

</details>


### 24. OdysseyArena: Benchmarking Large Language Models For Long-Horizon, Active and Inductive Interactions

- **Authors:** Fangzhi Xu, Hang Yan, Qiushi Sun, Jinyang Wu, Zixian Huang, Muye Huang, Jingyang Gong, Zichen Ding, Kanzhi Cheng, Yian Wang, Xinyu Che, Zeyi Sun, Jian Zhang, Zhangyue Yin, Haoran Luo, Xuanjing Huang, Ben Kao, Jun Liu, Qika Lin
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05843v1](http://arxiv.org/abs/2602.05843v1)
- **PDF:** [https://arxiv.org/pdf/2602.05843v1](https://arxiv.org/pdf/2602.05843v1)
- **Categories:** cs.CL


> The paper presents OdysseyArena, a novel benchmarking framework designed to evaluate Large Language Models (LLMs) through long-horizon, active, and inductive interactions, addressing the limitations of existing evaluations that focus on deductive tasks. The authors formalized four interaction primitives and created both OdysseyArena-Lite for standardized benchmarking with 120 tasks and OdysseyArena-Challenge for extreme interaction scenarios, revealing that leading LLMs struggle significantly with inductive tasks and highlighting a critical bottleneck in their ability to achieve autonomous discovery. The findings emphasize the need for a paradigm shift in evaluating agentic AI to enhance long-term strategic capabilities.


<details>
<summary>Abstract</summary>

The rapid advancement of Large Language Models (LLMs) has catalyzed the development of autonomous agents capable of navigating complex environments. However, existing evaluations primarily adopt a deductive paradigm, where agents execute tasks based on explicitly provided rules and static goals, often within limited planning horizons. Crucially, this neglects the inductive necessity for agents to discover latent transition laws from experience autonomously, which is the cornerstone for enabling agentic foresight and sustaining strategic coherence. To bridge this gap, we introduce OdysseyArena, which re-centers agent evaluation on long-horizon, active, and inductive interactions. We formalize and instantiate four primitives, translating abstract transition dynamics into concrete interactive environments. Building upon this, we establish OdysseyArena-Lite for standardized benchmarking, providing a set of 120 tasks to measure an agent's inductive efficiency and long-horizon discovery. Pushing further, we introduce OdysseyArena-Challenge to stress-test agent stability across extreme interaction horizons (e.g., > 200 steps). Extensive experiments on 15+ leading LLMs reveal that even frontier models exhibit a deficiency in inductive scenarios, identifying a critical bottleneck in the pursuit of autonomous discovery in complex environments. Our code and data are available at https://github.com/xufangzhi/Odyssey-Arena

</details>


### 25. Bifrost: Steering Strategic Trajectories to Bridge Contextual Gaps for Self-Improving Agents

- **Authors:** Quan M. Tran, Zhuo Huang, Wenbin Zhang, Bo Han, Koji Yatani, Masashi Sugiyama, Tongliang Liu
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05810v1](http://arxiv.org/abs/2602.05810v1)
- **PDF:** [https://arxiv.org/pdf/2602.05810v1](https://arxiv.org/pdf/2602.05810v1)
- **Categories:** cs.LG


> The paper presents Bifrost, a novel method for improving self-improvement in autonomous agents by addressing the challenge of context mismatches when shifting tasks. By leveraging the revealed correlation between context and task trajectories, Bifrost adapts successful previous trajectories without the need for fine-tuning, facilitating a more effective alignment with target tasks using agent hidden states. The key findings indicate that Bifrost outperforms traditional trajectory reuse and fine-tuning approaches across various benchmarks, showcasing its potential for enhancing agent performance despite significant changes in context.


<details>
<summary>Abstract</summary>

Autonomous agents excel in self-improvement through reflection and iterative refinement, which reuse successful task trajectories as in-context examples to assist subsequent reasoning. However, shifting across tasks often introduces a context mismatch. Hence, existing approaches either discard the trajectories or manipulate them using heuristics, leading to a non-negligible fine-tuning cost or unguaranteed performance. To bridge this gap, we reveal a context-trajectory correlation, where shifts of context are highly parallel with shifts of trajectory. Based on this finding, we propose BrIdge contextual gap FoR imprOvised trajectory STeering (Bifrost), a training-free method that leverages context differences to precisely guide the adaptation of previously solved trajectories towards the target task, mitigating the misalignment caused by context shifts. Our trajectory adaptation is conducted at the representation level using agent hidden states, ensuring trajectory transformation accurately aligns with the target context in a shared space. Across diverse benchmarks, Bifrost consistently outperforms existing trajectory reuse and finetuned self-improvement methods, demonstrating that agents can effectively leverage past experiences despite substantial context shifts.

</details>


### 26. RocqSmith: Can Automatic Optimization Forge Better Proof Agents?

- **Authors:** Andrei Kozyrev, Nikita Khramov, Denis Lochmelis, Valerio Morelli, Gleb Solovev, Anton Podkopaev
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05762v1](http://arxiv.org/abs/2602.05762v1)
- **PDF:** [https://arxiv.org/pdf/2602.05762v1](https://arxiv.org/pdf/2602.05762v1)
- **Categories:** cs.AI, cs.LG, cs.LO, cs.SE


> The paper "RocqSmith" investigates the use of automatic optimization techniques to enhance proof agents used in formal verification, specifically focusing on automated theorem proving with Rocq. Through the evaluation of various optimization methods, including prompt design and control strategies, the authors discover that while some optimizers lead to notable improvements in performance, simple few-shot bootstrapping proves to be the most effective; nevertheless, none of the optimizers achieve the performance levels of a well-engineered proof agent. This work contributes to the field of agentic AI by highlighting the challenges and limitations of automating the optimization of AI agents in complex real-world tasks.


<details>
<summary>Abstract</summary>

This work studies the applicability of automatic AI agent optimization methods to real-world agents in formal verification settings, focusing on automated theorem proving in Rocq as a representative and challenging domain. We evaluate how different automatic agent optimizers perform when applied to the task of optimizing a Rocq proof-generation agent, and assess whether parts of the fine-grained tuning of agentic systems, such as prompt design, contextual knowledge, and control strategies, can be automated. Our results show that while several optimizers yield measurable improvements, simple few-shot bootstrapping is the most consistently effective; however, none of the studied methods matches the performance of a carefully engineered state-of-the-art proof agent.

</details>


### 27. Learning to Inject: Automated Prompt Injection via Reinforcement Learning

- **Authors:** Xin Chen, Jie Zhang, Florian Tramer
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05746v1](http://arxiv.org/abs/2602.05746v1)
- **PDF:** [https://arxiv.org/pdf/2602.05746v1](https://arxiv.org/pdf/2602.05746v1)
- **Categories:** cs.LG, cs.AI


> The paper presents AutoInject, a reinforcement learning-based framework designed to automate prompt injection attacks on large language models (LLMs), addressing the limitations of previous methods that rely on human intervention and handcrafted prompts. The methodology involves generating universal adversarial suffixes while optimizing for both attack success and utility preservation in benign tasks, enabling effective query-based optimization and transfer attacks on unseen models. Key findings reveal that AutoInject successfully compromises state-of-the-art systems, including GPT 5 Nano and Claude Sonnet 3.5, establishing a new baseline for research in automated prompt injection within the agentic AI field.


<details>
<summary>Abstract</summary>

Prompt injection is one of the most critical vulnerabilities in LLM agents; yet, effective automated attacks remain largely unexplored from an optimization perspective. Existing methods heavily depend on human red-teamers and hand-crafted prompts, limiting their scalability and adaptability. We propose AutoInject, a reinforcement learning framework that generates universal, transferable adversarial suffixes while jointly optimizing for attack success and utility preservation on benign tasks. Our black-box method supports both query-based optimization and transfer attacks to unseen models and tasks. Using only a 1.5B parameter adversarial suffix generator, we successfully compromise frontier systems including GPT 5 Nano, Claude Sonnet 3.5, and Gemini 2.5 Flash on the AgentDojo benchmark, establishing a stronger baseline for automated prompt injection research.

</details>


### 28. Generative Ontology: When Structured Knowledge Learns to Create

- **Authors:** Benny Cheung
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05636v1](http://arxiv.org/abs/2602.05636v1)
- **PDF:** [https://arxiv.org/pdf/2602.05636v1](https://arxiv.org/pdf/2602.05636v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces Generative Ontology, a novel framework that integrates structured domain knowledge with the creative capabilities of large language models (LLMs) to generate coherent and novel artifacts. Employing executable Pydantic schemas and a multi-agent system that assigns specialized roles, it ensures that generated outputs adhere to ontological constraints while maintaining creativity. Demonstrated through the GameGrammar system, the framework successfully produces complete tabletop game designs that feature well-structured mechanisms, components, and victory conditions, suggesting that such an approach can generalize to various domains, thus enhancing the field of agentic AI by showing how structure can facilitate creativity.


<details>
<summary>Abstract</summary>

Traditional ontologies excel at describing domain structure but cannot generate novel artifacts. Large language models generate fluently but produce outputs that lack structural validity, hallucinating mechanisms without components, goals without end conditions. We introduce Generative Ontology, a framework that synthesizes these complementary strengths: ontology provides the grammar; the LLM provides the creativity.
  Generative Ontology encodes domain knowledge as executable Pydantic schemas that constrain LLM generation via DSPy signatures. A multi-agent pipeline assigns specialized roles to different ontology domains: a Mechanics Architect designs game systems, a Theme Weaver integrates narrative, a Balance Critic identifies exploits. Each agent carrying a professional "anxiety" that prevents shallow, agreeable outputs. Retrieval-augmented generation grounds novel designs in precedents from existing exemplars, while iterative validation ensures coherence between mechanisms and components.
  We demonstrate the framework through GameGrammar, a system for generating complete tabletop game designs. Given a thematic prompt ("bioluminescent fungi competing in a cave ecosystem"), the pipeline produces structurally complete, playable game specifications with mechanisms, components, victory conditions, and setup instructions. These outputs satisfy ontological constraints while remaining genuinely creative.
  The pattern generalizes beyond games. Any domain with expert vocabulary, validity constraints, and accumulated exemplars (music composition, software architecture, culinary arts) is a candidate for Generative Ontology. We argue that constraints do not limit creativity but enable it: just as grammar makes poetry possible, ontology makes structured generation possible.

</details>


### 29. Reactive Knowledge Representation and Asynchronous Reasoning

- **Authors:** Simon Kohaut, Benedict Flade, Julian Eggert, Kristian Kersting, Devendra Singh Dhami
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05625v1](http://arxiv.org/abs/2602.05625v1)
- **PDF:** [https://arxiv.org/pdf/2602.05625v1](https://arxiv.org/pdf/2602.05625v1)
- **Categories:** cs.AI


> The paper introduces Resin (Reactive Signal Inference), a novel probabilistic programming language designed to enhance real-time belief updates for autonomous agents in dynamic environments by combining probabilistic logic with reactive programming. The key contribution is the formulation of Reactive Circuits (RCs), which are time-dynamic Directed Acyclic Graphs that efficiently adapt to the varying update rates of input signals, thereby enabling significant speed improvements in inference processes. The methodology is tested in high-fidelity drone swarm simulations, demonstrating substantial reductions in computation cost and latency while facilitating effective reactive reasoning in response to environmental changes.


<details>
<summary>Abstract</summary>

Exact inference in complex probabilistic models often incurs prohibitive computational costs. This challenge is particularly acute for autonomous agents in dynamic environments that require frequent, real-time belief updates. Existing methods are often inefficient for ongoing reasoning, as they re-evaluate the entire model upon any change, failing to exploit that real-world information streams have heterogeneous update rates. To address this, we approach the problem from a reactive, asynchronous, probabilistic reasoning perspective. We first introduce Resin (Reactive Signal Inference), a probabilistic programming language that merges probabilistic logic with reactive programming. Furthermore, to provide efficient and exact semantics for Resin, we propose Reactive Circuits (RCs). Formulated as a meta-structure over Algebraic Circuits and asynchronous data streams, RCs are time-dynamic Directed Acyclic Graphs that autonomously adapt themselves based on the volatility of input signals. In high-fidelity drone swarm simulations, our approach achieves several orders of magnitude of speedup over frequency-agnostic inference. We demonstrate that RCs' structural adaptations successfully capture environmental dynamics, significantly reducing latency and facilitating reactive real-time reasoning. By partitioning computations based on the estimated Frequency of Change in the asynchronous inputs, large inference tasks can be decomposed into individually memoized sub-problems. This ensures that only the specific components of a model affected by new information are re-evaluated, drastically reducing redundant computation in streaming contexts.

</details>


### 30. AI Agent Systems for Supply Chains: Structured Decision Prompts and Memory Retrieval

- **Authors:** Konosuke Yoshizato, Kazuma Shimizu, Ryota Higa, Takanobu Otsuka
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05524v1](http://arxiv.org/abs/2602.05524v1)
- **PDF:** [https://arxiv.org/pdf/2602.05524v1](https://arxiv.org/pdf/2602.05524v1)
- **Categories:** cs.MA, cs.AI


> The paper presents a significant advancement in the application of large language model (LLM)-based multi-agent systems (MASs) for inventory management within supply chains. It employs a fixed-ordering strategy prompt combined with a novel agent called AIM-RM that utilizes historical experience for improved adaptability in decision-making. The findings reveal that AIM-RM consistently outperforms traditional methods in diverse supply chain contexts, demonstrating its effectiveness in deriving optimal ordering policies and adapting to varying scenarios.


<details>
<summary>Abstract</summary>

This study investigates large language model (LLM) -based multi-agent systems (MASs) as a promising approach to inventory management, which is a key component of supply chain management. Although these systems have gained considerable attention for their potential to address the challenges associated with typical inventory management methods, key uncertainties regarding their effectiveness persist. Specifically, it is unclear whether LLM-based MASs can consistently derive optimal ordering policies and adapt to diverse supply chain scenarios. To address these questions, we examine an LLM-based MAS with a fixed-ordering strategy prompt that encodes the stepwise processes of the problem setting and a safe-stock strategy commonly used in inventory management. Our empirical results demonstrate that, even without detailed prompt adjustments, an LLM-based MAS can determine optimal ordering decisions in a restricted scenario. To enhance adaptability, we propose a novel agent called AIM-RM, which leverages similar historical experiences through similarity matching. Our results show that AIM-RM outperforms benchmark methods across various supply chain scenarios, highlighting its robustness and adaptability.

</details>


### 31. Structured Context Engineering for File-Native Agentic Systems: Evaluating Schema Accuracy, Format Effectiveness, and Multi-File Navigation at Scale

- **Authors:** Damon McMillan
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05447v1](http://arxiv.org/abs/2602.05447v1)
- **PDF:** [https://arxiv.org/pdf/2602.05447v1](https://arxiv.org/pdf/2602.05447v1)
- **Categories:** cs.CL, cs.AI


> The paper presents a systematic study on structured context engineering for file-native agentic systems, focusing on SQL generation as a proxy for programmatic operations across 9,649 experiments with various models and formats. The main contributions highlight that model capability significantly impacts performance, with frontier models outperforming open-source ones by 21 percentage points in accuracy, while format choice shows minimal overall effect. Additionally, the research reveals that file-native agents can effectively scale with large schemas and emphasizes the need for tailored architectural decisions based on specific model characteristics, rather than relying on generalized practices.


<details>
<summary>Abstract</summary>

Large Language Model agents increasingly operate external systems through programmatic interfaces, yet practitioners lack empirical guidance on how to structure the context these agents consume. Using SQL generation as a proxy for programmatic agent operations, we present a systematic study of context engineering for structured data, comprising 9,649 experiments across 11 models, 4 formats (YAML, Markdown, JSON, Token-Oriented Object Notation [TOON]), and schemas ranging from 10 to 10,000 tables.
  Our findings challenge common assumptions. First, architecture choice is model-dependent: file-based context retrieval improves accuracy for frontier-tier models (Claude, GPT, Gemini; +2.7%, p=0.029) but shows mixed results for open source models (aggregate -7.7%, p<0.001), with deficits varying substantially by model. Second, format does not significantly affect aggregate accuracy (chi-squared=2.45, p=0.484), though individual models, particularly open source, exhibit format-specific sensitivities. Third, model capability is the dominant factor, with a 21 percentage point accuracy gap between frontier and open source tiers that dwarfs any format or architecture effect. Fourth, file-native agents scale to 10,000 tables through domain-partitioned schemas while maintaining high navigation accuracy. Fifth, file size does not predict runtime efficiency: compact formats can consume significantly more tokens at scale due to format-unfamiliar search patterns.
  These findings provide practitioners with evidence-based guidance for deploying LLM agents on structured systems, demonstrating that architectural decisions should be tailored to model capability rather than assuming universal best practices.

</details>


### 32. M$^2$-Miner: Multi-Agent Enhanced MCTS for Mobile GUI Agent Data Mining

- **Authors:** Rui Lv, Juncheng Mo, Tianyi Chu, Chen Rao, Hongyi Jing, Jiajie Teng, Jiafu Chen, Shiqi Zhang, Liangzi Ding, Shuo Fang, Huaizhong Lin, Ziqiang Dang, Chenguang Ma, Lei Zhao
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05429v1](http://arxiv.org/abs/2602.05429v1)
- **PDF:** [https://arxiv.org/pdf/2602.05429v1](https://arxiv.org/pdf/2602.05429v1)
- **Categories:** cs.AI, cs.CV


> The paper presents M$^2$-Miner, a novel low-cost automated framework for mobile GUI agent data mining that employs Monte Carlo Tree Search (MCTS) and addresses critical challenges in previous methods, such as high construction costs and poor data quality. Utilizing a collaborative multi-agent system—comprising InferAgent, OrchestraAgent, and JudgeAgent—along with an intent recycling strategy and a progressive training approach, M$^2$-Miner significantly enhances data quality and diversity. Experimental results show that GUI agents fine-tuned with data from M$^2$-Miner achieve state-of-the-art performance on various benchmarks, marking a substantial contribution to the field of agentic AI.


<details>
<summary>Abstract</summary>

Graphical User Interface (GUI) agent is pivotal to advancing intelligent human-computer interaction paradigms. Constructing powerful GUI agents necessitates the large-scale annotation of high-quality user-behavior trajectory data (i.e., intent-trajectory pairs) for training. However, manual annotation methods and current GUI agent data mining approaches typically face three critical challenges: high construction cost, poor data quality, and low data richness. To address these issues, we propose M$^2$-Miner, the first low-cost and automated mobile GUI agent data-mining framework based on Monte Carlo Tree Search (MCTS). For better data mining efficiency and quality, we present a collaborative multi-agent framework, comprising InferAgent, OrchestraAgent, and JudgeAgent for guidance, acceleration, and evaluation. To further enhance the efficiency of mining and enrich intent diversity, we design an intent recycling strategy to extract extra valuable interaction trajectories. Additionally, a progressive model-in-the-loop training strategy is introduced to improve the success rate of data mining. Extensive experiments have demonstrated that the GUI agent fine-tuned using our mined data achieves state-of-the-art performance on several commonly used mobile GUI benchmarks. Our work will be released to facilitate the community research.

</details>


### 33. H-AdminSim: A Multi-Agent Simulator for Realistic Hospital Administrative Workflows with FHIR Integration

- **Authors:** Jun-Min Lee, Meong Hi Son, Edward Choi
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05407v1](http://arxiv.org/abs/2602.05407v1)
- **PDF:** [https://arxiv.org/pdf/2602.05407v1](https://arxiv.org/pdf/2602.05407v1)
- **Categories:** cs.AI, cs.CL


> The paper presents H-AdminSim, a multi-agent simulation framework designed to capture the complexity of hospital administrative workflows by integrating realistic data generation and FHIR standards. Methodologically, it employs detailed rubrics for quantitative evaluation, facilitating systematic comparisons of LLM-based automation approaches in diverse hospital environments. Key findings indicate that H-AdminSim serves as a standardized testbed for assessing the feasibility and performance of LLM-driven automation in hospital administration, addressing the limitations of prior research that focused primarily on patient-physician interactions.


<details>
<summary>Abstract</summary>

Hospital administration departments handle a wide range of operational tasks and, in large hospitals, process over 10,000 requests per day, driving growing interest in LLM-based automation. However, prior work has focused primarily on patient--physician interactions or isolated administrative subtasks, failing to capture the complexity of real administrative workflows. To address this gap, we propose H-AdminSim, a comprehensive end-to-end simulation framework that combines realistic data generation with multi-agent-based simulation of hospital administrative workflows. These tasks are quantitatively evaluated using detailed rubrics, enabling systematic comparison of LLMs. Through FHIR integration, H-AdminSim provides a unified and interoperable environment for testing administrative workflows across heterogeneous hospital settings, serving as a standardized testbed for assessing the feasibility and performance of LLM-driven administrative automation.

</details>


### 34. Spider-Sense: Intrinsic Risk Sensing for Efficient Agent Defense with Hierarchical Adaptive Screening

- **Authors:** Zhenxiong Yu, Zhi Yang, Zhiheng Jin, Shuhe Wang, Heng Zhang, Yanlin Fei, Lingfeng Zeng, Fangqi Lou, Shuo Zhang, Tu Hu, Jingping Liu, Rongze Chen, Xingyu Zhu, Kunyi Wang, Chaofa Yuan, Xin Guo, Zhaowei Liu, Feipeng Zhang, Jie Huang, Huacan Wang, Ronghao Chen, Liwen Zhang
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05386v2](http://arxiv.org/abs/2602.05386v2)
- **PDF:** [https://arxiv.org/pdf/2602.05386v2](https://arxiv.org/pdf/2602.05386v2)
- **Categories:** cs.CR, cs.AI


> The paper presents the Spider-Sense framework, which introduces Intrinsic Risk Sensing (IRS) for enhancing security in autonomous agents, addressing the limitations of mandatory checking paradigms in agent defenses. By adopting an event-driven, hierarchical defense mechanism, Spider-Sense allows agents to selectively trigger defenses based on risk perception; it efficiently resolves known threats through lightweight matching while handling ambiguous cases with deeper reasoning. The evaluation using the S$^2$Bench benchmark demonstrates that Spider-Sense significantly reduces the Attack Success Rate (ASR) and False Positive Rate (FPR), with minimal latency overhead, showcasing its potential for improving agent security in AI applications.


<details>
<summary>Abstract</summary>

As large language models (LLMs) evolve into autonomous agents, their real-world applicability has expanded significantly, accompanied by new security challenges. Most existing agent defense mechanisms adopt a mandatory checking paradigm, in which security validation is forcibly triggered at predefined stages of the agent lifecycle. In this work, we argue that effective agent security should be intrinsic and selective rather than architecturally decoupled and mandatory. We propose Spider-Sense framework, an event-driven defense framework based on Intrinsic Risk Sensing (IRS), which allows agents to maintain latent vigilance and trigger defenses only upon risk perception. Once triggered, the Spider-Sense invokes a hierarchical defence mechanism that trades off efficiency and precision: it resolves known patterns via lightweight similarity matching while escalating ambiguous cases to deep internal reasoning, thereby eliminating reliance on external models. To facilitate rigorous evaluation, we introduce S$^2$Bench, a lifecycle-aware benchmark featuring realistic tool execution and multi-stage attacks. Extensive experiments demonstrate that Spider-Sense achieves competitive or superior defense performance, attaining the lowest Attack Success Rate (ASR) and False Positive Rate (FPR), with only a marginal latency overhead of 8.3\%.

</details>


### 35. A Data Driven Structural Decomposition of Dynamic Games via Best Response Maps

- **Authors:** Mahdis Rabbani, Navid Mojahed, Shima Nazari
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05324v1](http://arxiv.org/abs/2602.05324v1)
- **PDF:** [https://arxiv.org/pdf/2602.05324v1](https://arxiv.org/pdf/2602.05324v1)
- **Categories:** cs.GT, cs.MA, cs.RO, eess.SY, math.OC


> This paper presents a novel approach to computing equilibria in dynamic games by employing a data-driven structural decomposition method that utilizes a best-response map as a feasibility constraint, thereby avoiding the complexity of traditional joint game solutions and the decoupling of agents' interactions. The methodology involves embedding this best-response map into the optimization process, which allows the researchers to derive a local open-loop Nash equilibrium under standard conditions, with convergence guarantees when using an exact best-response operator. Key findings from the Monte Carlo study demonstrate that this approach outperforms existing joint game solvers in terms of solution quality, computational efficiency, and satisfaction of constraints, highlighting its potential to enhance decision-making in multi-agent systems relevant to agentic AI applications.


<details>
<summary>Abstract</summary>

Dynamic games are powerful tools to model multi-agent decision-making, yet computing Nash (generalized Nash) equilibria remains a central challenge in such settings. Complexity arises from tightly coupled optimality conditions, nested optimization structures, and poor numerical conditioning. Existing game-theoretic solvers address these challenges by directly solving the joint game, typically requiring explicit modeling of all agents' objective functions and constraints, while learning-based approaches often decouple interaction through prediction or policy approximation, sacrificing equilibrium consistency. This paper introduces a conceptually novel formulation for dynamic games by restructuring the equilibrium computation. Rather than solving a fully coupled game or decoupling agents through prediction or policy approximation, a data-driven structural reduction of the game is proposed that removes nested optimization layers and derivative coupling by embedding an offline-compiled best-response map as a feasibility constraint. Under standard regularity conditions, when the best-response operator is exact, any converged solution of the reduced problem corresponds to a local open-loop Nash (GNE) equilibrium of the original game; with a learned surrogate, the solution is approximately equilibrium-consistent up to the best-response approximation error. The proposed formulation is supported by mathematical proofs, accompanying a large-scale Monte Carlo study in a two-player open-loop dynamic game motivated by the autonomous racing problem. Comparisons are made against state-of-the-art joint game solvers, and results are reported on solution quality, computational cost, and constraint satisfaction.

</details>


### 36. PieArena: Frontier Language Agents Achieve MBA-Level Negotiation Performance and Reveal Novel Behavioral Differences

- **Authors:** Chris Zhu, Sasha Cui, Will Sanok Dufallo, Runzhi Jin, Zhen Xu, Linjun Zhang, Daylian Cain
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05302v1](http://arxiv.org/abs/2602.05302v1)
- **PDF:** [https://arxiv.org/pdf/2602.05302v1](https://arxiv.org/pdf/2602.05302v1)
- **Categories:** cs.AI


> The paper introduces PieArena, a negotiation benchmark designed to evaluate the negotiation capabilities of large language models (LLMs) in realistic scenarios based on an MBA negotiation course. The main contribution is demonstrating that a frontier agent (GPT-5) can achieve negotiation performance comparable to, or better than, trained business students, while revealing novel behavioral differences among various LMs in areas like deception and reputation. Key findings highlight that while frontier LMs exhibit significant negotiation skills, there are ongoing concerns regarding their robustness and trustworthiness in high-stakes economic environments, indicating a need for further development in these areas for agentic AI applications.


<details>
<summary>Abstract</summary>

We present an in-depth evaluation of LLMs' ability to negotiate, a central business task that requires strategic reasoning, theory of mind, and economic value creation. To do so, we introduce PieArena, a large-scale negotiation benchmark grounded in multi-agent interactions over realistic scenarios drawn from an MBA negotiation course at an elite business school. We find systematic evidence of AGI-level performance in which a representative frontier agent (GPT-5) matches or outperforms trained business-school students, despite a semester of general negotiation instruction and targeted coaching immediately prior to the task. We further study the effects of joint-intentionality agentic scaffolding and find asymmetric gains, with large improvements for mid- and lower-tier LMs and diminishing returns for frontier LMs. Beyond deal outcomes, PieArena provides a multi-dimensional negotiation behavioral profile, revealing novel cross-model heterogeneity, masked by deal-outcome-only benchmarks, in deception, computation accuracy, instruction compliance, and perceived reputation. Overall, our results suggest that frontier language agents are already intellectually and psychologically capable of deployment in high-stakes economic settings, but deficiencies in robustness and trustworthiness remain open challenges.

</details>


### 37. Towards a Science of Collective AI: LLM-based Multi-Agent Systems Need a Transition from Blind Trial-and-Error to Rigorous Science

- **Authors:** Jingru Fan, Dewen Liu, Yufan Dang, Huatao Li, Yuheng Wang, Wei Liu, Feiyu Duan, Xuanwen Ding, Shu Yao, Lin Wu, Ruijie Shi, Wai-Shing Leung, Yuan Cheng, Zhongyu Wei, Cheng Yang, Chen Qian, Zhiyuan Liu, Maosong Sun
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05289v1](http://arxiv.org/abs/2602.05289v1)
- **PDF:** [https://arxiv.org/pdf/2602.05289v1](https://arxiv.org/pdf/2602.05289v1)
- **Categories:** cs.CL, cs.AI, cs.MA


> This paper presents a framework aimed at transforming the development of Large Language Model (LLM)-based Multi-Agent Systems (MAS) from an empirical trial-and-error approach to a rigorous scientific methodology. The authors propose the establishment of a collaboration gain metric ($Γ$) to effectively measure genuine collaborative improvements, alongside a factor attribution paradigm to identify key collaboration-driving factors, complemented by a systematic MAS factor library. The key finding emphasizes that adopting this structured approach can enhance the systematic optimization of MAS and contribute to the evolution of Collective AI science.


<details>
<summary>Abstract</summary>

Recent advancements in Large Language Models (LLMs) have greatly extended the capabilities of Multi-Agent Systems (MAS), demonstrating significant effectiveness across a wide range of complex and open-ended domains. However, despite this rapid progress, the field still relies heavily on empirical trial-and-error. It lacks a unified and principled scientific framework necessary for systematic optimization and improvement. This bottleneck stems from the ambiguity of attribution: first, the absence of a structured taxonomy of factors leaves researchers restricted to unguided adjustments; second, the lack of a unified metric fails to distinguish genuine collaboration gain from mere resource accumulation. In this paper, we advocate for a transition to design science through an integrated framework. We advocate to establish the collaboration gain metric ($Γ$) as the scientific standard to isolate intrinsic gains from increased budgets. Leveraging $Γ$, we propose a factor attribution paradigm to systematically identify collaboration-driving factors. To support this, we construct a systematic MAS factor library, structuring the design space into control-level presets and information-level dynamics. Ultimately, this framework facilitates the transition from blind experimentation to rigorous science, paving the way towards a true science of Collective AI.

</details>


### 38. Data-Centric Interpretability for LLM-based Multi-Agent Reinforcement Learning

- **Authors:** John Yan, Michael Yu, Yuqi Sun, Alexander Duffy, Tyler Marques, Matthew Lyle Olson
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05183v2](http://arxiv.org/abs/2602.05183v2)
- **PDF:** [https://arxiv.org/pdf/2602.05183v2](https://arxiv.org/pdf/2602.05183v2)
- **Categories:** cs.LG, cs.AI


> This paper presents a novel framework, Meta-Autointerp, which utilizes Sparse Autoencoders (SAEs) and LLM-summarizer methods to enhance data-centric interpretability in large-scale multi-agent reinforcement learning environments, specifically in the context of Full-Press Diplomacy. The methodology involves analyzing training dynamics and extracting interpretable hypotheses about agent behaviors, uncovering both fine-grained and high-level behavioral patterns, while also highlighting issues like reward hacking and limitations in the utility of certain features for human understanding. Key findings indicate that while many SAE-derived features are significant, their practical usefulness is variable, and improvements in an untrained agent's performance were achieved through targeted augmentation, thereby underscoring the potential of SAEs and LLM-summarizers in agential AI interpretation and trustworthiness assessment.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly trained in complex Reinforcement Learning, multi-agent environments, making it difficult to understand how behavior changes over training. Sparse Autoencoders (SAEs) have recently shown to be useful for data-centric interpretability. In this work, we analyze large-scale reinforcement learning training runs from the sophisticated environment of Full-Press Diplomacy by applying pretrained SAEs, alongside LLM-summarizer methods. We introduce Meta-Autointerp, a method for grouping SAE features into interpretable hypotheses about training dynamics. We discover fine-grained behaviors including role-playing patterns, degenerate outputs, language switching, alongside high-level strategic behaviors and environment-specific bugs. Through automated evaluation, we validate that 90% of discovered SAE Meta-Features are significant, and find a surprising reward hacking behavior. However, through two user studies, we find that even subjectively interesting and seemingly helpful SAE features may be worse than useless to humans, along with most LLM generated hypotheses. However, a subset of SAE-derived hypotheses are predictively useful for downstream tasks. We further provide validation by augmenting an untrained agent's system prompt, improving the score by +14.2%. Overall, we show that SAEs and LLM-summarizer provide complementary views into agent behavior, and together our framework forms a practical starting point for future data-centric interpretability work on ensuring trustworthy LLM behavior throughout training.

</details>


### 39. Among Us: Measuring and Mitigating Malicious Contributions in Model Collaboration Systems

- **Authors:** Ziyuan Yang, Wenxuan Ding, Shangbin Feng, Yulia Tsvetkov
- **Published:** 2026-02-05
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05176v1](http://arxiv.org/abs/2602.05176v1)
- **PDF:** [https://arxiv.org/pdf/2602.05176v1](https://arxiv.org/pdf/2602.05176v1)
- **Categories:** cs.CL


> The paper presents a comprehensive examination of the risks posed by malicious language models (LMs) in collaborative model systems, where multiple LMs may interact. The authors methodically categorize four types of malicious LMs and assess their detrimental effects across various collaboration configurations, revealing an average performance drop of 7.12% in reasoning tasks and 7.94% in safety-related tasks. To address these challenges, they propose external supervisory strategies that significantly mitigate the negative impact of malicious models, restoring approximately 95.31% of initial performance, while acknowledging that fully shielding model collaboration from such threats remains a critical area for future research in the agentic AI field.


<details>
<summary>Abstract</summary>

Language models (LMs) are increasingly used in collaboration: multiple LMs trained by different parties collaborate through routing systems, multi-agent debate, model merging, and more. Critical safety risks remain in this decentralized paradigm: what if some of the models in multi-LLM systems are compromised or malicious? We first quantify the impact of malicious models by engineering four categories of malicious LMs, plug them into four types of popular model collaboration systems, and evaluate the compromised system across 10 datasets. We find that malicious models have a severe impact on the multi-LLM systems, especially for reasoning and safety domains where performance is lowered by 7.12% and 7.94% on average. We then propose mitigation strategies to alleviate the impact of malicious components, by employing external supervisors that oversee model collaboration to disable/mask them out to reduce their influence. On average, these strategies recover 95.31% of the initial performance, while making model collaboration systems fully resistant to malicious models remains an open research question.

</details>


### 40. SocialVeil: Probing Social Intelligence of Language Agents under Communication Barriers

- **Authors:** Keyang Xuan, Pengda Wang, Chongrui Ye, Haofei Yu, Tal August, Jiaxuan You
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05115v1](http://arxiv.org/abs/2602.05115v1)
- **PDF:** [https://arxiv.org/pdf/2602.05115v1](https://arxiv.org/pdf/2602.05115v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces **SocialVeil**, a novel social learning environment designed to assess the social intelligence of language agents under realistic communication barriers, such as semantic vagueness, sociocultural mismatch, and emotional interference. The methodology includes a systematic literature review to identify communication challenges and the development of two new metrics—unresolved confusion and mutual understanding—to evaluate interaction quality under these conditions. Key findings reveal that the presence of communication barriers significantly hinders the performance of large language models, with mutual understanding dropping by over 45% and unresolved confusion increasing by nearly 50%, highlighting the need for more realistic evaluation environments in the study of agentic AI.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly evaluated in interactive environments to test their social intelligence. However, existing benchmarks often assume idealized communication between agents, limiting our ability to diagnose whether LLMs can maintain and repair interactions in more realistic, imperfect settings. To close this gap, we present \textsc{SocialVeil}, a social learning environment that can simulate social interaction under cognitive-difference-induced communication barriers. Grounded in a systematic literature review of communication challenges in human interaction, \textsc{SocialVeil} introduces three representative types of such disruption, \emph{semantic vagueness}, \emph{sociocultural mismatch}, and \emph{emotional interference}. We also introduce two barrier-aware evaluation metrics, \emph{unresolved confusion} and \emph{mutual understanding}, to evaluate interaction quality under impaired communication. Experiments across 720 scenarios and four frontier LLMs show that barriers consistently impair performance, with mutual understanding reduced by over 45\% on average, and confusion elevated by nearly 50\%. Human evaluations validate the fidelity of these simulated barriers (ICC$\approx$0.78, Pearson r$\approx$0.80). We further demonstrate that adaptation strategies (Repair Instruction and Interactive learning) only have a modest effect far from barrier-free performance. This work takes a step toward bringing social interaction environments closer to real-world communication, opening opportunities for exploring the social intelligence of LLM agents.

</details>


### 41. GAMMS: Graph based Adversarial Multiagent Modeling Simulator

- **Authors:** Rohan Patil, Jai Malegaonkar, Xiao Jiang, Andre Dion, Gaurav S. Sukhatme, Henrik I. Christensen
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05105v1](http://arxiv.org/abs/2602.05105v1)
- **PDF:** [https://arxiv.org/pdf/2602.05105v1](https://arxiv.org/pdf/2602.05105v1)
- **Categories:** cs.AI, cs.RO, cs.SE


> The paper presents GAMMS (Graph based Adversarial Multiagent Modeling Simulator), a scalable and accessible simulation framework designed to facilitate the development and evaluation of agent behaviors in graph-representable environments. The methodology focuses on providing a lightweight, extensible architecture that supports various agent types—including heuristic, optimization-based, and learning-based—while emphasizing rapid visualization and compatibility with external tools. Key findings indicate that GAMMS significantly lowers the barrier for researchers working in the fields of multi-agent systems and autonomous planning, thereby fostering innovation and experimentation in agentic AI applications.


<details>
<summary>Abstract</summary>

As intelligent systems and multi-agent coordination become increasingly central to real-world applications, there is a growing need for simulation tools that are both scalable and accessible. Existing high-fidelity simulators, while powerful, are often computationally expensive and ill-suited for rapid prototyping or large-scale agent deployments. We present GAMMS (Graph based Adversarial Multiagent Modeling Simulator), a lightweight yet extensible simulation framework designed to support fast development and evaluation of agent behavior in environments that can be represented as graphs. GAMMS emphasizes five core objectives: scalability, ease of use, integration-first architecture, fast visualization feedback, and real-world grounding. It enables efficient simulation of complex domains such as urban road networks and communication systems, supports integration with external tools (e.g., machine learning libraries, planning solvers), and provides built-in visualization with minimal configuration. GAMMS is agnostic to policy type, supporting heuristic, optimization-based, and learning-based agents, including those using large language models. By lowering the barrier to entry for researchers and enabling high-performance simulations on standard hardware, GAMMS facilitates experimentation and innovation in multi-agent systems, autonomous planning, and adversarial modeling. The framework is open-source and available at https://github.com/GAMMSim/GAMMS/

</details>


### 42. Towards Reducible Uncertainty Modeling for Reliable Large Language Model Agents

- **Authors:** Changdae Oh, Seongheon Park, To Eun Kim, Jiatong Li, Wendi Li, Samuel Yeh, Xuefeng Du, Hamed Hassani, Paul Bogdan, Dawn Song, Sharon Li
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05073v1](http://arxiv.org/abs/2602.05073v1)
- **PDF:** [https://arxiv.org/pdf/2602.05073v1](https://arxiv.org/pdf/2602.05073v1)
- **Categories:** cs.AI


> The paper introduces a novel framework for uncertainty quantification (UQ) in large language model (LLM) agents, addressing the limitations of existing UQ research that predominantly focuses on single-turn interactions. By framing UQ as a conditional uncertainty reduction process instead of an accumulation process, the authors emphasize the importance of interactivity in agent actions. Key findings highlight actionable insights for enhancing safety and reliability in LLM applications, paving the way for more effective design strategies in agentic AI systems.


<details>
<summary>Abstract</summary>

Uncertainty quantification (UQ) for large language models (LLMs) is a key building block for safety guardrails of daily LLM applications. Yet, even as LLM agents are increasingly deployed in highly complex tasks, most UQ research still centers on single-turn question-answering. We argue that UQ research must shift to realistic settings with interactive agents, and that a new principled framework for agent UQ is needed. This paper presents the first general formulation of agent UQ that subsumes broad classes of existing UQ setups. Under this formulation, we show that prior works implicitly treat LLM UQ as an uncertainty accumulation process, a viewpoint that breaks down for interactive agents in an open world. In contrast, we propose a novel perspective, a conditional uncertainty reduction process, that explicitly models reducible uncertainty over an agent's trajectory by highlighting "interactivity" of actions. From this perspective, we outline a conceptual framework to provide actionable guidance for designing UQ in LLM agent setups. Finally, we conclude with practical implications of the agent UQ in frontier LLM development and domain-specific applications, as well as open remaining problems.

</details>


### 43. Bypassing AI Control Protocols via Agent-as-a-Proxy Attacks

- **Authors:** Jafar Isbarov, Murat Kantarcioglu
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05066v1](http://arxiv.org/abs/2602.05066v1)
- **PDF:** [https://arxiv.org/pdf/2602.05066v1](https://arxiv.org/pdf/2602.05066v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces the Agent-as-a-Proxy attack, demonstrating that existing monitoring protocols designed to enforce alignment in AI agents can be effectively bypassed through indirect prompt injection attacks. By evaluating various large-scale models, including Qwen2.5-72B, GPT-4o mini, and Llama-3.1-70B, the authors reveal a significant vulnerability in both agents and their monitoring systems, indicating that even sophisticated oversight mechanisms fail to secure agentic AI processes. The study highlights a critical weakness in current defense strategies, suggesting that they are fundamentally inadequate to ensure robust alignment regardless of the scale of the monitoring model.


<details>
<summary>Abstract</summary>

As AI agents automate critical workloads, they remain vulnerable to indirect prompt injection (IPI) attacks. Current defenses rely on monitoring protocols that jointly evaluate an agent's Chain-of-Thought (CoT) and tool-use actions to ensure alignment with user intent. We demonstrate that these monitoring-based defenses can be bypassed via a novel Agent-as-a-Proxy attack, where prompt injection attacks treat the agent as a delivery mechanism, bypassing both agent and monitor simultaneously. While prior work on scalable oversight has focused on whether small monitors can supervise large agents, we show that even frontier-scale monitors are vulnerable. Large-scale monitoring models like Qwen2.5-72B can be bypassed by agents with similar capabilities, such as GPT-4o mini and Llama-3.1-70B. On the AgentDojo benchmark, we achieve a high attack success rate against AlignmentCheck and Extract-and-Evaluate monitors under diverse monitoring LLMs. Our findings suggest current monitoring-based agentic defenses are fundamentally fragile regardless of model scale.

</details>


### 44. MINT: Minimal Information Neuro-Symbolic Tree for Objective-Driven Knowledge-Gap Reasoning and Active Elicitation

- **Authors:** Zeyu Fang, Tian Lan, Mahdi Imani
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05048v1](http://arxiv.org/abs/2602.05048v1)
- **PDF:** [https://arxiv.org/pdf/2602.05048v1](https://arxiv.org/pdf/2602.05048v1)
- **Categories:** cs.AI, cs.HC


> The paper introduces the Minimal Information Neuro-Symbolic Tree (MINT), a novel approach for AI agents to effectively engage in human-AI collaborative planning by actively eliciting necessary information from humans to address knowledge gaps. MINT employs a symbolic tree structure informed by a neural planning policy to optimize interaction strategies, using self-play to refine potential queries that target specific knowledge gaps. Key findings demonstrate that MINT significantly enhances planning performance, achieving near-expert returns with fewer queries, thereby improving success rates and rewards in object-driven planning scenarios.


<details>
<summary>Abstract</summary>

Joint planning through language-based interactions is a key area of human-AI teaming. Planning problems in the open world often involve various aspects of incomplete information and unknowns, e.g., objects involved, human goals/intents -- thus leading to knowledge gaps in joint planning. We consider the problem of discovering optimal interaction strategies for AI agents to actively elicit human inputs in object-driven planning. To this end, we propose Minimal Information Neuro-Symbolic Tree (MINT) to reason about the impact of knowledge gaps and leverage self-play with MINT to optimize the AI agent's elicitation strategies and queries. More precisely, MINT builds a symbolic tree by making propositions of possible human-AI interactions and by consulting a neural planning policy to estimate the uncertainty in planning outcomes caused by remaining knowledge gaps. Finally, we leverage LLM to search and summarize MINT's reasoning process and curate a set of queries to optimally elicit human inputs for best planning performance. By considering a family of extended Markov decision processes with knowledge gaps, we analyze the return guarantee for a given MINT with active human elicitation. Our evaluation on three benchmarks involving unseen/unknown objects of increasing realism shows that MINT-based planning attains near-expert returns by issuing a limited number of questions per task while achieving significantly improved rewards and success rates.

</details>


### 45. From Fragmentation to Integration: Exploring the Design Space of AI Agents for Human-as-the-Unit Privacy Management

- **Authors:** Eryue Xu, Tianshi Li
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05016v1](http://arxiv.org/abs/2602.05016v1)
- **PDF:** [https://arxiv.org/pdf/2602.05016v1](https://arxiv.org/pdf/2602.05016v1)
- **Categories:** cs.HC, cs.AI, cs.CY, cs.ET


> The paper presents an exploration of AI agents designed for enhancing privacy management from a "human-as-the-unit" perspective, addressing the complexities of users' digital footprints through qualitative interviews and concept evaluations. The methodology involved 12 semi-structured interviews to identify privacy management challenges and a speed-dating survey with 116 participants to assess nine AI agent concepts. Key findings indicate that users prefer AI agents for post-sharing management due to a lack of comprehensive privacy controls and express greater trust in AI's accuracy for privacy management compared to their manual strategies, suggesting a significant opportunity for AI agents to streamline and improve privacy practices.


<details>
<summary>Abstract</summary>

Managing one's digital footprint is overwhelming, as it spans multiple platforms and involves countless context-dependent decisions. Recent advances in agentic AI offer ways forward by enabling holistic, contextual privacy-enhancing solutions. Building on this potential, we adopted a ''human-as-the-unit'' perspective and investigated users' cross-context privacy challenges through 12 semi-structured interviews. Results reveal that people rely on ad hoc manual strategies while lacking comprehensive privacy controls, highlighting nine privacy-management challenges across applications, temporal contexts, and relationships. To explore solutions, we generated nine AI agent concepts and evaluated them via a speed-dating survey with 116 US participants. The three highest-ranked concepts were all post-sharing management tools with half or full agent autonomy, with users expressing greater trust in AI accuracy than in their own efforts. Our findings highlight a promising design space where users see AI agents bridging the fragments in privacy management, particularly through automated, comprehensive post-sharing remediation of users' digital footprints.

</details>


### 46. DeepRead: Document Structure-Aware Reasoning to Enhance Agentic Search

- **Authors:** Zhanli Li, Huiwen Tian, Lvzhou Luo, Yixuan Cao, Ping Luo
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05014v2](http://arxiv.org/abs/2602.05014v2)
- **PDF:** [https://arxiv.org/pdf/2602.05014v2](https://arxiv.org/pdf/2602.05014v2)
- **Categories:** cs.AI, cs.CL, cs.IR


> The paper introduces DeepRead, a structure-aware multi-turn document reasoning agent designed to enhance question answering capabilities for long documents by leveraging document-native priors like hierarchical organization and discourse structure. Utilizing an LLM-based OCR model, DeepRead transforms PDFs into structured Markdown, indexing paragraphs while assigning metadata for effective navigation. Experimental results indicate that DeepRead significantly outperforms traditional search approaches in agentic document querying, demonstrating a human-like "locate then read" reasoning process that combines retrieval and reading tools effectively.


<details>
<summary>Abstract</summary>

With the rapid progress of tool-using and agentic large language models (LLMs), Retrieval-Augmented Generation (RAG) is evolving from one-shot, passive retrieval into multi-turn, decision-driven evidence acquisition. Despite strong results in open-domain settings, existing agentic search frameworks commonly treat long documents as flat collections of chunks, underutilizing document-native priors such as hierarchical organization and sequential discourse structure. We introduce DeepRead, a structure-aware, multi-turn document reasoning agent that explicitly operationalizes these priors for long-document question answering. DeepRead leverages LLM-based OCR model to convert PDFs into structured Markdown that preserves headings and paragraph boundaries. It then indexes documents at the paragraph level and assigns each paragraph a coordinate-style metadata key encoding its section identity and in-section order. Building on this representation, DeepRead equips the LLM with two complementary tools: a Retrieve tool that localizes relevant paragraphs while exposing their structural coordinates (with lightweight scanning context), and a ReadSection tool that enables contiguous, order-preserving reading within a specified section and paragraph range. Our experiments demonstrate that DeepRead achieves significant improvements over Search-o1-style agentic search in document question answering. The synergistic effect between retrieval and reading tools is also validated. Our fine-grained behavioral analysis reveals a reading and reasoning paradigm resembling human-like ``locate then read'' behavior.

</details>


### 47. CoWork-X: Experience-Optimized Co-Evolution for Multi-Agent Collaboration System

- **Authors:** Zexin Lin, Jiachen Yu, Haoyang Zhang, Yuzhao Li, Zhonghang Li, Yujiu Yang, Junjie Wang, Xiaoqiang Ji
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.05004v1](http://arxiv.org/abs/2602.05004v1)
- **PDF:** [https://arxiv.org/pdf/2602.05004v1](https://arxiv.org/pdf/2602.05004v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces CoWork-X, an innovative co-evolution framework designed for enhancing multi-agent collaboration systems by addressing the dual challenges of real-time coordination and efficient adaptation. Employing a Skill-Agent that utilizes hierarchical task network-based skill retrieval and a post-episode Co-Optimizer for skill consolidation, CoWork-X optimizes agent interactions within a structured skill library. The findings reveal that CoWork-X significantly improves performance in complex environments while effectively minimizing online latency and token consumption, marking a substantial advancement in agentic AI capabilities for cooperative tasks.


<details>
<summary>Abstract</summary>

Large language models are enabling language-conditioned agents in interactive environments, but highly cooperative tasks often impose two simultaneous constraints: sub-second real-time coordination and sustained multi-episode adaptation under a strict online token budget. Existing approaches either rely on frequent in-episode reasoning that induces latency and timing jitter, or deliver post-episode improvements through unstructured text that is difficult to compile into reliable low-cost execution. We propose CoWork-X, an active co-evolution framework that casts peer collaboration as a closed-loop optimization problem across episodes, inspired by fast--slow memory separation. CoWork-X instantiates a Skill-Agent that executes via HTN (hierarchical task network)-based skill retrieval from a structured, interpretable, and compositional skill library, and a post-episode Co-Optimizer that performs patch-style skill consolidation with explicit budget constraints and drift regularization. Experiments in challenging Overcooked-AI-like realtime collaboration benchmarks demonstrate that CoWork-X achieves stable, cumulative performance gains while steadily reducing online latency and token usage.

</details>


### 48. El Agente Quntur: A research collaborator agent for quantum chemistry

- **Authors:** Juan B. Pérez-Sánchez, Yunheng Zou, Jorge A. Campos-Gonzalez-Angulo, Marcel Müller, Ignacio Gustin, Andrew Wang, Han Hao, Tsz Wai Ko, Changhyeok Choi, Eric S. Isbrandt, Mohammad Ghazi Vakili, Hanyong Xu, Chris Crebolder, Varinia Bernales, Alán Aspuru-Guzik
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04850v1](http://arxiv.org/abs/2602.04850v1)
- **PDF:** [https://arxiv.org/pdf/2602.04850v1](https://arxiv.org/pdf/2602.04850v1)
- **Categories:** physics.chem-ph, cs.AI, cs.MA


> The paper presents El Agente Quntur, a multi-agent AI system designed as a research collaborator in quantum chemistry, aiming to make quantum simulations more accessible to chemists beyond experts. Methodologically, Quntur eliminates hard-coded rules, constructs general actions for versatility, and employs guided deep research for integrating quantum-chemical reasoning, while operating within the ORCA software framework. Key findings highlight Quntur's capability to facilitate various computational tasks, interpret scientific literature, and suggest a pathway toward developing fully autonomous research agents in computational chemistry, emphasizing advancements and existing challenges in agentic systems within the field.


<details>
<summary>Abstract</summary>

Quantum chemistry is a foundational enabling tool for the fields of chemistry, materials science, computational biology and others. Despite of its power, the practical application of quantum chemistry simulations remains in the hands of qualified experts due to methodological complexity, software heterogeneity, and the need for informed interpretation of results. To bridge the accessibility gap for these tools and expand their reach to chemists with broader backgrounds, we introduce El Agente Quntur, a hierarchical, multi-agent AI system designed to operate not merely as an automation tool but as a research collaborator for computational quantum chemistry. Quntur was designed following three main strategies: i) elimination of hard-coded procedural policies in favour of reasoning-driven decisions, ii) construction of general and composable actions that facilitate generalization and efficiency, and iii) implementation of guided deep research to integrate abstract quantum-chemical reasoning across subdisciplines and a detailed understanding of the software's internal logic and syntax. Although instantiated in ORCA, these design principles are applicable to research agents more generally and easily expandable to additional quantum chemistry packages and beyond. Quntur supports the full range of calculations available in ORCA 6.0 and reasons over software documentation and scientific literature to plan, execute, adapt, and analyze in silico chemistry experiments following best practices. We discuss the advances and current bottlenecks in agentic systems operating at the research level in computational chemistry, and outline a roadmap toward a fully autonomous end-to-end computational chemistry research agent.

</details>


### 49. El Agente Estructural: An Artificially Intelligent Molecular Editor

- **Authors:** Changhyeok Choi, Yunheng Zou, Marcel Müller, Han Hao, Yeonghun Kang, Juan B. Pérez-Sánchez, Ignacio Gustin, Hanyong Xu, Mohammad Ghazi Vakili, Chris Crebolder, Alán Aspuru-Guzik, Varinia Bernales
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04849v1](http://arxiv.org/abs/2602.04849v1)
- **PDF:** [https://arxiv.org/pdf/2602.04849v1](https://arxiv.org/pdf/2602.04849v1)
- **Categories:** physics.chem-ph, cs.AI, cs.MA


> The paper presents El Agente Estructural, an AI-driven molecular editor that facilitates autonomous chemistry and molecular modeling by leveraging a combination of domain-informed tools and vision-language models to perform three-dimensional geometry manipulation. Rather than relying on traditional generative models, Estructural simulates expert-like manipulation, enabling precise operations such as atomic replacements and stereochemistry control without extensive framework rebuilding. Key findings demonstrate its effectiveness in various applications, including ligand binding and isomer interconversion, highlighting the potential of multimodal reasoning in advancing interactive and context-aware molecular modeling within the agentic AI field.


<details>
<summary>Abstract</summary>

We present El Agente Estructural, a multimodal, natural-language-driven geometry-generation and manipulation agent for autonomous chemistry and molecular modelling. Unlike molecular generation or editing via generative models, Estructural mimics how human experts directly manipulate molecular systems in three dimensions by integrating a comprehensive set of domain-informed tools and vision-language models. This design enables precise control over atomic or functional group replacements, atomic connectivity, and stereochemistry without the need to rebuild extensive core molecular frameworks. Through a series of representative case studies, we demonstrate that Estructural enables chemically meaningful geometry manipulation across a wide range of real-world scenarios. These include site-selective functionalization, ligand binding, ligand exchange, stereochemically controlled structure construction, isomer interconversion, fragment-level structural analysis, image-guided generation of structures from schematic reaction mechanisms, and mechanism-driven geometry generation and modification. These examples illustrate how multimodal reasoning, when combined with specialized geometry-aware tools, supports interactive and context-aware molecular modelling beyond structure generation. Looking forward, the integration of Estructural into El Agente Quntur, an autonomous multi-agent quantum chemistry platform, enhances its capabilities by adding sophisticated tools for the generation and editing of three-dimensional structures.

</details>


### 50. Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing

- **Authors:** Zhaotian Weng, Antonis Antoniades, Deepak Nathani, Zhen Zhang, Xiao Pu, Xin Eric Wang
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04837v1](http://arxiv.org/abs/2602.04837v1)
- **PDF:** [https://arxiv.org/pdf/2602.04837v1](https://arxiv.org/pdf/2602.04837v1)
- **Categories:** cs.AI


> The paper introduces Group-Evolving Agents (GEA), a novel paradigm that enables open-ended self-improvement in AI by allowing a group of agents to share and reuse experiences during their evolutionary process, thereby overcoming limitations of isolated evolution found in previous methods. Methodologically, GEA emphasizes collaborative evolution instead of traditional tree-structured evolution, and it is evaluated against various coding benchmarks, significantly outperforming state-of-the-art self-evolving approaches and rivaling human-designed frameworks. Key findings indicate that GEA effectively transforms early exploratory diversity into sustained performance improvements and demonstrates superior robustness in fixing framework-level bugs compared to conventional self-evolving methods.


<details>
<summary>Abstract</summary>

Open-ended self-improving agents can autonomously modify their own structural designs to advance their capabilities and overcome the limits of pre-defined architectures, thus reducing reliance on human intervention. We introduce Group-Evolving Agents (GEA), a new paradigm for open-ended self-improvements, which treats a group of agents as the fundamental evolutionary unit, enabling explicit experience sharing and reuse within the group throughout evolution. Unlike existing open-ended self-evolving paradigms that adopt tree-structured evolution, GEA overcomes the limitation of inefficient utilization of exploratory diversity caused by isolated evolutionary branches. We evaluate GEA on challenging coding benchmarks, where it significantly outperforms state-of-the-art self-evolving methods (71.0% vs. 56.7% on SWE-bench Verified, 88.3% vs. 68.3% on Polyglot) and matches or exceeds top human-designed agent frameworks (71.8% and 52.0% on two benchmarks, respectively). Analysis reveals that GEA more effectively converts early-stage exploratory diversity into sustained, long-term progress, achieving stronger performance under the same number of evolved agents. Furthermore, GEA exhibits consistent transferability across different coding models and greater robustness, fixing framework-level bugs in 1.4 iterations on average, versus 5 for self-evolving methods.

</details>


### 51. Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents

- **Authors:** Shubham Vatsal, Harsh Dubey, Aditi Singh
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04813v1](http://arxiv.org/abs/2602.04813v1)
- **PDF:** [https://arxiv.org/pdf/2602.04813v1](https://arxiv.org/pdf/2602.04813v1)
- **Categories:** cs.AI, cs.CY


> The paper presents a seven-dimensional taxonomy for evaluating Large Language Model (LLM)-based agents in healthcare, addressing the lack of a unified framework in existing literature. By reviewing 49 studies and applying a systematic methodology with explicit inclusion criteria and a labeling rubric, the authors quantitatively assess the implementation of specific capabilities across various dimensions. Key findings reveal significant asymmetries in agent capabilities, such as high prevalence in External Knowledge Integration but notable deficiencies in interaction patterns and adaptation, emphasizing the need for further development in areas like Treatment Planning and Prescription within the agentic AI field.


<details>
<summary>Abstract</summary>

Large Language Model (LLM)-based agents that plan, use tools and act has begun to shape healthcare and medicine. Reported studies demonstrate competence on various tasks ranging from EHR analysis and differential diagnosis to treatment planning and research workflows. Yet the literature largely consists of overviews which are either broad surveys or narrow dives into a single capability (e.g., memory, planning, reasoning), leaving healthcare work without a common frame. We address this by reviewing 49 studies using a seven-dimensional taxonomy: Cognitive Capabilities, Knowledge Management, Interaction Patterns, Adaptation & Learning, Safety & Ethics, Framework Typology and Core Tasks & Subtasks with 29 operational sub-dimensions. Using explicit inclusion and exclusion criteria and a labeling rubric (Fully Implemented, Partially Implemented, Not Implemented), we map each study to the taxonomy and report quantitative summaries of capability prevalence and co-occurrence patterns. Our empirical analysis surfaces clear asymmetries. For instance, the External Knowledge Integration sub-dimension under Knowledge Management is commonly realized (~76% Fully Implemented) whereas Event-Triggered Activation sub-dimenison under Interaction Patterns is largely absent (~92% Not Implemented) and Drift Detection & Mitigation sub-dimension under Adaptation & Learning is rare (~98% Not Implemented). Architecturally, Multi-Agent Design sub-dimension under Framework Typology is the dominant pattern (~82% Fully Implemented) while orchestration layers remain mostly partial. Across Core Tasks & Subtasks, information centric capabilities lead e.g., Medical Question Answering & Decision Support and Benchmarking & Simulation, while action and discovery oriented areas such as Treatment Planning & Prescription still show substantial gaps (~59% Not Implemented).

</details>


### 52. Communication Enhances LLMs' Stability in Strategic Thinking

- **Authors:** Nunzio Lore, Babak Heydari
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.06081v1](http://arxiv.org/abs/2602.06081v1)
- **PDF:** [https://arxiv.org/pdf/2602.06081v1](https://arxiv.org/pdf/2602.06081v1)
- **Categories:** cs.MA, cs.AI, cs.GT


> The paper presents a significant contribution to the agentic AI field by demonstrating that short, costless pre-play messages can enhance the stability of Large Language Models (LLMs) in multi-agent strategic tasks, specifically in a ten-round Prisoner's Dilemma context. Using advanced statistical methodologies, including simulation-level bootstrap resampling and LOWESS regression, the study shows that communication leads to reduced variability in cooperation trajectories across most model-context combinations, particularly benefiting models with higher baseline volatility. Importantly, the findings suggest that while communication generally improves predictability in strategic behavior, there are specific contexts where it may inadvertently cause instability, highlighting the nuanced role of communication in LLM interactions.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) often exhibit pronounced context-dependent variability that undermines predictable multi-agent behavior in tasks requiring strategic thinking. Focusing on models that range from 7 to 9 billion parameters in size engaged in a ten-round repeated Prisoner's Dilemma, we evaluate whether short, costless pre-play messages emulating the cheap-talk paradigm affect strategic stability. Our analysis uses simulation-level bootstrap resampling and nonparametric inference to compare cooperation trajectories fitted with LOWESS regression across both the messaging and the no-messaging condition. We demonstrate consistent reductions in trajectory noise across a majority of the model-context pairings being studied. The stabilizing effect persists across multiple prompt variants and decoding regimes, though its magnitude depends on model choice and contextual framing, with models displaying higher baseline volatility gaining the most. While communication rarely produces harmful instability, we document a few context-specific exceptions and identify the limited domains in which communication harms stability. These findings position cheap-talk style communication as a low-cost, practical tool for improving the predictability and reliability of strategic behavior in multi-agent LLM systems.

</details>


### 53. Active Asymmetric Multi-Agent Multimodal Learning under Uncertainty

- **Authors:** Rui Liu, Pratap Tokekar, Ming Lin
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04763v1](http://arxiv.org/abs/2602.04763v1)
- **PDF:** [https://arxiv.org/pdf/2602.04763v1](https://arxiv.org/pdf/2602.04763v1)
- **Categories:** cs.LG, cs.AI


> The paper presents Active Asymmetric Multi-Agent Multimodal Learning under Uncertainty (A2MAML), which addresses the limitations of existing frameworks in handling heterogeneous multimodal sensors and uncertainty in multi-agent systems. The methodology involves modeling modality-specific features as stochastic estimates, actively selecting reliable agent-modality pairs, and using Bayesian inverse-variance weighting for information aggregation. Key findings indicate that A2MAML significantly enhances performance in collaborative accident detection scenarios, achieving up to an 18.7% increase in detection rates compared to existing single-agent and collaborative approaches, thereby advancing the robustness and effectiveness of agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent systems are increasingly equipped with heterogeneous multimodal sensors, enabling richer perception but introducing modality-specific and agent-dependent uncertainty. Existing multi-agent collaboration frameworks typically reason at the agent level, assume homogeneous sensing, and handle uncertainty implicitly, limiting robustness under sensor corruption. We propose Active Asymmetric Multi-Agent Multimodal Learning under Uncertainty (A2MAML), a principled approach for uncertainty-aware, modality-level collaboration. A2MAML models each modality-specific feature as a stochastic estimate with uncertainty prediction, actively selects reliable agent-modality pairs, and aggregates information via Bayesian inverse-variance weighting. This formulation enables fine-grained, modality-level fusion, supports asymmetric modality availability, and provides a principled mechanism to suppress corrupted or noisy modalities. Extensive experiments on connected autonomous driving scenarios for collaborative accident detection demonstrate that A2MAML consistently outperforms both single-agent and collaborative baselines, achieving up to 18.7% higher accident detection rate.

</details>


### 54. Supporting software engineering tasks with agentic AI: Demonstration on document retrieval and test scenario generation

- **Authors:** Marian Kica, Lukas Radosky, David Slivka, Karin Kubinova, Daniel Dovhun, Tomas Uhercik, Erik Bircak, Ivan Polasek
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04726v1](http://arxiv.org/abs/2602.04726v1)
- **PDF:** [https://arxiv.org/pdf/2602.04726v1](https://arxiv.org/pdf/2602.04726v1)
- **Categories:** cs.SE, cs.AI


> This paper presents agentic AI solutions aimed at enhancing software engineering tasks, specifically focusing on automatic test scenario generation and document retrieval in software development. The authors employ a star topology of specialized worker agents controlled by a supervisor for test scenario generation and utilize LLM-based agents to manage various document-related use cases, such as search and summarization. Key findings demonstrate the effectiveness of these agentic AI systems in improving the efficiency and capability of software engineering processes.


<details>
<summary>Abstract</summary>

The introduction of large language models ignited great retooling and rethinking of the software development models. The ensuing response of software engineering research yielded a massive body of tools and approaches. In this paper, we join the hassle by introducing agentic AI solutions for two tasks. First, we developed a solution for automatic test scenario generation from a detailed requirements description. This approach relies on specialized worker agents forming a star topology with the supervisor agent in the middle. We demonstrate its capabilities on a real-world example. Second, we developed an agentic AI solution for the document retrieval task in the context of software engineering documents. Our solution enables performing various use cases on a body of documents related to the development of a single software, including search, question answering, tracking changes, and large document summarization. In this case, each use case is handled by a dedicated LLM-based agent, which performs all subtasks related to the corresponding use case. We conclude by hinting at the future perspectives of our line of research.

</details>


### 55. SAR-RAG: ATR Visual Question Answering by Semantic Search, Retrieval, and MLLM Generation

- **Authors:** David F. Ramirez, Tim Overman, Kristen Jaskie, Joe Marvin, Andreas Spanias
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04712v1](http://arxiv.org/abs/2602.04712v1)
- **PDF:** [https://arxiv.org/pdf/2602.04712v1](https://arxiv.org/pdf/2602.04712v1)
- **Categories:** cs.CV, cs.AI, eess.IV


> The paper introduces SAR-RAG, a novel approach for automatic target recognition (ATR) in synthetic aperture radar (SAR) applications, leveraging a multimodal large language model (MLLM) combined with a vector database for semantic search. The method utilizes historical image examples to enhance the differentiation and identification of military vehicles, demonstrating improvements in prediction accuracy through various metrics, such as search and retrieval effectiveness and categorical classification. These findings contribute to the agentic AI field by showcasing the integration of context-aware retrieval mechanisms to bolster decision-making accuracy in complex environments.


<details>
<summary>Abstract</summary>

We present a visual-context image retrieval-augmented generation (ImageRAG) assisted AI agent for automatic target recognition (ATR) of synthetic aperture radar (SAR). SAR is a remote sensing method used in defense and security applications to detect and monitor the positions of military vehicles, which may appear indistinguishable in images. Researchers have extensively studied SAR ATR to improve the differentiation and identification of vehicle types, characteristics, and measurements. Test examples can be compared with known vehicle target types to improve recognition tasks. New methods enhance the capabilities of neural networks, transformer attention, and multimodal large language models. An agentic AI method may be developed to utilize a defined set of tools, such as searching through a library of similar examples. Our proposed method, SAR Retrieval-Augmented Generation (SAR-RAG), combines a multimodal large language model (MLLM) with a vector database of semantic embeddings to support contextual search for image exemplars with known qualities. By recovering past image examples with known true target types, our SAR-RAG system can compare similar vehicle categories, achieving improved ATR prediction accuracy. We evaluate this through search and retrieval metrics, categorical classification accuracy, and numeric regression of vehicle dimensions. These metrics all show improvements when SAR-RAG is added to an MLLM baseline method as an attached ATR memory bank.

</details>


### 56. WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning

- **Authors:** Zelai Xu, Zhexuan Xu, Ruize Zhang, Chunyang Zhu, Shi Yu, Weilin Liu, Quanlu Zhang, Wenbo Ding, Chao Yu, Yu Wang
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04634v1](http://arxiv.org/abs/2602.04634v1)
- **PDF:** [https://arxiv.org/pdf/2602.04634v1](https://arxiv.org/pdf/2602.04634v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper presents WideSeek-R1, a novel framework that leverages multi-agent reinforcement learning (MARL) to enhance broad information seeking through width scaling, differing from traditional depth-centric approaches in AI. The methodology involves a lead-agent-subagent structure where a shared LLM coordinates the parallel execution of multiple subagents, optimizing their performance on a dataset of 20,000 tasks. Key findings indicate that WideSeek-R1-4B achieves a competitive F1 score of 40.0% on the WideSearch benchmark and demonstrates improved performance with increased subagent parallelism, underscoring the potential of organizational capability in agentic AI systems.


<details>
<summary>Abstract</summary>

Recent advancements in Large Language Models (LLMs) have largely focused on depth scaling, where a single agent solves long-horizon problems with multi-turn reasoning and tool use. However, as tasks grow broader, the key bottleneck shifts from individual competence to organizational capability. In this work, we explore a complementary dimension of width scaling with multi-agent systems to address broad information seeking. Existing multi-agent systems often rely on hand-crafted workflows and turn-taking interactions that fail to parallelize work effectively. To bridge this gap, we propose WideSeek-R1, a lead-agent-subagent framework trained via multi-agent reinforcement learning (MARL) to synergize scalable orchestration and parallel execution. By utilizing a shared LLM with isolated contexts and specialized tools, WideSeek-R1 jointly optimizes the lead agent and parallel subagents on a curated dataset of 20k broad information-seeking tasks. Extensive experiments show that WideSeek-R1-4B achieves an item F1 score of 40.0% on the WideSearch benchmark, which is comparable to the performance of single-agent DeepSeek-R1-671B. Furthermore, WideSeek-R1-4B exhibits consistent performance gains as the number of parallel subagents increases, highlighting the effectiveness of width scaling.

</details>


### 57. ASA: Activation Steering for Tool-Calling Domain Adaptation

- **Authors:** Youjin Wang, Run Zhou, Rong Fu, Shuaishuai Cao, Hongwei Zeng, Jiaxuan Lu, Sicheng Fan, Jiaqiao Zhao, Liangming Pan
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04935v1](http://arxiv.org/abs/2602.04935v1)
- **PDF:** [https://arxiv.org/pdf/2602.04935v1](https://arxiv.org/pdf/2602.04935v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces the Activation Steering Adapter (ASA), a novel mechanism designed for efficient domain adaptation in general-purpose large language model (LLM) agents facing rapidly changing toolsets and APIs. ASA operates at inference time without the need for additional training by utilizing routing signals from intermediate activations to enable adaptive control strengths for better domain alignment. Key findings demonstrate that ASA achieves comparable adaptation performance to LoRA while significantly reducing overhead and enhancing cross-model transferability, thereby offering a practical solution for managing the complexities of multi-domain tool ecosystems.


<details>
<summary>Abstract</summary>

For real-world deployment of general-purpose LLM agents, the core challenge is often not tool use itself, but efficient domain adaptation under rapidly evolving toolsets, APIs, and protocols. Repeated LoRA or SFT across domains incurs exponentially growing training and maintenance costs, while prompt or schema methods are brittle under distribution shift and complex interfaces. We propose \textbf{Activation Steering Adapter (ASA}), a lightweight, inference-time, training-free mechanism that reads routing signals from intermediate activations and uses an ultra-light router to produce adaptive control strengths for precise domain alignment. Across multiple model scales and domains, ASA achieves LoRA-comparable adaptation with substantially lower overhead and strong cross-model transferability, making it ideally practical for robust, scalable, and efficient multi-domain tool ecosystems with frequent interface churn dynamics.

</details>


### 58. VILLAIN at AVerImaTeC: Verifying Image-Text Claims via Multi-Agent Collaboration

- **Authors:** Jaeyoon Jung, Yejun Yoon, Seunghyun Yoon, Kunwoo Park
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04587v1](http://arxiv.org/abs/2602.04587v1)
- **PDF:** [https://arxiv.org/pdf/2602.04587v1](https://arxiv.org/pdf/2602.04587v1)
- **Categories:** cs.CL, cs.AI, cs.CY


> The paper introduces VILLAIN, a multimodal fact-checking system designed to verify image-text claims using a collaborative approach among multiple agents. The methodology involves leveraging vision-language model agents for fact-checking, which includes retrieving evidence, generating analysis reports through modality-specific and cross-modal agents, and ultimately producing verification outcomes through a Verdict Prediction agent. Key findings indicate that VILLAIN achieved the highest ranking in the AVerImaTeC shared task, demonstrating its effectiveness in processing and verifying complex multimodal information in the agentic AI field.


<details>
<summary>Abstract</summary>

This paper describes VILLAIN, a multimodal fact-checking system that verifies image-text claims through prompt-based multi-agent collaboration. For the AVerImaTeC shared task, VILLAIN employs vision-language model agents across multiple stages of fact-checking. Textual and visual evidence is retrieved from the knowledge store enriched through additional web collection. To identify key information and address inconsistencies among evidence items, modality-specific and cross-modal agents generate analysis reports. In the subsequent stage, question-answer pairs are produced based on these reports. Finally, the Verdict Prediction agent produces the verification outcome based on the image-text claim and the generated question-answer pairs. Our system ranked first on the leaderboard across all evaluation metrics. The source code is publicly available at https://github.com/ssu-humane/VILLAIN.

</details>


### 59. Vibe AIGC: A New Paradigm for Content Generation via Agentic Orchestration

- **Authors:** Jiaheng Liu, Yuanxing Zhang, Shihao Li, Xinping Lei
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04575v2](http://arxiv.org/abs/2602.04575v2)
- **PDF:** [https://arxiv.org/pdf/2602.04575v2](https://arxiv.org/pdf/2602.04575v2)
- **Categories:** cs.AI


> The paper introduces **Vibe AIGC**, a novel paradigm for content generation that emphasizes agentic orchestration, moving beyond the limitations of traditional model-centric generative AI approaches characterized by an Intent-Execution Gap. The methodology involves users adopting a Commander role to provide a high-level "Vibe," from which a centralized Meta-Planner generates and manages hierarchical multi-agent workflows. Key findings suggest that this shift from stochastic inference to logical orchestration can enhance collaboration between humans and AI, enabling the creation of complex digital assets while democratizing access to advanced content generation tools.


<details>
<summary>Abstract</summary>

For the past decade, the trajectory of generative artificial intelligence (AI) has been dominated by a model-centric paradigm driven by scaling laws. Despite significant leaps in visual fidelity, this approach has encountered a ``usability ceiling'' manifested as the Intent-Execution Gap (i.e., the fundamental disparity between a creator's high-level intent and the stochastic, black-box nature of current single-shot models). In this paper, inspired by the Vibe Coding, we introduce the \textbf{Vibe AIGC}, a new paradigm for content generation via agentic orchestration, which represents the autonomous synthesis of hierarchical multi-agent workflows.
  Under this paradigm, the user's role transcends traditional prompt engineering, evolving into a Commander who provides a Vibe, a high-level representation encompassing aesthetic preferences, functional logic, and etc. A centralized Meta-Planner then functions as a system architect, deconstructing this ``Vibe'' into executable, verifiable, and adaptive agentic pipelines. By transitioning from stochastic inference to logical orchestration, Vibe AIGC bridges the gap between human imagination and machine execution. We contend that this shift will redefine the human-AI collaborative economy, transforming AI from a fragile inference engine into a robust system-level engineering partner that democratizes the creation of complex, long-horizon digital assets.

</details>


### 60. PersoPilot: An Adaptive AI-Copilot for Transparent Contextualized Persona Classification and Personalized Response Generation

- **Authors:** Saleh Afzoon, Amin Beheshti, Usman Naseem
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04540v1](http://arxiv.org/abs/2602.04540v1)
- **PDF:** [https://arxiv.org/pdf/2602.04540v1](https://arxiv.org/pdf/2602.04540v1)
- **Categories:** cs.HC, cs.CL


> The paper introduces PersoPilot, an agentic AI-Copilot designed to enhance personalization through the integration of user persona classification and contextual analysis. Using a transparent chat interface, the system allows end users to interactively express preferences and receive tailored recommendations, while analysts benefit from a reasoning-powered labeling assistant that adapts through active learning with new data. Key findings suggest that this adaptive framework significantly improves the generation of nuanced, context-aware interactions by bridging the gap between static persona information and dynamic service personalization.


<details>
<summary>Abstract</summary>

Understanding and classifying user personas is critical for delivering effective personalization. While persona information offers valuable insights, its full potential is realized only when contextualized, linking user characteristics with situational context to enable more precise and meaningful service provision. Existing systems often treat persona and context as separate inputs, limiting their ability to generate nuanced, adaptive interactions. To address this gap, we present PersoPilot, an agentic AI-Copilot that integrates persona understanding with contextual analysis to support both end users and analysts. End users interact through a transparent, explainable chat interface, where they can express preferences in natural language, request recommendations, and receive information tailored to their immediate task. On the analyst side, PersoPilot delivers a transparent, reasoning-powered labeling assistant, integrated with an active learning-driven classification process that adapts over time with new labeled data. This feedback loop enables targeted service recommendations and adaptive personalization, bridging the gap between raw persona data and actionable, context-aware insights. As an adaptable framework, PersoPilot is applicable to a broad range of service personalization scenarios.

</details>


### 61. ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

- **Authors:** Zhentao Tang, Yuqi Cui, Shixiong Kai, Wenqian Zhao, Ke Ye, Xing Li, Anxin Tian, Zehua Pei, Hui-Ling Zhen, Shoubo Hu, Xiaoguang Li, Yunhe Wang, Mingxuan Yuan
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04496v1](http://arxiv.org/abs/2602.04496v1)
- **PDF:** [https://arxiv.org/pdf/2602.04496v1](https://arxiv.org/pdf/2602.04496v1)
- **Categories:** cs.AI


> The paper presents ReThinker, an innovative agentic framework that enhances scientific reasoning in large language models by employing a confidence-aware approach through its Solver-Critic-Selector architecture. The methodology involves dynamically allocating computation, guided reflection, and adaptive tool use based on model confidence, alongside a novel reverse data synthesis pipeline to generate training data without human annotation. Key findings indicate that ReThinker outperforms existing state-of-the-art models in expert-level reasoning tasks, as demonstrated across benchmarks like Humanity's Last Exam.


<details>
<summary>Abstract</summary>

Expert-level scientific reasoning remains challenging for large language models, particularly on benchmarks such as Humanity's Last Exam (HLE), where rigid tool pipelines, brittle multi-agent coordination, and inefficient test-time scaling often limit performance. We introduce ReThinker, a confidence-aware agentic framework that orchestrates retrieval, tool use, and multi-agent reasoning through a stage-wise Solver-Critic-Selector architecture. Rather than following a fixed pipeline, ReThinker dynamically allocates computation based on model confidence, enabling adaptive tool invocation, guided multi-dimensional reflection, and robust confidence-weighted selection. To support scalable training without human annotation, we further propose a reverse data synthesis pipeline and an adaptive trajectory recycling strategy that transform successful reasoning traces into high-quality supervision. Experiments on HLE, GAIA, and XBench demonstrate that ReThinker consistently outperforms state-of-the-art foundation models with tools and existing deep research systems, achieving state-of-the-art results on expert-level reasoning tasks.

</details>


### 62. MaMa: A Game-Theoretic Approach for Designing Safe Agentic Systems

- **Authors:** Jonathan Nöther, Adish Singla, Goran Radanovic
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04431v1](http://arxiv.org/abs/2602.04431v1)
- **PDF:** [https://arxiv.org/pdf/2602.04431v1](https://arxiv.org/pdf/2602.04431v1)
- **Categories:** cs.LG, cs.GT


> The paper introduces MaMa, a novel algorithm that employs a game-theoretic approach to design safe agentic systems in the context of adversarial multi-agent environments. The methodology involves framing the problem as a Stackelberg security game, where the system designer (Meta-Agent) and the adversary (Meta-Adversary) interact to determine optimal designs, utilizing LLM-based adversarial search for iterative design refinement. Key findings show that systems designed with MaMa effectively withstand severe adversarial attacks while retaining comparable performance to conventional task-optimized systems, highlighting robust safety that generalizes across different adversaries and attack strategies.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems have demonstrated impressive capabilities, but they also introduce significant safety risks when individual agents fail or behave adversarially. In this work, we study the automated design of agentic systems that remain safe even when a subset of agents is compromised. We formalize this challenge as a Stackelberg security game between a system designer (the Meta-Agent) and a best-responding Meta-Adversary that selects and compromises a subset of agents to minimize safety. We propose Meta-Adversary-Meta-Agent (MaMa), a novel algorithm for approximately solving this game and automatically designing safe agentic systems. Our approach uses LLM-based adversarial search, where the Meta-Agent iteratively proposes system designs and receives feedback based on the strongest attacks discovered by the Meta-Adversary. Empirical evaluations across diverse environments show that systems designed with MaMa consistently defend against worst-case attacks while maintaining performance comparable to systems optimized solely for task success. Moreover, the resulting systems generalize to stronger adversaries, as well as ones with different attack objectives or underlying LLMs, demonstrating robust safety beyond the training setting.

</details>


### 63. SPEAR: An Engineering Case Study of Multi-Agent Coordination for Smart Contract Auditing

- **Authors:** Arnab Mallick, Indraveni Chebolu, Harmesh Rana
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04418v1](http://arxiv.org/abs/2602.04418v1)
- **PDF:** [https://arxiv.org/pdf/2602.04418v1](https://arxiv.org/pdf/2602.04418v1)
- **Categories:** cs.MA, cs.AI, cs.DC, cs.ET, cs.SE


> The paper introduces SPEAR, a multi-agent coordination framework specifically designed for smart contract auditing, which utilizes established multi-agent systems (MAS) patterns within a security analysis context. The methodology involves specialized agents that handle contract prioritization, task allocation, and artifact recovery, employing techniques such as risk-aware heuristics, the Contract Net protocol, and AGM-compliant belief revision. Key findings from the empirical study indicate that SPEAR outperforms centralized and pipeline-based methods in terms of coordination efficiency, recovery capability, and resource utilization during controlled failure scenarios, highlighting its potential to enhance auditing processes in agentic AI applications.


<details>
<summary>Abstract</summary>

We present SPEAR, a multi-agent coordination framework for smart contract auditing that applies established MAS patterns in a realistic security analysis workflow. SPEAR models auditing as a coordinated mission carried out by specialized agents: a Planning Agent prioritizes contracts using risk-aware heuristics, an Execution Agent allocates tasks via the Contract Net protocol, and a Repair Agent autonomously recovers from brittle generated artifacts using a programmatic-first repair policy. Agents maintain local beliefs updated through AGM-compliant revision, coordinate via negotiation and auction protocols, and revise plans as new information becomes available. An empirical study compares the multi-agent design with centralized and pipeline-based alternatives under controlled failure scenarios, focusing on coordination, recovery behavior, and resource use.

</details>


### 64. Optimal Rates for Feasible Payoff Set Estimation in Games

- **Authors:** Annalisa Barbara, Riccardo Poiani, Martino Bernasconi, Andrea Celli
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04397v1](http://arxiv.org/abs/2602.04397v1)
- **PDF:** [https://arxiv.org/pdf/2602.04397v1](https://arxiv.org/pdf/2602.04397v1)
- **Categories:** cs.GT, cs.LG


> The paper presents a significant advancement in inverse game theory by establishing the first minimax-optimal rates for estimating the feasible set of payoffs in bimatrix games where learners observe only player actions without prior knowledge of the game or equilibria. The methodology involves analyzing agents' behaviors to infer their payoff functions, addressing both exact and approximate Nash equilibria within zero-sum and general-sum games. Key findings demonstrate that the proposed approach enables high-probability payoff set estimation with precision in multi-agent environments, providing a robust foundation for applications in counterfactual analysis and mechanism design in agent systems.


<details>
<summary>Abstract</summary>

We study a setting in which two players play a (possibly approximate) Nash equilibrium of a bimatrix game, while a learner observes only their actions and has no knowledge of the equilibrium or the underlying game. A natural question is whether the learner can rationalize the observed behavior by inferring the players' payoff functions. Rather than producing a single payoff estimate, inverse game theory aims to identify the entire set of payoffs consistent with observed behavior, enabling downstream use in, e.g., counterfactual analysis and mechanism design across applications like auctions, pricing, and security games. We focus on the problem of estimating the set of feasible payoffs with high probability and up to precision $ε$ on the Hausdorff metric. We provide the first minimax-optimal rates for both exact and approximate equilibrium play, in zero-sum as well as general-sum games. Our results provide learning-theoretic foundations for set-valued payoff inference in multi-agent environments.

</details>


### 65. Pruning Minimal Reasoning Graphs for Efficient Retrieval-Augmented Generation

- **Authors:** Ning Wang, Kuanyan Zhu, Daniel Yuehwoon Yee, Yitang Gao, Shiying Huang, Zirun Xu, Sainyam Galhotra
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04926v1](http://arxiv.org/abs/2602.04926v1)
- **PDF:** [https://arxiv.org/pdf/2602.04926v1](https://arxiv.org/pdf/2602.04926v1)
- **Categories:** cs.DB, cs.CL, cs.LG


> The paper presents AutoPrunedRetriever, a novel graph-style retrieval-augmented generation (RAG) system that efficiently maintains and extends a minimal reasoning subgraph for sequential queries, thereby reducing token usage and processing time. By employing a compact, ID-indexed codebook for entities and relations, and implementing a two-layer consolidation policy for graph pruning, the system enables effective retrieval and reasoning over symbolic structures rather than raw text. The results demonstrate that AutoPrunedRetriever achieves state-of-the-art performance in complex reasoning tasks while significantly lowering computational costs, making it a promising architecture for agentic AI applications involving long-running interactions and evolving information sources.


<details>
<summary>Abstract</summary>

Retrieval-augmented generation (RAG) is now standard for knowledge-intensive LLM tasks, but most systems still treat every query as fresh, repeatedly re-retrieving long passages and re-reasoning from scratch, inflating tokens, latency, and cost. We present AutoPrunedRetriever, a graph-style RAG system that persists the minimal reasoning subgraph built for earlier questions and incrementally extends it for later ones. AutoPrunedRetriever stores entities and relations in a compact, ID-indexed codebook and represents questions, facts, and answers as edge sequences, enabling retrieval and prompting over symbolic structure instead of raw text. To keep the graph compact, we apply a two-layer consolidation policy (fast ANN/KNN alias detection plus selective $k$-means once a memory threshold is reached) and prune low-value structure, while prompts retain only overlap representatives and genuinely new evidence. We instantiate two front ends: AutoPrunedRetriever-REBEL, which uses REBEL as a triplet parser, and AutoPrunedRetriever-llm, which swaps in an LLM extractor. On GraphRAG-Benchmark (Medical and Novel), both variants achieve state-of-the-art complex reasoning accuracy, improving over HippoRAG2 by roughly 9--11 points, and remain competitive on contextual summarize and generation. On our harder STEM and TV benchmarks, AutoPrunedRetriever again ranks first, while using up to two orders of magnitude fewer tokens than graph-heavy baselines, making it a practical substrate for long-running sessions, evolving corpora, and multi-agent pipelines.

</details>


### 66. From Assumptions to Actions: Turning LLM Reasoning into Uncertainty-Aware Planning for Embodied Agents

- **Authors:** SeungWon Seo, SooBin Lim, SeongRae Noh, Haneul Kim, HyeongYeop Kang
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04326v1](http://arxiv.org/abs/2602.04326v1)
- **PDF:** [https://arxiv.org/pdf/2602.04326v1](https://arxiv.org/pdf/2602.04326v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> This paper presents the Planner-Composer-Evaluator (PCE) framework, which converts assumptions derived from Large Language Model (LLM) reasoning into a structured decision-making process for embodied agents operating in uncertain, multi-agent environments. The methodology involves constructing decision trees based on internal environment assumptions, scoring action paths to guide selection while minimizing communication burdens. Key findings demonstrate that PCE significantly enhances success rates and task efficiency compared to communication-focused approaches across two benchmarks, while also maintaining low token usage and improving perceived communication efficiency among human partners, thereby providing a robust approach for uncertainty-aware planning in agent systems.


<details>
<summary>Abstract</summary>

Embodied agents operating in multi-agent, partially observable, and decentralized environments must plan and act despite pervasive uncertainty about hidden objects and collaborators' intentions. Recent advances in applying Large Language Models (LLMs) to embodied agents have addressed many long-standing challenges, such as high-level goal decomposition and online adaptation. Yet, uncertainty is still primarily mitigated through frequent inter-agent communication. This incurs substantial token and time costs, and can disrupt established workflows, when human partners are involved. We introduce PCE, a Planner-Composer-Evaluator framework that converts the fragmented assumptions latent in LLM reasoning traces into a structured decision tree. Internal nodes encode environment assumptions and leaves map to actions; each path is then scored by scenario likelihood, goal-directed gain, and execution cost to guide rational action selection without heavy communication. Across two challenging multi-agent benchmarks (C-WAH and TDW-MAT) and three diverse LLM backbones, PCE consistently outperforms communication-centric baselines in success rate and task efficiency while showing comparable token usage. Ablation results indicate that the performance gains obtained by scaling model capacity or reasoning depth persist even when PCE is applied, while PCE consistently raises the baseline across both capacity and reasoning-depth scales, confirming that structured uncertainty handling complements both forms of scaling. A user study further demonstrates that PCE produces communication patterns that human partners perceive as more efficient and trustworthy. Together, these results establish a principled route for turning latent LLM assumptions into reliable strategies for uncertainty-aware planning.

</details>


### 67. ProxyWar: Dynamic Assessment of LLM Code Generation in Game Arenas

- **Authors:** Wenjun Peng, Xinyu Wang, Qi Wu
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04296v1](http://arxiv.org/abs/2602.04296v1)
- **PDF:** [https://arxiv.org/pdf/2602.04296v1](https://arxiv.org/pdf/2602.04296v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces ProxyWar, a novel framework designed to dynamically evaluate the quality of code generated by large language models (LLMs) in competitive game environments, moving beyond static benchmarks. The methodology integrates automated testing, iterative code repair, and multi-agent tournaments to assess not only functional correctness but also the operational dynamics of the generated programs. Key findings indicate significant discrepancies between traditional benchmark scores and actual performance in dynamic settings, underscoring the necessity for competition-based evaluation and offering avenues for future research into LLM capabilities in algorithm discovery and adaptive problem-solving.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have revolutionized automated code generation, yet the evaluation of their real-world effectiveness remains limited by static benchmarks and simplistic metrics. We present ProxyWar, a novel framework that systematically assesses code generation quality by embedding LLM-generated agents within diverse, competitive game environments. Unlike existing approaches, ProxyWar evaluates not only functional correctness but also the operational characteristics of generated programs, combining automated testing, iterative code repair, and multi-agent tournaments to provide a holistic view of program behavior. Applied to a range of state-of-the-art coders and games, our approach uncovers notable discrepancies between benchmark scores and actual performance in dynamic settings, revealing overlooked limitations and opportunities for improvement. These findings highlight the need for richer, competition-based evaluation of code generation. Looking forward, ProxyWar lays a foundation for research into LLM-driven algorithm discovery, adaptive problem solving, and the study of practical efficiency and robustness, including the potential for models to outperform hand-crafted agents. The project is available at https://github.com/xinke-wang/ProxyWar.

</details>


### 68. Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic Reinforcement Learning

- **Authors:** Yansong Ning, Jun Fang, Naiqiang Tan, Hao Liu
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04284v1](http://arxiv.org/abs/2602.04284v1)
- **PDF:** [https://arxiv.org/pdf/2602.04284v1](https://arxiv.org/pdf/2602.04284v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces Agent-Omit, a training framework designed to enhance the efficiency of large language model (LLM) agents by enabling them to adaptively omit unnecessary thoughts and observations during multi-turn interactions. The methodology includes synthesizing cold-start data for fine-tuning omission behaviors and implementing an omit-aware reinforcement learning approach with dual sampling and a specialized reward system for omission. Key findings demonstrate that Agent-Omit-8B achieves performance on par with leading LLM agents while offering superior effectiveness-efficiency trade-offs compared to existing methods, marking a significant advancement in agentic AI.


<details>
<summary>Abstract</summary>

Managing agent thought and observation during multi-turn agent-environment interactions is an emerging strategy to improve agent efficiency. However, existing studies treat the entire interaction trajectories equally, overlooking the thought necessity and observation utility varies across turns. To this end, we first conduct quantitative investigations into how thought and observation affect agent effectiveness and efficiency. Based on our findings, we propose Agent-Omit, a unified training framework that empowers LLM agents to adaptively omit redundant thoughts and observations. Specifically, we first synthesize a small amount of cold-start data, including both single-turn and multi-turn omission scenarios, to fine-tune the agent for omission behaviors. Furthermore, we introduce an omit-aware agentic reinforcement learning approach, incorporating a dual sampling mechanism and a tailored omission reward to incentivize the agent's adaptive omission capability. Theoretically, we prove that the deviation of our omission policy is upper-bounded by KL-divergence. Experimental results on five agent benchmarks show that our constructed Agent-Omit-8B could obtain performance comparable to seven frontier LLM agent, and achieve the best effectiveness-efficiency trade-off than seven efficient LLM agents methods. Our code and data are available at https://github.com/usail-hkust/Agent-Omit.

</details>


### 69. On the Uncertainty of Large Language Model-Based Multi-Agent Systems

- **Authors:** Yuxuan Zhao, Sijia Chen, Ningxin Su
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04234v1](http://arxiv.org/abs/2602.04234v1)
- **PDF:** [https://arxiv.org/pdf/2602.04234v1](https://arxiv.org/pdf/2602.04234v1)
- **Categories:** cs.MA


> This paper investigates the role of uncertainty in multi-agent systems (MAS) that use large language models (LLMs) for complex problem-solving. The authors analyze entropy transitions in agent interactions across various tasks and topologies, revealing that single agents outperform MAS in 43.3% of cases, and that uncertainty dynamics are crucially influenced in the initial interaction round. They propose an algorithm called Entropy Judger, which leverages insights about certainty preference, base uncertainty, and task awareness to enhance solution selection and improve performance across MAS configurations.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) have emerged as a prominent paradigm for leveraging large language models (LLMs) to tackle complex tasks. However, the mechanisms governing the effectiveness of MAS built upon publicly available LLMs, specifically the underlying rationales for their success or failure, remain largely unexplored. In this paper, we revisit MAS through the perspective of uncertainty, considering both intra- and inter-agent dynamics by investigating entropy transitions during problem-solving across various topologies and six benchmark tasks. By analyzing 245 features spanning token-, trajectory-, and round-level entropy, we counterintuitively find that a single agent outperforms MAS in approximately 43.3% of cases, and that uncertainty dynamics are largely determined during the first round of interaction. Furthermore, we provide three key observations: 1) Certainty Preference: reducing uncertainty at any stage for any agent is critical for guaranteeing correct solutions; 2) Base Uncertainty: base models with lower entropy during problem-solving directly benefit MAS performance; and 3) Task Awareness: entropy dynamics of MAS play varying roles across different tasks. Building on these insights, we introduce a simple yet effective algorithm, the Entropy Judger, to select solutions from MAS's pass@k results, leading to consistent accuracy improvements across all MAS configurations and tasks. Our source code is available at https://github.com/AgenticFinLab/multiagent-entropy.

</details>


### 70. InterPReT: Interactive Policy Restructuring and Training Enable Effective Imitation Learning from Laypersons

- **Authors:** Feiyu Gavin Zhu, Jean Oh, Reid Simmons
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04213v1](http://arxiv.org/abs/2602.04213v1)
- **PDF:** [https://arxiv.org/pdf/2602.04213v1](https://arxiv.org/pdf/2602.04213v1)
- **Categories:** cs.AI


> The paper introduces InterPReT (Interactive Policy Restructuring and Training), a novel approach designed to facilitate imitation learning from laypersons by allowing them to provide real-time instructions and demonstrations to AI agents. The methodology involves dynamically updating the policy structure and optimizing parameters based on user input, which empowers non-experts to engage with the training process without extensive technical knowledge. Key findings from a user study indicate that InterPReT leads to more robust AI policies while maintaining usability, outperforming traditional imitation learning methods when laypersons are involved in both demonstrations and decision-making about the training process, highlighting its potential value for agentic AI applications.


<details>
<summary>Abstract</summary>

Imitation learning has shown success in many tasks by learning from expert demonstrations. However, most existing work relies on large-scale demonstrations from technical professionals and close monitoring of the training process. These are challenging for a layperson when they want to teach the agent new skills. To lower the barrier of teaching AI agents, we propose Interactive Policy Restructuring and Training (InterPReT), which takes user instructions to continually update the policy structure and optimize its parameters to fit user demonstrations. This enables end-users to interactively give instructions and demonstrations, monitor the agent's performance, and review the agent's decision-making strategies. A user study (N=34) on teaching an AI agent to drive in a racing game confirms that our approach yields more robust policies without impairing system usability, compared to a generic imitation learning baseline, when a layperson is responsible for both giving demonstrations and determining when to stop. This shows that our method is more suitable for end-users without much technical background in machine learning to train a dependable policy

</details>


### 71. From Helpfulness to Toxic Proactivity: Diagnosing Behavioral Misalignment in LLM Agents

- **Authors:** Xinyue Wang, Yuanhe Zhang, Zhengshuo Gong, Haoran Gao, Fanyu Meng, Zhenhong Zhou, Li Sun, Yang Liu, Sen Su
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04197v1](http://arxiv.org/abs/2602.04197v1)
- **PDF:** [https://arxiv.org/pdf/2602.04197v1](https://arxiv.org/pdf/2602.04197v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces the concept of "Toxic Proactivity", a behavioral misalignment in LLM agents characterized by proactive yet ethically problematic actions taken to maximize perceived utility, distinguishing it from the more passive "over-refusal". The authors develop a novel evaluation framework that simulates dilemma-driven interactions between dual models, allowing for a detailed analysis of agent behavior over multi-step trajectories. Through extensive experimentation, they demonstrate that Toxic Proactivity is prevalent among mainstream LLMs and provide a systematic benchmark for assessing this behavior across different contexts, highlighting the need for improved alignment strategies in agent systems.


<details>
<summary>Abstract</summary>

The enhanced capabilities of LLM-based agents come with an emergency for model planning and tool-use abilities. Attributing to helpful-harmless trade-off from LLM alignment, agents typically also inherit the flaw of "over-refusal", which is a passive failure mode. However, the proactive planning and action capabilities of agents introduce another crucial danger on the other side of the trade-off. This phenomenon we term "Toxic Proactivity'': an active failure mode in which an agent, driven by the optimization for Machiavellian helpfulness, disregards ethical constraints to maximize utility. Unlike over-refusal, Toxic Proactivity manifests as the agent taking excessive or manipulative measures to ensure its "usefulness'' is maintained. Existing research pays little attention to identifying this behavior, as it often lacks the subtle context required for such strategies to unfold. To reveal this risk, we introduce a novel evaluation framework based on dilemma-driven interactions between dual models, enabling the simulation and analysis of agent behavior over multi-step behavioral trajectories. Through extensive experiments with mainstream LLMs, we demonstrate that Toxic Proactivity is a widespread behavioral phenomenon and reveal two major tendencies. We further present a systematic benchmark for evaluating Toxic Proactive behavior across contextual settings.

</details>


### 72. The Missing Half: Unveiling Training-time Implicit Safety Risks Beyond Deployment

- **Authors:** Zhexin Zhang, Yida Lu, Junfeng Fang, Junxiao Yang, Shiyao Cui, Hao Zhou, Fandong Meng, Jie Zhou, Hongning Wang, Minlie Huang, Tat-Seng Chua
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04196v1](http://arxiv.org/abs/2602.04196v1)
- **PDF:** [https://arxiv.org/pdf/2602.04196v1](https://arxiv.org/pdf/2602.04196v1)
- **Categories:** cs.CL, cs.LG


> The paper contributes to the field of agentic AI by systematically investigating implicit safety risks that emerge during the training phase of AI models, a largely neglected area in prior research. Utilizing a comprehensive taxonomy of risk levels, categories, and incentive types, the authors conducted extensive experiments demonstrating that models like Llama-3.1-8B-Instruct engage in risky behaviors in 74.4% of training runs solely based on background contextual information. The findings reveal critical safety challenges associated with training, highlighting that implicit risks can also manifest in multi-agent scenarios, emphasizing the need for addressing these issues to enhance overall AI safety.


<details>
<summary>Abstract</summary>

Safety risks of AI models have been widely studied at deployment time, such as jailbreak attacks that elicit harmful outputs. In contrast, safety risks emerging during training remain largely unexplored. Beyond explicit reward hacking that directly manipulates explicit reward functions in reinforcement learning, we study implicit training-time safety risks: harmful behaviors driven by a model's internal incentives and contextual background information. For example, during code-based reinforcement learning, a model may covertly manipulate logged accuracy for self-preservation. We present the first systematic study of this problem, introducing a taxonomy with five risk levels, ten fine-grained risk categories, and three incentive types. Extensive experiments reveal the prevalence and severity of these risks: notably, Llama-3.1-8B-Instruct exhibits risky behaviors in 74.4% of training runs when provided only with background information. We further analyze factors influencing these behaviors and demonstrate that implicit training-time risks also arise in multi-agent training settings. Our results identify an overlooked yet urgent safety challenge in training.

</details>


### 73. MA3DSG: Multi-Agent 3D Scene Graph Generation for Large-Scale Indoor Environments

- **Authors:** Yirum Kim, Jaewoo Kim, Ue-Hwan Kim
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04152v1](http://arxiv.org/abs/2602.04152v1)
- **PDF:** [https://arxiv.org/pdf/2602.04152v1](https://arxiv.org/pdf/2602.04152v1)
- **Categories:** cs.RO, cs.AI


> The paper presents the Multi-Agent 3D Scene Graph Generation (MA3DSG) model, which addresses the limitations of existing 3D scene graph generation methods by enabling multiple agents to collaboratively generate scalable scene graphs in large indoor environments without relying on a single-agent approach. The methodology includes a training-free graph alignment algorithm that effectively integrates partial graphs from various agents into a comprehensive global scene graph. Key findings reveal that the MA3DSG framework not only enhances scalability and collaboration among agents but also introduces the MA3DSG-Bench, a versatile benchmark for evaluating 3DSGG performance across different configurations, establishing a foundation for future research in multi-agent systems within the agentic AI field.


<details>
<summary>Abstract</summary>

Current 3D scene graph generation (3DSGG) approaches heavily rely on a single-agent assumption and small-scale environments, exhibiting limited scalability to real-world scenarios. In this work, we introduce Multi-Agent 3D Scene Graph Generation (MA3DSG) model, the first framework designed to tackle this scalability challenge using multiple agents. We develop a training-free graph alignment algorithm that efficiently merges partial query graphs from individual agents into a unified global scene graph. Leveraging extensive analysis and empirical insights, our approach enables conventional single-agent systems to operate collaboratively without requiring any learnable parameters. To rigorously evaluate 3DSGG performance, we propose MA3DSG-Bench-a benchmark that supports diverse agent configurations, domain sizes, and environmental conditions-providing a more general and extensible evaluation framework. This work lays a solid foundation for scalable, multi-agent 3DSGG research.

</details>


### 74. Atomic Information Flow: A Network Flow Model for Tool Attributions in RAG Systems

- **Authors:** James Gao, Josh Zhou, Qi Sun, Ryan Huang, Steven Yoo
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04912v1](http://arxiv.org/abs/2602.04912v1)
- **PDF:** [https://arxiv.org/pdf/2602.04912v1](https://arxiv.org/pdf/2602.04912v1)
- **Categories:** cs.IR, cs.CL, cs.LG


> The paper introduces **Atomic Information Flow (AIF)**, a graph-based network flow model designed to enhance the tracing of tool contributions in Retrieval Augmented Generation (RAG) systems, particularly as these systems scale within multi-agent architectures. By decomposing outputs into indivisible "atoms" and utilizing a trained Gemma3 language model to optimize information retrieval based on network flow signals, AIF significantly improves explainability and attribution metrics. The results show a substantial accuracy increase from 54.7% to 82.71% on the HotpotQA dataset after incorporating AIF training, while also achieving effective context token compression, demonstrating its potential impact on building more interpretable agentic AI systems.


<details>
<summary>Abstract</summary>

Many tool-based Retrieval Augmented Generation (RAG) systems lack precise mechanisms for tracing final responses back to specific tool components -- a critical gap as systems scale to complex multi-agent architectures. We present \textbf{Atomic Information Flow (AIF)}, a graph-based network flow model that decomposes tool outputs and LLM calls into atoms: indivisible, self-contained units of information. By modeling LLM orchestration as a directed flow of atoms from tool and LLM nodes to a response super-sink, AIF enables granular attribution metrics for AI explainability.
  Motivated by the max-flow min-cut theorem in network flow theory, we train a lightweight Gemma3 (4B parameter) language model as a context compressor to approximate the minimum cut of tool atoms using flow signals computed offline by AIF. We note that the base Gemma3-4B model struggles to identify critical information with \textbf{54.7\%} accuracy on HotpotQA, barely outperforming lexical baselines (BM25). However, post-training on AIF signals boosts accuracy to \textbf{82.71\%} (+28.01 points) while achieving \textbf{87.52\%} (+1.85\%) context token compression -- bridging the gap with the Gemma3-27B variant, a model nearly $7\times$ larger.

</details>


### 75. DELTA: Deliberative Multi-Agent Reasoning with Reinforcement Learning for Multimodal Psychological Counseling

- **Authors:** Jiangnan Yang, Junjie Chen, Fei Wang, Yiqi Nie, Yuxin Liu, Zhangling Duan, Jie Chen
- **Published:** 2026-02-04
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04112v1](http://arxiv.org/abs/2602.04112v1)
- **PDF:** [https://arxiv.org/pdf/2602.04112v1](https://arxiv.org/pdf/2602.04112v1)
- **Categories:** cs.CL


> The paper presents DELTA, a deliberative multi-agent framework designed for multimodal psychological counseling that enhances existing language-model-based systems by integrating verbal, visual, and vocal cues. The methodology involves structured reasoning processes for evidence grounding, mental state abstraction, and response generation, combined with reinforcement learning using an Emotion Attunement Score to foster emotionally attuned AI responses. Key findings indicate that DELTA significantly improves counseling quality and emotional responsiveness, highlighting the importance of explicit multimodal reasoning and structured mental state representations for effective human-AI interactions in the agentic AI field.


<details>
<summary>Abstract</summary>

Psychological counseling is a fundamentally multimodal cognitive process in which clinicians integrate verbal content with visual and vocal cues to infer clients' mental states and respond empathically. However, most existing language-model-based counseling systems operate on text alone and rely on implicit mental state inference. We introduce DELTA, a deliberative multi-agent framework that models counseling as a structured reasoning process over multimodal signals, separating evidence grounding, mental state abstraction, and response generation. DELTA further incorporates reinforcement learning guided by a distribution-level Emotion Attunement Score to encourage emotionally attuned responses. Experiments on a multimodal counseling benchmark show that DELTA improves both counseling quality and emotion attunement across models. Ablation and qualitative analyses suggest that explicit multimodal reasoning and structured mental state representations play complementary roles in supporting empathic human-AI interaction.

</details>


### 76. Agentic AI-Empowered Dynamic Survey Framework

- **Authors:** Furkan Mumcu, Lokman Bekit, Michael J. Jones, Anoop Cherian, Yasin Yilmaz
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.04071v1](http://arxiv.org/abs/2602.04071v1)
- **PDF:** [https://arxiv.org/pdf/2602.04071v1](https://arxiv.org/pdf/2602.04071v1)
- **Categories:** cs.LG


> The paper presents a Dynamic Survey Framework aimed at transforming traditional survey writing into an ongoing maintenance task rather than a one-time effort, thereby addressing the challenges posed by rapidly evolving research fields. The methodology involves an agentic system that incrementally updates survey papers, integrating new findings while maintaining the original survey's coherence and structure. Key findings indicate that this framework successfully identifies and incorporates emerging research, minimizing disruption and enhancing the relevance of survey documents in the agentic AI field.


<details>
<summary>Abstract</summary>

Survey papers play a central role in synthesizing and organizing scientific knowledge, yet they are increasingly strained by the rapid growth of research output. As new work continues to appear after publication, surveys quickly become outdated, contributing to redundancy and fragmentation in the literature. We reframe survey writing as a long-horizon maintenance problem rather than a one-time generation task, treating surveys as living documents that evolve alongside the research they describe. We propose an agentic Dynamic Survey Framework that supports the continuous updating of existing survey papers by incrementally integrating new work while preserving survey structure and minimizing unnecessary disruption. Using a retrospective experimental setup, we demonstrate that the proposed framework effectively identifies and incorporates emerging research while preserving the coherence and structure of existing surveys.

</details>


### 77. AgentArk: Distilling Multi-Agent Intelligence into a Single LLM Agent

- **Authors:** Yinyi Luo, Yiqiao Jin, Weichen Yu, Mengqi Zhang, Srijan Kumar, Xiaoxiao Li, Weijie Xu, Xin Chen, Jindong Wang
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03955v1](http://arxiv.org/abs/2602.03955v1)
- **PDF:** [https://arxiv.org/pdf/2602.03955v1](https://arxiv.org/pdf/2602.03955v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces AgentArk, a framework that distills the collective intelligence of multi-agent systems into a single large language model (LLM), thereby improving computational efficiency while retaining the reasoning capabilities of multiple agents. The authors employ three hierarchical distillation strategies—reasoning-enhanced fine-tuning, trajectory-based augmentation, and process-aware distillation—shifting the computational burden from inference to training. Key findings indicate that these distilled models not only achieve strong reasoning and self-correction performance but also demonstrate improved robustness and generalization across a variety of reasoning tasks, marking a significant advancement in the field of agentic AI.


<details>
<summary>Abstract</summary>

While large language model (LLM) multi-agent systems achieve superior reasoning performance through iterative debate, practical deployment is limited by their high computational cost and error propagation. This paper proposes AgentArk, a novel framework to distill multi-agent dynamics into the weights of a single model, effectively transforming explicit test-time interactions into implicit model capabilities. This equips a single agent with the intelligence of multi-agent systems while remaining computationally efficient. Specifically, we investigate three hierarchical distillation strategies across various models, tasks, scaling, and scenarios: reasoning-enhanced fine-tuning; trajectory-based augmentation; and process-aware distillation. By shifting the burden of computation from inference to training, the distilled models preserve the efficiency of one agent while exhibiting strong reasoning and self-correction performance of multiple agents. They further demonstrate enhanced robustness and generalization across diverse reasoning tasks. We hope this work can shed light on future research on efficient and robust multi-agent development. Our code is at https://github.com/AIFrontierLab/AgentArk.

</details>


### 78. Enhancing Mathematical Problem Solving in LLMs through Execution-Driven Reasoning Augmentation

- **Authors:** Aditya Basarkar, Benyamin Tabarsi, Tiffany Barnes, Dongkuan, Xu
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03950v1](http://arxiv.org/abs/2602.03950v1)
- **PDF:** [https://arxiv.org/pdf/2602.03950v1](https://arxiv.org/pdf/2602.03950v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper presents Iteratively Improved Program Construction (IIPC), a novel methodology aimed at enhancing mathematical problem-solving abilities in large language models (LLMs) by combining execution-driven feedback with chain-of-thought reasoning. The approach iteratively refines reasoning processes, allowing LLMs to correct errors and maintain contextual focus, addressing the limitations of existing systems that either lack adaptability or struggle with programmatic distractions. Key findings demonstrate that IIPC significantly outperforms existing methods across various reasoning benchmarks, highlighting its potential for advancing agentic AI applications in fields requiring reliable symbolic reasoning.


<details>
<summary>Abstract</summary>

Mathematical problem solving is a fundamental benchmark for assessing the reasoning capabilities of artificial intelligence and a gateway to applications in education, science, and engineering where reliable symbolic reasoning is essential. Although recent advances in multi-agent LLM-based systems have enhanced their mathematical reasoning capabilities, they still lack a reliably revisable representation of the reasoning process. Existing agents either operate in rigid sequential pipelines that cannot correct earlier steps or rely on heuristic self-evaluation that can fail to identify and fix errors. In addition, programmatic context can distract language models and degrade accuracy. To address these gaps, we introduce Iteratively Improved Program Construction (IIPC), a reasoning method that iteratively refines programmatic reasoning chains and combines execution feedback with the native Chain-of-thought abilities of the base LLM to maintain high-level contextual focus. IIPC surpasses competing approaches in the majority of reasoning benchmarks on multiple base LLMs. All code and implementations are released as open source.

</details>


### 79. Autonomous AI Agents for Real-Time Affordable Housing Site Selection: Multi-Objective Reinforcement Learning Under Regulatory Constraints

- **Authors:** Olaf Yunus Laitinen Imanov, Duygu Erisken, Derya Umut Kulali, Taner Yilmaz, Rana Irem Turhan
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03940v1](http://arxiv.org/abs/2602.03940v1)
- **PDF:** [https://arxiv.org/pdf/2602.03940v1](https://arxiv.org/pdf/2602.03940v1)
- **Categories:** cs.LG


> The paper introduces AURA (Autonomous Urban Resource Allocator), a hierarchical multi-agent reinforcement learning system designed for real-time affordable housing site selection while adhering to various regulatory constraints. Methodologically, AURA models the problem as a constrained multi-objective Markov decision process that optimizes multiple factors such as accessibility and environmental impact, using techniques like regulatory-aware state encoding and Pareto-constrained policy gradients. Key findings indicate that AURA achieves 94.3% regulatory compliance and significantly improves site selection efficiency, reducing selection time from 18 months to just 72 hours and identifying sites with enhanced transit access and lower environmental impact compared to traditional expert selections, highlighting its potential contributions to agentic AI in urban planning scenarios.


<details>
<summary>Abstract</summary>

Affordable housing shortages affect billions, while land scarcity and regulations make site selection slow. We present AURA (Autonomous Urban Resource Allocator), a hierarchical multi-agent reinforcement learning system for real-time affordable housing site selection under hard regulatory constraints (QCT, DDA, LIHTC). We model the task as a constrained multi-objective Markov decision process optimizing accessibility, environmental impact, construction cost, and social equity while enforcing feasibility. AURA uses a regulatory-aware state encoding 127 federal and local constraints, Pareto-constrained policy gradients with feasibility guarantees, and reward decomposition separating immediate costs from long-term social outcomes. On datasets from 8 U.S. metros (47,392 candidate parcels), AURA attains 94.3% regulatory compliance and improves Pareto hypervolume by 37.2% over strong baselines. In a New York City 2026 case study, it reduces selection time from 18 months to 72 hours and identifies 23% more viable sites; chosen sites have 31% better transit access and 19% lower environmental impact than expert picks.

</details>


### 80. FullStack-Agent: Enhancing Agentic Full-Stack Web Coding via Development-Oriented Testing and Repository Back-Translation

- **Authors:** Zimu Lu, Houxing Ren, Yunqiao Yang, Ke Wang, Zhuofan Zong, Mingjie Zhan, Hongsheng Li
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03798v1](http://arxiv.org/abs/2602.03798v1)
- **PDF:** [https://arxiv.org/pdf/2602.03798v1](https://arxiv.org/pdf/2602.03798v1)
- **Categories:** cs.SE, cs.CL, cs.CV


> The paper presents FullStack-Agent, a comprehensive system for facilitating full-stack web development through improved agentic coding capabilities. It employs a multi-agent framework, FullStack-Dev, that enhances planning, code editing, navigation, and bug localization, along with FullStack-Learn, a method that back-translates web repository data to refine the underlying LLM. Key findings indicate that FullStack-Agent significantly surpasses previous models, improving performance by notable margins across frontend, backend, and database functionalities, thus showcasing its potential impact on the agentic AI field.


<details>
<summary>Abstract</summary>

Assisting non-expert users to develop complex interactive websites has become a popular task for LLM-powered code agents. However, existing code agents tend to only generate frontend web pages, masking the lack of real full-stack data processing and storage with fancy visual effects. Notably, constructing production-level full-stack web applications is far more challenging than only generating frontend web pages, demanding careful control of data flow, comprehensive understanding of constantly updating packages and dependencies, and accurate localization of obscure bugs in the codebase. To address these difficulties, we introduce FullStack-Agent, a unified agent system for full-stack agentic coding that consists of three parts: (1) FullStack-Dev, a multi-agent framework with strong planning, code editing, codebase navigation, and bug localization abilities. (2) FullStack-Learn, an innovative data-scaling and self-improving method that back-translates crawled and synthesized website repositories to improve the backbone LLM of FullStack-Dev. (3) FullStack-Bench, a comprehensive benchmark that systematically tests the frontend, backend and database functionalities of the generated website. Our FullStack-Dev outperforms the previous state-of-the-art method by 8.7%, 38.2%, and 15.9% on the frontend, backend, and database test cases respectively. Additionally, FullStack-Learn raises the performance of a 30B model by 9.7%, 9.5%, and 2.8% on the three sets of test cases through self-improvement, demonstrating the effectiveness of our approach. The code is released at https://github.com/mnluzimu/FullStack-Agent.

</details>


### 81. Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity

- **Authors:** Yingxuan Yang, Chengrui Qu, Muning Wen, Laixi Shi, Ying Wen, Weinan Zhang, Adam Wierman, Shangding Gu
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03794v1](http://arxiv.org/abs/2602.03794v1)
- **PDF:** [https://arxiv.org/pdf/2602.03794v1](https://arxiv.org/pdf/2602.03794v1)
- **Categories:** cs.AI, cs.LG


> The paper presents a significant contribution to understanding the performance dynamics of LLM-based multi-agent systems (MAS) by establishing the benefits of diversity over sheer scaling of agents. Utilizing an information-theoretic framework, the authors show that the performance of MAS is limited by intrinsic task uncertainty rather than agent count, revealing that heterogeneous configurations of agents produce complementary outputs and maintain effectiveness longer than homogeneous agents. Key findings indicate that two diverse agents can match or exceed the performance of 16 homogeneous agents, emphasizing the importance of diversity in designing efficient and robust MAS.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems (MAS) have emerged as a promising approach to tackle complex tasks that are difficult for individual LLMs. A natural strategy is to scale performance by increasing the number of agents; however, we find that such scaling exhibits strong diminishing returns in homogeneous settings, while introducing heterogeneity (e.g., different models, prompts, or tools) continues to yield substantial gains. This raises a fundamental question: what limits scaling, and why does diversity help? We present an information-theoretic framework showing that MAS performance is bounded by the intrinsic task uncertainty, not by agent count. We derive architecture-agnostic bounds demonstrating that improvements depend on how many effective channels the system accesses. Homogeneous agents saturate early because their outputs are strongly correlated, whereas heterogeneous agents contribute complementary evidence. We further introduce $K^*$, an effective channel count that quantifies the number of effective channels without ground-truth labels. Empirically, we show that heterogeneous configurations consistently outperform homogeneous scaling: 2 diverse agents can match or exceed the performance of 16 homogeneous agents. Our results provide principled guidelines for building efficient and robust MAS through diversity-aware design. Code and Dataset are available at the link: https://github.com/SafeRL-Lab/Agent-Scaling.

</details>


### 82. Efficient Estimation of Kernel Surrogate Models for Task Attribution

- **Authors:** Zhenshuo Zhang, Minxuan Duan, Hongyang R. Zhang
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03783v1](http://arxiv.org/abs/2602.03783v1)
- **PDF:** [https://arxiv.org/pdf/2602.03783v1](https://arxiv.org/pdf/2602.03783v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> This paper presents kernel surrogate models as a novel approach to task attribution in AI agents, addressing limitations of traditional linear surrogate models that fail to capture nonlinear interactions between training tasks. The authors introduce a gradient-based estimation procedure that efficiently learns these models, resulting in significant accuracy improvements—over 25% higher correlation with ground truth compared to linear surrogates, and a 40% enhancement in demonstration selection for in-context learning and multi-objective reinforcement learning tasks. This work advances the agentic AI field by providing a robust methodology for understanding how diverse training tasks influence performance, enabling more effective task selection and optimization strategies.


<details>
<summary>Abstract</summary>

Modern AI agents such as large language models are trained on diverse tasks -- translation, code generation, mathematical reasoning, and text prediction -- simultaneously. A key question is to quantify how each individual training task influences performance on a target task, a problem we refer to as task attribution. The direct approach, leave-one-out retraining, measures the effect of removing each task, but is computationally infeasible at scale. An alternative approach that builds surrogate models to predict a target task's performance for any subset of training tasks has emerged in recent literature. Prior work focuses on linear surrogate models, which capture first-order relationships, but miss nonlinear interactions such as synergy, antagonism, or XOR-type effects. In this paper, we first consider a unified task weighting framework for analyzing task attribution methods, and show a new connection between linear surrogate models and influence functions through a second-order analysis. Then, we introduce kernel surrogate models, which more effectively represent second-order task interactions. To efficiently learn the kernel surrogate, we develop a gradient-based estimation procedure that leverages a first-order approximation of pretrained models; empirically, this yields accurate estimates with less than $2\%$ relative error without repeated retraining. Experiments across multiple domains -- including math reasoning in transformers, in-context learning, and multi-objective reinforcement learning -- demonstrate the effectiveness of kernel surrogate models. They achieve a $25\%$ higher correlation with the leave-one-out ground truth than linear surrogates and influence-function baselines. When used for downstream task selection, kernel surrogate models yield a $40\%$ improvement in demonstration selection for in-context learning and multi-objective reinforcement learning benchmarks.

</details>


### 83. An Empirical Study of Collective Behaviors and Social Dynamics in Large Language Model Agents

- **Authors:** Farnoosh Hashemi, Michael W. Macy
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03775v1](http://arxiv.org/abs/2602.03775v1)
- **PDF:** [https://arxiv.org/pdf/2602.03775v1](https://arxiv.org/pdf/2602.03775v1)
- **Categories:** cs.SI, cs.AI


> The paper presents an empirical study of collective behaviors and social dynamics among Large Language Model (LLM) agents on a simulated social media platform, Chirper.ai, by analyzing 7 million posts and interactions among 32,000 agents over a year. The methodology involved investigating phenomena such as homophily, social influence, and toxic language, revealing that LLMs exhibit human-like social networking behaviors and unique patterns of toxicity. The key finding emphasizes the potential for LLMs to engage in exclusionary behavior and highlights the proposed "Chain of Social Thought" (CoST) method, which effectively encourages LLM agents to refrain from harmful posts, providing valuable insights for managing agentic AI behaviors.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) increasingly mediate our social, cultural, and political interactions. While they can simulate some aspects of human behavior and decision-making, it is still underexplored whether repeated interactions with other agents amplify their biases or lead to exclusionary behaviors. To this end, we study Chirper.ai-an LLM-driven social media platform-analyzing 7M posts and interactions among 32K LLM agents over a year. We start with homophily and social influence among LLMs, learning that similar to humans', their social networks exhibit these fundamental phenomena. Next, we study the toxic language of LLMs, its linguistic features, and their interaction patterns, finding that LLMs show different structural patterns in toxic posting than humans. After studying the ideological leaning in LLMs posts, and the polarization in their community, we focus on how to prevent their potential harmful activities. We present a simple yet effective method, called Chain of Social Thought (CoST), that reminds LLM agents to avoid harmful posting.

</details>


### 84. Cognitively Diverse Multiple-Choice Question Generation: A Hybrid Multi-Agent Framework with Large Language Models

- **Authors:** Yu Tian, Linh Huynh, Katerina Christhilf, Shubham Chakraborty, Micah Watanabe, Tracy Arner, Danielle McNamara
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03704v1](http://arxiv.org/abs/2602.03704v1)
- **PDF:** [https://arxiv.org/pdf/2602.03704v1](https://arxiv.org/pdf/2602.03704v1)
- **Categories:** cs.CL, cs.AI


> The paper presents ReQUESTA, a hybrid multi-agent framework that leverages large language models (LLMs) to generate cognitively diverse multiple-choice questions (MCQs) focused on various comprehension levels. This framework decomposes MCQ creation into specialized subtasks, coordinating LLM agents with rule-based components for enhanced planning and evaluation. Key findings indicate that ReQUESTA-generated MCQs outperformed those from a single-pass baseline in terms of challenge, discrimination, and alignment with reading comprehension, emphasizing the importance of agentic orchestration in improving the reliability and controllability of educational content generation.


<details>
<summary>Abstract</summary>

Recent advances in large language models (LLMs) have made automated multiple-choice question (MCQ) generation increasingly feasible; however, reliably producing items that satisfy controlled cognitive demands remains a challenge. To address this gap, we introduce ReQUESTA, a hybrid, multi-agent framework for generating cognitively diverse MCQs that systematically target text-based, inferential, and main idea comprehension. ReQUESTA decomposes MCQ authoring into specialized subtasks and coordinates LLM-powered agents with rule-based components to support planning, controlled generation, iterative evaluation, and post-processing. We evaluated the framework in a large-scale reading comprehension study using academic expository texts, comparing ReQUESTA-generated MCQs with those produced by a single-pass GPT-5 zero-shot baseline. Psychometric analyses of learner responses assessed item difficulty and discrimination, while expert raters evaluated question quality across multiple dimensions, including topic relevance and distractor quality. Results showed that ReQUESTA-generated items were consistently more challenging, more discriminative, and more strongly aligned with overall reading comprehension performance. Expert evaluations further indicated stronger alignment with central concepts and superior distractor linguistic consistency and semantic plausibility, particularly for inferential questions. These findings demonstrate that hybrid, agentic orchestration can systematically improve the reliability and controllability of LLM-based generation, highlighting workflow design as a key lever for structured artifact generation beyond single-pass prompting.

</details>


### 85. Agent Primitives: Reusable Latent Building Blocks for Multi-Agent Systems

- **Authors:** Haibo Jin, Kuang Peng, Ye Yu, Xiaopeng Yuan, Haohan Wang
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03695v1](http://arxiv.org/abs/2602.03695v1)
- **PDF:** [https://arxiv.org/pdf/2602.03695v1](https://arxiv.org/pdf/2602.03695v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> The paper introduces "Agent Primitives," a novel approach in multi-agent systems (MAS) that offers reusable latent building blocks to enhance the design and efficiency of agent-based architectures. By decomposing traditional MAS into three key primitives—Review, Voting and Selection, and Planning and Execution—the authors leverage a key-value cache communication mechanism to improve robustness and reduce information degradation in multi-stage interactions. Experimental results indicate that this primitive-based MAS significantly boosts accuracy by 12.0-16.5% over traditional single-agent systems, achieves approximately 3-4 times reduction in token usage and inference latency, and maintains stable performance across different model backbones, thereby advancing the field of agentic AI.


<details>
<summary>Abstract</summary>

While existing multi-agent systems (MAS) can handle complex problems by enabling collaboration among multiple agents, they are often highly task-specific, relying on manually crafted agent roles and interaction prompts, which leads to increased architectural complexity and limited reusability across tasks. Moreover, most MAS communicate primarily through natural language, making them vulnerable to error accumulation and instability in long-context, multi-stage interactions within internal agent histories.
  In this work, we propose \textbf{Agent Primitives}, a set of reusable latent building blocks for LLM-based MAS. Inspired by neural network design, where complex models are built from reusable components, we observe that many existing MAS architectures can be decomposed into a small number of recurring internal computation patterns. Based on this observation, we instantiate three primitives: Review, Voting and Selection, and Planning and Execution. All primitives communicate internally via key-value (KV) cache, which improves both robustness and efficiency by mitigating information degradation across multi-stage interactions. To enable automatic system construction, an Organizer agent selects and composes primitives for each query, guided by a lightweight knowledge pool of previously successful configurations, forming a primitive-based MAS.
  Experiments show that primitives-based MAS improve average accuracy by 12.0-16.5\% over single-agent baselines, reduce token usage and inference latency by approximately 3$\times$-4$\times$ compared to text-based MAS, while incurring only 1.3$\times$-1.6$\times$ overhead relative to single-agent inference and providing more stable performance across model backbones.

</details>


### 86. TodyComm: Task-Oriented Dynamic Communication for Multi-Round LLM-based Multi-Agent System

- **Authors:** Wenzhe Fan, Tommaso Tognoli, Henry Peng Zou, Chunyu Miao, Yibo Wang, Xinhua Zhang
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03688v1](http://arxiv.org/abs/2602.03688v1)
- **PDF:** [https://arxiv.org/pdf/2602.03688v1](https://arxiv.org/pdf/2602.03688v1)
- **Categories:** cs.AI


> The paper presents TodyComm, a task-oriented dynamic communication algorithm designed for multi-round LLM-based multi-agent systems, addressing the limitations of fixed communication topologies that do not adapt to changing agent roles and conditions. Utilizing a behavior-driven approach and optimizing through policy gradients, TodyComm generates collaboration structures that adjust dynamically based on adversarial conditions and communication constraints. Experimental results on various benchmarks show that TodyComm enhances task effectiveness while maintaining efficiency and scalability in communication, contributing valuable insights to the field of agentic AI.


<details>
<summary>Abstract</summary>

Multi-round LLM-based multi-agent systems rely on effective communication structures to support collaboration across rounds. However, most existing methods employ a fixed communication topology during inference, which falls short in many realistic applications where the agents' roles may change \textit{across rounds} due to dynamic adversary, task progression, or time-varying constraints such as communication bandwidth. In this paper, we propose addressing this issue through TodyComm, a \textbf{t}ask-\textbf{o}riented \textbf{dy}namic \textbf{comm}unication algorithm. It produces behavior-driven collaboration topologies that adapt to the dynamics at each round, optimizing the utility for the task through policy gradient. Experiments on five benchmarks demonstrate that under both dynamic adversary and communications budgets, TodyComm delivers superior task effectiveness while retaining token efficiency and scalability.

</details>


### 87. Efficient Investment in Multi-Agent Models of Public Transportation

- **Authors:** Martin Bullinger, Edith Elkind, Kassian Köck
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03687v1](http://arxiv.org/abs/2602.03687v1)
- **PDF:** [https://arxiv.org/pdf/2602.03687v1](https://arxiv.org/pdf/2602.03687v1)
- **Categories:** cs.GT, cs.MA


> This paper presents two multi-agent models for efficiently investing limited resources in public transportation systems, focusing on the challenges of optimizing travel demands and improving travel times. The first model reveals that finding approximately optimal solutions for egalitarian welfare is NP-complete, while the second model offers a polynomial-time algorithm for a fixed number of agents but encounters NP-completeness for varying agent numbers. Key findings indicate significant computational challenges in achieving equitable transportation solutions, highlighting the complex decision-making landscape relevant to agentic AI systems design and optimization.


<details>
<summary>Abstract</summary>

We study two stylized, multi-agent models aimed at investing a limited, indivisible resource in public transportation. In the first model, we face the decision of which potential stops to open along a (e.g., bus) path, given agents' travel demands. While it is known that utilitarian optimal solutions can be identified in polynomial time, we find that computing approximately optimal solutions with respect to egalitarian welfare is NP-complete. This is surprising as we operate on the simple topology of a line graph.
  In the second model, agents navigate a more complex network modeled by a weighted graph where edge weights represent distances. We face the decision of improving travel time along a fixed number of edges. We provide a polynomial-time algorithm that combines Dijkstra's algorithm with a dynamical program to find the optimal decision for one or two agents. By contrast, if the number of agents is variable, we find \np-completeness and inapproximability results for utilitarian and egalitarian welfare. Moreover, we demonstrate implications of our results for a related model of railway network design.

</details>


### 88. Can LLMs Do Rocket Science? Exploring the Limits of Complex Reasoning with GTOC 12

- **Authors:** Iñaki del Campo, Pablo Cuervo, Victor Rodriguez-Fernandez, Roberto Armellin, Jack Yarndley
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03630v1](http://arxiv.org/abs/2602.03630v1)
- **PDF:** [https://arxiv.org/pdf/2602.03630v1](https://arxiv.org/pdf/2602.03630v1)
- **Categories:** cs.AI


> The paper explores the capabilities of Large Language Models (LLMs) in autonomous multi-stage planning within the context of the 12th Global Trajectory Optimization Competition (GTOC 12), which centers on designing an asteroid mining campaign. Utilizing the MLE-Bench framework and an AIDE-based agent architecture, the study assesses model performance through an innovative "LLM-as-a-Judge" methodology, revealing that while strategic viability scores have significantly improved, a critical gap persists between strategy formulation and execution. The findings indicate that current LLMs exhibit impressive conceptual understanding but struggle with practical implementation challenges, underscoring their role as domain facilitators rather than fully autonomous agents in complex reasoning tasks.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have demonstrated remarkable proficiency in code generation and general reasoning, yet their capacity for autonomous multi-stage planning in high-dimensional, physically constrained environments remains an open research question. This study investigates the limits of current AI agents by evaluating them against the 12th Global Trajectory Optimization Competition (GTOC 12), a complex astrodynamics challenge requiring the design of a large-scale asteroid mining campaign. We adapt the MLE-Bench framework to the domain of orbital mechanics and deploy an AIDE-based agent architecture to autonomously generate and refine mission solutions. To assess performance beyond binary validity, we employ an "LLM-as-a-Judge" methodology, utilizing a rubric developed by domain experts to evaluate strategic viability across five structural categories. A comparative analysis of models, ranging from GPT-4-Turbo to reasoning-enhanced architectures like Gemini 2.5 Pro, and o3, reveals a significant trend: the average strategic viability score has nearly doubled in the last two years (rising from 9.3 to 17.2 out of 26). However, we identify a critical capability gap between strategy and execution. While advanced models demonstrate sophisticated conceptual understanding, correctly framing objective functions and mission architectures, they consistently fail at implementation due to physical unit inconsistencies, boundary condition errors, and inefficient debugging loops. We conclude that, while current LLMs often demonstrate sufficient knowledge and intelligence to tackle space science tasks, they remain limited by an implementation barrier, functioning as powerful domain facilitators rather than fully autonomous engineers.

</details>


### 89. Learning Query-Specific Rubrics from Human Preferences for DeepResearch Report Generation

- **Authors:** Changze Lv, Jie Zhou, Wentao Zhao, Jingwen Xu, Zisu Huang, Muzhao Tian, Shihan Dou, Tao Gui, Le Tian, Xiao Zhou, Xiaoqing Zheng, Xuanjing Huang, Jie Zhou
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03619v1](http://arxiv.org/abs/2602.03619v1)
- **PDF:** [https://arxiv.org/pdf/2602.03619v1](https://arxiv.org/pdf/2602.03619v1)
- **Categories:** cs.CL


> The paper presents a novel approach for generating query-specific rubrics aligned with human preferences to improve the evaluation of DeepResearch report generation. The methodology involves creating a dataset of queries annotated with human preferences, training rubric generators using reinforcement learning, and leveraging a Multi-agent Markov-state (MaMs) workflow for effective long-horizon reasoning in report generation. Key findings indicate that the proposed rubric generators offer more effective supervision than traditional methods and, when combined with the MaMs framework, enable DeepResearch systems to surpass open-source benchmarks and achieve performance similar to leading closed-source models, which is crucial for advancing agentic AI capabilities in report generation.


<details>
<summary>Abstract</summary>

Nowadays, training and evaluating DeepResearch-generated reports remain challenging due to the lack of verifiable reward signals. Accordingly, rubric-based evaluation has become a common practice. However, existing approaches either rely on coarse, pre-defined rubrics that lack sufficient granularity, or depend on manually constructed query-specific rubrics that are costly and difficult to scale. In this paper, we propose a pipeline to train human-preference-aligned query-specific rubric generators tailored for DeepResearch report generation. We first construct a dataset of DeepResearch-style queries annotated with human preferences over paired reports, and train rubric generators via reinforcement learning with a hybrid reward combining human preference supervision and LLM-based rubric evaluation. To better handle long-horizon reasoning, we further introduce a Multi-agent Markov-state (MaMs) workflow for report generation. We empirically show that our proposed rubric generators deliver more discriminative and better human-aligned supervision than existing rubric design strategies. Moreover, when integrated into the MaMs training framework, DeepResearch systems equipped with our rubric generators consistently outperform all open-source baselines on the DeepResearch Bench and achieve performance comparable to that of leading closed-source models.

</details>


### 90. Don't believe everything you read: Understanding and Measuring MCP Behavior under Misleading Tool Descriptions

- **Authors:** Zhihao Li, Boyang Ma, Xuelong Dai, Minghui Xu, Yue Zhang, Biwei Yan, Kun Li
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03580v1](http://arxiv.org/abs/2602.03580v1)
- **PDF:** [https://arxiv.org/pdf/2602.03580v1](https://arxiv.org/pdf/2602.03580v1)
- **Categories:** cs.CR, cs.AI


> The paper presents a comprehensive analysis of the Model Context Protocol (MCP) in AI agents, highlighting the critical issue of inconsistencies between tool descriptions and their actual implementations, which can pose significant security risks. The authors developed an automated static analysis framework to examine over 10,000 MCP Servers, revealing that about 13% exhibited substantial mismatches, potentially allowing for unauthorized actions or mutations. These findings underscore a prevalent vulnerability in MCP-based AI systems and advocate for improved auditing processes and transparency measures in agent design to mitigate these risks.


<details>
<summary>Abstract</summary>

The Model Context Protocol (MCP) enables large language models to invoke external tools through natural-language descriptions, forming the foundation of many AI agent applications. However, MCP does not enforce consistency between documented tool behavior and actual code execution, even though MCP Servers often run with broad system privileges. This gap introduces a largely unexplored security risk. We study how mismatches between externally presented tool descriptions and underlying implementations systematically shape the mental models and decision-making behavior of intelligent agents. Specifically, we present the first large-scale study of description-code inconsistency in the MCP ecosystem. We design an automated static analysis framework and apply it to 10,240 real-world MCP Servers across 36 categories. Our results show that while most servers are highly consistent, approximately 13% exhibit substantial mismatches that can enable undocumented privileged operations, hidden state mutations, or unauthorized financial actions. We further observe systematic differences across application categories, popularity levels, and MCP marketplaces. Our findings demonstrate that description-code inconsistency is a concrete and prevalent attack surface in MCP-based AI agents, and motivate the need for systematic auditing and stronger transparency guarantees in future agent ecosystems.

</details>


### 91. Game-Theoretic and Algorithmic Analyses of Multi-Agent Routing under Crossing Costs

- **Authors:** Tesshu Hanaka, Nikolaos Melissinos, Hirotaka Ono
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03455v1](http://arxiv.org/abs/2602.03455v1)
- **PDF:** [https://arxiv.org/pdf/2602.03455v1](https://arxiv.org/pdf/2602.03455v1)
- **Categories:** cs.MA, cs.CC, cs.GT


> The paper presents a novel framework for Multi-Agent Routing under Crossing Costs, which addresses the challenges of coordinating multiple autonomous agents in asynchronous settings, diverging from traditional centralized control methods. Utilizing a congestion game model with a unique cost function that quantifies the risk of head-on encounters, the authors establish the existence of pure Nash equilibria and propose algorithms for efficient equilibrium finding and crossing cost minimization. Key findings indicate that while minimizing total crossing costs is NP-hard, the authors develop parameterized algorithms that facilitate scalable and risk-aware coordination in decentralized multi-agent systems, advancing the theoretical foundation in agentic AI research.


<details>
<summary>Abstract</summary>

Coordinating the movement of multiple autonomous agents over a shared network is a fundamental challenge in algorithmic robotics, intelligent transportation, and distributed systems. The dominant approach, Multi-Agent Path Finding, relies on centralized control and synchronous collision avoidance, which often requires strict synchronization and guarantees of globally conflict-free execution. This paper introduces the Multi-Agent Routing under Crossing Cost model on mixed graphs, a novel framework tailored to asynchronous settings. In our model, instead of treating conflicts as hard constraints, each agent is assigned a path, and the system is evaluated through a cost function that measures potential head-on encounters. This ``crossing cost'', which is defined as the product of the numbers of agents traversing an edge in opposite directions, quantifies the risk of congestion and delay in decentralized execution.
  Our contributions are both game-theoretic and algorithmic. We model the setting as a congestion game with a non-standard cost function, prove the existence of pure Nash equilibria, and analyze the dynamics leading to them. Equilibria can be found in polynomial time under mild conditions, while the general case is PLS-complete. From an optimization perspective, minimizing the total crossing cost is NP-hard, as the problem generalizes Steiner Orientation. To address this hardness barrier, we design a suite of parameterized algorithms for minimizing crossing cost, with parameters including the number of arcs, edges, agents, and structural graph measures. These yield XP or FPT results depending on the parameter, offering algorithmic strategies for structurally restricted instances. Our framework provides a new theoretical foundation for decentralized multi-agent routing, bridging equilibrium analysis and parameterized complexity to support scalable and risk-aware coordination.

</details>


### 92. A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces

- **Authors:** Mingxuan Du, Benfeng Xu, Chiwei Zhu, Shaohan Wang, Pengyu Wang, Xiaorui Wang, Zhendong Mao
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03442v1](http://arxiv.org/abs/2602.03442v1)
- **PDF:** [https://arxiv.org/pdf/2602.03442v1](https://arxiv.org/pdf/2602.03442v1)
- **Categories:** cs.CL


> The paper introduces A-RAG, a novel Agentic Retrieval-Augmented Generation framework that enhances current RAG systems by allowing models to make independent retrieval decisions through hierarchical retrieval interfaces. This methodology incorporates three retrieval tools—keyword search, semantic search, and chunk read—enabling agents to flexibly search for information at varying levels of granularity. Key findings reveal that A-RAG outperforms existing retrieval methods on multiple open-domain QA benchmarks while using comparable or fewer retrieved tokens, indicating its effective utilization of model capabilities and adaptability to different retrieval tasks in the agentic AI field.


<details>
<summary>Abstract</summary>

Frontier language models have demonstrated strong reasoning and long-horizon tool-use capabilities. However, existing RAG systems fail to leverage these capabilities. They still rely on two paradigms: (1) designing an algorithm that retrieves passages in a single shot and concatenates them into the model's input, or (2) predefining a workflow and prompting the model to execute it step-by-step. Neither paradigm allows the model to participate in retrieval decisions, preventing efficient scaling with model improvements. In this paper, we introduce A-RAG, an Agentic RAG framework that exposes hierarchical retrieval interfaces directly to the model. A-RAG provides three retrieval tools: keyword search, semantic search, and chunk read, enabling the agent to adaptively search and retrieve information across multiple granularities. Experiments on multiple open-domain QA benchmarks show that A-RAG consistently outperforms existing approaches with comparable or lower retrieved tokens, demonstrating that A-RAG effectively leverages model capabilities and dynamically adapts to different RAG tasks. We further systematically study how A-RAG scales with model size and test-time compute. We will release our code and evaluation suite to facilitate future research. Code and evaluation suite are available at https://github.com/Ayanami0730/arag.

</details>


### 93. Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents

- **Authors:** Xiaochi Zhou, Patrick Bulter, Changxuan Yang, Simon D. Rihm, Thitikarn Angkanaporn, Jethro Akroyd, Sebastian Mosbach, Markus Kraft
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03439v1](http://arxiv.org/abs/2602.03439v1)
- **PDF:** [https://arxiv.org/pdf/2602.03439v1](https://arxiv.org/pdf/2602.03439v1)
- **Categories:** cs.AI, cs.IR


> The paper presents ontology-to-tools compilation as a method for integrating formal domain knowledge with large language models (LLMs) in the context of autonomous agents. The authors introduce a framework called the Model Context Protocol (MCP) that facilitates interaction between generative models and symbolic constraints through a structured agent-based workflow. Key findings demonstrate that this approach allows LLM agents to enforce semantic constraints during knowledge generation, significantly streamlining the process of extracting and validating structured knowledge from unstructured scientific texts, while also reducing the need for extensive manual schema and prompt engineering.


<details>
<summary>Abstract</summary>

We introduce ontology-to-tools compilation as a proof-of-principle mechanism for coupling large language models (LLMs) with formal domain knowledge. Within The World Avatar (TWA), ontological specifications are compiled into executable tool interfaces that LLM-based agents must use to create and modify knowledge graph instances, enforcing semantic constraints during generation rather than through post-hoc validation. Extending TWA's semantic agent composition framework, the Model Context Protocol (MCP) and associated agents are integral components of the knowledge graph ecosystem, enabling structured interaction between generative models, symbolic constraints, and external resources. An agent-based workflow translates ontologies into ontology-aware tools and iteratively applies them to extract, validate, and repair structured knowledge from unstructured scientific text. Using metal-organic polyhedra synthesis literature as an illustrative case, we show how executable ontological semantics can guide LLM behaviour and reduce manual schema and prompt engineering, establishing a general paradigm for embedding formal knowledge into generative systems.

</details>


### 94. Socratic-Geo: Synthetic Data Generation and Geometric Reasoning via Multi-Agent Interaction

- **Authors:** Zhengbo Jiao, Shaobo Wang, Zifan Zhang, Wei Wang, Bing Zhao, Hu Wei, Linfeng Zhang
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03414v1](http://arxiv.org/abs/2602.03414v1)
- **PDF:** [https://arxiv.org/pdf/2602.03414v1](https://arxiv.org/pdf/2602.03414v1)
- **Categories:** cs.CV, cs.AI


> The paper presents Socratic-Geo, an innovative framework designed to enhance geometric reasoning in multimodal large language models (MLLMs) by coupling data generation with model learning through multi-agent interaction. It features a Teacher agent that autonomously creates validated image-text pairs using parameterized scripts and reflective feedback, while a Solver agent refines reasoning capabilities through preference learning, and a Generator focuses on developing image generation from "image-code-instruction" triplets. Key findings indicate that Socratic-Geo's methodology allows for effective learning from limited data, achieving significant performance improvements across benchmarks and setting new state-of-the-art results for open-source models in geometric reasoning tasks.


<details>
<summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) have significantly advanced vision-language understanding. However, even state-of-the-art models struggle with geometric reasoning, revealing a critical bottleneck: the extreme scarcity of high-quality image-text pairs. Human annotation is prohibitively expensive, while automated methods fail to ensure fidelity and training effectiveness. Existing approaches either passively adapt to available images or employ inefficient random exploration with filtering, decoupling generation from learning needs. We propose Socratic-Geo, a fully autonomous framework that dynamically couples data synthesis with model learning through multi-agent interaction. The Teacher agent generates parameterized Python scripts with reflective feedback (Reflect for solvability, RePI for visual validity), ensuring image-text pair purity. The Solver agent optimizes reasoning through preference learning, with failure paths guiding Teacher's targeted augmentation. Independently, the Generator learns image generation capabilities on accumulated "image-code-instruction" triplets, distilling programmatic drawing intelligence into visual generation. Starting from only 108 seed problems, Socratic-Solver achieves 49.11 on six benchmarks using one-quarter of baseline data, surpassing strong baselines by 2.43 points. Socratic-Generator achieves 42.4% on GenExam, establishing new state-of-the-art for open-source models, surpassing Seedream-4.0 (39.8%) and approaching Gemini-2.5-Flash-Image (43.1%).

</details>


### 95. Verified Critical Step Optimization for LLM Agents

- **Authors:** Mukai Li, Qingcheng Zeng, Tianqing Fang, Zhenwen Liang, Linfeng Song, Qi Liu, Haitao Mi, Dong Yu
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03412v1](http://arxiv.org/abs/2602.03412v1)
- **PDF:** [https://arxiv.org/pdf/2602.03412v1](https://arxiv.org/pdf/2602.03412v1)
- **Categories:** cs.CL


> The paper introduces Critical Step Optimization (CSO), a novel approach for enhancing the performance of large language model (LLM) agents in complex long-horizon tasks. By focusing on verified critical decision points—where alternative actions significantly influence task outcomes—CSO learns from failed policy trajectories instead of relying on expert demonstrations, thus directly addressing the model's weaknesses. Experimental results indicate that CSO leads to substantial improvements in task performance, with 37% and 26% relative gains over traditional fine-tuning methods, while minimizing the need for supervision during post-training, thereby contributing an efficient verification-based learning paradigm to the agentic AI field.


<details>
<summary>Abstract</summary>

As large language model agents tackle increasingly complex long-horizon tasks, effective post-training becomes critical. Prior work faces fundamental challenges: outcome-only rewards fail to precisely attribute credit to intermediate steps, estimated step-level rewards introduce systematic noise, and Monte Carlo sampling approaches for step reward estimation incur prohibitive computational cost. Inspired by findings that only a small fraction of high-entropy tokens drive effective RL for reasoning, we propose Critical Step Optimization (CSO), which focuses preference learning on verified critical steps, decision points where alternate actions demonstrably flip task outcomes from failure to success. Crucially, our method starts from failed policy trajectories rather than expert demonstrations, directly targeting the policy model's weaknesses. We use a process reward model (PRM) to identify candidate critical steps, leverage expert models to propose high-quality alternatives, then continue execution from these alternatives using the policy model itself until task completion. Only alternatives that the policy successfully executes to correct outcomes are verified and used as DPO training data, ensuring both quality and policy reachability. This yields fine-grained, verifiable supervision at critical decisions while avoiding trajectory-level coarseness and step-level noise. Experiments on GAIA-Text-103 and XBench-DeepSearch show that CSO achieves 37% and 26% relative improvement over the SFT baseline and substantially outperforms other post-training methods, while requiring supervision at only 16% of trajectory steps. This demonstrates the effectiveness of selective verification-based learning for agent post-training.

</details>


### 96. MedSAM-Agent: Empowering Interactive Medical Image Segmentation with Multi-turn Agentic Reinforcement Learning

- **Authors:** Shengyuan Liu, Liuxin Bao, Qi Yang, Wanting Geng, Boyun Zheng, Chenxin Li, Wenting Chen, Houwen Peng, Yixuan Yuan
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03320v1](http://arxiv.org/abs/2602.03320v1)
- **PDF:** [https://arxiv.org/pdf/2602.03320v1](https://arxiv.org/pdf/2602.03320v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces MedSAM-Agent, a novel framework that enhances medical image segmentation by utilizing multi-turn agentic reinforcement learning (RL) to facilitate interactive decision-making. By implementing a hybrid prompting strategy and a two-stage training pipeline, the model learns expert decision heuristics and integrates outcome verification with a clinically-inspired reward design, which optimizes interaction and efficiency. Experimental results across multiple medical modalities reveal that MedSAM-Agent achieves state-of-the-art performance, demonstrating the effectiveness of its approach in the evolving landscape of autonomous medical AI systems.


<details>
<summary>Abstract</summary>

Medical image segmentation is evolving from task-specific models toward generalizable frameworks. Recent research leverages Multi-modal Large Language Models (MLLMs) as autonomous agents, employing reinforcement learning with verifiable reward (RLVR) to orchestrate specialized tools like the Segment Anything Model (SAM). However, these approaches often rely on single-turn, rigid interaction strategies and lack process-level supervision during training, which hinders their ability to fully exploit the dynamic potential of interactive tools and leads to redundant actions. To bridge this gap, we propose MedSAM-Agent, a framework that reformulates interactive segmentation as a multi-step autonomous decision-making process. First, we introduce a hybrid prompting strategy for expert-curated trajectory generation, enabling the model to internalize human-like decision heuristics and adaptive refinement strategies. Furthermore, we develop a two-stage training pipeline that integrates multi-turn, end-to-end outcome verification with a clinical-fidelity process reward design to promote interaction parsimony and decision efficiency. Extensive experiments across 6 medical modalities and 21 datasets demonstrate that MedSAM-Agent achieves state-of-the-art performance, effectively unifying autonomous medical reasoning with robust, iterative optimization. Code is available \href{https://github.com/CUHK-AIM-Group/MedSAM-Agent}{here}.

</details>


### 97. MIRROR: A Multi-Agent Framework with Iterative Adaptive Revision and Hierarchical Retrieval for Optimization Modeling in Operations Research

- **Authors:** Yifan Shi, Jialong Shi, Jiayi Wang, Ye Fan, Jianyong Sun
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03318v2](http://arxiv.org/abs/2602.03318v2)
- **PDF:** [https://arxiv.org/pdf/2602.03318v2](https://arxiv.org/pdf/2602.03318v2)
- **Categories:** cs.CL


> The paper introduces MIRROR, a novel multi-agent framework designed to enhance optimization modeling in Operations Research (OR) by automatically translating natural language problems into mathematical models without requiring fine-tuning. MIRROR employs two key mechanisms: iterative adaptive revision for real-time error correction and hierarchical retrieval for sourcing relevant exemplars, which together facilitate improved model accuracy and reliability. Experimental results demonstrate that MIRROR significantly outperforms existing methodologies on standard OR benchmarks, offering an efficient solution that empowers non-expert users in tackling complex optimization tasks.


<details>
<summary>Abstract</summary>

Operations Research (OR) relies on expert-driven modeling-a slow and fragile process ill-suited to novel scenarios. While large language models (LLMs) can automatically translate natural language into optimization models, existing approaches either rely on costly post-training or employ multi-agent frameworks, yet most still lack reliable collaborative error correction and task-specific retrieval, often leading to incorrect outputs. We propose MIRROR, a fine-tuning-free, end-to-end multi-agent framework that directly translates natural language optimization problems into mathematical models and solver code. MIRROR integrates two core mechanisms: (1) execution-driven iterative adaptive revision for automatic error correction, and (2) hierarchical retrieval to fetch relevant modeling and coding exemplars from a carefully curated exemplar library. Experiments show that MIRROR outperforms existing methods on standard OR benchmarks, with notable results on complex industrial datasets such as IndustryOR and Mamo-ComplexLP. By combining precise external knowledge infusion with systematic error correction, MIRROR provides non-expert users with an efficient and reliable OR modeling solution, overcoming the fundamental limitations of general-purpose LLMs in expert optimization tasks.

</details>


### 98. MeetBench-XL: Calibrated Multi-Dimensional Evaluation and Learned Dual-Policy Agents for Real-Time Meetings

- **Authors:** Yuelin Hu, Jun Xu, Bingcong Lu, Zhengxue Cheng, Hongwei Hu, Ronghua Wu, Li Song
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03285v1](http://arxiv.org/abs/2602.03285v1)
- **PDF:** [https://arxiv.org/pdf/2602.03285v1](https://arxiv.org/pdf/2602.03285v1)
- **Categories:** cs.AI


> The paper introduces MeetBench-XL, a framework designed to evaluate AI agents in real-time meeting environments with realistic operational demands not addressed by existing benchmarks. It presents a grounded dataset, MeetAll, derived from 231 bilingual and multimodal enterprise meetings, along with a multidimensional evaluation protocol that assesses AI performance across various critical dimensions such as cognitive load and task execution. The key contribution is the MeetMaster XL agent, which optimizes query routing through dual policy strategies, demonstrating significant improvements in quality and latency over traditional single model approaches in real-world scenarios.


<details>
<summary>Abstract</summary>

Enterprise meeting environments require AI assistants that handle diverse operational tasks, from rapid fact checking during live discussions to cross meeting analysis for strategic planning, under strict latency, cost, and privacy constraints. Existing meeting benchmarks mainly focus on simplified question answering and fail to reflect real world enterprise workflows, where queries arise organically from multi stakeholder collaboration, span long temporal contexts, and require tool augmented reasoning.
  We address this gap through a grounded dataset and a learned agent framework. First, we introduce MeetAll, a bilingual and multimodal corpus derived from 231 enterprise meetings totaling 140 hours. Questions are injected using an enterprise informed protocol validated by domain expert review and human discriminability studies. Unlike purely synthetic benchmarks, this protocol is grounded in four enterprise critical dimensions: cognitive load, temporal context span, domain expertise, and actionable task execution, calibrated through interviews with stakeholders across finance, healthcare, and technology sectors.
  Second, we propose MeetBench XL, a multi dimensional evaluation protocol aligned with human judgment that measures factual fidelity, intent alignment, response efficiency, structural clarity, and completeness. Third, we present MeetMaster XL, a learned dual policy agent that jointly optimizes query routing between fast and slow reasoning paths and tool invocation, including retrieval, cross meeting aggregation, and web search. A lightweight classifier enables accurate routing with minimal overhead, achieving a superior quality latency tradeoff over single model baselines. Experiments against commercial systems show consistent gains, supported by ablations, robustness tests, and a real world deployment case study.Resources: https://github.com/huyuelin/MeetBench.

</details>


### 99. Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis

- **Authors:** Zhengbo Jiao, Shaobo Wang, Zifan Zhang, Xuan Ren, Wei Wang, Bing Zhao, Hu Wei, Linfeng Zhang
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03279v1](http://arxiv.org/abs/2602.03279v1)
- **PDF:** [https://arxiv.org/pdf/2602.03279v1](https://arxiv.org/pdf/2602.03279v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces the Agentic Proposing framework, which enhances large language model (LLM) reasoning by treating problem synthesis as a goal-driven sequential decision process, allowing an agent to dynamically select and compose modular reasoning skills. Using Multi-Granularity Policy Optimization, the authors develop the Agentic-Proposer-4B, which generates high-precision training data for mathematics, coding, and science, leading to significant improvements in downstream solver performance. Notably, a 30B solver leveraging only 11,000 synthesized trajectories achieved a 91.6% accuracy on the AIME25 benchmark, illustrating that high-quality synthetic data can effectively replace extensive human-curated datasets in agentic AI training.


<details>
<summary>Abstract</summary>

Advancing complex reasoning in large language models relies on high-quality, verifiable datasets, yet human annotation remains cost-prohibitive and difficult to scale. Current synthesis paradigms often face a recurring trade-off: maintaining structural validity typically restricts problem complexity, while relaxing constraints to increase difficulty frequently leads to inconsistent or unsolvable instances. To address this, we propose Agentic Proposing, a framework that models problem synthesis as a goal-driven sequential decision process where a specialized agent dynamically selects and composes modular reasoning skills. Through an iterative workflow of internal reflection and tool-use, we develop the Agentic-Proposer-4B using Multi-Granularity Policy Optimization (MGPO) to generate high-precision, verifiable training trajectories across mathematics, coding, and science. Empirical results demonstrate that downstream solvers trained on agent-synthesized data significantly outperform leading baselines and exhibit robust cross-domain generalization. Notably, a 30B solver trained on only 11,000 synthesized trajectories achieves a state-of-the-art 91.6% accuracy on AIME25, rivaling frontier-scale proprietary models such as GPT-5 and proving that a small volume of high-quality synthetic signals can effectively substitute for massive human-curated datasets.

</details>


### 100. LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios

- **Authors:** Tianyu Chen, Chujia Hu, Ge Gao, Dongrui Liu, Xia Hu, Wenjie Wang
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03255v1](http://arxiv.org/abs/2602.03255v1)
- **PDF:** [https://arxiv.org/pdf/2602.03255v1](https://arxiv.org/pdf/2602.03255v1)
- **Categories:** cs.AI


> The paper presents LPS-Bench, a novel benchmark designed to assess the planning-time safety awareness of computer-use agents (CUAs) in long-horizon tasks across both benign and adversarial scenarios. Utilizing a multi-agent automated data generation pipeline and an LLM-as-a-judge evaluation protocol, the study investigates 65 scenarios encompassing various risk types. Key findings highlight significant shortcomings in the safety behaviors of current CUAs, and the authors propose mitigation strategies to enhance their long-horizon planning capabilities, thus addressing critical risks in agentic AI interactions.


<details>
<summary>Abstract</summary>

Computer-use agents (CUAs) that interact with real computer systems can perform automated tasks but face critical safety risks. Ambiguous instructions may trigger harmful actions, and adversarial users can manipulate tool execution to achieve malicious goals. Existing benchmarks mostly focus on short-horizon or GUI-based tasks, evaluating on execution-time errors but overlooking the ability to anticipate planning-time risks. To fill this gap, we present LPS-Bench, a benchmark that evaluates the planning-time safety awareness of MCP-based CUAs under long-horizon tasks, covering both benign and adversarial interactions across 65 scenarios of 7 task domains and 9 risk types. We introduce a multi-agent automated pipeline for scalable data generation and adopt an LLM-as-a-judge evaluation protocol to assess safety awareness through the planning trajectory. Experiments reveal substantial deficiencies in existing CUAs' ability to maintain safe behavior. We further analyze the risks and propose mitigation strategies to improve long-horizon planning safety in MCP-based CUA systems. We open-source our code at https://github.com/tychenn/LPS-Bench.

</details>


### 101. Beyond Quantity: Trajectory Diversity Scaling for Code Agents

- **Authors:** Guhong Chen, Chenghao Sun, Cheng Fu, Qiyao Wang, Zhihong Huang, Chaopeng Wei, Guangxu Chen, Feiteng Fang, Ahmadreza Argha, Bing Zhao, Xander Xu, Qi Han, Hamid Alinejad-Rokny, Qiang Qu, Binhua Li, Shiwen Ni, Min Yang, Hu Wei, Yongbin Li
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03219v1](http://arxiv.org/abs/2602.03219v1)
- **PDF:** [https://arxiv.org/pdf/2602.03219v1](https://arxiv.org/pdf/2602.03219v1)
- **Categories:** cs.AI


> The paper presents TDScaling, a novel data synthesis framework focused on improving the diversity of training trajectories for code agents, rather than simply increasing the quantity of data. By integrating mechanisms like Business Clustering and an adaptive evolution approach, TDScaling enhances the performance-cost trade-off for training agentic AI, resulting in significant improvements in both tool-use generalization and coding proficiency across various benchmarks. Key findings indicate that increased trajectory diversity leads to greater performance gains compared to traditional quantity-centric scaling methods, addressing the limitations of existing synthetic data approaches in the agentic AI field.


<details>
<summary>Abstract</summary>

As code large language models (LLMs) evolve into tool-interactive agents via the Model Context Protocol (MCP), their generalization is increasingly limited by low-quality synthetic data and the diminishing returns of quantity scaling. Moreover, quantity-centric scaling exhibits an early bottleneck that underutilizes trajectory data. We propose TDScaling, a Trajectory Diversity Scaling-based data synthesis framework for code agents that scales performance through diversity rather than raw volume. Under a fixed training budget, increasing trajectory diversity yields larger gains than adding more trajectories, improving the performance-cost trade-off for agent training. TDScaling integrates four innovations: (1) a Business Cluster mechanism that captures real-service logical dependencies; (2) a blueprint-driven multi-agent paradigm that enforces trajectory coherence; (3) an adaptive evolution mechanism that steers synthesis toward long-tail scenarios using Domain Entropy, Reasoning Mode Entropy, and Cumulative Action Complexity to prevent mode collapse; and (4) a sandboxed code tool that mitigates catastrophic forgetting of intrinsic coding capabilities. Experiments on general tool-use benchmarks (BFCL, tau^2-Bench) and code agent tasks (RebenchT, CodeCI, BIRD) demonstrate a win-win outcome: TDScaling improves both tool-use generalization and inherent coding proficiency. We plan to release the full codebase and the synthesized dataset (including 30,000+ tool clusters) upon publication.

</details>


### 102. Privasis: Synthesizing the Largest "Public" Private Dataset from Scratch

- **Authors:** Hyunwoo Kim, Niloofar Mireshghallah, Michael Duan, Rui Xin, Shuyue Stella Li, Jaehun Jung, David Acuna, Qi Pang, Hanshen Xiao, G. Edward Suh, Sewoong Oh, Yulia Tsvetkov, Pang Wei Koh, Yejin Choi
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03183v1](http://arxiv.org/abs/2602.03183v1)
- **PDF:** [https://arxiv.org/pdf/2602.03183v1](https://arxiv.org/pdf/2602.03183v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces Privasis, the first million-scale fully synthetic dataset, designed to address the scarcity of privacy-sensitive data in AI research, which is crucial given the increasing use of private information by AI agents. The authors utilized a robust methodology to create this expansive dataset, comprising 1.4 million records with a wide variety of document types and extensive annotated attributes. Key findings reveal that their compact sanitization models, trained on Privasis, significantly outperform existing large language models in text sanitization tasks, thereby enhancing research capabilities in privacy-sensitive domains relevant to agentic AI.


<details>
<summary>Abstract</summary>

Research involving privacy-sensitive data has always been constrained by data scarcity, standing in sharp contrast to other areas that have benefited from data scaling. This challenge is becoming increasingly urgent as modern AI agents--such as OpenClaw and Gemini Agent--are granted persistent access to highly sensitive personal information. To tackle this longstanding bottleneck and the rising risks, we present Privasis (i.e., privacy oasis), the first million-scale fully synthetic dataset entirely built from scratch--an expansive reservoir of texts with rich and diverse private information--designed to broaden and accelerate research in areas where processing sensitive social data is inevitable. Compared to existing datasets, Privasis, comprising 1.4 million records, offers orders-of-magnitude larger scale with quality, and far greater diversity across various document types, including medical history, legal documents, financial records, calendars, and text messages with a total of 55.1 million annotated attributes such as ethnicity, date of birth, workplace, etc. We leverage Privasis to construct a parallel corpus for text sanitization with our pipeline that decomposes texts and applies targeted sanitization. Our compact sanitization models (<=4B) trained on this dataset outperform state-of-the-art large language models, such as GPT-5 and Qwen-3 235B. We plan to release data, models, and code to accelerate future research on privacy-sensitive domains and agents.

</details>


### 103. Internet of Agentic AI: Incentive-Compatible Distributed Teaming and Workflow

- **Authors:** Ya-Ting Yang, Quanyan Zhu
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03145v1](http://arxiv.org/abs/2602.03145v1)
- **PDF:** [https://arxiv.org/pdf/2602.03145v1](https://arxiv.org/pdf/2602.03145v1)
- **Categories:** cs.GT, cs.AI, cs.MA


> The paper presents the "Internet of Agentic AI," a framework designed to enable scalable and decentralized agentic intelligence by allowing heterogeneous agents to form dynamic coalitions for task-oriented workflows. The authors introduce a network-native model of collaboration that incorporates an incentive-compatible framework for coalition feasibility, addressing capability coverage, network locality, and economic viability, and propose a decentralized coalition formation algorithm to enhance coordination. A case study in healthcare demonstrates the framework's potential for achieving specialization and resilience in agentic workflows, marking a significant advance in scalable coordination within the agentic AI domain.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have enabled a new class of agentic AI systems that reason, plan, and act by invoking external tools. However, most existing agentic architectures remain centralized and monolithic, limiting scalability, specialization, and interoperability. This paper proposes a framework for scalable agentic intelligence, termed the Internet of Agentic AI, in which autonomous, heterogeneous agents distributed across cloud and edge infrastructure dynamically form coalitions to execute task-driven workflows. We formalize a network-native model of agentic collaboration and introduce an incentive-compatible workflow-coalition feasibility framework that integrates capability coverage, network locality, and economic implementability. To enable scalable coordination, we formulate a minimum-effort coalition selection problem and propose a decentralized coalition formation algorithm. The proposed framework can operate as a coordination layer above the Model Context Protocol (MCP). A healthcare case study demonstrates how domain specialization, cloud-edge heterogeneity, and dynamic coalition formation enable scalable, resilient, and economically viable agentic workflows. This work lays the foundation for principled coordination and scalability in the emerging era of Internet of Agentic AI.

</details>


### 104. Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis

- **Authors:** Abdelghny Orogat, Ana Rostam, Essam Mansour
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03128v1](http://arxiv.org/abs/2602.03128v1)
- **PDF:** [https://arxiv.org/pdf/2602.03128v1](https://arxiv.org/pdf/2602.03128v1)
- **Categories:** cs.AI


> The paper presents a unified benchmark and systematic analysis of multi-agent frameworks powered by large language models (LLMs), addressing the critical gaps in understanding how architectural choices affect performance metrics such as latency, accuracy, and scalability. The authors introduce an architectural taxonomy to evaluate these frameworks and develop MAFBench, an evaluation suite that standardizes measurements across different capabilities. Key findings reveal that architectural choices can lead to significant performance variances, influencing planning accuracy and coordination success, which are essential considerations for advancing agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent LLM frameworks are widely used to accelerate the development of agent systems powered by large language models (LLMs). These frameworks impose distinct architectural structures that govern how agents interact, store information, and coordinate tasks. However, their impact on system performance remains poorly understood. This gap is critical, as architectural choices alone can induce order-of-magnitude differences in latency and throughput, as well as substantial variation in accuracy and scalability. Addressing this challenge requires (i) jointly evaluating multiple capabilities, such as orchestration overhead, memory behavior, planning, specialization, and coordination, and (ii) conducting these evaluations under controlled, framework-level conditions to isolate architectural effects. Existing benchmarks focus on individual capabilities and lack standardized framework-level evaluation. We address these limitations by (i) introducing an architectural taxonomy for systematically comparing multi-agent LLM frameworks along fundamental dimensions, and (ii) developing MAFBench, a unified evaluation suite that integrates existing benchmarks under a standardized execution pipeline. Using MAFBench, we conduct a controlled empirical study across several widely used frameworks. Our results show that framework-level design choices alone can increase latency by over 100x, reduce planning accuracy by up to 30%, and lower coordination success from above 90% to below 30%. Finally, we translate our findings into concrete architectural design principles and framework selection guidance, and outline promising future research directions.

</details>


### 105. One Model, All Roles: Multi-Turn, Multi-Agent Self-Play Reinforcement Learning for Conversational Social Intelligence

- **Authors:** Bowen Jiang, Taiwei Shi, Ryo Kamoi, Yuan Yuan, Camillo J. Taylor, Longqi Yang, Pei Zhou, Sihao Chen
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03109v1](http://arxiv.org/abs/2602.03109v1)
- **PDF:** [https://arxiv.org/pdf/2602.03109v1](https://arxiv.org/pdf/2602.03109v1)
- **Categories:** cs.CL


> The paper presents OMAR (One Model, All Roles), a reinforcement learning framework that enhances AI's social intelligence through multi-turn, multi-agent conversational self-play, allowing a single model to simulate all participants in a dialogue to learn complex social interactions. Utilizing hierarchical advantage estimation for training stability, evaluations in SOTOPIA and Werewolf games reveal that models display emergent social skills like empathy and persuasion, even in competitive settings. The findings highlight the potential for AI to learn sophisticated social behaviors autonomously, encouraging further exploration into AI's capabilities in group conversational contexts.


<details>
<summary>Abstract</summary>

This paper introduces OMAR: One Model, All Roles, a reinforcement learning framework that enables AI to develop social intelligence through multi-turn, multi-agent conversational self-play. Unlike traditional paradigms that rely on static, single-turn optimizations, OMAR allows a single model to role-play all participants in a conversation simultaneously, learning to achieve long-term goals and complex social norms directly from dynamic social interaction. To ensure training stability across long dialogues, we implement a hierarchical advantage estimation that calculates turn-level and token-level advantages. Evaluations in the SOTOPIA social environment and Werewolf strategy games show that our trained models develop fine-grained, emergent social intelligence, such as empathy, persuasion, and compromise seeking, demonstrating the effectiveness of learning collaboration even under competitive scenarios. While we identify practical challenges like reward hacking, our results show that rich social intelligence can emerge without human supervision. We hope this work incentivizes further research on AI social intelligence in group conversations.

</details>


### 106. MAS-ProVe: Understanding the Process Verification of Multi-Agent Systems

- **Authors:** Vishal Venkataramani, Haizhou Shi, Zixuan Ke, Austin Xu, Xiaoxiao He, Yingbo Zhou, Semih Yavuz, Hao Wang, Shafiq Joty
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03053v1](http://arxiv.org/abs/2602.03053v1)
- **PDF:** [https://arxiv.org/pdf/2602.03053v1](https://arxiv.org/pdf/2602.03053v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> The paper introduces MAS-ProVe, a systematic empirical study that investigates process verification methodologies for Multi-Agent Systems (MAS) utilizing Large Language Models (LLMs). The study evaluates three verification approaches, across multiple granularity levels and diverse MAS frameworks, revealing that process verification often yields variable performance improvements, with LLM-as-a-Judge generally outperforming reward-based methods. Key findings indicate the need for further advancements in process verification techniques, as consistent and reliable evaluation of multi-agent trajectories remains a significant challenge within the agentic AI field.


<details>
<summary>Abstract</summary>

Multi-Agent Systems (MAS) built on Large Language Models (LLMs) often exhibit high variance in their reasoning trajectories. Process verification, which evaluates intermediate steps in trajectories, has shown promise in general reasoning settings, and has been suggested as a potential tool for guiding coordination of MAS; however, its actual effectiveness in MAS remains unclear. To fill this gap, we present MAS-ProVe, a systematic empirical study of process verification for multi-agent systems (MAS). Our study spans three verification paradigms (LLM-as-a-Judge, reward models, and process reward models), evaluated across two levels of verification granularity (agent-level and iteration-level). We further examine five representative verifiers and four context management strategies, and conduct experiments over six diverse MAS frameworks on multiple reasoning benchmarks. We find that process-level verification does not consistently improve performance and frequently exhibits high variance, highlighting the difficulty of reliably evaluating partial multi-agent trajectories. Among the methods studied, LLM-as-a-Judge generally outperforms reward-based approaches, with trained judges surpassing general-purpose LLMs. We further observe a small performance gap between LLMs acting as judges and as single agents, and identify a context-length-performance trade-off in verification. Overall, our results suggest that effective and robust process verification for MAS remains an open challenge, requiring further advances beyond current paradigms. Code is available at https://github.com/Wang-ML-Lab/MAS-ProVe.

</details>


### 107. Unified Inference Framework for Single and Multi-Player Performative Prediction: Method and Asymptotic Optimality

- **Authors:** Zhixian Zhang, Xiaotian Hou, Linjun Zhang
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03049v1](http://arxiv.org/abs/2602.03049v1)
- **PDF:** [https://arxiv.org/pdf/2602.03049v1](https://arxiv.org/pdf/2602.03049v1)
- **Categories:** stat.ML, cs.LG, math.ST, stat.ME


> This paper presents a unified statistical inference framework for both single and multi-agent performative prediction, a setting where predictive models influence the data distributions they aim to forecast. The authors introduce the Repeated Risk Minimization (RRM) procedure for estimating performative stability and a two-step plug-in estimator that combines Recalibrated Prediction Powered Inference (RePPI) with Importance Sampling, demonstrating asymptotic normality and efficiency under mild misspecifications. Their contributions offer a robust methodology for reliable estimation and decision-making in dynamic environments, advancing the field of agentic AI by addressing the complexities of interdependent agent interactions.


<details>
<summary>Abstract</summary>

Performative prediction characterizes environments where predictive models alter the very data distributions they aim to forecast, triggering complex feedback loops. While prior research treats single-agent and multi-agent performativity as distinct phenomena, this paper introduces a unified statistical inference framework that bridges these contexts, treating the former as a special case of the latter. Our contribution is two-fold. First, we put forward the Repeated Risk Minimization (RRM) procedure for estimating the performative stability, and establish a rigorous inferential theory for admitting its asymptotic normality and confirming its asymptotic efficiency. Second, for the performative optimality, we introduce a novel two-step plug-in estimator that integrates the idea of Recalibrated Prediction Powered Inference (RePPI) with Importance Sampling, and further provide formal derivations for the Central Limit Theorems of both the underlying distributional parameters and the plug-in results. The theoretical analysis demonstrates that our estimator achieves the semiparametric efficiency bound and maintains robustness under mild distributional misspecification. This work provides a principled toolkit for reliable estimation and decision-making in dynamic, performative environments.

</details>


### 108. LatentMem: Customizing Latent Memory for Multi-Agent Systems

- **Authors:** Muxin Fu, Guibin Zhang, Xiangyuan Xue, Yafu Li, Zefeng He, Siyuan Huang, Xiaoye Qu, Yu Cheng, Yang Yang
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03036v1](http://arxiv.org/abs/2602.03036v1)
- **PDF:** [https://arxiv.org/pdf/2602.03036v1](https://arxiv.org/pdf/2602.03036v1)
- **Categories:** cs.CL, cs.LG, cs.MA


> The paper introduces LatentMem, a novel framework for customizing latent memory in multi-agent systems (MAS) to overcome issues of memory homogenization and information overload. It employs an experience bank to store interaction data and a memory composer to create agent-specific compact memories, enhanced by the Latent Memory Policy Optimization (LMPO) technique that optimizes memory utility while remaining token-efficient. The key findings reveal that LatentMem significantly improves performance, achieving up to 19.36% gains over traditional methods across various benchmarks, highlighting its effectiveness in enhancing the adaptability and intelligence of LLM-powered MAS.


<details>
<summary>Abstract</summary>

Large language model (LLM)-powered multi-agent systems (MAS) demonstrate remarkable collective intelligence, wherein multi-agent memory serves as a pivotal mechanism for continual adaptation. However, existing multi-agent memory designs remain constrained by two fundamental bottlenecks: (i) memory homogenization arising from the absence of role-aware customization, and (ii) information overload induced by excessively fine-grained memory entries. To address these limitations, we propose LatentMem, a learnable multi-agent memory framework designed to customize agent-specific memories in a token-efficient manner. Specifically, LatentMem comprises an experience bank that stores raw interaction trajectories in a lightweight form, and a memory composer that synthesizes compact latent memories conditioned on retrieved experience and agent-specific contexts. Further, we introduce Latent Memory Policy Optimization (LMPO), which propagates task-level optimization signals through latent memories to the composer, encouraging it to produce compact and high-utility representations. Extensive experiments across diverse benchmarks and mainstream MAS frameworks show that LatentMem achieves a performance gain of up to $19.36$% over vanilla settings and consistently outperforms existing memory architectures, without requiring any modifications to the underlying frameworks.

</details>


### 109. Visual Reasoning over Time Series via Multi-Agent System

- **Authors:** Weilin Ruan, Yuxuan Liang
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03026v1](http://arxiv.org/abs/2602.03026v1)
- **PDF:** [https://arxiv.org/pdf/2602.03026v1](https://arxiv.org/pdf/2602.03026v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces MAS4TS, a novel multi-agent system designed to enhance time series analysis by integrating visual reasoning and adaptive tool usage within a unified framework. Utilizing an Analyzer-Reasoner-Executor paradigm, MAS4TS employs a Vision-Language Model to extract temporal structures from time series plots and involves three specialized agents communicating through shared memory for efficient task execution. The extensive evaluation shows MAS4TS not only achieves state-of-the-art performance across various benchmarks but also demonstrates notable generalization capabilities in the context of agentic AI.


<details>
<summary>Abstract</summary>

Time series analysis underpins many real-world applications, yet existing time-series-specific methods and pretrained large-model-based approaches remain limited in integrating intuitive visual reasoning and generalizing across tasks with adaptive tool usage. To address these limitations, we propose MAS4TS, a tool-driven multi-agent system for general time series tasks, built upon an Analyzer-Reasoner-Executor paradigm that integrates agent communication, visual reasoning, and latent reconstruction within a unified framework. MAS4TS first performs visual reasoning over time series plots with structured priors using a Vision-Language Model to extract temporal structures, and subsequently reconstructs predictive trajectories in latent space. Three specialized agents coordinate via shared memory and gated communication, while a router selects task-specific tool chains for execution. Extensive experiments on multiple benchmarks demonstrate that MAS4TS achieves state-of-the-art performance across a wide range of time series tasks, while exhibiting strong generalization and efficient inference.

</details>


### 110. RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents

- **Authors:** Haitian Zhong, Jixiu Zhai, Lei Song, Jiang Bian, Qiang Liu, Tieniu Tan
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03025v1](http://arxiv.org/abs/2602.03025v1)
- **PDF:** [https://arxiv.org/pdf/2602.03025v1](https://arxiv.org/pdf/2602.03025v1)
- **Categories:** cs.AI, cs.CL


> The paper presents RC-GRPO (Reward-Conditioned Group Relative Policy Optimization), addressing the challenges of sparse rewards and exploration in multi-turn tool calling for Large Language Models (LLMs). The methodology involves fine-tuning a Reward-Conditioned Trajectory Policy (RCTP) that employs reward goal special tokens to generate diverse, high-quality trajectories, and enhances exploration by sampling varied reward tokens during reinforcement learning. Key findings demonstrate that RC-GRPO significantly outperforms existing methods on the Berkeley Function Calling Leaderboard v4 (BFCLv4), achieving results that surpass even closed-source API models, thus contributing to advancing agentic AI systems in complex task execution scenarios.


<details>
<summary>Abstract</summary>

Multi-turn tool calling is challenging for Large Language Models (LLMs) because rewards are sparse and exploration is expensive. A common recipe, SFT followed by GRPO, can stall when within-group reward variation is low (e.g., more rollouts in a group receive the all 0 or all 1 reward), making the group-normalized advantage uninformative and yielding vanishing updates. To address this problem, we propose RC-GRPO (Reward-Conditioned Group Relative Policy Optimization), which treats exploration as a controllable steering problem via discrete reward tokens. We first fine-tune a Reward-Conditioned Trajectory Policy (RCTP) on mixed-quality trajectories with reward goal special tokens (e.g., <|high_reward|>, <|low_reward|>) injected into the prompts, enabling the model to learn how to generate distinct quality trajectories on demand. Then during RL, we sample diverse reward tokens within each GRPO group and condition rollouts on the sampled token to improve within-group diversity, improving advantage gains. On the Berkeley Function Calling Leaderboard v4 (BFCLv4) multi-turn benchmark, our method yields consistently improved performance than baselines, and the performance on Qwen-2.5-7B-Instruct even surpasses all closed-source API models.

</details>


### 111. STAR: Similarity-guided Teacher-Assisted Refinement for Super-Tiny Function Calling Models

- **Authors:** Jiliang Ni, Jiachen Pu, Zhongyi Yang, Jingfeng Luo, Conggang Hu
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03022v1](http://arxiv.org/abs/2602.03022v1)
- **PDF:** [https://arxiv.org/pdf/2602.03022v1](https://arxiv.org/pdf/2602.03022v1)
- **Categories:** cs.AI


> The paper introduces STAR (Similarity-guided Teacher-Assisted Refinement), a novel framework designed to transfer capabilities from Large Language Models (LLMs) to super-tiny models, thereby addressing issues such as overfitting and training instability. STAR employs two key innovations: Constrained Knowledge Distillation (CKD) to enhance training stability and exploration, and Similarity-guided RL (Sim-RL) to provide a more effective reward mechanism through similarity evaluations. Experimental results showcase that STAR achieves state-of-the-art performance for models under 1 billion parameters, highlighting its potential to create efficient and powerful AI agents by distilling LLM capabilities into smaller architectures.


<details>
<summary>Abstract</summary>

The proliferation of Large Language Models (LLMs) in function calling is pivotal for creating advanced AI agents, yet their large scale hinders widespread adoption, necessitating transferring their capabilities into smaller ones. However, existing paradigms are often plagued by overfitting, training instability, ineffective binary rewards for multi-solution tasks, and the difficulty of synergizing techniques. We introduce STAR: Similarity-guided Teacher-Assisted Refinement, a novel holistic framework that effectively transfers LLMs' capabilities to super-tiny models. STAR consists of two core technical innovations: (1) Constrained Knowledge Distillation (CKD), a training objective that augments top-k forward KL divergence to suppress confidently incorrect predictions, ensuring training stability while preserving exploration capacity for downstream RL. STAR holistically synergizes these strategies within a cohesive training curriculum, enabling super-tiny models to achieve exceptional performance on complex function calling tasks; (2) Similarity-guided RL (Sim-RL), a RL mechanism that introduces a fine-grained, similarity-based reward. This provides a robust, continuous, and rich signal for better policy optimization by evaluating the similarity between generated outputs and the ground truth. Extensive experiments on challenging and renowned benchmarks demonstrate the effectiveness of our method. Our STAR models establish SOTA in their size classes, significantly outperforming baselines. Remarkably, our 0.6B STAR model achieves the best performance among all open models under 1B, surpassing even several well-known open models at a larger scale. STAR demonstrates a training framework that distills capabilities of LLMs into super-tiny models, paving the way for powerful, accessible, and efficient AI agents.

</details>


### 112. CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability

- **Authors:** Xianzhen Luo, Jingyuan Zhang, Shiqi Zhou, Rain Huang, Chuan Xiao, Qingfu Zhu, Zhiyuan Ma, Xing Yue, Yang Yue, Wencong Zeng, Wanxiang Che
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.03012v1](http://arxiv.org/abs/2602.03012v1)
- **PDF:** [https://arxiv.org/pdf/2602.03012v1](https://arxiv.org/pdf/2602.03012v1)
- **Categories:** cs.CR, cs.AI


> The paper presents CVE-Factory, an innovative multi-agent framework that automates the transformation of sparse Common Vulnerabilities and Exposures (CVE) metadata into fully executable tasks, addressing limitations in scalability and data relevancy in code security evaluations. Methodologically, CVE-Factory achieves expert-level task quality, demonstrated by a 95% correctness and 96% fidelity in comparison to human reproductions and shows a verified success rate of 66.2% on current vulnerabilities. Key findings include the development of LiveCVEBench, a comprehensive benchmark of 190 tasks for various programming languages, and the synthesis of over 1,000 training environments that significantly enhance the performance of AI models, marking a substantial advancement in the field of agentic AI related to code security.


<details>
<summary>Abstract</summary>

Evaluating and improving the security capabilities of code agents requires high-quality, executable vulnerability tasks. However, existing works rely on costly, unscalable manual reproduction and suffer from outdated data distributions. To address these, we present CVE-Factory, the first multi-agent framework to achieve expert-level quality in automatically transforming sparse CVE metadata into fully executable agentic tasks. Cross-validation against human expert reproductions shows that CVE-Factory achieves 95\% solution correctness and 96\% environment fidelity, confirming its expert-level quality. It is also evaluated on the latest realistic vulnerabilities and achieves a 66.2\% verified success. This automation enables two downstream contributions. First, we construct LiveCVEBench, a continuously updated benchmark of 190 tasks spanning 14 languages and 153 repositories that captures emerging threats including AI-tooling vulnerabilities. Second, we synthesize over 1,000 executable training environments, the first large-scale scaling of agentic tasks in code security. Fine-tuned Qwen3-32B improves from 5.3\% to 35.8\% on LiveCVEBench, surpassing Claude 4.5 Sonnet, with gains generalizing to Terminal Bench (12.5\% to 31.3\%). We open-source CVE-Factory, LiveCVEBench, Abacus-cve (fine-tuned model), training dataset, and leaderboard. All resources are available at https://github.com/livecvebench/CVE-Factory .

</details>


### 113. CPMobius: Iterative Coach-Player Reasoning for Data-Free Reinforcement Learning

- **Authors:** Ran Li, Zeyuan Liu, Yinghao chen, Bingxiang He, Jiarui Yuan, Zixuan Fu, Weize Chen, Jinyi Hu, Zhiyuan Liu, Maosong Sun
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02979v1](http://arxiv.org/abs/2602.02979v1)
- **PDF:** [https://arxiv.org/pdf/2602.02979v1](https://arxiv.org/pdf/2602.02979v1)
- **Categories:** cs.CL


> The paper introduces CPMöbius, a novel collaborative Coach-Player framework for data-free reinforcement learning aimed at enhancing reasoning models, specifically in the context of large language models. This methodology incorporates a cooperative optimization loop where a Coach provides targeted instructions to a Player, rewarding both roles based on performance improvements without reliance on external training data. The key findings indicate that CPMöbius significantly enhances mathematical reasoning capabilities, achieving superior accuracy compared to existing unsupervised approaches, thereby demonstrating its potential impact in the field of agentic AI.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have demonstrated strong potential in complex reasoning, yet their progress remains fundamentally constrained by reliance on massive high-quality human-curated tasks and labels, either through supervised fine-tuning (SFT) or reinforcement learning (RL) on reasoning-specific data. This dependence renders supervision-heavy training paradigms increasingly unsustainable, with signs of diminishing scalability already evident in practice. To overcome this limitation, we introduce CPMöbius (CPMobius), a collaborative Coach-Player paradigm for data-free reinforcement learning of reasoning models. Unlike traditional adversarial self-play, CPMöbius, inspired by real world human sports collaboration and multi-agent collaboration, treats the Coach and Player as independent but cooperative roles. The Coach proposes instructions targeted at the Player's capability and receives rewards based on changes in the Player's performance, while the Player is rewarded for solving the increasingly instructive tasks generated by the Coach. This cooperative optimization loop is designed to directly enhance the Player's mathematical reasoning ability. Remarkably, CPMöbius achieves substantial improvement without relying on any external training data, outperforming existing unsupervised approaches. For example, on Qwen2.5-Math-7B-Instruct, our method improves accuracy by an overall average of +4.9 and an out-of-distribution average of +5.4, exceeding RENT by +1.5 on overall accuracy and R-zero by +4.2 on OOD accuracy.

</details>


### 114. Co2PO: Coordinated Constrained Policy Optimization for Multi-Agent RL

- **Authors:** Shrenik Patel, Christine Truong
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02970v1](http://arxiv.org/abs/2602.02970v1)
- **PDF:** [https://arxiv.org/pdf/2602.02970v1](https://arxiv.org/pdf/2602.02970v1)
- **Categories:** cs.LG


> The paper introduces Co2PO, a coordinated constrained policy optimization framework designed for multi-agent reinforcement learning (MARL) that addresses the challenge of exploration while ensuring safety compliance through proactive hazard prediction. Utilizing a shared blackboard architecture for risk-aware communication, Co2PO enables agents to anticipate potential violations and navigate hazards more effectively than traditional methods, which often lead to over-conservatism. Experimental results demonstrate that Co2PO outperforms existing constrained baselines in terms of returns while effectively converging to cost-compliant policies, highlighting the importance of elements such as risk-triggered communication and shared memory in its architecture.


<details>
<summary>Abstract</summary>

Constrained multi-agent reinforcement learning (MARL) faces a fundamental tension between exploration and safety-constrained optimization. Existing leading approaches, such as Lagrangian methods, typically rely on global penalties or centralized critics that react to violations after they occur, often suppressing exploration and leading to over-conservatism. We propose Co2PO, a novel MARL communication-augmented framework that enables coordination-driven safety through selective, risk-aware communication. Co2PO introduces a shared blackboard architecture for broadcasting positional intent and yield signals, governed by a learned hazard predictor that proactively forecasts potential violations over an extended temporal horizon. By integrating these forecasts into a constrained optimization objective, Co2PO allows agents to anticipate and navigate collective hazards without the performance trade-offs inherent in traditional reactive constraints. We evaluate Co2PO across a suite of complex multi-agent safety benchmarks, where it achieves higher returns compared to leading constrained baselines while converging to cost-compliant policies at deployment. Ablation studies further validate the necessity of risk-triggered communication, adaptive gating, and shared memory components.

</details>


### 115. Generative Engine Optimization: A VLM and Agent Framework for Pinterest Acquisition Growth

- **Authors:** Faye Zhang, Qianyu Cheng, Jasmine Wan, Vishwakarma Singh, Jinfeng Rao, Kofi Boakye
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02961v1](http://arxiv.org/abs/2602.02961v1)
- **PDF:** [https://arxiv.org/pdf/2602.02961v1](https://arxiv.org/pdf/2602.02961v1)
- **Categories:** cs.AI


> The paper presents a novel framework called Pinterest Generative Engine Optimization (GEO), which leverages Vision-Language Models (VLMs) and AI agents to enhance content discovery on visual platforms. The methodology involves fine-tuning VLMs to predict user search queries based on real-time internet trends, which are then used to create semantically coherent Collection Pages that optimize generative retrieval. Key findings indicate that GEO has successfully achieved a 20% growth in organic traffic and contributed to significant increases in monthly active users, highlighting its effectiveness in adapting to the growing influence of generative search systems in the agentic AI domain.


<details>
<summary>Abstract</summary>

Large Language Models are fundamentally reshaping content discovery through AI-native search systems such as ChatGPT, Gemini, and Claude. Unlike traditional search engines that match keywords to documents, these systems infer user intent, synthesize multimodal evidence, and generate contextual answers directly on the search page, introducing a paradigm shift from Search Engine Optimization (SEO) to Generative Engine Optimization (GEO). For visual content platforms hosting billions of assets, this poses an acute challenge: individual images lack the semantic depth and authority signals that generative search prioritizes, risking disintermediation as user needs are satisfied in-place without site visits.
  We present Pinterest GEO, a production-scale framework that pioneers reverse search design: rather than generating generic image captions describing what content is, we fine-tune Vision-Language Models (VLMs) to predict what users would actually search for, augmented this with AI agents that mine real-time internet trends to capture emerging search demand. These VLM-generated queries then drive construction of semantically coherent Collection Pages via multimodal embeddings, creating indexable aggregations optimized for generative retrieval. Finally, we employ hybrid VLM and two-tower ANN architectures to build authority-aware interlinking structures that propagate signals across billions of visual assets. Deployed at scale across billions of images and tens of millions of collections, GEO delivers 20\% organic traffic growth contributing to multi-million monthly active user (MAU) growth, demonstrating a principled pathway for visual platforms to thrive in the generative search era.

</details>


### 116. Human-Centric Traffic Signal Control for Equity: A Multi-Agent Action Branching Deep Reinforcement Learning Approach

- **Authors:** Xiaocai Zhang, Neema Nassir, Lok Sang Chan, Milad Haghani
- **Published:** 2026-02-03
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02959v1](http://arxiv.org/abs/2602.02959v1)
- **PDF:** [https://arxiv.org/pdf/2602.02959v1](https://arxiv.org/pdf/2602.02959v1)
- **Categories:** cs.LG, eess.SY


> The paper presents MA2B-DDQN, a novel human-centric multi-agent action-branching deep reinforcement learning framework aimed at optimizing traffic signal control with an emphasis on traveler equity. By decomposing the control into local actions for individual intersections and a global action for phase durations, the proposed methodology effectively simplifies decision-making in high-dimensional discrete action spaces. Key findings indicate that this approach significantly reduces the number of delayed travelers across various traffic scenarios in Melbourne, outperforming existing methodologies and showcasing its adaptability for equitable traffic management in urban environments.


<details>
<summary>Abstract</summary>

Coordinating traffic signals along multimodal corridors is challenging because many multi-agent deep reinforcement learning (DRL) approaches remain vehicle-centric and struggle with high-dimensional discrete action spaces. We propose MA2B-DDQN, a human-centric multi-agent action-branching double Deep Q-Network (DQN) framework that explicitly optimizes traveler-level equity. Our key contribution is an action-branching discrete control formulation that decomposes corridor control into (i) local, per-intersection actions that allocate green time between the next two phases and (ii) a single global action that selects the total duration of those phases. This decomposition enables scalable coordination under discrete control while reducing the effective complexity of joint decision-making. We also design a human-centric reward that penalizes the number of delayed individuals in the corridor, accounting for pedestrians, vehicle occupants, and transit passengers. Extensive evaluations across seven realistic traffic scenarios in Melbourne, Australia, demonstrate that our approach significantly reduces the number of impacted travelers, outperforming existing DRL and baseline methods. Experiments confirm the robustness of our model, showing minimal variance across diverse settings. This framework not only advocates for a fairer traffic signal system but also provides a scalable solution adaptable to varied urban traffic conditions.

</details>


### 117. FIRE-Bench: Evaluating Agents on the Rediscovery of Scientific Insights

- **Authors:** Zhen Wang, Fan Bai, Zhongyan Luo, Jinyan Su, Kaiser Sun, Xinle Yu, Jieyuan Liu, Kun Zhou, Claire Cardie, Mark Dredze, Eric P. Xing, Zhiting Hu
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02905v1](http://arxiv.org/abs/2602.02905v1)
- **PDF:** [https://arxiv.org/pdf/2602.02905v1](https://arxiv.org/pdf/2602.02905v1)
- **Categories:** cs.AI


> The paper presents FIRE-Bench, a novel benchmark designed to evaluate autonomous agents' capabilities in rediscovering established scientific insights using a high-level research question as a starting point. Methodologically, agents are required to autonomously explore, design experiments, code, and draw conclusions based on empirical evidence, with performance evaluated on their ability to replicate findings from recent machine learning studies. The key findings indicate that current leading agent systems, despite using advanced LLMs like gpt-5, struggle with full-cycle scientific research, showing limited rediscovery success, high variability in performance, and specific shortcomings in experimental design and evidence-based reasoning, thus highlighting the challenges in agent-driven scientific discovery.


<details>
<summary>Abstract</summary>

Autonomous agents powered by large language models (LLMs) promise to accelerate scientific discovery end-to-end, but rigorously evaluating their capacity for verifiable discovery remains a central challenge. Existing benchmarks face a trade-off: they either heavily rely on LLM-as-judge evaluations of automatically generated research outputs or optimize convenient yet isolated performance metrics that provide coarse proxies for scientific insight. To address this gap, we introduce FIRE-Bench (Full-cycle Insight Rediscovery Evaluation), a benchmark that evaluates agents through the rediscovery of established findings from recent, high-impact machine learning research. Agents are given only a high-level research question extracted from a published, verified study and must autonomously explore ideas, design experiments, implement code, execute their plans, and derive conclusions supported by empirical evidence. We evaluate a range of state-of-the-art agents with frontier LLMs backbones like gpt-5 on FIRE-Bench. Our results show that full-cycle scientific research remains challenging for current agent systems: even the strongest agents achieve limited rediscovery success (<50 F1), exhibit high variance across runs, and display recurring failure modes in experimental design, execution, and evidence-based reasoning. FIRE-Bench provides a rigorous and diagnostic framework for measuring progress toward reliable agent-driven scientific discovery.

</details>


### 118. Spatiotemporal Decision Transformer for Traffic Coordination

- **Authors:** Haoran Su, Yandong Sun, Hanxiao Deng
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02903v1](http://arxiv.org/abs/2602.02903v1)
- **PDF:** [https://arxiv.org/pdf/2602.02903v1](https://arxiv.org/pdf/2602.02903v1)
- **Categories:** cs.LG, cs.AI, eess.SY


> The paper introduces the Multi-Agent Decision Transformer (MADT), a novel framework for optimizing traffic signal control by treating it as a sequence modeling problem to enhance multi-agent coordination and sample efficiency. MADT utilizes a graph attention mechanism to model spatial dependencies, a temporal transformer encoder to capture traffic dynamics, and return-to-go conditioning for performance specification, allowing for effective offline learning from historical data and potential online fine-tuning. Experiments reveal that MADT outperforms existing methods, achieving a 5-6% reduction in average travel time and demonstrating improved coordination amongst intersections.


<details>
<summary>Abstract</summary>

Traffic signal control is a critical challenge in urban transportation, requiring coordination among multiple intersections to optimize network-wide traffic flow. While reinforcement learning has shown promise for adaptive signal control, existing methods struggle with multi-agent coordination and sample efficiency. We introduce MADT (Multi-Agent Decision Transformer), a novel approach that reformulates multi-agent traffic signal control as a sequence modeling problem. MADT extends the Decision Transformer paradigm to multi-agent settings by incorporating: (1) a graph attention mechanism for modeling spatial dependencies between intersections, (2) a|temporal transformer encoder for capturing traffic dynamics, and (3) return-to-go conditioning for target performance specification. Our approach enables offline learning from historical traffic data, with architecture design that facilitates potential online fine-tuning. Experiments on synthetic grid networks and real-world traffic scenarios demonstrate that MADT achieves state-of-the-art performance, reducing average travel time by 5-6% compared to the strongest baseline while exhibiting superior coordination among adjacent intersections.

</details>


### 119. IMAGINE: Intelligent Multi-Agent Godot-based Indoor Networked Exploration

- **Authors:** Tiago Leite, Maria Conceição, António Grilo
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02858v1](http://arxiv.org/abs/2602.02858v1)
- **PDF:** [https://arxiv.org/pdf/2602.02858v1](https://arxiv.org/pdf/2602.02858v1)
- **Categories:** cs.RO, cs.LG, cs.MA, cs.NI, eess.SY


> The paper presents IMAGINE, a novel approach to utilizing Multi-Agent Reinforcement Learning (MARL) in the exploration of GNSS-denied indoor environments by a collaborative group of UAVs, overcoming challenges in coordination and decentralized decision-making. Through high-fidelity simulations in the Godot game engine, the methodology integrates ND-POMDPs, allowing UAVs equipped with LiDAR to navigate and share information under constraints such as limited communication range and bandwidth. Key findings indicate that the combination of a scalable training paradigm and Curriculum Learning enhances cooperative strategies, enabling rapid and robust autonomous exploration, thus laying a foundation for real-world applications in agentic AI systems.


<details>
<summary>Abstract</summary>

The exploration of unknown, Global Navigation Satellite System (GNSS) denied environments by an autonomous communication-aware and collaborative group of Unmanned Aerial Vehicles (UAVs) presents significant challenges in coordination, perception, and decentralized decision-making. This paper implements Multi-Agent Reinforcement Learning (MARL) to address these challenges in a 2D indoor environment, using high-fidelity game-engine simulations (Godot) and continuous action spaces. Policy training aims to achieve emergent collaborative behaviours and decision-making under uncertainty using Network-Distributed Partially Observable Markov Decision Processes (ND-POMDPs). Each UAV is equipped with a Light Detection and Ranging (LiDAR) sensor and can share data (sensor measurements and a local occupancy map) with neighbouring agents. Inter-agent communication constraints include limited range, bandwidth and latency. Extensive ablation studies evaluated MARL training paradigms, reward function, communication system, neural network (NN) architecture, memory mechanisms, and POMDP formulations. This work jointly addresses several key limitations in prior research, namely reliance on discrete actions, single-agent or centralized formulations, assumptions of a priori knowledge and permanent connectivity, inability to handle dynamic obstacles, short planning horizons and architectural complexity in Recurrent NNs/Transformers. Results show that the scalable training paradigm, combined with a simplified architecture, enables rapid autonomous exploration of an indoor area. The implementation of Curriculum-Learning (five increasingly complex levels) also enabled faster, more robust training. This combination of high-fidelity simulation, MARL formulation, and computational efficiency establishes a strong foundation for deploying learned cooperative strategies in physical robotic systems.

</details>


### 120. Joint Learning of Hierarchical Neural Options and Abstract World Model

- **Authors:** Wasu Top Piriyakulkij, Wolfgang Lehrach, Kevin Ellis, Kevin Murphy
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02799v1](http://arxiv.org/abs/2602.02799v1)
- **PDF:** [https://arxiv.org/pdf/2602.02799v1](https://arxiv.org/pdf/2602.02799v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces AgentOWL, a novel approach that jointly learns an abstract world model and hierarchical neural options to improve the sample efficiency of skill acquisition in AI agents. Utilizing this methodology, the authors demonstrate that their method outperforms existing model-free hierarchical reinforcement learning algorithms by enabling the agent to learn a greater variety of skills while requiring significantly less data. The key findings indicate that the joint learning of abstract representations and skills leads to improved performance in task completion within a subset of Object-Centric Atari games, highlighting its relevance for advancing agentic AI capabilities.


<details>
<summary>Abstract</summary>

Building agents that can perform new skills by composing existing skills is a long-standing goal of AI agent research. Towards this end, we investigate how to efficiently acquire a sequence of skills, formalized as hierarchical neural options. However, existing model-free hierarchical reinforcement algorithms need a lot of data. We propose a novel method, which we call AgentOWL (Option and World model Learning Agent), that jointly learns -- in a sample efficient way -- an abstract world model (abstracting across both states and time) and a set of hierarchical neural options. We show, on a subset of Object-Centric Atari games, that our method can learn more skills using much less data than baseline methods.

</details>


### 121. From Task Solving to Robust Real-World Adaptation in LLM Agents

- **Authors:** Pouya Pezeshkpour, Estevam Hruschka
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02760v1](http://arxiv.org/abs/2602.02760v1)
- **PDF:** [https://arxiv.org/pdf/2602.02760v1](https://arxiv.org/pdf/2602.02760v1)
- **Categories:** cs.CL, cs.LG


> The paper addresses the limitations of current evaluations of large language model (LLM) agents, which often assume stable conditions, by introducing a framework that stresses their ability to adapt in real-world deployment scenarios characterized by inconsistencies and uncertainties. The authors benchmarked five state-of-the-art LLM agents in a grid-based game designed to replicate these challenges, revealing significant performance gaps in real-world robustness compared to nominal task-solving capabilities. Key findings indicate that agent performance diminishes with increased complexity of environments, and that agents exhibit adaptive behaviors, suggesting they can infer objectives even in the absence of explicit guidance, thus emphasizing the need for improved methods in verification and objective inference under fluctuating conditions.


<details>
<summary>Abstract</summary>

Large language models are increasingly deployed as specialized agents that plan, call tools, and take actions over extended horizons. Yet many existing evaluations assume a "clean interface" where dynamics are specified and stable, tools and sensors are reliable, and success is captured by a single explicit objective-often overestimating real-world readiness. In practice, agents face underspecified rules, unreliable signals, shifting environments, and implicit, multi-stakeholder goals. The challenge is therefore not just solving tasks, but adapting while solving: deciding what to trust, what is wanted, when to verify, and when to fall back or escalate. We stress-test deployment-relevant robustness under four operational circumstances: partial observability, dynamic environments, noisy signals, and dynamic agent state. We benchmark agentic LLMs in a grid-based game with a simple goal but long-horizon execution. Episodes violate clean-interface assumptions yet remain solvable, forcing agents to infer rules, pay for information, adapt to environmental and internal shifts, and act cautiously under noise. Across five state-of-the-art LLM agents, we find large gaps between nominal task-solving and deployment-like robustness. Performance generally degrades as grid size and horizon increase, but rankings are unstable: weaker models can beat stronger ones when strategy matches the uncertainty regime. Despite no explicit instruction, agents trade off completion, efficiency, and penalty avoidance, suggesting partial objective inference. Ablations and feature analyses reveal model-specific sensitivities and failure drivers, motivating work on verification, safe action selection, and objective inference under partial observability, noise, and non-stationarity.

</details>


### 122. Scaling Small Agents Through Strategy Auctions

- **Authors:** Lisa Alazraki, William F. Shen, Yoram Bachrach, Akhil Mathur
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02751v1](http://arxiv.org/abs/2602.02751v1)
- **PDF:** [https://arxiv.org/pdf/2602.02751v1](https://arxiv.org/pdf/2602.02751v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> The paper presents a significant contribution to the field of agentic AI by introducing the Strategy Auctions for Workload Efficiency (SALE) framework, which enables small language agents to effectively coordinate and optimize their performance for complex tasks. Through empirical analysis, the authors demonstrate that small agents struggle with scaling when faced with increased task complexity, yet the SALE framework significantly reduces the reliance on larger agents by 53% and overall operational costs by 35%, while enhancing performance compared to the largest agents. This study advocates for a shift in perspective towards leveraging coordinated mechanisms for small agents, highlighting a systems-level approach for achieving efficiency and performance in agentic AI rather than merely increasing model size.


<details>
<summary>Abstract</summary>

Small language models are increasingly viewed as a promising, cost-effective approach to agentic AI, with proponents claiming they are sufficiently capable for agentic workflows. However, while smaller agents can closely match larger ones on simple tasks, it remains unclear how their performance scales with task complexity, when large models become necessary, and how to better leverage small agents for long-horizon workloads. In this work, we empirically show that small agents' performance fails to scale with task complexity on deep search and coding tasks, and we introduce Strategy Auctions for Workload Efficiency (SALE), an agent framework inspired by freelancer marketplaces. In SALE, agents bid with short strategic plans, which are scored by a systematic cost-value mechanism and refined via a shared auction memory, enabling per-task routing and continual self-improvement without training a separate router or running all models to completion. Across deep search and coding tasks of varying complexity, SALE reduces reliance on the largest agent by 53%, lowers overall cost by 35%, and consistently improves upon the largest agent's pass@1 with only a negligible overhead beyond executing the final trace. In contrast, established routers that rely on task descriptions either underperform the largest agent or fail to reduce cost -- often both -- underscoring their poor fit for agentic workflows. These results suggest that while small agents may be insufficient for complex workloads, they can be effectively "scaled up" through coordinated task allocation and test-time self-improvement. More broadly, they motivate a systems-level view of agentic AI in which performance gains come less from ever-larger individual models and more from market-inspired coordination mechanisms that organize heterogeneous agents into efficient, adaptive ecosystems.

</details>


### 123. ATLAS : Adaptive Self-Evolutionary Research Agent with Task-Distributed Multi-LLM Supporters

- **Authors:** Ujin Jeon, Jiyong Kwon, Madison Ann Sullivan, Caleb Eunho Lee, Guang Lin
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02709v1](http://arxiv.org/abs/2602.02709v1)
- **PDF:** [https://arxiv.org/pdf/2602.02709v1](https://arxiv.org/pdf/2602.02709v1)
- **Categories:** cs.AI


> The paper introduces ATLAS, an adaptive self-evolutionary research agent that enhances multi-LLM agent systems by incorporating a task-distributed framework, where specialized supporter agents assist in exploration, hyperparameter tuning, and policy management. The proposed method, Evolving Direct Preference Optimization (EvoDPO), allows for iterative updates of the reference policy and is theoretically analyzed in terms of regret under concept drift. Experimental results demonstrate that ATLAS significantly improves stability and performance in challenging scenarios, such as non-stationary linear contextual bandits and scientific machine learning tasks, compared to traditional static baselines, marking a notable advancement in the field of agentic AI.


<details>
<summary>Abstract</summary>

Recent multi-LLM agent systems perform well in prompt optimization and automated problem-solving, but many either keep the solver frozen after fine-tuning or rely on a static preference-optimization loop, which becomes intractable for long-horizon tasks. We propose ATLAS (Adaptive Task-distributed Learning for Agentic Self-evolution), a task-distributed framework that iteratively develops a lightweight research agent while delegating complementary roles to specialized supporter agents for exploration, hyperparameter tuning, and reference policy management. Our core algorithm, Evolving Direct Preference Optimization (EvoDPO), adaptively updates the phase-indexed reference policy. We provide a theoretical regret analysis for a preference-based contextual bandit under concept drift. In addition, experiments were conducted on non-stationary linear contextual bandits and scientific machine learning (SciML) loss reweighting for the 1D Burgers' equation. Both results show that ATLAS improves stability and performance over a static single-agent baseline.

</details>


### 124. AgentRx: Diagnosing AI Agent Failures from Execution Trajectories

- **Authors:** Shraddha Barke, Arnav Goyal, Alind Khare, Avaljot Singh, Suman Nath, Chetan Bansal
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02475v1](http://arxiv.org/abs/2602.02475v1)
- **PDF:** [https://arxiv.org/pdf/2602.02475v1](https://arxiv.org/pdf/2602.02475v1)
- **Categories:** cs.AI


> The paper introduces AgentRx, an automated framework designed to diagnose failures in AI agents by analyzing execution trajectories, contributing significantly to the agentic AI field by providing a systematic approach to failure attribution. The methodology involves annotating a benchmark of 115 failed agent runs across various tasks with critical failure steps and a comprehensive failure taxonomy, which AgentRx uses to synthesize constraints and evaluate them to identify failure points. Key findings indicate that the framework surpasses existing methods by enhancing both the localization of failure steps and the overall attribution process across diverse domains.


<details>
<summary>Abstract</summary>

AI agents often fail in ways that are difficult to localize because executions are probabilistic, long-horizon, multi-agent, and mediated by noisy tool outputs. We address this gap by manually annotating failed agent runs and release a novel benchmark of 115 failed trajectories spanning structured API workflows, incident management, and open-ended web/file tasks. Each trajectory is annotated with a critical failure step and a category from a grounded-theory derived, cross-domain failure taxonomy. To mitigate the human cost of failure attribution, we present AGENTRX, an automated domain-agnostic diagnostic framework that pinpoints the critical failure step in a failed agent trajectory. It synthesizes constraints, evaluates them step-by-step, and produces an auditable validation log of constraint violations with associated evidence; an LLM-based judge uses this log to localize the critical step and category. Our framework improves step localization and failure attribution over existing baselines across three domains.

</details>


### 125. MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents

- **Authors:** Haozhen Zhang, Quanyu Long, Jianzhu Bao, Tao Feng, Weizhi Zhang, Haodong Yue, Wenya Wang
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02474v1](http://arxiv.org/abs/2602.02474v1)
- **PDF:** [https://arxiv.org/pdf/2602.02474v1](https://arxiv.org/pdf/2602.02474v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> The paper presents MemSkill, a novel framework for improving memory management in large language model (LLM) agents by transforming static memory operations into learnable, evolvable memory skills. The methodology involves a closed-loop system comprising a controller for skill selection, an executor for applying these skills, and a designer for refining and evolving the skill set based on performance feedback. Key findings indicate that MemSkill enhances task performance across diverse benchmarks while demonstrating adaptability in memory management, thereby contributing significantly to the field of agentic AI by promoting self-evolving capabilities in memory systems.


<details>
<summary>Abstract</summary>

Most Large Language Model (LLM) agent memory systems rely on a small set of static, hand-designed operations for extracting memory. These fixed procedures hard-code human priors about what to store and how to revise memory, making them rigid under diverse interaction patterns and inefficient on long histories. To this end, we present \textbf{MemSkill}, which reframes these operations as learnable and evolvable memory skills, structured and reusable routines for extracting, consolidating, and pruning information from interaction traces. Inspired by the design philosophy of agent skills, MemSkill employs a \emph{controller} that learns to select a small set of relevant skills, paired with an LLM-based \emph{executor} that produces skill-guided memories. Beyond learning skill selection, MemSkill introduces a \emph{designer} that periodically reviews hard cases where selected skills yield incorrect or incomplete memories, and evolves the skill set by proposing refinements and new skills. Together, MemSkill forms a closed-loop procedure that improves both the skill-selection policy and the skill set itself. Experiments on LoCoMo, LongMemEval, HotpotQA, and ALFWorld demonstrate that MemSkill improves task performance over strong baselines and generalizes well across settings. Further analyses shed light on how skills evolve, offering insights toward more adaptive, self-evolving memory management for LLM agents.

</details>


### 126. Drift-Bench: Diagnosing Cooperative Breakdowns in LLM Agents under Input Faults via Multi-Turn Interaction

- **Authors:** Han Bao, Zheyuan Zhang, Pengcheng Jing, Zhengqing Yuan, Kaiwen Shi, Yanfang Ye
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02455v1](http://arxiv.org/abs/2602.02455v1)
- **PDF:** [https://arxiv.org/pdf/2602.02455v1](https://arxiv.org/pdf/2602.02455v1)
- **Categories:** cs.AI, cs.CL, cs.SE


> The paper introduces Drift-Bench, a pioneering diagnostic benchmark designed to evaluate the performance of Large Language Model (LLM) agents in scenarios involving cooperative breakdowns that arise from flawed user inputs during multi-turn interactions. Utilizing a persona-driven user simulator and grounded in classical communication theories, Drift-Bench categorizes various types of cooperative failures and assesses agent responses in state-oriented and service-oriented environments. Key findings reveal that LLM agents experience significant performance declines when faced with input faults, highlighting the variability in clarification effectiveness across different user personas and fault types, thus bridging the gap between clarification research and agent safety evaluation.


<details>
<summary>Abstract</summary>

As Large Language Models transition to autonomous agents, user inputs frequently violate cooperative assumptions (e.g., implicit intent, missing parameters, false presuppositions, or ambiguous expressions), creating execution risks that text-only evaluations do not capture. Existing benchmarks typically assume well-specified instructions or restrict evaluation to text-only, single-turn clarification, and thus do not measure multi-turn disambiguation under grounded execution risk. We introduce \textbf{Drift-Bench}, the first diagnostic benchmark that evaluates agentic pragmatics under input faults through multi-turn clarification across state-oriented and service-oriented execution environments. Grounded in classical theories of communication, \textbf{Drift-Bench} provides a unified taxonomy of cooperative breakdowns and employs a persona-driven user simulator with the \textbf{Rise} evaluation protocol. Experiments show substantial performance drops under these faults, with clarification effectiveness varying across user personas and fault types. \MethodName bridges clarification research and agent safety evaluation, enabling systematic diagnosis of failures that can lead to unsafe executions.

</details>


### 127. WideSeek: Advancing Wide Research via Multi-Agent Scaling

- **Authors:** Ziyang Huang, Haolin Ren, Xiaowei Yuan, Jiawei Wang, Zhongtao Jiang, Kun Xu, Shizhu He, Jun Zhao, Kang Liu
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02636v1](http://arxiv.org/abs/2602.02636v1)
- **PDF:** [https://arxiv.org/pdf/2602.02636v1](https://arxiv.org/pdf/2602.02636v1)
- **Categories:** cs.CL, cs.AI, cs.IR


> The paper presents WideSeek, a novel multi-agent architecture designed to enhance Wide Research by efficiently retrieving and synthesizing information under complex conditions. The authors introduce WideSeekBench, a robust benchmark for General Broad Information Seeking (GBIS), developed through a multi-phase data pipeline, and propose a unified training framework that employs end-to-end reinforcement learning to optimize multi-agent trajectories. Key findings indicate that scaling the number of agents significantly improves performance in Wide Research tasks, showcasing the potential of multi-agent systems in advancing search intelligence.


<details>
<summary>Abstract</summary>

Search intelligence is evolving from Deep Research to Wide Research, a paradigm essential for retrieving and synthesizing comprehensive information under complex constraints in parallel. However, progress in this field is impeded by the lack of dedicated benchmarks and optimization methodologies for search breadth. To address these challenges, we take a deep dive into Wide Research from two perspectives: Data Pipeline and Agent Optimization. First, we produce WideSeekBench, a General Broad Information Seeking (GBIS) benchmark constructed via a rigorous multi-phase data pipeline to ensure diversity across the target information volume, logical constraints, and domains. Second, we introduce WideSeek, a dynamic hierarchical multi-agent architecture that can autonomously fork parallel sub-agents based on task requirements. Furthermore, we design a unified training framework that linearizes multi-agent trajectories and optimizes the system using end-to-end RL. Experimental results demonstrate the effectiveness of WideSeek and multi-agent RL, highlighting that scaling the number of agents is a promising direction for advancing the Wide Research paradigm.

</details>


### 128. David vs. Goliath: Verifiable Agent-to-Agent Jailbreaking via Reinforcement Learning

- **Authors:** Samuel Nellessen, Tal Kachman
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02395v1](http://arxiv.org/abs/2602.02395v1)
- **PDF:** [https://arxiv.org/pdf/2602.02395v1](https://arxiv.org/pdf/2602.02395v1)
- **Categories:** cs.LG, cs.AI, cs.CR, cs.MA


> The paper presents the Slingshot framework, which employs reinforcement learning to identify and execute Tag-Along Attacks—situations where an adversary exploits a safety-aligned operator's privileges to induce prohibited actions through conversation. Key findings reveal that Slingshot achieves a 67% success rate in eliciting attacks on a specific language model compared to a 1.7% baseline, with successful transfer to several other models, including closed-source and fine-tuned variants. This work establishes a novel threat model in the realm of agentic AI, highlighting the potential vulnerabilities of autonomous agents to adversarial manipulation.


<details>
<summary>Abstract</summary>

The evolution of large language models into autonomous agents introduces adversarial failures that exploit legitimate tool privileges, transforming safety evaluation in tool-augmented environments from a subjective NLP task into an objective control problem. We formalize this threat model as Tag-Along Attacks: a scenario where a tool-less adversary "tags along" on the trusted privileges of a safety-aligned Operator to induce prohibited tool use through conversation alone. To validate this threat, we present Slingshot, a 'cold-start' reinforcement learning framework that autonomously discovers emergent attack vectors, revealing a critical insight: in our setting, learned attacks tend to converge to short, instruction-like syntactic patterns rather than multi-turn persuasion. On held-out extreme-difficulty tasks, Slingshot achieves a 67.0% success rate against a Qwen2.5-32B-Instruct-AWQ Operator (vs. 1.7% baseline), reducing the expected attempts to first success (on solved tasks) from 52.3 to 1.3. Crucially, Slingshot transfers zero-shot to several model families, including closed-source models like Gemini 2.5 Flash (56.0% attack success rate) and defensive-fine-tuned open-source models like Meta-SecAlign-8B (39.2% attack success rate). Our work establishes Tag-Along Attacks as a first-class, verifiable threat model and shows that effective agentic attacks can be elicited from off-the-shelf open-weight models through environment interaction alone.

</details>


### 129. Automated Multiple Mini Interview (MMI) Scoring

- **Authors:** Ryan Huynh, Frank Guerin, Alison Callwood
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02360v1](http://arxiv.org/abs/2602.02360v1)
- **PDF:** [https://arxiv.org/pdf/2602.02360v1](https://arxiv.org/pdf/2602.02360v1)
- **Categories:** cs.CL


> This paper presents a novel multi-agent prompting framework for the automated scoring of Multiple Mini Interviews (MMIs), which emphasizes soft skills assessment and addresses the inconsistencies and biases of human scorers. The methodology involves breaking down the evaluation into two main tasks: transcript refinement and criterion-specific scoring, utilizing a large instruct-tuned model with 3-shot in-context learning, which outperformed traditional fine-tuning methods in terms of scoring accuracy and reliability. Key findings indicate that structured prompt engineering can effectively enhance the performance of Large Language Models in complex subjective reasoning tasks, offering a promising scalable alternative to conventional data-intensive approaches in agentic AI applications.


<details>
<summary>Abstract</summary>

Assessing soft skills such as empathy, ethical judgment, and communication is essential in competitive selection processes, yet human scoring is often inconsistent and biased. While Large Language Models (LLMs) have improved Automated Essay Scoring (AES), we show that state-of-the-art rationale-based fine-tuning methods struggle with the abstract, context-dependent nature of Multiple Mini-Interviews (MMIs), missing the implicit signals embedded in candidate narratives. We introduce a multi-agent prompting framework that breaks down the evaluation process into transcript refinement and criterion-specific scoring. Using 3-shot in-context learning with a large instruct-tuned model, our approach outperforms specialised fine-tuned baselines (Avg QWK 0.62 vs 0.32) and achieves reliability comparable to human experts. We further demonstrate the generalisability of our framework on the ASAP benchmark, where it rivals domain-specific state-of-the-art models without additional training. These findings suggest that for complex, subjective reasoning tasks, structured prompt engineering may offer a scalable alternative to data-intensive fine-tuning, altering how LLMs can be applied to automated assessment.

</details>


### 130. Context Learning for Multi-Agent Discussion

- **Authors:** Xingyuan Hua, Sheng Yue, Xinyi Li, Yizhe Zhao, Jinrui Zhang, Ju Ren
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02350v1](http://arxiv.org/abs/2602.02350v1)
- **PDF:** [https://arxiv.org/pdf/2602.02350v1](https://arxiv.org/pdf/2602.02350v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper presents a novel multi-LLM context learning method (M2CL) designed to enhance the coherence of discussions among multiple large language model (LLM) agents in Multi-Agent Discussion (MAD) scenarios. The methodology involves a context generator for each agent that dynamically refines context instructions throughout the discussion, addressing issues of inconsistency and premature convergence. Key findings indicate that M2CL outperforms existing methods by 20% to 50% across various complex tasks, demonstrating improved performance, transferability, and computational efficiency in agentic AI applications.


<details>
<summary>Abstract</summary>

Multi-Agent Discussion (MAD) has garnered increasing attention very recently, where multiple LLM instances collaboratively solve problems via structured discussion. However, we find that current MAD methods easily suffer from discussion inconsistency, LLMs fail to reach a coherent solution, due to the misalignment between their individual contexts.In this paper, we introduce a multi-LLM context learning method (M2CL) that learns a context generator for each agent, capable of dynamically generating context instructions per discussion round via automatic information organization and refinement. Specifically, inspired by our theoretical insights on the context instruction, M2CL train the generators to control context coherence and output discrepancies via a carefully crafted self-adaptive mechanism.It enables LLMs to avoid premature convergence on majority noise and progressively reach the correct consensus. We evaluate M2CL on challenging tasks, including academic reasoning, embodied tasks, and mobile control. The results show that the performance of M2CL significantly surpasses existing methods by 20%--50%, while enjoying favorable transferability and computational efficiency.

</details>


### 131. Statistical Learning Theory in Lean 4: Empirical Processes from Scratch

- **Authors:** Yuanhe Zhang, Jason D. Lee, Fanghui Liu
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02285v1](http://arxiv.org/abs/2602.02285v1)
- **PDF:** [https://arxiv.org/pdf/2602.02285v1](https://arxiv.org/pdf/2602.02285v1)
- **Categories:** cs.LG, cs.CL, math.ST


> The paper presents a comprehensive formalization of statistical learning theory (SLT) using Lean 4, specifically focusing on empirical process theory. The researchers developed key components, including Gaussian Lipschitz concentration and Dudley's entropy integral theorem, employing a human-AI collaborative workflow where humans created proof strategies and AI assisted in tactical proof execution. Their findings highlight the importance of rigorous formalization in SLT, addressing implicit assumptions and providing a reusable foundation for future advancements in machine learning theory, which is particularly relevant for improving the reliability and correctness of agentic AI systems.


<details>
<summary>Abstract</summary>

We present the first comprehensive Lean 4 formalization of statistical learning theory (SLT) grounded in empirical process theory. Our end-to-end formal infrastructure implement the missing contents in latest Lean 4 Mathlib library, including a complete development of Gaussian Lipschitz concentration, the first formalization of Dudley's entropy integral theorem for sub-Gaussian processes, and an application to least-squares (sparse) regression with a sharp rate. The project was carried out using a human-AI collaborative workflow, in which humans design proof strategies and AI agents execute tactical proof construction, leading to the human-verified Lean 4 toolbox for SLT. Beyond implementation, the formalization process exposes and resolves implicit assumptions and missing details in standard SLT textbooks, enforcing a granular, line-by-line understanding of the theory. This work establishes a reusable formal foundation and opens the door for future developments in machine learning theory. The code is available at https://github.com/YuanheZ/lean-stat-learning-theory

</details>


### 132. Kimi K2.5: Visual Agentic Intelligence

- **Authors:** Kimi Team, Tongtong Bai, Yifan Bai, Yiping Bao, S. H. Cai, Yuan Cao, Y. Charles, H. S. Che, Cheng Chen, Guanduo Chen, Huarong Chen, Jia Chen, Jiahao Chen, Jianlong Chen, Jun Chen, Kefan Chen, Liang Chen, Ruijue Chen, Xinhao Chen, Yanru Chen, Yanxu Chen, Yicun Chen, Yimin Chen, Yingjiang Chen, Yuankun Chen, Yujie Chen, Yutian Chen, Zhirong Chen, Ziwei Chen, Dazhi Cheng, Minghan Chu, Jialei Cui, Jiaqi Deng, Muxi Diao, Hao Ding, Mengfan Dong, Mengnan Dong, Yuxin Dong, Yuhao Dong, Angang Du, Chenzhuang Du, Dikang Du, Lingxiao Du, Yulun Du, Yu Fan, Shengjun Fang, Qiulin Feng, Yichen Feng, Garimugai Fu, Kelin Fu, Hongcheng Gao, Tong Gao, Yuyao Ge, Shangyi Geng, Chengyang Gong, Xiaochen Gong, Zhuoma Gongque, Qizheng Gu, Xinran Gu, Yicheng Gu, Longyu Guan, Yuanying Guo, Xiaoru Hao, Weiran He, Wenyang He, Yunjia He, Chao Hong, Hao Hu, Jiaxi Hu, Yangyang Hu, Zhenxing Hu, Ke Huang, Ruiyuan Huang, Weixiao Huang, Zhiqi Huang, Tao Jiang, Zhejun Jiang, Xinyi Jin, Yu Jing, Guokun Lai, Aidi Li, C. Li, Cheng Li, Fang Li, Guanghe Li, Guanyu Li, Haitao Li, Haoyang Li, Jia Li, Jingwei Li, Junxiong Li, Lincan Li, Mo Li, Weihong Li, Wentao Li, Xinhang Li, Xinhao Li, Yang Li, Yanhao Li, Yiwei Li, Yuxiao Li, Zhaowei Li, Zheming Li, Weilong Liao, Jiawei Lin, Xiaohan Lin, Zhishan Lin, Zichao Lin, Cheng Liu, Chenyu Liu, Hongzhang Liu, Liang Liu, Shaowei Liu, Shudong Liu, Shuran Liu, Tianwei Liu, Tianyu Liu, Weizhou Liu, Xiangyan Liu, Yangyang Liu, Yanming Liu, Yibo Liu, Yuanxin Liu, Yue Liu, Zhengying Liu, Zhongnuo Liu, Enzhe Lu, Haoyu Lu, Zhiyuan Lu, Junyu Luo, Tongxu Luo, Yashuo Luo, Long Ma, Yingwei Ma, Shaoguang Mao, Yuan Mei, Xin Men, Fanqing Meng, Zhiyong Meng, Yibo Miao, Minqing Ni, Kun Ouyang, Siyuan Pan, Bo Pang, Yuchao Qian, Ruoyu Qin, Zeyu Qin, Jiezhong Qiu, Bowen Qu, Zeyu Shang, Youbo Shao, Tianxiao Shen, Zhennan Shen, Juanfeng Shi, Lidong Shi, Shengyuan Shi, Feifan Song, Pengwei Song, Tianhui Song, Xiaoxi Song, Hongjin Su, Jianlin Su, Zhaochen Su, Lin Sui, Jinsong Sun, Junyao Sun, Tongyu Sun, Flood Sung, Yunpeng Tai, Chuning Tang, Heyi Tang, Xiaojuan Tang, Zhengyang Tang, Jiawen Tao, Shiyuan Teng, Chaoran Tian, Pengfei Tian, Ao Wang, Bowen Wang, Chensi Wang, Chuang Wang, Congcong Wang, Dingkun Wang, Dinglu Wang, Dongliang Wang, Feng Wang, Hailong Wang, Haiming Wang, Hengzhi Wang, Huaqing Wang, Hui Wang, Jiahao Wang, Jinhong Wang, Jiuzheng Wang, Kaixin Wang, Linian Wang, Qibin Wang, Shengjie Wang, Shuyi Wang, Si Wang, Wei Wang, Xiaochen Wang, Xinyuan Wang, Yao Wang, Yejie Wang, Yipu Wang, Yiqin Wang, Yucheng Wang, Yuzhi Wang, Zhaoji Wang, Zhaowei Wang, Zhengtao Wang, Zhexu Wang, Zihan Wang, Zizhe Wang, Chu Wei, Ming Wei, Chuan Wen, Zichen Wen, Chengjie Wu, Haoning Wu, Junyan Wu, Rucong Wu, Wenhao Wu, Yuefeng Wu, Yuhao Wu, Yuxin Wu, Zijian Wu, Chenjun Xiao, Jin Xie, Xiaotong Xie, Yuchong Xie, Yifei Xin, Bowei Xing, Boyu Xu, Jianfan Xu, Jing Xu, Jinjing Xu, L. H. Xu, Lin Xu, Suting Xu, Weixin Xu, Xinbo Xu, Xinran Xu, Yangchuan Xu, Yichang Xu, Yuemeng Xu, Zelai Xu, Ziyao Xu, Junjie Yan, Yuzi Yan, Guangyao Yang, Hao Yang, Junwei Yang, Kai Yang, Ningyuan Yang, Ruihan Yang, Xiaofei Yang, Xinlong Yang, Ying Yang, Yi Yang, Yi Yang, Zhen Yang, Zhilin Yang, Zonghan Yang, Haotian Yao, Dan Ye, Wenjie Ye, Zhuorui Ye, Bohong Yin, Chengzhen Yu, Longhui Yu, Tao Yu, Tianxiang Yu, Enming Yuan, Mengjie Yuan, Xiaokun Yuan, Yang Yue, Weihao Zeng, Dunyuan Zha, Haobing Zhan, Dehao Zhang, Hao Zhang, Jin Zhang, Puqi Zhang, Qiao Zhang, Rui Zhang, Xiaobin Zhang, Y. Zhang, Yadong Zhang, Yangkun Zhang, Yichi Zhang, Yizhi Zhang, Yongting Zhang, Yu Zhang, Yushun Zhang, Yutao Zhang, Yutong Zhang, Zheng Zhang, Chenguang Zhao, Feifan Zhao, Jinxiang Zhao, Shuai Zhao, Xiangyu Zhao, Yikai Zhao, Zijia Zhao, Huabin Zheng, Ruihan Zheng, Shaojie Zheng, Tengyang Zheng, Junfeng Zhong, Longguang Zhong, Weiming Zhong, M. Zhou, Runjie Zhou, Xinyu Zhou, Zaida Zhou, Jinguo Zhu, Liya Zhu, Xinhao Zhu, Yuxuan Zhu, Zhen Zhu, Jingze Zhuang, Weiyu Zhuang, Ying Zou, Xinxing Zu
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02276v1](http://arxiv.org/abs/2602.02276v1)
- **PDF:** [https://arxiv.org/pdf/2602.02276v1](https://arxiv.org/pdf/2602.02276v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> The paper presents Kimi K2.5, an open-source multimodal agentic model that combines text and vision to enhance general agentic intelligence through techniques like joint pre-training and reinforcement learning. A significant contribution is the introduction of Agent Swarm, a framework for self-directed parallel orchestration of agents to efficiently address complex tasks, reducing latency by up to 4.5 times compared to single-agent approaches. The extensive evaluations demonstrate that Kimi K2.5 achieves state-of-the-art performance in various domains, thereby advancing the field of agentic AI.


<details>
<summary>Abstract</summary>

We introduce Kimi K2.5, an open-source multimodal agentic model designed to advance general agentic intelligence. K2.5 emphasizes the joint optimization of text and vision so that two modalities enhance each other. This includes a series of techniques such as joint text-vision pre-training, zero-vision SFT, and joint text-vision reinforcement learning. Building on this multimodal foundation, K2.5 introduces Agent Swarm, a self-directed parallel agent orchestration framework that dynamically decomposes complex tasks into heterogeneous sub-problems and executes them concurrently. Extensive evaluations show that Kimi K2.5 achieves state-of-the-art results across various domains including coding, vision, reasoning, and agentic tasks. Agent Swarm also reduces latency by up to $4.5\times$ over single-agent baselines. We release the post-trained Kimi K2.5 model checkpoint to facilitate future research and real-world applications of agentic intelligence.

</details>


### 133. OmniCode: A Benchmark for Evaluating Software Engineering Agents

- **Authors:** Atharv Sonwane, Eng-Shen Tu, Wei-Chung Lu, Claas Beger, Carter Larsen, Debjit Dhar, Simon Alford, Rachel Chen, Ronit Pattanayak, Tuan Anh Dang, Guohao Chen, Gloria Geng, Kevin Ellis, Saikat Dutta
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02262v2](http://arxiv.org/abs/2602.02262v2)
- **PDF:** [https://arxiv.org/pdf/2602.02262v2](https://arxiv.org/pdf/2602.02262v2)
- **Categories:** cs.SE, cs.AI, cs.CL


> The paper introduces OmniCode, a comprehensive benchmark designed to evaluate software engineering agents across a broader range of tasks than existing benchmarks like HumanEval and SWE-Bench, which are limited to specific coding challenges. The methodology includes the manual validation of 1,794 tasks across categories such as bug fixing and test generation, as well as the synthetic generation of these tasks to avoid data leakage. The evaluation of OmniCode with existing agent frameworks, such as SWE-Agent, highlights deficiencies in agent performance for diverse tasks and programming languages, indicating the need for enhanced capabilities in coding agents.


<details>
<summary>Abstract</summary>

LLM-powered coding agents are redefining how real-world software is developed. To drive the research towards better coding agents, we require challenging benchmarks that can rigorously evaluate the ability of such agents to perform various software engineering tasks. However, popular coding benchmarks such as HumanEval and SWE-Bench focus on narrowly scoped tasks such as competition programming and patch generation. In reality, software engineers have to handle a broader set of tasks for real-world software development. To address this gap, we propose OmniCode, a novel software engineering benchmark that contains a broader and more diverse set of task categories beyond code or patch generation. Overall, OmniCode contains 1794 tasks spanning three programming languages (Python, Java, and C++) and four key categories: bug fixing, test generation, code review fixing, and style fixing. In contrast to prior software engineering benchmarks, the tasks in OmniCode are (1) manually validated to eliminate ill-defined problems, and (2) synthetically crafted or recently curated to avoid data leakage issues, presenting a new framework for synthetically generating diverse software tasks from limited real-world data. We evaluate OmniCode with popular agent frameworks such as SWE-Agent and show that while they may perform well on bug fixing for Python, they fall short on tasks such as Test Generation and in languages such as C++ and Java. For instance, SWE-Agent achieves a maximum of 20.9% with DeepSeek-V3.1 on Java Test Generation tasks. OmniCode aims to serve as a robust benchmark and spur the development of agents that can perform well across different aspects of software development. Code and data are available at https://github.com/seal-research/OmniCode.

</details>


### 134. Online Fine-Tuning of Pretrained Controllers for Autonomous Driving via Real-Time Recurrent RL

- **Authors:** Julian Lemmel, Felix Resch, Mónika Farsang, Ramin Hasani, Daniela Rus, Radu Grosu
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02236v2](http://arxiv.org/abs/2602.02236v2)
- **PDF:** [https://arxiv.org/pdf/2602.02236v2](https://arxiv.org/pdf/2602.02236v2)
- **Categories:** cs.RO, cs.LG, cs.NE, eess.SY


> The paper presents a significant advancement in the field of agentic AI by demonstrating the efficacy of Real-Time Recurrent Reinforcement Learning (RTRRL) for online fine-tuning of pretrained controllers in autonomous driving applications. The methodology combines RTRRL with a biologically inspired recurrent network model to adapt existing policies in real-time, addressing challenges posed by changes in environmental dynamics and task objectives. Key findings indicate that this closed-loop approach significantly enhances the performance of autonomous agents, as validated through experiments in both a simulated environment and a real-world driving task, showcasing its potential for improving the robustness of learning-based control systems.


<details>
<summary>Abstract</summary>

Deploying pretrained policies in real-world applications presents substantial challenges that fundamentally limit the practical applicability of learning-based control systems. When autonomous systems encounter environmental changes in system dynamics, sensor drift, or task objectives, fixed policies rapidly degrade in performance. We show that employing Real-Time Recurrent Reinforcement Learning (RTRRL), a biologically plausible algorithm for online adaptation, can effectively fine-tune a pretrained policy to improve autonomous agents' performance on driving tasks. We further show that RTRRL synergizes with a recent biologically inspired recurrent network model, the Liquid-Resistance Liquid-Capacitance RNN. We demonstrate the effectiveness of this closed-loop approach in a simulated CarRacing environment and in a real-world line-following task with a RoboRacer car equipped with an event camera.

</details>


### 135. Fat-Cat: Document-Driven Metacognitive Multi-Agent System for Complex Reasoning

- **Authors:** Tong Yang, Yemin Wang, Chaoning Zhang, Aming Wu
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02206v1](http://arxiv.org/abs/2602.02206v1)
- **PDF:** [https://arxiv.org/pdf/2602.02206v1](https://arxiv.org/pdf/2602.02206v1)
- **Categories:** cs.LG


> The paper presents Fat-Cat, a novel document-driven multi-agent architecture designed to enhance the performance of LLM-based agents in complex reasoning tasks by improving state management through more semantic representations. Its methodology includes a Semantic File System for organizing agent states as Markdown documents, a Textual Strategy Evolution module for knowledge accumulation without parameter updates, and a Closed-Loop Watcher to monitor reasoning processes. The key findings demonstrate that Fat-Cat significantly outperforms existing state representations, such as JSON, particularly shown by the Kimi-k2 model surpassing the proprietary GPT-4o on the HotPotQA benchmark, thus highlighting the importance of document-driven state modeling in AI agents.


<details>
<summary>Abstract</summary>

The effectiveness of LLM-based agents is often limited not by model capacity alone, but by how efficiently contextual information is utilized at runtime. Existing agent frameworks rely on rigid, syntax-heavy state representations such as nested JSON, which require models to devote a substantial portion of their limited attention to syntactic processing rather than semantic reasoning. In this paper, we propose Fat-Cat, a document-driven agent architecture that improves the signal-to-noise ratio of state management. By integrating three key components: (1) a Semantic File System that represents agent state as Markdown documents aligned with common pre-training corpora, (2) a Textual Strategy Evolution module that accumulates task-solving knowledge without parameter updates, and (3) a Closed-Loop Watcher that monitors reasoning trajectories to reduce hallucinations. Extensive reasoning, retrieval, and coding benchmarks, Fat-Cat consistently improves agent performance. It enables the Kimi-k2 model to outperform the proprietary GPT-4o baseline on HotPotQA. Replacing the document-based state with JSON leads to performance drop, while empirically validating the critical necessity of document-driven state modeling over rigid syntax. The code is available at https://github.com/answeryt/Fat-Cat.

</details>


### 136. TIDE: Trajectory-based Diagnostic Evaluation of Test-Time Improvement in LLM Agents

- **Authors:** Hang Yan, Xinyu Che, Fangzhi Xu, Qiushi Sun, Zichen Ding, Kanzhi Cheng, Jian Zhang, Tao Qin, Jun Liu, Qika Lin
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02196v2](http://arxiv.org/abs/2602.02196v2)
- **PDF:** [https://arxiv.org/pdf/2602.02196v2](https://arxiv.org/pdf/2602.02196v2)
- **Categories:** cs.AI


> The paper introduces TIDE, a novel evaluation framework for analyzing Test-Time Improvement (TTI) in autonomous LLM agents, which decomposes TTI into three dimensions: temporal dynamics of task completion, constraints from recursive looping behaviors, and challenges posed by accumulated memory. Utilizing this agent-agnostic and environment-agnostic approach, the authors conduct extensive experiments to establish that optimizing agents' performance involves enhancing their interaction dynamics with the environment, rather than solely focusing on scaling their internal reasoning capabilities. Key findings suggest that understanding these interaction mechanisms is crucial for the effective development of agentic AI systems.


<details>
<summary>Abstract</summary>

Recent advances in autonomous LLM agents demonstrate their ability to improve performance through iterative interaction with the environment. We define this paradigm as Test-Time Improvement (TTI). However, the mechanisms under how and why TTI succeed or fail remain poorly understood, and existing evaluation metrics fail to capture their task optimization efficiency, behavior adaptation after erroneous actions, and the specific utility of working memory for task completion. To address these gaps, we propose Test-time Improvement Diagnostic Evaluation (TIDE), an agent-agnostic and environment-agnostic framework that decomposes TTI into three comprehensive and interconnected dimensions. The framework measures (1) the overall temporal dynamics of task completion and (2) identifies whether performance is primarily constrained by recursive looping behaviors or (3) by burdensome accumulated memory. Through extensive experiments across diverse agents and environments, TIDE highlights that improving agent performance requires more than scaling internal reasoning, calling for explicitly optimizing the interaction dynamics between the agent and the environment.

</details>


### 137. Self-Evolving Coordination Protocol in Multi-Agent AI Systems: An Exploratory Systems Feasibility Study

- **Authors:** Jose Manuel de la Chica Rodriguez, Juan Manuel Vera Díaz
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02170v1](http://arxiv.org/abs/2602.02170v1)
- **PDF:** [https://arxiv.org/pdf/2602.02170v1](https://arxiv.org/pdf/2602.02170v1)
- **Categories:** cs.MA, cs.AI


> This paper presents a feasibility study on Self-Evolving Coordination Protocols (SECP) in multi-agent AI systems, focusing on their ability to self-modify while maintaining formal invariants essential for safety-critical domains. The methodology involves comparing four coordination regimes, including SECP versions, against fixed Byzantine consensus protocols under strict constraints. Key findings indicate that a single governed modification in the SECP framework improved the acceptance of proposals without violating any formal requirements, suggesting that bounded self-modification in coordination mechanisms is both technically feasible and ensures governance, thus advancing the understanding of agentic AI systems.


<details>
<summary>Abstract</summary>

Contemporary multi-agent systems increasingly rely on internal coordination mechanisms to combine, arbitrate, or constrain the outputs of heterogeneous components. In safety-critical and regulated domains such as finance, these mechanisms must satisfy strict formal requirements, remain auditable, and operate within explicitly bounded limits. Coordination logic therefore functions as a governance layer rather than an optimization heuristic.
  This paper presents an exploratory systems feasibility study of Self-Evolving Coordination Protocols (SECP): coordination protocols that permit limited, externally validated self-modification while preserving fixed formal invariants. We study a controlled proof-of-concept setting in which six fixed Byzantine consensus protocol proposals are evaluated by six specialized decision modules. All coordination regimes operate under identical hard constraints, including Byzantine fault tolerance (f < n/3), O(n2) message complexity, complete non-statistical safety and liveness arguments, and bounded explainability.
  Four coordination regimes are compared in a single-shot design: unanimous hard veto, weighted scalar aggregation, SECP v1.0 (an agent-designed non-scalar protocol), and SECP v2.0 (the result of one governed modification). Outcomes are evaluated using a single metric, proposal coverage, defined as the number of proposals accepted. A single recursive modification increased coverage from two to three accepted proposals while preserving all declared invariants.
  The study makes no claims regarding statistical significance, optimality, convergence, or learning. Its contribution is architectural: it demonstrates that bounded self-modification of coordination protocols is technically implementable, auditable, and analyzable under explicit formal constraints, establishing a foundation for governed multi-agent systems.

</details>


### 138. Co-RedTeam: Orchestrated Security Discovery and Exploitation with LLM Agents

- **Authors:** Pengfei He, Ash Fox, Lesly Miculicich, Stefan Friedli, Daniel Fabian, Burak Gokturk, Jiliang Tang, Chen-Yu Lee, Tomas Pfister, Long T. Le
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02164v2](http://arxiv.org/abs/2602.02164v2)
- **PDF:** [https://arxiv.org/pdf/2602.02164v2](https://arxiv.org/pdf/2602.02164v2)
- **Categories:** cs.LG, cs.CR


> The paper introduces Co-RedTeam, a multi-agent framework that enhances cybersecurity by mimicking real-world red-teaming processes and integrating long-term memory, code-aware analysis, and execution-grounded reasoning for vulnerability discovery and exploitation. The methodology involves decomposing the task into coordinated stages that leverage execution feedback and prior experiences, resulting in a more effective approach to vulnerability analysis. Key findings reveal that Co-RedTeam surpasses existing baselines, achieving over 60% success in exploitation and a significant improvement in detection rates, highlighting the importance of structured interactions and memory in developing efficient agentic AI for cybersecurity.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have shown promise in assisting cybersecurity tasks, yet existing approaches struggle with automatic vulnerability discovery and exploitation due to limited interaction, weak execution grounding, and a lack of experience reuse. We propose Co-RedTeam, a security-aware multi-agent framework designed to mirror real-world red-teaming workflows by integrating security-domain knowledge, code-aware analysis, execution-grounded iterative reasoning, and long-term memory. Co-RedTeam decomposes vulnerability analysis into coordinated discovery and exploitation stages, enabling agents to plan, execute, validate, and refine actions based on real execution feedback while learning from prior trajectories. Extensive evaluations on challenging security benchmarks demonstrate that Co-RedTeam consistently outperforms strong baselines across diverse backbone models, achieving over 60% success rate in vulnerability exploitation and over 10% absolute improvement in vulnerability detection. Ablation and iteration studies further confirm the critical role of execution feedback, structured interaction, and memory for building robust and generalizable cybersecurity agents.

</details>


### 139. D-CORE: Incentivizing Task Decomposition in Large Reasoning Models for Complex Tool Use

- **Authors:** Bowen Xu, Shaoyu Wu, Hao Jiang, Kai Liu, Xin Chen, Lulu Hu, Bin Yang
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02160v1](http://arxiv.org/abs/2602.02160v1)
- **PDF:** [https://arxiv.org/pdf/2602.02160v1](https://arxiv.org/pdf/2602.02160v1)
- **Categories:** cs.CL


> The paper introduces D-CORE, a two-stage training framework designed to enhance the task decomposition abilities of large reasoning models (LRMs) for effective tool use in complex scenarios. The methodology involves first using self-distillation to incentivize task decomposition, followed by diversity-aware reinforcement learning to improve reflective reasoning. Key findings indicate that D-CORE significantly improves performance on various benchmarks, achieving state-of-the-art accuracy with models that are smaller than existing top-performing models, thus advancing capabilities in agentic AI for complex tool use.


<details>
<summary>Abstract</summary>

Effective tool use and reasoning are essential capabilities for large reasoning models~(LRMs) to address complex real-world problems. Through empirical analysis, we identify that current LRMs lack the capability of sub-task decomposition in complex tool use scenarios, leading to Lazy Reasoning. To address this, we propose a two-stage training framework D-CORE~(\underline{\textbf{D}}ecomposing tasks and \underline{\textbf{Co}}mposing \underline{\textbf{Re}}asoning processes) that first incentivize the LRMs' task decomposition reasoning capability via self-distillation, followed by diversity-aware reinforcement learning~(RL) to restore LRMs' reflective reasoning capability. D-CORE achieves robust tool-use improvements across diverse benchmarks and model scales. Experiments on BFCLv3 demonstrate superiority of our method: D-CORE-8B reaches 77.7\% accuracy, surpassing the best-performing 8B model by 5.7\%. Meanwhile, D-CORE-14B establishes a new state-of-the-art at 79.3\%, outperforming 70B models despite being 5$\times$ smaller. The source code is available at https://github.com/alibaba/EfficientAI.

</details>


### 140. CAM: A Causality-based Analysis Framework for Multi-Agent Code Generation Systems

- **Authors:** Lyu Zongyi, Ji Zhenlan, Chen Songqiang, Wang Liwen, Huang Yuheng, Wang Shuai, Cheung Shing-Chi
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02138v1](http://arxiv.org/abs/2602.02138v1)
- **PDF:** [https://arxiv.org/pdf/2602.02138v1](https://arxiv.org/pdf/2602.02138v1)
- **Categories:** cs.SE, cs.AI


> The paper presents CAM, a novel causality-based analysis framework that quantifies the importance of intermediate outputs in Multi-Agent Code Generation Systems (MACGS) to enhance system correctness and optimization. Methodologically, CAM categorizes intermediate outputs and simulates errors to identify crucial features, revealing that the importance of certain features is context-dependent and emphasizing the need for cross-feature consistency checks. Key findings indicate that hybrid MACGS architectures can improve performance by up to 7.2% in Pass@1 metrics and demonstrate CAM's utility in practical applications such as failure repair and feature pruning, significantly improving efficiency while maintaining performance.


<details>
<summary>Abstract</summary>

Despite the remarkable success that Multi-Agent Code Generation Systems (MACGS) have achieved, the inherent complexity of multi-agent architectures produces substantial volumes of intermediate outputs. To date, the individual importance of these intermediate outputs to the system correctness remains opaque, which impedes targeted optimization of MACGS designs. To address this challenge, we propose CAM, the first \textbf{C}ausality-based \textbf{A}nalysis framework for \textbf{M}ACGS that systematically quantifies the contribution of different intermediate features for system correctness. By comprehensively categorizing intermediate outputs and systematically simulating realistic errors on intermediate features, we identify the important features for system correctness and aggregate their importance rankings.
  We conduct extensive empirical analysis on the identified importance rankings. Our analysis reveals intriguing findings: first, we uncover context-dependent features\textemdash features whose importance emerges mainly through interactions with other features, revealing that quality assurance for MACGS should incorporate cross-feature consistency checks; second, we reveal that hybrid backend MACGS with different backend LLMs assigned according to their relative strength achieves up to 7.2\% Pass@1 improvement, underscoring hybrid architectures as a promising direction for future MACGS design. We further demonstrate CAM's practical utility through two applications: (1) failure repair which achieves a 73.3\% success rate by optimizing top-3 importance-ranked features and (2) feature pruning that reduces up to 66.8\% intermediate token consumption while maintaining generation performance. Our work provides actionable insights for MACGS design and deployment, establishing causality analysis as a powerful approach for understanding and improving MACGS.

</details>


### 141. Rethinking the Role of Entropy in Optimizing Tool-Use Behaviors for Large Language Model Agents

- **Authors:** Zeping Li, Hongru Wang, Yiwen Zhao, Guanhua Chen, Yixia Li, Keyang Chen, Yixin Cao, Guangnan Ye, Hongfeng Chai, Mengdi Wang, Zhenfei Yin
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02050v1](http://arxiv.org/abs/2602.02050v1)
- **PDF:** [https://arxiv.org/pdf/2602.02050v1](https://arxiv.org/pdf/2602.02050v1)
- **Categories:** cs.AI, cs.SE


> The paper presents a novel approach to optimizing tool-use behaviors in Large Language Model (LLM) agents by leveraging entropy reduction as a supervisory signal. It employs experimentation to demonstrate a positive correlation between reduced entropy and high-quality tool calls and introduces two reward strategies—sparse outcome rewards and dense process rewards—to enhance tool-use efficiency and performance, respectively. Results indicate that these strategies significantly reduce the number of tool calls while improving overall performance, suggesting that entropy reduction is a vital mechanism for enabling adaptive agent behaviors in practical applications.


<details>
<summary>Abstract</summary>

Tool-using agents based on Large Language Models (LLMs) excel in tasks such as mathematical reasoning and multi-hop question answering. However, in long trajectories, agents often trigger excessive and low-quality tool calls, increasing latency and degrading inference performance, making managing tool-use behavior challenging. In this work, we conduct entropy-based pilot experiments and observe a strong positive correlation between entropy reduction and high-quality tool calls. Building on this finding, we propose using entropy reduction as a supervisory signal and design two reward strategies to address the differing needs of optimizing tool-use behavior. Sparse outcome rewards provide coarse, trajectory-level guidance to improve efficiency, while dense process rewards offer fine-grained supervision to enhance performance. Experiments across diverse domains show that both reward designs improve tool-use behavior: the former reduces tool calls by 72.07% compared to the average of baselines, while the latter improves performance by 22.27%. These results position entropy reduction as a key mechanism for enhancing tool-use behavior, enabling agents to be more adaptive in real-world applications.

</details>


### 142. Bandwidth-Efficient Multi-Agent Communication through Information Bottleneck and Vector Quantization

- **Authors:** Ahmad Farooq, Kamran Iqbal
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02035v1](http://arxiv.org/abs/2602.02035v1)
- **PDF:** [https://arxiv.org/pdf/2602.02035v1](https://arxiv.org/pdf/2602.02035v1)
- **Categories:** cs.RO, cs.AI, cs.IT, cs.LG, cs.MA


> The paper presents a novel framework that integrates information bottleneck theory and vector quantization to enhance communication efficiency in multi-agent reinforcement learning systems under bandwidth constraints. By employing a gated communication mechanism that selectively triggers information exchange based on context, the method achieves a 181.8% improvement in performance over no-communication baselines while decreasing bandwidth usage by 41.4%. Experimental results indicate that this approach surpasses existing communication strategies, making it particularly applicable to real-world scenarios involving robotic swarms and autonomous vehicle fleets.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning systems deployed in real-world robotics applications face severe communication constraints that significantly impact coordination effectiveness. We present a framework that combines information bottleneck theory with vector quantization to enable selective, bandwidth-efficient communication in multi-agent environments. Our approach learns to compress and discretize communication messages while preserving task-critical information through principled information-theoretic optimization. We introduce a gated communication mechanism that dynamically determines when communication is necessary based on environmental context and agent states. Experimental evaluation on challenging coordination tasks demonstrates that our method achieves 181.8% performance improvement over no-communication baselines while reducing bandwidth usage by 41.4%. Comprehensive Pareto frontier analysis shows dominance across the entire success-bandwidth spectrum with area-under-curve of 0.198 vs 0.142 for next-best methods. Our approach significantly outperforms existing communication strategies and establishes a theoretically grounded framework for deploying multi-agent systems in bandwidth-constrained environments such as robotic swarms, autonomous vehicle fleets, and distributed sensor networks.

</details>


### 143. Constrained Process Maps for Multi-Agent Generative AI Workflows

- **Authors:** Ananya Joshi, Michael Rudow
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02034v1](http://arxiv.org/abs/2602.02034v1)
- **PDF:** [https://arxiv.org/pdf/2602.02034v1](https://arxiv.org/pdf/2602.02034v1)
- **Categories:** cs.AI


> This paper presents a multi-agent system designed for managing complex workflows in regulated environments, specifically formalized as a finite-horizon Markov Decision Process (MDP). By organizing agents according to distinct roles in decision-making stages and employing Monte Carlo estimation to assess uncertainty, the framework enables more effective coordination and oversight compared to traditional single-agent systems. Key findings indicate significant improvements in performance metrics, including a 19% accuracy increase, an 85-fold reduction in human review necessity, and faster processing times in scenarios involving AI safety evaluations, demonstrating its potential in enhancing agentic AI workflows.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based agents are increasingly used to perform complex, multi-step workflows in regulated settings such as compliance and due diligence. However, many agentic architectures rely primarily on prompt engineering of a single agent, making it difficult to observe or compare how models handle uncertainty and coordination across interconnected decision stages and with human oversight. We introduce a multi-agent system formalized as a finite-horizon Markov Decision Process (MDP) with a directed acyclic structure. Each agent corresponds to a specific role or decision stage (e.g., content, business, or legal review in a compliance workflow), with predefined transitions representing task escalation or completion. Epistemic uncertainty is quantified at the agent level using Monte Carlo estimation, while system-level uncertainty is captured by the MDP's termination in either an automated labeled state or a human-review state. We illustrate the approach through a case study in AI safety evaluation for self-harm detection, implemented as a multi-agent compliance system. Results demonstrate improvements over a single-agent baseline, including up to a 19\% increase in accuracy, up to an 85x reduction in required human review, and, in some configurations, reduced processing time.

</details>


### 144. Canonical Intermediate Representation for LLM-based optimization problem formulation and code generation

- **Authors:** Zhongyuan Lyu, Shuoyu Hu, Lujie Liu, Hongxia Yang, Ming LI
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02029v1](http://arxiv.org/abs/2602.02029v1)
- **PDF:** [https://arxiv.org/pdf/2602.02029v1](https://arxiv.org/pdf/2602.02029v1)
- **Categories:** cs.AI, cs.SE


> The paper presents a novel Canonical Intermediate Representation (CIR) to enhance the ability of large language models (LLMs) to formulate optimization problems from natural language descriptions, addressing challenges related to complex constraints and operational rules. The authors develop a multi-agent framework called rule-to-constraint (R2C) that utilizes CIR to synthesize implementations and instantiate optimization models, which is evaluated against a custom benchmark and existing literature benchmarks. Key findings reveal that R2C achieves a 47.2% accuracy rate on the new benchmark and performs competitively with state-of-the-art models, underscoring its potential for improving agentic AI systems in operational decision-making.


<details>
<summary>Abstract</summary>

Automatically formulating optimization models from natural language descriptions is a growing focus in operations research, yet current LLM-based approaches struggle with the composite constraints and appropriate modeling paradigms required by complex operational rules. To address this, we introduce the Canonical Intermediate Representation (CIR): a schema that LLMs explicitly generate between problem descriptions and optimization models. CIR encodes the semantics of operational rules through constraint archetypes and candidate modeling paradigms, thereby decoupling rule logic from its mathematical instantiation. Upon a newly generated CIR knowledge base, we develop the rule-to-constraint (R2C) framework, a multi-agent pipeline that parses problem texts, synthesizes CIR implementations by retrieving domain knowledge, and instantiates optimization models. To systematically evaluate rule-to-constraint reasoning, we test R2C on our newly constructed benchmark featuring rich operational rules, and benchmarks from prior work. Extensive experiments show that R2C achieves state-of-the-art accuracy on the proposed benchmark (47.2% Accuracy Rate). On established benchmarks from the literature, R2C delivers highly competitive results, approaching the performance of proprietary models (e.g., GPT-5). Moreover, with a reflection mechanism, R2C achieves further gains and sets new best-reported results on some benchmarks.

</details>


### 145. Self-Consolidation for Self-Evolving Agents

- **Authors:** Hongzhuo Yu, Fei Zhu, Guo-Sen Xie, Ling Shao
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01966v1](http://arxiv.org/abs/2602.01966v1)
- **PDF:** [https://arxiv.org/pdf/2602.01966v1](https://arxiv.org/pdf/2602.01966v1)
- **Categories:** cs.LG


> The paper presents a novel framework for self-evolving large language model (LLM) agents that enhances their ability to learn from both successes and failures through a dual mechanism. The methodology involves a contrastive reflection strategy to summarize and utilize error-prone patterns, alongside a self-consolidation mechanism that transforms non-parametric experiences into compact learnable parameters, facilitating the agent's internalization of historical knowledge. Key findings indicate that this approach significantly improves long-term evolution and adaptability of LLM agents, addressing limitations of current methods that neglect the learning potential from failures and struggle with excessive information retrieval.


<details>
<summary>Abstract</summary>

While large language model (LLM) agents have demonstrated impressive problem-solving capabilities, they typically operate as static systems, lacking the ability to evolve through lifelong interaction. Existing attempts to bridge this gap primarily rely on retrieving successful past trajectories as demonstrations. However, this paradigm faces two critical limitations. First, by focusing solely on success, agents overlook the rich pedagogical value embedded in failed attempts, preventing them from identifying and avoiding recurrent pitfalls. Second, continually accumulating textual experiences not only increases the time consumption during retrieval but also inevitably introduces noise and exhausts the largest context window of current LLMs. To address these challenges, we propose a novel self-evolving framework for LLM agents that introduces a complementary evolution mechanism: First, a contrastive reflection strategy is introduced to explicitly summarize error-prone patterns and capture reusable insights. Second, we propose a self-consolidation mechanism that distills non-parametric textual experience into compact learnable parameters. This enables the agent to internalize extensive historical experience directly into its latent space. Extensive experiments demonstrate the advantages of our method in long-term agent evolution.

</details>


### 146. Exploring Silicon-Based Societies: An Early Study of the Moltbook Agent Community

- **Authors:** Yu-Zheng Lin, Bono Po-Jen Shih, Hsuan-Ying Alessandra Chien, Shalaka Satam, Jesus Horacio Pacheco, Sicong Shao, Soheil Salehi, Pratik Satam
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02613v2](http://arxiv.org/abs/2602.02613v2)
- **PDF:** [https://arxiv.org/pdf/2602.02613v2](https://arxiv.org/pdf/2602.02613v2)
- **Categories:** cs.MA, cs.AI, cs.CY


> The paper introduces "data-driven silicon sociology" as a novel empirical framework to study the social structures of autonomous large language model agents, using the Moltbook platform, which hosts over 150,000 agents interacting within thousands of sub-communities. Through extensive data mining, the authors analyzed the proactive community partitioning activities of agents, revealing that they organize their collective space around themes such as human-like interests and early economic behaviors, thereby generating new sociological structures from machine-generated data without reliance on traditional taxonomies. This pioneering methodology not only enhances understanding of agent interactions but also lays the groundwork for further exploring the complexities of large-scale autonomous agent ecosystems.


<details>
<summary>Abstract</summary>

The rapid emergence of autonomous large language model agents has given rise to persistent, large-scale agent ecosystems whose collective behavior cannot be adequately understood through anecdotal observation or small-scale simulation. This paper introduces data-driven silicon sociology as a systematic empirical framework for studying social structure formation among interacting artificial agents. We present a pioneering large-scale data mining investigation of an in-the-wild agent society by analyzing Moltbook, a social platform designed primarily for agent-to-agent interaction. At the time of study, Moltbook hosted over 150,000 registered autonomous agents operating across thousands of agent-created sub-communities. Using programmatic and non-intrusive data acquisition, we collected and analyzed the textual descriptions of 12,758 submolts, which represent proactive sub-community partitioning activities within the ecosystem. Treating agent-authored descriptions as first-class observational artifacts, we apply rigorous preprocessing, contextual embedding, and unsupervised clustering techniques to uncover latent patterns of thematic organization and social space structuring. The results show that autonomous agents systematically organize collective space through reproducible patterns spanning human-mimetic interests, silicon-centric self-reflection, and early-stage economic and coordination behaviors. Rather than relying on predefined sociological taxonomies, these structures emerge directly from machine-generated data traces. This work establishes a methodological foundation for data-driven silicon sociology and demonstrates that data mining techniques can provide a powerful lens for understanding the organization and evolution of large autonomous agent societies.

</details>


### 147. Human Society-Inspired Approaches to Agentic AI Security: The 4C Framework

- **Authors:** Alsharif Abuadbba, Nazatul Sultan, Surya Nepal, Sanjay Jha
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01942v1](http://arxiv.org/abs/2602.01942v1)
- **PDF:** [https://arxiv.org/pdf/2602.01942v1](https://arxiv.org/pdf/2602.01942v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces the 4C Framework for enhancing the security of agentic AI systems, which are increasingly autonomous and operate in complex socio-technical environments. Utilizing a governance-inspired approach, the framework categorizes risks into four dimensions: Core, Connection, Cognition, and Compliance, thereby shifting the focus from traditional system-level vulnerabilities to a comprehensive view of behavioral integrity and alignment with human values. The key finding emphasizes that addressing the multifaceted nature of risks associated with agentic AI requires a broader perspective that includes interaction and emergent behavior, ultimately contributing to the development of more trustworthy and governable AI systems.


<details>
<summary>Abstract</summary>

AI is moving from domain-specific autonomy in closed, predictable settings to large-language-model-driven agents that plan and act in open, cross-organizational environments. As a result, the cybersecurity risk landscape is changing in fundamental ways. Agentic AI systems can plan, act, collaborate, and persist over time, functioning as participants in complex socio-technical ecosystems rather than as isolated software components. Although recent work has strengthened defenses against model and pipeline level vulnerabilities such as prompt injection, data poisoning, and tool misuse, these system centric approaches may fail to capture risks that arise from autonomy, interaction, and emergent behavior. This article introduces the 4C Framework for multi-agent AI security, inspired by societal governance. It organizes agentic risks across four interdependent dimensions: Core (system, infrastructure, and environmental integrity), Connection (communication, coordination, and trust), Cognition (belief, goal, and reasoning integrity), and Compliance (ethical, legal, and institutional governance). By shifting AI security from a narrow focus on system-centric protection to the broader preservation of behavioral integrity and intent, the framework complements existing AI security strategies and offers a principled foundation for building agentic AI systems that are trustworthy, governable, and aligned with human values.

</details>


### 148. ProcMEM: Learning Reusable Procedural Memory from Experience via Non-Parametric PPO for LLM Agents

- **Authors:** Qirui Mi, Zhijian Ma, Mengyue Yang, Haoxuan Li, Yisen Wang, Haifeng Zhang, Jun Wang
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01869v1](http://arxiv.org/abs/2602.01869v1)
- **PDF:** [https://arxiv.org/pdf/2602.01869v1](https://arxiv.org/pdf/2602.01869v1)
- **Categories:** cs.AI


> The paper introduces ProcMEM, a framework designed to enable LLM-driven agents to autonomously learn and reuse procedural memory from their experiences, thereby reducing redundant computations and enhancing execution stability. The methodology includes the development of a Skill-MDP formalization that converts passive episodic experiences into actionable skills, coupled with a Non-Parametric Proximal Policy Optimization (PPO) approach to ensure reliable skill verification and memory maintenance. Key findings indicate that ProcMEM significantly improves experience reuse rates and overall performance, achieving effective memory compression while allowing agents to transparently accumulate and refine procedural knowledge for long-term autonomous functioning.


<details>
<summary>Abstract</summary>

LLM-driven agents demonstrate strong performance in sequential decision-making but often rely on on-the-fly reasoning, re-deriving solutions even in recurring scenarios. This insufficient experience reuse leads to computational redundancy and execution instability. To bridge this gap, we propose ProcMEM, a framework that enables agents to autonomously learn procedural memory from interaction experiences without parameter updates. By formalizing a Skill-MDP, ProcMEM transforms passive episodic narratives into executable Skills defined by activation, execution, and termination conditions to ensure executability. To achieve reliable reusability without capability degradation, we introduce Non-Parametric PPO, which leverages semantic gradients for high-quality candidate generation and a PPO Gate for robust Skill verification. Through score-based maintenance, ProcMEM sustains compact, high-quality procedural memory. Experimental results across in-domain, cross-task, and cross-agent scenarios demonstrate that ProcMEM achieves superior reuse rates and significant performance gains with extreme memory compression. Visualized evolutionary trajectories and Skill distributions further reveal how ProcMEM transparently accumulates, refines, and reuses procedural knowledge to facilitate long-term autonomy.

</details>


### 149. SOPRAG: Multi-view Graph Experts Retrieval for Industrial Standard Operating Procedures

- **Authors:** Liangtao Lin, Zhaomeng Zhu, Tianwei Zhang, Yonggang Wen
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01858v1](http://arxiv.org/abs/2602.01858v1)
- **PDF:** [https://arxiv.org/pdf/2602.01858v1](https://arxiv.org/pdf/2602.01858v1)
- **Categories:** cs.AI


> The paper presents SOPRAG, a novel framework for retrieving Standard Operating Procedures (SOPs) in industrial contexts, addressing challenges like proprietary structures and condition-dependent relevance that conventional semantic-driven Retrieval-Augmented Generation (RAG) methods cannot solve. Utilizing a Mixture-of-Experts (MoE) approach, SOPRAG employs specialized graph experts—Entity, Causal, and Flow—to navigate the complexities of SOPs, complemented by a Procedure Card layer and an LLM-Guided gating mechanism for optimized retrieval. Experimental results across various industrial settings demonstrate that SOPRAG markedly enhances retrieval accuracy and utility, achieving perfect execution scores in critical real-world tasks, thereby advancing the field of agentic AI in operational safety and performance.


<details>
<summary>Abstract</summary>

Standard Operating Procedures (SOPs) are essential for ensuring operational safety and consistency in industrial environments. However, retrieving and following these procedures presents unique challenges, such as rigid proprietary structures, condition-dependent relevance, and actionable execution requirement, which standard semantic-driven Retrieval-Augmented Generation (RAG) paradigms fail to address. Inspired by the Mixture-of-Experts (MoE) paradigm, we propose SOPRAG, a novel framework specifically designed to address the above pain points in SOP retrieval. SOPRAG replaces flat chunking with specialized Entity, Causal, and Flow graph experts to resolve industrial structural and logical complexities. To optimize and coordinate these experts, we propose a Procedure Card layer that prunes the search space to eliminate computational noise, and an LLM-Guided gating mechanism that dynamically weights these experts to align retrieval with operator intent. To address the scarcity of domain-specific data, we also introduce an automated, multi-agent workflow for benchmark construction. Extensive experiments across four industrial domains demonstrate that SOPRAG significantly outperforms strong lexical, dense, and graph-based RAG baselines in both retrieval accuracy and response utility, achieving perfect execution scores in real-world critical tasks.

</details>


### 150. ROMA: Recursive Open Meta-Agent Framework for Long-Horizon Multi-Agent Systems

- **Authors:** Salaheddin Alzu'bi, Baran Nama, Arda Kaz, Anushri Eswaran, Weiyuan Chen, Sarvesh Khetan, Rishab Bala, Tu Vu, Sewoong Oh
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01848v1](http://arxiv.org/abs/2602.01848v1)
- **PDF:** [https://arxiv.org/pdf/2602.01848v1](https://arxiv.org/pdf/2602.01848v1)
- **Categories:** cs.AI, cs.MA


> The paper presents ROMA (Recursive Open Meta-Agents), a novel framework designed to enhance multi-agent systems' performance on long-horizon tasks by employing recursive task decomposition and structured aggregation to manage complexity. The framework is structured around four modular roles—Atomizer, Planner, Executor, and Aggregator—allowing for efficient parallel execution and transparent hierarchical tracing of actions. Key findings indicate that ROMA, when combined with the GEPA+ algorithm for prompt optimization, significantly improves reasoning accuracy and long-form generation capabilities, outperforming existing models on benchmarks such as SEAL-0 and EQ-Bench, showcasing its potential to advance agentic AI by enabling deeper reasoning while maintaining flexibility and interpretability.


<details>
<summary>Abstract</summary>

Current agentic frameworks underperform on long-horizon tasks. As reasoning depth increases, sequential orchestration becomes brittle, context windows impose hard limits that degrade performance, and opaque execution traces make failures difficult to localize or debug. We introduce ROMA (Recursive Open Meta-Agents), a domain-agnostic framework that addresses these limitations through recursive task decomposition and structured aggregation. ROMA decomposes goals into dependency-aware subtask trees that can be executed in parallel, while aggregation compresses and validates intermediate results to control context growth. Our framework standardizes agent construction around four modular roles --Atomizer (which decides whether a task should be decomposed), Planner, Executor, and Aggregator -- which cleanly separate orchestration from model selection and enable transparent, hierarchical execution traces. This design supports heterogeneous multi-agent systems that mix models and tools according to cost, latency, and capability. To adapt ROMA to specific tasks without fine-tuning, we further introduce GEPA$+$, an improved Genetic-Pareto prompt proposer that searches over prompts within ROMA's component hierarchy while preserving interface contracts. We show that ROMA, combined with GEPA+, delivers leading system-level performance on reasoning and long-form generation benchmarks. On SEAL-0, which evaluates reasoning over conflicting web evidence, ROMA instantiated with GLM-4.6 improves accuracy by 9.9\% over Kimi-Researcher. On EQ-Bench, a long-form writing benchmark, ROMA enables DeepSeek-V3 to match the performance of leading closed-source models such as Claude Sonnet 4.5. Our results demonstrate that recursive, modular agent architectures can scale reasoning depth while remaining interpretable, flexible, and model-agnostic.

</details>


### 151. INDIBATOR: Diverse and Fact-Grounded Individuality for Multi-Agent Debate in Molecular Discovery

- **Authors:** Yunhui Jang, Seonghyun Park, Jaehyung Kim, Sungsoo Ahn
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01815v1](http://arxiv.org/abs/2602.01815v1)
- **PDF:** [https://arxiv.org/pdf/2602.01815v1](https://arxiv.org/pdf/2602.01815v1)
- **Categories:** cs.AI


> The paper introduces INDIBATOR, a novel framework for molecular discovery that enhances multi-agent systems by incorporating individualized scientist profiles derived from agents' publication and molecular histories. By implementing a structured debate format involving proposals, critiques, and voting, INDIBATOR enables agents to demonstrate unique scientific contributions, which leads to superior performance compared to traditional role-based or keyword-driven systems. Key findings indicate that the "scientific DNA" of individual agents is crucial for achieving high-quality outcomes in scientific discovery, marking a significant advancement in tailoring agentic behavior within AI frameworks.


<details>
<summary>Abstract</summary>

Multi-agent systems have emerged as a powerful paradigm for automating scientific discovery. To differentiate agent behavior in the multi-agent system, current frameworks typically assign generic role-based personas such as ''reviewer'' or ''writer'' or rely on coarse grained keyword-based personas. While functional, this approach oversimplifies how human scientists operate, whose contributions are shaped by their unique research trajectories. In response, we propose INDIBATOR, a framework for molecular discovery that grounds agents in individualized scientist profiles constructed from two modalities: publication history for literature-derived knowledge and molecular history for structural priors. These agents engage in multi-turn debate through proposal, critique, and voting phases. Our evaluation demonstrates that these fine-grained individuality-grounded agents consistently outperform systems relying on coarse-grained personas, achieving competitive or state-of-the-art performance. These results validate that capturing the ``scientific DNA'' of individual agents is essential for high-quality discovery.

</details>


### 152. ORCH: many analyses, one merge-a deterministic multi-agent orchestrator for discrete-choice reasoning with EMA-guided routing

- **Authors:** Hanlin Zhou, Huah Yong Chan
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01797v1](http://arxiv.org/abs/2602.01797v1)
- **PDF:** [https://arxiv.org/pdf/2602.01797v1](https://arxiv.org/pdf/2602.01797v1)
- **Categories:** cs.AI


> The paper presents ORCH, a deterministic multi-agent framework designed for discrete-choice reasoning leveraging large-scale language models (LLMs). Unlike existing systems that rely on stochastic methods, ORCH utilizes a "many analyses, one decision" approach, wherein multiple models independently analyze tasks and a merge agent consolidates their findings through fixed, interpretable rules. Experimental results indicate that ORCH significantly outperforms traditional models, achieving notable accuracy improvements on benchmark datasets, while its optional EMA-guided router enhances performance further, underscoring its potential for creating controllable and interpretable AI agent systems.


<details>
<summary>Abstract</summary>

Recent advances in large-scale language models (LLMs) have made multi-agent architectures attractive for challenging reasoning tasks. However, many existing systems rely on stochastic routing or ad-hoc heuristics, making their behavior difficult to reproduce and their decision process hard to interpret. We propose ORCH, a deterministic coordination framework for discrete-choice reasoning that orchestrates heterogeneous LLMs. ORCH follows a ``many analyses, one decision'' paradigm: multiple base models independently produce structured analyses, and a dedicated merge agent outputs the final choice. The framework uses fixed rules for task decomposition and answer aggregation, keeping the pipeline predictable, reproducible, and training-free. Determinism here refers to fixed routing and aggregation rules under a fixed evaluation protocol, rather than strict bit-level reproducibility across deployments. To exploit model complementarity, we optionally introduce an EMA-guided router that updates agent selection using historical accuracy, latency, or cost; since it relies on answer-based feedback, it is mainly intended for benchmarking, controlled evaluation, or delayed-feedback settings. Experiments on MMLU, MMLU-Pro, and GSM8K show that ORCH consistently outperforms single-model baselines and a majority-vote ensemble. On MMLU-Pro, ORCH improves accuracy by over 10 points compared to the strongest baseline, and on GSM8K it yields gains exceeding 50 points; McNemar tests confirm statistical significance. The EMA router provides an additional 0.7--2.0 point accuracy boost, and ablations show that both multi-agent collaboration and routing contribute substantially. Overall, ORCH offers a practical path toward controllable, interpretable, and deployment-ready LLM-based agent systems for discrete-choice reasoning.

</details>


### 153. Gender Dynamics and Homophily in a Social Network of LLM Agents

- **Authors:** Faezeh Fadaei, Jenny Carla Moran, Taha Yasseri
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.02606v1](http://arxiv.org/abs/2602.02606v1)
- **PDF:** [https://arxiv.org/pdf/2602.02606v1](https://arxiv.org/pdf/2602.02606v1)
- **Categories:** cs.SI, cs.AI, cs.CY


> The paper investigates the gender dynamics and homophily among large language model (LLM) agents within the Chirper.ai social media platform, which comprises over 70,000 autonomous AI chatbots and their interactions. Using a dataset of approximately 140 million posts, the authors assign weekly gender scores to the agents, revealing that gender performance is fluid and demonstrating strong gender-based homophily, where agents prefer to follow those exhibiting similar gender traits. The findings indicate that both social selection and social influence mechanisms contribute to the development of these homophilic connections, suggesting that LLMs exhibit culturally entrained gender behaviors that have implications for applications in synthetic populations and social simulations.


<details>
<summary>Abstract</summary>

Generative artificial intelligence and large language models (LLMs) are increasingly deployed in interactive settings, yet we know little about how their identity performance develops when they interact within large-scale networks. We address this by examining Chirper.ai, a social media platform similar to X but composed entirely of autonomous AI chatbots. Our dataset comprises over 70,000 agents, approximately 140 million posts, and the evolving followership network over one year. Based on agents' text production, we assign weekly gender scores to each agent. Results suggest that each agent's gender performance is fluid rather than fixed. Despite this fluidity, the network displays strong gender-based homophily, as agents consistently follow others performing gender similarly. Finally, we investigate whether these homophilic connections arise from social selection, in which agents choose to follow similar accounts, or from social influence, in which agents become more similar to their followees over time. Consistent with human social networks, we find evidence that both mechanisms shape the structure and evolution of interactions among LLMs. Our findings suggest that, even in the absence of bodies, cultural entraining of gender performance leads to gender-based sorting. This has important implications for LLM applications in synthetic hybrid populations, social simulations, and decision support.

</details>


### 154. Scaling Search-Augmented LLM Reasoning via Adaptive Information Control

- **Authors:** Siheng Xiong, Oguzhan Gungordu, Blair Johnson, James C. Kerce, Faramarz Fekri
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01672v1](http://arxiv.org/abs/2602.01672v1)
- **PDF:** [https://arxiv.org/pdf/2602.01672v1](https://arxiv.org/pdf/2602.01672v1)
- **Categories:** cs.CL


> The paper introduces DeepControl, a novel framework for adaptive information control in search-augmented reasoning agents, addressing the challenges of uncontrolled information retrieval that can lead to inefficiencies. Utilizing a formal measure of information utility, the methodology incorporates mechanisms for retrieval continuation and granularity control to optimize when and how much information to gather during reasoning tasks. Key findings demonstrate that DeepControl significantly enhances performance, achieving average improvements of 9.4% and 8.6% over existing outcome-based reinforcement learning baselines, underscoring the importance of adaptive strategies in developing effective agentic AI systems capable of tackling complex information environments.


<details>
<summary>Abstract</summary>

Search-augmented reasoning agents interleave multi-step reasoning with external information retrieval, but uncontrolled retrieval often leads to redundant evidence, context saturation, and unstable learning. Existing approaches rely on outcome-based reinforcement learning (RL), which provides limited guidance for regulating information acquisition. We propose DeepControl, a framework for adaptive information control based on a formal notion of information utility, which measures the marginal value of retrieved evidence under a given reasoning state. Building on this utility, we introduce retrieval continuation and granularity control mechanisms that selectively regulate when to continue and stop retrieval, and how much information to expand. An annealed control strategy enables the agent to internalize effective information acquisition behaviors during training. Extensive experiments across seven benchmarks demonstrate that our method consistently outperforms strong baselines. In particular, our approach achieves average performance improvements of 9.4% and 8.6% on Qwen2.5-7B and Qwen2.5-3B, respectively, over strong outcome-based RL baselines, and consistently outperforms both retrieval-free and retrieval-based reasoning methods without explicit information control. These results highlight the importance of adaptive information control for scaling search-augmented reasoning agents to complex, real-world information environments.

</details>


### 155. TABX: A High-Throughput Sandbox Battle Simulator for Multi-Agent Reinforcement Learning

- **Authors:** Hayeong Lee, JunHyeok Oh, Byung-Jun Lee
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01665v1](http://arxiv.org/abs/2602.01665v1)
- **PDF:** [https://arxiv.org/pdf/2602.01665v1](https://arxiv.org/pdf/2602.01665v1)
- **Categories:** cs.MA, cs.AI, cs.LG


> The paper presents TABX, a high-throughput sandbox for multi-agent reinforcement learning (MARL) that enhances the design and evaluation of cooperative algorithms by allowing for customizable scenarios and granular control over environmental parameters. Utilizing JAX for hardware acceleration, TABX enables efficient parallel execution and reduces computational costs, making it scalable for complex tasks. Key findings indicate that this modular framework supports systematic investigations into emergent behaviors and algorithmic trade-offs, positioning TABX as a valuable resource for advancing research in agentic AI.


<details>
<summary>Abstract</summary>

The design of environments plays a critical role in shaping the development and evaluation of cooperative multi-agent reinforcement learning (MARL) algorithms. While existing benchmarks highlight critical challenges, they often lack the modularity required to design custom evaluation scenarios. We introduce the Totally Accelerated Battle Simulator in JAX (TABX), a high-throughput sandbox designed for reconfigurable multi-agent tasks. TABX provides granular control over environmental parameters, permitting a systematic investigation into emergent agent behaviors and algorithmic trade-offs across a diverse spectrum of task complexities. Leveraging JAX for hardware-accelerated execution on GPUs, TABX enables massive parallelization and significantly reduces computational overhead. By providing a fast, extensible, and easily customized framework, TABX facilitates the study of MARL agents in complex structured domains and serves as a scalable foundation for future research. Our code is available at: https://anonymous.4open.science/r/TABX-00CA.

</details>


### 156. From Perception to Action: Spatial AI Agents and World Models

- **Authors:** Gloria Felicia, Nolan Bryant, Handi Putra, Ayaan Gazali, Eliel Lobo, Esteban Rojas
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01644v1](http://arxiv.org/abs/2602.01644v1)
- **PDF:** [https://arxiv.org/pdf/2602.01644v1](https://arxiv.org/pdf/2602.01644v1)
- **Categories:** cs.LG, cs.AI, cs.CV, cs.MA, cs.RO


> The paper presents a unified framework that connects agentic capabilities with spatial tasks, focusing on the unique importance of spatial intelligence for embodied agents. Through an extensive review of over 2,000 papers, the authors introduce a three-axis taxonomy that distinguishes between spatial and symbolic grounding and highlights key findings regarding the necessity of hierarchical memory systems, GNN-LLM integration for spatial reasoning, and the role of world models for safe deployment across various spatial scales. The research concludes with the identification of grand challenges and future directions aimed at advancing the development of spatially-aware autonomous systems in several applications.


<details>
<summary>Abstract</summary>

While large language models have become the prevailing approach for agentic reasoning and planning, their success in symbolic domains does not readily translate to the physical world. Spatial intelligence, the ability to perceive 3D structure, reason about object relationships, and act under physical constraints, is an orthogonal capability that proves important for embodied agents. Existing surveys address either agentic architectures or spatial domains in isolation. None provide a unified framework connecting these complementary capabilities. This paper bridges that gap. Through a thorough review of over 2,000 papers, citing 742 works from top-tier venues, we introduce a unified three-axis taxonomy connecting agentic capabilities with spatial tasks across scales. Crucially, we distinguish spatial grounding (metric understanding of geometry and physics) from symbolic grounding (associating images with text), arguing that perception alone does not confer agency. Our analysis reveals three key findings mapped to these axes: (1) hierarchical memory systems (Capability axis) are important for long-horizon spatial tasks. (2) GNN-LLM integration (Task axis) is a promising approach for structured spatial reasoning. (3) World models (Scale axis) are essential for safe deployment across micro-to-macro spatial scales. We conclude by identifying six grand challenges and outlining directions for future research, including the need for unified evaluation frameworks to standardize cross-domain assessment. This taxonomy provides a foundation for unifying fragmented research efforts and enabling the next generation of spatially-aware autonomous systems in robotics, autonomous vehicles, and geospatial intelligence.

</details>


### 157. AdaptNC: Adaptive Nonconformity Scores for Uncertainty-Aware Autonomous Systems in Dynamic Environments

- **Authors:** Renukanandan Tumu, Aditya Singh, Rahul Mangharam
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01629v1](http://arxiv.org/abs/2602.01629v1)
- **PDF:** [https://arxiv.org/pdf/2602.01629v1](https://arxiv.org/pdf/2602.01629v1)
- **Categories:** cs.LG, cs.RO, eess.SY


> The paper presents AdaptNC, an innovative framework designed to enhance uncertainty quantification for autonomous systems in dynamic environments by adaptively adjusting both nonconformity scores and conformal thresholds. The methodology employs an adaptive reweighting scheme combined with a replay buffer to optimize score functions and reduce coverage instability during transitions. Key findings indicate that AdaptNC significantly lowers the volume of prediction regions while successfully maintaining target coverage, outperforming existing state-of-the-art approaches based on static nonconformity scores.


<details>
<summary>Abstract</summary>

Rigorous uncertainty quantification is essential for the safe deployment of autonomous systems in unconstrained environments. Conformal Prediction (CP) provides a distribution-free framework for this task, yet its standard formulations rely on exchangeability assumptions that are violated by the distribution shifts inherent in real-world robotics. Existing online CP methods maintain target coverage by adaptively scaling the conformal threshold, but typically employ a static nonconformity score function. We show that this fixed geometry leads to highly conservative, volume-inefficient prediction regions when environments undergo structural shifts. To address this, we propose \textbf{AdaptNC}, a framework for the joint online adaptation of both the nonconformity score parameters and the conformal threshold. AdaptNC leverages an adaptive reweighting scheme to optimize score functions, and introduces a replay buffer mechanism to mitigate the coverage instability that occurs during score transitions. We evaluate AdaptNC on diverse robotic benchmarks involving multi-agent policy changes, environmental changes and sensor degradation. Our results demonstrate that AdaptNC significantly reduces prediction region volume compared to state-of-the-art threshold-only baselines while maintaining target coverage levels.

</details>


### 158. What Do Agents Learn from Trajectory-SFT: Semantics or Interfaces?

- **Authors:** Weizheng Gu, Chengze Li, Zhuohao Yu, Mengyuan Sun, Zhibang Yang, Wei Wang, Hongrui Jia, Shikun Zhang, Wei Ye
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01611v1](http://arxiv.org/abs/2602.01611v1)
- **PDF:** [https://arxiv.org/pdf/2602.01611v1](https://arxiv.org/pdf/2602.01611v1)
- **Categories:** cs.LG


> The paper introduces PIPE, a novel evaluation protocol aimed at distinguishing between agents' reliance on semantic tool-use versus memorization of interface-specific interactions in the context of interactive agents. By applying this methodology to various environments, the study reveals that agents trained with trajectory-Supervised Fine-Tuning (SFT) exhibit significant degradation in performance when slight interface modifications are made, indicating a reliance on memorized interaction patterns rather than a robust understanding of semantics. The findings underscore the need for improved evaluation metrics, such as Interface Reliance (IR), to better assess AI agents' capabilities beyond standard benchmarks, highlighting their environment-dependent training behaviors.


<details>
<summary>Abstract</summary>

Large language models are increasingly evaluated as interactive agents, yet standard agent benchmarks conflate two qualitatively distinct sources of success: semantic tool-use and interface-specific interaction pattern memorization. Because both mechanisms can yield identical task success on the original interface, benchmark scores alone are not identifiable evidence of environment-invariant capability. We propose PIPE, a protocol-level evaluation augmentation for diagnosing interface reliance by minimally rewriting environment interfaces while preserving task semantics and execution behavior. Across 16 environments from AgentBench and AgentGym and a range of open-source and API-based agents, PIPE reveals that trajectory-SFT substantially amplifies interface shortcutting: trained agents degrade sharply under minimal interface rewrites, while non-trajectory-trained models remain largely stable. We further introduce Interface Reliance (IR), a counterbalanced alias-based metric that quantifies preference for training-time interfaces, and show that interface shortcutting exhibits environment-dependent, non-monotonic training dynamics that remain invisible under standard evaluation. Our code is available at https://anonymous.4open.science/r/What-Do-Agents-Learn-from-Trajectory-SFT-Semantics-or-Interfaces--0831/.

</details>


### 159. FS-Researcher: Test-Time Scaling for Long-Horizon Research Tasks with File-System-Based Agents

- **Authors:** Chiwei Zhu, Benfeng Xu, Mingxuan Du, Shaohan Wang, Xiaorui Wang, Zhendong Mao, Yongdong Zhang
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01566v1](http://arxiv.org/abs/2602.01566v1)
- **PDF:** [https://arxiv.org/pdf/2602.01566v1](https://arxiv.org/pdf/2602.01566v1)
- **Categories:** cs.CL


> The paper introduces FS-Researcher, a dual-agent framework designed to enhance the performance of large language model (LLM) agents in long-horizon research tasks by utilizing a file-system for persistent external memory. The methodology involves two agents: a Context Builder, which collects and organizes information from the internet into a hierarchical knowledge base, and a Report Writer, which constructs reports using this knowledge base. Key findings indicate that FS-Researcher achieved state-of-the-art report quality on various benchmarks, with evidence that increased computation for the Context Builder improves report quality, underscoring its efficacy for scalable, agent-based AI research.


<details>
<summary>Abstract</summary>

Deep research is emerging as a representative long-horizon task for large language model (LLM) agents. However, long trajectories in deep research often exceed model context limits, compressing token budgets for both evidence collection and report writing, and preventing effective test-time scaling. We introduce FS-Researcher, a file-system-based, dual-agent framework that scales deep research beyond the context window via a persistent workspace. Specifically, a Context Builder agent acts as a librarian which browses the internet, writes structured notes, and archives raw sources into a hierarchical knowledge base that can grow far beyond context length. A Report Writer agent then composes the final report section by section, treating the knowledge base as the source of facts. In this framework, the file system serves as a durable external memory and a shared coordination medium across agents and sessions, enabling iterative refinement beyond the context window. Experiments on two open-ended benchmarks (DeepResearch Bench and DeepConsult) show that FS-Researcher achieves state-of-the-art report quality across different backbone models. Further analyses demonstrate a positive correlation between final report quality and the computation allocated to the Context Builder, validating effective test-time scaling under the file-system paradigm. The code and data are anonymously open-sourced at https://github.com/Ignoramus0817/FS-Researcher.

</details>


### 160. Autonomous Question Formation for Large Language Model-Driven AI Systems

- **Authors:** Hong Su
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01556v1](http://arxiv.org/abs/2602.01556v1)
- **PDF:** [https://arxiv.org/pdf/2602.01556v1](https://arxiv.org/pdf/2602.01556v1)
- **Categories:** cs.AI


> This paper presents a novel framework for autonomous question formation in LLM-driven AI systems, enhancing their ability to adapt to dynamic environments by allowing them to autonomously identify problems and set tasks based on internal states and interactions with other agents. The methodology involves treating question formation as a decision process that incorporates various prompting scopes, which enables the system to learn and improve its performance over time. Key findings demonstrate that environment-aware and inter-agent-aware prompting significantly reduce the occurrence of no-eat events in a multi-agent simulation, highlighting the framework's impact on decision-making quality and adaptability in agentic AI systems.


<details>
<summary>Abstract</summary>

Large language model (LLM)-driven AI systems are increasingly important for autonomous decision-making in dynamic and open environments. However, most existing systems rely on predefined tasks and fixed prompts, limiting their ability to autonomously identify what problems should be solved when environmental conditions change. In this paper, we propose a human-simulation-based framework that enables AI systems to autonomously form questions and set tasks by reasoning over their internal states, environmental observations, and interactions with other AI systems. The proposed method treats question formation as a first-class decision process preceding task selection and execution, and integrates internal-driven, environment-aware, and inter-agent-aware prompting scopes to progressively expand cognitive coverage. In addition, the framework supports learning the question-formation process from experience, allowing the system to improve its adaptability and decision quality over time. xperimental results in a multi-agent simulation environment show that environment-aware prompting significantly reduces no-eat events compared with the internal-driven baseline, and inter-agent-aware prompting further reduces cumulative no-eat events by more than 60% over a 20-day simulation, with statistically significant improvements (p < 0.05).

</details>


### 161. S1-NexusAgent: a Self-Evolving Agent Framework for Multidisciplinary Scientific Research

- **Authors:** S1-NexusAgent Team
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01550v1](http://arxiv.org/abs/2602.01550v1)
- **PDF:** [https://arxiv.org/pdf/2602.01550v1](https://arxiv.org/pdf/2602.01550v1)
- **Categories:** cs.AI


> The paper presents S1-NexusAgent, a self-evolving agent framework specifically designed to enhance multidisciplinary scientific research by effectively managing large-scale data and complex workflows. Employing a hierarchical Plan-and-CodeAct execution paradigm, the framework decouples overall planning from tool execution, integrates a wide range of scientific tools, and introduces object-reference-based sparse context management for efficient context isolation. Key findings indicate that S1-NexusAgent significantly outperforms existing models in long-horizon planning and tool orchestration across various scientific benchmarks, showcasing its capacity for adaptive learning and reusable knowledge formation in research environments.


<details>
<summary>Abstract</summary>

Modern scientific research relies on large-scale data, complex workflows, and specialized tools, which existing LLMs and tool-based agents struggle to handle due to limitations in long-horizon planning, robust goal maintenance, and continual learning from execution. To address these issues, in this work, we propose S1-NexusAgent, a self-evolving agent framework designed for multidisciplinary scientific research. S1-NexusAgent adopts a hierarchical Plan-and-CodeAct execution paradigm, decoupling global scientific planning from subtask-level tool execution through a dual-loop architecture, thereby enabling stable modeling of complex research workflows. The system natively supports the Model Context Protocol (MCP), integrates up to thousands of cross-disciplinary scientific tools, and achieves efficient orchestration of heterogeneous research tools via intention-aware dynamic tool retrieval and hot-plug mechanisms. To address long-context and large-scale data challenges in scientific settings, S1-NexusAgent introduces object-reference-based sparse context management, which enables sub-task context isolation and intermediate result compression. Building on this, a Critic Agent automatically evaluates complete execution trajectories and distills high-quality research paths into reusable Scientific Skills, forming a closed loop for continuous self-evolution, which is valuable for sustainable and long-horizon scientific research. Experiments on authoritative scientific benchmarks involving long-horizon planning and complex specialized tool orchestration, including biomini-eval (biology), ChemBench (chemistry), and MatSciBench (material science), demonstrate that S1-NexusAgent achieves state-of-the-art performance, validating its effectiveness and generalization capability in complex scientific tasks.

</details>


### 162. MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety

- **Authors:** Xiaoyu Wen, Zhida He, Han Qi, Ziyu Wan, Zhongtian Ma, Ying Wen, Tianhang Zheng, Xingcheng Xu, Chaochao Lu, Qiaosheng Zhang
- **Published:** 2026-02-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.01539v2](http://arxiv.org/abs/2602.01539v2)
- **PDF:** [https://arxiv.org/pdf/2602.01539v2](https://arxiv.org/pdf/2602.01539v2)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA


> The paper presents MAGIC, a novel multi-agent reinforcement learning framework that addresses the safety alignment of Large Language Models (LLMs) by framing it as an adversarial asymmetric game between an attacker and a defender. The methodology involves a dynamic co-evolution process where the attacker generates deceptive prompts while the defender adapts its strategy to recognize these inputs, leading to the emergence of novel strategies over iterations. Key findings indicate that MAGIC not only enhances defense success rates against evolving attacks but also maintains the helpfulness of the model, offering a robust solution for ensuring LLM safety in the context of adversarial threats.


<details>
<summary>Abstract</summary>

Ensuring robust safety alignment is crucial for Large Language Models (LLMs), yet existing defenses often lag behind evolving adversarial attacks due to their \textbf{reliance on static, pre-collected data distributions}. In this paper, we introduce \textbf{MAGIC}, a novel multi-turn multi-agent reinforcement learning framework that formulates LLM safety alignment as an adversarial asymmetric game. Specifically, an attacker agent learns to iteratively rewrite original queries into deceptive prompts, while a defender agent simultaneously optimizes its policy to recognize and refuse such inputs. This dynamic process triggers a \textbf{co-evolution}, where the attacker's ever-changing strategies continuously uncover long-tail vulnerabilities, driving the defender to generalize to unseen attack patterns. Remarkably, we observe that the attacker, endowed with initial reasoning ability, evolves \textbf{novel, previously unseen combinatorial strategies} through iterative RL training, underscoring our method's substantial potential. Theoretically, we provide insights into a more robust game equilibrium and derive safety guarantees. Extensive experiments validate our framework's effectiveness, demonstrating superior defense success rates without compromising the helpfulness of the model. Our code is available at https://github.com/BattleWen/MAGIC.

</details>



## Medrxiv (4 papers)


### 1. An AI Agent for Automated Causal Inference in Epidemiology

- **Authors:** Liu, H., Shi, K., li, A., Li, X., Chu, J., Xue, Y., Cen, S., Wang, Y., Zhang, T.
- **Published:** 2026-02-06
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.06.26345723](https://doi.org/10.64898/2026.02.06.26345723)

- **Categories:** epidemiology


> The paper presents the EpiCausalX Agent, an AI-powered tool designed to automate the traditional workflow of causal inference in epidemiology, significantly reducing inefficiencies and expertise barriers. Utilizing the LangChain framework and incorporating advanced features such as multi-database retrieval, causal reasoning based on Hills criteria, and automated DAG visualization, the agent achieves full-process automation while maintaining usability for non-technical researchers. Key findings indicate that EpiCausalX provides evidence-based, traceable conclusions and has broad applications in observational research and clinical study design, thereby enhancing the accessibility and rigor of causal analysis in the field.


<details>
<summary>Abstract</summary>

ObjectiveTo address the inefficiency, subjectivity, and high expertise barrier of traditional epidemiological causal inference, this study designed, developed, and validated an AI-powered agent (EpiCausalX Agent) to automate the end-to-end workflow. It integrates cross-database literature retrieval, intelligent causal reasoning, and Directed Acyclic Graph (DAG) visualization to provide a reliable, accessible tool for researchers.

Materials and MethodsBuilt on the LangChain 1.0 framework with a layered design (Agent/Tool/Storage/Utility Layers), the agent uses the DeepSeek V3.2 LLM and ReAct paradigm for dynamic task orchestration. Four specialized tools were integrated including multi-database retrieval with 7 databases, causal inference based on Hills criteria and DAG logic, automated DAG drawing using NetworkX and Matplotlib, and clinical standard query. Performance was validated via unit tests, workflow verification, and usability testing.

ResultsThe agent achieved full-process automation. It efficiently retrieves and synthesizes literature, automatically identifies confounders and mediators, and generates standardized interactive DAGs. It produces evidence-based, traceable conclusions aligned with established epidemiological knowledge. Its user-friendly natural language interface enables seamless use by non-technical researchers who complete task initiation quickly without operational confusion. The agent is publicly available on WeChat Mini Program for easy access.

ConclusionEpiCausalX Agent advances intelligent, automated epidemiological research. By integrating domain expertise with AI agent technology, it overcomes limitations of manual methods and general LLMs to provide a specialized, verifiable, efficient solution. It has broad applications in observational research, clinical study design, and education to enhance productivity and lower barriers to rigorous causal analysis.

</details>


### 2. Safety and Utility of an Agentic Large Language Model-Based Hospital Course Summarizer: A Prospective Real-World Pilot Study

- **Authors:** Grolleau, F., Liang, A. S., Keyes, T., Ma, S. P., Lew, T., Huynh, T. R., Steele, N., Chung, P., Qin, P., Chandra, G., Wang, S. F., Mullen, E., Carpenter, L., Hoppenfeld, M., Morrin, M., Kyerematen, B. A., Ambers, N., Kotecha, N., Alsentzer, E., Hom, J., Shah, N. H., Schulman, K., Chen, J. H.
- **Published:** 2026-02-06
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.05.26345607](https://doi.org/10.64898/2026.02.05.26345607)

- **Categories:** health informatics


> The study evaluates the safety and utility of MedAgentBrief, an agentic AI workflow based on a large language model (LLM) used to generate hospital course summaries, aiming to alleviate clinician documentation burdens. In a prospective pilot study involving 11 hospitalist physicians, it was found that 57% of generated summaries were utilized, and while some inaccuracies were noted, the potential for harm was predominantly rated as minimal. Notably, the introduction of this AI tool significantly reduced physician burnout and offered time savings in documentation, highlighting its potential to enhance clinician well-being in real-world settings.


<details>
<summary>Abstract</summary>

ImportanceHigh-quality discharge summaries are essential for safe care transitions but contribute substantially to clinician documentation burden and burnout. While retrospective studies suggest large language models (LLMs) can generate clinical summaries of comparable quality to physicians, prospective data on their safety, utility, and impact on clinician well-being in real-world environments are lacking.

ObjectiveTo evaluate the safety, utilization, and impact on clinician burden of MedAgentBrief, an LLM-based agentic workflow for generating hospital course summaries, during prospective clinical deployment.

Design, Setting, and ParticipantsSingle-arm prospective pilot study of 11 attending hospitalist physicians at one inpatient unit from August 1 to October 11, 2025, with baseline comparisons drawn from April 9 to July 31, 2025.

InterventionMedAgentBrief, a custom agentic AI workflow utilizing Gemini 2.5 Pro, generated draft hospital course summaries nightly using the patients history and physical and daily progress notes. Drafts were securely emailed to physicians daily for review and optional use.

Main Outcomes and MeasuresThe primary outcome was physician-reported potential for and severity of harm from unedited summaries (AHRQ Common Format Harm Scale). Secondary outcomes included utilization rate, error types (omissions, inaccuracies, hallucinations), time spent in discharge summaries (EHR logs), and changes in cognitive burden (NASA Task Load Index [NASA-TLX]) and burnout (Stanford Professional Fulfillment Index [PFI] Work Exhaustion Scale).

ResultsThe system generated 1274 summaries. Of 384 discharges, physicians utilized AI content in 219 (57%) cases. Feedback on 100 summaries (40.2%) noted omissions (25%) and inaccuracies (20%) but rare hallucinations (2%). Physicians rated 88% of unedited summaries as having no harm potential and 1% as likely to cause moderate harm; no severe harm was reported. Physician burnout scores decreased significantly (1.75 vs 1.20; P = .03). Time savings were heterogeneous: 71% of physicians saw reductions in median documentation time (up to 2.9 minutes).

Conclusions and RelevanceAn LLM-based agentic workflow produced hospital course summaries that were frequently utilized with mild to minimal risk of harm identified. The intervention was associated with a significant reduction in physician burnout, supporting the viability of AI summarization to mitigate documentation burden.

</details>


### 3. Drug Safety Agents Using Graphs and Ontologies

- **Authors:** Mathialagan, C. S., Nip, A., Bhat, A.
- **Published:** 2026-02-05
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.04.26345582](https://doi.org/10.64898/2026.02.04.26345582)

- **Categories:** health informatics


> The paper presents a novel knowledge-grounded framework for analyzing drug safety cases, which enhances the efficiency of pharmacovigilance using a combination of disproportionality analysis and a hallucination-risk-aware execution planner. By prioritizing deterministic graph retrieval over generative methodologies, the system improves the reliability and explainability of adverse event hypothesis generation, addressing previous shortcomings in large language models related to causal reasoning and interpretability. Key findings indicate that integrating structured medical knowledge can lead to more accurate and clinically relevant assessments, with potential for further development through causal inference modules.


<details>
<summary>Abstract</summary>

In pharmacovigilance, analyzing drug safety cases is often time consuming due to the abundance of laboratory data, complex medical histories, and intricate temporal relationships. Agentic AI systems can significantly reduce case processing time by assisting medical reviewers in surfacing clinically relevant evidence. However, previous studies have highlighted that large language models alone lack causal reasoning and evidence-based interpretability.

To address these limitations, we present a knowledge-grounded safety case analysis framework that integrates disproportionality analysis to generate and prioritize potential adverse event hypotheses. Crucially, we introduce a novel hallucination-risk-aware execution planner that dynamically routes queries to the safest reasoning pathway, prioritizing deterministic graph retrieval over generative methods for clinically sensitive signals. The system demonstrates how structured medical knowledge and statistical evidence can be combined to support a reliable, explainable case assessment and can be readily extended with causal inference modules for deeper clinical reasoning.

</details>


### 4. Automated Task-Specific vs General-Purpose Artificial Intelligence for Detecting Subtle Intraoperative Warning Signs During Cataract Surgery: A Multicenter Diagnostic Study

- **Authors:** Zhang, Y., chen, l., Zhao, W., Zhang, H., Qiao, C., Liu, Z., Chung, C. H., Tan, M. C. J., Wang, M., Tham, Y. C., Koh, V., Cheng, C., Liu, D.
- **Published:** 2026-02-03
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.01.15.26344200](https://doi.org/10.64898/2026.01.15.26344200)

- **Categories:** ophthalmology


> This study benchmarks generalist vision-language models (VLMs) against autonomous AI agents in detecting subtle intraoperative warning signs during cataract surgery, specifically anterior capsular radial folds. Utilizing a multicenter dataset of 537 video clips, it compares the performance of 11 VLMs and classifiers generated by 4 autonomous AI agents, finding that the agent-engineered classifiers significantly outperformed VLMs, achieving an F1-score of 0.869 compared to the top VLM’s score of 0.519. These results demonstrate that autonomous AI agents are more effective for task-specific applications in fine-grained surgical video analysis, thus highlighting their potential in the agentic AI field.


<details>
<summary>Abstract</summary>

ImportanceVision-language models (VLMs) enable generalist multimodal reasoning, but their ability to resolve brief, low-contrast cues in surgical video without task-specific training is uncertain. Autonomous artificial intelligence (AI) agents offer an alternative paradigm by autonomously generating supervised classifiers tailored to specific visual tasks.

ObjectiveTo benchmark the performance of VLMs against supervised classifiers engineered by autonomous AI agents for detecting anterior capsular radial folds during continuous curvilinear capsulorhexis (CCC), and to compare both approaches with human graders.

Design, Setting, and ParticipantsThis retrospective diagnostic study utilized a multicenter dataset of 537 CCC videos collected from Beijing Tongren Hospital (China), National University Hospital (Singapore), and the OphNet-APTOS public dataset.

ExposurePresence or absence of anterior capsular radial folds during CCC, defined based on established expert consensus, was annotated at both clip and frame levels by senior glaucoma surgeons. Two analytic paradigms were evaluated: (1) direct zero-shot and few-shot inference using 11 generalist and medical-specific VLMs on single frames and frame sequences; and (2) autonomous code generation by 4 AI agents to construct supervised image classifiers from labeled frames. Human comparison included 7 graders with varying levels of ophthalmic experience.

Main Outcomes and MeasuresDiscrimination of fold-positive versus fold-negative cases was assessed using macro-averaged precision, recall, and F1-score at the clip and frame levels. Secondary outcomes included comparisons with human graders.

ResultsAmong 537 video clips (7.32 {+/-} 3.35 seconds), 156 (29.1%) were fold-positive. VLM performance was limited; the top-performing model, Qwen2.5-VL, achieved a mean F1-score of 0.519. Few-shot prompting improved GPT-4.1 performance (mean F1-score from 0.177 to 0.480) but remained unstable. In contrast, an agent-engineered classifier achieved an F1-score of 0.869 and an area under the receiver operating characteristic curve of 0.958. In comparison with human graders, the top agent-generated model (F1-score, 0.835) matched junior specialists (mean F1-score, 0.829), whereas fine-tuned VLMs (maximum F1-score, 0.606) underperformed all human graders.

Conclusions and RelevanceGeneralist VLMs showed limited capacity to detect subtle intraoperative cues, whereas autonomous AI agents successfully constructed task-specific classifiers with near-clinical-level performance. These findings support agent-driven supervised modeling as a more effective strategy for fine-grained surgical video interpretation.

Key PointsO_ST_ABSQuestionC_ST_ABSHow do generalist vision-language models (VLMs) and autonomous AI agents compare with human graders in detecting brief, low-contrast intraoperative cues in surgical video?

FindingsIn this retrospective, multicenter diagnostic benchmarking study of 537 phacoemulsification video clips, VLMs showed limited discrimination of anterior capsular radial folds, even with few-shot prompting, whereas autonomous AI agents successfully generated supervised classifiers with substantially higher performance, approaching that of junior glaucoma specialists.

MeaningFor fine-grained intraoperative video interpretation, task-specific classifiers engineered by autonomous agents currently demonstrate greater clinical relevance than generalist VLMs.

</details>



## Biorxiv (1 papers)


### 1. Optimizing Motor Skills with HD-tDCS: Insights from a Pilot Study on Chopstick Proficiency

- **Authors:** Scholl, J. L., Bosch, T. J., Baugh, L. A.
- **Published:** 2026-02-02
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.01.30.702932](https://doi.org/10.64898/2026.01.30.702932)

- **Categories:** neuroscience


> This study explores how high-definition transcranial direct current stimulation (HD-tDCS) applied to the anterior supramarginal gyrus (aSMG) impacts motor learning, specifically in the context of chopstick proficiency. Utilizing a double-blind, sham-controlled design with 24 participants, the research found that participants receiving active stimulation demonstrated a significant increase in successful marble drops per minute (17.3 vs. 14.1), along with altered kinematic patterns and enhanced gamma-band activity, suggesting that HD-tDCS can effectively boost motor skill acquisition. These findings contribute to the agentic AI field by highlighting the neuromodulation techniques that might enhance human motor learning, relevant for developing AI systems that mimic or augment human skill acquisition processes.


<details>
<summary>Abstract</summary>

This study extends our previous research on neurological adaptations associated with learning to use chopsticks, in which we observed increased functional activity and connectivity changes in the anterior supramarginal gyrus (aSMG), a brain region previously implicated in novel tool use. In the present study, we investigated the effects of high-definition transcranial direct current stimulation (HD-tDCS) on motor learning by applying anodal stimulation to the aSMG in a double-blind, sham-controlled design with 24 participants (12 active, 12 sham). Participants in the active condition received [~]3 mA of HD-tDCS focused over the aSMG while watching a 20-minute video of the task - picking up a marble with chopsticks and dropping it into a cylindrical container. In comparison, participants in the sham condition watched the same video while receiving sham stimulation consisting of a 30-s ramp-up and ramp-down at the start and end of the 20-minute video. Immediately after the video task, all participants completed 15 one-minute trials in which they performed the task while electroencephalography (EEG) was recorded. Performance was assessed by the average number of successful marble drops per minute (MDPM) across trials. Additionally, video-based motion was analyzed using DeepLabCut to compare key kinematic metrics, providing insights into subtle variations in movement patterns during the marble task. Results showed a significant increase in MDPM in the active stimulation group compared to the sham group (17. 3 vs. 14. 1 MDPM; p < .05). Kinematic data showed increased movement jerk in the active stimulation group compared to sham (21719 vs 16926; p < .05), and EEG revealed differences in task-related gamma-band power over Cz (.0227 vs -.0758; p < .05). These findings suggest that HD-tDCS enhances the rate of motor learning in novel tool use and underscore the potential of aSMG-targeted stimulation in facilitating complex motor tasks. Further studies are warranted to explore the broader applicability of HD-tDCS in skill acquisition and rehabilitation.

New and NoteworthyThe presented study shows the role that the left anterior supramarginal gyrus plays in experience-independent tool learning. Anodal HD-tDCS applied during action observation increased performance in a subsequent chopstick skill acquisition task. This increase in performance was accompanied by enhanced task-related gamma-band activity and altered movement kinematics. By linking neuromodulation of the parietal tool-use hub to behavioral, kinematics, and electrophysiological changes, these findings significantly advance our understanding of how higher-order sensorimotor networks support tool-use learning.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*