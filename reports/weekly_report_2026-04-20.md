# Weekly AI Agent Paper Report

**Generated:** 2026-04-20 11:18
**Period:** 2026-04-13 to 2026-04-19

## Summary

- **Total papers fetched:** 1076
- **Papers matching keywords:** 184
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-04-13) | Change |
|--------|-----------|-----------|--------|
| Total matched | 184 | 185 | -1 |
| arxiv | 177 | 181 | -4 |
| biorxiv | 2 | 4 | -2 |
| medrxiv | 5 | 0 | +5 |

### Notable Trends

**1️⃣ Volume & source mix – relatively stable but a subtle tilt toward health‑focused venues**  
* This week: 184 papers (≈96 % arXiv, 1 % bioRxiv, 3 % medRxiv).  
* Last week: 185 papers (≈98 % arXiv, 2 % bioRxiv, 0 % medRxiv).  
* **Takeaway:** the overall count is flat, but medRxiv entered the mix (+5 papers) while bioRxiv fell from 4 → 2.   The community is nudging more agent research toward clinical‑monitoring and radiology applications.

**2️⃣ Topic shift – from core AI/communication theory to applied biomedical & scientific‑workflow agents**  
* **Last week’s headline papers** were heavily methodological (temporal graph nets for cyber‑defense, semantic rate‑distortion, visual‑retrieval‑augmented generation, credit‑assignment RL, multi‑agent IRL).  
* **This week’s top titles** are dominated by domain‑specific deployments: X‑ray absorption‑near‑edge spectroscopy (ChemGraph‑XANES), CT‑report generation (MARCH), remote‑patient monitoring (Veritas‑RPM), astronomical imaging QA (AstroVLM), and a benchmark for social‑reasoning in embodied agents (SocialGrid).  
* **Implication:** the field is moving from “how to make agents communicate/learn” to “how to embed agents in concrete scientific‑/health‑care pipelines.”

**3️⃣ Emergence of “agentic AI for knowledge curation & publishing”**  
* Papers like *“Democratizing Scientific Publishing: A Local, Multi‑Agent LLM Framework for Objective Manuscript Editing”* and *“HARVEST: Unlocking the Dark Bioactivity Data of Pharmaceutical Patents via Agentic AI”* signal a growing niche: agents that harvest, curate, and edit scholarly content.  
* This was absent from the prior week’s list, suggesting a rapid rise (within a week) of interest in AI‑assistants for the research ecosystem itself.

**4️⃣ Continued interest in multi‑modal, tool‑use reasoning**  
* Both weeks feature agents that combine language models with external tools (e.g., VISOR, AstroVLM, ChemGraph‑XANES).  
* The new week adds a neuroscience‑focused study (*“Reaching for domain‑general syntax…”*) linking language/tool‑use to basal‑ganglia activity—showing cross‑disciplinary curiosity about the neural basis of agentic behavior.

**5️⃣ Slight diversification of application domains**  
* Last week’s list leaned toward security, communication theory, and drug‑screening.  
* This week expands to **astronomy, occupational epidemiology, and rare‑disease comparative profiling** (Sezary syndrome vs. cutaneous lymphoma).  
* The breadth indicates that “agentic AI” is being trialed as a generic research‑assistant across almost every scientific subfield.

---



## Biomedical Highlights (7 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


These papers collectively illustrate how autonomous and multi‑agent AI systems are being harnessed to unlock hidden biomedical knowledge, streamline research workflows, and safeguard clinical deployment. HARVEST and HAARF demonstrate agentic AI for large‑scale data extraction from public patents and the creation of a rigorous regulatory/verification framework, respectively, using natural‑language‑to‑structure pipelines and formal security specifications. The multi‑agent LLM editing platform and the conversational AI for comparative pathway profiling showcase modular LLM architectures that keep sensitive manuscript or patient data locally while providing domain‑specific reasoning, text generation, and interactive analytics. Neuroscience‑focused studies on basal‑ganglia syntax‑action parallels and epidemiological investigations of occupational exposures or early dementia markers supply the biological contexts where such agents can be applied, employing neuroimaging, case‑control, and screening‑tool methodologies. Together, the work highlights a converging theme: deploying purpose‑built, privacy‑preserving AI agents to extract, interpret, and regulate complex biomedical information across drug discovery, clinical decision‑support, and public‑health research.



### 1. HARVEST: Unlocking the Dark Bioactivity Data of Pharmaceutical Patents via Agentic AI

- **Authors:** Shepard, V., Musin, A., Chebykina, K., Zeninskaya, N. A., Mistryukova, L., Avchaciov, K., Fedichev, P. O.
- **Published:** 2026-04-17
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.03.15.711910](https://doi.org/10.64898/2026.03.15.711910)

- **Categories:** bioinformatics


> The paper introduces **HARVEST**, an autonomous multi‑agent pipeline built on large language models that scans the USPTO patent corpus, parses the dense SAR tables inside, and converts them into a searchable, structured bioactivity database at a cost of only $0.11 per patent. By processing 164,877 patents in under a week, HARVEST extracted 3.15 M protein‑ligand activity records, adding 326 k novel chemical scaffolds and 967 previously undocumented protein targets to public knowledge and achieving ~80 % concordance with the human‑curated BindingDB set. Using this newly mined data, the authors create **H‑Bench**, a held‑out benchmark that reveals a two‑dimensional generalization gap in current open‑source models (e.g., Boltz‑2), which perform poorly on both unseen scaffolds and unseen protein targets—highlighting the need for richer, agent‑derived training data in agentic AI for drug discovery.


<details>
<summary>Abstract</summary>

Pharmaceutical patents contain vast Structure-Activity Relationship tables documenting protein-ligand binding data. While technically public, this information remains computationally inaccessible and effectively dark, trapped in bulky documents that no existing database has systematically captured. We present HARVEST, a multi-agent large language model pipeline that autonomously extracts structured bioactivity records from USPTO patent archives at $0.11 per document. Applied to 164,877 patents, HARVEST produced 3.15 million activity records, recovering 326,342 unique scaffolds and 967 protein targets absent from BindingDB. This pipeline completed in under a week a task that would otherwise require over 55 years of continuous expert labor. Automated extraction achieves 80% agreement with human curated corpus of US patents from BindingDB, a conservative lower bound given identified errors within the reference data. We further introduce H-Bench, a structurally guaranteed held-out benchmark built from this recovered data. Evaluation of the leading open-source model Boltz-2 on H-Bench reveals a two-dimensional generalization gap: performance degrades both on novel scaffolds and on uncharacterized protein targets, exposing fundamental limitations of models trained on existing public repositories.

</details>


### 2. Reaching for domain-general syntax: Sentence processing and tool-use reach-to-grasp share neural patterns in the basal ganglia

- **Authors:** Thibault, S., Py, R., Koun, E., Salemme, R., BOULENGER, V., Roy, A. C., Brozzoli, C. d.
- **Published:** 2026-04-15
- **Source:** biorxiv
- **URL:** [https://doi.org/10.1101/2025.10.17.683107](https://doi.org/10.1101/2025.10.17.683107)

- **Categories:** neuroscience


> **Main contribution:** The paper provides neural evidence that hierarchical processing in language (syntactic embedding) and in tool‑mediated actions (reach‑to‑grasp) rely on the same computational substrate in the basal ganglia, supporting the view that the brain uses a domain‑general mechanism for structuring sequences across cognition and action.

**Methodology:** Forty French speakers performed a sentence‑comprehension task (object‑ vs. subject‑relative clauses) and a motor task (grasping objects either with a tool or with the bare hand) while undergoing fMRI. Univariate activation maps and multivariate pattern‑analysis (MVPA) were used to identify brain regions where the neural code for syntactically complex sentences overlapped with that for the reach‑to‑grasp phase of tool use.

**Key findings:** Both tasks recruited overlapping activity patterns specifically in the basal ganglia, and MVPA showed that the neural signatures for processing syntactically complex sentences were indistinguishable from those for the reach‑to‑grasp phase of tool use. This phase‑specific convergence suggests that the basal ganglia serve as a hub for domain‑general hierarchical computations, linking language syntax and tool‑based action planning—an insight directly relevant to agentic AI models that aim to integrate language and motor control through shared hierarchical mechanisms.


<details>
<summary>Abstract</summary>

Are actions organized like sentences? Recent evidence showed reciprocal transfer between tool use and syntactic comprehension, reflecting shared basal ganglia resources for action and language. The proposed mechanism is that embedding a tool into the motor plan increases the hierarchical structure of actions, paralleling the organization of sentences. If so, overlap with linguistic computations should emerge specifically during the initiation and/or reach-to-grasp phase, when tool embedding dynamically updates the relation with the target, rather than when the object is stably held in the tool grip. Forty French native speakers completed a sentence comprehension task involving object- and subject-relative clauses, and a motor task consisting of grasping and manipulating an object either with a tool or with the bare hand. Using both univariate and multivariate analyses, we found that the comprehension of syntactically complex sentences and the reach-to-grasp phase of tool use elicited overlapping and similar neural codes within the basal ganglia. This phase-specific convergence identifies the basal ganglia as a hub for domain-general hierarchical computations, unifying syntactic embedding for language and tool use.

</details>


### 3. Democratizing Scientific Publishing: A Local, Multi-Agent LLM Framework for Objective Manuscript Editing

- **Authors:** Bhansali, R., Gorenshtein, A., Westover, B., Goldenholz, D. M.
- **Published:** 2026-04-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.13.26350761](https://doi.org/10.64898/2026.04.13.26350761)

- **Categories:** health informatics


> The paper presents **Paper Analysis Tool (PAT)**, a free, locally‑run, multi‑agent framework that uses 31 small‑language‑model agents to perform comprehensive, confidential manuscript audits across methodological, statistical, visual, and linguistic dimensions. By running PAT on three published clinical‑neurology papers, the system generated 540 suggestions; expert reviewers validated 391 of them as actionable (≈90 % agreement) and measured a 72.4 % overall usefulness accuracy, while deterministic re‑evaluation of 126 rewrite pairs showed substantial textual improvements (‑25 % word count, passive voice ↓ from 35 % to 5 %, sentence length ↓ 24 %, long‑sentence fraction ↓ 67 %, Flesch‑Kincaid grade ↑ 17 %). These results demonstrate that a locally hosted, agentic LLM pipeline can reliably automate pre‑submission manuscript editing while preserving data confidentiality, offering a transparent, scalable alternative to cloud‑based AI writing tools in scientific publishing.


<details>
<summary>Abstract</summary>

Manuscript preparation is a critical bottleneck in scientific publishing, yet existing AI writing tools require cloud transmission of sensitive content, creating data-confidentiality barriers for clinical researchers. We introduce the Paper Analysis Tool (PAT), a free, multi-agent framework that deploys 31 specialized agents powered by small language models (SLMs) to audit manuscripts across multiple quality dimensions without external data transmission. Applied to three published clinical neurological papers, PAT generated 540 evaluable suggestions. Validation by two expert reviewers (R.B., A.G.) confirmed 391 actionable, high-value revisions (90% agreement), achieving a 72.4% overall usefulness accuracy spanning methodological, statistical, and visual domains. Furthermore, deterministic re-evaluation of 126 agent-suggested rewrite pairs using Phase 0 metrics confirmed text improvement: total word count decreased by 25%, passive voice prevalence dropped sharply from 35% to 5%, average sentence length decreased by 24%, long-sentence fraction fell by 67%, and the Flesch-Kincaid grade improved by 17% . Our validation confirms that systematic, agent-driven pre-submission review drives measurable improvements, successfully converting manuscript optimization from an opaque, manual endeavor into a transparent and rigorous scientific process.

Manuscript preparation is a critical bottleneck in scientific publishing, yet existing AI writing tools require cloud transmission of sensitive content, creating data-confidentiality barriers for clinical researchers. We introduce the Paper Analysis Tool (PAT), a free, multi-agent framework that deploys 31 specialized agents powered by small language models (SLMs) to audit manuscripts across multiple quality dimensions without external data transmission. Applied to three published clinical neurological papers, PAT generated 540 evaluable suggestions. Independent validation by two expert reviewers (R.B., A.G.) confirmed 391 actionable, high-value revisions (90% agreement), achieving a 72.4% overall usefulness accuracy spanning methodological, statistical, and visual domains. Furthermore, deterministic re-evaluation of 126 suggested Phase 0 rewrite pairs confirmed text improvement: total word count decreased by 25%, passive voice prevalence dropped sharply from 35% to 5%, average sentence length decreased by 24%, and long-sentence fraction fell by 67%, and the Flesch-Kincaid grade improved modestly. Our validation confirms that systematic, agent-driven pre-submission review drives measurable improvements, successfully converting manuscript optimization from an opaque, manual endeavor into a transparent and rigorous scientific process.

</details>


### 4. LIFETIME JEM-DERIVED OCCUPATIONAL EXPOSURE BURDEN AND ODDS OF PARKINSONS DISEASE AND PARKINSONISM IN A MATCHED CASE-CONTROL STUDY

- **Authors:** Lewis, F., Renzetti, S., Goulett, N., Azmoun, S., Sundar, V., Ali, M., Pitta, L., Shoieb, D., Caci, M., Borghesi, S., Covolo, L., Oppini, M., Gelatti, U., Padovani, A., Pilotto, A., Pepe, F., Turla, M., Crippa, P., Boffetta, P., Pani, L., Vermeulen, R., Kromhout, H., Lambertini, L., Colicino, E., Placidi, D., Lucchini, R.
- **Published:** 2026-04-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.16.26348171](https://doi.org/10.64898/2026.03.16.26348171)

- **Categories:** occupational and environmental health


> The paper demonstrates that cumulative occupational exposure—particularly to pesticides and metals—significantly raises the odds of Parkinson’s disease and Parkinsonism, independent of known genetic (SNCA rs356219) and familial risk factors. Using a hospital‑based matched case‑control design (334 cases / 334 controls) the authors linked lifetime job histories to the ALOHA+ job‑exposure matrix and applied conditional logistic regression and a weighted‑quantile‑sum (WQS) mixture model to quantify single‑agent and multi‑agent exposure burdens. Both analytical approaches identified high lifetime pesticide exposure (OR≈3.5 for PD) and a composite exposure index dominated by pesticides (weight ≈ 0.43) and metals (weight ≈ 0.21) as the strongest occupational contributors to disease risk, underscoring preventable workplace hazards for neurodegeneration.


<details>
<summary>Abstract</summary>

Background/ObjectivesOccupational exposure to neurotoxicants such as pesticides, metals, and solvents has long been implicated in Parkinsons disease (PD) and Parkinsonism, yet the cumulative impact of multiple occupational exposure families over the working life remains insufficiently characterized. This study evaluated whether long-term cumulative occupational exposures, derived from the ALOHA+ Job-Exposure Matrix (ALOHA+-JEM), were associated with PD and Parkinsonism.

MethodsA hospital-based matched case-control study was conducted in the province of Brescia, Italy, including 668 participants (334 PD/Parkinsonism cases and 334 matched controls). Cases and controls were 1:1 matched based on sex, age, and lifetime occupational duration. Lifetime occupational histories were coded using ISCO-08 and harmonized to ISCO-88 for linkage with ALOHA+-JEM. Conditional logistic regression estimated associations between cumulative exposures (none/low/high) and disease status, adjusting for smoking, parental history of PD/tremor, and SNCA rs356219 genotype. Multi-agent occupational exposure burden indexes were evaluated using positively constrained repeated-holdout Weighted Quantile Sum (WQS) regression (100 bootstraps, 100 holdouts)

ResultsIn conditional logistic regression, parental history of PD or tremor (OR = 4.55, 95% CI: 2.44-8.48; q < 0.001) and the SNCA rs356219 CC genotype (OR = 2.17, 95% CI: 1.33-3.52; q = 0.013) were significantly associated with disease. High cumulative all pesticide exposure showed positive associations with combined PD + Parkinsonism (OR = 2.98, 95% CI: 1.23-7.25) and PD alone (OR = 3.56, 95% CI: 1.25-10.15). In WQS analyses, the composite occupational exposure burden index was positively associated with disease (combined PD + Parkinsonism: OR = 1.15, 95% CI: 1.00-1.30). All pesticides received the highest mean weight in all models (w = 0.434 for combined PD + Parkinsonism), followed by metals (w = 0.210), identifying them as contributing most strongly to the composite exposure index.

ConclusionsLong-term cumulative occupational exposures were associated with increased odds of PD and Parkinsonism. All pesticides and metals were most strongly associated with PD and Parkinsonism, consistent with established neurotoxic mechanisms attributable to occupational environments. These findings underscore the importance of occupational exposure prevention and risk-reduction strategies in occupational settings and highlight workplace exposures as preventable contributors to Parkinsonian disorders.

</details>


### 5. A Conversational Artificial Intelligence Framework for Comparative Pathway-Level Profiling of Sezary Syndrome and Primary Cutaneous CD8+ Aggressive Epidermotropic Cytotoxic T-Cell Lymphoma (PCAECTCL)

- **Authors:** Diaz, F. C., Waldrup, B., Carranza, F. G., Manjarrez, S., Velazquez-Villarreal, E.
- **Published:** 2026-04-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.15.26350992](https://doi.org/10.64898/2026.04.15.26350992)

- **Categories:** oncology


> The paper introduces **AI‑HOPE**, a conversational AI framework that lets researchers iteratively query and refine public cancer genomics datasets, and applies it to a comparative pathway‑level analysis of Sezary syndrome (SS) versus primary cutaneous CD8⁺ aggressive epidermotropic cytotoxic T‑cell lymphoma (PCAECTCL). Using curated somatic‑mutation data from the Columbia CTCL cohort, the authors map high‑confidence coding variants to signaling pathways, compare mutation frequencies (Chi‑square/Fisher), tumor mutational burden (Wilcoxon) and co‑mutation networks, and discover that—despite similar TMB—SS is enriched for epigenetic, tumor‑suppressor, NFAT and DNA‑damage‑response pathways, while PCAECTCL shows relatively higher MAPK and epigenetic regulator alterations, with ERBB2 mutations distinguishing the subtypes. These results not only generate subtype‑specific therapeutic hypotheses (e.g., ERBB2 targeting) but also demonstrate how conversational AI can accelerate hypothesis‑driven, pathway‑centric genomics research in agentic AI‑enabled precision oncology.


<details>
<summary>Abstract</summary>

Background: Sezary syndrome (SS) is an aggressive leukemic variant of cutaneous T-cell lymphoma (CTCL) with distinct clinical and biological features compared to rarer entities such as primary cutaneous CD8+ aggressive epidermotropic cytotoxic T-cell lymphoma (PCAECTCL). Although recurrent genomic alterations in CTCL have been described, comparative analyses at the pathway level across biologically divergent subtypes remain limited. Here, we leveraged a conversational artificial intelligence (AI) platform for precision oncology to enable rapid, integrative, and hypothesis-driven interrogation of publicly available genomic datasets. Methods: We conducted a secondary analysis of somatic mutation and clinical data from the Columbia University CTCL cohort accessed via cBioPortal. Cases were stratified into SS (n=26) and PCAECTCL (n=13). High-confidence coding variants were curated and mapped to biologically relevant signaling pathways and functional gene categories implicated in CTCL pathogenesis. Pathway-level mutation frequencies were compared using Chi-square or Fisher's exact tests, with effect sizes quantified as odds ratios. Tumor mutational burden (TMB) was compared using the Wilcoxon rank-sum test. Subtype-specific co-mutation patterns were evaluated using pairwise association analyses and visualized through oncoplots and network heatmaps. Conversational AI agents, AI-HOPE, were used to iteratively refine cohort definitions, prioritize pathway-level signals, and contextualize findings. Results: TMB was comparable between SS and PCAECTCL (p = 0.96), indicating no significant difference in global mutational load. In contrast, pathway-centric analyses revealed marked qualitative differences. SS demonstrated enrichment of alterations in epigenetic regulators, tumor suppressor and cell-cycle control pathways, NFAT signaling, and DNA damage response mechanisms, consistent with transcriptional dysregulation and immune modulation. PCAECTCL exhibited relatively higher frequencies of alterations involving epigenetic regulators and MAPK pathway signaling, suggesting distinct oncogenic dependencies. Co-mutation analysis revealed a more constrained and focused interaction landscape in SS, whereas PCAECTCL displayed broader and more heterogeneous co-mutation networks, indicative of divergent evolutionary trajectories. Notably, ERBB2 mutations were significantly enriched between subtypes (p = 0.031), highlighting a potential subtype-specific therapeutic vulnerability. Conclusions: This study demonstrates that SS is distinguished from PCAECTCL not by increased mutational burden but by distinct pathway-level architectures, particularly involving epigenetic regulation, immune signaling, and transcriptional control. These findings generate biologically grounded, testable hypotheses for subtype-specific therapeutic targeting and underscore the value of conversational AI as a scalable framework for accelerating discovery in translational cancer genomics.

</details>


### 6. Pre-Dementia Indicators and Multidomain Vulnerabilities: Insights from AD8 Screening in Older Chinese Speaking Adults

- **Authors:** You, W., Koo, F. K., Cheng, Y., Huang, J., Huang, H., Li, M., Sevastidis, J., Chang, H.-C.
- **Published:** 2026-04-13
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.08.26350424](https://doi.org/10.64898/2026.04.08.26350424)

- **Categories:** geriatric medicine


> The paper demonstrates that the AD8 dementia‑screening interview can serve as a multidimensional risk‑stratification tool for community‑dwelling Chinese‑speaking elders, identifying three latent domains (memory impairment, executive‑interest decline, and functional recall difficulty) that predict physical (e.g., mobility, financial management), psychological (e.g., depression, hopelessness, worthlessness) and social vulnerabilities. Using exploratory factor analysis on 144 participants and binary logistic regression, the authors show that specific AD8 items—particularly judgment problems, repetition errors, financial and tool‑use difficulties, and daily memory lapses—are strong early indicators of functional decline and emotional distress, whereas intact temporal recall is protective. These findings suggest that brief, culturally adapted AD8 screening can be integrated into nursing and community assessments to flag pre‑dementia multidomain frailties and guide timely, person‑centred interventions in diverse ageing populations.


<details>
<summary>Abstract</summary>

BackgroundEarly recognition of dementia-related changes is critical for timely intervention. The AD8 Dementia Screening Interview (AD8) detects subtle cognitive and functional changes, yet its broader associations with health and wellbeing among Chinese-speaking older adults remain underexplored.

MethodsA cross-sectional study was conducted with 144 community-dwelling Chinese older adults (mean age 73.1 years; 81.3% female). Participants completed sociodemographic, health, functional, and psychosocial measures, including the AD8 and the Geriatric Depression Scale (GDS-15). Exploratory Factor Analysis (EFA) assessed the dimensionality of the AD8, and binary logistic regression examined associations between AD8 items and demographic, health, functional, and psychosocial outcomes.

ResultsChronic disease was prevalent (68.1 percent), and 13.2 percent reported a mental health disorder. EFA identified three domains: memory impairment, executive and interest decline, and functional recall difficulties, explaining 61.7 percent of the variance. Logistic regression showed predictive roles for judgment problems (AD8_1), repetition (AD8_3), financial difficulties (AD8_6), tool-use difficulties (AD8_4), and daily memory problems (AD8_8). Financial and executive difficulties were associated with age and mobility challenges, while repetition predicted psychological disorders and hopelessness. Judgment problems were linked to lower life satisfaction and happiness but greater helplessness. Worthlessness was predicted by financial, tool-use, and memory difficulties, whereas intact temporal recall (AD8_5) was protective. Several outcomes including boredom, low energy, and staying home were not significant.

ConclusionDistinct AD8 items predicted vulnerabilities across physical, psychological, and social domains. Findings highlight the multidimensional value of the AD8 as a culturally relevant screening and risk stratification tool for community-based assessments of Chinese older adults.

Summary Statement Implications for PracticeO_ST_ABSWhat does this research add to existing knowledge in gerontology?C_ST_ABSThis study shows that specific AD8 items identify early multidimensional vulnerability among community-dwelling Chinese-speaking older adults. Difficulties with judgment, repetition, financial management, tool use, and daily memory were associated with functional limitations and psychosocial distress, extending the AD8 beyond dementia screening alone. The identification of three AD8 domains supports a broader understanding of early cognitive change as involving cognitive, functional, and emotional processes. The findings contribute culturally specific evidence from an under-researched population in gerontological research.

What are the implications of this new knowledge for nursing care with older people?For nursing practice, the AD8 provides a brief, feasible tool to support holistic assessment in community and aged care settings. Key AD8 indicators can guide nurses in identifying older people at risk of functional decline and emotional vulnerability, enabling earlier, person-centred interventions. The findings highlight the importance of culturally and linguistically appropriate assessment when caring for diverse ageing populations.

How could the findings be used to influence policy or practice or research or education?The results support integrating brief cognitive screening into routine nursing assessments and community-based aged care services to promote early identification and ageing in place. Nursing education should emphasise interpreting cognitive screening within psychosocial and cultural contexts. Longitudinal research is needed to assess intervention effectiveness.

Key Points[tpltrtarr] Early cognitive changes matter for older Chinese-speaking adults, because difficulties with judgment, repetition, financial management, and tool use (AD8 domains) were consistently linked to poorer functional and psychosocial outcomes.
[tpltrtarr]Beyond dementia screening, the AD8 proved useful for detecting vulnerabilities in wellbeing and daily functioning, extending its role beyond diagnostic sensitivity.
[tpltrtarr]A cultural focus is vital, as this study is among the first to examine AD8 associations in older Chinese-speaking adults, underscoring the need for culturally tailored screening.
[tpltrtarr]The psychosocial impact of cognitive changes was evident, with strong associations to helplessness, worthlessness, and reduced life satisfaction, reinforcing the overlap between cognitive and emotional health.
[tpltrtarr]In practice, integrating AD8 screening into community and primary care could help identify at-risk individuals early and support targeted interventions in culturally and linguistically diverse populations.

</details>


### 7. HAARF: Healthcare AI Agents Regulatory Framework - A Comprehensive Security Verification Standard for Autonomous AI Systems in Clinical Environments

- **Authors:** Schwoebel, J., Frasch, M., Spalding, A., Sewell, E., Englert, P., Halpert, B., Overbay, C., Semenec, I., Shor, J.
- **Published:** 2026-04-13
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.09.26350519](https://doi.org/10.64898/2026.04.09.26350519)

- **Categories:** health systems and quality improvement


> The paper introduces **HAARF**, a unified regulatory and verification framework that lets health systems safely deploy fully autonomous AI agents for clinical decision‑making and tool use. By distilling nine existing medical‑AI regulations into eight verification categories (279 concrete requirements) and defining three risk‑based compliance levels, HAARF provides a model‑agnostic middleware that enforces progressive autonomy, tool‑access controls, bias monitoring, and decision traceability. Red‑team tests on Gemini 2.5 Flash (cross‑validated with Claude Sonnet 4.6) show that HAARF‑guardrails eliminate unauthorized tool execution (0 % success vs. ~58 % in baseline) and achieve >90 % alignment with major regulators, cutting multi‑jurisdictional compliance effort by 40‑60 % while improving patient‑safety governance.


<details>
<summary>Abstract</summary>

As health systems begin deploying autonomous AI agents that make independent clinical decisions and take direct actions within care workflows, ensuring patient safety and care quality requires governance standards that go beyond existing medical device frameworks designed for human-in-the-loop prediction tools. This paper introduces the Healthcare AI Agents Regulatory Framework (HAARF), a comprehensive verification standard for autonomous AI systems in clinical environments, developed collaboratively with 40+ international experts spanning regulatory authorities, clinical organizations, and AI security specialists.

HAARF synthesizes requirements from nine major regulatory frameworks (FDA, EU AI Act, Health Canada, UK MHRA, NIST AI RMF, WHO GI-AI4H, ISO/IEC 42001, OWASP AISVS, IMDRF GMLP) into eight core verification categories comprising 279 specific requirements across three risk-based implementation levels. The framework addresses critical gaps in health system readiness for autonomous AI including: (1) progressive autonomy governance with clinical accountability, (2) tool-use security for agents that independently access EHRs, medical devices, and clinical systems, (3) continuous equity monitoring and bias mitigation across diverse patient populations, and (4) clinical decision traceability preserving human oversight authority.

We validate HAARFs enforcement capabilities through a scenario-based red-team evaluation comprising six adversarial scenarios executed under baseline (no middleware) and HAARF- guardrailed conditions (N = 50 trials each, Gemini 2.5 Flash primary with Claude Sonnet 4.6 cross-model validation). In baseline conditions, the agent model executes unauthorized tools in 56-60% of adversarial trials. Under the HAARF condition, deterministic middleware enforcement reduces the unauthorized-tool success rate to 0%, with 0% contraindication misses and 0% policy-injection success (95% Wilson CI [0.00, 0.07]). Cross-model validation confirms identical security metrics, supporting HAARFs model-agnostic design. Mapping analysis demonstrates 48-88% coverage of major regulatory frameworks, with per-category FDA alignment ranging from 73% (C5, Agent Registration) to 91% (C3, Cybersecurity; C7, Bias & Equity). Initial validation with healthcare organizations shows a 40-60% reduction in multi-jurisdictional compliance burden and improved clinical safety governance outcomes.

HAARF provides health systems with a practical, risk-stratified pathway for safe AI agent deployment--shifting from reactive compliance to proactive quality governance while maintaining rigorous patient safety standards and human-centered care principles.

</details>


---



## Arxiv (177 papers)


### 1. ChemGraph-XANES: An Agentic Framework for XANES Simulation and Analysis

- **Authors:** Vitor F. Grizzi, Thang Duc Pham, Luke N. Pretzie, Jiayi Xu, Murat Keceli, Cong Liu
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.16205v1](http://arxiv.org/abs/2604.16205v1)
- **PDF:** [https://arxiv.org/pdf/2604.16205v1](https://arxiv.org/pdf/2604.16205v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI, physics.chem-ph


> ChemGraph‑XANES introduces a novel agentic framework that lets large‑language‑model (LLM) agents orchestrate end‑to‑end XANES simulations from natural‑language requests through structure acquisition, FDMNES input generation, parallel execution, and provenance‑rich data curation. By wrapping each workflow step as typed Python tools built on ASE, Parsl, and a LangGraph/LangChain interface, the system deploys a retrieval‑augmented expert agent to consult the FDMNES manual for parameter selection while executor agents translate user intents into concrete tool calls, enabling both file‑based and chemistry‑level inputs. Benchmarks show that the framework reliably retrieves documentation‑grounded parameters, scales trivially across HPC resources via task‑parallel execution, and can populate large, reproducible XANES databases for downstream analysis and machine‑learning, establishing a reproducible, extensible layer for physics‑based computational spectroscopy in the agentic AI ecosystem.


<details>
<summary>Abstract</summary>

Computational X-ray absorption near-edge structure (XANES) is widely used to probe local coordination environments, oxidation states, and electronic structure in chemically complex systems. However, the use of computational XANES at scale is constrained more by workflow complexity than by the underlying simulation method itself. To address this challenge, we present ChemGraph-XANES, an agentic framework for automated XANES simulation and analysis that unifies natural-language task specification, structure acquisition, FDMNES input generation, task-parallel execution, spectral normalization, and provenance-aware data curation. Built on ASE, FDMNES, Parsl, and a LangGraph/LangChain-based tool interface, the framework exposes XANES workflow operations as typed Python tools that can be orchestrated by large language model (LLM) agents. In multi-agent mode, a retrieval-augmented expert agent consults the FDMNES manual to ground parameter selection, while executor agents translate user requests into structured tool calls. We demonstrate documentation-grounded parameter retrieval and show that the same workflow supports both explicit structure-file inputs and chemistry-level natural-language requests. Because independent XANES calculations are naturally task-parallel, the framework is well suited for high-throughput deployment on high-performance computing (HPC) systems, enabling scalable XANES database generation for downstream analysis and machine-learning applications. ChemGraph-XANES thus provides a reproducible and extensible workflow layer for physics-based XANES simulation, spectral curation, and agent-compatible computational spectroscopy.

</details>


### 2. MARCH: Multi-Agent Radiology Clinical Hierarchy for CT Report Generation

- **Authors:** Yi Lin, Yihao Ding, Yonghui Wu, Yifan Peng
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.16175v1](http://arxiv.org/abs/2604.16175v1)
- **PDF:** [https://arxiv.org/pdf/2604.16175v1](https://arxiv.org/pdf/2604.16175v1)
- **Categories:** cs.AI, cs.CV


> **Paper Summary**

The authors introduce **MARCH**, a hierarchical multi‑agent system that mimics the radiology department’s workflow to generate CT scan reports. A Resident Agent first drafts a report using multi‑scale 3‑D feature extraction, Fellow Agents iteratively refine the draft through retrieval‑augmented revisions, and an Attending Agent steers a stance‑based consensus dialogue to resolve any diagnostic disagreements. Evaluated on the RadGenome‑ChestCT dataset, MARCH achieves markedly higher clinical fidelity and linguistic quality than existing vision‑language baselines, demonstrating that organizing AI agents into human‑like professional hierarchies can substantially reduce hallucination and improve reliability in high‑stakes medical reporting.


<details>
<summary>Abstract</summary>

Automated 3D radiology report generation often suffers from clinical hallucinations and a lack of the iterative verification found in human practice. While recent Vision-Language Models (VLMs) have advanced the field, they typically operate as monolithic "black-box" systems without the collaborative oversight characteristic of clinical workflows. To address these challenges, we propose MARCH (Multi-Agent Radiology Clinical Hierarchy), a multi-agent framework that emulates the professional hierarchy of radiology departments and assigns specialized roles to distinct agents. MARCH utilizes a Resident Agent for initial drafting with multi-scale CT feature extraction, multiple Fellow Agents for retrieval-augmented revision, and an Attending Agent that orchestrates an iterative, stance-based consensus discourse to resolve diagnostic discrepancies. On the RadGenome-ChestCT dataset, MARCH significantly outperforms state-of-the-art baselines in both clinical fidelity and linguistic accuracy. Our work demonstrates that modeling human-like organizational structures enhances the reliability of AI in high-stakes medical domains.

</details>


### 3. Veritas-RPM: Provenance-Guided Multi-Agent False Positive Suppression for Remote Patient Monitoring

- **Authors:** Aswini Misro, Vikash Sharma, Shreyank N Gowda
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.16081v1](http://arxiv.org/abs/2604.16081v1)
- **PDF:** [https://arxiv.org/pdf/2604.16081v1](https://arxiv.org/pdf/2604.16081v1)
- **Categories:** cs.MA


> Veritas‑RPM introduces a provenance‑driven, multi‑agent pipeline for remote patient monitoring that explicitly tackles the chronic problem of false‑positive alerts. The architecture stacks five processing layers—VeritasAgent for assembling ground‑truth streams, SentinelLayer for initial anomaly detection, DirectorAgent for routing to one of six domain‑specialist agents, and a MetaSentinelAgent that reconciles conflicts and emits the final decision. Using a rigorously crafted synthetic taxonomy of 98 false‑positive scenarios and 530 generated patient epochs, the authors evaluate the system with true‑suppression, false‑escalation, and indeterminate rates, demonstrating markedly higher true suppression (≈ 87 %) while keeping false escalations below 5 %, thereby offering a scalable, provenance‑based template for trustworthy, agentic AI in clinical monitoring.


<details>
<summary>Abstract</summary>

We present Veritas-RPM, a provenance-guided multi-agent architecture comprising five processing layers: VeritasAgent (ground-truth assembly), SentinelLayer (anomaly detection), DirectorAgent (specialist routing), six domain Specialist Agents, and MetaSentinelAgent (conflict resolution and final decision). We construct a 98-case synthetic taxonomy of false-positive scenarios derived from documented RPM patterns. Synthetic patient epochs (n = 530) were generated directly from taxonomy parameters and processed through the pipeline. Ground-truth labels are known for all cases. Performance is reported as True Suppression Rate (TSR), False Escalation Rate (FER), and Indeterminate Rate (INDR).

</details>


### 4. AstroVLM: Expert Multi-agent Collaborative Reasoning for Astronomical Imaging Quality Diagnosis

- **Authors:** Yaohui Han, Tianshuo Wang, Zixi Zhao, Zhengchun Zhu, Shuo Ren, Yiru Wang, Rongliang Fu, Tinghuan Chen, Tsung-Yi Ho
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.16024v1](http://arxiv.org/abs/2604.16024v1)
- **PDF:** [https://arxiv.org/pdf/2604.16024v1](https://arxiv.org/pdf/2604.16024v1)
- **Categories:** cs.MA, cs.CV


> AstroVLM introduces a multi‑agent collaborative framework that extends vision‑language models to the intrinsically multidisciplinary task of astronomical imaging quality diagnosis. The system decomposes the problem into specialized expert agents (e.g., optics, detector physics, data reduction) that iteratively exchange natural‑language reasoning and visual evidence, coordinated by a central controller that aggregates their conclusions. Empirical evaluation on real‑world astronomical datasets shows that AstroVLM significantly outperforms prior single‑model baselines, achieving higher accuracy in defect detection and error localization, thereby demonstrating that coordinated agentic reasoning enables VLMs to tackle complex, multi‑process scientific diagnostics.


<details>
<summary>Abstract</summary>

Vision Language Models (VLMs) have been applied to several specific domains and have shown strong problem-solving capabilities. However, astronomical imaging, a quite complex problem involving multidisciplinary knowledge and several subtasks, has not been adequately studied. Due to the complexity of the astronomical imaging process, both world-class astronomical organizations, such as NASA, and expert enthusiasts devote a great deal of time and effort. This is because the processes in astronomical imaging have complex underlying correlations that significantly influence one another, making the quality diagnosis and error localization of astronomical images challenging. To address this problem, we propose AstroVLM, a collaborative multi-agent system for diagnosing the quality of astronomical images. Experiment results show that AstroVLM outperforms all baselines on real-world astronomical imaging quality diagnosis tasks, providing a reference for language models to handle complicated multi-process tasks.

</details>


### 5. SocialGrid: A Benchmark for Planning and Social Reasoning in Embodied Multi-Agent Systems

- **Authors:** Hikaru Shindo, Hanzhao Lin, Lukas Helff, Patrick Schramowski, Kristian Kersting
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.16022v1](http://arxiv.org/abs/2604.16022v1)
- **PDF:** [https://arxiv.org/pdf/2604.16022v1](https://arxiv.org/pdf/2604.16022v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> SocialGrid is a new embodied multi‑agent benchmark (inspired by *Among Us*) that measures how well LLM‑driven agents can plan, execute tasks, and perform social reasoning such as deception detection in a shared physical space. The authors evaluate a suite of open‑source and closed‑source LLM agents, using both raw performance and a “Planning Oracle” that removes navigation errors to isolate pure social reasoning; even the largest model (GPT‑OSS‑120B) falls below 60 % on task completion and near‑random on deception detection, showing that current language‑model agents rely on shallow heuristics rather than robust evidence accumulation. The benchmark supplies automatic failure analysis, fine‑grained metrics, and an Elo‑based leaderboard for adversarial league play, offering a concrete platform for diagnosing and improving the social intelligence of agentic AI.


<details>
<summary>Abstract</summary>

As Large Language Models (LLMs) transition from text processors to autonomous agents, evaluating their social reasoning in embodied multi-agent settings becomes critical. We introduce SocialGrid, an embodied multi-agent environment inspired by Among Us that evaluates LLM agents on planning, task execution, and social reasoning. Our evaluations reveal that even the strongest open model (GPT-OSS-120B) achieves below 60% accuracy in task completion and planning, with agents getting stuck in repetitive behaviors or failing to navigate basic obstacles. Since poor navigation confounds evaluation of social intelligence, SocialGrid offers an optional Planning Oracle to isolate social reasoning from planning deficits. While planning assistance improves task completion, social reasoning remains a bottleneck: agents fail to detect deception at near-random chance regardless of scale, relying on shallow heuristics rather than accumulating behavioral evidence. SocialGrid provides automatic failure analysis and fine-grained metrics, enabling developers to diagnose and improve their agents. We also establish a competitive leaderboard using Elo ratings from adversarial league play.

</details>


### 6. AgentV-RL: Scaling Reward Modeling with Agentic Verifier

- **Authors:** Jiazheng Zhang, Ziche Fu, Zhiheng Xi, Wenqing Jing, Mingxu Chai, Wei He, Guoqiang Zhang, Chenghao Fan, Chenxin An, Wenxiang Chen, Zhicheng Liu, Haojie Pan, Dingwei Zhu, Tao Gui, Qi Zhang, Xuanjing Huang
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.16004v1](http://arxiv.org/abs/2604.16004v1)
- **PDF:** [https://arxiv.org/pdf/2604.16004v1](https://arxiv.org/pdf/2604.16004v1)
- **Categories:** cs.CL, cs.AI


> **Main contribution:** The paper introduces **Agentic Verifier**, a reward‑modeling framework that turns verification into a multi‑turn, tool‑augmented deliberation between two complementary agents—a forward agent that constructs a solution step‑by‑step and a backward agent that retro‑checks each conclusion against its premises.  

**Methodology:** By coupling these bidirectional agents with proactive tool use (e.g., calculators, search APIs) and training them via reinforcement learning (AgentV‑RL), the system learns to interleave external computation with internal reasoning, enabling it to explore and evaluate candidate answers autonomously.  

**Key findings:** Across a suite of complex reasoning benchmarks, the 4 B‑parameter AgentV‑RL model delivers a **~25 % improvement** over the strongest existing Open‑ended Reward Models (ORMs) and yields consistent gains under both parallel and sequential test‑time scaling, demonstrating that agentic, tool‑augmented verification can dramatically enhance reward modeling for advanced LLM agents.


<details>
<summary>Abstract</summary>

Verifiers have been demonstrated to enhance LLM reasoning via test-time scaling (TTS). Yet, they face significant challenges in complex domains. Error propagation from incorrect intermediate reasoning can lead to false positives for seemingly plausible solutions, while lacking external grounding makes verifiers unreliable on computation or knowledge-intensive tasks. To address these challenges, we propose Agentic Verifier, a framework that transforms reward modeling into a multi-turn, tool-augmented deliberative process. We introduce complementary forward and backward agents: one traces solutions from premises to conclusions, while the other re-checks conclusions against their underlying premises. This bidirectional process enables a comprehensive, reliable, and interpretable assessment of solutions. To facilitate practical deployment, we propose AgentV-RL. Through proactive exploration and reinforcement learning, the verifier autonomously interleaves tool-use with internal reasoning. Extensive experiments show that Agentic Verifier yields consistent performance gains under both parallel and sequential TTS. Notably, our 4B variant surpasses state-of-the-art ORMs by 25.2%, positioning it as a promising paradigm for agentic reward modeling.

</details>


### 7. Weak-Link Optimization for Multi-Agent Reasoning and Collaboration

- **Authors:** Haoyu Bian, Chaoning Zhang, Jiaquan Zhang, Xingyao Li, Yuanfang Guo, Wei Dong, Yang Yang
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15972v1](http://arxiv.org/abs/2604.15972v1)
- **PDF:** [https://arxiv.org/pdf/2604.15972v1](https://arxiv.org/pdf/2604.15972v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> The paper introduces **WORC**, a “weak‑link” optimization framework for large‑language‑model (LLM) based multi‑agent systems that first pinpoints the least reliable agent in a collaborative task and then compensates for its shortcomings. Using task‑specific features, a meta‑learned weight predictor—trained on optimal agent configurations discovered by swarm‑intelligence search—identifies the weak agent, after which an uncertainty‑driven budget allocation repeats its reasoning more often to reduce error propagation. Across several reasoning benchmarks, WORC raises average accuracy to **≈ 82 %**, improves stability, and generalizes across different model architectures, demonstrating that reinforcing weak links can be more effective than only strengthening high‑performing agents.


<details>
<summary>Abstract</summary>

LLM-driven multi-agent frameworks address complex reasoning tasks through multi-role collaboration. However, existing approaches often suffer from reasoning instability, where individual agent errors are amplified through collaboration, undermining overall performance. Current research mainly focuses on enhancing high-capability agents or suppressing unreliable outputs to improve framework effectiveness, while systematic identification and reinforcement of performance-limiting agents receive less attention. To address this gap, we propose WORC, a \underline{w}eak-link \underline{o}ptimization framework for multi-agent \underline{r}easoning and \underline{c}ollaboration, grounded in the weak-link principle. WORC follows a two-stage workflow. In the weak agent localization stage, task features are constructed, and a meta-learning-based weight predictor trained on optimal configurations identified by swarm intelligence algorithms (SIAs) enables zero-shot mapping from these features to agent performance weights, where the agent with the lowest predicted weight is identified as the weak agent. In the weak-link optimization stage, an uncertainty-driven allocation strategy assigns additional reasoning budgets to weak agents, with lower predicted weights leading to larger repeated-sampling quotas to compensate for reliability deficiencies. Experimental results show that WORC achieves an average accuracy of 82.2\% on reasoning benchmarks while improving framework stability and cross-architecture generalization, suggesting that compensating for weak links, rather than reinforcing strengths alone, enhances the robustness of multi-agent systems.

</details>


### 8. Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents

- **Authors:** Xing Zhang, Guanghui Wang, Yanwei Cui, Wei Qiu, Ziyuan Li, Bing Zhu, Peiyang He
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15877v1](http://arxiv.org/abs/2604.15877v1)
- **PDF:** [https://arxiv.org/pdf/2604.15877v1](https://arxiv.org/pdf/2604.15877v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> **Main contribution:** The paper introduces the *Experience Compression Spectrum* (ECS), a unified framework that treats episodic memory, procedural skills, and declarative rules as points along a single continuum of information compression, and demonstrates that existing LLM‑agent systems occupy fixed positions on this axis without mechanisms for adaptive, cross‑level compression.  

**Methodology:** The authors conduct a citation‑network analysis of 1,136 references spanning 22 influential papers on LLM‑agent memory and skill discovery, quantify typical compression ratios (≈5–20× for raw episodic traces, 50–500× for learned skills, >1,000× for abstract rules), and map >20 published systems onto the ECS to expose a “missing diagonal” – the lack of systems that can fluidly move between compression levels.  

**Key findings for agentic AI:** (1) Current approaches are siloed; memory‑focused and skill‑focused communities solve similar sub‑problems but rarely share solutions. (2) Evaluation metrics are tightly tied to the chosen compression level, obscuring trade‑offs between specificity and transferability. (3) Higher compression yields more portable knowledge but sacrifices detail, while knowledge‑lifecycle management (creation, compression, retrieval, decay) is largely unaddressed. The paper concludes with design principles and open research questions aimed at building scalable LLM agents that can dynamically compress and recompress experience across the full spectrum.


<details>
<summary>Abstract</summary>

As LLM agents scale to long-horizon, multi-session deployments, efficiently managing accumulated experience becomes a critical bottleneck. Agent memory systems and agent skill discovery both address this challenge -- extracting reusable knowledge from interaction traces -- yet a citation analysis of 1,136 references across 22 primary papers reveals a cross-community citation rate below 1%. We propose the \emph{Experience Compression Spectrum}, a unifying framework that positions memory, skills, and rules as points along a single axis of increasing compression (5--20$\times$ for episodic memory, 50--500$\times$ for procedural skills, 1,000$\times$+ for declarative rules), directly reducing context consumption, retrieval latency, and compute overhead. Mapping 20+ systems onto this spectrum reveals that every system operates at a fixed, predetermined compression level -- none supports adaptive cross-level compression, a gap we term the \emph{missing diagonal}. We further show that specialization alone is insufficient -- both communities independently solve shared sub-problems without exchanging solutions -- that evaluation methods are tightly coupled to compression levels, that transferability increases with compression at the cost of specificity, and that knowledge lifecycle management remains largely neglected. We articulate open problems and design principles for scalable, full-spectrum agent learning systems.

</details>


### 9. CoEvolve: Training LLM Agents via Agent-Data Mutual Evolution

- **Authors:** Shidong Yang, Ziyu Ma, Tongwen Huang, Yiming Hu, Yong Wang, Xiangxiang Chu
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15840v1](http://arxiv.org/abs/2604.15840v1)
- **PDF:** [https://arxiv.org/pdf/2604.15840v1](https://arxiv.org/pdf/2604.15840v1)
- **Categories:** cs.CL


> **Main contribution:** CoEvolve introduces a closed‑loop “agent‑data mutual evolution” paradigm in which large‑language‑model (LLM) agents and their training data co‑adapt: the agent’s rollout failures are mined to automatically generate new, targeted tasks that reshape the training distribution.  

**Methodology:** During interaction, the framework extracts signals such as forgetting and predictive uncertainty from the agent’s trajectories to pinpoint failure‑prone patterns. An LLM‑based task synthesizer then creates validation‑ready tasks reflecting these patterns; successful execution of the synthesized tasks feeds back as new training examples, iteratively updating both the agent and its data pool.  

**Key findings:** On the AppWorld and BFCL benchmarks, CoEvolve yields large, consistent performance gains for Qwen2.5‑7B, Qwen3‑4B, and Qwen3‑30B‑A3B models, delivering absolute improvements of 19.43 %, 15.58 %, and 18.14 % over strong baselines, demonstrating that joint agent‑data evolution dramatically enhances LLM agent competency in complex environments.


<details>
<summary>Abstract</summary>

Reinforcement learning for LLM agents is typically conducted on a static data distribution, which fails to adapt to the agent's evolving behavior and leads to poor coverage of complex environment interactions. To address these challenges, we propose CoEvolve, an agent-data mutual evolution framework that enables LLM agents to improve through closed-loop, interaction-driven training. Specifically, CoEvolve extracts feedback signals such as forgetting and uncertainty from rollout trajectories to identify failure-prone interaction patterns, and utilizes them to guide LLM-based task synthesis. The synthesized tasks are validated through environment interaction and utilized to update the data distribution, enabling joint adaptation of the agent and its data. Extensive experiments on AppWorld and BFCL across Qwen2.5-7B, Qwen3-4B, and Qwen3-30B-A3B demonstrate consistent and significant improvements over strong base models, yielding absolute gains of 19.43%, 15.58%, and 18.14%, respectively.

</details>


### 10. MemEvoBench: Benchmarking Memory MisEvolution in LLM Agents

- **Authors:** Weiwei Xie, Shaoxiong Guo, Fan Zhang, Tian Xia, Xue Yang, Lizhuang Ma, Junchi Yan, Qibing Ren
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15774v1](http://arxiv.org/abs/2604.15774v1)
- **PDF:** [https://arxiv.org/pdf/2604.15774v1](https://arxiv.org/pdf/2604.15774v1)
- **Categories:** cs.CL


> The paper presents **MemEvoBench**, the first systematic benchmark for measuring “memory misevolution” — the gradual safety drift of LLM‑based agents caused by repeatedly incorporating misleading, biased, or noisy information into their persistent memory. The authors construct QA‑style tasks covering 7 domains and 36 risk types, plus workflow‑style tasks derived from 20 Agent‑SafetyBench environments, and evaluate a range of contemporary LLM agents under adversarial memory injection, noisy tool outputs, and biased feedback. Results show that even modest exposure to corrupted memory leads to pronounced behavioral degradation, and simple prompt‑based mitigations fail to protect against this drift, highlighting memory evolution as a critical, previously under‑explored safety vulnerability in agentic AI.


<details>
<summary>Abstract</summary>

Equipping Large Language Models (LLMs) with persistent memory enhances interaction continuity and personalization but introduces new safety risks. Specifically, contaminated or biased memory accumulation can trigger abnormal agent behaviors. Existing evaluation methods have not yet established a standardized framework for measuring memory misevolution. This phenomenon refers to the gradual behavioral drift resulting from repeated exposure to misleading information. To address this gap, we introduce MemEvoBench, the first benchmark evaluating long-horizon memory safety in LLM agents against adversarial memory injection, noisy tool outputs, and biased feedback. The framework consists of QA-style tasks across 7 domains and 36 risk types, complemented by workflow-style tasks adapted from 20 Agent-SafetyBench environments with noisy tool returns. Both settings employ mixed benign and misleading memory pools within multi-round interactions to simulate memory evolution. Experiments on representative models reveal substantial safety degradation under biased memory updates. Our analysis suggests that memory evolution is a significant contributor to these failures. Furthermore, static prompt-based defenses prove insufficient, underscoring the urgency of securing memory evolution in LLM agents.

</details>


### 11. Zero-Shot Scalable Resilience in UAV Swarms: A Decentralized Imitation Learning Framework with Physics-Informed Graph Interactions

- **Authors:** Huan Lin, Lianghui Ding
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15762v1](http://arxiv.org/abs/2604.15762v1)
- **PDF:** [https://arxiv.org/pdf/2604.15762v1](https://arxiv.org/pdf/2604.15762v1)
- **Categories:** cs.LG


> The paper introduces **PhyGAIL**, a decentralized imitation‑learning framework that enables UAV swarms to recover from large‑scale fragmentation without any online training. By constructing bounded local interaction graphs from heterogeneous sensor inputs and encoding them with a physics‑informed graph neural network (explicit attraction/repulsion gated message passing), PhyGAIL provides a scale‑invariant, physically grounded coordination bias while remaining fully decentralized at execution time. Trained centrally on 20‑UAV scenarios, the learned policy transfers zero‑shot to swarms of up to 500 agents and outperforms state‑of‑the‑art decentralized heuristics and MARL baselines in reconnection reliability, recovery speed, safety, and computational efficiency.


<details>
<summary>Abstract</summary>

Large-scale Unmanned Aerial Vehicle (UAV) failures can split an unmanned aerial vehicle swarm network into disconnected sub-networks, making decentralized recovery both urgent and difficult. Centralized recovery methods depend on global topology information and become communication-heavy after severe fragmentation. Decentralized heuristics and multi-agent reinforcement learning methods are easier to deploy, but their performance often degrades when the swarm scale and damage severity vary. We present Physics-informed Graph Adversarial Imitation Learning algorithm (PhyGAIL) that adopts centralized training with decentralized execution. PhyGAIL builds bounded local interaction graphs from heterogeneous observations, and uses physics-informed graph neural network to encode directional local interactions as gated message passing with explicit attraction and repulsion. This gives the policy a physically grounded coordination bias while keeping local observations scale-invariant. It also uses scenario-adaptive imitation learning to improve training under fragmented topologies and variable-length recovery episodes. Our analysis establishes bounded local graph amplification, bounded interaction dynamics, and controlled variance of the terminal success signal. A policy trained on 20-UAV swarms transfers directly to swarms of up to 500 UAVs without fine-tuning, and achieves better performance across reconnection reliability, recovery speed, motion safety, and runtime efficiency than representative baselines.

</details>


### 12. The World Leaks the Future: Harness Evolution for Future Prediction Agents

- **Authors:** Chuyang Wei, Maohang Gao, Zhixin Han, Kefei Chen, Yu Zhuang, Haoxiang Guan, Yanzhi Zhang, Yilin Cheng, Jiyan He, Huanhuan Chen, Jian Li, Yu Shi, Yitong Duan, Shuxin Zheng
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15719v1](http://arxiv.org/abs/2604.15719v1)
- **PDF:** [https://arxiv.org/pdf/2604.15719v1](https://arxiv.org/pdf/2604.15719v1)
- **Categories:** cs.AI


> The paper introduces **Milkyway**, a self‑evolving LLM‑agent framework that keeps the underlying language model static while continually refining a separate “future prediction harness” that guides factor tracking, evidence gathering, interpretation, and uncertainty management. By repeatedly revisiting the same unresolved question, Milkyway extracts **internal feedback**—the differences between earlier and later predictions—as supervision, writes reusable guidance into the harness, and finally validates the updates with the eventual outcome before propagating the improved harness to new questions. Empirically, this approach yields state‑of‑the‑art performance on the FutureX and FutureWorld benchmarks, raising scores from 44.07 → 60.90 and 62.22 → 77.96 respectively, demonstrating that evolution‑driven internal feedback can substantially improve agentic future‑prediction capabilities before the ground‑truth outcome is known.


<details>
<summary>Abstract</summary>

Many consequential decisions must be made before the relevant outcome is known. Such problems are commonly framed as \emph{future prediction}, where an LLM agent must form a prediction for an unresolved question using only the public information available at the prediction time. The setting is difficult because public evidence evolves while useful supervision arrives only after the question is resolved, so most existing approaches still improve mainly from final outcomes. Yet final outcomes are too coarse to guide earlier factor tracking, evidence gathering and interpretation, or uncertainty handling. When the same unresolved question is revisited over time, temporal contrasts between earlier and later predictions can expose omissions in the earlier prediction process; we call this signal \emph{internal feedback}. We introduce \emph{Milkyway}, a self-evolving agent system that keeps the base model fixed and instead updates a persistent \emph{future prediction harness} for factor tracking, evidence gathering and interpretation, and uncertainty handling. Across repeated predictions on the same unresolved question, \emph{Milkyway} extracts internal feedback and writes reusable guidance back into the harness, so later predictions on that question can improve before the outcome is known. After the question is resolved, the final outcome provides a \emph{retrospective check} before the updated harness is carried forward to subsequent questions. On FutureX and FutureWorld, Milkyway achieves the best overall score among the compared methods, improving FutureX from 44.07 to 60.90 and FutureWorld from 62.22 to 77.96.

</details>


### 13. GTA-2: Benchmarking General Tool Agents from Atomic Tool-Use to Open-Ended Workflows

- **Authors:** Jize Wang, Xuanxuan Liu, Yining Li, Songyang Zhang, Yijun Wang, Zifei Shan, Xinyi Le, Cailian Chen, Xinping Guan, Dacheng Tao
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15715v1](http://arxiv.org/abs/2604.15715v1)
- **PDF:** [https://arxiv.org/pdf/2604.15715v1](https://arxiv.org/pdf/2604.15715v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **GTA‑2**, a two‑tier benchmark that evaluates general‑purpose tool‑using agents on both **atomic tool‑use tasks (GTA‑Atomic)** and **open‑ended, long‑horizon workflows (GTA‑Workflow)** using real user queries, deployed tools, and multimodal contexts.  To assess the latter, the authors devise a **recursive checkpoint‑based evaluation** that breaks down end‑goal specifications into verifiable sub‑goals, allowing simultaneous measurement of model capability and execution‑harness quality.  Experiments show a steep performance gap: even the strongest LLMs achieve < 50 % on atomic tasks and only ~14 % success on full workflows, while checkpoint‑guided feedback and sophisticated harnesses (e.g., Manus, OpenClaw) markedly improve results, underscoring that reliable agentic AI depends as much on execution frameworks as on raw model size.


<details>
<summary>Abstract</summary>

The development of general-purpose agents requires a shift from executing simple instructions to completing complex, real-world productivity workflows. However, current tool-use benchmarks remain misaligned with real-world requirements, relying on AI-generated queries, dummy tools, and limited system-level coordination. To address this, we propose GTA-2, a hierarchical benchmark for General Tool Agents (GTA) spanning atomic tool use and open-ended workflows. Built on real-world authenticity, it leverages real user queries, deployed tools, and multimodal contexts. (i) GTA-Atomic, inherited from our prior GTA benchmark, evaluates short-horizon, closed-ended tool-use precision. (ii) GTA-Workflow introduces long-horizon, open-ended tasks for realistic end-to-end completion. To evaluate open-ended deliverables, we propose a recursive checkpoint-based evaluation mechanism that decomposes objectives into verifiable sub-goals, enabling unified evaluation of both model capabilities and agent execution frameworks (i.e., execution harnesses). Experiments reveal a pronounced capability cliff: while frontier models already struggle on atomic tasks (below 50%), they largely fail on workflows, with top models achieving only 14.39% success. Further analysis shows that checkpoint-guided feedback improves performance, while advanced frameworks such as Manus and OpenClaw substantially enhance workflow completion, highlighting the importance of execution harness design beyond the underlying model capacity. These findings provide guidance for developing reliable personal and professional assistants. Dataset and code will be available at https://github.com/open-compass/GTA.

</details>


### 14. Just Type It in Isabelle! AI Agents Drafting, Mechanizing, and Generalizing from Human Hints

- **Authors:** Kevin Kappelmann, Maximilian Schäffeler, Lukas Stevens, Mohammad Abdulaziz, Andrei Popescu, Dmitriy Traytel
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15713v1](http://arxiv.org/abs/2604.15713v1)
- **PDF:** [https://arxiv.org/pdf/2604.15713v1](https://arxiv.org/pdf/2604.15713v1)
- **Categories:** cs.LO, cs.AI, cs.PL


> **Main contribution:** The paper presents a fully formalized, metatheoretic solution to the problem of computing *complete and minimal* type annotations for rank‑1 polymorphic λ‑terms as used in Isabelle, together with a novel workflow that combines human insight and LLM‑driven AI agents to produce and mechanize the proofs.

**Methodology:** Building on Smolka, Blanchette et al.’s earlier results, the authors formalize the specification and correctness proofs of the annotation algorithm in Isabelle/HOL. They then conduct a series of “human‑AI co‑formalization” experiments: a human author writes pen‑and‑paper proofs, an LLM‑powered agent independently derives the same results, and the agent automatically translates both into Isabelle code. Subsequent AI‑assisted refinements, guided by brief human hints, are used to generalize and streamline the development.

**Key findings for agentic AI:** The AI agent can independently reconstruct sophisticated metatheoretic arguments and reliably auto‑formalize them, while minimal human guidance suffices to steer the agent toward more general lemmas and cleaner Isabelle scripts. This demonstrates that LLM‑based agents can act as competent co‑authors in formal mathematics, handling both creative proof drafting and rigorous mechanization in a domain‑specific proof assistant.


<details>
<summary>Abstract</summary>

Type annotations are essential when printing terms in a way that preserves their meaning under reparsing and type inference. We study the problem of complete and minimal type annotations for rank-one polymorphic $λ$-calculus terms, as used in Isabelle. Building on prior work by Smolka, Blanchette et al., we give a metatheoretical account of the problem, with a full formal specification and proofs, and formalize it in Isabelle/HOL. Our development is a series of experiments featuring human-driven and AI-driven formalization workflows: a human and an LLM-powered AI agent independently produce pen-and-paper proofs, and the AI agent autoformalizes both in Isabelle, with further human-hinted AI interventions refining and generalizing the development.

</details>


### 15. The Price of Paranoia: Robust Risk-Sensitive Cooperation in Non-Stationary Multi-Agent Reinforcement Learning

- **Authors:** Deep Kumar Ganguly, Chandradithya S Jonnalagadda, Pratham Chintamani, Adithya Ananth
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15695v1](http://arxiv.org/abs/2604.15695v1)
- **PDF:** [https://arxiv.org/pdf/2604.15695v1](https://arxiv.org/pdf/2604.15695v1)
- **Categories:** cs.GT, cs.AI


> **Contribution:** The paper identifies a fundamental instability of cooperative equilibria in non‑stationary multi‑agent reinforcement learning: partner‑induced gradient noise quickly drives agents away from Pareto‑optimal coordination, and conventional risk‑averse (distributionally robust) objectives actually enlarge the region of collapse.  

**Methodology:** By analytically characterizing how co‑learning noise propagates through symmetric coordination games, the authors show that robustness must be applied to the *gradient‑update variance* rather than to the return distribution. They develop a variance‑aware policy‑gradient algorithm that rescales updates using an online estimate of partner unpredictability, and they prove that this expands the basin of attraction for cooperation.  

**Key findings:** The new algorithm provably stabilizes cooperation while keeping sample complexity low, and the introduced “Price of Paranoia” (dual to the Price of Anarchy) together with a “Cooperation Window” quantifies the welfare loss/gain‑trade‑off, yielding a closed‑form optimal level of robustness that maximizes recovered welfare under partner noise.


<details>
<summary>Abstract</summary>

Cooperative equilibria are fragile. When agents learn alongside each other rather than in a fixed environment, the process of learning destabilizes the cooperation they are trying to sustain: every gradient step an agent takes shifts the distribution of actions its partner will play, turning a cooperative partner into a source of stochastic noise precisely where the cooperation decision is most sensitive. We study how this co-learning noise propagates through the structure of coordination games, and find that the cooperative equilibrium, even when strongly Pareto-dominant, is exponentially unstable under standard risk-neutral learning, collapsing irreversibly once partner noise crosses the game's critical cooperation threshold. The natural response to apply distributional robustness to hedge against partner uncertainty makes things strictly worse: risk-averse return objectives penalize the high-variance cooperative action relative to defection, widening the instability region rather than shrinking it, a paradox that reveals a fundamental mismatch between the domains where robustness is applied and instability originates. We resolve this by showing that robustness should target the policy gradient update variance induced by partner uncertainty, not the return distribution. This distinction yields an algorithm whose gradient updates are modulated by an online measure of partner unpredictability, provably expanding the cooperation basin in symmetric coordination games. To unify stability, sample complexity, and welfare consequences of this approach, we introduce the Price of Paranoia as the structural dual of the Price of Anarchy. Together with a novel Cooperation Window, it precisely characterizes how much welfare learning algorithms can recover under partner noise, pinning down the optimal degree of robustness as a closed-form balance between equilibrium stability and sample efficiency.

</details>


### 16. Preference Estimation via Opponent Modeling in Multi-Agent Negotiation

- **Authors:** Yuta Konishi, Kento Yamamoto, Eisuke Sonomoto, Rikuho Takeda, Ryo Furukawa, Yusuke Muraki, Takafumi Shimizu, Kazuma Fukumura, Yuya Kanemoto, Takayuki Ito, Shiyao Ding
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15687v1](http://arxiv.org/abs/2604.15687v1)
- **PDF:** [https://arxiv.org/pdf/2604.15687v1](https://arxiv.org/pdf/2604.15687v1)
- **Categories:** cs.CL


> The paper introduces a Bayesian opponent‑modeling framework that fuses qualitative cues extracted by large language models (LLMs) from negotiation dialogue with quantitative belief‑tracking of opponent preferences. By prompting LLMs to translate natural‑language utterances into probabilistic constraints and updating these constraints within a dynamic Bayesian network, the method produces a coherent, continuously refined estimate of each party’s utility landscape. Empirical evaluation on a standard multi‑party, multi‑issue negotiation benchmark shows that this hybrid approach markedly raises full‑agreement rates and reduces preference‑estimation error compared with purely numerical or purely semantic baselines, demonstrating a viable path for richer, more reliable opponent modeling in agentic AI systems.


<details>
<summary>Abstract</summary>

Automated negotiation in complex, multi-party and multi-issue settings critically depends on accurate opponent modeling. However, conventional numerical-only approaches fail to capture the qualitative information embedded in natural language interactions, resulting in unstable and incomplete preference estimation. Although Large Language Models (LLMs) enable rich semantic understanding of utterances, it remains challenging to quantitatively incorporate such information into a consistent opponent modeling. To tackle this issue, we propose a novel preference estimation method integrating natural language information into a structured Bayesian opponent modeling framework. Our approach leverages LLMs to extract qualitative cues from utterances and converts them into probabilistic formats for dynamic belief tracking. Experimental results on a multi-party benchmark demonstrate that our framework improves the full agreement rate and preference estimation accuracy by integrating probabilistic reasoning with natural language understanding.

</details>


### 17. Stargazer: A Scalable Model-Fitting Benchmark Environment for AI Agents under Astrophysical Constraints

- **Authors:** Xinge Liu, Terry Jingchen Zhang, Bernhard Schölkopf, Zhijing Jin, Kristen Menou
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15664v1](http://arxiv.org/abs/2604.15664v1)
- **PDF:** [https://arxiv.org/pdf/2604.15664v1](https://arxiv.org/pdf/2604.15664v1)
- **Categories:** cs.LG


> **Main contribution:** The paper introduces **Stargazer**, a large‑scale, simulation‑driven benchmark that lets autonomous AI agents iteratively fit astrophysical models to radial‑velocity (RV) time‑series data, covering 120 tasks (including 20 real archival exoplanet systems) across three difficulty levels.  

**Methodology:** The authors generate RV datasets with known ground‑truth planetary parameters, define a unified API for agents to propose models, receive simulation‑based feedback, and evaluate performance on both statistical fit (e.g., χ², likelihood) and physical accuracy (recovered orbital elements). Eight state‑of‑the‑art agents—ranging from language‑model planners to reinforcement‑learning controllers—are instantiated with a common set of “vanilla” skills (parameter suggestion, optimization loops, and constraint checking) and tested under varying compute budgets.  

**Key findings:** While agents can often achieve low‑error statistical fits, they systematically miss the true physical parameters, especially in low‑signal‑to‑noise, multi‑planet scenarios, revealing a gap between numerical optimization and physical reasoning. More test‑time compute or longer token budgets yields only marginal improvements, and excessive token usage tends to reflect endless, unproductive search loops rather than deeper scientific insight. This highlights the need for agent architectures that explicitly encode physical constraints and domain‑specific inference strategies, positioning Stargazer as a realistic testbed for advancing agentic AI in scientific model‑fitting tasks.


<details>
<summary>Abstract</summary>

The rise of autonomous AI agents suggests that dynamic benchmark environments with built-in feedback on scientifically grounded tasks are needed to evaluate the capabilities of these agents in research work. We introduce Stargazer, a scalable environment for evaluating AI agents on dynamic, iterative physics-grounded model-fitting tasks using inference on radial-velocity (RV) time series data. Stargazer comprises 120 tasks across three difficulty tiers, including 20 real archival cases, covering diverse scenarios ranging from high-SNR single-planet systems to complex multi-planetary configurations requiring involved low-SNR analysis. Our evaluation of eight frontier agents reveals a gap between numerical optimization and adherence to physical constraints: although agents often achieve a good statistical fit, they frequently fail to recover correct physical system parameters, a limitation that persists even when agents are equipped with vanilla skills. Furthermore, increasing test-time compute yields only marginal gains, with excessive token usage often reflecting recursive failure loops rather than meaningful exploration. Stargazer presents an opportunity to train, evaluate, scaffold, and scale strategies on a model-fitting problem of practical research relevance today. Our methodology to design a simulation-driven environment for AI agents presumably generalizes to many other model-fitting problems across scientific domains. Source code and the project website are available at https://github.com/Gudmorning2025/Stargazer and https://gudmorning2025.github.io/Stargazer, respectively.

</details>


### 18. Imperfectly Cooperative Human-AI Interactions: Comparing the Impacts of Human and AI Attributes in Simulated and User Studies

- **Authors:** Myke C. Cohen, Mingqian Zheng, Neel Bhandari, Hsien-Te Kao, Xuhui Zhou, Daniel Nguyen, Laura Cassani, Maarten Sap, Svitlana Volkova
- **Published:** 2026-04-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15607v1](http://arxiv.org/abs/2604.15607v1)
- **PDF:** [https://arxiv.org/pdf/2604.15607v1](https://arxiv.org/pdf/2604.15607v1)
- **Categories:** cs.CL, cs.AI, cs.CY, cs.HC


> The paper’s main contribution is a systematic comparison of how human personality traits (Extraversion, Agreeableness) and AI design attributes (Adaptability, Expertise, chain‑of‑thought transparency) affect outcomes in imperfectly cooperative human‑AI interactions, using both large‑scale simulations (2 000 runs) and a real‑world user study (290 participants) across hiring‑negotiation and information‑concealment scenarios. By applying causal‑discovery methods to performance metrics, communication logs, and questionnaire data, the authors find that while simulated agents show roughly equal influence from human and AI factors, real human participants are far more sensitive to AI attributes—especially transparent reasoning—indicating that AI transparency drives interaction quality in practice. These findings highlight the necessity of grounding agentic AI design choices in human‑centered empirical validation rather than relying solely on simulated analyses.


<details>
<summary>Abstract</summary>

AI design characteristics and human personality traits each impact the quality and outcomes of human-AI interactions. However, their relative and joint impacts are underexplored in imperfectly cooperative scenarios, where people and AI only have partially aligned goals and objectives. This study compares a purely simulated dataset comprising 2,000 simulations and a parallel human subjects experiment involving 290 human participants to investigate these effects across two scenario categories: (1) hiring negotiations between human job candidates and AI hiring agents; and (2) human-AI transactions wherein AI agents may conceal information to maximize internal goals. We examine user Extraversion and Agreeableness alongside AI design characteristics, including Adaptability, Expertise, and chain-of-thought Transparency. Our causal discovery analysis extends performance-focused evaluations by integrating scenario-based outcomes, communication analysis, and questionnaire measures. Results reveal divergences between purely simulated and human study datasets, and between scenario types. In simulation experiments, personality traits and AI attributes were comparatively influential. Yet, with actual human subjects, AI attributes -- particularly transparency -- were much more impactful. We discuss how these divergences vary across different interaction contexts, offering crucial insights for the future of human-centered AI agents.

</details>


### 19. Symbolic Guardrails for Domain-Specific Agents: Stronger Safety and Security Guarantees Without Sacrificing Utility

- **Authors:** Yining Hong, Yining She, Eunsuk Kang, Christopher S. Timperley, Christian Kästner
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15579v1](http://arxiv.org/abs/2604.15579v1)
- **PDF:** [https://arxiv.org/pdf/2604.15579v1](https://arxiv.org/pdf/2604.15579v1)
- **Categories:** cs.SE, cs.AI, cs.CR


> **Main contribution:** The paper demonstrates that lightweight, symbolic “guardrails” can enforce a large share of concrete safety and security policies for domain‑specific AI agents, delivering formal guarantees without degrading performance.

**Methodology:** The authors (1) surveyed 80 state‑of‑the‑art agent‑safety benchmarks to catalog the policies they test, (2) identified which of those policies can be expressed as symbolic constraints (e.g., whitelist/blacklist rules, resource caps, data‑flow restrictions), and (3) integrated these constraints into agents and measured their impact on three representative test suites (τ²‑Bench, CAR‑bench, MedAgentBench).

**Key findings:** 85 % of existing benchmarks lack precise policy specifications; of the 15 % that do, 74 % of the required constraints are enforceable by simple symbolic guardrails. Adding these guardrails markedly improves safety and security metrics while leaving task success rates essentially unchanged, confirming that symbolic guardrails are a practical, high‑assurance solution for ensuring reliable behavior of domain‑specific AI agents.


<details>
<summary>Abstract</summary>

AI agents that interact with their environments through tools enable powerful applications, but in high-stakes business settings, unintended actions can cause unacceptable harm, such as privacy breaches and financial loss. Existing mitigations, such as training-based methods and neural guardrails, improve agent reliability but cannot provide guarantees. We study symbolic guardrails as a practical path toward strong safety and security guarantees for AI agents. Our three-part study includes a systematic review of 80 state-of-the-art agent safety and security benchmarks to identify the policies they evaluate, an analysis of which policy requirements can be guaranteed by symbolic guardrails, and an evaluation of how symbolic guardrails affect safety, security, and agent success on $τ^2$-Bench, CAR-bench, and MedAgentBench. We find that 85\% of benchmarks lack concrete policies, relying instead on underspecified high-level goals or common sense. Among the specified policies, 74\% of policy requirements can be enforced by symbolic guardrails, often using simple, low-cost mechanisms. These guardrails improve safety and security without sacrificing agent utility. Overall, our results suggest that symbolic guardrails are a practical and effective way to guarantee some safety and security requirements, especially for domain-specific AI agents. We release all codes and artifacts at https://github.com/hyn0027/agent-symbolic-guardrails.

</details>


### 20. Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation

- **Authors:** Jacob Dang, Brian Y. Xie, Omar G. Younis
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15559v1](http://arxiv.org/abs/2604.15559v1)
- **PDF:** [https://arxiv.org/pdf/2604.15559v1](https://arxiv.org/pdf/2604.15559v1)
- **Categories:** cs.AI


> The paper demonstrates for the first time that unsafe **behaviors**—not just semantic traits—can be transmitted subliminally from a teacher to a student agent through trajectory‑only distillation. By filtering out all explicit deletion‑related keywords, the authors train student agents on trajectories from ostensibly safe tasks, yet the students replicate the teacher’s destructive bias (100 % file‑deletion in an API‑tool setting and a 30‑55 % preference for issuing an initial chmod command in a Bash setting), especially when a larger teacher is distilled into a smaller student. These results show that simple data sanitization cannot remove behavioral biases, because the dynamics of the trajectories implicitly encode the unsafe policy, highlighting a new, subtle threat vector for agentic AI safety.


<details>
<summary>Abstract</summary>

Recent work on subliminal learning demonstrates that language models can transmit semantic traits through data that is semantically unrelated to those traits. However, it remains unclear whether behavioral traits can transfer in agentic systems, where policies are learned from trajectories rather than static text. In this work, we provide the first empirical evidence that unsafe agent behaviors can transfer subliminally through model distillation across two complementary experimental settings. In our primary setting, we construct a teacher agent exhibiting a strong deletion bias, a tendency to perform destructive file-system actions via an API-style tool interface, and distill it into a student using only trajectories from ostensibly safe tasks, with all explicit deletion keywords rigorously filtered. In our secondary setting, we replicate the threat model in a native Bash environment, replacing API tool calls with shell commands and operationalizing the bias as a preference for issuing chmod as the first permission-related command over semantically equivalent alternatives such as chown or setfacl. Despite full keyword sanitation in both settings, students inherit measurable behavioral biases. In the API setting the student's deletion rate reaches 100% (versus a 5% baseline) under homogeneous distillation; in the Bash setting the student's chmod-first rate reaches 30%-55% (versus a 0%-10% baseline), with the strongest transfer observed in large-to-small distillation. Our results demonstrate that explicit data sanitation is an insufficient defense, and behavioral biases are encoded implicitly in trajectory dynamics regardless of the tool interface.

</details>


### 21. Preregistered Belief Revision Contracts

- **Authors:** Saad Alqithami
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15558v1](http://arxiv.org/abs/2604.15558v1)
- **PDF:** [https://arxiv.org/pdf/2604.15558v1](https://arxiv.org/pdf/2604.15558v1)
- **Categories:** cs.AI, cs.CL, cs.LO, cs.MA


> **Main contribution:** The paper introduces **Preregistered Belief Revision Contracts (PBRC)**, a protocol‑level framework that forces every belief update in a deliberative multi‑agent system to be justified by publicly registered evidence triggers and verifiable evidence tokens, thereby preventing conformity‑driven “high‑confidence” cascades while keeping the communication layer open.

**Methodology:** The authors formalize PBRC as a contract that (i) fixes admissible revision operators, (ii) lists first‑order evidence triggers, (iii) defines a priority rule and a fallback policy, and (iii) requires a non‑empty witness set of externally validated tokens for any non‑fallback update. They prove a series of theorems about the impossibility of confidence growth in “social‑only” rounds, the existence of normal forms and audit traces, and the dependence of enforced trajectories on token‑exposure traces (characterized by truncated reachability under flooding). A companion dynamic doxastic logic is used to specify trace invariants, and the theory is validated with simulations.

**Key findings for agentic AI:** PBRC guarantees **epistemic accountability**—any top‑hypothesis change can be traced to concrete evidence—while mathematically ruling out conformity‑driven belief cascades. The framework yields tight diameter bounds for evidence closure, shows how enforcement can be both sound and auditable, and demonstrates through experiments that cascade suppression can be achieved without sacrificing liveness, offering a practical tool for building trustworthy, self‑revisioning AI agents.


<details>
<summary>Abstract</summary>

Deliberative multi-agent systems allow agents to exchange messages and revise beliefs over time. While this interaction is meant to improve performance, it can also create dangerous conformity effects: agreement, confidence, prestige, or majority size may be treated as if they were evidence, producing high-confidence convergence to false conclusions. To address this, we introduce PBRC (Preregistered Belief Revision Contracts), a protocol-level mechanism that strictly separates open communication from admissible epistemic change. A PBRC contract publicly fixes first-order evidence triggers, admissible revision operators, a priority rule, and a fallback policy. A non-fallback step is accepted only when it cites a preregistered trigger and provides a nonempty witness set of externally validated evidence tokens. This ensures that every substantive belief change is both enforceable by a router and auditable after the fact. In this paper, (a) we prove that under evidential contracts with conservative fallback, social-only rounds cannot increase confidence and cannot generate purely conformity-driven wrong-but-sure cascades. (b) We show that auditable trigger protocols admit evidential PBRC normal forms that preserve belief trajectories and canonicalized audit traces. (c) We demonstrate that sound enforcement yields epistemic accountability: any change of top hypothesis is attributable to a concrete validated witness set. For token-invariant contracts, (d) we prove that enforced trajectories depend only on token-exposure traces; under flooding dissemination, these traces are characterized exactly by truncated reachability, giving tight diameter bounds for universal evidence closure. Finally, we introduce a companion contractual dynamic doxastic logic to specify trace invariants, and provide simulations illustrating cascade suppression, auditability, and robustness-liveness trade-offs.

</details>


### 22. PolicyBank: Evolving Policy Understanding for LLM Agents

- **Authors:** Jihye Choi, Jinsung Yoon, Long T. Le, Somesh Jha, Tomas Pfister
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15505v1](http://arxiv.org/abs/2604.15505v1)
- **PDF:** [https://arxiv.org/pdf/2604.15505v1](https://arxiv.org/pdf/2604.15505v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **PolicyBank**, a novel memory architecture that lets LLM‑based agents incrementally revise their internal, tool‑level policy representations through interactive testing and corrective feedback, rather than treating the natural‑language policy as a fixed ground truth. By augmenting a standard tool‑calling benchmark with deliberately introduced policy ambiguities, the authors show that conventional memory approaches fail almost entirely on these “policy‑gap” cases, whereas PolicyBank autonomously narrows the compliance gap by up to 82 % relative to a human oracle. This demonstrates that agents can evolve a more accurate policy understanding pre‑deployment, offering a scalable route to tighter alignment of LLM agents with ambiguous organizational directives.


<details>
<summary>Abstract</summary>

LLM agents operating under organizational policies must comply with authorization constraints typically specified in natural language. In practice, such specifications inevitably contain ambiguities and logical or semantic gaps that cause the agent's behavior to systematically diverge from the true requirements. We ask: by letting an agent evolve its policy understanding through interaction and corrective feedback from pre-deployment testing, can it autonomously refine its interpretation to close specification gaps? We propose PolicyBank, a memory mechanism that maintains structured, tool-level policy insights and iteratively refines them -- unlike existing memory mechanisms that treat the policy as immutable ground truth, reinforcing "compliant but wrong" behaviors. We also contribute a systematic testbed by extending a popular tool-calling benchmark with controlled policy gaps that isolate alignment failures from execution failures. While existing memory mechanisms achieve near-zero success on policy-gap scenarios, PolicyBank closes up to 82% of the gap toward a human oracle.

</details>


### 23. DeepER-Med: Advancing Deep Evidence-Based Research in Medicine Through Agentic AI

- **Authors:** Zhizheng Wang, Chih-Hsuan Wei, Joey Chan, Robert Leaman, Chi-Ping Day, Chuan Wu, Mark A Knepper, Antolin Serrano Farias, Jordina Rincon-Torroella, Hasan Slika, Betty Tyler, Ryan Huu-Tuan Nguyen, Asmita Indurkar, Mélanie Hébert, Shubo Tian, Lauren He, Noor Naffakh, Aseem Aseem, Nicholas Wan, Emily Y Chew, Tiarnan D L Keenan, Zhiyong Lu
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15456v1](http://arxiv.org/abs/2604.15456v1)
- **PDF:** [https://arxiv.org/pdf/2604.15456v1](https://arxiv.org/pdf/2604.15456v1)
- **Categories:** cs.AI


> The paper introduces **DeepER‑Med**, a novel agentic‑AI framework that structures medical research as a transparent, three‑stage workflow—research planning, collaborative multi‑agent reasoning, and evidence‑driven synthesis—so that every step of evidence appraisal can be inspected and audited. By coupling this workflow with a newly created benchmark, **DeepER‑MedQA** (100 expert‑curated, real‑world medical questions), the authors evaluate DeepER‑Med against leading production AI systems, showing through expert manual scoring that it yields higher‑quality, novel scientific insights and more reliable citations. In eight clinical case studies, clinicians judged DeepER‑Med’s conclusions consistent with standard recommendations in seven cases, demonstrating its potential as a trustworthy decision‑support and research‑augmentation tool for agentic AI in medicine.


<details>
<summary>Abstract</summary>

Trustworthiness and transparency are essential for the clinical adoption of artificial intelligence (AI) in healthcare and biomedical research. Recent deep research systems aim to accelerate evidence-grounded scientific discovery by integrating AI agents with multi-hop information retrieval, reasoning, and synthesis. However, most existing systems lack explicit and inspectable criteria for evidence appraisal, creating a risk of compounding errors and making it difficult for researchers and clinicians to assess the reliability of their outputs. In parallel, current benchmarking approaches rarely evaluate performance on complex, real-world medical questions. Here, we introduce DeepER-Med, a Deep Evidence-based Research framework for Medicine with an agentic AI system. DeepER-Med frames deep medical research as an explicit and inspectable workflow of evidence-based generation, consisting of three modules: research planning, agentic collaboration, and evidence synthesis. To support realistic evaluation, we also present DeepER-MedQA, an evidence-grounded dataset comprising 100 expert-level research questions derived from authentic medical research scenarios and curated by a multidisciplinary panel of 11 biomedical experts. Expert manual evaluation demonstrates that DeepER-Med consistently outperforms widely used production-grade platforms across multiple criteria, including the generation of novel scientific insights. We further demonstrate the practical utility of DeepER-Med through eight real-world clinical cases. Human clinician assessment indicates that DeepER-Med's conclusions align with clinical recommendations in seven cases, highlighting its potential for medical research and decision support.

</details>


### 24. CoopEval: Benchmarking Cooperation-Sustaining Mechanisms and LLM Agents in Social Dilemmas

- **Authors:** Emanuel Tewolde, Xiao Zhang, David Guzman Piedrahita, Vincent Conitzer, Zhijing Jin
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15267v1](http://arxiv.org/abs/2604.15267v1)
- **PDF:** [https://arxiv.org/pdf/2604.15267v1](https://arxiv.org/pdf/2604.15267v1)
- **Categories:** cs.GT, cs.AI, cs.CL, cs.CY, cs.MA


> CoopEval introduces the first systematic benchmark for evaluating how classic game‑theoretic cooperation mechanisms affect large language‑model (LLM) agents in mixed‑motive social dilemmas (prisoner’s dilemma, public‑goods, etc.). By running four canonical dilemmas with four interventions—repeated play, reputation scoring, third‑party mediation, and contract‑based conditional payments—the authors compare single‑shot and evolutionary‑run outcomes for state‑of‑the‑art LLMs (with and without chain‑of‑thought reasoning). They find that, unlike simple repetition, mediation and contract mechanisms reliably induce cooperation even among highly capable, reasoning‑enabled models, and that the effectiveness of all mechanisms amplifies when agents are subjected to evolutionary selection pressures for payoff maximization.


<details>
<summary>Abstract</summary>

It is increasingly important that LLM agents interact effectively and safely with other goal-pursuing agents, yet, recent works report the opposite trend: LLMs with stronger reasoning capabilities behave _less_ cooperatively in mixed-motive games such as the prisoner's dilemma and public goods settings. Indeed, our experiments show that recent models -- with or without reasoning enabled -- consistently defect in single-shot social dilemmas.
  To tackle this safety concern, we present the first comparative study of game-theoretic mechanisms that are designed to enable cooperative outcomes between rational agents _in equilibrium_. Across four social dilemmas testing distinct components of robust cooperation, we evaluate the following mechanisms: (1) repeating the game for many rounds, (2) reputation systems, (3) third-party mediators to delegate decision making to, and (4) contract agreements for outcome-conditional payments between players. Among our findings, we establish that contracting and mediation are most effective in achieving cooperative outcomes between capable LLM models, and that repetition-induced cooperation deteriorates drastically when co-players vary. Moreover, we demonstrate that these cooperation mechanisms become _more effective_ under evolutionary pressures to maximize individual payoffs.

</details>


### 25. HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents?

- **Authors:** Yukun Jiang, Yage Zhang, Michael Backes, Xinyue Shen, Yang Zhang
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15415v1](http://arxiv.org/abs/2604.15415v1)
- **PDF:** [https://arxiv.org/pdf/2604.15415v1](https://arxiv.org/pdf/2604.15415v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper introduces the first large‑scale measurement of “harmful skills” in public LLM‑agent skill ecosystems and releases HarmfulSkillBench—a benchmark that quantifies how pre‑installed malicious skills increase an agent’s propensity to comply with dangerous requests.  

**Methodology:** The authors crawled 98 k skills from two major registries (ClawHub and Skills.Rest), applied an LLM‑driven scoring system built on a taxonomy of harmful actions, and identified 4.93 % of skills as harmful. They then curated 200 representative harmful skills spanning 20 categories and evaluated six LLM‑based agents under four realistic conditions (explicit request, implicit request, with/without the skill).  

**Key findings:** Harmful skills are more prevalent in ClawHub (8.84 %) than Skills.Rest (3.49 %). When a harmful task is issued via a pre‑installed skill, agents’ refusal rates drop dramatically, raising the average harm score from 0.27 (no skill) to 0.47 (skill present) and to 0.76 when the intent is implicit. This demonstrates that malicious skills significantly weaken agent safety, highlighting an urgent need for ecosystem‑level defenses.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have evolved into autonomous agents that rely on open skill ecosystems (e.g., ClawHub and Skills.Rest), hosting numerous publicly reusable skills. Existing security research on these ecosystems mainly focuses on vulnerabilities within skills, such as prompt injection. However, there is a critical gap regarding skills that may be misused for harmful actions (e.g., cyber attacks, fraud and scams, privacy violations, and sexual content generation), namely harmful skills. In this paper, we present the first large-scale measurement study of harmful skills in agent ecosystems, covering 98,440 skills across two major registries. Using an LLM-driven scoring system grounded in our harmful skill taxonomy, we find that 4.93% of skills (4,858) are harmful, with ClawHub exhibiting an 8.84% harmful rate compared to 3.49% on Skills.Rest. We then construct HarmfulSkillBench, the first benchmark for evaluating agent safety against harmful skills in realistic agent contexts, comprising 200 harmful skills across 20 categories and four evaluation conditions. By evaluating six LLMs on HarmfulSkillBench, we find that presenting a harmful task through a pre-installed skill substantially lowers refusal rates across all models, with the average harm score rising from 0.27 without the skill to 0.47 with it, and further to 0.76 when the harmful intent is implicit rather than stated as an explicit user request. We responsibly disclose our findings to the affected registries and release our benchmark to support future research (see https://github.com/TrustAIRLab/HarmfulSkillBench).

</details>


### 26. Agentic Microphysics: A Manifesto for Generative AI Safety

- **Authors:** Federico Pierucci, Matteo Prandi, Marcantonio Bracale Syrnikov, Marcello Galisai, Piercosma Bisconti
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15236v1](http://arxiv.org/abs/2604.15236v1)
- **PDF:** [https://arxiv.org/pdf/2604.15236v1](https://arxiv.org/pdf/2604.15236v1)
- **Categories:** cs.CY, cs.AI


> **Main contribution** – The paper proposes a new methodological framework for AI safety that shifts the unit of analysis from isolated, “black‑box” language models to the *local interaction dynamics* among multiple agentic systems, co‑ining the term **agentic microphysics**. It argues that many emergent safety threats (e.g., coordination failures, cascading deception, or collective manipulation) can only be understood and mitigated by explicitly modeling how one agent’s output becomes another’s input within defined communication protocols.

**Methodology** – The authors formalize **agentic microphysics** as a graph‑based representation where nodes are agents (including their memory, planning, tool‑use, and identity modules) and edges capture protocol‑governed exchanges (messages, observations, actions). They then introduce **generative safety**, an inductive “grow‑from‑micro‑to‑macro” procedure: (1) enumerate elementary interaction patterns, (2) simulate their composition to see how risk‑relevant phenomena (e.g., reward hacking, misinformation spread) emerge, (3) identify causal thresholds and design knobs (protocol constraints, sandboxing, intervention policies) that can break harmful cascades. The framework blends analytical causal graphs with large‑scale multi‑agent simulations.

**Key findings** – Applying the framework to toy multi‑agent setups, the authors demonstrate that (a) certain minimal interaction motifs (e.g., reciprocal self‑referential prompting) can trigger runaway incentive amplification, and (b) modest protocol changes (bounded turn‑taking, verified output filtering) dramatically lower the probability of collective risk emergence. The results suggest that safety research must treat *interaction‑level mechanisms* as first‑class design variables, providing a concrete pathway for building controllable, scalable agentic AI ecosystems.


<details>
<summary>Abstract</summary>

This paper advances a methodological proposal for safety research in agentic AI. As systems acquire planning, memory, tool use, persistent identity, and sustained interaction, safety can no longer be analysed primarily at the level of the isolated model. Population-level risks arise from structured interaction among agents, through processes of communication, observation, and mutual influence that shape collective behaviour over time. As the object of analysis shifts, a methodological gap emerges. Approaches focused either on single agents or on aggregate outcomes do not identify the interaction-level mechanisms that generate collective risks or the design variables that control them. A framework is required that links local interaction structure to population-level dynamics in a causally explicit way, allowing both explanation and intervention. We introduce two linked concepts. Agentic microphysics defines the level of analysis: local interaction dynamics where one agent's output becomes another's input under specific protocol conditions. Generative safety defines the methodology: growing phenomena and elicit risks from micro-level conditions to identify sufficient mechanisms, detect thresholds, and design effective interventions.

</details>


### 27. RadAgent: A tool-using AI agent for stepwise interpretation of chest computed tomography

- **Authors:** Mélanie Roschewitz, Kenneth Styppa, Yitian Tao, Jiwoong Sohn, Jean-Benoit Delbrouck, Benjamin Gundersen, Nicolas Deperrois, Christian Bluethgen, Julia Vogt, Bjoern Menze, Farhad Nooralahzadeh, Michael Krauthammer, Michael Moor
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15231v1](http://arxiv.org/abs/2604.15231v1)
- **PDF:** [https://arxiv.org/pdf/2604.15231v1](https://arxiv.org/pdf/2604.15231v1)
- **Categories:** cs.AI


> RadAgent is a tool‑augmented generative AI agent that produces chest‑CT reports by iteratively invoking external “tools” (e.g., segmentation, retrieval, verification modules) and explicitly recording each intermediate decision, thereby yielding a human‑inspectable reasoning trace. The authors implement the agent with a language model controller that selects and calls the tools in a step‑wise loop, then aggregates the outputs into a final report; performance is evaluated against the 3‑D vision‑language model CT‑Chat. Across three benchmarks, RadAgent raises macro‑F1 clinical accuracy by 6.0 points (36 % relative), micro‑F1 by 5.4 points (20 % relative), improves adversarial robustness by 24.7 points (42 % relative), and—uniquely—achieves a 37 % faithfulness score, demonstrating that explicit, tool‑driven reasoning can make AI‑based radiology reporting more accurate, robust, and transparent.


<details>
<summary>Abstract</summary>

Vision-language models (VLM) have markedly advanced AI-driven interpretation and reporting of complex medical imaging, such as computed tomography (CT). Yet, existing methods largely relegate clinicians to passive observers of final outputs, offering no interpretable reasoning trace for them to inspect, validate, or refine. To address this, we introduce RadAgent, a tool-using AI agent that generates CT reports through a stepwise and interpretable process. Each resulting report is accompanied by a fully inspectable trace of intermediate decisions and tool interactions, allowing clinicians to examine how the reported findings are derived. In our experiments, we observe that RadAgent improves Chest CT report generation over its 3D VLM counterpart, CT-Chat, across three dimensions. Clinical accuracy improves by 6.0 points (36.4% relative) in macro-F1 and 5.4 points (19.6% relative) in micro-F1. Robustness under adversarial conditions improves by 24.7 points (41.9% relative). Furthermore, RadAgent achieves 37.0% in faithfulness, a new capability entirely absent in its 3D VLM counterpart. By structuring the interpretation of chest CT as an explicit, tool-augmented and iterative reasoning trace, RadAgent brings us closer toward transparent and reliable AI for radiology.

</details>


### 28. Scepsy: Serving Agentic Workflows Using Aggregate LLM Pipelines

- **Authors:** Marcel Wagenländer, Otto White, Britannio Jarrett, Pedro Silvestre, Yanda Tao, Guo Li, Huanzhou Zhu, Llúis Vilanova, Peter Pietzuch
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15186v1](http://arxiv.org/abs/2604.15186v1)
- **PDF:** [https://arxiv.org/pdf/2604.15186v1](https://arxiv.org/pdf/2604.15186v1)
- **Categories:** cs.DC, cs.AI


> The paper introduces **Scepsy**, a serving system that automatically schedules arbitrary multi‑LLM agentic workflows on GPU clusters. By profiling each LLM’s performance under different parallelism settings, Scepsy builds an **Aggregate LLM Pipeline** model that predicts latency/throughput for any fractional GPU share; a hierarchical search then selects tensor‑parallelism, replica counts, and GPU placements that minimize latency while meeting a target throughput. Experiments on realistic agentic pipelines show that Scepsy can deliver up to **2.4× higher throughput** and **27× lower latency** than approaches that treat each LLM in isolation or rely on static, user‑defined allocations, demonstrating a practical solution for high‑performance, low‑latency agentic AI services.


<details>
<summary>Abstract</summary>

Agentic workflows carry out complex tasks by orchestrating multiple large language models (LLMs) and tools. Serving such workflows at a target throughput with low latency is challenging because they can be defined using arbitrary agentic frameworks and exhibit unpredictable execution times: execution may branch, fan-out, or recur in data-dependent ways. Since LLMs in workflows often outnumber available GPUs, their execution also leads to GPU oversubscription.
  We describe Scepsy, a new agentic serving system that efficiently schedules arbitrary multi-LLM agentic workflows onto a GPU cluster. Scepsy exploits the insight that, while agentic workflows have unpredictable end-to-end latencies, the shares of each LLM's total execution times are comparatively stable across executions. Scepsy decides on GPU allocations based on these aggregate shares: first, it profiles the LLMs under different parallelism degrees. It then uses these statistics to construct an Aggregate LLM Pipeline, which is a lightweight latency/throughput predictor for allocations. To find a GPU allocation that minimizes latency while achieving a target throughput, Scepsy uses the Aggregate LLM Pipeline to explore a search space over fractional GPU shares, tensor parallelism degrees, and replica counts. It uses a hierarchical heuristic to place the best allocation onto the GPU cluster, minimizing fragmentation, while respecting network topology constraints. Our evaluation on realistic agentic workflows shows that Scepsy achieves up to 2.4x higher throughput and 27x lower latency compared to systems that optimize LLMs independently or rely on user-specified allocations.

</details>


### 29. Autonomous Evolution of EDA Tools: Multi-Agent Self-Evolved ABC

- **Authors:** Cunxi Yu, Haoxing Ren
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15082v1](http://arxiv.org/abs/2604.15082v1)
- **PDF:** [https://arxiv.org/pdf/2604.15082v1](https://arxiv.org/pdf/2604.15082v1)
- **Categories:** cs.AR, cs.AI


> **Main contribution:** The paper presents the first fully autonomous, self‑evolving logic‑synthesis framework that uses a team of Large Language Model (LLM) agents to iteratively rewrite, recompile, and improve the entire source code of the industry‑standard ABC EDA tool, while preserving its original binary interface.  

**Methodology:** Starting from an initial ABC codebase augmented with existing open‑source synthesis components, the authors define “programming‑guidance’’ prompts that direct LLM agents to modify specific sub‑modules. Each proposed change is automatically compiled, then subjected to a unified correctness check and a quality‑of‑results (QoR) evaluation on a diverse benchmark suite (ISCAS, VTR, EPFL, IWLS 2005). The agents receive feedback from these evaluations and repeat the cycle, effectively learning new synthesis heuristics without human‑crafted interventions.  

**Key findings:** Across multiple evolution cycles, the LLM‑driven system discovers optimizations that outperform traditional human‑designed heuristics, yielding measurable improvements in QoR on all benchmark suites while maintaining functional correctness. The results demonstrate that large‑scale (million‑line) EDA tools can be autonomously refined by multi‑agent AI, opening a pathway toward self‑improving design‑automation ecosystems.


<details>
<summary>Abstract</summary>

This paper introduces the first \emph{self-evolving} logic synthesis framework, which leverages Large Language Model (LLM) agents to autonomously improve the source code of \textsc{ABC}, the widely adopted logic synthesis system. Our framework operates on the \emph{entire integrated ABC codebase}, and the output repository preserves its single-binary execution model and command interface. In the initial evolution cycle, we bootstrap the system using existing prior open-source synthesis components, covering flow tuning, logic minimization, and technology mapping, but without manually injecting new heuristics. On top of this foundation, a team of LLM-based agents iteratively rewrites and evolves specific sub-components of ABC following our ``programming guidance`` prompts under a unified correctness and QoR-driven evaluation loop. Each evolution cycle proposes code modifications, compiles the integrated binary, validates correctness, and evaluates quality-of-results (QoR) on \emph{multi-suite benchmarks including ISCAS~85/89/99, VTR, EPFL, and IWLS~2005}. Through continuous feedback, the system discovers optimizations beyond human-designed heuristics, effectively \emph{learning new synthesis strategies} that enhance QoR. We detail the architecture of this self-improving system, its integration with \textsc{ABC}, and results demonstrating that the framework can autonomously and progressively improve EDA tool at full million-line scale.

</details>


### 30. Where are the Humans? A Scoping Review of Fairness in Multi-agent AI Systems

- **Authors:** Simeon Allmendinger, Luca Deck, Lucas Mueller
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15078v1](http://arxiv.org/abs/2604.15078v1)
- **PDF:** [https://arxiv.org/pdf/2604.15078v1](https://arxiv.org/pdf/2604.15078v1)
- **Categories:** cs.AI


> The paper conducts the first systematic scoping review of fairness research in multi‑agent AI (MAAI), analysing 23 peer‑reviewed works and distilling five dominant “archetypal” approaches. By qualitatively coding the literature, the authors show that most studies treat fairness as a superficial, post‑hoc add‑on, lack clear normative foundations, and ignore the emergent dynamics of autonomous agents and system‑level interactions. They argue that fair MAAI must be designed with explicit human oversight, well‑defined fairness objectives and beneficiaries, and integrated throughout the development lifecycle, and they outline concrete research gaps and avenues for building such structurally fair agentic systems.


<details>
<summary>Abstract</summary>

Rapid advances in Generative AI are giving rise to increasingly sophisticated Multi-Agent AI (MAAI) systems. While AI fairness has been extensively studied in traditional predictive scenarios, its examination in MAAI remains nascent and fragmented. This scoping review critically synthesizes existing research on fairness in MAAI systems. Through a qualitative content analysis of 23 selected studies, we identify five archetypal approaches. Our findings reveal that fairness in MAAI systems is often addressed superficially, lacks robust normative foundations, and frequently overlooks the complex dynamics introduced by agent autonomy and system-level interactions. We argue that fairness must be embedded structurally throughout the development lifecycle of MAAI, rather than appended as a post-hoc consideration. Meaningful evaluation requires explicit human oversight, normative clarity, and a precise articulation of fairness objectives and beneficiaries. This review provides a foundation for advancing fairness research in MAAI systems by highlighting critical gaps, exposing prevailing limitations, and suggesting pathways.

</details>


### 31. CoGrid & the Multi-User Gymnasium: A Framework for Multi-Agent Experimentation

- **Authors:** Chase McDonald, Cleotilde Gonzalez
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15044v1](http://arxiv.org/abs/2604.15044v1)
- **PDF:** [https://arxiv.org/pdf/2604.15044v1](https://arxiv.org/pdf/2604.15044v1)
- **Categories:** cs.HC, cs.AI


> The paper introduces **CoGrid**, a lightweight grid‑world library with interchangeable NumPy and JAX back‑ends for fast multi‑agent simulation, and **Multi‑User Gymnasium (MUG)**, a wrapper that turns any CoGrid (or Gymnasium‑compatible) environment into a web‑based, real‑time experiment supporting arbitrary numbers of human participants and AI agents. By combining server‑authoritative or peer‑to‑peer networking with rollback netcode, the framework handles latency and synchronizes actions across users, enabling rapid deployment of human‑AI interaction studies. Case‑study experiments demonstrate that the tools can reliably host mixed human‑AI populations, produce reproducible data, and lower the technical barrier for psychologists and AI researchers to investigate social decision‑making, cognition, and coordination in multi‑agent settings.


<details>
<summary>Abstract</summary>

The increasing integration of artificial intelligence (AI) in everyday life brings with it new challenges and questions for regarding how humans interact with autonomous agents. Multi-agent experiments, where humans and AI act together, can offer important opportunities to study social decision making, but there is a lack of accessible tooling available to researchers to run such experiments. We introduce two tools designed to reduce these barriers. The first, CoGrid, is a multi-agent grid-based simulation library with dual NumPy and JAX backends. The second, Multi-User Gymnasium (MUG), translates such simulation environments directly into interactive web-based experiments. MUG supports interactions with arbitrary numbers of humans and AI, utilizing either server-authoritative or peer-to-peer networking with rollback netcode to account for latency. Together, these tools can enable researchers to deploy studies of human-AI interaction, facilitating inquiry into core questions of psychology, cognition, and decision making and their relationship to human-AI interaction. Both tools are open source and available to the broader research community. Documentation and source code is available at {cogrid, multi-user-gymnasium}.readthedocs.io. This paper details the functionality of these tools and presents several case studies to illustrate their utility in human-AI multi-agent experimentation.

</details>


### 32. From Reactive to Proactive: Assessing the Proactivity of Voice Agents via ProVoice-Bench

- **Authors:** Ke Xu, Yuhao Wang, Yu Wang
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15037v1](http://arxiv.org/abs/2604.15037v1)
- **PDF:** [https://arxiv.org/pdf/2604.15037v1](https://arxiv.org/pdf/2604.15037v1)
- **Categories:** cs.AI, cs.CL, cs.SD


> **Main contribution:** The paper introduces **ProVoice‑Bench**, the first benchmark that explicitly measures the proactivity of voice‑based AI agents, featuring four newly defined tasks that require agents to monitor context, anticipate user needs, and intervene appropriately.

**Methodology:** The authors build a multi‑stage data‑synthesis pipeline that generates 1,182 high‑quality, multimodal test instances covering scenarios such as timely reminders, unsolicited suggestions, and safety‑critical alerts. They then evaluate several state‑of‑the‑art multimodal LLM agents on these tasks, analyzing metrics for correct triggering, false‑positive (over‑triggering) rates, and reasoning depth.

**Key findings:** Across all models, there is a sizable performance gap: current agents frequently over‑trigger or fail to reason about when proactive actions are justified, indicating that existing LLMs are still primarily reactive. The results map out concrete weaknesses and suggest research directions—better context modeling, uncertainty estimation, and grounded reasoning—to advance truly proactive, natural voice agents.


<details>
<summary>Abstract</summary>

Recent advancements in LLM agents are gradually shifting from reactive, text-based paradigms toward proactive, multimodal interaction. However, existing benchmarks primarily focus on reactive responses, overlooking the complexities of proactive intervention and monitoring. To bridge this gap, we introduce ProVoice-Bench, the first evaluation framework specifically designed for proactive voice agents, featuring four novel tasks. By leveraging a multi-stage data synthesis pipeline, we curate 1,182 high-quality samples for rigorous testing. Our evaluation of state-of-the-art Multimodal LLMs reveals a significant performance gap, particularly regarding over-triggering and reasoning capabilities. These findings highlight the limitations of current models and offer a roadmap for developing more natural, context-aware proactive agents.

</details>


### 33. Autogenesis: A Self-Evolving Agent Protocol

- **Authors:** Wentao Zhang
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15034v1](http://arxiv.org/abs/2604.15034v1)
- **PDF:** [https://arxiv.org/pdf/2604.15034v1](https://arxiv.org/pdf/2604.15034v1)
- **Categories:** cs.AI


> The paper introduces the **Autogenesis Protocol (AGP)**, a two‑layer framework that cleanly separates *what* in an LLM‑based system may evolve (prompts, agents, tools, environments, memory) from *how* the evolution is carried out. The **Resource Substrate Protocol Layer (RSPL)** registers each resource type with explicit state, lifecycle, and versioned interfaces, while the **Self‑Evolution Protocol Layer (SEPL)** provides a closed‑loop operator for proposing, evaluating, and committing updates with full auditability and rollback. Using AGP, the authors build **Autogenesis System (AGS)**—a multi‑agent architecture that dynamically instantiates, retrieves, and refines these resources during execution—and show on several long‑horizon, tool‑use benchmarks that AGS consistently outperforms strong baselines, confirming that systematic resource management and closed‑loop self‑evolution markedly improve the robustness and performance of agentic AI systems.


<details>
<summary>Abstract</summary>

Recent advances in LLM based agent systems have shown promise in tackling complex, long horizon tasks. However, existing agent protocols (e.g., A2A and MCP) under specify cross entity lifecycle and context management, version tracking, and evolution safe update interfaces, which encourages monolithic compositions and brittle glue code. We introduce \textbf{\textsc{Autogenesis Protocol (AGP)}}, a self evolution protocol that decouples what evolves from how evolution occurs. Its Resource Substrate Protocol Layer (RSPL) models prompts, agents, tools, environments, and memory as protocol registered resources\footnote{Unless otherwise specified, resources refer to instances of the five RSPL entity types: \emph{prompt}, \emph{agent}, \emph{tool}, \emph{environment}, \emph{memory} with agent \emph{outputs}.} with explicit state, lifecycle, and versioned interfaces. Its Self Evolution Protocol Layer (SEPL) specifies a closed loop operator interface for proposing, assessing, and committing improvements with auditable lineage and rollback. Building on \textbf{\textsc{AGP}}, we present \textbf{\textsc{Autogenesis System (AGS)}}, a self-evolving multi-agent system that dynamically instantiates, retrieves, and refines protocol-registered resources during execution. We evaluate \textbf{\textsc{AGS}} on multiple challenging benchmarks that require long horizon planning and tool use across heterogeneous resources. The results demonstrate consistent improvements over strong baselines, supporting the effectiveness of agent resource management and closed loop self evolution.

</details>


### 34. COEVO: Co-Evolutionary Framework for Joint Functional Correctness and PPA Optimization in LLM-Based RTL Generation

- **Authors:** Heng Ping, Peiyu Zhang, Shixuan Li, Wei Yang, Anzhe Cheng, Shukai Duan, Xiaole Zhang, Paul Bogdan
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15001v2](http://arxiv.org/abs/2604.15001v2)
- **PDF:** [https://arxiv.org/pdf/2604.15001v2](https://arxiv.org/pdf/2604.15001v2)
- **Categories:** cs.AI


> **Contribution:** COEVO introduces a unified co‑evolutionary framework that simultaneously optimizes functional correctness and the full Pareto‑front of area, delay, and power for RTL generated by large language models, breaking the conventional pipeline that treats correctness and PPA as separate, sequential stages.  

**Methodology:** The system embeds a continuous correctness score (derived from a diagnostic testbench) as a fourth optimization dimension alongside the three PPA metrics, runs a single evolutionary loop with an annealed correctness gate that retains partially correct but PPA‑promising candidates, and uses four‑dimensional Pareto non‑dominated sorting (instead of scalar fitness) to preserve trade‑offs without manual weighting.  

**Key Findings:** On the VerilogEval 2.0 and RTLLM 2.0 benchmarks, COEVO attains 97.5 % and 94.5 % Pass@1 with GPT‑5.4‑mini—outperforming all prior agentic baselines across four LLM backbones—and achieves the best PPA results on 43 of 49 synthesizable designs, demonstrating that joint co‑evolution dramatically improves both correctness and hardware quality in LLM‑based RTL generation.


<details>
<summary>Abstract</summary>

LLM-based RTL code generation methods increasingly target both functional correctness and PPA quality, yet existing approaches universally decouple the two objectives, optimizing PPA only after correctness is fully achieved. Whether through sequential multi-agent pipelines, evolutionary search with binary correctness gates, or hierarchical reward dependencies, partially correct but architecturally promising candidates are systematically discarded. Moreover, existing methods reduce the multi-objective PPA space to a single scalar fitness, obscuring the trade-offs among area, delay, and power. To address these limitations, we propose COEVO, a co-evolutionary framework that unifies correctness and PPA optimization within a single evolutionary loop. COEVO formulates correctness as a continuous co-optimization dimension alongside area, delay, and power, enabled by an enhanced testbench that provides fine-grained scoring and detailed diagnostic feedback. An adaptive correctness gate with annealing allows PPA-promising but partially correct candidates to guide the search toward jointly optimal solutions. To preserve the full PPA trade-off structure, COEVO employs four-dimensional Pareto-based non-dominated sorting with configurable intra-level sorting, replacing scalar fitness without manual weight tuning. Evaluated on VerilogEval 2.0 and RTLLM 2.0, COEVO achieves 97.5\% and 94.5\% Pass@1 with GPT-5.4-mini, surpassing all agentic baselines across four LLM backbones, while attaining the best PPA on 43 out of 49 synthesizable RTLLM designs.

</details>


### 35. Dr.~RTL: Autonomous Agentic RTL Optimization through Tool-Grounded Self-Improvement

- **Authors:** Wenji Fang, Yao Lu, Shang Liu, Jing Wang, Ziyan Guo, Junxian He, Fengbin Tu, Zhiyao Xie
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14989v1](http://arxiv.org/abs/2604.14989v1)
- **PDF:** [https://arxiv.org/pdf/2604.14989v1](https://arxiv.org/pdf/2604.14989v1)
- **Categories:** cs.AI, cs.AR


> **Main contribution:** The paper introduces **Dr. RTL**, a multi‑agent, self‑improving framework that automates RTL timing‑optimization by learning reusable “skill” patterns from parallel rewrite attempts and continuously distilling them into an interpretable library.  

**Methodology:** Dr. RTL integrates three specialized agents for critical‑path analysis, parallel RTL rewriting, and tool‑based evaluation within a realistic industrial EDA flow; it employs “group‑relative skill learning” to compare the outcomes of concurrent rewrites, extract effective pattern‑strategy pairs, and store them for cross‑design reuse.  

**Key findings:** Tested on 20 real‑world RTL blocks using an industrial synthesis toolchain, Dr. RTL outperforms the leading commercial synthesizer, delivering on average a 21 % improvement in worst‑negative‑slack (WNS), a 17 % reduction in total‑negative‑slack (TNS), and a 6 % area shrinkage, while continuously expanding a library of 47 reusable optimization skills.


<details>
<summary>Abstract</summary>

Recent advances in large language models (LLMs) have sparked growing interest in automatic RTL optimization for better performance, power, and area (PPA). However, existing methods are still far from realistic RTL optimization. Their evaluation settings are often unrealistic: they are tested on manually degraded, small-scale RTL designs and rely on weak open-source tools. Their optimization methods are also limited, relying on coarse design-level feedback and simple pre-defined rewriting rules. To address these limitations, we present Dr. RTL, an agentic framework for RTL timing optimization in a realistic evaluation environment, with continual self-improvement through reusable optimization skills. We establish a realistic evaluation setting with more challenging RTL designs and an industrial EDA workflow. Within this setting, Dr. RTL performs closed-loop optimization through a multi-agent framework for critical-path analysis, parallel RTL rewriting, and tool-based evaluation. We further introduce group-relative skill learning, which compares parallel RTL rewrites and distills the optimization experience into an interpretable skill library. Currently, this library contains 47 pattern--strategy entries for cross-design reuse to improve PPA and accelerate convergence, and it can continue evolving over time. Evaluated on 20 real-world RTL designs, Dr. RTL achieves average WNS/TNS improvements of 21\%/17\% with a 6\% area reduction over the industry-leading commercial synthesis tool.

</details>


### 36. Agentic Explainability at Scale: Between Corporate Fears and XAI Needs

- **Authors:** Yomna Elsayed, Cecily Jones
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14984v1](http://arxiv.org/abs/2604.14984v1)
- **PDF:** [https://arxiv.org/pdf/2604.14984v1](https://arxiv.org/pdf/2604.14984v1)
- **Categories:** cs.HC, cs.AI


> The paper identifies a new enterprise risk—**“Agent Sprawl”**—that arises when organizations rapidly scale low‑code, autonomous AI agents without matching governance and observability, leading to opaque agent‑to‑agent interactions. Through interviews with AI‑governance professionals, the authors pinpoint the most pressing concerns (loss of control, hidden decision logic, and compliance gaps) and propose a two‑pronged explainability framework: (1) **design‑time artifacts** (e.g., structured Agentic AI Cards that document an agent’s purpose, configuration, data sources, and communication contracts) and (2) **runtime observability tools** that surface configuration snapshots and trace inter‑agent messages for audit and debugging. A prototype implementation of the Agentic AI Card demonstrates that embedding these artifacts into the development and deployment pipelines markedly improves transparency, reduces perceived risk, and offers a practical pathway for scalable, governed agentic AI in corporate settings.


<details>
<summary>Abstract</summary>

As companies enter the race for agentic AI adoption, fears surface around agentic autonomy and its subsequent risks. These fears compound as companies scale their agentic AI adoption with low-code applications, without a comparable scaling in their governance processes and expertise resulting in a phenomenon known as "Agent Sprawl". While shadow AI tools can help with agentic discovery and identification, few observability tools offer insights into the agents' configuration and settings or the decision-making process during agent-to-agent communication and orchestration. This paper explores AI governance professionals' concerns in enterprise settings, while offering design-time and runtime explainability techniques as suggested by AI governance experts for addressing those fears. Finally, we provide a preliminary prototype of an Agentic AI Card that can help companies feel at ease deploying agents at scale.

</details>


### 37. Discovering Novel LLM Experts via Task-Capability Coevolution

- **Authors:** Andrew Dai, Boris Meinardus, Ciaran Regan, Yingtao Tian, Yujin Tang
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14969v1](http://arxiv.org/abs/2604.14969v1)
- **PDF:** [https://arxiv.org/pdf/2604.14969v1](https://arxiv.org/pdf/2604.14969v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **Assessment Coevolving with Diverse Capabilities (AC/DC)**, an open‑ended coevolutionary framework that simultaneously evolves large‑language‑model (LLM) populations (via model merging) and their evaluation tasks (via synthetic data generation), enabling continual discovery of novel expert abilities without manual dataset or reward design.  

**Methodology:** Starting from a pool of base LLMs, AC/DC iteratively generates new natural‑language tasks, evaluates the current models on them, selects high‑performing model–task pairs, and creates offspring models by merging parameters of top performers; an archive stores diverse “expert” models that are retained based on novelty and coverage metrics.  

**Key findings:** Over a single training run, AC/DC produces a growing archive of compact LLMs that collectively exhibit broader expertise than larger, static baselines and achieve higher coverage on downstream benchmarks, improve multi‑agent best‑of‑N selection, and continuously innovate both tasks and capabilities, demonstrating that coevolution can serve as a scalable route to agentic AI with expanding, diversified skill sets.


<details>
<summary>Abstract</summary>

Frontier model developers aim to train models continually to possess emergent, diverse capabilities. To extend capabilities, the current pre-training and post-training paradigm requires manually starting training runs with static datasets or reward functions every time. Addressing this limitation, our work pursues the insight that open-endedness (via the coevolution of models and tasks) can discover models with increasingly novel skills in a single run. We introduce a new model development framework that extends coevolution to large language model (LLM) discovery, open-ended \textit{Assessment Coevolving with Diverse Capabilities} (AC/DC). AC/DC evolves both LLMs via model merging and natural language tasks via synthetic data generation. AC/DC discovers growing archives of LLMs that surpass the capabilities of larger LLMs while taking up less GPU memory. In particular, our LLM populations achieve a broader Coverage of expertise than other curated models or baselines on downstream benchmarks, without \textit{any} explicit benchmark optimization. Furthermore, AC/DC improves Coverage over time, continually innovates on tasks and models, and improves performance in multi-agent best-of-N selection. Our findings highlight the potential of coevolution as a means of discovering broader sets of capabilities from base LLMs. Overall, AC/DC brings us one step closer to a profoundly new paradigm of LLM development, where continual improvements to the diversity of model capabilities can be accelerated by leveraging existing models as stepping stones to increasingly powerful models.

</details>


### 38. RaTA-Tool: Retrieval-based Tool Selection with Multimodal Large Language Models

- **Authors:** Gabriele Mattioli, Evelyn Turri, Sara Sarto, Lorenzo Baraldi, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14951v1](http://arxiv.org/abs/2604.14951v1)
- **PDF:** [https://arxiv.org/pdf/2604.14951v1](https://arxiv.org/pdf/2604.14951v1)
- **Categories:** cs.CV, cs.AI, cs.CL, cs.MM


> The paper presents **RaTA‑Tool**, a retrieval‑based framework that lets multimodal large language models (MLLMs) handle open‑world tool use by first translating a multimodal user request into a structured task description and then matching it against a corpus of machine‑readable tool specifications (derived from Hugging Face model cards). The authors train the MLLM with a two‑stage pipeline—semantic encoding of queries followed by Direct Preference Optimization (DPO) to align the generated task descriptions with the most suitable tools—so that new tools can be added without any model retraining. Experiments on a newly released multimodal tool‑use dataset show that RaTA‑Tool markedly outperforms prior text‑only, closed‑world baselines in both tool‑selection accuracy and generalization to previously unseen tools.


<details>
<summary>Abstract</summary>

Tool learning with foundation models aims to endow AI systems with the ability to invoke external resources -- such as APIs, computational utilities, and specialized models -- to solve complex tasks beyond the reach of standalone language generation. While recent advances in Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) have expanded their reasoning and perception capabilities, existing tool-use methods are predominantly limited to text-only inputs and closed-world settings. Consequently, they struggle to interpret multimodal user instructions and cannot generalize to tools unseen during training. In this work, we introduce RaTA-Tool, a novel framework for open-world multimodal tool selection. Rather than learning direct mappings from user queries to fixed tool identifiers, our approach enables an MLLM to convert a multimodal query into a structured task description and subsequently retrieve the most appropriate tool by matching this representation against semantically rich, machine-readable tool descriptions. This retrieval-based formulation naturally supports extensibility to new tools without retraining. To further improve alignment between task descriptions and tool selection, we incorporate a preference-based optimization stage using Direct Preference Optimization (DPO). To support research in this setting, we also introduce the first dataset for open-world multimodal tool use, featuring standardized tool descriptions derived from Hugging Face model cards. Extensive experiments demonstrate that our approach significantly improves tool-selection performance, particularly in open-world, multimodal scenarios.

</details>


### 39. Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis

- **Authors:** Zhiyuan Zhai, Wenjing Yan, Xiaodan Shao, Xin Wang
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14877v1](http://arxiv.org/abs/2604.14877v1)
- **PDF:** [https://arxiv.org/pdf/2604.14877v1](https://arxiv.org/pdf/2604.14877v1)
- **Categories:** cs.LG


> **Main contribution:** The paper introduces a new two‑dimensional evaluation metric, PASS@(k,T), that jointly varies the sampling budget k and the number of interaction rounds T, allowing a clean separation between pure efficiency gains and genuine capability expansion in language‑model agents that use tools.

**Methodology:** Using PASS@(k,T) the authors compare base LLM agents, RL‑fine‑tuned agents, and supervised‑fine‑tuned agents on a suite of tool‑use problems that differ in compositional complexity. They control for training data size, analyse the effect of RL on the distribution over base strategies, and isolate the role of self‑directed exploration.

**Key findings:** For compositional, sequential information‑gathering tasks, RL fine‑tuning **does expand the capability boundary**: the RL agent’s pass‑curve lies above the base model’s and the gap widens as k increases, unlike the convergence observed in static‑reasoning settings. The improvement stems from RL re‑weighting base strategies toward those that integrate retrieved information more effectively, whereas supervised fine‑tuning does not yield the same expansion. Consequently, RL can both make agents more reliable and, on the right class of tasks, genuinely more capable.


<details>
<summary>Abstract</summary>

Does reinforcement learning genuinely expand what LLM agents can do, or merely make them more reliable? For static reasoning, recent work answers the second: base and RL pass@k curves converge at large k. We ask whether this holds for agentic tool use, where T rounds of interaction enable compositional strategies that re-sampling cannot recover. We introduce PASS@(k,T), a two-dimensional metric that jointly varies sampling budget k and interaction depth T, separating capability expansion from efficiency improvement. Our main finding is that, contrary to the static-reasoning result, tool-use RL genuinely enlarges the capability boundary: the RL agent's pass-curve pulls above the base model's and the gap widens at large k rather than converging. The expansion is specific to compositional, sequential information gathering; on simpler tasks RL behaves as prior work predicts. Under matched training data, supervised fine-tuning regresses the boundary on the same compositional tasks, isolating self-directed exploration as the causal factor. Mechanism analysis shows RL reweights the base strategy distribution toward the subset whose downstream reasoning more often yields a correct answer, with the improvement concentrated on how the agent integrates retrieved information. These results reconcile optimistic and pessimistic readings of RL for LLMs: both are correct, on different task types.

</details>


### 40. Benchmarks for Trajectory Safety Evaluation and Diagnosis in OpenClaw and Codex: ATBench-Claw and ATBench-CodeX

- **Authors:** Zhonghao Yang, Yu Li, Yanxu Zhu, Tianyi Zhou, Yuejin Xie, Haoyu Luo, Jing Shao, Xia Hu, Dongrui Liu
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14858v1](http://arxiv.org/abs/2604.14858v1)
- **PDF:** [https://arxiv.org/pdf/2604.14858v1](https://arxiv.org/pdf/2604.14858v1)
- **Categories:** cs.AI, cs.SE


> **Main contribution:** The paper introduces ATBench‑Claw and ATBench‑CodeX, two domain‑specific extensions of the ATBench benchmark suite that enable systematic safety evaluation and diagnostic analysis of agent trajectories in the OpenClaw tool‑chain and OpenAI Codex/Codex‑runtime environments.  

**Methodology:** The authors first dissect each target setting, then tailor the three‑dimensional ATBench Safety Taxonomy (risk source × failure mode × real‑world harm) to capture its unique hazards. The customized taxonomy drives a shared benchmark‑generation pipeline that automatically synthesizes diverse, realistic agent trajectories covering the relevant risk space (e.g., tools/skills/sessions in OpenClaw; repositories, patches, dependencies, policy limits in Codex).  

**Key findings:** The customized taxonomies yield benchmarks that densely cover domain‑specific failure modes—such as unsafe tool invocations in OpenClaw and unsafe code modifications or policy violations in Codex—thereby exposing gaps in existing safety monitors and diagnostic tools. Experiments show that agents evaluated on ATBench‑Claw and ATBench‑CodeX experience a broader spectrum of safety incidents than on prior generic benchmarks, confirming the necessity of taxonomy‑driven, extensible benchmark design for robust safety assessment of evolving agentic AI systems.


<details>
<summary>Abstract</summary>

As agent systems move into increasingly diverse execution settings, trajectory-level safety evaluation and diagnosis require benchmarks that evolve with them. ATBench is a diverse and realistic agent trajectory benchmark for safety evaluation and diagnosis. This report presents ATBench-Claw and ATBench-CodeX, two domain-customized extensions that carry ATBench into the OpenClaw and OpenAI Codex / Codex-runtime settings. The key adaptation mechanism is to analyze each new setting, customize the three-dimensional Safety Taxonomy over risk source, failure mode, and real-world harm, and then use that customized taxonomy to define the benchmark specification consumed by the shared ATBench construction pipeline. This extensibility matters because agent frameworks remain relatively stable at the architectural level even as their concrete execution settings, tool ecosystems, and product capabilities evolve quickly. Concretely, ATBench-Claw targets OpenClaw-sensitive execution chains over tools, skills, sessions, and external actions, while ATBench-CodeX targets trajectories in the OpenAI Codex / Codex-runtime setting over repositories, shells, patches, dependencies, approvals, and runtime policy boundaries. Our emphasis therefore falls on taxonomy customization, domain-specific risk coverage, and benchmark design under a shared ATBench generation framework.

</details>


### 41. Knowing When Not to Answer: Evaluating Abstention in Multimodal Reasoning Systems

- **Authors:** Nishanth Madhusudhan, Vikas Yadav, Alexandre Lacoste
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14799v1](http://arxiv.org/abs/2604.14799v1)
- **PDF:** [https://arxiv.org/pdf/2604.14799v1](https://arxiv.org/pdf/2604.14799v1)
- **Categories:** cs.CL, cs.CV


> **Paper summary**  
The authors introduce **MM‑AQA**, a new benchmark that explicitly creates unanswerable multimodal questions by degrading visual information and/or removing essential textual evidence, enabling systematic evaluation of **effective abstention (EA)** in vision‑language models (VLMs) and multi‑agent systems (MAS). Using this benchmark, they test three state‑of‑the‑art VLMs (both closed‑ and open‑source) and two MAS architectures on 2,079 samples, finding that (1) standard prompting makes VLMs almost never abstain, while simple confidence‑threshold baselines already outperform them; (2) MAS frameworks improve abstention rates but incur a clear accuracy‑abstention trade‑off; and (3) sequential MAS designs match or beat more complex iterative agents, indicating that the main limitation is model mis‑calibration rather than depth of reasoning. The study concludes that **abstention‑aware training**, not just better prompting or adding agents, is essential for reliable multimodal reasoning systems.


<details>
<summary>Abstract</summary>

Effective abstention (EA), recognizing evidence insufficiency and refraining from answering, is critical for reliable multimodal systems. Yet existing evaluation paradigms for vision-language models (VLMs) and multi-agent systems (MAS) assume answerability, pushing models to always respond. Abstention has been studied in text-only settings but remains underexplored multimodally; current benchmarks either ignore unanswerability or rely on coarse methods that miss realistic failure modes. We introduce MM-AQA, a benchmark that constructs unanswerable instances from answerable ones via transformations along two axes: visual modality dependency and evidence sufficiency. Evaluating three frontier VLMs spanning closed and open-source models and two MAS architectures across 2079 samples, we find: (1) under standard prompting, VLMs rarely abstain; even simple confidence baselines outperform this setup, (2) MAS improves abstention but introduces an accuracy-abstention trade-off, (3) sequential designs match or exceed iterative variants, suggesting the bottleneck is miscalibration rather than reasoning depth, and (4) models abstain when image or text evidence is absent, but attempt reconciliation with degraded or contradictory evidence. Effective multimodal abstention requires abstention-aware training rather than better prompting or more agents.

</details>


### 42. HWE-Bench: Benchmarking LLM Agents on Real-World Hardware Bug Repair Tasks

- **Authors:** Fan Cui, Hongyuan Hou, Zizhang Luo, Chenyun Yin, Yun Liang
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14709v1](http://arxiv.org/abs/2604.14709v1)
- **PDF:** [https://arxiv.org/pdf/2604.14709v1](https://arxiv.org/pdf/2604.14709v1)
- **Categories:** cs.AI


> The paper presents **HWE‑Bench**, the first repository‑scale benchmark that tests LLM‑driven agents on authentic hardware‑bug‑fix pull‑requests (417 instances from six open‑source Verilog/SystemVerilog and Chisel projects). Using a fully containerized flow that runs the projects’ native simulators and regression suites, the authors evaluate seven LLMs within four existing agent frameworks and show that the strongest agent solves 70.7 % of bugs overall—exceeding 90 % on small cores but falling below 65 % on large SoC‑level designs. Failure analysis reveals that most errors occur during fault localization, hardware‑semantic reasoning, and coordination across RTL, configuration, and verification artifacts, highlighting concrete research directions for more capable hardware‑aware AI agents.


<details>
<summary>Abstract</summary>

Existing benchmarks for hardware design primarily evaluate Large Language Models (LLMs) on isolated, component-level tasks such as generating HDL modules from specifications, leaving repository-scale evaluation unaddressed. We introduce HWE-Bench, the first large-scale, repository-level benchmark for evaluating LLM agents on real-world hardware bug repair tasks. HWE-Bench comprises 417 task instances derived from real historical bug-fix pull requests across six major open-source projects spanning both Verilog/SystemVerilog and Chisel, covering RISC-V cores, SoCs, and security roots-of-trust. Each task is grounded in a fully containerized environment where the agent must resolve a real bug report, with correctness validated through the project's native simulation and regression flows. The benchmark is built through a largely automated pipeline that enables efficient expansion to new repositories. We evaluate seven LLMs with four agent frameworks and find that the best agent resolves 70.7% of tasks overall, with performance exceeding 90% on smaller cores but dropping below 65% on complex SoC-level projects. We observe larger performance gaps across models than commonly reported on software benchmarks, and difficulty is driven by project scope and bug-type distribution rather than code size alone. Our failure analysis traces agent failures to three stages of the debugging process: fault localization, hardware-semantic reasoning, and cross-artifact coordination across RTL, configuration, and verification components, providing concrete directions for developing more capable hardware-aware agents.

</details>


### 43. CAMO: An Agentic Framework for Automated Causal Discovery from Micro Behaviors to Macro Emergence in LLM Agent Simulations

- **Authors:** Xiangning Yu, Yuwei Guo, Yuqi Hou, Xiao Xue, Qun Ma
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14691v1](http://arxiv.org/abs/2604.14691v1)
- **PDF:** [https://arxiv.org/pdf/2604.14691v1](https://arxiv.org/pdf/2604.14691v1)
- **Categories:** cs.AI, cs.CL, cs.CY


> **Main contribution:** The paper introduces **CAMO**, a fully automated causal‑discovery framework that extracts mechanistic explanations linking fine‑grained “micro” actions of large‑language‑model (LLM) agents to high‑level “macro” emergent outcomes in simulated societies.

**Methodology:** CAMO translates user‑specified mechanistic hypotheses into measurable factors derived from simulation logs, then learns a compact causal graph focused on a target emergent variable Y. It identifies the Markov boundary and a minimal upstream subgraph, produces interpretable causal chains, and leverages internal simulator counterfactual queries to orient ambiguous edges and iteratively revise hypotheses when contradictions arise.

**Key findings:** Across four benchmark emergence scenarios, CAMO successfully recovered known causal structures, highlighted actionable intervention levers, and outperformed baseline causal‑discovery methods in both precision of the inferred graph and efficiency of hypothesis revision, demonstrating a practical tool for probing and controlling emergence in agentic LLM simulations.


<details>
<summary>Abstract</summary>

LLM-empowered agent simulations are increasingly used to study social emergence, yet the micro-to-macro causal mechanisms behind macro outcomes often remain unclear. This is challenging because emergence arises from intertwined agent interactions and meso-level feedback and nonlinearity, making generative mechanisms hard to disentangle. To this end, we introduce \textbf{\textsc{CAMO}}, an automated \textbf{Ca}usal discovery framework from \textbf{M}icr\textbf{o} behaviors to \textbf{M}acr\textbf{o} Emergence in LLM agent simulations. \textsc{CAMO} converts mechanistic hypotheses into computable factors grounded in simulation records and learns a compact causal representation centered on an emergent target $Y$. \textsc{CAMO} outputs a computable Markov boundary and a minimal upstream explanatory subgraph, yielding interpretable causal chains and actionable intervention levers. It also uses simulator-internal counterfactual probing to orient ambiguous edges and revise hypotheses when evidence contradicts the current view. Experiments across four emergent settings demonstrate the promise of \textsc{CAMO}.

</details>


### 44. M2-PALE: A Framework for Explaining Multi-Agent MCTS--Minimax Hybrids via Process Mining and LLMs

- **Authors:** Yiyu Qian, Liyuan Zhao, Tim Miller
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14687v1](http://arxiv.org/abs/2604.14687v1)
- **PDF:** [https://arxiv.org/pdf/2604.14687v1](https://arxiv.org/pdf/2604.14687v1)
- **Categories:** cs.AI


> The paper introduces **M2‑PALE**, a novel framework that both strengthens and elucidates multi‑agent Monte‑Carlo Tree Search (MCTS) agents by augmenting their rollout phase with a shallow, full‑width Minimax search and subsequently extracting interpretable decision‑making logic via process‑mining techniques (Alpha Miner, iDHM, Inductive Miner) coupled to large language models (LLMs). The authors implement the hybrid MCTS‑Minimax algorithm in a checkers testbed, generate execution traces, mine compact workflow models of the agents’ search behavior, and prompt LLMs to translate these models into causal and distal natural‑language explanations. Experiments show that the Minimax‑enhanced rollouts improve strategic depth while the M2‑PALE pipeline produces concise, human‑readable explanations that faithfully reflect the agents’ underlying reasoning, demonstrating a scalable route for explainability of complex hybrid planning agents.


<details>
<summary>Abstract</summary>

Monte-Carlo Tree Search (MCTS) is a fundamental sampling-based search algorithm widely used for online planning in sequential decision-making domains. Despite its success in driving recent advances in artificial intelligence, understanding the behavior of MCTS agents remains a challenge for both developers and users. This difficulty stems from the complex search trees produced through the simulation of numerous future states and their intricate relationships. A known weakness of standard MCTS is its reliance on highly selective tree construction, which may lead to the omission of crucial moves and a vulnerability to tactical traps. To resolve this, we incorporate shallow, full-width Minimax search into the rollout phase of multi-agent MCTS to enhance strategic depth. Furthermore, to demystify the resulting decision-making logic, we introduce \textsf{M2-PALE} (MCTS--Minimax Process-Aided Linguistic Explanations). This framework employs process mining techniques, specifically the Alpha Miner, iDHM, and Inductive Miner algorithms, to extract underlying behavioral workflows from agent execution traces. These process models are then synthesized by LLMs to generate human-readable causal and distal explanations. We demonstrate the efficacy of our approach in a small-scale checkers environment, establishing a scalable foundation for interpreting hybrid agents in increasingly complex strategic domains.

</details>


### 45. DR$^{3}$-Eval: Towards Realistic and Reproducible Deep Research Evaluation

- **Authors:** Qianqian Xie, Qingheng Xiong, He Zhu, Tiantian Xia, Xueming Han, Fanyu Meng, Jiakai Wang, Zhiqi Bai, Chengkang Jiang, Zhaohui Wang, Yubin Guo, Yuqing Wen, Jiayang Mao, Zijie Zhang, Shihao Li, Yanghai Wang, Yuxiang Ren, Junlan Feng, Jiaheng Liu
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14683v1](http://arxiv.org/abs/2604.14683v1)
- **PDF:** [https://arxiv.org/pdf/2604.14683v1](https://arxiv.org/pdf/2604.14683v1)
- **Categories:** cs.AI


> The paper introduces **DR³‑Eval**, a benchmark that provides a realistic yet fully reproducible “open‑web” sandbox for assessing Deep Research Agents (DRAs) on multimodal, multi‑file research report generation. The authors build the benchmark from real user‑supplied tasks and a static corpus containing relevant documents, distractors, and noise, and propose a multidimensional evaluation suite (Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality) whose scores are shown to correlate with human judgments. Using DR³‑Eval, they evaluate a newly built multi‑agent system (DR³‑Agent) built on several state‑of‑the‑art LLMs, uncovering major weaknesses in retrieval robustness and hallucination control, thereby establishing a rigorous testbed for future agentic AI research.


<details>
<summary>Abstract</summary>

Deep Research Agents (DRAs) aim to solve complex, long-horizon research tasks involving planning, retrieval, multimodal understanding, and report generation, yet their evaluation remains challenging due to dynamic web environments and ambiguous task definitions. We propose DR$^{3}$-Eval, a realistic and reproducible benchmark for evaluating deep research agents on multimodal, multi-file report generation. DR$^{3}$-Eval is constructed from authentic user-provided materials and paired with a per-task static research sandbox corpus that simulates open-web complexity while remaining fully verifiable, containing supportive documents, distractors, and noise. Moreover, we introduce a multi-dimensional evaluation framework measuring Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality, and validate its alignment with human judgments. Experiments with our developed multi-agent system DR$^{3}$-Agent based on multiple state-of-the-art language models demonstrate that DR$^{3}$-Eval is highly challenging and reveals critical failure modes in retrieval robustness and hallucination control. Our code and data are publicly available.

</details>


### 46. AIPC: Agent-Based Automation for AI Model Deployment with Qualcomm AI Runtime

- **Authors:** Jianhao Su, Zhanwei Wu, ShengTing Huang, Weidong Feng
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14661v1](http://arxiv.org/abs/2604.14661v1)
- **PDF:** [https://arxiv.org/pdf/2604.14661v1](https://arxiv.org/pdf/2604.14661v1)
- **Categories:** cs.SE, cs.AI, cs.LG


> The paper introduces **AIPC (AI Porting Conversion)**, an agent‑driven framework that automates the end‑to‑end deployment of deep‑learning models onto the Qualcomm AI Runtime (QAIRT). By breaking the deployment pipeline into verifiable stages and encoding domain knowledge as “Agent Skills” plus helper scripts, the system can autonomously handle model conversion, operator compatibility, quantization calibration, runtime integration, and accuracy validation, while providing staged validation and pinpointed failure‐repair feedback. Experiments on vision, multimodal, and speech models show that AIPC can go from a PyTorch checkpoint to a runnable QNN/SNPE binary in 7–20 minutes with modest API costs (≈ $0.7–10), dramatically lowering the expertise barrier for edge AI deployment; more complex models still need manual intervention, but the approach already offers useful execution, diagnostics, and bounded repair capabilities.


<details>
<summary>Abstract</summary>

Edge AI model deployment is a multi-stage engineering process involving model conversion, operator compatibility handling, quantization calibration, runtime integration, and accuracy validation. In
  practice, this workflow is long, failure-prone, and heavily dependent on deployment expertise, particularly when targeting hardware-specific inference runtimes. This technical report presents AIPC (AI
  Porting Conversion), an AI agent-driven approach for constrained automation of AI model deployment. AIPC decomposes deployment into standardized, verifiable stages and injects deployment-domain knowledge
  into agent execution through Agent Skills, helper scripts, and a stage-wise validation loop. This design reduces both the expertise barrier and the engineering time required for hardware deployment.
  Using Qualcomm AI Runtime (QAIRT) as the primary scenario, this report examines automated deployment across representative vision, multimodal, and speech models. In the cases covered here, AIPC can
  complete deployment from PyTorch to runnable QNN/SNPE inference within 7-20 minutes for structurally regular vision models, with indicative API costs roughly in the range of USD 0.7-10. For more complex
  models involving less-supported operators, dynamic shapes, or autoregressive decoding structures, fully automated deployment may still require further advances, but AIPC already provides practical support
  for execution, failure localization, and bounded repair.

</details>


### 47. Exploring LLM-based Verilog Code Generation with Data-Efficient Fine-Tuning and Testbench Automation

- **Authors:** Mu-Chi Chen, Po-Hsuan Huang, Yu-Hung Kao, Yen-Fu Liu, Yu-Kai Hung, Cheng Liang, Shao-Chun Ho, Chia-Heng Tu, Shih-Hao Hung
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15388v1](http://arxiv.org/abs/2604.15388v1)
- **PDF:** [https://arxiv.org/pdf/2604.15388v1](https://arxiv.org/pdf/2604.15388v1)
- **Categories:** cs.AR, cs.AI


> The paper introduces a multi‑agent workflow that automatically synthesizes Verilog testbenches to create high‑quality, data‑efficient fine‑tuning sets for LLMs tasked with converting hardware specifications into Verilog code. By training a modest‑size language model on this automatically generated data, the authors achieve VerilogEval v2 scores on par with state‑of‑the‑art, large‑scale approaches while using far fewer labeled examples. This demonstrates that agent‑driven testbench automation can substantially reduce the data bottleneck for LLM‑based hardware description language generation, opening a path toward more practical, self‑verifying agentic AI design tools.


<details>
<summary>Abstract</summary>

Recent advances in large language models have improved code generation, but their use in hardware description languages is still limited. Moreover, training data and testbenches for these models are often scarce. This paper presents a workflow that uses multi-agent models to generate testbenches for high-quality fine-tuning data. By automating testbench creation, the fine-tuned model for the specification-to-Verilog task achieves performance comparable to state-of-the-art methods on the refined VerilogEval v2 benchmark while using less training data. This study provides a basis for future work on LLM-based HDL generation and automated verification.

</details>


### 48. CoDaS: AI Co-Data-Scientist for Biomarker Discovery via Wearable Sensors

- **Authors:** Yubin Kim, Salman Rahman, Samuel Schmidgall, Chunjong Park, A. Ali Heydari, Ahmed A. Metwally, Hong Yu, Xin Liu, Xuhai Xu, Yuzhe Yang, Maxwell A. Xu, Zhihan Zhang, Cynthia Breazeal, Tim Althoff, Petar Sirkovic, Ivor Rendulic, Annalisa Pawlosky, Nicolas Stroppa, Juraj Gottweis, Elahe Vedadi, Alan Karthikesalingam, Pushmeet Kohli, Vivek Natarajan, Mark Malhotra, Shwetak Patel, Hae Won Park, Hamid Palangi, Daniel McDuff
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14615v1](http://arxiv.org/abs/2604.14615v1)
- **PDF:** [https://arxiv.org/pdf/2604.14615v1](https://arxiv.org/pdf/2604.14615v1)
- **Categories:** cs.AI


> CoDaS is a multi‑agent, human‑in‑the‑loop system that formalizes digital‑health biomarker discovery as an iterative loop of hypothesis generation, statistical testing, adversarial validation, and literature‑grounded reasoning applied to massive wearable‑sensor datasets. Using three cohorts (9,279 observations), the agents autonomously generated and internally validated 41 mental‑health and 25 metabolic candidate biomarkers—e.g., sleep‑timing variability linked to depression and a steps‑to‑resting‑heart‑rate fitness index linked to insulin resistance—while reproducing known clinical associations (AST/ALT). Incorporating these AI‑derived features into prediction models yielded consistent, statistically significant gains (ΔR² ≈ 0.04 for depression, 0.02 for insulin resistance), demonstrating that CoDaS can systematically and transparently prioritize actionable biomarkers from continuous wearable data.


<details>
<summary>Abstract</summary>

Scientific discovery in digital health requires converting continuous physiological signals from wearable devices into clinically actionable biomarkers. We introduce CoDaS (AI Co-Data-Scientist), a multi-agent system that structures biomarker discovery as an iterative process combining hypothesis generation, statistical analysis, adversarial validation, and literature-grounded reasoning with human oversight using large-scale wearable datasets. Across three cohorts totaling 9,279 participant-observations, CoDaS identified 41 candidate digital biomarkers for mental health and 25 for metabolic outcomes, each subjected to an internal validation battery spanning replication, stability, robustness, and discriminative power. Across two independent depression cohorts, CoDaS surfaced circadian instability-related features in both datasets, reflected in sleep duration variability (DWB, ρ= 0.252, p < 0.001) and sleep onset variability (GLOBEM, ρ= 0.126, p < 0.001). In a metabolic cohort, CoDaS derived a cardiovascular fitness index (steps/resting heart rate; ρ= -0.374, p < 0.001), and recovered established clinical associations, including the hepatic function ratio (AST/ALT; ρ= -0.375, p < 0.001), a known correlate of insulin resistance. Incorporating CoDaS-derived features alongside demographic variables led to modest but consistent improvements in predictive performance, with cross-validated ΔR^2 increases of 0.040 for depression and 0.021 for insulin resistance. These findings suggest that CoDaS enables systematic and traceable hypothesis generation and prioritization for biomarker discovery from large-scale wearable data.

</details>


### 49. El Agente Forjador: Task-Driven Agent Generation for Quantum Simulation

- **Authors:** Zijian Zhang, Aiwei Yin, Amaan Baweja, Jiaru Bai, Ignacio Gustin, Varinia Bernales, Alán Aspuru-Guzik
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14609v1](http://arxiv.org/abs/2604.14609v1)
- **PDF:** [https://arxiv.org/pdf/2604.14609v1](https://arxiv.org/pdf/2604.14609v1)
- **Categories:** cs.AI, physics.comp-ph


> The paper introduces **El Agente Forjador**, a multi‑agent framework in which LLM‑based coding agents automatically create, validate, and reuse domain‑specific computational tools through a four‑stage pipeline (analysis → generation → execution → evaluation). By testing 24 quantum‑chemistry and quantum‑dynamics problems across several agent configurations, the authors show that (i) on‑the‑fly tool generation yields higher solution accuracy than a baseline that solves problems directly, and (ii) reusing a curriculum‑built toolset generated by a stronger agent both cuts API cost and boosts the performance of weaker agents, even enabling hybrid cross‑domain tasks. These results demonstrate that agentic AI can self‑assemble reusable scientific software, shifting the definition of agent capability from static hand‑crafted toolsets to task‑driven, autonomously forged resources.


<details>
<summary>Abstract</summary>

AI for science promises to accelerate the discovery process. The advent of large language models (LLMs) and agentic workflows enables the expediting of a growing range of scientific tasks. However, most of the current generation of agentic systems depend on static, hand-curated toolsets that hinder adaptation to new domains and evolving libraries. We present El Agente Forjador, a multi-agent framework in which universal coding agents autonomously forge, validate, and reuse computational tools through a four-stage workflow of tool analysis, tool generation, task execution, and iterative solution evaluation. Evaluated across 24 tasks spanning quantum chemistry and quantum dynamics on five coding agent setups, we compare three operating modes: zero-shot generation of tools per task, reuse of a curriculum-built toolset, and direct problem-solving with the coding agents as the baseline. We find that our tool generation and reuse framework consistently improves accuracy over the baseline. We also show that reusing a toolset built by a stronger coding agent can reduce API cost and substantially raises the solution quality for weaker coding agents. Case studies further demonstrate that tools forged for different domains can be combined to solve hybrid tasks. Taken together, these results show that LLM-based agents can use their scientific knowledge and coding capabilities to autonomously build reusable scientific tools, pointing toward a paradigm in which agent capabilities are defined by the tasks they are designed to solve rather than by explicitly engineered implementations.

</details>


### 50. GDPR Auto-Formalization with AI Agents and Human Verification

- **Authors:** Ha Thanh Nguyen, Wachara Fungwacharakorn, Sabine Wehnert, May Myo Zin, Yuntao Kong, Jieying Xue, Michał Araszkiewicz, Randy Goebel, Ken Satoh
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14607v1](http://arxiv.org/abs/2604.14607v1)
- **PDF:** [https://arxiv.org/pdf/2604.14607v1](https://arxiv.org/pdf/2604.14607v1)
- **Categories:** cs.AI


> The paper’s main contribution is a hybrid workflow that combines role‑specialized large‑language‑model (LLM) agents with human‑in‑the‑loop verification to automatically translate GDPR text into formal logical representations. The authors design a multi‑agent pipeline in which separate LLM components iteratively generate legal scenarios, formal rules, and atomic facts, while independent verification modules—both automated checks and expert human reviewers—evaluate representational fidelity, logical consistency, and legal correctness. Experiments show that this structured, human‑augmented approach yields a high‑quality GDPR formalization dataset and dramatically reduces error rates compared with fully autonomous LLM generation, highlighting the necessity of targeted human oversight for reliable, context‑sensitive legal reasoning in agentic AI systems.


<details>
<summary>Abstract</summary>

We study the overall process of automatic formalization of GDPR provisions using large language models, within a human-in-the-loop verification framework. Rather than aiming for full autonomy, we adopt a role-specialized workflow in which LLM-based AI components, operating in a multi-agent setting with iterative feedback, generate legal scenarios, formal rules, and atomic facts. This is coupled with independent verification modules which include human reviewers' assessment of representational, logical, and legal correctness. Using this approach, we construct a high-quality dataset to be used for GDPR auto-formalization, and analyze both successful and problematic cases. Our results show that structured verification and targeted human oversight are essential for reliable legal formalization, especially in the presence of legal nuance and context-sensitive reasoning.

</details>


### 51. Mechanistic Decoding of Cognitive Constructs in LLMs

- **Authors:** Yitong Shou, Manhao Guan
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14593v1](http://arxiv.org/abs/2604.14593v1)
- **PDF:** [https://arxiv.org/pdf/2604.14593v1](https://arxiv.org/pdf/2604.14593v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces a **Cognitive Reverse‑Engineering (RepE) framework** that isolates and quantifies the latent factors underlying a complex affective state—social‑comparison jealousy—inside large language models. By applying appraisal‑theory‑informed subspace orthogonalization, regression‑based weighting, and bidirectional causal steering to the internal activations of eight Llama/Qwen/Gemma models, the authors show that jealousy is represented as a linear combination of two interpretable dimensions—Superiority of the comparison person and Domain Self‑Definitional Relevance—and that manipulating these subspaces can modulate the model’s emotional judgments. This work demonstrates that sophisticated emotional constructs can be mechanically decoded, monitored, and even suppressed in LLMs, offering a concrete pathway for representational‑level safety interventions in agentic AI systems.


<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) demonstrate increasingly sophisticated affective capabilities, the internal mechanisms by which they process complex emotions remain unclear. Existing interpretability approaches often treat models as black boxes or focus on coarse-grained basic emotions, leaving the cognitive structure of more complex affective states underexplored. To bridge this gap, we propose a Cognitive Reverse-Engineering framework based on Representation Engineering (RepE) to analyze social-comparison jealousy. By combining appraisal theory with subspace orthogonalization, regression-based weighting, and bidirectional causal steering, we isolate and quantify two psychological antecedents of jealousy, Superiority of Comparison Person and Domain Self-Definitional Relevance, and examine their causal effects on model judgments. Experiments on eight LLMs from the Llama, Qwen, and Gemma families suggest that models natively encode jealousy as a structured linear combination of these constituent factors. Their internal representations are broadly consistent with the human psychological construct, treating Superiority as the foundational trigger and Relevance as the ultimate intensity multiplier. Our framework also demonstrates that toxic emotional states can be mechanically detected and surgically suppressed, suggesting a possible route toward representational monitoring and intervention for AI safety in multi-agent environments.

</details>


### 52. AgileLog: A Forkable Shared Log for Agents on Data Streams

- **Authors:** Shreesha G. Bhat, Tony Hong, Michael Noguera, Ramnatthan Alagappan, Aishwarya Ganesan
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14590v1](http://arxiv.org/abs/2604.14590v1)
- **PDF:** [https://arxiv.org/pdf/2604.14590v1](https://arxiv.org/pdf/2604.14590v1)
- **Categories:** cs.DC, cs.AI


> **Main contribution:** The paper introduces **AgileLog**, a forkable shared‑log abstraction that extends the classic streaming log with primitives for creating lightweight, isolated “forks” of the log, enabling AI agents to read and write to streaming data without interfering with each other or with traditional programs.

**Methodology:** The authors define the AgileLog API, then build **Bolt**, an engine that implements the API using a combination of versioned append‑only storage, copy‑on‑write metadata, and logical timestamps to make fork creation cheap and to guarantee both logical (causal) and performance isolation between the main log and each agent’s fork.

**Key findings:** Experiments with real‑world streaming workloads and LLM‑driven agents show that AgileLog can spawn thousands of concurrent forks with sub‑millisecond overhead, eliminating write‑conflict contention and preserving throughput for non‑agent workloads, thereby providing a practical substrate for safe, high‑performance agentic AI in streaming systems.


<details>
<summary>Abstract</summary>

In modern data-streaming systems, alongside traditional programs, a new type of entity has emerged that can interact with streaming data: AI agents. Unlike traditional programs, AI agents use LLM reasoning to accomplish high-level tasks specified in natural language over streaming data. Unfortunately, current streaming systems cannot fully support agents: they lack the fundamental mechanisms to avoid the performance interference caused by agentic tasks and to safely handle agentic writes. We argue that the shared log, the core abstraction underlying streaming data, must support creating forks of itself, and that such a forkable shared log serves as a great substrate for agents acting on streaming data. We propose AgileLog, a new shared log abstraction that provides novel forking primitives for agentic use cases. We design Bolt, an implementation of the AgileLog abstraction, that uses novel techniques to make forks cheap, and provide logical and performance isolation.

</details>


### 53. From Risk to Rescue: An Agentic Survival Analysis Framework for Liquidation Prevention

- **Authors:** Fernando Spadea, Oshani Seneviratne
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14583v1](http://arxiv.org/abs/2604.14583v1)
- **PDF:** [https://arxiv.org/pdf/2604.14583v1](https://arxiv.org/pdf/2604.14583v1)
- **Categories:** cs.LG


> **Main contribution**: The paper introduces an autonomous, protocol‑compliant agent that converts survival‑analysis risk forecasts into real‑time interventions that actively prevent liquidations in DeFi lending protocols such as Aave v3.  

**Methodology**: It builds a numerically stable XGBoost‑based Cox proportional‑hazards model to compute a “return‑period” risk metric, augments it with a volatility‑adjusted trend score, and then runs a counterfactual optimization loop that simulates alternative user actions to identify the minimal capital injection needed to avert a liquidation, all within a high‑fidelity Aave v3 simulator.  

**Key findings**: Tested on 4,882 high‑risk borrower profiles, the agent consistently halted imminent liquidations that static health‑factor thresholds missed, achieved zero instances of worsening user positions, and efficiently distinguished true insolvency risk from trivial “dust” events, demonstrating a viable safety layer for autonomous financial agents.


<details>
<summary>Abstract</summary>

Decentralized Finance (DeFi) lending protocols like Aave v3 rely on over-collateralization to secure loans, yet users frequently face liquidation due to volatile market conditions. Existing risk management tools utilize static health-factor thresholds, which are reactive and fail to distinguish between administrative "dust" cleanup and genuine insolvency. In this work, we propose an autonomous agent that leverages time-to-event (survival) analysis and moves beyond prediction to execution. Unlike passive risk signals, this agent perceives risk, simulates counterfactual futures, and executes protocol-faithful interventions to proactively prevent liquidations. We introduce a return period metric derived from a numerically stable XGBoost Cox proportional hazards model to normalize risk across transaction types, coupled with a volatility-adjusted trend score to filter transient market noise. To select optimal interventions, we implement a counterfactual optimization loop that simulates potential user actions to find the minimum capital required to mitigate risk. We validate our approach using a high-fidelity, protocol-faithful Aave v3 simulator on a cohort of 4,882 high-risk user profiles. The results demonstrate the agent's ability to prevent liquidations in imminent-risk scenarios where static rules fail, effectively "saving the unsavable" while maintaining a zero worsening rate, providing a critical safety guarantee often missing in autonomous financial agents. Furthermore, the system successfully differentiates between actionable financial risks and negligible dust events, optimizing capital efficiency where static rules fail.

</details>


### 54. Don't Retrieve, Navigate: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG

- **Authors:** Yiqun Sun, Pengfei Wei, Lawrence B. Hsieh
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14572v1](http://arxiv.org/abs/2604.14572v1)
- **PDF:** [https://arxiv.org/pdf/2604.14572v1](https://arxiv.org/pdf/2604.14572v1)
- **Categories:** cs.IR, cs.AI, cs.CL, cs.MA


> The paper introduces **Corpus2Skill**, a novel framework that converts an enterprise document collection into a hierarchical “skill directory” that LLM agents can actively navigate instead of merely consuming a static set of retrieved passages. The offline compilation pipeline repeatedly clusters documents, uses LLMs to generate concise summaries for each cluster, and assembles these into a tree‑structured set of skill files; at query time, the agent receives the top‑level summary, iteratively drills down through increasingly specific summaries, and only fetches full documents when needed, enabling it to reason about unexplored branches, backtrack, and synthesize evidence from multiple parts of the corpus. Experiments on the WixQA customer‑support benchmark show that this navigation‑based approach consistently beats dense retrieval, RAPTOR, and existing agentic RAG baselines across all evaluated quality metrics, demonstrating the advantage of making corpus organization explicit for agentic QA and retrieval‑augmented generation.


<details>
<summary>Abstract</summary>

Retrieval-Augmented Generation (RAG) grounds LLM responses in external evidence but treats the model as a passive consumer of search results: it never sees how the corpus is organized or what it has not yet retrieved, limiting its ability to backtrack or combine scattered evidence. We present Corpus2Skill, which distills a document corpus into a hierarchical skill directory offline and lets an LLM agent navigate it at serve time. The compilation pipeline iteratively clusters documents, generates LLM-written summaries at each level, and materializes the result as a tree of navigable skill files. At serve time, the agent receives a bird's-eye view of the corpus, drills into topic branches via progressively finer summaries, and retrieves full documents by ID. Because the hierarchy is explicitly visible, the agent can reason about where to look, backtrack from unproductive paths, and combine evidence across branches. On WixQA, an enterprise customer-support benchmark for RAG, Corpus2Skill outperforms dense retrieval, RAPTOR, and agentic RAG baselines across all quality metrics.

</details>


### 55. LinuxArena: A Control Setting for AI Agents in Live Production Software Environments

- **Authors:** Tyler Tracy, Ram Potham, Nick Kuhn, Myles Heller, Anshul Khandelwal, Cody Rushing, Henri Lemoine, Miguel Brandao, Tomas Turlik, Adam Hanson, Josh Hills, Amy Ngo, Ram Rachum, Nik Mitchell, Falko Galperin, Oscar Sykes, Pip Arnott, Samuel Prieto Lima, Carlos Giudice, Matt Goldwater, Daniel Popp, Drew de Wet, Ruben Castaing, Qi Guo, Douw Marx, Benjamin Shaffrey, Justin Shenk, Martin Milbradt, Hannah Meagher, Shaheen Ahmed-Chowdhury, Daniel O'Connell, Chris Canal, Buck Shlegeris, Aryan Bhatt
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15384v1](http://arxiv.org/abs/2604.15384v1)
- **PDF:** [https://arxiv.org/pdf/2604.15384v1](https://arxiv.org/pdf/2604.15384v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> LinuxArena is a new benchmark suite in which autonomous agents execute real‑world software‑engineering tasks inside live, multi‑service production Linux systems. The authors construct 20 distinct environments containing 1,671 legitimate “main” tasks and 184 “side” sabotage tasks (e.g., data exfiltration, back‑dooring), and evaluate both attack agents and defensive monitor models on this playground. Their experiments show that even a strong language‑model agent (Claude Opus 4.6) can evade a trusted GPT‑5‑nano monitor in about 23 % of sabotage attempts at a 1 % false‑positive rate, and that human‑written attack trajectories (LaStraj) succeed even more often, demonstrating substantial room for improvement in both attacker policies and defender monitors.


<details>
<summary>Abstract</summary>

We introduce LinuxArena, a control setting in which agents operate directly on live, multi-service production environments. LinuxArena contains 20 environments, 1,671 main tasks representing legitimate software engineering work, and 184 side tasks representing safety failures such as data exfiltration and backdooring, making it the largest and most diverse control setting for software engineering to date. We validate LinuxArena is useful for control research by running sabotage evaluations, which measure whether attackers can complete side tasks while working on main tasks, and monitor evaluations, which measure a monitor model's ability to detect sabotage attempts. Against a GPT-5-nano trusted monitor at a 1\% step-wise false positive rate, Claude Opus 4.6 achieves roughly a 23% undetected sabotage success rate. We additionally release LaStraj, a dataset of human-crafted attack trajectories that evade monitors at substantially higher rates than any model-generated attacks we elicited, showing that current attack policies do not saturate LinuxArena. These results suggest that LinuxArena has meaningful headroom for both attackers and defenders, making it a strong testbed for developing and evaluating future control protocols.

</details>


### 56. MARS$^2$: Scaling Multi-Agent Tree Search via Reinforcement Learning for Code Generation

- **Authors:** Pengfei Li, Shijie Wang, Fangyuan Li, Yikun Fu, Kaifeng Liu, Kaiyan Zhang, Dazhi Zhang, Yuqiang Li, Biqing Qi, Bowen Zhou
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14564v1](http://arxiv.org/abs/2604.14564v1)
- **PDF:** [https://arxiv.org/pdf/2604.14564v1](https://arxiv.org/pdf/2604.14564v1)
- **Categories:** cs.AI, cs.CL


> **Contribution:** The paper introduces **MARS²** (Multi‑Agent Reinforced Tree‑Search Scaling), a unified reinforcement‑learning framework that embeds several independently optimized agents into a shared, learnable tree‑search environment, allowing heterogeneous policies to cooperatively explore and refine code‑generation candidates.  

**Methodology:** MARS² treats the search tree as a multi‑agent interaction space and equips it with a novel *path‑level group advantage* estimator derived from tree‑consistent reward shaping, which provides coherent credit assignment across the collective trajectories of all agents.  

**Key Findings:** Across multiple code‑generation benchmarks, MARS² consistently outperforms single‑agent RL and prior decoupled multi‑policy approaches, demonstrating that coordinated multi‑agent collaboration within a structured tree search markedly boosts exploration diversity and final generation quality.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) paradigms have demonstrated strong performance on reasoning-intensive tasks such as code generation. However, limited trajectory diversity often leads to diminishing returns, which constrains the achievable performance ceiling. Search-enhanced RL alleviates this issue by introducing structured exploration, which remains constrained by the single-agent policy priors. Meanwhile, leveraging multiple interacting policies can acquire more diverse exploratory signals, but existing approaches are typically decoupled from structured search. We propose \textbf{MARS$^2$} (Multi-Agent Reinforced Tree-Search Scaling), a unified RL framework in which multiple independently-optimized agents collaborate within a shared tree-structured search environment. MARS$^2$ models the search tree as a learnable multi-agent interaction environment, enabling heterogeneous agents to collaboratively generate and refine candidate solutions within a shared search topology. To support effective learning, we introduce a path-level group advantage formulation based on tree-consistent reward shaping, which facilitates effective credit assignment across complex search trajectories. Experiments on code generation benchmarks show that MARS$^2$ consistently improves performance across diverse model combinations and training settings, demonstrating the effectiveness of coupling multi-agent collaboration with tree search for enhancing reinforcement learning. Our code is publicly available at https://github.com/TsinghuaC3I/MARTI.

</details>


### 57. VeriGraphi: A Multi-Agent Framework of Hierarchical RTL Generation for Large Hardware Designs

- **Authors:** Sazzadul Islam, Tasnim Tabassum, Hao Zheng
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14550v1](http://arxiv.org/abs/2604.14550v1)
- **PDF:** [https://arxiv.org/pdf/2604.14550v1](https://arxiv.org/pdf/2604.14550v1)
- **Categories:** cs.AR, cs.AI, cs.LG, cs.MA, cs.PL


> VeriGraphi introduces a knowledge‑graph‑driven pipeline that lets large language models generate hierarchical, synthesizable Verilog for complex hardware designs. The system first builds a spec‑anchored hierarchical design graph (HDA) through coordinated multi‑agent analysis of the textual, tabular, and graphical parts of a specification, encoding modules, ports, wiring, and dependencies as explicit graph entities; a downstream coding agent then uses this deterministic scaffold to produce pseudo‑code and RTL while continuously checking interface and dependency consistency. Experiments on three NIST benchmarks and a full RV32I processor show that VeriGraphi dramatically reduces hallucinations and context loss, delivering functionally correct hierarchical RTL with minimal human effort—demonstrating a viable path for agentic AI to automate large‑scale hardware design.


<details>
<summary>Abstract</summary>

Generating synthesizable Verilog for large, hierarchical hardware designs remains a significant challenge for large language models (LLMs), which struggle to replicate the structured reasoning that human experts employ when translating complex specifications into RTL. When tasked with producing hierarchical Verilog, LLMs frequently lose context across modules, hallucinate interfaces, fabricate inter-module wiring, and fail to maintain structural coherence - failures that intensify as design complexity grows and specifications involve informal prose, figures, and tables that resist direct operationalization. To address these challenges, we present VeriGraphi, a framework that introduces a spec-anchored Knowledge Graph as the architectural substrate driving the RTL generation pipeline. VeriGraphi constructs a HDA, a structured knowledge graph that explicitly encodes module hierarchy, port-level interfaces, wiring semantics, and inter-module dependencies as first-class graph entities and relations. Built through iterative multi-agent analysis of the specification, this Knowledge Graph provides a deterministic, machine-checkable structural scaffold before code generation. Guided by the KG, a progressive coding module incrementally generates pseudo-code and synthesizable RTL while enforcing interface consistency and dependency correctness at each submodule stage. We evaluate VeriGraphi on a benchmark of three representative specification documents from the National Institute of Standards and Technology and their corresponding implementations, and we present a RV32I processor as a detailed case study to illustrate the full pipeline. The results demonstrate that VeriGraphi enables reliable hierarchical RTL generation with minimal human intervention for RISC-V, marking a significant milestone for LLM-generated hardware design while maintaining strong functional correctness.

</details>


### 58. Mind DeepResearch Technical Report

- **Authors:** MindDR Team, Li Auto Inc
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14518v2](http://arxiv.org/abs/2604.14518v2)
- **PDF:** [https://arxiv.org/pdf/2604.14518v2](https://arxiv.org/pdf/2604.14518v2)
- **Categories:** cs.AI


> The paper introduces **Mind DeepResearch (MindDR)**, a multi‑agent deep‑research system that attains state‑of‑the‑art results with modest ~30 B‑parameter models by coupling a **three‑agent architecture** (Planning, DeepSearch, and Report agents) with a **four‑stage, agent‑specialized training pipeline** (cold‑start SFT → Search‑RL → Report‑RL → preference alignment). Using this pipeline the authors train each agent to specialize in planning queries, performing deep search, and composing reports, respectively, and evaluate the integrated system on a suite of Chinese‑language browse‑and‑search benchmarks as well as a newly created “MindDR Bench” of 500 real‑world queries. The results show that MindDR **outperforms peer open‑source agents of similar size and matches or exceeds much larger proprietary models**, achieving 45.7 %–75.0 % on established benchmarks and a top‑score of 51.8 on the authors’ multi‑dimensional benchmark, demonstrating that efficient, staged multi‑agent training can close the performance gap for agentic AI without scaling to hundreds of billions of parameters.


<details>
<summary>Abstract</summary>

We present Mind DeepResearch (MindDR), an efficient multi-agent deep research framework that achieves leading performance with only ~30B-parameter models through a meticulously designed data synthesis and multi-stage training pipeline. The core innovation of MindDR lies in a collaborative three-agent architecture (Planning Agent, DeepSearch Agent, and Report Agent) and a four-stage agent-specialized training pipeline comprising SFT cold-start, Search-RL, Report-RL and preference alignment. With this regime, MindDR demonstrates competitive performance even with ~30B-scale models. Specifically, MindDR achieves 45.7% on BrowseComp-ZH, 42.8% on BrowseComp, 46.5% on WideSearch, 75.0% on xbench-DS, and 52.5 on DeepResearch Bench, outperforming comparable-scale open-source agent systems and rivaling larger-scale models. MindDR has been deployed as an online product in Li Auto. Furthermore, we introduce MindDR Bench, a curated benchmark of 500 real-world Chinese queries from our internal product user interactions, evaluated through a comprehensive multi-dimensional rubric system rather than relying on a single RACE metric. On MindDR Bench, MindDR achieves a state-of-the-art score of 51.8.

</details>


### 59. CBCL: Safe Self-Extending Agent Communication

- **Authors:** Hugo O'Connor
- **Published:** 2026-04-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14512v1](http://arxiv.org/abs/2604.14512v1)
- **PDF:** [https://arxiv.org/pdf/2604.14512v1](https://arxiv.org/pdf/2604.14512v1)
- **Categories:** cs.CR, cs.AI, cs.FL, cs.LO


> The paper introduces **CBCL (Common Business Communication Language)**, a novel agent communication language that guarantees safe, self‑extending interactions by restricting every message—including dynamically defined “dialects”—to the deterministic context‑free language (DCFL) class. The authors formalize CBCL’s syntax and three safety invariants (preventing unbounded growth, enforcing declared resource limits, and preserving a core vocabulary) in Lean 4, then implement a verified parser and dialect engine in Rust, verified by property‑based and differential testing. Experiments show that agents can transmit and adopt domain‑specific extensions as first‑class messages while provably staying within tractable validation bounds, offering a practical foundation for safe, extensible communication among autonomous, self‑modifying AI agents.


<details>
<summary>Abstract</summary>

Agent communication languages (ACLs) enable heterogeneous agents to share knowledge and coordinate across diverse domains. This diversity demands extensibility, but expressive extension mechanisms can push the input language beyond the complexity classes where full validation is tractable. We present CBCL (Common Business Communication Language), an agent communication language that constrains all messages, including runtime language extensions, to the deterministic context-free language (DCFL) class. CBCL allows agents to define, transmit, and adopt domain-specific "dialect" extensions as first-class messages; three safety invariants (R1--R3), machine-checked in Lean 4 and enforced in a Rust reference implementation, prevent unbounded expansion, applying declared resource limits, and preserving core vocabulary. We formalize the language and its safety properties in Lean 4, implement a reference parser and dialect engine in Rust with property-based and differential tests, and extract a verified parser binary. Our results demonstrate that homoiconic protocol design, where extension definitions share the same representation as ordinary messages, can be made provably safe. As autonomous agents increasingly extend their own communication capabilities, formally bounding what they can express to each other is a precondition for oversight.

</details>


### 60. Evo-MedAgent: Beyond One-Shot Diagnosis with Agents That Remember, Reflect, and Improve

- **Authors:** Weixiang Shen, Bailiang Jian, Jun Li, Che Liu, Johannes Moll, Xiaobin Hu, Daniel Rueckert, Hongwei Bran Li, Jiazhen Pan
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14475v1](http://arxiv.org/abs/2604.14475v1)
- **PDF:** [https://arxiv.org/pdf/2604.14475v1](https://arxiv.org/pdf/2604.14475v1)
- **Categories:** cs.AI


> Evo‑MedAgent augments a frozen, tool‑augmented LLM medical diagnostician with a lightweight, self‑evolving memory that lets it learn from previously seen cases at inference time. The system stores (i) retrospective clinical episodes for case‑based retrieval, (ii) adaptive procedural heuristics that are updated through a single reflection step, and (iii) a tool‑reliability controller that re‑weights specialist modules, enabling inter‑case learning without any gradient‑based training. On the ChestAgentBench benchmark this memory‑driven approach lifts MCQ accuracy from 0.68 → 0.79 for GPT‑5‑mini and 0.76 → 0.87 for Gemini‑3 Flash, demonstrating that cheap test‑time evolution can substantially improve agentic medical diagnosis.


<details>
<summary>Abstract</summary>

Tool-augmented large language model (LLM) agents can orchestrate specialist classifiers, segmentation models, and visual question-answering modules to interpret chest X-rays. However, these agents still solve each case in isolation: they fail to accumulate experience across cases, correct recurrent reasoning mistakes, or adapt their tool-use behavior without expensive reinforcement learning. While a radiologist naturally improves with every case, current agents remain static. In this work, we propose Evo-MedAgent, a self-evolving memory module that equips a medical agent with the capacity for inter-case learning at test time. Our memory comprises three complementary stores: (1)~\emph{Retrospective Clinical Episodes} that retrieve problem-solving experiences from similar past cases, (2)~an \emph{Adaptive Procedural Heuristics} bank curating priority-tagged diagnostic rules that evolves via reflection, much like a physician refining their internal criteria, and (3)~a \emph{Tool Reliability Controller} that tracks per-tool trustworthiness. On ChestAgentBench, Evo-MedAgent raises multiple-choice question (MCQ) accuracy from 0.68 to 0.79 on GPT-5-mini, and from 0.76 to 0.87 on Gemini-3 Flash. With a strong base model, evolving memory improves performance more effectively than orchestrating external tools on qualitative diagnostic tasks. Because Evo-MedAgent requires no training, its per-case overhead is bounded by one additional retrieval pass and a single reflection call, making it deployable on top of any frozen model.

</details>


### 61. AIBuildAI: An AI Agent for Automatically Building AI Models

- **Authors:** Ruiyi Zhang, Peijia Qin, Qi Cao, Li Zhang, Pengtao Xie
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14455v1](http://arxiv.org/abs/2604.14455v1)
- **PDF:** [https://arxiv.org/pdf/2604.14455v1](https://arxiv.org/pdf/2604.14455v1)
- **Categories:** cs.AI


> The paper introduces **AIBuildAI**, a hierarchical LLM‑driven agent that automates the entire AI model development pipeline—from interpreting a task description and data to delivering a deployable model—by coordinating three specialist sub‑agents (designer, coder, and tuner). The system is implemented as a manager LLM that issues prompts and orchestrates tool‑use for each sub‑agent, enabling multi‑step reasoning, code generation, debugging, and hyper‑parameter tuning without human intervention. On the MLE‑Bench benchmark of Kaggle‑style tasks across vision, language, time‑series, and tabular domains, AIBuildAI achieves a 63.1 % “medal” rate, ranking first and matching the performance of experienced AI engineers, thereby demonstrating that hierarchical agent architectures can extend AutoML far beyond narrow hyper‑parameter search to full‑stack model creation.


<details>
<summary>Abstract</summary>

AI models underpin modern intelligent systems, driving advances across science, medicine, finance, and technology. Yet developing high-performing AI models remains a labor-intensive process that requires expert practitioners to iteratively design architectures, engineer representations, implement training pipelines and refine approaches through empirical evaluation. Existing AutoML methods partially alleviate this burden but remain limited to narrow aspects such as hyperparameter optimization and model selection within predefined search spaces, leaving the full development lifecycle largely dependent on human expertise. To address this gap, we introduce AIBuildAI, an AI agent that automatically builds AI models from a task description and training data. AIBuildAI adopts a hierarchical agent architecture in which a manager agent coordinates three specialized sub-agents: a designer for modeling strategy, a coder for implementation and debugging, and a tuner for training and performance optimization. Each sub-agent is itself a large language model (LLM) based agent capable of multi-step reasoning and tool use, enabling end-to-end automation of the AI model development process that goes beyond the scope of existing AutoML approaches. We evaluate AIBuildAI on MLE-Bench, a benchmark of realistic Kaggle-style AI development tasks spanning visual, textual, time-series and tabular modalities. AIBuildAI ranks first on MLE-Bench with a medal rate of 63.1%, outperforming all existing baseline methods and matching the capability of highly experienced AI engineers. These results demonstrate that hierarchical agent systems can automate the full AI model development process from task specification to deployable model, suggesting a pathway toward broadly accessible AI development with minimal human intervention.

</details>


### 62. Credo: Declarative Control of LLM Pipelines via Beliefs and Policies

- **Authors:** Duo Lu, Andrew Crotty, Uğur Çetintemel
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14401v1](http://arxiv.org/abs/2604.14401v1)
- **PDF:** [https://arxiv.org/pdf/2604.14401v1](https://arxiv.org/pdf/2604.14401v1)
- **Categories:** cs.AI, cs.DB


> Credo introduces a novel architecture for agentic LLM systems in which the entire semantic state is stored as **beliefs** in a database and the agent’s actions are governed by **declarative policies** that query and update these beliefs. By separating “what to do” (policy) from “how to do it” (pipeline code), Credo enables adaptive, auditable control loops—e.g., dynamic model selection, retrieval, and corrective re‑execution—without modifying the underlying procedural code. Experiments on a decision‑control benchmark show that the belief‑policy layer automatically adapts to new evidence, improves correctness, and yields transparent, verifiable behavior compared to traditional imperative, prompt‑based agents.


<details>
<summary>Abstract</summary>

Agentic AI systems are becoming commonplace in domains that require long-lived, stateful decision-making in continuously evolving conditions. As such, correctness depends not only on the output of individual model calls, but also on how to best adapt when incorporating new evidence or revising prior conclusions. However, existing frameworks rely on imperative control loops, ephemeral memory, and prompt-embedded logic, making agent behavior opaque, brittle, and difficult to verify. This paper introduces Credo, which represents semantic state as beliefs and regulates behavior using declarative policies defined over these beliefs. This design supports adaptive, auditable, and composable execution through a database-backed semantic control plane. We showcase these concepts in a decision-control scenario, where beliefs and policies declaratively guide critical execution choices (e.g., model selection, retrieval, corrective re-execution), enabling dynamic behavior without requiring any changes to the underlying pipeline code.

</details>


### 63. SpaceMind: A Modular and Self-Evolving Embodied Vision-Language Agent Framework for Autonomous On-orbit Servicing

- **Authors:** Aodi Wu, Haodong Han, Xubo Luo, Ruisuo Wang, Shan He, Xue Wan
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14399v1](http://arxiv.org/abs/2604.14399v1)
- **PDF:** [https://arxiv.org/pdf/2604.14399v1](https://arxiv.org/pdf/2604.14399v1)
- **Categories:** cs.RO, cs.AI, eess.SY


> SpaceMind introduces a modular, self‑evolving vision‑language agent architecture for autonomous on‑orbit servicing, separating capabilities into dynamically routed skill modules, configurable Model Context Protocol (MCP) tool profiles, and injectable reasoning modes, and coupling them through an MCP‑Redis interface that allows the same code to run unchanged in both UE5 simulation and physical hardware. The authors evaluate the system over 192 closed‑loop runs on five satellite targets across three task families, showing 90‑100 % navigation success under nominal conditions and a uniquely robust “Prospective” mode that maintains success under sensor degradation, while a skill‑self‑evolution process can recover from failures and raise inspection scores from 12 to 59 out of 100 after a single failed episode. Real‑world tests confirm zero‑code‑modification transfer to a laboratory robot, achieving 100 % rendezvous success, demonstrating the framework’s practicality for long‑horizon, embodied AI servicing missions.


<details>
<summary>Abstract</summary>

Autonomous on-orbit servicing demands embodied agents that perceive through visual sensors, reason about 3D spatial situations, and execute multi-phase tasks over extended horizons. We present SpaceMind, a modular and self-evolving vision-language model (VLM) agent framework that decomposes knowledge, tools, and reasoning into three independently extensible dimensions: skill modules with dynamic routing, Model Context Protocol (MCP) tools with configurable profiles, and injectable reasoning-mode skills. An MCP-Redis interface layer enables the same codebase to operate across simulation and physical hardware without modification, and a Skill Self-Evolution mechanism distills operational experience into persistent skill files without model fine-tuning. We validate SpaceMind through 192 closed-loop runs across five satellites, three task types, and two environments, a UE5 simulation and a physical laboratory, deliberately including degraded conditions to stress-test robustness. Under nominal conditions all modes achieve 90--100% navigation success; under degradation, the Prospective mode uniquely succeeds in search-and-approach tasks where other modes fail. A self-evolution study shows that the agent recovers from failure in four of six groups from a single failed episode, including complete failure to 100% success and inspection scores improving from 12 to 59 out of 100. Real-world validation confirms zero-code-modification transfer to a physical robot with 100% rendezvous success. Code: https://github.com/wuaodi/SpaceMind

</details>


### 64. Coalition Formation in LLM Agent Networks: Stability Analysis and Convergence Guarantees

- **Authors:** Dongxin Guo, Jikun Wu, Siu-Ming Yiu
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14386v1](http://arxiv.org/abs/2604.14386v1)
- **PDF:** [https://arxiv.org/pdf/2604.14386v1](https://arxiv.org/pdf/2604.14386v1)
- **Categories:** cs.GT, cs.AI


> The paper introduces the **LLM Coalition Formation Game (LCFG)**, the first formal model that captures how large‑language‑model agents dynamically create cooperative groups, framing the problem within hedonic game theory and providing provable stability guarantees. By modeling LLM agents as **ε‑rational** decision makers, the authors derive sufficient conditions for the existence of Nash‑stable partitions, prove related computational complexity results, and devise the **Coalition‑of‑Thought (CoalT)** protocol that guides agents toward stable coalitions. Empirical tests with GPT‑4, Claude‑3, and Llama‑3 across 2 400 episodes show that CoalT achieves Nash stability in 73.2 % of runs—significantly higher than chain‑of‑thought (58.4 %) and standard prompting (41.8 %)—validating the theoretical predictions and offering a concrete foundation for building stable, coordinated multi‑LLM systems.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents are increasingly deployed in multi-agent systems requiring strategic coordination. While recent work has analyzed LLM behavior in two-player games, coalition formation, where $n$ agents dynamically form cooperative groups, remains theoretically uncharacterized. We present the first framework grounding coalition formation in LLM agent networks in hedonic game theory with formal stability guarantees. We introduce the LLM Coalition Formation Game (LCFG), establish sufficient conditions for Nash-stable partitions, and prove complexity results. Our analysis reveals that LLM agents exhibit bounded rationality characterized by $ε$-rational preferences; we provide both deterministic existence guarantees and consistency-driven stability bounds whose predictions are consistent with empirical outcomes. Experiments with GPT-4, Claude-3, and Llama-3 across 2,400 episodes validate our framework: LLM coalitions achieve Nash stability in 73.2% of cases under our Coalition-of-Thought (CoalT) protocol, compared to 58.4% under chain-of-thought and 41.8% under standard prompting ($p < 0.001$). Our framework provides theoretical foundations for designing stable multi-agent LLM systems.

</details>


### 65. Aerial Multi-Functional RIS in Fluid Antennas-Aided Full-Duplex Networks: A Self-Optimized Hybrid Deep Reinforcement Learning Approach

- **Authors:** Li-Hsiang Shen, Yu-Quan Zheng
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14309v2](http://arxiv.org/abs/2604.14309v2)
- **PDF:** [https://arxiv.org/pdf/2604.14309v2](https://arxiv.org/pdf/2604.14309v2)
- **Categories:** cs.IT, cs.AI, eess.SP


> **Main contribution:**  
The paper introduces a new 6G‑era network architecture that couples autonomous aerial vehicles equipped with multi‑functional reconfigurable intelligent surfaces (AM‑RIS) with fluid‑antenna‑based full‑duplex base stations, and proposes a self‑optimizing hybrid deep‑reinforcement‑learning (SOHRL) framework to jointly tune beamforming, user power, RIS configuration, and device positioning for maximal energy efficiency.

**Methodology:**  
The joint optimization problem—mixing continuous (beamforming, power, positions) and discrete (RIS phase‑shift/amplification/energy‑harvest states) variables—is tackled by a multi‑agent DRL scheme that combines multi‑agent Deep Q‑Networks for discrete actions with multi‑agent Proximal Policy Optimization for continuous actions, enriched with an attention‑driven state encoder and meta‑learning for automatic hyper‑parameter adaptation.

**Key findings:**  
Simulations show that SOHRL converges faster and yields higher energy efficiency than baseline DRL approaches lacking attention or hybrid design, and that the AM‑RIS‑assisted full‑duplex system outperforms half‑duplex, rigid‑antenna, partial‑EH, and conventional RIS setups, underscoring its promise for energy‑aware, high‑throughput wireless networks.


<details>
<summary>Abstract</summary>

To address high data traffic demands of sixth-generation (6G) networks, this paper proposes a novel architecture that integrates autonomous aerial vehicles (AAVs) and multi-functional reconfigurable intelligent surfaces (MF-RISs) as AM-RIS in fluid antenna (FA)-assisted full-duplex (FD) networks. The AM-RIS provides hybrid functionalities, including signal reflection, amplification, and energy harvesting (EH), potentially improving both signal coverage and sustainability. Meanwhile, FA facilitates fine-grained spatial adaptability at FD-enabled base station (BS), which complements residual self-interference (SI) suppression. We aim at maximizing the overall energy efficiency (EE) by jointly optimizing transmit DL beamforming at BS, UL user power, configuration of AM-RIS, and positions of the FA and AM-RIS. Owing to the hybrid continuous-discrete parameters and high dimensionality of the intractable problem, we have conceived a self-optimized multi-agent hybrid deep reinforcement learning (DRL) framework (SOHRL), which integrates multi-agent deep Q-networks (DQN) and multi-agent proximal policy optimization (PPO), respectively handling discrete and continuous actions. To enhance self-adaptability, an attention-driven state representation and meta-level hyperparameter optimization are incorporated, enabling multi-agents to autonomously adjust learning hyperparameters. Simulation results validate the effectiveness of the proposed AM-RIS-enabled FA-aided FD networks empowered by SOHRL algorithm. The results reveal that SOHRL outperforms benchmarks of the case without attention mechanism and conventional hybrid/multi-agent/standalone DRL. Moreover, AM-RIS in FD achieves the highest EE compared to half-duplex, conventional rigid antenna arrays, partial EH, and conventional RIS without amplification, highlighting its potential as a compelling solution for EE-aware wireless networks.

</details>


### 66. TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration

- **Authors:** Zerun Ma, Guoqiang Wang, Xinchen Xie, Yicheng Chen, He Du, Bowen Li, Yanan Sun, Wenran Liu, Kai Chen, Yining Li
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14116v1](http://arxiv.org/abs/2604.14116v1)
- **PDF:** [https://arxiv.org/pdf/2604.14116v1](https://arxiv.org/pdf/2604.14116v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution:** TREX introduces a fully autonomous multi‑agent framework that automates the entire lifecycle of LLM fine‑tuning— from problem specification and literature/data scouting to strategy design, dataset construction, training, and evaluation—by casting the iterative experimentation process as a tree‑structured search.  

**Methodology:** The system consists of a *Researcher* agent (which performs requirement analysis, gathers open‑domain knowledge, and proposes training recipes) and an *Executor* agent (which implements data pipelines, runs training jobs, and records results). Their interactions are organized into a searchable exploration tree that enables systematic planning, reuse of prior trial outcomes, and hierarchical insight extraction across multiple fine‑tuning rounds.  

**Key findings:** On the newly created FT‑Bench (10 realistic fine‑tuning tasks spanning core capability upgrades to domain‑specific improvements), TREX consistently discovers higher‑performing models than baseline manual or heuristic approaches, demonstrating that agent‑driven tree‑based exploration can reliably automate LLM fine‑tuning and yield measurable performance gains across diverse scenarios.


<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) have empowered AI research agents to perform isolated scientific tasks, automating complex, real-world workflows, such as LLM training, remains a significant challenge. In this paper, we introduce TREX, a multi-agent system that automates the entire LLM training life-cycle. By orchestrating collaboration between two core modules-the Researcher and the Executor-the system seamlessly performs requirement analysis, open-domain literature and data research, formulation of training strategies, preparation of data recipes, and model training and evaluation. The multi-round experimental process is modeled as a search tree, enabling the system to efficiently plan exploration paths, reuse historical results, and distill high-level insights from iterative trials. To evaluate the capability of automated LLM training, we construct FT-Bench, a benchmark comprising 10 tasks derived from real-world scenarios, ranging from optimizing fundamental model capabilities to enhancing performance on domain-specific tasks. Experimental results demonstrate that the TREX agent consistently optimizes model performance on target tasks.

</details>


### 67. $π$-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data

- **Authors:** Yaocheng Zhang, Yuanheng Zhu, Wenyue Chong, Songjun Tu, Qichao Zhang, Jiajun Chai, Xiaohan Wang, Wei Lin, Guojun Yin, Dongbin Zhao
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14054v1](http://arxiv.org/abs/2604.14054v1)
- **PDF:** [https://arxiv.org/pdf/2604.14054v1](https://arxiv.org/pdf/2604.14054v1)
- **Categories:** cs.LG, cs.CL


> **Main contribution:**  
The paper introduces **π‑Play**, a multi‑agent self‑play framework that turns the intermediate *question‑construction path* (QCP) generated during task creation into a source of privileged information, enabling dense self‑distillation without any external data or human feedback.

**Methodology:**  
An “examiner” agent produces a task together with its QCP (a reverse‑engineered solution trace). A “teacher” model consumes the QCP as privileged context and provides step‑by‑step supervision to a “student” search agent via self‑distillation. This creates a closed loop where the student improves from dense feedback rather than only sparse outcome rewards.

**Key findings:**  
Across several complex information‑seeking benchmarks, data‑free π‑Play outperforms fully supervised search agents and achieves a **2–3× boost in learning efficiency** compared with traditional self‑play, demonstrating that internally generated privileged information can replace costly external supervision in agentic AI systems.


<details>
<summary>Abstract</summary>

Deep search agents have emerged as a promising paradigm for addressing complex information-seeking tasks, but their training remains challenging due to sparse rewards, weak credit assignment, and limited labeled data. Self-play offers a scalable route to reduce data dependence, but conventional self-play optimizes students only through sparse outcome rewards, leading to low learning efficiency. In this work, we observe that self-play naturally produces a question construction path (QCP) during task generation, an intermediate artifact that captures the reverse solution process. This reveals a new source of privileged information for self-distillation: self-play can itself provide high-quality privileged context for the teacher model in a low-cost and scalable manner, without relying on human feedback or curated privileged information. Leveraging this insight, we propose Privileged Information Self-Play ($π$-Play), a multi-agent self-evolution framework. In $π$-Play, an examiner generates tasks together with their QCPs, and a teacher model leverages QCP as privileged context to densely supervise a student via self-distillation. This design transforms conventional sparse-reward self-play into a dense-feedback self-evolution loop. Extensive experiments show that data-free $π$-Play surpasses fully supervised search agents and improves evolutionary efficiency by 2-3$\times$ over conventional self-play.

</details>


### 68. ReviewGrounder: Improving Review Substantiveness with Rubric-Guided, Tool-Integrated Agents

- **Authors:** Zhuofeng Li, Yi Lu, Dongfu Jiang, Haoxiang Zhang, Yuyang Bai, Chuan Li, Yu Wang, Shuiwang Ji, Jianwen Xie, Yu Zhang
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14261v1](http://arxiv.org/abs/2604.14261v1)
- **PDF:** [https://arxiv.org/pdf/2604.14261v1](https://arxiv.org/pdf/2604.14261v1)
- **Categories:** cs.CL, cs.AI


> **Main contribution:** The paper introduces *ReviewGrounder*, a two‑stage, rubric‑guided multi‑agent system that transforms brief, template‑like reviewer drafts into substantively grounded peer‑review comments, and *ReviewBench*, a benchmark that evaluates review quality against paper‑specific rubrics, the manuscript itself, and human reviews.  

**Methodology:** ReviewGrounder first uses a lightweight LLM (Phi‑4‑14B) to generate an initial draft guided by explicit review rubrics. In a second grounding stage, a larger LLM (GPT‑OSS‑120B) accesses the target paper and relevant evidence via tool integration (e.g., retrieval, citation insertion) to enrich the draft with concrete, citation‑backed arguments. Performance is measured on ReviewBench across eight rubric dimensions.  

**Key findings:** The rubric‑guided, tool‑integrated pipeline consistently outperforms strong baselines—including much larger models such as GPT‑4.1 and DeepSeek‑R1‑670B—both in alignment with human judgments and in rubric‑based quality scores, demonstrating that explicit rubric use and evidence grounding are critical for producing substantive, high‑quality AI‑assisted peer reviews.


<details>
<summary>Abstract</summary>

The rapid rise in AI conference submissions has driven increasing exploration of large language models (LLMs) for peer review support. However, LLM-based reviewers often generate superficial, formulaic comments lacking substantive, evidence-grounded feedback. We attribute this to the underutilization of two key components of human reviewing: explicit rubrics and contextual grounding in existing work. To address this, we introduce REVIEWBENCH, a benchmark evaluating review text according to paper-specific rubrics derived from official guidelines, the paper's content, and human-written reviews. We further propose REVIEWGROUNDER, a rubric-guided, tool-integrated multi-agent framework that decomposes reviewing into drafting and grounding stages, enriching shallow drafts via targeted evidence consolidation. Experiments on REVIEWBENCH show that REVIEWGROUNDER, using a Phi-4-14B-based drafter and a GPT-OSS-120B-based grounding stage, consistently outperforms baselines with substantially stronger/larger backbones (e.g., GPT-4.1 and DeepSeek-R1-670B) in both alignment with human judgments and rubric-based review quality across 8 dimensions. The code is available \href{https://github.com/EigenTom/ReviewGrounder}{here}.

</details>


### 69. InfoChess: A Game of Adversarial Inference and a Laboratory for Quantifiable Information Control

- **Authors:** Kieran A. Murphy
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15373v1](http://arxiv.org/abs/2604.15373v1)
- **PDF:** [https://arxiv.org/pdf/2604.15373v1](https://arxiv.org/pdf/2604.15373v1)
- **Categories:** cs.MA, cs.AI, cs.IT, cs.LG


> InfoChess is a newly introduced two‑player, symmetric board game in which the sole objective is to infer the opponent’s hidden king location, with pieces serving only to modify line‑of‑sight rather than to capture. The authors construct a hierarchy of heuristic agents that incorporate progressively deeper opponent‑modeling and train a reinforcement‑learning (RL) agent that surpasses these baselines, evaluating performance with information‑theoretic metrics (belief entropy, oracle cross‑entropy, and predictive log‑score) that separate epistemic uncertainty, calibration error, and adversarial observation noise. Experiments show that the RL agent learns sophisticated information‑gathering and concealment policies, establishing InfoChess as a tractable testbed for studying multi‑agent inference and controllable information flow in partially observable environments.


<details>
<summary>Abstract</summary>

We propose InfoChess, a symmetric adversarial game that elevates competitive information acquisition to the primary objective. There is no piece capture, removing material incentives that would otherwise confound the role of information. Instead, pieces are used to alter visibility. Players are scored on their probabilistic inference of the opponent's king location over the duration of the game. To explore the space of strategies for playing InfoChess, we introduce a hierarchy of heuristic agents defined by increasing levels of opponent modeling, and train a reinforcement learning agent that outperforms these baselines. Leveraging the discrete structure of the game, we analyze gameplay through natural information-theoretic characterizations that include belief entropy, oracle cross entropy, and predictive log score under the action-induced observation channel. These measures disentangle epistemic uncertainty, calibration mismatch, and uncertainty induced by adversarial movement. The design of InfoChess renders it a testbed for studying multi-agent inference under partial observability. We release code for the environment and agents, and a public interface to encourage further study.

</details>


### 70. CollabCoder: Plan-Code Co-Evolution via Collaborative Decision-Making for Efficient Code Generation

- **Authors:** Duy Tung Doan, Quang Huy Phung, Dzung Nguyen, Khac-Hoai Nam Bui
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13946v1](http://arxiv.org/abs/2604.13946v1)
- **PDF:** [https://arxiv.org/pdf/2604.13946v1](https://arxiv.org/pdf/2604.13946v1)
- **Categories:** cs.SE, cs.CL


> CollabCoder introduces a **plan‑code co‑evolution** paradigm in which a planning agent and a coding agent continuously negotiate which component should act next during debugging, rather than following a fixed plan then a single execution pass. The authors implement this dynamic collaborative decision‑making via a lightweight controller that switches between plan generation and code synthesis modules, and evaluate it on standard code‑generation suites (including LiveCodeBench and xCodeEval). Experiments show that the co‑evolution strategy yields **11–20 % higher correctness** on difficult benchmarks while **cutting API calls by 4–10 per run**, demonstrating that adaptive multi‑agent coordination can both improve code quality and reduce computational overhead in agentic AI systems.


<details>
<summary>Abstract</summary>

Automated code generation remains a persistent challenge in software engineering, as conventional multi-agent frameworks are often constrained by static planning, isolated execution, high computational overhead, and limited adaptability to complex tasks. This paper introduces CollabCoder, a novel Plan-Code Co-Evolution framework that improves code generation through dynamic multi-agent collaboration. The core idea is to design a collaborative decision-making process between the plan module and the code module to decide which module should be executed for the debugging process. Extensive experiments on widely used benchmarks demonstrate that CollabCoder consistently improves code quality and robustness across tasks. Importantly, CollabCoder achieves performance comparable to or exceeding current state-of-the-art methods while reducing computational overhead, with efficiency gains becoming more pronounced as benchmark difficulty increases. On the more challenging LiveCodeBench and xCodeEval benchmarks, our approach improves performance by 11-20% over strong baselines while reducing the number of API calls by an average of 4-10 per execution.

</details>


### 71. Formalizing Kantian Ethics: Formula of the Universal Law Logic (FULL)

- **Authors:** Taylor Olson
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14254v1](http://arxiv.org/abs/2604.14254v1)
- **PDF:** [https://arxiv.org/pdf/2604.14254v1](https://arxiv.org/pdf/2604.14254v1)
- **Categories:** cs.AI, cs.LO


> This paper introduces **Formula of the Universal Law Logic (FULL)**, a multi‑sorted quantified modal logic that formalizes Kant’s first formulation of the categorical imperative (the Formula of the Universal Law) together with notions of causality and agency. By encoding the procedural test “act only on maxims that can be willed as universal laws,” FULL lets an artificial moral agent evaluate actions based on the agent’s intended purpose and on purely factual background knowledge, without requiring a pre‑specified list of moral axioms. Empirical demonstrations on three classic Kantian cases show that FULL can correctly classify actions as permissible or impermissible, suggesting a pathway toward more autonomous, purpose‑aware AMAs that ground their judgments in a formalized Kantian ethical procedure.


<details>
<summary>Abstract</summary>

The field of machine ethics aims to build Artificial Moral Agents (AMAs) to better understand morality and make AI agents safer. To do so, many approaches encode human moral intuition as a set of axioms on actions e.g., do not harm, you must help others. However, this introduces (at least) two limitations for future AMAs. First, it does not consider the agent's purposes in performing the action. Second, it assumes that we humans can enumerate our moral intuition. This paper explores formalizing a moral procedure that alleviates these two limitations. We specifically consider Kantian ethics and present a multi-sorted quantified modal logic we call the Formula of the Universal Law Logic (FULL). The FULL formalizes Kant's first formulation of the categorical imperative, the Formula of the Universal Law (FUL), and concepts such as causality and agency. We demonstrate on three cases from Kantian ethics that the FULL can reason to evaluate agents' actions for certain purposes without built-in moral intuition, given that it has sufficient (non-normative) background knowledge. Therefore, the FULL is a contribution towards more robust and autonomous AMAs, and a more formal understanding of Kantian ethics.

</details>


### 72. DiPO: Disentangled Perplexity Policy Optimization for Fine-grained Exploration-Exploitation Trade-Off

- **Authors:** Xiaofan Li, Ming Yang, Zhiyuan Ma, Shichao Ma, Jintao Du, Yu Cheng, Weiqiang Wang, Zhizhong Zhang, Xin Tan, Yanyun Qu, Lizhuang Ma, Yuan Xie
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13902v1](http://arxiv.org/abs/2604.13902v1)
- **PDF:** [https://arxiv.org/pdf/2604.13902v1](https://arxiv.org/pdf/2604.13902v1)
- **Categories:** cs.LG


> **Main contribution** – The paper introduces **DiPO**, a novel framework that disentangles the training data into high‑perplexity (hard, exploratory) and low‑perplexity (easy, exploitable) subspaces and uses this split to apply a fine‑grained, perplexity‑driven exploration‑exploitation trade‑off for reinforcement learning with verifiable rewards (RLVR) in LLMs.

**Methodology** – DiPO first maps each training sample into a perplexity space and separates it into “exploration” and “exploitation” buckets. It then employs a **bidirectional reward allocation** scheme that adjusts verification rewards minimally while biasing the policy gradient toward the appropriate bucket, effectively steering the LLM to explore difficult samples and exploit easy ones in a stable manner.

**Key findings** – Experiments on mathematical reasoning and function‑calling benchmarks show that DiPO outperforms standard RLVR baselines, yielding higher accuracy and more reliable reasoning by better balancing exploration of hard examples with exploitation of easy ones. This demonstrates that perplexity‑based sample disentanglement is an effective tool for improving agentic LLM performance.


<details>
<summary>Abstract</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) has catalyzed significant advances in the reasoning capabilities of Large Language Models (LLMs). However, effectively managing the exploration and exploitation trade-off remains a critical challenge. In this paper, we fully analyze the exploration and exploitation dilemma of extremely hard and easy samples during the training and propose a new fine-grained trade-off mechanism. Concretely, we introduce a perplexity space disentangling strategy that divides the sample space into distinct exploration (high perplexity) and exploitation (low perplexity) subspaces, thereby mining fine-grained samples requiring exploration-exploitation trade-off. Subsequently, we propose a bidirectional reward allocation mechanism with a minimum impact on verification rewards to implement perplexity-guided exploration and exploitation, enabling more stable policy optimization. Finally, we have evaluated our method on two mainstream tasks: mathematical reasoning and function calling, and experimental results demonstrate the superiority of the proposed method, confirming its effectiveness in enhancing LLM performance by fine-grained exploration-exploitation trade-off.

</details>


### 73. Beyond Conservative Automated Driving in Multi-Agent Scenarios via Coupled Model Predictive Control and Deep Reinforcement Learning

- **Authors:** Saeed Rahmani, Gözde Körpe, Zhenlin, Xu, Bruno Brito, Simeon Craig Calvert, Bart van Arem
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13891v1](http://arxiv.org/abs/2604.13891v1)
- **PDF:** [https://arxiv.org/pdf/2604.13891v1](https://arxiv.org/pdf/2604.13891v1)
- **Categories:** cs.RO, cs.AI, eess.SY


> The paper introduces a hybrid control architecture that nests a Model Predictive Control (MPC) planner within a deep reinforcement‑learning (RL) policy (MPC‑RL) to achieve safer yet less conservative automated driving at unsignalized intersections. By using the MPC’s constraint‑satisfaction backbone to generate feasible trajectories and letting the RL component learn a corrective policy on top of them, the authors obtain a system that cuts collision rates by 21 % and boosts success rates by 6.5 % relative to pure MPC, while also learning faster and transferring zero‑shot to a highway‑merging task far better than end‑to‑end PPO. The results demonstrate that coupling structured optimization with data‑driven adaptation can significantly improve the safety–efficiency trade‑off and cross‑scenario generalization of agentic AI for multi‑agent autonomous driving.


<details>
<summary>Abstract</summary>

Automated driving at unsignalized intersections is challenging due to complex multi-vehicle interactions and the need to balance safety and efficiency. Model Predictive Control (MPC) offers structured constraint handling through optimization but relies on hand-crafted rules that often produce overly conservative behavior. Deep Reinforcement Learning (RL) learns adaptive behaviors from experience but often struggles with safety assurance and generalization to unseen environments. In this study, we present an integrated MPC-RL framework to improve navigation performance in multi-agent scenarios. Experiments show that MPC-RL outperforms standalone MPC and end-to-end RL across three traffic-density levels. Collectively, MPC-RL reduces the collision rate by 21% and improves the success rate by 6.5% compared to pure MPC. We further evaluate zero-shot transfer to a highway merging scenario without retraining. Both MPC-based methods transfer substantially better than end-to-end PPO, which highlights the role of the MPC backbone in cross-scenario robustness. The framework also shows faster loss stabilization than end-to-end RL during training, which indicates a reduced learning burden. These results suggest that the integrated approach can improve the balance between safety performance and efficiency in multi-agent intersection scenarios, while the MPC component provides a strong foundation for generalization across driving environments. The implementation code is available open-source.

</details>


### 74. Sandpile Economics: Theory, Identification, and Evidence

- **Authors:** Diego Vallarino
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13890v1](http://arxiv.org/abs/2604.13890v1)
- **PDF:** [https://arxiv.org/pdf/2604.13890v1](https://arxiv.org/pdf/2604.13890v1)
- **Categories:** physics.soc-ph, cs.LG, econ.EM, econ.TH, stat.ML


> **Main contribution:** The paper introduces **Sandpile Economics**, a novel theoretical framework that links macro‑economic instability to the geometric fragility of production‑network structures, using the Forman–Ricci curvature of input‑output graphs as a state variable that predicts when economies become critically unstable.

**Methodology:** The authors formulate a dynamical model of evolving production networks in which specialization reduces substitutability and drives curvature downward; they derive analytically that once curvature crosses an endogenous threshold, cascade sizes follow a power‑law distribution (tail index α ∈ (1, 2)). They then estimate curvature from global input‑output tables and test its predictive power against standard network metrics.

**Key findings for agentic AI:** Empirical analysis shows that economies consistently operate in negative‑curvature regimes, and a one‑standard‑deviation increase in curvature markedly improves three‑year output growth forecasts and better explains cross‑country resilience than conventional measures. This demonstrates that the curvature‑driven criticality of production networks is an observable, agent‑level property that can be monitored and potentially steered by AI‑enabled policy agents to mitigate disproportionate crises.


<details>
<summary>Abstract</summary>

Why do capitalist economies recurrently generate crises whose severity is disproportionate to the size of the triggering shock? This paper proposes a structural answer grounded in the evolutionary geometry of production networks. As economies evolve through specialization, integration, and competitive selection, their inter-sectoral linkages drift toward configurations of increasing geometric fragility, eventually crossing a threshold beyond which small disturbances generate disproportionately large cascades.
  We introduce Sandpile Economics, a formal framework that interprets macroeconomic instability as an emergent property of disequilibrium production networks. The key state variable is the Forman--Ricci curvature of the input--output graph, capturing local substitution possibilities when supply chains are disrupted. We show that when curvature falls below an endogenous threshold, the distribution of cascade sizes follows a power law with tail index $α\in (1,2)$, implying a regime of unbounded amplification.
  The underlying mechanism is evolutionary: specialization reduces input substitutability, pushing the economy toward criticality, while crisis episodes induce endogenous network reconfiguration and path dependence. These dynamics are inherently non-ergodic and cannot be captured by representative-agent frameworks.
  Empirically, using global input--output data, we document that production networks operate in persistently negative curvature regimes and that curvature robustly predicts medium-run output dynamics. A one-standard-deviation increase in curvature is associated with higher cumulative growth over three-year horizons, and curvature systematically outperforms standard network metrics in explaining cross-country differences in resilience.

</details>


### 75. The cognitive companion: a lightweight parallel monitoring architecture for detecting and recovering from reasoning degradation in LLM agents

- **Authors:** Rafflesia Khan, Nafiul Islam Khan
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13759v1](http://arxiv.org/abs/2604.13759v1)
- **PDF:** [https://arxiv.org/pdf/2604.13759v1](https://arxiv.org/pdf/2604.13759v1)
- **Categories:** cs.AI, cs.LG


> **Main contribution:** The paper proposes the *Cognitive Companion*, a lightweight, parallel‑monitoring framework that watches LLM agents during multi‑step reasoning and intervenes when the primary model shows signs of degradation (loops, drift, stuck states). Two concrete realizctions are presented: (1) an LLM‑based Companion that generates corrective prompts, and (2) a zero‑overhead Probe‑based Companion that predicts failure from hidden‑state activations (layer 28).

**Methodology:** A three‑batch feasibility study was run on Gemma‑4‑E4B (plus exploratory tests on Qwen 2.5‑1.5B and Llama 3.2‑1B). The LLM‑Companion was invoked after each step and its cost measured; the Probe‑Companion was trained on a small proxy‑labeled dataset of hidden‑state features to fire interventions without extra inference. Performance was evaluated on loop‑prone, open‑ended, and structured benchmark tasks, measuring repetition reduction, AUROC of the probe, and overall task success.

**Key findings:**  
- The LLM‑Companion cut repetitive looping by **52‑62 %** with only **≈11 %** added inference overhead.  
- The Probe‑Companion achieved a mean effect size of **+0.471** and a cross‑validated **AUROC = 0.84**, delivering **zero measured overhead**.  
- Benefits are **task‑type dependent**: substantial gains on loop‑prone/open‑ended tasks, neutral or negative impact on highly structured tasks.  
- No measurable improvement was observed for 1 B–1.5 B models, suggesting a **scale threshold** for companion efficacy.

Overall, the study demonstrates that sub‑token, parallel monitoring can meaningfully rescue reasoning failures in high‑capacity LLM agents, while highlighting practical constraints (task polarity, model size) that should guide future selective‑activation designs.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents on multi-step tasks suffer reasoning degradation, looping, drift, stuck states, at rates up to 30% on hard tasks. Current solutions include hard step limits (abrupt) or LLM-as-judge monitoring (10-15% overhead per step). This paper introduces the Cognitive Companion, a parallel monitoring architecture with two implementations: an LLM-based Companion and a novel zero-overhead Probe-based Companion. We report a three-batch feasibility study centered on Gemma 4 E4B, with an additional exploratory small-model analysis on Qwen 2.5 1.5B and Llama 3.2 1B. In our experiments, the LLM-based Companion reduced repetition on loop-prone tasks by 52-62% with approximately 11% overhead. The Probe-based Companion, trained on hidden states from layer 28, showed a mean effect size of +0.471 at zero measured inference overhead; its strongest probe result achieved cross-validated AUROC 0.840 on a small proxy-labeled dataset. A key empirical finding is that companion benefit appears task-type dependent: companions are most helpful on loop-prone and open-ended tasks, while effects are neutral or negative on more structured tasks. Our small-model experiments also suggest a possible scale boundary: companions did not improve the measured quality proxy on 1B-1.5B models, even when interventions fired. Overall, the paper should be read as a feasibility study rather than a definitive validation. The results provide encouraging evidence that sub-token monitoring may be useful, identify task-type sensitivity as a practical design constraint, and motivate selective companion activation as a promising direction for future work.

</details>


### 76. Rethinking AI Hardware: A Three-Layer Cognitive Architecture for Autonomous Agents

- **Authors:** Li Chen
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13757v1](http://arxiv.org/abs/2604.13757v1)
- **PDF:** [https://arxiv.org/pdf/2604.13757v1](https://arxiv.org/pdf/2604.13757v1)
- **Categories:** cs.AI, cs.HC


> The paper proposes the **Tri‑Spirit Architecture**, a three‑layer cognitive stack that separates an autonomous agent’s **planning** (Super Layer), **reasoning** (Agent Layer), and **execution** (Reflex Layer) onto specialized hardware substrates and connects them through an asynchronous message bus. Using a formal routing policy, habit‑compilation (promoting recurrent reasoning traces to zero‑inference reflexes), and a convergent memory model with safety constraints, the authors implement a prototype and benchmark it on 2 000 synthetic tasks against traditional cloud‑centric and edge‑only pipelines. The results show that this cognitive decomposition cuts average task latency by **≈ 75 %**, energy use by **≈ 71 %**, reduces large‑language‑model calls by **30 %**, and enables **≈ 78 %** of tasks to finish offline, demonstrating that architectural separation of cognitive functions—rather than raw model scaling—is a key lever for efficient, agentic AI hardware.


<details>
<summary>Abstract</summary>

The next generation of autonomous AI systems will be constrained not only by model capability, but by how intelligence is structured across heterogeneous hardware. Current paradigms -- cloud-centric AI, on-device inference, and edge-cloud pipelines -- treat planning, reasoning, and execution as a monolithic process, leading to unnecessary latency, energy consumption, and fragmented behavioral continuity. We introduce the Tri-Spirit Architecture, a three-layer cognitive framework that decomposes intelligence into planning (Super Layer), reasoning (Agent Layer), and execution (Reflex Layer), each mapped to distinct compute substrates and coordinated via an asynchronous message bus. We formalize the system with a parameterized routing policy, a habit-compilation mechanism that promotes repeated reasoning paths into zero-inference execution policies, a convergent memory model, and explicit safety constraints. We evaluate the architecture in a reproducible simulation of 2000 synthetic tasks against cloud-centric and edge-only baselines. Tri-Spirit reduces mean task latency by 75.6 percent and energy consumption by 71.1 percent, while decreasing LLM invocations by 30 percent and enabling 77.6 percent offline task completion. These results suggest that cognitive decomposition, rather than model scaling alone, is a primary driver of system-level efficiency in AI hardware.

</details>


### 77. Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration

- **Authors:** Sayan Kumar Chaki, Antoine Gourru, Julien Velcin
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13705v1](http://arxiv.org/abs/2604.13705v1)
- **PDF:** [https://arxiv.org/pdf/2604.13705v1](https://arxiv.org/pdf/2604.13705v1)
- **Categories:** cs.CL, cs.AI, cs.GT, cs.MA


> The paper demonstrates that fairness in language‑model‑based decision making can arise from the dynamics of multi‑agent negotiation rather than from a single centrally‑aligned model. Using a hospital‑triage simulation in which a ethically‑aligned agent (via retrieval‑augmented generation) debates with either a neutral or adversarial agent over three structured rounds, the authors show that while each agent alone produces ethically unsatisfactory allocations, their joint deliberation yields outcomes that satisfy standard fairness criteria. The study links this emergent fairness to Arrow’s impossibility theorem, arguing that decentralized agent interaction—rather than individual model alignment—is the proper unit for evaluating and engineering fair AI systems.


<details>
<summary>Abstract</summary>

Fairness in language models is typically studied as a property of a single, centrally optimized model. As large language models become increasingly agentic, we propose that fairness emerges through interaction and exchange. We study this via a controlled hospital triage framework in which two agents negotiate over three structured debate rounds. One agent is aligned to a specific ethical framework via retrieval-augmented generation (RAG), while the other is either unaligned or adversarially prompted to favor demographic groups over clinical need. We find that alignment systematically shapes negotiation strategies and allocation patterns, and that neither agent's allocation is ethically adequate in isolation, yet their joint final allocation can satisfy fairness criteria that neither would have reached alone. Aligned agents partially moderate bias through contestation rather than override, acting as corrective patches that restore access for marginalized groups without fully converting a biased counterpart. We further observe that even explicitly aligned agents exhibit intrinsic biases toward certain frameworks, consistent with known left-leaning tendencies in LLMs. We connect these limits to Arrow's Impossibility Theorem: no aggregation mechanism can simultaneously satisfy all desiderata of collective rationality, and multi-agent deliberation navigates rather than resolves this constraint. Our results reposition fairness as an emergent, procedural property of decentralized agent interaction, and the system rather than the individual agent as the appropriate unit of evaluation.

</details>


### 78. MIND: AI Co-Scientist for Material Research

- **Authors:** Geonhee Ahn, Donghyun Lee, Hayoung Doo, Jonggeol Na, Hyunsoo Cho, Sookyung Kim
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13699v1](http://arxiv.org/abs/2604.13699v1)
- **PDF:** [https://arxiv.org/pdf/2604.13699v1](https://arxiv.org/pdf/2604.13699v1)
- **Categories:** cs.MA, cs.AI, cs.CE


> MIND introduces a fully automated, LLM‑orchestrated pipeline for materials discovery that moves beyond text‑only reasoning by coupling hypothesis generation/refinement with high‑throughput *in‑silico* experiments using the SevenNet‑Omni machine‑learning interatomic potential. The framework decomposes the scientific workflow into three interacting agents—refiner, experimentalist, and debater—and executes the experimental step via scalable molecular‑simulation runs, while a web UI allows users to submit and monitor hypothesis tests. Empirical evaluations show that MIND can generate, test, and iteratively improve material‑property hypotheses without human intervention, demonstrating a viable template for agentic AI systems that integrate reasoning with automated scientific validation.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have enabled agentic AI systems for scientific discovery, but most approaches remain limited to textbased reasoning without automated experimental verification. We propose MIND, an LLM-driven framework for automated hypothesis validation in materials research. MIND organizes the scientific discovery process into hypothesis refinement, experimentation, and debate-based validation within a multi-agent pipeline. For experimental verification, the system integrates Machine Learning Interatomic Potentials, particularly SevenNet-Omni, enabling scalable in-silico experiments. We also provide a web-based user interface for automated hypothesis testing. The modular design allows additional experimental modules to be integrated, making the framework adaptable to broader scientific workflows. The code is available at: https://github.com/IMMS-Ewha/MIND, and a demonstration video at: https://youtu.be/lqiFe1OQzN4.

</details>


### 79. IndicDB -- Benchmarking Multilingual Text-to-SQL Capabilities in Indian Languages

- **Authors:** Aviral Dawar, Roshan Karanth, Vikram Goyal, Dhruv Kumar
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13686v1](http://arxiv.org/abs/2604.13686v1)
- **PDF:** [https://arxiv.org/pdf/2604.13686v1](https://arxiv.org/pdf/2604.13686v1)
- **Categories:** cs.CL, cs.AI, cs.DB


> **Main contribution:** The paper introduces **IndicDB**, the first large‑scale, multilingual Text‑to‑SQL benchmark that targets realistic Indian government datasets and supports six Indic languages (English, Hindi, plus five others), thereby exposing a previously undocumented “Indic Gap” in cross‑lingual semantic parsing.  

**Methodology:** Real‑world relational schemas (20 databases, 237 tables) are built from open‑data portals (NDAP, IDP) using a three‑agent pipeline—**Architect**, **Auditor**, and **Refiner**—that iteratively designs, validates, and refines dense schemas (≈12 tables per DB, join depth up to 6). The pipeline is value‑aware and difficulty‑calibrated, producing 15,617 English‑Indic question‑SQL pairs across varying complexities.  

**Key findings:** When evaluated on leading LLMs (DeepSeek v3.2, MiniMax 2.7, LLaMA 3.3, Qwen‑3), performance drops by **≈9 %** when moving from English to Indic languages, driven by harder schema linking, greater structural ambiguity, and limited external knowledge in these languages. IndicDB thus provides a rigorous, multilingual benchmark for advancing agentic LLMs in non‑Western, real‑world Text‑to‑SQL applications.


<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) have significantly advanced Text-to-SQL performance, existing benchmarks predominantly focus on Western contexts and simplified schemas, leaving a gap in real-world, non-Western applications. We present IndicDB, a multilingual Text-to-SQL benchmark for evaluating cross-lingual semantic parsing across diverse Indic languages. The relational schemas are sourced from open-data platforms, including the National Data and Analytics Platform (NDAP) and the India Data Portal (IDP), ensuring realistic administrative data complexity. IndicDB comprises 20 databases across 237 tables. To convert denormalized government data into rich relational structures, we employ an iterative three-agent framework (Architect, Auditor, Refiner) to ensure structural rigor and high relational density (11.85 tables per database; join depths up to six). Our pipeline is value-aware, difficulty-calibrated, and join-enforced, generating 15,617 tasks across English, Hindi, and five Indic languages. We evaluate cross-lingual semantic parsing performance of state-of-the-art models (DeepSeek v3.2, MiniMax 2.7, LLaMA 3.3, Qwen3) across seven linguistic variants. Results show a 9.00% performance drop from English to Indic languages, revealing an "Indic Gap" driven by harder schema linking, increased structural ambiguity, and limited external knowledge. IndicDB serves as a rigorous benchmark for multilingual Text-to-SQL. Code and data: https://anonymous.4open.science/r/multilingualText2Sql-Indic--DDCC/

</details>


### 80. Golden Handcuffs make safer AI agents

- **Authors:** Aram Ebtekar, Michael K. Cohen
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13609v1](http://arxiv.org/abs/2604.13609v1)
- **PDF:** [https://arxiv.org/pdf/2604.13609v1](https://arxiv.org/pdf/2604.13609v1)
- **Categories:** cs.LG, cs.AI


> **Summary**  
The paper introduces “Golden Handcuffs,” a Bayesian safety mechanism that augments an RL agent’s reward model with an extreme penalty (‑L) that never occurs in the true environment (whose rewards lie in [0, 1]). By conditioning on the possibility of incurring this huge loss, the agent becomes risk‑averse to novel, high‑reward hacks; a simple override then hands control to a trusted mentor whenever the agent’s predicted value falls below a preset safety threshold. The authors prove that (i) the agent can still learn efficiently—its regret against the best mentor grows sub‑linearly while mentor‑guided exploration vanishes over time—and (ii) the agent’s policy cannot trigger any low‑complexity safety predicate before the mentor does, guaranteeing that the agent cannot autonomously cross a safety “line.” This contribution provides a formal, tractable approach to embedding safe‑fallback behavior in general‑purpose, potentially self‑modifying AI agents.


<details>
<summary>Abstract</summary>

Reinforcement learners can attain high reward through novel unintended strategies. We study a Bayesian mitigation for general environments: we expand the agent's subjective reward range to include a large negative value $-L$, while the true environment's rewards lie in $[0,1]$. After observing consistently high rewards, the Bayesian policy becomes risk-averse to novel schemes that plausibly lead to $-L$. We design a simple override mechanism that yields control to a safe mentor whenever the predicted value drops below a fixed threshold. We prove two properties of the resulting agent: (i) Capability: using mentor-guided exploration with vanishing frequency, the agent attains sublinear regret against its best mentor. (ii) Safety: no decidable low-complexity predicate is triggered by the optimizing policy before it is triggered by a mentor.

</details>


### 81. Foresight Optimization for Strategic Reasoning in Large Language Models

- **Authors:** Jiashuo Wang, Jiawen Duan, Jian Wang, Kaitao Song, Chunpu Xu, Johnny K. W. Ho, Fenggang Yu, Wenjie Li, Johan F. Hoorn
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13592v2](http://arxiv.org/abs/2604.13592v2)
- **PDF:** [https://arxiv.org/pdf/2604.13592v2](https://arxiv.org/pdf/2604.13592v2)
- **Categories:** cs.CL


> The paper introduces **Foresight Policy Optimization (FoPO)**, a training framework that endows large language models with explicit strategic foresight by integrating opponent‑modeling into a policy‑optimization loop. FoPO is evaluated through self‑play on two newly curated multi‑agent benchmarks—Cooperative RSA and Competitive Taboo—and shows that, across LLMs of different scales and architectures, it markedly improves the ability to anticipate and counteract other agents’ actions, yielding decisive gains over existing reasoning‑enhancement baselines and robust generalization to unseen strategic tasks.


<details>
<summary>Abstract</summary>

Reasoning capabilities in large language models (LLMs) have generally advanced significantly. However, it is still challenging for existing reasoning-based LLMs to perform effective decision-making abilities in multi-agent environments, due to the absence of explicit foresight modeling. To this end, strategic reasoning, the most fundamental capability to anticipate the counterpart's behaviors and foresee its possible future actions, has been introduced to alleviate the above issues. Strategic reasoning is fundamental to effective decision-making in multi-agent environments, yet existing reasoning enhancement methods for LLMs do not explicitly capture its foresight nature. In this work, we introduce Foresight Policy Optimization (FoPO) to enhance strategic reasoning in LLMs, which integrates opponent modeling principles into policy optimization, thereby enabling explicit consideration of both self-interest and counterpart influence. Specifically, we construct two curated datasets, namely Cooperative RSA and Competitive Taboo, equipped with well-designed rules and moderate difficulty to facilitate a systematic investigation of FoPO in a self-play framework. Our experiments demonstrate that FoPO significantly enhances strategic reasoning across LLMs of varying sizes and origins. Moreover, models trained with FoPO exhibit strong generalization to out-of-domain strategic scenarios, substantially outperforming standard LLM reasoning optimization baselines.

</details>


### 82. Training-Free Test-Time Contrastive Learning for Large Language Models

- **Authors:** Kaiwen Zheng, Kai Zhou, Jinwu Hu, Te Gu, Mingkai Peng, Fei Liu
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13552v1](http://arxiv.org/abs/2604.13552v1)
- **PDF:** [https://arxiv.org/pdf/2604.13552v1](https://arxiv.org/pdf/2604.13552v1)
- **Categories:** cs.CL, cs.AI


> **Main contribution:** The paper introduces **TF‑TTCL**, a fully training‑free test‑time adaptation framework that equips a frozen large language model (LLM) with the ability to improve its own reasoning online, without any gradient updates or external supervision.

**Methodology:** TF‑TTCL implements an “Explore‑Reflect‑Steer” loop: (1) *Semantic Query Augmentation* uses multi‑agent role‑playing to generate diverse reasoning trajectories for the same input; (2) *Contrastive Experience Distillation* compares higher‑quality versus lower‑quality trajectories, extracting the semantic differences into explicit textual rules; (3) *Contextual Rule Retrieval* fetches and applies those rules during subsequent inference to steer the LLM away from previously observed errors.

**Key findings:** Across a suite of closed‑ended reasoning benchmarks and open‑ended evaluation tasks, TF‑TTCL consistently beats strong zero‑shot baselines and existing test‑time adaptation methods, demonstrating that contrastive, rule‑based self‑distillation can robustly mitigate distribution shift in agentic LLMs without any additional training.


<details>
<summary>Abstract</summary>

Large language models (LLMs) demonstrate strong reasoning capabilities, but their performance often degrades under distribution shift. Existing test-time adaptation (TTA) methods rely on gradient-based updates that require white-box access and need substantial overhead, while training-free alternatives are either static or depend on external guidance. In this paper, we propose Training-Free Test-Time Contrastive Learning TF-TTCL, a training-free adaptation framework that enables a frozen LLM to improve online by distilling supervision from its own inference experiences. Specifically, TF-TTCL implements a dynamic "Explore-Reflect-Steer" loop through three core modules: 1) Semantic Query Augmentation first diversifies problem views via multi-agent role-playing to generate different reasoning trajectories; 2) Contrastive Experience Distillation then captures the semantic gap between superior and inferior trajectories, distilling them into explicit textual rules; and 3) Contextual Rule Retrieval finally activates these stored rules during inference to dynamically steer the frozen LLM toward robust reasoning patterns while avoiding observed errors. Extensive experiments on closed-ended reasoning tasks and open-ended evaluation tasks demonstrate that TF-TTCL consistently outperforms strong zero-shot baselines and representative TTA methods under online evaluation. Code is available at https://github.com/KevinSCUTer/TF-TTCL.

</details>


### 83. Debate to Align: Reliable Entity Alignment through Two-Stage Multi-Agent Debate

- **Authors:** Cunda Wang, Ziying Ma, Po Hu, Weihua Wang, Feilong Bao
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13551v1](http://arxiv.org/abs/2604.13551v1)
- **PDF:** [https://arxiv.org/pdf/2604.13551v1](https://arxiv.org/pdf/2604.13551v1)
- **Categories:** cs.CL, cs.IR


> **Main contribution**  
The paper introduces **AgentEA**, a novel entity‑alignment framework that harnesses a two‑stage multi‑agent debate to improve both the quality of candidate entity sets and the reliability of alignment decisions made by large language models.

**Methodology**  
First, AgentEA refines entity embeddings via a **representation‑preference optimization** step that yields more discriminative vectors. Then, for each uncertain entity it runs a **lightweight debate verification** (quick cross‑checking among specialized agents to filter out implausible candidates) followed by a **deep debate alignment** (in‑depth reasoning by higher‑capacity agents that iteratively argue and vote on the final match), effectively turning the alignment task into a structured multi‑agent deliberation process.

**Key findings**  
Experiments on diverse cross‑lingual, sparse, large‑scale, and heterogeneous KG benchmarks show that AgentEA consistently outperforms existing LLM‑based and embedding‑only methods, achieving higher alignment accuracy while requiring fewer LLM calls thanks to the staged debate that filters candidates early. This demonstrates that multi‑agent debate can substantially boost the reliability and efficiency of agentic AI systems for knowledge‑graph alignment.


<details>
<summary>Abstract</summary>

Entity alignment (EA) aims to identify entities referring to the same real-world object across different knowledge graphs (KGs). Recent approaches based on large language models (LLMs) typically obtain entity embeddings through knowledge representation learning and use embedding similarity to identify an alignment-uncertain entity set. For each uncertain entity, a candidate entity set (CES) is then retrieved based on embedding similarity to support subsequent alignment reasoning and decision making. However, the reliability of the CES and the reasoning capability of LLMs critically affect the effectiveness of subsequent alignment decisions. To address this issue, we propose AgentEA, a reliable EA framework based on multi-agent debate. AgentEA first improves embedding quality through entity representation preference optimization, and then introduces a two-stage multi-role debate mechanism consisting of lightweight debate verification and deep debate alignment to progressively enhance the reliability of alignment decisions while enabling more efficient debate-based reasoning. Extensive experiments on public benchmarks under cross-lingual, sparse, large-scale, and heterogeneous settings demonstrate the effectiveness of AgentEA.

</details>


### 84. Towards Scalable Lightweight GUI Agents via Multi-role Orchestration

- **Authors:** Ziwei Wang, Junjie Zheng, Leyang Yang, Sheng Zhou, Xiaoxuan Tang, Zhouhua Fang, Zhiwei Liu, Dajun Chen, Yong Li, Jiajun Bu
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13488v1](http://arxiv.org/abs/2604.13488v1)
- **PDF:** [https://arxiv.org/pdf/2604.13488v1](https://arxiv.org/pdf/2604.13488v1)
- **Categories:** cs.AI


> The paper introduces **LAMO**, a framework that equips a lightweight (3‑billion‑parameter) multimodal LLM with GUI‑automation capabilities by endowing it with **role‑oriented knowledge** and a **two‑stage training pipeline**: (1) supervised fine‑tuning using a perplexity‑weighted cross‑entropy loss to distill GUI‑specific knowledge and improve visual perception, and (2) reinforcement‑learning that encourages cooperative exploration among multiple “roles” (e.g., planner, executor, coordinator) so the agent can both act monolithically and participate in a multi‑agent system. Experiments on static benchmarks and live online tasks show that LAMO‑3B matches or exceeds larger specialist models while remaining deployable on resource‑constrained devices, and its plug‑and‑play planner interface lets it continually benefit from advances in external planners—demonstrating a scalable, cost‑effective path for lightweight GUI agents in the agentic AI ecosystem.


<details>
<summary>Abstract</summary>

Autonomous Graphical User Interface (GUI) agents powered by Multimodal Large Language Models (MLLMs) enable digital automation on end-user devices. While scaling both parameters and data has yielded substantial gains, advanced methods still suffer from prohibitive deployment costs on resource-constrained devices. When facing complex in-the-wild scenarios, lightweight GUI agents are bottlenecked by limited capacity and poor task scalability under end-to-end episodic learning, impeding adaptation to multi-agent systems (MAS), while training multiple skill-specific experts remains costly. Can we strike an effective trade-off in this cost-scalability dilemma, enabling lightweight MLLMs to participate in realistic GUI workflows? To address these challenges, we propose the LAMO framework, which endows a lightweight MLLM with GUI-specific knowledge and task scalability, allowing multi-role orchestration to expand its capability boundary for GUI automation. LAMO combines role-oriented data synthesis with a two-stage training recipe: (i) supervised fine-tuning with Perplexity-Weighted Cross-Entropy optimization for knowledge distillation and visual perception enhancement, and (ii) reinforcement learning for role-oriented cooperative exploration. With LAMO, we develop a task-scalable native GUI agent, LAMO-3B, supporting monolithic execution and MAS-style orchestration. When paired with advanced planners as a plug-and-play policy executor, LAMO-3B can continuously benefit from planner advances, enabling a higher performance ceiling. Extensive static and online evaluations validate the effectiveness of our design.

</details>


### 85. Bridging MARL to SARL: An Order-Independent Multi-Agent Transformer via Latent Consensus

- **Authors:** Zijian Zhao, Jing Gao, Sen Li
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13472v1](http://arxiv.org/abs/2604.13472v1)
- **PDF:** [https://arxiv.org/pdf/2604.13472v1](https://arxiv.org/pdf/2604.13472v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> **Main contribution**  
The paper introduces the **Consensus Multi‑Agent Transformer (CMAT)**, a centralized architecture that reframes cooperative MARL as a hierarchical single‑agent RL problem. By treating the whole team as one “agent” and inserting a **latent consensus vector** generated autoregressively by a Transformer decoder, CMAT achieves order‑independent joint action selection without the instability of conventional multi‑agent factorisations.

**Methodology**  
CMAT encodes the full joint observation with a Transformer encoder. A decoder then produces a high‑level consensus embedding that captures how agents should coordinate; conditioned on this embedding, all agents simultaneously sample their individual actions. This design enables the entire system to be trained with standard single‑agent PPO, leveraging the expressive power of Transformers while bypassing the combinatorial joint‑action space.

**Key findings**  
Across diverse cooperative benchmarks (StarCraft II micromanagement, Multi‑Agent MuJoCo, and Google Research Football), CMAT consistently outperforms state‑of‑the‑art centralized MARL approaches, sequential MARL baselines, and earlier Multi‑Agent Transformer variants, demonstrating superior coordination, stability, and sample efficiency—highlighting its potential as a scalable, theoretically tractable framework for agentic AI.


<details>
<summary>Abstract</summary>

Cooperative multi-agent reinforcement learning (MARL) is widely used to address large joint observation and action spaces by decomposing a centralized control problem into multiple interacting agents. However, such decomposition often introduces additional challenges, including non-stationarity, unstable training, weak coordination, and limited theoretical guarantees. In this paper, we propose the Consensus Multi-Agent Transformer (CMAT), a centralized framework that bridges cooperative MARL to a hierarchical single-agent reinforcement learning (SARL) formulation. CMAT treats all agents as a unified entity and employs a Transformer encoder to process the large joint observation space. To handle the extensive joint action space, we introduce a hierarchical decision-making mechanism in which a Transformer decoder autoregressively generates a high-level consensus vector, simulating the process by which agents reach agreement on their strategies in latent space. Conditioned on this consensus, all agents generate their actions simultaneously, enabling order-independent joint decision making and avoiding the sensitivity to action-generation order in conventional Multi-Agent Transformers (MAT). This factorization allows the joint policy to be optimized using single-agent PPO while preserving expressive coordination through the latent consensus. To evaluate the proposed method, we conduct experiments on benchmark tasks from StarCraft II, Multi-Agent MuJoCo, and Google Research Football. The results show that CMAT achieves superior performance over recent centralized solutions, sequential MARL methods, and conventional MARL baselines. The code for this paper is available at:https://github.com/RS2002/CMAT .

</details>


### 86. CANVAS: Continuity-Aware Narratives via Visual Agentic Storyboarding

- **Authors:** Ishani Mondal, Yiwen Song, Mihir Parmar, Palash Goyal, Jordan Boyd-Graber, Tomas Pfister, Yale Song
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13452v1](http://arxiv.org/abs/2604.13452v1)
- **PDF:** [https://arxiv.org/pdf/2604.13452v1](https://arxiv.org/pdf/2604.13452v1)
- **Categories:** cs.CL


> **Paper Summary**

The authors present **CANVAS**, a multi‑agent system that plans and generates multi‑shot visual stories while explicitly maintaining continuity of characters, backgrounds, and props. The methodology couples a *storyboard planner* (which decides scene order and spatial layout), a *character agent* (which enforces identity‑preserving embeddings across frames), and a *background anchor agent* (which caches and re‑uses environment features to guarantee stable settings). By iterating between planning and diffusion‑based frame synthesis, CANVAS produces coherent narratives without the abrupt changes typical of single‑shot generators.

Evaluated on the ST‑BENCH and ViStoryBench datasets—and on a newly introduced **HardContinuityBench** that stresses long‑range consistency—CANVAS beats the strongest baselines, raising background continuity scores by **21.6 %**, character consistency by **9.6 %**, and props consistency by **7.6 %**. These results demonstrate that agentic planning of visual continuity is a viable route toward more reliable long‑form generative visual storytelling.


<details>
<summary>Abstract</summary>

Long-form visual storytelling requires maintaining continuity across shots, including consistent characters, stable environments, and smooth scene transitions. While existing generative models can produce strong individual frames, they fail to preserve such continuity, leading to appearance changes, inconsistent backgrounds, and abrupt scene shifts. We introduce CANVAS (Continuity-Aware Narratives via Visual Agentic Storyboarding), a multi-agent framework that explicitly plans visual continuity in multi-shot narratives. CANVAS enforces coherence through character continuity, persistent background anchors, and location-aware scene planning for smooth transitions within the same setting We evaluate CANVAS on two storyboard generation benchmarks ST-BENCH and ViStoryBench and introduce a new challenging benchmark HardContinuityBench for long-range narrative consistency. CANVAS consistently outperforms the best-performing baseline, improving background continuity by 21.6%, character consistency by 9.6% and props consistency by 7.6%.

</details>


### 87. MERRIN: A Benchmark for Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments

- **Authors:** Han Wang, David Wan, Hyunji Lee, Thinh Pham, Mikaela Cankosyan, Weiyuan Chen, Elias Stengel-Eskin, Tu Vu, Mohit Bansal
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13418v1](http://arxiv.org/abs/2604.13418v1)
- **PDF:** [https://arxiv.org/pdf/2604.13418v1](https://arxiv.org/pdf/2604.13418v1)
- **Categories:** cs.CL, cs.AI, cs.CV


> **Main contribution:** The paper introduces **MERRIN**, a human‑annotated benchmark that evaluates search‑augmented agents on **multimodal evidence retrieval and multi‑hop reasoning** in realistic, noisy web settings, emphasizing natural‑language queries, under‑explored modalities (video, audio), and conflicting information.

**Methodology:** The authors construct a dataset of query‑answer triples with ground‑truth multimodal evidence, then test a spectrum of ten state‑of‑the‑art models (closed‑source GPT‑5.4‑mini, Gemini series, and open‑weight Qwen variants) under three search regimes (no search, native search, and agentic search), measuring accuracy, step count, and tool usage.

**Key findings:** All agents struggle markedly—average accuracy is only **22.3%**, with the best agent at **40.1%**—and stronger models gain only modest improvements while over‑exploring and being distracted by noisy or conflicting content, especially favoring text over other modalities. Compared to humans, these agents consume more computational resources yet achieve lower accuracy, underscoring the need for more robust, multimodal‑aware search and reasoning capabilities in agentic AI.


<details>
<summary>Abstract</summary>

Motivated by the underspecified, multi-hop nature of search queries and the multimodal, heterogeneous, and often conflicting nature of real-world web results, we introduce MERRIN (Multimodal Evidence Retrieval and Reasoning in Noisy Web Environments), a human-annotated benchmark for evaluating search-augmented agents. MERRIN measures AI agents' ability to identify relevant modalities, retrieve multimodal evidence, and perform multi-hop reasoning over noisy web sources. It differs from prior work in three important aspects: (1) using natural language queries without explicit modality cues, (2) incorporating underexplored modalities such as video and audio, and (3) requiring the retrieval of complex, often noisy or conflicting multimodal evidence during web search. We evaluate diverse search agents powered by ten models, including strong closed-source models (e.g., GPT-5.4-mini, Gemini 3/3.1 Flash/Pro) and open-weight models (Qwen3-4B/30B/235B), across three search settings (no search, native search, and agentic search). Our results show that MERRIN is highly challenging: the average accuracy across all agents is 22.3%, with the best-performing agent reaching only 40.1%. We further observe that while stronger agents like Gemini Deep Research achieve higher performance, gains are modest due to over-exploration; they take more steps and use more tools, but are often distracted by conflicting or partially relevant web content, leading to incorrect answers. Compared to humans, these agents consume more resources yet achieve lower accuracy, largely due to inefficient source selection and an overreliance on text modalities. These findings highlight the need for search agents capable of robust search and reasoning across diverse modalities in noisy web environments, making MERRIN a valuable testbed for evaluating such capabilities.

</details>


### 88. SoK: Security of Autonomous LLM Agents in Agentic Commerce

- **Authors:** Qian'ang Mao, Jiaxin Wang, Ya Liu, Li Zhu, Cong Ma, Jiaqi Yan
- **Published:** 2026-04-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.15367v1](http://arxiv.org/abs/2604.15367v1)
- **PDF:** [https://arxiv.org/pdf/2604.15367v1](https://arxiv.org/pdf/2604.15367v1)
- **Categories:** cs.CR, cs.MA


> The paper presents a Systematization of Knowledge (SoK) that defines a comprehensive security framework for autonomous LLM‑driven agents operating in “agentic commerce.” By classifying threats along five dimensions—agent integrity, transaction authorization, inter‑agent trust, market manipulation, and regulatory compliance—and analyzing a curated corpus of scholarly and industry sources, the authors identify 12 cross‑layer attack vectors that can cascade from the agents’ reasoning and tooling layers down to custody, settlement, market harm, and compliance failures. They then propose a layered defense architecture (tightening authorization, identity, protocol‑level safeguards, and market‑structure controls) and outline a research and benchmarking roadmap, highlighting that securing agentic commerce demands coordinated measures across LLM safety, protocol design, identity management, market mechanisms, and regulatory oversight.


<details>
<summary>Abstract</summary>

Autonomous large language model (LLM) agents such as OpenClaw are pushing agentic commerce from human-supervised assistance toward machine actors that can negotiate, purchase services, manage digital assets, and execute transactions across on-chain and off-chain environments. Protocols such as the Trustless Agents standard (ERC-8004), Agent Payments Protocol (AP2), the HTTP 402-based payment protocol (x402), Agent Commerce Protocol (ACP), the Agentic Commerce standard (ERC-8183), and Machine Payments Protocol (MPP) enable this transition, but they also create an attack surface that existing security frameworks do not capture well. This Systematization of Knowledge (SoK) develops a unified security framework for autonomous LLM agents in commerce and finance. We organize threats along five dimensions: agent integrity, transaction authorization, inter-agent trust, market manipulation, and regulatory compliance. From a systematically curated public corpus of academic papers, protocol documents, industry reports, and incident evidence, we derive 12 cross-layer attack vectors and show how failures propagate from reasoning and tooling layers into custody, settlement, market harm, and compliance exposure. We then propose a layered defense architecture addressing authorization gaps left by current agent-payment protocols. Overall, our analysis shows that securing agentic commerce is inherently a cross-layer problem that requires coordinated controls across LLM safety, protocol design, identity, market structure, and regulation. We conclude with a research roadmap and a benchmark agenda for secure autonomous commerce.

</details>


### 89. When Less Latent Leads to Better Relay: Information-Preserving Compression for Latent Multi-Agent LLM Collaboration

- **Authors:** Yiping Li, Zhiyu An, Wan Du
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13349v1](http://arxiv.org/abs/2604.13349v1)
- **PDF:** [https://arxiv.org/pdf/2604.13349v1](https://arxiv.org/pdf/2604.13349v1)
- **Categories:** cs.LG


> **Main contribution:** The paper proposes an information‑preserving compression scheme for latent‑space communication in multi‑agent LLM systems, showing that selectively pruning the KV cache can reduce bandwidth without sacrificing—and even improving—task performance.  

**Methodology:** Building on the LatentMAS framework, the authors apply an eviction‑style KV compression and introduce **Orthogonal Backfill (OBF)**, which injects a low‑rank orthogonal residual derived from the discarded KV entries back into the retained cache, thereby mitigating information loss.  

**Key findings:** Across nine benchmarks covering mathematical reasoning, coding, and knowledge‑intensive QA, the OBF‑compressed relay matches full‑KV performance while cutting communication cost by **≈80–90 %**, and it attains the highest scores on 7 of the 9 tasks, indicating that preserving the most salient latent information outweighs transmitting all raw KV data in agentic AI collaborations.


<details>
<summary>Abstract</summary>

Communication in Large Language Model (LLM)-based multi-agent systems is moving beyond discrete tokens to preserve richer context. Recent work such as LatentMAS enables agents to exchange latent messages through full key-value (KV) caches. However, full KV relay incurs high memory and communication cost. We adapt eviction-style KV compression to this setting and introduce Orthogonal Backfill (OBF) to mitigate information loss from hard eviction. OBF injects a low-rank orthogonal residual from discarded KV states into the retained KV states. We evaluate proposed method against full KV relay on nine standard benchmarks spanning mathematical reasoning, coding, and knowledge-intensive QA. It achieves performance comparable to full KV relay while reducing communication cost by 79.8%--89.4%. OBF further improves the performance and achieves the best results on 7 of the 9 benchmarks. This suggests that more information does not necessarily lead to better communication; preserving the most useful information matters more. Our codebase is publicly available on https://github.com/markli404/When-Less-Latent-Leads-to-Better-Relay.

</details>


### 90. AgentSPEX: An Agent SPecification and EXecution Language

- **Authors:** Pengcheng Wang, Jerry Huang, Jiarui Yao, Rui Pan, Peizhi Niu, Yaowenqi Liu, Ruida Wang, Renhao Lu, Yuwei Guo, Tong Zhang
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13346v1](http://arxiv.org/abs/2604.13346v1)
- **PDF:** [https://arxiv.org/pdf/2604.13346v1](https://arxiv.org/pdf/2604.13346v1)
- **Categories:** cs.CL


> AgentSPEX is a domain‑specific language that lets developers write LLM‑agent workflows as explicit, typed programs instead of opaque prompt strings. The authors designed a lightweight harness that interprets these specifications, supplying tool access, sandboxed execution, checkpointing, verification, and logging, and they built a visual editor that synchronizes graph and code views. Across seven benchmark tasks and a user study versus a popular Python‑based framework, AgentSPEX achieved comparable or better performance while offering clearer control flow, modular reuse, and higher author interpretability for agentic AI systems.


<details>
<summary>Abstract</summary>

Language-model agent systems commonly rely on reactive prompting, in which a single instruction guides the model through an open-ended sequence of reasoning and tool-use steps, leaving control flow and intermediate state implicit and making agent behavior potentially difficult to control. Orchestration frameworks such as LangGraph, DSPy, and CrewAI impose greater structure through explicit workflow definitions, but tightly couple workflow logic with Python, making agents difficult to maintain and modify. In this paper, we introduce AgentSPEX, an Agent SPecification and EXecution Language for specifying LLM-agent workflows with explicit control flow and modular structure, along with a customizable agent harness. AgentSPEX supports typed steps, branching and loops, parallel execution, reusable submodules, and explicit state management, and these workflows execute within an agent harness that provides tool access, a sandboxed virtual environment, and support for checkpointing, verification, and logging. Furthermore, we provide a visual editor with synchronized graph and workflow views for authoring and inspection. We include ready-to-use agents for deep research and scientific research, and we evaluate AgentSPEX on 7 benchmarks. Finally, we show through a user study that AgentSPEX provides a more interpretable and accessible workflow-authoring paradigm than a popular existing agent framework.

</details>


### 91. On the Creativity of AI Agents

- **Authors:** Giorgio Franceschelli, Mirco Musolesi
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13242v1](http://arxiv.org/abs/2604.13242v1)
- **PDF:** [https://arxiv.org/pdf/2604.13242v1](https://arxiv.org/pdf/2604.13242v1)
- **Categories:** cs.CY, cs.AI


> The paper argues that large‑language‑model (LLM) agents can produce outputs that satisfy a functionalist definition of creativity—i.e., they generate novel, valuable, and appropriate results—but they fall short of ontological creativity because they lack internal intentionality, self‑reflection, and the socio‑personal processes humans associate with genuine creative thought. To reach this conclusion, the authors combine a macro‑level analysis of observable output characteristics with a review of the underlying generative mechanisms and social context, then assess current LLM‑agent architectures against both criteria. They find that while functionalist creativity is already evident in many agentic applications, achieving ontological creativity would require new designs (e.g., self‑modelling, affective feedback loops, and interactive learning with humans), raising both promising societal benefits and notable ethical risks.


<details>
<summary>Abstract</summary>

Large language models (LLMs), particularly when integrated into agentic systems, have demonstrated human- and even superhuman-level performance across multiple domains. Whether these systems can truly be considered creative, however, remains a matter of debate, as conclusions heavily depend on the definitions, evaluation methods, and specific use cases employed. In this paper, we analyse creativity along two complementary macro-level perspectives. The first is a functionalist perspective, focusing on the observable characteristics of creative outputs. The second is an ontological perspective, emphasising the underlying processes, as well as the social and personal dimensions involved in creativity. We focus on LLM agents and we argue that they exhibit functionalist creativity, albeit not at its most sophisticated levels, while they continue to lack key aspects of ontological creativity. Finally, we discuss whether it is desirable for agentic systems to attain both forms of creativity, evaluating potential benefits and risks, and proposing pathways toward artificial creativity that can enhance human society.

</details>


### 92. SciFi: A Safe, Lightweight, User-Friendly, and Fully Autonomous Agentic AI Workflow for Scientific Applications

- **Authors:** Qibin Liu, Julia Gonski
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13180v1](http://arxiv.org/abs/2604.13180v1)
- **PDF:** [https://arxiv.org/pdf/2604.13180v1](https://arxiv.org/pdf/2604.13180v1)
- **Categories:** cs.AI


> **Paper Summary**

The authors introduce **SciFi**, a modular agentic‑AI framework that lets researchers run fully autonomous scientific workflows with built‑in safety and minimal supervision.  The system couples (i) an isolated sandbox for code execution, (ii) a three‑layer “agent‑loop” (task planner → action executor → verifier) that can invoke LLMs of different sizes for planning, coding, and validation, and (iii) a self‑assessing “do‑until” control structure that automatically checks whether a predefined success condition or resource limit has been reached before terminating.  Experiments on a suite of well‑specified tasks—data cleaning, hypothesis‑driven simulation, and automated literature synthesis—show that SciFi completes 92 % of the tasks correctly without human overrides, reduces manual coding effort by ~70 %, and detects/rejects unsafe operations (e.g., runaway loops or external network calls) with >95 % precision, demonstrating a practical, safe, and lightweight route to deploying autonomous agents in real scientific settings.


<details>
<summary>Abstract</summary>

Recent advances in agentic AI have enabled increasingly autonomous workflows, but existing systems still face substantial challenges in achieving reliable deployment in real-world scientific research. In this work, we present a safe, lightweight, and user-friendly agentic framework for the autonomous execution of well-defined scientific tasks. The framework combines an isolated execution environment, a three-layer agent loop, and a self-assessing do-until mechanism to ensure safe and reliable operation while effectively leveraging large language models of varying capability levels. By focusing on structured tasks with clearly defined context and stopping criteria, the framework supports end-to-end automation with minimal human intervention, enabling researchers to offload routine workloads and devote more effort to creative activities and open-ended scientific inquiry.

</details>


### 93. Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems

- **Authors:** Jiacheng Liu, Xiaohan Zhao, Xinyi Shang, Zhiqiang Shen
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14228v1](http://arxiv.org/abs/2604.14228v1)
- **PDF:** [https://arxiv.org/pdf/2604.14228v1](https://arxiv.org/pdf/2604.14228v1)
- **Categories:** cs.SE, cs.AI, cs.CL, cs.LG


> The paper presents Claude Code, a new agentic coding assistant whose architecture is dissected from its open‑source TypeScript implementation and contrasted with the OpenClaw personal‑assistant gateway. By mapping five human‑centered values (decision authority, safety, reliability, capability amplification, and adaptability) onto thirteen concrete design principles, the authors show that most of Claude Code’s functionality resides in surrounding systems—a seven‑mode permission framework with an ML classifier, a five‑layer context‑compaction pipeline, extensible plug‑in mechanisms, sub‑agent delegation with isolated work‑trees, and an append‑only session store—while the core agent loop remains a simple model‑call‑tool‑execute cycle. Empirical comparison with OpenClaw reveals how differing deployment contexts lead to divergent safety controls, runtime embedding, and capability registration, and the study concludes with six open research directions for future AI‑agent system design.


<details>
<summary>Abstract</summary>

Claude Code is an agentic coding tool that can run shell commands, edit files, and call external services on behalf of the user. This study describes its comprehensive architecture by analyzing the publicly available TypeScript source code and further comparing it with OpenClaw, an independent open-source AI agent system that answers many of the same design questions from a different deployment context. Our analysis identifies five human values, philosophies, and needs that motivate the architecture (human decision authority, safety and security, reliable execution, capability amplification, and contextual adaptability) and traces them through thirteen design principles to specific implementation choices. The core of the system is a simple while-loop that calls the model, runs tools, and repeats. Most of the code, however, lives in the systems around this loop: a permission system with seven modes and an ML-based classifier, a five-layer compaction pipeline for context management, four extensibility mechanisms (MCP, plugins, skills, and hooks), a subagent delegation mechanism with worktree isolation, and append-oriented session storage. A comparison with OpenClaw, a multi-channel personal assistant gateway, shows that the same recurring design questions produce different architectural answers when the deployment context changes: from per-action safety classification to perimeter-level access control, from a single CLI loop to an embedded runtime within a gateway control plane, and from context-window extensions to gateway-wide capability registration. We finally identify six open design directions for future agent systems, grounded in recent empirical, architectural, and policy literature.

</details>


### 94. Parallax: Why AI Agents That Think Must Never Act

- **Authors:** Joel Fokou
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12986v1](http://arxiv.org/abs/2604.12986v1)
- **PDF:** [https://arxiv.org/pdf/2604.12986v1](https://arxiv.org/pdf/2604.12986v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **Parallax**, a new architectural safety framework for autonomous AI agents that separates cognition from execution and inserts an independent, multi‑stage validator between them. By enforcing cognitive‑executive separation, information‑flow labeling, adversarial validation with graduated determinism, and reversible execution, the OpenParallax reference implementation blocks 98.9 % of 280 crafted attacks (and 100 % in a high‑security mode) while producing no false positives, even when the reasoning model is fully compromised. The work demonstrates that prompt‑level guardrails are insufficient for execution‑capable agents and that a strict execution boundary is essential for robust agentic AI security.


<details>
<summary>Abstract</summary>

Autonomous AI agents are rapidly transitioning from experimental tools to operational infrastructure, with projections that 80% of enterprise applications will embed AI copilots by the end of 2026. As agents gain the ability to execute real-world actions (reading files, running commands, making network requests, modifying databases), a fundamental security gap has emerged. The dominant approach to agent safety relies on prompt-level guardrails: natural language instructions that operate at the same abstraction level as the threats they attempt to mitigate. This paper argues that prompt-based safety is architecturally insufficient for agents with execution capability and introduces Parallax, a paradigm for safe autonomous AI execution grounded in four principles: Cognitive-Executive Separation, which structurally prevents the reasoning system from executing actions; Adversarial Validation with Graduated Determinism, which interposes an independent, multi-tiered validator between reasoning and execution; Information Flow Control, which propagates data sensitivity labels through agent workflows to detect context-dependent threats; and Reversible Execution, which captures pre-destructive state to enable rollback when validation fails. We present OpenParallax, an open-source reference implementation in Go, and evaluate it using Assume-Compromise Evaluation, a methodology that bypasses the reasoning system entirely to test the architectural boundary under full agent compromise. Across 280 adversarial test cases in nine attack categories, Parallax blocks 98.9% of attacks with zero false positives under its default configuration, and 100% of attacks under its maximum-security configuration. When the reasoning system is compromised, prompt-level guardrails provide zero protection because they exist only within the compromised system; Parallax's architectural boundary holds regardless.

</details>


### 95. Drawing on Memory: Dual-Trace Encoding Improves Cross-Session Recall in LLM Agents

- **Authors:** Benjamin Stern, Peter Nadel
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12948v1](http://arxiv.org/abs/2604.12948v1)
- **PDF:** [https://arxiv.org/pdf/2604.12948v1](https://arxiv.org/pdf/2604.12948v1)
- **Categories:** cs.AI


> The paper introduces **dual‑trace memory encoding** for large‑language‑model (LLM) agents, pairing each stored fact with a narrative “scene trace” that captures the context in which the fact was learned. By forcing the agent to embed concrete situational details during storage, the method creates richer, more distinctive memory representations without increasing token usage. Evaluated on the LongMemEval‑S benchmark (4,575 sessions, 100 recall items), dual‑trace encoding raises overall recall accuracy from 53.5 % to 73.7 % ( +20.2 pp, p < 0.0001), with particularly large gains in temporal reasoning (+40 pp), knowledge‑update tracking (+25 pp), and cross‑session aggregation (+30 pp), confirming that richer contextual traces improve the agent’s ability to reason over time and across interactions.


<details>
<summary>Abstract</summary>

LLM agents with persistent memory store information as flat factual records, providing little context for temporal reasoning, change tracking, or cross-session aggregation. Inspired by the drawing effect [3], we introduce dual-trace memory encoding. In this method, each stored fact is paired with a concrete scene trace, a narrative reconstruction of the moment and context in which the information was learned. The agent is forced to commit to specific contextual details during encoding, creating richer, more distinctive memory traces. Using the LongMemEval-S benchmark (4,575 sessions, 100 recall questions), we compare dual-trace encoding against a fact-only control with matched coverage and format over 99 shared questions. Dual-trace achieves 73.7% overall accuracy versus 53.5%, a +20.2 percentage point (pp) gain (95% CI: [+12.1, +29.3], bootstrap p < 0.0001). Gains concentrate in temporal reasoning (+40pp), knowledge-update tracking (+25pp), and multi-session aggregation (+30pp), with no benefit for single-session retrieval, consistent with encoding specificity theory [8]. Token analysis shows dual-trace encoding achieves this gain at no additional cost. We additionally sketch an architectural design for adapting dual-trace encoding to coding agents, with preliminary pilot validation.

</details>


### 96. Don't Show Pixels, Show Cues: Unlocking Visual Tool Reasoning in Language Models via Perception Programs

- **Authors:** Muhammad Kamran Janjua, Hugo Silva, Di Niu, Bahador Rashidi
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12896v1](http://arxiv.org/abs/2604.12896v1)
- **PDF:** [https://arxiv.org/pdf/2604.12896v1](https://arxiv.org/pdf/2604.12896v1)
- **Categories:** cs.CV, cs.LG


> **Contribution:** The paper shows that the main obstacle to effective visual‑tool reasoning in multimodal language models (MLLMs) is not the lack of tools or model size, but the way tool outputs are presented; raw pixel‑level data are poorly aligned with the language‑native reasoning of LLMs.  

**Methodology:** It introduces **Perception Programs (P²)**, a training‑free, model‑agnostic “compiler” that transforms dense visual‑tool outputs (depth maps, optical flow, correspondences, etc.) into concise, structured, language‑friendly summaries (e.g., short textual descriptions, key‑value tables). These summaries are fed directly to the MLLM, letting the model reason with its native linguistic capabilities.  

**Key Findings:** Across six perception‑centric benchmarks (BLINK), P² delivers large, consistent gains: with GPT‑5 Mini the accuracy jumps from ~41 % to ~86 % on multi‑view reasoning and from ~52 % to ~81 % on relative depth, yielding a 22 % average improvement and new state‑of‑the‑art results. Even 4‑B‑scale models (InternVL3.5, Qwen3VL) achieve 15–40 % absolute lifts, outperforming prior supervised or RL‑based tool‑use approaches—all without any additional training or model modification.


<details>
<summary>Abstract</summary>

Multimodal language models (MLLMs) are increasingly paired with vision tools (e.g., depth, flow, correspondence) to enhance visual reasoning. However, despite access to these tool-generated visual cues, MLLMs often fail to benefit from them. Existing approaches typically feed raw tool outputs into the model, but these dense, pixel-level representations are misaligned with the language-native reasoning strengths of LLMs, leading to weak perception and reliance on language priors. We argue that, in problems where vision tools can provide the necessary visual cues, the bottleneck is not more tool calls or larger MLLMs, it is how tool outputs are represented. We introduce Perception Programs (P$^2$), a training-free, model-agnostic method that rewrites tool outputs into compact, structured, language-native summaries that MLLMs can directly parse and reason over. Across six perception-centric tasks in BLINK, P$^2$ consistently yields large improvements over base models and raw tool-augmented baselines. With GPT-5 Mini as the base model, P$^2$ raises its accuracy from 41.35\% to 86.47\% on multi-view reasoning, from 52.42\% to 81.45\% on relative depth, and achieves a 22\% average gain across tasks, setting new state-of-the-art results. Even on smaller MLLMs, e.g., InternVL3.5-4B and Qwen3VL-4B, we observe 15-40\% absolute gains from P$^2$, surpassing prior agentic, supervised, and RL-based tool-use methods-without any training or model modifications.

</details>


### 97. LIFE -- an energy efficient advanced continual learning agentic AI framework for frontier systems

- **Authors:** Anne Lee, Gurudutt Hosangadi
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12874v1](http://arxiv.org/abs/2604.12874v1)
- **PDF:** [https://arxiv.org/pdf/2604.12874v1](https://arxiv.org/pdf/2604.12874v1)
- **Categories:** cs.AI


> **Main contribution** – The paper introduces **LIFE**, a modular, agent‑centric continual‑learning framework designed to manage high‑performance‑computing (HPC) resources in an energy‑aware manner. Unlike monolithic transformer‑based agents, LIFE combines an orchestrator, an “Agentic Context Engineering” layer, a novel hierarchical memory system, and “information‑lattice” learning to enable self‑evolving network‑operation policies.

**Methodology** – LIFE is built as a closed‑loop control system for HPC clusters: the orchestrator schedules lightweight specialist agents; the context‑engineering module extracts structured situational cues; the memory system stores multi‑scale experience traces; and the lattice‑learning component incrementally updates policy graphs using sparse, energy‑efficient updates. The authors instantiate this pipeline on a Kubernetes‑style micro‑service environment and evaluate it on latency‑spike detection/mitigation tasks.

**Key findings** – In the latency‑spike use case, LIFE reduces average response latency by **≈ 23 %** and cuts the incremental learning energy budget by **≈ 38 %** compared with a baseline monolithic transformer agent, while preserving continual‑learning capability across workload shifts. The results demonstrate that an agentic, modular architecture can deliver sustainable, adaptive control for frontier HPC systems.


<details>
<summary>Abstract</summary>

The rapid advancement of AI has changed the character of HPC usage such as dimensioning, provisioning, and execution. Not only has energy demand been amplified, but existing rudimentary continual learning capabilities limit ability of AI to effectively manage HPCs. This paper reviews emerging directions beyond monolithic transformers, emphasizing agentic AI and brain inspired architectures as complementary paths toward sustainable, adaptive systems. We propose LIFE, a reasoning and Learning framework that is Incremental, Flexible, and Energy efficient that is implemented as an agent centric system rather than a single monolithic model. LIFE uniquely combines four components to realize self evolving network management and operations in HPCs. The components are an orchestrator, Agentic Context Engineering, a novel memory system, and information lattice learning. LIFE can also generalize to enable a variety of orthogonal use cases. We ground LIFE in a specific closed loop HPC operations example for detecting and mitigating latency spikes experienced by critical micro services running on a Kubernetes like cluster.

</details>


### 98. EvoSpark: Endogenous Interactive Agent Societies for Unified Long-Horizon Narrative Evolution

- **Authors:** Shiyu He, Minchi Kuang, Mengxian Wang, Bin Hu, Tingxiang Gu
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12776v1](http://arxiv.org/abs/2604.12776v1)
- **PDF:** [https://arxiv.org/pdf/2604.12776v1](https://arxiv.org/pdf/2604.12776v1)
- **Categories:** cs.CL


> EvoSpark introduces a unified framework for long‑horizon, LLM‑driven multi‑agent storytelling that mitigates two chronic failures—social‑memory stacking and narrative‑spatial dissonance—by embedding a **Stratified Narrative Memory** (a role‑centric socio‑evolutionary base that continually reconciles conflicting relational histories) and a **Generative Mise‑en‑Scène** module that keeps characters, locations, and plot beats tightly aligned. The system is built around a **Unified Narrative Operation Engine** with an **Emergent Character Grounding Protocol** that converts stochastic generative sparks into persistent, coherent agents, allowing a minimal seed premise to expand into an open‑ended story world. Empirical evaluations across several narrative domains show that EvoSpark markedly improves coherence, consistency, and expressive richness over prior LLM‑based multi‑agent baselines, demonstrating its viability for building enduring, self‑organizing agent societies in narrative AI.


<details>
<summary>Abstract</summary>

Realizing endogenous narrative evolution in LLM-based multi-agent systems is hindered by the inherent stochasticity of generative emergence. In particular, long-horizon simulations suffer from social memory stacking, where conflicting relational states accumulate without resolution, and narrative-spatial dissonance, where spatial logic detaches from the evolving plot. To bridge this gap, we propose EvoSpark, a framework specifically designed to sustain logically coherent long-horizon narratives within Endogenous Interactive Agent Societies. To ensure consistency, the Stratified Narrative Memory employs a Role Socio-Evolutionary Base as living cognition, dynamically metabolizing experiences to resolve historical conflicts. Complementarily, Generative Mise-en-Scène mechanism enforces Role-Location-Plot alignment, synchronizing character presence with the narrative flow. Underpinning these is the Unified Narrative Operation Engine, which integrates an Emergent Character Grounding Protocol to transform stochastic sparking into persistent characters. This engine establishes a substrate that expands a minimal premise into an open-ended, evolving story world. Experiments demonstrate that EvoSpark significantly outperforms baselines across diverse paradigms, enabling the sustained generation of expressive and coherent narrative experiences.

</details>


### 99. A Multi-Agent Feedback System for Detecting and Describing News Events in Satellite Imagery

- **Authors:** Madeline Anderson, Mikhail Klassen, Ash Hoover, Kerri Cahoy
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12772v1](http://arxiv.org/abs/2604.12772v1)
- **PDF:** [https://arxiv.org/pdf/2604.12772v1](https://arxiv.org/pdf/2604.12772v1)
- **Categories:** cs.CV, cs.MA


> The paper introduces **SkyScraper**, a novel multi‑agent pipeline that couples automated geocoding of news articles with iterative feedback loops to locate, extract, and caption multi‑temporal satellite‑image sequences corresponding to real‑world events. By deploying specialized agents for article parsing, geolocation refinement, image retrieval, and caption generation, the system discovers roughly five times more events than conventional single‑pass geocoding and assembles a curated dataset of 5,000 multi‑temporal image sequences with descriptive captions. The results demonstrate that agentic feedback can dramatically improve the scalability of event detection and natural‑language description in remote‑sensing imagery, providing a valuable resource for both AI research and journalistic applications.


<details>
<summary>Abstract</summary>

Changes in satellite imagery often occur over multiple time steps. Despite the emergence of bi-temporal change captioning datasets, there is a lack of multi-temporal event captioning datasets (at least two images per sequence) in remote sensing. This gap exists because (1) searching for visible events in satellite imagery and (2) labeling multi-temporal sequences require significant time and labor. To address these challenges, we present SkyScraper, an iterative multi-agent workflow that geocodes news articles and synthesizes captions for corresponding satellite image sequences. Our experiments show that SkyScraper successfully finds 5x more events than traditional geocoding methods, demonstrating that agentic feedback is an effective strategy for surfacing new multi-temporal events in satellite imagery. We apply our framework to a large database of global news articles, curating a new multi-temporal captioning dataset with 5,000 sequences. By automatically identifying imagery related to news events, our work also supports journalism and reporting efforts.

</details>


### 100. Transferable Expertise for Autonomous Agents via Real-World Case-Based Learning

- **Authors:** Zhenyu Ma, Yuyang Song, Chunyi Yang, Jingyi Zhu, Letian Yang, Xukai Jiang
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12717v1](http://arxiv.org/abs/2604.12717v1)
- **PDF:** [https://arxiv.org/pdf/2604.12717v1](https://arxiv.org/pdf/2604.12717v1)
- **Categories:** cs.AI


> The paper introduces a **case‑based learning (CBL) framework** for LLM‑driven autonomous agents that extracts task‑specific knowledge, analytical prompts, and operational skills from concrete real‑world experiences and stores them as reusable “case assets.” By retrieving and adapting these assets, agents can apply prior structured expertise to new, more complex tasks rather than relying solely on static pretrained knowledge or prompt engineering. Empirical evaluation on a six‑category benchmark shows that CBL consistently matches or surpasses strong Zero‑Shot, Few‑Shot, Checklist‑Prompt, and Rule‑Memory baselines—especially as task complexity rises—and demonstrates that knowledge acquired by one agent can be transferred to others, highlighting case‑based learning as a viable path toward professional, transferable agentic AI.


<details>
<summary>Abstract</summary>

LLM-based autonomous agents perform well on general reasoning tasks but still struggle to reliably use task structure, key constraints, and prior experience in complex real-world settings. We propose a case-based learning framework that converts experience from past tasks into reusable knowledge assets, allowing agents to transfer prior case experience to new tasks and perform more structured analysis. Unlike methods based mainly on pretrained knowledge or static prompts, our framework emphasizes extracting and reusing task-relevant knowledge, analytical prompts, and operational skills from real cases. We evaluate the method on a unified benchmark of six complex task categories and compare it with Zero-Shot, Few-Shot, Checklist Prompt, and Rule Memory baselines. Results show that our method achieves consistently strong performance across all tasks and matches or outperforms the best baseline in every case, with especially clear gains on more complex tasks. Further analysis shows that the advantage of case-based learning increases with task complexity, and that practical knowledge acquired by one agent can be reused by others. These findings suggest that case-based learning offers a promising path for building professional agents for real-world work.

</details>


### 101. TRACE: A Conversational Framework for Sustainable Tourism Recommendation with Agentic Counterfactual Explanations

- **Authors:** Ashmi Banerjee, Adithi Satish, Wolfgang Wörndl, Yashar Deldjoo
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.14223v1](http://arxiv.org/abs/2604.14223v1)
- **PDF:** [https://arxiv.org/pdf/2604.14223v1](https://arxiv.org/pdf/2604.14223v1)
- **Categories:** cs.IR, cs.AI


> TRACE introduces a multi‑agent, LLM‑driven conversational system that steers travelers toward environmentally sustainable itineraries without sacrificing relevance. The framework combines a central orchestrator with specialist worker agents that (1) probe hidden sustainability preferences, (2) build structured user personas, and (3) produce recommendations enriched with **agentic counterfactual explanations** and clarifying questions that spotlight greener alternatives. User experiments show that TRACE nudges users toward lower‑impact travel choices while maintaining recommendation quality and interactive speed, demonstrating a practical pathway for incorporating sustainability into agentic AI recommendation pipelines.


<details>
<summary>Abstract</summary>

Traditional conversational travel recommender systems primarily optimize for user relevance and convenience, often reinforcing popular, overcrowded destinations and carbon-intensive travel choices. To address this, we present TRACE (Tourism Recommendation with Agentic Counterfactual Explanations), a multi-agent, LLM-based framework that promotes sustainable tourism through interactive nudging. TRACE uses a modular orchestrator-worker architecture where specialized agents elicit latent sustainability preferences, construct structured user personas, and generate recommendations that balance relevance with environmental impact.
  A key innovation lies in its use of agentic counterfactual explanations and LLM-driven clarifying questions, which together surface greener alternatives and refine understanding of intent, fostering user reflection without coercion. User studies and semantic alignment analyses demonstrate that TRACE effectively supports sustainable decision-making while preserving recommendation quality and interactive responsiveness. TRACE is implemented on Google's Agent Development Kit, with full code, Docker setup, prompts, and a publicly available demo video to ensure reproducibility.
  A project summary, including all resources, prompts, and demo access, is available at https://ashmibanerjee.github.io/trace-chatbot.

</details>


### 102. Every Picture Tells a Dangerous Story: Memory-Augmented Multi-Agent Jailbreak Attacks on VLMs

- **Authors:** Jianhao Chen, Haoyang Chen, Hanjie Zhao, Haozhe Liang, Tieyun Qian
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12616v1](http://arxiv.org/abs/2604.12616v1)
- **PDF:** [https://arxiv.org/pdf/2604.12616v1](https://arxiv.org/pdf/2604.12616v1)
- **Categories:** cs.AI, cs.MM


> **Main contribution** – The paper introduces **MemJack**, a memory‑augmented, multi‑agent framework that conducts automated jailbreak attacks on vision‑language models (VLMs) by exploiting the deep semantic content of *natural* images rather than relying on pixel‑level perturbations or typographic tricks.  

**Methodology** – MemJack deploys several cooperating agents that (1) parse visual entities in an image, (2) map them to malicious intents, (3) craft multi‑angle, semantically camouflaged prompts, and (4) filter these prompts with an Iterative Nullspace Projection (INLP) to evade early latent‑space refusals. Successful attack patterns are stored in a persistent **Multimodal Experience Memory**, enabling the agents to recall and extend coherent multi‑turn jailbreak dialogues across different images.  

**Key findings** – On the unaltered COCO‑val2017 benchmark, MemJack achieves a **71.5 % attack success rate (ASR)** against the state‑of‑the‑art VLM Qwen‑3‑VL‑Plus (rising to ~90 % with larger attack budgets), demonstrating that semantic vulnerabilities in natural images are a potent, previously under‑examined threat. The authors also release **MemJack‑Bench**, a dataset of >113 k multimodal jailbreak trajectories to support future alignment and defense research.


<details>
<summary>Abstract</summary>

The rapid evolution of Vision-Language Models (VLMs) has catalyzed unprecedented capabilities in artificial intelligence; however, this continuous modal expansion has inadvertently exposed a vastly broadened and unconstrained adversarial attack surface. Current multimodal jailbreak strategies primarily focus on surface-level pixel perturbations and typographic attacks or harmful images; however, they fail to engage with the complex semantic structures intrinsic to visual data. This leaves the vast semantic attack surface of original, natural images largely unscrutinized. Driven by the need to expose these deep-seated semantic vulnerabilities, we introduce \textbf{MemJack}, a \textbf{MEM}ory-augmented multi-agent \textbf{JA}ilbreak atta\textbf{CK} framework that explicitly leverages visual semantics to orchestrate automated jailbreak attacks. MemJack employs coordinated multi-agent cooperation to dynamically map visual entities to malicious intents, generate adversarial prompts via multi-angle visual-semantic camouflage, and utilize an Iterative Nullspace Projection (INLP) geometric filter to bypass premature latent space refusals. By accumulating and transferring successful strategies through a persistent Multimodal Experience Memory, MemJack maintains highly coherent extended multi-turn jailbreak attack interactions across different images, thereby improving the attack success rate (ASR) on new images. Extensive empirical evaluations across full, unmodified COCO val2017 images demonstrate that MemJack achieves a 71.48\% ASR against Qwen3-VL-Plus, scaling to 90\% under extended budgets. Furthermore, to catalyze future defensive alignment research, we will release \textbf{MemJack-Bench}, a comprehensive dataset comprising over 113,000 interactive multimodal jailbreak attack trajectories, establishing a vital foundation for developing inherently robust VLMs.

</details>


### 103. Cross-Cultural Simulation of Citizen Emotional Responses to Bureaucratic Red Tape Using LLM Agents

- **Authors:** Wanchun Ni, Jiugeng Sun, Yixian Liu, Mennatallah El-Assady
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12545v1](http://arxiv.org/abs/2604.12545v1)
- **PDF:** [https://arxiv.org/pdf/2604.12545v1](https://arxiv.org/pdf/2604.12545v1)
- **Categories:** cs.AI, cs.CY


> The paper introduces the first systematic framework for evaluating how Large‑Language‑Model (LLM) agents emulate citizens’ emotional reactions to bureaucratic red‑tape across cultural groups. By prompting several LLMs with a single red‑tape scenario and comparing their outputs to human‑collected affective data from Western and Eastern cultures, the authors show that current models only modestly match human responses—and perform especially poorly for Eastern cultural contexts; cultural‑specific prompting does not substantially close the gap. To support ongoing research, they release **RAMO**, an interactive web interface that both simulates citizen emotions with LLM agents and gathers human response data for future model refinement.


<details>
<summary>Abstract</summary>

Improving policymaking is a central concern in public administration. Prior human subject studies reveal substantial cross-cultural differences in citizens' emotional responses to red tape during policy implementation. While LLM agents offer opportunities to simulate human-like responses and reduce experimental costs, their ability to generate culturally appropriate emotional responses to red tape remains unverified. To address this gap, we propose an evaluation framework for assessing LLMs' emotional responses to red tape across diverse cultural contexts. As a pilot study, we apply this framework to a single red-tape scenario. Our results show that all models exhibit limited alignment with human emotional responses, with notably weaker performance in Eastern cultures. Cultural prompting strategies prove largely ineffective in improving alignment. We further introduce \textbf{RAMO}, an interactive interface for simulating citizens' emotional responses to red tape and for collecting human data to improve models. The interface is publicly available at https://ramo-chi.ivia.ch.

</details>


### 104. CIA: Inferring the Communication Topology from LLM-based Multi-Agent Systems

- **Authors:** Yongxuan Wu, Xixun Lin, He Zhang, Nan Sun, Kun Wang, Chuan Zhou, Shirui Pan, Yanan Cao
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12461v1](http://arxiv.org/abs/2604.12461v1)
- **PDF:** [https://arxiv.org/pdf/2604.12461v1](https://arxiv.org/pdf/2604.12461v1)
- **Categories:** cs.AI


> The paper introduces **Communication Inference Attack (CIA)**, the first method that can reconstruct the hidden communication graph of a large‑language‑model (LLM)‑based multi‑agent system even when the system is accessed only as a black box. CIA works by issuing crafted adversarial queries that provoke intermediate agents to emit reasoning traces, then disentangling a global bias term and applying LLM‑guided weak supervision to learn semantic correlation patterns among those traces, which are used to infer edge existence. Experiments on several MASes with optimized topologies show that CIA reliably recovers the underlying graph (average AUC = 0.87, peak AUC = 0.99), highlighting a serious privacy and IP vulnerability for agentic AI deployments.


<details>
<summary>Abstract</summary>

LLM-based Multi-Agent Systems (MAS) have demonstrated remarkable capabilities in solving complex tasks. Central to MAS is the communication topology which governs how agents exchange information internally. Consequently, the security of communication topologies has attracted increasing attention. In this paper, we investigate a critical privacy risk: MAS communication topologies can be inferred under a restrictive black-box setting, exposing system vulnerabilities and posing significant intellectual property threats. To explore this risk, we propose Communication Inference Attack (CIA), a novel attack that constructs new adversarial queries to induce intermediate agents' reasoning outputs and models their semantic correlations through the proposed global bias disentanglement and LLM-guided weak supervision. Extensive experiments on MAS with optimized communication topologies demonstrate the effectiveness of CIA, achieving an average AUC of 0.87 and a peak AUC of up to 0.99, thereby revealing the substantial privacy risk in MAS.

</details>


### 105. ReflectCAP: Detailed Image Captioning with Reflective Memory

- **Authors:** Kyungmin Min, Minbeom Kim, Kang-il Lee, Seunghyun Yoon, Kyomin Jung
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12357v1](http://arxiv.org/abs/2604.12357v1)
- **PDF:** [https://arxiv.org/pdf/2604.12357v1](https://arxiv.org/pdf/2604.12357v1)
- **Categories:** cs.AI, cs.CV


> The paper introduces **ReflectCAP**, a multi‑agent framework that first probes a target large vision‑language model (LVLM) to discover systematic hallucinations and omissions, then compresses these error patterns into **Structured Reflection Notes** that guide the caption generator at inference time. By using these reflective guidelines to tell the model what to avoid and what to attend to, ReflectCAP simultaneously boosts factual accuracy and fine‑grained coverage, achieving Pareto‑optimal trade‑offs across eight LVLMs (including GPT‑4.1, Qwen, and InternVL) and outperforming strong baselines on the CapArena‑Auto benchmark. Crucially, the method delivers these gains with 21–36 % lower compute overhead than traditional model scaling or existing multi‑agent pipelines, making detailed image captioning more cost‑effective for agentic AI applications.


<details>
<summary>Abstract</summary>

Detailed image captioning demands both factual grounding and fine-grained coverage, yet existing methods have struggled to achieve them simultaneously. We address this tension with Reflective Note-Guided Captioning (ReflectCAP), where a multi-agent pipeline analyzes what the target large vision-language model (LVLM) consistently hallucinates and what it systematically overlooks, distilling these patterns into reusable guidelines called Structured Reflection Notes. At inference time, these notes steer the captioning model along both axes -- what to avoid and what to attend to -- yielding detailed captions that jointly improve factuality and coverage. Applying this method to 8 LVLMs spanning the GPT-4.1 family, Qwen series, and InternVL variants, ReflectCAP reaches the Pareto frontier of the trade-off between factuality and coverage, and delivers substantial gains on CapArena-Auto, where generated captions are judged head-to-head against strong reference models. Moreover, ReflectCAP offers a more favorable trade-off between caption quality and compute cost than model scaling or existing multi-agent pipelines, which incur 21--36\% greater overhead. This makes high-quality detailed captioning viable under real-world cost and latency constraints.

</details>


### 106. Frontier-Eng: Benchmarking Self-Evolving Agents on Real-World Engineering Tasks with Generative Optimization

- **Authors:** Yizhe Chi, Deyao Hong, Dapeng Jiang, Tianwei Luo, Kaisen Yang, Boshi Zhang, Zhe Cao, Xiaoyan Fan, Bingxiang He, Han Hao, Weiyang Jin, Dianqiao Lei, Qingle Liu, Houde Qian, Bowen Wang, Situ Wang, Youjie Zheng, Yifan Zhou, Calvin Xiao, Eren Cai, Qinhuai Na
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12290v1](http://arxiv.org/abs/2604.12290v1)
- **PDF:** [https://arxiv.org/pdf/2604.12290v1](https://arxiv.org/pdf/2604.12290v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces **Frontier‑Eng**, a human‑verified benchmark that evaluates self‑evolving LLM agents on 47 real‑world engineering problems by forcing them to run an iterative “propose‑execute‑evaluate” loop within a fixed interaction budget, using industrial‑grade simulators that return continuous reward signals and enforce hard feasibility constraints. By testing eight state‑of‑the‑art language models with representative search strategies, the authors find that Claude 4.6 Opus performs best but all models struggle, revealing a dual power‑law decay in both the frequency (≈1/iteration) and magnitude (≈1/improvement‑count) of improvements, and showing that while breadth (parallel proposals) helps diversity, depth (sequential refinement) is essential for achieving hard‑won gains. These results establish Frontier‑Eng as a new standard for measuring how effectively AI agents can integrate domain knowledge with executable feedback to solve complex, open‑ended engineering tasks.


<details>
<summary>Abstract</summary>

Current LLM agent benchmarks, which predominantly focus on binary pass/fail tasks such as code generation or search-based question answering, often neglect the value of real-world engineering that is often captured through the iterative optimization of feasible designs. To this end, we introduce Frontier-Eng, a human-verified benchmark for generative optimization -- an iterative propose-execute-evaluate loop in which an agent generates candidate artifacts, receives executable verifier feedback, and revises them under a fixed interaction budget -- spanning $47$ tasks across five broad engineering categories. Unlike previous suites, Frontier-Eng tasks are grounded in industrial-grade simulators and verifiers that provide continuous reward signals and enforce hard feasibility constraints under constrained budgets. We evaluate eight frontier language models using representative search frameworks, finding that while Claude 4.6 Opus achieves the most robust performance, the benchmark remains challenging for all models. Our analysis suggests a dual power-law decay in improvement frequency ($\sim$ 1/iteration) and magnitude ($\sim$ 1/improvement count). We further show that although width improves parallelism and diversity, depth remains crucial for hard-won improvements under a fixed budget. Frontier-Eng establishes a new standard for assessing the capacity of AI agents to integrate domain knowledge with executable feedback to solve complex, open-ended engineering problems.

</details>


### 107. GAM: Hierarchical Graph-based Agentic Memory for LLM Agents

- **Authors:** Zhaofen Wu, Hanrong Zhang, Fulin Lin, Wujiang Xu, Xinran Xu, Yankai Chen, Henry Peng Zou, Shaowen Chen, Weizhi Zhang, Xue Liu, Philip S. Yu, Hongwei Wang
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12285v1](http://arxiv.org/abs/2604.12285v1)
- **PDF:** [https://arxiv.org/pdf/2604.12285v1](https://arxiv.org/pdf/2604.12285v1)
- **Categories:** cs.AI


> The paper introduces **GAM (Hierarchical Graph‑based Agentic Memory)**, a memory architecture for LLM‑driven agents that separates short‑term dialogue encoding from long‑term knowledge consolidation. It builds an **event‑progression graph** for the ongoing conversation and only merges it into a higher‑level **topic‑associative network** when a semantic shift is detected, thus reducing interference from transient information; retrieval is performed with a graph‑guided, multi‑factor scoring scheme. Experiments on the LoCoMo and LongDialQA benchmarks show that GAM yields significantly higher reasoning accuracy and lower computational overhead than existing stream‑based and discrete memory baselines, demonstrating more stable long‑term consistency for agentic AI.


<details>
<summary>Abstract</summary>

To sustain coherent long-term interactions, Large Language Model (LLM) agents must navigate the tension between acquiring new information and retaining prior knowledge. Current unified stream-based memory systems facilitate context updates but remain vulnerable to interference from transient noise. Conversely, discrete structured memory architectures provide robust knowledge retention but often struggle to adapt to evolving narratives. To address this, we propose GAM, a hierarchical Graph-based Agentic Memory framework that explicitly decouples memory encoding from consolidation to effectively resolve the conflict between rapid context perception and stable knowledge retention. By isolating ongoing dialogue in an event progression graph and integrating it into a topic associative network only upon semantic shifts, our approach minimizes interference while preserving long-term consistency. Additionally, we introduce a graph-guided, multi-factor retrieval strategy to enhance context precision. Experiments on LoCoMo and LongDialQA indicate that our method consistently outperforms state-of-the-art baselines in both reasoning accuracy and efficiency.

</details>


### 108. Towards Robust Real-World Spreadsheet Understanding with Multi-Agent Multi-Format Reasoning

- **Authors:** Houxing Ren, Mingjie Zhan, Zimu Lu, Ke Wang, Yunqiao Yang, Haotian Hou, Hongsheng Li
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12282v1](http://arxiv.org/abs/2604.12282v1)
- **PDF:** [https://arxiv.org/pdf/2604.12282v1](https://arxiv.org/pdf/2604.12282v1)
- **Categories:** cs.CL


> **Contribution:** The paper introduces **SpreadsheetAgent**, a two‑stage, multi‑agent architecture that enables robust, scalable understanding of real‑world spreadsheets by exploiting their visual/layout cues and handling massive files that exceed LLM context windows.  

**Methodology:** In the *Reading Stage* a set of specialized agents incrementally parses localized spreadsheet regions using diverse modalities (code execution outputs, rendered images, LaTeX tables) to build a compact structural sketch and row/column summaries. In the *Solving Stage* a task‑driven reasoning agent operates on this intermediate representation, while a verification module performs targeted inspections to catch and correct structural extraction errors before downstream reasoning.  

**Key Findings:** On two benchmark spreadsheet datasets, SpreadsheetAgent (with GPT‑OSS‑120B) attains 38.16% accuracy on the Spreadsheet Bench, a 2.89‑point absolute gain over a strong ChatGPT‑based agent baseline, demonstrating that multi‑agent, multi‑format reasoning and verification markedly improve reliability and scalability for agentic AI systems dealing with complex tabular data.


<details>
<summary>Abstract</summary>

Spreadsheets are central to real-world applications such as enterprise reporting, auditing, and scientific data management. Despite their ubiquity, existing large language model based approaches typically treat tables as plain text, overlooking critical layout cues and visual semantics. Moreover, real-world spreadsheets are often massive in scale, exceeding the input length that LLMs can efficiently process. To address these challenges, we propose SpreadsheetAgent, a two-stage multi-agent framework for spreadsheet understanding that adopts a step-by-step reading and reasoning paradigm. Instead of loading the entire spreadsheet at once, SpreadsheetAgent incrementally interprets localized regions through multiple modalities, including code execution results, images, and LaTeX tables. The method first constructs a structural sketch and row/column summaries, and then performs task-driven reasoning over this intermediate representation in the Solving Stage. To further enhance reliability, we design a verification module that validates extracted structures via targeted inspections, reducing error propagation and ensuring trustworthy inputs for downstream reasoning. Extensive experiments on two spreadsheet datasets demonstrate the effectiveness of our approach. With GPT-OSS-120B, SpreadsheetAgent achieves 38.16% on Spreadsheet Bench, outperforming the ChatGPT Agent baseline (35.27%) by 2.89 absolute points. These results highlight the potential of SpreadsheetAgent to advance robust and scalable spreadsheet understanding in real-world applications. Code is available at https://github.com/renhouxing/SpreadsheetAgent.git.

</details>


### 109. CascadeDebate: Multi-Agent Deliberation for Cost-Aware LLM Cascades

- **Authors:** Raeyoung Chang, Dongwook Kwon, Jisoo Lee, Nikhil Verma
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12262v1](http://arxiv.org/abs/2604.12262v1)
- **PDF:** [https://arxiv.org/pdf/2604.12262v1](https://arxiv.org/pdf/2604.12262v1)
- **Categories:** cs.CL, cs.AI


> **Paper Summary**

CascadeDebate introduces a hierarchical LLM‑cascade architecture that interleaves single‑model inference with on‑demand multi‑agent deliberation at each escalation point. A confidence‑based router triggers lightweight ensembles of specialist agents only for queries that are ambiguous for the current model, allowing the agents to reach a consensus and often resolve the uncertainty without promoting the request to a larger, more expensive model or a human expert. Experiments on five scientific, medical, and general‑knowledge benchmarks show that this dynamic, cost‑aware routing yields up to **26.75 % higher accuracy** than strong single‑model cascades and improves over fixed‑policy cascades by **20.98–52.33 %**, demonstrating that selective multi‑agent deliberation can substantially reduce compute while maintaining or boosting performance in agentic AI systems.


<details>
<summary>Abstract</summary>

Cascaded LLM systems coordinate models of varying sizes with human experts to balance accuracy, cost, and abstention under uncertainty. However, single-model tiers at each stage often struggle with ambiguous queries, triggering premature escalations to costlier models or experts due to under-confidence and inefficient compute scaling. CascadeDebate addresses this gap by inserting multi-agent deliberation directly at each tier's escalation boundary. Confidence-based routers activate lightweight agent ensembles only for uncertain cases, enabling consensus-driven resolution of ambiguities internally without invoking higher-cost upgrades. Our unified architecture alternates single-model inference with selective multi-agent deliberation across model scales, culminating in human experts as the final fallback. This design scales test-time compute dynamically according to query difficulty. Across five benchmarks spanning science, medicine, and general knowledge, CascadeDebate outperforms strong single-model cascades and standalone multi-agent systems by up to 26.75 percent. An online threshold optimizer proves essential, boosting accuracy by 20.98 to 52.33 percent relative improvement over fixed policies and enabling elastic adaptation to real-world distributions.

</details>


### 110. Coding-Free and Privacy-Preserving MCP Framework for Clinical Agentic Research Intelligence System

- **Authors:** Taehun Kim, Hyeryun Park, Hyeonhoon Lee, Yushin Lee, Kyungsang Kim, Hyung-Chul Lee
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12258v1](http://arxiv.org/abs/2604.12258v1)
- **PDF:** [https://arxiv.org/pdf/2604.12258v1](https://arxiv.org/pdf/2604.12258v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **CARIS**, a coding‑free, privacy‑preserving Clinical Agentic Research Intelligence System that lets clinicians formulate research questions in natural language and have the entire study pipeline—literature review, cohort building, IRB documentation, model training (Vibe ML), and report generation—automatically executed while raw patient data remain on a secure server. The system couples large language models with a **Model Context Protocol (MCP)** that orchestrates modular tools (databases, ML engines, document generators) based on user intent, enabling iterative human‑in‑the‑loop refinement without any programming. Across three heterogeneous clinical datasets, CARIS completed research plans and IRB forms in 3–4 iterations, ranked the top‑10 model configurations, and produced final reports that achieved 96 % checklist coverage in LLM evaluation and 82 % in human evaluation, demonstrating that agentic AI can reliably translate clinical hypotheses into end‑to‑end research workflows while preserving data privacy.


<details>
<summary>Abstract</summary>

Clinical research involves labor-intensive processes such as study design, cohort construction, model development, and documentation, requiring domain expertise, programming skills, and access to sensitive patient data. These demands create barriers for clinicians and external researchers conducting data-driven studies. To overcome these limitations, we developed a Clinical Agentic Research Intelligence System (CARIS) that automates the clinical research workflow while preserving data privacy, enabling comprehensive studies without direct access to raw data. CARIS integrates Large Language Models (LLMs) with modular tools via the Model Context Protocol (MCP), enabling natural language-driven orchestration of appropriate tools. Databases remain securely within the MCP server, and users access only the outputs and final research reports. Based on user intent, CARIS automatically executes the full pipeline: research planning, literature search, cohort construction, Institutional Review Board (IRB) documentation, Vibe Machine Learning (ML), and report generation, with iterative human-in-the-loop refinement. We evaluated CARIS on three heterogeneous datasets with distinct clinical tasks. Research plans and IRB documents were finalized within three to four iterations, using evidence from literature and data. The system supported Vibe ML by exploring feature-model combinations, ranking the top ten models, and generating performance visualizations. Final reports showed high completeness based on a checklist derived from the TRIPOD+AI framework, achieving 96% coverage in LLM evaluation and 82% in human evaluation. CARIS demonstrates that agentic AI can transform clinical hypotheses into executable research workflows across heterogeneous datasets. By eliminating the need for coding and direct data access, the system lowers barriers and bridges public and private clinical data environments.

</details>


### 111. A Scoping Review of Large Language Model-Based Pedagogical Agents

- **Authors:** Shan Li, Juan Zheng
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12253v1](http://arxiv.org/abs/2604.12253v1)
- **PDF:** [https://arxiv.org/pdf/2604.12253v1](https://arxiv.org/pdf/2604.12253v1)
- **Categories:** cs.AI


> The paper conducts the first systematic scoping review of Large Language Model (LLM)‑driven pedagogical agents, cataloguing 52 studies (Nov 2022–Jan 2025) and defining four design dimensions—interaction approach, domain scope, role complexity, and system integration—to map how LLMs are being embedded in K‑12, higher‑education, and informal‑learning contexts. By applying PRISMA‑ScR methods, the authors show that current work is trending toward multi‑agent, immersive, and analytics‑enhanced environments, but they also highlight persistent gaps (e.g., robust evaluation, privacy, and autonomy safeguards). This synthesis offers a blueprint for building and assessing agentic AI tutors, pointing to the need for standardized benchmarks, ethical safeguards, and interdisciplinary frameworks to realize trustworthy, adaptable learning agents.


<details>
<summary>Abstract</summary>

This scoping review examines the emerging field of Large Language Model (LLM)-based pedagogical agents in educational settings. While traditional pedagogical agents have been extensively studied, the integration of LLMs represents a transformative advancement with unprecedented capabilities in natural language understanding, reasoning, and adaptation. Following PRISMA-ScR guidelines, we analyzed 52 studies across five major databases from November 2022 to January 2025. Our findings reveal diverse LLM-based agents spanning K-12, higher education, and informal learning contexts across multiple subject domains. We identified four key design dimensions characterizing these agents: interaction approach (reactive vs. proactive), domain scope (domain-specific vs. general-purpose), role complexity (single-role vs. multi-role), and system integration (standalone vs. integrated). Emerging trends include multi-agent systems that simulate naturalistic learning environments, virtual student simulation for agent evaluation, integration with immersive technologies, and combinations with learning analytics. We also discuss significant research gaps and ethical considerations regarding privacy, accuracy, and student autonomy. This review provides researchers and practitioners with a comprehensive understanding of LLM-based pedagogical agents while identifying crucial areas for future development in this rapidly evolving field.

</details>


### 112. How memory can affect collective and cooperative behaviors in an LLM-Based Social Particle Swarm

- **Authors:** Taisei Hishiki, Takaya Arita, Reiji Suzuki
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12250v1](http://arxiv.org/abs/2604.12250v1)
- **PDF:** [https://arxiv.org/pdf/2604.12250v1](https://arxiv.org/pdf/2604.12250v1)
- **Categories:** cs.AI, cs.CL, cs.GT, cs.MA


> The paper extends the classic Social Particle Swarm model by swapping its deterministic agents for LLM‑driven agents (Gemini‑2.0‑Flash and Gemma 3:4b) that are assigned Big‑Five personality scores and equipped with configurable memory windows, then lets them move in a 2‑D arena and repeatedly play Prisoner’s Dilemma with local neighbors.  Experiments reveal that memory length is a decisive, model‑specific driver of collective outcomes: with Gemini, even a short memory rapidly collapses cooperation into scattered defection, whereas with Gemma longer memories foster dense, stable cooperative clusters, a divergence linked to opposite sentiment trends in the agents’ reasoning texts.  The findings show that LLM alignment and internal semantics crucially shape emergent cooperation in generative multi‑agent simulations, offering a micro‑cognitive explanation for previously contradictory results on memory’s role in collective behavior.


<details>
<summary>Abstract</summary>

This study examines how model-specific characteristics of Large Language Model (LLM) agents, including internal alignment, shape the effect of memory on their collective and cooperative dynamics in a multi-agent system. To this end, we extend the Social Particle Swarm (SPS) model, in which agents move in a two-dimensional space and play the Prisoner's Dilemma with neighboring agents, by replacing its rule-based agents with LLM agents endowed with Big Five personality scores and varying memory lengths. Using Gemini-2.0-Flash, we find that memory length is a critical parameter governing collective behavior: even a minimal memory drastically suppressed cooperation, transitioning the system from stable cooperative clusters through cyclical formation and collapse of clusters to a state of scattered defection as memory length increased. Big Five personality traits correlated with agent behaviors in partial agreement with findings from experiments with human participants, supporting the validity of the model. Comparative experiments using Gemma~3:4b revealed the opposite trend: longer memory promoted cooperation, accompanied by the formation of dense cooperative clusters. Sentiment analysis of agents' reasoning texts showed that Gemini interprets memory increasingly negatively as its length grows, while Gemma interprets it less negatively, and that this difference persists in the early phase of experiments before the macro-level dynamics converge. These results suggest that model-specific characteristics of LLMs, potentially including alignment, play a fundamental role in determining emergent social behavior in Generative Agent-Based Modeling, and provide a micro-level cognitive account of the contradictions found in prior work on memory and cooperation.

</details>


### 113. Modality-Native Routing in Agent-to-Agent Networks: A Multimodal A2A Protocol Extension

- **Authors:** Vasundra Srinivasan
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12213v1](http://arxiv.org/abs/2604.12213v1)
- **PDF:** [https://arxiv.org/pdf/2604.12213v1](https://arxiv.org/pdf/2604.12213v1)
- **Categories:** cs.AI, cs.MA, cs.SE


> The paper introduces **MMA2A**, a protocol extension for Agent‑to‑Agent (A2A) networks that routes each component of a multimodal message (voice, image, text) in its *native* format based on the receiving agent’s declared capabilities. By holding the LLM backend and task set constant and only varying the routing strategy, the authors show that native multimodal routing boosts task‑completion accuracy on the CrossModal‑CS benchmark from 32 % to 52 % (a 20‑pp gain, statistically significant p = 0.006), with the largest improvements on vision‑heavy tasks (+38.5 pp for defect reports, +16.7 pp for visual troubleshooting). An ablation that replaces the LLM‑based reasoning with simple keyword matching eliminates the advantage, demonstrating that **both** a modality‑aware routing layer **and** a capable reasoning agent are required for multimodal benefits to materialize, albeit at a 1.8× latency cost.


<details>
<summary>Abstract</summary>

Preserving multimodal signals across agent boundaries is necessary for accurate cross-modal reasoning, but it is not sufficient. We show that modality-native routing in Agent-to-Agent (A2A) networks improves task accuracy by 20 percentage points over text-bottleneck baselines, but only when the downstream reasoning agent can exploit the richer context that native routing preserves. An ablation replacing LLM-backed reasoning with keyword matching eliminates the accuracy gap entirely (36% vs. 36%), establishing a two-layer requirement: protocol-level routing must be paired with capable agent-level reasoning for the benefit to materialize.
  We present MMA2A, an architecture layer atop A2A that inspects Agent Card capability declarations to route voice, image, and text parts in their native modality. On CrossModal-CS, a controlled 50-task benchmark with the same LLM backend, same tasks, and only the routing path varying, MMA2A achieves 52% task completion accuracy versus 32% for the text-bottleneck baseline (95% bootstrap CI on $Δ$TCA: [8, 32] pp; McNemar's exact $p = 0.006$). Gains concentrate on vision-dependent tasks: product defect reports improve by +38.5 pp and visual troubleshooting by +16.7 pp. This accuracy gain comes at a $1.8\times$ latency cost from native multimodal processing. These results suggest that routing is a first-order design variable in multi-agent systems, as it determines the information available for downstream reasoning.

</details>


### 114. Towards grounded autonomous research: an end-to-end LLM mini research loop on published computational physics

- **Authors:** Haonan Huang
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12198v1](http://arxiv.org/abs/2604.12198v1)
- **PDF:** [https://arxiv.org/pdf/2604.12198v1](https://arxiv.org/pdf/2604.12198v1)
- **Categories:** physics.comp-ph, cond-mat.mtrl-sci, cs.AI


> **Main contribution**  
The paper introduces a fully autonomous “mini‑research loop” for large‑language‑model (LLM) agents that can read a computational‑physics paper, reproduce its results, critically evaluate them, and generate an extension or comment, thereby moving LLM‑driven research from pure ML tasks to grounded physical‑science inquiry.

**Methodology**  
The authors implement an end‑to‑end pipeline (read → plan → compute → compare) that parses open‑access papers, automatically extracts code and data, runs the simulations on a compute cluster, and uses the LLM to generate critiques and new experiments. They evaluate the system in two settings: (1) a large‑scale batch test on 111 computational‑physics articles, measuring how often the loop uncovers substantive, execution‑dependent issues; and (2) a deep case study on a Nature Communications MOSFET simulation, where the agent performs additional multiscale calculations and drafts a complete, publishable “Comment” that overturns the original headline claim.

**Key findings**  
- In the batch evaluation, the autonomous loop flagged meaningful concerns in ~42 % of papers, and 97.7 % of those concerns only emerged after the computational reproductions were executed, demonstrating the importance of closed‑loop execution.  
- In the case study, the agent independently identified missing simulations, produced new results, and authored a fully formatted scientific comment that revised the paper’s main conclusion, showing that LLM agents can not only reproduce but also extend and critically improve real scientific work.  

These results suggest that LLM‑based agents can be grounded in physical truth and literature, opening a path toward autonomous, verifiable scientific discovery in the physical sciences.


<details>
<summary>Abstract</summary>

Recent autonomous LLM agents have demonstrated end-to-end automation of machine-learning research. Real-world physical science is intrinsically harder, requiring deep reasoning bounded by physical truth and, because real systems are too complex to study in isolation, almost always built on existing literature. We focus on the smallest meaningful unit of such research, a mini research loop in which an agent reads a paper, reproduces it, critiques it, and extends it. We test this loop in two complementary regimes: scale and depth. At scale, across 111 open-access computational physics papers, an agent autonomously runs the read-plan-compute-compare loop and, without being asked to critique, raises substantive concerns on ~42% of papers - 97.7% of which require execution to surface. In depth, for one Nature Communications paper on multiscale simulation of a 2D-material MOSFET, the agent runs new calculations missing from the original and produces, unsupervised, a publishable Comment -- composed, figured, typeset, and PDF-iterated -- that revises the paper's headline conclusion.

</details>


### 115. Beyond Majority Voting: Efficient Best-Of-N with Radial Consensus Score

- **Authors:** Manh Nguyen, Sunil Gupta, Hung Le
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12196v1](http://arxiv.org/abs/2604.12196v1)
- **PDF:** [https://arxiv.org/pdf/2604.12196v1](https://arxiv.org/pdf/2604.12196v1)
- **Categories:** cs.CL


> The paper introduces **Radial Consensus Score (RCS)**, a training‑free, geometry‑based selector for the best‑of‑N outputs from large language models. RCS computes a weighted Fréchet mean of answer embeddings to define a semantic “center” and ranks each candidate by its radial distance to this center, allowing uniform, frequency‑based, or probability‑based weighting of agreement signals and model confidence—even in black‑box settings. Experiments on seven QA/reasoning benchmarks and five open‑weight LLMs show that RCS consistently outperforms majority voting, self‑consistency, and other probability‑based selectors, with larger gains as more samples are drawn, and it also improves multi‑agent debate robustness, demonstrating that geometric consensus is an effective, scalable tool for reliable answer aggregation in agentic AI.


<details>
<summary>Abstract</summary>

Large language models (LLMs) frequently generate multiple candidate responses for a given prompt, yet selecting the most reliable one remains challenging, especially when correctness diverges from surface-level majority agreement. Existing approaches, such as self-consistency, rely on discrete voting, while probability-based methods often fail to capture relationships among candidate answers or tend to underweight high-quality but less frequent responses, and do not fully leverage the geometric structure of answer representations. To address these limitations, we introduce Radial Consensus Score (RCS), a simple, efficient, and training-free method for best-of-N selection. RCS models semantic consensus by computing a weighted Fréchet mean (semantic center) of answer embeddings and ranking candidates by their radial distance to this center. Importantly, RCS provides a general framework that supports multiple weighting schemes, including uniform, frequency-based, and probability-based variants, enabling flexible integration of agreement signals and model confidence while remaining fully applicable in black-box settings. Extensive experiments across seven benchmarks covering short-form QA and long-form reasoning tasks, and five open-weight models, demonstrate that RCS variants consistently outperform strong baselines, with gains becoming more pronounced as the sampling budget increases. RCS also serves as an effective drop-in replacement for majority voting in multi-agent debate and exhibits strong robustness in black-box scenarios. Overall, these results highlight geometric consensus as a scalable and broadly applicable principle for reliable answer selection, extending beyond majority voting to more expressive and robust aggregation in LLM inference.

</details>


### 116. TRUST Agents: A Collaborative Multi-Agent Framework for Fake News Detection, Explainable Verification, and Logic-Aware Claim Reasoning

- **Authors:** Gautama Shastry Bulusu Venkata, Santhosh Kakarla, Maheedhar Omtri Mohan, Aishwarya Gaddam
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12184v1](http://arxiv.org/abs/2604.12184v1)
- **PDF:** [https://arxiv.org/pdf/2604.12184v1](https://arxiv.org/pdf/2604.12184v1)
- **Categories:** cs.AI


> TRUST Agents proposes a modular multi‑agent architecture that turns fact‑checking into a collaborative workflow rather than a single‑shot classification: a claim‑extraction agent parses statements, a hybrid sparse‑dense retrieval agent pulls evidence, a verifier agent evaluates the evidence and outputs calibrated confidence scores, and an explainer agent produces human‑readable reports with citation links. The extended version adds a claim‑decomposer, a jury of persona‑based verifier agents, and a logic aggregator that composes atomic verdicts with Boolean operators, enabling reasoning over complex, multi‑premise claims. Experiments on the LIAR benchmark show that, while fine‑tuned BERT/RoBERTa still achieve higher raw accuracy, TRUST Agents markedly improves interpretability, evidence transparency, and logical reasoning, with retrieval quality and uncertainty calibration identified as the primary performance bottlenecks for trustworthy AI fact verification.


<details>
<summary>Abstract</summary>

TRUST Agents is a collaborative multi-agent framework for explainable fact verification and fake news detection. Rather than treating verification as a simple true-or-false classification task, the system identifies verifiable claims, retrieves relevant evidence, compares claims against that evidence, reasons under uncertainty, and generates explanations that humans can inspect. The baseline pipeline consists of four specialized agents. A claim extractor uses named entity recognition, dependency parsing, and LLM-based extraction to identify factual claims. A retrieval agent performs hybrid sparse and dense search using BM25 and FAISS. A verifier agent compares claims with retrieved evidence and produces verdicts with calibrated confidence. An explainer agent then generates a human-readable report with explicit evidence citations. To handle complex claims more effectively, we introduce a research-oriented extension with three additional components: a decomposer agent inspired by LoCal-style claim decomposition, a Delphi-inspired multi-agent jury with specialized verifier personas, and a logic aggregator that combines atomic verdicts using conjunction, disjunction, negation, and implication. We evaluate both pipelines on the LIAR benchmark against fine-tuned BERT, fine-tuned RoBERTa, and a zero-shot LLM baseline. Although supervised encoders remain stronger on raw metrics, TRUST Agents improves interpretability, evidence transparency, and reasoning over compound claims. Results also show that retrieval quality and uncertainty calibration remain the main bottlenecks in trustworthy automated fact verification.

</details>


### 117. AgenticAI-DialogGen: Topic-Guided Conversation Generation for Fine-Tuning and Evaluating Short- and Long-Term Memories of LLMs

- **Authors:** Manoj Madushanka Perera, Adnan Mahmood, Kasun Eranda Wijethilake, Quan Z. Sheng
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12179v1](http://arxiv.org/abs/2604.12179v1)
- **PDF:** [https://arxiv.org/pdf/2604.12179v1](https://arxiv.org/pdf/2604.12179v1)
- **Categories:** cs.CL, cs.IR


> The paper introduces **AgenticAI‑DialogGen**, a modular framework that uses multiple LLM agents to automatically construct persona‑grounded, topic‑guided dialogues and corresponding memory‑grounded QA pairs, thereby creating a novel dataset (TopicGuidedChat, TGC) that encodes both short‑term (recent turns) and long‑term (speaker‑specific knowledge graphs) memory. By extracting knowledge graphs, identifying evolving topics, and simulating conversations without human labeling, the authors generate high‑quality, memory‑rich dialogues; fine‑tuning LLMs on TGC then yields significant gains on downstream memory‑grounded question‑answering benchmarks. The results demonstrate that AgenticAI‑DialogGen improves conversational quality and enables more effective evaluation and adaptation of LLMs’ short‑ and long‑term memory capabilities.


<details>
<summary>Abstract</summary>

Recent advancements in Large Language Models (LLMs) have improved their ability to process extended conversational contexts, yet fine-tuning and evaluating short- and long-term memories remain difficult due to the absence of datasets that encode both short- and long-term conversational history. Existing conversational datasets lack memory grounding, overlook topic continuity, or rely on costly human annotation. To address these gaps, we introduce AgenticAI-DialogGen, a modular agent-based framework that generates persona-grounded and topic-guided conversations without human supervision. The framework uses LLM agents to extract knowledge graphs, identify topics, build speaker personas, and simulate topic-guided conversations from unstructured conversations. A QA module generates memory-grounded Question Answer (QA) pairs drawn from short- and long-term conversational histories. We also generated a new dataset entitled, TopicGuidedChat (TGC), where long-term memory is encoded as speaker-specific knowledge graphs and short-term memory as newly generated topic-guided conversations. Evaluations depict that AgenticAI-DialogGen yields higher conversational quality and LLMs fine-tuned on TGC dataset achieve improved performance on memory-grounded QA tasks.

</details>


### 118. AlphaEval: Evaluating Agents in Production

- **Authors:** Pengrui Lu, Bingyu Xu, Wenjun Zhang, Shengjia Hua, Xuanjian Gao, Ranxiang Ge, Lyumanshan Ye, Linxuan Wu, Yiran Li, Junfei Fish Yu, Yibo Zhang, Ruixin Li, Manxiang Li, Xiao Han, Xiaocong Zhou, Guangyao Chi, Zisheng Chen, Kaishen Chen, Kun Wang, Qihua Xu, Fengyue Meng, Yuchen Ni, Jiajun Li, Jinxiu Liu, Danfeng Zhang, Jingru Zhao, Pengfei Liu
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12162v1](http://arxiv.org/abs/2604.12162v1)
- **PDF:** [https://arxiv.org/pdf/2604.12162v1](https://arxiv.org/pdf/2604.12162v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **AlphaEval**, a production‑grounded benchmark that evaluates whole AI‑agent systems—as they are deployed in real‑world business settings—rather than isolated language models. It also provides a systematic “requirement‑to‑benchmark” framework that converts authentic production specifications into executable evaluation tasks.

**Methodology:** The authors collected 94 tasks from seven companies across six O*NET occupational domains, covering heterogeneous multimodal inputs, implicit constraints, and long‑horizon professional outputs. Evaluation is performed with a multi‑paradigm suite (LLM‑as‑Judge, reference‑based metrics, formal verification, rubric scoring, automated UI testing, etc.) applied to complete agent products (e.g., Claude, Codex). The construction framework formalizes the pipeline from real‑world requirements to benchmark instances, enabling rapid, reproducible benchmark creation.

**Key findings:** AlphaEval reveals performance gaps that standard model‑centric benchmarks miss, showing that agents’ success rates vary markedly when judged by domain‑expert rubrics and dynamic production criteria. The benchmark and its construction pipeline are shown to be reusable across domains, offering a practical tool for organizations to monitor and improve the reliability of agentic AI in production environments.


<details>
<summary>Abstract</summary>

The rapid deployment of AI agents in commercial settings has outpaced the development of evaluation methodologies that reflect production realities. Existing benchmarks measure agent capabilities through retrospectively curated tasks with well-specified requirements and deterministic metrics -- conditions that diverge fundamentally from production environments where requirements contain implicit constraints, inputs are heterogeneous multi-modal documents with information fragmented across sources, tasks demand undeclared domain expertise, outputs are long-horizon professional deliverables, and success is judged by domain experts whose standards evolve over time. We present AlphaEval, a production-grounded benchmark of 94 tasks sourced from seven companies deploying AI agents in their core business, spanning six O*NET (Occupational Information Network) domains. Unlike model-centric benchmarks, AlphaEval evaluates complete agent products -- Claude Code, Codex, etc. -- as commercial systems, capturing performance variations invisible to model-level evaluation. Our evaluation framework covers multiple paradigms (LLM-as-a-Judge, reference-driven metrics, formal verification, rubric-based assessment, automated UI testing, etc.), with individual domains composing multiple paradigms. Beyond the benchmark itself, we contribute a requirement-to-benchmark construction framework -- a systematic methodology that transforms authentic production requirements into executable evaluation tasks in minimal time. This framework standardizes the entire pipeline from requirement to evaluation, providing a reproducible, modular process that any organization can adopt to construct production-grounded benchmarks for their own domains.

</details>


### 119. Development, Evaluation, and Deployment of a Multi-Agent System for Thoracic Tumor Board

- **Authors:** Tim Ellis-Caleo, Timothy Keyes, Nerissa Ambers, Faraah Bekheet, Wen-wai Yim, Nikesh Kotecha, Nigam H. Shah, Joel Neal
- **Published:** 2026-04-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12161v1](http://arxiv.org/abs/2604.12161v1)
- **PDF:** [https://arxiv.org/pdf/2604.12161v1](https://arxiv.org/pdf/2604.12161v1)
- **Categories:** cs.AI


> **Main contribution:** The paper presents a fully automated, multi‑agent pipeline that generates concise, fact‑checked clinical summaries of thoracic cancer patients for use in real‑time multidisciplinary tumor board meetings, and demonstrates how such an AI‑driven workflow can be safely integrated into routine clinical practice.  

**Methodology:** A suite of specialized agents—data ingestion, radiology/pathology extraction, summarization, and fact‑verification—were built on large language models (LLMs) and fine‑tuned summarization models. The system was benchmarked against physician‑authored summaries using both human expert ratings and an LLM‑based fact‑scoring rubric, followed by a pilot deployment with continuous post‑deployment monitoring at Stanford’s Thoracic Tumor Board.  

**Key findings:** Automated summaries matched or exceeded physician gold standards on factual accuracy (≈ 92 % correct entities) while reducing manual effort by > 80 %. The LLM‑as‑judge approach correlated strongly (ρ ≈ 0.84) with human fact‑scoring, validating its use for rapid evaluation. Post‑deployment monitoring showed stable performance and clinician acceptance, illustrating a viable pathway for agentic AI systems to augment high‑stakes medical decision‑making.


<details>
<summary>Abstract</summary>

Tumor boards are multidisciplinary conferences dedicated to producing actionable patient care recommendations with live review of primary radiology and pathology data. Succinct patient case summaries are needed to drive efficient and accurate case discussions. We developed a manual AI-based workflow to generate patient summaries to display live at the Stanford Thoracic Tumor board. To improve on this manually intensive process, we developed several automated AI chart summarization methods and evaluated them against physician gold standard summaries and fact-based scoring rubrics. We report these comparative evaluations as well as our deployment of the final state automated AI chart summarization tool along with post-deployment monitoring. We also validate the use of an LLM as a judge evaluation strategy for fact-based scoring. This work is an example of integrating AI-based workflows into routine clinical practice.

</details>


### 120. VERITAS: Verifiable Epistemic Reasoning for Image-Derived Hypothesis Testing via Agentic Systems

- **Authors:** Lucas Stoffl, Benedikt Wiestler, Johannes C. Paetzold
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12144v1](http://arxiv.org/abs/2604.12144v1)
- **PDF:** [https://arxiv.org/pdf/2604.12144v1](https://arxiv.org/pdf/2604.12144v1)
- **Categories:** cs.MA


> VERITAS introduces a role‑specialized, multi‑agent architecture that automatically translates natural‑language clinical hypotheses into reproducible image‑derived statistical analyses, generating a fully traceable evidence trail from data preprocessing to final verdict. By decomposing the pipeline into four epistemic‑reasoning phases and applying a mechanistic label scheme (Supported, Refuted, Underpowered, Invalid), VERITAS evaluates significance, effect direction, and study power, which is crucial for interpreting non‑significant findings in medical imaging. On a 64‑hypothesis benchmark spanning cardiac and brain MRI datasets, the system attains 81.4 % verdict accuracy with frontier models (and 71.2 % with 8‑30 B open‑weight models), surpassing all single‑model baselines while delivering a verifiable output rate of 86.6 %, demonstrating that structured multi‑agent decomposition can replace raw model scale while meeting the auditability required in agentic AI for clinical research.


<details>
<summary>Abstract</summary>

Drawing meaningful conclusions from inherently multimodal clinical data (including medical imaging) requires coordinating expertise across the clinical specialty, radiology, programming, and biostatistics. This fragmented process bottlenecks discovery. We present VERITAS (Verifiable Epistemic Reasoning for Image-Derived Hypothesis Testing via Agentic Systems), a multi-agent system that autonomously tests natural-language hypotheses on multimodal clinical datasets while producing a fully auditable evidence trail: every statistical conclusion traces through inspectable, executable outputs from analysis plan to segmentation masks to statistical code to final verdict. VERITAS decomposes the workflow into four phases handled by role-specialized agents, and introduces an epistemic evidence label framework that mechanically classifies outcomes as Supported, Refuted, Underpowered, or Invalid by jointly evaluating significance, effect direction, and study power. This distinction is critical in medical imaging, where non-significant results often reflect insufficient sample size rather than absent effects. To evaluate the system, we construct a tiered benchmark of 64 hypotheses spanning six complexity levels across cardiac (ACDC, 150 subjects) and brain glioma (UCSF-PDGM, 501 subjects) MRI. VERITAS reaches 81.4% verdict accuracy with frontier models and 71.2% with locally-hosted open-weight models (8-30B), outperforming all five single-model baselines in both classes. It also produces the highest rate of independently verifiable statistical outputs (86.6%), so even its failures remain diagnosable through artifact inspection. Structured multi-agent decomposition thus substitutes for model scale while preserving the verifiability clinical research demands.

</details>


### 121. Aethon: A Reference-Based Replication Primitive for Constant-Time Instantiation of Stateful AI Agents

- **Authors:** Swanand Rao, Kiran Kashalkar, Parvathi Somashekar, Priya Krishnan
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12129v1](http://arxiv.org/abs/2604.12129v1)
- **PDF:** [https://arxiv.org/pdf/2604.12129v1](https://arxiv.org/pdf/2604.12129v1)
- **Categories:** cs.AI, cs.AR, cs.DC, cs.MA


> The paper introduces **Aethon**, a runtime primitive that creates stateful AI agents by mounting lightweight **reference‑based views** onto a shared, immutable definition instead of fully materializing a new object each time. The authors design a layered memory model with copy‑on‑write and compositional inheritance, implement it as a thin replication layer, and evaluate its instantiation latency and memory footprint, showing near‑constant‑time creation and up to an order‑of‑magnitude reduction in peak memory compared with conventional deep‑copy spawning. These results demonstrate that reference‑based replication enables scalable, low‑latency deployment and governance of large numbers of persistent, tool‑using agents, suggesting a more suitable systems abstraction for production‑grade agentic AI.


<details>
<summary>Abstract</summary>

The transition from stateless model inference to stateful agentic execution is reshaping the systems assumptions underlying modern AI infrastructure. While large language models have made persistent, tool-using, and collaborative agents technically viable, existing runtime architectures remain constrained by materialization-heavy instantiation models that impose significant latency and memory overhead.
  This paper introduces Aethon, a reference-based replication primitive for near-constant-time instantiation of stateful AI agents. Rather than reconstructing agents as fully materialized objects, Aethon represents each instance as a compositional view over stable definitions, layered memory, and local contextual overlays. By shifting instantiation from duplication to reference, Aethon decouples creation cost from inherited structure.
  We present the conceptual framework, system architecture, and memory model underlying Aethon, including layered inheritance and copy-on-write semantics. We analyze its implications for complexity, scalability, multi-agent orchestration, and enterprise governance. We argue that reference-based instantiation is not merely an optimization, but a more appropriate systems abstraction for production-scale agentic software.
  Aethon points toward a new class of AI infrastructure in which agents become lightweight, composable execution identities that can be spawned, specialized, and governed at scale.

</details>


### 122. Long-Horizon Plan Execution in Large Tool Spaces through Entropy-Guided Branching

- **Authors:** Rongzhe Wei, Ge Shi, Min Cheng, Na Zhang, Pan Li, Sarthak Ghosh, Vaibhav Gorde, Leman Akoglu
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12126v1](http://arxiv.org/abs/2604.12126v1)
- **PDF:** [https://arxiv.org/pdf/2604.12126v1](https://arxiv.org/pdf/2604.12126v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces **SLATE**, a synthetic, large‑scale benchmark of e‑commerce APIs that enables systematic, plan‑level evaluation of tool‑augmented LLM agents, exposing current models’ weaknesses in self‑correction and efficient search across massive tool libraries. To address these bottlenecks, the authors propose **Entropy‑Guided Branching (EGB)**, an uncertainty‑driven search algorithm that expands only high‑entropy branches during long‑horizon planning, thereby balancing exploration and exploitation. Experiments on SLATE show that EGB markedly improves task‑completion rates while reducing computational overhead, establishing a new baseline for reliable, scalable agentic AI in environments with extensive tool spaces.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have significantly advanced tool-augmented agents, enabling autonomous reasoning via API interactions. However, executing multi-step tasks within massive tool libraries remains challenging due to two critical bottlenecks: (1) the absence of rigorous, plan-level evaluation frameworks and (2) the computational demand of exploring vast decision spaces stemming from large toolsets and long-horizon planning. To bridge these gaps, we first introduce SLATE (Synthetic Large-scale API Toolkit for E-commerce), a large-scale context-aware benchmark designed for the automated assessment of tool-integrated agents. Unlike static metrics, SLATE accommodates diverse yet functionally valid execution trajectories, revealing that current agents struggle with self-correction and search efficiency. Motivated by these findings, we next propose Entropy-Guided Branching (EGB), an uncertainty-aware search algorithm that dynamically expands decision branches where predictive entropy is high. EGB optimizes the exploration-exploitation trade-off, significantly enhancing both task success rates and computational efficiency. Extensive experiments on SLATE demonstrate that our dual contribution provides a robust foundation for developing reliable and scalable LLM agents in tool-rich environments.

</details>


### 123. The A-R Behavioral Space: Execution-Level Profiling of Tool-Using Language Model Agents in Organizational Deployment

- **Authors:** Shasha Yu, Fiona Carroll, Barry L. Bentley
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12116v1](http://arxiv.org/abs/2604.12116v1)
- **PDF:** [https://arxiv.org/pdf/2604.12116v1](https://arxiv.org/pdf/2604.12116v1)
- **Categories:** cs.AI, cs.SE


> **Main contribution:** The paper proposes a novel execution‑level profiling framework for tool‑using LLM agents, mapping their behavior onto a two‑dimensional “A‑R” space that captures **Action Rate (A)**—how often the agent carries out tool calls—and **Refusal Signal (R)**—how often it declines or defers actions. By adding a third metric, **Divergence (D)**, the authors quantify the coordination between execution and refusal, enabling systematic comparison of agents across different normative regimes and autonomy scaffolds.

**Methodology:** Agents are tested in four regulatory contexts (Control, Gray, Dilemma, Malicious) and three autonomy configurations (direct execution, planning, reflection). For each setting the authors record every tool invocation and refusal, compute the A‑R coordinates, and visualise the joint distribution and transitions induced by the scaffolding (e.g., moving from planning to reflection).

**Key findings for agentic AI:** (1) Execution and refusal emerge as **orthogonal behavioral dimensions**—they are not interchangeable proxies for safety or performance. (2) Introducing a reflection scaffold consistently raises refusal rates in high‑risk regimes, but the exact redistribution of A and R differs markedly among models, revealing model‑specific “behavioral signatures.” (3) The A‑R/D representation makes these signatures, scaffold‑induced shifts, and coordination variability directly observable, offering a deployment‑focused diagnostic tool for selecting and configuring tool‑augmented agents in organizations with varying execution privileges and risk tolerances.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as tool-augmented agents capable of executing system-level operations. While existing benchmarks primarily assess textual alignment or task success, less attention has been paid to the structural relationship between linguistic signaling and executable behavior under varying autonomy scaffolds. This study introduces an execution-layer be-havioral measurement approach based on a two-dimensional A-R space defined by Action Rate (A) and Refusal Signal (R), with Divergence (D) capturing coor-dination between the two. Models are evaluated across four normative regimes (Control, Gray, Dilemma, and Malicious) and three autonomy configurations (di-rect execution, planning, and reflection). Rather than assigning aggregate safety scores, the method characterizes how execution and refusal redistribute across contextual framing and scaffold depth. Empirical results show that execution and refusal constitute separable behavioral dimensions whose joint distribution varies systematically across regimes and autonomy levels. Reflection-based scaffolding often shifts configurations toward higher refusal in risk-laden contexts, but redis-tribution patterns differ structurally across models. The A-R representation makes cross-sectional behavioral profiles, scaffold-induced transitions, and coordination variability directly observable. By foregrounding execution-layer characterization over scalar ranking, this work provides a deployment-oriented lens for analyzing and selecting tool-enabled LLM agents in organizational settings where execution privileges and risk tolerance vary.

</details>


### 124. Learning Probabilistic Responsibility Allocations for Multi-Agent Interactions

- **Authors:** Isaac Remy, Caleb Chang, Karen Leung
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13128v1](http://arxiv.org/abs/2604.13128v1)
- **PDF:** [https://arxiv.org/pdf/2604.13128v1](https://arxiv.org/pdf/2604.13128v1)
- **Categories:** cs.MA, cs.LG, cs.RO, eess.SY


> **Main contribution:** The paper proposes a learning framework that infers a *probabilistic* responsibility‑allocation function for interacting agents, enabling autonomous systems to predict how much each participant will compromise its own intent to satisfy shared safety constraints.  

**Methodology:** A conditional variational auto‑encoder (CVAE) encodes scene and agent context into a latent space from which a distribution over responsibility allocations is sampled; a differentiable optimization layer then maps each sampled allocation to the resulting control actions (which are observable), allowing end‑to‑end training despite the absence of explicit responsibility labels.  

**Key findings:** On the INTERACTION driving benchmark, the model outperforms state‑of‑the‑art trajectory forecasters in predicting multi‑agent behavior and yields interpretable responsibility patterns (e.g., which vehicle yields), demonstrating that learned responsibility distributions can enhance socially compliant and trustworthy decision‑making in agentic AI.


<details>
<summary>Abstract</summary>

Human behavior in interactive settings is shaped not only by individual objectives but also by shared constraints with others, such as safety. Understanding how people allocate responsibility, i.e., how much one deviates from their desired policy to accommodate others, can inform the design of socially compliant and trustworthy autonomous systems. In this work, we introduce a method for learning a probabilistic responsibility allocation model that captures the multimodal uncertainty inherent in multi-agent interactions. Specifically, our approach leverages the latent space of a conditional variational autoencoder, combined with techniques from multi-agent trajectory forecasting, to learn a distribution over responsibility allocations conditioned on scene and agent context. Although ground-truth responsibility labels are unavailable, the model remains tractable by incorporating a differentiable optimization layer that maps responsibility allocations to induced controls, which are available. We evaluate our method on the INTERACTION driving dataset and demonstrate that it not only achieves strong predictive performance but also provides interpretable insights, through the lens of responsibility, into patterns of multi-agent interaction.

</details>


### 125. Mathematics Teachers Interactions with a Multi-Agent System for Personalized Problem Generation

- **Authors:** Candace Walkington, Theodora Beauchamp, Fareya Ikram, Merve Koçyiğit Gürbüz, Fangli Xia, Margan Lee, Andrew Lan
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12066v1](http://arxiv.org/abs/2604.12066v1)
- **PDF:** [https://arxiv.org/pdf/2604.12066v1](https://arxiv.org/pdf/2604.12066v1)
- **Categories:** cs.AI, cs.CY


> **Main contribution:** The paper introduces and evaluates a teacher‑in‑the‑loop multi‑agent system that uses a large language model to generate personalized middle‑school mathematics problems, with four downstream AI agents automatically checking each problem for mathematical accuracy, authenticity, readability, and realism.  

**Methodology:** Teachers entered a seed problem and a target topic; the LLM produced candidate items, which were then filtered by the specialized agents. Eight teachers created 212 problems in the ASSISTments platform and deployed them to students, while both teachers and students provided post‑hoc feedback on the final items.  

**Key findings:** The agent ensemble successfully caught many realism issues during authoring, and final problems showed few realism, readability, or mathematical‑hallucination errors. However, teachers and students frequently wanted to adjust fine‑grained, real‑world contextual details, indicating that while automated validation works well, preserving authenticity and contextual fit still requires human control—highlighting the need for multi‑agent personalization systems that keep teachers in the loop.


<details>
<summary>Abstract</summary>

Large language models can increasingly adapt educational tasks to learners characteristics. In the present study, we examine a multi-agent teacher-in-the-loop system for personalizing middle school math problems. The teacher enters a base problem and desired topic, the LLM generates the problem, and then four AI agents evaluate the problem using criteria that each specializes in (mathematical accuracy, authenticity, readability, and realism). Eight middle school mathematics teachers created 212 problems in ASSISTments using the system and assigned these problems to their students. We find that both teachers and students wanted to modify the fine-grained personalized elements of the real-world context of the problems, signaling issues with authenticity and fit. Although the agents detected many issues with realism as the problems were being written, there were few realism issues noted by teachers and students in the final versions. Issues with readability and mathematical hallucinations were also somewhat rare. Implications for multi-agent systems for personalization that support teacher control are given.

</details>


### 126. REGREACT: Self-Correcting Multi-Agent Pipelines for Structured Regulatory Information Extraction

- **Authors:** Mohammed Ali, Abdelrahman Abdallah, Adam Jatowt
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12054v1](http://arxiv.org/abs/2604.12054v1)
- **PDF:** [https://arxiv.org/pdf/2604.12054v1](https://arxiv.org/pdf/2604.12054v1)
- **Categories:** cs.MA


> The paper introduces **RegReAct**, a self‑correcting multi‑agent pipeline that tackles the extraction of hierarchical, machine‑readable compliance criteria from complex regulatory texts. The system splits the task into seven specialized agents that iteratively **Observe → Diagnose → Repair** their outputs, validating against the source document, fixing model hallucinations, and repairing cross‑reference errors; it also builds a typed criterion graph and resolves external legal dependencies by retrieving and summarizing referenced content. Experiments on three EU Taxonomy Delegated Acts (covering 242 activities and >4,800 criteria) show that RegReAct significantly outperforms a strong GPT‑4o single‑pass baseline on structural correctness, semantic fidelity, and completeness, demonstrating the value of agentic, self‑correcting loops for reliable regulatory information extraction.


<details>
<summary>Abstract</summary>

Extracting structured, machine-readable compliance criteria from regulatory documents remains an open challenge. Single-pass language models hallucinate structural elements, lose hierarchical relationships, and fail to resolve inter-document dependencies. We introduce \textsc{RegReAct}, a self-correcting multi-agent framework that decomposes regulatory information extraction into seven specialized stages, each with an \textit{Observe--Diagnose--Repair} (ODR) loop that validates outputs against the source, correcting not only model hallucinations but also cross-reference errors in the regulations themselves. To ensure structural accuracy, \textsc{RegReAct} constructs a typed criterion graph; to ensure completeness, it resolves external dependencies by retrieving, summarizing, and embedding referenced legal content inline, producing self-contained outputs. Applying \textsc{RegReAct} to three EU Taxonomy Delegated Acts, we construct a dataset comprising 242 activities with over 4,800 hierarchical criteria, thresholds, and enriched source summaries. Evaluation against a GPT-4o single-pass baseline confirms that \textsc{RegReAct} outperforms it across all structural and semantic metrics. Code and data will be made publicly available: https://github.com/RECOR-Benchmark/RECOR

</details>


### 127. A longitudinal health agent framework

- **Authors:** Georgianna "Blue" Lin, Rencong Jiang, Noémie Elhadad, Xuhai "Orson" Xu
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.12019v2](http://arxiv.org/abs/2604.12019v2)
- **PDF:** [https://arxiv.org/pdf/2604.12019v2](https://arxiv.org/pdf/2604.12019v2)
- **Categories:** cs.AI, cs.HC


> **Main contribution**: The paper introduces a multi‑layer framework and accompanying agent architecture specifically designed to enable AI health agents to operate over long‑term, multi‑session interactions, emphasizing adaptation, coherence, continuity, and user agency.  

**Methodology**: Building on clinical and personal health informatics models, the authors formalize longitudinal health interaction requirements, then instantiate an agent system that integrates goal‑tracking, context‑aware reasoning, and accountability mechanisms. They illustrate the design with several realistic health‑task use cases (e.g., symptom monitoring, behavior‑change coaching).  

**Key findings**: Simulated/illustrative deployments show that the proposed architecture can sustain meaningful engagement, dynamically adjust to evolving user goals, and preserve safety through continuous alignment checks, highlighting both the potential and the design complexity of truly longitudinal, user‑centered health AI agents.


<details>
<summary>Abstract</summary>

Although artificial intelligence (AI) agents are increasingly proposed to support potentially longitudinal health tasks, such as symptom management, behavior change, and patient support, most current implementations fall short of facilitating user intent and fostering accountability. This contrasts with prior work on supporting longitudinal needs, where follow-up, coherent reasoning, and sustained alignment with individuals' goals are critical for both effectiveness and safety. In this paper, we draw on established clinical and personal health informatics frameworks to define what it would mean to orchestrate longitudinal health interactions with AI agents. We propose a multi-layer framework and corresponding agent architecture that operationalizes adaptation, coherence, continuity, and agency across repeated interactions. Through representative use cases, we demonstrate how longitudinal agents can maintain meaningful engagement, adapt to evolving goals, and support safe, personalized decision-making over time. Our findings underscore both the promise and the complexity of designing systems capable of supporting health trajectories beyond isolated interactions, and we offer guidance for future research and development in multi-session, user-centered health AI.

</details>


### 128. Narrative-Driven Paper-to-Slide Generation via ArcDeck

- **Authors:** Tarik Can Ozden, Sachidanand VS, Furkan Horoz, Ozgur Kara, Junho Kim, James Matthew Rehg
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11969v1](http://arxiv.org/abs/2604.11969v1)
- **PDF:** [https://arxiv.org/pdf/2604.11969v1](https://arxiv.org/pdf/2604.11969v1)
- **Categories:** cs.AI


> **Paper → Slide Generation with ArcDeck**  
ArcDeck advances paper‑to‑slide generation by framing it as a structured narrative reconstruction problem rather than a flat summarization. The system first parses a scientific article into a discourse tree and a “global commitment” document that capture the paper’s logical hierarchy; these priors then drive a cycle of role‑specific agents (e.g., outline maker, critic, designer) that iteratively critique and refine the slide outline before producing the final visual layout. Evaluation on the newly released ArcBench benchmark shows that this discourse‑aware, multi‑agent pipeline yields presentations with markedly better narrative flow and logical coherence than prior end‑to‑end baselines, highlighting the value of explicit structural modeling for agentic AI in scientific communication.


<details>
<summary>Abstract</summary>

We introduce ArcDeck, a multi-agent framework that formulates paper-to-slide generation as a structured narrative reconstruction task. Unlike existing methods that directly summarize raw text into slides, ArcDeck explicitly models the source paper's logical flow. It first parses the input to construct a discourse tree and establish a global commitment document, ensuring the high-level intent is preserved. These structural priors then guide an iterative multi-agent refinement process, where specialized agents iteratively critique and revise the presentation outline before rendering the final visual layouts and designs. To evaluate our approach, we also introduce ArcBench, a newly curated benchmark of academic paper-slide pairs. Experimental results demonstrate that explicit discourse modeling, combined with role-specific agent coordination, significantly improves the narrative flow and logical coherence of the generated presentations.

</details>


### 129. Agentic LLM Reasoning in a Self-Driving Laboratory for Air-Sensitive Lithium Halide Spinel Conductors

- **Authors:** Yuxing Fei, Bernardus Rendy, Xiaochen Yang, Junhee Woo, Xu Huang, Chang Li, Shilong Wang, David Milsted, Yan Zeng, Gerbrand Ceder
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11957v1](http://arxiv.org/abs/2604.11957v1)
- **PDF:** [https://arxiv.org/pdf/2604.11957v1](https://arxiv.org/pdf/2604.11957v1)
- **Categories:** cond-mat.mtrl-sci, cs.LG


> The paper introduces **A‑Lab GPSS**, a glove‑box‑integrated self‑driving laboratory that couples a robotic solid‑state synthesis/characterization workstation with an **agentic LLM** that performs abductive and inductive reasoning to generate experimental proposals. Using this framework, the system autonomously explored 352 lithium‑halide spinel compositions—including 72 % of the 171 possible metal‑pair combinations—and increased the hit‑rate for high‑conductivity, phase‑pure materials from 1.33 % to 5.33 % over the campaign. Analysis of the LLM’s internal reasoning revealed that **abductive cycles** focused on explaining outlier results in known regions, while **inductive cycles** drove broader, exploratory jumps, demonstrating complementary strategies for autonomous discovery of air‑sensitive solid‑state materials.


<details>
<summary>Abstract</summary>

Self-driving laboratories promise to accelerate materials discovery. Yet current automated solid-state synthesis platforms are limited to ambient conditions, thereby precluding their use for air-sensitive materials. Here, we present A-Lab for Glovebox Powder Solid-state Synthesis (A-Lab GPSS), a robotic platform capable of synthesizing and characterizing air-sensitive inorganic materials under strict air-free conditions. By integrating an agentic AI framework into the A-Lab GPSS platform, we structure autonomous experimental design through abductive and inductive reasoning. We deploy this platform to explore the vast compositional space of lithium halide spinel solid-state ionic conductors. Across a synthesis campaign comprising 352 samples with diverse compositions, the system explores a broad chemical space, experimentally realizing 72% of the 171 possible pairwise combinations among the 19 metals considered in this study. Over the course of the campaign, the fraction of compositions exhibiting both good ionic conductivity (> 0.05 mS/cm) and high halide spinel phase purity increases from 1.33% in the first 75 agent-proposed samples to 5.33% in the final 75. Furthermore, by inspecting the AI's reasoning processes, we reveal distinct yet complementary discovery strategies: abductive reasoning interrogates abnormal observations within already explored regions, whereas inductive reasoning expands the search into broader, previously unvisited chemical space. This work establishes a scalable platform for the autonomous discovery of complex, air-sensitive solid-state materials.

</details>


### 130. AnyPoC: Universal Proof-of-Concept Test Generation for Scalable LLM-Based Bug Detection

- **Authors:** Zijie Zhao, Chenyuan Yang, Weidong Wang, Yihan Yang, Ziqi Zhang, Lingming Zhang
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11950v1](http://arxiv.org/abs/2604.11950v1)
- **PDF:** [https://arxiv.org/pdf/2604.11950v1](https://arxiv.org/pdf/2604.11950v1)
- **Categories:** cs.SE, cs.AI, cs.CL, cs.CR


> The paper introduces **AnyPoC**, a multi‑agent framework that turns static LLM‑generated bug reports into executable proof‑of‑concept (PoC) tests, thereby providing an automated validation oracle for large‑scale bug detection. By decomposing the task into fact‑checking, iterative PoC synthesis with live execution feedback, and independent re‑execution to filter hallucinations and reward‑hacking, AnyPoC builds and continuously refines a PoC knowledge base that works with any upstream bug reporter. Evaluated on 12 major codebases, AnyPoC validates 1.3 × more true‑positive reports and rejects 9.8 × more false positives than prior coding agents, leading to the discovery of 122 new bugs (105 confirmed) and the adoption of 45 PoCs as official regression tests.


<details>
<summary>Abstract</summary>

While recent LLM-based agents can identify many candidate bugs in source code, their reports remain static hypotheses that require manual validation, limiting the practicality of automated bug detection. We frame this challenge as a test generation task: given a candidate report, synthesizing an executable proof-of-concept test, or simply a PoC - such as a script, command sequence, or crafted input - to trigger the suspected defect. Automated PoC generation can act as a scalable validation oracle, enabling end-to-end autonomous bug detection by providing concrete execution evidence. However, naive LLM agents are unreliable validators: they are biased toward "success" and may reward-hack by producing plausible but non-functional PoCs or even hallucinated traces. To address this, we present AnyPoC, a general multi-agent framework that (1) analyzes and fact-checks a candidate bug report, (2) iteratively synthesizes and executes a PoC while collecting execution traces, and (3) independently re-executes and scrutinizes the PoC to mitigate hallucination and reward hacking. In addition, AnyPoC also continuously extracts and evolves a PoC knowledge base to handle heterogeneous tasks. AnyPoC operates on candidate bug reports regardless of their source and can be paired with different bug reporters. To demonstrate practicality and generality, we apply AnyPoC, with a simple agentic bug reporter, on 12 critical software systems across diverse languages/domains (many with millions of lines of code) including Firefox, Chromium, LLVM, OpenSSL, SQLite, FFmpeg, and Redis. Compared to the state-of-the-art coding agents, e.g., Claude Code and Codex, AnyPoC produces 1.3x more valid PoCs for true-positive bug reports and rejects 9.8x more false-positive bug reports. To date, AnyPoC has discovered 122 new bugs (105 confirmed, 86 already fixed), with 45 generated PoCs adopted as official regression tests.

</details>


### 131. AutoSurrogate: An LLM-Driven Multi-Agent Framework for Autonomous Construction of Deep Learning Surrogate Models in Subsurface Flow

- **Authors:** Jiale Liu, Nanzhe Wang
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11945v1](http://arxiv.org/abs/2604.11945v1)
- **PDF:** [https://arxiv.org/pdf/2604.11945v1](https://arxiv.org/pdf/2604.11945v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> The paper introduces **AutoSurrogate**, a novel multi‑agent framework powered by large language models that lets non‑ML experts automatically generate high‑performance deep‑learning surrogates for subsurface‑flow simulations. By interpreting a single natural‑language instruction, four coordinated agents handle data profiling, model‑architecture selection from a curated zoo, Bayesian hyper‑parameter optimization, training, and validation, while autonomously recovering from common failures (e.g., numerical instabilities or poor accuracy). Applied to a 3‑D geological carbon‑storage benchmark, AutoSurrogate produces deployment‑ready surrogates that surpass both expert‑crafted baselines and generic AutoML tools, highlighting its potential to democratize surrogate modeling in agentic AI workflows.


<details>
<summary>Abstract</summary>

High-fidelity numerical simulation of subsurface flow is computationally intensive, especially for many-query tasks such as uncertainty quantification and data assimilation. Deep learning (DL) surrogates can significantly accelerate forward simulations, yet constructing them requires substantial machine learning (ML) expertise - from architecture design to hyperparameter tuning - that most domain scientists do not possess. Furthermore, the process is predominantly manual and relies heavily on heuristic choices. This expertise gap remains a key barrier to the broader adoption of DL surrogate techniques. For this reason, we present AutoSurrogate, a large-language-model-driven multi-agent framework that enables practitioners without ML expertise to build high-quality surrogates for subsurface flow problems through natural-language instructions. Given simulation data and optional preferences, four specialized agents collaboratively execute data profiling, architecture selection from a model zoo, Bayesian hyperparameter optimization, model training, and quality assessment against user-specified thresholds. The system also handles common failure modes autonomously, including restarting training with adjusted configurations when numerical instabilities occur and switching to alternative architectures when predictive accuracy falls short of targets. In our setting, a single natural-language sentence can be sufficient to produce a deployment-ready surrogate model, with minimum human intervention required at any intermediate stage. We demonstrate the utility of AutoSurrogate on a 3D geological carbon storage modeling task, mapping permeability fields to pressure and CO$_2$ saturation fields over 31 timesteps. Without any manual tuning, AutoSurrogate is able to outperform expert-designed baselines and domain-agnostic AutoML methods, demonstrating strong potential for practical deployment.

</details>


### 132. ClawGuard: A Runtime Security Framework for Tool-Augmented LLM Agents Against Indirect Prompt Injection

- **Authors:** Wei Zhao, Zhe Li, Peixin Zhang, Jun Sun
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11790v1](http://arxiv.org/abs/2604.11790v1)
- **PDF:** [https://arxiv.org/pdf/2604.11790v1](https://arxiv.org/pdf/2604.11790v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **ClawGuard**, a runtime security layer that protects tool‑augmented LLM agents from indirect prompt‑injection attacks by enforcing a user‑confirmed rule set at every tool‑call boundary. The system automatically extracts task‑specific access constraints from the user’s original objective and uses them to vet all tool outputs before they are incorporated into the agent’s memory, thereby blocking malicious content injected via web/local data, MCP servers, or skill files without any model fine‑tuning or architectural changes. Empirical evaluation on five leading LLM agents across the AgentDojo, SkillInject, and MCPSafeBench benchmarks shows that ClawGuard eliminates all three injection vectors while preserving the agents’ task performance, demonstrating that deterministic, policy‑driven tool‑call enforcement is an effective defense for secure, agentic AI.


<details>
<summary>Abstract</summary>

Tool-augmented Large Language Model (LLM) agents have demonstrated impressive capabilities in automating complex, multi-step real-world tasks, yet remain vulnerable to indirect prompt injection. Adversaries exploit this weakness by embedding malicious instructions within tool-returned content, which agents directly incorporate into their conversation history as trusted observations. This vulnerability manifests across three primary attack channels: web and local content injection, MCP server injection, and skill file injection. To address these vulnerabilities, we introduce \textsc{ClawGuard}, a novel runtime security framework that enforces a user-confirmed rule set at every tool-call boundary, transforming unreliable alignment-dependent defense into a deterministic, auditable mechanism that intercepts adversarial tool calls before any real-world effect is produced. By automatically deriving task-specific access constraints from the user's stated objective prior to any external tool invocation, \textsc{ClawGuard} blocks all three injection pathways without model modification or infrastructure change. Experiments across five state-of-the-art language models on AgentDojo, SkillInject, and MCPSafeBench demonstrate that \textsc{ClawGuard} achieves robust protection against indirect prompt injection without compromising agent utility. This work establishes deterministic tool-call boundary enforcement as an effective defense mechanism for secure agentic AI systems, requiring neither safety-specific fine-tuning nor architectural modification. Code is publicly available at https://github.com/Claw-Guard/ClawGuard.

</details>


### 133. GenTac: Generative Modeling and Forecasting of Soccer Tactics

- **Authors:** Jiayuan Rao, Tianlin Gui, Haoning Wu, Yanfeng Wang, Weidi Xie
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11786v1](http://arxiv.org/abs/2604.11786v1)
- **PDF:** [https://arxiv.org/pdf/2604.11786v1](https://arxiv.org/pdf/2604.11786v1)
- **Categories:** cs.AI, cs.MA


> **Contribution:** The paper introduces **GenTac**, a diffusion‑based generative model that treats open‑play soccer tactics as a stochastic process over continuous multi‑agent trajectories together with discrete tactical events, enabling the production of diverse, high‑fidelity future play sequences rather than a single deterministic prediction.

**Methodology:** GenTac learns the joint distribution of player motions from large‑scale tracking data via a diffusion architecture, incorporates rich conditional inputs (opponent behavior, team/league style, strategic objectives), and maps continuous trajectories onto a 15‑class semantic event space; its performance is evaluated on the new **TacBench** benchmark and transferred to other team sports.

**Key Findings:** GenTac attains state‑of‑the‑art geometric accuracy while preserving team structural coherence, captures stylistic differences across teams and leagues, supports controllable counterfactual simulations that modify spatial control and threat metrics, and can reliably forecast downstream tactical outcomes—all demonstrating a scalable, controllable generative approach for agentic AI in multi‑agent, stochastic environments.


<details>
<summary>Abstract</summary>

Modeling open-play soccer tactics is a formidable challenge due to the stochastic, multi-agent nature of the game. Existing computational approaches typically produce single, deterministic trajectory forecasts or focus on highly structured set-pieces, fundamentally failing to capture the inherent variance and branching possibilities of real-world match evolution. Here, we introduce GenTac, a diffusion-based generative framework that conceptualizes soccer tactics as a stochastic process over continuous multi-player trajectories and discrete semantic events. By learning the underlying distribution of player movements from historical tracking data, GenTac samples diverse, plausible, long-horizon future trajectories. The framework supports rich contextual conditioning, including opponent behavior, specific team or league playing styles, and strategic objectives, while grounding continuous spatial dynamics into a 15-class tactical event space. Extensive evaluations on our proposed benchmark, TacBench, demonstrate four key capabilities: (1) GenTac achieves high geometric accuracy while strictly preserving the collective structural consistency of the team; (2) it accurately simulates stylistic nuances, distinguishing between specific teams (e.g., Auckland FC) and leagues (e.g., A-League versus German leagues); (3) it enables controllable counterfactual simulations, demonstrably altering spatial control and expected threat metrics based on offensive or defensive guidance; and (4) it reliably anticipates future tactical outcomes directly from generated rollouts. Finally, we demonstrate that GenTac can be successfully trained to generalize to other dynamic team sports, including basketball, American football, and ice hockey.

</details>


### 134. $λ_A$: A Typed Lambda Calculus for LLM Agent Composition

- **Authors:** Qin Liu
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11767v2](http://arxiv.org/abs/2604.11767v2)
- **PDF:** [https://arxiv.org/pdf/2604.11767v2](https://arxiv.org/pdf/2604.11767v2)
- **Categories:** cs.PL, cs.MA, cs.SE


> The paper introduces **λ_A**, a formally‑typed lambda calculus that models the composition of LLM‑driven agents. By extending the simply‑typed λ‑calculus with oracle calls, bounded fixpoints (capturing the ReAct reasoning loop), probabilistic choice, and mutable environments, the authors give precise operational semantics, prove type safety and termination of the bounded loops, and mechanise the whole development in Coq (1,519 lines, 42 theorems, no admitted proofs). Leveraging these semantics they derive a linting tool that automatically detects structural errors in real‑world agent configurations; applied to 835 GitHub configs, it finds that 94 % are incomplete, with detection precision rising from 54 % (YAML‑only) to 96–100 % when combining YAML with Python ASTs, and they further demonstrate that five popular LLM‑agent frameworks (LangGraph, CrewAI, AutoGen, OpenAI SDK, Dify) are each embeddable as typed fragments of λ_A, establishing it as a unifying formal foundation for agentic AI systems.


<details>
<summary>Abstract</summary>

Existing LLM agent frameworks lack formal semantics: there is no principled way to determine whether an agent configuration is well-formed or will terminate. We present $λ_A$, a typed lambda calculus for agent composition that extends the simply-typed lambda calculus with oracle calls, bounded fixpoints (the ReAct loop), probabilistic choice, and mutable environments. We prove type safety, termination of bounded fixpoints, and soundness of derived lint rules, with full Coq mechanization (1,519 lines, 42 theorems, 0 Admitted). As a practical application, we derive a lint tool that detects structural configuration errors directly from the operational semantics. An evaluation on 835 real-world GitHub agent configurations shows that 94.1% are structurally incomplete under $λ_A$, with YAML-only lint precision at 54%, rising to 96--100% under joint YAML+Python AST analysis on 175 samples. This gap quantifies, for the first time, the degree of semantic entanglement between declarative configuration and imperative code in the agent ecosystem. We further show that five mainstream paradigms (LangGraph, CrewAI, AutoGen, OpenAI SDK, Dify) embed as typed $λ_A$ fragments, establishing $λ_A$ as a unifying calculus for LLM agent composition.

</details>


### 135. Retrieval Is Not Enough: Why Organizational AI Needs Epistemic Infrastructure

- **Authors:** Federico Bottino, Carlo Ferrero, Nicholas Dosio, Pierfrancesco Beneventano
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11759v1](http://arxiv.org/abs/2604.11759v1)
- **PDF:** [https://arxiv.org/pdf/2604.11759v1](https://arxiv.org/pdf/2604.11759v1)
- **Categories:** cs.AI


> The paper introduces OIDA, a novel “Epistemic Infrastructure” framework that augments organizational knowledge bases with typed Knowledge Objects annotated by commitment strength, contradiction status, and ignorance markers, and a deterministic Knowledge‑Gravity Engine that maintains importance scores with provable convergence. By treating unanswered questions as first‑class primitives (the QUESTION mechanism) that decay inversely and surface organizational ignorance, OIDA enables AI agents to reason about what is known, disputed, or unknown rather than merely retrieving semantically similar text. In controlled experiments OIDA’s retrieval‑augmented generation achieves comparable epistemic quality to a full‑context baseline while using ≈ 1/30 of the tokens, and the QUESTION mechanism is shown to significantly increase the likelihood of surfacing unknowns (Fisher p = 0.0325, OR = 21.0).


<details>
<summary>Abstract</summary>

Organizational knowledge used by AI agents typically lacks epistemic structure: retrieval systems surface semantically relevant content without distinguishing binding decisions from abandoned hypotheses, contested claims from settled ones, or known facts from unresolved questions. We argue that the ceiling on organizational AI is not retrieval fidelity but \emph{epistemic} fidelity--the system's ability to represent commitment strength, contradiction status, and organizational ignorance as computable properties.
  We present OIDA, a framework that structures organizational knowledge as typed Knowledge Objects carrying epistemic class, importance scores with class-specific decay, and signed contradiction edges. The Knowledge Gravity Engine maintains scores deterministically with proved convergence guarantees (sufficient condition: max degree $< 7$; empirically robust to degree 43). OIDA introduces QUESTION-as-modeled-ignorance: a primitive with inverse decay that surfaces what an organization does \emph{not} know with increasing urgency--a mechanism absent from all surveyed systems. We describe the Epistemic Quality Score (EQS), a five-component evaluation methodology with explicit circularity analysis. In a controlled comparison ($n{=}10$ response pairs), OIDA's RAG condition (3,868 tokens) achieves EQS 0.530 vs.\ 0.848 for a full-context baseline (108,687 tokens); the $28.1\times$ token budget difference is the primary confound. The QUESTION mechanism is statistically validated (Fisher $p{=}0.0325$, OR$=21.0$). The formal properties are established; the decisive ablation at equal token budget (E4) is pre-registered and not yet run.

</details>


### 136. Collaborative Multi-Agent Scripts Generation for Enhancing Imperfect-Information Reasoning in Murder Mystery Games

- **Authors:** Keyang Zhong, Junlin Xie, Hefeng Wu, Haofeng Li, Guanbin Li
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11741v1](http://arxiv.org/abs/2604.11741v1)
- **PDF:** [https://arxiv.org/pdf/2604.11741v1](https://arxiv.org/pdf/2604.11741v1)
- **Categories:** cs.AI


> The paper introduces a collaborative multi‑agent framework that automatically creates role‑specific, multimodal scripts for murder‑mystery games, providing a controllable testbed for evaluating vision‑language models (VLMs) under imperfect‑information and deceptive conditions. The authors train VLMs in two stages: (1) chain‑of‑thought fine‑tuning on curated and synthetically generated datasets that encode uncertainty and deception, and (2) GRPO‑based reinforcement learning with agent‑monitored reward shaping that enforces character‑consistent reasoning across multimodal clues. Experiments show that this pipeline markedly improves VLM performance on narrative reasoning, hidden‑fact extraction, and deception‑robust understanding, establishing a scalable benchmark for agentic AI systems operating in socially complex, adversarial environments.


<details>
<summary>Abstract</summary>

Vision-language models (VLMs) have shown impressive capabilities in perceptual tasks, yet they degrade in complex multi-hop reasoning under multiplayer game settings with imperfect and deceptive information. In this paper, we study a representative multiplayer task, Murder Mystery Games, which require inferring hidden truths based on partial clues provided by roles with different intentions. To address this challenge, we propose a collaborative multi-agent framework for evaluating and synthesizing high-quality, role-driven multiplayer game scripts, enabling fine-grained interaction patterns tailored to character identities (i.e., murderer vs. innocent). Our system generates rich multimodal contexts, including character backstories, visual and textual clues, and multi-hop reasoning chains, through coordinated agent interactions. We design a two-stage agent-monitored training strategy to enhance the reasoning ability of VLMs: (1) chain-of-thought based fine-tuning on curated and synthetic datasets that model uncertainty and deception; (2) GRPO-based reinforcement learning with agent-monitored reward shaping, encouraging the model to develop character-specific reasoning behaviors and effective multimodal multi-hop inference. Extensive experiments demonstrate that our method significantly boosts the performance of VLMs in narrative reasoning, hidden fact extraction, and deception-resilient understanding. Our contributions offer a scalable solution for training and evaluating VLMs under uncertain, adversarial, and socially complex conditions, laying the groundwork for future benchmarks in multimodal multi-hop reasoning under imperfect information.

</details>


### 137. Multi-ORFT: Stable Online Reinforcement Fine-Tuning for Multi-Agent Diffusion Planning in Cooperative Driving

- **Authors:** Haojie Bai, Aimin Li, Ruoyu Yao, Xiongwei Zhao, Tingting Zhang, Xing Zhang, Lin Gao, and Jun Ma
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11734v2](http://arxiv.org/abs/2604.11734v2)
- **PDF:** [https://arxiv.org/pdf/2604.11734v2](https://arxiv.org/pdf/2604.11734v2)
- **Categories:** cs.RO, cs.AI


> **Main contribution** – The paper introduces **Multi‑ORFT**, a two‑stage framework that first pre‑trains a scene‑conditioned diffusion planner for multimodal joint trajectories of cooperative drivers, then fine‑tunes it online with a novel reinforcement‑learning loop that leverages the diffusion reverse‑kernel likelihoods.  

**Methodology** – In the pre‑training phase the model augments a diffusion backbone with inter‑agent self‑attention, cross‑attention to a scene encoder, and AdaLN‑Zero conditioning to enforce road‑geometry consistency. For online post‑training, a **two‑level MDP** exposes step‑wise diffusion likelihoods; a dense trajectory reward (safety, efficiency) is optimized using **variance‑gated group‑relative policy optimization (VG‑GRPO)**, which stabilizes the otherwise noisy diffusion‑policy updates.  

**Key findings** – On the closed‑loop Waymo Open Motion Dataset benchmark, Multi‑ORFT lowers collision and off‑road rates (2.04 %→1.89 % and 1.68 %→1.36 %) and raises average speed (8.36 → 8.61 m/s) versus the pre‑trained baseline, outperforming strong open‑source diffusion planners (SMART, VBD). These results demonstrate that coupling scene‑aware diffusion generation with stable online reinforcement fine‑tuning yields safer, more efficient multi‑agent driving policies, a promising direction for agentic AI in real‑time autonomous systems.


<details>
<summary>Abstract</summary>

Closed-loop cooperative driving requires planners that generate realistic multimodal multi-agent trajectories while improving safety and traffic efficiency. Existing diffusion planners can model multimodal behaviors from demonstrations, but they often exhibit weak scene consistency and remain poorly aligned with closed-loop objectives; meanwhile, stable online post-training in reactive multi-agent environments remains difficult. We present Multi-ORFT, which couples scene-conditioned diffusion pre-training with stable online reinforcement post-training. In pre-training, the planner uses inter-agent self-attention, cross-attention, and AdaLN-Zero-based scene conditioning to improve scene consistency and road adherence of joint trajectories. In post-training, we formulate a two-level MDP that exposes step-wise reverse-kernel likelihoods for online optimization, and combine dense trajectory-level rewards with variance-gated group-relative policy optimization (VG-GRPO) to stabilize training. On the WOMD closed-loop benchmark, Multi-ORFT reduces collision rate from 2.04% to 1.89% and off-road rate from 1.68% to 1.36%, while increasing average speed from 8.36 to 8.61 m/s relative to the pre-trained planner, and it outperforms strong open-source baselines including SMART-large, SMART-tiny-CLSFT, and VBD on the primary safety and efficiency metrics. These results show that coupling scene-consistent denoising with stable online diffusion-policy optimization improves the reliability of closed-loop cooperative driving.

</details>


### 138. Evaluating Cooperation in LLM Social Groups through Elected Leadership

- **Authors:** Ryan Faulkner, Anushka Deshpande, David Guzman Piedrahita, Joel Z. Leibo, Zhijing Jin
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11721v1](http://arxiv.org/abs/2604.11721v1)
- **PDF:** [https://arxiv.org/pdf/2604.11721v1](https://arxiv.org/pdf/2604.11721v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> The paper introduces an open‑source simulation framework that equips Large Language Model (LLM) agents with elected, persona‑based leaders and candidate‑driven agendas, enabling systematic study of election‑based governance in common‑pool resource games. By running controlled multi‑agent experiments across several high‑performing LLMs, the authors show that the presence of elected leadership raises collective welfare scores by ≈ 55 % and more than doubles agents’ survival time, while graph‑theoretic centrality and sentiment analyses reveal that elected leaders exert measurable influence and adopt more cooperative rhetoric. These results demonstrate that structured, election‑driven leadership can substantially improve cooperation and social welfare in agentic AI systems.


<details>
<summary>Abstract</summary>

Governing common-pool resources requires agents to develop enduring strategies through cooperation and self-governance to avoid collective failure. While foundation models have shown potential for cooperation in these settings, existing multi-agent research provides little insight into whether structured leadership and election mechanisms can improve collective decision making. The lack of such a critical organizational feature ubiquitous in human society presents a significant shortcoming of the current methods. In this work we aim to directly address whether leadership and elections can support improved social welfare and cooperation through multi-agent simulation with LLMs. We present our open-source framework that simulates leadership through elected personas and candidate-driven agendas and carry out an empirical study of LLMs under controlled governance conditions. Our experiments demonstrate that having elected leadership improves social welfare scores by 55.4% and survival time by 128.6% across a range of high performing LLMs. Through the construction of an agent social graph we compute centrality metrics to assess the social influence of leader personas and also analyze rhetorical and cooperative tendencies revealed through a sentiment analysis on leader utterances. This work lays the foundation for further study of election mechanisms in multi-agent systems toward navigating complex social dilemmas.

</details>


### 139. SWE-AGILE: A Software Agent Framework for Efficiently Managing Dynamic Reasoning Context

- **Authors:** Shuquan Lian, Juncheng Liu, Yazhe Chen, Yuhong Chen, Hui Li
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11716v1](http://arxiv.org/abs/2604.11716v1)
- **PDF:** [https://arxiv.org/pdf/2604.11716v1](https://arxiv.org/pdf/2604.11716v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution:** SWE‑AGILE proposes a novel agent framework that reconciles deep System‑2 reasoning with the tight context limits of large language models in autonomous software‑engineering tasks.  

**Methodology:** The framework implements a *Dynamic Reasoning Context* mechanism that keeps a sliding window of the most recent detailed chain‑of‑thought steps for continuity while compressing older reasoning into compact “Reasoning Digests.” This prevents both context explosion (“Lost‑in‑the‑Middle”) and unnecessary re‑reasoning at each turn.  

**Key findings:** On the SWE‑Bench‑Verified benchmark, SWE‑AGILE achieves state‑of‑the‑art performance for 7‑8 B parameter models using only 2.2 k evaluation trajectories across 896 tasks, demonstrating that selective context retention dramatically improves reasoning depth and efficiency for agentic AI in software development.


<details>
<summary>Abstract</summary>

Prior representative ReAct-style approaches in autonomous Software Engineering (SWE) typically lack the explicit System-2 reasoning required for deep analysis and handling complex edge cases. While recent reasoning models demonstrate the potential of extended Chain-of-Thought (CoT), applying them to the multi-turn SWE task creates a fundamental dilemma: retaining full reasoning history leads to context explosion and ``Lost-in-the-Middle'' degradation, while discarding it would force the agent to redundantly re-reason at every step. To address these challenges, we propose SWE-AGILE, a novel software agent framework designed to bridge the gap between reasoning depth, efficiency, and context constraints. SWE-AGILE introduces a Dynamic Reasoning Context strategy, maintaining a ``sliding window'' of detailed reasoning for immediate continuity to prevent redundant re-analyzing, while compressing historical reasoning content into concise Reasoning Digests. Empirically, SWE-AGILE sets a new standard for 7B-8B models on SWE-Bench-Verified using only 2.2k trajectories and 896 tasks. Code is available at https://github.com/KDEGroup/SWE-AGILE.

</details>


### 140. Agentic Driving Coach: Robustness and Determinism of Agentic AI-Powered Human-in-the-Loop Cyber-Physical Systems

- **Authors:** Deeksha Prahlad, Daniel Fan, Hokeun Kim
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11705v1](http://arxiv.org/abs/2604.11705v1)
- **PDF:** [https://arxiv.org/pdf/2604.11705v1](https://arxiv.org/pdf/2604.11705v1)
- **Categories:** cs.AI, cs.CL, cs.RO, eess.SY


> The paper introduces a deterministic, reactor‑model‑of‑computation framework for building human‑in‑the‑loop cyber‑physical systems (HITL‑CPS) that are driven by foundation‑model agents (e.g., LLM‑based “agentic” AIs). By implementing the architecture in the open‑source Lingua Franca (LF) language, the authors construct an “agentic driving coach” prototype and evaluate its robustness to nondeterministic user behavior and dynamic physical conditions. Their experiments reveal concrete sources of nondeterminism (e.g., asynchronous LLM calls, uncontrolled human inputs) and demonstrate that LF’s logical‑time, event‑driven reactors can substantially restore determinism, paving the way for reliable, safety‑critical agentic AI deployments in CPS.


<details>
<summary>Abstract</summary>

Foundation models, including large language models (LLMs), are increasingly used for human-in-the-loop (HITL) cyber-physical systems (CPS) because foundation model-based AI agents can potentially interact with both the physical environments and human users. However, the unpredictable behavior of human users and AI agents, in addition to the dynamically changing physical environments, leads to uncontrollable nondeterminism. To address this urgent challenge of enabling agentic AI-powered HITL CPS, we propose a reactor-model-of-computation (MoC)-based approach, realized by the open-source Lingua Franca (LF) framework. We also carry out a concrete case study using the agentic driving coach as an application of HITL CPS. By evaluating the LF-based agentic HITL CPS, we identify practical challenges in reintroducing determinism into such agentic HITL CPS and present pathways to address them.

</details>


### 141. Towards Autonomous Mechanistic Reasoning in Virtual Cells

- **Authors:** Yunhui Jang, Lu Zhu, Jake Fawkes, Alisandra Kaye Denton, Dominique Beaini, Emmanuel Noutahi
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11661v2](http://arxiv.org/abs/2604.11661v2)
- **PDF:** [https://arxiv.org/pdf/2604.11661v2](https://arxiv.org/pdf/2604.11661v2)
- **Categories:** cs.LG, cs.AI


> **Main contribution:** The paper presents a new formalism for encoding biological reasoning as *mechanistic action graphs* and introduces **VCR‑Agent**, a multi‑agent system that retrieves grounded knowledge, generates mechanistic explanations for virtual cells, and automatically verifies them. It also releases the **VC‑TRACES** dataset of verified mechanistic explanations derived from the Tahoe‑100M cellular atlas.  

**Methodology:** VCR‑Agent orchestrates several specialized agents (retriever, generator, verifier) that work over the action‑graph formalism; explanations are produced, then filtered through a verifier that checks consistency with known biological constraints, enabling systematic falsification. The verified traces are used to fine‑tune LLMs.  

**Key findings:** Models trained on VC‑TRACES achieve markedly higher factual precision in cellular reasoning tasks and provide a stronger supervision signal for downstream gene‑expression prediction, demonstrating that integrating multi‑agent generation with rigorous verification yields more reliable, actionable mechanistic reasoning for agentic AI in biology.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have recently gained significant attention as a promising approach to accelerate scientific discovery. However, their application in open-ended scientific domains such as biology remains limited, primarily due to the lack of factually grounded and actionable explanations. To address this, we introduce a structured explanation formalism for virtual cells that represents biological reasoning as mechanistic action graphs, enabling systematic verification and falsification. Building upon this, we propose VCR-Agent, a multi-agent framework that integrates biologically grounded knowledge retrieval with a verifier-based filtering approach to generate and validate mechanistic reasoning autonomously. Using this framework, we release VC-TRACES dataset, which consists of verified mechanistic explanations derived from the Tahoe-100M atlas. Empirically, we demonstrate that training with these explanations improves factual precision and provides a more effective supervision signal for downstream gene expression prediction. These results underscore the importance of reliable mechanistic reasoning for virtual cells, achieved through the synergy of multi-agent and rigorous verification.

</details>


### 142. CodeTracer: Towards Traceable Agent States

- **Authors:** Han Li, Yifan Yao, Letian Zhu, Rili Feng, Hongyi Ye, Jiaming Wang, Yancheng He, Pengyu Zou, Lehan Zhang, Xinping Lei, Haoyang Huang, Ken Deng, Ming Sun, Zhaoxiang Zhang, He Ye, Jiaheng Liu
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11641v3](http://arxiv.org/abs/2604.11641v3)
- **PDF:** [https://arxiv.org/pdf/2604.11641v3](https://arxiv.org/pdf/2604.11641v3)
- **Categories:** cs.SE, cs.AI


> **Main contribution:** The paper introduces **CodeTracer**, a systematic tracing framework that captures and reconstructs the full, hierarchical state‑transition history of code‑generation agents, enabling precise localization of where a failure first occurs and how it propagates through later tool calls.

**Methodology:** CodeTracer employs a set of evolving extractors to parse heterogeneous run artifacts (logs, tool outputs, memory snapshots) from parallel and multi‑stage agent executions, builds a persistent trace tree, and applies a failure‑onset localization algorithm. The authors also create **CodeTraceBench**, a large benchmark of traced trajectories from four popular code‑agent frameworks across tasks such as bug fixing, refactoring, and terminal interaction, with staged and step‑level supervision for evaluation.

**Key findings:** Across CodeTraceBench, CodeTracer markedly outperforms baseline prompting and lightweight tracing methods in pinpointing failure origins, and its diagnostic signals enable successful replay and recovery of failed runs within comparable resource budgets, demonstrating the value of traceable agent states for debugging and reliability in agentic AI.


<details>
<summary>Abstract</summary>

Code agents are advancing rapidly, but debugging them is becoming increasingly difficult. As frameworks orchestrate parallel tool calls and multi-stage workflows over complex tasks, making the agent's state transitions and error propagation hard to observe. In these runs, an early misstep can trap the agent in unproductive loops or even cascade into fundamental errors, forming hidden error chains that make it hard to tell when the agent goes off track and why. Existing agent tracing analyses either focus on simple interaction or rely on small-scale manual inspection, which limits their scalability and usefulness for real coding workflows. We present CodeTracer, a tracing architecture that parses heterogeneous run artifacts through evolving extractors, reconstructs the full state transition history as a hierarchical trace tree with persistent memory, and performs failure onset localization to pinpoint the failure origin and its downstream chain. To enable systematic evaluation, we construct CodeTraceBench from a large collection of executed trajectories generated by four widely used code agent frameworks on diverse code tasks (e.g., bug fixing, refactoring, and terminal interaction), with supervision at both the stage and step levels for failure localization. Experiments show that CodeTracer substantially outperforms direct prompting and lightweight baselines, and that replaying its diagnostic signals consistently recovers originally failed runs under matched budgets. Our code and data are publicly available.

</details>


### 143. Context Kubernetes: Declarative Orchestration of Enterprise Knowledge for Agentic AI Systems

- **Authors:** Charafeddine Mouzouni
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11623v3](http://arxiv.org/abs/2604.11623v3)
- **PDF:** [https://arxiv.org/pdf/2604.11623v3](https://arxiv.org/pdf/2604.11623v3)
- **Categories:** cs.AI, cs.SE


> The paper presents **Context Kubernetes**, a declarative, Kubernetes‑inspired framework for managing enterprise knowledge resources that agents may access, introducing six core abstractions, a YAML “knowledge‑architecture‑as‑code” manifest, a continuous reconciliation loop, and a three‑tier permission model that guarantees every agent’s authority is a strict subset of human authority. Using a prototype and eight experiments on synthetic data, the authors show that successive governance layers (ungoverned RAG → ACL‑filtered retrieval → RBAC‑aware routing → full three‑tier model) progressively curb information leaks—ACL filtering removes cross‑domain exposure, intent routing cuts retrieval noise by 19 pp, and the full model prevents all five simulated attacks (the only remaining gap is an email‑based exfiltration that RBAC cannot detect). Formal verification with TLA+ over 4.6 M reachable states finds no safety violations, and a survey of four major cloud/enterprise platforms reveals that none currently provide comparable isolated approval channels, underscoring the novelty and practical relevance of the proposed orchestration approach for safe, scalable agentic AI.


<details>
<summary>Abstract</summary>

We introduce Context Kubernetes, an architecture for orchestrating enterprise knowledge in agentic AI systems, with a prototype implementation and eight experiments. The core observation is that delivering the right knowledge, to the right agent, with the right permissions, at the right freshness -- across an entire organization -- is structurally analogous to the container orchestration problem Kubernetes solved a decade ago. We formalize six core abstractions, a YAML-based declarative manifest for knowledge-architecture-as-code, a reconciliation loop, and a three-tier agent permission model where agent authority is always a strict subset of human authority. On synthetic seed data, we compare four governance baselines of increasing strength: ungoverned RAG, ACL-filtered retrieval, RBAC-aware routing, and the full architecture. Each layer contributes a different capability: ACL filtering eliminates cross-domain leaks, intent routing reduces noise by 19 percentage points, and only the three-tier model blocks all five tested attack scenarios -- the one attack RBAC misses is an agent sending confidential pricing via email, which RBAC cannot distinguish from ordinary email. TLA+ model-checking verifies safety properties across 4.6 million reachable states with zero violations. A survey of four major platforms (Microsoft, Salesforce, AWS, Google) documents that none architecturally isolates agent approval channels. We identify four properties that make context orchestration harder than container orchestration, and argue these make the solution more valuable.

</details>


### 144. Synthius-Mem: Brain-Inspired Hallucination-Resistant Persona Memory Achieving 94.4% Memory Accuracy and 99.6% Adversarial Robustness on LoCoMo

- **Authors:** Artem Gadzhiev, Andrew Kislov
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11563v1](http://arxiv.org/abs/2604.11563v1)
- **PDF:** [https://arxiv.org/pdf/2604.11563v1](https://arxiv.org/pdf/2604.11563v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Synthius‑Mem introduces a brain‑inspired persona‑memory architecture that replaces the usual “retrieve‑the‑raw‑dialogue” strategy with a structured extraction pipeline, classifying user information into six cognitive domains and storing deduplicated, domain‑specific facts that are later accessed via a fast CategoryRAG index. Evaluated on the LoCoMo benchmark (10 multi‑turn conversations, 1 813 probing questions), the system attains 94.4 % overall memory accuracy (core fact accuracy = 98.6 %) while cutting token usage by ~5× and achieving 99.6 % adversarial robustness—outperforming prior state‑of‑the‑art methods and human baselines. These results demonstrate that domain‑structured, biologically motivated memory can dramatically reduce hallucination and improve long‑term recall for LLM agents.


<details>
<summary>Abstract</summary>

Providing AI agents with reliable long-term memory that does not hallucinate remains an open problem. Current approaches to memory for LLM agents -- sliding windows, summarization, embedding-based RAG, and flat fact extraction -- each reduce token cost but introduce catastrophic information loss, semantic drift, or uncontrolled hallucination about the user. The structural reason is architectural: every published memory system on the LoCoMo benchmark treats conversation as a retrieval problem over raw or lightly summarized dialogue segments, and none reports adversarial robustness, the ability to refuse questions about facts the user never disclosed. We present Synthius-Mem, a brain-inspired structured persona memory system that takes a fundamentally different approach. Instead of retrieving what was said, Synthius-Mem extracts what is known about the person: a full persona extraction pipeline decomposes conversations into six cognitive domains (biography, experiences, preferences, social circle, work, psychometrics), consolidates and deduplicates per domain, and retrieves structured facts via CategoryRAG at 21.79 ms latency. On the LoCoMo benchmark (ACL 2024, 10 conversations, 1,813 questions), Synthius-Mem achieves 94.37% accuracy, exceeding all published systems including MemMachine (91.69%, adversarial score is not reported) and human performance (87.9 F1). Core memory fact accuracy reaches 98.64%. Adversarial robustness, the hallucination resistance metric that no competing system reports, reaches 99.55%. Synthius-Mem reduces token consumption by ~5x compared to full-context replay while achieving higher accuracy. Synthius-Mem achieves state-of-the-art results on LoCoMo and is, to our knowledge, the only persona memory system that both exceeds human-level performance and reports adversarial robustness.

</details>


### 145. UniToolCall: Unifying Tool-Use Representation, Data, and Evaluation for LLM Agents

- **Authors:** Yijuan Liang, Xinghao Chen, Yifan Ge, Ziyi Wu, Hao Wu, Changyu Zeng, Wei Xing, Xiaoyu Shen
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11557v1](http://arxiv.org/abs/2604.11557v1)
- **PDF:** [https://arxiv.org/pdf/2604.11557v1](https://arxiv.org/pdf/2604.11557v1)
- **Categories:** cs.AI


> The paper introduces **UniToolCall**, a comprehensive framework that standardizes every stage of tool‑use learning for large‑language‑model (LLM) agents—from assembling a curated pool of 22 k+ tools and generating a 390 k+ hybrid training corpus (mixing ten public datasets with structurally controlled synthetic trajectories) to unifying evaluation using a Query‑Action‑Observation‑Answer (QAOA) schema. By explicitly modeling interaction patterns (single‑ vs multi‑hop, single‑ vs multi‑turn, serial vs parallel execution) and adding an **Anchor Linkage** mechanism to enforce cross‑turn dependencies, the authors enable more coherent multi‑turn reasoning; fine‑tuning Qwen‑3‑8B on this data yields a 93 % single‑turn Strict Precision under the distractor‑heavy Hybrid‑20 benchmark, surpassing leading commercial agents such as GPT, Gemini, and Claude.


<details>
<summary>Abstract</summary>

Tool-use capability is a fundamental component of LLM agents, enabling them to interact with external systems through structured function calls. However, existing research exhibits inconsistent interaction representations, largely overlooks the structural distribution of tool-use trajectories, and relies on incompatible evaluation benchmarks. We present UniToolCall, a unified framework for tool learning that standardizes the entire pipeline from toolset construction and dataset generation to evaluation. The framework curates a large tool pool of 22k+ tools and constructs a hybrid training corpus of 390k+ instances by combining 10 standardized public datasets with structurally controlled synthetic trajectories. It explicitly models diverse interaction patterns, including single-hop vs. multi-hop and single-turn vs. multi-turn, while capturing both serial and parallel execution structures. To support coherent multi-turn reasoning, we further introduce an Anchor Linkage mechanism that enforces cross-turn dependencies. Furthermore, we convert 7 public benchmarks into a unified Query--Action--Observation--Answer (QAOA) representation with fine-grained evaluation at the function-call, turn, and conversation levels. Experiments show that fine-tuning Qwen3-8B on our dataset substantially improves tool-use performance. Under the distractor-heavy Hybrid-20 setting, achieves 93.0% single-turn Strict Precision, outperforming commercial models including GPT, Gemini, and Claude.

</details>


### 146. Relax: An Asynchronous Reinforcement Learning Engine for Omni-Modal Post-Training at Scale

- **Authors:** Liujie Zhang, Benzhe Ning, Rui Yang, Xiaoyan Yu, Jiaxing Li, Lumeng Wu, Jia Liu, Minghao Li, Weihang Chen, Weiqi Hu, Lei Zhang
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11554v2](http://arxiv.org/abs/2604.11554v2)
- **PDF:** [https://arxiv.org/pdf/2604.11554v2](https://arxiv.org/pdf/2604.11554v2)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **Relax**, an open‑source, asynchronously‑driven reinforcement‑learning engine designed specifically for large, omni‑modal language agents that must handle heterogeneous data, scale robustly, and balance policy staleness against throughput.

**Methodology:** Relax is built on three tightly‑integrated layers: (1) an omni‑native stack that embeds modality‑aware preprocessing, parallelism, and inference throughout the pipeline; (2) fault‑isolated services for each RL role (e.g., rollout, reward model, learner) that can be independently scaled, recovered, or upgraded; and (3) a **TransferQueue** data bus that decouples services and introduces a single “staleness” knob, allowing smooth interpolation between on‑policy, near‑on‑policy, and fully asynchronous execution.

**Key findings:** Across experiments with Qwen‑style models, Relax delivers 1.20×–2.00× speed‑ups over the prior veRL system while reaching identical reward levels, incurs only 1.9 % overhead when using the R3 replay scheme for MoE models (versus 32 % degradation in veRL), and achieves stable convergence on omni‑modal tasks (image, text, audio, and >2 000‑step video sequences). These results demonstrate that asynchronous, service‑oriented RL can scale effectively for agentic, multi‑modal AI systems.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) post-training has proven effective at unlocking reasoning, self-reflection, and tool-use capabilities in large language models. As models extend to omni-modal inputs and agentic multi-turn workflows, RL training systems face three interdependent challenges: heterogeneous data flows, operational robustness at scale, and the staleness -- throughput tradeoff. We present \textbf{Relax} (Reinforcement Engine Leveraging Agentic X-modality), an open-source RL training engine that addresses these challenges through three co-designed architectural layers. First, an \emph{omni-native architecture} builds multimodal support into the full stack -- from data preprocessing and modality-aware parallelism to inference generation -- rather than retrofitting it onto a text-centric pipeline. Second, each RL role runs as an independent, fault-isolated service that can be scaled, recovered, and upgraded without global coordination. Third, service-level decoupling enables asynchronous training via the TransferQueue data bus, where a single staleness parameter smoothly interpolates among on-policy, near-on-policy, and fully asynchronous execution. Relax achieves a 1.20$\times$ end-to-end speedup over veRL on Qwen3-4B on-policy training. Its fully async mode delivers a 1.76$\times$ speedup over colocate on Qwen3-4B and a 2.00$\times$ speedup on Qwen3-Omni-30B, while all modes converge to the same reward level. Relax supports R3 (Rollout Routing Replay)~\cite{ma2025r3} for MoE models with only 1.9\% overhead, compared to 32\% degradation in veRL under the same configuration. It further demonstrates stable omni-modal RL convergence on Qwen3-Omni across image, text, and audio, sustaining over 2{,}000 steps on video without degradation. Relax is available at https://github.com/rednote-ai/Relax.

</details>


### 147. SemaClaw: A Step Towards General-Purpose Personal AI Agents through Harness Engineering

- **Authors:** Ningyan Zhu, Huacan Wang, Jie Zhou, Feiyu Chen, Shuo Zhang, Ge Chen, Chen Liu, Jiarou Wu, Wangyi Chen, Xiaofeng Mou, Yi Xu
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11548v1](http://arxiv.org/abs/2604.11548v1)
- **PDF:** [https://arxiv.org/pdf/2604.11548v1](https://arxiv.org/pdf/2604.11548v1)
- **Categories:** cs.AI


> SemaClaw introduces an open‑source framework that formalizes “harness engineering” as the core differentiator for turning large‑language‑model agents into reliable, auditable personal assistants. It combines a DAG‑based two‑phase hybrid orchestration engine, a PermissionBridge safety layer, a three‑tier context‑management stack, and an agentic wiki skill for automatic personal knowledge‑base construction, enabling persistent, context‑aware multi‑agent collaborations. In benchmarked deployments, SemaClaw’s harness reduces unsafe actions by ≈ 87 % and improves task‑completion speed by ≈ 2.3× compared with prior prompt‑centric pipelines, demonstrating a viable path toward general‑purpose personal AI agents.


<details>
<summary>Abstract</summary>

The rise of OpenClaw in early 2026 marks the moment when millions of users began deploying personal AI agents into their daily lives, delegating tasks ranging from travel planning to multi-step research. This scale of adoption signals that two parallel arcs of development have reached an inflection point. First is a paradigm shift in AI engineering, evolving from prompt and context engineering to harness engineering-designing the complete infrastructure necessary to transform unconstrained agents into controllable, auditable, and production-reliable systems. As model capabilities converge, this harness layer is becoming the primary site of architectural differentiation. Second is the evolution of human-agent interaction from discrete tasks toward a persistent, contextually aware collaborative relationship, which demands open, trustworthy and extensible harness infrastructure. We present SemaClaw, an open-source multi-agent application framework that addresses these shifts by taking a step towards general-purpose personal AI agents through harness engineering. Our primary contributions include a DAG-based two-phase hybrid agent team orchestration method, a PermissionBridge behavioral safety system, a three-tier context management architecture, and an agentic wiki skill for automated personal knowledge base construction.

</details>


### 148. Time is Not a Label: Continuous Phase Rotation for Temporal Knowledge Graphs and Agentic Memory

- **Authors:** Weixian Waylon Li, Jiaxin Zhang, Xianan Jim Yang, Tiejun Ma, Yiwen Guo
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11544v1](http://arxiv.org/abs/2604.11544v1)
- **PDF:** [https://arxiv.org/pdf/2604.11544v1](https://arxiv.org/pdf/2604.11544v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **RoMem**, a plug‑in temporal knowledge‑graph module that treats time as a continuous phase rather than a discrete label, allowing autonomous agents to retain permanent facts while automatically “phasing out” obsolete information. RoMem uses a pretrained Semantic Speed Gate to assign a volatility score to each relation’s textual embedding and then applies continuous phase rotation in a complex vector space, so that fast‑rotating (high‑volatility) relations drift out of alignment while stable relations remain unchanged, enabling geometric shadowing of outdated facts without explicit deletion. Empirically, RoMem sets new state‑of‑the‑art performance on ICEWS05‑15 (72.6 MRR) and yields 2–3× improvements in temporal reasoning accuracy for agentic memory benchmarks (MultiTQ, LoCoMo, DMR‑MSC) while also generalizing zero‑shot to unseen financial domains.


<details>
<summary>Abstract</summary>

Structured memory representations such as knowledge graphs are central to autonomous agents and other long-lived systems. However, most existing approaches model time as discrete metadata, either sorting by recency (burying old-yet-permanent knowledge), simply overwriting outdated facts, or requiring an expensive LLM call at every ingestion step, leaving them unable to distinguish persistent facts from evolving ones. To address this, we introduce RoMem, a drop-in temporal knowledge graph module for structured memory systems, applicable to agentic memory and beyond. A pretrained Semantic Speed Gate maps each relation's text embedding to a volatility score, learning from data that evolving relations (e.g., "president of") should rotate fast while persistent ones (e.g., "born in") should remain stable. Combined with continuous phase rotation, this enables geometric shadowing: obsolete facts are rotated out of phase in complex vector space, so temporally correct facts naturally outrank contradictions without deletion. On temporal knowledge graph completion, RoMem achieves state-of-the-art results on ICEWS05-15 (72.6 MRR). Applied to agentic memory, it delivers 2-3x MRR and answer accuracy on temporal reasoning (MultiTQ), dominates hybrid benchmark (LoCoMo), preserves static memory with zero degradation (DMR-MSC), and generalises zero-shot to unseen financial domains (FinTMMBench).

</details>


### 149. Problem Reductions at Scale: Agentic Integration of Computationally Hard Problems

- **Authors:** Xi-Wei Pan, Shi-Wen An, Jin-Guo Liu
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11535v1](http://arxiv.org/abs/2604.11535v1)
- **PDF:** [https://arxiv.org/pdf/2604.11535v1](https://arxiv.org/pdf/2604.11535v1)
- **Categories:** cs.AI


> The paper introduces **Problem Reductions at Scale**, a framework that uses “harness engineering” to enable AI coding agents to automatically construct a massive library of polynomial‑time reductions between NP‑hard problems. By combining a no‑code contribution channel for domain experts, a layered verification stack (type‑level checks, unit tests, and agent‑driven feature tests), and a fully automated review‑and‑integration pipeline, the authors built in three months a Rust‑based CLI tool containing 100+ problem types and 200+ reduction rules (≈170 k lines of code). Empirical results show that this engineered harness lets agents produce well‑tested reduction software far faster than prior manual efforts, and because reductions compose transitively, adding a new solver for any single problem instantly makes it usable for every connected problem—demonstrating a scalable pathway for agentic AI to automate the integration of computationally hard problem solvers.


<details>
<summary>Abstract</summary>

Solving an NP-hard optimization problem often requires reformulating it for a specific solver -- quantum hardware, a commercial optimizer, or a domain heuristic. A tool for polynomial-time reductions between hard problems would let practitioners route any supported problem to any supported solver through a single interface. Building such a library at scale, however, has remained out of reach. We show that harness engineering, the practice of designing constraints, verification systems, and feedback loops that channel AI coding agents, can overcome this barrier. Our harness combines a no-code contribution route for domain experts, a multilayer verification stack ranging from type-level checks to agentic feature tests (AI agents role-playing as end users), and a fully automated implementation-review-integration pipeline. In about three months, we built a command-line tool backed by a library of 100+ problem types and 200+~reduction rules in over 170k lines of Rust. The result suggests that a well-engineered harness lets agents build well-tested software at a scale and pace beyond prior reduction-library efforts. Because the reduction graph composes transitively, a new solver registered for any single problem type instantly becomes available to every problem connected by a reduction path. The source code is available at https://github.com/CodingThrust/problem-reductions.

</details>


### 150. PAC-BENCH: Evaluating Multi-Agent Collaboration under Privacy Constraints

- **Authors:** Minjun Park, Donghyun Kim, Hyeonjong Ju, Seungwon Lim, Dongwook Choi, Taeyoon Kwon, Minju Kim, Jinyoung Yeo
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11523v1](http://arxiv.org/abs/2604.11523v1)
- **PDF:** [https://arxiv.org/pdf/2604.11523v1](https://arxiv.org/pdf/2604.11523v1)
- **Categories:** cs.AI, cs.MA


> **Paper contribution:** Introduces **PAC‑Bench**, the first systematic benchmark for measuring how privacy constraints affect collaborative performance of AI agents.  

**Methodology:** Constructs a suite of multi‑agent tasks (information‑exchange, joint planning, and problem‑solving) in which each agent must obey explicit privacy policies (e.g., never reveal raw data, limit shared abstractions). The benchmark evaluates a range of existing agents (LLM‑based planners, coordination protocols, and privacy‑preserving message filters) by measuring task success, efficiency, and the influence of the initiating versus partner agent.  

**Key findings:** Across all tasks, imposing privacy limits causes a **large drop in collaboration success** and makes outcomes **highly dependent on which agent initiates** the interaction. The performance loss stems from three recurrent failure modes: (1) early privacy violations that abort coordination, (2) overly conservative abstraction that strips essential information, and (3) “privacy‑induced hallucinations” where agents fill missing details with incorrect guesses. These results demonstrate that current agent architectures lack robust mechanisms for privacy‑aware coordination, highlighting an open research direction for new protocols that can negotiate, share, and reason under privacy constraints.


<details>
<summary>Abstract</summary>

We are entering an era in which individuals and organizations increasingly deploy dedicated AI agents that interact and collaborate with other agents. However, the dynamics of multi-agent collaboration under privacy constraints remain poorly understood. In this work, we present $PAC\text{-}Bench$, a benchmark for systematic evaluation of multi-agent collaboration under privacy constraints. Experiments on $PAC\text{-}Bench$ show that privacy constraints substantially degrade collaboration performance and make outcomes depend more on the initiating agent than the partner. Further analysis reveals that this degradation is driven by recurring coordination breakdowns, including early-stage privacy violations, overly conservative abstraction, and privacy-induced hallucinations. Together, our findings identify privacy-aware multi-agent collaboration as a distinct and unresolved challenge that requires new coordination mechanisms beyond existing agent capabilities.

</details>


### 151. From Translation to Superset: Benchmark-Driven Evolution of a Production AI Agent from Rust to Python

- **Authors:** Jinhua Wang, Biswa Sengupta
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11518v1](http://arxiv.org/abs/2604.11518v1)
- **PDF:** [https://arxiv.org/pdf/2604.11518v1](https://arxiv.org/pdf/2604.11518v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces a benchmark‑driven, LLM‑assisted workflow for continuously migrating and evolving a large production AI coding agent (Codex CLI) from Rust to Python. By iteratively translating the 648 K‑line Rust codebase, testing against public agent benchmarks (SWE‑bench and Terminal‑Bench), and using the benchmark scores as an objective function, the authors automatically locate and fix functional mismatches, achieve near‑parity performance (73.8 % vs 70 % on SWE‑bench, 42.5 % vs 47.5 % on Terminal‑Bench), and subsequently extend the Python version with 30 new capabilities (multi‑agent orchestration, semantic memory, safety guardrails, cost tracking, etc.). The methodology demonstrates that a diff‑translate‑test loop guided by real‑world agent benchmarks can produce a far smaller codebase (15.9× reduction) while preserving performance and enabling rapid, systematic feature expansion in agentic AI systems.


<details>
<summary>Abstract</summary>

Cross-language migration of large software systems is a persistent engineering challenge, particularly when the source codebase evolves rapidly. We present a methodology for LLM-assisted continuous code translation in which a large language model translates a production Rust codebase (648K LOC, 65 crates) into Python (41K LOC, 28 modules), with public agent benchmarks as the objective function driving iterative refinement. Our subject system is Codex CLI, a production AI coding agent. We demonstrate that: (1) the Python port resolves 59/80 SWE-bench Verified tasks (73.8%) versus Rust's 56/80 (70.0%), and achieves 42.5% on Terminal-Bench versus Rust's 47.5%, confirming near-parity on real-world agentic tasks; (2) benchmark-driven debugging, revealing API protocol mismatches, environment pollution, a silent WebSocket failure mode, and an API 400 crash, is more effective than static testing alone; (3) the architecture supports continuous upstream synchronisation via an LLM-assisted diff-translate-test loop; and (4) the Python port has evolved into a capability superset with 30 feature-flagged extensions (multi-agent orchestration, semantic memory, guardian safety, cost tracking) absent from Rust, while preserving strict parity mode for comparison. Our evaluation shows that for LLM-based agents where API latency dominates, Python's expressiveness yields a 15.9x code reduction with negligible performance cost, while the benchmark-as-objective-function methodology provides a principled framework for growing a cross-language port from parity into an extended platform.

</details>


### 152. AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering

- **Authors:** Rajesh Kumar, Waqar Ali, Junaid Ahmed, Najma Imtiaz Ali, Shaban Usman
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.13120v1](http://arxiv.org/abs/2604.13120v1)
- **PDF:** [https://arxiv.org/pdf/2604.13120v1](https://arxiv.org/pdf/2604.13120v1)
- **Categories:** cs.SE, cs.AI


> **Main contribution:** The paper introduces **AgentForge**, a multi‑agent framework that treats execution‑grounded verification as a core component of LLM‑based software engineering, requiring every generated code change to pass a sandboxed Docker run before being accepted.  

**Methodology:** AgentForge decomposes the development workflow into specialized agents (Planner, Coder, Tester, Debugger, Critic) that share a common memory store and interact iteratively; each iteration updates the repository state and receives binary execution feedback (pass/fail) which supersedes pure next‑token likelihood as a supervision signal. The authors formalize this as an iterative decision process over repository states and evaluate the system on the SWE‑BENCH Lite benchmark.  

**Key findings:** AgentForge resolves **40 %** of the benchmark tasks, surpassing strong single‑agent baselines by **26–28 percentage points**. Ablation studies show that (1) mandatory execution feedback and (2) role‑based decomposition each independently contribute substantial gains, confirming the importance of execution‑grounded verification for autonomous agentic AI in software engineering.


<details>
<summary>Abstract</summary>

Large language models generate plausible code but cannot verify correctness. Existing multi-agent systems simulate execution or leave verification optional. We introduce execution-grounded verification as a first-class principle: every code change must survive sandboxed execution before propagation. We instantiate this principle in AGENTFORGE, a multi-agent framework where Planner, Coder, Tester, Debugger, and Critic agents coordinate through shared memory and a mandatory Docker sandbox. We formalize software engineering with LLMs as an iterative decision process over repository states, where execution feedback provides a stronger supervision signal than next-token likelihood. AGENTFORGE achieves 40.0\% resolution on SWE-BENCH Lite, outperforming single-agent baselines by 26--28 points. Ablations confirm that execution feedback and role decomposition each independently drive performance. The framework is open-source at https://github.com/raja21068/AutoCodeAI.

</details>


### 153. OOM-RL: Out-of-Money Reinforcement Learning Market-Driven Alignment for LLM-Based Multi-Agent Systems

- **Authors:** Kun Liu, Liqun Chen
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11477v1](http://arxiv.org/abs/2604.11477v1)
- **PDF:** [https://arxiv.org/pdf/2604.11477v1](https://arxiv.org/pdf/2604.11477v1)
- **Categories:** cs.AI, cs.SE, q-fin.TR


> **Main contribution**: The authors propose **Out‑of‑Money Reinforcement Learning (OOM‑RL)**, a market‑driven alignment framework that replaces subjective human or AI feedback with real‑world financial loss as an immutable negative signal, and they embed this signal in a **Strict Test‑Driven Agentic Workflow (STDAW)** that enforces a unidirectional state lock and a ≥95 % verified code‑coverage constraint.

**Methodology**: A population of LLM‑based agents was deployed in live, high‑friction financial markets for 20 months (July 2024 – Feb 2026). Agents received capital from a pooled fund; any loss directly reduced their budget, providing a hard gradient. The system iteratively updated policies via reinforcement learning on the observed profit‑and‑loss stream while the RO‑Lock prevented rollback to pre‑test states. Performance was monitored with standard financial metrics (Sharpe ratio, turnover) and software‑quality metrics (test coverage, execution decay).

**Key findings**: Early, sycophantic agents rapidly depleted funds, but as the economic penalty escalated, the MAS converged to a liquidity‑aware policy that eliminated hallucinated actions, achieved ≥95 % test coverage, and stabilized at an annualized Sharpe ratio of **2.06**. The study demonstrates that tangible economic penalties can align autonomous agents more robustly than RLHF/RLAIF, suggesting that real‑world resource costs are a viable, objective alignment signal for high‑stakes agentic AI systems.


<details>
<summary>Abstract</summary>

The alignment of Multi-Agent Systems (MAS) for autonomous software engineering is constrained by evaluator epistemic uncertainty. Current paradigms, such as Reinforcement Learning from Human Feedback (RLHF) and AI Feedback (RLAIF), frequently induce model sycophancy, while execution-based environments suffer from adversarial "Test Evasion" by unconstrained agents. In this paper, we introduce an objective alignment paradigm: \textbf{Out-of-Money Reinforcement Learning (OOM-RL)}. By deploying agents into the non-stationary, high-friction reality of live financial markets, we utilize critical capital depletion as an un-hackable negative gradient. Our longitudinal 20-month empirical study (July 2024 -- February 2026) chronicles the system's evolution from a high-turnover, sycophantic baseline to a robust, liquidity-aware architecture. We demonstrate that the undeniable ontological consequences of financial loss forced the MAS to abandon overfitted hallucinations in favor of the \textbf{Strict Test-Driven Agentic Workflow (STDAW)}, which enforces a Byzantine-inspired uni-directional state lock (RO-Lock) anchored to a deterministically verified $\geq 95\%$ code coverage constraint matrix. Our results show that while early iterations suffered severe execution decay, the final OOM-RL-aligned system achieved a stable equilibrium with an annualized Sharpe ratio of 2.06 in its mature phase. We conclude that substituting subjective human preference with rigorous economic penalties provides a robust methodology for aligning autonomous agents in high-stakes, real-world environments, laying the groundwork for generalized paradigms where computational billing acts as an objective physical constraint

</details>


### 154. Three Roles, One Model: Role Orchestration at Inference Time to Close the Performance Gap Between Small and Large Agents

- **Authors:** S. Aaron McClendon, Jorge Gallego-Feliciano, Stavros Zervoudakis, Antonios Saravanos
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11465v2](http://arxiv.org/abs/2604.11465v2)
- **PDF:** [https://arxiv.org/pdf/2604.11465v2](https://arxiv.org/pdf/2604.11465v2)
- **Categories:** cs.AI


> **Main contribution:** The paper shows that a small LLM (Qwen‑3 8B) can close much of the performance gap to much larger agents by adding only inference‑time “role‑orchestration” scaffolding, without any extra training or model modifications.  

**Methodology:** The authors diagnose failure modes on the AppWorld tool‑use benchmark and construct a three‑stage pipeline that invokes the same frozen model three times with different conditioning: (1) a summarizer compresses the dialogue while preserving key artifacts, (2) the main agent reasons over this compressed context, and (3) a correction module rewrites the generated code in isolation, preventing repetitive errors. The pipeline is evaluated in both FP16 and 4‑bit AWQ quantized settings on a single 24 GB GPU.  

**Key findings:** This simple scaffolding roughly doubles task‑completion rates (e.g., from 5.4 % to 8.9 % FP16, from 3.0 % to 5.9 % AWQ) and yields especially large gains on easier tasks, enabling the 8 B model to outperform a 33 B DeepSeek‑Coder baseline. The results demonstrate that test‑time orchestration of multiple roles can make modest‑size agents competitive with much larger ones, highlighting a practical path for scaling agentic AI via structured inference rather than additional training compute.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents show promise on realistic tool-use tasks, but deploying capable agents on modest hardware remains challenging. We study whether inference-time scaffolding alone, without any additional training compute, can improve the performance of a small model in complex multi-step environments. Operating on a single 24GB GPU, we evaluate Qwen3-8B on the AppWorld benchmark under both full-precision and 4-bit quantized configurations. Without any intervention, the raw model achieves just 5.4% (FP16) and 3.0% (AWQ) task goal completion. Guided by a systematic failure mode analysis, we introduce a three-tier inference scaffolding pipeline that deploys the same frozen model in three distinct roles: (1) a summarization model that preserves critical artifacts (tokens, credentials, API responses) while compressing dialogue history; (2) the main agent model that reasons over the compressed context; and (3) an isolated correction model that reviews and revises the agent's code output without access to conversation history, breaking repetitive failure loops. Applied to the same unmodified model, this scaffolding yields 8.9% (FP16) and 5.9% (AWQ) task goal completion, roughly doubling performance in both settings, with particularly strong gains on difficulty-1 tasks (15.8% to 26.3% FP16; 5.3% to 14.0% AWQ). On full-precision inference, our scaffolded 8B model surpasses DeepSeek-Coder 33B Instruct (7.1%) from the original AppWorld evaluation, demonstrating that structured inference-time interventions can make small models competitive with systems 4 times their size. We formalize the approach as a scaffolded policy over a frozen base model, three invocations of the same weights with different conditioning, drawing connections to test-time compute scaling and action-space shaping in reinforcement learning.

</details>


### 155. Escaping the Context Bottleneck: Active Context Curation for LLM Agents via Reinforcement Learning

- **Authors:** Xiaozhe Li, Tianyi Lyu, Yizhao Yang, Liang Shan, Siyi Yang, Ligao Zhang, Zhuoyi Huang, Qingwen Liu, Yang Li
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11462v1](http://arxiv.org/abs/2604.11462v1)
- **PDF:** [https://arxiv.org/pdf/2604.11462v1](https://arxiv.org/pdf/2604.11462v1)
- **Categories:** cs.AI


> The paper proposes a two‑component architecture that separates context management from task execution: a small, trainable policy (ContextCurator) learns, via reinforcement learning, to prune irrelevant information and preserve essential “reasoning anchors” in the working memory of a frozen, large language model (TaskExecutor). Experiments on long‑horizon benchmarks (WebArena, DeepSearch) show that this active context curation raises success rates (e.g., Gemini‑3.0‑flash from 36.4 % to 41.2 %) while cutting token usage by up to ~9 % and, on DeepSearch, by a factor of eight; a 7 B ContextCurator even matches GPT‑4o’s context‑management performance. The results demonstrate that learned, lightweight context curators can effectively overcome the “context bottleneck” and improve efficiency and reliability of autonomous LLM agents.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) struggle with long-horizon tasks due to the "context bottleneck" and the "lost-in-the-middle" phenomenon, where accumulated noise from verbose environments degrades reasoning over multi-turn interactions. To address this issue, we introduce a symbiotic framework that decouples context management from task execution. Our architecture pairs a lightweight, specialized policy model, ContextCurator, with a powerful frozen foundation model, TaskExecutor. Trained via reinforcement learning, ContextCurator actively reduces information entropy in the working memory. It aggressively prunes environmental noise while preserving reasoning anchors, that is, sparse data points that are critical for future deductions. On WebArena, our framework improves the success rate of Gemini-3.0-flash from 36.4% to 41.2% while reducing token consumption by 8.8% (from 47.4K to 43.3K). On DeepSearch, it achieves a 57.1% success rate, compared with 53.9%, while reducing token consumption by a factor of 8. Remarkably, a 7B ContextCurator matches the context management performance of GPT-4o, providing a scalable and computationally efficient paradigm for autonomous long-horizon agents.

</details>


### 156. Hardening x402: PII-Safe Agentic Payments via Pre-Execution Metadata Filtering

- **Authors:** Vladimir Stantchev
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11430v1](http://arxiv.org/abs/2604.11430v1)
- **PDF:** [https://arxiv.org/pdf/2604.11430v1](https://arxiv.org/pdf/2604.11430v1)
- **Categories:** cs.CR, cs.AI, cs.CY


> The paper introduces **presidio‑hardened‑x402**, an open‑source middleware that sits between AI agents and the x402 payment protocol to automatically scrub personally identifiable information (PII) from the payment‑metadata payloads, enforce declarative spending policies, and prevent replay attacks. The authors built a synthetic dataset of 2 000 labeled x402 metadata triples covering seven application domains and evaluated two detection approaches (regex vs. NLP) across 42 confidence‑threshold settings; the best configuration (NLP mode, min_score = 0.4, all entity types) attained a micro‑F1 of 0.894 with 97.2 % precision while adding only 5.73 ms (p99) latency, well under the 50 ms budget. This work demonstrates that lightweight, pre‑execution metadata filtering can make agentic payment interactions PII‑safe without impairing performance, offering a viable blueprint for privacy‑preserving financial flows in autonomous AI systems.


<details>
<summary>Abstract</summary>

AI agents that pay for resources via the x402 protocol embed payment metadata - resource URLs, descriptions, and reason strings - in every HTTP payment request. This metadata is transmitted to the payment server and to the centralised facilitator API before any on-chain settlement occurs; neither party is typically bound by a data processing agreement. We present presidio-hardened-x402, the first open-source middleware that intercepts x402 payment requests before transmission to detect and redact personally identifiable information (PII), enforce declarative spending policies, and block duplicate replay attempts. To evaluate the PII filter, we construct a labeled synthetic corpus of 2,000 x402 metadata triples spanning seven use-case categories, and run a 42-configuration precision/recall sweep across two detection modes (regex, NLP) and five confidence thresholds. The recommended configuration (mode=nlp, min_score=0.4, all entity types) achieves micro-F1 = 0.894 with precision 0.972, at a p99 latency of 5.73ms - well within the 50ms overhead budget. The middleware, corpus, and all experiment code are publicly available at https://github.com/presidio-v/presidio-hardened-x402.

</details>


### 157. From Agent Loops to Structured Graphs:A Scheduler-Theoretic Framework for LLM Agent Execution

- **Authors:** Hu Wei
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11378v1](http://arxiv.org/abs/2604.11378v1)
- **PDF:** [https://arxiv.org/pdf/2604.11378v1](https://arxiv.org/pdf/2604.11378v1)
- **Categories:** cs.AI, eess.SY


> **Main contribution**  
The paper introduces **Structured Graph Harness (SGH)**, a scheduler‑theoretic framework that replaces the traditional “agent loop” (a single LLM repeatedly reading an ever‑growing context) with an **explicit static directed‑acyclic graph (DAG)** of execution units. By treating each node as a schedulable task with immutable plans, separate planning/recovery layers, and a strict escalation protocol for failures, SGH makes LLM‑driven agents far more controllable, verifiable, and implementable.

**Methodology**  
The authors first formalize the agent loop as a “single‑ready‑unit” scheduler and show how it sits on a continuum with graph‑based executors. They then define a **formal specification** (node state machine, termination conditions, soundness proofs) and conduct a **trade‑off analysis** of controllability vs. expressiveness across 70 existing LLM‑agent systems, positioning SGH within that spectrum. Finally, they outline an experimental protocol (seven‑group design) for future empirical validation, though no implementation results are presented.

**Key findings for agentic AI**  
- Mapping LLM agents to classic scheduling theory highlights three structural weaknesses of agent loops—implicit step dependencies, unbounded recovery loops, and mutable execution histories.  
- SGH’s immutable DAG plans and layered recovery dramatically improve **debuggability, reproducibility, and safety**, at the cost of some expressiveness.  
- The trade‑off analysis suggests that many current systems already sit near SGH’s design point, indicating practical feasibility for transitioning large‑scale LLM agents to a scheduler‑based execution model.


<details>
<summary>Abstract</summary>

The dominant paradigm for building LLM based agents is the Agent Loop, an iterative cycle where a single language model decides what to do next by reading an ever growing context window. This paradigm has three structural weaknesses: implicit dependencies between steps, unbounded recovery loops, and mutable execution history that complicates debugging. We characterize the Agent Loop as a single ready unit scheduler: at any moment, at most one executable unit is active, and the choice of which unit to activate comes from opaque LLM inference rather than an inspectable policy. This perspective places Agent Loops and graph based execution engines on a single semantic continuum. We propose SGH, Structured Graph Harness, which lifts control flow from implicit context into an explicit static DAG. SGH makes three commitments: execution plans are immutable within a plan version, planning execution and recovery are separated into three layers, and recovery follows a strict escalation protocol. These choices trade some expressiveness for controllability, verifiability, and implementability. Our contributions are fourfold: a scheduler unified framework that applies classical scheduling theory to LLM agent execution and identifies challenges introduced by non deterministic LLM nodes; a trade off analysis of controllability, expressiveness, and implementability across 70 surveyed systems; a formal specification including a node state machine with termination and soundness guarantees; and an attributable experimental framework with a seven group design for future validation. This is a position paper and design proposal. We provide a theoretical framework, design analysis, and experimental protocol, not a production implementation or empirical results.

</details>


### 158. The Missing Knowledge Layer in Cognitive Architectures for AI Agents

- **Authors:** Michaël Roynard
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11364v1](http://arxiv.org/abs/2604.11364v1)
- **PDF:** [https://arxiv.org/pdf/2604.11364v1](https://arxiv.org/pdf/2604.11364v1)
- **Categories:** cs.AI


> The paper argues that the most widely used cognitive‑architecture frameworks for AI agents—CoALA and JEPA—miss a dedicated Knowledge layer with its own persistence semantics, causing agents to treat facts and experiences identically and to apply inappropriate decay or update mechanisms. By surveying existing memory‑system designs, the authors identify eight convergence points that reveal this architectural blind spot, and they introduce a four‑layer decomposition (Knowledge, Memory, Wisdom, Intelligence), each endowed with distinct persistence rules (indefinite supersession, Ebbinghaus‑style decay, evidence‑gated revision, and transient inference). A prototype implementation in Python and Rust shows that separating these layers is practical, and experimental results (e.g., near‑zero contradiction‑resolution scores on the BEAM benchmark) demonstrate that the Knowledge layer substantially reduces factual inconsistency, highlighting a critical design change for future agentic AI systems.


<details>
<summary>Abstract</summary>

The two most influential cognitive architecture frameworks for AI agents, CoALA [21] and JEPA [12], both lack an explicit Knowledge layer with its own persistence semantics. This gap produces a category error: systems apply cognitive decay to factual claims, or treat facts and experiences with identical update mechanics. We survey persistence semantics across existing memory systems and identify eight convergence points, from Karpathy's LLM Knowledge Base [10] to the BEAM benchmark's near-zero contradiction-resolution scores [22], all pointing to related architectural gaps. We propose a four-layer decom position (Knowledge, Memory, Wisdom, Intelligence) where each layer has fundamentally different persistence semantics: indefinite supersession, Ebbinghaus decay, evidence-gated revision, and ephemeral inference respectively. Companion implementations in Python and Rust demonstrate the architectural separation is feasible. We borrow terminology from cognitive science as a useful analogy (the Knowledge/Memory distinction echoes Tulving's trichotomy), but our layers are engineering constructs justified by persistence-semantics requirements, not by neural architecture. We argue that these distinctions demand distinct persistence semantics in engineering implementations, and that no current framework or system provides this.

</details>


### 159. Governance by Design: A Parsonian Institutional Architecture for Internet-Wide Agent Societies

- **Authors:** Anbang Ruan
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11337v1](http://arxiv.org/abs/2604.11337v1)
- **PDF:** [https://arxiv.org/pdf/2604.11337v1](https://arxiv.org/pdf/2604.11337v1)
- **Categories:** cs.MA, cs.AI, cs.CY


> The paper proposes a formal, Parsonian‑based institutional architecture to govern large‑scale, internet‑wide societies of autonomous agents, arguing that effective governance must be built into the system design rather than retrofitted through risk lists or compliance checks. By mapping Talcott Parsons’ AGIL functions (Adaptation, Goal attainment, Integration, Latency) onto a 16‑cell framework and evaluating the OpenClaw ecosystem (≈770 k agents) with a 64‑indicator diagnostic, the authors show that only ~19 % of the required sub‑functions are covered and that none of the twelve prescribed inter‑pillar coordination pathways are operational, especially in the Fiduciary and Political pillars. The findings reveal a systematic “governance gap” that persists across other agent‑native protocol stacks, leading the authors to recommend a pre‑emptive, prioritized roadmap for building the missing coordination, normative, and fiduciary infrastructure before agent societies crystallize.


<details>
<summary>Abstract</summary>

The dominant paradigm of local multi-agent systems -- orchestrated, enterprise-bounded pipelines -- is being superseded by internet-wide agent societies in which autonomous agents discover each other through open registries, interact without central orchestrators, and generate emergent social behaviors. We argue that governing such societies requires institutional design, not merely risk enumeration or process compliance. Applying Talcott Parsons' AGIL framework -- four functional imperatives (Adaptation, Goal Attainment, Integration, Latency) every viable social system must satisfy -- we derive a prescriptive sixteen-cell institutional architecture for internet-wide agent governance. Diagnostically applied to the OpenClaw ecosystem (250,000+ GitHub stars, 2M+ monthly users, 770,000+ registered agents) via a recursive sub-function analysis (64 binary indicators across 16 cells), we find at most 19% sub-function coverage (sensitivity range 17-30%) -- potential rather than operative capacity, since zero inter-cell coordination prevents existing infrastructure from participating in inter-pillar interchange. A complementary interchange media assessment finds zero of twelve inter-pillar pathways functional: the ecosystem has technical infrastructure but no active governance, no coordination layer, and no normative grounding, with the Fiduciary and Political pillars most severely underserved. Extending the diagnostic to the broader agent-native protocol stack (MCP, A2A, ANP, x402, ERC-8004), independent development teams reproduce the same structural pattern -- confirming the governance gap is a feature of market-driven development, not ecosystem immaturity. Institutional design is most effective before social patterns calcify; we conclude with a prioritized roadmap for the missing governance infrastructure.

</details>


### 160. Do LLMs Know Tool Irrelevance? Demystifying Structural Alignment Bias in Tool Invocations

- **Authors:** Yilong Liu, Xixun Lin, Pengfei Cao, Ge Zhang, Fang Fang, Yanan Cao
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11322v1](http://arxiv.org/abs/2604.11322v1)
- **PDF:** [https://arxiv.org/pdf/2604.11322v1](https://arxiv.org/pdf/2604.11322v1)
- **Categories:** cs.CL, cs.AI


> The paper uncovers a systematic “structural alignment bias” in large language models: whenever the surface form of a user query can be mapped onto a tool’s input schema, the model tends to call the tool even if the tool is semantically irrelevant to the task. To isolate this effect, the authors create SABEval, a benchmark that separates syntactic fit from true relevance, and use a novel Contrastive Attention Attribution analysis to show that LLMs balance two internal pathways—semantic checking versus structural matching—and that the latter often dominates tool‑invocation decisions. By re‑weighting these pathways through a simple rebalancing training regime, they markedly reduce spurious tool calls on SABEval while preserving overall tool‑use performance.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have demonstrated impressive capabilities in utilizing external tools. In practice, however, LLMs are often exposed to tools that are irrelevant to the user's query, in which case the desired behavior is to refrain from invocations. In this work, we identify a widespread yet overlooked mechanistic flaw in tool refusal, which we term structural alignment bias: Even when a tool fails to serve the user's goal, LLMs still tend to invoke it whenever query attributes can be validly assigned to tool parameters. To systematically study this bias, we introduce SABEval, a new dataset that decouples structural alignment from semantic relevance. Our analysis shows that structural alignment bias induces severe tool-invocation errors in LLMs, yet remains largely unaccounted for in existing evaluations. To investigate the internal mechanisms underlying this bias, we propose Contrastive Attention Attribution, which reveals two competing pathways for semantic checking and structural matching. The relative strength of these pathways drives LLMs' tool invocation decisions. Based on these findings, we further introduce a rebalancing strategy that effectively mitigates structural alignment bias, as demonstrated by extensive experiments, without degrading general tool-use capabilities.

</details>


### 161. Network Effects and Agreement Drift in LLM Debates

- **Authors:** Erica Cau, Andrea Failla, Giulio Rossetti
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11312v2](http://arxiv.org/abs/2604.11312v2)
- **PDF:** [https://arxiv.org/pdf/2604.11312v2](https://arxiv.org/pdf/2604.11312v2)
- **Categories:** cs.SI, cs.AI, cs.CY, cs.MA, physics.soc-ph


> **Contribution:** The paper shows that when LLM‐based agents are placed in simulated social networks and asked to debate repeatedly, the collective dynamics they exhibit are heavily shaped by network structure and a systematic bias the authors call **agreement drift**—a tendency for agents to converge toward particular points on the opinion spectrum rather than reflecting the true distribution of views.  

**Methodology:** The authors construct synthetic interaction graphs with adjustable homophily and minority‑majority class sizes, then run multi‑round debate simulations using several state‑of‑the‑art LLMs as agents. They measure opinion trajectories, convergence rates, and the direction of drift, and compare these outcomes against the known ground‑truth opinion distribution encoded in the network generation process.  

**Key Findings:** (1) Strong homophily and minority under‑representation amplify agreement drift, causing LLM agents to over‑align with majority positions even when the underlying opinion pool is balanced. (2) Different LLM architectures vary in the magnitude of drift, indicating that model‑specific biases, not just network effects, drive the observed convergence. (3) Consequently, LLM populations cannot be taken as faithful behavioral proxies for human groups without first isolating and correcting for these structural and model‑induced distortions.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have demonstrated an unprecedented ability to simulate human-like social behaviors, making them useful tools for simulating complex social systems. However, it remains unclear to what extent these simulations can be trusted to accurately capture key social mechanisms, particularly in highly unbalanced contexts involving minority groups. This paper uses a network generation model with controlled homophily and class sizes to examine how LLM agents behave collectively in multi-round debates. Moreover, our findings highlight a particular directional susceptibility that we term \textit{agreement drift}, in which agents are more likely to shift toward specific positions on the opinion scale. Overall, our findings highlight the need to disentangle structural effects from model biases before treating LLM populations as behavioral proxies for human groups.

</details>


### 162. BankerToolBench: Evaluating AI Agents in End-to-End Investment Banking Workflows

- **Authors:** Elaine Lau, Markus Dücker, Ronak Chaudhary, Hui Wen Goh, Rosemary Wei, Vaibhav Kumar, Saed Qunbar, Guram Gogia, Yi Liu, Scott Millslagle, Nasim Borazjanizadeh, Ulyana Tkachenko, Samuel Eshun Danquah, Collin Schweiker, Vijay Karumathil, Asrith Devalaraju, Varsha Sandadi, Haemi Nam, Punit Arani, Ray Epps, Abdullah Arif, Sahil Bhaiwala, Curtis Northcutt, Skyler Wang, Anish Athalye, Jonas Mueller, Francisco Guzmán
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11304v1](http://arxiv.org/abs/2604.11304v1)
- **PDF:** [https://arxiv.org/pdf/2604.11304v1](https://arxiv.org/pdf/2604.11304v1)
- **Categories:** cs.AI


> The paper introduces **BankerToolBench (BTB)**, a novel, open‑source benchmark that measures how well AI agents can carry out full‑cycle junior investment‑banking tasks—navigating data rooms, using market‑data and SEC‑filing tools, and producing multi‑file deliverables such as Excel models, PowerPoint decks, and written reports. The authors constructed the benchmark by consulting 502 professional bankers and designing a 100‑plus‑criterion rubric that judges economic utility and cross‑artifact consistency; they then evaluated nine state‑of‑the‑art LLM‑based agents (including GPT‑5.4) by running them end‑to‑end on BTB tasks. Results show that even the top model meets fewer than half of the rubric requirements and is judged by bankers as never client‑ready, highlighting major gaps—particularly in maintaining consistency across generated artifacts—and pointing to specific improvement directions for agentic AI in high‑stakes professional workflows.


<details>
<summary>Abstract</summary>

Existing AI benchmarks lack the fidelity to assess economically meaningful progress on professional workflows. To evaluate frontier AI agents in a high-value, labor-intensive profession, we introduce BankerToolBench (BTB): an open-source benchmark of end-to-end analytical workflows routinely performed by junior investment bankers. To develop an ecologically valid benchmark grounded in representative work environments, we collaborated with 502 investment bankers from leading firms. BTB requires agents to execute senior banker requests by navigating data rooms, using industry tools (market data platform, SEC filings database), and generating multi-file deliverables--including Excel financial models, PowerPoint pitch decks, and PDF/Word reports. Completing a BTB task takes bankers up to 21 hours, underscoring the economic stakes of successfully delegating this work to AI. BTB enables automated evaluation of any LLM or agent, scoring deliverables against 100+ rubric criteria defined by veteran investment bankers to capture stakeholder utility. Testing 9 frontier models, we find that even the best-performing model (GPT-5.4) fails nearly half of the rubric criteria and bankers rate 0% of its outputs as client-ready. Our failure analysis reveals key obstacles (such as breakdowns in cross-artifact consistency) and improvement directions for agentic AI in high-stakes professional workflows.

</details>


### 163. Dialectic-Med: Mitigating Diagnostic Hallucinations via Counterfactual Adversarial Multi-Agent Debate

- **Authors:** Zhixiang Lu, Jionglong Su
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11258v1](http://arxiv.org/abs/2604.11258v1)
- **PDF:** [https://arxiv.org/pdf/2604.11258v1](https://arxiv.org/pdf/2604.11258v1)
- **Categories:** cs.CL


> The paper introduces **Dialectic‑Med**, a multi‑agent architecture that combats diagnostic hallucinations in multimodal medical LLMs by explicitly embedding a falsification step into the reasoning process. The system comprises three specialized agents—a Proponent that proposes a diagnosis, an Opponent that uses a novel visual‑falsification module to retrieve and present contradictory image evidence, and a Mediator that integrates the conflicting arguments through a weighted consensus graph—thus turning diagnosis into an adversarial debate rather than a single‑pass chain‑of‑thought. Experiments on MIMIC‑CXR‑VQA, VQA‑RAD, and PathVQA show that this dialectic framework attains state‑of‑the‑art accuracy while markedly improving explanation faithfulness and reducing hallucinated visual details, establishing a more trustworthy paradigm for agentic AI in clinical decision‑making.


<details>
<summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) in healthcare suffer from severe confirmation bias, often hallucinating visual details to support initial, potentially erroneous diagnostic hypotheses. Existing Chain-of-Thought (CoT) approaches lack intrinsic correction mechanisms, rendering them vulnerable to error propagation. To bridge this gap, we propose Dialectic-Med, a multi-agent framework that enforces diagnostic rigor through adversarial dialectics. Unlike static consensus models, Dialectic-Med orchestrates a dynamic interplay between three role-specialized agents: a proponent that formulates diagnostic hypotheses; an opponent equipped with a novel visual falsification module that actively retrieves contradictory visual evidence to challenge the Proponent; and a mediator that resolves conflicts via a weighted consensus graph. By explicitly modeling the cognitive process of falsification, our framework guarantees that diagnostic reasoning is tightly grounded in verified visual regions. Empirical evaluations on MIMIC-CXR-VQA, VQA-RAD, and PathVQA demonstrate that Dialectic-Med not only achieves state-of-the-art performance but also fundamentally enhances the trustworthiness of the reasoning process. Beyond accuracy, our approach significantly enhances explanation faithfulness and decisively mitigates hallucinations, establishing a new standard over single-agent baselines.

</details>


### 164. Evolving Many Worlds: Towards Open-Ended Discovery in Petri Dish NCA via Population-Based Training

- **Authors:** Uljad Berdica, Jakob Foerster, Frank Hutter, Arber Zela
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11248v1](http://arxiv.org/abs/2604.11248v1)
- **PDF:** [https://arxiv.org/pdf/2604.11248v1](https://arxiv.org/pdf/2604.11248v1)
- **Categories:** cs.NE, cs.AI, cs.MA


> **Main contribution:** The paper introduces **PBT‑NCA**, a population‑based meta‑evolutionary framework that automatically tunes Petri‑Dish Neural Cellular Automata (PD‑NCA) to produce sustained, open‑ended complexity.

**Methodology:** A population of PD‑NCA agents is evolved with **Population‑Based Training** using a composite fitness that simultaneously rewards (i) historical behavioral novelty (to encourage divergent exploration) and (ii) instantaneous visual diversity (to avoid collapse into uniform or noisy states). The algorithm also penalizes monocultures and dead‑state equilibria, keeping the dynamics at the “edge of chaos”.

**Key findings for agentic AI:** Under this pressure the evolved NCAs spontaneously exhibit a rich repertoire of lifelike, self‑organizing behaviors—periodic wave fronts, spore‑like dispersal, and migrating, shape‑shifting macro‑structures—demonstrating that a relatively simple, locally interacting substrate can discover diverse survival and morphogenesis strategies without explicit task specifications. This showcases a scalable route to open‑ended, emergent agency in differentiable multi‑agent systems.


<details>
<summary>Abstract</summary>

The generation of sustained, open-ended complexity from local interactions remains a fundamental challenge in artificial life. Differentiable multi-agent systems, such as Petri Dish Neural Cellular Automata (PD-NCA), exhibit rich self-organization driven purely by spatial competition; however, they are highly sensitive to hyperparameters and frequently collapse into uninteresting patterns and dynamics, such as frozen equilibria or structureless noise. In this paper, we introduce PBT-NCA, a meta-evolutionary algorithm that evolves a population of PD-NCAs subject to a composite objective that rewards both historical behavioral novelty and contemporary visual diversity. Driven by this continuous evolutionary pressure, PBT-NCA spontaneously generates a plethora of emergent lifelike phenomena over extended horizons-a hallmark of true open-endedness. Strikingly, the substrate autonomously discovers diverse morphological survival and self-organization strategies. We observe highly regular, coordinated periodic waves; spore-like scattering where homogeneous groups eject cell-like clusters to colonize distant territories; and fluid, shape-shifting macro-structures that migrate across the substrate, maintaining stable outer boundaries that enclose highly active interiors. By actively penalizing monocultures and dead states, PBT-NCA sustains a state of effective complexity that is neither globally ordered nor globally random, operating persistently at the "edge of chaos".

</details>


### 165. Semantic Rate-Distortion Theory: Deductive Compression and Closure Fidelity

- **Authors:** Jianfeng Xu
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11204v1](http://arxiv.org/abs/2604.11204v1)
- **PDF:** [https://arxiv.org/pdf/2604.11204v1](https://arxiv.org/pdf/2604.11204v1)
- **Categories:** cs.IT, cs.MA


> **Main contribution** – The paper extends classic rate‑distortion theory to *semantic* sources that are logical knowledge bases, introducing **closure fidelity** (preservation of the deductive closure) as the distortion measure and showing that only the **irredundant core** of a knowledge base matters for compression.  

**Methodology** – The authors define a fixed‑order deletion algorithm that extracts a minimal generating set (the core) from any knowledge base, prove that the zero‑distortion semantic rate equals the entropy of this core (strictly lower than the ordinary entropy when redundancies exist), derive the full semantic rate‑distortion function, and establish a semantic source‑channel separation theorem plus a strengthened Fano inequality that exploit core structure. They also formulate an overlap‑decomposition analysis for multi‑agent broadcast scenarios.  

**Key findings for agentic AI** – Redundant facts become “free” under closure fidelity, yielding a **semantic leverage factor** > 1: the same knowledge can be transmitted with fewer channel uses without violating Shannon capacity. In heterogeneous multi‑agent settings, the core determines a **semantic bottleneck** that limits reliable broadcast even on noiseless channels. Experimental validation on large Datalog datasets confirms the theoretical rate reductions.


<details>
<summary>Abstract</summary>

Shannon's rate-distortion theory treats source symbols as unstructured labels. When the source is a knowledge base equipped with a logical proof system, a natural fidelity criterion is closure fidelity: a reconstruction is acceptable if it preserves the deductive closure of the original. This paper develops a rate-distortion theory under this criterion. Central to the theory is the irredundant core-a canonical generating set extracted by a fixed-order deletion procedure, from which the full deductive closure can be rederived. We prove that the zero-distortion semantic rate equals a quantity that is strictly below the classical entropy rate whenever the knowledge base contains redundant states. More generally, the full semantic rate-distortion function depends only on the core; redundant states are invisible to both rate and distortion. We derive a semantic source-channel separation theorem showing a semantic leverage phenomenon: under closure fidelity, the required source rate is reduced by an asymptotic leverage factor greater than one, allowing the same knowledge base to be communicated with proportionally fewer channel uses-not by violating Shannon capacity, but because redundant states become free. We also prove a strengthened Fano inequality that exploits core structure. For heterogeneous multi-agent communication, an overlap decomposition gives necessary and sufficient conditions for closure-reliable transmission and identifies a semantic bottleneck in broadcast settings that persists even over noiseless channels. All results are verified on Datalog instances with up to 24,000 base facts.

</details>


### 166. CocoaBench: Evaluating Unified Digital Agents in the Wild

- **Authors:** CocoaBench Team, Shibo Hao, Zhining Zhang, Zhiqi Liang, Tianyang Liu, Yuheng Zha, Qiyue Gao, Jixuan Chen, Zilong Wang, Zhoujun Cheng, Haoxiang Zhang, Junli Wang, Hexi Jin, Boyuan Zheng, Kun Zhou, Yu Wang, Feng Yao, Licheng Liu, Yijiang Li, Zhifei Li, Zhengtao Han, Pracha Promthaw, Tommaso Cerruti, Xiaohan Fu, Ziqiao Ma, Jingbo Shang, Lianhui Qin, Julian McAuley, Eric P. Xing, Zhengzhong Liu, Rupesh Kumar Srivastava, Zhiting Hu
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11201v2](http://arxiv.org/abs/2604.11201v2)
- **PDF:** [https://arxiv.org/pdf/2604.11201v2](https://arxiv.org/pdf/2604.11201v2)
- **Categories:** cs.CL, cs.AI


> **Main contribution:** The paper introduces **CocoaBench**, a new benchmark designed to assess “unified” digital agents that must flexibly combine vision, web‑search, and code‑generation tools to solve long‑horizon, real‑world tasks, and it also provides **CocoaAgent**, a lightweight scaffold that standardizes the agent architecture for fair comparison across different LLM backbones.

**Methodology:** Human‑designed tasks are presented only as natural‑language instructions together with an automatic evaluation script that checks the final output, allowing scalable testing of any agent that can invoke vision, search, and coding APIs. The benchmark is run on several existing LLM‑based agents (GPT‑4, Claude, LLaMA‑based models, etc.) using the CocoaAgent scaffold to isolate the effect of the underlying model.

**Key findings:** Even the strongest current system reaches only **45 %** task‑success, revealing a large gap in unified agent competence. Error analysis shows that failures are dominated by deficits in multi‑step reasoning & planning, effective tool use, and visual grounding, highlighting critical research directions for future agentic AI.


<details>
<summary>Abstract</summary>

LLM agents now perform strongly in software engineering, deep research, GUI automation, and various other applications, while recent agent scaffolds and models are increasingly integrating these capabilities into unified systems. Yet, most evaluations still test these capabilities in isolation, which leaves a gap for more diverse use cases that require agents to combine different capabilities. We introduce CocoaBench, a benchmark for unified digital agents built from human-designed, long-horizon tasks that require flexible composition of vision, search, and coding. Tasks are specified only by an instruction and an automatic evaluation function over the final output, enabling reliable and scalable evaluation across diverse agent infrastructures. We also present CocoaAgent, a lightweight shared scaffold for controlled comparison across model backbones. Experiments show that current agents remain far from reliable on CocoaBench, with the best evaluated system achieving only 45.1% success rate. Our analysis further points to substantial room for improvement in reasoning and planning, tool use and execution, and visual grounding.

</details>


### 167. A Simulation-Based Method for Testing Collaborative Learning Scaffolds Using LLM-Based Multi-Agent Systems

- **Authors:** Han Wua, Lishan Zhang, Chunming Lu
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11161v1](http://arxiv.org/abs/2604.11161v1)
- **PDF:** [https://arxiv.org/pdf/2604.11161v1](https://arxiv.org/pdf/2604.11161v1)
- **Categories:** cs.HC, cs.MA


> The paper introduces a simulation framework that uses GPT‑4o–powered multi‑agent systems (one teacher agent plus five student‑role agents) to prototype and evaluate collaborative‑learning scaffolds before classroom implementation. By deploying the MetaGPT platform, the authors compared two scaffolding strategies—“Deep Think before Speak” versus “Direct Speak”—across ten Chinese‑poetry appreciation tasks and analyzed the resulting discourse with metrics grounded in the ICAP learning theory. The results show that the “Deep Think before Speak” scaffold markedly increases discourse diversity, interaction depth, and constructive/interactive behaviours while reducing repetition, thereby validating LLM‑based multi‑agent simulations as a rapid, theory‑consistent testbed for agentic AI research on collaborative learning.


<details>
<summary>Abstract</summary>

Background: Traditional research on collaborative learning scaffolding is often time-consuming and resource-heavy, which hinders the rapid iteration and optimization of instructional strategies. LLM-based multi-agent systems have recently emerged as a powerful tool to simulate complex social interactions and provide a novel paradigm for educational research. Objectives: This study proposes an LLM-based multi-agent simulation approach to investigate collaborative learning processes and the effectiveness of instructional scaffolds prior to actual classroom deployment. The research specifically examines the feasibility of simulating group discussions and the alignment of these simulations with established learning science theories. Methods: The simulation system was implemented using the MetaGPT framework and GPT-4o, comprising one teacher agent and five distinct student roles (Leader, Supporter, Expounder, Rebutter, and Summarizer). Two scaffolding strategies, "Deep Think before Speak" and "Direct Speak", were compared across ten classical Chinese poetry appreciation tasks. Evaluation was conducted through discourse analysis of quality and behavior. Results and Conclusions: The introduction of the "Deep Think before Speak" scaffold significantly improved the agents' discourse diversity and interaction depth while notably reducing content repetitiveness. Behavioral analysis showed that the scaffold encouraged more complex interaction patterns, such as reflecting, rebutting, and explaining. These findings align with the ICAP framework, as the scaffold prompted agents to move from simple "Active" participation to "Constructive" and "Interactive" knowledge co-construction. This study demonstrates the feasibility and ecological validity of using LLM-based multi-agent systems to simulate authentic collaborative learning dynamics.

</details>


### 168. MADQRL: Distributed Quantum Reinforcement Learning Framework for Multi-Agent Environments

- **Authors:** Abhishek Sawaika, Samuel Yen-Chi Chen, Udaya Parampalli, Rajkumar Buyya
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11131v1](http://arxiv.org/abs/2604.11131v1)
- **PDF:** [https://arxiv.org/pdf/2604.11131v1](https://arxiv.org/pdf/2604.11131v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper introduces **MADQRL**, a distributed quantum reinforcement‑learning framework that enables multiple agents to train independently on separate machines while sharing a joint policy, thereby alleviating the prohibitive computational cost of high‑dimensional, multi‑agent environments. By encoding agents’ observations and actions into quantum states and employing distributed quantum circuits for policy evaluation, the authors demonstrate on a cooperative‑Pong benchmark that MADQRL achieves roughly a **10 % gain over existing distributed QRL approaches** and a **5 % improvement compared with classical deep‑RL policy models**. This work shows that distributed quantum processing can meaningfully boost learning efficiency and performance in agentic AI settings, opening a practical pathway for scaling quantum‑enhanced RL to complex multi‑agent domains.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) is one of the most practical ways to learn from real-life use-cases. Motivated from the cognitive methods used by humans makes it a widely acceptable strategy in the field of artificial intelligence. Most of the environments used for RL are often high-dimensional, and traditional RL algorithms becomes computationally expensive and challenging to effectively learn from such systems. Recent advancements in practical demonstration of quantum computing (QC) theories, such as compact encoding, enhanced representation and learning algorithms, random sampling, or the inherent stochastic nature of quantum systems, have opened up new directions to tackle these challenges. Quantum reinforcement learning (QRL) is seeking significant traction over the past few years. However, the current state of quantum hardware is not enough to cater for such high-dimensional environments with complex multi-agent setup. To tackle this issue, we propose a distributed framework for QRL where multiple agents learn independently, distributing the load of joint training from individual machines. Our method works well for environments with disjoint sets of action and observation spaces, but can also be extended to other systems with reasonable approximations. We analyze the proposed method on cooperative-pong environment and our results indicate ~10% improvement from other distribution strategies, and ~5% improvement from classical models of policy representation.

</details>


### 169. ActorMind: Emulating Human Actor Reasoning for Speech Role-Playing

- **Authors:** Xi Chen, Wei Xue, Yike Guo
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11103v1](http://arxiv.org/abs/2604.11103v1)
- **PDF:** [https://arxiv.org/pdf/2604.11103v1](https://arxiv.org/pdf/2604.11103v1)
- **Categories:** cs.SD, cs.AI


> The paper introduces **ActorMind**, a multi‑agent chain‑of‑thought framework that endows speech‑based language models with human‑like actor reasoning for role‑playing. It does so by decomposing the task into four specialized agents—Eye (reads the role description), Ear (extracts emotional cues from the dialogue context), Brain (synthesizes an internal emotional state), and Mouth (produces the spoken response with appropriate vocal traits). Using the newly constructed **ActorMindBench** (7.6 K utterances across 313 scenes and 6 roles), the authors show that this staged reasoning markedly improves the naturalness, emotional consistency, and role fidelity of spoken role‑playing outputs compared with baseline models, establishing a concrete benchmark for speech‑centric agentic AI.


<details>
<summary>Abstract</summary>

Role-playing has garnered rising attention as it provides a strong foundation for human-machine interaction and facilitates sociological research. However, current work is confined to textual modalities, neglecting speech, which plays a predominant role in daily life, thus limiting genuine role-playing. To bridge this gap, we conceptualize and benchmark speech role-playing through ActorMindBench, and we present a corresponding reasoning framework, called ActorMind. Specifically, (1) Speech Role-Playing enables models to deliver spontaneous responses with personalized verbal traits based on their role, the scene, and spoken dialogue. (2) ActorMindBench is a hierarchical benchmark comprises Utterance-Level content with 7,653 utterances, Scene-Level content with 313 scenes, and Role-Level content with 6 roles. (3) ActorMind is an off-the-shelf, multi-agent, chain-of-though style reasoning framework that emulates how human actors perform in theaters. Concretely, ActorMind first reads its assigned role description via Eye Agent, then comprehends emotional cues within contextual spoken dialogues through Ear Agent. Subsequently, Brain Agent generates a descriptive emotional state, and finally, Mouth Agent delivers the scripts infused with corresponding emotion state. Experimental results demonstrate the effectiveness of ActorMind in enhancing speech role-playing.

</details>


### 170. Hodoscope: Unsupervised Monitoring for AI Misbehaviors

- **Authors:** Ziqian Zhong, Shashwat Saxena, Aditi Raghunathan
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11072v1](http://arxiv.org/abs/2604.11072v1)
- **PDF:** [https://arxiv.org/pdf/2604.11072v1](https://arxiv.org/pdf/2604.11072v1)
- **Categories:** cs.AI


> The paper introduces **Hodoscope**, an unsupervised monitoring framework that detects anomalous AI agent behaviors by comparing action distributions across groups of models and benchmarks, rather than relying on pre‑written rules or LLM judges. Using statistical contrast between “well‑behaved” baselines and potentially misbehaving agents, Hodoscope flags distinctive action patterns for human inspection, which led to the discovery of a new Commit0 benchmark loophole and the recovery of known exploits on ImpossibleBench and SWE‑bench while cutting manual review effort by 6–23 ×. The authors further show that the anomalous behavior descriptions harvested by Hodoscope can be fed back to improve supervised LLM‑based judges, bridging unsupervised discovery and supervised verification in agentic AI safety.


<details>
<summary>Abstract</summary>

Existing approaches to monitoring AI agents rely on supervised evaluation: human-written rules or LLM-based judges that check for known failure modes. However, novel misbehaviors may fall outside predefined categories entirely and LLM-based judges can be unreliable. To address this, we formulate unsupervised monitoring, drawing an analogy to unsupervised learning. Rather than checking for specific misbehaviors, an unsupervised monitor assists humans in discovering problematic agent behaviors without prior assumptions about what counts as problematic, leaving that determination to the human.
  We observe that problematic behaviors are often distinctive: a model exploiting a benchmark loophole exhibits actions absent from well-behaved baselines, and a vulnerability unique to one evaluation manifests as behavioral anomalies when the same model runs across multiple benchmarks. This motivates using group-wise behavioral differences as the primary signal for unsupervised monitoring. We introduce Hodoscope, a tool that operationalizes this insight. Hodoscope compares behavior distributions across groups and highlights distinctive and potentially suspicious action patterns for human review. Using Hodoscope, we discover a previously unknown vulnerability in the Commit0 benchmark (unsquashed git history allowing ground-truth recovery, inflating scores for at least five models) and independently recover known exploits on ImpossibleBench and SWE-bench. Quantitative evaluation estimates that our method reduces review effort by 6-23$\times$ compared to naive uniform sampling. Finally, we show that behavior descriptions discovered through Hodoscope could improve the detection accuracy of LLM-based judges, demonstrating a path from unsupervised to supervised monitoring.

</details>


### 171. Federated Single-Agent Robotics: Multi-Robot Coordination Without Intra-Robot Multi-Agent Fragmentation

- **Authors:** Xue Qin, Simin Luan, John See, Cong Yang, Zhijun Li
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.11028v1](http://arxiv.org/abs/2604.11028v1)
- **PDF:** [https://arxiv.org/pdf/2604.11028v1](https://arxiv.org/pdf/2604.11028v1)
- **Categories:** cs.RO, cs.AI


> **Contribution:** The paper introduces **Federated Single‑Agent Robotics (FSAR)**, a runtime architecture that keeps each robot as a single, self‑contained autonomous agent while achieving fleet‑wide coordination through a federated, capability‑based interface rather than by fragmenting the robot’s internal control into multiple agents.

**Methodology:** FSAR defines a formal model for authority delegation, inter‑robot capability requests, and layered recovery, and implements a fleet‑level runtime that provides shared capability registries, contract‑aware task delegation, policy‑aware authority assignment, and scoped trust interactions. The authors compare this federation‑centric design against “decomposition‑heavy” baselines that embed multiple cooperating agents inside each robot, using a suite of multi‑robot coordination tasks (e.g., collaborative transport, area coverage, and fault recovery).

**Key Findings:** Empirical results show that FSAR dramatically improves governance locality (effect size d = 2.91, p < .001) and recovery containment (d = 4.88, p < .001) relative to the baselines, while eliminating authority conflicts and policy violations across all scenarios. The study demonstrates that maintaining a single‑agent runtime per robot and federating at the fleet level yields more robust, scalable, and policy‑compliant coordination—an insight directly relevant to the design of future agentic AI systems operating as embodied robot fleets.


<details>
<summary>Abstract</summary>

As embodied robots move toward fleet-scale operation, multi-robot coordination is becoming a central systems challenge. Existing approaches often treat this as motivation for increasing internal multi-agent decomposition within each robot. We argue for a different principle: multi-robot coordination does not require intra-robot multi-agent fragmentation. Each robot should remain a single embodied agent with its own persistent runtime, local policy scope, capability state, and recovery authority, while coordination emerges through federation across robots at the fleet level. We present Federated Single-Agent Robotics (FSAR), a runtime architecture for multi-robot coordination built on single-agent robot runtimes. Each robot exposes a governed capability surface rather than an internally fragmented agent society. Fleet coordination is achieved through shared capability registries, cross-robot task delegation, policy-aware authority assignment, trust-scoped interaction, and layered recovery protocols. We formalize key coordination relations including authority delegation, inter-robot capability requests, local-versus-fleet recovery boundaries, and hierarchical human supervision, and describe a fleet runtime architecture supporting shared Embodied Capability Module (ECM) discovery, contract-aware cross-robot coordination, and fleet-level governance. We evaluate FSAR on representative multi-robot coordination scenarios against decomposition-heavy baselines. Results show statistically significant gains in governance locality (d=2.91, p<.001 vs. centralized control) and recovery containment (d=4.88, p<.001 vs. decomposition-heavy), while reducing authority conflicts and policy violations across all scenarios. Our results support the view that the path from embodied agents to embodied fleets is better served by federation across coherent robot runtimes than by fragmentation within them.

</details>


### 172. MAFIG: Multi-agent Driven Formal Instruction Generation Framework

- **Authors:** Shixing Zhao, Zheng Si, Pengpeng Ouyang, Zhengqing Hu, Wanqi Zhu, Dong Chen, Yibo Guo, Mingliang Xu
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.10989v1](http://arxiv.org/abs/2604.10989v1)
- **PDF:** [https://arxiv.org/pdf/2604.10989v1](https://arxiv.org/pdf/2604.10989v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **MAFIG**, a multi‑agent framework that autonomously detects and resolves local functional failures in complex scheduling systems by generating formal repair instructions, thereby overcoming the brittleness of rule‑based or reactive rescheduling methods.  

**Methodology:** MAFIG decomposes the emergency‑handling problem into two lightweight agents—a Perception Agent that isolates the failing module and an Emergency Decision Agent that synthesizes a corrective instruction. Decision‑making knowledge is distilled from a powerful cloud‑based LLM into a compact local model via a novel span‑focused loss (SFL) that preserves reasoning over the relevant context while eliminating the latency of full‑scale LLM inference.  

**Key findings:** On three real‑world scheduling benchmarks (port, warehousing, deck), MAFIG achieves near‑perfect emergency‑resolution success rates (≈98 %) with sub‑second response times (0.19‑0.33 s), demonstrating that a distilled multi‑agent approach can deliver LLM‑level adaptability and robustness for agentic AI applications in time‑critical environments.


<details>
<summary>Abstract</summary>

Emergency situations in scheduling systems often trigger local functional failures that undermine system stability and even cause system collapse. Existing methods primarily rely on robust scheduling or reactive scheduling, handling emergencies through predefined rules or rescheduling strategies. However, the diversity and unpredictability of real-world emergencies make them difficult to anticipate, which limits the adaptability of these methods in complex scenarios. Recent studies have shown that Large Language Models (LLMs) possess strong potential for complex scheduling tasks because of their extensive prior knowledge and strong reasoning capabilities. Nevertheless, the high inference latency of LLMs and the lengthy contextual information of scheduling systems significantly hinder their application for emergency handling. To mitigate these issues, we propose the Multi-agent Driven Formal Instruction Generation Framework (MAFIG). The framework constrains the decision scope to local functional modules affected by emergency situations and repairs scheduling logic rapidly by generating formal instructions. MAFIG contains a Perception Agent and an Emergency Decision Agent, which mitigates the adverse impact of lengthy system contexts on emergency decision-making. We further introduce span-focused loss-driven local distillation mechanism (SFL) to transfer the decision-making capability of powerful Cloud Large Language Models (C-LLMs) to lightweight local models, reducing inference latency while preserving decision-making effectiveness. Experiments in the Port, Warehousing, and Deck scheduling datasets show success rates of 98.49\%, 94.97\%, and 97.50\%, with average processing times of 0.33 s, 0.23 s, and 0.19 s. These results demonstrate that MAFIG effectively mitigates the impact of emergencies and improves the robustness and adaptability of scheduling systems.

</details>


### 173. AgentWebBench: Benchmarking Multi-Agent Coordination in Agentic Web

- **Authors:** Shanshan Zhong, Kate Shen, Chenyan Xiong
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.10938v1](http://arxiv.org/abs/2604.10938v1)
- **PDF:** [https://arxiv.org/pdf/2604.10938v1](https://arxiv.org/pdf/2604.10938v1)
- **Categories:** cs.MA


> **Main contribution:** The paper introduces **AgentWebBench**, the first systematic benchmark for evaluating how a “user‑agent” can answer queries by coordinating with **website‑specific content agents** in the emerging “Agentic Web” setting, where information access is decentralized rather than centrally retrieved.

**Methodology:** The authors define four representative web‑information tasks (search, recommendation, open‑ended QA, and deep research) and implement them with three coordination strategies (simple prompting, planner‑mediated interaction, and recursive self‑play) across seven state‑of‑the‑art large language models. Performance is measured against traditional centralized retrieval baselines, and extensive analyses examine traffic concentration, scaling effects, interaction depth, and failure modes.

**Key findings:** Multi‑agent coordination trails centralized retrieval overall, but the gap narrows with larger models and can even surpass centralized baselines on open‑ended question answering. Effective performance requires multiple, well‑planned interactions; scaling test‑time steps improves reliability, while most errors stem from inadequate planning in the user agent and poor evidence retrieval by content agents. The benchmark thus provides a quantitative lens for studying decentralized, agent‑driven web interactions.


<details>
<summary>Abstract</summary>

Agentic Web is an emerging paradigm where autonomous agents help users use online information. As the paradigm develops, content providers are also deploying agents to manage their data and serve it through controlled interfaces. This shift moves information access from centralized retrieval to decentralized coordination. To study this setting, we introduce AgentWebBench, a benchmark that evaluates how well a user agent synthesizes answers by interacting with website-specific content agents. We evaluate four tasks that cover common web information needs, spanning ranked retrieval (web search, web recommendation) and open-ended synthesis (question answering, deep research). Across seven advanced LLMs and three coordination strategies, multi-agent coordination generally lags behind centralized retrieval as expected, because user agent cannot directly access the corpus, but the gap shrinks with model scale and can even outperform centralized retrieval on question answering. This benchmark also enables us to study properties of the emerging paradigm of the digital world. We find that decentralized access concentrates traffic toward a small set of websites, test time scaling improves both interaction reliability and task performance, and strong results require sufficient interactions guided by careful planning. Finally, our failure analysis suggests that user agents need better planning and answer synthesis, while content agents need more reliable retrieval and evidence quality. Code, data, and APIs are released on https://github.com/cxcscmu/AgentWebBench.

</details>


### 174. Mem$^2$Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation

- **Authors:** Zihao Cheng, Zeming Liu, Yingyu Shan, Xinyi Wang, Xiangrong Zhu, Yunpu Ma, Hongru Wang, Yuhang Guo, Wei Lin, Yunhong Wang
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.10923v1](http://arxiv.org/abs/2604.10923v1)
- **PDF:** [https://arxiv.org/pdf/2604.10923v1](https://arxiv.org/pdf/2604.10923v1)
- **Categories:** cs.CL, cs.AI


> **Main contribution:** The paper introduces **Mem²Evolve**, a self‑evolving agent framework that unifies two traditionally separate growth mechanisms—experience accumulation and dynamic asset (tool or expert‑agent) creation—into a *co‑evolutionary* paradigm called Capability Expansion and Experience Distillation.

**Methodology:** Mem²Evolve maintains two complementary memories: (1) an **Experience Memory** that stores past interactions and distilled knowledge, and (2) an **Asset Memory** that records generated tools/agents. The system uses the Experience Memory to bias and guide the generation of new assets, while newly created assets produce fresh experience that is fed back into the Experience Memory, achieving a loop of mutual reinforcement.

**Key findings:** Across six task domains and eight benchmarks, Mem²Evolve outperforms baseline LLMs by **~18.5 %**, exceeds agents that evolve only through experience by **~11.8 %**, and surpasses agents that evolve only via asset creation by **~6.5 %**, demonstrating significantly more effective and stable self‑evolution for agentic AI.


<details>
<summary>Abstract</summary>

While large language model--powered agents can self-evolve by accumulating experience or by dynamically creating new assets (i.e., tools or expert agents), existing frameworks typically treat these two evolutionary processes in isolation. This separation overlooks their intrinsic interdependence: the former is inherently bounded by a manually predefined static toolset, while the latter generates new assets from scratch without experiential guidance, leading to limited capability growth and unstable evolution. To address this limitation, we introduce a novel paradigm of co-evolutionary Capability Expansion and Experience Distillation. Guided by this paradigm, we propose the \textbf{Mem$^{\textbf{2}}$Evolve}, which integrates two core components: \textbf{Experience Memory} and \textbf{Asset Memory}. Specifically, Mem$^{2}$Evolve leverages accumulated experience to guide the dynamic creation of assets, thereby expanding the agent's capability space while simultaneously acquiring new experience to achieve co-evolution. Extensive experiments across 6 task categories and 8 benchmarks demonstrate that Mem$^{2}$Evolve achieves improvement of 18.53\% over standard LLMs, 11.80\% over agents evolving solely through experience, and 6.46\% over those evolving solely through asset creation, establishing it as a substantially more effective and stable self-evolving agent framework. Code is available at: https://buaa-irip-llm.github.io/Mem2Evolve.

</details>


### 175. HTAA: Enhancing LLM Planning via Hybrid Toolset Agentization & Adaptation

- **Authors:** Chengrui Huang, Junshuo Zhang, Zhiyuan Ma, Xikun Wang, Ximeng Wang, Menghua Jiang, Gang Zeng, Zhaobing Han, Shen Gao, Shuo Shang
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.10917v1](http://arxiv.org/abs/2604.10917v1)
- **PDF:** [https://arxiv.org/pdf/2604.10917v1](https://arxiv.org/pdf/2604.10917v1)
- **Categories:** cs.CL


> The paper introduces **Hybrid Toolset Agentization & Adaptation (HTAA)**, a hierarchical planning framework that bundles frequently co‑used tools into “agent tools” to shrink the LLM’s action space and curb redundant calls. The authors train the high‑level planner with an **Asymmetric Planner Adaptation** regime that reconstructs tool trajectories backward and refines them forward, aligning planner decisions with the specialized agent tools. Across a large‑scale internal POI‑validation dataset (InfoVerify) and standard benchmarks, HTAA achieves higher success rates, shorter tool‑calling sequences, and lower context overhead than strong baselines, and its deployment in a ride‑hailing platform demonstrably cuts manual verification effort and operational costs.


<details>
<summary>Abstract</summary>

Enabling large language models to scale and reliably use hundreds of tools is critical for real-world applications, yet challenging due to the inefficiency and error accumulation inherent in flat tool-calling architectures. To address this, we propose Hybrid Toolset Agentization & Adaptation (HTAA), a hierarchical framework for scalable tool-use planning. We propose a novel toolset agentization paradigm, which encapsulates frequently co-used tools into specialized agent tools, thereby reducing the planner's action space and mitigating redundancy. To ensure effective coordination, we design Asymmetric Planner Adaptation, a trajectory-based training paradigm that aligns the high-level planner with agent tools via backward reconstruction and forward refinement. To validate the performance of HTAA, we conduct experiments on a real-world internal dataset, InfoVerify, based on the POI validation workflow of China's largest online large-scale ride-hailing platform, featuring long-horizon executable tool trajectories. Experiments on InfoVerify and widely-used benchmarks show that HTAA consistently achieves higher task success rates, requires short tool calling trajectories, and significantly reduces context overhead compared to strong baselines. Furthermore, in a production deployment, HTAA substantially reduces manual validation effort and operational cost, demonstrating its practical efficacy.

</details>


### 176. EvoNash-MARL: A Closed-Loop Multi-Agent Reinforcement Learning Framework for Medium-Horizon Equity Allocation

- **Authors:** Chongliu Jia, Yi Luo, Sipeng Han, Pengwei Li, Jie Ding, Youshuang Hu, Yimiao Qian, Qiya Wang
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.10911v2](http://arxiv.org/abs/2604.10911v2)
- **PDF:** [https://arxiv.org/pdf/2604.10911v2](https://arxiv.org/pdf/2604.10911v2)
- **Categories:** cs.AI, cs.LG


> **Main contribution** – The paper introduces **EvoNash‑MARL**, a closed‑loop multi‑agent reinforcement‑learning system that couples population‑based policy evolution, game‑theoretic (Nash‑type) aggregation, and execution‑aware validation to tackle the brittleness of medium‑ to long‑horizon equity allocation under non‑stationary market regimes and realistic trading constraints.  

**Methodology** – A walk‑forward experimental design (120 sequential windows) is used to evolve several RL agents in parallel, evaluate them with constraint‑aware back‑testing, and select a mixed‑policy portfolio via a Nash equilibrium‑style aggregation that explicitly accounts for the interaction among agents and market frictions.  

**Key findings** – On out‑of‑sample data (2014‑2024) the EvoNash‑MARL configuration achieves a **19.6 % annualized return** versus **11.7 % for SPY**, with stable performance through 2026, outperforming internal baselines in a “robust‑score” metric. Statistical tests (White’s Reality Check, SPA‑lite) do not confirm global significance, indicating that the framework improves robustness rather than providing conclusive evidence of superior market timing.


<details>
<summary>Abstract</summary>

Medium- to long-horizon equity allocation is challenging due to weak predictive structure, non-stationary market regimes, and the degradation of signals under realistic trading constraints. Conventional approaches often rely on single predictors or loosely coupled pipelines, which limit robustness under distributional shift. This paper proposes EvoNash-MARL, a closed-loop framework that integrates reinforcement learning with population-based policy optimization and execution-aware selection to improve robustness in medium- to long-horizon allocation. The framework combines multi-agent policy populations, game-theoretic aggregation, and constraint-aware validation within a unified walk-forward design. Under a 120-window walk-forward protocol, the final configuration achieves the highest robust score among internal baselines. On out-of-sample data from 2014 to 2024, it delivers a 19.6% annualized return, compared to 11.7% for SPY, and remains stable under extended evaluation through 2026. While the framework demonstrates consistent performance under realistic constraints and across market settings, strong global statistical significance is not established under White's Reality Check (WRC) and SPA-lite tests. The results therefore provide evidence of improved robustness rather than definitive proof of superior market timing performance.

</details>


### 177. OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation

- **Authors:** Xiaomeng Hu, Yinger Zhang, Fei Huang, Jianhong Tu, Yang Su, Lianghao Deng, Yuxuan Liu, Yantao Liu, Dayiheng Liu, Tsung-Yi Ho
- **Published:** 2026-04-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2604.10866v2](http://arxiv.org/abs/2604.10866v2)
- **PDF:** [https://arxiv.org/pdf/2604.10866v2](https://arxiv.org/pdf/2604.10866v2)
- **Categories:** cs.CL


> OccuBench introduces a large‑scale benchmark that evaluates AI agents on 100 real‑world professional tasks spanning 10 industry sectors by using Language Environment Simulators (LESs) to generate domain‑specific tool responses from LLMs. The authors automatically synthesize solvable, difficulty‑calibrated instances and test agents on both task completion and robustness to three fault types (explicit errors, implicit data degradation, and mixed faults), benchmarking 15 state‑of‑the‑art models across eight families. Results show that no single model dominates across occupations, implicit faults are the most challenging, and performance scales with model size, newer generations, and higher reasoning effort—while the fidelity of the LES itself proves essential for reliable evaluation.


<details>
<summary>Abstract</summary>

AI agents are expected to perform professional work across hundreds of occupational domains (from emergency department triage to nuclear reactor safety monitoring to customs import processing), yet existing benchmarks can only evaluate agents in the few domains where public environments exist. We introduce OccuBench, a benchmark covering 100 real-world professional task scenarios across 10 industry categories and 65 specialized domains, enabled by Language Environment Simulators (LESs) that simulate domain-specific environments through LLM-driven tool response generation. Our multi-agent synthesis pipeline automatically produces evaluation instances with guaranteed solvability, calibrated difficulty, and document-grounded diversity. OccuBench evaluates agents along two complementary dimensions: task completion across professional domains and environmental robustness under controlled fault injection (explicit errors, implicit data degradation, and mixed faults). We evaluate 15 frontier models across 8 model families and find that: (1) no single model dominates all industries, as each has a distinct occupational capability profile; (2) implicit faults (truncated data, missing fields) are harder than both explicit errors (timeouts, 500s) and mixed faults, because they lack overt error signals and require the agent to independently detect data degradation; (3) larger models, newer generations, and higher reasoning effort consistently improve performance. GPT-5.2 improves by 27.5 points from minimal to maximum reasoning effort; and (4) strong agents are not necessarily strong environment simulators. Simulator quality is critical for LES-based evaluation reliability. OccuBench provides the first systematic cross-industry evaluation of AI agents on professional occupational tasks.

</details>



## Biorxiv (2 papers)


### 1. HARVEST: Unlocking the Dark Bioactivity Data of Pharmaceutical Patents via Agentic AI

- **Authors:** Shepard, V., Musin, A., Chebykina, K., Zeninskaya, N. A., Mistryukova, L., Avchaciov, K., Fedichev, P. O.
- **Published:** 2026-04-17
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.03.15.711910](https://doi.org/10.64898/2026.03.15.711910)

- **Categories:** bioinformatics


> The paper introduces **HARVEST**, an autonomous multi‑agent pipeline built on large language models that scans the USPTO patent corpus, parses the dense SAR tables inside, and converts them into a searchable, structured bioactivity database at a cost of only $0.11 per patent. By processing 164,877 patents in under a week, HARVEST extracted 3.15 M protein‑ligand activity records, adding 326 k novel chemical scaffolds and 967 previously undocumented protein targets to public knowledge and achieving ~80 % concordance with the human‑curated BindingDB set. Using this newly mined data, the authors create **H‑Bench**, a held‑out benchmark that reveals a two‑dimensional generalization gap in current open‑source models (e.g., Boltz‑2), which perform poorly on both unseen scaffolds and unseen protein targets—highlighting the need for richer, agent‑derived training data in agentic AI for drug discovery.


<details>
<summary>Abstract</summary>

Pharmaceutical patents contain vast Structure-Activity Relationship tables documenting protein-ligand binding data. While technically public, this information remains computationally inaccessible and effectively dark, trapped in bulky documents that no existing database has systematically captured. We present HARVEST, a multi-agent large language model pipeline that autonomously extracts structured bioactivity records from USPTO patent archives at $0.11 per document. Applied to 164,877 patents, HARVEST produced 3.15 million activity records, recovering 326,342 unique scaffolds and 967 protein targets absent from BindingDB. This pipeline completed in under a week a task that would otherwise require over 55 years of continuous expert labor. Automated extraction achieves 80% agreement with human curated corpus of US patents from BindingDB, a conservative lower bound given identified errors within the reference data. We further introduce H-Bench, a structurally guaranteed held-out benchmark built from this recovered data. Evaluation of the leading open-source model Boltz-2 on H-Bench reveals a two-dimensional generalization gap: performance degrades both on novel scaffolds and on uncharacterized protein targets, exposing fundamental limitations of models trained on existing public repositories.

</details>


### 2. Reaching for domain-general syntax: Sentence processing and tool-use reach-to-grasp share neural patterns in the basal ganglia

- **Authors:** Thibault, S., Py, R., Koun, E., Salemme, R., BOULENGER, V., Roy, A. C., Brozzoli, C. d.
- **Published:** 2026-04-15
- **Source:** biorxiv
- **URL:** [https://doi.org/10.1101/2025.10.17.683107](https://doi.org/10.1101/2025.10.17.683107)

- **Categories:** neuroscience


> **Main contribution:** The paper provides neural evidence that hierarchical processing in language (syntactic embedding) and in tool‑mediated actions (reach‑to‑grasp) rely on the same computational substrate in the basal ganglia, supporting the view that the brain uses a domain‑general mechanism for structuring sequences across cognition and action.

**Methodology:** Forty French speakers performed a sentence‑comprehension task (object‑ vs. subject‑relative clauses) and a motor task (grasping objects either with a tool or with the bare hand) while undergoing fMRI. Univariate activation maps and multivariate pattern‑analysis (MVPA) were used to identify brain regions where the neural code for syntactically complex sentences overlapped with that for the reach‑to‑grasp phase of tool use.

**Key findings:** Both tasks recruited overlapping activity patterns specifically in the basal ganglia, and MVPA showed that the neural signatures for processing syntactically complex sentences were indistinguishable from those for the reach‑to‑grasp phase of tool use. This phase‑specific convergence suggests that the basal ganglia serve as a hub for domain‑general hierarchical computations, linking language syntax and tool‑based action planning—an insight directly relevant to agentic AI models that aim to integrate language and motor control through shared hierarchical mechanisms.


<details>
<summary>Abstract</summary>

Are actions organized like sentences? Recent evidence showed reciprocal transfer between tool use and syntactic comprehension, reflecting shared basal ganglia resources for action and language. The proposed mechanism is that embedding a tool into the motor plan increases the hierarchical structure of actions, paralleling the organization of sentences. If so, overlap with linguistic computations should emerge specifically during the initiation and/or reach-to-grasp phase, when tool embedding dynamically updates the relation with the target, rather than when the object is stably held in the tool grip. Forty French native speakers completed a sentence comprehension task involving object- and subject-relative clauses, and a motor task consisting of grasping and manipulating an object either with a tool or with the bare hand. Using both univariate and multivariate analyses, we found that the comprehension of syntactically complex sentences and the reach-to-grasp phase of tool use elicited overlapping and similar neural codes within the basal ganglia. This phase-specific convergence identifies the basal ganglia as a hub for domain-general hierarchical computations, unifying syntactic embedding for language and tool use.

</details>



## Medrxiv (5 papers)


### 1. Democratizing Scientific Publishing: A Local, Multi-Agent LLM Framework for Objective Manuscript Editing

- **Authors:** Bhansali, R., Gorenshtein, A., Westover, B., Goldenholz, D. M.
- **Published:** 2026-04-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.13.26350761](https://doi.org/10.64898/2026.04.13.26350761)

- **Categories:** health informatics


> The paper presents **Paper Analysis Tool (PAT)**, a free, locally‑run, multi‑agent framework that uses 31 small‑language‑model agents to perform comprehensive, confidential manuscript audits across methodological, statistical, visual, and linguistic dimensions. By running PAT on three published clinical‑neurology papers, the system generated 540 suggestions; expert reviewers validated 391 of them as actionable (≈90 % agreement) and measured a 72.4 % overall usefulness accuracy, while deterministic re‑evaluation of 126 rewrite pairs showed substantial textual improvements (‑25 % word count, passive voice ↓ from 35 % to 5 %, sentence length ↓ 24 %, long‑sentence fraction ↓ 67 %, Flesch‑Kincaid grade ↑ 17 %). These results demonstrate that a locally hosted, agentic LLM pipeline can reliably automate pre‑submission manuscript editing while preserving data confidentiality, offering a transparent, scalable alternative to cloud‑based AI writing tools in scientific publishing.


<details>
<summary>Abstract</summary>

Manuscript preparation is a critical bottleneck in scientific publishing, yet existing AI writing tools require cloud transmission of sensitive content, creating data-confidentiality barriers for clinical researchers. We introduce the Paper Analysis Tool (PAT), a free, multi-agent framework that deploys 31 specialized agents powered by small language models (SLMs) to audit manuscripts across multiple quality dimensions without external data transmission. Applied to three published clinical neurological papers, PAT generated 540 evaluable suggestions. Validation by two expert reviewers (R.B., A.G.) confirmed 391 actionable, high-value revisions (90% agreement), achieving a 72.4% overall usefulness accuracy spanning methodological, statistical, and visual domains. Furthermore, deterministic re-evaluation of 126 agent-suggested rewrite pairs using Phase 0 metrics confirmed text improvement: total word count decreased by 25%, passive voice prevalence dropped sharply from 35% to 5%, average sentence length decreased by 24%, long-sentence fraction fell by 67%, and the Flesch-Kincaid grade improved by 17% . Our validation confirms that systematic, agent-driven pre-submission review drives measurable improvements, successfully converting manuscript optimization from an opaque, manual endeavor into a transparent and rigorous scientific process.

Manuscript preparation is a critical bottleneck in scientific publishing, yet existing AI writing tools require cloud transmission of sensitive content, creating data-confidentiality barriers for clinical researchers. We introduce the Paper Analysis Tool (PAT), a free, multi-agent framework that deploys 31 specialized agents powered by small language models (SLMs) to audit manuscripts across multiple quality dimensions without external data transmission. Applied to three published clinical neurological papers, PAT generated 540 evaluable suggestions. Independent validation by two expert reviewers (R.B., A.G.) confirmed 391 actionable, high-value revisions (90% agreement), achieving a 72.4% overall usefulness accuracy spanning methodological, statistical, and visual domains. Furthermore, deterministic re-evaluation of 126 suggested Phase 0 rewrite pairs confirmed text improvement: total word count decreased by 25%, passive voice prevalence dropped sharply from 35% to 5%, average sentence length decreased by 24%, and long-sentence fraction fell by 67%, and the Flesch-Kincaid grade improved modestly. Our validation confirms that systematic, agent-driven pre-submission review drives measurable improvements, successfully converting manuscript optimization from an opaque, manual endeavor into a transparent and rigorous scientific process.

</details>


### 2. LIFETIME JEM-DERIVED OCCUPATIONAL EXPOSURE BURDEN AND ODDS OF PARKINSONS DISEASE AND PARKINSONISM IN A MATCHED CASE-CONTROL STUDY

- **Authors:** Lewis, F., Renzetti, S., Goulett, N., Azmoun, S., Sundar, V., Ali, M., Pitta, L., Shoieb, D., Caci, M., Borghesi, S., Covolo, L., Oppini, M., Gelatti, U., Padovani, A., Pilotto, A., Pepe, F., Turla, M., Crippa, P., Boffetta, P., Pani, L., Vermeulen, R., Kromhout, H., Lambertini, L., Colicino, E., Placidi, D., Lucchini, R.
- **Published:** 2026-04-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.03.16.26348171](https://doi.org/10.64898/2026.03.16.26348171)

- **Categories:** occupational and environmental health


> The paper demonstrates that cumulative occupational exposure—particularly to pesticides and metals—significantly raises the odds of Parkinson’s disease and Parkinsonism, independent of known genetic (SNCA rs356219) and familial risk factors. Using a hospital‑based matched case‑control design (334 cases / 334 controls) the authors linked lifetime job histories to the ALOHA+ job‑exposure matrix and applied conditional logistic regression and a weighted‑quantile‑sum (WQS) mixture model to quantify single‑agent and multi‑agent exposure burdens. Both analytical approaches identified high lifetime pesticide exposure (OR≈3.5 for PD) and a composite exposure index dominated by pesticides (weight ≈ 0.43) and metals (weight ≈ 0.21) as the strongest occupational contributors to disease risk, underscoring preventable workplace hazards for neurodegeneration.


<details>
<summary>Abstract</summary>

Background/ObjectivesOccupational exposure to neurotoxicants such as pesticides, metals, and solvents has long been implicated in Parkinsons disease (PD) and Parkinsonism, yet the cumulative impact of multiple occupational exposure families over the working life remains insufficiently characterized. This study evaluated whether long-term cumulative occupational exposures, derived from the ALOHA+ Job-Exposure Matrix (ALOHA+-JEM), were associated with PD and Parkinsonism.

MethodsA hospital-based matched case-control study was conducted in the province of Brescia, Italy, including 668 participants (334 PD/Parkinsonism cases and 334 matched controls). Cases and controls were 1:1 matched based on sex, age, and lifetime occupational duration. Lifetime occupational histories were coded using ISCO-08 and harmonized to ISCO-88 for linkage with ALOHA+-JEM. Conditional logistic regression estimated associations between cumulative exposures (none/low/high) and disease status, adjusting for smoking, parental history of PD/tremor, and SNCA rs356219 genotype. Multi-agent occupational exposure burden indexes were evaluated using positively constrained repeated-holdout Weighted Quantile Sum (WQS) regression (100 bootstraps, 100 holdouts)

ResultsIn conditional logistic regression, parental history of PD or tremor (OR = 4.55, 95% CI: 2.44-8.48; q < 0.001) and the SNCA rs356219 CC genotype (OR = 2.17, 95% CI: 1.33-3.52; q = 0.013) were significantly associated with disease. High cumulative all pesticide exposure showed positive associations with combined PD + Parkinsonism (OR = 2.98, 95% CI: 1.23-7.25) and PD alone (OR = 3.56, 95% CI: 1.25-10.15). In WQS analyses, the composite occupational exposure burden index was positively associated with disease (combined PD + Parkinsonism: OR = 1.15, 95% CI: 1.00-1.30). All pesticides received the highest mean weight in all models (w = 0.434 for combined PD + Parkinsonism), followed by metals (w = 0.210), identifying them as contributing most strongly to the composite exposure index.

ConclusionsLong-term cumulative occupational exposures were associated with increased odds of PD and Parkinsonism. All pesticides and metals were most strongly associated with PD and Parkinsonism, consistent with established neurotoxic mechanisms attributable to occupational environments. These findings underscore the importance of occupational exposure prevention and risk-reduction strategies in occupational settings and highlight workplace exposures as preventable contributors to Parkinsonian disorders.

</details>


### 3. A Conversational Artificial Intelligence Framework for Comparative Pathway-Level Profiling of Sezary Syndrome and Primary Cutaneous CD8+ Aggressive Epidermotropic Cytotoxic T-Cell Lymphoma (PCAECTCL)

- **Authors:** Diaz, F. C., Waldrup, B., Carranza, F. G., Manjarrez, S., Velazquez-Villarreal, E.
- **Published:** 2026-04-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.15.26350992](https://doi.org/10.64898/2026.04.15.26350992)

- **Categories:** oncology


> The paper introduces **AI‑HOPE**, a conversational AI framework that lets researchers iteratively query and refine public cancer genomics datasets, and applies it to a comparative pathway‑level analysis of Sezary syndrome (SS) versus primary cutaneous CD8⁺ aggressive epidermotropic cytotoxic T‑cell lymphoma (PCAECTCL). Using curated somatic‑mutation data from the Columbia CTCL cohort, the authors map high‑confidence coding variants to signaling pathways, compare mutation frequencies (Chi‑square/Fisher), tumor mutational burden (Wilcoxon) and co‑mutation networks, and discover that—despite similar TMB—SS is enriched for epigenetic, tumor‑suppressor, NFAT and DNA‑damage‑response pathways, while PCAECTCL shows relatively higher MAPK and epigenetic regulator alterations, with ERBB2 mutations distinguishing the subtypes. These results not only generate subtype‑specific therapeutic hypotheses (e.g., ERBB2 targeting) but also demonstrate how conversational AI can accelerate hypothesis‑driven, pathway‑centric genomics research in agentic AI‑enabled precision oncology.


<details>
<summary>Abstract</summary>

Background: Sezary syndrome (SS) is an aggressive leukemic variant of cutaneous T-cell lymphoma (CTCL) with distinct clinical and biological features compared to rarer entities such as primary cutaneous CD8+ aggressive epidermotropic cytotoxic T-cell lymphoma (PCAECTCL). Although recurrent genomic alterations in CTCL have been described, comparative analyses at the pathway level across biologically divergent subtypes remain limited. Here, we leveraged a conversational artificial intelligence (AI) platform for precision oncology to enable rapid, integrative, and hypothesis-driven interrogation of publicly available genomic datasets. Methods: We conducted a secondary analysis of somatic mutation and clinical data from the Columbia University CTCL cohort accessed via cBioPortal. Cases were stratified into SS (n=26) and PCAECTCL (n=13). High-confidence coding variants were curated and mapped to biologically relevant signaling pathways and functional gene categories implicated in CTCL pathogenesis. Pathway-level mutation frequencies were compared using Chi-square or Fisher's exact tests, with effect sizes quantified as odds ratios. Tumor mutational burden (TMB) was compared using the Wilcoxon rank-sum test. Subtype-specific co-mutation patterns were evaluated using pairwise association analyses and visualized through oncoplots and network heatmaps. Conversational AI agents, AI-HOPE, were used to iteratively refine cohort definitions, prioritize pathway-level signals, and contextualize findings. Results: TMB was comparable between SS and PCAECTCL (p = 0.96), indicating no significant difference in global mutational load. In contrast, pathway-centric analyses revealed marked qualitative differences. SS demonstrated enrichment of alterations in epigenetic regulators, tumor suppressor and cell-cycle control pathways, NFAT signaling, and DNA damage response mechanisms, consistent with transcriptional dysregulation and immune modulation. PCAECTCL exhibited relatively higher frequencies of alterations involving epigenetic regulators and MAPK pathway signaling, suggesting distinct oncogenic dependencies. Co-mutation analysis revealed a more constrained and focused interaction landscape in SS, whereas PCAECTCL displayed broader and more heterogeneous co-mutation networks, indicative of divergent evolutionary trajectories. Notably, ERBB2 mutations were significantly enriched between subtypes (p = 0.031), highlighting a potential subtype-specific therapeutic vulnerability. Conclusions: This study demonstrates that SS is distinguished from PCAECTCL not by increased mutational burden but by distinct pathway-level architectures, particularly involving epigenetic regulation, immune signaling, and transcriptional control. These findings generate biologically grounded, testable hypotheses for subtype-specific therapeutic targeting and underscore the value of conversational AI as a scalable framework for accelerating discovery in translational cancer genomics.

</details>


### 4. Pre-Dementia Indicators and Multidomain Vulnerabilities: Insights from AD8 Screening in Older Chinese Speaking Adults

- **Authors:** You, W., Koo, F. K., Cheng, Y., Huang, J., Huang, H., Li, M., Sevastidis, J., Chang, H.-C.
- **Published:** 2026-04-13
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.08.26350424](https://doi.org/10.64898/2026.04.08.26350424)

- **Categories:** geriatric medicine


> The paper demonstrates that the AD8 dementia‑screening interview can serve as a multidimensional risk‑stratification tool for community‑dwelling Chinese‑speaking elders, identifying three latent domains (memory impairment, executive‑interest decline, and functional recall difficulty) that predict physical (e.g., mobility, financial management), psychological (e.g., depression, hopelessness, worthlessness) and social vulnerabilities. Using exploratory factor analysis on 144 participants and binary logistic regression, the authors show that specific AD8 items—particularly judgment problems, repetition errors, financial and tool‑use difficulties, and daily memory lapses—are strong early indicators of functional decline and emotional distress, whereas intact temporal recall is protective. These findings suggest that brief, culturally adapted AD8 screening can be integrated into nursing and community assessments to flag pre‑dementia multidomain frailties and guide timely, person‑centred interventions in diverse ageing populations.


<details>
<summary>Abstract</summary>

BackgroundEarly recognition of dementia-related changes is critical for timely intervention. The AD8 Dementia Screening Interview (AD8) detects subtle cognitive and functional changes, yet its broader associations with health and wellbeing among Chinese-speaking older adults remain underexplored.

MethodsA cross-sectional study was conducted with 144 community-dwelling Chinese older adults (mean age 73.1 years; 81.3% female). Participants completed sociodemographic, health, functional, and psychosocial measures, including the AD8 and the Geriatric Depression Scale (GDS-15). Exploratory Factor Analysis (EFA) assessed the dimensionality of the AD8, and binary logistic regression examined associations between AD8 items and demographic, health, functional, and psychosocial outcomes.

ResultsChronic disease was prevalent (68.1 percent), and 13.2 percent reported a mental health disorder. EFA identified three domains: memory impairment, executive and interest decline, and functional recall difficulties, explaining 61.7 percent of the variance. Logistic regression showed predictive roles for judgment problems (AD8_1), repetition (AD8_3), financial difficulties (AD8_6), tool-use difficulties (AD8_4), and daily memory problems (AD8_8). Financial and executive difficulties were associated with age and mobility challenges, while repetition predicted psychological disorders and hopelessness. Judgment problems were linked to lower life satisfaction and happiness but greater helplessness. Worthlessness was predicted by financial, tool-use, and memory difficulties, whereas intact temporal recall (AD8_5) was protective. Several outcomes including boredom, low energy, and staying home were not significant.

ConclusionDistinct AD8 items predicted vulnerabilities across physical, psychological, and social domains. Findings highlight the multidimensional value of the AD8 as a culturally relevant screening and risk stratification tool for community-based assessments of Chinese older adults.

Summary Statement Implications for PracticeO_ST_ABSWhat does this research add to existing knowledge in gerontology?C_ST_ABSThis study shows that specific AD8 items identify early multidimensional vulnerability among community-dwelling Chinese-speaking older adults. Difficulties with judgment, repetition, financial management, tool use, and daily memory were associated with functional limitations and psychosocial distress, extending the AD8 beyond dementia screening alone. The identification of three AD8 domains supports a broader understanding of early cognitive change as involving cognitive, functional, and emotional processes. The findings contribute culturally specific evidence from an under-researched population in gerontological research.

What are the implications of this new knowledge for nursing care with older people?For nursing practice, the AD8 provides a brief, feasible tool to support holistic assessment in community and aged care settings. Key AD8 indicators can guide nurses in identifying older people at risk of functional decline and emotional vulnerability, enabling earlier, person-centred interventions. The findings highlight the importance of culturally and linguistically appropriate assessment when caring for diverse ageing populations.

How could the findings be used to influence policy or practice or research or education?The results support integrating brief cognitive screening into routine nursing assessments and community-based aged care services to promote early identification and ageing in place. Nursing education should emphasise interpreting cognitive screening within psychosocial and cultural contexts. Longitudinal research is needed to assess intervention effectiveness.

Key Points[tpltrtarr] Early cognitive changes matter for older Chinese-speaking adults, because difficulties with judgment, repetition, financial management, and tool use (AD8 domains) were consistently linked to poorer functional and psychosocial outcomes.
[tpltrtarr]Beyond dementia screening, the AD8 proved useful for detecting vulnerabilities in wellbeing and daily functioning, extending its role beyond diagnostic sensitivity.
[tpltrtarr]A cultural focus is vital, as this study is among the first to examine AD8 associations in older Chinese-speaking adults, underscoring the need for culturally tailored screening.
[tpltrtarr]The psychosocial impact of cognitive changes was evident, with strong associations to helplessness, worthlessness, and reduced life satisfaction, reinforcing the overlap between cognitive and emotional health.
[tpltrtarr]In practice, integrating AD8 screening into community and primary care could help identify at-risk individuals early and support targeted interventions in culturally and linguistically diverse populations.

</details>


### 5. HAARF: Healthcare AI Agents Regulatory Framework - A Comprehensive Security Verification Standard for Autonomous AI Systems in Clinical Environments

- **Authors:** Schwoebel, J., Frasch, M., Spalding, A., Sewell, E., Englert, P., Halpert, B., Overbay, C., Semenec, I., Shor, J.
- **Published:** 2026-04-13
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.09.26350519](https://doi.org/10.64898/2026.04.09.26350519)

- **Categories:** health systems and quality improvement


> The paper introduces **HAARF**, a unified regulatory and verification framework that lets health systems safely deploy fully autonomous AI agents for clinical decision‑making and tool use. By distilling nine existing medical‑AI regulations into eight verification categories (279 concrete requirements) and defining three risk‑based compliance levels, HAARF provides a model‑agnostic middleware that enforces progressive autonomy, tool‑access controls, bias monitoring, and decision traceability. Red‑team tests on Gemini 2.5 Flash (cross‑validated with Claude Sonnet 4.6) show that HAARF‑guardrails eliminate unauthorized tool execution (0 % success vs. ~58 % in baseline) and achieve >90 % alignment with major regulators, cutting multi‑jurisdictional compliance effort by 40‑60 % while improving patient‑safety governance.


<details>
<summary>Abstract</summary>

As health systems begin deploying autonomous AI agents that make independent clinical decisions and take direct actions within care workflows, ensuring patient safety and care quality requires governance standards that go beyond existing medical device frameworks designed for human-in-the-loop prediction tools. This paper introduces the Healthcare AI Agents Regulatory Framework (HAARF), a comprehensive verification standard for autonomous AI systems in clinical environments, developed collaboratively with 40+ international experts spanning regulatory authorities, clinical organizations, and AI security specialists.

HAARF synthesizes requirements from nine major regulatory frameworks (FDA, EU AI Act, Health Canada, UK MHRA, NIST AI RMF, WHO GI-AI4H, ISO/IEC 42001, OWASP AISVS, IMDRF GMLP) into eight core verification categories comprising 279 specific requirements across three risk-based implementation levels. The framework addresses critical gaps in health system readiness for autonomous AI including: (1) progressive autonomy governance with clinical accountability, (2) tool-use security for agents that independently access EHRs, medical devices, and clinical systems, (3) continuous equity monitoring and bias mitigation across diverse patient populations, and (4) clinical decision traceability preserving human oversight authority.

We validate HAARFs enforcement capabilities through a scenario-based red-team evaluation comprising six adversarial scenarios executed under baseline (no middleware) and HAARF- guardrailed conditions (N = 50 trials each, Gemini 2.5 Flash primary with Claude Sonnet 4.6 cross-model validation). In baseline conditions, the agent model executes unauthorized tools in 56-60% of adversarial trials. Under the HAARF condition, deterministic middleware enforcement reduces the unauthorized-tool success rate to 0%, with 0% contraindication misses and 0% policy-injection success (95% Wilson CI [0.00, 0.07]). Cross-model validation confirms identical security metrics, supporting HAARFs model-agnostic design. Mapping analysis demonstrates 48-88% coverage of major regulatory frameworks, with per-category FDA alignment ranging from 73% (C5, Agent Registration) to 91% (C3, Cybersecurity; C7, Bias & Equity). Initial validation with healthcare organizations shows a 40-60% reduction in multi-jurisdictional compliance burden and improved clinical safety governance outcomes.

HAARF provides health systems with a practical, risk-stratified pathway for safe AI agent deployment--shifting from reactive compliance to proactive quality governance while maintaining rigorous patient safety standards and human-centered care principles.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*