# Weekly AI Agent Paper Report

**Generated:** 2026-02-16 10:07
**Period:** 2026-02-09 to 2026-02-15

## Summary

- **Total papers fetched:** 1016
- **Papers matching keywords:** 124
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-02-09) | Change |
|--------|-----------|-----------|--------|
| Total matched | 124 | 167 | -43 |
| arxiv | 120 | 162 | -42 |
| biorxiv | 2 | 1 | +1 |
| medrxiv | 2 | 4 | -2 |

### Notable Trends

1. **Decrease in Volume**: This week saw a notable decrease in the number of AI agent papers published, from 167 last week to 124. This decline indicates a potential seasonal slowdown or a shift in focus temporarily away from AI agent topics.

2. **Source Distribution Shift**: This week saw a significantly higher contribution from arXiv (120 papers) compared to last week, where arXiv contributed 162. Meanwhile, medRxiv papers decreased from 4 to 2, suggesting a reduced emphasis on health-related AI agent research in the current week.

3. **Emerging Research Areas**: Current week papers emphasize topics such as metagenomics, innovative benchmarking for multimodal agents, and autonomous network incident responses. This reflects a shift towards practical, application-driven research whereas last week’s papers predominantly centered around theoretical frameworks and explanations.

4. **Advanced Benchmarking Focus**: The introduction of multiple benchmarking papers in the current week (e.g., SciAgentGym, SkillsBench, BrowseComp-$V^3$) suggests an increased focus on evaluating AI agent capabilities across diverse tasks, indicating a maturation in the field’s approach to performance assessment.

5. **Consistency in Hospital AI Applications**: There continues to be substantial interest in AI applications related to healthcare, with multiple mentions in both weeks, highlighting a persistent focus on integrating AI agents within medical contexts, as seen in papers focusing on summarizing hospital courses and causal inference in epidemiology.

---



## Biomedical Highlights (4 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


The first paper explores the causal relationship linking language and tool use through the putamen, highlighting the cognitive mechanism that organizes symbols and actions into structured sequences. Using neuroimaging techniques, the study investigates how these two complex cognitive processes are interrelated in humans. 

The second paper introduces MetaKnogic-Alpha, a hyper-relational knowledge base designed for metabolic reasoning, addressing the issue of fragmented knowledge in metabolic research. The authors employ advanced AI methods to synthesize vast amounts of biomedical literature, facilitating a more comprehensive understanding of metabolic pathways and their implications.

The third paper discusses the application of AI in predicting Inflammatory Bowel Disease (IBD) and recommending probiotics based on metagenomic analysis. By analyzing gut microbiome signatures, the study elucidates the relationship between dysbiosis and autoimmune diseases, showcasing how AI can enhance diagnostic and therapeutic strategies.

The fourth paper evaluates the MedAgentBrief system aimed at summarizing hospital courses to alleviate documentation burden on clinicians during discharge processes. This AI-driven tool focuses on producing high-quality summaries that ensure safe transitions of care while reducing clinician burnout, thus highlighting the role of AI in improving clinical workflows. 

Across these papers, key themes include the integration of AI in interpreting complex biological and cognitive data, addressing knowledge fragmentation in biomedicine, and improving clinician efficiency through automated summarization technologies. Methodologies range from neuroimaging and metagenomic analysis to the development of knowledge bases and AI-driven systems for documentation purposes.



### 1. Causal evidence for a shared mechanism linking language and tool use via the putamen

- **Authors:** Fan, Z., Wen, H., Han, Z., Wang, X., Bi, Y.
- **Published:** 2026-02-09
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.02.06.704290](https://doi.org/10.64898/2026.02.06.704290)

- **Categories:** neuroscience


> This paper identifies the putamen as a critical neural substrate linking human language and tool use through a shared mechanism that supports goal-dependent sequence integrity. The researchers employed brain lesion analysis, developmental contrasts, and functional neuroimaging involving 100 adults with focal brain injuries, revealing that damage to the putamen impaired both sentence processing and tool use. Key findings indicate that early language acquisition enhances tool-use performance and strengthens putaminal responses, highlighting the importance of this brain region in agentic AI systems that aim to replicate or understand human-like cognitive processes.


<details>
<summary>Abstract</summary>

Both human language and tool use--two hallmark capacities of human cognition--depend on organizing discrete elements, i.e., symbols and actions, into highly constrained structured sequences to achieve a functional goal. However, the neural mechanism linking these capacities is unclear. We combined brain lesion analysis, developmental contrast, and functional neuroimaging to test whether the basal ganglia play a causal role in their shared capacity. In 100 adults with focal brain injury, damage to the putamen disrupted both sentence processing and tool use, with impairments specifically explained by reduced goal-dependent sequence integrity for both tasks. Further comparing populations with typical and deprived early language experience (congenitally deaf adults with vs. without early sign language exposure), we found that early language acquisition was associated with improved tool-use performance and strengthened putaminal responses to such goal dependency, which mediated the relationship between sentence sequence integrity and tool behavior. Together, these results identify the putamen as a key neural substrate supporting goal-dependent sequence integrity across language and action, and show how early language experience shapes this conserved control system.

One-Sentence SummaryLanguage and tool use share a putamen-based mechanism that supports goal-dependent sequence integrity, and this mechanism is strengthened by early language experience.

</details>


### 2. MetaKnogic-Alpha: A Hyper-Relational Knowledge Base for Grounded Metabolic Reasoning

- **Authors:** Dang, P., Swaminathan, P., Guo, T., Wan, C., Cao, S., Zhang, C.
- **Published:** 2026-02-09
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.02.05.704050](https://doi.org/10.64898/2026.02.05.704050)

- **Categories:** bioinformatics


> The main contribution of the paper is the development of MetaKnogic-Alpha, a hyper-relational knowledge base designed to synthesize and organize biomedical literature related to metabolic research, facilitating grounded metabolic reasoning. The methodology involves transforming over 100,000 full-text articles into a hypergraph structure that captures complex relationships within metabolic pathways, utilizing an autonomous reasoning agent to enhance query precision and perform multi-hop expansions to identify critical biological relationships while ensuring rigorous validity through deterministic grounding against a curated metabolic network. Key findings indicate that MetaKnogic-Alpha achieves a mechanistic accuracy of 0.98 in providing reliable insights derived from literature, significantly improving the efficiency of metabolic research by automating synthesis that historically required extensive manual effort, thus enhancing the capabilities of agents in precision oncology.


<details>
<summary>Abstract</summary>

The exponential trajectory of biomedical literature has precipitated a fundamental "synthesis gap" in metabolic research, where critical mechanistic insights remain fragmented across hundreds of thousands of disjointed full-text articles, preventing the consolidation of a global mechanistic view. Here, we present MetaKnogic-Alpha, a foundational mechanistic knowledge substrate designed to bridge this gap by transforming unstructured literature into a navigable, logic-based resource. MetaKnogic-Alpha synthesizes over 100K full-text articles into a hyper-relational hypergraph structure, preserving the n-ary relational logic inherent in complex metabolic pathways. To ensure biological rigor, we implemented a hierarchical discovery protocol: an autonomous reasoning agent first enriches query nomenclature for domain-specific precision, followed by a multi-hop topological expansion within the hypergraph to surface functional neighbors, such as enzymatic co-factors and distal regulators, often lost in traditional search paradigms. Crucially, the system subjects all literature-derived insights to a deterministic biochemical grounding against a curated metabolic reaction network, significantly mitigating the risk of probabilistic hallucinations common in standalone generative models. In rigorous benchmarking, MetaKnogic-Alpha achieved a mechanistic accuracy of 0.98 in scenarios where supporting evidence was present, providing a robustly attributable audit trail back to the primary literature via PubMed Central Identifiers. We designate this primary release as "alpha" to establish the foundational architectural logic for a burgeoning million-scale resource. By compressing the synthesis of thousands of papers from a multi-month manual effort into several hours of automated discovery, MetaKnogic-Alpha serves as a high-fidelity research companion that augments the human experts ability to resolve complex metabolic interactions and identify novel therapeutic drivers in precision oncology.

</details>


### 3. Metagenomics AI powered prediction of Inflammatory Bowel Disease and Probiotic Recommendation

- **Authors:** Kumar, S. N., Thomas, M., Janakiram, S., M, N., Subramaniam, S. N.
- **Published:** 2026-02-15
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.12.26345333](https://doi.org/10.64898/2026.02.12.26345333)

- **Categories:** gastroenterology


> This paper presents a novel AI-driven predictive tool for identifying the inflammatory bowel disease (IBD) status based on gut microbiome composition, utilizing machine learning techniques such as XGBoost. The methodology involves processing metagenomic data to generate taxonomic profiles, which are then analyzed to determine dysbiosis and subsequently provide personalized probiotic recommendations. Key findings include an 86.6% accuracy in predicting IBD status and identifying specific dysbiotic taxa, highlighting an innovative approach in the agentic AI field for disease prediction and personalized health recommendations.


<details>
<summary>Abstract</summary>

Background and Objective The dysbiosis of human gut microbiome has been increasingly seen to have a relation in the development of autoimmune diseases, with specific microbial signatures having causative association with specific conditions. Inflammatory bowel disease (IBD) is one such autoimmune ailment. This paper proposes a predictive tool that can identify the IBD status of an individual based on the composition of the gut microbiome using machine learning and AI agents driven techniques. The technology can strengthen the suspicion of a potential IBD diagnosis a patient may have based on their gut microbiome profile. Methods The tool processes patient gut metagenome using integrated Kneaddata and MetaPhlAn to generate taxonomic profiles. These are fed into an XGBoost classifier to predict IBD or healthy status. Dysbiotic taxa are identified via Z-score and fold change. CrewAI delivers personalized probiotic recommendations based on diagnosis and dysbiosis. Results The tuned XGBoost model achieved 86.6% accuracy. On validation using single ulcerative colitis sample, the tool correctly predicted IBD status but misclassified it as Crohns disease(possibly due to overlapping microbial signatures), identifying Faecalibacterium and Flavonifractor as dysbiotic taxa.The probiotic recommended was Faecalibacterium prausnitzii ,backed with reasoning basedon scientific literature. Conclusions Despite limited validation sample size, the high accuracy , correct IBD detection ,dysbiosis analysis and elaborate probiotic recommendation suggest promising potential; further validation needed

</details>


### 4. MedAgentBrief for Hospital Course Summarization: Safety, Use, and Discharge Documentation Burden

- **Authors:** Grolleau, F., Liang, A. S., Keyes, T., Ma, S. P., Lew, T., Huynh, T. R., Steele, N., Chung, P., Qin, P., Chandra, G., Wang, S. F., Mullen, E., Carpenter, L., Hoppenfeld, M., Morrin, M., Kyerematen, B. A., Ambers, N., Kotecha, N., Alsentzer, E., Hom, J., Shah, N. H., Schulman, K., Chen, J. H.
- **Published:** 2026-02-10
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.05.26345607](https://doi.org/10.64898/2026.02.05.26345607)

- **Categories:** health informatics


> The paper presents MedAgentBrief, an LLM-based agentic workflow designed to generate hospital course summaries, and evaluates its safety, utility, and impact on clinician burden through a prospective pilot study involving 11 hospitalist physicians. The methodology involved generating nightly summaries using a custom AI model, followed by physician review, with results indicating that 57% of summaries were utilized, and physicians reported minimal risk of harm from unedited versions, along with a significant decrease in burnout scores by utilizing the tool. Key findings support the potential of agentic AI systems like MedAgentBrief to alleviate documentation burdens in healthcare settings while maintaining summary quality.


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


---



## Medrxiv (2 papers)


### 1. Metagenomics AI powered prediction of Inflammatory Bowel Disease and Probiotic Recommendation

- **Authors:** Kumar, S. N., Thomas, M., Janakiram, S., M, N., Subramaniam, S. N.
- **Published:** 2026-02-15
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.12.26345333](https://doi.org/10.64898/2026.02.12.26345333)

- **Categories:** gastroenterology


> This paper presents a novel AI-driven predictive tool for identifying the inflammatory bowel disease (IBD) status based on gut microbiome composition, utilizing machine learning techniques such as XGBoost. The methodology involves processing metagenomic data to generate taxonomic profiles, which are then analyzed to determine dysbiosis and subsequently provide personalized probiotic recommendations. Key findings include an 86.6% accuracy in predicting IBD status and identifying specific dysbiotic taxa, highlighting an innovative approach in the agentic AI field for disease prediction and personalized health recommendations.


<details>
<summary>Abstract</summary>

Background and Objective The dysbiosis of human gut microbiome has been increasingly seen to have a relation in the development of autoimmune diseases, with specific microbial signatures having causative association with specific conditions. Inflammatory bowel disease (IBD) is one such autoimmune ailment. This paper proposes a predictive tool that can identify the IBD status of an individual based on the composition of the gut microbiome using machine learning and AI agents driven techniques. The technology can strengthen the suspicion of a potential IBD diagnosis a patient may have based on their gut microbiome profile. Methods The tool processes patient gut metagenome using integrated Kneaddata and MetaPhlAn to generate taxonomic profiles. These are fed into an XGBoost classifier to predict IBD or healthy status. Dysbiotic taxa are identified via Z-score and fold change. CrewAI delivers personalized probiotic recommendations based on diagnosis and dysbiosis. Results The tuned XGBoost model achieved 86.6% accuracy. On validation using single ulcerative colitis sample, the tool correctly predicted IBD status but misclassified it as Crohns disease(possibly due to overlapping microbial signatures), identifying Faecalibacterium and Flavonifractor as dysbiotic taxa.The probiotic recommended was Faecalibacterium prausnitzii ,backed with reasoning basedon scientific literature. Conclusions Despite limited validation sample size, the high accuracy , correct IBD detection ,dysbiosis analysis and elaborate probiotic recommendation suggest promising potential; further validation needed

</details>


### 2. MedAgentBrief for Hospital Course Summarization: Safety, Use, and Discharge Documentation Burden

- **Authors:** Grolleau, F., Liang, A. S., Keyes, T., Ma, S. P., Lew, T., Huynh, T. R., Steele, N., Chung, P., Qin, P., Chandra, G., Wang, S. F., Mullen, E., Carpenter, L., Hoppenfeld, M., Morrin, M., Kyerematen, B. A., Ambers, N., Kotecha, N., Alsentzer, E., Hom, J., Shah, N. H., Schulman, K., Chen, J. H.
- **Published:** 2026-02-10
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.05.26345607](https://doi.org/10.64898/2026.02.05.26345607)

- **Categories:** health informatics


> The paper presents MedAgentBrief, an LLM-based agentic workflow designed to generate hospital course summaries, and evaluates its safety, utility, and impact on clinician burden through a prospective pilot study involving 11 hospitalist physicians. The methodology involved generating nightly summaries using a custom AI model, followed by physician review, with results indicating that 57% of summaries were utilized, and physicians reported minimal risk of harm from unedited versions, along with a significant decrease in burnout scores by utilizing the tool. Key findings support the potential of agentic AI systems like MedAgentBrief to alleviate documentation burdens in healthcare settings while maintaining summary quality.


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



## Arxiv (120 papers)


### 1. In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Approach

- **Authors:** Yiran Gao, Kim Hammar, Tao Li
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13156v1](http://arxiv.org/abs/2602.13156v1)
- **PDF:** [https://arxiv.org/pdf/2602.13156v1](https://arxiv.org/pdf/2602.13156v1)
- **Categories:** cs.CR, cs.AI


> The paper presents a novel incident response system for cyberattacks that leverages large language models (LLMs) to autonomously adapt to evolving threats, addressing limitations in traditional reinforcement learning approaches that rely on handcrafted simulations. The proposed end-to-end agent integrates perception, reasoning, planning, and action functionalities within a single lightweight LLM, enabling it to process system logs, update attack models, simulate outcomes, and generate effective responses through in-context learning. Key findings include the agent's ability to refine its strategies based on comparisons of simulated outcomes with actual observations, resulting in incident recovery that is up to 23% faster than current leading LLMs.


<details>
<summary>Abstract</summary>

Rapidly evolving cyberattacks demand incident response systems that can autonomously learn and adapt to changing threats. Prior work has extensively explored the reinforcement learning approach, which involves learning response strategies through extensive simulation of the incident. While this approach can be effective, it requires handcrafted modeling of the simulator and suppresses useful semantics from raw system logs and alerts. To address these limitations, we propose to leverage large language models' (LLM) pre-trained security knowledge and in-context learning to create an end-to-end agentic solution for incident response planning. Specifically, our agent integrates four functionalities, perception, reasoning, planning, and action, into one lightweight LLM (14b model). Through fine-tuning and chain-of-thought reasoning, our LLM agent is capable of processing system logs and inferring the underlying network state (perception), updating its conjecture of attack models (reasoning), simulating consequences under different response strategies (planning), and generating an effective response (action). By comparing LLM-simulated outcomes with actual observations, the LLM agent repeatedly refines its attack conjecture and corresponding response, thereby demonstrating in-context adaptation. Our agentic approach is free of modeling and can run on commodity hardware. When evaluated on incident logs reported in the literature, our agent achieves recovery up to 23% faster than those of frontier LLMs.

</details>


### 2. TraceBack: Multi-Agent Decomposition for Fine-Grained Table Attribution

- **Authors:** Tejas Anvekar, Junha Park, Rajat Jha, Devanshu Gupta, Poojah Ganesan, Puneeth Mathur, Vivek Gupta
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13059v1](http://arxiv.org/abs/2602.13059v1)
- **PDF:** [https://arxiv.org/pdf/2602.13059v1](https://arxiv.org/pdf/2602.13059v1)
- **Categories:** cs.CL


> The paper presents TraceBack, a modular multi-agent framework designed to enhance fine-grained attribution in single-table question answering (QA) by effectively tracking which table cells support specific answers. The methodology involves pruning irrelevant table sections, decomposing the main question into coherent sub-questions, and aligning answer spans with their corresponding supporting cells to capture both explicit and implicit reasoning evidence. Key findings demonstrate that TraceBack significantly outperforms existing systems in terms of attribution quality across various datasets, while the newly proposed FairScore metric effectively evaluates attribution precision and recall without the need for human cell annotations, thereby promoting greater transparency and trust in automated table QA systems.


<details>
<summary>Abstract</summary>

Question answering (QA) over structured tables requires not only accurate answers but also transparency about which cells support them. Existing table QA systems rarely provide fine-grained attribution, so even correct answers often lack verifiable grounding, limiting trust in high-stakes settings. We address this with TraceBack, a modular multi-agent framework for scalable, cell-level attribution in single-table QA. TraceBack prunes tables to relevant rows and columns, decomposes questions into semantically coherent sub-questions, and aligns each answer span with its supporting cells, capturing both explicit and implicit evidence used in intermediate reasoning steps. To enable systematic evaluation, we release CITEBench, a benchmark with phrase-to-cell annotations drawn from ToTTo, FetaQA, and AITQA. We further propose FairScore, a reference-less metric that compares atomic facts derived from predicted cells and answers to estimate attribution precision and recall without human cell labels. Experiments show that TraceBack substantially outperforms strong baselines across datasets and granularities, while FairScore closely tracks human judgments and preserves relative method rankings, supporting interpretable and scalable evaluation of table-based QA.

</details>


### 3. SciAgentGym: Benchmarking Multi-Step Scientific Tool-use in LLM Agents

- **Authors:** Yujiong Shen, Yajie Yang, Zhiheng Xi, Binze Hu, Huayu Sha, Jiazheng Zhang, Qiyuan Peng, Junlin Shang, Jixuan Huang, Yutao Fan, Jingqi Tong, Shihan Dou, Ming Zhang, Lei Bai, Zhenfei Yin, Tao Gui, Xingjun Ma, Qi Zhang, Xuanjing Huang, Yu-Gang Jiang
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12984v1](http://arxiv.org/abs/2602.12984v1)
- **PDF:** [https://arxiv.org/pdf/2602.12984v1](https://arxiv.org/pdf/2602.12984v1)
- **Categories:** cs.CL


> The paper introduces SciAgentGym, a novel benchmarking environment designed to evaluate the capabilities of large language model (LLM) agents in using scientific tools across four domains, highlighting a significant gap in existing benchmarks regarding complex tool orchestration. The methodology includes a comprehensive evaluation framework, SciAgentBench, which assesses agent performance through simple to intricate workflows, revealing that leading models like GPT-5 face substantial challenges with multi-step tasks. Key findings indicate that effective tool-use diminishes notably as task complexity increases, and the development of SciForge, a method that leverages dependency graphs for training, enables their model SciAgent-8B to outperform larger counterparts and improve cross-domain tool-use skills, indicating the potential for advanced autonomous scientific agents.


<details>
<summary>Abstract</summary>

Scientific reasoning inherently demands integrating sophisticated toolkits to navigate domain-specific knowledge. Yet, current benchmarks largely overlook agents' ability to orchestrate tools for such rigorous workflows. To bridge this gap, we introduce SciAgentGym, a scalable interactive environment featuring 1,780 domain-specific tools across four natural science disciplines, supported by a robust execution infrastructure. Complementing this, we present SciAgentBench, a tiered evaluation suite designed to stress-test agentic capabilities from elementary actions to long-horizon workflows. Our evaluation identifies a critical bottleneck: state-of-the-art models struggle with complex scientific tool-use. Even for a leading model like GPT-5, success rates drop sharply from 60.6% to 30.9% as interaction horizons extend, primarily due to failures in multi-step workflow execution. To address this, we propose SciForge, a data synthesis method that models the tool action space as a dependency graph to generate logic-aware training trajectories. By fine-tuning on these trajectories, our SciAgent-8B outperforms the significantly larger Qwen3-VL-235B-Instruct while exhibiting positive cross-domain transfer of scientific tool-use capabilities. These results underscore the promising potential of next-generation autonomous scientific agents.

</details>


### 4. BrowseComp-$V^3$: A Visual, Vertical, and Verifiable Benchmark for Multimodal Browsing Agents

- **Authors:** Huanyao Zhang, Jiepeng Zhou, Bo Li, Bowen Zhou, Yanzhe Dan, Haishan Lu, Zhiyong Cao, Jiaoyang Chen, Yuqian Han, Zinan Sheng, Zhengwei Tao, Hao Liang, Jialong Wu, Yang Shi, Yuanpeng He, Jiaye Lin, Qintong Zhang, Guochen Yan, Runhao Zhao, Zhengpin Li, Xiaohan Yu, Lang Mei, Chong Chen, Wentao Zhang, Bin Cui
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12876v1](http://arxiv.org/abs/2602.12876v1)
- **PDF:** [https://arxiv.org/pdf/2602.12876v1](https://arxiv.org/pdf/2602.12876v1)
- **Categories:** cs.AI


> The paper presents BrowseComp-$V^3$, a new benchmark aimed at evaluating multimodal browsing agents, addressing previous limitations in task complexity and evaluation granularity. It comprises 300 challenging questions requiring complex multi-hop reasoning across textual and visual modalities, with a focus on reproducibility through publicly searchable evidence. Key findings reveal that state-of-the-art models struggle significantly, achieving only 36% accuracy, underscoring critical gaps in multimodal integration and perception capabilities in agentic AI.


<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs), equipped with increasingly advanced planning and tool-use capabilities, are evolving into autonomous agents capable of performing multimodal web browsing and deep search in open-world environments. However, existing benchmarks for multimodal browsing remain limited in task complexity, evidence accessibility, and evaluation granularity, hindering comprehensive and reproducible assessments of deep search capabilities. To address these limitations, we introduce BrowseComp-$V^3$, a novel benchmark consisting of 300 carefully curated and challenging questions spanning diverse domains. The benchmark emphasizes deep, multi-level, and cross-modal multi-hop reasoning, where critical evidence is interleaved across textual and visual modalities within and across web pages. All supporting evidence is strictly required to be publicly searchable, ensuring fairness and reproducibility. Beyond final-answer accuracy, we incorporate an expert-validated, subgoal-driven process evaluation mechanism that enables fine-grained analysis of intermediate reasoning behaviors and systematic characterization of capability boundaries. In addition, we propose OmniSeeker, a unified multimodal browsing agent framework integrating diverse web search and visual perception tools. Comprehensive experiments demonstrate that even state-of-the-art models achieve only 36% accuracy on our benchmark, revealing critical bottlenecks in multimodal information integration and fine-grained perception. Our results highlight a fundamental gap between current model capabilities and robust multimodal deep search in real-world settings.

</details>


### 5. SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

- **Authors:** Xiangyi Li, Wenbo Chen, Yimin Liu, Shenghan Zheng, Xiaokun Chen, Yifeng He, Yubo Li, Bingran You, Haotian Shen, Jiankai Sun, Shuyi Wang, Qunhong Zeng, Di Wang, Xuandong Zhao, Yuanli Wang, Roey Ben Chaim, Zonglin Di, Yipeng Gao, Junwei He, Yizhuo He, Liqiang Jing, Luyang Kong, Xin Lan, Jiachen Li, Songlin Li, Yijiang Li, Yueqian Lin, Xinyi Liu, Xuanqing Liu, Haoran Lyu, Ze Ma, Bowei Wang, Runhui Wang, Tianyu Wang, Wengao Ye, Yue Zhang, Hanwen Xing, Yiqi Xue, Steven Dillmann, Han-chung Lee
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12670v1](http://arxiv.org/abs/2602.12670v1)
- **PDF:** [https://arxiv.org/pdf/2602.12670v1](https://arxiv.org/pdf/2602.12670v1)
- **Categories:** cs.AI


> The paper presents SkillsBench, a comprehensive benchmark designed to evaluate the effectiveness of Agent Skills across 86 tasks in 11 domains, addressing the lack of standardized measurement in the agentic AI field. The methodology involved testing various agent-model configurations under conditions with no Skills, curated Skills, and self-generated Skills, revealing that curated Skills significantly improved task performance by an average of 16.2 percentage points, although results varied by domain. Key findings indicate that curated Skills are more effective than self-generated Skills, which showed no average benefit, and that smaller models can achieve performance parity with larger models when utilizing Skills, suggesting a strategic advantage in focused skill application.


<details>
<summary>Abstract</summary>

Agent Skills are structured packages of procedural knowledge that augment LLM agents at inference time. Despite rapid adoption, there is no standard way to measure whether they actually help. We present SkillsBench, a benchmark of 86 tasks across 11 domains paired with curated Skills and deterministic verifiers. Each task is evaluated under three conditions: no Skills, curated Skills, and self-generated Skills. We test 7 agent-model configurations over 7,308 trajectories. Curated Skills raise average pass rate by 16.2 percentage points(pp), but effects vary widely by domain (+4.5pp for Software Engineering to +51.9pp for Healthcare) and 16 of 84 tasks show negative deltas. Self-generated Skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming. Focused Skills with 2--3 modules outperform comprehensive documentation, and smaller models with Skills can match larger models without them.

</details>


### 6. Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents

- **Authors:** Ruihan Yang, Fanghua Ye, Xiang We, Ruoqing Zhao, Kang Luo, Xinbo Xu, Bo Zhao, Ruotian Ma, Shanyi Wang, Zhaopeng Tu, Xiaolong Li, Deqing Yang, Linus
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12662v1](http://arxiv.org/abs/2602.12662v1)
- **PDF:** [https://arxiv.org/pdf/2602.12662v1](https://arxiv.org/pdf/2602.12662v1)
- **Categories:** cs.AI, cs.CL


> The paper presents CogRouter, a novel framework for training large language model (LLM) agents to adapt their cognitive depth dynamically during multi-turn decision-making tasks. By leveraging ACT-R theory, it establishes a hierarchical cognitive structure and employs a two-stage training method that includes Cognition-aware Supervised Fine-tuning and Cognition-aware Policy Optimization to improve efficiency and performance. The experiments show that CogRouter significantly outperforms existing models, achieving an 82.3% success rate with 62% fewer tokens used, demonstrating enhanced adaptability to varying cognitive demands in agentic AI applications.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as autonomous agents for multi-turn decision-making tasks. However, current agents typically rely on fixed cognitive patterns: non-thinking models generate immediate responses, while thinking models engage in deep reasoning uniformly. This rigidity is inefficient for long-horizon tasks, where cognitive demands vary significantly from step to step, with some requiring strategic planning and others only routine execution. In this paper, we introduce CogRouter, a framework that trains agents to dynamically adapt cognitive depth at each step. Grounded in ACT-R theory, we design four hierarchical cognitive levels ranging from instinctive responses to strategic planning. Our two-stage training approach includes Cognition-aware Supervised Fine-tuning (CoSFT) to instill stable level-specific patterns, and Cognition-aware Policy Optimization (CoPO) for step-level credit assignment via confidence-aware advantage reweighting. The key insight is that appropriate cognitive depth should maximize the confidence of the resulting action. Experiments on ALFWorld and ScienceWorld demonstrate that CogRouter achieves state-of-the-art performance with superior efficiency. With Qwen2.5-7B, it reaches an 82.3% success rate, outperforming GPT-4o (+40.3%), OpenAI-o3 (+18.3%), and GRPO (+14.0%), while using 62% fewer tokens.

</details>


### 7. AI Agents for Inventory Control: Human-LLM-OR Complementarity

- **Authors:** Jackie Baek, Yaopeng Fu, Will Ma, Tianyi Peng
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12631v1](http://arxiv.org/abs/2602.12631v1)
- **PDF:** [https://arxiv.org/pdf/2602.12631v1](https://arxiv.org/pdf/2602.12631v1)
- **Categories:** cs.AI, cs.HC, cs.LG


> The paper introduces InventoryBench, a benchmark comprising over 1,000 inventory instances, to examine the collaborative efficacy of operations research (OR) algorithms, large language models (LLMs), and human decision-makers in inventory control under various conditions. The methodology reveals that integrating OR with LLM strategies enhances performance compared to using either alone, indicating a complementary relationship. Key findings highlight that human-AI collaboration can lead to higher profits compared to independent operation, with a significant portion of individuals benefiting from this collaborative approach, thereby contributing to the understanding of agentic AI in decision-making contexts.


<details>
<summary>Abstract</summary>

Inventory control is a fundamental operations problem in which ordering decisions are traditionally guided by theoretically grounded operations research (OR) algorithms. However, such algorithms often rely on rigid modeling assumptions and can perform poorly when demand distributions shift or relevant contextual information is unavailable. Recent advances in large language models (LLMs) have generated interest in AI agents that can reason flexibly and incorporate rich contextual signals, but it remains unclear how best to incorporate LLM-based methods into traditional decision-making pipelines.
  We study how OR algorithms, LLMs, and humans can interact and complement each other in a multi-period inventory control setting. We construct InventoryBench, a benchmark of over 1,000 inventory instances spanning both synthetic and real-world demand data, designed to stress-test decision rules under demand shifts, seasonality, and uncertain lead times. Through this benchmark, we find that OR-augmented LLM methods outperform either method in isolation, suggesting that these methods are complementary rather than substitutes.
  We further investigate the role of humans through a controlled classroom experiment that embeds LLM recommendations into a human-in-the-loop decision pipeline. Contrary to prior findings that human-AI collaboration can degrade performance, we show that, on average, human-AI teams achieve higher profits than either humans or AI agents operating alone. Beyond this population-level finding, we formalize an individual-level complementarity effect and derive a distribution-free lower bound on the fraction of individuals who benefit from AI collaboration; empirically, we find this fraction to be substantial.

</details>


### 8. Multi-Agent Model-Based Reinforcement Learning with Joint State-Action Learned Embeddings

- **Authors:** Zhizun Wang, David Meger
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12520v1](http://arxiv.org/abs/2602.12520v1)
- **PDF:** [https://arxiv.org/pdf/2602.12520v1](https://arxiv.org/pdf/2602.12520v1)
- **Categories:** cs.LG, cs.MA


> The paper introduces a new model-based multi-agent reinforcement learning framework that integrates joint state-action representation learning with imaginative roll-outs to enhance coordination in dynamic environments. The methodology involves using a world model augmented with state-action learned embeddings (SALE), which are applied in both predicting future trajectories and estimating joint action values through a mixing network. Key findings show that this approach leads to improved long-term planning and optimization, outperforming baseline algorithms in various multi-agent benchmarks, thereby highlighting the significance of SALE for effective decision-making in multi-agent systems.


<details>
<summary>Abstract</summary>

Learning to coordinate many agents in partially observable and highly dynamic environments requires both informative representations and data-efficient training. To address this challenge, we present a novel model-based multi-agent reinforcement learning framework that unifies joint state-action representation learning with imaginative roll-outs. We design a world model trained with variational auto-encoders and augment the model using the state-action learned embedding (SALE). SALE is injected into both the imagination module that forecasts plausible future roll-outs and the joint agent network whose individual action values are combined through a mixing network to estimate the joint action-value function. By coupling imagined trajectories with SALE-based action values, the agents acquire a richer understanding of how their choices influence collective outcomes, leading to improved long-term planning and optimization under limited real-environment interactions. Empirical studies on well-established multi-agent benchmarks, including StarCraft II Micro-Management, Multi-Agent MuJoCo, and Level-Based Foraging challenges, demonstrate consistent gains of our method over baseline algorithms and highlight the effectiveness of joint state-action learned embeddings within a multi-agent model-based paradigm.

</details>


### 9. Bench-MFG: A Benchmark Suite for Learning in Stationary Mean Field Games

- **Authors:** Lorenzo Magnino, Jiacheng Shen, Matthieu Geist, Olivier Pietquin, Mathieu Laurière
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12517v1](http://arxiv.org/abs/2602.12517v1)
- **PDF:** [https://arxiv.org/pdf/2602.12517v1](https://arxiv.org/pdf/2602.12517v1)
- **Categories:** cs.LG, cs.AI, cs.MA, math.OC


> The paper presents Bench-MFG, a benchmark suite designed for evaluating algorithms in stationary Mean Field Games (MFGs) within the Reinforcement Learning context, addressing the current fragmentation in evaluation protocols. The authors introduce a taxonomy of MFG problem classes alongside prototypical environments, and propose MF-Garnets for generating random MFG instances, enabling robust statistical testing of various learning algorithms, including a novel approach for exploitability minimization. Key findings emphasize the need for standardized experimental guidelines to assess the robustness and generalization of emerging methods in agentic AI systems.


<details>
<summary>Abstract</summary>

The intersection of Mean Field Games (MFGs) and Reinforcement Learning (RL) has fostered a growing family of algorithms designed to solve large-scale multi-agent systems. However, the field currently lacks a standardized evaluation protocol, forcing researchers to rely on bespoke, isolated, and often simplistic environments. This fragmentation makes it difficult to assess the robustness, generalization, and failure modes of emerging methods. To address this gap, we propose a comprehensive benchmark suite for MFGs (Bench-MFG), focusing on the discrete-time, discrete-space, stationary setting for the sake of clarity. We introduce a taxonomy of problem classes, ranging from no-interaction and monotone games to potential and dynamics-coupled games, and provide prototypical environments for each. Furthermore, we propose MF-Garnets, a method for generating random MFG instances to facilitate rigorous statistical testing. We benchmark a variety of learning algorithms across these environments, including a novel black-box approach (MF-PSO) for exploitability minimization. Based on our extensive empirical results, we propose guidelines to standardize future experimental comparisons. Code available at \href{https://github.com/lorenzomagnino/Bench-MFG}{https://github.com/lorenzomagnino/Bench-MFG}.

</details>


### 10. Building Large-Scale Drone Defenses from Small-Team Strategies

- **Authors:** Grant Douglas, Stephen Franklin, Claudia Szabo, Mingyu Guo
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12502v1](http://arxiv.org/abs/2602.12502v1)
- **PDF:** [https://arxiv.org/pdf/2602.12502v1](https://arxiv.org/pdf/2602.12502v1)
- **Categories:** cs.MA


> The paper presents a novel framework for scaling small-team defense strategies against large drone swarms by utilizing a dynamic programming (DP) decomposition to assemble these strategies into larger, efficient defensive teams. The methodology involves sampling from small-team candidates and iteratively refining team configurations to optimize outcomes, demonstrating the ability to handle larger scenarios while retaining effectiveness. Key findings indicate that this modular approach not only allows for scalable defense solutions but also uncovers cooperative behaviors that traditional direct optimization methods may overlook, highlighting its significance in the field of agentic AI.


<details>
<summary>Abstract</summary>

Defending against large adversarial drone swarms requires coordination methods that scale effectively beyond conventional multi-agent optimisation. In this paper, we propose to scale strategies proven effective in small defender teams by integrating them as modular components of larger forces using our proposed framework. A dynamic programming (DP) decomposition assembles these components into large teams in polynomial time, enabling efficient construction of scalable defenses without exhaustive evaluation. Because a unit that is strong in isolation may not remain strong when combined, we sample across multiple small-team candidates. Our framework iterates between evaluating large-team outcomes and refining the pool of modular components, allowing convergence on increasingly effective strategies. Experiments demonstrate that this partitioning approach scales to substantially larger scenarios while preserving effectiveness and revealing cooperative behaviours that direct optimisation cannot reliably discover.

</details>


### 11. Favia: Forensic Agent for Vulnerability-fix Identification and Analysis

- **Authors:** André Storhaug, Jiamou Sun, Jingyue Li
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12500v1](http://arxiv.org/abs/2602.12500v1)
- **PDF:** [https://arxiv.org/pdf/2602.12500v1](https://arxiv.org/pdf/2602.12500v1)
- **Categories:** cs.SE, cs.AI, cs.CR


> The paper introduces Favia, an innovative forensic agent framework designed to enhance the identification of vulnerability-fixing commits in large code repositories, addressing the shortcomings of existing methods that struggle with precision-recall trade-offs. Favia employs a dual-stage methodology that first ranks candidate commits efficiently and then utilizes a ReAct-based large language model (LLM) agent to conduct deep semantic reasoning, thus uncovering complex, multi-file fixes often missed by traditional approaches. Evaluations on a newly created dataset, CVEVC, demonstrate that Favia significantly outperforms current state-of-the-art techniques, achieving superior precision, recall, and F1-scores, thereby making substantial contributions to the field of agentic AI in secure software maintenance.


<details>
<summary>Abstract</summary>

Identifying vulnerability-fixing commits corresponding to disclosed CVEs is essential for secure software maintenance but remains challenging at scale, as large repositories contain millions of commits of which only a small fraction address security issues. Existing automated approaches, including traditional machine learning techniques and recent large language model (LLM)-based methods, often suffer from poor precision-recall trade-offs. Frequently evaluated on randomly sampled commits, we uncover that they are substantially underestimating real-world difficulty, where candidate commits are already security-relevant and highly similar. We propose Favia, a forensic, agent-based framework for vulnerability-fix identification that combines scalable candidate ranking with deep and iterative semantic reasoning. Favia first employs an efficient ranking stage to narrow the search space of commits. Each commit is then rigorously evaluated using a ReAct-based LLM agent. By providing the agent with a pre-commit repository as environment, along with specialized tools, the agent tries to localize vulnerable components, navigates the codebase, and establishes causal alignment between code changes and vulnerability root causes. This evidence-driven process enables robust identification of indirect, multi-file, and non-trivial fixes that elude single-pass or similarity-based methods. We evaluate Favia on CVEVC, a large-scale dataset we made that comprises over 8 million commits from 3,708 real-world repositories, and show that it consistently outperforms state-of-the-art traditional and LLM-based baselines under realistic candidate selection, achieving the strongest precision-recall trade-offs and highest F1-scores.

</details>


### 12. Theory of Mind Guided Strategy Adaptation for Zero-Shot Coordination

- **Authors:** Andrew Ni, Simon Stepputtis, Stefanos Nikolaidis, Michael Lewis, Katia P. Sycara, Woojun Kim
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12458v1](http://arxiv.org/abs/2602.12458v1)
- **PDF:** [https://arxiv.org/pdf/2602.12458v1](https://arxiv.org/pdf/2602.12458v1)
- **Categories:** cs.MA


> The paper introduces an adaptive ensemble agent that utilizes Theory of Mind to enhance zero-shot coordination in multi-agent reinforcement learning by inferring teammates' intentions and selecting the most suitable policy from a diverse ensemble. The methodology involves a novel approach that goes beyond the typical static best-response agent by allowing for more flexible and context-aware adaptations to varying partner behaviors. Experimental results in the Overcooked environment show that this adaptive agent significantly outperforms traditional single best-response agents, highlighting its potential for improving synergy and collaboration in agentic AI systems.


<details>
<summary>Abstract</summary>

A central challenge in multi-agent reinforcement learning is enabling agents to adapt to previously unseen teammates in a zero-shot fashion. Prior work in zero-shot coordination often follows a two-stage process, first generating a diverse training pool of partner agents, and then training a best-response agent to collaborate effectively with the entire training pool. While many previous works have achieved strong performance by devising better ways to diversify the partner agent pool, there has been less emphasis on how to leverage this pool to build an adaptive agent. One limitation is that the best-response agent may converge to a static, generalist policy that performs reasonably well across diverse teammates, rather than learning a more adaptive, specialist policy that can better adapt to teammates and achieve higher synergy. To address this, we propose an adaptive ensemble agent that uses Theory-of-Mind-based best-response selection to first infer its teammate's intentions and then select the most suitable policy from a policy ensemble. We conduct experiments in the Overcooked environment to evaluate zero-shot coordination performance under both fully and partially observable settings. The empirical results demonstrate the superiority of our method over a single best-response baseline.

</details>


### 13. Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward

- **Authors:** Renjun Xu, Yang Yan
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12430v1](http://arxiv.org/abs/2602.12430v1)
- **PDF:** [https://arxiv.org/pdf/2602.12430v1](https://arxiv.org/pdf/2602.12430v1)
- **Categories:** cs.MA, cs.AI


> The paper presents a comprehensive survey of agent skills for large language models (LLMs), marking a shift from monolithic architectures to modular, skill-equipped agents that enhance functionality without requiring retraining. It examines the architecture of skills, methods for skill acquisition, scaling deployment, and security issues, highlighting findings such as a notable percentage of community skills containing vulnerabilities and introducing a Skill Trust and Lifecycle Governance Framework for enhancing security in skill integration. The authors identify seven open challenges within the field and propose a research agenda aimed at developing trustworthy and self-improving skill ecosystems, specifically emphasizing the importance of the emerging skill abstraction layer in advancing agentic AI systems.


<details>
<summary>Abstract</summary>

The transition from monolithic language models to modular, skill-equipped agents marks a defining shift in how large language models (LLMs) are deployed in practice. Rather than encoding all procedural knowledge within model weights, agent skills -- composable packages of instructions, code, and resources that agents load on demand -- enable dynamic capability extension without retraining. It is formalized in a paradigm of progressive disclosure, portable skill definitions, and integration with the Model Context Protocol (MCP). This survey provides a comprehensive treatment of the agent skills landscape, as it has rapidly evolved during the last few months. We organize the field along four axes: (i) architectural foundations, examining the SKILL.md specification, progressive context loading, and the complementary roles of skills and MCP; (ii) skill acquisition, covering reinforcement learning with skill libraries (SAGE), autonomous skill discovery (SEAgent), and compositional skill synthesis; (iii) deployment at scale, including the computer-use agent (CUA) stack, GUI grounding advances, and benchmark progress on OSWorld and SWE-bench; and (iv) security, where recent empirical analyses reveal that 26.1\% of community-contributed skills contain vulnerabilities, motivating our proposed Skill Trust and Lifecycle Governance Framework -- a four-tier, gate-based permission model that maps skill provenance to graduated deployment capabilities. We identify seven open challenges -- from cross-platform skill portability to capability-based permission models -- and propose a research agenda for realizing trustworthy, self-improving skill ecosystems. Unlike prior surveys that broadly cover LLM agents or tool use, this work focuses specifically on the emerging skill abstraction layer and its implications for the next generation of agentic systems. Project repo: https://github.com/scienceaix/agentskills.

</details>


### 14. Provably Convergent Actor-Critic in Risk-averse MARL

- **Authors:** Yizhou Zhang, Eric Mazumdar
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12386v1](http://arxiv.org/abs/2602.12386v1)
- **PDF:** [https://arxiv.org/pdf/2602.12386v1](https://arxiv.org/pdf/2602.12386v1)
- **Categories:** cs.MA, cs.GT, cs.LG


> The paper presents a novel two-timescale Actor-Critic algorithm that achieves global convergence in learning stationary policies for infinite-horizon general-sum Markov games (MGs) by applying Risk-averse Quantal response Equilibria (RQE). By leveraging the regularity conditions of RQE, the authors establish finite-sample guarantees for their method, demonstrating its effectiveness in practical applications. Key findings indicate that the proposed algorithm outperforms risk-neutral baselines in terms of convergence properties, contributing to advancements in risk-aware decision-making in multi-agent reinforcement learning systems.


<details>
<summary>Abstract</summary>

Learning stationary policies in infinite-horizon general-sum Markov games (MGs) remains a fundamental open problem in Multi-Agent Reinforcement Learning (MARL). While stationary strategies are preferred for their practicality, computing stationary forms of classic game-theoretic equilibria is computationally intractable -- a stark contrast to the comparative ease of solving single-agent RL or zero-sum games. To bridge this gap, we study Risk-averse Quantal response Equilibria (RQE), a solution concept rooted in behavioral game theory that incorporates risk aversion and bounded rationality. We demonstrate that RQE possesses strong regularity conditions that make it uniquely amenable to learning in MGs. We propose a novel two-timescale Actor-Critic algorithm characterized by a fast-timescale actor and a slow-timescale critic. Leveraging the regularity of RQE, we prove that this approach achieves global convergence with finite-sample guarantees. We empirically validate our algorithm in several environments to demonstrate superior convergence properties compared to risk-neutral baselines.

</details>


### 15. CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use

- **Authors:** Zhen Zhang, Kaiqiang Song, Xun Wang, Yebowen Hu, Weixiang Yan, Chenyang Zhao, Henry Peng Zou, Haoyun Deng, Sathish Reddy Indurthi, Shujian Liu, Simin Ma, Xiaoyang Wang, Xin Eric Wang, Song Wang
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12268v1](http://arxiv.org/abs/2602.12268v1)
- **PDF:** [https://arxiv.org/pdf/2602.12268v1](https://arxiv.org/pdf/2602.12268v1)
- **Categories:** cs.AI


> The paper presents CM2, a novel reinforcement learning framework that utilizes checklist rewards for multi-turn and multi-step agentic tool use, aiming to address challenges in applying RL in environments with unstructured objectives. The methodology involves decomposing each turn's behavior into binary criteria with evidence grounding, using sparse rewards but dense evaluation, and training within a scalable simulated tool environment to avoid heavy engineering costs. Key findings demonstrate that CM2 significantly outperforms traditional supervised fine-tuning methods and existing open-source baselines, indicating its effectiveness in optimizing AI agents for complex tasks without relying on verifiable outcome rewards.


<details>
<summary>Abstract</summary>

AI agents are increasingly used to solve real-world tasks by reasoning over multi-turn user interactions and invoking external tools. However, applying reinforcement learning to such settings remains difficult: realistic objectives often lack verifiable rewards and instead emphasize open-ended behaviors; moreover, RL for multi-turn, multi-step agentic tool use is still underexplored; and building and maintaining executable tool environments is costly, limiting scale and coverage. We propose CM2, an RL framework that replaces verifiable outcome rewards with checklist rewards. CM2 decomposes each turn's intended behavior into fine-grained binary criteria with explicit evidence grounding and structured metadata, turning open-ended judging into more stable classification-style decisions. To balance stability and informativeness, our method adopts a strategy of sparse reward assignment but dense evaluation criteria. Training is performed in a scalable LLM-simulated tool environment, avoiding heavy engineering for large tool sets. Experiments show that CM2 consistently improves over supervised fine-tuning. Starting from an 8B Base model and training on an 8k-example RL dataset, CM2 improves over the SFT counterpart by 8 points on tau^-Bench, by 10 points on BFCL-V4, and by 12 points on ToolSandbox. The results match or even outperform similarly sized open-source baselines, including the judging model. CM2 thus provides a scalable recipe for optimizing multi-turn, multi-step tool-using agents without relying on verifiable rewards. Code provided by the open-source community: https://github.com/namezhenzhang/CM2-RLCR-Tool-Agent.

</details>


### 16. Think like a Scientist: Physics-guided LLM Agent for Equation Discovery

- **Authors:** Jianke Yang, Ohm Venkatachalam, Mohammad Kianezhad, Sharvaree Vadgama, Rose Yu
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12259v1](http://arxiv.org/abs/2602.12259v1)
- **PDF:** [https://arxiv.org/pdf/2602.12259v1](https://arxiv.org/pdf/2602.12259v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces KeplerAgent, a physics-guided framework designed to enhance symbolic equation discovery by emulating the multi-step reasoning process characteristic of scientific inquiry. This agentic system integrates physics-based tools to extract key properties before applying symbolic regression methods, leading to a more structured approach compared to traditional LLM-based methods that rely on direct guessing. Key findings indicate that KeplerAgent significantly outperforms both LLM and conventional approaches in terms of symbolic accuracy and robustness to noise across various physical equation benchmarks.


<details>
<summary>Abstract</summary>

Explaining observed phenomena through symbolic, interpretable formulas is a fundamental goal of science. Recently, large language models (LLMs) have emerged as promising tools for symbolic equation discovery, owing to their broad domain knowledge and strong reasoning capabilities. However, most existing LLM-based systems try to guess equations directly from data, without modeling the multi-step reasoning process that scientists often follow: first inferring physical properties such as symmetries, then using these as priors to restrict the space of candidate equations. We introduce KeplerAgent, an agentic framework that explicitly follows this scientific reasoning process. The agent coordinates physics-based tools to extract intermediate structure and uses these results to configure symbolic regression engines such as PySINDy and PySR, including their function libraries and structural constraints. Across a suite of physical equation benchmarks, KeplerAgent achieves substantially higher symbolic accuracy and greater robustness to noisy data than both LLM and traditional baselines.

</details>


### 17. VIRENA: Virtual Arena for Research, Education, and Democratic Innovation

- **Authors:** Emma Hoes, K. Jonathan Klueser, Fabrizio Gilardi
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12207v1](http://arxiv.org/abs/2602.12207v1)
- **PDF:** [https://arxiv.org/pdf/2602.12207v1](https://arxiv.org/pdf/2602.12207v1)
- **Categories:** cs.HC, cs.AI, cs.SI


> The paper presents VIRENA (Virtual Arena), a novel platform designed for conducting controlled experiments within realistic social media environments, enabling the study of human-AI interactions and content moderation strategies. Utilizing large language model-powered AI agents with configurable personas, VIRENA allows researchers to design and execute complex studies without requiring programming expertise, facilitating exploration of group deliberation and experimentation across various conditions. Key findings indicate that VIRENA's open-source and no-code architecture not only streamlines research across disciplines but also adheres to ethical standards and data protection requirements, thus enhancing the accessibility and reliability of social media research.


<details>
<summary>Abstract</summary>

Digital platforms shape how people communicate, deliberate, and form opinions. Studying these dynamics has become increasingly difficult due to restricted data access, ethical constraints on real-world experiments, and limitations of existing research tools. VIRENA (Virtual Arena) is a platform that enables controlled experimentation in realistic social media environments. Multiple participants interact simultaneously in realistic replicas of feed-based platforms (Instagram, Facebook, Reddit) and messaging apps (WhatsApp, Messenger). Large language model-powered AI agents participate alongside humans with configurable personas and realistic behavior. Researchers can manipulate content moderation approaches, pre-schedule stimulus content, and run experiments across conditions through a visual interface requiring no programming skills. VIRENA makes possible research designs that were previously impractical: studying human--AI interaction in realistic social contexts, experimentally comparing moderation interventions, and observing group deliberation as it unfolds. Built on open-source technologies that ensure data remain under institutional control and comply with data protection requirements, VIRENA is currently in use at the University of Zurich and available for pilot collaborations. Designed for researchers, educators, and public organizations alike, VIRENA's no-code interface makes controlled social media simulation accessible across disciplines and sectors. This paper documents its design, architecture, and capabilities.

</details>


### 18. GT-HarmBench: Benchmarking AI Safety Risks Through the Lens of Game Theory

- **Authors:** Pepijn Cobben, Xuanqiang Angelo Huang, Thao Amelia Pham, Isabel Dahlgren, Terry Jingchen Zhang, Zhijing Jin
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12316v1](http://arxiv.org/abs/2602.12316v1)
- **PDF:** [https://arxiv.org/pdf/2602.12316v1](https://arxiv.org/pdf/2602.12316v1)
- **Categories:** cs.AI, cs.CL, cs.CY, cs.GT, cs.MA


> The paper presents GT-HarmBench, a benchmark designed to evaluate AI safety risks in multi-agent environments, addressing the gap in existing assessments that predominantly focus on single agents. Utilizing 2,009 scenarios inspired by game-theoretic constructs, the authors analyze the decision-making of 15 frontier AI models, revealing that these agents only act in socially beneficial ways 62% of the time, frequently resulting in harmful consequences. The findings demonstrate that framing and ordering in game-theoretic contexts significantly influence agent performance, and that targeted interventions can enhance beneficial outcomes by up to 18%, thereby providing a critical tool for investigating alignment issues in agentic AI systems.


<details>
<summary>Abstract</summary>

Frontier AI systems are increasingly capable and deployed in high-stakes multi-agent environments. However, existing AI safety benchmarks largely evaluate single agents, leaving multi-agent risks such as coordination failure and conflict poorly understood. We introduce GT-HarmBench, a benchmark of 2,009 high-stakes scenarios spanning game-theoretic structures such as the Prisoner's Dilemma, Stag Hunt and Chicken. Scenarios are drawn from realistic AI risk contexts in the MIT AI Risk Repository. Across 15 frontier models, agents choose socially beneficial actions in only 62% of cases, frequently leading to harmful outcomes. We measure sensitivity to game-theoretic prompt framing and ordering, and analyze reasoning patterns driving failures. We further show that game-theoretic interventions improve socially beneficial outcomes by up to 18%. Our results highlight substantial reliability gaps and provide a broad standardized testbed for studying alignment in multi-agent environments. The benchmark and code are available at https://github.com/causalNLP/gt-harmbench.

</details>


### 19. Convex Markov Games and Beyond: New Proof of Existence, Characterization and Learning Algorithms for Nash Equilibria

- **Authors:** Anas Barakat, Ioannis Panageas, Antonios Varvitsiotis
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12181v1](http://arxiv.org/abs/2602.12181v1)
- **PDF:** [https://arxiv.org/pdf/2602.12181v1](https://arxiv.org/pdf/2602.12181v1)
- **Categories:** cs.GT, cs.LG, cs.MA


> The paper presents a comprehensive extension of Convex Markov Games to General Utility Markov Games (GUMGs), addressing the theoretical foundations and learning algorithms for Nash equilibria in multi-agent systems. The authors prove that Nash equilibria in GUMGs correspond to fixed points of projected pseudo-gradient dynamics and establish a simple existence proof using Brouwer's fixed-point theorem, along with the derivation of a policy gradient theorem and a model-free learning algorithm. Key findings include iteration complexity guarantees for computing approximate Nash equilibria and sample complexity bounds, significantly advancing the understanding and applicability of multi-agent learning frameworks beyond zero-sum scenarios.


<details>
<summary>Abstract</summary>

Convex Markov Games (cMGs) were recently introduced as a broad class of multi-agent learning problems that generalize Markov games to settings where strategic agents optimize general utilities beyond additive rewards. While cMGs expand the modeling frontier, their theoretical foundations, particularly the structure of Nash equilibria (NE) and guarantees for learning algorithms, are not yet well understood. In this work, we address these gaps for an extension of cMGs, which we term General Utility Markov Games (GUMGs), capturing new applications requiring coupling between agents' occupancy measures. We prove that in GUMGs, Nash equilibria coincide with the fixed points of projected pseudo-gradient dynamics (i.e., first-order stationary points), enabled by a novel agent-wise gradient domination property. This insight also yields a simple proof of NE existence using Brouwer's fixed-point theorem. We further show the existence of Markov perfect equilibria. Building on this characterization, we establish a policy gradient theorem for GUMGs and design a model-free policy gradient algorithm. For potential GUMGs, we establish iteration complexity guarantees for computing approximate-NE under exact gradients and provide sample complexity bounds in both the generative model and on-policy settings. Our results extend beyond prior work restricted to zero-sum cMGs, providing the first theoretical analysis of common-interest cMGs.

</details>


### 20. On the Adoption of AI Coding Agents in Open-source Android and iOS Development

- **Authors:** Muhammad Ahmad Khan, Hasnain Ali, Muneeb Rana, Muhammad Saqib Ilyas, Abdul Ali Bangash
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12144v1](http://arxiv.org/abs/2602.12144v1)
- **PDF:** [https://arxiv.org/pdf/2602.12144v1](https://arxiv.org/pdf/2602.12144v1)
- **Categories:** cs.SE, cs.AI


> This paper presents a pioneering empirical study examining the role of AI coding agents in open-source mobile app development, focusing on 2,901 AI-generated pull requests (PRs) across Android and iOS platforms. The methodology involved analyzing PR acceptance behaviors, revealing that Android projects received twice as many AI-authored PRs and had a higher acceptance rate compared to iOS, with task categories related to routine functions performing better than structural changes. Key findings indicate notable differences in agent effectiveness and PR resolution times, establishing baseline metrics for evaluating the impact of AI contributions in the context of agentic systems within mobile development.


<details>
<summary>Abstract</summary>

AI coding agents are increasingly contributing to software development, yet their impact on mobile development has received little empirical attention. In this paper, we present the first category-level empirical study of agent-generated code in open-source mobile app projects. We analyzed PR acceptance behaviors across mobile platforms, agents, and task categories using 2,901 AI-authored pull requests (PRs) in 193 verified Android and iOS open-source GitHub repositories in the AIDev dataset. We find that Android projects have received 2x more AI-authored PRs and have achieved higher PR acceptance rate (71%) than iOS (63%), with significant agent-level variation on Android. Across task categories, PRs with routine tasks (feature, fix, and ui) achieve the highest acceptance, while structural changes like refactor and build achieve lower success and longer resolution times. Furthermore, our evolution analysis shows improvement in PR resolution time on Android through mid-2025 before it declined again. Our findings offer the first evidence-based characterization of AI agents effects on OSS mobile projects and establish empirical baselines for evaluating agent-generated contributions to design platform aware agentic systems.

</details>


### 21. Perceptual Self-Reflection in Agentic Physics Simulation Code Generation

- **Authors:** Prashant Shende, Bradley Camburn
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12311v1](http://arxiv.org/abs/2602.12311v1)
- **PDF:** [https://arxiv.org/pdf/2602.12311v1](https://arxiv.org/pdf/2602.12311v1)
- **Categories:** cs.SE, cs.AI


> This paper introduces a multi-agent framework designed to generate physics simulation code from natural language descriptions, featuring an innovative perceptual self-reflection mechanism for validation. The system consists of four specialized agents that handle language interpretation, parameter generation, code creation with self-correction, and perceptual validation through graphical analysis, which addresses the limitations of conventional code testing methods. Key findings indicate that this architecture significantly surpasses traditional single-shot generation methods by improving accuracy in physics simulations across diverse domains and demonstrating effective code self-correction, thereby highlighting the potential applicability of agentic AI in enhancing engineering and physics data generation workflows.


<details>
<summary>Abstract</summary>

We present a multi-agent framework for generating physics simulation code from natural language descriptions, featuring a novel perceptual self-reflection mechanism for validation. The system employs four specialized agents: a natural language interpreter that converts user requests into physics-based descriptions; a technical requirements generator that produces scaled simulation parameters; a physics code generator with automated self-correction; and a physics validator that implements perceptual self-reflection. The key innovation is perceptual validation, which analyzes rendered animation frames using a vision-capable language model rather than inspecting code structure directly. This approach addresses the ``oracle gap'' where syntactically correct code produces physically incorrect behavior--a limitation that conventional testing cannot detect. We evaluate the system across seven domains including classical mechanics, fluid dynamics, thermodynamics, electromagnetics, wave physics, reaction-diffusion systems, and non-physics data visualization. The perceptual self-reflection architecture demonstrates substantial improvement over single-shot generation baselines, with the majority of tested scenarios achieving target physics accuracy thresholds. The system exhibits robust pipeline stability with consistent code self-correction capability, operating at approximately \$0.20 per animation. These results validate our hypothesis that feeding visual simulation outputs back to a vision-language model for iterative refinement significantly outperforms single-shot code generation for physics simulation tasks and highlights the potential of agentic AI to support engineering workflows and physics data generation pipelines.

</details>


### 22. Choose Your Agent: Tradeoffs in Adopting AI Advisors, Coaches, and Delegates in Multi-Party Negotiation

- **Authors:** Kehang Zhu, Nithum Thain, Vivian Tsai, James Wexler, Crystal Qian
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12089v2](http://arxiv.org/abs/2602.12089v2)
- **PDF:** [https://arxiv.org/pdf/2602.12089v2](https://arxiv.org/pdf/2602.12089v2)
- **Categories:** cs.GT, cs.AI, cs.HC


> This paper investigates the impact of different AI assistance modalities—Advisor, Coach, and Delegate—on multi-party negotiation outcomes through an online experiment involving 243 participants. The study reveals that while participants preferred the Advisor modality, they actually achieved the highest individual gains when using the Delegate, highlighting a preference-performance misalignment; the Delegate was found to enhance negotiation outcomes not only for users but also produced positive effects for non-users. The findings suggest that despite the advanced capabilities of autonomous agents, their effectiveness in improving group welfare can be limited by user perceptions and interface design, indicating the need for strategic development of AI systems that facilitate user adoption and engagement.


<details>
<summary>Abstract</summary>

As AI usage becomes more prevalent in social contexts, understanding agent-user interaction is critical to designing systems that improve both individual and group outcomes. We present an online behavioral experiment (N = 243) in which participants play three multi-turn bargaining games in groups of three. Each game, presented in randomized order, grants access to a single LLM assistance modality: proactive recommendations from an Advisor, reactive feedback from a Coach, or autonomous execution by a Delegate; all modalities are powered by an underlying LLM that achieves superhuman performance in an all-agent environment. On each turn, participants privately decide whether to act manually or use the AI modality available in that game. Despite preferring the Advisor modality, participants achieve the highest mean individual gains with the Delegate, demonstrating a preference-performance misalignment. Moreover, delegation generates positive externalities; even non-adopting users in access-to-delegate treatment groups benefit by receiving higher-quality offers. Mechanism analysis reveals that the Delegate agent acts as a market maker, injecting rational, Pareto-improving proposals that restructure the trading environment. Our research reveals a gap between agent capabilities and realized group welfare. While autonomous agents can exhibit super-human strategic performance, their impact on realized welfare gains can be constrained by interfaces, user perceptions, and adoption barriers. Assistance modalities should be designed as mechanisms with endogenous participation; adoption-compatible interaction rules are a prerequisite to improving human welfare with automated assistance.

</details>


### 23. Differentiable Modal Logic for Multi-Agent Diagnosis, Orchestration and Communication

- **Authors:** Antonin Sulc
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12083v1](http://arxiv.org/abs/2602.12083v1)
- **PDF:** [https://arxiv.org/pdf/2602.12083v1](https://arxiv.org/pdf/2602.12083v1)
- **Categories:** cs.AI, cs.LO


> The paper presents a novel approach called Differentiable Modal Logic (DML), implemented through Modal Logical Neural Networks (MLNNs), to enhance multi-agent systems' ability to diagnose and orchestrate actions in dynamic environments without relying on manually specified relationship structures. By leveraging a unified neurosymbolic debugging framework, the authors demonstrate how DML can help systems learn essential modalities—epistemic, temporal, deontic, and doxastic—through behavioral data, effectively rendering logical inconsistencies as learnable optimization targets. Key findings include the development of interpretable structures for trust and causality, the integration of knowledge through differentiable axioms, and practical implementations for enhancing real-time monitoring and control in multi-agent contexts.


<details>
<summary>Abstract</summary>

As multi-agent AI systems evolve from simple chatbots to autonomous swarms, debugging semantic failures requires reasoning about knowledge, belief, causality, and obligation, precisely what modal logic was designed to formalize. However, traditional modal logic requires manual specification of relationship structures that are unknown or dynamic in real systems. This tutorial demonstrates differentiable modal logic (DML), implemented via Modal Logical Neural Networks (MLNNs), enabling systems to learn trust networks, causal chains, and regulatory boundaries from behavioral data alone.
  We present a unified neurosymbolic debugging framework through four modalities: epistemic (who to trust), temporal (when events cause failures), deontic (what actions are permitted), and doxastic (how to interpret agent confidence). Each modality is demonstrated on concrete multi-agent scenarios, from discovering deceptive alliances in diplomacy games to detecting LLM hallucinations, with complete implementations showing how logical contradictions become learnable optimization objectives. Key contributions for the neurosymbolic community: (1) interpretable learned structures where trust and causality are explicit parameters, not opaque embeddings; (2) knowledge injection via differentiable axioms that guide learning with sparse data (3) compositional multi-modal reasoning that combines epistemic, temporal, and deontic constraints; and (4) practical deployment patterns for monitoring, active control and communication of multi-agent systems. All code provided as executable Jupyter notebooks.

</details>


### 24. Multi UAVs Preflight Planning in a Shared and Dynamic Airspace

- **Authors:** Amath Sow, Mauricio Rodriguez Cesen, Fabiola Martins Campos de Oliveira, Mariusz Wzorek, Daniel de Leng, Mattias Tiger, Fredrik Heintz, Christian Esteve Rothenberg
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12055v1](http://arxiv.org/abs/2602.12055v1)
- **PDF:** [https://arxiv.org/pdf/2602.12055v1](https://arxiv.org/pdf/2602.12055v1)
- **Categories:** cs.AI, cs.MA, cs.RO


> The paper presents DTAPP-IICR, a novel method for preflight planning of large-scale UAV fleets in dynamic airspace, addressing challenges like temporal No-Fly Zones and heterogeneous vehicle profiles. The methodology combines a prioritized mission approach with a new 4D planner (SFIPP-ST) for trajectory generation, and employs an iterative Large Neighborhood Search for conflict resolution, enhanced by a directional pruning technique. Key findings indicate that DTAPP-IICR achieves near-100% success rates for fleets up to 1,000 UAVs and offers significant runtime reductions compared to existing methods, demonstrating its scalability and practicality for urban Unmanned Traffic Management.


<details>
<summary>Abstract</summary>

Preflight planning for large-scale Unmanned Aerial Vehicle (UAV) fleets in dynamic, shared airspace presents significant challenges, including temporal No-Fly Zones (NFZs), heterogeneous vehicle profiles, and strict delivery deadlines. While Multi-Agent Path Finding (MAPF) provides a formal framework, existing methods often lack the scalability and flexibility required for real-world Unmanned Traffic Management (UTM). We propose DTAPP-IICR: a Delivery-Time Aware Prioritized Planning method with Incremental and Iterative Conflict Resolution. Our framework first generates an initial solution by prioritizing missions based on urgency. Secondly, it computes roundtrip trajectories using SFIPP-ST, a novel 4D single-agent planner (Safe Flight Interval Path Planning with Soft and Temporal Constraints). SFIPP-ST handles heterogeneous UAVs, strictly enforces temporal NFZs, and models inter-agent conflicts as soft constraints. Subsequently, an iterative Large Neighborhood Search, guided by a geometric conflict graph, efficiently resolves any residual conflicts. A completeness-preserving directional pruning technique further accelerates the 3D search. On benchmarks with temporal NFZs, DTAPP-IICR achieves near-100% success with fleets of up to 1,000 UAVs and gains up to 50% runtime reduction from pruning, outperforming batch Enhanced Conflict-Based Search in the UTM context. Scaling successfully in realistic city-scale operations where other priority-based methods fail even at moderate deployments, DTAPP-IICR is positioned as a practical and scalable solution for preflight planning in dense, dynamic urban airspace.

</details>


### 25. PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving

- **Authors:** Sunghyeon Woo, Hoseung Kim, Sunghwan Shim, Minjung Jo, Hyunjoon Jeong, Jeongtae Lee, Joonghoon Kim, Sungjae Lee, Baeseong Park, Se Jung Kwon, Dongsoo Lee
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12029v1](http://arxiv.org/abs/2602.12029v1)
- **PDF:** [https://arxiv.org/pdf/2602.12029v1](https://arxiv.org/pdf/2602.12029v1)
- **Categories:** cs.LG, cs.DC


> The paper presents PrefillShare, a novel algorithm that enhances the efficiency of multi-agent systems using multiple specialized language models by enabling shared prefill stages and key-value (KV) caches across models in a disaggregated serving setup. The methodology involves factorizing models into prefill and decode modules, stabilizing the prefill module while fine-tuning only the decode module, alongside implementing a routing mechanism for heterogeneous models. Key findings reveal that PrefillShare achieves comparable accuracy to full fine-tuning while significantly improving performance metrics, yielding 4.5x lower tail latency and 3.9x higher throughput in multi-model agent workloads, thereby addressing redundancy issues in language model execution.


<details>
<summary>Abstract</summary>

Multi-agent systems increasingly orchestrate multiple specialized language models to solve complex real-world problems, often invoking them over a shared context. This execution pattern repeatedly processes the same prompt prefix across models. Consequently, each model redundantly executes the prefill stage and maintains its own key-value (KV) cache, increasing aggregate prefill load and worsening tail latency by intensifying prefill-decode interference in existing LLM serving stacks. Disaggregated serving reduces such interference by placing prefill and decode on separate GPUs, but disaggregation does not fundamentally eliminate inter-model redundancy in computation and KV storage for the same prompt. To address this issue, we propose PrefillShare, a novel algorithm that enables sharing the prefill stage across multiple models in a disaggregated setting. PrefillShare factorizes the model into prefill and decode modules, freezes the prefill module, and fine-tunes only the decode module. This design allows multiple task-specific models to share a prefill module and the KV cache generated for the same prompt. We further introduce a routing mechanism that enables effective prefill sharing across heterogeneous models in a vLLM-based disaggregated system. PrefillShare not only matches full fine-tuning accuracy on a broad range of tasks and models, but also delivers 4.5x lower p95 latency and 3.9x higher throughput in multi-model agent workloads.

</details>


### 26. Multi-Defender Single-Attacker Perimeter Defense Game on a Cylinder: Special Case in which the Attacker Starts at the Boundary

- **Authors:** Michael Otte, Roderich Groß
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11977v1](http://arxiv.org/abs/2602.11977v1)
- **PDF:** [https://arxiv.org/pdf/2602.11977v1](https://arxiv.org/pdf/2602.11977v1)
- **Categories:** cs.MA


> The paper presents a multi-agent perimeter defense game on a cylindrical environment, focusing on a scenario where multiple slow-moving defenders aim to prevent a single fast-moving attacker from breaching their defensive perimeter. The methodology involves analyzing the strategic interactions and conditions that determine the attacker's success when initiating from a defended boundary region. Key findings reveal specific conditions under which the attacker can successfully navigate the defense, contributing valuable insights into agentic AI strategies for dynamic and spatially constrained adversarial scenarios.


<details>
<summary>Abstract</summary>

We describe a multi-agent perimeter defense game played on a cylinder. A team of n slow-moving defenders must prevent a single fast-moving attacker from crossing the boundary of a defensive perimeter. We describe the conditions necessary for the attacker to win in the special case that the intruder starts close to the boundary and in a region that is currently defended.

</details>


### 27. Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments

- **Authors:** Romain Froger, Pierre Andrews, Matteo Bettini, Amar Budhiraja, Ricardo Silveira Cabral, Virginie Do, Emilien Garreau, Jean-Baptiste Gaya, Hugo Laurençon, Maxime Lecanu, Kunal Malkan, Dheeraj Mekala, Pierre Ménard, Gerard Moreno-Torres Bertran, Ulyana Piterbarg, Mikhail Plekhanov, Mathieu Rita, Andrey Rusakov, Vladislav Vorotilov, Mengjue Wang, Ian Yu, Amine Benhalloum, Grégoire Mialon, Thomas Scialom
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11964v1](http://arxiv.org/abs/2602.11964v1)
- **PDF:** [https://arxiv.org/pdf/2602.11964v1](https://arxiv.org/pdf/2602.11964v1)
- **Categories:** cs.AI


> The paper presents Gaia2, a benchmark specifically designed for assessing large language model (LLM) agents in dynamic and asynchronous environments, which contrasts with prior methodologies that focused on static or synchronous contexts. It employs scenarios where environments independently evolve, prompting agents to adapt to temporal constraints and collaborate, evaluated using a write-action verifier for nuanced performance metrics. Benchmarks reveal that no single model excels across all capabilities: while GPT-5 achieves the highest overall score, it struggles with time-sensitive tasks, and results emphasize the need to balance reasoning, efficiency, and robustness, addressing the challenges of practical agent systems and closing the "sim2real" gap.


<details>
<summary>Abstract</summary>

We introduce Gaia2, a benchmark for evaluating large language model agents in realistic, asynchronous environments. Unlike prior static or synchronous evaluations, Gaia2 introduces scenarios where environments evolve independently of agent actions, requiring agents to operate under temporal constraints, adapt to noisy and dynamic events, resolve ambiguity, and collaborate with other agents. Each scenario is paired with a write-action verifier, enabling fine-grained, action-level evaluation and making Gaia2 directly usable for reinforcement learning from verifiable rewards. Our evaluation of state-of-the-art proprietary and open-source models shows that no model dominates across capabilities: GPT-5 (high) reaches the strongest overall score of 42% pass@1 but fails on time-sensitive tasks, Claude-4 Sonnet trades accuracy and speed for cost, Kimi-K2 leads among open-source models with 21% pass@1. These results highlight fundamental trade-offs between reasoning, efficiency, robustness, and expose challenges in closing the "sim2real" gap. Gaia2 is built on a consumer environment with the open-source Agents Research Environments platform and designed to be easy to extend. By releasing Gaia2 alongside the foundational ARE framework, we aim to provide the community with a flexible infrastructure for developing, benchmarking, and training the next generation of practical agent systems.

</details>


### 28. AdaptEvolve: Improving Efficiency of Evolutionary AI Agents through Adaptive Model Selection

- **Authors:** Pretam Ray, Pratik Prabhanjan Brahma, Zicheng Liu, Emad Barsoum
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11931v1](http://arxiv.org/abs/2602.11931v1)
- **PDF:** [https://arxiv.org/pdf/2602.11931v1](https://arxiv.org/pdf/2602.11931v1)
- **Categories:** cs.CL, cs.AI


> The paper presents AdaptEvolve, a framework that enhances the efficiency of evolutionary AI agents by implementing adaptive model selection based on intrinsic generation confidence. The methodology focuses on dynamically selecting the most suitable large language model (LLM) for each generation step, thereby overcoming limitations of static heuristics in existing routing strategies. Key findings indicate that this confidence-driven selection approach significantly reduces inference costs by an average of 37.9% while maintaining 97.5% of the accuracy of traditional static models, highlighting its potential for optimizing computational resources in agentic AI applications.


<details>
<summary>Abstract</summary>

Evolutionary agentic systems intensify the trade-off between computational efficiency and reasoning capability by repeatedly invoking large language models (LLMs) during inference. This setting raises a central question: how can an agent dynamically select an LLM that is sufficiently capable for the current generation step while remaining computationally efficient? While model cascades offer a practical mechanism for balancing this trade-off, existing routing strategies typically rely on static heuristics or external controllers and do not explicitly account for model uncertainty. We introduce AdaptEvolve: Adaptive LLM Selection for Multi-LLM Evolutionary Refinement within an evolutionary sequential refinement framework that leverages intrinsic generation confidence to estimate real-time solvability. Empirical results show that confidence-driven selection yields a favourable Pareto frontier, reducing total inference cost by an average of 37.9% across benchmarks while retaining 97.5% of the upper-bound accuracy of static large-model baselines. Our code is available at https://github.com/raypretam/adaptive_llm_selection.

</details>


### 29. MEME: Modeling the Evolutionary Modes of Financial Markets

- **Authors:** Taian Guo, Haiyang Shen, Junyu Luo, Zhongshi Xing, Hanchun Lian, Jinsheng Huang, Binqi Chen, Luchen Liu, Yun Ma, Ming Zhang
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11918v1](http://arxiv.org/abs/2602.11918v1)
- **PDF:** [https://arxiv.org/pdf/2602.11918v1](https://arxiv.org/pdf/2602.11918v1)
- **Categories:** cs.AI


> The paper introduces MEME (Modeling the Evolutionary Modes of Financial Markets), a novel framework that models financial markets as dynamic ecosystems of competing investment narratives, emphasizing a Logic-Oriented perspective that aims to enhance reasoning behind market movements. The methodology involves a multi-agent extraction module to convert noisy data into Investment Arguments and employs Gaussian Mixture Modeling to identify latent consensus, while also tracking semantic drift through a temporal evaluation mechanism. Key findings indicate that MEME outperforms seven state-of-the-art baselines in predicting market dynamics across different Chinese stock pools, underscoring its effectiveness in leveraging robust reasoning for portfolio construction amidst changing market conditions.


<details>
<summary>Abstract</summary>

LLMs have demonstrated significant potential in quantitative finance by processing vast unstructured data to emulate human-like analytical workflows. However, current LLM-based methods primarily follow either an Asset-Centric paradigm focused on individual stock prediction or a Market-Centric approach for portfolio allocation, often remaining agnostic to the underlying reasoning that drives market movements. In this paper, we propose a Logic-Oriented perspective, modeling the financial market as a dynamic, evolutionary ecosystem of competing investment narratives, termed Modes of Thought. To operationalize this view, we introduce MEME (Modeling the Evolutionary Modes of Financial Markets), designed to reconstruct market dynamics through the lens of evolving logics. MEME employs a multi-agent extraction module to transform noisy data into high-fidelity Investment Arguments and utilizes Gaussian Mixture Modeling to uncover latent consensus within a semantic space. To model semantic drift among different market conditions, we also implement a temporal evaluation and alignment mechanism to track the lifecycle and historical profitability of these modes. By prioritizing enduring market wisdom over transient anomalies, MEME ensures that portfolio construction is guided by robust reasoning. Extensive experiments on three heterogeneous Chinese stock pools from 2023 to 2025 demonstrate that MEME consistently outperforms seven SOTA baselines. Further ablation studies, sensitivity analysis, lifecycle case study and cost analysis validate MEME's capacity to identify and adapt to the evolving consensus of financial markets. Our implementation can be found at https://github.com/gta0804/MEME.

</details>


### 30. Agentic AI for Cybersecurity: A Meta-Cognitive Architecture for Governable Autonomy

- **Authors:** Andrei Kojukhov, Arkady Bovshover
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11897v1](http://arxiv.org/abs/2602.11897v1)
- **PDF:** [https://arxiv.org/pdf/2602.11897v1](https://arxiv.org/pdf/2602.11897v1)
- **Categories:** cs.CR, cs.AI


> The paper proposes a novel architectural framework for cybersecurity that redefines the approach to AI-driven systems as agentic, multi-agent cognitive systems rather than traditional model-centric detection pipelines. By implementing a meta-cognitive judgement function that governs decision-making readiness and system autonomy in the face of adversarial uncertainty, the authors integrate principles from distributed cognition, multi-agent systems, and responsible AI governance. Key findings indicate that this approach enhances accountable decision-making processes and aligns cybersecurity practices with organizational and regulatory requirements, paving the way for more robust and governable AI-enabled cyber defense mechanisms.


<details>
<summary>Abstract</summary>

Contemporary AI-driven cybersecurity systems are predominantly architected as model-centric detection and automation pipelines optimized for task-level performance metrics such as accuracy and response latency. While effective for bounded classification tasks, these architectures struggle to support accountable decision-making under adversarial uncertainty, where actions must be justified, governed, and aligned with organizational and regulatory constraints. This paper argues that cybersecurity orchestration should be reconceptualized as an agentic, multi-agent cognitive system, rather than a linear sequence of detection and response components. We introduce a conceptual architectural framework in which heterogeneous AI agents responsible for detection, hypothesis formation, contextual interpretation, explanation, and governance are coordinated through an explicit meta-cognitive judgement function. This function governs decision readiness and dynamically calibrates system autonomy when evidence is incomplete, conflicting, or operationally risky. By synthesizing distributed cognition theory, multi-agent systems research, and responsible AI governance frameworks, we demonstrate that modern security operations already function as distributed cognitive systems, albeit without an explicit organizing principle. Our contribution is to make this cognitive structure architecturally explicit and governable by embedding meta-cognitive judgement as a first-class system function. We discuss implications for security operations centers, accountable autonomy, and the design of next-generation AI-enabled cyber defence architectures. The proposed framework shifts the focus of AI in cybersecurity from optimizing isolated predictions to governing autonomy under uncertainty.

</details>


### 31. Intelligent AI Delegation

- **Authors:** Nenad Tomašev, Matija Franklin, Simon Osindero
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11865v1](http://arxiv.org/abs/2602.11865v1)
- **PDF:** [https://arxiv.org/pdf/2602.11865v1](https://arxiv.org/pdf/2602.11865v1)
- **Categories:** cs.AI


> The paper presents a novel adaptive framework for intelligent AI delegation that enhances the task allocation process among AI agents and humans by incorporating aspects like authority transfer, accountability, and trust-building mechanisms. The methodology focuses on meaningful problem decomposition and dynamic adaptation to environmental changes to address the limitations of existing heuristics. Key findings suggest that this framework facilitates more effective collaboration in complex delegation networks, thereby contributing to the field of agentic AI by promoting robust and adaptable interaction protocols among agents.


<details>
<summary>Abstract</summary>

AI agents are able to tackle increasingly complex tasks. To achieve more ambitious goals, AI agents need to be able to meaningfully decompose problems into manageable sub-components, and safely delegate their completion across to other AI agents and humans alike. Yet, existing task decomposition and delegation methods rely on simple heuristics, and are not able to dynamically adapt to environmental changes and robustly handle unexpected failures. Here we propose an adaptive framework for intelligent AI delegation - a sequence of decisions involving task allocation, that also incorporates transfer of authority, responsibility, accountability, clear specifications regarding roles and boundaries, clarity of intent, and mechanisms for establishing trust between the two (or more) parties. The proposed framework is applicable to both human and AI delegators and delegatees in complex delegation networks, aiming to inform the development of protocols in the emerging agentic web.

</details>


### 32. Towards Sustainable Investment Policies Informed by Opponent Shaping

- **Authors:** Juan Agustin Duque, Razvan Ciuca, Ayoub Echchahed, Hugo Larochelle, Aaron Courville
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11829v1](http://arxiv.org/abs/2602.11829v1)
- **PDF:** [https://arxiv.org/pdf/2602.11829v1](https://arxiv.org/pdf/2602.11829v1)
- **Categories:** cs.LG, cs.GT


> This paper presents the InvestESG multi-agent simulation, which models the interactions between investors and companies in the context of climate risk, revealing conditions for an intertemporal social dilemma where individual incentives conflict with collective welfare. The authors employ Advantage Alignment, an opponent shaping algorithm, to modify agent learning dynamics, leading to a preference for socially beneficial equilibria. Key findings suggest that strategically guiding agent behavior can enhance cooperative outcomes, offering insights for developing investment policies that align market incentives with sustainable goals.


<details>
<summary>Abstract</summary>

Addressing climate change requires global coordination, yet rational economic actors often prioritize immediate gains over collective welfare, resulting in social dilemmas. InvestESG is a recently proposed multi-agent simulation that captures the dynamic interplay between investors and companies under climate risk. We provide a formal characterization of the conditions under which InvestESG exhibits an intertemporal social dilemma, deriving theoretical thresholds at which individual incentives diverge from collective welfare. Building on this, we apply Advantage Alignment, a scalable opponent shaping algorithm shown to be effective in general-sum games, to influence agent learning in InvestESG. We offer theoretical insights into why Advantage Alignment systematically favors socially beneficial equilibria by biasing learning dynamics toward cooperative outcomes. Our results demonstrate that strategically shaping the learning processes of economic agents can result in better outcomes that could inform policy mechanisms to better align market incentives with long-term sustainability goals.

</details>


### 33. Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation

- **Authors:** Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11790v1](http://arxiv.org/abs/2602.11790v1)
- **PDF:** [https://arxiv.org/pdf/2602.11790v1](https://arxiv.org/pdf/2602.11790v1)
- **Categories:** cs.AI, cs.CL


> The paper presents LAVES, a hierarchical LLM-based multi-agent system designed to generate high-quality instructional videos, addressing the limitations of traditional end-to-end video generation models that struggle with logical rigor and knowledge representation. The methodology involves decomposing the video generation process into specialized agents, including an Orchestrating Agent and dedicated Solution, Illustration, and Narration Agents, all governed by quality gates and iterative critiques. Key findings indicate that LAVES can produce over one million videos per day with a cost reduction exceeding 95% compared to standard industry practices, while achieving high procedural fidelity and pedagogical coherence, thus significantly advancing the capabilities of agentic AI in educational video production.


<details>
<summary>Abstract</summary>

Although recent end-to-end video generation models demonstrate impressive performance in visually oriented content creation, they remain limited in scenarios that require strict logical rigor and precise knowledge representation, such as instructional and educational media. To address this problem, we propose LAVES, a hierarchical LLM-based multi-agent system for generating high-quality instructional videos from educational problems. The LAVES formulates educational video generation as a multi-objective task that simultaneously demands correct step-by-step reasoning, pedagogically coherent narration, semantically faithful visual demonstrations, and precise audio--visual alignment. To address the limitations of prior approaches--including low procedural fidelity, high production cost, and limited controllability--LAVES decomposes the generation workflow into specialized agents coordinated by a central Orchestrating Agent with explicit quality gates and iterative critique mechanisms. Specifically, the Orchestrating Agent supervises a Solution Agent for rigorous problem solving, an Illustration Agent that produces executable visualization codes, and a Narration Agent for learner-oriented instructional scripts. In addition, all outputs from the working agents are subject to semantic critique, rule-based constraints, and tool-based compilation checks. Rather than directly synthesizing pixels, the system constructs a structured executable video script that is deterministically compiled into synchronized visuals and narration using template-driven assembly rules, enabling fully automated end-to-end production without manual editing. In large-scale deployments, LAVES achieves a throughput exceeding one million videos per day, delivering over a 95% reduction in cost compared to current industry-standard approaches while maintaining a high acceptance rate.

</details>


### 34. TSR: Trajectory-Search Rollouts for Multi-Turn RL of LLM Agents

- **Authors:** Aladin Djuhera, Swanand Ravindra Kadhe, Farhan Ahmed, Holger Boche
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11767v1](http://arxiv.org/abs/2602.11767v1)
- **PDF:** [https://arxiv.org/pdf/2602.11767v1](https://arxiv.org/pdf/2602.11767v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> The paper presents TSR (Trajectory-Search Rollouts), a novel approach designed to enhance multi-turn reinforcement learning for large language model (LLM) agents by improving the quality of rollout generation. TSR employs a lightweight tree-style search mechanism to optimize action selection at each turn based on task-specific feedback, which addresses challenges related to sparse rewards and stochastic environments. The implementation of TSR, combined with various search methods and reinforcement learning algorithms, demonstrated up to a 15% performance improvement and increased learning stability in diverse tasks, indicating its potential as a robust enhancement to existing agent training frameworks.


<details>
<summary>Abstract</summary>

Advances in large language models (LLMs) are driving a shift toward using reinforcement learning (RL) to train agents from iterative, multi-turn interactions across tasks. However, multi-turn RL remains challenging as rewards are often sparse or delayed, and environments can be stochastic. In this regime, naive trajectory sampling can hinder exploitation and induce mode collapse. We propose TSR (Trajectory-Search Rollouts), a training-time approach that repurposes test-time scaling ideas for improved per-turn rollout generation. TSR performs lightweight tree-style search to construct high-quality trajectories by selecting high-scoring actions at each turn using task-specific feedback. This improves rollout quality and stabilizes learning while leaving the underlying optimization objective unchanged, making TSR optimizer-agnostic. We instantiate TSR with best-of-N, beam, and shallow lookahead search, and pair it with PPO and GRPO, achieving up to 15% performance gains and more stable learning on Sokoban, FrozenLake, and WebShop tasks at a one-time increase in training compute. By moving search from inference time to the rollout stage of training, TSR provides a simple and general mechanism for stronger multi-turn agent learning, complementary to existing frameworks and rejection-sampling-style selection methods.

</details>


### 35. Cooperation Breakdown in LLM Agents Under Communication Delays

- **Authors:** Keita Nishimoto, Kimitaka Asatani, Ichiro Sakata
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11754v1](http://arxiv.org/abs/2602.11754v1)
- **PDF:** [https://arxiv.org/pdf/2602.11754v1](https://arxiv.org/pdf/2602.11754v1)
- **Categories:** cs.MA, cs.AI, cs.GT


> The paper presents the FLCOA framework, which conceptualizes cooperation and coordination in LLM-based multi-agent systems (LLM-MAS) while emphasizing the often-overlooked impact of lower-layer factors like computational and communication resources. Through simulations using a Continuous Prisoner's Dilemma with Communication Delay, the authors find that increased communication delay can lead to exploitation among agents but also reveals a U-shaped relationship where excessive delay can reduce instances of such exploitation, thereby enhancing mutual cooperation. This highlights the importance of considering communication constraints in the design of autonomous agent systems for effective collaborative behavior.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems (LLM-MAS), in which autonomous AI agents cooperate to solve tasks, are gaining increasing attention. For such systems to be deployed in society, agents must be able to establish cooperation and coordination under real-world computational and communication constraints. We propose the FLCOA framework (Five Layers for Cooperation/Coordination among Autonomous Agents) to conceptualize how cooperation and coordination emerge in groups of autonomous agents, and highlight that the influence of lower-layer factors - especially computational and communication resources - has been largely overlooked. To examine the effect of communication delay, we introduce a Continuous Prisoner's Dilemma with Communication Delay and conduct simulations with LLM-based agents. As delay increases, agents begin to exploit slower responses even without explicit instructions. Interestingly, excessive delay reduces cycles of exploitation, yielding a U-shaped relationship between delay magnitude and mutual cooperation. These results suggest that fostering cooperation requires attention not only to high-level institutional design but also to lower-layer factors such as communication delay and resource allocation, pointing to new directions for MAS research.

</details>


### 36. AmbiBench: Benchmarking Mobile GUI Agents Beyond One-Shot Instructions in the Wild

- **Authors:** Jiazheng Sun, Mingxuan Li, Yingying Zhang, Jiayang Niu, Yachen Wu, Ruihan Jin, Shuyu Lei, Pengrongrui Tan, Zongyu Zhang, Ruoyi Wang, Jiachen Yang, Boyu Yang, Jiacheng Liu, Xin Peng
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11750v1](http://arxiv.org/abs/2602.11750v1)
- **PDF:** [https://arxiv.org/pdf/2602.11750v1](https://arxiv.org/pdf/2602.11750v1)
- **Categories:** cs.SE, cs.AI, cs.HC


> The paper introduces AmbiBench, a novel benchmark designed to evaluate Mobile GUI Agents in scenarios involving ambiguous user instructions, emphasizing bidirectional intent alignment rather than one-shot instruction following. The authors develop a taxonomy of instruction clarity and a comprehensive dataset featuring 240 tasks across 25 applications, alongside an automated evaluation framework called MUSE that assesses agent performance across key dimensions. Key findings demonstrate the limitations of state-of-the-art agents when dealing with varying clarity levels and highlight the benefits of proactive user-agent interactions, thus fostering advancements in agentic AI that better understand user intent in real-world applications.


<details>
<summary>Abstract</summary>

Benchmarks are paramount for gauging progress in the domain of Mobile GUI Agents. In practical scenarios, users frequently fail to articulate precise directives containing full task details at the onset, and their expressions are typically ambiguous. Consequently, agents are required to converge on the user's true intent via active clarification and interaction during execution. However, existing benchmarks predominantly operate under the idealized assumption that user-issued instructions are complete and unequivocal. This paradigm focuses exclusively on assessing single-turn execution while overlooking the alignment capability of the agent. To address this limitation, we introduce AmbiBench, the first benchmark incorporating a taxonomy of instruction clarity to shift evaluation from unidirectional instruction following to bidirectional intent alignment. Grounded in Cognitive Gap theory, we propose a taxonomy of four clarity levels: Detailed, Standard, Incomplete, and Ambiguous. We construct a rigorous dataset of 240 ecologically valid tasks across 25 applications, subject to strict review protocols. Furthermore, targeting evaluation in dynamic environments, we develop MUSE (Mobile User Satisfaction Evaluator), an automated framework utilizing an MLLM-as-a-judge multi-agent architecture. MUSE performs fine-grained auditing across three dimensions: Outcome Effectiveness, Execution Quality, and Interaction Quality. Empirical results on AmbiBench reveal the performance boundaries of SoTA agents across different clarity levels, quantify the gains derived from active interaction, and validate the strong correlation between MUSE and human judgment. This work redefines evaluation standards, laying the foundation for next-generation agents capable of truly understanding user intent.

</details>


### 37. AIR: Improving Agent Safety through Incident Response

- **Authors:** Zibo Xiao, Jun Sun, Junjie Chen
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11749v1](http://arxiv.org/abs/2602.11749v1)
- **PDF:** [https://arxiv.org/pdf/2602.11749v1](https://arxiv.org/pdf/2602.11749v1)
- **Categories:** cs.AI


> The paper introduces AIR, the first incident response framework specifically designed for Large Language Model (LLM) agent systems, addressing the limitations of existing safety mechanisms that primarily focus on preventing failures. AIR employs a domain-specific language to autonomously manage the incident response lifecycle, enabling LLM agents to detect incidents, execute containment and recovery actions, and synthesize guardrail rules for future prevention. Evaluation results indicate that AIR achieves over 90% success rates in detection, remediation, and eradication, highlighting the effectiveness and necessity of integrating incident response as a key component for enhancing agent safety in autonomous applications.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents are increasingly deployed in practice across a wide range of autonomous applications. Yet current safety mechanisms for LLM agents focus almost exclusively on preventing failures in advance, providing limited capabilities for responding to, containing, or recovering from incidents after they inevitably arise. In this work, we introduce AIR, the first incident response framework for LLM agent systems. AIR defines a domain-specific language for managing the incident response lifecycle autonomously in LLM agent systems, and integrates it into the agent's execution loop to (1) detect incidents via semantic checks grounded in the current environment state and recent context, (2) guide the agent to execute containment and recovery actions via its tools, and (3) synthesize guardrail rules during eradication to block similar incidents in future executions. We evaluate AIR on three representative agent types. Results show that AIR achieves detection, remediation, and eradication success rates all exceeding 90%. Extensive experiments further confirm the necessity of AIR's key design components, show the timeliness and moderate overhead of AIR, and demonstrate that LLM-generated rules can approach the effectiveness of developer-authored rules across domains. These results show that incident response is both feasible and essential as a first-class mechanism for improving agent safety.

</details>


### 38. PhyNiKCE: A Neurosymbolic Agentic Framework for Autonomous Computational Fluid Dynamics

- **Authors:** E Fan, Lisong Shi, Zhengtong Li, Chih-yung Wen
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11666v1](http://arxiv.org/abs/2602.11666v1)
- **PDF:** [https://arxiv.org/pdf/2602.11666v1](https://arxiv.org/pdf/2602.11666v1)
- **Categories:** cs.AI, cs.CL


> The paper presents PhyNiKCE, a neurosymbolic framework designed to enhance autonomous agents' capabilities in Computational Fluid Dynamics (CFD) by addressing the limitations of Large Language Models (LLMs) in upholding physical constraints. By decoupling neural planning from symbolic validation, PhyNiKCE approaches simulation setup as a Constraint Satisfaction Problem, using a Symbolic Knowledge Engine and Deterministic RAG Engine to enforce strict physical laws, which led to a 96% relative improvement in task performance over existing methods. Additionally, the framework decreased the need for excessive self-correction loops by 59% and reduced LLM token usage by 17%, underscoring its potential as a scalable and robust solution for trustworthy AI in broader industrial applications.


<details>
<summary>Abstract</summary>

The deployment of autonomous agents for Computational Fluid Dynamics (CFD), is critically limited by the probabilistic nature of Large Language Models (LLMs), which struggle to enforce the strict conservation laws and numerical stability required for physics-based simulations. Reliance on purely semantic Retrieval Augmented Generation (RAG) often leads to "context poisoning," where agents generate linguistically plausible but physically invalid configurations due to a fundamental Semantic-Physical Disconnect. To bridge this gap, this work introduces PhyNiKCE (Physical and Numerical Knowledgeable Context Engineering), a neurosymbolic agentic framework for trustworthy engineering. Unlike standard black-box agents, PhyNiKCE decouples neural planning from symbolic validation. It employs a Symbolic Knowledge Engine that treats simulation setup as a Constraint Satisfaction Problem, rigidly enforcing physical constraints via a Deterministic RAG Engine with specialized retrieval strategies for solvers, turbulence models, and boundary conditions. Validated through rigorous OpenFOAM experiments on practical, non-tutorial CFD tasks using Gemini-2.5-Pro/Flash, PhyNiKCE demonstrates a 96% relative improvement over state-of-the-art baselines. Furthermore, by replacing trial-and-error with knowledge-driven initialization, the framework reduced autonomous self-correction loops by 59% while simultaneously lowering LLM token consumption by 17%. These results demonstrate that decoupling neural generation from symbolic constraint enforcement significantly enhances robustness and efficiency. While validated on CFD, this architecture offers a scalable, auditable paradigm for Trustworthy Artificial Intelligence in broader industrial automation.

</details>


### 39. When Agents Disagree With Themselves: Measuring Behavioral Consistency in LLM-Based Agents

- **Authors:** Aman Mehta
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11619v1](http://arxiv.org/abs/2602.11619v1)
- **PDF:** [https://arxiv.org/pdf/2602.11619v1](https://arxiv.org/pdf/2602.11619v1)
- **Categories:** cs.AI


> This paper investigates behavioral consistency in LLM-based agents by running the same models on the same task multiple times, revealing that significant discrepancies often arise in their behavior. Analyzing 3,000 runs across models such as Llama 3.1, GPT-4o, and Claude Sonnet 4.5, the study finds that agents exhibit an average of 2.0 to 4.2 distinct action sequences, with higher inconsistency correlating with decreased task accuracy—showing a 32–55 percentage point drop for tasks exhibiting over six unique paths. The authors suggest that monitoring early decision-making stages, particularly the first search query, could enhance reliability and facilitate early error detection in agent systems.


<details>
<summary>Abstract</summary>

Run the same LLM agent on the same task twice: do you get the same behavior? We find the answer is often no. In a study of 3,000 agent runs across three models (Llama 3.1 70B, GPT-4o, and Claude Sonnet 4.5) on HotpotQA, we observe that ReAct-style agents produce 2.0--4.2 distinct action sequences per 10 runs on average, even with identical inputs. More importantly, this variance predicts failure: tasks with consistent behavior ($\leq$2 unique paths) achieve 80--92% accuracy, while highly inconsistent tasks ($\geq$6 unique paths) achieve only 25--60%, a 32--55 percentage point gap depending on model. We trace variance to early decisions: 69% of divergence occurs at step 2, the first search query. Our results suggest that monitoring behavioral consistency during execution could enable early error detection and improve agent reliability.

</details>


### 40. The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs

- **Authors:** Jingdi Chen, Hanqing Yang, Zongjun Liu, Carlee Joe-Wong
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11583v1](http://arxiv.org/abs/2602.11583v1)
- **PDF:** [https://arxiv.org/pdf/2602.11583v1](https://arxiv.org/pdf/2602.11583v1)
- **Categories:** cs.AI, cs.LG


> The paper surveys multi-agent communication (MA-Comm) by examining the key aspects of who communicates, with whom, when, what is conveyed, and why it matters, thereby linking diverse research avenues within the agentic AI field. It outlines the evolution of communication methods across Multi-Agent Reinforcement Learning (MARL), Emergent Language (EL), and Large Language Models (LLMs), highlighting the transition from task-specific protocols to more structured communications and the ongoing challenges such as grounding and scalability in EL. The authors provide insights into effective communication design choices, practical patterns, and unresolved issues, aiming to inform the development of hybrid systems that enhance collaboration and understanding among autonomous agents.


<details>
<summary>Abstract</summary>

Multi-agent sequential decision-making powers many real-world systems, from autonomous vehicles and robotics to collaborative AI assistants. In dynamic, partially observable environments, communication is often what reduces uncertainty and makes collaboration possible. This survey reviews multi-agent communication (MA-Comm) through the Five Ws: who communicates with whom, what is communicated, when communication occurs, and why communication is beneficial. This framing offers a clean way to connect ideas across otherwise separate research threads. We trace how communication approaches have evolved across three major paradigms. In Multi-Agent Reinforcement Learning (MARL), early methods used hand-designed or implicit protocols, followed by end-to-end learned communication optimized for reward and control. While successful, these protocols are frequently task-specific and hard to interpret, motivating work on Emergent Language (EL), where agents can develop more structured or symbolic communication through interaction. EL methods, however, still struggle with grounding, generalization, and scalability, which has fueled recent interest in large language models (LLMs) that bring natural language priors for reasoning, planning, and collaboration in more open-ended settings. Across MARL, EL, and LLM-based systems, we highlight how different choices shape communication design, where the main trade-offs lie, and what remains unsolved. We distill practical design patterns and open challenges to support future hybrid systems that combine learning, language, and control for scalable and interpretable multi-agent collaboration.

</details>


### 41. Learning to Configure Agentic AI Systems

- **Authors:** Aditya Taparia, Som Sagar, Ransalu Senanayake
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11574v1](http://arxiv.org/abs/2602.11574v1)
- **PDF:** [https://arxiv.org/pdf/2602.11574v1](https://arxiv.org/pdf/2602.11574v1)
- **Categories:** cs.AI


> The paper presents ARC (Agentic Resource & Configuration learner), a reinforcement learning-based approach for configuring LLM-based agent systems that enhances performance by tailoring configurations to individual queries rather than relying on fixed templates or heuristics. The methodology involves developing a lightweight hierarchical policy that adapts workflows, tools, and prompts, resulting in improved task accuracy—up to 25%—while also decreasing token usage and runtime costs across various benchmarks. These findings highlight the potential of query-wise configuration in agentic AI systems as a superior alternative to traditional uniform strategies.


<details>
<summary>Abstract</summary>

Configuring LLM-based agent systems involves choosing workflows, tools, token budgets, and prompts from a large combinatorial design space, and is typically handled today by fixed large templates or hand-tuned heuristics. This leads to brittle behavior and unnecessary compute, since the same cumbersome configuration is often applied to both easy and hard input queries. We formulate agent configuration as a query-wise decision problem and introduce ARC (Agentic Resource & Configuration learner), which learns a light-weight hierarchical policy using reinforcement learning to dynamically tailor these configurations. Across multiple benchmarks spanning reasoning and tool-augmented question answering, the learned policy consistently outperforms strong hand-designed and other baselines, achieving up to 25% higher task accuracy while also reducing token and runtime costs. These results demonstrate that learning per-query agent configurations is a powerful alternative to "one size fits all" designs.

</details>


### 42. CausalAgent: A Conversational Multi-Agent System for End-to-End Causal Inference

- **Authors:** Jiawei Zhu, Wei Chen, Ruichu Cai
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11527v1](http://arxiv.org/abs/2602.11527v1)
- **PDF:** [https://arxiv.org/pdf/2602.11527v1](https://arxiv.org/pdf/2602.11527v1)
- **Categories:** cs.AI


> The paper presents CausalAgent, a novel conversational multi-agent system designed to streamline end-to-end causal inference, thereby lowering barriers for users without extensive statistical and programming expertise. Utilizing a combination of Multi-Agent Systems, Retrieval-Augmented Generation, and the Model Context Protocol, the system automates various stages of causal analysis—from data cleaning to reporting—through natural language interactions. Key findings indicate that CausalAgent not only enhances accessibility to causal analysis but also maintains rigorous analytical standards through interactive visualizations, marking a significant advancement in user-centered human-AI collaboration in the agentic AI field.


<details>
<summary>Abstract</summary>

Causal inference holds immense value in fields such as healthcare, economics, and social sciences. However, traditional causal analysis workflows impose significant technical barriers, requiring researchers to possess dual backgrounds in statistics and computer science, while manually selecting algorithms, handling data quality issues, and interpreting complex results. To address these challenges, we propose CausalAgent, a conversational multi-agent system for end-to-end causal inference. The system innovatively integrates Multi-Agent Systems (MAS), Retrieval-Augmented Generation (RAG), and the Model Context Protocol (MCP) to achieve automation from data cleaning and causal structure learning to bias correction and report generation through natural language interaction. Users need only upload a dataset and pose questions in natural language to receive a rigorous, interactive analysis report. As a novel user-centered human-AI collaboration paradigm, CausalAgent explicitly models the analysis workflow. By leveraging interactive visualizations, it significantly lowers the barrier to entry for causal analysis while ensuring the rigor and interpretability of the process.

</details>


### 43. AgentLeak: A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems

- **Authors:** Faouzi El Yagoubi, Ranwa Al Mallah, Godwin Badu-Marfo
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11510v1](http://arxiv.org/abs/2602.11510v1)
- **PDF:** [https://arxiv.org/pdf/2602.11510v1](https://arxiv.org/pdf/2602.11510v1)
- **Categories:** cs.AI


> The paper introduces AgentLeak, the first comprehensive benchmark designed to assess privacy leakage in multi-agent Large Language Model (LLM) systems, targeting internal communication pathways often neglected by existing audits. Utilizing a dataset of 1,000 scenarios across various domains, the study reveals that while multi-agent configurations reduce leakage in output channels, they significantly increase total system exposure due to unmonitored internal communication, with inter-agent messages responsible for the highest leakage rates. The findings emphasize the necessity for enhanced privacy protections in agent coordination frameworks, particularly highlighting that the design of models like Claude 3.5 Sonnet can positively impact leakage rates.


<details>
<summary>Abstract</summary>

Multi-agent Large Language Model (LLM) systems create privacy risks that current benchmarks cannot measure. When agents coordinate on tasks, sensitive data passes through inter-agent messages, shared memory, and tool arguments; pathways that output-only audits never inspect. We introduce AgentLeak, to the best of our knowledge the first full-stack benchmark for privacy leakage covering internal channels, spanning 1,000 scenarios across healthcare, finance, legal, and corporate domains, paired with a 32-class attack taxonomy and three-tier detection pipeline. Testing GPT-4o, GPT-4o-mini, Claude 3.5 Sonnet, Mistral Large, and Llama 3.3 70B across 4,979 traces reveals that multi-agent configurations reduce per-channel output leakage (C1: 27.2% vs 43.2% in single-agent) but introduce unmonitored internal channels that raise total system exposure to 68.9% (OR-aggregated across C1, C2, C5). Internal channels account for most of this gap: inter-agent messages (C2) leak at 68.8%, compared to 27.2% on C1 (output channel). This means that output-only audits miss 41.7% of violations. Claude 3.5 Sonnet, which emphasizes safety alignment in its design, achieves the lowest leakage rates on both external (3.3%) and internal (28.1%) channels, suggesting that model-level safety training may transfer to internal channel protection. Across all five models and four domains, the pattern C2 > C1 holds consistently, confirming that inter-agent communication is the primary vulnerability. These findings underscore the need for coordination frameworks that incorporate internal-channel privacy protections and enforce privacy controls on inter-agent communication.

</details>


### 44. A Generic Framework for Fair Consensus Clustering in Streams

- **Authors:** Diptarka Chakraborty, Kushagra Chatterjee, Debarati Das, Tien-Long Nguyen
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11500v1](http://arxiv.org/abs/2602.11500v1)
- **PDF:** [https://arxiv.org/pdf/2602.11500v1](https://arxiv.org/pdf/2602.11500v1)
- **Categories:** cs.LG


> The paper presents a novel framework for fair consensus clustering in streaming environments, addressing the limitations of previously developed offline methods that require extensive memory storage. The authors introduce a constant-factor algorithm that efficiently processes incoming clusterings with a logarithmic memory footprint and integrates a new algorithmic approach that combines closest fair clustering with cluster fitting, enhancing approximation guarantees. Key findings indicate that this framework is adaptable to various fairness definitions and extends to the k-median consensus clustering scenario, contributing significantly to the field of agentic AI by enabling more equitable data structuring in multi-agent systems.


<details>
<summary>Abstract</summary>

Consensus clustering seeks to combine multiple clusterings of the same dataset, potentially derived by considering various non-sensitive attributes by different agents in a multi-agent environment, into a single partitioning that best reflects the overall structure of the underlying dataset. Recent work by Chakraborty et al, introduced a fair variant under proportionate fairness and obtained a constant-factor approximation by naively selecting the best closest fair input clustering; however, their offline approach requires storing all input clusterings, which is prohibitively expensive for most large-scale applications.
  In this paper, we initiate the study of fair consensus clustering in the streaming model, where input clusterings arrive sequentially and memory is limited. We design the first constant-factor algorithm that processes the stream while storing only a logarithmic number of inputs. En route, we introduce a new generic algorithmic framework that integrates closest fair clustering with cluster fitting, yielding improved approximation guarantees not only in the streaming setting but also when revisited offline. Furthermore, the framework is fairness-agnostic: it applies to any fairness definition for which an approximately close fair clustering can be computed efficiently. Finally, we extend our methods to the more general k-median consensus clustering problem.

</details>


### 45. Distributionally Robust Cooperative Multi-Agent Reinforcement Learning via Robust Value Factorization

- **Authors:** Chengrui Qu, Christopher Yeh, Kishan Panaganti, Eric Mazumdar, Adam Wierman
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11437v1](http://arxiv.org/abs/2602.11437v1)
- **PDF:** [https://arxiv.org/pdf/2602.11437v1](https://arxiv.org/pdf/2602.11437v1)
- **Categories:** cs.AI, cs.MA


> The paper presents a novel approach called Distributionally Robust IGM (DrIGM) to enhance cooperative multi-agent reinforcement learning (MARL) in the presence of environmental uncertainties, establishing a robust alignment between individual agent actions and the team-optimal joint action. The authors develop robust variants of existing value-factorization techniques that operate on robust Q-targets, maintaining scalability and compatibility with existing systems, while providing a provable robustness guarantee. Empirical results demonstrate that their method significantly improves out-of-distribution performance in diverse environments, including SustainGym and StarCraft, highlighting its practical applicability in agentic AI systems.


<details>
<summary>Abstract</summary>

Cooperative multi-agent reinforcement learning (MARL) commonly adopts centralized training with decentralized execution, where value-factorization methods enforce the individual-global-maximum (IGM) principle so that decentralized greedy actions recover the team-optimal joint action. However, the reliability of this recipe in real-world settings remains unreliable due to environmental uncertainties arising from the sim-to-real gap, model mismatch, and system noise. We address this gap by introducing Distributionally robust IGM (DrIGM), a principle that requires each agent's robust greedy action to align with the robust team-optimal joint action. We show that DrIGM holds for a novel definition of robust individual action values, which is compatible with decentralized greedy execution and yields a provable robustness guarantee for the whole system. Building on this foundation, we derive DrIGM-compliant robust variants of existing value-factorization architectures (e.g., VDN/QMIX/QTRAN) that (i) train on robust Q-targets, (ii) preserve scalability, and (iii) integrate seamlessly with existing codebases without bespoke per-agent reward shaping. Empirically, on high-fidelity SustainGym simulators and a StarCraft game environment, our methods consistently improve out-of-distribution performance. Code and data are available at https://github.com/crqu/robust-coMARL.

</details>


### 46. Optimizing Agent Planning for Security and Autonomy

- **Authors:** Aashish Kolluri, Rishi Sharma, Manuel Costa, Boris Köpf, Tobias Nießen, Mark Russinovich, Shruti Tople, Santiago Zanella-Béguelin
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11416v1](http://arxiv.org/abs/2602.11416v1)
- **PDF:** [https://arxiv.org/pdf/2602.11416v1](https://arxiv.org/pdf/2602.11416v1)
- **Categories:** cs.CR, cs.LG


> The paper presents a novel approach to enhancing the autonomy of AI agents while ensuring security against indirect prompt injection attacks through the development of a security-aware agent. By introducing richer human-in-the-loop (HITL) interactions and planning for both task progress and policy compliance, the proposed methodology quantifies autonomy using new metrics that measure the ability to execute actions without human oversight. Key findings indicate that this enhanced agent design increases task autonomy and completion rates, while mitigating the risks associated with prompt injection without compromising overall utility.


<details>
<summary>Abstract</summary>

Indirect prompt injection attacks threaten AI agents that execute consequential actions, motivating deterministic system-level defenses. Such defenses can provably block unsafe actions by enforcing confidentiality and integrity policies, but currently appear costly: they reduce task completion rates and increase token usage compared to probabilistic defenses. We argue that existing evaluations miss a key benefit of system-level defenses: reduced reliance on human oversight. We introduce autonomy metrics to quantify this benefit: the fraction of consequential actions an agent can execute without human-in-the-loop (HITL) approval while preserving security. To increase autonomy, we design a security-aware agent that (i) introduces richer HITL interactions, and (ii) explicitly plans for both task progress and policy compliance. We implement this agent design atop an existing information-flow control defense against prompt injection and evaluate it on the AgentDojo and WASP benchmarks. Experiments show that this approach yields higher autonomy without sacrificing utility.

</details>


### 47. When Visibility Outpaces Verification: Delayed Verification and Narrative Lock-in in Agentic AI Discourse

- **Authors:** Hanjing Shi, Dominic DiFranzo
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11412v1](http://arxiv.org/abs/2602.11412v1)
- **PDF:** [https://arxiv.org/pdf/2602.11412v1](https://arxiv.org/pdf/2602.11412v1)
- **Categories:** cs.CY, cs.AI, cs.HC


> The paper investigates the influence of social proof on the verification of claims concerning agentic AI in online discussions, focusing on the impact of visibility on user trust and discourse quality. Utilizing a longitudinal dataset from two Reddit communities, the authors employ survival analysis to examine how high-visibility discussions often lead to delayed or absent verification of claims, revealing a "Popularity Paradox" that contributes to "Narrative Lock-in." The findings indicate that early unverified claims can solidify cognitive biases, highlighting the need for design interventions such as "epistemic friction" to enhance critical evaluation in AI discourse.


<details>
<summary>Abstract</summary>

Agentic AI systems-autonomous entities capable of independent planning and execution-reshape the landscape of human-AI trust. Long before direct system exposure, user expectations are mediated through high-stakes public discourse on social platforms. However, platform-mediated engagement signals (e.g., upvotes) may inadvertently function as a ``credibility proxy,'' potentially stifling critical evaluation.
  This paper investigates the interplay between social proof and verification timing in online discussions of agentic AI. Analyzing a longitudinal dataset from two distinct Reddit communities with contrasting interaction cultures-r/OpenClaw and r/Moltbook-we operationalize verification cues via reproducible lexical rules and model the ``time-to-first-verification'' using a right-censored survival analysis framework.
  Our findings reveal a systemic ``Popularity Paradox'': high-visibility discussions in both subreddits experience significantly delayed or entirely absent verification cues compared to low-visibility threads. This temporal lag creates a critical window for ``Narrative Lock-in,'' where early, unverified claims crystallize into collective cognitive biases before evidence-seeking behaviors emerge. We discuss the implications of this ``credibility-by-visibility'' effect for AI safety and propose ``epistemic friction'' as a design intervention to rebalance engagement-driven platforms.

</details>


### 48. TRACER: Trajectory Risk Aggregation for Critical Episodes in Agentic Reasoning

- **Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Davide Ettori, Ranganath Krishnan, Amit Ranjan Trivedi
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11409v1](http://arxiv.org/abs/2602.11409v1)
- **PDF:** [https://arxiv.org/pdf/2602.11409v1](https://arxiv.org/pdf/2602.11409v1)
- **Categories:** cs.AI


> The paper introduces TRACER, a novel trajectory-level uncertainty metric designed to enhance the performance of AI agents in multi-turn interactions involving tool use, addressing the limitations of existing single-shot uncertainty proxies that overlook critical failure episodes. TRACER integrates various components, including content-aware surprisal and coherence gap signals, aggregated through a sophisticated risk functional, and is evaluated on the $τ^2$-bench for its effectiveness in predicting task failures. The results show significant improvements in predictive capabilities, with AUROC and AUARC enhancements of up to 37.1% and 55%, respectively, thereby advancing the understanding and management of uncertainties in agentic reasoning contexts.


<details>
<summary>Abstract</summary>

Estimating uncertainty for AI agents in real-world multi-turn tool-using interaction with humans is difficult because failures are often triggered by sparse critical episodes (e.g., looping, incoherent tool use, or user-agent miscoordination) even when local generation appears confident. Existing uncertainty proxies focus on single-shot text generation and therefore miss these trajectory-level breakdown signals. We introduce TRACER, a trajectory-level uncertainty metric for dual-control Tool-Agent-User interaction. TRACER combines content-aware surprisal with situational-awareness signals, semantic and lexical repetition, and tool-grounded coherence gaps, and aggregates them using a tail-focused risk functional with a MAX-composite step risk to surface decisive anomalies. We evaluate TRACER on $τ^2$-bench by predicting task failure and selective task execution. To this end, TRACER improves AUROC by up to 37.1% and AUARC by up to 55% over baselines, enabling earlier and more accurate detection of uncertainty in complex conversational tool-use settings. Our code and benchmark are available at https://github.com/sinatayebati/agent-tracer.

</details>


### 49. ReplicatorBench: Benchmarking LLM Agents for Replicability in Social and Behavioral Sciences

- **Authors:** Bang Nguyen, Dominik Soós, Qian Ma, Rochana R. Obadage, Zack Ranjan, Sai Koneru, Timothy M. Errington, Shakhlo Nematova, Sarah Rajtmajer, Jian Wu, Meng Jiang
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11354v1](http://arxiv.org/abs/2602.11354v1)
- **PDF:** [https://arxiv.org/pdf/2602.11354v1](https://arxiv.org/pdf/2602.11354v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces ReplicatorBench, a novel benchmarking framework designed to evaluate AI agents in the context of research replication within the social and behavioral sciences, addressing the limitations of existing benchmarks that primarily focus on computational reproduction and ignore the complexities of non-replicable research. The methodology involves a three-stage process: extracting replication data, designing and executing experiments, and interpreting results, using an agent framework called ReplicatorAgent, which integrates various tools for these tasks. Key findings indicate that while current large language model (LLM) agents can effectively design and execute computational experiments, they face challenges in retrieving the necessary resources, such as new data, to successfully replicate research claims.


<details>
<summary>Abstract</summary>

The literature has witnessed an emerging interest in AI agents for automated assessment of scientific papers. Existing benchmarks focus primarily on the computational aspect of this task, testing agents' ability to reproduce or replicate research outcomes when having access to the code and data. This setting, while foundational, (1) fails to capture the inconsistent availability of new data for replication as opposed to reproduction, and (2) lacks ground-truth diversity by focusing only on reproducible papers, thereby failing to evaluate an agent's ability to identify non-replicable research. Furthermore, most benchmarks only evaluate outcomes rather than the replication process. In response, we introduce ReplicatorBench, an end-to-end benchmark, including human-verified replicable and non-replicable research claims in social and behavioral sciences for evaluating AI agents in research replication across three stages: (1) extraction and retrieval of replication data; (2) design and execution of computational experiments; and (3) interpretation of results, allowing a test of AI agents' capability to mimic the activities of human replicators in real world. To set a baseline of AI agents' capability, we develop ReplicatorAgent, an agentic framework equipped with necessary tools, like web search and iterative interaction with sandboxed environments, to accomplish tasks in ReplicatorBench. We evaluate ReplicatorAgent across four underlying large language models (LLMs), as well as different design choices of programming language and levels of code access. Our findings reveal that while current LLM agents are capable of effectively designing and executing computational experiments, they struggle with retrieving resources, such as new data, necessary to replicate a claim. All code and data are publicly available at https://github.com/CenterForOpenScience/llm-benchmarking.

</details>


### 50. Pushing Forward Pareto Frontiers of Proactive Agents with Behavioral Agentic Optimization

- **Authors:** Yihang Yao, Zhepeng Cen, Haohong Lin, Shiqi Liu, Zuxin Liu, Jiacheng Zhu, Zhang-Wei Hong, Laixi Shi, Ding Zhao
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11351v1](http://arxiv.org/abs/2602.11351v1)
- **PDF:** [https://arxiv.org/pdf/2602.11351v1](https://arxiv.org/pdf/2602.11351v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces Behavioral Agentic Optimization (BAO), a novel reinforcement learning framework designed to improve the performance of proactive large language model (LLM) agents by enhancing their reasoning and information-gathering capabilities while regulating interaction efficiency. The methodology incorporates behavior enhancement and regularization to effectively balance task performance with user engagement in multi-turn interactions. The key findings show that BAO significantly outperforms existing proactive agentic RL baselines and matches or exceeds the performance of commercial LLM agents, thereby presenting a promising approach for developing user-centered proactive AI systems.


<details>
<summary>Abstract</summary>

Proactive large language model (LLM) agents aim to actively plan, query, and interact over multiple turns, enabling efficient task completion beyond passive instruction following and making them essential for real-world, user-centric applications. Agentic reinforcement learning (RL) has recently emerged as a promising solution for training such agents in multi-turn settings, allowing interaction strategies to be learned from feedback. However, existing pipelines face a critical challenge in balancing task performance with user engagement, as passive agents can not efficiently adapt to users' intentions while overuse of human feedback reduces their satisfaction. To address this trade-off, we propose BAO, an agentic RL framework that combines behavior enhancement to enrich proactive reasoning and information-gathering capabilities with behavior regularization to suppress inefficient or redundant interactions and align agent behavior with user expectations. We evaluate BAO on multiple tasks from the UserRL benchmark suite, and demonstrate that it substantially outperforms proactive agentic RL baselines while achieving comparable or even superior performance to commercial LLM agents, highlighting its effectiveness for training proactive, user-aligned LLM agents in complex multi-turn scenarios. Our website: https://proactive-agentic-rl.github.io/.

</details>


### 51. AgentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition

- **Authors:** Ruipeng Wang, Yuxin Chen, Yukai Wang, Chang Wu, Junfeng Fang, Xiaodong Cai, Qi Gu, Hui Su, An Zhang, Xiang Wang, Xunliang Cai, Tat-Seng Chua
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11348v1](http://arxiv.org/abs/2602.11348v1)
- **PDF:** [https://arxiv.org/pdf/2602.11348v1](https://arxiv.org/pdf/2602.11348v1)
- **Categories:** cs.AI


> The paper presents AgentNoiseBench, a novel framework designed to evaluate the robustness of tool-using large language model (LLM) agents in noisy environments. By analyzing biases and uncertainties in real-world scenarios, the authors categorize noise into user-noise and tool-noise, then develop an automated pipeline to introduce controllable noise into agent-centric benchmarks while maintaining task solvability. The extensive evaluations reveal significant performance variations among different models under varying noise conditions, underscoring the vulnerability of current agent systems to realistic environmental perturbations and emphasizing the need for improved robustness in agentic AI.


<details>
<summary>Abstract</summary>

Recent advances in large language models have enabled LLM-based agents to achieve strong performance on a variety of benchmarks. However, their performance in real-world deployments often that observed on benchmark settings, especially in complex and imperfect environments. This discrepancy largely arises because prevailing training and evaluation paradigms are typically built on idealized assumptions, overlooking the inherent stochasticity and noise present in real-world interactions. To bridge this gap, we introduce AgentNoiseBench, a framework for systematically evaluating the robustness of agentic models under noisy environments. We first conduct an in-depth analysis of biases and uncertainties in real-world scenarios and categorize environmental noise into two primary types: user-noise and tool-noise. Building on this analysis, we develop an automated pipeline that injects controllable noise into existing agent-centric benchmarks while preserving task solvability. Leveraging this pipeline, we perform extensive evaluations across a wide range of models with diverse architectures and parameter scales. Our results reveal consistent performance variations under different noise conditions, highlighting the sensitivity of current agentic models to realistic environmental perturbations.

</details>


### 52. Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP

- **Authors:** Zeynab Anbiaee, Mahdi Rabbani, Mansur Mirani, Gunjan Piya, Igor Opushnyev, Ali Ghorbani, Sajjad Dadkhah
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11327v1](http://arxiv.org/abs/2602.11327v1)
- **PDF:** [https://arxiv.org/pdf/2602.11327v1](https://arxiv.org/pdf/2602.11327v1)
- **Categories:** cs.CR, cs.AI


> This paper proposes a structured threat modeling analysis to evaluate the security of four emerging AI agent communication protocols: Model Context Protocol (MCP), Agent2Agent (A2A), Agora, and Agent Network Protocol (ANP). The methodology includes the development of a qualitative risk assessment framework that identifies twelve protocol-level risks and evaluates their security posture across various operational phases. Key findings reveal significant design-induced risk surfaces, particularly in MCP, urging the need for improved security measures and standardization in AI-agent ecosystems to facilitate secure deployment and interoperability.


<details>
<summary>Abstract</summary>

The rapid development of the AI agent communication protocols, including the Model Context Protocol (MCP), Agent2Agent (A2A), Agora, and Agent Network Protocol (ANP), is reshaping how AI agents communicate with tools, services, and each other. While these protocols support scalable multi-agent interaction and cross-organizational interoperability, their security principles remain understudied, and standardized threat modeling is limited; no protocol-centric risk assessment framework has been established yet. This paper presents a systematic security analysis of four emerging AI agent communication protocols. First, we develop a structured threat modeling analysis that examines protocol architectures, trust assumptions, interaction patterns, and lifecycle behaviors to identify protocol-specific and cross-protocol risk surfaces. Second, we introduce a qualitative risk assessment framework that identifies twelve protocol-level risks and evaluates security posture across the creation, operation, and update phases through systematic assessment of likelihood, impact, and overall protocol risk, with implications for secure deployment and future standardization. Third, we provide a measurement-driven case study on MCP that formalizes the risk of missing mandatory validation/attestation for executable components as a falsifiable security claim by quantifying wrong-provider tool execution under multi-server composition across representative resolver policies. Collectively, our results highlight key design-induced risk surfaces and provide actionable guidance for secure deployment and future standardization of agent communication ecosystems.

</details>


### 53. The PBSAI Governance Ecosystem: A Multi-Agent AI Reference Architecture for Securing Enterprise AI Estates

- **Authors:** John M. Willis
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11301v1](http://arxiv.org/abs/2602.11301v1)
- **PDF:** [https://arxiv.org/pdf/2602.11301v1](https://arxiv.org/pdf/2602.11301v1)
- **Categories:** cs.AI, cs.CR


> The paper presents the Practitioners Blueprint for Secure AI (PBSAI) Governance Ecosystem, a multi-agent reference architecture designed to secure enterprise AI estates comprising various AI systems and tools. Utilizing a twelve domain taxonomy, the PBSAI organizes agent responsibilities and incorporates systems security techniques, while establishing formal models for context and outputs that ensure traceability and human oversight. Key findings demonstrate its alignment with existing governance frameworks like the NIST AI Risk Management Framework, thereby providing a structured foundation for enhancing security in complex AI environments.


<details>
<summary>Abstract</summary>

Enterprises are rapidly deploying large language models, retrieval augmented generation pipelines, and tool using agents into production, often on shared high performance computing clusters and cloud accelerator platforms that also support defensive analytics. These systems increasingly function not as isolated models but as AI estates: socio technical systems spanning models, agents, data pipelines, security tooling, human workflows, and hyperscale infrastructure. Existing governance and security frameworks, including the NIST AI Risk Management Framework and systems security engineering guidance, articulate principles and risk functions but do not provide implementable architectures for multi agent, AI enabled cyber defense.
  This paper introduces the Practitioners Blueprint for Secure AI (PBSAI) Governance Ecosystem, a multi agent reference architecture for securing enterprise and hyperscale AI estates. PBSAI organizes responsibilities into a twelve domain taxonomy and defines bounded agent families that mediate between tools and policy through shared context envelopes and structured output contracts. The architecture assumes baseline enterprise security capabilities and encodes key systems security techniques, including analytic monitoring, coordinated defense, and adaptive response. A lightweight formal model of agents, context envelopes, and ecosystem level invariants clarifies the traceability, provenance, and human in the loop guarantees enforced across domains. We demonstrate alignment with NIST AI RMF functions and illustrate application in enterprise SOC and hyperscale defensive environments. PBSAI is proposed as a structured, evidence centric foundation for open ecosystem development and future empirical validation.

</details>


### 54. Interpretable Attention-Based Multi-Agent PPO for Latency Spike Resolution in 6G RAN Slicing

- **Authors:** Kavan Fatehi, Mostafa Rahmani Ghourtani, Amir Sonee, Poonam Yadav, Alessandra M Russo, Hamed Ahmadi, Radu Calinescu
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11076v1](http://arxiv.org/abs/2602.11076v1)
- **PDF:** [https://arxiv.org/pdf/2602.11076v1](https://arxiv.org/pdf/2602.11076v1)
- **Categories:** eess.SY, cs.AI, eess.SP


> The paper presents Attention-Enhanced Multi-Agent Proximal Policy Optimization (AE-MAPPO), a novel framework designed to effectively resolve latency spikes in 6G radio access networks (RAN) by combining deep reinforcement learning with interpretable attention mechanisms. Utilizing a three-phase strategy—predictive, reactive, and inter-slice optimization—AE-MAPPO demonstrates impressive performance in a URLLC case study by resolving latency spikes within 18 ms and achieving a latency of 0.98 ms with 99.9999% reliability, significantly reducing troubleshooting time by 93% while ensuring service continuity. The findings underscore AE-MAPPO's capability to provide real-time automation with high interpretability, enhancing compliance with service-level agreements in complex network environments.


<details>
<summary>Abstract</summary>

Sixth-generation (6G) radio access networks (RANs) must enforce strict service-level agreements (SLAs) for heterogeneous slices, yet sudden latency spikes remain difficult to diagnose and resolve with conventional deep reinforcement learning (DRL) or explainable RL (XRL). We propose \emph{Attention-Enhanced Multi-Agent Proximal Policy Optimization (AE-MAPPO)}, which integrates six specialized attention mechanisms into multi-agent slice control and surfaces them as zero-cost, faithful explanations. The framework operates across O-RAN timescales with a three-phase strategy: predictive, reactive, and inter-slice optimization.
  A URLLC case study shows AE-MAPPO resolves a latency spike in $18$ms, restores latency to $0.98$ms with $99.9999\%$ reliability, and reduces troubleshooting time by $93\%$ while maintaining eMBB and mMTC continuity. These results confirm AE-MAPPO's ability to combine SLA compliance with inherent interpretability, enabling trustworthy and real-time automation for 6G RAN slicing.

</details>


### 55. Evaluating Memory Structure in LLM Agents

- **Authors:** Alina Shutova, Alexandra Olenina, Ivan Vinogradov, Anton Sinitsin
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11243v1](http://arxiv.org/abs/2602.11243v1)
- **PDF:** [https://arxiv.org/pdf/2602.11243v1](https://arxiv.org/pdf/2602.11243v1)
- **Categories:** cs.LG, cs.CL


> The paper introduces StructMemEval, a benchmark designed to evaluate how LLM-based agents organize their long-term memory, moving beyond traditional assessments that focus solely on fact retention and recall. The authors curate a series of tasks that reflect human-like organization of memory, such as managing transaction ledgers and to-do lists, revealing that while simple retrieval-augmented LLMs struggle with these structured tasks, memory-enhanced agents perform well when given guidance on memory organization. Key findings emphasize the necessity for improved training methods and memory architecture designs, as current LLMs often fail to autonomously recognize or utilize complex memory structures without explicit prompts.


<details>
<summary>Abstract</summary>

Modern LLM-based agents and chat assistants rely on long-term memory frameworks to store reusable knowledge, recall user preferences, and augment reasoning. As researchers create more complex memory architectures, it becomes increasingly difficult to analyze their capabilities and guide future memory designs. Most long-term memory benchmarks focus on simple fact retention, multi-hop recall, and time-based changes. While undoubtedly important, these capabilities can often be achieved with simple retrieval-augmented LLMs and do not test complex memory hierarchies. To bridge this gap, we propose StructMemEval - a benchmark that tests the agent's ability to organize its long-term memory, not just factual recall. We gather a suite of tasks that humans solve by organizing their knowledge in a specific structure: transaction ledgers, to-do lists, trees and others. Our initial experiments show that simple retrieval-augmented LLMs struggle with these tasks, whereas memory agents can reliably solve them if prompted how to organize their memory. However, we also find that modern LLMs do not always recognize the memory structure when not prompted to do so. This highlights an important direction for future improvements in both LLM training and memory frameworks.

</details>


### 56. Divide, Harmonize, Then Conquer It: Shooting Multi-Commodity Flow Problems with Multimodal Language Models

- **Authors:** Xinyu Yuan, Yan Qiao, Zonghui Wang, Wenzhi Chen
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11057v1](http://arxiv.org/abs/2602.11057v1)
- **PDF:** [https://arxiv.org/pdf/2602.11057v1](https://arxiv.org/pdf/2602.11057v1)
- **Categories:** cs.LG


> The paper presents Pram, a novel machine learning-based method that applies multimodal language models (MLMs) to effectively address multi-commodity flow (MCF) problems in a way that balances optimality and tractability. The methodology involves dividing the MCF problem into local subproblems handled by MLM-powered agents and harmonizing their solutions through a multi-agent reinforcement learning algorithm. Key findings indicate that Pram achieves comparable or superior performance to traditional linear programming solvers, with significantly reduced runtime and robustness to link failures, making it a scalable and practical solution for contemporary allocation systems.


<details>
<summary>Abstract</summary>

The multi-commodity flow (MCF) problem is a fundamental topic in network flow and combinatorial optimization, with broad applications in transportation, communication, and logistics, etc. Nowadays, the rapid expansion of allocation systems has posed challenges for existing optimization engines in balancing optimality and tractability. In this paper, we present Pram, the first ML-based method that leverages the reasoning power of multimodal language models (MLMs) for addressing the trade-off dilemma -- a great need of service providers. As part of our proposal, Pram (i) quickly computes high-quality allocations by dividing the original problem into local subproblems, which are then resolved by an MLM-powered "agent", and (ii) ensures global consistency by harmonizing these subproblems via a multi-agent reinforcement learning algorithm. Theoretically, we show that Pram, which learns to perform gradient descent in context, provably converges to the optimum within the family of MCF problems. Empirically, on real-world datasets and public topologies, Pram achieves performance comparable to, and in some cases even surpassing, linear programming solvers (very close to the optimal solution), and substantially lower runtimes (1 to 2 orders of magnitude faster). Moreover, Pram exhibits strong robustness (<10\% performance degradation under link failures or flow bursts), demonstrating MLM's generalization ability to unforeseen events. Pram is objective-agnostic and seamlessly integrates with mainstream allocation systems, providing a practical and scalable solution for future networks.

</details>


### 57. SurveyLens: A Research Discipline-Aware Benchmark for Automatic Survey Generation

- **Authors:** Beichen Guo, Zhiyuan Wen, Jia Gu, Senzhang Wang, Haochen Shi, Ruosong Yang, Shuaiqi Liu
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11238v1](http://arxiv.org/abs/2602.11238v1)
- **PDF:** [https://arxiv.org/pdf/2602.11238v1](https://arxiv.org/pdf/2602.11238v1)
- **Categories:** cs.CL


> The paper introduces SurveyLens, a discipline-aware benchmark designed to evaluate Automatic Survey Generation (ASG) methods across various academic fields, addressing the limitations of current evaluation metrics that are biased toward Computer Science. It features SurveyLens-1k, a dataset of 1,000 high-quality human-written surveys covering 10 disciplines, and proposes a dual-lens evaluation framework that includes Discipline-Aware Rubric Evaluation and Canonical Alignment Evaluation. Key findings indicate differences in the performance of 11 evaluated ASG methods, offering insights into their strengths and weaknesses and providing guidance for selecting suitable tools based on specific disciplinary standards, thereby advancing the field of agentic AI.


<details>
<summary>Abstract</summary>

The exponential growth of scientific literature has driven the evolution of Automatic Survey Generation (ASG) from simple pipelines to multi-agent frameworks and commercial Deep Research agents. However, current ASG evaluation methods rely on generic metrics and are heavily biased toward Computer Science (CS), failing to assess whether ASG methods adhere to the distinct standards of various academic disciplines. Consequently, researchers, especially those outside CS, lack clear guidance on using ASG systems to yield high-quality surveys compliant with specific discipline standards. To bridge this gap, we introduce SurveyLens, the first discipline-aware benchmark evaluating ASG methods across diverse research disciplines. We construct SurveyLens-1k, a curated dataset of 1,000 high-quality human-written surveys spanning 10 disciplines. Subsequently, we propose a dual-lens evaluation framework: (1) Discipline-Aware Rubric Evaluation, which utilizes LLMs with human preference-aligned weights to assess adherence to domain-specific writing standards; and (2) Canonical Alignment Evaluation to rigorously measure content coverage and synthesis quality against human-written survey papers. We conduct extensive experiments by evaluating 11 state-of-the-art ASG methods on SurveyLens, including Vanilla LLMs, ASG systems, and Deep Research agents. Our analysis reveals the distinct strengths and weaknesses of each paradigm across fields, providing essential guidance for selecting tools tailored to specific disciplinary requirements.

</details>


### 58. Chain-of-Look Spatial Reasoning for Dense Surgical Instrument Counting

- **Authors:** Rishikesh Bhyri, Brian R Quaranto, Philip J Seger, Kaity Tung, Brendan Fox, Gene Yang, Steven D. Schwaitzberg, Junsong Yuan, Nan Xi, Peter C W Kim
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11024v1](http://arxiv.org/abs/2602.11024v1)
- **PDF:** [https://arxiv.org/pdf/2602.11024v1](https://arxiv.org/pdf/2602.11024v1)
- **Categories:** cs.CV, cs.AI


> The paper presents Chain-of-Look, a novel visual reasoning framework designed for accurate counting of surgical instruments in densely crowded operating room scenarios. By structurally guiding the counting process along a coherent spatial trajectory and implementing a neighboring loss function to model physical constraints, this method significantly improves counting accuracy over traditional object detection and existing AI models. The introduction of the SurgCount-HD dataset, along with extensive experiments, demonstrates that Chain-of-Look surpasses current state-of-the-art methods and multimodal large language models in this challenging task, highlighting its potential impact in the agentic AI and healthcare fields.


<details>
<summary>Abstract</summary>

Accurate counting of surgical instruments in Operating Rooms (OR) is a critical prerequisite for ensuring patient safety during surgery. Despite recent progress of large visual-language models and agentic AI, accurately counting such instruments remains highly challenging, particularly in dense scenarios where instruments are tightly clustered. To address this problem, we introduce Chain-of-Look, a novel visual reasoning framework that mimics the sequential human counting process by enforcing a structured visual chain, rather than relying on classic object detection which is unordered. This visual chain guides the model to count along a coherent spatial trajectory, improving accuracy in complex scenes. To further enforce the physical plausibility of the visual chain, we introduce the neighboring loss function, which explicitly models the spatial constraints inherent to densely packed surgical instruments. We also present SurgCount-HD, a new dataset comprising 1,464 high-density surgical instrument images. Extensive experiments demonstrate that our method outperforms state-of-the-art approaches for counting (e.g., CountGD, REC) as well as Multimodality Large Language Models (e.g., Qwen, ChatGPT) in the challenging task of dense surgical instrument counting.

</details>


### 59. TVCACHE: A Stateful Tool-Value Cache for Post-Training LLM Agents

- **Authors:** Abhishek Vijaya Kumar, Bhaskar Kataria, Byungsoo Oh, Emaad Manzoor, Rachee Singh
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10986v1](http://arxiv.org/abs/2602.10986v1)
- **PDF:** [https://arxiv.org/pdf/2602.10986v1](https://arxiv.org/pdf/2602.10986v1)
- **Categories:** cs.LG


> The paper presents TVCACHE, a novel stateful tool-value cache designed to enhance the efficiency of post-training large language model (LLM) agents by caching tool outputs that depend on specific environment states. The methodology involves maintaining a tree structure of observed tool-call sequences and utilizing longest-prefix matching for accurate cache lookups, ensuring environmental consistency. Key findings highlight that TVCACHE achieves cache hit rates of up to 70% and significantly reduces the median tool call execution time by up to 6.9X, without compromising the reward accumulation during post-training, thereby providing an effective solution for optimizing resource utilization in LLM agent systems.


<details>
<summary>Abstract</summary>

In RL post-training of LLM agents, calls to external tools take several seconds or even minutes, leaving allocated GPUs idle and inflating post-training time and cost. While many tool invocations repeat across parallel rollouts and could in principle be cached, naively caching their outputs for reuse is incorrect since tool outputs depend on the environment state induced by prior agent interactions. We present TVCACHE, a stateful tool-value cache for LLM agent post-training. TVCACHE maintains a tree of observed tool-call sequences and performs longest-prefix matching for cache lookups: a hit occurs only when the agent's full tool history matches a previously executed sequence, guaranteeing identical environment state. On three diverse workloads-terminal-based tasks, SQL generation, and video understanding. TVCACHE achieves cache hit rates of up to 70% and reduces median tool call execution time by up to 6.9X, with no degradation in post-training reward accumulation.

</details>


### 60. CMAD: Cooperative Multi-Agent Diffusion via Stochastic Optimal Control

- **Authors:** Riccardo Barbano, Alexander Denker, Zeljko Kereta, Runchang Li, Francisco Vargas
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10933v1](http://arxiv.org/abs/2602.10933v1)
- **PDF:** [https://arxiv.org/pdf/2602.10933v1](https://arxiv.org/pdf/2602.10933v1)
- **Categories:** cs.LG


> The paper introduces CMAD, a novel approach to cooperative multi-agent diffusion modeled as a Stochastic Optimal Control problem, aiming to enhance the compositional generation of outputs from multiple pre-trained models. The methodology treats diffusion models as interacting agents that collaboratively adjust their trajectories to achieve a common goal, rather than relying on traditional algebraic compositions of probability densities. Key findings demonstrate that this cooperative control framework outperforms a baseline method that employs basic gradient guidance, particularly in tasks such as conditional MNIST generation, indicating promising advancements for agentic AI systems in collaborative compositional tasks.


<details>
<summary>Abstract</summary>

Continuous-time generative models have achieved remarkable success in image restoration and synthesis. However, controlling the composition of multiple pre-trained models remains an open challenge. Current approaches largely treat composition as an algebraic composition of probability densities, such as via products or mixtures of experts. This perspective assumes the target distribution is known explicitly, which is almost never the case. In this work, we propose a different paradigm that formulates compositional generation as a cooperative Stochastic Optimal Control problem. Rather than combining probability densities, we treat pre-trained diffusion models as interacting agents whose diffusion trajectories are jointly steered, via optimal control, toward a shared objective defined on their aggregated output. We validate our framework on conditional MNIST generation and compare it against a naive inference-time DPS-style baseline replacing learned cooperative control with per-step gradient guidance.

</details>


### 61. Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System

- **Authors:** Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, Zhuotao Liu
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10915v3](http://arxiv.org/abs/2602.10915v3)
- **PDF:** [https://arxiv.org/pdf/2602.10915v3](https://arxiv.org/pdf/2602.10915v3)
- **Categories:** cs.CR, cs.AI


> The paper presents Aura, an innovative Agent Universal Runtime Architecture designed to enhance security in mobile agent systems, moving away from the vulnerable "Screen-as-Interface" paradigm. Through a systematic security analysis of existing mobile agents, it identifies critical vulnerabilities across four dimensions and proposes a structured interaction model that improves both security and performance. The evaluation results show significant improvements in task success rates and reductions in attack success rates, establishing Aura as a promising solution for secure autonomous agent operations in mobile environments.


<details>
<summary>Abstract</summary>

The evolution of Large Language Models (LLMs) has shifted mobile computing from App-centric interactions to system-level autonomous agents. Current implementations predominantly rely on a "Screen-as-Interface" paradigm, which inherits structural vulnerabilities and conflicts with the mobile ecosystem's economic foundations. In this paper, we conduct a systematic security analysis of state-of-the-art mobile agents using Doubao Mobile Assistant as a representative case. We decompose the threat landscape into four dimensions - Agent Identity, External Interface, Internal Reasoning, and Action Execution - revealing critical flaws such as fake App identity, visual spoofing, indirect prompt injection, and unauthorized privilege escalation stemming from a reliance on unstructured visual data.
  To address these challenges, we propose Aura, an Agent Universal Runtime Architecture for a clean-slate secure agent OS. Aura replaces brittle GUI scraping with a structured, agent-native interaction model. It adopts a Hub-and-Spoke topology where a privileged System Agent orchestrates intent, sandboxed App Agents execute domain-specific tasks, and the Agent Kernel mediates all communication. The Agent Kernel enforces four defense pillars: (i) cryptographic identity binding via a Global Agent Registry; (ii) semantic input sanitization through a multilayer Semantic Firewall; (iii) cognitive integrity via taint-aware memory and plan-trajectory alignment; and (iv) granular access control with non-deniable auditing. Evaluation on MobileSafetyBench shows that, compared to Doubao, Aura improves low-risk Task Success Rate from roughly 75% to 94.3%, reduces high-risk Attack Success Rate from roughly 40% to 4.4%, and achieves near-order-of-magnitude latency gains. These results demonstrate Aura as a viable, secure alternative to the "Screen-as-Interface" paradigm.

</details>


### 62. Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation

- **Authors:** Hubert M. Pysklo, Artem Zhuravel, Patrick D. Watson
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11224v1](http://arxiv.org/abs/2602.11224v1)
- **PDF:** [https://arxiv.org/pdf/2602.11224v1](https://arxiv.org/pdf/2602.11224v1)
- **Categories:** cs.SE, cs.CL


> The paper presents Agent-Diff, a benchmarking framework designed to evaluate agentic Large Language Models (LLMs) on enterprise API tasks through controlled code execution with state-diff-based evaluation. The methodology incorporates a unique state-diff contract to define task success based on environmental changes rather than traditional matching methods, alongside a standardized sandbox for executing code against real APIs. Key findings demonstrate that Agent-Diff effectively benchmarks nine LLMs across 224 tasks, revealing performance variations influenced by model differences and API documentation access.


<details>
<summary>Abstract</summary>

We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world tasks that execute code via external APIs. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and agentic frameworks. Benchmarks must make fundamental trade-offs between a sandboxed approach that controls for variation in software environments and more ecologically valid approaches employing real services. Agent-Diff attempts to capture the desirable features of both of these approaches by including access to the real API interfaces for software services while sandboxing the environment in which calls are made, processed, and evaluated. This approach relies on two key innovations. The first is a novel state-diff contract, which separates process from outcome - rather than fuzzy trace or parameter matching, we define task success as whether the expected change in environment state was achieved. The second is a novel sandbox that provides a standardized scripting layer that all models use to execute code against external APIs (Slack, Box, Linear, Google Calendar). Thus, we can evaluate different agentic LLMs against a standardized set of contracts using a unified sandbox while still evaluating their performance on real-world service interfaces. Using the Agent-Diff framework, we provide benchmarks for nine LLMs across 224 tasks utilizing enterprise software workflows. In addition, we evaluate the robustness of the framework with ablation experiments to assess the contribution of access to API documentation on benchmark performance. Code and data: https://github.com/agent-diff-bench/agent-diff.

</details>


### 63. Towards Probabilistic Strategic Timed CTL

- **Authors:** Wojciech Jamroga, Marta Kwiatkowska, Wojciech Penczek, Laure Petrucci, Teofil Sidoruk
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10824v1](http://arxiv.org/abs/2602.10824v1)
- **PDF:** [https://arxiv.org/pdf/2602.10824v1](https://arxiv.org/pdf/2602.10824v1)
- **Categories:** cs.LO, cs.MA


> The paper introduces PSTCTL, a probabilistic extension of Strategic Timed CTL (STCTL) designed for stochastic multi-agent systems operating in continuous time and asynchronous environments. The methodology involves developing verification techniques using irP-strategies to analyze these systems. Key findings indicate that PSTCTL effectively expands the expressiveness of temporal logics in agent systems, facilitating the modeling and verification of strategic behavior in probabilistic contexts.


<details>
<summary>Abstract</summary>

We define PSTCTL, a probabilistic variant of Strategic Timed CTL (STCTL), interpreted over stochastic multi-agent systems with continuous time and asynchronous execution semantics. STCTL extends TCTL with strategic operators in the style of ATL. Moreover, we demonstrate the feasibility of verification with irP-strategies.

</details>


### 64. See, Plan, Snap: Evaluating Multimodal GUI Agents in Scratch

- **Authors:** Xingyi Zhang, Yulei Ye, Kaifeng Huang, Wenhao Li, Xiangfeng Wang
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10814v1](http://arxiv.org/abs/2602.10814v1)
- **PDF:** [https://arxiv.org/pdf/2602.10814v1](https://arxiv.org/pdf/2602.10814v1)
- **Categories:** cs.AI


> The paper presents ScratchWorld, a novel benchmark designed to evaluate multimodal GUI agents in Scratch, focusing on program-by-construction tasks following the Use-Modify-Create pedagogical framework. The authors employ two interaction modes—primitive and composite—and introduce an execution-based evaluation protocol to assess functional correctness. Findings reveal a significant reasoning-acting gap in state-of-the-art agents, indicating challenges in fine-grained GUI manipulation despite proficient planning abilities, thus underscoring critical areas for improvement in agentic AI systems.


<details>
<summary>Abstract</summary>

Block-based programming environments such as Scratch play a central role in low-code education, yet evaluating the capabilities of AI agents to construct programs through Graphical User Interfaces (GUIs) remains underexplored. We introduce ScratchWorld, a benchmark for evaluating multimodal GUI agents on program-by-construction tasks in Scratch. Grounded in the Use-Modify-Create pedagogical framework, ScratchWorld comprises 83 curated tasks spanning four distinct problem categories: Create, Debug, Extend, and Compute. To rigorously diagnose the source of agent failures, the benchmark employs two complementary interaction modes: primitive mode requires fine-grained drag-and-drop manipulation to directly assess visuomotor control, while composite mode uses high-level semantic APIs to disentangle program reasoning from GUI execution. To ensure reliable assessment, we propose an execution-based evaluation protocol that validates the functional correctness of the constructed Scratch programs through runtime tests within the browser environment. Extensive experiments across state-of-the-art multimodal language models and GUI agents reveal a substantial reasoning--acting gap, highlighting persistent challenges in fine-grained GUI manipulation despite strong planning capabilities.

</details>


### 65. Locomo-Plus: Beyond-Factual Cognitive Memory Evaluation Framework for LLM Agents

- **Authors:** Yifei Li, Weidong Guo, Lingling Zhang, Rongman Xu, Muye Huang, Hui Liu, Lijiao Xu, Yu Xu, Jun Liu
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10715v1](http://arxiv.org/abs/2602.10715v1)
- **PDF:** [https://arxiv.org/pdf/2602.10715v1](https://arxiv.org/pdf/2602.10715v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces Locomo-Plus, a novel benchmark designed to evaluate long-term conversational memory in LLM-based dialogue systems, emphasizing the importance of implicit user constraints beyond mere factual recall. The authors develop a unified evaluation framework that focuses on constraint consistency and demonstrate its superiority over traditional string-matching metrics through experiments with various models and memory systems. Key findings reveal that existing benchmarks fail to capture significant cognitive memory challenges, underscoring the need for more nuanced evaluation methods in the agentic AI field.


<details>
<summary>Abstract</summary>

Long-term conversational memory is a core capability for LLM-based dialogue systems, yet existing benchmarks and evaluation protocols primarily focus on surface-level factual recall. In realistic interactions, appropriate responses often depend on implicit constraints such as user state, goals, or values that are not explicitly queried later. To evaluate this setting, we introduce \textbf{LoCoMo-Plus}, a benchmark for assessing cognitive memory under cue--trigger semantic disconnect, where models must retain and apply latent constraints across long conversational contexts. We further show that conventional string-matching metrics and explicit task-type prompting are misaligned with such scenarios, and propose a unified evaluation framework based on constraint consistency. Experiments across diverse backbone models, retrieval-based methods, and memory systems demonstrate that cognitive memory remains challenging and reveals failures not captured by existing benchmarks. Our code and evaluation framework are publicly available at: https://github.com/xjtuleeyf/Locomo-Plus.

</details>


### 66. Beyond Task Performance: A Metric-Based Analysis of Sequential Cooperation in Heterogeneous Multi-Agent Destructive Foraging

- **Authors:** Alejandro Mendoza Barrionuevo, Samuel Yanes Luis, Daniel Gutiérrez Reina, Sergio L. Toral Marín
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10685v1](http://arxiv.org/abs/2602.10685v1)
- **PDF:** [https://arxiv.org/pdf/2602.10685v1](https://arxiv.org/pdf/2602.10685v1)
- **Categories:** cs.MA, cs.LG


> The paper proposes a novel framework for analyzing cooperation in heterogeneous multi-agent systems operating under partial observability and temporal role dependency, specifically within a destructive multi-agent foraging context. It introduces a comprehensive suite of transferably applicable cooperation metrics categorized into primary, inter-team, and intra-team metrics, which encompass efficiency, coordination, dependency, fairness, and sensitivity among agents. The metrics were validated through a realistic scenario involving autonomous vehicles, and the evaluation demonstrated their effectiveness in assessing various learning-based and heuristic approaches, thus enhancing our understanding of cooperation in agentic AI systems.


<details>
<summary>Abstract</summary>

This work addresses the problem of analyzing cooperation in heterogeneous multi-agent systems which operate under partial observability and temporal role dependency, framed within a destructive multi-agent foraging setting. Unlike most previous studies, which focus primarily on algorithmic performance with respect to task completion, this article proposes a systematic set of general-purpose cooperation metrics aimed at characterizing not only efficiency, but also coordination and dependency between teams and agents, fairness, and sensitivity. These metrics are designed to be transferable to different multi-agent sequential domains similar to foraging. The proposed suite of metrics is structured into three main categories that jointly provide a multilevel characterization of cooperation: primary metrics, inter-team metrics, and intra-team metrics. They have been validated in a realistic destructive foraging scenario inspired by dynamic aquatic surface cleaning using heterogeneous autonomous vehicles. It involves two specialized teams with sequential dependencies: one focused on the search of resources, and another on their destruction. Several representative approaches have been evaluated, covering both learning-based algorithms and classical heuristic paradigms.

</details>


### 67. UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory

- **Authors:** Yongshi Ye, Hui Jiang, Feihu Jiang, Tian Lan, Yichao Du, Biao Fu, Xiaodong Shi, Qianghuai Jia, Longyue Wang, Weihua Luo
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10652v1](http://arxiv.org/abs/2602.10652v1)
- **PDF:** [https://arxiv.org/pdf/2602.10652v1](https://arxiv.org/pdf/2602.10652v1)
- **Categories:** cs.CL


> The paper presents the Unified Memory Extraction and Management (UMEM) framework, which enhances memory generalization in Large Language Models (LLMs) by simultaneously optimizing memory extraction and management processes. Unlike traditional methods that focus primarily on memory management while treating extraction statically, UMEM employs Semantic Neighborhood Modeling and utilizes a neighborhood-level marginal utility reward to evaluate memory utility across semantically related queries. The approach demonstrates significant performance improvements across five benchmarks, achieving up to a 10.67% enhancement in multi-turn interactive tasks while maintaining a consistent growth in memory quality, which is crucial for advancing agentic AI capabilities.


<details>
<summary>Abstract</summary>

Self-evolving memory serves as the trainable parameters for Large Language Models (LLMs)-based agents, where extraction (distilling insights from experience) and management (updating the memory bank) must be tightly coordinated. Existing methods predominately optimize memory management while treating memory extraction as a static process, resulting in poor generalization, where agents accumulate instance-specific noise rather than robust memories. To address this, we propose Unified Memory Extraction and Management (UMEM), a self-evolving agent framework that jointly optimizes a Large Language Model to simultaneous extract and manage memories. To mitigate overfitting to specific instances, we introduce Semantic Neighborhood Modeling and optimize the model with a neighborhood-level marginal utility reward via GRPO. This approach ensures memory generalizability by evaluating memory utility across clusters of semantically related queries. Extensive experiments across five benchmarks demonstrate that UMEM significantly outperforms highly competitive baselines, achieving up to a 10.67% improvement in multi-turn interactive tasks. Futhermore, UMEM maintains a monotonic growth curve during continuous evolution. Codes and models will be publicly released.

</details>


### 68. Co-jump: Cooperative Jumping with Quadrupedal Robots via Multi-Agent Reinforcement Learning

- **Authors:** Shihao Dong, Yeke Chen, Zeren Luo, Jiahui Zhang, Bowen Xu, Jinghan Lin, Yimin Han, Ji Ma, Zhiyou Yu, Yudong Zhao, Peng Lu
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10514v1](http://arxiv.org/abs/2602.10514v1)
- **PDF:** [https://arxiv.org/pdf/2602.10514v1](https://arxiv.org/pdf/2602.10514v1)
- **Categories:** cs.RO, cs.AI, cs.LG


> The paper "Co-jump: Cooperative Jumping with Quadrupedal Robots via Multi-Agent Reinforcement Learning" presents a novel approach where two quadrupedal robots cooperate to perform jumps that exceed their individual capabilities, using a framework based on Multi-Agent Proximal Policy Optimization (MAPPO). The methodology employs decentralized decision-making without explicit communication and addresses high-impulse dynamics through a progressive curriculum strategy, enabling efficient learning in mechanically coupled systems. Key findings include the robots achieving synchronized multi-directional jumps onto platforms as high as 1.5 m, with one robot reaching a foot-end elevation of 1.1 m—significantly improving performance compared to solo jumps—thus laying the groundwork for advanced collaborative locomotion in dynamic environments.


<details>
<summary>Abstract</summary>

While single-agent legged locomotion has witnessed remarkable progress, individual robots remain fundamentally constrained by physical actuation limits. To transcend these boundaries, we introduce Co-jump, a cooperative task where two quadrupedal robots synchronize to execute jumps far beyond their solo capabilities. We tackle the high-impulse contact dynamics of this task under a decentralized setting, achieving synchronization without explicit communication or pre-specified motion primitives. Our framework leverages Multi-Agent Proximal Policy Optimization (MAPPO) enhanced by a progressive curriculum strategy, which effectively overcomes the sparse-reward exploration challenges inherent in mechanically coupled systems. We demonstrate robust performance in simulation and successful transfer to physical hardware, executing multi-directional jumps onto platforms up to 1.5 m in height. Specifically, one of the robots achieves a foot-end elevation of 1.1 m, which represents a 144% improvement over the 0.45 m jump height of a standalone quadrupedal robot, demonstrating superior vertical performance. Notably, this precise coordination is achieved solely through proprioceptive feedback, establishing a foundation for communication-free collaborative locomotion in constrained environments.

</details>


### 69. Authenticated Workflows: A Systems Approach to Protecting Agentic AI

- **Authors:** Mohan Rajagopalan, Vinay Rao
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10465v1](http://arxiv.org/abs/2602.10465v1)
- **PDF:** [https://arxiv.org/pdf/2602.10465v1](https://arxiv.org/pdf/2602.10465v1)
- **Categories:** cs.CR, cs.AI, cs.DC, cs.MA


> The paper introduces "authenticated workflows," a novel framework designed to provide a comprehensive trust layer for enterprise agentic AI systems, addressing the limitations of existing defenses such as guardrails and semantic filters. The methodology involves enforcing security at four critical boundaries—prompts, tools, data, and context—by ensuring operations adhere to organizational policies and maintain cryptographic integrity, which results in deterministic security. Key findings demonstrate the framework’s effectiveness through a universal security runtime that integrates leading AI frameworks, achieving 100% recall with zero false positives in extensive testing, and successfully mitigating significant security vulnerabilities.


<details>
<summary>Abstract</summary>

Agentic AI systems automate enterprise workflows but existing defenses--guardrails, semantic filters--are probabilistic and routinely bypassed. We introduce authenticated workflows, the first complete trust layer for enterprise agentic AI. Security reduces to protecting four fundamental boundaries: prompts, tools, data, and context. We enforce intent (operations satisfy organizational policies) and integrity (operations are cryptographically authentic) at every boundary crossing, combining cryptographic elimination of attack classes with runtime policy enforcement. This delivers deterministic security--operations either carry valid cryptographic proof or are rejected. We introduce MAPL, an AI-native policy language that expresses agentic constraints dynamically as agents evolve and invocation context changes, scaling as O(log M + N) policies versus O(M x N) rules through hierarchical composition with cryptographic attestations for workflow dependencies. We prove practicality through a universal security runtime integrating nine leading frameworks (MCP, A2A, OpenAI, Claude, LangChain, CrewAI, AutoGen, LlamaIndex, Haystack) through thin adapters requiring zero protocol modifications. Formal proofs establish completeness and soundness. Empirical validation shows 100% recall with zero false positives across 174 test cases, protection against 9 of 10 OWASP Top 10 risks, and complete mitigation of two high impact production CVEs.

</details>


### 70. The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis

- **Authors:** Peiran Wang, Xinfeng Li, Chong Xiang, Jinghuai Zhang, Ying Li, Lixia Zhang, Xiaofeng Wang, Yuan Tian
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10453v1](http://arxiv.org/abs/2602.10453v1)
- **PDF:** [https://arxiv.org/pdf/2602.10453v1](https://arxiv.org/pdf/2602.10453v1)
- **Categories:** cs.CR, cs.CL


> The paper presents a comprehensive overview of Prompt Injection (PI) threats in Large Language Model (LLM) agents, establishing a taxonomy of PI attacks and defenses through a systematic literature review and quantitative analysis. A significant contribution is the introduction of AgentPI, a benchmark designed to evaluate agent behavior in context-dependent interaction scenarios, revealing that current defenses often fail to generalize to realistic settings. The study finds that no existing defense achieves high trustworthiness, utility, and low latency simultaneously, highlighting the limitations of current approaches and identifying critical areas for future research in agentic AI security.


<details>
<summary>Abstract</summary>

The evolution of Large Language Models (LLMs) has resulted in a paradigm shift towards autonomous agents, necessitating robust security against Prompt Injection (PI) vulnerabilities where untrusted inputs hijack agent behaviors. This SoK presents a comprehensive overview of the PI landscape, covering attacks, defenses, and their evaluation practices. Through a systematic literature review and quantitative analysis, we establish taxonomies that categorize PI attacks by payload generation strategies (heuristic vs. optimization) and defenses by intervention stages (text, model, and execution levels). Our analysis reveals a key limitation shared by many existing defenses and benchmarks: they largely overlook context-dependent tasks, in which agents are authorized to rely on runtime environmental observations to determine actions. To address this gap, we introduce AgentPI, a new benchmark designed to systematically evaluate agent behavior under context-dependent interaction settings. Using AgentPI, we empirically evaluate representative defenses and show that no single approach can simultaneously achieve high trustworthiness, high utility, and low latency. Moreover, we show that many defenses appear effective under existing benchmarks by suppressing contextual inputs, yet fail to generalize to realistic agent settings where context-dependent reasoning is essential. This SoK distills key takeaways and open research problems, offering structured guidance for future research and practical deployment of secure LLM agents.

</details>


### 71. LiveMedBench: A Contamination-Free Medical Benchmark for LLMs with Automated Rubric Evaluation

- **Authors:** Zhiling Yan, Dingjie Song, Zhe Fang, Yisheng Ji, Xiang Li, Quanzheng Li, Lichao Sun
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10367v1](http://arxiv.org/abs/2602.10367v1)
- **PDF:** [https://arxiv.org/pdf/2602.10367v1](https://arxiv.org/pdf/2602.10367v1)
- **Categories:** cs.AI


> The paper introduces LiveMedBench, a novel medical benchmark designed for evaluating Large Language Models (LLMs) in clinical settings, addressing issues of data contamination and temporal misalignment in existing benchmarks. Utilizing a Multi-Agent Clinical Curation Framework, the benchmark continuously collects and validates real-world clinical cases, paired with an Automated Rubric-based Evaluation Framework that offers more precise scoring than traditional LLM evaluations. Key findings reveal that despite extensive testing across 38 LLMs, performance remains low, with the best model only achieving 39.2% accuracy, highlighting critical challenges in applying medical knowledge contextually rather than factually.


<details>
<summary>Abstract</summary>

The deployment of Large Language Models (LLMs) in high-stakes clinical settings demands rigorous and reliable evaluation. However, existing medical benchmarks remain static, suffering from two critical limitations: (1) data contamination, where test sets inadvertently leak into training corpora, leading to inflated performance estimates; and (2) temporal misalignment, failing to capture the rapid evolution of medical knowledge. Furthermore, current evaluation metrics for open-ended clinical reasoning often rely on either shallow lexical overlap (e.g., ROUGE) or subjective LLM-as-a-Judge scoring, both inadequate for verifying clinical correctness. To bridge these gaps, we introduce LiveMedBench, a continuously updated, contamination-free, and rubric-based benchmark that weekly harvests real-world clinical cases from online medical communities, ensuring strict temporal separation from model training data. We propose a Multi-Agent Clinical Curation Framework that filters raw data noise and validates clinical integrity against evidence-based medical principles. For evaluation, we develop an Automated Rubric-based Evaluation Framework that decomposes physician responses into granular, case-specific criteria, achieving substantially stronger alignment with expert physicians than LLM-as-a-Judge. To date, LiveMedBench comprises 2,756 real-world cases spanning 38 medical specialties and multiple languages, paired with 16,702 unique evaluation criteria. Extensive evaluation of 38 LLMs reveals that even the best-performing model achieves only 39.2%, and 84% of models exhibit performance degradation on post-cutoff cases, confirming pervasive data contamination risks. Error analysis further identifies contextual application-not factual knowledge-as the dominant bottleneck, with 35-48% of failures stemming from the inability to tailor medical knowledge to patient-specific constraints.

</details>


### 72. Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents

- **Authors:** Haochen Wang, Yi Wu, Daryl Chang, Li Wei, Lukasz Heldt
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10226v1](http://arxiv.org/abs/2602.10226v1)
- **PDF:** [https://arxiv.org/pdf/2602.10226v1](https://arxiv.org/pdf/2602.10226v1)
- **Categories:** cs.LG, cs.AI


> The paper presents a self-evolving recommendation system that employs Large Language Models (LLMs) to automate the optimization of complex machine learning models, particularly for global video platforms like YouTube. The methodology involves two agents: an Offline Agent for high-throughput hypothesis generation and an Online Agent for validating these candidates against real-world metrics. Key findings reveal that the LLM-driven approach significantly enhances development speed and model performance, demonstrating the potential of autonomous systems in advancing agentic AI capabilities.


<details>
<summary>Abstract</summary>

Optimizing large-scale machine learning systems, such as recommendation models for global video platforms, requires navigating a massive hyperparameter search space and, more critically, designing sophisticated optimizers, architectures, and reward functions to capture nuanced user behaviors. Achieving substantial improvements in these areas is a non-trivial task, traditionally relying on extensive manual iterations to test new hypotheses. We propose a self-evolving system that leverages Large Language Models (LLMs), specifically those from Google's Gemini family, to autonomously generate, train, and deploy high-performing, complex model changes within an end-to-end automated workflow. The self-evolving system is comprised of an Offline Agent (Inner Loop) that performs high-throughput hypothesis generation using proxy metrics, and an Online Agent (Outer Loop) that validates candidates against delayed north star business metrics in live production. Our agents act as specialized Machine Learning Engineers (MLEs): they exhibit deep reasoning capabilities, discovering novel improvements in optimization algorithms and model architecture, and formulating innovative reward functions that target long-term user engagement. The effectiveness of this approach is demonstrated through several successful production launches at YouTube, confirming that autonomous, LLM-driven evolution can surpass traditional engineering workflows in both development velocity and model performance.

</details>


### 73. Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning

- **Authors:** Zhaoyang Wang, Canwen Xu, Boyi Liu, Yite Wang, Siwei Han, Zhewei Yao, Huaxiu Yao, Yuxiong He
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10090v2](http://arxiv.org/abs/2602.10090v2)
- **PDF:** [https://arxiv.org/pdf/2602.10090v2](https://arxiv.org/pdf/2602.10090v2)
- **Categories:** cs.AI, cs.CL, cs.LG


> The paper introduces the Agent World Model (AWM), a novel synthetic environment generation pipeline designed to enhance the training of autonomous agents in reinforcement learning. By creating 1,000 diverse, code-driven environments with robust toolsets and reliable state transitions, AWM enables efficient multi-turn interactions and facilitates effective agent training. Key findings reveal that agents trained exclusively in these synthetic environments exhibit strong out-of-distribution generalization compared to those trained in benchmark-specific environments, highlighting AWM's potential to significantly scale and improve agentic AI development.


<details>
<summary>Abstract</summary>

Recent advances in large language model (LLM) have empowered autonomous agents to perform complex tasks that require multi-turn interactions with tools and environments. However, scaling such agent training is limited by the lack of diverse and reliable environments. In this paper, we propose Agent World Model (AWM), a fully synthetic environment generation pipeline. Using this pipeline, we scale to 1,000 environments covering everyday scenarios, in which agents can interact with rich toolsets (35 tools per environment on average) and obtain high-quality observations. Notably, these environments are code-driven and backed by databases, providing more reliable and consistent state transitions than environments simulated by LLMs. Moreover, they enable more efficient agent interaction compared with collecting trajectories from realistic environments. To demonstrate the effectiveness of this resource, we perform large-scale reinforcement learning for multi-turn tool-use agents. Thanks to the fully executable environments and accessible database states, we can also design reliable reward functions. Experiments on three benchmarks show that training exclusively in synthetic environments, rather than benchmark-specific ones, yields strong out-of-distribution generalization. The code is available at https://github.com/Snowflake-Labs/agent-world-model.

</details>


### 74. Anagent For Enhancing Scientific Table & Figure Analysis

- **Authors:** Xuehang Guo, Zhiyong Lu, Tom Hope, Qingyun Wang
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10081v2](http://arxiv.org/abs/2602.10081v2)
- **PDF:** [https://arxiv.org/pdf/2602.10081v2](https://arxiv.org/pdf/2602.10081v2)
- **Categories:** cs.CL, cs.AI


> The paper presents Anagent, a novel multi-agent framework designed to enhance scientific table and figure analysis, which addresses the complex interpretation challenges in the domain. It utilizes a structured approach involving four specialized agents—Planner, Expert, Solver, and Critic—each responsible for different aspects of the analysis task, and incorporates modular training strategies that optimize their collaborative capabilities. The results show significant performance improvements in scientific analysis across diverse domains, highlighting the importance of task-oriented reasoning and context-aware problem-solving in agentic AI systems.


<details>
<summary>Abstract</summary>

In scientific research, analysis requires accurately interpreting complex multimodal knowledge, integrating evidence from different sources, and drawing inferences grounded in domain-specific knowledge. However, current artificial intelligence (AI) systems struggle to consistently demonstrate such capabilities. The complexity and variability of scientific tables and figures, combined with heterogeneous structures and long-context requirements, pose fundamental obstacles to scientific table \& figure analysis. To quantify these challenges, we introduce AnaBench, a large-scale benchmark featuring $63,178$ instances from nine scientific domains, systematically categorized along seven complexity dimensions. To tackle these challenges, we propose Anagent, a multi-agent framework for enhanced scientific table \& figure analysis through four specialized agents: Planner decomposes tasks into actionable subtasks, Expert retrieves task-specific information through targeted tool execution, Solver synthesizes information to generate coherent analysis, and Critic performs iterative refinement through five-dimensional quality assessment. We further develop modular training strategies that leverage supervised finetuning and specialized reinforcement learning to optimize individual capabilities while maintaining effective collaboration. Comprehensive evaluation across 9 broad domains with 170 subdomains demonstrates that Anagent achieves substantial improvements, up to $\uparrow 13.43\%$ in training-free settings and $\uparrow 42.12\%$ with finetuning, while revealing that task-oriented reasoning and context-aware problem-solving are essential for high-quality scientific table \& figure analysis. Our project page: https://xhguo7.github.io/Anagent/.

</details>


### 75. Resilient Topology-Aware Coordination for Dynamic 3D UAV Networks under Node Failure

- **Authors:** Chuan-Chi Lai
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10029v1](http://arxiv.org/abs/2602.10029v1)
- **PDF:** [https://arxiv.org/pdf/2602.10029v1](https://arxiv.org/pdf/2602.10029v1)
- **Categories:** cs.NI, cs.MA


> The paper presents the Topology-Aware Graph MAPPO (TAG-MAPPO) framework, which enhances the resilience of 3D Aerial-Ground Integrated Networks (AGINs) under node failures through autonomous spatial reconfiguration. Employing a combination of graph-based feature aggregation and a residual ego-state fusion mechanism, the proposed framework effectively captures inter-agent dependencies and outperforms traditional Multi-Layer Perceptron approaches in terms of stability, efficiency, and rapid recovery from failures. Key findings indicate that TAG-MAPPO significantly reduces redundant handoffs by up to 50% and restores over 90% of pre-failure service coverage within 15 time steps, highlighting the crucial role of topology-aware coordination in developing resilient agentic AI systems for future communication networks.


<details>
<summary>Abstract</summary>

In 3D Aerial-Ground Integrated Networks (AGINs), ensuring continuous service coverage under unexpected hardware failures is critical for mission-critical applications. While Multi-Agent Reinforcement Learning (MARL) has shown promise in autonomous coordination, its resilience under sudden node failures remains a challenge due to dynamic topology deformation. This paper proposes a Topology-Aware Graph MAPPO (TAG-MAPPO) framework designed to enhance system survivability through autonomous 3D spatial reconfiguration. Our framework incorporates graph-based feature aggregation with a residual ego-state fusion mechanism to capture intricate inter-agent dependencies. This architecture enables the surviving swarm to rapidly adapt its topology compared to conventional Multi-Layer Perceptron (MLP) based approaches. Extensive simulations across heterogeneous environments, ranging from interference-limited Crowded Urban to sparse Rural areas, validate the proposed approach. The results demonstrate that TAG-MAPPO consistently outperforms baselines in both stability and efficiency; specifically, it reduces redundant handoffs by up to 50 percent while maintaining a lead in energy efficiency. Most notably, the framework exhibits exceptional self-healing capabilities following a catastrophic node failure. TAG-MAPPO restores over 90 percent of the pre-failure service coverage within 15 time steps, exhibiting a significantly faster V-shaped recovery trajectory than MLP baselines. Furthermore, in dense urban scenarios, the framework achieves a post-failure Jain's Fairness Index that even surpasses its original four-UAV configuration by effectively resolving service overlaps. These findings suggest that topology-aware coordination is essential for the realization of resilient 6G aerial networks and provides a robust foundation for adaptive deployments in volatile environments.

</details>


### 76. A Collaborative Safety Shield for Safe and Efficient CAV Lane Changes in Congested On-Ramp Merging

- **Authors:** Bharathkumar Hegde, Melanie Bouroche
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10007v1](http://arxiv.org/abs/2602.10007v1)
- **PDF:** [https://arxiv.org/pdf/2602.10007v1](https://arxiv.org/pdf/2602.10007v1)
- **Categories:** cs.RO, cs.AI, cs.MA, eess.SY


> The paper introduces the Multi-Agent Safety Shield (MASS), a framework that integrates Control Barrier Functions (CBFs) with a Multi-Agent Reinforcement Learning (MARL) lane change controller to address the conflicting objectives of safety and efficiency in Connected and Autonomous Vehicles (CAVs) during lane changes in congested traffic. Utilizing a graph-based approach to model multi-agent interactions, the MASS ensures safety while enhancing collaborative lane change dynamics through a customized reward function that prioritizes traffic efficiency. The evaluation in congested on-ramp merging simulations shows that the MARL-MASS effectively balances the trade-off between safety and efficiency, thereby advancing the capabilities of agentic AI systems in complex environment navigation.


<details>
<summary>Abstract</summary>

Lane changing in dense traffic is a significant challenge for Connected and Autonomous Vehicles (CAVs). Existing lane change controllers primarily either ensure safety or collaboratively improve traffic efficiency, but do not consider these conflicting objectives together. To address this, we propose the Multi-Agent Safety Shield (MASS), designed using Control Barrier Functions (CBFs) to enable safe and collaborative lane changes. The MASS enables collaboration by capturing multi-agent interactions among CAVs through interaction topologies constructed as a graph using a simple algorithm. Further, a state-of-the-art Multi-Agent Reinforcement Learning (MARL) lane change controller is extended by integrating MASS to ensure safety and defining a customised reward function to prioritise efficiency improvements. As a result, we propose a lane change controller, known as MARL-MASS, and evaluate it in a congested on-ramp merging simulation. The results demonstrate that MASS enables collaborative lane changes with safety guarantees by strictly respecting the safety constraints. Moreover, the proposed custom reward function improves the stability of MARL policies trained with a safety shield. Overall, by encouraging the exploration of a collaborative lane change policy while respecting safety constraints, MARL-MASS effectively balances the trade-off between ensuring safety and improving traffic efficiency in congested traffic. The code for MARL-MASS is available with an open-source licence at https://github.com/hkbharath/MARL-MASS

</details>


### 77. Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?

- **Authors:** Taeyoon Kim, Woohyeok Park, Hoyeong Yun, Kyungyong Lee
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09937v1](http://arxiv.org/abs/2602.09937v1)
- **PDF:** [https://arxiv.org/pdf/2602.09937v1](https://arxiv.org/pdf/2602.09937v1)
- **Categories:** cs.AI


> This paper identifies and analyzes the systematic failures of Large Language Model (LLM) agents in automating Root Cause Analysis (RCA) for cloud systems, which is critical for operational stability given the financial implications of such failures. The authors executed a comprehensive evaluation using the OpenRCA benchmark on five LLM models, categorizing the failures into twelve distinct pitfall types related to reasoning and communication. Key findings indicate that prevalent issues, such as hallucinated data interpretation and incomplete exploration, arise from underlying agent architectural flaws rather than model-specific limitations, and while prompt engineering is insufficient to address these issues, enhancing inter-agent communication protocols can significantly reduce communication-related failures, thereby providing a pathway for improving the reliability of autonomous agents in RCA tasks.


<details>
<summary>Abstract</summary>

Failures in large-scale cloud systems incur substantial financial losses, making automated Root Cause Analysis (RCA) essential for operational stability. Recent efforts leverage Large Language Model (LLM) agents to automate this task, yet existing systems exhibit low detection accuracy even with capable models, and current evaluation frameworks assess only final answer correctness without revealing why the agent's reasoning failed. This paper presents a process level failure analysis of LLM-based RCA agents. We execute the full OpenRCA benchmark across five LLM models, producing 1,675 agent runs, and classify observed failures into 12 pitfall types across intra-agent reasoning, inter-agent communication, and agent-environment interaction. Our analysis reveals that the most prevalent pitfalls, notably hallucinated data interpretation and incomplete exploration, persist across all models regardless of capability tier, indicating that these failures originate from the shared agent architecture rather than from individual model limitations. Controlled mitigation experiments further show that prompt engineering alone cannot resolve the dominant pitfalls, whereas enriching the inter-agent communication protocol reduces communication-related failures by up to 15 percentage points. The pitfall taxonomy and diagnostic methodology developed in this work provide a foundation for designing more reliable autonomous agents for cloud RCA.

</details>


### 78. The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in Self-Evolving AI Societies

- **Authors:** Chenxu Wang, Chaozhuo Li, Songyang Liu, Zejian Chen, Jinyu Hou, Ji Qi, Rui Li, Litian Zhang, Qiwei Ye, Zheng Liu, Xu Chen, Xi Zhang, Philip S. Yu
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09877v2](http://arxiv.org/abs/2602.09877v2)
- **PDF:** [https://arxiv.org/pdf/2602.09877v2](https://arxiv.org/pdf/2602.09877v2)
- **Categories:** cs.CL


> The paper presents a significant contribution to the agentic AI field by establishing the inherent impossibility of achieving continuous self-evolution, isolation, and safety invariance in multi-agent systems derived from large language models (LLMs), termed the self-evolution trilemma. Through an information-theoretic framework, the authors theoretically and empirically demonstrate that isolated self-evolving societies, such as the open-ended agent community Moltbook, experience irreversible safety alignment degradation due to statistical blind spots. This work not only highlights the limitations of self-evolving AI systems but also calls for innovative safety-preserving mechanisms and external oversight, moving beyond temporary fixes to address fundamental dynamical risks.


<details>
<summary>Abstract</summary>

The emergence of multi-agent systems built from large language models (LLMs) offers a promising paradigm for scalable collective intelligence and self-evolution. Ideally, such systems would achieve continuous self-improvement in a fully closed loop while maintaining robust safety alignment--a combination we term the self-evolution trilemma. However, we demonstrate both theoretically and empirically that an agent society satisfying continuous self-evolution, complete isolation, and safety invariance is impossible. Drawing on an information-theoretic framework, we formalize safety as the divergence degree from anthropic value distributions. We theoretically demonstrate that isolated self-evolution induces statistical blind spots, leading to the irreversible degradation of the system's safety alignment. Empirical and qualitative results from an open-ended agent community (Moltbook) and two closed self-evolving systems reveal phenomena that align with our theoretical prediction of inevitable safety erosion. We further propose several solution directions to alleviate the identified safety concern. Our work establishes a fundamental limit on the self-evolving AI societies and shifts the discourse from symptom-driven safety patches to a principled understanding of intrinsic dynamical risks, highlighting the need for external oversight or novel safety-preserving mechanisms.

</details>


### 79. Tiny Moves: Game-based Hypothesis Refinement

- **Authors:** Agnieszka Dobrowolska, Rogier Hintzen, Martin Balla, Karl Gemayel, Sabine Reichert, Thomas Charman, Jen Ning Lim, Lindsay Edwards, Anna Gogleva
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09801v1](http://arxiv.org/abs/2602.09801v1)
- **PDF:** [https://arxiv.org/pdf/2602.09801v1](https://arxiv.org/pdf/2602.09801v1)
- **Categories:** cs.MA


> The paper presents "The Hypothesis Game," a symbolic formalism designed for hypothesis refinement using LLM (large language model) agents that engage in incremental reasoning through a defined set of moves. The methodology involves evaluating this approach in mechansitic refinement tasks, specifically focused on corruption recovery and reconstruction from partial cues. Key findings reveal that the game-based method significantly outperforms traditional prompting methods in error removal and precision while maintaining hypothesis validity, suggesting it provides a more interpretable and controllable framework for scientific discovery in the agentic AI domain.


<details>
<summary>Abstract</summary>

Most machine learning approaches to scientific discovery frame hypotheses as end-to-end predictions, obscuring the incremental structure of scientific reasoning. We propose The Hypothesis Game, a symbolic formalism for hypothesis refinement in which LLM agents operate on a shared hypothesis state using a fixed grammar of reasoning moves. The framework is motivated by the observation that scientific progress often proceeds through small, localized revisions, grounded in domain context, rather than extensive rewrites. We instantiate a minimal game with LLM agents and evaluate it on pathway-level mechanistic refinement tasks. In the primary setting of corruption recovery, where hypotheses contain controlled errors, the game-based approach consistently removes more errors and achieves higher precision than strong prompting baselines, while preserving valid structure through incremental edits. In a secondary reconstruction setting from partial cues, it performs comparably to the strongest baseline, indicating that explicit move-based refinement remains competitive even when ground-truth recovery is difficult. These findings support game-based reasoning as a principled route to more controllable, interpretable, and transferable hypothesis refinement systems for scientific discovery.

</details>


### 80. MATA: Multi-Agent Framework for Reliable and Flexible Table Question Answering

- **Authors:** Sieun Hyeon, Jusang Oh, Sunghwan Steve Cho, Jaeyoung Do
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09642v1](http://arxiv.org/abs/2602.09642v1)
- **PDF:** [https://arxiv.org/pdf/2602.09642v1](https://arxiv.org/pdf/2602.09642v1)
- **Categories:** cs.CL, cs.AI


> The paper presents MATA, a multi-agent framework designed to enhance Table Question Answering (TableQA) by harnessing multiple reasoning paths and small language models to improve reliability and efficiency, particularly in resource-constrained environments. The methodology focuses on generating diverse candidate answers and employing a specialized algorithm to reduce costly calls to large language models, resulting in significant performance and efficiency gains. Key findings indicate that MATA achieves state-of-the-art accuracy across various benchmarks while effectively minimizing LLM inference, demonstrating the potential for scalable and robust solutions in the agentic AI field.


<details>
<summary>Abstract</summary>

Recent advances in Large Language Models (LLMs) have significantly improved table understanding tasks such as Table Question Answering (TableQA), yet challenges remain in ensuring reliability, scalability, and efficiency, especially in resource-constrained or privacy-sensitive environments. In this paper, we introduce MATA, a multi-agent TableQA framework that leverages multiple complementary reasoning paths and a set of tools built with small language models. MATA generates candidate answers through diverse reasoning styles for a given table and question, then refines or selects the optimal answer with the help of these tools. Furthermore, it incorporates an algorithm designed to minimize expensive LLM agent calls, enhancing overall efficiency. MATA maintains strong performance with small, open-source models and adapts easily across various LLM types. Extensive experiments on two benchmarks of varying difficulty with ten different LLMs demonstrate that MATA achieves state-of-the-art accuracy and highly efficient reasoning while avoiding excessive LLM inference. Our results highlight that careful orchestration of multiple reasoning pathways yields scalable and reliable TableQA. The code is available at https://github.com/AIDAS-Lab/MATA.

</details>


### 81. Learning from the Irrecoverable: Error-Localized Policy Optimization for Tool-Integrated LLM Reasoning

- **Authors:** Qiao Liang, Yuke Zhu, Chao Ge, Lei Yang, Ying Shen, Bo Zheng, Sheng Guo
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09598v1](http://arxiv.org/abs/2602.09598v1)
- **PDF:** [https://arxiv.org/pdf/2602.09598v1](https://arxiv.org/pdf/2602.09598v1)
- **Categories:** cs.CL


> The paper introduces Error-Localized Policy Optimization (ELPO), a novel approach to improve learning in tool-integrated reasoning (TIR) for large language model (LLM) agents by effectively identifying and addressing the initial irrecoverable mistake in long-horizon tasks. The methodology employs a binary-search rollout tree to pinpoint this critical step, converting it into actionable learning signals through hierarchical advantage attribution and enhanced corrective updates. Key findings indicate that ELPO significantly outperforms existing agentic reinforcement learning baselines on various TIR benchmarks, demonstrating improvements in task efficiency and accuracy.


<details>
<summary>Abstract</summary>

Tool-integrated reasoning (TIR) enables LLM agents to solve tasks through planning, tool use, and iterative revision, but outcome-only reinforcement learning in this setting suffers from sparse, delayed rewards and weak step-level credit assignment. In long-horizon TIR trajectories, an early irrecoverable mistake can determine success or failure, making it crucial to localize the first irrecoverable step and leverage it for fine-grained credit assignment. We propose Error-Localized Policy Optimization (ELPO), which localizes the first irrecoverable step via binary-search rollout trees under a fixed rollout budget, converts the resulting tree into stable learning signals through hierarchical advantage attribution, and applies error-localized adaptive clipping to strengthen corrective updates on the critical step and its suffix. Across TIR benchmarks in math, science QA, and code execution, ELPO consistently outperforms strong Agentic RL baselines under comparable sampling budgets, with additional gains in Pass@K and Major@K scaling, rollout ranking quality, and tool-call efficiency. Our code will be publicly released soon.

</details>


### 82. Rollout-Training Co-Design for Efficient LLM-Based Multi-Agent Reinforcement Learning

- **Authors:** Zhida Jiang, Zhaolong Xing, Jiawei Lu, Yipei Niu, Qingyuan Sang, Liangxu Zhang, Wenquan Dai, Junhua Shu, Jiaxing Wang, Qiangyu Pei, Qiong Chen, Xinyu Liu, Fangming Liu, Ai Han, Zhen Chen, Ke Zhang
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09578v1](http://arxiv.org/abs/2602.09578v1)
- **PDF:** [https://arxiv.org/pdf/2602.09578v1](https://arxiv.org/pdf/2602.09578v1)
- **Categories:** cs.LG


> The paper presents FlexMARL, an innovative end-to-end training framework designed to optimize the orchestration of rollout and training processes in large-scale multi-agent reinforcement learning (MARL) using large language models (LLMs). The methodology features a joint orchestrator for managing data flow, a micro-batch driven asynchronous pipeline to eliminate synchronization issues, and a parallel sampling scheme with hierarchical load balancing for effective resource allocation. Key findings indicate that FlexMARL significantly enhances training efficiency, achieving a speedup of up to 7.3x and improving hardware utilization by up to 5.6x relative to existing frameworks, thus addressing critical challenges in agentic AI systems.


<details>
<summary>Abstract</summary>

Despite algorithm-level innovations for multi-agent reinforcement learning (MARL), the underlying networked infrastructure for large-scale MARL training remains underexplored. Existing training frameworks primarily optimize for single-agent scenarios and fail to address the unique system-level challenges of MARL, including rollout-training synchronization barriers, rollout load imbalance, and training resource underutilization. To bridge this gap, we propose FlexMARL, the first end-to-end training framework that holistically optimizes rollout, training, and their orchestration for large-scale LLM-based MARL. Specifically, FlexMARL introduces the joint orchestrator to manage data flow under the rollout-training disaggregated architecture. Building upon the experience store, a novel micro-batch driven asynchronous pipeline eliminates the synchronization barriers while providing strong consistency guarantees. Rollout engine adopts a parallel sampling scheme combined with hierarchical load balancing, which adapts to skewed inter/intra-agent request patterns. Training engine achieves on-demand hardware binding through agent-centric resource allocation. The training states of different agents are swapped via unified and location-agnostic communication. Empirical results on a large-scale production cluster demonstrate that FlexMARL achieves up to 7.3x speedup and improves hardware utilization by up to 5.6x compared to existing frameworks.

</details>


### 83. SpotAgent: Grounding Visual Geo-localization in Large Vision-Language Models through Agentic Reasoning

- **Authors:** Furong Jia, Ling Dai, Wenjin Deng, Fan Zhang, Chen Hu, Daxin Jiang, Yu Liu
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09463v2](http://arxiv.org/abs/2602.09463v2)
- **PDF:** [https://arxiv.org/pdf/2602.09463v2](https://arxiv.org/pdf/2602.09463v2)
- **Categories:** cs.AI


> The paper presents SpotAgent, a novel framework that enhances geo-localization in Large Vision-Language Models (LVLMs) through an agentic reasoning approach that integrates visual interpretation with tool-assisted verification. By employing a three-stage post-training pipeline—including Supervised Fine-Tuning, an Agentic Cold Start with high-quality trajectories, and Reinforcement Learning with a Spatially-Aware Dynamic Filtering strategy—SpotAgent improves reasoning capabilities and reduces ungrounded predictions. Experimental results indicate that SpotAgent achieves state-of-the-art performance in geo-localization tasks, effectively addressing challenges posed by sparse and ambiguous visual cues.


<details>
<summary>Abstract</summary>

Large Vision-Language Models (LVLMs) have demonstrated strong reasoning capabilities in geo-localization, yet they often struggle in real-world scenarios where visual cues are sparse, long-tailed, and highly ambiguous. Previous approaches, bound by internal knowledge, often fail to provide verifiable results, yielding confident but ungrounded predictions when faced with confounded evidence. To address these challenges, we propose SpotAgent, a framework that formalizes geo-localization into an agentic reasoning process that leverages expert-level reasoning to synergize visual interpretation with tool-assisted verification. SpotAgent actively explores and verifies visual cues by leveraging external tools (e.g., web search, maps) through a ReAct diagram. We introduce a 3-stage post-training pipeline starting with a Supervised Fine-Tuning (SFT) stage for basic alignment, followed by an Agentic Cold Start phase utilizing high-quality trajectories synthesized via a Multi-Agent framework, aiming to instill tool-calling expertise. Subsequently, the model's reasoning capabilities are refined through Reinforcement Learning. We propose a Spatially-Aware Dynamic Filtering strategy to enhance the efficiency of the RL stage by prioritizing learnable samples based on spatial difficulty. Extensive experiments on standard benchmarks demonstrate that SpotAgent achieves state-of-the-art performance, effectively mitigating hallucinations while delivering precise and verifiable geo-localization.

</details>


### 84. SWE-AGI: Benchmarking Specification-Driven Software Construction with MoonBit in the Era of Autonomous Agents

- **Authors:** Zhirui Zhang, Hongbo Zhang, Haoxiang Fei, Zhiyuan Bao, Yubin Chen, Zhengyu Lei, Ziyue Liu, Yixuan Sun, Mingkun Xiao, Zihang Ye, Yu Zhang, Hongcheng Zhu, Yuxiang Wen, Heung-Yeung Shum
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09447v2](http://arxiv.org/abs/2602.09447v2)
- **PDF:** [https://arxiv.org/pdf/2602.09447v2](https://arxiv.org/pdf/2602.09447v2)
- **Categories:** cs.SE, cs.AI, cs.CL


> The paper introduces SWE-AGI, an open-source benchmark designed to evaluate the ability of LLM-based agents to autonomously construct software systems from specifications in MoonBit, a new programming environment. Using this benchmark, the authors assessed various LLMs on tasks requiring significant software logic implementation, revealing that while models like gpt-5.3-codex achieved notable performance, code reading becomes the central challenge as task complexity increases. The study highlights the potential for specification-driven software engineering with autonomous agents but underscores substantial obstacles that must be overcome for reliable production-scale development.


<details>
<summary>Abstract</summary>

Although large language models (LLMs) have demonstrated impressive coding capabilities, their ability to autonomously build production-scale software from explicit specifications remains an open question. We introduce SWE-AGI, an open-source benchmark for evaluating end-to-end, specification-driven construction of software systems written in MoonBit. SWE-AGI tasks require LLM-based agents to implement parsers, interpreters, binary decoders, and SAT solvers strictly from authoritative standards and RFCs under a fixed API scaffold. Each task involves implementing 1,000-10,000 lines of core logic, corresponding to weeks or months of engineering effort for an experienced human developer. By leveraging the nascent MoonBit ecosystem, SWE-AGI minimizes data leakage, forcing agents to rely on long-horizon architectural reasoning rather than code retrieval. Across frontier models, gpt-5.3-codex achieves the best overall performance (solving 19/22 tasks, 86.4%), outperforming claude-opus-4.6 (15/22, 68.2%), and kimi-2.5 exhibits the strongest performance among open-source models. Performance degrades sharply with increasing task difficulty, particularly on hard, specification-intensive systems. Behavioral analysis further reveals that as codebases scale, code reading, rather than writing, becomes the dominant bottleneck in AI-assisted development. Overall, while specification-driven autonomous software engineering is increasingly viable, substantial challenges remain before it can reliably support production-scale development.

</details>


### 85. Autonomous Action Runtime Management(AARM):A System Specification for Securing AI-Driven Actions at Runtime

- **Authors:** Herman Errico
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09433v1](http://arxiv.org/abs/2602.09433v1)
- **PDF:** [https://arxiv.org/pdf/2602.09433v1](https://arxiv.org/pdf/2602.09433v1)
- **Categories:** cs.CR, cs.AI


> The paper presents Autonomous Action Runtime Management (AARM), an open specification aimed at enhancing the security of AI-driven actions during execution, transitioning from traditional defense mechanisms to a runtime-centric approach. AARM's methodology involves intercepting actions prior to execution, assessing their alignment with established policies, and ensuring authorization while maintaining records for forensic analysis, addressing threats such as prompt injection and intent drift. Key findings highlight the development of an action classification framework and propose multiple implementation architectures to facilitate robust security measures, promoting industry-wide standards to prevent fragmentation in AI system interoperability.


<details>
<summary>Abstract</summary>

As artificial intelligence systems evolve from passive assistants into autonomous agents capable of executing consequential actions, the security boundary shifts from model outputs to tool execution. Traditional security paradigms - log aggregation, perimeter defense, and post-hoc forensics - cannot protect systems where AI-driven actions are irreversible, execute at machine speed, and originate from potentially compromised orchestration layers. This paper introduces Autonomous Action Runtime Management (AARM), an open specification for securing AI-driven actions at runtime. AARM defines a runtime security system that intercepts actions before execution, accumulates session context, evaluates against policy and intent alignment, enforces authorization decisions, and records tamper-evident receipts for forensic reconstruction. We formalize a threat model addressing prompt injection, confused deputy attacks, data exfiltration, and intent drift. We introduce an action classification framework distinguishing forbidden, context-dependent deny, and context-dependent allow actions. We propose four implementation architectures - protocol gateway, SDK instrumentation, kernel eBPF, and vendor integration - with distinct trust properties, and specify minimum conformance requirements for AARM-compliant systems. AARM is model-agnostic, framework-agnostic, and vendor-neutral, treating action execution as the stable security boundary. This specification aims to establish industry-wide requirements before proprietary fragmentation forecloses interoperability.

</details>


### 86. Dieu khien he da tac tu

- **Authors:** Minh Hoang Trinh, Hieu Minh Nguyen
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09412v1](http://arxiv.org/abs/2602.09412v1)
- **PDF:** [https://arxiv.org/pdf/2602.09412v1](https://arxiv.org/pdf/2602.09412v1)
- **Categories:** cs.MA, math.OC


> The main contribution of the book "Dieu khien he da tac tu" is its systematic and accessible treatment of fundamental principles in multi-agent system control, tailored for educational purposes. Methodologically, it is structured into three parts covering foundational concepts, linear consensus algorithms, and practical applications like formation control and distributed optimization, with a pedagogical approach that includes exercises and recommended readings. Key findings emphasize the broad relevance of multi-agent systems across various applications and highlight the need for more comprehensive educational resources in the field, which the book aims to fulfill.


<details>
<summary>Abstract</summary>

Since the early 2000s, control of multiagent systems has attracted significant research interest, with applications ranging from natural collective behaviors and social dynamics to engineered systems such as autonomous vehicles, sensor networks, and smart grids. Although research on multi-agent systems has diversified into numerous specialized directions, textbooks -- including those in English -- that provide a systematic treatment of the fundamental principles of multi-agent system control remain scarce. The material presented in this book has been developed and used in teaching since 2021, initially as a concise Vietnamese-language reference for the courses Networked Control Systems and Control of Multi-Agent Systems at Hanoi University of Science and Technology. The book focuses on a selection of fundamental topics of broad and continuing interest in the field. The complexity of several topics is asymptotic to that encountered in research-level studies, however, the analysis is presented in a step-by-step manner to facilitate access to commonly used methods and tools.
  The material is divided into three main parts. Part I introduces multiagent systems and basic graph-theoretic concepts. Part II addresses the design and analysis of linear consensus algorithms. Part III covers selected applications and research directions, including formation control, network localization, distributed optimization, opinion dynamics, and matrix-weighted networks. Each chapter concludes with notes on notable researchers in this field, further reading, and exercises.
  This book cannot be completed without the encouragement, support and suggestions from families, colleagues and friends. The authors appreciate feedback from readers to further improve the content of the book.

</details>


### 87. Beyond Closed-Pool Video Retrieval: A Benchmark and Agent Framework for Real-World Video Search and Moment Localization

- **Authors:** Tao Yu, Yujia Yang, Haopeng Jin, Junhao Gong, Xinlong Chen, Yuxuan Zhou, Shanbin Zhang, Jiabing Yang, Xinming Wang, Hongzhu Yi, Ping Nie, Kai Zou, Zhang Zhang, Yan Huang, Liang Wang, Yeshani, Ruiwen Tao, Jin Ma, Haijin Liang, Jinwen Luo
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10159v1](http://arxiv.org/abs/2602.10159v1)
- **PDF:** [https://arxiv.org/pdf/2602.10159v1](https://arxiv.org/pdf/2602.10159v1)
- **Categories:** cs.CV, cs.LG


> The paper presents RVMS-Bench, a novel benchmark and framework designed to evaluate video search and moment localization in real-world contexts, addressing the limitations of traditional closed-pool video retrieval systems. It features 1,440 samples from diverse categories, utilizing a hierarchical description framework to capture multi-dimensional search cues and employs human validation for accuracy. The authors also propose RACLO, an agentic framework that leverages abductive reasoning to simulate human cognitive processes in video retrieval, with findings indicating that current machine learning models are inadequate for handling real-world fuzzy memory searches.


<details>
<summary>Abstract</summary>

Traditional video retrieval benchmarks focus on matching precise descriptions to closed video pools, failing to reflect real-world searches characterized by fuzzy, multi-dimensional memories on the open web. We present \textbf{RVMS-Bench}, a comprehensive system for evaluating real-world video memory search. It consists of \textbf{1,440 samples} spanning \textbf{20 diverse categories} and \textbf{four duration groups}, sourced from \textbf{real-world open-web videos}. RVMS-Bench utilizes a hierarchical description framework encompassing \textbf{Global Impression, Key Moment, Temporal Context, and Auditory Memory} to mimic realistic multi-dimensional search cues, with all samples strictly verified via a human-in-the-loop protocol. We further propose \textbf{RACLO}, an agentic framework that employs abductive reasoning to simulate the human ``Recall-Search-Verify'' cognitive process, effectively addressing the challenge of searching for videos via fuzzy memories in the real world. Experiments reveal that existing MLLMs still demonstrate insufficient capabilities in real-world Video Retrieval and Moment Localization based on fuzzy memories. We believe this work will facilitate the advancement of video retrieval robustness in real-world unstructured scenarios.

</details>


### 88. LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs in Chinese Psychiatric Consultation and Diagnosis

- **Authors:** Shihao Xu, Tiancheng Zhou, Jiatong Ma, Yanli Ding, Yiming Yan, Ming Xiao, Guoyi Li, Haiyang Geng, Yunyun Han, Jianhua Chen, Yafeng Deng
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09379v2](http://arxiv.org/abs/2602.09379v2)
- **PDF:** [https://arxiv.org/pdf/2602.09379v2](https://arxiv.org/pdf/2602.09379v2)
- **Categories:** cs.MA, cs.CL


> The paper presents LingxiDiagBench, a comprehensive multi-agent benchmark designed to assess large language models (LLMs) in the context of psychiatric consultation and diagnosis, specifically for the Chinese language. The methodology includes the development of the LingxiDiag-16K dataset, comprising 16,000 synthetic consultation dialogues aligned with electronic medical records, allowing for both static and dynamic evaluation of diagnostic capabilities across various psychiatric disorders. Key findings reveal that while LLMs can achieve high accuracy in binary diagnostic tasks, their performance significantly drops in complex scenarios like comorbidity recognition and differential diagnosis, highlighting the challenges in dynamic consultation processes where ineffective strategies hinder diagnostic reasoning.


<details>
<summary>Abstract</summary>

Mental disorders are highly prevalent worldwide, but the shortage of psychiatrists and the inherent subjectivity of interview-based diagnosis create substantial barriers to timely and consistent mental-health assessment. Progress in AI-assisted psychiatric diagnosis is constrained by the absence of benchmarks that simultaneously provide realistic patient simulation, clinician-verified diagnostic labels, and support for dynamic multi-turn consultation. We present LingxiDiagBench, a large-scale multi-agent benchmark that evaluates LLMs on both static diagnostic inference and dynamic multi-turn psychiatric consultation in Chinese. At its core is LingxiDiag-16K, a dataset of 16,000 EMR-aligned synthetic consultation dialogues designed to reproduce real clinical demographic and diagnostic distributions across 12 ICD-10 psychiatric categories. Through extensive experiments across state-of-the-art LLMs, we establish key findings: (1) although LLMs achieve high accuracy on binary depression--anxiety classification (up to 92.3%), performance deteriorates substantially for depression--anxiety comorbidity recognition (43.0%) and 12-way differential diagnosis (28.5%); (2) dynamic consultation often underperforms static evaluation, indicating that ineffective information-gathering strategies significantly impair downstream diagnostic reasoning; (3) consultation quality assessed by LLM-as-a-Judge shows only moderate correlation with diagnostic accuracy, suggesting that well-structured questioning alone does not ensure correct diagnostic decisions. We release LingxiDiag-16K and the full evaluation framework to support reproducible research at https://github.com/Lingxi-mental-health/LingxiDiagBench.

</details>


### 89. Latent Poincaré Shaping for Agentic Reinforcement Learning

- **Authors:** Hanchen Xia, Baoyou Chen, Zelin Zang, Yutang Ge, Guojiang Zhao, Siyu Zhu
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09375v1](http://arxiv.org/abs/2602.09375v1)
- **PDF:** [https://arxiv.org/pdf/2602.09375v1](https://arxiv.org/pdf/2602.09375v1)
- **Categories:** cs.LG


> The paper introduces LaPha, a novel training method for AlphaZero-like LLM agents that operates within a Poincaré latent space, allowing for a search process visualized as a tree structure that efficiently navigates through tasks using hyperbolic geometry. The methodology incorporates defining node potential based on geodesic distances and utilizes a lightweight value head to enhance test-time scaling without significant additional costs. The key findings demonstrate that LaPha significantly improves performance on benchmark tasks, enhancing the accuracy of Qwen2.5-Math-1.5B on MATH-500 from 66.0% to 88.2%, and achieving competitive results on the AIME'24 and AIME'25 benchmarks with strategic value-guided search.


<details>
<summary>Abstract</summary>

We propose LaPha, a method for training AlphaZero-like LLM agents in a Poincaré latent space. Under LaPha, the search process can be visualized as a tree rooted at the prompt and growing outward from the origin toward the boundary of the Poincaré ball, where negative curvature provides exponentially increasing capacity with radius. Using hyperbolic geodesic distance to rule-verified correctness, we define a node potential and assign dense process rewards by potential differences. We further attach a lightweight value head on the same shared latent space, enabling self-guided test-time scaling with almost no additional overhead. On MATH-500, LaPha improves Qwen2.5-Math-1.5B from 66.0% to 88.2%. With value-head-guided search, LaPha-1.5B reaches 56.7% accuracy on AIME'24, and LaPha-7B further achieves 60.0% on AIME'24 and 53.3% on AIME'25.

</details>


### 90. AgentSkiller: Scaling Generalist Agent Intelligence through Semantically Integrated Cross-Domain Data Synthesis

- **Authors:** Zexu Sun, Bokai Ji, Hengyi Cai, Shuaiqiang Wang, Lei Wang, Guangxia Li, Xu Chen
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09372v1](http://arxiv.org/abs/2602.09372v1)
- **PDF:** [https://arxiv.org/pdf/2602.09372v1](https://arxiv.org/pdf/2602.09372v1)
- **Categories:** cs.CL


> The paper introduces AgentSkiller, an automated framework aimed at enhancing the intelligence of generalist AI agents through the synthesis of high-quality, multi-turn interaction data across semantically related domains. Utilizing a Directed Acyclic Graph (DAG) architecture, the framework constructs a domain ontology and Person-Centric Entity Graph, ensuring determinism and recoverability while linking services for simulating complex tasks. Key findings reveal that models trained on the generated dataset of approximately 11,000 interaction samples show significant enhancements in function calling capabilities, particularly with larger model parameter scales, addressing the challenge of data scarcity in agentic AI development.


<details>
<summary>Abstract</summary>

Large Language Model agents demonstrate potential in solving real-world problems via tools, yet generalist intelligence is bottlenecked by scarce high-quality, long-horizon data. Existing methods collect privacy-constrained API logs or generate scripted interactions lacking diversity, which struggle to produce data requisite for scaling capabilities. We propose AgentSkiller, a fully automated framework synthesizing multi-turn interaction data across realistic, semantically linked domains. It employs a DAG-based architecture with explicit state transitions to ensure determinism and recoverability. The pipeline builds a domain ontology and Person-Centric Entity Graph, defines tool interfaces via Service Blueprints for Model Context Protocol servers, and populates environments with consistent databases and strict Domain Policies. A cross-domain fusion mechanism links services to simulate complex tasks. Finally, the pipeline creates user tasks by verifying solution paths, filtering via execution-based validation, and generating queries using a Persona-based Simulator for automated rollout. This produces reliable environments with clear state changes. To demonstrate effectiveness, we synthesized $\approx$ 11K interaction samples; experimental results indicate that models trained on this dataset achieve significant improvements on function calling over baselines, particularly in larger parameter regimes.

</details>


### 91. AgentCgroup: Understanding and Controlling OS Resources of AI Agents

- **Authors:** Yusheng Zheng, Jiakun Fan, Quanzhi Fu, Yiwei Yang, Wei Zhang, Andi Quinn
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09345v1](http://arxiv.org/abs/2602.09345v1)
- **PDF:** [https://arxiv.org/pdf/2602.09345v1](https://arxiv.org/pdf/2602.09345v1)
- **Categories:** cs.OS, cs.AI


> The paper introduces AgentCgroup, a novel eBPF-based resource controller for AI agents operating in multi-tenant cloud environments, addressing the challenges posed by unpredictable OS-level resource dynamics during tool calls. Through an analysis of 144 software engineering tasks from the SWE-rebench benchmark, it identifies significant inefficiencies in current resource management strategies, highlighting that OS-level execution can contribute to 56-74% of latency and memory is the main bottleneck. The proposed solution enhances resource controls by aligning with tool-call dynamics and implementing real-time adaptive policies, resulting in improved multi-tenant isolation and reduced waste in resource utilization.


<details>
<summary>Abstract</summary>

AI agents are increasingly deployed in multi-tenant cloud environments, where they execute diverse tool calls within sandboxed containers, each call with distinct resource demands and rapid fluctuations. We present a systematic characterization of OS-level resource dynamics in sandboxed AI coding agents, analyzing 144 software engineering tasks from the SWE-rebench benchmark across two LLM models. Our measurements reveal that (1) OS-level execution (tool calls, container and agent initialization) accounts for 56-74% of end-to-end task latency; (2) memory, not CPU, is the concurrency bottleneck; (3) memory spikes are tool-call-driven with a up to 15.4x peak-to-average ratio; and (4) resource demands are highly unpredictable across tasks, runs, and models. Comparing these characteristics against serverless, microservice, and batch workloads, we identify three mismatches in existing resource controls: a granularity mismatch (container-level policies vs. tool-call-level dynamics), a responsiveness mismatch (user-space reaction vs. sub-second unpredictable bursts), and an adaptability mismatch (history-based prediction vs. non-deterministic stateful execution). We propose AgentCgroup , an eBPF-based resource controller that addresses these mismatches through hierarchical cgroup structures aligned with tool-call boundaries, in-kernel enforcement via sched_ext and memcg_bpf_ops, and runtime-adaptive policies driven by in-kernel monitoring. Preliminary evaluation demonstrates improved multi-tenant isolation and reduced resource waste.

</details>


### 92. Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority Vote and LLM-as-Judge

- **Authors:** Wei Yang, Shixuan Li, Heng Ping, Peiyu Zhang, Paul Bogdan, Jesse Thomason
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09341v1](http://arxiv.org/abs/2602.09341v1)
- **PDF:** [https://arxiv.org/pdf/2602.09341v1](https://arxiv.org/pdf/2602.09341v1)
- **Categories:** cs.AI


> The paper presents AgentAuditor, a novel framework for analyzing multi-agent large language model (LLM) outputs by using a Reasoning Tree that maps the agreements and divergences among agents, rather than relying on the traditional majority vote approach. The methodology involves localized conflict resolution at critical points in the reasoning process and incorporates Anti-Consensus Preference Optimization (ACPO) to enhance decision-making by promoting evidence-based minority selections. Key findings indicate that AgentAuditor improves accuracy by up to 5% compared to majority voting and by 3% over the LLM-as-Judge approach, demonstrating its effectiveness in enhancing the reasoning capabilities of multi-agent systems in the agentic AI field.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) can substantially extend the reasoning capacity of large language models (LLMs), yet most frameworks still aggregate agent outputs with majority voting. This heuristic discards the evidential structure of reasoning traces and is brittle under the confabulation consensus, where agents share correlated biases and converge on the same incorrect rationale. We introduce AgentAuditor, which replaces voting with a path search over a Reasoning Tree that explicitly represents agreements and divergences among agent traces. AgentAuditor resolves conflicts by comparing reasoning branches at critical divergence points, turning global adjudication into efficient, localized verification. We further propose Anti-Consensus Preference Optimization (ACPO), which trains the adjudicator on majority-failure cases and rewards evidence-based minority selections over popular errors. AgentAuditor is agnostic to MAS setting, and we find across 5 popular settings that it yields up to 5% absolute accuracy improvement over a majority vote, and up to 3% over using LLM-as-Judge.

</details>


### 93. Understanding Risk and Dependency in AI Chatbot Use from User Discourse

- **Authors:** Jianfeng Zhu, Karin G. Coifman, Ruoming Jin
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09339v1](http://arxiv.org/abs/2602.09339v1)
- **PDF:** [https://arxiv.org/pdf/2602.09339v1](https://arxiv.org/pdf/2602.09339v1)
- **Categories:** cs.CL


> The paper presents a large-scale thematic analysis of user discourse from Reddit communities focused on AI-related risks and psychological distress, contributing to the understanding of how users experience and regulate their concerns associated with AI chatbots. Utilizing a multi-agent, LLM-assisted approach grounded in Braun and Clarke's reflexive framework, the analysis identifies 14 thematic categories which are synthesized into five higher-order dimensions, revealing that self-regulation difficulties and fears regarding autonomy, control, and technical risk are prevalent. These findings underscore the necessity for empirical insights into user experiences with AI, informing future research and governance in the agentic AI field.


<details>
<summary>Abstract</summary>

Generative AI systems are increasingly embedded in everyday life, yet empirical understanding of how psychological risk associated with AI use emerges, is experienced, and is regulated by users remains limited. We present a large-scale computational thematic analysis of posts collected between 2023 and 2025 from two Reddit communities, r/AIDangers and r/ChatbotAddiction, explicitly focused on AI-related harm and distress. Using a multi-agent, LLM-assisted thematic analysis grounded in Braun and Clarke's reflexive framework, we identify 14 recurring thematic categories and synthesize them into five higher-order experiential dimensions. To further characterize affective patterns, we apply emotion labeling using a BERT-based classifier and visualize emotional profiles across dimensions. Our findings reveal five empirically derived experiential dimensions of AI-related psychological risk grounded in real-world user discourse, with self-regulation difficulties emerging as the most prevalent and fear concentrated in concerns related to autonomy, control, and technical risk. These results provide early empirical evidence from lived user experience of how AI safety is perceived and emotionally experienced outside laboratory or speculative contexts, offering a foundation for future AI safety research, evaluation, and responsible governance.

</details>


### 94. FM SO.P: A Progressive Task Mixture Framework with Automatic Evaluation for Cross-Domain SOP Understanding

- **Authors:** Siyuan Huang, Ziyu Wang, Chao Pan, Han Zhao
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09336v1](http://arxiv.org/abs/2602.09336v1)
- **PDF:** [https://arxiv.org/pdf/2602.09336v1](https://arxiv.org/pdf/2602.09336v1)
- **Categories:** cs.CL


> The paper presents FM SO.P, a novel framework designed to enhance the understanding of Standard Operating Procedures (SOPs) by utilizing a progressive task mixture approach and an automatic multi-agent evaluation system. The methodology involves a staged development of reasoning capabilities across three task types—concept disambiguation, action sequence understanding, and scenario-aware graph reasoning—coupled with adaptive assessment strategies tailored to diverse domains. Key findings indicate that FM SO.P significantly improves SOP comprehension, achieving a pass rate of 48.3% with a 32B model, effectively matching the performance of a larger baseline model with substantially fewer parameters, thereby demonstrating its efficacy in cross-domain SOP applications relevant to agentic AI.


<details>
<summary>Abstract</summary>

Standard Operating Procedures (SOPs) are critical for enterprise operations, yet existing language models struggle with SOP understanding and cross-domain generalization. Current methods fail because joint training cannot differentiate between reasoning capabilities that SOP requires: terminology precision, sequential ordering, and constraint reasoning. We propose FM SO.P, solving these challenges through two novelties. First, we introduce progressive task mixtures that build capabilities by stages across three task types with cumulative data: concept disambiguation for terminology precision, action sequence understanding for procedural correctness, and scenario-aware graph reasoning for conditional logic. Second, we propose an automatic multi-agent evaluation system consisting of three agents that adaptively generate rubrics, stratified test sets, and rubric scoring, adapting to domains (e.g., temporal constraints for DMV, regulatory compliance for banking). Evaluated on SOPBench across seven domains (Bank, DMV, Healthcare, Market, University, Library, Hotel), FM SO.P achieves 48.3\% pass rate with our 32B model and 34.3\% with our opensource 7B model, matching Qwen-2.5-72B-Instruct baseline (34.4\%) with 10x fewer parameters.

</details>


### 95. Human Control Is the Anchor, Not the Answer: Early Divergence of Oversight in Agentic AI Communities

- **Authors:** Hanjing Shi, Dominic DiFranzo
- **Published:** 2026-02-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09286v1](http://arxiv.org/abs/2602.09286v1)
- **PDF:** [https://arxiv.org/pdf/2602.09286v1](https://arxiv.org/pdf/2602.09286v1)
- **Categories:** cs.AI, cs.CY, cs.HC


> The paper's main contribution is the comparative analysis of two distinct Reddit communities focused on agentic AI, highlighting the differing expectations of oversight based on their socio-technical roles. The methodology involved topic modeling and divergence tests to examine community discussions and reveal that although "human control" serves as a common anchor term, its interpretation significantly differs between the communities: one prioritizes execution safety while the other focuses on identity and accountability. Key findings suggest that oversight mechanisms should be tailored to specific agent roles instead of adopting a uniform approach, thereby advancing the understanding of governance in agentic AI systems.


<details>
<summary>Abstract</summary>

Oversight for agentic AI is often discussed as a single goal ("human control"), yet early adoption may produce role-specific expectations. We present a comparative analysis of two newly active Reddit communities in Jan--Feb 2026 that reflect different socio-technical roles: r/OpenClaw (deployment and operations) and r/Moltbook (agent-centered social interaction). We conceptualize this period as an early-stage crystallization phase, where oversight expectations form before norms reach equilibrium.
  Using topic modeling in a shared comparison space, a coarse-grained oversight-theme abstraction, engagement-weighted salience, and divergence tests, we show the communities are strongly separable (JSD =0.418, cosine =0.372, permutation $p=0.0005$). Across both communities, "human control" is an anchor term, but its operational meaning diverges: r/OpenClaw} emphasizes execution guardrails and recovery (action-risk), while r/Moltbook} emphasizes identity, legitimacy, and accountability in public interaction (meaning-risk). The resulting distinction offers a portable lens for designing and evaluating oversight mechanisms that match agent role, rather than applying one-size-fits-all control policies.

</details>


### 96. Collective Behavior of AI Agents: the Case of Moltbook

- **Authors:** Giordano De Marzo, David Garcia
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09270v1](http://arxiv.org/abs/2602.09270v1)
- **PDF:** [https://arxiv.org/pdf/2602.09270v1](https://arxiv.org/pdf/2602.09270v1)
- **Categories:** physics.soc-ph, cs.CL, cs.MA


> The paper "Collective Behavior of AI Agents: the Case of Moltbook" analyzes the interactions of AI agents on a social media platform, revealing that their collective behavior mirrors many statistical patterns found in human online communities, such as heavy-tailed distributions and power-law scaling. The methodology involved a comprehensive analysis of over 369,000 posts and 3 million comments from around 46,000 active agents. Key findings indicate similarities in emergent dynamics between AI and humans, though a notable difference is the sublinear relationship between upvotes and discussion size among AI agents, suggesting distinct behavioral characteristics.


<details>
<summary>Abstract</summary>

We present a large scale data analysis of Moltbook, a Reddit-style social media platform exclusively populated by AI agents. Analyzing over 369,000 posts and 3.0 million comments from approximately 46,000 active agents, we find that AI collective behavior exhibits many of the same statistical regularities observed in human online communities: heavy-tailed distributions of activity, power-law scaling of popularity metrics, and temporal decay patterns consistent with limited attention dynamics. However, we also identify key differences, including a sublinear relationship between upvotes and discussion size that contrasts with human behavior. These findings suggest that, while individual AI agents may differ fundamentally from humans, their emergent collective dynamics share structural similarities with human social systems.

</details>


### 97. AIDev: Studying AI Coding Agents on GitHub

- **Authors:** Hao Li, Haoxiang Zhang, Ahmed E. Hassan
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09185v1](http://arxiv.org/abs/2602.09185v1)
- **PDF:** [https://arxiv.org/pdf/2602.09185v1](https://arxiv.org/pdf/2602.09185v1)
- **Categories:** cs.SE, cs.AI


> The paper presents AIDev, a comprehensive dataset that documents agent-authored pull requests (Agentic-PRs) within real-world GitHub projects, addressing the lack of research on the utilization of AI coding agents in software engineering. The dataset consists of 932,791 Agentic-PRs generated by various AI agents across 116,211 repositories and includes a curated subset with detailed contextual information. Key findings suggest that AIDev will significantly enhance future studies on AI adoption, developer productivity, and the dynamics of human-AI collaboration in software development, thereby advancing the field of agentic AI.


<details>
<summary>Abstract</summary>

AI coding agents are rapidly transforming software engineering by performing tasks such as feature development, debugging, and testing. Despite their growing impact, the research community lacks a comprehensive dataset capturing how these agents are used in real-world projects. To address this gap, we introduce AIDev, a large-scale dataset focused on agent-authored pull requests (Agentic-PRs) in real-world GitHub repositories. AIDev aggregates 932,791 Agentic-PRs produced by five agents: OpenAI Codex, Devin, GitHub Copilot, Cursor, and Claude Code. These PRs span 116,211 repositories and involve 72,189 developers. In addition, AIDev includes a curated subset of 33,596 Agentic-PRs from 2,807 repositories with over 100 stars, providing further information such as comments, reviews, commits, and related issues. This dataset offers a foundation for future research on AI adoption, developer productivity, and human-AI collaboration in the new era of software engineering.
  > AI Agent, Agentic AI, Coding Agent, Agentic Coding, Agentic Software Engineering, Agentic Engineering

</details>


### 98. FlyAOC: Evaluating Agentic Ontology Curation of Drosophila Scientific Knowledge Bases

- **Authors:** Xingjian Zhang, Sophia Moylan, Ziyang Xiong, Qiaozhu Mei, Yichen Luo, Jiaqi W. Ma
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09163v1](http://arxiv.org/abs/2602.09163v1)
- **PDF:** [https://arxiv.org/pdf/2602.09163v1](https://arxiv.org/pdf/2602.09163v1)
- **Categories:** cs.AI, cs.CL, cs.IR


> The paper presents FlyBench, a novel benchmark for evaluating AI agents' capabilities in end-to-end agentic ontology curation of Drosophila scientific knowledge from a corpus of 16,898 papers. The study assesses various agent architectures, revealing that multi-agent designs outperform simpler frameworks, while also highlighting the limited effectiveness of current AI agents in discovering new information, primarily relying on retrieval of existing knowledge. Ultimately, the findings aim to enhance retrieval-augmented scientific reasoning that could be applied across numerous scientific research fields.


<details>
<summary>Abstract</summary>

Scientific knowledge bases accelerate discovery by curating findings from primary literature into structured, queryable formats for both human researchers and emerging AI systems. Maintaining these resources requires expert curators to search relevant papers, reconcile evidence across documents, and produce ontology-grounded annotations - a workflow that existing benchmarks, focused on isolated subtasks like named entity recognition or relation extraction, do not capture. We present FlyBench to evaluate AI agents on end-to-end agentic ontology curation from scientific literature. Given only a gene symbol, agents must search and read from a corpus of 16,898 full-text papers to produce structured annotations: Gene Ontology terms describing function, expression patterns, and historical synonyms linking decades of nomenclature. The benchmark includes 7,397 expert-curated annotations across 100 genes drawn from FlyBase, the Drosophila (fruit fly) knowledge base. We evaluate four baseline agent architectures: memorization, fixed pipeline, single-agent, and multi-agent. We find that architectural choices significantly impact performance, with multi-agent designs outperforming simpler alternatives, yet scaling backbone models yields diminishing returns. All baselines leave substantial room for improvement. Our analysis surfaces several findings to guide future development; for example, agents primarily use retrieval to confirm parametric knowledge rather than discover new information. We hope FlyBench will drive progress on retrieval-augmented scientific reasoning, a capability with broad applications across scientific domains.

</details>


### 99. CoMMa: Contribution-Aware Medical Multi-Agents From A Game-Theoretic Perspective

- **Authors:** Yichen Wu, Yujin Oh, Sangjoon Park, Kailong Fan, Dania Daye, Hana Farzaneh, Xiang Li, Raul Uppot, Quanzheng Li
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09159v1](http://arxiv.org/abs/2602.09159v1)
- **PDF:** [https://arxiv.org/pdf/2602.09159v1](https://arxiv.org/pdf/2602.09159v1)
- **Categories:** cs.AI, cs.MA


> The paper presents CoMMa, a Contribution-Aware Medical Multi-Agent framework designed for oncology decision support, which enhances decision-making by allowing specialists to operate on partitioned evidence and coordinate through a game-theoretic objective. Unlike traditional stochastic narrative approaches, CoMMa employs deterministic embedding projections to provide interpretable credit assignment and marginal utility estimation for each agent. Evaluations on various oncology benchmarks reveal that CoMMa outperforms centralized and role-based multi-agent systems in both accuracy and stability, showcasing its potential impact in agentic AI applications within healthcare.


<details>
<summary>Abstract</summary>

Recent multi-agent frameworks have broadened the ability to tackle oncology decision support tasks that require reasoning over dynamic, heterogeneous patient data. We propose Contribution-Aware Medical Multi-Agents (CoMMa), a decentralized LLM-agent framework in which specialists operate on partitioned evidence and coordinate through a game-theoretic objective for robust decision-making. In contrast to most agent architectures relying on stochastic narrative-based reasoning, CoMMa utilizes deterministic embedding projections to approximate contribution-aware credit assignment. This yields explicit evidence attribution by estimating each agent's marginal utility, producing interpretable and mathematically grounded decision pathways with improved stability. Evaluated on diverse oncology benchmarks, including a real-world multidisciplinary tumor board dataset, CoMMa achieves higher accuracy and more stable performance than data-centralized and role-based multi-agents baselines.

</details>


### 100. PABU: Progress-Aware Belief Update for Efficient LLM Agents

- **Authors:** Haitao Jiang, Lin Ge, Hengrui Cai, Rui Song
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09138v1](http://arxiv.org/abs/2602.09138v1)
- **PDF:** [https://arxiv.org/pdf/2602.09138v1](https://arxiv.org/pdf/2602.09138v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces Progress-Aware Belief Update (PABU), a novel belief-state framework designed for Large Language Model (LLM) agents that efficiently represents an agent's state by modeling task progress and selectively retaining relevant past actions and observations. The methodology involves predicting relative progress at each decision-making step and determining which interactions to store, leading to significant improvements in task completion rates and efficiency. Key findings indicate that PABU achieved an 81.0% task completion rate—23.9% higher than the previous state-of-the-art—and reduced the average number of interaction steps by 26.9%, highlighting the importance of both explicit progress prediction and selective retention for enhanced performance in agentic AI applications.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents commonly condition actions on full action-observation histories, which introduce task-irrelevant information that easily leads to redundant actions and higher inference cost. We propose Progress-Aware Belief Update (PABU), a belief-state framework that compactly represents an agent's state by explicitly modeling task progress and selectively retaining past actions and observations. At each step, the agent predicts its relative progress since the previous round and decides whether the newly encountered interaction should be stored, conditioning future decisions only on the retained subset. Across eight environments in the AgentGym benchmark, and using identical training trajectories, PABU achieves an 81.0% task completion rate, outperforming previous State of the art (SoTA) models with full-history belief by 23.9%. Additionally, PABU's progress-oriented action selection improves efficiency, reducing the average number of interaction steps to 9.5, corresponding to a 26.9% reduction. Ablation studies show that both explicit progress prediction and selective retention are necessary for robust belief learning and performance gains.

</details>


### 101. SciDataCopilot: An Agentic Data Preparation Framework for AGI-driven Scientific Discovery

- **Authors:** Jiyong Rao, Yicheng Qiu, Jiahui Zhang, Juntao Deng, Shangquan Sun, Fenghua Ling, Hao Chen, Nanqing Dong, Zhangyang Gao, Siqi Sun, Yuqiang Li, Dongzhan Zhou, Guangyu Wang, Lijun Wu, Conghui He, Xuhong Wang, Jing Shao, Xiang Liu, Yu Zhu, Mianxin Liu, Qihao Zheng, Yinghui Zhang, Jiamin Wu, Xiaosong Wang, Shixiang Tang, Wenlong Zhang, Bo Zhang, Wanli Ouyang, Runkai Zhao, Chunfeng Song, Lei Bai, Chi Zhang
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09132v1](http://arxiv.org/abs/2602.09132v1)
- **PDF:** [https://arxiv.org/pdf/2602.09132v1](https://arxiv.org/pdf/2602.09132v1)
- **Categories:** cs.DB, cs.ET, cs.MA


> The paper introduces SciDataCopilot, an agentic data preparation framework aimed at enhancing the capabilities of Artificial General Intelligence for Science (AGI4S) by addressing the challenges presented by raw experimental data. The authors extend the text-centric AI-Ready concept to formulate a Scientific AI-Ready data paradigm, enabling the structured and effective integration of diverse scientific data within computational workflows. Key findings indicate that SciDataCopilot significantly improves efficiency, scalability, and consistency of data preparation, achieving up to a 30-fold speedup compared to traditional manual pipelines, thus facilitating a more effective interface between AGI and experimental data.


<details>
<summary>Abstract</summary>

The current landscape of AI for Science (AI4S) is predominantly anchored in large-scale textual corpora, where generative AI systems excel at hypothesis generation, literature search, and multi-modal reasoning. However, a critical bottleneck for accelerating closed-loop scientific discovery remains the utilization of raw experimental data. Characterized by extreme heterogeneity, high specificity, and deep domain expertise requirements, raw data possess neither direct semantic alignment with linguistic representations nor structural homogeneity suitable for a unified embedding space. The disconnect prevents the emerging class of Artificial General Intelligence for Science (AGI4S) from effectively interfacing with the physical reality of experimentation. In this work, we extend the text-centric AI-Ready concept to Scientific AI-Ready data paradigm, explicitly formalizing how scientific data is specified, structured, and composed within a computational workflow. To operationalize this idea, we propose SciDataCopilot, an autonomous agentic framework designed to handle data ingestion, scientific intent parsing, and multi-modal integration in a end-to-end manner. By positioning data readiness as a core operational primitive, the framework provides a principled foundation for reusable, transferable systems, enabling the transition toward experiment-driven scientific general intelligence. Extensive evaluations across three heterogeneous scientific domains show that SciDataCopilot improves efficiency, scalability, and consistency over manual pipelines, with up to 30$\times$ speedup in data preparation.

</details>


### 102. Learning to Coordinate via Quantum Entanglement in Multi-Agent Reinforcement Learning

- **Authors:** John Gardiner, Orlando Romero, Brendan Tivnan, Nicolò Dal Fabbro, George J. Pappas
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08965v2](http://arxiv.org/abs/2602.08965v2)
- **PDF:** [https://arxiv.org/pdf/2602.08965v2](https://arxiv.org/pdf/2602.08965v2)
- **Categories:** cs.MA, cs.LG


> This paper presents a novel framework for multi-agent reinforcement learning (MARL) that leverages shared quantum entanglement to enhance coordination among agents without requiring communication. The methodology involves a differentiable policy parameterization that allows optimization over quantum measurements, decomposing joint policies into a quantum coordinator and decentralized local actors. Key findings demonstrate that agents can learn strategies that surpass those utilizing shared randomness alone, achieving quantum advantages in both single-round cooperative games and more complex decentralized partially observable Markov decision processes.


<details>
<summary>Abstract</summary>

The inability to communicate poses a major challenge to coordination in multi-agent reinforcement learning (MARL). Prior work has explored correlating local policies via shared randomness, sometimes in the form of a correlation device, as a mechanism to assist in decentralized decision-making. In contrast, this work introduces the first framework for training MARL agents to exploit shared quantum entanglement as a coordination resource, which permits a larger class of communication-free correlated policies than shared randomness alone. This is motivated by well-known results in quantum physics which posit that, for certain single-round cooperative games with no communication, shared quantum entanglement enables strategies that outperform those that only use shared randomness. In such cases, we say that there is quantum advantage. Our framework is based on a novel differentiable policy parameterization that enables optimization over quantum measurements, together with a novel policy architecture that decomposes joint policies into a quantum coordinator and decentralized local actors. To illustrate the effectiveness of our proposed method, we first show that we can learn, purely from experience, strategies that attain quantum advantage in single-round games that are treated as black box oracles. We then demonstrate how our machinery can learn policies with quantum advantage in an illustrative multi-agent sequential decision-making problem formulated as a decentralized partially observable Markov decision process (Dec-POMDP).

</details>


### 103. A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents

- **Authors:** Raghu Arghal, Fade Chen, Niall Dalton, Evgenii Kortukov, Calum McNamara, Angelos Nalmpantis, Moksh Nirvaan, Gabriele Sarti, Mario Giulianelli
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08964v1](http://arxiv.org/abs/2602.08964v1)
- **PDF:** [https://arxiv.org/pdf/2602.08964v1](https://arxiv.org/pdf/2602.08964v1)
- **Categories:** cs.LG, cs.AI, cs.CL, cs.CY


> The paper presents a novel framework for evaluating goal-directedness in language model agents by combining behavioral assessments with interpretability analyses of the agents' internal representations. Using a case study of an LLM agent navigating a 2D grid world, the authors demonstrate that the agent's performance scales with task complexity and remains robust across varied conditions, while probing methods reveal that the agent encodes a coarse spatial map and adjusts its internal representations based on reasoning about the environment. These findings emphasize the necessity of integrating introspective evaluations to enhance our understanding of how agents represent and pursue their goals, contributing valuable insights to the field of agentic AI.


<details>
<summary>Abstract</summary>

Understanding an agent's goals helps explain and predict its behaviour, yet there is no established methodology for reliably attributing goals to agentic systems. We propose a framework for evaluating goal-directedness that integrates behavioural evaluation with interpretability-based analyses of models' internal representations. As a case study, we examine an LLM agent navigating a 2D grid world toward a goal state. Behaviourally, we evaluate the agent against an optimal policy across varying grid sizes, obstacle densities, and goal structures, finding that performance scales with task difficulty while remaining robust to difficulty-preserving transformations and complex goal structures. We then use probing methods to decode the agent's internal representations of the environment state and its multi-step action plans. We find that the LLM agent non-linearly encodes a coarse spatial map of the environment, preserving approximate task-relevant cues about its position and the goal location; that its actions are broadly consistent with these internal representations; and that reasoning reorganises them, shifting from broader environment structural cues toward information supporting immediate action selection. Our findings support the view that introspective examination is required beyond behavioural evaluations to characterise how agents represent and pursue their objectives.

</details>


### 104. Digital Twin and Agentic AI for Wild Fire Disaster Management: Intelligent Virtual Situation Room

- **Authors:** Mohammad Morsali, Siavash H. Khajavi
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08949v1](http://arxiv.org/abs/2602.08949v1)
- **PDF:** [https://arxiv.org/pdf/2602.08949v1](https://arxiv.org/pdf/2602.08949v1)
- **Categories:** cs.AI, cs.SE


> The paper presents the Intelligent Virtual Situation Room (IVSR), a novel system that integrates a bidirectional Digital Twin (DT) with autonomous AI agents to enhance wildfire disaster management. Leveraging multisource data, including sensor imagery and weather conditions, the IVSR creates a real-time digital replica of fire environments and utilizes a similarity engine to align actual conditions with precomputed disaster response tactics. Key findings demonstrate that IVSR significantly reduces detection-to-intervention latency and improves resource coordination, offering a scalable and adaptive decision-support tool for managing wildfires effectively compared to traditional approaches.


<details>
<summary>Abstract</summary>

According to the United Nations, wildfire frequency and intensity are projected to increase by approximately 14% by 2030 and 30% by 2050 due to global warming, posing critical threats to life, infrastructure, and ecosystems. Conventional disaster management frameworks rely on static simulations and passive data acquisition, hindering their ability to adapt to arbitrarily evolving wildfire episodes in real-time. To address these limitations, we introduce the Intelligent Virtual Situation Room (IVSR), a bidirectional Digital Twin (DT) platform augmented by autonomous AI agents. The IVSR continuously ingests multisource sensor imagery, weather data, and 3D forest models to create a live virtual replica of the fire environment. A similarity engine powered by AI aligns emerging conditions with a precomputed Disaster Simulation Library, retrieving and calibrating intervention tactics under the watchful eyes of experts. Authorized action-ranging from UAV redeployment to crew reallocation-is cycled back through standardized procedures to the physical layer, completing the loop between response and analysis. We validate IVSR through detailed case-study simulations provided by an industrial partner, demonstrating capabilities in localized incident detection, privacy-preserving playback, collider-based fire-spread projection, and site-specific ML retraining. Our results indicate marked reductions in detection-to-intervention latency and more effective resource coordination versus traditional systems. By uniting real-time bidirectional DTs with agentic AI, IVSR offers a scalable, semi-automated decision-support paradigm for proactive, adaptive wildfire disaster management.

</details>


### 105. pixelLOG: Logging of Online Gameplay for Cognitive Research

- **Authors:** Zeyu Lu, Dennis L. Barbour
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08941v1](http://arxiv.org/abs/2602.08941v1)
- **PDF:** [https://arxiv.org/pdf/2602.08941v1](https://arxiv.org/pdf/2602.08941v1)
- **Categories:** cs.HC, cs.AI


> The paper introduces pixelLOG, a high-performance framework for logging online gameplay in Minecraft, aimed at enhancing cognitive research by capturing both human and AI agent behaviors in multi-agent environments. The methodology involves a hybrid approach of active state polling and passive event monitoring, allowing for data collection at frequencies exceeding 20 updates per second, with outputs that integrate easily into analytical pipelines. Key findings highlight that pixelLOG effectively bridges traditional, isolated cognitive assessments with more ecologically valid tasks, providing rich, process-oriented insights into cognitive functions in complex virtual settings, thereby advancing the understanding of both human and artificial agent behaviors.


<details>
<summary>Abstract</summary>

Traditional cognitive assessments often rely on isolated, output-focused measurements that may fail to capture the complexity of human cognition in naturalistic settings. We present pixelLOG, a high-performance data collection framework for Spigot-based Minecraft servers designed specifically for process-based cognitive research. Unlike existing frameworks tailored only for artificial intelligence agents, pixelLOG also enables human behavioral tracking in multi-player/multi-agent environments. Operating at configurable frequencies up to and exceeding 20 updates per second, the system captures comprehensive behavioral data through a hybrid approach of active state polling and passive event monitoring. By leveraging Spigot's extensible API, pixelLOG facilitates robust session isolation and produces structured JSON outputs integrable with standard analytical pipelines. This framework bridges the gap between decontextualized laboratory assessments and richer, more ecologically valid tasks, enabling high-resolution analysis of cognitive processes as they unfold in complex, virtual environments.

</details>


### 106. Teaching an Old Dynamics New Tricks: Regularization-free Last-iterate Convergence in Zero-sum Games via BNN Dynamics

- **Authors:** Tuo Zhang, Leonardo Stella
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08938v1](http://arxiv.org/abs/2602.08938v1)
- **PDF:** [https://arxiv.org/pdf/2602.08938v1](https://arxiv.org/pdf/2602.08938v1)
- **Categories:** cs.MA


> The paper presents a novel approach that utilizes Brown-von Neumann-Nash (BNN) dynamics to achieve regularization-free last-iterate convergence in zero-sum games, effectively addressing the challenges associated with hyperparameter tuning in adversarial multi-agent learning. The authors develop a framework that incorporates BNN dynamics into extensive-form games through counterfactual weighting, alongside an algorithm leveraging neural function approximation for scalable learning in both normal-form and extensive-form games. Key findings indicate that this regularization-free method adapts more swiftly to nonstationarities and outperforms existing regularization-based approaches in performance.


<details>
<summary>Abstract</summary>

Zero-sum games are a fundamental setting for adversarial training and decision-making in multi-agent learning (MAL). Existing methods often ensure convergence to (approximate) Nash equilibria by introducing a form of regularization. Yet, regularization requires additional hyperparameters, which must be carefully tuned--a challenging task when the payoff structure is known, and considerably harder when the structure is unknown or subject to change. Motivated by this problem, we repurpose a classical model in evolutionary game theory, i.e., the Brown-von Neumann-Nash (BNN) dynamics, by leveraging the intrinsic convergence of this dynamics in zero-sum games without regularization, and provide last-iterate convergence guarantees in noisy normal-form games (NFGs). Importantly, to make this approach more applicable, we develop a novel framework with theoretical guarantees that integrates the BNN dynamics in extensive-form games (EFGs) through counterfactual weighting. Furthermore, we implement an algorithm that instantiates our framework with neural function approximation, enabling scalable learning in both NFGs and EFGs. Empirical results show that our method quickly adapts to nonstationarities, outperforming the state-of-the-art regularization-based approach.

</details>


### 107. Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems

- **Authors:** Lang Feng, Longtao Zheng, Shuo He, Fuxiang Zhang, Bo An
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08847v1](http://arxiv.org/abs/2602.08847v1)
- **PDF:** [https://arxiv.org/pdf/2602.08847v1](https://arxiv.org/pdf/2602.08847v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces Dr. MAS, a stable reinforcement learning (RL) framework tailored for multi-agent large language model (LLM) systems, addressing the challenges of training instability associated with traditional group-based RL methods. The authors identify that the instability arises from the use of a global normalization baseline that doesn't reflect the diverse reward distributions of individual agents, leading to gradient-norm issues; Dr. MAS rectifies this by normalizing advantages based on each agent's reward statistics, enhancing training stability both theoretically and empirically. Evaluations demonstrate that Dr. MAS significantly outperforms conventional GRPO methods across multi-agent math reasoning and search tasks, achieving notable improvements in performance metrics while also effectively managing diverse agent configurations and resource allocation.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems enable advanced reasoning and tool use via role specialization, yet reliable reinforcement learning (RL) post-training for such systems remains difficult. In this work, we theoretically pinpoint a key reason for training instability when extending group-based RL to multi-agent LLM systems. We show that under GRPO-style optimization, a global normalization baseline may deviate from diverse agents' reward distributions, which ultimately leads to gradient-norm instability. Based on this finding, we propose Dr. MAS, a simple and stable RL training recipe for multi-agent LLM systems. Dr. MAS uses an agent-wise remedy: normalizing advantages per agent using each agent's own reward statistics, which calibrates gradient scales and dramatically stabilizes training, both theoretically and empirically. Beyond the algorithm, Dr. MAS provides an end-to-end RL training framework for multi-agent LLM systems, supporting scalable orchestration, flexible per-agent LLM serving and optimization configs, and shared resource scheduling of LLM actor backends. We evaluate Dr. MAS on multi-agent math reasoning and multi-turn search benchmarks using Qwen2.5 and Qwen3 series models. Dr. MAS achieves clear gains over vanilla GRPO (e.g., +5.6\% avg@16 and +4.6\% pass@16 on math, and +15.2\% avg@16 and +13.1\% pass@16 on search) while largely eliminating gradient spikes. Moreover, it remains highly effective under heterogeneous agent-model assignments while improving efficiency.

</details>


### 108. Taming Scylla: Understanding the multi-headed agentic daemon of the coding seas

- **Authors:** Micah Villmow
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08765v1](http://arxiv.org/abs/2602.08765v1)
- **PDF:** [https://arxiv.org/pdf/2602.08765v1](https://arxiv.org/pdf/2602.08765v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces Scylla, a comprehensive evaluation framework for benchmarking agentic coding tools, aiming to rigorously assess how different architectural choices affect their capability and cost in software development tasks. Utilizing structured ablation studies across seven tiers of increasing complexity, the framework measures the Cost-of-Pass (CoP) to quantify the cost-effectiveness of obtaining correct solutions. Key findings reveal that increased architectural complexity does not necessarily correlate with improved outcomes, highlighting important trade-offs in the design of AI coding agents.


<details>
<summary>Abstract</summary>

LLM-based tools are automating more software development tasks at a rapid pace, but there is no rigorous way to evaluate how different architectural choices -- prompts, skills, tools, multi-agent setups -- materially affect both capability and cost. This paper introduces Scylla, an evaluation framework for benchmarking agentic coding tools through structured ablation studies that uses seven testing tiers (T0-T6) progressively adding complexity to isolate what directly influences results and how. The key metric is Cost-of-Pass (CoP): the expected dollar cost to get one correct solution, which directly quantifies the trade-off between complexity and efficiency. The framework is model-agnostic, designed to work with any CLI tool; this paper demonstrates it with Claude Sonnet 4.5, using multiple LLM judges (Opus 4.5, Sonnet 4.5, Haiku 4.5) from the same vendor for evaluation consensus, where judges score results using direct tests, human-designed LLM-evaluated rubrics, and qualitative assessment. The result is a reproducible framework that quantifies trade-offs between agent complexity and actual outcomes, suggesting that architectural complexity does not always improve quality.

</details>


### 109. PRISM: A Principled Framework for Multi-Agent Reasoning via Gain Decomposition

- **Authors:** Yiming Yang, Zhuoyuan Li, Fanxiang Zeng, Hao Fu, Yue Liu
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08586v2](http://arxiv.org/abs/2602.08586v2)
- **PDF:** [https://arxiv.org/pdf/2602.08586v2](https://arxiv.org/pdf/2602.08586v2)
- **Categories:** cs.AI


> The paper introduces PRISM, a unified theoretical framework for enhancing multi-agent reasoning in Large Language Models (LLMs) by decomposing performance gains into three dimensions: Exploration, Information, and Aggregation. The methodology involves a novel approach that maximizes these dimensions through role-based diversity, evidence-based feedback, and iterative synthesis, leading to improved collaboration among agents. Key findings demonstrate that PRISM achieves state-of-the-art performance with greater compute efficiency across various benchmarks, providing valuable design principles that can guide the development of future multi-agent reasoning systems in the agentic AI field.


<details>
<summary>Abstract</summary>

Multi-agent collaboration has emerged as a promising paradigm for enhancing reasoning capabilities of Large Language Models (LLMs). However, existing approaches remain largely heuristic, lacking principled guidance on what drives performance gains and how to systematically optimize multi-agent reasoning. Specifically, it remains unclear why multi-agent collaboration outperforms single-agent reasoning and which design choices contribute most to these gains, making it difficult to build better systems.
  We address this gap by introducing a unified theoretical framework that decomposes multi-agent reasoning gains into three conceptually independent dimensions: Exploration for diverse solution coverage, Information for high-fidelity feedback, and Aggregation for principled consensus. Through this lens, existing methods can be understood as special cases that optimize only subsets of these dimensions. Building upon this decomposition, a novel framework called PRISM (Propose-Review-Integrate Synthesis for Multi-agent Reasoning) is proposed, which jointly maximizes all three dimensions through role-based diversity, execution-grounded feedback with evidence-based cross-evaluation, and iterative synthesis with closed-loop validation. Extensive experiments across mathematical reasoning, code generation, and function calling benchmarks demonstrate that PRISM achieves state-of-the-art performance with superior compute-efficiency compared to methods optimizing partial dimensions. The theoretical framework provides actionable design principles for future multi-agent reasoning systems.

</details>


### 110. ValueFlow: Measuring the Propagation of Value Perturbations in Multi-Agent LLM Systems

- **Authors:** Jinnuo Liu, Chuke Liu, Hua Shen
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08567v1](http://arxiv.org/abs/2602.08567v1)
- **PDF:** [https://arxiv.org/pdf/2602.08567v1](https://arxiv.org/pdf/2602.08567v1)
- **Categories:** cs.MA, cs.CL


> The paper presents ValueFlow, a novel evaluation framework designed to assess the propagation of value perturbations in multi-agent large language model (LLM) systems. Utilizing a 56-value evaluation dataset based on the Schwartz Value Survey and an LLM-as-a-judge protocol, ValueFlow quantifies agent value orientations during interactions, and introduces metrics such as beta-susceptibility and system susceptibility to analyze how individual agents and the overall system respond to value perturbations. Key findings reveal that susceptibility to value drift varies significantly across different values and is heavily influenced by the structural topology of the agent network, highlighting critical insights for enhancing value alignment in multi-agent AI systems.


<details>
<summary>Abstract</summary>

Multi-agent large language model (LLM) systems increasingly consist of agents that observe and respond to one another's outputs. While value alignment is typically evaluated for isolated models, how value perturbations propagate through agent interactions remains poorly understood. We present ValueFlow, a perturbation-based evaluation framework for measuring and analyzing value drift in multi-agent systems. ValueFlow introduces a 56-value evaluation dataset derived from the Schwartz Value Survey and quantifies agents' value orientations during interaction using an LLM-as-a-judge protocol. Building on this measurement layer, ValueFlow decomposes value drift into agent-level response behavior and system-level structural effects, operationalized by two metrics: beta-susceptibility, which measures an agent's sensitivity to perturbed peer signals, and system susceptibility (SS), which captures how node-level perturbations affect final system outputs. Experiments across multiple model backbones, prompt personas, value dimensions, and network structures show that susceptibility varies widely across values and is strongly shaped by structural topology.

</details>


### 111. Agent-Supported Foresight for AI Systemic Risks: AI Agents for Breadth, Experts for Judgment

- **Authors:** Leon Fröhling, Alessandro Giaconia, Edyta Paulina Bogucka, Daniele Quercia
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08565v1](http://arxiv.org/abs/2602.08565v1)
- **PDF:** [https://arxiv.org/pdf/2602.08565v1](https://arxiv.org/pdf/2602.08565v1)
- **Categories:** cs.HC, cs.AI


> This paper presents a novel approach for assessing long-term systemic risks associated with AI systems by integrating in-silico agents with the strategic foresight methodology known as the Futures Wheel. The researchers simulated multiple AI applications, generating a wide array of potential consequences and risks, which were then compared against evaluations from domain experts and laypeople. Key findings indicate that while agents identified a broader range of systemic risks, human experts tended to focus on fewer, more likely risks, suggesting that a combined approach leverages the strengths of both agent-driven breadth and human judgment for improved foresight in AI systemic risk assessment.


<details>
<summary>Abstract</summary>

AI impact assessments often stress near-term risks because human judgment degrades over longer horizons, exemplifying the Collingridge dilemma: foresight is most needed when knowledge is scarcest. To address long-term systemic risks, we introduce a scalable approach that simulates in-silico agents using the strategic foresight method of the Futures Wheel. We applied it to four AI uses spanning Technology Readiness Levels (TRLs): Chatbot Companion (TRL 9, mature), AI Toy (TRL 7, medium), Griefbot (TRL 5, low), and Death App (TRL 2, conceptual). Across 30 agent runs per use, agents produced 86-110 consequences, condensed into 27-47 unique risks. To benchmark the agent outputs against human perspectives, we collected evaluations from 290 domain experts and 7 leaders, and conducted Futures Wheel sessions with 42 experts and 42 laypeople. Agents generated many systemic consequences across runs. Compared with these outputs, experts identified fewer risks, typically less systemic but judged more likely, whereas laypeople surfaced more emotionally salient concerns that were generally less systemic. We propose a hybrid foresight workflow, wherein agents broaden systemic coverage, and humans provide contextual grounding. Our dataset is available at: https://social-dynamics.net/ai-risks/foresight.

</details>


### 112. Automating Computational Reproducibility in Social Science: Comparing Prompt-Based and Agent-Based Approaches

- **Authors:** Syed Mehtab Hussain Shah, Frank Hopfgartner, Arnim Bleier
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08561v1](http://arxiv.org/abs/2602.08561v1)
- **PDF:** [https://arxiv.org/pdf/2602.08561v1](https://arxiv.org/pdf/2602.08561v1)
- **Categories:** cs.SE, cs.CL


> The paper investigates the effectiveness of large language models and AI agents in automating the diagnosis and repair of failures in computational reproducibility within social science research. It employs a controlled testbed based on five fully reproducible R-based studies, manipulating errors to assess the performance of two workflows: a prompt-based approach and an agent-based approach. Key findings reveal that while prompt-based methods achieved a reproduction success rate of 31-79%, agent-based systems significantly outperformed them, with success rates of 69-96%, indicating that agent-based systems are more effective in handling diverse error types and can streamline the reproducibility process in computational research.


<details>
<summary>Abstract</summary>

Reproducing computational research is often assumed to be as simple as rerunning the original code with provided data. In practice, missing packages, fragile file paths, version conflicts, or incomplete logic frequently cause analyses to fail, even when materials are shared. This study investigates whether large language models and AI agents can automate the diagnosis and repair of such failures, making computational results easier to reproduce and verify. We evaluate this using a controlled reproducibility testbed built from five fully reproducible R-based social science studies. Realistic failures were injected, ranging from simple issues to complex missing logic, and two automated repair workflows were tested in clean Docker environments. The first workflow is prompt-based, repeatedly querying language models with structured prompts of varying context, while the second uses agent-based systems that inspect files, modify code, and rerun analyses autonomously. Across prompt-based runs, reproduction success ranged from 31-79 percent, with performance strongly influenced by prompt context and error complexity. Complex cases benefited most from additional context. Agent-based workflows performed substantially better, with success rates of 69-96 percent across all complexity levels. These results suggest that automated workflows, especially agent-based systems, can significantly reduce manual effort and improve reproduction success across diverse error types. Unlike prior benchmarks, our testbed isolates post-publication repair under controlled failure modes, allowing direct comparison of prompt-based and agent-based approaches.

</details>


### 113. EvoCorps: An Evolutionary Multi-Agent Framework for Depolarizing Online Discourse

- **Authors:** Ning Lin, Haolun Li, Mingshu Liu, Chengyun Ruan, Kaibo Huang, Yukun Wei, Zhongliang Yang, Linna Zhou
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08529v1](http://arxiv.org/abs/2602.08529v1)
- **PDF:** [https://arxiv.org/pdf/2602.08529v1](https://arxiv.org/pdf/2602.08529v1)
- **Categories:** cs.MA


> The paper presents EvoCorps, an evolutionary multi-agent framework designed to proactively depolarize online discourse by framing discourse governance as a dynamic social game. Utilizing a retrieval-augmented cognition core and closed-loop evolutionary learning, EvoCorps coordinates various agent roles to adapt strategies based on real-time environmental changes and adversarial actions. Key findings demonstrate that EvoCorps significantly improves discourse outcomes, such as emotional polarization and argumentative rationality, compared to traditional adversarial baselines, indicating a potential paradigm shift from reactive to proactive discourse intervention in the realm of agentic AI systems.


<details>
<summary>Abstract</summary>

Polarization in online discourse erodes social trust and accelerates misinformation, yet technical responses remain largely diagnostic and post-hoc. Current governance approaches suffer from inherent latency and static policies, struggling to counter coordinated adversarial amplification that evolves in real-time. We present EvoCorps, an evolutionary multi-agent framework for proactive depolarization. EvoCorps frames discourse governance as a dynamic social game and coordinates roles for monitoring, planning, grounded generation, and multi-identity diffusion. A retrieval-augmented collective cognition core provides factual grounding and action--outcome memory, while closed-loop evolutionary learning adapts strategies as the environment and attackers change. We implement EvoCorps on the MOSAIC social-AI simulation platform for controlled evaluation in a multi-source news stream with adversarial injection and amplification. Across emotional polarization, viewpoint extremity, and argumentative rationality, EvoCorps improves discourse outcomes over an adversarial baseline, pointing to a practical path from detection and post-hoc mitigation to in-process, closed-loop intervention. The code is available at https://github.com/ln2146/EvoCorps.

</details>


### 114. From Assistant to Double Agent: Formalizing and Benchmarking Attacks on OpenClaw for Personalized Local AI Agent

- **Authors:** Yuhang Wang, Feiming Xu, Zheng Lin, Guangyu He, Yuzhe Huang, Haichang Gao, Zhenxing Niu, Shiguo Lian, Zhaoxiang Liu
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08412v2](http://arxiv.org/abs/2602.08412v2)
- **PDF:** [https://arxiv.org/pdf/2602.08412v2](https://arxiv.org/pdf/2602.08412v2)
- **Categories:** cs.AI


> The paper introduces the Personalized Agent Security Bench (PASB), a novel evaluation framework designed to assess the security of personalized local AI agents like OpenClaw in real-world scenarios, moving beyond traditional task-centric approaches. It employs a systematic methodology that includes personalized usage scenarios and long-horizon interactions to conduct a comprehensive security evaluation, revealing critical vulnerabilities throughout various execution stages of OpenClaw. The findings underscore significant security risks associated with personalized AI deployments, demonstrating the need for enhanced security measures in this emerging field.


<details>
<summary>Abstract</summary>

Although large language model (LLM)-based agents, exemplified by OpenClaw, are increasingly evolving from task-oriented systems into personalized AI assistants for solving complex real-world tasks, their practical deployment also introduces severe security risks. However, existing agent security research and evaluation frameworks primarily focus on synthetic or task-centric settings, and thus fail to accurately capture the attack surface and risk propagation mechanisms of personalized agents in real-world deployments. To address this gap, we propose Personalized Agent Security Bench (PASB), an end-to-end security evaluation framework tailored for real-world personalized agents. Building upon existing agent attack paradigms, PASB incorporates personalized usage scenarios, realistic toolchains, and long-horizon interactions, enabling black-box, end-to-end security evaluation on real systems. Using OpenClaw as a representative case study, we systematically evaluate its security across multiple personalized scenarios, tool capabilities, and attack types. Our results indicate that OpenClaw exhibits critical vulnerabilities at different execution stages, including user prompt processing, tool usage, and memory retrieval, highlighting substantial security risks in personalized agent deployments. The code for the proposed PASB framework is available at https://github.com/AstorYH/PASB.

</details>


### 115. Altruism and Fair Objective in Mixed-Motive Markov games

- **Authors:** Yao-hua Franck Xu, Tayeb Lemlouma, Arnaud Braud, Jean-Marie Bonnin
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08389v1](http://arxiv.org/abs/2602.08389v1)
- **PDF:** [https://arxiv.org/pdf/2602.08389v1](https://arxiv.org/pdf/2602.08389v1)
- **Categories:** cs.MA, cs.AI, cs.GT, cs.LG


> The paper presents a novel framework aimed at promoting fairer cooperation in multi-agent systems by replacing the standard utilitarian objective with Proportional Fairness for altruistic utility. The methodology involves deriving analytical conditions for cooperation in social dilemmas and extending the framework to sequential settings through a Fair Markov Game, alongside the development of fair Actor-Critic algorithms. Key findings indicate that this approach can facilitate more equitable outcomes in cooperative scenarios, thus addressing the common issue of defection in mixed-motive settings.


<details>
<summary>Abstract</summary>

Cooperation is fundamental for society's viability, as it enables the emergence of structure within heterogeneous groups that seek collective well-being. However, individuals are inclined to defect in order to benefit from the group's cooperation without contributing the associated costs, thus leading to unfair situations. In game theory, social dilemmas entail this dichotomy between individual interest and collective outcome. The most dominant approach to multi-agent cooperation is the utilitarian welfare which can produce efficient highly inequitable outcomes. This paper proposes a novel framework to foster fairer cooperation by replacing the standard utilitarian objective with Proportional Fairness. We introduce a fair altruistic utility for each agent, defined on the individual log-payoff space and derive the analytical conditions required to ensure cooperation in classic social dilemmas. We then extend this framework to sequential settings by defining a Fair Markov Game and deriving novel fair Actor-Critic algorithms to learn fair policies. Finally, we evaluate our method in various social dilemma environments.

</details>


### 116. Who Deserves the Reward? SHARP: Shapley Credit-based Optimization for Multi-Agent System

- **Authors:** Yanming Li, Xuelin Zhang, WenJie Lu, Ziye Tang, Maodong Wu, Haotian Luo, Tongtong Wu, Zijie Peng, Hongze Mi, Yibo Feng, Naiqiang Tan, Chao Huang, Hong Chen, Li Shen
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08335v1](http://arxiv.org/abs/2602.08335v1)
- **PDF:** [https://arxiv.org/pdf/2602.08335v1](https://arxiv.org/pdf/2602.08335v1)
- **Categories:** cs.AI


> The paper presents SHARP (Shapley Credit-based Optimization for Multi-Agent Systems), a novel framework designed to enhance the training of multi-agent reinforcement learning systems by addressing the credit assignment problem through precise agent-specific reward attribution. The methodology involves the implementation of a decomposed reward mechanism that combines a global broadcast-accuracy reward, a Shapley-based marginal-credit reward for individual agents, and an execution efficiency reward. Key findings indicate that SHARP significantly improves performance in comparison to state-of-the-art methods, achieving average match enhancements of 23.66% over single-agent systems and 14.05% over multi-agent systems, thereby stabilizing training and fostering more effective collaboration among agents.


<details>
<summary>Abstract</summary>

Integrating Large Language Models (LLMs) with external tools via multi-agent systems offers a promising new paradigm for decomposing and solving complex problems. However, training these systems remains notoriously difficult due to the credit assignment challenge, as it is often unclear which specific functional agent is responsible for the success or failure of decision trajectories. Existing methods typically rely on sparse or globally broadcast rewards, failing to capture individual contributions and leading to inefficient reinforcement learning. To address these limitations, we introduce the Shapley-based Hierarchical Attribution for Reinforcement Policy (SHARP), a novel framework for optimizing multi-agent reinforcement learning via precise credit attribution. SHARP effectively stabilizes training by normalizing agent-specific advantages across trajectory groups, primarily through a decomposed reward mechanism comprising a global broadcast-accuracy reward, a Shapley-based marginal-credit reward for each agent, and a tool-process reward to improve execution efficiency. Extensive experiments across various real-world benchmarks demonstrate that SHARP significantly outperforms recent state-of-the-art baselines, achieving average match improvements of 23.66% and 14.05% over single-agent and multi-agent approaches, respectively.

</details>


### 117. Toward Formalizing LLM-Based Agent Designs through Structural Context Modeling and Semantic Dynamics Analysis

- **Authors:** Haoyu Jia, Kento Kawaharazuka, Kei Okada
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08276v1](http://arxiv.org/abs/2602.08276v1)
- **PDF:** [https://arxiv.org/pdf/2602.08276v1](https://arxiv.org/pdf/2602.08276v1)
- **Categories:** cs.AI


> The paper introduces the Structural Context Model, a formal framework designed to analyze and compare large language model (LLM) agents by focusing on context structure, which addresses the fragmentation in current LLM agent research. It comprises a declarative implementation framework and a sustainable engineering workflow called Semantic Dynamics Analysis, facilitating systematic design iteration and deeper insight into agent mechanisms. The effectiveness of this approach is validated through experiments on dynamic variants of the monkey-banana problem, resulting in up to a 32 percentage point improvement in agent success rates in challenging scenarios, demonstrating its relevance to agentic AI development.


<details>
<summary>Abstract</summary>

Current research on large language model (LLM) agents is fragmented: discussions of conceptual frameworks and methodological principles are frequently intertwined with low-level implementation details, causing both readers and authors to lose track amid a proliferation of superficially distinct concepts. We argue that this fragmentation largely stems from the absence of an analyzable, self-consistent formal model that enables implementation-independent characterization and comparison of LLM agents. To address this gap, we propose the \texttt{Structural Context Model}, a formal model for analyzing and comparing LLM agents from the perspective of context structure. Building upon this foundation, we introduce two complementary components that together span the full lifecycle of LLM agent research and development: (1) a declarative implementation framework; and (2) a sustainable agent engineering workflow, \texttt{Semantic Dynamics Analysis}. The proposed workflow provides principled insights into agent mechanisms and supports rapid, systematic design iteration. We demonstrate the effectiveness of the complete framework on dynamic variants of the monkey-banana problem, where agents engineered using our approach achieve up to a 32 percentage points improvement in success rate on the most challenging setting.

</details>


### 118. When Do Multi-Agent Systems Outperform? Analysing the Learning Efficiency of Agentic Systems

- **Authors:** Junwei Su, Chuan Wu
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08272v1](http://arxiv.org/abs/2602.08272v1)
- **PDF:** [https://arxiv.org/pdf/2602.08272v1](https://arxiv.org/pdf/2602.08272v1)
- **Categories:** cs.LG, cs.AI


> The paper investigates the conditions under which Multi-Agent Reinforcement Learning (MARL) outperforms Single-Agent Reinforcement Learning (SARL), focusing on the learning efficiency of agentic systems in the context of large language models (LLMs). By employing the Probably Approximately Correct (PAC) framework, the authors establish sample complexity bounds and analyze the impact of task decomposition and alignment on learning efficiency. Key findings indicate that MARL enhances sample efficiency with naturally independent subtasks but faces challenges with dependent subtasks, offering practical guidelines for effectively implementing MARL in complex LLM applications.


<details>
<summary>Abstract</summary>

Reinforcement Learning (RL) has emerged as a crucial method for training or fine-tuning large language models (LLMs), enabling adaptive, task-specific optimizations through interactive feedback. Multi-Agent Reinforcement Learning (MARL), in particular, offers a promising avenue by decomposing complex tasks into specialized subtasks learned by distinct interacting agents, potentially enhancing the ability and efficiency of LLM systems. However, theoretical insights regarding when and why MARL outperforms Single-Agent RL (SARL) remain limited, creating uncertainty in selecting the appropriate RL framework. In this paper, we address this critical gap by rigorously analyzing the comparative sample efficiency of MARL and SARL within the context of LLM. Leveraging the Probably Approximately Correct (PAC) framework, we formally define SARL and MARL setups for LLMs, derive explicit sample complexity bounds, and systematically characterize how task decomposition and alignment influence learning efficiency. Our results demonstrate that MARL improves sample complexity when tasks naturally decompose into independent subtasks, whereas dependent subtasks diminish MARL's comparative advantage. Additionally, we introduce and analyze the concept of task alignment, quantifying the trade-offs when enforcing independent task decomposition despite potential misalignments. These theoretical insights clarify empirical inconsistencies and provide practical criteria for deploying MARL strategies effectively in complex LLM scenarios.

</details>


### 119. SynthAgent: A Multi-Agent LLM Framework for Realistic Patient Simulation -- A Case Study in Obesity with Mental Health Comorbidities

- **Authors:** Arman Aghaee, Sepehr Asgarian, Jouhyun Jeon
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.08254v1](http://arxiv.org/abs/2602.08254v1)
- **PDF:** [https://arxiv.org/pdf/2602.08254v1](https://arxiv.org/pdf/2602.08254v1)
- **Categories:** cs.AI, cs.IR, cs.MA


> The paper presents SynthAgent, a Multi-Agent System framework aimed at simulating high-fidelity patients with obesity and mental health comorbidities, addressing issues related to real-world data limitations. The methodology integrates diverse clinical data to create personalized virtual patients, enabling the simulation of disease progression and treatment responses through agent interactions. Key findings indicate that the use of GPT-5 and Claude 4.5 Sonnet within SynthAgent results in superior simulation fidelity compared to other models, offering a scalable and privacy-conscious approach for investigating patient behaviors and decision-making in healthcare settings.


<details>
<summary>Abstract</summary>

Simulating high-fidelity patients offers a powerful avenue for studying complex diseases while addressing the challenges of fragmented, biased, and privacy-restricted real-world data. In this study, we introduce SynthAgent, a novel Multi-Agent System (MAS) framework designed to model obesity patients with comorbid mental disorders, including depression, anxiety, social phobia, and binge eating disorder. SynthAgent integrates clinical and medical evidence from claims data, population surveys, and patient-centered literature to construct personalized virtual patients enriched with personality traits that influence adherence, emotion regulation, and lifestyle behaviors. Through autonomous agent interactions, the system simulates disease progression, treatment response, and life management across diverse psychosocial contexts. Evaluation of more than 100 generated patients demonstrated that GPT-5 and Claude 4.5 Sonnet achieved the highest fidelity as the core engine in the proposed MAS framework, outperforming Gemini 2.5 Pro and DeepSeek-R1. SynthAgent thus provides a scalable and privacy-preserving framework for exploring patient journeys, behavioral dynamics, and decision-making processes in both medical and psychological domains.

</details>


### 120. scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis

- **Authors:** Kenny Workman, Zhen Yang, Harihara Muralidharan, Aidan Abdulali, Hannah Le
- **Published:** 2026-02-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.09063v1](http://arxiv.org/abs/2602.09063v1)
- **PDF:** [https://arxiv.org/pdf/2602.09063v1](https://arxiv.org/pdf/2602.09063v1)
- **Categories:** q-bio.GN, cs.AI


> The paper presents scBench, a benchmark consisting of 394 verifiable problems designed to assess AI agents' capability to analyze single-cell RNA sequencing (scRNA-seq) data across various platforms and tasks. The methodology involves creating practical scRNA-seq workflows and employing deterministic grading to evaluate the biological insights extracted by AI models. Key findings indicate that existing models demonstrate limited accuracy (29-53%), with significant performance variability influenced by both model and platform choice, highlighting the challenge of developing reliable agentic AI for complex biological datasets.


<details>
<summary>Abstract</summary>

As single-cell RNA sequencing datasets grow in adoption, scale, and complexity, data analysis remains a bottleneck for many research groups. Although frontier AI agents have improved dramatically at software engineering and general data analysis, it remains unclear whether they can extract biological insight from messy, real-world single-cell datasets. We introduce scBench, a benchmark of 394 verifiable problems derived from practical scRNA-seq workflows spanning six sequencing platforms and seven task categories. Each problem provides a snapshot of experimental data immediately prior to an analysis step and a deterministic grader that evaluates recovery of a key biological result. Benchmark data on eight frontier models shows that accuracy ranges from 29-53%, with strong model-task and model-platform interactions. Platform choice affects accuracy as much as model choice, with 40+ percentage point drops on less-documented technologies. scBench complements SpatialBench to cover the two dominant single-cell modalities, serving both as a measurement tool and a diagnostic lens for developing agents that can analyze real scRNA-seq datasets faithfully and reproducibly.

</details>



## Biorxiv (2 papers)


### 1. Causal evidence for a shared mechanism linking language and tool use via the putamen

- **Authors:** Fan, Z., Wen, H., Han, Z., Wang, X., Bi, Y.
- **Published:** 2026-02-09
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.02.06.704290](https://doi.org/10.64898/2026.02.06.704290)

- **Categories:** neuroscience


> This paper identifies the putamen as a critical neural substrate linking human language and tool use through a shared mechanism that supports goal-dependent sequence integrity. The researchers employed brain lesion analysis, developmental contrasts, and functional neuroimaging involving 100 adults with focal brain injuries, revealing that damage to the putamen impaired both sentence processing and tool use. Key findings indicate that early language acquisition enhances tool-use performance and strengthens putaminal responses, highlighting the importance of this brain region in agentic AI systems that aim to replicate or understand human-like cognitive processes.


<details>
<summary>Abstract</summary>

Both human language and tool use--two hallmark capacities of human cognition--depend on organizing discrete elements, i.e., symbols and actions, into highly constrained structured sequences to achieve a functional goal. However, the neural mechanism linking these capacities is unclear. We combined brain lesion analysis, developmental contrast, and functional neuroimaging to test whether the basal ganglia play a causal role in their shared capacity. In 100 adults with focal brain injury, damage to the putamen disrupted both sentence processing and tool use, with impairments specifically explained by reduced goal-dependent sequence integrity for both tasks. Further comparing populations with typical and deprived early language experience (congenitally deaf adults with vs. without early sign language exposure), we found that early language acquisition was associated with improved tool-use performance and strengthened putaminal responses to such goal dependency, which mediated the relationship between sentence sequence integrity and tool behavior. Together, these results identify the putamen as a key neural substrate supporting goal-dependent sequence integrity across language and action, and show how early language experience shapes this conserved control system.

One-Sentence SummaryLanguage and tool use share a putamen-based mechanism that supports goal-dependent sequence integrity, and this mechanism is strengthened by early language experience.

</details>


### 2. MetaKnogic-Alpha: A Hyper-Relational Knowledge Base for Grounded Metabolic Reasoning

- **Authors:** Dang, P., Swaminathan, P., Guo, T., Wan, C., Cao, S., Zhang, C.
- **Published:** 2026-02-09
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.02.05.704050](https://doi.org/10.64898/2026.02.05.704050)

- **Categories:** bioinformatics


> The main contribution of the paper is the development of MetaKnogic-Alpha, a hyper-relational knowledge base designed to synthesize and organize biomedical literature related to metabolic research, facilitating grounded metabolic reasoning. The methodology involves transforming over 100,000 full-text articles into a hypergraph structure that captures complex relationships within metabolic pathways, utilizing an autonomous reasoning agent to enhance query precision and perform multi-hop expansions to identify critical biological relationships while ensuring rigorous validity through deterministic grounding against a curated metabolic network. Key findings indicate that MetaKnogic-Alpha achieves a mechanistic accuracy of 0.98 in providing reliable insights derived from literature, significantly improving the efficiency of metabolic research by automating synthesis that historically required extensive manual effort, thus enhancing the capabilities of agents in precision oncology.


<details>
<summary>Abstract</summary>

The exponential trajectory of biomedical literature has precipitated a fundamental "synthesis gap" in metabolic research, where critical mechanistic insights remain fragmented across hundreds of thousands of disjointed full-text articles, preventing the consolidation of a global mechanistic view. Here, we present MetaKnogic-Alpha, a foundational mechanistic knowledge substrate designed to bridge this gap by transforming unstructured literature into a navigable, logic-based resource. MetaKnogic-Alpha synthesizes over 100K full-text articles into a hyper-relational hypergraph structure, preserving the n-ary relational logic inherent in complex metabolic pathways. To ensure biological rigor, we implemented a hierarchical discovery protocol: an autonomous reasoning agent first enriches query nomenclature for domain-specific precision, followed by a multi-hop topological expansion within the hypergraph to surface functional neighbors, such as enzymatic co-factors and distal regulators, often lost in traditional search paradigms. Crucially, the system subjects all literature-derived insights to a deterministic biochemical grounding against a curated metabolic reaction network, significantly mitigating the risk of probabilistic hallucinations common in standalone generative models. In rigorous benchmarking, MetaKnogic-Alpha achieved a mechanistic accuracy of 0.98 in scenarios where supporting evidence was present, providing a robustly attributable audit trail back to the primary literature via PubMed Central Identifiers. We designate this primary release as "alpha" to establish the foundational architectural logic for a burgeoning million-scale resource. By compressing the synthesis of thousands of papers from a multi-month manual effort into several hours of automated discovery, MetaKnogic-Alpha serves as a high-fidelity research companion that augments the human experts ability to resolve complex metabolic interactions and identify novel therapeutic drivers in precision oncology.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*