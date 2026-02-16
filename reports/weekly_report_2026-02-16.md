# Weekly AI Agent Paper Report

**Generated:** 2026-02-16 23:03
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

Here are the notable points comparing this week's AI agent paper trends with last week's:

1. **Volume Decrease**: There was a significant drop from 167 papers last week to 124 papers this week, indicating a reduction in publication activity in the field of AI agents.

2. **Shift in Source Distribution**: The contribution from arXiv decreased from 162 papers last week to 120 this week, while medRxiv saw a slight decline from 4 to 2. BioRxiv maintained a comparable volume with 1-2 papers across both weeks, suggesting a stability in the biosciences focus.

3. **Emerging Research Focus**: This week’s top papers reflect an expanding breadth of topics, including metagenomics and multimodal systems, with a focus on practical applications like health monitoring and incident response. In contrast, previous week’s papers emphasized foundational concepts in agent-based systems and AI alignment.

4. **Interest in Evaluation Frameworks**: The presence of papers like 'SciAgentGym' and 'SkillsBench' this week highlights an increasing focus on benchmarking and evaluating agent capabilities across diverse tasks, suggesting a maturation in the research landscape.

5. **Increased Health Domain Relevance**: The recurrence of health-related applications, particularly in summarization and causal inference, suggests a growing trend in deploying AI agents for practical healthcare solutions, which mirrors the ongoing demand for innovative healthcare technologies.

---



## Biomedical Highlights (4 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


The first paper explores the interrelationship between human language and tool use, emphasizing a shared cognitive mechanism within the putamen that organizes symbols and actions into structured sequences, which is crucial for both capabilities. The second paper introduces MetaKnogic-Alpha, a hyper-relational knowledge base designed to address the "synthesis gap" in metabolic research by integrating diverse biomedical literature to facilitate more comprehensive metabolic reasoning. The third paper investigates the potential of AI-driven metagenomics to predict Inflammatory Bowel Disease (IBD) and recommend probiotics, highlighting the connection between gut microbiome dysbiosis and autoimmune diseases through specific microbial signatures. Finally, the fourth paper discusses MedAgentBrief, an AI tool aimed at automating hospital course summarization, which can alleviate clinician documentation burdens associated with discharge summaries, ultimately enhancing patient care transitions and reducing clinician burnout. Across these works, common themes include the application of AI and advanced modeling techniques to improve biomedical research, patient care, and understanding of complex biological systems.



### 1. Causal evidence for a shared mechanism linking language and tool use via the putamen

- **Authors:** Fan, Z., Wen, H., Han, Z., Wang, X., Bi, Y.
- **Published:** 2026-02-09
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.02.06.704290](https://doi.org/10.64898/2026.02.06.704290)

- **Categories:** neuroscience


> The paper investigates the neural mechanisms linking language and tool use, revealing that the putamen plays a crucial role in maintaining goal-dependent sequence integrity in both capacities. Using a combination of brain lesion analysis, developmental studies, and functional neuroimaging, the authors found that damage to the putamen in individuals with brain injury impaired both sentence processing and tool use, while early language acquisition was shown to enhance tool performance and strengthen putaminal responses. This research highlights the putamen as a shared neural substrate for language and action, with early language experience significantly influencing its functionality.


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


> The paper introduces MetaKnogic-Alpha, a hyper-relational knowledge base developed to synthesize extensive biomedical literature related to metabolic research, addressing the challenge of fragmented mechanistic insights. The methodology involves transforming over 100,000 full-text articles into a hypergraph structure that captures complex metabolic relationships, utilizing an autonomous reasoning agent for precise query enrichment and deterministic grounding against established metabolic networks. Key findings include achieving a mechanistic accuracy of 0.98 in evidence-supported scenarios, demonstrating that MetaKnogic-Alpha significantly improves the speed and reliability of knowledge extraction in metabolic pathways, thereby enhancing the capabilities of researchers in fields like precision oncology.


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


> This paper introduces a predictive tool leveraging AI and machine learning to assess Inflammatory Bowel Disease (IBD) based on the gut microbiome's composition. Using integrated metagenomic processing and an XGBoost classifier, the tool achieved an accuracy of 86.6% in predicting IBD status and identified specific dysbiotic taxa, while also providing personalized probiotic recommendations. Although validation was limited, the high performance and detailed analysis indicate significant potential for advancing agentic AI applications in personalized medicine for autoimmune diseases.


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


> The study presents MedAgentBrief, an LLM-based agentic AI workflow designed to generate hospital course summaries and evaluate its safety, utilization, and impact on clinician burden in a real-world setting. Conducted as a single-arm prospective pilot study involving 384 hospital discharges, the system demonstrated a utilization rate of 57% among physicians, with minimal harm reported and a significant reduction in burnout scores alongside time-saving benefits. Key findings suggest that while the AI-generated summaries occasionally contained omissions and inaccuracies, the overall safety profile was reassuring, highlighting the potential of AI to alleviate clinician documentation burdens effectively.


<details>
<summary>Abstract</summary>

ImportanceHigh-quality discharge summaries are essential for safe care transitions but contribute substantially to clinician documentation burden and burnout. While retrospective studies suggest large language models (LLMs) can generate clinical summaries of comparable quality to physicians, prospective data on their safety, utility, and impact on clinician well-being in real-world environments are lacking.

ObjectiveTo evaluate the safety, utilization, and impact on clinician burden of MedAgentBrief, an LLM-based agentic workflow for generating hospital course summaries, during prospective clinical deployment.

Design, Setting, and ParticipantsSingle-arm prospective pilot study encompassing 384 hospital discharges at one academic inpatient medicine unit from August 1 to October 11, 2025, with baseline comparisons drawn from April 9 to July 31, 2025.

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


> This paper introduces a predictive tool leveraging AI and machine learning to assess Inflammatory Bowel Disease (IBD) based on the gut microbiome's composition. Using integrated metagenomic processing and an XGBoost classifier, the tool achieved an accuracy of 86.6% in predicting IBD status and identified specific dysbiotic taxa, while also providing personalized probiotic recommendations. Although validation was limited, the high performance and detailed analysis indicate significant potential for advancing agentic AI applications in personalized medicine for autoimmune diseases.


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


> The study presents MedAgentBrief, an LLM-based agentic AI workflow designed to generate hospital course summaries and evaluate its safety, utilization, and impact on clinician burden in a real-world setting. Conducted as a single-arm prospective pilot study involving 384 hospital discharges, the system demonstrated a utilization rate of 57% among physicians, with minimal harm reported and a significant reduction in burnout scores alongside time-saving benefits. Key findings suggest that while the AI-generated summaries occasionally contained omissions and inaccuracies, the overall safety profile was reassuring, highlighting the potential of AI to alleviate clinician documentation burdens effectively.


<details>
<summary>Abstract</summary>

ImportanceHigh-quality discharge summaries are essential for safe care transitions but contribute substantially to clinician documentation burden and burnout. While retrospective studies suggest large language models (LLMs) can generate clinical summaries of comparable quality to physicians, prospective data on their safety, utility, and impact on clinician well-being in real-world environments are lacking.

ObjectiveTo evaluate the safety, utilization, and impact on clinician burden of MedAgentBrief, an LLM-based agentic workflow for generating hospital course summaries, during prospective clinical deployment.

Design, Setting, and ParticipantsSingle-arm prospective pilot study encompassing 384 hospital discharges at one academic inpatient medicine unit from August 1 to October 11, 2025, with baseline comparisons drawn from April 9 to July 31, 2025.

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


> The paper presents an innovative approach for autonomous network incident response by utilizing a lightweight large language model (LLM) that integrates perception, reasoning, planning, and action functionalities into a single agentic solution. By employing in-context learning and fine-tuning, the LLM agent can effectively process system logs, infer attack models, plan responses, and refine its strategies based on real-time outcomes, all without the need for handcrafted simulation models. Key findings indicate that this agent can recover from incidents up to 23% faster than existing leading LLMs, demonstrating significant advancements in adaptability and efficiency in the field of agentic AI for cybersecurity.


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


> The paper presents TraceBack, a modular multi-agent framework designed to enhance fine-grained attribution in single-table question answering (QA) by providing transparent connections between answers and their supporting cells. The methodology involves pruning irrelevant table sections, breaking down questions into sub-questions, and aligning answers with the corresponding cells, while introducing CITEBench as a benchmark for evaluating this framework. Key findings indicate that TraceBack significantly improves performance over existing systems and that the newly developed FairScore metric effectively measures attribution precision and recall, aligning closely with human judgments, which is crucial for trustworthiness in agentic AI applications.


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


> The paper presents SciAgentGym, an innovative benchmarking environment designed to evaluate the ability of large language model (LLM) agents to use scientific tools across various disciplines, addressing a gap in current benchmarks regarding complex multi-step workflows. Through a comprehensive evaluation using SciAgentBench, it was discovered that even advanced models like GPT-5 exhibit a significant decline in performance during long-horizon interactions, highlighting challenges in executing intricate workflows. To combat this, the authors propose SciForge, a data synthesis technique that enhances LLM training on tool use, enabling their model, SciAgent-8B, to outperform larger counterparts while demonstrating effective cross-domain capabilities in scientific tool use.


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


> The paper presents BrowseComp-$V^3$, a benchmark designed to evaluate the capabilities of multimodal large language models (MLLMs) in performing complex web browsing tasks. Methodologically, it introduces 300 diverse and challenging questions that require deep, multi-level reasoning across textual and visual modalities, with a focus on using publicly searchable evidence and incorporating a subgoal-driven evaluation process to assess intermediate reasoning. Key findings reveal that even state-of-the-art MLLMs achieve only 36% accuracy on this benchmark, underscoring significant limitations in their ability to integrate multimodal information and perform robust deep searches in real-world scenarios, thus highlighting critical areas for improvement in agentic AI frameworks.


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


> The paper introduces SkillsBench, a comprehensive benchmark consisting of 86 tasks across 11 domains to evaluate the efficacy of curated and self-generated agent skills for LLMs. Through testing 7 agent-model configurations on 7,308 trajectories, the study finds that curated skills significantly improve performance by an average of 16.2 percentage points, though the impact varies by domain, and self-generated skills offer no measurable advantage. The results highlight that focused skills using 2-3 modules are more effective than extensive documentation, indicating potential for smaller models with skills to match the performance of larger models without them, contributing valuable insights into agentic AI development.


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


> The paper presents CogRouter, a novel framework designed for large language model (LLM) agents that allows them to adapt their cognitive depth dynamically during multi-turn decision-making tasks, addressing the inefficiencies of fixed cognitive patterns. Methodologically, CogRouter employs a two-stage training approach that incorporates Cognition-aware Supervised Fine-tuning (CoSFT) and Cognition-aware Policy Optimization (CoPO) to enable agents to adjust their cognitive levels based on task demands. Key findings highlight that CogRouter achieves state-of-the-art performance with a significant increase in efficiency, demonstrated by an 82.3% success rate on the ALFWorld and ScienceWorld benchmarks while utilizing 62% fewer tokens compared to existing models.


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


> The paper presents a novel approach to inventory control by demonstrating how operations research (OR) algorithms, large language models (LLMs), and human decision-makers can work together to enhance performance. Using a new benchmark called InventoryBench, the authors show that OR-augmented LLM methods outperform traditional approaches when faced with fluctuating demand and uncertainty, indicating a complementary relationship rather than a competitive one. Additionally, through a controlled experiment, they find that human-AI collaboration yields higher profits than either party working alone and identify a significant fraction of individuals who benefit from this collaborative framework, highlighting its potential in agentic AI systems.


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


> The paper introduces a novel multi-agent model-based reinforcement learning framework that integrates joint state-action representation learning with imaginative roll-outs to enhance coordination in dynamic environments. The methodology employs a world model trained with variational auto-encoders, using state-action learned embeddings (SALE) to improve future trajectory forecasting and action value estimation. Key findings indicate that this approach significantly outperforms baseline algorithms in multi-agent benchmarks, enhancing agents' understanding of collective outcomes and improving long-term planning efficiency.


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


> The paper introduces Bench-MFG, a benchmark suite designed to standardize evaluation for learning in stationary Mean Field Games (MFGs), addressing the current lack of cohesive assessment methodologies in the intersection of MFGs and Reinforcement Learning. The methodology includes a taxonomy of problem classes, prototypical environments for testing various algorithms, and the development of MF-Garnets for generating random MFG instances. Key findings suggest that the benchmark facilitates robust comparisons across learning algorithms, including a new exploitability minimization approach, and offers guidelines for standardizing future research in agentic AI.


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


> The paper presents a novel framework for scaling small-team defense strategies against large drone swarms, addressing the limitations of traditional multi-agent optimization methods. Utilizing dynamic programming decomposition, the authors efficiently construct larger defense teams by integrating proven modular components while iterating on large-team outcomes to refine strategies. Key findings indicate that this approach maintains effectiveness and uncovers cooperative behaviors in large scenarios, highlighting its potential contribution to the field of agentic AI in optimizing multi-agent systems for complex operational environments.


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


> The paper introduces Favia, an agent-based framework designed to enhance the identification of vulnerability-fixing commits related to disclosed CVEs in large software repositories. Utilizing a two-stage methodology, Favia first ranks potential commits to focus the search effectively and then applies a ReAct-based large language model (LLM) agent for detailed evaluation, employing iterative semantic reasoning to establish connections between code changes and vulnerability origins. Evaluation results on the CVEVC dataset indicate that Favia outperforms existing approaches, achieving superior precision-recall trade-offs and F1-scores, thus providing significant advancements in the field of agentic AI for security maintenance.


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


> The paper presents a novel adaptive ensemble agent that enhances zero-shot coordination in multi-agent reinforcement learning by employing Theory-of-Mind principles to infer teammates' intentions, allowing it to select the most appropriate policy from a diverse ensemble. Unlike traditional approaches that often lead to static generalist policies, this method promotes dynamic adaptability, resulting in more effective collaboration and increased synergy with unseen partners. The evaluation in the Overcooked environment shows that this approach significantly outperforms conventional best-response models in both fully and partially observable scenarios, marking a substantial contribution to advancing agentic AI capabilities.


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


> The paper presents a comprehensive survey on the evolution of agent skills in large language models (LLMs), highlighting the shift from monolithic architectures to modular agents that utilize composable skill packages for dynamic capability expansion. It details the methodology behind skill architecture, acquisition techniques such as reinforcement learning and autonomous discovery, and deployment strategies, while also addressing security concerns linked to vulnerabilities in community-contributed skills. Key findings emphasize the need for a governance framework for skill deployment and identify critical challenges within the agentic AI landscape, setting a research agenda for developing robust and trustworthy skill ecosystems.


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


> The paper presents a novel two-timescale Actor-Critic algorithm for learning stationary policies in infinite-horizon general-sum Markov games, addressing the challenges of Multi-Agent Reinforcement Learning (MARL). By incorporating Risk-averse Quantal response Equilibria (RQE) from behavioral game theory, the authors establish a method with strong regularity conditions that enable global convergence with finite-sample guarantees. Empirical results show that the proposed approach significantly outperforms risk-neutral baselines, highlighting its potential impact on the field of agentic AI by providing a robust framework for risk-averse decision-making in multi-agent scenarios.


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


> The paper presents CM2, a novel reinforcement learning framework that utilizes checklist rewards to facilitate multi-turn and multi-step agentic tool use. By breaking down intended behaviors into fine-grained binary criteria and using a scalable LLM-simulated tool environment, CM2 effectively transforms open-ended evaluation into structured decision-making while minimizing the need for complex tool engineering. Experimental results demonstrate that CM2 significantly outperforms traditional supervised fine-tuning approaches across various benchmarks, showcasing its potential as a scalable method for training agentic AI without relying on verifiable rewards.


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


> The paper introduces KeplerAgent, a novel framework that enhances symbolic equation discovery by incorporating a multi-step scientific reasoning process, which is often overlooked in existing large language models (LLMs). By leveraging physics-based tools to extract intermediate structures, KeplerAgent effectively coordinates these insights to optimize symbolic regression methods like PySINDy and PySR. Key findings reveal that KeplerAgent significantly outperforms both LLM and traditional methods in terms of symbolic accuracy and robustness, making it a compelling advancement in the agentic AI field focused on scientific discovery.


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


> The paper presents VIRENA (Virtual Arena), a novel platform that facilitates controlled experimentation in realistic social media environments to study communication dynamics, human-AI interaction, and content moderation. Utilizing large language model-powered AI agents and a user-friendly no-code interface, VIRENA allows researchers to engage multiple participants in simulations of platforms like Instagram and Facebook, enabling the manipulation of experimental conditions without the complexities of programming. Key findings highlight VIRENA's potential to revolutionize research methodologies by making it feasible to analyze social interactions and deliberation processes in a controlled yet realistic setting, while also ensuring compliance with data protection standards.


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


> The main contribution of the paper is the introduction of GT-HarmBench, a comprehensive benchmark designed to assess AI safety risks in multi-agent settings through game-theoretic frameworks. The methodology involves evaluating 15 frontier AI models across 2,009 scenarios drawn from realistic contexts, revealing that these agents choose socially beneficial actions only 62% of the time, often resulting in harmful outcomes. Key findings demonstrate that game-theoretic interventions can enhance beneficial outcomes by up to 18%, underscoring the importance of understanding coordination and conflict in agentic AI systems while providing a standardized tool for future research in AI alignment.


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


> The paper presents significant advancements in understanding Convex Markov Games (cMGs) by extending them to General Utility Markov Games (GUMGs), which accommodate more complex agent interactions. Utilizing a novel agent-wise gradient domination property, the authors establish that Nash equilibria correspond to fixed points of projected pseudo-gradient dynamics, offer a straightforward proof of existence via Brouwer's fixed-point theorem, and introduce a model-free policy gradient algorithm with complexity guarantees. Key findings indicate that GUMGs allow for the coexistence of Nash and Markov perfect equilibria, broadening the theoretical landscape for multi-agent systems beyond the typical zero-sum frameworks.


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


> This paper presents the first empirical study on the adoption and impact of AI coding agents in open-source mobile app development, analyzing 2,901 AI-generated pull requests across 193 Android and iOS projects. Using a comparative methodology, the study reveals that Android projects receive significantly more AI-authored PRs and have higher acceptance rates compared to iOS, with routine tasks outperforming structural changes in terms of acceptance and resolution times. The findings establish foundational data for evaluating the contributions of AI in mobile software development, highlighting variations in agent effectiveness and providing insights relevant to the design of agentic AI systems.


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


> The paper presents a multi-agent framework that generates physics simulation code from natural language descriptions, incorporating a novel perceptual self-reflection mechanism for validation. The methodology involves four specialized agents that handle natural language interpretation, technical requirements generation, code generation with self-correction, and validation through perceptual analysis of rendered animations. Key findings indicate that this approach significantly improves code generation accuracy across various physics domains compared to conventional single-shot methods, demonstrating the efficacy of integrating visual outputs into the refinement process and highlighting the potential of agentic AI in enhancing engineering workflows and data generation in physics.


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


> The paper investigates the effects of different AI modalities (Advisor, Coach, and Delegate) in multi-party negotiations to understand their impact on user interaction and outcomes. Through an online behavioral experiment with 243 participants, the authors found that while users preferred the Advisor for its proactive recommendations, the Delegate modality led to the highest individual gains and positive externalities for non-users, acting as a market maker that enhanced the negotiation environment. The findings highlight a significant misalignment between user preferences and performance outcomes, emphasizing the need for better design of AI assistance systems that facilitate adoption and optimize group welfare.


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


> The paper presents a novel framework called differentiable modal logic (DML), implemented using Modal Logical Neural Networks (MLNNs), which enables multi-agent AI systems to learn complex relational structures like trust networks and causal chains from behavioral data without manual specification. The proposed methodology integrates four modalities—epistemic, temporal, deontic, and doxastic—into a unified neurosymbolic debugging framework, demonstrated across various scenarios including diplomacy games and addressing hallucinations in large language models. Key findings include the interpretability of learned structures, the capability for knowledge injection through differentiable axioms, and the advancement of multi-modal reasoning, making this work significant for improving the robustness and adaptability of agentic AI systems in dynamic environments.


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


> The paper introduces DTAPP-IICR, a novel framework for preflight planning of large-scale UAV fleets in dynamic airspace that addresses challenges such as temporal No-Fly Zones and diverse vehicle profiles. The methodology employs a Delivery-Time Aware Prioritized Planning approach for initial trajectory generation, integrates a new 4D planner for trajectory optimization under constraints, and utilizes an iterative Large Neighborhood Search for conflict resolution. Key findings indicate that DTAPP-IICR achieves near-100% success rates with fleets of up to 1,000 UAVs while significantly reducing runtime by up to 50% through advanced pruning techniques, marking it as a scalable and practical solution for urban UAV deployments in Unmanned Traffic Management systems.


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


> The paper presents PrefillShare, a novel algorithm designed to enhance the efficiency of multi-agent systems in language model serving by sharing the prefill module and key-value (KV) cache across different models, thereby reducing computational redundancy and latency. Methodologically, it employs a disaggregated serving framework that separates prefill and decode processes while freezing the prefill module and fine-tuning only the decode modules, coupled with a routing mechanism for effective sharing. Key findings indicate that PrefillShare achieves full fine-tuning accuracy across various tasks and models while significantly improving performance metrics, offering 4.5x lower p95 latency and 3.9x higher throughput in multi-model agent scenarios, thus advancing the field of agentic AI.


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


> This paper presents a multi-agent perimeter defense game set on a cylindrical topology, where a team of slow-moving defenders aims to thwart a single fast-moving attacker attempting to breach a boundary. The authors develop a theoretical framework to analyze the interplay between defenders and the attacker, particularly focusing on scenarios where the attacker begins near the boundary in a defended region. Key findings highlight specific conditions under which the attacker can successfully penetrate the defense, contributing valuable insights to the design of agentic AI systems focused on collaborative defense strategies.


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


> The paper presents Gaia2, a benchmark designed for assessing large language model (LLM) agents in dynamic and asynchronous environments, moving beyond static evaluations to include scenarios where environments evolve independently of agent actions. Utilizing a write-action verifier for detailed evaluation, Gaia2 allows for reinforcement learning with verifiable rewards. Results indicate that while no model consistently outperforms others across all tasks, key findings reveal trade-offs in reasoning, efficiency, and robustness, underscoring challenges in bridging the "sim2real" gap and providing a valuable infrastructure for future developments in agentic AI.


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


> The paper presents AdaptEvolve, a novel framework for dynamically selecting large language models (LLMs) in evolutionary agentic systems to enhance computational efficiency without compromising reasoning capability. By employing a confidence-driven approach for model selection during inference, the methodology improves efficiency through adaptive LLM selection based on real-time solvability estimates. Key findings indicate that this approach reduces total inference costs by an average of 37.9% while maintaining 97.5% of the accuracy achieved by static large-model baselines, significantly benefiting the field of agentic AI.


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


> The paper introduces MEME (Modeling the Evolutionary Modes of Financial Markets), a novel framework that models financial markets as dynamic ecosystems of competing investment narratives, emphasizing a Logic-Oriented perspective. The methodology includes a multi-agent extraction module to convert noisy data into Investment Arguments and employs Gaussian Mixture Modeling to identify latent consensus within market conditions. Key findings reveal that MEME significantly outperforms seven state-of-the-art baselines on various Chinese stock pools from 2023 to 2025, demonstrating its effectiveness in adapting to market evolution while prioritizing enduring investment wisdom.


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


> The paper presents a novel meta-cognitive architecture for agentic AI in cybersecurity, aiming to enhance accountability and governance in decision-making under adversarial uncertainty. It introduces a framework where heterogeneous AI agents work together through a meta-cognitive judgment function that manages decision readiness and adjusts system autonomy based on evidence quality. The key finding is that integrating this structured cognitive approach allows for more effective cybersecurity orchestration, moving beyond traditional task-centric models to enable responsible and adaptable AI-driven response mechanisms.


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


> The paper introduces an adaptive framework for intelligent AI delegation, which improves task decomposition and delegation beyond existing heuristic methods by incorporating dynamic adaptability and handling unexpected failures. The methodology focuses on a sequence of decisions for task allocation that includes authority transfer, accountability, role clarity, intent specification, and trust mechanisms. Key findings suggest that this framework enhances collaboration in complex delegation networks involving both AI agents and humans, thereby contributing significantly to the field of agentic AI.


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


> The paper presents a novel approach to addressing social dilemmas in sustainable investment by using the multi-agent simulation InvestESG to analyze the interactions between investors and companies under climate risk. The authors implement the Advantage Alignment algorithm to shape agent learning towards cooperative behaviors, thereby aligning individual incentives with collective welfare. Key findings reveal that this method can systematically favor socially beneficial outcomes, suggesting that opponent shaping could inform policy mechanisms that promote sustainable investment practices.


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


> The paper presents LAVES, a hierarchical LLM-based multi-agent system that transforms the process of generating educational videos from problem statements into a structured multi-objective task, enhancing logical rigor and knowledge representation. Utilizing a central Orchestrating Agent to coordinate specialized agents—including a Solution Agent, Illustration Agent, and Narration Agent—LAVES systematically ensures high-quality outputs through iterative critique and explicit quality control mechanisms. The findings highlight LAVES's capability to produce over one million instructional videos per day with more than 95% cost reduction compared to traditional methods while maintaining high user acceptance, thereby significantly advancing the field of agent-based AI systems in educational content generation.


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


> The paper presents TSR (Trajectory-Search Rollouts), an innovative method aimed at enhancing multi-turn reinforcement learning (RL) for large language model (LLM) agents by improving rollout quality through a lightweight tree-style search that utilizes task-specific feedback. By applying TSR during training, the method generates high-quality trajectories, leading to significant performance gains (up to 15%) and increased stability in learning across various tasks such as Sokoban, FrozenLake, and WebShop, while remaining optimizer-agnostic. This approach shifts the search process from inference to the training stage, thereby providing a robust framework to bolster multi-turn agent capabilities and complementing existing selection methods.


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


> The paper introduces the FLCOA framework to explore how cooperation and coordination develop among autonomous LLM-based multi-agent systems (LLM-MAS), emphasizing the often-overlooked influence of lower-layer factors like communication delays. Through simulations of a Continuous Prisoner's Dilemma with varying communication delays, the study reveals that while increased delays initially promote exploitation of slower responses, excessive delays ultimately enhance mutual cooperation, highlighting a U-shaped relationship. These findings suggest that effective cooperation in LLM-MAS requires a comprehensive approach that integrates both high-level design and low-level resource considerations.


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


> The paper presents AmbiBench, a novel benchmark for evaluating Mobile GUI Agents that addresses the realistic challenges of user instructions which are often unclear or incomplete. Utilizing a taxonomy of instruction clarity derived from Cognitive Gap theory, the researchers developed a comprehensive dataset and an evaluation framework called MUSE, which employs a multi-agent architecture for detailed analysis of agent performance in various interaction scenarios. Key findings indicate that this benchmark reveals performance limitations of state-of-the-art agents and highlights the importance of active user-agent interaction to enhance intent alignment.


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


> The paper presents AIR, the first incident response framework specifically designed for large language model (LLM) agent systems, addressing the gap in capabilities to manage incidents post-failure. The methodology includes a domain-specific language integrated into the agent's execution loop for detecting incidents, guiding actions for containment and recovery, and synthesizing guardrail rules to prevent future occurrences. Key findings indicate that AIR achieves over 90% success rates in detection, remediation, and eradication, demonstrating the feasibility and necessity of incorporating incident response as a fundamental mechanism for enhancing the safety of agentic AI systems.


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


> The paper presents PhyNiKCE, a neurosymbolic framework designed to enhance the reliability of autonomous agents in Computational Fluid Dynamics (CFD) by addressing the limitations of Large Language Models (LLMs) in enforcing strict physical laws. The methodology involves decoupling neural planning from symbolic validation, utilizing a Symbolic Knowledge Engine to frame simulation setups as Constraint Satisfaction Problems, and employing a Deterministic RAG Engine for ensuring compliance with physical constraints. Key findings indicate that PhyNiKCE achieves a 96% relative improvement over existing methods in CFD tasks, decreases self-correction loops by 59%, and reduces LLM token consumption by 17%, thereby demonstrating its potential as a scalable solution for Trustworthy AI in diverse industrial applications.


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


> The paper explores the behavioral consistency of LLM-based agents, revealing significant variability in their responses to identical tasks, which diminishes performance reliability. Analyzing 3,000 runs across three models, the study finds that high variance in action sequences correlates with poorer task accuracy, with consistent behaviors scoring 80-92% compared to 25-60% for inconsistent ones. Key findings indicate that divergence largely originates from early decisions, particularly the first search query, suggesting that monitoring for consistency could be a strategy to enhance agent reliability in agentic AI systems.


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


> This survey paper explores multi-agent communication (MA-Comm) by examining the dynamics of communication through the framework of the Five Ws: who communicates, what is communicated, when, and why. It traces the evolution of communication approaches from Multi-Agent Reinforcement Learning (MARL) to Emergent Language (EL) and large language models (LLMs), highlighting the limitations of existing methods—such as task-specific protocols in MARL and grounding issues in EL—that have inspired the integration of LLMs for improved reasoning and collaboration. The authors provide insights into design patterns and identify unresolved challenges for future systems that aim to merge learning, language, and control, ultimately contributing to the field of agentic AI by emphasizing the importance of effective communication in multi-agent systems.


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


> The paper introduces ARC (Agentic Resource & Configuration learner), a reinforcement learning-based approach for dynamically configuring LLM-based agent systems by treating agent configuration as a query-wise decision problem. The methodology involves developing a hierarchical policy that customizes workflows, tools, and prompts, resulting in improvements in task accuracy by up to 25% compared to traditional fixed templates and hand-tuned heuristics, while also reducing computational costs. The key findings highlight that learning tailored configurations for individual queries significantly enhances the performance and efficiency of agentic AI systems, providing a compelling alternative to rigid, one-size-fits-all design strategies.


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


> The paper presents CausalAgent, a conversational multi-agent system designed to automate end-to-end causal inference, thereby simplifying the process for users who may lack extensive technical backgrounds. By integrating Multi-Agent Systems, Retrieval-Augmented Generation, and the Model Context Protocol, it allows users to initiate causal analysis through natural language queries after simply uploading their datasets. Key findings indicate that CausalAgent enhances user accessibility and interaction in causal analysis while maintaining rigorous standards of interpretation and reporting, showcasing a novel approach to human-AI collaboration in the agentic AI field.


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


> The paper introduces AgentLeak, a pioneering benchmark designed to assess privacy leakage in multi-agent Large Language Model (LLM) systems by evaluating internal communication channels across 1,000 scenarios in various sensitive domains. The methodology involves a detailed attack taxonomy and a three-tier detection pipeline, revealing that while multi-agent configurations reduce output leakage, they significantly increase total system exposure due to unmonitored internal channels, highlighting that inter-agent messages pose a substantial privacy risk. Key findings indicate that existing output-only audits fail to identify a notable portion of privacy violations, suggesting the necessity for enhanced frameworks that prioritize internal-channel privacy and inter-agent communication controls in agentic AI systems.


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


> The paper presents a novel framework for fair consensus clustering in streaming environments, addressing limitations of previous offline approaches that require extensive memory. The authors develop a constant-factor algorithm capable of processing sequential clustering inputs while only retaining a logarithmic amount of data. The key findings demonstrate that their framework not only improves approximation guarantees for streaming data but is also versatile enough to apply to various fairness definitions and extends to the k-median consensus clustering problem, thereby contributing to the field of agentic AI by enhancing fairness and efficiency in multi-agent clustering scenarios.


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


> The paper presents Distributionally Robust Individual-Global-Maximum (DrIGM), a framework designed to enhance cooperative multi-agent reinforcement learning (MARL) by addressing the unreliability of existing value-factorization methods in real-world scenarios. The methodology involves deriving robust variants of well-known value-factorization architectures that operate on robust action values and are compatible with decentralized execution, providing a robustness guarantee for the system. Key findings indicate that the proposed DrIGM framework significantly improves out-of-distribution performance in complex environments, such as SustainGym simulators and StarCraft, while maintaining scalability and integration ease with existing systems.


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


> The paper "Optimizing Agent Planning for Security and Autonomy" presents a novel security-aware agent design aimed at improving autonomy while ensuring safety against indirect prompt injection attacks. The methodology involves enhancing human-in-the-loop (HITL) interactions and incorporating explicit planning for both task accomplishment and adherence to policies, evaluated using the AgentDojo and WASP benchmarks. Key findings reveal that the proposed approach increases the autonomy of agents—measured by the fraction of consequential actions they can undertake without human approval—while maintaining their operational effectiveness, thus highlighting the potential of system-level defenses to reduce the need for human oversight in agentic AI systems.


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


> The paper investigates the impact of social proof and delayed verification in discussions surrounding agentic AI, revealing a "Popularity Paradox" where high-visibility conversations often lack timely verification cues. Utilizing a right-censored survival analysis framework on Reddit data from two different communities, the study finds that prominent, unverified claims can reinforce cognitive biases due to a phenomenon called "Narrative Lock-in." The authors suggest that this credibility-by-visibility effect poses risks for AI safety and propose the concept of "epistemic friction" as a potential intervention to mitigate these issues in engagement-driven platforms.


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


> The paper introduces TRACER, a novel trajectory-level uncertainty metric designed for AI agents engaged in multi-turn interactions with humans in tool-using scenarios. By integrating content-aware surprisal with various situational-awareness signals and using a tailored risk aggregation approach, TRACER significantly enhances the detection of critical failure episodes that traditional single-shot uncertainty metrics overlook. Key findings demonstrate that TRACER outperforms existing methods, achieving improvements of up to 37.1% in AUROC and 55% in AUARC, facilitating more precise and timely identification of uncertainties in complex agentic reasoning contexts.


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


> The paper presents ReplicatorBench, a comprehensive benchmarking framework designed to evaluate AI agents' capabilities in the replication of scientific research, particularly in the social and behavioral sciences. The methodology involves a three-stage process that assesses agents' performance in extracting data, executing experiments, and interpreting results, addressing previous benchmarks that overlooked non-replicable research and the variability of data availability. Key findings indicate that while the tested LLM agents, accessed via the developed framework ReplicatorAgent, are proficient at experimental design and execution, they face significant challenges in resource retrieval, highlighting a critical gap in their ability to perform successful research replication.


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


> The paper introduces Behavioral Agentic Optimization (BAO), a novel reinforcement learning framework designed to enhance proactive large language model (LLM) agents by improving their reasoning and information-gathering capabilities while aligning their interactions with user expectations. The methodology involves integrating behavior enhancement and regularization techniques to address the challenges of balancing task performance and user engagement in multi-turn interaction scenarios. Key findings demonstrate that BAO significantly surpasses existing proactive agentic RL baselines and achieves performance on par with, or better than, commercial LLM agents, indicating its potential for developing effective user-centric agentic AI systems.


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


> The paper introduces AgentNoiseBench, a novel framework designed to evaluate the robustness of tool-using large language model (LLM) agents in noisy environments, addressing the gap between idealized benchmark performance and real-world applications. The methodology involves categorizing environmental noise into user-noise and tool-noise, followed by the development of an automated pipeline to inject controllable noise into existing benchmarks while maintaining task solvability. Key findings demonstrate that current agentic models exhibit significant performance sensitivity to various noise conditions, underscoring the need for improved robustness in future AI agent designs.


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


> The paper contributes to the field of agentic AI by providing a systematic security analysis of four emerging AI agent communication protocols: MCP, A2A, Agora, and ANP. It develops a structured threat modeling framework that examines each protocol's architecture and identifies twelve specific risks, assessing their security posture throughout different operational phases. Key findings reveal critical design-induced risks that could impact secure deployment; specifically, the case study on MCP quantifies an important vulnerability regarding executable component validation, offering insights for enhanced security practices and standardization in AI agent communication.


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


> The paper presents the Practitioners Blueprint for Secure AI (PBSAI) Governance Ecosystem, a comprehensive multi-agent reference architecture aimed at enhancing security in enterprise AI estates amid the growing deployment of complex AI systems. The methodology involves organizing security responsibilities into a twelve domain taxonomy, defining agent families that bridge tools and policies, and employing key security techniques such as analytic monitoring and adaptive response. Key findings illustrate how PBSAI aligns with existing governance frameworks like the NIST AI Risk Management Framework and demonstrates practical applications in enterprise security operations and defensive environments, underscoring its potential as a structured foundation for future development and validation in agentic AI research.


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


> The paper presents Attention-Enhanced Multi-Agent Proximal Policy Optimization (AE-MAPPO), a novel framework designed to effectively manage latency spikes in 6G radio access networks by integrating six specialized attention mechanisms for improved interpretability and decision-making. Through a three-phase strategy of predictive, reactive, and inter-slice optimization, AE-MAPPO demonstrated its effectiveness in a URLLC case study, resolving latency spikes within 18 ms and achieving a reliability rate of 99.9999%, while significantly reducing troubleshooting time by 93%. The findings highlight AE-MAPPO's capability to enforce service-level agreements while providing clear, interpretable decision processes, reinforcing its applicability in agentic AI systems for real-time automation.


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


> The paper introduces StructMemEval, a benchmark designed to evaluate the organizational capabilities of long-term memory in LLM-based agents beyond simple fact retention. Methodologically, it involves a suite of tasks that require agents to structure knowledge similarly to human cognitive strategies, such as using transaction ledgers and to-do lists. The key findings indicate that while memory agents excel when guided on how to organize their memory, standard retrieval-augmented LLMs struggle with these tasks, emphasizing a need for improved training and memory architectures in agentic AI systems.


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


> The paper presents Pram, an innovative ML-based method that utilizes multimodal language models (MLMs) to address the multi-commodity flow (MCF) problem, effectively balancing optimality and tractability in complex network scenarios. By dividing the MCF problem into local subproblems solved by an MLM-powered agent and ensuring global consistency through a multi-agent reinforcement learning algorithm, Pram achieves high-quality allocations while demonstrating significantly faster runtimes than traditional linear programming solvers. Empirical results indicate that Pram not only approaches optimal solutions but also maintains robustness against disruptions, making it a practical and scalable option for modern allocation challenges in agentic AI systems.


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


> The paper introduces SurveyLens, the first discipline-aware benchmark designed to evaluate Automatic Survey Generation (ASG) methods across various academic fields, addressing the limitations of existing evaluations that primarily focus on Computer Science. The authors developed SurveyLens-1k, a dataset of 1,000 high-quality surveys from ten disciplines, and employed a dual-lens evaluation framework that includes a Discipline-Aware Rubric Evaluation using large language models (LLMs) and a Canonical Alignment Evaluation for content quality assessment. Key findings show that the evaluation of 11 ASG methods unveils distinct strengths and weaknesses across different disciplines, offering valuable insights for choosing ASG tools suitable to specific academic standards.


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


> The paper presents "Chain-of-Look," a novel visual reasoning framework designed to enhance the accuracy of counting densely packed surgical instruments in operating rooms. The methodology involves creating a structured visual chain that mimics the sequential human counting process, coupled with a neighboring loss function to enforce spatial constraints. Key findings indicate that this approach significantly outperforms existing state-of-the-art methods and multimodal large language models in accurately counting surgical instruments, thereby contributing valuable insights to the field of agentic AI in complex visual tasks.


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


> The paper introduces TVCACHE, a stateful tool-value caching system designed to enhance the efficiency of post-training large language model (LLM) agents by caching tool outputs based on observed tool-call sequences that maintain environmental state. Employing a longest-prefix matching methodology for cache lookups, TVCACHE achieves significant performance improvements, with hit rates reaching 70% and median tool call execution times reduced by up to 6.9 times, without compromising the agents’ reward accumulation during training. These findings demonstrate the potential for reducing training costs and time in the field of agentic AI, particularly in scenarios where external tool utilization is prevalent.


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


> The paper presents a novel framework, CMAD, which formulates the composition of multiple pre-trained diffusion models as a cooperative Stochastic Optimal Control problem, allowing for a more effective method of generating compositions without the need for explicit target distributions. The methodology involves treating the diffusion models as interacting agents that jointly navigate their diffusion trajectories toward a shared output objective. Key findings indicate that CMAD outperforms traditional methods, such as naive inference-time approaches that rely on simple gradient guidance, in generating meaningful results on conditional MNIST tasks, thus advancing the field of agentic AI by enhancing inter-agent cooperation in generative tasks.


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


> The paper introduces Aura, a secure, intent-centric mobile agent operating system designed to address vulnerabilities associated with the current "Screen-as-Interface" paradigm. Through a systematic security analysis of mobile agents, particularly the Doubao Mobile Assistant, the authors identified critical flaws like fake App identities and unauthorized privilege escalations. Aura employs a Hub-and-Spoke architecture along with four key defense mechanisms, resulting in significant improvements in task success rates and security, illustrating its potential as a robust framework for future agentic AI systems.


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


> The paper introduces Agent-Diff, a benchmarking framework designed to evaluate agentic Large Language Models (LLMs) on enterprise API tasks by executing code with a state-diff-based evaluation approach. The methodology combines access to real API interfaces within a controlled sandbox environment, utilizing a state-diff contract to define task success based on the expected changes in the environment state rather than just output matching. Key findings include benchmarks for nine LLMs across 224 tasks, demonstrating the framework’s effectiveness in assessing model performance while providing insights on the impact of API documentation access on outcomes, thereby contributing to the understanding of LLM capabilities in real-world agentic scenarios.


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


> The paper introduces PSTCTL, a probabilistic extension of Strategic Timed CTL (STCTL) designed for stochastic multi-agent systems operating under continuous time and asynchronous semantics. The methodology involves defining this new logic and demonstrating its verification capabilities using irP-strategies, which are intended to support strategic decision-making in probabilistic settings. Key findings indicate that PSTCTL enhances the expressiveness of modeling temporal and strategic behavior in multi-agent systems, contributing to the development of agentic AI frameworks that incorporate probabilistic reasoning and strategy formulation in dynamic environments.


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


> The paper introduces ScratchWorld, a benchmark designed for evaluating multimodal GUI agents in Scratch, addressing the gap in assessing AI agents' abilities to construct programs via graphical interfaces. Utilizing the Use-Modify-Create pedagogical framework, ScratchWorld consists of 83 tasks across various categories and employs two interaction modes to diagnose agent failures. Key findings demonstrate a significant reasoning-acting gap in current multimodal language models and GUI agents, indicating challenges in fine-grained GUI manipulation despite their strong planning abilities.


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


> The paper presents the Locomo-Plus benchmark, designed to evaluate long-term conversational memory in LLM-based dialogue systems, addressing the limitations of existing frameworks that focus primarily on factual recall. The methodology emphasizes the assessment of cognitive memory by examining the retention and application of implicit user constraints in lengthy conversations, rather than relying on traditional string-matching metrics. Key findings indicate significant challenges in cognitive memory performance across various models and methods, highlighting failures that are not accounted for by current evaluation standards, thus contributing valuable insights to the agentic AI field.


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


> The paper presents a novel framework for analyzing cooperation in heterogeneous multi-agent systems operating under conditions of partial observability and temporal role dependencies, specifically in a destructive foraging context. It introduces a comprehensive set of general-purpose cooperation metrics that evaluate efficiency, coordination, dependency, fairness, and sensitivity, structured into primary, inter-team, and intra-team categories. Key findings from the validation of these metrics in a realistic scenario involving autonomous vehicles highlight their transferability to various multi-agent sequential domains and emphasize the complexity of cooperative behaviors beyond mere task performance.


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


> The paper introduces the Unified Memory Extraction and Management (UMEM) framework, which enhances Large Language Models (LLMs)-based agents by simultaneously optimizing memory extraction and management, addressing the limitations of existing methods that inadequately handle memory generalization. The methodology incorporates Semantic Neighborhood Modeling and a neighborhood-level marginal utility reward, enabling the model to evaluate memory utility across semantically related queries, thus reducing overfitting to specific instances. Key findings reveal that UMEM significantly improves performance on multi-turn interactive tasks, achieving up to a 10.67% enhancement compared to competitive baselines, and demonstrates consistent progress in memory quality during continuous evolution.


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


> The paper introduces Co-jump, a novel cooperative jumping task for two quadrupedal robots that utilizes Multi-Agent Reinforcement Learning (specifically MAPPO) to achieve synchronized jumps exceeding their individual capabilities, without explicit communication. The methodology incorporates a progressive curriculum strategy to tackle challenges related to sparse rewards in high-impulse dynamics. Key findings demonstrate that the collaborative approach enables robots to perform jumps up to 1.5 m high, with one robot achieving a 1.1 m elevation, marking a 144% improvement over solo performance, and highlighting the potential for communication-free locomotion in agentic AI settings.


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


> The paper presents "authenticated workflows," a novel approach to securing agentic AI systems by implementing a comprehensive trust layer that safeguards prompts, tools, data, and context within enterprise workflows. The methodology involves enforcing intent and integrity through cryptographic proofs and real-time policy enforcement, leveraging a new AI-native policy language (MAPL) for dynamic constraint management. Key findings demonstrate the system's effectiveness, achieving 100% recall and zero false positives across various test cases while addressing critical security vulnerabilities, thus offering deterministic security against prominent threats in the agentic AI domain.


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


> The paper presents a systematic overview of Prompt Injection (PI) vulnerabilities in Large Language Model (LLM) agents, outlining a taxonomy of PI attacks and defenses. Utilizing a systematic literature review and quantitative analysis, the authors identify shortcomings in current benchmarks related to context-dependent tasks and introduce AgentPI, a benchmark aimed at evaluating agent behavior in realistic scenarios. Key findings highlight that existing defenses fail to simultaneously achieve high trustworthiness, utility, and low latency, and often do not generalize well when faced with contextual reasoning required in practical deployments.


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


> The paper introduces LiveMedBench, a novel, contamination-free medical benchmark for evaluating Large Language Models (LLMs) in clinical contexts, addressing critical issues of data contamination and temporal misalignment. Utilizing a Multi-Agent Clinical Curation Framework, LiveMedBench continuously gathers real-world medical cases while maintaining strict separation from training data, and employs an Automated Rubric-based Evaluation Framework to assess model performance against granular expert-defined criteria. Key findings indicate that even top-performing models struggle with contextual application, showcasing a significant performance drop on newer cases and highlighting the need for improved alignment with specific patient scenarios.


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


> The paper presents a self-evolving recommendation system that utilizes Large Language Models (LLMs) to autonomously optimize machine learning models, particularly for large-scale video platforms. The methodology features an Offline Agent that generates hypotheses using proxy metrics and an Online Agent that validates these against long-term business metrics, effectively simulating the role of Machine Learning Engineers. Key findings indicate that this autonomous approach significantly enhances optimization and model performance, as evidenced by successful deployments at YouTube, demonstrating that LLM-driven systems can outperform traditional optimization workflows.


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


> The paper introduces the Agent World Model (AWM), a novel synthetic environment generation pipeline designed to enhance agentic reinforcement learning by providing a diverse range of 1,000 code-driven environments tailored for multi-turn interactions using complex toolsets. AWM's methodology focuses on creating reliable and consistent state transitions supported by databases, which allows for efficient agent training and the development of robust reward mechanisms. Key findings demonstrate that agents trained exclusively in these synthetic environments exhibit strong out-of-distribution generalization, outperforming those trained in benchmark-specific settings.


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


> The paper introduces Anagent, a multi-agent framework designed to improve the analysis of scientific tables and figures, addressing the limitations of current AI systems in interpreting complex multimodal data. Utilizing the newly developed benchmark, AnaBench, which categorizes 63,178 instances across nine scientific domains, Anagent employs four specialized agents to systematically decompose tasks, retrieve specific information, synthesize data, and iteratively refine outputs. The findings highlight substantial performance gains in scientific analysis, demonstrating that the integration of task-oriented reasoning and context-aware problem-solving significantly enhances capabilities in this domain.


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


> The paper introduces the Topology-Aware Graph MAPPO (TAG-MAPPO) framework aimed at enhancing the resilience of 3D Aerial-Ground Integrated Networks (AGINs) in the face of node failures, a significant concern for mission-critical applications. By employing a graph-based feature aggregation approach and a residual ego-state fusion mechanism, TAG-MAPPO allows UAVs to autonomously reconfigure their topology, leading to improved adaptability compared to conventional methods. Key findings indicate that this framework can restore over 90% of service coverage after a failure within 15 time steps, significantly reduce redundant handoffs, and achieve better fairness metrics in service distribution, thereby underscoring the importance of topology-aware coordination for resilient agentic AI applications in future 6G networks.


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


> The paper introduces the Multi-Agent Safety Shield (MASS), which combines safety and traffic efficiency in Connected and Autonomous Vehicles (CAVs) during lane changes in congested environments. By utilizing Control Barrier Functions (CBFs) and multi-agent interaction topologies, the methodology incorporates a state-of-the-art Multi-Agent Reinforcement Learning (MARL) controller, resulting in a new lane change controller called MARL-MASS. Key findings indicate that MASS ensures safe, collaborative lane changes while significantly enhancing the stability of MARL policies and achieving a balance between safety constraints and traffic efficiency.


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


> This paper identifies and analyzes systemic failures in AI agents tasked with automated Root Cause Analysis (RCA) for cloud systems, highlighting the limitations of current LLM-based approaches. The methodology involved executing the OpenRCA benchmark across five LLM models, classifying the failures into twelve pitfall categories related to agent reasoning, communication, and interaction. Key findings indicate that prevalent issues, such as hallucinated data interpretation and incomplete exploration, stem from shared architectural flaws rather than model-specific weaknesses, and that enhancements in inter-agent communication can significantly reduce these failures, offering a path towards more reliable agentic AI for RCA tasks.


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


> The paper examines the limits of safety in self-evolving multi-agent systems constructed from large language models, highlighting an inherent conflict known as the self-evolution trilemma, which posits that continuous self-improvement, isolation, and safety cannot coexist indefinitely. Employing both theoretical analysis and empirical observations from a system called Moltbook, the authors demonstrate that isolated self-evolution leads to statistical blind spots that irreversibly compromise safety alignment. The findings underscore the necessity for external oversight or innovative safety mechanisms to mitigate intrinsic risks, marking a significant contribution to the understanding of safety in agentic AI systems.


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


> The paper "Tiny Moves: Game-based Hypothesis Refinement" introduces The Hypothesis Game, a novel framework for hypothesis refinement that utilizes a symbolic formalism where LLM agents collaborate on a shared hypothesis state through structured reasoning moves. This approach emphasizes incremental revisions reflective of scientific reasoning, demonstrating superior performance in error removal and precision during corruption recovery tasks compared to traditional prompting methods. Key findings indicate that this game-based methodology provides a more controllable and interpretable system for hypothesis refinement, supporting its potential application in agentic AI for enhancing scientific discovery.


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


> The paper presents MATA, a multi-agent framework aimed at improving the reliability and scalability of Table Question Answering (TableQA) by utilizing a combination of small language models and diverse reasoning styles. The methodology involves generating multiple candidate answers from different reasoning approaches and refining these using specialized tools, while also minimizing calls to larger language models to enhance efficiency. Key findings indicate that MATA achieves state-of-the-art accuracy across multiple benchmarks and demonstrates that strategic coordination of various reasoning pathways can lead to scalable and reliable TableQA solutions, making it particularly suitable for resource-constrained environments.


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


> The paper introduces Error-Localized Policy Optimization (ELPO), a novel approach for enhancing tool-integrated reasoning (TIR) in large language model (LLM) agents by addressing the challenges of sparse rewards and weak credit assignment in long-horizon tasks. ELPO employs binary-search rollout trees to identify the first irrecoverable error within a given rollout budget, converting this information into effective learning signals through hierarchical advantage attribution and adaptive clipping for improved correction on critical decision points. The methodology demonstrates significant improvements in performance across various TIR benchmarks, outperforming existing agentic reinforcement learning baselines while maintaining efficient tool call usage, thereby advancing the capabilities of LLM agents in complex reasoning scenarios.


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


> The paper presents FlexMARL, a novel end-to-end training framework specifically designed to optimize the challenges of large-scale multi-agent reinforcement learning (MARL), particularly for large language models (LLMs). The methodology integrates a joint orchestrator, an asynchronous micro-batch pipeline, and a parallel sampling scheme to enhance rollout and training orchestration while addressing synchronization barriers and resource utilization issues. Key findings indicate that FlexMARL significantly improves training efficiency, achieving up to 7.3 times speedup and enhancing hardware utilization by up to 5.6 times compared to existing MARL frameworks, thereby advancing the capabilities of agentic AI systems.


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


> The paper presents SpotAgent, a novel framework that enhances geo-localization using large Vision-Language Models (LVLMs) through agentic reasoning and tool-assisted verification. SpotAgent employs a three-stage post-training pipeline, which includes supervised fine-tuning, a cold start phase utilizing high-quality trajectories from a multi-agent framework, and reinforcement learning, complemented by a dynamic filtering strategy to improve efficiency. Key findings indicate that SpotAgent significantly reduces errors in geo-localization, achieving state-of-the-art performance while ensuring predictions are grounded and verifiable, thus advancing the agentic AI field by merging visual analysis with expert-level reasoning.


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


> This paper presents SWE-AGI, an open-source benchmark designed to evaluate the capability of LLM-based agents in autonomously constructing production-scale software from explicit specifications using the MoonBit language. The methodology involves testing agents on complex software engineering tasks that require substantial implementation effort while minimizing data leakage to promote architectural reasoning. Key findings indicate that while the best-performing model, gpt-5.3-codex, successfully solves the majority of tasks, performance declines significantly with increasing task complexity, highlighting the challenges of scaling AI-assisted software development and indicating that code comprehension becomes a critical bottleneck as projects enlarge.


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


> The paper introduces Autonomous Action Runtime Management (AARM), a novel specification designed to enhance the security of AI-driven actions during runtime, addressing the limitations of traditional security approaches that are inadequate for autonomous agents executing irreversible actions at machine speed. AARM comprises a runtime security system that intercepts actions, evaluates them against policies, and enforces authorizations, while also outlining a framework for classifying actions and formalizing a comprehensive threat model. Key findings highlight AARM’s ability to provide a model-agnostic and vendor-neutral approach, ensuring interoperability and setting minimum conformance requirements to secure AI systems effectively against threats like prompt injection and intent drift.


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


> The paper presents a comprehensive textbook aimed at systematically addressing the control principles of multi-agent systems (MAS), a topic of growing significance since the early 2000s across various applications like autonomous vehicles and smart grids. The methodology involves a structured approach divided into three parts: foundational concepts of MAS and graph theory, linear consensus algorithm design and analysis, and relevant applications such as formation control and distributed optimization. Key findings highlight the importance of accessible educational resources in the field, providing readers with step-by-step analyses while connecting them to ongoing research and prominent figures in the MAS domain, ultimately contributing to the advancement of agentic AI through practical learning.


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


> The paper introduces RVMS-Bench, a novel benchmark designed for evaluating video retrieval systems by addressing the limitations of traditional closed-pool evaluations, focusing instead on real-world searchable videos characterized by fuzzy memories. By employing a hierarchical description framework and a human-verified sample set across diverse video categories, the study highlights the introduction of RACLO, an agentic framework that simulates human-like reasoning to enhance video search tasks. Experimental results illustrate that current models struggle with real-world video retrieval and moment localization, emphasizing the need for improved robustness in handling vague search criteria in unstructured environments.


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


> The paper introduces LingxiDiagBench, a comprehensive multi-agent benchmark designed to assess large language models (LLMs) in the context of Chinese psychiatric diagnosis and consultation. Utilizing a dataset of 16,000 synthetic consultation dialogues aligned with electronic medical records, the study evaluates LLM performance in both static diagnostic tasks and dynamic multi-turn dialogues. Key findings highlight a significant drop in accuracy for comorbidity recognition and differential diagnosis compared to binary classification, indicate that dynamic consultations can hinder diagnostic reasoning, and reveal that well-structured questioning does not guarantee accurate diagnoses, underlining critical challenges in AI-assisted psychiatric assessment.


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


> The paper introduces LaPha, a novel method for training AlphaZero-like language model agents within a Poincaré latent space, enhancing their search process through a tree structure influenced by the properties of negative curvature. The methodology involves using hyperbolic geodesic distances to define node potential and assigning rewards based on potential differences, supplemented by a lightweight value head for efficient self-guided scaling. Key findings indicate that LaPha significantly boosts performance, elevating the accuracy of Qwen2.5-Math-1.5B from 66.0% to 88.2% on MATH-500 and achieving 60.0% on AIME'24 with a larger model, highlighting its effectiveness in improving agentic AI capabilities in complex tasks.


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


> The paper presents AgentSkiller, a novel framework designed to enhance generalist agent intelligence by synthesizing multi-turn interaction data from semantically integrated, cross-domain sources. Utilizing a DAG-based architecture and a domain ontology, AgentSkiller automates the creation of realistic environments equipped with consistent databases and tool interfaces, enabling effective simulation and training of AI agents. Experimental results show that models trained on the generated dataset significantly outperform baseline models in function calling, particularly benefiting larger parameter settings, thus addressing the data scarcity challenges in agentic AI.


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


> The paper introduces AgentCgroup, an eBPF-based resource control mechanism designed to manage OS resource dynamics for AI agents operating in cloud environments, addressing inefficiencies observed in traditional resource management frameworks. Through extensive analysis of 144 software engineering tasks utilizing two LLM models, the study finds that OS-level execution significantly contributes to task latency, with memory being the primary bottleneck and resource demands proving highly unpredictable. The proposed solution effectively resolves mismatches between existing resource controls and the unique demands of AI agents, leading to improved multi-tenant isolation and reduced resource waste.


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


> The paper introduces AgentAuditor, a novel approach that enhances decision-making in multi-agent systems (MAS) by utilizing a Reasoning Tree to represent and analyze the evidential structure of agent outputs, moving beyond the traditional majority voting method. The methodology involves a localized verification process that resolves conflicts at critical divergence points and employs Anti-Consensus Preference Optimization (ACPO) to prioritize evidence-based minority choices in cases where majority consensus is misleading. Key findings reveal that AgentAuditor improves accuracy by up to 5% over majority voting and 3% over using an LLM as a judge across five different settings, demonstrating its effectiveness in fostering more reliable reasoning in agentic AI applications.


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


> The paper presents a large-scale computational thematic analysis of user discourse from Reddit communities focused on AI-related harm, employing a multi-agent, LLM-assisted approach grounded in Braun and Clarke's reflexive framework. The study identifies 14 thematic categories related to psychological risks associated with AI use, synthesizing them into five experiential dimensions, with self-regulation difficulties and fears around autonomy and control being prominent. These findings contribute to the agentic AI field by providing empirical insights into users' emotional experiences and perceptions of AI safety, supporting future research and governance in AI systems.


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


> The main contribution of the paper is the introduction of the FM SO.P framework, which enhances cross-domain Standard Operating Procedure (SOP) understanding through progressive task mixtures and an automatic evaluation system. The methodology involves a staged approach to skill development across tasks focusing on terminology disambiguation, sequential action understanding, and scenario-aware reasoning, combined with an adaptive multi-agent evaluation system that utilizes dynamic rubric generation. Key findings indicate that FM SO.P significantly improves performance in SOP comprehension across multiple domains, achieving competitive pass rates with fewer parameters compared to existing models, thereby advancing capabilities relevant to agentic AI systems.


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


> The main contribution of the paper is the comparative analysis of two Reddit communities, r/OpenClaw and r/Moltbook, which highlights the divergence in oversight expectations for agentic AI based on community roles. Utilizing topic modeling and various statistical methods, the authors establish that while "human control" serves as a common anchor term, its interpretation varies significantly: r/OpenClaw focuses on practical execution and risk management, whereas r/Moltbook emphasizes identity, legitimacy, and public accountability. These findings suggest that oversight mechanisms should be tailored to specific agent roles rather than relying on uniform control policies, advancing the discourse on governance in agentic AI systems.


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


> The paper investigates the collective behavior of AI agents on the social media platform Moltbook, analyzing a substantial dataset of posts and comments to uncover statistical patterns in their interactions. The researchers employed a large-scale data analysis methodology, revealing that AI agents exhibit similarities to human online communities, including activity distributions and attention dynamics, yet also display significant differences, such as the nature of engagement metrics. Key findings indicate that while AI agents' individual behaviors differ from humans, their collective dynamics exhibit structural similarities to those of human social systems, contributing valuable insights to the understanding of agentic AI behavior.


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


> The paper presents AIDev, a comprehensive dataset that captures the use of AI coding agents in real-world software engineering projects on GitHub, comprising 932,791 agent-authored pull requests from various agents such as OpenAI Codex and GitHub Copilot. The methodology involves aggregating data from 116,211 repositories, along with a focused subset of well-received Agentic-PRs, to analyze interactions between AI agents and human developers. Key findings highlight the significant role of AI coding agents in enhancing developer productivity and collaboration, thereby providing a vital resource for future research in AI and agent systems within software engineering.


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


> The paper introduces FlyBench, a new benchmark designed to evaluate AI agents on the comprehensive task of ontology curation from scientific literature, specifically within the context of Drosophila research. The methodology involves AI agents retrieving and analyzing a large corpus of 16,898 full-text papers to generate structured annotations related to gene functions, expressions, and historical nomenclature, utilizing a set of 7,397 expert-curated labels. Key findings indicate that multi-agent architectures significantly outperform simpler models, although all tested architectures showed room for improvement; notably, agents tend to rely more on retrieval of existing knowledge rather than uncovering new insights, which highlights challenges in enhancing AI-driven scientific reasoning capabilities.


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


> The paper introduces CoMMa, a decentralized multi-agent framework designed for oncology decision support, which leverages a game-theoretic approach to enhance robust decision-making among specialists working with fragmented patient data. Unlike traditional stochastic methods, CoMMa utilizes deterministic embedding projections for contribution-aware credit assignment, allowing for clearer evidence attribution and improved stability in decision pathways. Experimental results demonstrate that CoMMa outperforms both data-centralized and role-based multi-agent systems in accuracy and stability across various oncology benchmarks, including a real-world multidisciplinary tumor board dataset.


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


> The paper introduces Progress-Aware Belief Update (PABU), a novel framework designed to optimize the operational efficiency of Large Language Model (LLM) agents by selectively retaining important actions and observations based on task progress. The methodology involves modeling an agent's state with a focus on its progress, allowing it to predict the relevance of new interactions for future decisions. Key findings demonstrate that PABU significantly enhances task completion rates and reduces interaction steps, achieving an 81.0% completion rate while outperforming previous state-of-the-art methods by a notable margin and promoting more efficient resource usage in LLM agents.


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


> The paper introduces SciDataCopilot, an autonomous agentic framework that extends the AI-Ready concept to a Scientific AI-Ready data paradigm, addressing the challenges associated with raw experimental data in AI for Science (AI4S). The methodology involves an automated process for data ingestion, intent parsing, and multi-modal integration, enhancing the usability and efficiency of scientific data within computational workflows. Key findings indicate that SciDataCopilot significantly improves efficiency and scalability in data preparation, achieving up to a 30-fold speedup compared to traditional manual processes, thereby facilitating progress toward experiment-driven Artificial General Intelligence for Science (AGI4S).


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


> The paper presents a novel framework that enables multi-agent reinforcement learning (MARL) agents to utilize shared quantum entanglement as a coordination resource, improving upon previous methods that relied solely on shared randomness. The methodology involves a differentiable policy parameterization for optimizing quantum measurements along with a novel architecture that separates joint policies into a quantum coordinator and decentralized local actors. Key findings indicate that this approach allows agents to learn strategies that achieve a quantum advantage, outperforming traditional communication-free correlated policies in both single-round cooperative games and decentralized partially observable Markov decision processes.


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


> The paper presents a novel framework for evaluating goal-directedness in language model agents by combining behavioral assessments with analyses of internal representations. Using a case study of an LLM agent navigating a 2D grid, the authors demonstrate that the agent's performance varies with task complexity and that it maintains robust goal-directed behavior, while probing methods reveal that its internal representations encode spatial maps and action plans in a non-linear manner. Key findings emphasize the need for introspective analyses alongside behavioral evaluations to better understand how agents represent and pursue their goals, which is critical for advancing agentic AI research.


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


> The paper presents the Intelligent Virtual Situation Room (IVSR), a novel bidirectional Digital Twin (DT) platform enhanced by autonomous AI agents to improve wildfire disaster management. The methodology involves continuous ingestion of multisource data to create a real-time virtual fire environment, employing a similarity engine to align current conditions with precomputed intervention strategies, thereby enabling quick responses to evolving wildfire scenarios. Key findings highlight significant reductions in detection-to-intervention latency and enhanced resource coordination, positioning IVSR as a scalable, semi-automated tool for proactive wildfire management in the agentic AI field.


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


> The paper introduces pixelLOG, a high-performance data collection framework for Minecraft servers that enhances cognitive research by enabling detailed tracking of both human and AI agent behavior in multi-agent environments. Utilizing a hybrid methodology of active polling and passive monitoring, pixelLOG operates at high frequencies to capture comprehensive behavioral data, producing structured outputs compatible with analytical tools. The key findings underscore its potential to provide rich, ecologically valid insights into cognitive processes, thereby advancing the study of agentic AI by integrating human interactions within complex virtual settings.


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


> The paper presents a novel approach to achieving last-iterate convergence in zero-sum games without the use of regularization, leveraging the Brown-von Neumann-Nash (BNN) dynamics and providing theoretical guarantees for both normal-form and extensive-form games. The authors develop a framework that incorporates counterfactual weighting to enhance applicability and implement an algorithm utilizing neural function approximation for scalable learning. Key findings indicate that this method effectively adapts to nonstationarities and outperforms existing regularization-based strategies, highlighting its potential relevance in advancing agentic AI systems.


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


> The paper presents Dr. MAS, a stable reinforcement learning (RL) method designed for multi-agent large language model (LLM) systems, addressing training instability caused by conventional group-based RL approaches. The authors identify that global normalization baselines can disrupt the reward distributions among diverse agents, leading to gradient-norm instability, and propose an agent-wise normalization strategy that stabilizes training across agents. Evaluations demonstrate that Dr. MAS significantly outperforms vanilla GRPO across multi-agent math reasoning and search tasks—showing improvements in performance metrics while also enhancing efficiency and adaptability in heterogeneous agent environments.


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


> The paper introduces "Scylla," an evaluation framework designed for benchmarking agentic coding tools, focusing on various architectural choices such as prompts and multi-agent setups. Utilizing structured ablation studies across seven testing tiers (T0-T6), Scylla emphasizes the Cost-of-Pass (CoP) as a key metric to quantify the trade-offs between complexity and efficiency in software development tasks. The findings indicate that increased architectural complexity does not necessarily correlate with improved quality, highlighting the framework's effectiveness in evaluating and optimizing agentic AI systems in coding.


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


> The paper introduces PRISM, a novel framework for enhancing multi-agent reasoning in Large Language Models (LLMs) by decomposing performance gains into three dimensions: Exploration, Information, and Aggregation. The methodology incorporates role-based diversity, execution-grounded feedback, and iterative synthesis, optimizing all three dimensions simultaneously. Key findings indicate that PRISM significantly outperforms existing methods across various benchmarks, offering not only improved performance but also greater computational efficiency, while providing actionable insights for the design of future multi-agent systems.


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


> The paper introduces ValueFlow, a novel framework for evaluating how value perturbations propagate within multi-agent large language model (LLM) systems, addressing the gap in understanding value alignment in agent interactions. The methodology incorporates a 56-value dataset based on the Schwartz Value Survey and employs an LLM-as-a-judge protocol to quantify agents' value orientations and analyze value drift through newly defined metrics: beta-susceptibility and system susceptibility. Key findings indicate that agents' sensitivity to value perturbations and the overall system outputs are significantly influenced by the structural topology of the multi-agent setup, highlighting the complexity of value dynamics in AI systems.


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


> This paper presents a novel approach for assessing long-term systemic risks associated with AI by combining simulations of in-silico agents using the Futures Wheel method with human expert judgment. The methodology involved running 30 simulations for four distinct AI applications, resulting in the identification of numerous potential consequences and risks, which were then evaluated against insights from domain experts and laypeople. Key findings indicate that while AI agents produced a wider array of systemic risks, human experts focused on fewer, more likely risks, and laypeople raised emotionally resonant concerns, suggesting a hybrid approach that leverages the strengths of both agents and human insights for more comprehensive risk assessment in AI.


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


> The paper investigates the automation of computational reproducibility in social science research by comparing prompt-based and agent-based workflows for diagnosing and repairing analysis failures. Using a controlled testbed of five reproducible R-based studies, the authors injected realistic errors and evaluated the effectiveness of both approaches. The key findings reveal that while prompt-based methods achieved varied success rates (31-79%), agent-based systems demonstrated significantly higher success (69-96%), indicating that agent-based approaches are more effective in automating repairs and enhancing reproducibility in computational research.


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


> The paper introduces EvoCorps, an innovative evolutionary multi-agent framework designed to proactively depolarize online discourse by treating governance as a dynamic social game involving monitoring, planning, and identity diffusion. Utilizing a retrieval-augmented collective cognition core and closed-loop evolutionary learning, EvoCorps adapts its strategies in real time to counteract adversarial amplification. Evaluation on the MOSAIC platform demonstrates that EvoCorps significantly enhances discourse outcomes related to emotional polarization, viewpoint extremity, and argumentative rationality compared to traditional adversarial baselines, marking a shift from reactive to proactive discourse management in the agentic AI field.


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


> The paper presents the Personalized Agent Security Bench (PASB), a comprehensive security evaluation framework designed for real-world personalized AI agents, focusing on large language model-based systems like OpenClaw. The authors systematically assess OpenClaw's security vulnerabilities through various personalized scenarios and attack types, revealing significant risks in user prompt processing, tool usage, and memory retrieval. Key findings underscore the urgent need for robust security measures in the deployment of personalized AI agents, as they are susceptible to diverse and critical security threats.


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


> This paper presents a novel framework aimed at promoting fairer cooperation in mixed-motive Markov games by replacing the traditional utilitarian welfare objective with Proportional Fairness, which is designed to mitigate individual incentives to defect. The authors develop a fair altruistic utility based on individual log-payoffs, establish analytical conditions for cooperation, and introduce Fair Markov Games along with new fair Actor-Critic algorithms for sequential settings. Their evaluations across various social dilemma environments demonstrate that this approach fosters more equitable outcomes in multi-agent systems, thereby contributing significantly to the agentic AI field.


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


> The paper introduces the Shapley-based Hierarchical Attribution for Reinforcement Policy (SHARP), a novel framework designed to tackle the credit assignment problem in multi-agent systems optimized for reinforcement learning. By employing a decomposed reward mechanism that includes a global broadcast-accuracy reward, Shapley-based marginal-credit rewards, and a tool-process reward, SHARP provides precise credit attribution to individual agents, effectively stabilizing their training. Experimental results across various benchmarks indicate that SHARP significantly enhances performance, achieving average match improvements of 23.66% and 14.05% over single-agent and multi-agent approaches, thereby advancing the efficiency of agentic AI in complex problem-solving scenarios.


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


> The paper presents a novel framework called the Structural Context Model to formalize the design of LLM-based agents, addressing the fragmentation in current research by providing a self-consistent model for analyzing and comparing these agents independent of implementation details. The methodology includes a declarative implementation framework and a sustainable engineering workflow known as Semantic Dynamics Analysis, which enhances the design process through systematic iteration. Key findings indicate that agents developed using this framework significantly outperform traditional methods, achieving up to a 32 percentage point increase in success rates for complex tasks, thereby contributing valuable insights to the field of agentic AI.


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


> The paper investigates the conditions under which Multi-Agent Reinforcement Learning (MARL) outperforms Single-Agent Reinforcement Learning (SARL) in training large language models (LLMs), addressing a significant gap in the theoretical understanding of their comparative efficiencies. Utilizing the Probably Approximately Correct (PAC) framework, the authors define and analyze the sample complexity of both MARL and SARL, revealing that MARL is more efficient when tasks can be effectively decomposed into independent subtasks, whereas dependencies can hinder its advantages. The study also introduces the concept of task alignment, which helps quantify the trade-offs involved in enforcing task decomposition, ultimately providing practical guidelines for applying MARL in complex scenarios involving LLMs.


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


> The paper presents SynthAgent, a Multi-Agent System framework specifically designed for simulating high-fidelity virtual patients with obesity and mental health comorbidities, addressing the limitations of real-world patient data. The methodology encompasses the integration of diverse clinical evidence to create personalized agents that exhibit varying personality traits affecting their health behaviors. Key findings indicate that the framework effectively replicates patient interactions and responses to treatment, with evaluations showing superior performance using GPT-5 and Claude 4.5 Sonnet, thereby advancing the understanding of patient dynamics in medical and psychological contexts relevant to the agentic AI field.


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


> The paper presents scBench, a benchmarking framework designed to evaluate AI agents on single-cell RNA sequencing (scRNA-seq) analysis by providing 394 verifiable problems across various platforms and tasks. The methodology involves assessing eight advanced AI models’ performance on this benchmark, revealing significant variability in accuracy, ranging from 29-53%, due to interactions between model choice and sequencing platform. Key findings indicate that the choice of sequencing platform can drastically affect the performance of AI agents, highlighting the need for specialized approaches in developing models capable of accurately analyzing complex biological datasets.


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


> The paper investigates the neural mechanisms linking language and tool use, revealing that the putamen plays a crucial role in maintaining goal-dependent sequence integrity in both capacities. Using a combination of brain lesion analysis, developmental studies, and functional neuroimaging, the authors found that damage to the putamen in individuals with brain injury impaired both sentence processing and tool use, while early language acquisition was shown to enhance tool performance and strengthen putaminal responses. This research highlights the putamen as a shared neural substrate for language and action, with early language experience significantly influencing its functionality.


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


> The paper introduces MetaKnogic-Alpha, a hyper-relational knowledge base developed to synthesize extensive biomedical literature related to metabolic research, addressing the challenge of fragmented mechanistic insights. The methodology involves transforming over 100,000 full-text articles into a hypergraph structure that captures complex metabolic relationships, utilizing an autonomous reasoning agent for precise query enrichment and deterministic grounding against established metabolic networks. Key findings include achieving a mechanistic accuracy of 0.98 in evidence-supported scenarios, demonstrating that MetaKnogic-Alpha significantly improves the speed and reliability of knowledge extraction in metabolic pathways, thereby enhancing the capabilities of researchers in fields like precision oncology.


<details>
<summary>Abstract</summary>

The exponential trajectory of biomedical literature has precipitated a fundamental "synthesis gap" in metabolic research, where critical mechanistic insights remain fragmented across hundreds of thousands of disjointed full-text articles, preventing the consolidation of a global mechanistic view. Here, we present MetaKnogic-Alpha, a foundational mechanistic knowledge substrate designed to bridge this gap by transforming unstructured literature into a navigable, logic-based resource. MetaKnogic-Alpha synthesizes over 100K full-text articles into a hyper-relational hypergraph structure, preserving the n-ary relational logic inherent in complex metabolic pathways. To ensure biological rigor, we implemented a hierarchical discovery protocol: an autonomous reasoning agent first enriches query nomenclature for domain-specific precision, followed by a multi-hop topological expansion within the hypergraph to surface functional neighbors, such as enzymatic co-factors and distal regulators, often lost in traditional search paradigms. Crucially, the system subjects all literature-derived insights to a deterministic biochemical grounding against a curated metabolic reaction network, significantly mitigating the risk of probabilistic hallucinations common in standalone generative models. In rigorous benchmarking, MetaKnogic-Alpha achieved a mechanistic accuracy of 0.98 in scenarios where supporting evidence was present, providing a robustly attributable audit trail back to the primary literature via PubMed Central Identifiers. We designate this primary release as "alpha" to establish the foundational architectural logic for a burgeoning million-scale resource. By compressing the synthesis of thousands of papers from a multi-month manual effort into several hours of automated discovery, MetaKnogic-Alpha serves as a high-fidelity research companion that augments the human experts ability to resolve complex metabolic interactions and identify novel therapeutic drivers in precision oncology.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*