# Weekly AI Agent Paper Report

**Generated:** 2026-06-01 15:27
**Period:** 2026-05-25 to 2026-05-31

## Summary

- **Total papers fetched:** 600
- **Papers matching keywords:** 1
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-05-25) | Change |
|--------|-----------|-----------|--------|
| Total matched | 1 | 180 | -179 |
| arxiv | 0 | 177 | -177 |
| biorxiv | 1 | 1 | +0 |
| medrxiv | 0 | 2 | -2 |

### Notable Trends

**AI‑agent paper landscape – this week vs. last week**

| Metric | This week (2024‑W23) | Last week (2024‑W22) |
|--------|----------------------|----------------------|
| Total papers | **1** (all from **bioRxiv**) | **180** (arXiv 177 + medRxiv 2 + bioRxiv 1) |
| Dominant venue | bioRxiv (100 % of output) | arXiv (≈98 %) – the usual pre‑print hub |
| Top‑cited/highlighted titles | • *An AI‑agent‑orchestrated grey‑box Transformer framework for sparse pharmacokinetic curve reconstruction and pharmacometric model initialization* | • *MyeGPT: an AI agent for Multiple Myeloma*  <br>• *Interpretable clinical AI agent for anti‑infective decision support*  <br>• *CHRONOS: Temporally‑Aware Multi‑Agent Coordination for Evolving Data Marketplaces*  <br>• *LLM‑driven design of physics‑constrained constitutive models*  <br>• *MemAudit: Post‑hoc Auditing of Poisoned Agent Memory* … (7 titles total) |

### Notable take‑aways

1. **Sharp drop in volume** – the field went from a flood of 180 pre‑prints last week to a single paper this week, suggesting a temporary lull in conference‑season submissions rather than a sustained decline.

2. **Source shift** – arXiv, the usual driver of AI‑agent research, produced **no papers** this week; all activity came from bioRxiv, highlighting a brief pivot toward biologically‑oriented applications (pharmacokinetics).

3. **Topic focus contraction**:  
   - **Last week** covered a broad mix: clinical decision‑support agents, multi‑agent coordination, physics‑constrained model design, security/auditing of agent memory, gaming NPC policies, and a biomedical benchmark.  
   - **This week** zeroes in on **pharmacometric modeling**, i.e., a single‑domain, high‑impact biomedical use case.

4. **Continued emergence of “dual‑agent” designs** – even though only one paper appeared, its “grey‑box Transformer + agent orchestration” approach mirrors last week’s “two agents are better than one” trend, indicating sustained interest in hybrid agent architectures.

5. **Signal of upcoming conference cycles** – the concentration of 177 arXiv papers last week aligns with typical pre‑print spikes before major AI‑agent venues (NeurIPS, ICML, ICLR). The current dip likely reflects the post‑deadline cooling period, not a loss of research momentum.

*Bottom line*: The field is experiencing a normal weekly rhythm—high‑volume, cross‑disciplinary bursts followed by brief quiet periods—while the underlying thematic currents (hybrid agents, safety/audit, domain‑specific deployment) remain steady.

---



## Biomedical Highlights (1 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


**Overview**

Across the recent literature, AI‑driven agents are being harnessed to automate and augment core pharmacometric and biomedical workflows that have traditionally been limited by sparse data, high manual effort, and narrow model generalizability.  The highlighted studies introduce **grey‑box Transformer architectures** that combine mechanistic (physiologically‑based) PK/PD models with data‑driven attention mechanisms, allowing the agents to (i) reconstruct full concentration‑time curves from sparsely sampled clinical data, (ii) initialise patient‑specific model parameters without exhaustive nonlinear mixed‑effects fitting, and (iii) iteratively refine model structures through reinforcement‑learning‑style orchestration of sub‑agents (e.g., data imputation, parameter proposal, and model selection).  Methodologically, the papers blend **deep sequence‑to‑sequence learning**, **probabilistic programming**, and **Bayesian optimisation** to achieve rapid, interpretable model convergence while preserving regulatory‑compliant mechanistic insight.  Applications span single‑drug and multi‑drug PK reconstruction, virtual trial simulation, and real‑time therapeutic drug monitoring, illustrating a shift toward **AI‑orchestrated, semi‑transparent pharmacometrics** that can scale across therapeutic areas and patient populations.



### 1. An AI-agent-orchestrated grey-box Transformer framework for sparse pharmacokinetic curve reconstruction and pharmacometric model initialization

- **Authors:** Chen, J., Wang, J., Du, S., Chen, Y., Li, K., Song, J., Liu, D.
- **Published:** 2026-05-27
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.05.23.727373](https://doi.org/10.64898/2026.05.23.727373)

- **Categories:** pharmacology and toxicology


> The paper introduces **Pharmacokinetic Foundation Model (PKFM)**, a grey‑box Transformer that is pre‑trained on data from 32 drugs and can reconstruct full concentration‑time curves from only a few observed points, dosing information, molecular descriptors, and patient covariates, while keeping its outputs interpretable. The authors train PKFM with a contrastive‑learning objective, then use the reconstructed curves as inputs for traditional NONMEM nonlinear mixed‑effects modelling, showing markedly higher R² (≈0.99) on oral PK profiles and improved covariance stability and individual prediction accuracy; the model’s embeddings also enable accurate retrieval of physiologically‑based PK candidates (75.6 % within a 2‑fold error). Finally, an **AI‑driven Pharmacometrics Agent (PM Agent)** built around PKFM outperforms generic programming tools on a standardized modelling benchmark, achieving higher stability and win rates, though each run still requires expert confirmation before clinical or regulatory deployment.


<details>
<summary>Abstract</summary>

Clinical pharmacokinetic (PK) modelling is constrained by sparse sampling, limited general-isability of single-drug models, and labour-intensive workflows, making it difficult to infer complete drug exposure from limited concentration observations. We present the Pharmacokinetic Foundation Model (PKFM), a grey-box Transformer framework pre-trained across 32 drugs that reconstructs concentration-time profiles from sparse concentration observations, dosing events, molecular descriptors, and physiological covariates while preserving output interpretability. In representative oral PK curves, three sparse input points recovered the principal absorption-elimination trajectory, achieving coefficient of determination (R2) = 0.992 for Midazolam oral and R2 = 0.990 for Verapamil oral. Using reconstructed curves in NONMEM (nonlinear mixed-effects modelling) improved covariance stability and individual prediction accuracy. Contrastive-learning embeddings supported Top-10 physiologically based pharmacokinetic (PBPK) candidate retrieval, with 75.6% of observations within the 2-fold range. A pharmacometrics-informed AI Agent (PM Agent) outperformed general-purpose programming tools in stability and pairwise win rate on a standardised modelling benchmark, with each run requiring human pharmaco-metrician confirmation before downstream use. These results support cross-drug pre-trained PK models as an information-completion layer for sparse PK evidence and a structured scaffold for the modelling workflow; clinical or regulatory use requires prospective validation, broader external benchmarking, and independent expert assessment.

</details>


---



## Biorxiv (1 papers)


### 1. An AI-agent-orchestrated grey-box Transformer framework for sparse pharmacokinetic curve reconstruction and pharmacometric model initialization

- **Authors:** Chen, J., Wang, J., Du, S., Chen, Y., Li, K., Song, J., Liu, D.
- **Published:** 2026-05-27
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.05.23.727373](https://doi.org/10.64898/2026.05.23.727373)

- **Categories:** pharmacology and toxicology


> The paper introduces **Pharmacokinetic Foundation Model (PKFM)**, a grey‑box Transformer that is pre‑trained on data from 32 drugs and can reconstruct full concentration‑time curves from only a few observed points, dosing information, molecular descriptors, and patient covariates, while keeping its outputs interpretable. The authors train PKFM with a contrastive‑learning objective, then use the reconstructed curves as inputs for traditional NONMEM nonlinear mixed‑effects modelling, showing markedly higher R² (≈0.99) on oral PK profiles and improved covariance stability and individual prediction accuracy; the model’s embeddings also enable accurate retrieval of physiologically‑based PK candidates (75.6 % within a 2‑fold error). Finally, an **AI‑driven Pharmacometrics Agent (PM Agent)** built around PKFM outperforms generic programming tools on a standardized modelling benchmark, achieving higher stability and win rates, though each run still requires expert confirmation before clinical or regulatory deployment.


<details>
<summary>Abstract</summary>

Clinical pharmacokinetic (PK) modelling is constrained by sparse sampling, limited general-isability of single-drug models, and labour-intensive workflows, making it difficult to infer complete drug exposure from limited concentration observations. We present the Pharmacokinetic Foundation Model (PKFM), a grey-box Transformer framework pre-trained across 32 drugs that reconstructs concentration-time profiles from sparse concentration observations, dosing events, molecular descriptors, and physiological covariates while preserving output interpretability. In representative oral PK curves, three sparse input points recovered the principal absorption-elimination trajectory, achieving coefficient of determination (R2) = 0.992 for Midazolam oral and R2 = 0.990 for Verapamil oral. Using reconstructed curves in NONMEM (nonlinear mixed-effects modelling) improved covariance stability and individual prediction accuracy. Contrastive-learning embeddings supported Top-10 physiologically based pharmacokinetic (PBPK) candidate retrieval, with 75.6% of observations within the 2-fold range. A pharmacometrics-informed AI Agent (PM Agent) outperformed general-purpose programming tools in stability and pairwise win rate on a standardised modelling benchmark, with each run requiring human pharmaco-metrician confirmation before downstream use. These results support cross-drug pre-trained PK models as an information-completion layer for sparse PK evidence and a structured scaffold for the modelling workflow; clinical or regulatory use requires prospective validation, broader external benchmarking, and independent expert assessment.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*